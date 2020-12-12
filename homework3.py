genres = ["classic","pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def get_melon_best_album(genre_array, play_array):
    genre_max={}
    for h in range(0,len(genre_array)):
        if genre_array[h] not in genre_max:
            genre_max[genre_array[h]] = play_array[h]
        else:
            genre_max[genre_array[h]] += play_array[h]
    #print(genre_max) #{'pop': 2500, 'classic': 800}
    genre_sort=[]
    while genre_max!={}:
        xstr = max(genre_max.keys(), key = (lambda k: genre_max[k]))
        x = genre_max.pop(max(genre_max.keys(), key = (lambda k: genre_max[k])))
        genre_sort.append(xstr)
    #print(genre_sort) #['pop', 'classic']
    playlist=[] 
    while genre_sort!=[]:        
        counter=0     
        while counter<2:
            max_play = 0
            max_play_index = -1            
            for i in range(0,len(genre_array)):
                if genre_sort[0] == genre_array[i] and max_play<play_array[i]:                    
                    max_play = play_array[i]
                    max_play_index = i

            playlist.append(max_play_index)
            counter+=1            
            play_array[max_play_index]=-1
            #print(playlist)
        genre_sort.pop(0)
    return playlist 


print(get_melon_best_album(genres, plays))
