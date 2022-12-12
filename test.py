import webbrowser
import random

# ... construct your list of search terms ...
for i in range(10):
    url = f"https://www.bing.com.tr/search?q=10+{i*random.randint(0,10000)}"
    webbrowser.open_new_tab(url)