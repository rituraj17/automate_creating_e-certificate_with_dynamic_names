import pandas as pd
from PIL import Image, ImageDraw, ImageFont


def certificate_create():
    try:
        # TODO Add the  required CSV file
        data = pd.read_csv("sample.csv")
        name_list = data["Name"].tolist()

        for i in name_list:
            # TODO Add the E-Certificate jpg file
            im = Image.open("sample.jpg")
            d = ImageDraw.Draw(im)
            # TODO Add the Font Type to be used for Name
            location = (913, 1023)
            text_color = (0, 137, 209)
            font = ImageFont.truetype("arial.ttf", 120)
            d.text(location, i, fill=text_color, font=font)
            # TODO Add the Competition name
            location = (952, 1408)
            text_color = (0, 137, 209)
            font = ImageFont.truetype("arial.ttf", 90)
            d.text(location, "Drawing Competition", fill=text_color, font=font)

            im.save("certificate_" + i + ".pdf")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    certificate_create()
