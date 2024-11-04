<h1>FEMBOY ACCESS (Unzesified)</h1>


<p align="center">
  <a href="https://github.com/wevls/rvrsl-accesser"><img src="logo.png" alt="Logo" width="128" /></a> 
</p>
<p align="center">
  RVRSL is a remote administration trojan that uses Discord as a C2C server.
</p>
<p align="center">
  Newest version: 0.1
</p>

## ⚠️ Disclaimer ⚠️

**<div align="center">This project is intended for educational and research purposes only. It is your responsibility to ensure that you use this software in compliance with all applicable laws. The authors of this project are not responsible for any misuse or illegal activities performed with it.</div>**

## Purpose 🔥

RVRSL is a RAT (Remote Administration Tool/Trojan)(forked from femboyaccess, credits to Ambr0sial) that uses the Discord platform as a C2C (command & control) server. More specifically, it uses your own custom Discord guild and then uses a bot account to send commands from the server to the victim's computer.

## Features ✨

- almost undetectable
- escalate privileges without UAC
- can handle multiple machines at once
- a lot of commands
- silent

Rvrsl contains a stealth mode activated by default (line `61` to change that) that hides the Python window and changes the process name. 

## Usage 🛠

  1. Download Python with all the necessary requirements (`pip install -r requirements.txt` or `pip install -r builder_requirements.txt` for the builder) and the repository to your computer.
  2. [Create a Discord bot](https://discord.dev/) (make sure to check all intents on) then invite it on a new server.
  3. Open `builder.py` and enter what's requested (server ID and bot token).
  4. Finished! Now, you can obfuscate it yourself if you want to. Whenever someone will open the generated `build.py` file, a new channel will be created in your defined server with a custom session ID. Type `help` to see a list of all available commands.

Note: FemboyAccess treats all machines like sessions and attributes them a 8-character long ID with letters and numbers. That's how the bot can manage multiple machines at the same time. The format of the generated channel name is something like:

`<computer_name>-<session_id>`

So if the computer's name is 'John', the channel name will be something like:

`John-6ef87f83`

## License 📜

Rvrsl (FemboyAccess) is using the CC BY-NC 4.0 license. You can click on the badge to see what's it's all about! ✨

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-magenta.svg)](https://creativecommons.org/licenses/by-nc/4.0/)


#### FORKED BY [WEVLS](https://github.com/wevls)
MASSIVE CREDITS TO [ambr0sial](https://www.github.com/ambr0sial) and [kaipicpic](https://www.github.com/kaipicpic)
