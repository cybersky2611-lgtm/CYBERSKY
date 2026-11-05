import subprocess
import os

# Enter the correct path of your Hashcat here (if not set in environment variables)
HASHCAT_PATH = r"c:\hashcat-8.0.0\hashcat.exe"  # For Linux, you can simply use "hashcat"

def run_hashcat_brute():
    # Clean and 100% proper-looking Cyber Sky banner (No font distortion)
    print("\n" + "╔" + "═" * 63 + "╗")
    print("║                  C Y B E R   S K Y   T O O L                  ║")
    print("╚" + "═" * 63 + "╝")
    print("        [+] Advanced Hashcat Automation & Brute-Force Tool")
    print("=" * 65 + "\n")

    # 1. Hash File Input (.hc22000)
    hash_file = input("Enter .hc22000 file path (e.g., wifivikash_7e-b0-de-49-7b-a2.hc22000): ").strip()
    if not os.path.exists(hash_file):
        print("[-] Error: This file does not exist! Please provide the correct path.")
        return

    # 2. Password Length Range Input
    try:
        min_len = int(input("Enter the Minimum Length of the password (e.g., 8): "))
        max_len = int(input("Enter the Maximum Length of the password (e.g., 12): "))
    except ValueError:
        print("[-] Please enter a valid number.")
        return

    if min_len > max_len:
        print("[-] Error: Minimum length cannot be greater than the maximum length!")
        return

    # 3. Character Set Selection Menu
    print("\n" + "="*25 + " CHARACTER SET " + "="*25)
    print("1. Numbers only (0-9)")
    print("2. Lowercase Alphabets only (a-z)")
    print("3. Numbers + Alphabets (A-Z, a-z, 0-9)")
    print("4. All Mix (Numbers + Alphabets + Symbols)")
    print("=" * 65)
    
    choice = input("Choose your option (1-4): ").strip()

    # Hashcat custom charset mapping (for -1 flag)
    if choice == '1':
        charset_arg = ["-1", "?d"]
        desc = "Numbers only (0-9)"
    elif choice == '2':
        charset_arg = ["-1", "?l"]
        desc = "Lowercase Alphabets only (a-z)"
    elif choice == '3':
        charset_arg = ["-1", "?l?u?d"]
        desc = "Numbers + Alphabets (A-Z, a-z, 0-9)"
    elif choice == '4':
        charset_arg = ["-1", "?l?u?d?s"]
        desc = "All Mix (Numbers + Alphabets + Symbols)"
    else:
        print("[-] Invalid option! Default option 4 (All Mix) will be used.")
        charset_arg = ["-1", "?l?u?d?s"]
        desc = "All Mix (Default)"

    # Creating the mask (repeating ?1 equal to the max length)
    mask = "?1" * max_len

    # Building the Hashcat command (-a 3 means Mask/Brute-force attack)
    cmd = [
        HASHCAT_PATH,
        "-m", "22000",
        "-a", "3",
        hash_file,
    ] + charset_arg + [
        mask,
        "--increment",
        f"--increment-min={min_len}",
        f"--increment-max={max_len}",
        "--force"
    ]

    print(f"\n[+] Target File   : {hash_file}")
    print(f"[+] Length Range  : {min_len} to {max_len} characters")
    print(f"[+] Character Set : {desc}")
    print(f"\n[+] Executing Hashcat Command:\n {' '.join(cmd)}\n")
    print("-" * 65)
    print("Hashcat is running in the background. Press 'Ctrl + C' to stop...\n")

    try:
        # Executing Hashcat
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n[-] Attack interrupted by the user.")

if __name__ == "__main__":
    run_hashcat_brute()