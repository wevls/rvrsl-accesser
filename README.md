> [!IMPORTANT]
> Hey everyone,
>
> I wanted to take a moment to address the current state of this project and my future involvement. I worked hard on FemboyAccess, and I've learned a lot from this experience. However, life has gotten busier than expected, and unfortunately, I no longer have the time or energy to continue maintaining and developing this project as I once did.
>
> Additionally, after some reflection, I've decided to step away from working on malware-related projects for now. While this started as a fun project, I feel it's time for me to focus on different areas of development and contribute in ways that align more with my current goals and values.
>
> To those who reached out asking for help or had questions I didn’t manage to respond to: I sincerely apologize. I wasn’t able to keep up with the messages and requests, and I know that might have been frustrating for some of you. Please understand that it wasn’t intentional, I couldn't be available a lot. I hope those who needed assistance were able to find a solution or workaround.
>
> Going forward, I won’t be pushing any more updates or providing support for this project. I'll archive this repository after pushing this commit. However, FemboyAccess will remain open-source, and if anyone wants to fork the project to improve upon it, you’re more than welcome to do so.
>
> Thank you to everyone who has supported this project, provided feedback, and contributed along the way. It’s been a unique journey, but I’m looking forward to focusing on new things. All the best!
>
> — ambr0sial

---

<p align="center">
  <a href="https://github.com/ambr0sial/femboyaccess"><img src="femboyaccess_logo.png" alt="FemboyAccess" width="128" /></a> 
</p>
<p align="center">
  FemboyAccess is a remote administration trojan that uses Discord as a C2C server.
</p>
<p align="center">
  Newest version: 1.8
</p>

## ⚠️ Disclaimer ⚠️

**<div align="center">This project is intended for educational and research purposes only. It is your responsibility to ensure that you use this software in compliance with all applicable laws. The authors of this project are not responsible for any misuse or illegal activities performed with it.</div>**

## Purpose 🔥

FemboyAccess is a RAT (Remote Administration Tool/Trojan) that uses the Discord platform as a C2C (command & control) server. More specifically, it uses your own custom Discord guild and then uses a bot account to send commands from the server to the victim's computer.

## Features ✨

- almost undetectable
- escalate privileges without UAC
- can handle multiple machines at once
- a lot of commands
- silent

FemboyAccess 1.6 and higher contains a stealth mode activated by default (line `61` to change that) that hides the Python window and changes the process name. Reminder that you can create pull requests, so if you have any ideas to hide FemboyAccess even more, give it a shot!

## Usage 🛠

  1. Download Python with all the necessary requirements (`pip install -r requirements.txt` or `pip install -r builder_requirements.txt` for the builder) and the repository to your computer.
  2. [Create a Discord bot](https://discord.dev/) (make sure to check all intents on) then invite it on a new server.
  3. Open `builder.py` and enter what's requested (server ID and bot token).
  4. Finished! Now, you can obfuscate it yourself if you want to. Whenever someone will open the generated `built_femboyaccess.py` file, a new channel will be created in your defined server with a custom session ID. Type `help` to see a list of all available commands.

Note: FemboyAccess treats all machines like sessions and attributes them a 8-character long ID with letters and numbers. That's how the bot can manage multiple machines at the same time. The format of the generated channel name is something like:

`<computer_name>-<session_id>`

So if the computer's name is 'ambr0sial', the channel name will be something like:

`ambr0sial-6ef87f83`

## License 📜

FemboyAccess is using the CC BY-NC 4.0 license. You can click on the badge to see what's it's all about! ✨

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-magenta.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

## Contributing ❤

Contributions are always welcome!

You can create pull requests, we're pretty active.


#### Made with ❤ by [ambr0sial](https://www.github.com/ambr0sial) and [kaipicpic](https://www.github.com/kaipicpic).
