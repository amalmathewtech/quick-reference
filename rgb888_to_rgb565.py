'''
    RGB888 to RGB565 Converter

* Useful when working with  TFT colour display

Especially (cheap) screens used with embedded devices do
not provide 24 bit color-depth. Moreover, storing and/or
transmitting 3 bytes per pixel is consuming quite some
memory and creates latency. RGB565 requires only 16 (5+6+5)
bits/2 bytes and is commonly used with embedded screens. It
provides 5 bits for Red and Blue and 6 bits for Green.
Providing 5 bits for 2 colors and 6 bits for another seems
asymmetric but storing and transmitting something which cannot
nicely be packed in bytes would be complicated. Note that since we
have less bits (information) available, we can represent less colors.
While RGB888 provides 2^24=16 777 216 colors, RGB565 only provides
2^16=65 536 colors.

'''

print('       RGB888 to RGB565 Converter         ')
print('        ------------------------        \n')


loop = True

while loop:

    rgb_value_in_decimal = input("enter r,g,b values in decimal format \n")

    rgb_values = rgb_value_in_decimal.split(',') #splits string at the character ','

    r = int(rgb_values[0])

    g = int(rgb_values[1])

    b = int(rgb_values[2])

    print("corresponding RGB565 format is ")

    dec_to_hex = hex((int(r/8)<<11) | (int(g/4)<<5) | (int(b/8)))

    print(dec_to_hex.upper())
    print('\n')
    choice = input("Enter Q to quit, or press return to continue \n")
    if choice.lower() == "q":
        break
