'''
    DWIN DGUS  CRC checksum Calculator

* This python code can be used to  find crc checksum
  while working with  DWIN displays, uses "CRC-16 Modbus"

DGUSII platform uses Cyclic Redundancy Check (CRC) to verify data integrity during communication. The
specific variation used is "CRC-16 Modbus"

Note :
Based on "T5L_DGUSII Application Development Guide Version 1.0"
If you are using different version , This might not work.The later versions
uses CRC32 ,


The CRC32 checksum calculator coming soon , wait wait .....
an all in one calculator is coming soon :)

Made with Love in Open Source
73,
Amal Mathew

'''


""""
A Frame (or packet) structure follows this format:
<Frame Header H> <Frame Header L> <Byte Count> <Command> [<Data>] [<CRC H> <CRC L>] Or,
in abbreviated notation:
<FHH> <FHL> <BC> <CMD> [<DATA>] [<CRCH> <CRCL>]

Frame header is 0x5AA5


"""

while True:
    hex_input_str = input("from frame structure enter command and data bytes followed by comma(,) in hexadecimal format \n")

    hex_input_arr = hex_input_str.split(',') #splits string at the character ','

    user_input_arr = []

    for i in range(len(hex_input_arr)):
        #print(hex_input_arr[i])
        user_input_arr.append(hex(int(hex_input_arr[i], 16)))

	#print(user_input_arr)

        crc = 0xFFFF

        length = len(user_input_arr)

        for x in range(0,length):
            #print(hex(int(user_input_arr[x], 16)))
            crc = crc ^ (int(user_input_arr[x], 16))

            for i in range(0,8):

                if((crc & 0x0001) != 0):
                    crc = crc >> 1
                    crc = crc ^ 0xA001

                else:
                    crc = crc >> 1

    crc = ((crc & 0xFF00)>>8) | ((crc & 0x00FF)<< 8)

    print("The CRC checksum is : \t" + hex(crc).upper()+ "\n" )
	
    choice = input("Enter Q to quit, or press return to continue \n")
	
    if choice.lower() == "q":
        break



    



    
