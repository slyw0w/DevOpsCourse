# #1.
# try:
#     a = 1/0
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")

#3. The code isn't legal as there are syntax errors. The colon needs to be on the same line as try and finally,
#    and the 2nd error is that the indentation is missing for the code blocks and the 3rd error is the double quotes for finally are wrong.
#4. The handler except: without specifying any exception type) will catch ALL exceptions, which considered a bad practice.
#5. We didn't specify the exception handler we would like to use so it will catch ALL exceptions, system exceptions.
#6. IOError will catch input/output errors such as 'file not found/permission denied'
   # ZeroDivisionError will catch attempts to divide by zero such as 'x/0'
# #7.
# def create_text_file():
#     with open("words.txt", "w") as f:
#         f.write("")
#
#
# #8.
# def write_name_to_file():
# with open("words.txt", "w") as f:
#     f.write("Nadav\n")

# #9.
# def read_and_print_file():
# with open("words.txt", "r") as f:
# content = f.read()
# print(content)

# #10.
# def write_hebrew_to_file():
# hebrew_text = "אני אוהב פייתון"
# with open('words.txt', 'a', encoding="utf-8") as file:
#     file.write(hebrew_text + "\n")
#
# with open('words.txt', 'r', encoding="utf-8") as file:
#     content = file.read()
#     print(content)

# #Challenge:
# from PIL import Image, ImageDraw, ImageFont
# def create_image():
#     img = Image.new('RGB', (400, 400), 'purple')
#     img.save("image.png")
#     draw = ImageDraw.Draw(img)
#     try:
#         font = ImageFont.truetype("arial.ttf", 20)
#     except IOError:
#         font = ImageFont.load_default()
#     draw.text((10, 40), "hello", fill=(0, 0, 0), font=font)
#     img.save("image.png")
#     print("Image 'image.png' created!")








