flask-video-streaming
=====================

Supporting code for my article [video streaming with Flask](http://blog.miguelgrinberg.com/post/video-streaming-with-flask) and its follow-up [Flask Video Streaming Revisited](http://blog.miguelgrinberg.com/post/flask-video-streaming-revisited).

camera.py module has been edited so that webcam data can be streamed. Other modifications have been made elsewhere in order to omit redundent code, as well as some modules being removed all together.

Run the app.py script to begin the application, and open https://localhost:5000 to see the webcam stream.

Go to camera.py in order to modify the video stream that is yielded.
