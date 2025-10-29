# cheapbananas

Inspiration
Starting university was the first time many of us began fully funding our meal and snack habits—and these expenses definitely add up. Both personal experience and the familiar stereotype that college students love free food inspired us to build a central platform to discover nearby restaurant and snack deals for anyone looking to try new food and save money.

What it does
cheap bananas! locates free and discounted food, including BOGOs, special, seasonal, and new customer offers, near the user's location. We blended Bright Data's power to web scrape data in real time with Letta's persistent, shareable, and self-adaptive memory to create an app above other snack and meal apps by providing comprehensive, up-to-date, and intelligent recommendations that provides the most recent & local meal deals and events with food for users.

How we built it
We used Letta's agent builder, running Claude Opus 4.1, to create our agents that use Bright Data to scrape the web. We used HTML, Python, and JavaScript to code the UI and link to Letta, and Google Maps API to access the user's location and support the interface.

Challenges we ran into
Efficiency was one of the biggest hurdles when we built our platform. The need to link many services introduced significant latency, which exacerbated the event's overloaded wifi, leading to query timeouts and high webscraping response times. We explored different ways to divide and conquer query work including distributing the workload amongst multiple specialized agents simultaneously, unifying them with Letta's shared memory. We also spent time ironing out the links between the UI and the backend given the complex queries and agents needed.

Accomplishments that we're proud of
Integrating various apps to work together, especially giving Letta Bright Data's power to elevate our application's reach and accuracy was one of our greatest accomplishments. Integrating UI locational features, including multiple location displays and interactions is also a source of pride for us.

What we learned
The breadth of knowledge needed for our project brought us to many new areas of knowledge, including ideation and brainstorming techniques, agentic project architecture/design, connecting services through various APIs, SDKs, and MCPs, and fluency with important UI design elements.

What's next for cheap bananas
Our goals for cheap bananas! include increasing the range and efficiency of our queries by migrating to Bright Data SDK, as well as leveraging Letta's persistent memory to create more personalized recommendations.

Built With
brightdata
css
flask
google-maps
html
javascript
letta
python
react

Try it out:

<u>Installing Node.js:</u>
[Node](https://nodejs.org/en/download)

<u>Installing Flask:</u>
[Flask](https://flask.palletsprojects.com/en/stable/installation/)

1. Change directory to backend folder in project directory
2. Download .venv folder: ```python3 -m venv .venv```
3. Activate .venv (virtual environment): ```. .venv/bin/activate```
4. Install required modules in the virtual environment: ```pip install -r requirements.txt```

<u>Running frontend:<u>
1. Change directory to the frontend folder
2. Run ```npm install``` to install the required modules
3. Run ```npm run dev``` to run the development website
