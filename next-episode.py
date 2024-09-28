import requests

# Replace with your TMDB API key
# Get the API key from https://www.themoviedb.org
API_KEY = 'your-api-key'
BASE_URL = 'https://api.themoviedb.org/3'

# List of TV series names
tv_series_list = ['baby reindeer','better call saul','foundation','friends','game of thrones','the big bang theory','unorthodox','x-men 97','yellowstone','young sheldon',]

# Output file path
output_file = 'tv_series_data.txt'

def get_tv_series_id(tv_show_name):
    search_url = f"{BASE_URL}/search/tv"
    params = {
        'api_key': API_KEY,
        'query': tv_show_name
    }
    response = requests.get(search_url, params=params)
    data = response.json()
    if data['results']:
        return data['results'][0]['id']
    else:
        return None

def get_last_episode(tv_id):
    url = f"{BASE_URL}/tv/{tv_id}"
    params = {'api_key': API_KEY}
    response = requests.get(url, params=params)
    data = response.json()

    last_episode = data.get('last_episode_to_air')
    if last_episode:
        episode_name = last_episode['name']
        air_date = last_episode['air_date']
        return f"Last episode: {episode_name} @ date: {air_date}"
    else:
        return "No last episodes found."

def get_next_episode(tv_id):
    url = f"{BASE_URL}/tv/{tv_id}"
    params = {'api_key': API_KEY}
    response = requests.get(url, params=params)
    data = response.json()
    
    status = data.get('status', 'Unknown')
    if status in ['Ended', 'Canceled', 'Canceled/Ended']:
        last_episode_info = get_last_episode(tv_id)
        return f"Series has been ended. Status: {status}\n{last_episode_info}"

    next_episode = data.get('next_episode_to_air')
    if next_episode:
        episode_name = next_episode['name']
        air_date = next_episode['air_date']
        return f"Next episode: {episode_name} @ date: {air_date}"
    else:
        return "No upcoming episodes found."

with open(output_file, 'w') as file:
    file.write("Information for TV Series:\n")
    file.write("="*50 + "\n\n")

    for series in tv_series_list:
        tv_id = get_tv_series_id(series)
        if tv_id:
            result = get_next_episode(tv_id)
        else:
            result = "TV series not found on TMDB."
        
        file.write(f"{series}:\n{result}\n\n")
        print(f"{series}: {result}")  # Optional: also print to console

print(f"Results have been saved to {output_file}.")
