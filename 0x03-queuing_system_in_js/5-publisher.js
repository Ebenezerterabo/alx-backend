import { createClient } from 'redis';

/* Create a client */
const client = createClient();

/* Connect to the server */
client.on('connect', () => {
    console.log('Redis client connected to the server');
});
/* Handle errors */
client.on('error', (err) => {
    console.log('Redis client not connected to the server: ', err);
});


function publishMessage(message, time) {
    client.publish('holberton school channel', message, (err, reply) => {
        console.log(`About to send ${message}`);
    });
    setTimeout(() => {
        client.disconnect();
    }, time * 1000);
}


publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);