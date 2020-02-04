# Monoprice Switcher Service

Tested on the Monoprice 8X1 Enhanced Powered HDMI Switcher. The serial communication was reversed engineered by a person going by the name Josh in the Amazon reviews. Without their time and effort this would not be possible. https://amzn.to/2UqCu31

## How to run

1. Create a virtual environment: `virtualenv venv`
2. Activate the virtual environment; `. venv/bin/activate`
3. Install the requirements: `pip install -r requirements.txt`
4. Run service: `python -m flask run`
