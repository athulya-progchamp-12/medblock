import firebase from "firebase/app";
import "firebase/auth";

const app = firebase.initializeApp({
    apiKey: "AIzaSyCMca_IJRhJxZCaK8OSezfq79p_s7RkoxM",
    authDomain: "med-block-e33c9.firebaseapp.com",
    projectId: "med-block-e33c9",
    storageBucket: "med-block-e33c9.appspot.com",
    messagingSenderId: "974141592492",
    appId: "1:974141592492:web:859b2f15e320516a19a009",
    measurementId: "G-6PD76DXELY"
});

export const auth = app.auth();
export default app;


