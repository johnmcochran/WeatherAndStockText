# WeatherAndStockText

			§ Make repos
			§ Create python scripts
			§ weather high/low 
				□ Get today's forecast from api.weather.gov at 7am EST for Indianapolis
				□ Parse the forecast to get the day's high and low and % chance of rain
					® High: highest temp between 7am and 9pm
					® Low: lowest temp between 7am and 9pm
					® % rain: between 7am and 9pm
			§ Yesterday's price change on whichever target date fund I have the most money in
				□ Marketstack api
					® https://marketstack.com/
			§ Orchestrate with airflow
				□ Set up Astronomer developer tier
				□ Set up cheapest possible workers
				□ Look into how dev process works in Astronomer
					® Need to be able to test deployments before pushing to prod
				□ Create DAGs
			§ Send text w/ Twilio
				□ Weather: high/low, rain %
				□ Prior day's % change and current value of retirement date fund
