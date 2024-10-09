import kue from 'kue';

// Create a new job queue
const queue = kue.createQueue();

// Create sendNotification function
function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Writing a que process
queue.process('push_notification_code', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
});