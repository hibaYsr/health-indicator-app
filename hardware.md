# Hardware Setup Guide
This document describes the hardware components wiring, and installation for the RFID-Based Room Access Control System.


## 1. Overview

The hardware layer is responsible for physical access control. It reads RFID cards, processes the data with an Arduino microcontroller, and controls door locking mechanisms. Feedback is provided via LEDs, buzzer, and optionally an LCD display.

## 2. Hardware Components

- **RFID Reader (RC522)** — Reads the unique ID from RFID cards.

- **Arduino Board (Uno / Mega / ESP8266)** — Processes card IDs, checks schedules, and controls the relay.

- **Relay Module** — Activates the door locking mechanism.

- **LED Indicators** — Provide visual feedback (Green = Access Granted, Red = Access Denied).

- **Buzzer** — Provides audio feedback for access events.

- **LCD Display (optional)** — Displays messages like “Access Granted” or “Access Denied”.

- **Power Supply** — Provides stable 3.3V/5V power to Arduino and peripherals.

- **Connecting Wires** — Jumper wires for SPI and GPIO connections.

## 3. Wiring Diagram

### 3.1 RFID Reader → Arduino

| RFID Pin | Arduino Pin |
|----------|------------|
| SDA      | 10         |
| SCK      | 13         |
| MOSI     | 11         |
| MISO     | 12         |
| GND      | GND        |
| RST      | 9          |
| 3.3V     | 3.3V       |

### 3.2 Relay Module → Arduino

| Relay Pin | Arduino Pin |
|-----------|------------|
| IN        | 7          |
| VCC       | 5V         |
| GND       | GND        |

### 3.3 LED Indicators → Arduino

| LED Color | Arduino Pin |
|-----------|------------|
| Green     | 5          |
| Red       | 6          |

### 3.4 Buzzer → Arduino

| Pin    | Arduino Pin |
|--------|------------|
| Signal | 8          |
| GND    | GND        |

## 4. Physical Installation

1. Mount the RFID reader at door height (chest level).

2. Install the relay module near the door lock.

3. Connect LEDs and buzzer to the corresponding Arduino GPIO pins.

4. Secure the Arduino and wiring inside a protective enclosure.

5. Connect a stable power supply to the Arduino and peripherals.

6. Optionally, install an LCD display for real-time access messages.

7. Test the system thoroughly before deployment.

## 5. Hardware Testing

- Verify the Arduino detects the RFID card ID via serial monitor.

- Test LED and buzzer feedback for access granted and denied scenarios.

- Confirm relay activation correctly unlocks the door for authorized users.

- If using a Wi-Fi enabled Arduino (ESP8266/ESP32), check Firebase connectivity for logging.

## 6. Safety Considerations

- Ensure all wiring is insulated and secured.

- Use low-voltage DC supplies only.

- Avoid exposing electronics to moisture, heat, or physical stress.

- Confirm the relay module can safely handle the door lock current.

## 7. Optional Enhancements

- Add backup power supply for operation during outages.

- Include tamper detection switches on the door or relay.

- Integrate additional sensors (motion, door open/close) for monitoring.

- Use LCD display to show friendly access messages.