import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel(r"C:\Users\xxdho\OneDrive\Desktop\iot-light-temp-dashboard\data\iot final.xlsx")


df = df.rename(columns={
    'Temp (°C)': 'temp',
    'Light (Lux)': 'light_intensity_lux',
    'Blind Status': 'blind_status',
    'Sun Elevation': 'sun_elevation',
    'Timestamp': 'timestamp'
})


print(df.columns)
print(df.head())


print("Missing values per column:")
print(df.isnull().sum())


plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x='light_intensity_lux',
    y='temp',
    hue='blind_status',
    palette='viridis'
)
plt.title('Relationship between Light Intensity and Temperature')
plt.xlabel('Light Intensity (Lux)')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()


plt.figure(figsize=(8, 6))
correlation_matrix = df[['temp', 'light_intensity_lux']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix between Temperature and Light Intensity')
plt.show()
