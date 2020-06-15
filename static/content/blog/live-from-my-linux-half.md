Title: Live From My Linux Half!
Intro: Finally took the plunge into dual boot
Summary: Finally got off my Ubuntu Virtual Machine into a real dual boot.
Date: 2019-07-31
Tag: pelican site
Slug: live-from-my-linux-half

Since beginning this leg of my coding education, I decided early on to try and develop on Linux. I have a fairly fast machine (Acer Nitro Spin) that hosts an SSD as well as a 1TB HDD as it's intended to be a lower cost gaming machine. Because it was fast, I decided to try working on a virtual machine.

Using Virtualbox and the latest version of Ubuntu, I built myself a basic linux virtual desktop that ran decently on my laptop. And until recently, I was happy to work on it. It ran on the SSD, so it was running fast enough to feel like a real machine.

But it wasn't without it's issues. Video playback was severely stalled, and audio was inconsistent. If I wanted to watch a quick tutorial video, I'd have to launch a browser and go back and forth between my virtual machine and my actual operating system. It would also occasionally lag, specifically with VS Code.

Finally I realized that I really didn't want to go back to coding in Windows, and decided to take the plunge and install a dual boot situation on my computer.

Now I've been someone that has loved to peek under the hood of (and often break) my computers. I take them apart, find software and hardware tweaks, and have more often than not learned what to do by doing it wrong many times over. Took 3 total losses to properly learn how to back up my computer! Anyway, it had been a while since I had a computer project, so I was very excited to take the plunge. 

Annnnnd.....the end result was it worked! I am proudly typing this message on a fully functioning installation of Ubuntu on my computer!

But to get there.....man that was a journey!

First off, I started following [this tutorial](https://itsfoss.com/install-ubuntu-1404-dual-boot-mode-windows-8-81-uefi/) to start the process. And side note, this whole site is just amazing. Truly a lifesaver in this whole process.

Anyway, part way through installation, I got a little cocky and went to brag to my husband about what I was doing. (He humors my nerd code rants). But when I came back, my computer screen was black, the flash drive that held the ISO for Ubuntu was flashing like mad, and I couldn't access anything.

<img style="max-height:40rem;" class="img-fluid d-block mx-auto mb-3" src="{static}/images/Computer-Angry-User-Internet-Unhappy-Frustration.png" alt="Unhappy Computer User">

DAMNIT!!!

I let it go for 30 minutes before finally doing a hard restart on the computer. I started up with my fingers crossed, and it started! And I even had GRUB, the linux boot menu there to pick my operating system.

But, I couldn't log into the linux side of things. It kept cycling. So I did another hard restart, and debated what to do - delete and start over, or see if I could just re-install over the errors. I opted for choice two. That was the wrong choice. While the new installation did work, it did not allow me to shut down on the linux side. It just gave me a black screen with really scary messages of the CPU being frozen. Yet another hard restart.

Then I had to figure out how to start back from zero properly. That required several tutorials, a few videos, and a couple of Stack Overflow posts to get it all done. Again, [It's FOSS](https://itsfoss.com/uninstall-ubuntu-linux-windows-dual-boot/) was a lifesaver.

Finally, I got it working! I set everything up, installed my programs, downloaded by backed up sites...but I couldn't get any of my Python virtual environments to work. I had assumed, since they're virtual, that copying and pasting the folder and files should be ready to work. It wasn't. And I'm honestly not completely clear on why it didn't work. Finally, I just deleted the Venv folder, and re-installed it, along with a new installation of Pelican.

And now I'm back online! It was, at times, very frustrating, but I'm really glad I did it. Running Linux directly on my computer is so much faster, I have better access to my hardware, and honestly I just feel like a badass!
