<?xml version="1.0" encoding="UTF-8"?>
<api>
  <strong><h1>FastAPI YouTube Downloader API</h1><br></strong>
  <strong><description>This API allows you to download YouTube videos by providing the video URL.</description><br></strong> 



![1609606275382](https://github.com/FranceCawich/YoutubeDownloader_FastAPi_Backend/assets/72179627/5cdfbfe5-cec3-4dab-9102-5ad8cff377e0)

  
<setup>
    <step>Install Python 3.7 or higher.</step><br>
    <step>Clone this repository.</step><br>
    <step>Install the required dependencies using pip:</step><br>
    <code>pip install -r requirements.txt</code>
  </setup>
  <strong><usage>
    <step>Start the FastAPI server by running the following command:</step><br>
    <code>uvicorn app:app --reload</code><br>
    <step>Send a POST request to the /download/ endpoint with a JSON payload containing the YouTube video URL. For example:</step><br>
    <request>
      <url>/download/</url><br>
      <payload>{"video_url": "https://www.youtube.com/watch?v=your_video_id_here"}</payload>
    </request>
    <step>If the request is successful, you will receive a JSON response with a message indicating that the video was downloaded successfully and the filename of the downloaded video.</step><br>
  </usage></strong>
  <strong><additional_notes>
    <note>This API uses the pytube library to download YouTube videos. Make sure you have an active internet connection to download videos from YouTube.</note><br>
    <note>By default, the downloaded videos will be saved in the same directory as the FastAPI application. You can modify the code to specify a different download location if needed.</note><br>
  </additional_notes>
</api>


  <strong><h1>Postman Test </h1><br></strong>
  <p> Create a new Post Request as show in the image </p>
  
  
  ![Screenshot 2024-04-30 161435](https://github.com/FranceCawich/YoutubeDownloader_FastAPi_Backend/assets/72179627/743a9fd6-70f8-4265-838b-cb59302674d9)

