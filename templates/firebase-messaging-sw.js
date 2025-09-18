// Import the Firebase messaging library (only available inside a service worker)
importScripts('https://www.gstatic.com/firebasejs/10.3.1/firebase-messaging.js');

// Initialize Firebase in the service worker
firebase.initializeApp({
    apiKey: "AIzaSyDmPjonCWaeVbGjJOhJqL7khTT_qCe1OkU",
    authDomain: "green-grow-45.firebaseapp.com",
    projectId: "green-grow-45",
    storageBucket: "green-grow-45.firebasestorage.app",
    messagingSenderId: "941319547900",
    appId: "1:941319547900:web:6a76f3249652f2bf1c2079",
    measurementId: "G-ZLZ02F0608"
});

// Set up messaging instance
const messaging = firebase.messaging();

// Handle background notifications
messaging.onBackgroundMessage(function(payload) {
    console.log("Received background message: ", payload);

    // Customize the notification content
    const notificationTitle = payload.notification.title;
    const notificationOptions = {
        body: payload.notification.body,
        icon: payload.notification.icon || '/default-icon.png',
        badge: '/badge.png',  // Optional: custom badge for the app icon
    };

    // Show the notification
    self.registration.showNotification(notificationTitle, notificationOptions);
});
