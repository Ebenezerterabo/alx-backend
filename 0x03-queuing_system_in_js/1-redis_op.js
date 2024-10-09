import { redis } from 'kue';
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

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, () => {
        console.log('Reply: OK');
    });
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        console.log(reply);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');