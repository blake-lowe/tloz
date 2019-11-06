from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC
from colorama import Fore, Back, Style
import os
os.system('color')

PlaySound('audio/Intro.wav', SND_FILENAME|SND_ASYNC|SND_LOOP)

print(f'''
 {Fore.GREEN}.--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--.
{Fore.GREEN}/ .. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\
{Fore.GREEN}\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/ /
{Fore.GREEN} \\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /
{Fore.GREEN} / /\\/ /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /\\/ /\\
{Fore.GREEN}/ /\\ \\/`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\\ \\/\\ \\
{Fore.GREEN}\\ \\/\\ \\                                                                            /\\ \\/ /
{Fore.GREEN} \\/ /\\ \\{Fore.WHITE}                      ___________________________                       {Fore.GREEN}  / /\\/ /
 {Fore.GREEN}/ /\\/ /{Fore.WHITE}              THE LEGEND OF ——————————————————  /                        {Fore.GREEN} \\ \\/ /\\
{Fore.GREEN}/ /\\ \\/                   {Fore.RED}____{Fore.WHITE}\\{Fore.RED}_{Fore.WHITE}\\    {Fore.RED}______  _   ____{Fore.WHITE}/ / {Fore.RED}__{Fore.GREEN}                        \\ \\/\\ \\
{Fore.GREEN}\\ \\/\\ \\                  {Fore.RED}/___  / {Fore.WHITE}\\{Fore.RED}  / ____/ / / |  __ \\ |  \\                       {Fore.GREEN}/\\ \\/ /
{Fore.GREEN} \\/ /\\ \\                    {Fore.RED}/ / {Fore.WHITE}\\ \\{Fore.RED}/ /__   / /  | |{Fore.WHITE}/ {Fore.RED}| ||   \\                    {Fore.GREEN} / /\\/ /
{Fore.GREEN} / /\\/ /                   {Fore.RED}/ /   {Fore.WHITE}\\{Fore.RED}/ ___/  / /   | | {Fore.WHITE}/{Fore.RED}| || |\\ \\                  {Fore.GREEN}  \\ \\/ /\\
{Fore.GREEN}/ /\\ \\/                  {Fore.RED} / /___ / //___ / /___ | |{Fore.WHITE}/{Fore.RED}_| || ___ \\                  {Fore.GREEN}  \\ \\/\\ \\
{Fore.GREEN}\\ \\/\\ \\                  {Fore.RED}/_____//______//_____/ |_____/ |_|  \\_\\              {Fore.GREEN}     /\\ \\/ /
{Fore.GREEN} \\/ /\\ \\ {Fore.WHITE}                           \\ \\        / /                           {Fore.GREEN}     / /\\/ /
{Fore.GREEN} / /\\/ / {Fore.WHITE}    ________________________\\_\\______/_/________________________/^^^^|  {Fore.GREEN} \\ \\/ /\\
{Fore.GREEN}/ /\\ \\/   {Fore.WHITE}    ---_____________________________________________________|-&\\\\\\\\||  {Fore.GREEN}  \\ \\/\\ \\
{Fore.GREEN}\\ \\/\\ \\  {Fore.WHITE}                              \\ \\  / /                          \\___/  {Fore.GREEN}   /\\ \\/ /
{Fore.GREEN} \\/ /\\ \\{Fore.WHITE}                                \\ \\/ /                                  {Fore.GREEN}  / /\\/ /
{Fore.GREEN} / /\\/ /  {Fore.WHITE}                               \\  /                                   {Fore.GREEN}  \\ \\/ /\\
{Fore.GREEN}/ /\\ \\/   {Fore.WHITE}                                \\/                                    {Fore.GREEN}   \\ \\/\\ \\
{Fore.GREEN}\\ \\/\\ \\                                                                            /\\ \\/ /
{Fore.GREEN} \\/ /\\/\\--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--/ /\\/ /
{Fore.GREEN} / /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\
{Fore.GREEN}/ /\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\bl/\\ \\
{Fore.GREEN}\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `' /
{Fore.GREEN} `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'{Fore.WHITE}
''')
input()

PlaySound(None, SND_FILENAME)
