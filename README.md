
# cnab-automation
Simple Python Script that automates the task of putting separators so the data can be used with Microsoft Excel.
## How to use

    Usage: python main.py [file_path] [--help]
    Description: This script separates the text in a file into specific groups of characters
             adding a delimiter after a variable number of characters
    Parameters
    file_path: (optional) Path of the data file to be processed.
             If not provided, the user will be prompted to enter the path.
             --help: Display this help message.
## Sample Workflow

### Terminal

    $ python3 main.py /home/whoami/Documents/cnab-automation/dummy-data1.txt
    Enter the delimiter character: ;
    Enter the number of characters to jump (0 to finish): 9
    Enter the number of characters to jump (0 to finish): 8
    Enter the number of characters to jump (0 to finish): 5
    Enter the number of characters to jump (0 to finish): 0
    Result file saved: /home/whoami/Documents/cnab-automation/dummy-data1-converted.txt
### Input

    5555555550101202311111
    4444444440205202412345
    3333333330312202512346
    2222222220412202612347
    1111111110511202712348
    9999999990609202812349
    8888888880712202912350
    7777777770810203012351
    6666666660912203112352
    5555555551006203212353
    ...
### Output

    555555555;01012023;11111
    444444444;02052024;12345
    333333333;03122025;12346
    222222222;04122026;12347
    111111111;05112027;12348
    999999999;06092028;12349
    888888888;07122029;12350
    777777777;08102030;12351
    666666666;09122031;12352
    555555555;10062032;12353
    ...
    

Source code under [GPL v3](https://www.gnu.org/licenses/gpl-3.0.pt-br.html)
