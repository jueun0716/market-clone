import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";
import { getStorage } from "firebase/storage";
import { getAuth } from "firebase/auth";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  //소셜 로그인, 데이터베이스 연동 , 깃허브에 연동하면 안된다.
  apiKey: "AIzaSyCJSwDY8czF0Gn3KLts1DtgrZAMLEg25uM",
  authDomain: "carrot-market-87879.firebaseapp.com",
  databaseURL:
    "https://carrot-market-87879-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "carrot-market-87879",
  storageBucket: "carrot-market-87879.appspot.com",
  messagingSenderId: "1076860648039",
  appId: "1:1076860648039:web:993890341fb5a40a3472c2",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Realtime Database and get a reference to the service
const database = getDatabase(app);
const storage = getStorage(app);
const auth = getAuth(app);
