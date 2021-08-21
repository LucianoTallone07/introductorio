import pandas as pd
#sea el siguiente panel
data = [["EDN.BA",26.20],["CVH.BA",458.50],["BMA.BA",233.95],["GGAL.BA",126.55]]

df = pd.DataFrame(data)
df

df.columns= ["ticker", "price"]
df= df.set_index("ticker")
df


## como obtener solo los precios?
#df.reset_index(inplace= True)
#df = df.loc[:,["price"]]
#df

#como obtengo el precio de edn.ba?
df.loc["BMA.BA","price"]

#como obtengo la ultima fila?
#df.iloc[-1,:]
