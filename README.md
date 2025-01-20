# RansomwarePy

RansomwarePy is a Python-based script designed to simulate ransomware behavior for educational and research purposes. It encrypts files within a specified directory, demonstrating the potential impact of ransomware attacks. **This tool is intended solely for educational use.** Unauthorized deployment against systems without explicit permission is illegal and unethical.

## Features

- **File Encryption**: Recursively encrypts files in a specified directory using symmetric encryption.
- **Customizable Parameters**: Allows users to define target directories and encryption keys.
- **Educational Demonstration**: Serves as a practical example of ransomware mechanics for learning purposes.

## Requirements

- Python 3.x
- Required Python libraries (listed in `requirements.txt`)

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/sftp-nik/RansomwarePy.git
   ```

2. **Navigate to the Directory**:

   ```bash
   cd RansomwarePy
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

**Warning**: Executing this script will encrypt files in the specified directory. Ensure you have backups and are operating in a controlled environment.

1. **Run the Script**:

   ```bash
   python ransomware.py --target /path/to/target_directory --key your_encryption_key
   ```

   - `--target`: Path to the directory containing files to encrypt.
   - `--key`: Encryption key used for encrypting files.

2. **Decrypt Files**:

   To decrypt the files, use the decryption script provided:

   ```bash
   python decrypt.py --target /path/to/target_directory --key your_encryption_key
   ```

## Legal Disclaimer

This project is intended for educational purposes only to understand the mechanics of ransomware. Unauthorized use of this script against systems without explicit permission is illegal and unethical. The author is not responsible for any misuse of this tool.

## References

- [Ransomware - Wikipedia](https://en.wikipedia.org/wiki/Ransomware)
- [Ransomware - FBI](https://www.fbi.gov/how-we-can-help-you/scams-and-safety/common-frauds-and-scams/ransomware)
- [A guide to ransomware - NCSC.GOV.UK](https://www.ncsc.gov.uk/ransomware/home)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Note**: Always operate within legal and ethical boundaries when using security-related tools. Unauthorized access to computer systems is prohibited by law. 
