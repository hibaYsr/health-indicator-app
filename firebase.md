# Firebase Setup Guide

This document explains how to configure Firebase for the **RFID-Based Room Access Control System** and describes the database structure, authentication, and real-time integration with the Flutter dashboard.

---

## 1. Overview

Firebase handles the **backend services** for this system:

- **Firestore Database / Realtime Database** – Stores users, room info, schedules, and access logs.  
- **Firebase Authentication** – Secures the manager dashboard.  
- **Cloud Functions (optional)** – Automates actions like access expiration or alerts.  

The Flutter desktop app listens to database streams for **real-time updates** on room status and access events.

---

## 2. Firebase Project Setup

1. Create a new project in the [Firebase Console](https://console.firebase.google.com/).  
2. Enable **Authentication**:
   - Choose **Email/Password** method for manager login.  
3. Enable **Cloud Firestore** or **Realtime Database**:  
   - Cloud Firestore is recommended for structured data and real-time streams.  
4. For Flutter integration:  
   - Use **FlutterFire CLI**:  
     ```bash
     flutterfire configure
     ```
   - This generates `lib/firebase_options.dart` with your Firebase config.  

---

## 3. Database Structure

### 3.1 Rooms Collection

```text
/rooms
   /room_A
      status: "available"        // "available" | "occupied" | "maintenance"
      current_user: null
      last_access: timestamp
      capacity: 50

### 3.2 Users Collection

/users
   /prof_1234
      name: "Dr. A. Smith"
      email: "a.smith@university.edu"
      rfid_id: "E3F29A4B"
      department: "Computer Science"
      schedule: {
         monday: ["09:00-11:00", "14:00-16:00"],
         wednesday: ["13:00-15:00"],
         friday: ["10:00-12:00"]
      }

### 3.3 Access Logs Collection

/access_logs
   /log_001
      user_id: "prof_1234"
      user_name: "Dr. A. Smith"
      room_id: "room_A"
      timestamp: "2025-11-06T09:05:00Z"
      status: "granted"           // "granted" | "denied"
      reason: "scheduled_access"

---

## 4. Authentication

- Only manager accounts can log in to the Flutter dashboard.

- Use Firebase Authentication with Email/Password.

- Implement role-based rules in Firestore:

rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /rooms/{room} {
      allow read: if request.auth != null;
      allow write: if request.auth.token.role == 'manager';
    }
    match /users/{user} {
      allow read: if request.auth != null;
      allow write: if request.auth.token.role == 'manager';
    }
    match /access_logs/{log} {
      allow read: if request.auth != null;
      allow write: if request.auth.token.role == 'manager';
    }
  }
}

---

## 5. Real-Time Updates

- Flutter app listens to database streams:

FirebaseFirestore.instance
  .collection('rooms')
  .snapshots()
  .listen((snapshot) {
    // Update room status in UI in real-time
  });


- Access logs can be streamed similarly for live monitoring.

---

## 6. Optional Features

- Cloud Functions can automate access expiration, alerts, or notifications.

- Security Rules can be extended to handle maintenance or cleaning staff access.

- Offline persistence can be enabled in Firestore for Flutter:

- FirebaseFirestore.instance.settings = const Settings(persistenceEnabled: true);

## 7. Testing & Verification

- Test manager login with Firebase Authentication.

- Verify Firestore writes/reads when a card is scanned.

- Confirm real-time UI updates in Flutter dashboard when room status changes.

- Test access denial and log creation for invalid access attempts.