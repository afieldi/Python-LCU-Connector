# LCU Connector for Python
This project helps to easily connect to Riot Games' LCU API. 

## Install
To use this, install with 
```
pip install lcu_connector_python
```
## Usage
When you want to use it. 
```
import lcu_connector_python as lcu
api_connection_data = lcu.connect()
```
If League of Legends is not installed in the defualt location, "C:/Riot Games/League of Legends", then you will need to pass the location of your league folder. Example:
```
import lcu_connector_python as lcu
api_connection_data = lcu.connect("C:/Riot Games/League of Legends/RADS/projects/league_client/releases/0.0.0.178/deploy/LeagueClient.exe")
```

The connect() function returns a dictionary which include data required to connect to the LCU
```
{
    port: "localhost port number",
    url: "url used to communicated with the lcu",
    authorization: "auth token",
    connection_method: "http or https"
}
```

## Extra Notes
When connecting to the LCU you will need to pass the auth token as a header. 
```
{
    "Authorization": "Basic AUTH_TOKEN_HERE",
    ... other headers
}
```
