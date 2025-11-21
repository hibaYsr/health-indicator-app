# System Architecture

This document describes the overall architecture of the **RFID-Based Room Access Control System**, explaining how the hardware, firmware, and software components interact.

---

## 1. Overview

The system is divided into two layers:
1. **Hardware Layer** – Handles physical access control using RFID and Arduino.
2. **Software Layer** – Manages data, user roles, and real-time room monitoring via Flutter and Firebase.

---

## 2. Hardware Architecture

### Components
- **RFID Reader (RC522)** — Captures the RFID card UID.
- **Arduino Microcontroller** — Processes UID, checks schedule, and triggers the relay.
- **Relay Module** — Controls door lock mechanism.
- **LED Indicators and Buzzer** — Provide status feedback.
- **LCD Display (optional)** — Displays messages like “Access Granted”.

### Communication Flow
1. RFID reader scans card → sends UID to Arduino.
2. Arduino validates time and ID.
3. If valid → activates relay and updates Firebase.

---

## 3. Software Architecture

### Flutter App (Manager Dashboard)
- Built with **Flutter Desktop**.
- Displays real-time room statuses using data streams from Firebase.
- Provides CRUD access to users and rooms.
- Authentication handled by Firebase Authentication.

### Firebase Backend
- **Firestore Database** stores:
  - Rooms and their statuses
  - Users and schedules
  - Access logs
- **Firebase Authentication** secures access for managers only.
- **Cloud Functions (optional)** can automate access expiration or alerts.

---

## 4. Data Flow Diagram

```mermaid
flowchart LR
    A[Teacher (RFID Card)] --> B[RFID Reader]
    B --> C[Access Controller]
    C --> D{Check Schedule in Database}
    D -->|Valid Time Slot| E[Grant Access to Classroom]
    D -->|Invalid Time Slot| F[Deny Access]
    E --> G[Log Entry in CheckIn Database]
    F --> H[Log Access Denied Attempt]
```


