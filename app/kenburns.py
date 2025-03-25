from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import subprocess
import uuid
import os

router = APIRouter()

class KenburnsRequest(BaseModel):
    image_url: str

@router.post("/kenburns")
def create_kenburns_video(req: KenburnsRequest):
    output_path = f"/tmp/kenburns_{uuid.uuid4().hex}.mp4"

    command = [
        "ffmpeg",
        "-loop", "1",
        "-i", req.image_url,
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
        raise HTTPException(status_code=500, detail=str(e))
