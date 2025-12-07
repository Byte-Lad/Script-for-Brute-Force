import urllib3
import threading
import queue
import urllib.parse

import urllib.request
import urllib.error
import urllib.parse


threads = 50
target_url = "Target" # Change this
wordlist_file = "YourWordlist.txt"# Change this
resume = None
user_agent = "PutOurUserAgent"# Change this



def build_wordlist(wordlist_file):
	# Read in the word list
	try:
		with open(wordlist_file, "rb") as fd:
			raw_words = fd.readlines()
	except FileExistsError:
		print(f"The file {wordlist_file} not exist..")


	found_resume = False
	words = queue.Queue()

	try:
		for word in raw_words:
			word = word.rstrip()

			if resume is not None:
				if found_resume:
					words.put(word)
				else:
					if word.decode() == resume:
						found_resume =  True
						print(f"Resuming wordlist from: {resume}")
			else:
				words.put(word)
	except Exception as e:
		print(f"{e}\n",words)

	return words


def dir_bruter(word_queue, extensions=None):

	while not word_queue.empty():
		attempt = word_queue.get()

		attemp_list = []

		# Check to see if there is a file extension; if not,
		# it's a directory path we're bruting
		if b"." not in attempt:
			brute = f"/{attempt}/"
		else:
			brute = f"/{attempt}"
		attemp_list.append(brute)

		# If we want to bruteforce extensions
		if extensions:
			for extension in extensions:
				attemp_list.append(f"{attempt}{extension}")

		# Iterate over our list of attemps
		for brute in attemp_list:

			url = f"{target_url}{urllib.parse.quote(brute)}"
		

			try:
				http = urllib3.PoolManager()

				headers = {}
				headers["User-Agent"] = user_agent

				req = urllib.request.Request(url, headers=headers)
				response = urllib.request.urlopen(req)


				if len(body.read()):
					print(f"[{r.status}] => {url}")

			except urllib.error.HTTPError as e:
				if e.code != 404:
					print(f"!!!{e.code} => {url}")

			except urllib.error.URLError as e:
				print(f"[URL ERROR] {e.reason} => {url}")
				pass



if __name__ == "__main__":
	word_queue = build_wordlist(wordlist_file)
	extensions = [".php",".bak",".orig",".inc"]

	for i in range(threads):
		t = threading.Thread(target=dir_bruter, args=(word_queue, extensions,))
		t.start()