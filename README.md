flask-video-streaming
=====================

Supporting code for my article [video streaming with Flask](http://blog.miguelgrinberg.com/post/video-streaming-with-flask) and its follow-up [Flask Video Streaming Revisited](http://blog.miguelgrinberg.com/post/flask-video-streaming-revisited).

=====================
Matt's notes:

camera.py module has been edited so that the processed image from the CV GUI is displayed. Other modifications have been made elsewhere in order to omit redundent code, as well as some modules being removed all together.

Run the GUI executable to begin the CV processes. Run the app.py script to begin streaming the processed images to a browser, and open https://localhost:5000 to see the stream.
