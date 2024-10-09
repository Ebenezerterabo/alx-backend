import { createClient } from 'redis';
import { promisify } from 'util';

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

async function displaySchoolValue(schoolName) {
    const getAsync = promisify(client.get).bind(client);
    const reply = await getAsync(schoolName);
    console.log(reply);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');