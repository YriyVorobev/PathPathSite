from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

IMAGE_DIR = BASE_DIR/os.getenv("IMAGE_DIR", "image")

CAT_IMAGE = IMAGE_DIR/"zhivotnye_kot_ochki.jpg"