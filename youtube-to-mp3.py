# [Dependencies] pip install pytube moviepy

from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

# Function to get the user's desktop path
def get_desktop_path():
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') if os.name == 'nt' else os.path.join(os.path.expanduser('~'), 'Desktop')

# Function to download YouTube video and convert to MP3
def download_youtube_to_mp3(youtube_url, output_path):
    # Download YouTube video
    yt = YouTube(youtube_url)
    video_stream = yt.streams.filter(only_audio=True).first()
    video_file_path = video_stream.download(output_path=output_path)

    # Convert video to audio
    video_clip = VideoFileClip(video_file_path)
    audio_file_path = os.path.splitext(video_file_path)[0] + ".mp3"
    video_clip.audio.write_audiofile(audio_file_path)

    # Close the clips
    video_clip.close()

    # Optionally, delete the original video file
    os.remove(video_file_path)

    return audio_file_path

# Main function to prompt for YouTube link
def main():
    youtube_url = input("Enter the YouTube video URL: ")
    output_path = get_desktop_path()
    mp3_file_path = download_youtube_to_mp3(youtube_url, output_path)
    print(f"MP3 file saved to: {mp3_file_path}")

if __name__ == "__main__":
    main()
