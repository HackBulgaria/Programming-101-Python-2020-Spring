# A Music Library

We are going to implement a music library + crawler for the music on our computer.

## Songs

First, we are going to need a `Song` class which we want to initialize like that:

```python
s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
```

**Length can have hours!:**

Those are all valid lengths:

- `"3:44"`
- `"1:30:44"`

The methods we want for our `Song` are:

- `__str__` - should be able to turn the song into the following string: `"{artist} - {title} from {album} - {length}"`
- Our `Song` should be hashabe! Implement `__eq__` and `__hash__`
- `length(seconds=True)` should return the length in seconds.
- `length(minutes=True)` should return the length in minutes (omit the seconds)
- `length(hours=True)` should return the length in hours (omit minutes and seconds that does not add up to a full hour)
- `length()` should return the string representation of the length

## Playlist class

We are going to implement a collection for our songs.

The playlist should be initialized with a name:

```python
code_songs = Playlist(name="Code", repeat=True, shuffle=True)
```

- `repeat` should be defaulted to `False`
- `shuffle` should be defaulted to `False`

The `Playlist` should behave like that:

- `add_song(song)` and `remove_song(song)` are self explanatory.
- `add_songs(songs)` should add a list of `songs`.
- `total_length()` should return a string representation of tha total length of all songs in the playlist
- `artists()` - returns a histogram of all artists in the playlist. For each artist, we must have the count of songs in the playlist.
- `next_song()` should return a `Song` instance from the order of the playlist. If `repeat=True`, when our playlist reaches the end, it should loop back again at the beginning. If `shuffle=True`, everytime we call `next_song()`, we should get a different song. **Make it randomize so it wont repeat a played song unless every song from the playlist has been played!**

## Saving and Loading the playlist

> JSON is a format which is really handy if we want to represent objects. It looks like Python dictionaties. You can check this [tutorial](https://github.com/HackBulgaria/Programming-101-Python-2020-Spring/blob/master/week03/json_tutorial.py) for working JSON files.

We should be able to save and load a playlist to a JSON file. Use the [json](https://docs.python.org/3/library/json.html) module from python.

- `save()` should be a instance method, that saves the playlist to a JSON filed, which has the name of the playlist. If the name has whitespaces in it, replace them with `"-"` - the so-called dasherize.
- `load(path)` should return a new `Playlist` instance with all songs from the file.

Example usage:

```python
code = Playlist("For Code")
# ... adding songs ...

# Saves to For-Code.json
code.save()
```

Later on:

```python
code = Playlist.load("For-Code.json")
code.name == "For Code" # True
```

Save the `*.json` files in a specified folder, for instance, called `playlist-data`. Make the `load` function look there too.
