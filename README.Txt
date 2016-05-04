This is the README file for data mining pinterest using MinePin created by Tatiana Ensslin 2016.

Description: MinePin makes API requests to the Pinterests API, which uses OAUTH 2.0. There are 7 data mining functions, which mine the pin count, creation date, and username of a spcific board. These board categories are: Bunny, Cat, Dog, Summer, Winter, Fall, and Spring. It requires an Access Token to allow for any data mining or API requests to be made. This means that to data mine an individual user's board, one must get their authentication by having them give access to their account. To get a personal Access Token, necesary for MinePin, one can find it at https://developers.pinterest.com/tools/access_token/. Because of this limitation, MinePin requires MANUAL data collection of each user's username. These can be found for Bunny, Summer, Winter, Spring, and Fall through file I/O. The files have been provided in this folder. Cat and Dog username data can be found in a List under each specific function definition. Mine Pin contains three Pinterest API request functions, each providing different data. These include: returnUserInfo(), getBoardInfo(), retrievePins(). MinePin also contains a parser() helper function, which intakes the date and time in isoformat and parses it to the YMD without any spaces. 

RATE LIMITING: Pinterest API only allows 1000 calls per endpoint per hour for each unique user token. Therefore, if you run all seven data functions at the same time, you will be rate limited and shown a 429 ERROR during the last function. All 7 functions require 1050 requests. 

A report of all the data and its findings can be found under PinterestReport.pdf, and a file containing all of the already mined data is under Completed Data. The Excel Data Charts folder contains all the .elsb Excel charts and averages for each board mined.

NOTE: Before you run the code, please use the command: pip install python-dateutil .. for the data parser required within MinePin for your Python.

To Run MinePin.py:

0.Download Python, if not already installed.
1.Download EnsslinMinPin to your working directory.
2.Open up a terminal and cd to the working directory and then cd EnsslinMinPin.
3.Open up MinePin.py on a text editor.
4.Select which data mining functions you would like to run at a time. (You can uncomment/comment them out.)
5.Save the file.
6.Return to the terminal and type the command python MinePin.py 
7.Watch the data be mined for all board categories selected.
8.Upon successful completetion of the code, BOARDNAMEdata.txt will appear within the EnsslinMinPin file. This is all your data!
9. For screenshots of output data please see the ScreenShots folder and locate Output Preview and Output Example.


Social Media Mining 2016. Edmund Yu. Syracuse University College of Engineering and Computer Science.