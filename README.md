# TV Series Next Episode Tracker

This Python script fetches the next episode information for a list of TV series using The Movie Database (TMDB) API. If a series has ended or been canceled, it will report the status and display details of the last aired episode, including its name and air date. The results are saved to a text file.

## Features

- **Fetch Next Episode:** Shows the next episode's name and air date for ongoing TV series.
- **Ended or Canceled Series:** Reports the status of ended or canceled series and displays the last episode aired.
- **Output to File:** Saves all results to a text file for easy review.

## Prerequisites

- Python 3.x installed on your system.
- TMDB API key (register on [TMDB](https://www.themoviedb.org/) to get an API key).
- Python `requests` library.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/reza-qalekhani/tv-series-next-ep.git
   cd tv-series-next-ep
   ```

2. **Install Required Library:**
   Ensure that the `requests` library is installed:
   ```bash
   pip install requests
   ```

3. **Get TMDB API Key:**
Register on [TMDB](https://www.themoviedb.org/) to get an API key. Replace `'your-api-key'` in the script with your TMDB API key.

## Usage

1. **Update the TV Series List:**
Open the script file (`next-episode.py`). Update the `tv_series_list` with the names of the TV series you want to track:
    ```python
    tv_series_list = ['Breaking Bad', 'Stranger Things', 'Friends']
    ```

2. **Run the Script:**
   Run the script from the command line:
   ```bash
   python next-episode.py
   ```

3. **Check the Results:**
    The results will be saved in a file named `tv_series_data.txt` in the same directory. Each series will display either the next episode's information or the last aired episode for ended/canceled series.

## Example Output

Below is an example of what the output file will look like:

```
Next Episode Information for TV Series:
==================================================

Breaking Bad:
Series has been ended. Status: Ended
Last episode: Felina @ date: 2013-09-29

Stranger Things:
No upcoming episodes found.

Friends:
Series has been ended. Status: Ended
Last episode: The Last One @ date: 2004-05-06
```

## Contact

For further information, contact [https://t.me/reza_qalekhani].