# Análisis de Salarios vs. Calificación de Empresas para Analistas de Datos 📊

Este proyecto realiza un Análisis Exploratorio de Datos (EDA) para comprobar la hipótesis: **¿Existe una relación directa entre la calificación de reputación de una empresa y el salario que ofrece para puestos de Análisis de Datos?**

El objetivo principal es demostrar habilidades técnicas en la manipulación, limpieza y visualización de datos utilizando entornos profesionales como **VS Code**.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3
* **Librerías:** Pandas (Procesamiento y ETL), Matplotlib (Visualización de datos)
* **Entorno de Desarrollo:** VS Code

## 📈 El Proceso de Análisis (ETL & EDA)
El dataset original (`DataAnalyst.csv`) presentaba desafíos reales de calidad de datos que requirieron un proceso de limpieza estructurado:
1. **Tratamiento de nulos:** Se eliminaron los registros donde las calificaciones o las estimaciones salariales estaban ausentes (marcadas con `-1`).
2. **Transformación de Texto a Numérico:** La columna de salarios venía en formato de texto (ej. `"$37K-$66K"`). Se desarrolló una función personalizada en Python para extraer los límites, limpiar caracteres especiales y calcular el **salario promedio numérico** de cada rango.
3. **Segmentación:** Se agruparon las calificaciones en rangos categóricos (`Baja`, `Regular`, `Buena`, `Excelente`) usando `pd.cut` para identificar tendencias con mayor facilidad.

## 📊 Visualización de Resultados

A continuación, se presenta el gráfico generado automáticamente por el script, el cual cruza el salario promedio anual estimado (en miles de USD) con los rangos de calificación de Glassdoor:

![Salario vs Calificación](rating_vs_salario.png)

## 💡 Conclusiones Clave (Insights de Negocio)
* **La hipótesis es parcialmente falsa:** Los datos demuestran que las empresas con calificaciones más bajas (1-2) ofrecen un salario promedio de **$70.1K**, mientras que las empresas excelentes (4-5) ofrecen **$73.4K**.
* **Margen mínimo:** Existe un incremento salarial en las empresas top, pero la diferencia es de apenas **$3.3K anuales (un ~4.6%)**. 
* **Conclusión para el candidato:** Un analista de datos junior no debería descartar ofertas de empresas con calificaciones regulares o bajas basándose únicamente en la expectativa salarial, ya que el mercado compensa de forma muy similar económicamente en este sector.

---
*Proyecto desarrollado por José Paéz. ¡Conéctate conmigo en www.linkedin.com/in/josé-páez-474367417
