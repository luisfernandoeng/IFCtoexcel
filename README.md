# 🚰 **IFC to Excel: Extração de Dados de Tubos Hidráulicos e Eletrodutos**

![Python](https://img.shields.io/badge/Python-3.7%20|%203.8%20|%203.9%20|%203.10-blue?logo=python) ![IFC](https://img.shields.io/badge/IFC-Extractor-orange)

> **O IFC to Excel é uma ferramenta Python desenvolvida para extrair informações precisas sobre comprimentos de tubos hidráulicos e eletrodutos de arquivos IFC (Industry Foundation Classes). O objetivo é facilitar a análise de projetos de engenharia, permitindo que profissionais obtenham dados organizados em formato CSV para uso em planilhas Excel.**

---

## 🌟 **Recursos Principais**

✅ **Extração de Comprimento de Tubos Hidráulicos**:  
- Calcula o comprimento total dos tubos hidráulicos presentes no arquivo IFC.  
- Organiza os dados por família e tipo de tubo.  
- Exporta os resultados para um arquivo CSV formatado para o Brasil.

✅ **Extração de Comprimento de Eletrodutos**:  
- Extrai o comprimento de segmentos elétricos, como conduítes e bandejas de cabos.  
- Os dados são exportados para um arquivo CSV com formatação adequada.

✅ **Depuração de Entidades IFC**:  
- A função `debug_ifc` permite visualizar as entidades IFC encontradas no arquivo, facilitando a identificação de componentes.

✅ **Compatível com Ferramentas BIM**:  
- Funciona com arquivos IFC gerados por softwares como Revit, ArchiCAD e outros.

---

## 🛠️ **Como Usar**

### **Pré-requisitos**

1. **Python**: Certifique-se de ter o Python instalado (versão 3.7 ou superior).  
   [Baixe aqui](https://www.python.org/downloads/).

2. **Biblioteca `ifcopenshell`**: Instale a biblioteca usando o pip:
   ```bash
   pip install ifcopenshell
   ```

### **Execução**

1. Clone este repositório:
   ```bash
   git clone https://github.com/luisfernandoeng/IFCtoexcel.git
   cd ifc-to-excel
   ```

2. Execute o script:
   ```python
   python extract_data.py "caminho/do/arquivo.ifc"
   ```

3. Verifique os arquivos CSV gerados (`pipe_lengths.csv` e `electrical_lengths.csv`) no diretório atual.

---

## 📊 **Exemplo de Resultados**

### **Saída CSV para Tubos Hidráulicos**
| **Família**       | **Tipo**          | **Comprimento Total (m)** |
|--------------------|-------------------|---------------------------|
| PVC               | Tubo de 50mm      | 120.500                   |
| Metal             | Tubo de 25mm      | 85.750                    |

### **Saída CSV para Eletrodutos**
| **Família**       | **Tipo**          | **Comprimento Total (m)** |
|--------------------|-------------------|---------------------------|
| Conduíte          | 20mm              | 200.000                   |
| Bandeja de Cabos  | 300x100mm         | 50.250                    |

---

## 🧩 **Funcionalidades Detalhadas**

### **1. Depuração de Entidades IFC**
A função `debug_ifc` lista todas as entidades IFC encontradas no arquivo, ajudando a identificar os tipos de componentes disponíveis. Exemplo de saída:

```
Entidades IFC encontradas:
IfcFlowSegment: 45 elementos
IfcWall: 120 elementos
IfcDoor: 10 elementos
...
```

### **2. Extração de Comprimento de Tubos Hidráulicos**
A função `extract_pipe_lengths` calcula o comprimento total dos tubos hidráulicos e organiza os dados por família e tipo. Exemplo de saída:

```
Total de tubos: 45
Comprimento total dos tubos: 206.250 m
Dados exportados para pipe_lengths.csv
```

### **3. Extração de Comprimento de Eletrodutos**
A função `extract_electrical_lengths` realiza uma tarefa semelhante para segmentos elétricos, como conduítes e bandejas de cabos.

---

## 📝 **Explicação do Código**

O script realiza as seguintes etapas:

1. **Carregamento do Modelo**:  
   Usa a biblioteca `ifcopenshell` para carregar o arquivo IFC.

2. **Identificação de Componentes**:  
   - Para tubos hidráulicos, busca entidades do tipo `IfcFlowSegment`.  
   - Para eletrodutos, busca entidades relacionadas a conduítes e bandejas de cabos.

3. **Cálculo de Comprimentos**:  
   - Extrai a geometria dos componentes (por exemplo, `IfcExtrudedAreaSolid`) para calcular o comprimento.  
   - Agrupa os dados por família e tipo.

4. **Exportação para CSV**:  
   Gera arquivos CSV com os resultados organizados.

---
