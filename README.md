# Crushbase Logger

Small Crushbase Logger coded on Python with undetected browser and Selenium. This is very experimental, it will only work with intervals of seconds.

## How to install 

```
git clone https://github.com/BSD-Yassin/Undetected_logger 
cd Undetected_logger

# Optionally use a venv for less conflict 
# python -m venv venv && source venv/bin/activate

pip -r install requirements.txt
```

## Configuration

Do change the line 24 and 25 with your own **login** and **password**

## Notes 

This will not work if you overuse it within several minutes as the bot detection will flag this as bot use, a better solution is to log once and reuse cookies for several selenium sessions. An even better way would be to use the internal API of the website if it can be reverse engineered for everything.