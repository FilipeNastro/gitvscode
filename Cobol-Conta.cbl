IDENTIFICATION DIVISION.
PROGRAM-ID. AddNumbers.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 Num1 PIC 9 VALUE ZEROS.
01 Num2 PIC 9 VALUE ZEROS.
01 Sum  PIC 9 VALUE ZEROS.

PROCEDURE DIVISION.
Begin.
    DISPLAY "Enter the first number: ".
    ACCEPT Num1.
    DISPLAY "Enter the second number: ".
    ACCEPT Num2.
    ADD Num1, Num2 GIVING Sum.
    DISPLAY "The sum of ", Num1, " and ", Num2, " is ", Sum.
    STOP RUN.