# Steps involved

1. got to https://openweathermap.org/
2. click on API and scroll to 5 Day / 3 Hour Forecast
3. Subscribe - Free - Create account
4. Go back to API 5 Day / 3 Hour Forecast click on API doc
5. Scroll all the way down to Built-in API request by city name
6. api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}&units={units}
7. create a data.txt file and write the first line and remember to get the cursor to the second/third line, since we will only append using the code
8. Every time you run this file, data keeps getting appended, so you can write a script for this file to run every 24 hrs etc.