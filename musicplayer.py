import pygame
import os

pygame.init()
pygame.mixer.init()

MUSIC_FOLDER = r"C:\Users\Th\.vscode\Lab1\songs" 

songs = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
current_song_index = 0

def play_song(index):
    global current_song_index
    if songs:
        pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[index]))
        pygame.mixer.music.play()
        print(f"Now playing: {songs[index]}")

if songs:
    play_song(current_song_index)
else:
    print("No music files found in folder.")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Play/Pause
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:  # Stop
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:  # Next song
                current_song_index = (current_song_index + 1) % len(songs)
                play_song(current_song_index)
            elif event.key == pygame.K_p:  # Previous song
                current_song_index = (current_song_index - 1) % len(songs)
                play_song(current_song_index)

pygame.quit()
