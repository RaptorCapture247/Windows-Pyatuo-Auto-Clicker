# Wallet-Transaction-Auto-Clicker
python script using PyAutoGUI to see and act on user submitted screenshots for confirming or canceling wallet transaction popups. Built for automation of Pond0x particicpation

## !!!REMEMBER!!!

## The pyautogui script WILL click ALL confirm images that match your screen shots for the ENTIRE monitor.

## IF YOU ARE NOT USING IT FOR AUTO MINING/SWAPPING TURN IT OFF!!!!


If you are using the extension "EzmodeV2" to automate your participation on [Pond0x](https://www.pond0x.com/)} you do not need the secondary auto clicker. You can skips steps 8, 9, and 11.

Python Download Windows

https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe

Check the box that says "Add Python to PATH" (super important!) during install.

pip install pyautogui
pip install pillow
pip install opencv-python

.
Windows PyAutoGUI Error Handling Script

https://x.com/i/grok/share/ShKKlqR7tLQLThpdFn1Ma7Fdn

# Step 1

*If you're running the previous version of pyautogui script this should be done already.*

Download and install Python from python.org
on install window click the box that says "add python.exe to path"
then begin install process
you do not need to disable character length

# Step 2
open Windows command prompt
if you dont know where it is:
press windows key + S
type in "command" and select the command prompt at the top of the list


# Step 3
*If running the previous version of the pyautogui script this is done already.*

once Command Prompt is open we will now install PyAutoGUI and the required tools. (all three commands are above for easy copy paste)
first we will type in  or paste the "pip install pyautogui" and press enter
once complete move on to next install command
next we will type in "pip install pillow" and press enter
once complete move to final install command
last we will type in "pip install opencv-python" and press enter

depending on your system some of the packages may require an update. if prompted run the command it gives you.


# Step 4

*If you're running the previous version of pyautogui script this should be done already.*

We will now make a file to save the script and images of your pop-ups.
open file explorer
left hand side of screen you should see a list of locations click "This PC" then "Local Disk (C:)"  then "Users" then you should have a file that is the name of your computer, typically it is your username or a portion of your username, click it.
now right click and create a new folder. We will call this folder "Pyautogui"

# Step 5
Open a blank Notepad document.

Travel to the following grok conversation
https://x.com/i/grok/share/ShKKlqR7tLQLThpdFn1Ma7Fdn


scroll down on the conversation until you see the colored text. This the script you need to copy.
there is a little copy icon in the right corner of the  conversation  (click it).

now go back to the notepad document you opened and paste the script there.

we need to modify a portion of the script before we save it.
from the top of the page count down 3 hashtags (#) you should see the following text

`# Base directory for images (Windows path)
BASE_DIR = "C:\\Users\\YourUsername\\Pyautogui\\`


where it says "YourUsername" delete that section and replace it with your user name. (your username is the folder we opened to create and save the Pyautogui folder in Step 4.

example: my user name is joek so my text should read>

`# Base directory for images (Windows path)
BASE_DIR = "C:\\Users\\joek\\Pyautogui\\`

Next we will go to file and save as. travel to the Pyautogui folder we created in step 4 inside the popup window that appears.
we will name the file "autoswap2.py". under where we typed the file name there is a box that should say .txt (text) click it to open a drop down menu and select "all files"

now click save. 

travel to the folder we created in step 4 and confirm the file has been saved there.


# Step 6
now we will create take a few screen shots of the Phantom popup windows.

travel to Pond0x.com and perform a swap of Sol to wPOND. DO NOT CONFIRM THE TRANSACTION
once you have the popup on screen using your keyboard press windows + shift + S to open the snip tool
take your cursor over to the popup , click and hold, then drag a box around the area seen in the image with this message.
if you see a popup to open the screen shot do so.
if not, open your file explorer and go to your "photos" and look for a folder titled screenshots. right click the icon and select open with and select the snipping tool.
once open you can further crop the image to trim down excess borders not seen in the example image. 

click the save icon and travel to the pyautogui folder we created in step 4 save the file as "confirm1.png"

check the folder to ensure the image is now saved there

this step can be performed with any wallet that you are using. 

IMPORTANT NOTE: once this script is started it will approve ANY and ALL popups that match your images. If you are not using the auto swapper TURN OFF THE SCRIPT!


The next image we are going to grab will be off the slippage tolerance exceeded popup.

in order to force this image we will adjust our slippage to Fixed and a value of 0.01% and use $SOL>USDC.

once we do that we can repeat the above actions. Cancel and retry until you see the image in this message. we will call this image cancel1.png

Finally we will now grab the popup for the xminer when we start a mining session.

Again follow the steps at the beginning of this section to capture the screen shot except you will start a mining session and use the confirm popup that appears. you will want it to look like the example in this message.

we will call this "mine.png"


Additionally you will encounter other popups that are not listed here. you will want to grab screen shots of them and save them.  the first image you will notice a < symbol in the network fee section. you will want to save this one as "confirm2.png". The other is a no balance found error message, This one will need to be saved as cancel2.png. these are both built into the script and after saving will be handled appropriately.

Any other popups that appear will cause the script to pause, making it easy to grab them. if you encounter one, and after grabbing the image and cropping to look similar to the other examples here you can save it as either:
(if you want confirm clicked)
confirm3.png 
confirm4.png
confirm5.png
(if you want cancel clicked)
cancel3.png
cancel4.png
cancel5.png

This gives you a little customization ability to help the script work for you. If you run out of image slots then let us know and we can help you with adding more to the script.



Additional images i have so far.

# Step 7

*If you're running the previous version of pyautogui script this should be done already.*

now we will create a command cheat sheet for you to reference when you need to start the autoswap script

open a new notepad document and paste the commands in the following message.

*If you are using the old pyautogui script you will have two run commands now, autoswap.py and autoswap2.py. this is so if you do not get the newest one running immediately you can still revert back to and use the old one.*

cd C:\Users\YourUsername\PyAutoGUI

python autoswap2.py


after pasting those commands into the fresh notepad document you will change the section that says "YourUsername" to be your username just like we did in step  5.

then save as, name it cheat sheet, and put it into pyautogui folder

# Step 8

### Skip if running EzmodeV2 Extension 
.
we now need to download an auto clicker if you do not have one.
We have found that OP Auto Clicker works well and is a free download.

OP Autoclicker 
https://www.opautoclicker.com/

download and install

# Step 9
### Skip if running EzmodeV2 Extension 
.
once we have an auto clicker installed we are now ready to begin setting up our pond0x swap browser.
open an internet browser that has your wallet installed as an extension.
travel to pond0x.com/swap.
Set browser window zoom to 75%

A few notes:
1- I start my browser size from the "swap again" button position. This is the largest swap console area.
2- The white Pond0x banner at the top of the page is just above the usdc about where it says "you pay"
3- Take note how I have aligned the bottom of the browser just below the purple area of the swap console The reason for this is when the ui glitches and I need to refresh it I know exactly where I need to scroll down to so my auto clicker continues to click the "swap" and "swap again" buttons accurately.
4- Place the browser window towards the top of your screen.
5- If you have multiple monitors you may encounter issues with the script finding the confirm button. to minimize this place the browser window on you number 1 or main monitor


# Step 10
set up your swap settings. use your own personal judgement. i am personally using:
max cap
ultra
0.000007
fixed
1%

make sure you save the settings by scrolling down and clicking save.

You can test if a token pair is eligible for swap boost by making a swap and then referencing your manifest data either through dev tools on the website or Carys manifest dashboard.

i have seen as low as a $0.001 usdc swap to sol count towards swap boost. make your own personal judgement and set a value you wish to swap with.

load you wallet with sufficient funds. the way phantom ( i can not speak for other wallets) works that when you run out of either token in your swap pair it does not generate a confirm button thus once your out of funds it will stop swapping. the script will continue to run and the auto clicker will continue to click but nothing should happen.


# Step 11
### Skip if running EzmodeV2 Extension 
.
open your auto clicker we will be specific to op auto clicker here. adjust to fit your specific clicker program.
set "click repeat" to "repeat until stopped"
click the circle to toggle on "set location"
now go back to your browser and to pond0x.com/swap
make a swap and stop on the popup where the  confirm button is visible.  do not click confirm.
we need to reference the location of the popup to the purple swap button that now should be partially hidden. 
when the Phantom pop-up appears the cursor needs to be hovering over top of the popup in a place that doesn't do anything aka dead space. Your auto clicker will continue to run while this is visible and if it clicks outside the popup or on a clickable box within the popup before 
 has a chance to click confirm the popup will be hidden or you will be redirected and your auto swapper will stall.
in my experience with the above browser setup your cursor should be able to be placed somewhere around the words "network fee" and if the popup is gone it will be on the swap button. ( be aware that there is a clickable section directly below this area)
when we set the auto clicker it will engage the swap button so it needs to land on that if the popup is gone.

once you find a suitable location return to OP and click the box that says "pick location"

your op auto clicker window will disappear now take your cursor and click one time in the location on the popup that you found is dead space and will land on the "swap" button.

once you click once the op window will return and there will now be coordinates listed in the x,y boxes.

# Step 12
Now lets start your script!

open command prompt, and your command cheat sheet. (dont forget we changed the "YourUsername" this is an example)

copy the first line of the cheat sheet > 

cd C:\Users\YourUsername\PyAutoGUI

paste it into your prompt by right clicking in the terminal window. and press enter
the text should now read > C:\Users\YourUsername\PyAutoGUI>

Next copy the second line of the cheat sheet > 

python autoswap.py

paste it into your terminal and press enter.

it should now begin printing a response 

Screen size: 1920x1080 pixels
Attempting to initialize Tkinter...
Tkinter initialized successfully.
Start button created
Stop button created
Starting Tkinter mainloop...

if so then the script is running as intended and you should now have a control panel on screen.

The script will print error messages for the missing images. This is normal, as you encounter and save the popup images these will disappear.

if you receive any other error copy the error and paste it into grok or tag myself or Bearly and we will help you trouble shoot.

# Step 13
minimize the command prompt window.
bring back your pond0x browser window and the new Autoclicker control panel.

on the new control panel you will notice that there are two sections to adjust x and y coordinates for the confirm offsets and the cancel offsets. these are the button locations.

Before you can run the  auto clicker without worry, you will need to fine tune these values to ensure it clicks accurately on each style button. simply stop the clicker with the stop button change the value in x for horizontal direction or y for vertical direction. use small increments probably no more than 5 at a time to get it just right. Do not run the extension while you are doing this. Simply manually process transactions through.

to fine tune the cancel button apply the same settings as you did to force the popup you grabbed the image from in step 6.

Once you have them set, return to your cheat sheet and record the confirm and cancel x,y coordinates. You will need to re enter these everytime you restart the autoclicker program after you close the window.

Congratulations you are now ready to press start and begin your automation journey. 

To end the Autoclicker program simply close the control panel window or close command prompt.

To restart simply open command prompt and your cheat sheet, copy paste each command line into the terminal one at a time and hit enter after each. Once the Autoclicker control panel is on screen re enter your saved coordinates from the cheat sheet and your ready to press start.

## !!!REMEMBER!!!

## The pyautogui script WILL click ALL confirm images that match your screen shots for the ENTIRE monitor.

## IF YOU ARE NOT USING IT FOR AUTO MINING/SWAPPING TURN IT OFF!!!!



