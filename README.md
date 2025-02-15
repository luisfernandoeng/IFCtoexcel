Este programa foi desenvolvido para ler arquivos no formato IFC (Industry Foundation Classes) e extrair informações relevantes sobre o comprimento de tubos utilizados em sistemas hidráulicos e eletrodutos para instalações elétricas. O objetivo é facilitar a análise de projetos de engenharia, permitindo que profissionais da área obtenham dados precisos sobre os componentes de tubulação em seus projetos.

O programa possui duas funcionalidades principais:

Extração de Comprimento de Tubos Hidráulicos: Através da função extract_pipe_lengths, o usuário pode obter o comprimento total dos tubos hidráulicos presentes no arquivo IFC. Os dados são organizados por família e tipo de tubo, e exportados para um arquivo CSV.

Extração de Comprimento de Eletrodutos: A função extract_electrical_lengths realiza uma tarefa semelhante, mas focada em segmentos elétricos, como conduítes e bandejas de cabos. Os resultados também são exportados para um arquivo CSV, com formatação adequada para o Brasil.

Ambas as funções incluem uma etapa de depuração (debug_ifc) que permite ao usuário visualizar as entidades IFC encontradas no arquivo, facilitando a identificação de componentes.

##

This program is designed to read files in the IFC (Industry Foundation Classes) format and extract relevant information about the lengths of pipes used in hydraulic systems and conduits for electrical installations. The aim is to facilitate engineering project analysis by allowing professionals in the field to obtain accurate data about the piping components in their designs.

The program has two main functionalities:

Extraction of Hydraulic Pipe Lengths: Through the extract_pipe_lengths function, users can obtain the total length of hydraulic pipes present in the IFC file. The data is organized by family and type of pipe and exported to a CSV file.

Extraction of Electrical Conduit Lengths: The extract_electrical_lengths function performs a similar task but focuses on electrical segments, such as conduits and cable trays. The results are also exported to a CSV file, formatted appropriately for Brazil.

Both functions include a debugging step (debug_ifc) that allows users to view the IFC entities found in the file, making it easier to identify components.

Esta descrição pode ser utilizada na seção README do seu repositório no GitHub para fornecer uma visão clara e concisa do propósito e funcionamento do seu programa.
