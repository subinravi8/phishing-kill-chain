<<<<<<< HEAD
# 🎣 End-to-End Phishing Kill Chain Simulator
<p align="center">
  <img src="https://github.com/user-attachments/assets/a11be579-ad10-448f-8664-0a522ec1644b"
       alt="End-to-End Phishing Kill Chain"
       width="400">
</p>

A complete Red Team simulation demonstrating the entire attack lifecycle—from reconnaissance to credential harvesting and lateral movement.

## 📋 Overview
This project simulates a sophisticated phishing operation in a controlled lab environment. It showcases:
- OSINT Reconnaissance (email gathering)
- Phishing Infrastructure (Gophish, SMTP, DNS)
- Social Engineering (HTML email templates)
- Credential Harvesting (Fake login pages)
- Post-Exploitation (SSH lateral movement)

## 🛠️ Tools Used
- **Gophish** – Phishing campaign management
- **Python (Paramiko)** – SSH automation for lateral movement
- **Gmail SMTP** – Email delivery relay
- **Ubuntu Server** – Hosting environment
- **Windows/Kali** – Victim and attacker simulation

## Diagram 
<img width="1536" height="1024" alt="d3ad187c-76a8-4ef5-b4d7-5db88baf105f" src="https://github.com/user-attachments/assets/e087f50b-0c54-4dba-b700-3f1f58d5d91b" />

ost_exploit.png             # Successful SSH lateral movement output
```

## 🚀 How to Run (Lab Setup)
1. Clone this repo.
2. Install Gophish and configure the `config.json` to listen on `0.0.0.0`.
3. Update your `hosts` file to point `mysecurelab.com` to your server IP.
4. Launch Gophish and create a campaign using the provided templates.
5. Run `python3 scripts/lateral_movement.py` to simulate post-exploitation.

## ⚠️ Disclaimer
This project is for **educational purposes only**. Unauthorized use against real targets is illegal. Always obtain explicit written permission before testing.

## 📊 Results
- Successfully harvested credentials via a cloned login page.
- Used stolen credentials to SSH into a target server.
- Simulated data exfiltration.

## 📄 Full Report
See [docs/report.md](docs/report.md) for the detailed attack narrative and defensive recommendations.
=======
