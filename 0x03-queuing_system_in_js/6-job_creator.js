import redis from 'redis';
import kue from 'kue';

const queue = kue.createQueue();
const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

const jobData = {
  phoneNumber: '01063440605',
  message: 'This is the code to verify your account',
};

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', () => console.log('Notification job completed'));

job.on('falied', () => console.log('Notification job failed'));
