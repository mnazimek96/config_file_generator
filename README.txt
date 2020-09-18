This script is written to generate configuration files:
1. parameters.csv
2. param_alloc.h
3. defaults.h
4. config.ini

First of all make sure that your INPUT data is in input folder and that it is named parameters_list.csv.
Than make sure that functions directory is in the same directory as input folder.
Last but not least install requirements:
-> enter command prompt
-> navigate to folder with main.py
-> enter command: pip install -r requirements.txt

INPUT file must have columns: GRUPA, ID, OPIS, FORMAT, MIN, MAX, DEFAULT, RW, SW_DEFINE_NAME, CONFIG, TRANSFER

To generate files type to cmd: python main.py
