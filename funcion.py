def eco_funcion(material: str):
    material = material.lower().strip()

    tipos_papel = ["papel normal", "papel de cuaderno", "papel periódico"]
    tipos_carton = ["cartón corrugado", "papel kraft"]
    tipos_plastico = ["plástico de botella (pet)", "plástico de productos de limpieza y alimentos (pead, pebd, pp)"]
    tipos_vidrio = ["vidrio de botellas de bebidas", "frascos de alimentos y cosméticos"]
    tipos_metal = ["latas de aluminio (cerveza, gaseosa)",
             "latas de conserva (acero)",
             "tapas metálicas y chatarra pequeña"]

    reciclables = {
        "Papel": tipos_papel,
        "Cartón": tipos_carton,
        "Plástico": tipos_plastico,
        "Vidrio": tipos_vidrio,
        "Metal": tipos_metal
    }

    

    for categoria, items in reciclables.items():
        for item in items:
            if material in item.lower():
                resultado = f" El material '{material}' pertenece a la categoría: {categoria}"
            else:
                    resultado = f" El material '{material}' no está en la lista de reciclables"
    return resultado
