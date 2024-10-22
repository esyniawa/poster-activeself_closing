import qrcode
import sys


def generate_github_qr(repo_url, output_file="githubQR.png"):
    # Create QR code instance
    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    # Add data to the QR code
    qr.add_data(repo_url)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(output_file)
    print(f"QR code saved as {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <github_repo_url> [output_file]")
        sys.exit(1)

    repo_url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "githubQR.png"

    generate_github_qr(repo_url, output_file)