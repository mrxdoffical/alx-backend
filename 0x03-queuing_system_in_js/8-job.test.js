const express = require('express');
const app = express();
const redis = require('redis');
const client = redis.createClient();

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const product = listProducts.find((product) => product.itemId === parseInt(itemId, 10));
  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await client.getAsync(`item.${itemId}`);
  const currentQuantity = product.initialAvailableQuantity - parseInt(reservedStock, 10);
  res.json({
    itemId: product.itemId,
    itemName: product.itemName,
    price: product.price,
    initialAvailableQuantity: product.initialAvailableQuantity,
    currentQuantity,
  });
});

const reserveStockById = async (itemId, stock) => {
  await client.setAsync(`item.${itemId}`, stock);
};

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const product = listProducts.find((product) => product.itemId === parseInt(itemId, 10));
  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await client.getAsync(`item.${itemId}`);
  const currentQuantity = product.initialAvailableQuantity - parseInt(reservedStock, 10);
  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: product.itemId });
  }

  await reserveStockById(itemId, reservedStock + 1);
  res.json({ status: 'Reservation confirmed', itemId: product.itemId });
});

app.listen(1245, () => {
  console.log('Server listening on port 1245');
});
