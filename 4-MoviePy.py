from moviepy import *

video = VideoFileClip("input.mp4").subclip(0, 5)  # First 5 seconds
video = video.fx(vfx.colorx, 1.5)  # Brighten video
video.write_videofile("output.mp4")