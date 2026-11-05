import subprocess
import os

# Yahan apne Hashcat ka sahi path daal dein (agar environment variable mein set nahi hai)
HASHCAT_PATH = r"c:\hashcat-8.0.0\hashcat.exe"  # Linux ke liye sirf "hashcat" kar sakte hain

def run_hashcat_brute():
    # Clean aur 100% proper dikhne wala Cyber Sky banner (No font distortion)
    print("\n" + "╔" + "═" * 63 + "╗")
    print("║                  C Y B E R   S K Y   T O O L                  ║")
    print("╚" + "═" * 63 + "╝")
    print("        [+] Advanced Hashcat Automation & Brute-Force Tool")
    print("=" * 65 + "\n")

    # 1. Hash File Input (.hc22000)
    hash_file = input("Enter .hc22000 file path (e.g., wifivikash_7e-b0-de-49-7b-a2.hc22000): ").strip()
    if not os.path.exists(hash_file):
        print("[-] Error: Yeh file maujood nahi hai! Kripya sahi path dein.")
        return

    # 2. Password Length Range Input
    try:
        min_len = int(input("Password ki Minimum Length enter karein (e.g., 8): "))
        max_len = int(input("Password ki Maximum Length enter karein (e.g., 12): "))
    except ValueError:
        print("[-] Kripya valid number enter karein.")
        return

    if min_len > max_len:
        print("[-] Error: Minimum length maximum se badi nahi ho sakti!")
        return

    # 3. Character Set Selection Menu
    print("\n" + "="*25 + " CHARACTER SET " + "="*25)
    print("1. Sirf Numbers (0-9)")
    print("2. Sirf Chote Alphabets (a-z)")
    print("3. Numbers + Alphabets (A-Z, a-z, 0-9)")
    print("4. Sabhi Mix (Numbers + Alphabets + Symbols)")
    print("=" * 65)
    
    choice = input("Apna option chunein (1-4): ").strip()

    # Hashcat custom charset mapping (-1 flag ke liye)
    if choice == '1':
        charset_arg = ["-1", "?d"]
        desc = "Sirf Numbers (0-9)"
    elif choice == '2':
        charset_arg = ["-1", "?l"]
        desc = "Sirf Chote Alphabets (a-z)"
    elif choice == '3':
        charset_arg = ["-1", "?l?u?d"]
        desc = "Numbers + Alphabets (A-Z, a-z, 0-9)"
    elif choice == '4':
        charset_arg = ["-1", "?l?u?d?s"]
        desc = "Sabhi Mix (Numbers + Alphabets + Symbols)"
    else:
        print("[-] Galat option! Default option 4 (Sabhi Mix) use hoga.")
        charset_arg = ["-1", "?l?u?d?s"]
        desc = "Sabhi Mix (Default)"

    # Mask banana (Jitni max length hai, utni baar ?1 repeat hoga)
    mask = "?1" * max_len

    # Hashcat command build karna (-a 3 matlab Mask/Brute-force attack)
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
    print(f"[+] Length Range  : {min_len} se {max_len} characters")
    print(f"[+] Character Set : {desc}")
    print(f"\n[+] Executing Hashcat Command:\n {' '.join(cmd)}\n")
    print("-" * 65)
    print("Hashcat background mein chal raha hai. Rokne ke liye 'Ctrl + C' dabayein...\n")

    try:
        # Hashcat ko execute karna
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n[-] Attack user dwara beech mein rok diya gaya.")

if __name__ == "__main__":
    run_hashcat_brute()