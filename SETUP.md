# TechnoCore Setup Guide

Complete setup guide for getting TechnoCore running locally and in production.

## Local Development (5 minutes)

### Step 1: Clone Repository
```bash
git clone https://github.com/jdariko45/technocore.git
cd technocore
```

### Step 2: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Generate Your DID
```bash
python3 << EOF
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
import hashlib

private_key = ed25519.Ed25519PrivateKey.generate()
public_bytes = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw
)
fingerprint = hashlib.sha256(public_bytes).hexdigest()[:16]
did = f'did:key:z6Mk{fingerprint}'

print(f'Your DID: {did}')

with open('identity.pem', 'wb') as f:
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    f.write(pem)
EOF
```

### Step 5: Run Example Agent
```bash
python3 examples/simple_agent.py
```

## Production Deployment (VPS)

### Prerequisites
- VPS (DigitalOcean, AWS, Tencent Cloud, etc.)
- SSH access
- Ubuntu 20.04+

### Setup
```bash
# SSH to VPS
ssh ubuntu@[YOUR_VPS_IP]

# Clone repo
git clone --depth 1 https://github.com/jdariko45/technocore.git
cd technocore

# Setup
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run in screen
screen -S agents
python3 examples/simple_agent.py
# Ctrl+A then D to detach
```

## Troubleshooting

### Agent Won''t Start
```bash
python3 --version  # Should be 3.10+
which python       # Should show venv path
pip list           # Should show packages
```

### SSH Connection Failed
```bash
ping [VPS_IP]
ssh -v ubuntu@[VPS_IP]
```

---

For detailed guide, see full [SETUP.md](SETUP.md) in repository.
