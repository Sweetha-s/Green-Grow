const admin = require('firebase-admin');
const path = require('path');

// Provide the path to the service account key file
const serviceAccount = path.resolve(`D:/3rdSem/DesignThinking/GreenGrow/green-grow-2394d-firebase-adminsdk-1oj3t-1c5d215d7c.json`);
// Initialize Firebase Admin SDK with the service account key
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
});

const message = {
  notification: {
    title: 'Low Humidity Alert',
    body: 'The humidity level is below the threshold. Please water your plants.',
  },
  token: 'de5IlAGb1qYdyvuBoqI0Ef:APA91bGr5T4sp96UTyv1KAIviB6cb983lZBAZjJETi-mtQWgr_ssLLreot3Hk_x-YCckTuuFBgX--su3p4RYZdcuTinFAjqKqLniyY0k3z-YCyEEqq56FSY',  // Use the FCM token from the client
};

admin.messaging().send(message)
  .then((response) => {
    console.log('Successfully sent message:', response);
  })
  .catch((error) => {
    console.log('Error sending message:', error);
  });