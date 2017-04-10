import webbrowser as WebBrowser

# MacOS
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

chrome = WebBrowser.get('windows-default')

chrome.open('http://www.youtube.com/')
chrome.open('http://www.finofilipino.org/')
chrome.open('http://www.reddit.com/')
chrome.open_new('http://www.gmail.com/')
