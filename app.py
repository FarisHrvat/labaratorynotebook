import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCiIonF87F8yOS0YmPeXl3ZdNYQrVPvDR0",
  authDomain: "labaratorynotebook.firebaseapp.com",
  projectId: "labaratorynotebook",
  storageBucket: "labaratorynotebook.appspot.com",
  messagingSenderId: "917925815807",
  appId: "1:917925815807:web:e6f599480e7f5385a773ca",
  measurementId: "G-HE3GF7LJ85"
};

def add_entry(date, experiment, results, observations):
    ref = db.reference('entries')
    entry = {
        "date": date,
        "experiment": experiment,
        "results": results,
        "observations": observations
    }
    ref.push(entry)

def view_entries():
    ref = db.reference('entries')
    entries = ref.get()
    return entries
