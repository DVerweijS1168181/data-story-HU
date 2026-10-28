import streamlit as st
import pandas as pd
from operator import index
from geopy.geocoders import Nominatim
import plotly.express as px
import altair as alt   #version 4.2.0
from codeviewer import app as code_viewer
from notebookcode import app as notebook_code_page

# import dataframes
# df_death_cause_per_country = pd.read_csv('/HU/Streamlit_HeartAttack/Data/deaths_cause/death_cause_per_country_bar_chart.csv')
df_deaths_cause = pd.read_csv(
	'HU/Streamlit_HeartAttack/Data/deaths_cause/share-of-deaths-from-major-causes.csv')

df_deaths_cause_per_type = pd.read_csv(
	'HU/Streamlit_HeartAttack/Data/deaths_cardiovascular_types/deaths-from-cardiovascular-disease-type.csv')

df_ischaemic_heart_disease = pd.read_csv(
	"HU/Streamlit_HeartAttack/Data/Ischaemic_heart_disease/death_rate_ischaemic_heart_disease_percentage.csv")

df_deaths_cause_by_gender_cardiovascular = (
	pd.read_csv("HU/Streamlit_HeartAttack/Data/deaths_cardiovascular_gender/df_deaths_cause_by_gender_cardiovascular.csv"))

# Page settings
st.set_page_config(layout="wide")

# Sidebar navigation
page = st.sidebar.selectbox(
    "Choose a page:",
    # ["Home", "View Source Code", "View Data Preparation"]
    ["Home", "View Source Code"]
)

if page == "Home":
	left_column, middle_column, right_column = st.columns([1, 3, 1])
	with middle_column:
		st.title('The cause of Cardiovascular diseases :broken_heart:')
		st.markdown(':grey[Created by Daan Verweij]')

		st.markdown("""___""")

		## ------------------------------------------------------------------------------------- ##

	left_column_1, middle_column_1, right_column_1 = st.columns([1, 2, 2])

	with middle_column_1:
		st.header('1. Introduction')
		st.text('Cardiovascular diseases (CVD) are a global health challenge and '
				'the leading cause of death worldwide. They encompass a range of '
				'conditions affecting the heart and blood vessels, driven by a '
				'combination of lifestyle, environmental, and genetic factors. '
				'This data story delves into the various types of cardiovascular '
				'diseases, their prevalence, and the disparities in diagnosis and '
				'treatment, especially between men and women. By gaining a better '
				'understanding of these conditions, we can identify key areas for '
				'action and work towards reducing the global impact of cardiovascular '
				'diseases.')

	with right_column_1:
		st.image('HU/Streamlit_HeartAttack/images/pngtree-cardiac-clipart-illustration-of-a-human-heart-with-various-objects-around-vector-png-image_6800894.png')

	st.markdown("""___""")

	## ------------------------------------------------------------------------------------- ##
	# https://ourworldindata.org/grapher/share-of-deaths-from-major-causes?v=1&csvType=full&useColumnShortNames=false

	left_column_2, middle_column_2, right_column_2 = st.columns([1, 3, 1])

	# Explanation to terms and legenda
	with left_column_2:
		st.markdown("<p style='padding-top:3%'></p>", unsafe_allow_html=True)
		if st.checkbox("Show terms"):
			st.markdown("**Terms:**")
			with st.expander("Digestive diseases"):
				st.text(
					"Common digestive disorders include gastroesophageal reflux disease, cancer, irritable bowel syndrome, lactose intolerance and hiatal hernia. The most common symptoms of digestive disorders include bleeding, bloating, constipation, diarrhea, heartburn, pain, nausea and vomiting.")
				st.markdown(
					"<a href='https://www.hopkinsmedicine.org/health/wellness-and-prevention/digestive-disorders#:~:text=Common%20digestive%20disorders%20include%20gastroesophageal,%2C%20pain%2C%20nausea%20and%20vomiting.'>:grey[*Source*]",
					unsafe_allow_html=True)
			with st.expander("Infectious and parasitic diseases"):
				st.text(
					"This category includes a wide range of communicable diseases, including sexually transmitted diseases including HIV/AIDS, tuberculosis, diarrheal diseases, some vaccine-preventable diseases such as measles and diseases caused by tropical parasites such as malaria and hookworm.")
				st.markdown(
					"<a href='https://platform.who.int/mortality/themes/theme-details/topics/topic-details/MDB/infectious-and-parasitic-diseases#:~:text=This%20category%20includes%20a%20wide,such%20as%20malaria%20and%20hookworm.'>:grey[*Source*]",
					unsafe_allow_html=True)
			with st.expander("Respiratory diseases"):
				st.text(
					"Chronic respiratory diseases (CRDs) affect the airways and other structures of the lungs. Some of the most common are chronic obstructive pulmonary disease (COPD), asthma, occupational lung diseases and pulmonary hypertension. In addition to tobacco smoke, other risk factors include air pollution, occupational chemicals and dusts and frequent lower respiratory infections during childhood.")
				st.markdown(
					"<a href='https://www.who.int/health-topics/chronic-respiratory-diseases#tab=tab_1'>:grey[*Source*]",
					unsafe_allow_html=True)
			with st.expander("Diabetes mellitus"):
				st.text(
					"Diabetes (also called diabetes mellitus or diabetes) is a disease in which you have too much glucose (sugar) in your blood. Diabetes mellitus occurs either because your body has become less sensitive to insulin or because your body makes too little insulin. The main long-term complications of diabetes are problems with the large blood vessels (in heart, brain and legs) and the small blood vessels (in eyes, kidneys and nerves).")
				st.markdown("<a href='https://www.umcutrecht.nl/nl/ziekte/diabetes?lang=en'>:grey[*Source*]",
							unsafe_allow_html=True)
			with st.expander("Blood and endocrine disorders"):
				st.text(
					"The hormonal system, also called the endocrine system, is a network of glands and organs that make hormones. Sometimes, the body may make too many or too few hormones, or it might stop responding properly to them. This can result in endocrine disorders and diseases")
				st.markdown("<a href='https://www.healthdirect.gov.au/endocrine-disorders-and-diseases'>:grey[*Source*]",
							unsafe_allow_html=True)
			with st.expander("Perinatal conditions"):
				st.text(
					"Perinatal conditions arise during the perinatal period, which spans from 22 completed weeks of gestation and ends 7 completed days after birth. Leading perinatal conditions include birth trauma and consequences of preterm birth. Although most deaths in this category occur during the perinatal period, a few deaths that are caused by perinatal conditions occur later in life.")
				st.markdown(
					"<a href='https://platform.who.int/mortality/themes/theme-details/topics/topic-details/MDB/perinatal-conditions#:~:text=Perinatal%20conditions%20arise%20during%20the,and%20consequences%20of%20preterm%20birth.'>:grey[*Source*]",
					unsafe_allow_html=True)
			with st.expander("Respiratory infections"):
				st.text(
					"A respiratory infection is an inflammation of the mucous membranes in your respiratory system (nose, mouth and airways) caused by a virus or bacteria. The air you breathe can contain all sorts of pathogens, including viruses and bacteria – such as Legionella or pneumococci bacteria")
				st.markdown("<a href='https://www.rivm.nl/en/respiratory-infections'>:grey[*Source*]",
							unsafe_allow_html=True)
			with st.expander("Neuropsychiatric conditions"):
				st.text(
					"For the most part, neuropsychiatric conditions rarely lead to death. However, many deaths are caused by the use of psychoactive substances, namely drugs or alcohol.")
				st.markdown(
					"<a href='https://platform.who.int/mortality/themes/theme-details/topics/topic-details/MDB/neuropsychiatric-conditions'>:grey[*Source*]",
					unsafe_allow_html=True)
			with st.expander("Malignant neoplasms"):
				st.text(
					"Malignant neoplasms are cancerous tumors. They develop when cells grow and divide more than they should. Malignant neoplasms can spread to nearby tissues and to distant parts of your body.")
				st.markdown(
					"<a href='https://my.clevelandclinic.org/health/diseases/22319-malignant-neoplasm'>:grey[*Source*]",
					unsafe_allow_html=True)
			with st.expander("Cardiovascular diseases"):
				st.text(
					"Cardiovascular disease (CVD) is a general term for conditions affecting the heart or blood vessels. It's usually associated with a build-up of fatty deposits inside the arteries (atherosclerosis) and an increased risk of blood clots.")
				st.markdown(
					"<a href='https://www.nhs.uk/conditions/cardiovascular-disease/#:~:text=Cardiovascular%20disease%20(CVD)%20is%20a,increased%20risk%20of%20blood%20clots.'>:grey[*Source*]",
					unsafe_allow_html=True)
			with st.expander("Ill-defined injuries"):
				st.text(
					"Ill-defined diseases include symptoms, signs, abnormal results of clinical or other investigative procedures and ill-defined conditions regarding which no diagnosis classifiable elsewhere is recorded.")
				st.markdown(
					"<a href='https://platform.who.int/mortality/themes/theme-details/MDB/ill-defined-diseases#:~:text=Ill%2Ddefined%20diseases%20include%20symptoms,an%20indicator%20of%20data%20quality.'>:grey[*Source*]",
					unsafe_allow_html=True)
			with st.expander("Musculoskeletal diseases"):
				st.text(
					"Musculoskeletal conditions make up a group of more than 150 diseases and conditions that affect the muscles, joints, bones and connective tissues of the body. Musculoskeletal conditions can affect broad areas, such as the neck or back, or even produce pain throughout the body.2")
				st.markdown(
					"<a href='https://www.pfizer.com/disease-and-conditions/musculoskeletal-conditions'>:grey[*Source*]",
					unsafe_allow_html=True)
			with st.expander("Congenital anomalies"):
				st.text(
					"Congenital anomalies are conditions or differences in health, development or genetics that occur when a baby doesn't develop as expected before birth. Anomalies may also be known as birth defects, genetic conditions, or fetal abnormalities.")
				st.markdown(
					"<a href='https://www.betterhealth.vic.gov.au/health/conditionsandtreatments/congenital-anomalies#:~:text=Congenital%20anomalies%20are%20conditions%20or,genetic%20conditions%2C%20or%20fetal%20abnormalities.'>:grey[*Source*]",
					unsafe_allow_html=True)
			with st.expander("Maternal conditions"):
				st.text(
					"Maternal deaths comprise deaths of women who are pregnant or within 42 days of the termination of the pregnancy, from any cause related to or aggravated by the pregnancy or its management (other than unintentional injuries or incidental causes).")
				st.markdown(
					"<a href='https://platform.who.int/mortality/themes/theme-details/topics/topic-details/MDB/maternal-conditions'>:grey[*Source*]",
					unsafe_allow_html=True)
			with st.expander("Nutritional deficiencies"):
				st.text(
					"Nutritional inadequacy” involves an intake of nutrients that is lower than the estimated average requirement, whereas “nutritional deficiency” consists of severely reduced levels of one or more nutrients, making the body unable to normally perform its functions and thus leading to an increased risk of several diseases.")
				st.markdown(
					"<a href='https://pmc.ncbi.nlm.nih.gov/articles/PMC9710417/#:~:text=%E2%80%9CNutritional%20inadequacy%E2%80%9D%20involves%20an%20intake,increased%20risk%20of%20several%20diseases'>:grey[*Source*]",
					unsafe_allow_html=True)
			with st.expander("Other neoplasms"):
				st.text(
					"Other neoplasms include in-situ tumors, tumors that are benign and tumors for which there is uncertainty whether they are malignant or benign.")
				st.markdown(
					"<a href='https://platform.who.int/mortality/themes/theme-details/topics/topic-details/MDB/other-neoplasms#:~:text=Other%20neoplasms%20include%20in%2Dsitu,they%20are%20malignant%20or%20benign.'>:grey[*Source*]",
					unsafe_allow_html=True)
			with st.expander("Skin diseases"):
				st.text(
					"Skin diseases are conditions that affect your skin. These diseases may cause rashes, inflammation, itchiness or other skin changes. Some skin conditions may be genetic, while lifestyle factors may cause others. Skin disease treatment may include medications, creams or ointments, or lifestyle changes.")
				st.markdown("<a href='https://my.clevelandclinic.org/health/diseases/21573-skin-diseases'>:grey[*Source*]",
							unsafe_allow_html=True)

			st.markdown(
				"<a href='https://ourworldindata.org/grapher/share-of-deaths-from-major-causes?v=1&csvType=full&useColumnShortNames=false'>:grey[*Source*]",
				unsafe_allow_html=True)

	with middle_column_2:
		st.header('2. Causes of deaths')

		# Dropdown selectbox with countries
		selected_entity = st.selectbox("Select a country:", df_deaths_cause["Entity"].unique())

		# Select correct data based on selected country
		selected_data_country = df_deaths_cause[df_deaths_cause["Entity"] == selected_entity]

		# Exclude non-relevant columns
		columns_to_exclude = ["Entity", "Code"]
		filtered_data = selected_data_country.drop(columns=columns_to_exclude)

		# When World wide is selected
		if selected_entity == "World Wide":
			# variable for message
			show_values_message = 70

			# Show lower year because incomplete data in some countries
			filtered_data = filtered_data[filtered_data["Year"] <= 2019]

			# Remove low values to make graph more clear
			filtered_data = filtered_data.loc[:, filtered_data.mean() >= 70]
		else:
			# variable for message
			show_values_message = 1

			# Remove low values to make graph more clear
			filtered_data = filtered_data.loc[:, filtered_data.mean() >= 1]

		# Set year as index
		filtered_data = filtered_data.set_index("Year")

		# Remove "," from year
		filtered_data.index = pd.to_datetime(filtered_data.index.astype(str), format="%Y")

		# Show subheader with title and start/end year & message
		st.subheader(
			fr'Cause of death, {selected_entity}, {filtered_data.iloc[0].name.year} - {filtered_data.iloc[-1].name.year}.')
		st.caption(f":blue-background[Shows diseases with average deaths {show_values_message}% or higher.]")

		# Use st.line_chart() to plot data
		st.line_chart(filtered_data.round(2), x_label="Year", y_label="Deaths (%)", use_container_width=True)

		peak_year = filtered_data['cardiovascular diseases'].idxmax()

		st.markdown(
			"<a href='https://ourworldindata.org/grapher/share-of-deaths-from-major-causes?v=1&csvType=full&useColumnShortNames=false'>:grey[*Source data*]",
			unsafe_allow_html=True)

		st.markdown(f"This graph offers a historical perspective on the leading causes of death in {selected_entity} between "
					f"{filtered_data.iloc[0].name.year} and {filtered_data.iloc[-1].name.year}. "
					"It showcases how different causes have evolved in their contribution to global mortality rates over nearly "
					'seven decades. The most striking trend in the graph is the dominance of cardiovascular diseases. They '
					f"consistently remain the highest cause of death globally, peaking around **{peak_year.year}**. \n\n")

		st.text("But what are cardiovascular diseases exactly? Cardiovascular disease (CVD) is a general term for conditions "
				"affecting the heart or blood vessels. It's usually associated with a build-up of fatty deposits inside the "
				"arteries (atherosclerosis) and an increased risk of blood clots.")

		st.markdown("The most important behavioural risk factors of heart disease and stroke are unhealthy diet, physical inactivity, "
					"tobacco use and harmful use of alcohol. Amongst environmental risk factors, air pollution is an important factor. "
					"The effects of behavioural risk factors may show up in individuals as raised blood pressure, raised blood glucose, "
					"raised blood lipids and overweight and obesity. "
					"<a href='https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-%28cvds%29'>:grey[*Source*]",
					unsafe_allow_html=True)

		if filtered_data.iloc[-1].name.year < 2019 or selected_entity == "World Wide":
			st.markdown("*It's important to note that some years of data are missing in this dataset. While the trends and "
						"patterns are still insightful, these gaps may slightly affect the completeness of the analysis. "
						"Please take this into account when interpreting the results.*")

		st.markdown("""___""")

	## ------------------------------------------------------------------------------------- ##
	# https://www.who.int/data/gho/data/indicators/indicator-details/GHO/number-of-deaths-attributed-to-non-communicable-diseases-by-type-of-disease-and-sex

		st.header('3. Cardiovascular diseases between gender')

		# Dropdown selectbox with countries
		selected_entity = st.selectbox("Select a country:", df_deaths_cause_by_gender_cardiovascular["Location"].unique())

		# Select correct data based on selected country
		selected_data_country = df_deaths_cause_by_gender_cardiovascular[df_deaths_cause_by_gender_cardiovascular["Location"] == selected_entity]

		# Filter data for selected country and remove 'Both sexes'
		df_selected = df_deaths_cause_by_gender_cardiovascular[(df_deaths_cause_by_gender_cardiovascular["Location"] == selected_entity) & (df_deaths_cause_by_gender_cardiovascular["Dim1"].isin(["Female", "Male"]))]

		df_long = df_selected.rename(columns={"Period": "Year", "Dim1": "Gender", "FactValueNumeric": "Mortality rates"})

		# Create the Altair chart
		chart = (
			alt.Chart(df_long)
			.mark_bar()
			.encode(
				x=alt.X("Year:O", title="Year", sort="ascending"),
				y=alt.Y("Mortality rates:Q", title="Mortality rates"),
				color=alt.Color("Gender:N", scale=alt.Scale(domain=["Male", "Female"], range=["blue", "purple"])),
				tooltip=["Year", "Gender", "Mortality rates"]
			)
			.properties(title="Mortality rates between males and females", width=800)
		)

		# Show graph in Streamlit
		st.altair_chart(chart, use_container_width=True)

		st.markdown("<a href='https://www.who.int/data/gho/data/indicators/indicator-details/GHO/number-of-deaths-attributed-to-non-communicable-diseases-by-type-of-disease-and-sex'>:grey[*Source data*]",
			unsafe_allow_html=True)

		st.markdown('A comparison of death rates from cardiovascular diseases (CVD) between men and women reveals an '
					'unexpected result: the rates are nearly identical. However, research highlights that women '
					'frequently face disparities in diagnosis, treatment and care for CVD. This persistent inequality '
					'raises an important question: **Why do these gaps exist and what can be done to address them '
					'effectively?** \n\n')

		st.text('One big reason is that women don’t always show the same symptoms as men. Instead of the usual chest '
				'pain, women might feel tired, nauseous, or short of breath. These differences can lead to doctors '
				'missing the signs of a heart problem. Women also have unique risks for CVD, like complications during '
				'pregnancy, early menopause, or autoimmune diseases, which don’t always get the attention they should. \n\n')

		st.text('When it comes to treatment, women often face challenges too. They are less likely to get aggressive '
				'care or be referred to specialists. Even medications can affect women differently, leading to more '
				'side effects. On top of that, many women put their own health last, focusing on their families instead.')

		st.markdown('To address these issues, the research recommends taking action across every stage of a woman’s '
					'life. This includes creating environments that encourage healthy behaviors for young women, '
					'improving awareness and monitoring of heart health during and after pregnancy, launching prevention '
					'programs for women in midlife and managing health risks in elderly women. Special focus is needed '
					'on addressing inequalities among women in lower socioeconomic groups and those from ethnic minorities. '
					'By tackling these gaps, better outcomes can be achieved for women with CVD. '
					'<a href="https://www.nature.com/articles/s44294-024-00040-0">:grey[*Source data*]',
					unsafe_allow_html=True)

		st.markdown("""___""")

	## ------------------------------------------------------------------------------------- ##
	# https://ourworldindata.org/grapher/deaths-from-cardiovascular-disease-type

	left_column_3, middle_column_3, right_column_3 = st.columns([1, 3, 1])

	# Explanation to terms and legenda
	with left_column_3:
		st.markdown("<p style='padding-top:3%'></p>", unsafe_allow_html=True)
		if st.checkbox("Show Terms"):
			st.markdown("**Terms:**")
			with st.expander("Ischemic heart disease"):
				st.write(
					"Ischaemic heart disease, which is also known as coronary artery disease, develops when there is a blockage of blood flow to the heart, often due to atherosclerosis.")
			with st.expander("Hemorrhagic stroke"):
				st.write(
					"Hemorrhagic stroke is when blood supply to the brain is reduced by bleeding, when a blood vessel tears or breaks. The leaked blood puts pressure on brain cells and damages them.")
			with st.expander("Ischemic stroke"):
				st.write(
					"Ischemic stroke is when blood supply to the brain, spinal cord or retina is reduced or blocked by a clot. This includes clots that developed in the brain’s arteries, or clots that traveled to the brain from other parts of the body.")
			with st.expander("Hypertensive heart diseases"):
				st.write(
					"Hypertensive heart diseases are diseases caused by long-term high blood pressure (‘hypertension’), which puts pressure on the heart. When this happens, the heart’s structure changes – for example, the heart’s muscles thicken – and its ability to pump blood worsens.")
			with st.expander("Cardiomyopathy"):
				st.write(
					"Cardiomyopathies are a range of abnormalities of the heart muscle – for example, conditions that cause them to stretch, thicken or become rigid.")
			with st.expander("Myocarditis"):
				st.write(
					"Myocarditis is a medical condition caused by inflammation of the middle muscles of the heart. It can result from infections, toxins, drugs, autoimmune diseases and other immune conditions.")
			with st.expander("Endocarditis"):
				st.write(
					"Endocarditis is an inflammation of the heart's inner lining. It typically arises from infections – usually by Streptococcus and Staphylococcus bacteria – that can enter the bloodstream and adhere to the heart.")
			with st.expander("Rheumatic heart disease"):
				st.write(
					"Rheumatic heart diseases can develop as a consequence of rheumatic fever. This is caused by untreated Strep throat and scarlet fever infections, from group A Streptococcus bacteria.")
			st.markdown(
				"<a href='https://ourworldindata.org/grapher/deaths-from-cardiovascular-disease-type?time=2021'>:grey[*Source*]",
				unsafe_allow_html=True)

	with middle_column_3:
		st.header('4. Types of cardiovascular diseases')

		selected_entity_types = st.selectbox("Select a country:",
											 df_deaths_cause_per_type["Entity"].unique())

		# Select correct data based on selected country
		selected_data_country_types = df_deaths_cause_per_type[df_deaths_cause_per_type["Entity"] == selected_entity_types]

		# columns_to_exclude = ["Entity", "Code"]
		filtered_data_types = selected_data_country_types.drop(columns=columns_to_exclude)

		# Set year as index
		filtered_data_types = filtered_data_types.set_index("Year")

		# Remove "," from year
		filtered_data_types.index = pd.to_datetime(filtered_data_types.index.astype(str), format="%Y")

		# Show subheader with title and start/end year & message
		st.subheader(
			fr'Types of cardiovascular diseases, {selected_entity_types}, {filtered_data_types.iloc[0].name.year} - {filtered_data_types.iloc[-1].name.year}.')
		# st.caption(f":blue-background[Shows diseases with an average value above {show_values_message}.]")

		latest_year = filtered_data_types.index.max()
		latest_value = filtered_data_types.loc[latest_year, "ischaemic heart disease"].astype(int)

		# max_year_types_value = filtered_data_types.name.year == max_year_types

		# Use st.line_chart() to plot data
		st.line_chart(filtered_data_types.round(2), x_label="Year", y_label="Deaths", use_container_width=True)

		st.markdown(
			"<a href='https://ourworldindata.org/grapher/deaths-from-cardiovascular-disease-type'>:grey[*Source data*]",
			unsafe_allow_html=True)

		st.text(f'An analysis has been conducted to explore the different types of cardiovascular diseases and their '
				'impact on global mortality. By examining trends over time, this analysis sheds light on the '
				'prevalence and severity of various conditions, highlighting which diseases contribute most '
				f'significantly to cardiovascular-related deaths in {selected_entity_types}.')

		st.text('The graph illustrates global death trends from various cardiovascular diseases between '
				f'{filtered_data_types.iloc[0].name.year} and {filtered_data_types.iloc[-1].name.year}. '
				f'Among the conditions, ischaemic heart disease stands out significantly. Its death toll '
				f'has remaint on top throughout the years, reaching {latest_value} deaths by {latest_year.year}. '
				f'This overwhelming dominance highlights its critical role as the leading contributor to '
				f'cardiovascular-related deaths worldwide.')

		st.markdown("But what is ischaemic heart disease exactly? Ischaemic heart disease, which is also known as "
				"coronary artery disease, develops when there is a blockage of blood flow to the heart, often "
				"due to atherosclerosis. <a href='https://ourworldindata.org/grapher/deaths-from-cardiovascular-disease-type'>:grey[*Source*]</a>\n\n "
				"Atherosclerosis can be caused by lifestyle factors, such as smoking and regularly drinking excessive amounts of alcohol. "
					"<a href='https://www.nhs.uk/conditions/coronary-heart-disease/'>:grey[*Source*]</a>", unsafe_allow_html=True)

		st.markdown("""___""")

		## ------------------------------------------------------------------------------------- ##

		# Get coordinates based on country name
		def get_coordinates(country_name):
			geolocator = Nominatim(user_agent="geoapi")
			location = geolocator.geocode(country_name)
			if location:
				return location.latitude, location.longitude
			else:
				return None, None

		st.header(fr'5. Ischaemic heart disease')

		# Get unique years
		ischaemic_year_unique = df_ischaemic_heart_disease['Year'].unique()

		# Create slider with unique years
		ischaemic_heart_disease_select_year = st.slider("Select year:", ischaemic_year_unique[0], ischaemic_year_unique[-1], index(2021))

		# Turn selected value into necessary data
		ischaemic_heart_disease_select_data = df_ischaemic_heart_disease[df_ischaemic_heart_disease['Year'] == ischaemic_heart_disease_select_year]
		st.caption(":blue-background[Mortality rate based on total population.]")

		fig = px.choropleth(
			ischaemic_heart_disease_select_data,
			locations="Entity",
			locationmode="country names",
			color="Death rate percentage",
			title="Mortality rate by ischaemic heart disease per country",
			hover_name='Entity',
			color_continuous_scale="BuPu",
			projection='natural earth',
		)

		# Change background color
		fig.update_layout(geo=dict(bgcolor='rgba(0,0,0,0)'))

		# Add map to Streamlit
		st.plotly_chart(fig)

		st.markdown(
			"<a href='https://data.worldbank.org/indicator/SP.POP.TOTL?most_recent_year_desc=false'>:grey[*Source data one*]</a> :grey[ *and* ] "
			"<a href='https://ourworldindata.org/grapher/deaths-from-cardiovascular-disease-type'>:grey[*Source data two*]</a>",
			unsafe_allow_html=True)

		st.text('In 2021, Ukraine had the highest mortality rate for ischemic heart disease (IHD) among individuals '
				'aged 55 and above, with a staggering 0.64% mortality rate on the total number of citizens. This figure stood out starkly '
				'on the global map, far exceeding the rates in other countries. But what could be driving these '
				'alarming numbers?')

		st.text('A study reveals that several factors are at play. Ukraine faces significant lifestyle and health '
				'challenges, including high rates of smoking, unhealthy dietary habits and limited physical '
				'activity—all of which are key contributors to cardiovascular diseases. Additionally, air pollution '
				'in the region adds to the burden, as it is a major risk factor for heart health. These environmental '
				'and lifestyle risks are compounded by a healthcare system that struggles with limited resources, '
				'making early detection and effective management of IHD difficult.')

		st.text("Socioeconomic conditions also play a critical role. The country's economic instability, combined "
				"with stress from prolonged conflict and displacement, further worsens health outcomes. Stress is "
				"a well-documented risk factor for heart disease and its impact cannot be overlooked in Ukraine's case.")

		st.markdown("This situation highlights the urgent need for comprehensive interventions. The research suggests "
				"improving access to preventive care, encouraging healthier lifestyles through public health "
				"campaigns and addressing environmental factors like air pollution. Strengthening healthcare "
				"infrastructure to provide better screening and management of IHD is also crucial. "
				"<a href='https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-025-22193-6'>:grey[*Source data*]",
				unsafe_allow_html=True)

		st.markdown("""___""")

		## ------------------------------------------------------------------------------------- ##

		st.header(fr'6. Conclusion')

		st.text("Cardiovascular diseases continue to be a leading cause of mortality globally, with "
				"ischaemic heart disease standing out as the most significant contributor. Analyzing "
				"data across various countries and demographics has revealed critical disparities, "
				"particularly in the diagnosis and treatment of women, as well as challenges in specific "
				"regions like Ukraine, where lifestyle, environmental and socioeconomic factors exacerbate "
				"the issue. These findings emphasize the urgent need for comprehensive strategies, ranging "
				"from preventative health measures and education to targeted interventions addressing "
				"disparities and improving healthcare systems. By prioritizing these efforts, it is possible "
				"to reduce the global burden of cardiovascular diseases and improve outcomes for millions of "
				"people worldwide.")

elif page == "View Source Code":
    code_viewer()

# elif page == "View Data Preparation":
#     notebook_code_page()
