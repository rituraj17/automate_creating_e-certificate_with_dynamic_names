import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import json

with open("config.json", "r") as f:
    config = json.loads(f.read())

csv_file_name = config["csv_file_name"]
certificate_image = config["certificate_image"]
competition_name = config["competition_name"]
name_input_location = config["location_metrics"]["name_input_location"]
competation_input_location = config["location_metrics"]["competation_input_location"]


def certificate_create():
    try:
        # TODO Add the  required CSV file
        data = pd.read_csv(csv_file_name)
        name_list = data["Name"].tolist()

        for i in name_list:
            # TODO Add the E-Certificate jpg file
            im = Image.open(certificate_image)
            d = ImageDraw.Draw(im)
            # TODO Add the Font Type to be used for Name
            name_location = (
                int(name_input_location["x"]), int(name_input_location["y"]))
            text_color = (0, 137, 209)
            font = ImageFont.truetype("arial.ttf", 120)
            d.text(name_location, i, fill=text_color, font=font)
            # TODO Add the Competition name
            competation_location = (
                int(competation_input_location["x"]), int(competation_input_location["y"]))
            text_color = (0, 137, 209)
            font = ImageFont.truetype("arial.ttf", 90)
            d.text(competation_location, competition_name,
                   fill=text_color, font=font)

            im.save("certificate_" + i + ".pdf")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    certificate_create()
