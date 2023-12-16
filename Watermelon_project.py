import numpy as np
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import plotly. express as px


st.title("WORLD HAPPINESS REPORT")
st.write("## Kelompok Watermelon")
st.write("""
##### Nama Anggota:
###### Diah Ayu Mailadani (021002204001)
###### Chika Aisyah Putri Setianto (021002204002)
###### Chika Ristysuatantri (021002201017)
""")


st.write( "PENDAHULUAN" )
st.write("""Happiness Index, atau yang dikenal juga sebagai World Happiness Report, adalah sebuah laporan tahunan yang diterbitkan oleh Perserikatan Bangsa-Bangsa (PBB) yang mengukur tingkat kebahagiaan di berbagai negara di dunia.  Laporan ini pertama kali diterbitkan pada tahun 2012 dan mengevaluasi faktor-faktor yang berkontribusi terhadap kebahagiaan masyarakat.

World Happiness Report menggunakan sejumlah indikator dan variabel untuk menilai kebahagiaan di suatu negara. Beberapa faktor yang umumnya diperhitungkan dalam indeks ini antara lain: GDP per capita, Social support (Dukungan sosial, Healthy life expectancy (Harapan Hidup Sehat), Freedom to make life choices (Kebebasan untuk memilih), Generosity (Kemurahan Hati), dan Perceptions of corruption (Persepsi terhadap Korupsi).

Data-data ini dikumpulkan melalui survei yang dilakukan kepada warga negara di berbagai negara. Setiap faktor diberi bobot tertentu dan dihitung untuk memberikan skor akhir yang mencerminkan tingkat kebahagiaan suatu negara.Laporan ini memberikan wawasan tentang kualitas hidup dan kesejahteraan masyarakat di seluruh dunia.
""")
    
#df = pd.read_csv('data 2019.csv)
st.text ("Data Happiness Index Report 2019" )
df=pd.read_csv('data/2019.csv')
df

#Visual data untuk 5 negara dengan ranking tertinggi
Highest_Ranking = st.write("## Top 5 Negara dengan Skor Tertinggi")
st.write( df.head(5) )
st.write ("Lima negara dengan peringkat teratas skor Happiness Index tahun 2019. PDB per kapita lebih tinggi dari rata-rata (0,905147) dan di atas 75% sebaran sampel. Angka harapan hidup sehat berada di atas rata-rata (0,725244) dan di atas 75% sampel di 5 negara teratas. Dukungan sosial, kebebasan memilih dan persepsi korupsi juga berada di atas rata-rata dan di atas 75% sampel (yang merupakan data yang menarik). Kedermawanan juga berada di atas 75% sampel, kecuali Finlandia (peringkat pertama) yang kemurahan hatinya berada di bawah rata-rata.")

st.write ( df.describe())
st.write("""Deskripsi data umum
Skor kebahagiaan: 
1) Rata-rata di 156 negara adalah 5,4 pada skala 0 hingga 10. Nilai minimumnya adalah 2,85 Nilai maksimumnya adalah 7,76.
2) PDB per kapita: Rata-rata adalah 0,905147 GPD per kapita. Kelompok 25% yang berpendapatan lebih rendah kurang dari 0,602750 GPD per kapita. Kelompok 75% yang berpendapatan lebih tinggi mempunyai lebih dari 1,232500 GPD per kapita.
3) Angka Harapan Hidup Sehat Rata-rata angka harapan hidup adalah 0,725244. 25% terbawah berada di bawah 0,547750 angka harapan hidup, 75% tertinggi berada di atas 0,881750 angka harapan hidup.""")

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

factors = {'Overall rank', 'Country or region','Score', 'GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption'}

# Multiselect for choosing the attribute
selected_factors = st.multiselect('Pilih faktor', factors, default=['Score'])

# Check if an factors is selected
if selected_factors:
    # Display a bar chart based on the selected attributes
    fig = px.bar(df, x='Country or region', y=selected_factors, title=f'Bar Chart for {", ".join(selected_factors)}')
    st.plotly_chart(fig)
else:
    st.warning('Pilih setidaknya satu faktor.')
income=df['GDP per capita'].values
income
life_expectancy=df['Healthy life expectancy'].values
life_expectancy

# Check if an attribute is selected
x=income
y=life_expectancy
plt.scatter(x,y, color='yellow')
plt.xlabel('GDP per capita')
plt.ylabel('Healthy life expectancy')
plt.show()