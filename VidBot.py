import webbrowser as web
def watch(url):
    try:
        vid = web.open_new(url)
        print "VidBot successful"
    except:
        print "VidBot could not run at the time. Please check your connection."

def main():
    print "Welcome to VidBot, the bot that gives you instant views on your youtube videos!"
    url = raw_input("Enter a URL or enter 'default' for a default one. ")
    if url == 'default':
        url = "https://www.youtube.com/watch?v=cJYqRst4F9M"
    views = raw_input("How many views do you need? ")
    while True:
        try:
            for i in range(int(views)):
                watch(url)
            break
        except:
            print "You did not enter a realistic number of views and/or a real url. Please try again. "
            url = raw_input("Enter a URL or enter 'default' for a default one. ")
            if url == 'default':
                url = "https://www.youtube.com/watch?v=cJYqRst4F9M"

if __name__ == '__main__':
    main()
