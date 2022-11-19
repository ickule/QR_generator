"""
This program generates a QR code based on user input.

It also support adding an optionnal image atr the center of the QR code.
"""

import argparse
from pathlib import Path

from PIL import Image

import qrcode


def argument_parser(*args):
    """Handle argumentrs for the program."""
    parser = argparse.ArgumentParser(
        description="This program  generates a QR code with an optionnal image inclusion."
    )
    parser.add_argument(
        "data",
        help="Data of the QR code.",
        type=str,
    )
    parser.add_argument(
        "--ratio",
        "-r",
        help="Select the size ratio for the image.",
        type=float,
        default=1.0,
    )
    parser.add_argument(
        "--image",
        "-i",
        help="Path to the image to iunclude.",
        type=Path,
    )
    parser.add_argument(
        "--color",
        "-c",
        help="Color of the QR code, support X11 colors.",
        type=str,
        default="Black",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Path of the output QR code.",
        type=Path,
        default="dist/QR.png",
    )
    return parser.parse_args(*args)


def main(*args):
    """Run main programm."""
    args = argument_parser(*args)

    output__path = Path(__file__).parent.parent / args.output
    if not output__path.parent.exists():
        output__path.parent.mkdir(mode=0o755)

    # taking image which user wants in the QR code center
    logo = Image.open(args.image)

    # adjust image size
    wpercent = args.ratio * 100 / float(logo.size[0])
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((int(args.ratio * 100), hsize), Image.Resampling.LANCZOS)

    # use highest correction amount to support bigger images
    qr_code = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

    # adding URL or text to qr_code
    qr_code.add_data(args.data)

    # generating QR code
    qr_code.make()

    # adding color to QR code
    qr_image = qr_code.make_image(fill_color=args.color, back_color="white").convert("RGB")

    # set size of QR code
    pos = ((qr_image.size[0] - logo.size[0]) // 2, (qr_image.size[1] - logo.size[1]) // 2)
    qr_image.paste(logo, pos)

    # save the QR code generated
    qr_image.save(Path(__file__).parent / args.output)

    print(f"QR code generated at '{str(output__path)}'!")


if __name__ == "__main__":
    main()
