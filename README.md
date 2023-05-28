# Sample : Analyzing climate-risk with location-intelligence products
Climate and climate change is increasingly an important element to capture for anyone looking to get a full understanding risk. Moodys Climate on Demand provides fiancial loss estimates and impact scores to help incorperate risk from nature-made perils including floods, wildfires, wind-storms, earhquakes as well as heat-stress, water-stress and sea-level rise. 

This sample show how using the Moody's Climate on Demand product, one can retrieve data for a set of locations/addresses the associated risk in the form of average-annual-loss for each of the nature-made perils. 

With the sample, one can see the simple steps it takes to
- Retrieve financial loss metrics in USD for a given asset such as a building at a given address. 
- Retrieve damage and loss impact predicting future impact of climate change using scenarios such as RCP 4.5 and RCP 8.5 (https://github.com/cihanb/sample-climate-risk-with-location-intelligence) for a given time horizon like year 2030 or year 2090.

To get started, ensure you set up your env (env_setup.sh for bash users) and run the climate_risk_data_with_cod.py.
The sample uses a small list of random addresses to build a job to retrieve climate risk scores, then saves the output to a cod_output.csv file.

