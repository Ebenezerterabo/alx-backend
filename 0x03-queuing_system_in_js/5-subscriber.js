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


/* Subscribe to 'holberton school channel' */
client.subscribe('holberton school channel');

/* Listen for messages */
client.on('message', (channel, message) => {
    console.log(message);

    /* Stop listening for messages */
    if (message === 'KILL_SERVER') {
        client.unsubscribe('holberton school channel');
        client.quit();
    }
});