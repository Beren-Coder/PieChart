import matplotlib.pyplot as plt
import numpy as np

y = np.array([20,30,50,60,40])
mylabels = ["Giderler" , "Gelirler" , "Yemek" , "Kira" , "Fatura"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 