### 0. Create venv and download dependencies
1. `python -m pip install uncompyle6`
2. download [pyinstallerextractor](https://sourceforge.net/projects/pyinstallerextractor/)

### 1. Convert exe file to pyc file
Using pyinstxtrator.py, enter the command in cmd (from venv): `python pyinstxtractor.py xxx.exe`
![изображение](https://user-images.githubusercontent.com/28976238/161386032-52525b9a-5c9d-4a01-a884-e608d1e76ec6.png)
![изображение](https://user-images.githubusercontent.com/28976238/161386070-977719bf-a352-43ee-93d8-b9cfd94f3919.png)

After successful decompression, a [XXX. Exe] extracted folder will appear in the same path, which contains the main program without any suffix. What we need to decompile is this file, and others are dependent libraries, such as pyz extracted folder. At this point, we may wonder why this file is not a. pyc file? This may be one of the shortcomings of the pyinstxtrator. The main program converted is not in the right format. We need to fix it manually.

### 2. Repair .pyc file
If you directly change the suffix of the main file to main.pyc for decompilation, an error will occur.
![изображение](https://user-images.githubusercontent.com/28976238/161386297-21ad985d-6dd5-4767-b4de-f8c3503d481c.png)

The reason is that the file header magic number is not aligned, so you need to add magic number. Different python versions of magic number are different.

Python 3.6.0's:  
![изображение](https://user-images.githubusercontent.com/28976238/161387150-c7d92f53-90c1-4641-b21d-9dcd5124aed9.png)

Python 3.7.2's:  
![изображение](https://user-images.githubusercontent.com/28976238/161387245-0be678eb-5027-473d-a76c-4c7bf1f2f82c.png)


### 3. How to get magic number
Compile one by yourself to see how many pyinstaller is required for compiling py files, and modules can be installed with pip.  
![изображение](https://user-images.githubusercontent.com/28976238/161386452-40c2d8b3-6ca5-4109-aa77-e36120a200a0.png)

Hexadecimal view its magic number (`C:\Users\Maksim\desktop\1\__pycache__`)  
![изображение](https://user-images.githubusercontent.com/28976238/161386485-cc334c74-ba1b-4166-9fa6-5bb8fe85a8f4.png)

### 4. Add magic number
Add magic number at the top.  
Source:  
![изображение](https://user-images.githubusercontent.com/28976238/161386835-4ede663c-0a3c-4014-b1dd-f2bbf1b1acf2.png)

Add bytes:  
![изображение](https://user-images.githubusercontent.com/28976238/161386911-cf123d93-b480-442f-bc85-ad559b765085.png)

After adding:  
![изображение](https://user-images.githubusercontent.com/28976238/161386925-f817d094-6b18-44d5-b4c4-f0ac489a2fb4.png)

Save .pyc file.

### 5. Decompile pyc files
![изображение](https://user-images.githubusercontent.com/28976238/161387014-2dbe3e37-f8f1-4e85-b410-880584fc5bf6.png)

Done, the source code is displayed in the terminal (a part of the source code is visible in the screenshot).
