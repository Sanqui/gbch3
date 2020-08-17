from os import listdir
from collections import Counter, defaultdict
import json

DIR = "data/"
BARCHARS = " ▁▂▃▄▅▆▇█"


def parse_games():
    games = {}
    for filename in listdir(DIR):
        game = filename.split('.txt')[0]
        
        waves = Counter()
        wave_songs = defaultdict(set)

        for line in open(DIR + filename):
            line = line.strip()
            if line.startswith("Song"):
                song_number = int(line.split()[1])+1
            elif line.startswith("WAVE:"):
                _, wave, ticks = line.split()
                wave = tuple([int(x, 16) for x in wave])
                ticks = int(ticks)
                waves[wave] += ticks
                wave_songs[wave].add(song_number)
        
        games[game] = {}
        games[game]['waves'] = waves
        games[game]['wave_songs'] = wave_songs
    
    games = dict(sorted(games.items(), key=lambda x: x[0]))
    return games

def output():
    # Outdated
    print("\n        Ch3 waveform statistics for Pokémon Red\n")

    for wave, count in waves.most_common(50):
        lines = ["", ""]
        for wc in wave:
            lines[0] += BARCHARS[wc&0b111 if wc > 8 else 0]
            lines[1] += BARCHARS[wc&0b1111 if wc < 9 else 8]

        lines[0] += " "
        lines[0] += "".join(['{:x}'.format(x) for x in wave])
        num_ticks = count
        num_songs = len(wave_songs[wave])
        if num_songs < 5:
            song_text = str(wave_songs[wave])
        else:
            song_text = str(num_songs)
        lines[1] += f" Ticks: {num_ticks:> 7}  Songs: {song_text:>3}"

        print("\n".join(lines))

    print('\n')

def export():
    json_out = {}
    for game, data in games.items():
        json_out[game] = {}
        json_out[game]['waves'] = {}
        json_out[game]['most_ticks'] = data['waves'].most_common(1)[0][1]
        for wave, count in data['waves'].most_common(50):
            if count < 50: continue;
            wave_hex = "".join(['{:x}'.format(x) for x in wave])
            songs = data['wave_songs'][wave]
            json_out[game]['waves'][wave_hex] = {'ticks': count, 'songs': list(songs)}

    print(json.dumps(json_out))

games = parse_games()
export()
