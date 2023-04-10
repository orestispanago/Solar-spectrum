import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("astmg173.csv", skiprows=1, index_col="Wavelength (nm)")
df.plot()
plt.ylabel("Spectral Irradiance $(W \cdot m^{-2} \cdot nm^{-1})$")
plt.legend(
    [
        "Extraterrestial",
        "Global tilt $37 \degree$",
        "Direct + circumsolar",
    ]
)
plt.savefig("astm_reference_spectra.png")
plt.show()
