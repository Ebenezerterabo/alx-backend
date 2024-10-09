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



/* Create an object of hash data */
const data = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 5,
    'Cali': 40,
    'Paris': 2
};

/* Store data in redis hash */
for (const [key, value] of Object.entries(data)) {
    client.hset('HolbertonSchools', key, value, () => {
        console.log('Reply: 1');
    });
}

/* Retrieve data from redis hash */
client.hgetall('HolbertonSchools', (err, value) => {
    console.log(value);
})