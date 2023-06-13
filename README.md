# Analyzing climate risk with Moody's Climate on Demand
Climate change is a major challenge for businesses and investors, as it poses significant risks to their assets and operations. To assess and manage these risks, we need reliable and comprehensive data on the physical impacts of climate change and their financial implications. This repo shows a quick example of how one can retrieve financial metrics like expected damage and loss due to climate and climate change details on a set of addresses using Moody's Climate on Demand. 

## What is Moody's Climate on Demand?
Moody's Climate on Demand (https://climate.moodys.com/climate-on-demand) is a powerful tool that provides such data for a wide range of climate hazards and scenarios. It enables users to quantify the potential losses and impacts from natural disasters, such as floods, wildfires, windstorms, and earthquakes, as well as from chronic stressors, such as heat-stress, water-stress and sea-level rise. By using Climate on Demand, users can integrate climate risk into their decision making and reporting processes, and enhance their resilience and sustainability.

<p align="center">
<img src="https://github.com/cihanb/sample-climate-risk-with-location-intelligence/blob/main/images/cod-screenshot.png?raw=true" width="500" align= />
</p>

The sample code in the repo show how one can retrieve data for a set of locations/addresses the associated risk in the form of average-annual-loss for each of the nature-made perils like floods, wildfires, sea-level rise and so on. The output generated can be seen in the screenshot below.

<p align="center">
<img src="https://github.com/cihanb/sample-climate-risk-with-location-intelligence/blob/main/images/cod-output-screenshot.png?raw=true" width="500" align= />
</p>

# Getting Started
Ensure to have pandas, python_loadenv, requests available in your python env (or run env_setup.sh). And ensure to have credentials for Moody's Climate on Demand. Copy sample.env to .env and specify the following settings in the ".env" file. 

```markdown
userID = 'your_CoD_username/email'
password = 'your_CoD_password'
baseURL = 'your_URL_for_CoD' 
tenantName = 'your_CoD_tenant_name' 
```

To get the output generated, climate_risk_data_with_cod.py goes through 3 steps
- Get an auth token: ```get_cod_api_token(api_userID, api_password, api_tenantID)```
- Submit your job: ```kick_off_cod_lookup_job(api_tokenID, api_data))```
- Collect scores: ```get_cod_data(api_tokenID, api_jobID)```

the output file generated will contain the risk data and financial metrics next to the addresses passed in to the job. The sample list of addresses used in the code is in the file ```'sample-data/sample_addresses.csv'```.

# Introducing Moody's Climate on Demand
Climate on Demand comes with two editions. 
- **Climate on Demand Standard Edition** provides climate risk scores and climate change risk scores all the way to year 2100 based on hazard intensity. This edition is great for anyone looking to understand where climate and climate change risk is greatest in their portfolios. How that will change over time with the impact of climate change for each location and so on.
- **Climate on Demand Pro Edition** provides advanced climate risk impact scores and financial metrics as well as climate change financial metrics all the way to year 2100 based on loss experience Moody’s RMS has modeled. RMS’s superior science in understanding damage and financial loss comes from its cooperation with the Insurance Industry and 3 decades of historical claims experience that validate how hazards impact assets and how assets vulnerabilities result in financial loss. 

You can read more about how RMS’s science and experience in building models turn into the Climate on Demand Pro metrics [here](https://www.moodysanalytics.com/articles/2023/quantifying-financial-impact-of-climate-risk-with-moodys-climate-on-demand) and [here](https://www.moodysanalytics.com/articles/2023/climate-on-demand-our-vision-for-quantifying-climate-impacts) and find roadmap for Climate on Demand [here](https://www.moodysanalytics.com/articles/2023/moodys-climate-on-demand-version-2-the-road-ahead-for-2023-and-beyond). 

Enjoy.

