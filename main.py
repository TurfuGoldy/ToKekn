import threading
import os
import signal
import ctypes
import httpx
import time
from colorama import Fore, init
from datetime import datetime


class Tokekn:
    def __init__(self):
        self.lock = threading.Lock()

        self.totalchecked = 0
        self.valid = 0
        self.invalid = 0
        self.locked = 0
        self.ratelimited = 0
        self.unknown = 0

        init(autoreset=True)
        if os.name == "nt":
            os.system("mode con: cols=138 lines=30")

    def title(self, title):
        if os.name == "nt":
            ctypes.windll.kernel32.SetConsoleTitleW(
                f"ToKekn | An Advanced Token Checker | {title}"
            )
        else:
            print(
                f"\33]0;ToKekn | An Advanced Token Checker | {title}\a",
                end="",
                flush=True,
            )

    def logo(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

        print(
            f"""{Fore.LIGHTBLUE_EX}

                                           ████████╗ ██████╗ ██╗  ██╗███████╗██╗  ██╗███╗   ██╗
                                           ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝██║ ██╔╝████╗  ██║
                                              ██║   ██║   ██║█████╔╝ █████╗  █████╔╝ ██╔██╗ ██║
                                              ██║   ██║   ██║██╔═██╗ ██╔══╝  ██╔═██╗ ██║╚██╗██║
                                              ██║   ╚██████╔╝██║  ██╗███████╗██║  ██╗██║ ╚████║
                                              ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                           {Fore.LIGHTMAGENTA_EX}An Advanced Discord Token Checker by Goldy
                                                  
{Fore.RESET}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n
        """
        )

    def tprint(self, text):
        self.lock.acquire()
        print(text)
        self.lock.release()

    def cpm(self):
        while self.totalchecked != self.totaltokens:
            if self.totalchecked != 0:
                self.title(
                    f"[{self.totalchecked}/{self.totaltokens}] VALID - {self.valid} | INVALID - {self.invalid} | LOCKED - {self.locked} | RATELIMITED - {self.ratelimited} | UNKNOWN - {self.unknown}"
                )

            time.sleep(0.1)

    def check(self, token):
        getCookies = httpx.get(
            "https://discord.com/",
            headers={
                "Host": "discord.com",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
                "Accept-Encoding": "gzip, deflate, br",
                "DNT": "1",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Pragma": "no-cache",
                "Cache-Control": "no-cache",
            },
        )

        headers = {
            "Host": "discord.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",
            "Accept": "*/*",
            "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Authorization": token,
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk2LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTYuMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijk2LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTExODgxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
            "X-Discord-Locale": "fr",
            "X-Debug-Options": "bugReporterEnabled",
            "DNT": "1",
            "Connection": "keep-alive",
            "Referer": "https://discord.com/app",
            "Cookie": f"__dcfduid={getCookies.cookies['__dcfduid']}; __sdcfduid={getCookies.cookies['__sdcfduid']}; locale=fr",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "TE": "trailers",
        }

        response = httpx.get(
            "https://discord.com/api/v9/users/@me/affinities/guilds", headers=headers
        )

        if self.tokencensor == "y":
            consoletoken = token.replace(
                token.split(".")[2], "***************************"
            )
        else:
            consoletoken = token

        if not os.path.exists(f"results/{self.date}/"):
            os.makedirs(f"results/{self.date}/")

        if response.status_code == 200:
            if not os.path.exists(f"results/{self.date}/valid"):
                os.makedirs(f"results/{self.date}/valid")

            if self.fullcapture == "y":
                capturerequest = httpx.get(
                    "https://discord.com/api/v9/users/@me", headers=headers
                ).json()

                if "premium_type" in capturerequest:
                    if capturerequest["premium_type"] == 1:
                        nitro = "Nitro Classic"
                    elif capturerequest["premium_type"] == 2:
                        nitro = "Nitro Boost"
                else:
                    nitro = "No Nitro"

                if capturerequest["bio"] == "":
                    bio = "None"
                else:
                    bio = capturerequest["bio"]

                paymentsource = httpx.get(
                    "https://discord.com/api/v9/users/@me/billing/payment-sources",
                    headers=headers,
                ).json()

                allsources = len(paymentsource)
                validsources = 0
                for source in paymentsource:
                    if not source["invalid"]:
                        validsources += 1

                badges = {
                    0: "No Badge",
                    1: "Discord Employee",
                    2: "Discord Partner",
                    4: "HypeSquad Events",
                    8: "Bug Hunter Level 1",
                    16: "SMS recovery for 2FA enabled",
                    32: "Dismissed Nitro promotion",
                    64: "HypeSquad Online House Bravery",
                    128: "HypeSquad Online House Brilliance",
                    256: "HypeSquad Online House Balance",
                    512: "Early Supporter",
                    1024: "Team User",
                    2048: "Relates to partner/verification applications.",
                    4096: "System User",
                    8192: "Has an unread system message",
                    16384: "Bug Hunter Level 2",
                    32768: "Pending deletion for being underage in DOB prompt",
                    65536: "Verified Bot",
                    131072: "Early Verified Bot Developer",
                    262144: "Discord Certified Moderator",
                    524288: "Bot has set an interactions endpoint url",
                    1048576: "User is disabled for being a spammer",
                }

                capture = f"\n    ID - {capturerequest['id']}\n    Username - {capturerequest['username']}#{capturerequest['discriminator']}\n    Creation Date - {datetime.utcfromtimestamp(((int(capturerequest['id']) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %Hh%Mm%Ss')}\n    Email - {capturerequest['email']} (Verified: {capturerequest['verified']})\n    Phone - {capturerequest['phone']}\n    Payment Sources - {validsources}/{allsources} valid source(s)\n    Nitro - {nitro}\n    Badges - {badges[capturerequest['flags']]}\n    MFA - {capturerequest['mfa_enabled']}\n    Locale - {capturerequest['locale']}\n    Bio - {bio}\n"

                with open(
                    f"results/{self.date}/valid/valid_capture.txt",
                    "a",
                    encoding="utf-8",
                ) as file:
                    file.write(f"{token}{capture}\n")
                    file.close()

                if capturerequest["verified"]:
                    with open(
                        f"results/{self.date}/valid/valid_emailverified.txt",
                        "a",
                        encoding="utf-8",
                    ) as file:
                        file.write(f"{token}\n")
                        file.close()

                if capturerequest["phone"]:
                    with open(
                        f"results/{self.date}/valid/valid_phoneverified.txt",
                        "a",
                        encoding="utf-8",
                    ) as file:
                        file.write(f"{token}\n")
                        file.close()

                if capturerequest["verified"] and capturerequest["phone"]:
                    with open(
                        f"results/{self.date}/valid/valid_fullverified.txt",
                        "a",
                        encoding="utf-8",
                    ) as file:
                        file.write(f"{token}\n")
                        file.close()

                if capturerequest["mfa_enabled"]:
                    with open(
                        f"results/{self.date}/valid/valid_mfa.txt",
                        "a",
                        encoding="utf-8",
                    ) as file:
                        file.write(f"{token}\n")
                        file.close()
            else:
                capture = "\n"

            self.tprint(f"{Fore.LIGHTGREEN_EX}[Valid] {consoletoken}{capture}")

            with open(
                f"results/{self.date}/valid/valid_all.txt", "a", encoding="utf-8"
            ) as file:
                file.write(f"{token}\n")
                file.close()

            self.valid += 1
        elif response.status_code == 401:
            self.tprint(f"{Fore.LIGHTRED_EX}[Invalid] {consoletoken}\n")

            with open(
                f"results/{self.date}/invalid.txt", "a", encoding="utf-8"
            ) as file:
                file.write(f"{token}\n")
                file.close()

            self.invalid += 1
        elif response.status_code == 403:
            self.tprint(f"{Fore.LIGHTRED_EX}[Locked] {consoletoken}\n")

            with open(f"results/{self.date}/locked.txt", "a", encoding="utf-8") as file:
                file.write(f"{token}\n")
                file.close()

            self.locked += 1
        elif response.status_code == 429:
            self.tprint(f"{Fore.LIGHTRED_EX}[Ratelimited] {consoletoken}\n")

            with open(
                f"results/{self.date}/ratelimited.txt", "a", encoding="utf-8"
            ) as file:
                file.write(f"{token}\n")
                file.close()

            self.ratelimited += 1
        else:
            self.tprint(f"{Fore.LIGHTRED_EX}[Unknown API Error] {consoletoken}\n")

            with open(
                f"results/{self.date}/unknown.txt", "a", encoding="utf-8"
            ) as file:
                file.write(f"{token}\n")
                file.close()

            self.unknown += 1

        self.totalchecked += 1

    def start(self):
        self.title("Starting")

        self.date = datetime.now().strftime("%d-%m-%Y %Hh%Mm%Ss")

        tokens = []
        for token in open(self.tokensfilename, encoding="utf-8").readlines():
            if not token.isspace():
                tokens.append(token.replace(" ", "").rstrip())

        self.totaltokens = len(tokens)

        threading.Thread(target=self.cpm).start()

        for token in tokens:
            thread = threading.Thread(target=self.check, args=(token,))
            thread.start()
            if threading.active_count() > self.max_threads:
                thread.join()

        while self.totalchecked != self.totaltokens:
            time.sleep(0.1)

        self.title(
            f"(Finished) [{self.totalchecked}/{self.totaltokens}] VALID - {self.valid} | INVALID - {self.invalid} | LOCKED - {self.locked} | RATELIMITED - {self.ratelimited} | UNKNOWN - {self.unknown}"
        )

        print(
            f"{Fore.LIGHTYELLOW_EX}\n\nChecking Finished! Results here: results/{self.date}"
        )

        input()
        os.kill(os.getpid(), signal.SIGTERM)

    def init(self):
        self.title("Initialization")

        self.logo()
        self.tokensfilename = input(
            f"{Fore.LIGHTYELLOW_EX}Enter your tokens file name.\n{Fore.RESET}~# "
        )

        self.logo()
        self.fullcapture = input(
            f"{Fore.LIGHTYELLOW_EX}Do you want a full capture of each valid token? (y/n)\n{Fore.RESET}~# "
        ).lower()
        if not self.fullcapture in ["y", "n"]:
            self.fullcapture = "y"

        self.logo()
        self.tokencensor = input(
            f"{Fore.LIGHTYELLOW_EX}Do you want to censor token in console? (y/n)\n{Fore.RESET}~# "
        ).lower()
        if not self.tokencensor in ["y", "n"]:
            self.tokencensor = "y"

        self.logo()
        self.max_threads = int(
            input(f"{Fore.LIGHTYELLOW_EX}Enter max threads.\n{Fore.RESET}~# ")
        )
        self.logo()

        self.start()


if __name__ == "__main__":
    try:
        Tokekn().init()
    except KeyboardInterrupt:
        os.kill(os.getpid(), signal.SIGTERM)
