import segno

qrcode = segno.make_qr("https://scientificcomputing.github.io/fenics2024/")


qrcode.to_artistic(
    background="fenics_logo.png",
    target="fenics_qr.png",
    scale=5,
)
