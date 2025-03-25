import uuid
import subprocess
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class KenBurnsInput(BaseModel):
    image_url: str

@router.post("/kenburns")
def kenburns(input: KenBurnsInput):
    image_url = input.image_url
    output_path = f"/tmp/kenburns_{uuid.uuid4().hex}.mp4"

    command = [
        "ffmpeg",
        "-loop", "1",
        "-i", image_url,
        "-vf", "zoompan=z='min(zoom+0.0005,1.5)':d=150:s=1280x720",
        "-c:v", "libx264",
        "-t", "6",
        "-pix_fmt", "yuv420p",
        "-y",
        output_path
    ]

    try:
        subprocess.run(command, check=True)
        return {"status": "success", "video_path": output_path}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "detail": str(e)}
