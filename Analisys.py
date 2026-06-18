import pandas as pd 
import matplotlib.pyplot as plt

print("Cargando el dataset...")
df = pd.read_csv('DataAnalyst.csv')

df = df[df['Rating'] != -1]
df = df[df['Salary Estimate'] != '-1']

def limpiar_salario(texto_salario):
    try:
        salario_limpio = texto_salario.split('(')[0].strip()
        salario_limpio = salario_limpio.replace('$','').replace('K', '')
        partes = salario_limpio.split('-')

        min_sal = float(parts[0]) if 'parts' in locals() else float(partes[0])
        max_sal = float(partes[1])

        return ( min_sal + max_sal) / 2
    except:
        return None

df["Salario_Promedio_K"] = df['Salary Estimate'].apply(limpiar_salario)
df = df.dropna(subset=['Salario_Promedio_K'])

rangos = [1, 2, 3, 4, 5]
etiquetas = ['1-2 (Baja)', '2-3 (Regular)', '3-4 (Buena)', '4-5(Excelente)']
df['Rango_Calificación'] = pd.cut(df['Rating'], bins=rangos, labels=etiquetas, include_lowest=True)

analisis_agrupado = df.groupby('Rango_Calificación', observed=False)["Salario_Promedio_K"].mean().reset_index()

print("\n--- Resultados del Análisis ---")
print(analisis_agrupado)

print("\nGenerando gráfico...")
plt.figure(figsize=(9, 5))

barras = plt.bar(analisis_agrupado['Rango_Calificación'],
                 analisis_agrupado['Salario_Promedio_K'],
                 color='#3498db', edgecolor='black', alpha=0.8)

for barra in barras:
    yval = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2, yval + 1, f"${yval:.1f}K", ha="center", va="bottom", fontsize=10, weight='bold')

plt.title('¿Las empresas mejor calificadas pagan más?\n(Salario Promedio Anual vs Calificación de Empresas)', fontsize=13, weight='bold', pad=15)
plt.xlabel('Calificación de la Empresa (Rating)', fontsize=11, labelpad=10)
plt.ylabel('Salario Promedio Estimado (en Miles en USD)', fontsize=11, labelpad=10)
plt.ylim(0, 90)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('rating vs salario.png', dpi=300)
print("¡Grafico guardado con exito como 'rating vs salario.png'!")