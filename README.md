# PayAttention
This is a simple Python script that I have created to help me study. I started it a while ago to practice file i/o and thought it was quite handy.

The basic idea was that I wanted a way to block certain websites when I am trying to study, I originally thought of creating a proxy server but that turned out more unnecessary than I first thought. I found a workaround which was to edit the '/etc/hosts' file (on unix systems) and route the domain name to a bogus IP address: '0.0.0.0'. 

## Usage
This only requires a UNIX system (this was tested on OSX Mojave) and Python 3 installed. You also need 'sudo' privileges otherwise the program can't edit the '/etc/hosts' file.

The following command will run the program: ``` sudo python3 PayAttention.py ```

The contents of the sites.txt file should just be plain text URL's with the <div>'www.'</div> prefix included as well. Please start a new line after entering one domain name.

```
www.youtube.com
youtube.com
www.facebook.com
facebook.com
```
