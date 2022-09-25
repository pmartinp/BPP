import pandas as pd

try:
    # Indicamos que el separador será la tabulación con \t
    df = pd.read_csv("finanzas2020.csv", sep="\t", header=(0))

    # Comprobamos que el archivo tenga 12 columnas
    if len(df.columns) != 12:
        raise Exception("El número de columnas es incorrecto")

    # Comprobamos que haya contenido para cada mes
    for meses in df:
        if df[meses].dropna(how="all").empty:
            raise Exception("No hay contenido para el mes:", meses)

    # ¿Qué mes se ha gastado más?
    gastoMeses = {}
    for meses in df:
        gasto = 0
        for valor in df[meses]:
            try:
                if valor != "" and int(valor) < 0:
                    gasto += int(valor)
            except Exception as e:
                print("No se ha podido convertir ese dato")
        gastoMeses[meses] = gasto

    mayorGasto = gastoMeses["Enero"]
    mes = "Enero"
    for clave in gastoMeses:
        if mayorGasto > gastoMeses[clave]:
            mayorGasto = gastoMeses[clave]
            mes = clave

    print("\nEl mes que más se ha gastado ha sido:", mes)

    # ¿Qué mes se ha ahorrado más?
    ahorroMeses = {}
    for meses in df:
        ahorro = 0
        for valor in df[meses]:
            try:
                if valor != "":
                    ahorro += int(valor)
            except Exception as e:
                print("No se ha podido convertir ese dato")
        ahorroMeses[meses] = ahorro

    mayorAhorro = ahorroMeses["Enero"]
    mes = "Enero"
    for clave in ahorroMeses:
        if mayorAhorro < ahorroMeses[clave]:
            mayorAhorro = ahorroMeses[clave]
            mes = clave

    print("\nEl mes que más se ha ahorrado ha sido:", mes)

    # ¿Cuál es la media de gastos al año?
    mediaGasto = 0
    for clave in gastoMeses:
        mediaGasto += gastoMeses[clave]

    mediaGasto = mediaGasto/len(gastoMeses.keys())
    print("\nLa media de gastos mensuales es:", mediaGasto)

    # ¿Cuál ha sido el gasto total a lo largo del año?
    gastoTotal = 0
    for clave in gastoMeses:
        gastoTotal += gastoMeses[clave]

    print("\nEl gasto total anual ha sido de:", gastoTotal)

    # ¿Cuáles han sido los ingresos totales a lo largo del año?
    ingresoTotal = 0
    for meses in df:
        for valor in df[meses]:
            try:
                if valor != "" and int(valor) > 0:
                    ingresoTotal += int(valor)
            except Exception as e:
                print("No se ha podido convertir ese dato")

    print("\nEl ingreso total anual ha sido de:", ingresoTotal)
    
except FileNotFoundError:
    print("No existe el archivo indicado")
except Exception as e:
    print("Ha ocurrido el siguiente error", e)
