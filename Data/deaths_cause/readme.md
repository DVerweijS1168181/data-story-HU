# Share of deaths from major causes - Data package

This data package contains the data that powers the chart ["Share of deaths from major causes"](https://ourworldindata.org/grapher/share-of-deaths-from-major-causes?v=1&csvType=full&useColumnShortNames=false) on the Our World in Data website.

## CSV Structure

The high level structure of the CSV file is that each row is an observation for an entity (usually a country or region) and a timepoint (usually a year).

The first two columns in the CSV file are "Entity" and "Code". "Entity" is the name of the entity (e.g. "United States"). "Code" is the OWID internal entity code that we use if the entity is a country or region. For normal countries, this is the same as the [iso alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of the entity (e.g. "USA") - for non-standard countries like historical countries these are custom codes.

The third column is either "Year" or "Day". If the data is annual, this is "Year" and contains only the year as an integer. If the column is "Day", the column contains a date string in the form "YYYY-MM-DD".

The remaining columns are the data columns, each of which is a time series. If the CSV data is downloaded using the "full data" option, then each column corresponds to one time series below. If the CSV data is downloaded using the "only selected data visible in the chart" option then the data columns are transformed depending on the chart type and thus the association with the time series might not be as straightforward.

## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc.. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc..

## About the data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stich together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

### How we process data at Our World In Data
All data and visualizations on Our World in Data rely on data sourced from one or several original data providers. Preparing this original data involves several processing steps. Depending on the data, this can include standardizing country names and world region definitions, converting units, calculating derived indicators such as per capita measures, as well as adding or adapting metadata such as the name or the description given to an indicator.
[Read about our data pipeline](https://docs.owid.io/projects/etl/)

## Detailed information about each time series


## Digestive diseases
Share of total reported deaths in both sexes in those aged all ages that are from digestive diseases.
Last updated: July 26, 2024  
Next update: July 2025  
Date range: 1950–2022  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
WHO Mortality Database (2024) – with minor processing by Our World in Data

#### Full citation
WHO Mortality Database (2024) – with minor processing by Our World in Data. “Digestive diseases” [dataset]. WHO Mortality Database, “WHO Mortality Database” [original data].
Source: WHO Mortality Database (2024) – with minor processing by Our World In Data

### What you should know about this data
* The International Classification of Diseases (Version 10) codes that define digestive diseases are K20-K92.

### Source

#### WHO Mortality Database
Retrieved on: 2024-07-26  
Retrieved from: https://platform.who.int/mortality  


## Infectious and parasitic diseases
Share of total reported deaths in both sexes in those aged all ages that are from infectious and parasitic diseases.
Last updated: July 26, 2024  
Next update: July 2025  
Date range: 1950–2022  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
WHO Mortality Database (2024) – with minor processing by Our World in Data

#### Full citation
WHO Mortality Database (2024) – with minor processing by Our World in Data. “Infectious and parasitic diseases” [dataset]. WHO Mortality Database, “WHO Mortality Database” [original data].
Source: WHO Mortality Database (2024) – with minor processing by Our World In Data

### What you should know about this data
* The International Classification of Diseases (Version 10) codes that define infectious and parasitic diseases are A00-B99, G00-G04, G14, N70-N73, P37.3, P37.4.

### Source

#### WHO Mortality Database
Retrieved on: 2024-07-26  
Retrieved from: https://platform.who.int/mortality  


## Respiratory diseases
Share of total reported deaths in both sexes in those aged all ages that are from respiratory diseases.
Last updated: July 26, 2024  
Next update: July 2025  
Date range: 1950–2022  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
WHO Mortality Database (2024) – with minor processing by Our World in Data

#### Full citation
WHO Mortality Database (2024) – with minor processing by Our World in Data. “Respiratory diseases” [dataset]. WHO Mortality Database, “WHO Mortality Database” [original data].
Source: WHO Mortality Database (2024) – with minor processing by Our World In Data

### What you should know about this data
* The International Classification of Diseases (Version 10) codes that define respiratory diseases are J30-J98.

### Source

#### WHO Mortality Database
Retrieved on: 2024-07-26  
Retrieved from: https://platform.who.int/mortality  


## Diabetes, blood and endocrine disorders
Share of total reported deaths in both sexes in those aged all ages that are from diabetes mellitus, blood and endocrine disorders.
Last updated: July 26, 2024  
Next update: July 2025  
Date range: 1950–2022  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
WHO Mortality Database (2024) – with minor processing by Our World in Data

#### Full citation
WHO Mortality Database (2024) – with minor processing by Our World in Data. “Diabetes, blood and endocrine disorders” [dataset]. WHO Mortality Database, “WHO Mortality Database” [original data].
Source: WHO Mortality Database (2024) – with minor processing by Our World In Data

### What you should know about this data
* The International Classification of Diseases (Version 10) codes that define diabetes mellitus, blood and endocrine disorders are E10-E14, D55-D64 (minus D64.9),D65-D89, E03-E07, E15-E16, E20-E34, E65-E88.

### Source

#### WHO Mortality Database
Retrieved on: 2024-07-26  
Retrieved from: https://platform.who.int/mortality  


## Intentional injuries
Share of total reported deaths in both sexes in those aged all ages that are from intentional injuries.
Last updated: July 26, 2024  
Next update: July 2025  
Date range: 1950–2022  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
WHO Mortality Database (2024) – with minor processing by Our World in Data

#### Full citation
WHO Mortality Database (2024) – with minor processing by Our World in Data. “Intentional injuries” [dataset]. WHO Mortality Database, “WHO Mortality Database” [original data].
Source: WHO Mortality Database (2024) – with minor processing by Our World In Data

### What you should know about this data
* The International Classification of Diseases (Version 10) codes that define intentional injuries are X60-Y09, Y35-Y36, Y870, Y871.

### Source

#### WHO Mortality Database
Retrieved on: 2024-07-26  
Retrieved from: https://platform.who.int/mortality  


## Perinatal conditions
Share of total reported deaths in both sexes in those aged all ages that are from perinatal conditions.
Last updated: July 26, 2024  
Next update: July 2025  
Date range: 1950–2022  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
WHO Mortality Database (2024) – with minor processing by Our World in Data

#### Full citation
WHO Mortality Database (2024) – with minor processing by Our World in Data. “Perinatal conditions” [dataset]. WHO Mortality Database, “WHO Mortality Database” [original data].
Source: WHO Mortality Database (2024) – with minor processing by Our World In Data

### What you should know about this data
* The International Classification of Diseases (Version 10) codes that define perinatal conditions are P00-P96 (minus P23, P37.3, P37.4).

### Source

#### WHO Mortality Database
Retrieved on: 2024-07-26  
Retrieved from: https://platform.who.int/mortality  


## Respiratory infections
Share of total reported deaths in both sexes in those aged all ages that are from respiratory infections.
Last updated: July 26, 2024  
Next update: July 2025  
Date range: 1950–2022  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
WHO Mortality Database (2024) – with minor processing by Our World in Data

#### Full citation
WHO Mortality Database (2024) – with minor processing by Our World in Data. “Respiratory infections” [dataset]. WHO Mortality Database, “WHO Mortality Database” [original data].
Source: WHO Mortality Database (2024) – with minor processing by Our World In Data

### What you should know about this data
* The International Classification of Diseases (Version 10) codes that define respiratory infections are H65-H66, J00-J22,  P23, U04, U07.1, U07.2, U09.9, U10.9.

### Source

#### WHO Mortality Database
Retrieved on: 2024-07-26  
Retrieved from: https://platform.who.int/mortality  


## Dementias and neuropsychiatric disorders
Share of total reported deaths in both sexes in those aged all ages that are from neuropsychiatric conditions.
Last updated: July 26, 2024  
Next update: July 2025  
Date range: 1950–2022  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
WHO Mortality Database (2024) – with minor processing by Our World in Data

#### Full citation
WHO Mortality Database (2024) – with minor processing by Our World in Data. “Dementias and neuropsychiatric disorders” [dataset]. WHO Mortality Database, “WHO Mortality Database” [original data].
Source: WHO Mortality Database (2024) – with minor processing by Our World In Data

### What you should know about this data
* The International Classification of Diseases (Version 10) codes that define neuropsychiatric conditions are F01-F99, G06-G98 (minus G14), U07.0, X41, X42, X44, X45.

### Source

#### WHO Mortality Database
Retrieved on: 2024-07-26  
Retrieved from: https://platform.who.int/mortality  


## Cancers
Share of total reported deaths in both sexes in those aged all ages that are from malignant neoplasms.
Last updated: July 26, 2024  
Next update: July 2025  
Date range: 1950–2022  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
WHO Mortality Database (2024) – with minor processing by Our World in Data

#### Full citation
WHO Mortality Database (2024) – with minor processing by Our World in Data. “Cancers” [dataset]. WHO Mortality Database, “WHO Mortality Database” [original data].
Source: WHO Mortality Database (2024) – with minor processing by Our World In Data

### What you should know about this data
* The International Classification of Diseases (Version 10) codes that define malignant neoplasms are C00-C97.

### Source

#### WHO Mortality Database
Retrieved on: 2024-07-26  
Retrieved from: https://platform.who.int/mortality  


## Cardiovascular disease
Share of total reported deaths in both sexes in those aged all ages that are from cardiovascular diseases.
Last updated: July 26, 2024  
Next update: July 2025  
Date range: 1950–2022  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
WHO Mortality Database (2024) – with minor processing by Our World in Data

#### Full citation
WHO Mortality Database (2024) – with minor processing by Our World in Data. “Cardiovascular disease” [dataset]. WHO Mortality Database, “WHO Mortality Database” [original data].
Source: WHO Mortality Database (2024) – with minor processing by Our World In Data

### What you should know about this data
* The International Classification of Diseases (Version 10) codes that define cardiovascular diseases are I00-I99.

### Source

#### WHO Mortality Database
Retrieved on: 2024-07-26  
Retrieved from: https://platform.who.int/mortality  


## Ill-defined injuries
Share of total reported deaths in both sexes in those aged all ages that are from ill-defined injuries.
Last updated: July 26, 2024  
Next update: July 2025  
Date range: 1968–2022  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
WHO Mortality Database (2024) – with minor processing by Our World in Data

#### Full citation
WHO Mortality Database (2024) – with minor processing by Our World in Data. “Ill-defined injuries” [dataset]. WHO Mortality Database, “WHO Mortality Database” [original data].
Source: WHO Mortality Database (2024) – with minor processing by Our World In Data

### What you should know about this data
* The International Classification of Diseases (Version 10) codes that define ill-defined injuries are Y10-Y34, Y872.

### Source

#### WHO Mortality Database
Retrieved on: 2024-07-26  
Retrieved from: https://platform.who.int/mortality  


## Musculoskeletal diseases
Share of total reported deaths in both sexes in those aged all ages that are from musculoskeletal diseases.
Last updated: July 26, 2024  
Next update: July 2025  
Date range: 1950–2022  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
WHO Mortality Database (2024) – with minor processing by Our World in Data

#### Full citation
WHO Mortality Database (2024) – with minor processing by Our World in Data. “Musculoskeletal diseases” [dataset]. WHO Mortality Database, “WHO Mortality Database” [original data].
Source: WHO Mortality Database (2024) – with minor processing by Our World In Data

### What you should know about this data
* The International Classification of Diseases (Version 10) codes that define musculoskeletal diseases are M00-M99.

### Source

#### WHO Mortality Database
Retrieved on: 2024-07-26  
Retrieved from: https://platform.who.int/mortality  


## Congenital anomalies
Share of total reported deaths in both sexes in those aged all ages that are from congenital anomalies.
Last updated: July 26, 2024  
Next update: July 2025  
Date range: 1950–2022  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
WHO Mortality Database (2024) – with minor processing by Our World in Data

#### Full citation
WHO Mortality Database (2024) – with minor processing by Our World in Data. “Congenital anomalies” [dataset]. WHO Mortality Database, “WHO Mortality Database” [original data].
Source: WHO Mortality Database (2024) – with minor processing by Our World In Data

### What you should know about this data
* The International Classification of Diseases (Version 10) codes that define congenital anomalies are Q00-Q99.

### Source

#### WHO Mortality Database
Retrieved on: 2024-07-26  
Retrieved from: https://platform.who.int/mortality  


## Maternal conditions
Share of total reported deaths in both sexes in those aged all ages that are from maternal conditions.
Last updated: July 26, 2024  
Next update: July 2025  
Date range: 1950–2022  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
WHO Mortality Database (2024) – with minor processing by Our World in Data

#### Full citation
WHO Mortality Database (2024) – with minor processing by Our World in Data. “Maternal conditions” [dataset]. WHO Mortality Database, “WHO Mortality Database” [original data].
Source: WHO Mortality Database (2024) – with minor processing by Our World In Data

### What you should know about this data
* The International Classification of Diseases (Version 10) codes that define maternal conditions are O00-O99.

### Source

#### WHO Mortality Database
Retrieved on: 2024-07-26  
Retrieved from: https://platform.who.int/mortality  


## Nutritional deficiencies
Share of total reported deaths in both sexes in those aged all ages that are from nutritional deficiencies.
Last updated: July 26, 2024  
Next update: July 2025  
Date range: 1950–2022  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
WHO Mortality Database (2024) – with minor processing by Our World in Data

#### Full citation
WHO Mortality Database (2024) – with minor processing by Our World in Data. “Nutritional deficiencies” [dataset]. WHO Mortality Database, “WHO Mortality Database” [original data].
Source: WHO Mortality Database (2024) – with minor processing by Our World In Data

### What you should know about this data
* The International Classification of Diseases (Version 10) codes that define nutritional deficiencies are E00-E02, E40-E46, E50, D50-D53,D64.9, E51-E64.

### Source

#### WHO Mortality Database
Retrieved on: 2024-07-26  
Retrieved from: https://platform.who.int/mortality  


## Non-malignant cancers
Share of total reported deaths in both sexes in those aged all ages that are from other neoplasms.
Last updated: July 26, 2024  
Next update: July 2025  
Date range: 1950–2022  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
WHO Mortality Database (2024) – with minor processing by Our World in Data

#### Full citation
WHO Mortality Database (2024) – with minor processing by Our World in Data. “Non-malignant cancers” [dataset]. WHO Mortality Database, “WHO Mortality Database” [original data].
Source: WHO Mortality Database (2024) – with minor processing by Our World In Data

### What you should know about this data
* The International Classification of Diseases (Version 10) codes that define other neoplasms are D00-D48.

### Source

#### WHO Mortality Database
Retrieved on: 2024-07-26  
Retrieved from: https://platform.who.int/mortality  


## Skin diseases
Share of total reported deaths in both sexes in those aged all ages that are from skin diseases.
Last updated: July 26, 2024  
Next update: July 2025  
Date range: 1950–2022  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
WHO Mortality Database (2024) – with minor processing by Our World in Data

#### Full citation
WHO Mortality Database (2024) – with minor processing by Our World in Data. “Skin diseases” [dataset]. WHO Mortality Database, “WHO Mortality Database” [original data].
Source: WHO Mortality Database (2024) – with minor processing by Our World In Data

### What you should know about this data
* The International Classification of Diseases (Version 10) codes that define skin diseases are L00-L98.

### Source

#### WHO Mortality Database
Retrieved on: 2024-07-26  
Retrieved from: https://platform.who.int/mortality  


## Unintentional injuries
Share of total reported deaths in both sexes in those aged all ages that are from unintentional injuries.
Last updated: July 26, 2024  
Next update: July 2025  
Date range: 1950–2022  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
WHO Mortality Database (2024) – with minor processing by Our World in Data

#### Full citation
WHO Mortality Database (2024) – with minor processing by Our World in Data. “Unintentional injuries” [dataset]. WHO Mortality Database, “WHO Mortality Database” [original data].
Source: WHO Mortality Database (2024) – with minor processing by Our World In Data

### What you should know about this data
* The International Classification of Diseases (Version 10) codes that define unintentional injuries are V01-X59, Y40-Y86, Y88, Y89 (minus X41-X42, X44-X45), U12.9.

### Source

#### WHO Mortality Database
Retrieved on: 2024-07-26  
Retrieved from: https://platform.who.int/mortality  


    