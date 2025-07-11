# 🔐 Secure Data Encryption System

This is a Streamlit-based web application that allows users to securely **store** and **retrieve** sensitive data using **encryption** and a **passkey-based authentication system**.

---

## 💡 Features

- **Encrypt & Store Data** securely using the Fernet symmetric encryption algorithm.
- **Decrypt Data** with passkey verification using salted hashing (PBKDF2 with SHA-256).
- **Brute-force protection** with lockout after 3 failed attempts.
- **Admin Reauthorization** to unlock the system after repeated failed access.
- Uses **session state** to track login attempts securely within a session.
- Data is saved locally in a `data.json` file.

---

## 🚀 How It Works

### 📝 Store Data

1. Enter the sensitive data you want to secure.
2. Provide a passkey (password).
3. The app encrypts the data using Fernet, and hashes the passkey using a salt.
4. You receive an encrypted string — **copy and save this**; you'll need it later to retrieve your data.

### 🔍 Retrieve Data

1. Paste the encrypted string into the input field.
2. Enter the same passkey used during encryption.
3. If both match, the app decrypts and shows your original data.
4. After 3 incorrect attempts, access is **blocked until reauthorization**.

### 🔑 Reauthorization

- Use the **Master Password** (`admin123` by default) in the "Login" section.
- This resets the failed attempts and allows you to try again.

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Encryption:** `cryptography.fernet`
- **Hashing:** `hashlib.pbkdf2_hmac` with salt
- **Storage:** Local JSON file (`data.json`)

---

## 🔐 Security Considerations

- **Passkeys are never stored** — only their salted hashes are saved.
- A **new random salt** is generated for each encryption operation.
- The app prevents brute-force attempts by **blocking access** after 3 failed tries.
- Even if someone accesses `data.json`, they **cannot decrypt without the correct passkey**.
