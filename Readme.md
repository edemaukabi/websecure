# WebSecure 🔐

**WebSecure** is a Django-based web application I built to demonstrate robust web security implementations. It is designed to enhance the security of our Django apps using modern security strategies and best practices.

---

## 🔧 Features

### ✅ reCAPTCHA Integration
Blocks bots from submitting login or registration forms by verifying human interaction with Google reCAPTCHA.

### ✅ Two-Factor Authentication (2FA)
Implements Time-based One-Time Password (TOTP) using virtual authenticator apps like Google Authenticator or Authy.

### ✅ Failed Login Attempt Tracking
Limits brute-force attempts by monitoring and restricting repeated failed login attempts using Django’s built-in tools and django-otp.

### ✅ Session Timeout
Ensures automatic user logout after a defined period of inactivity, reducing the risk of session hijacking.

### ✅ Password Management
- Strong password validation.
- Secure password reset and change workflows.
- Uses Django's secure password hashing algorithm.

### ✅ Hardened Security Settings
Configures key Django settings for a secure deployment environment:
- `SECURE_SSL_REDIRECT`
- `SESSION_COOKIE_SECURE`
- `CSRF_COOKIE_SECURE`
- `SECURE_HSTS_SECONDS`
- `X_FRAME_OPTIONS`, etc.

### ✅ Additional Measures
- Content Security Policy (CSP)
- Clickjacking protection
- Email verification
- HTTPS enforcement
- Admin hardening

---

## 📦 Dependencies

All dependencies are listed in `requirements.txt`:

```txt
asgiref==3.8.1
colorama==0.4.6
crispy-bootstrap5==2024.10
Django==5.1.5
django-crispy-forms==2.3
django-formtools==2.5.1
django-otp==1.5.4
django-phonenumber-field==8.0.0
django-recaptcha==4.0.0
django-two-factor-auth==1.17.0
phonenumbers==8.13.54
pypng==0.20220715.0
qrcode==7.4.2
sqlparse==0.5.3
typing_extensions==4.12.2
tzdata==2025.1
```

---

## 💻 Local Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/edemaukabi/websecure.git
cd websecure
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install the Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key
DEBUG=True
RECAPTCHA_PUBLIC_KEY=your-recaptcha-site-key
RECAPTCHA_PRIVATE_KEY=your-recaptcha-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost
```


### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser
```bash
python manage.py createsuperuser
```

### 7. Start the Development Server
```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Project Structure (Simplified)

```
websecure/
├── .gitignore
├── README.md
├── manage.py
├── requirements.txt
├── appsecure/
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   ├── templatetags/
│   └── static/
├── static/
└── websecure/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

```
