import base64
from io import BytesIO
from PIL import Image

def image_to_base64(image_path: str, format: str = "PNG") -> str:
    """
    Converts an image file to a base64-encoded string.

    Args:
        image_path (str): Path to the image file.
        format (str): Output format (e.g., "PNG", "JPEG"). Defaults to "PNG".

    Returns:
        str: A base64-encoded string representing the image.
    """
    # Open the image
    image = Image.open(image_path)

    # Create a buffer to hold the image data
    buffer = BytesIO()

    # Save the image to the buffer in the specified format
    image.save(buffer, format=format)

    # Encode the buffer contents to base64
    encoded_image = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return encoded_image