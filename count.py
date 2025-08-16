import os
import pandas as pd

carpetas_a_inspeccionar = [
    r"C:\Users\rocio\Documentos\Facultad\Canasta básica\CBTE\data\supermercados\disco",
    r"C:\Users\rocio\Documentos\Facultad\Canasta básica\CBTE\data\supermercados\vea",
    r"C:\Users\rocio\Documentos\Facultad\Canasta básica\CBTE\data\supermercados\carrefour"
]

detalle = []
resumen = []

for carpeta_base in carpetas_a_inspeccionar:
    for root, dirs, files in os.walk(carpeta_base):
        
        if files:  # Solo si hay excels en la carpeta
            # Agregar al resumen
            resumen.append({
                "Carpeta Base": carpeta_base,
                "Carpeta": root,
                "Total excels": len(files)
            })
            
            # Agregar detalle por archivo
            for excel_file in files:
                file_path = os.path.join(root, excel_file)
                try:
                    df = pd.read_excel(file_path)
                    num_filas = len(df)
                except Exception as e:
                    num_filas = f"Error: {e}"
                
                detalle.append({
                    "Carpeta Base": carpeta_base,
                    "Carpeta": root,
                    "Archivo": excel_file,
                    "Cantidad de filas": num_filas
                })

# Pasar a DataFrames
df_detalle = pd.DataFrame(detalle)
df_resumen = pd.DataFrame(resumen)

# Guardar ambos en un solo Excel con 2 hojas

output_file = r"C:\Users\rocio\Documentos\Facultad\Canasta básica\CBTE\chequeos.xlsx"
with pd.ExcelWriter(output_file) as writer:
    df_resumen.to_excel(writer, index=False, sheet_name="Resumen por carpeta")
    df_detalle.to_excel(writer, index=False, sheet_name="Detalle archivos")

print(f"✅ Resumen generado en: {output_file}")

