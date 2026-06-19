# End-to-End Phishing Kill Chain – Red Team Simulation Report

**Author:** Subin R 
**Project Repository:** [Link to your GitHub repo]  

---

## 1. Executive Summary
This report documents a complete end-to-end phishing simulation conducted in a controlled lab environment. The attack lifecycle—from OSINT reconnaissance to credential harvesting and lateral movement—was successfully executed. This exercise demonstrates critical security gaps that organizations face and provides actionable defensive recommendations.

---

## 2. Attack Lifecycle Walkthrough

### Phase 1: Reconnaissance (OSINT)
**Objective:** Gather potential target email addresses.
**Method:** Simulated using a dummy employee list (`employees.csv`). In a real-world scenario, attackers use tools like `theHarvester` or Hunter.io to scrape public data.
**Outcome:** 4 dummy target emails were identified and imported into Gophish.

### Phase 2: Infrastructure Setup
**Objective:** Create a convincing phishing environment.
**Method:** 
- Configured local DNS (`hosts` file) to resolve `mysecurelab.com` to the Ubuntu server.
- Deployed **Gophish** (open-source phishing framework).
- Created a Gmail SMTP relay for sending emails.

### Phase 3: Campaign Execution
**Objective:** Deliver the phishing lure.
**Method:** An urgent "Password Expiration Alert" email was crafted using Gophish's HTML template engine. The email included a malicious link pointing to the fake login page.
**Statistics:**
- Emails Sent: 4
- Emails Opened: 2
- Links Clicked: 2
- Credentials Submitted: 2 (Test credentials entered)

### Phase 4: Credential Harvesting
**Objective:** Capture victim credentials.
**Method:** A cloned login page (mimicking Office 365) was hosted via Gophish. Upon form submission, credentials were logged in the Gophish database.
**Captured Data:** 
- Username: `victim_user`
- Password: `victim`

### Phase 5: Post-Exploitation (Lateral Movement)
**Objective:** Demonstrate how stolen credentials compromise internal systems.
**Method:** A Python script using `paramiko` automated an SSH login attempt against a local server using the captured credentials.
**Result:** Successful authentication. The script executed reconnaissance commands (`whoami`, `hostname`, `ls`) and created a mock exfiltrated file (`stolen_data.txt`).
**Terminal Output:**
    =====================================
    POST-EXPLOITATION KILL CHAIN PHASE
    =====================================
    
[*] Attempting lateral movement to 127.0.0.1:22 with victim_user...
[+] SUCCESS! Logged in as victim_user on 127.0.0.1

[*] Executing reconnaissance commands...
[+] Current User: victim_user
[+] Hostname: subin-virtual-machine

[+] Directory listing of /home/victim_user/:
total 32
drwxr-x--- 5 victim_user victim_user 4096 Jun 19 23:25 .
drwxr-xr-x 7 root        root        4096 Jun 19 23:09 ..
-rw-r--r-- 1 victim_user victim_user  220 Jan  6  2022 .bash_logout
-rw-r--r-- 1 victim_user victim_user 3771 Jan  6  2022 .bashrc
drwx------ 2 victim_user victim_user 4096 Jun 19 23:25 .cache
drwx------ 3 victim_user victim_user 4096 Jun 19 23:25 .config
-rw-r--r-- 1 victim_user victim_user  807 Jan  6  2022 .profile
drwx------ 3 victim_user victim_user 4096 Jun 19 23:25 snap

[+] Created a mock exfiltrated file: /home/victim_user/stolen_data.txt


---

## 3. Detection & Evasion Techniques Used
1. **Domain Typosquatting:** Used a local domain (`mysecurelab.com`) to mimic a legitimate corporate domain.
2. **HTTPS (TLS):** Simulated using HTTP for local testing; in production, Let's Encrypt would be used.
3. **Urgency Scare Tactics:** The email claimed the password expires in 24 hours to bypass logical thinking.

---

## 4. Defensive Recommendations
To mitigate these threats, organizations should implement:

1. **Multi-Factor Authentication (MFA):** Enforce MFA on all public-facing and internal applications. Stolen passwords are useless without the second factor.
2. **Security Awareness Training:** Conduct regular simulated phishing exercises (like this one) to train employees to recognize and report suspicious emails.
3. **Email Filtering & SPF/DKIM/DMARC:** Strictly configure email authentication protocols to prevent domain spoofing.
4. **Endpoint Detection & Response (EDR):** Monitor for unusual SSH processes or outbound connections from sensitive servers.
5. **Principle of Least Privilege:** Ensure users (like `victim_user`) have only the access necessary for their role.

---

## 5. Conclusion
This simulation successfully demonstrated the entire cyber kill chain. It highlights that even a single compromised credential can lead to full system access. Proactive defense strategies—combining technology, policy, and user education—are essential to break the chain.

---
