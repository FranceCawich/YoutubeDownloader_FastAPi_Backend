from fastapi import FastAPI, HTTPException, Form
from pytube import YouTube

app = FastAPI()

@app.post("/download/")
async def download_video(video_url: str = Form(...)):
    try:
        if not video_url:
            raise HTTPException(status_code=400, detail="Missing video_url parameter")
        
        yt = YouTube(video_url)
        stream = yt.streams.first()
        filename = stream.download()
        return {"message": "Video downloaded successfully", "filename": filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
