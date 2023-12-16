import numpy as np
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import plotly. express as px

st.title("WORLD HAPPINESS REPORT")
st.write("Nama Kelompok Watermelon")
st.write("Diah Ayu Mailadani 021002204001",
         "Chika Aisyah Putri Setianto 021002204002")

st.write("#pendahuluan")
st.write("")
    
#df = pd.read_csv('data 2019.csv)
df=pd.read_csv('data/2019.csv')
df

#Visual data untuk 5 negara dengan ranking tertinggi
Highest_Ranking = st.write("## Top 5 Negara dengan Skor Tertinggi")
st.write( df.head(5) )

plt.bar(df['Country or region'].head(5), df['Score'].head(5))
plt.xlabel('Negara atau Wilayah')
plt.ylabel('Skor')
plt.title('Top 5 Negara dengan Skor Tertinggi')

fig, ax = plt.subplots()
ax.bar(df['Country or region'].head(5), df['Score'].head(5))
ax.set_xlabel('Negara atau Wilayah')
ax.set_ylabel('Skor')
ax.set_title('Top 5 Negara dengan Skor Tertinggi')
st.pyplot(fig)

# Menambahkan kolom 'Wilayah' berdasarkan kelompok wilayah tertentu
region_mapping = {
    'Asia': ['Afghanistan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Timor-Leste', 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen'],
    'Europe': ['Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kazakhstan', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom', 'Vatican City'],
    'North America': ['Antigua and Barbuda', 'Bahamas', 'Barbados', 'Belize', 'Canada', 'Costa Rica', 'Cuba', 'Dominica', 'Dominican Republic', 'El Salvador', 'Grenada', 'Guatemala', 'Haiti', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Trinidad and Tobago', 'United States'],
    'South America': ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela'],
    'Africa': ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Congo (Congo-Brazzaville)', 'Côte d\'Ivoire', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini (fmr. "Swaziland")', 'Ethiopia', 'Gabon','Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Uganda', 'Zambia', 'Zimbabwe'],
    'Oceania': ['Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia', 'Nauru', 'New Zealand', 'Palau', 'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu'],
}
df['Wilayah'] = df['Country or region'].apply(lambda x: next((region for region, countries in region_mapping.items() if x in countries), None))

#membuat multiselect berdasarkan wilayah dan negara
selected_regions = st.multiselect('Pilih Wilayah', list(region_mapping.keys()), key='multiselect_regions')

# Membuat multiselect untuk memilih negara dalam wilayah 'Asia' dengan kunci yang unik
if 'Asia' in selected_regions:
    default_countries_asia = ['Afghanistan', 'Bahrain', 'Bangladesh']  # Sesuaikan nilai default sesuai kebutuhan
    region_mappings_asia = st.multiselect("Pilih Negara atau Wilayah", region_mapping['Asia'], default=default_countries_asia, key='multiselect_countries_asia')
     # Menampilkan judul dan data negara-negara dalam wilayah dan negara yang dipilih
    st.markdown("Data berdasarkan Wilayah dan Negara yang dipilih:")
    st.write(df[(df['Wilayah'].isin(selected_regions)) & (df['Country or region'].isin(region_mappings_asia))])

# Membuat multiselect untuk memilih negara dalam wilayah 'Eropa' dengan kunci yang unik
elif 'Europe' in selected_regions:
    default_countries_europe = ['Albania', 'Andorra', 'Armenia']
    region_mappings_europe = st.multiselect("Pilih Negara atau Wilayah", region_mapping['Europe'], default=default_countries_europe, key='multiselect_countries_europe')
    st.markdown("Data berdasarkan Wilayah dan Negara yang dipilih:")
    st.write(df[(df['Wilayah'].isin(selected_regions)) & (df['Country or region'].isin(region_mappings_europe))])

# Membuat multiselect untuk memilih negara dalam wilayah 'North America' dengan kunci yang unik
elif 'North America' in selected_regions:
    default_countries_north_america = ['Canada', 'United States', 'Mexico']
    region_mappings_north_america = st.multiselect("Pilih Negara atau Wilayah", region_mapping['North America'], default=default_countries_north_america, key='multiselect_countries_north_america')
    st.markdown("Data berdasarkan Wilayah dan Negara yang dipilih:")
    st.write(df[(df['Wilayah'].isin(selected_regions)) & (df['Country or region'].isin(region_mappings_north_america))])

# Membuat multiselect untuk memilih negara dalam wilayah 'South America' dengan kunci yang unik
elif 'South America' in selected_regions:
    default_countries_south_america = ['Brazil', 'Argentina', 'Chile']
    region_mappings_south_america = st.multiselect("Pilih Negara atau Wilayah", region_mapping['South America'], default=default_countries_south_america, key='multiselect_countries_south_america')
    st.markdown("Data berdasarkan Wilayah dan Negara yang dipilih:")
    st.write(df[(df['Wilayah'].isin(selected_regions)) & (df['Country or region'].isin(region_mappings_south_america))])

# Membuat multiselect untuk memilih negara dalam wilayah 'Africa' dengan kunci yang unik
elif 'Africa' in selected_regions:
    default_countries_africa = ['Nigeria', 'South Africa', 'Kenya']  # Sesuaikan nilai default sesuai kebutuhan
    region_mappings_africa = st.multiselect("Pilih Negara atau Wilayah", region_mapping['Africa'], default=default_countries_africa, key='multiselect_countries_africa')
    st.markdown("Data berdasarkan Wilayah dan Negara yang dipilih:")
    st.write(df[(df['Wilayah'].isin(selected_regions)) & (df['Country or region'].isin(region_mappings_africa))])

# Membuat multiselect untuk memilih negara dalam wilayah 'Oceania' dengan kunci yang unik
elif 'Oceania' in selected_regions:
    default_countries_oceania = ['Australia', 'New Zealand', 'Fiji']
    region_mappings_oceania = st.multiselect("Pilih Negara atau Wilayah", region_mapping['Oceania'], default=default_countries_oceania, key='multiselect_countries_oceania')
    st.markdown("Data berdasarkan Wilayah dan Negara yang dipilih:")
    st.write(df[(df['Wilayah'].isin(selected_regions)) & (df['Country or region'].isin(region_mappings_oceania))])

else:
# Menampilkan peringatan jika tidak ada wilayah yang dipilih
    st.warning("Pilih setidaknya satu wilayah.")

# Daftar wilayah dan atribut
region_attributes = {
    'Asia': ['Overall rank', 'Country or region','Score', 'GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption'],
    'Europe': ['Overall rank', 'Country or region','Score', 'GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption'],
    'North America': ['Overall rank', 'Country or region','Score', 'GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption'],
    'South America': ['Overall rank', 'Country or region','Score', 'GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption'],
    'Africa': ['Overall rank', 'Country or region','Score', 'GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption'],
    'Ocenia' : ['Overall rank', 'Country or region','Score', 'GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption'],
}
attribute = {'Overall rank', 'Country or region','Score', 'GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption'}

# Memilih wilayah
# Multiselect for choosing the region
selected_region = st.multiselect('Pilih Wilayah', list(region_attributes.keys()), key='ymultiselect_regions')


if selected_region:
    attributes = st.multiselect(
        "Informasi yang ditampilkan:",
        options=region_attributes[selected_region[0]],  # Select the first region if multiple are selected
        default=[region_attributes[selected_region[0]][0]]  # Default to the first attribute of the selected region
    )

# Menampilkan hasil pemilihan
st.write(f"Anda memilih wilayah: {selected_region}")
st.write(f"Anda memilih atribut: {selected_attributes}")

selected_attribute= st.selectbox("attribute: ", ['Overall rank', 'Country or region','Score', 'GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption',])
st.write("pilihan faktor: ", attribute)

