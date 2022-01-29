I programmed this app with python using the kivy library. It fetches fights from tapology and presents upcoming cards within the app. When clicked it directs you to the fight card page. It also sends notifications to your desktop. Currently only runs on windows but if it somehow gets popular enough I can add different flavors for other OS's. The windows build is under /windows_build/dist. 

Some of the more complex features I implemented:
* I use beautiful soup to load the website and then parse it.
* Uses a regex to indentify fight cards.
* Was able to identify the time zone that is running the application and determine the time is remaining until the fight happens.

![Demo image](/images/demo.png)
