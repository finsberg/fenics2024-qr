import segno

def main() -> None:
    qrcode = segno.make_qr("https://scientificcomputing.github.io/fenics2024/")


    qrcode.to_artistic(
        background="fenics_logo.png",
        target="fenics_qr.png",
        scale=5,
    )


if __name__ == "__main__":
    main()
