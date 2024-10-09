import kue from 'kue';

// Create a new job queue
const queue = kue.createQueue();

// Create a job and add it to the queue
const jobData = {
    phoneNumber: '4153518780',
    message: 'This is your message notification!'
};

// Create a job in the push notification queue
const job = queue.create('push_notification_code', jobData)
    .save(err => {
        if (!err) {
            console.log(`Notification job created: ${job.id}`);
        }
});

// Handle job completion and failure
job.on('complete', () => {
    console.log('Notification job completed');
}).on('failed', () => {
    console.log('Notification job failed');
});