from moviepy.editor import VideoFileClip

# Load the video file (.ogv, .mp4, .mpeg, .avi, .mov etc.)
video_file_path = r"C:\Users\d-daemon\Desktop\video_file.mov"
video_clip = VideoFileClip(video_file_path)

# Extract the audio
audio_clip = video_clip.audio

# Define the output audio file path
output_audio_path = r"C:\Users\d-daemon\Desktop\converted_audio.mp3"

# Write the audio file
audio_clip.write_audiofile(output_audio_path)

# Close the clips
audio_clip.close()
video_clip.close()

# End of program
