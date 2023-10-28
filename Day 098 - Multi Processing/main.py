import concurrent.futures
import requests
import os  # Import the os module

def downloadFile(url, name):
    base_path = r"D:\Python\Day 098 - Multi Processing"  # Define the base directory

    print(f"Started Downloading {name}")
    response = requests.get(url)
    with open(os.path.join(base_path, f"file{name}.jpg"), "wb") as file:
        file.write(response.content)
    print(f"Finished Downloading {name}")

if __name__ == '__main__':
    url = "https://picsum.photos/2000/3000"

    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for i in range(6)]  # Create a list of URLs
        l2 = [i for i in range(6)]   # Create a list of corresponding file names
        results = executor.map(downloadFile, l1, l2)  # Use multi-processing to download files

        for r in results:
            print(r)  # Print the result (if any)
