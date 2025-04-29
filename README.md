# SWIFT-MESSAGING-TESTING, Simple app for SWIFT messaging

<!-- How to Test
Start the server:
bash
python swift_server.py

Run the client:
bash
python swift_client.py
Expected Output:

Server logs valid SWIFT messages

Client receives "ACK" for valid messages

Invalid messages get "NAK" -->
-------------- output expected ---------
$ python swift_client.py
Raw bytes sent: b'{1:F01BANKDEFFAXXX5432109876}\r\n{2:202BANKGB2LAXXX1234567890}\r\n3:\r\n4:20:TRANSREF2024\r\n21:RELATEDREF123\r\n32A:240531EUR50000,\r\n52A:BANKFRPP\r\n53A:BANKUS33\r\n58A:BANKDEFF\r\n72:/BNF/INV 5678\n-\n}'
Server response: ACK
Sent SWIFT:
{1:F01BANKDEFFAXXX5432109876}
{2:202BANKGB2LAXXX1234567890}
3:
4:20:TRANSREF2024
21:RELATEDREF123
32A:240531EUR50000,
52A:BANKFRPP
53A:BANKUS33
58A:BANKDEFF
72:/BNF/INV 5678
-
}

Family@DESKTOP-DS566KH MINGW64 ~/Documents/SWIFT-MESSAGING-TESTING (main)
$
----------------------------------------

Key Validation Rules in SWIFT
Your server likely checks these (explaining the NAK):

No leading/trailing whitespace in lines

CR/LF line endings (\r\n)

Exact block structure:

{1:...} and {2:...} must be at start of their lines

-} must be the last line

## Field ordering (e.g., 32A before 50K in MT103)

--------------

--------------
Here are valid SWIFT MT message examples you can use for testing, formatted exactly as they appear in real banking systems:

1. MT103 (Single Customer Credit Transfer)
   swift
   {1:F01BANKFRPPAXXX1234123456}
   {2:103BANKUS33AXXX9876543210}
   3:
   4:20:REF1234567
   23B:CRED
   32A:240530USD10000,
   50K:/123456789
   JOHN DOE
   123 MAIN ST
   NEW YORK NY 10001
   59:/987654321
   JANE SMITH
   456 OAK AVE
   LONDON EC1A 1BB
   70:INVOICE 1234
   71A:SHA

-

2. MT202 (General Financial Institution Transfer)
   swift
   {1:F01BANKDEFFAXXX5432109876}
   {2:202BANKGB2LAXXX1234567890}
   3:
   4:20:TRANSREF2024
   21:RELATEDREF123
   32A:240531EUR50000,
   52A:BANKFRPP
   53A:BANKUS33
   58A:BANKDEFF
   72:/BNF/INV 5678

-

3. MT940 (Customer Statement Message)
   swift
   {1:F01BANKGB2LAXXX1234567890}
   {2:940BANKFRPPAXXX9876543210}
   3:
   4:20:STMTREF20240601
   25:FR7630001007941234567890185
   28C:001/001
   60F:C240531EUR10000,
   61:2405310531D500,NTRFNONREF//20240601-0001
   86:/EREF/INV2024-5678/ORDP/JOHN DOE
   62F:C240531EUR9500,

- Key Features of Valid SWIFT Messages:
  Block Structure:

{1:...} = Basic Header Block (F01 = FIN, BANKFRPP = Sender BIC)

{2:...} = Application Header (Message Type + Receiver BIC)

4: = Text Block (Transaction Details)

Field Formatting:

Field Tags: 20, 23B, 32A, etc. (SWIFT-defined)

Dates: Format YYMMDD (e.g., 240530 = May 30, 2024)

Amounts: USD10000, (comma as decimal separator)

Message Termination:

Always ends with -} on its own line
