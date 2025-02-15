import ifcopenshell
import csv

def debug_ifc(ifc_file_path):
    # Carregar o arquivo IFC
    ifc_file = ifcopenshell.open(ifc_file_path)
    
    # Contar tipos de elementos
    class_counts = {}
    for entity in ifc_file:
        entity_type = entity.is_a()
        class_counts[entity_type] = class_counts.get(entity_type, 0) + 1
    
    print("Entidades IFC encontradas:")
    for entity_type, count in sorted(class_counts.items()):
        print(f"{entity_type}: {count} elementos")

def extract_pipe_lengths(ifc_file_path):
    # Carregar o arquivo IFC
    ifc_file = ifcopenshell.open(ifc_file_path)
    
    # Selecionar segmentos de tubo
    pipes = ifc_file.by_type("IfcFlowSegment")
    data = {}
    total_length = 0.0
    
    for pipe in pipes:
        family_name = "Unknown"
        pipe_type = "Unknown"
        length = 0.0
        
        # Tentar obter o tipo do tubo
        for rel in ifc_file.get_inverse(pipe):
            if rel.is_a("IfcRelDefinesByType"):
                type_object = rel.RelatingType
                if type_object:
                    if hasattr(type_object, "Name"):
                        family_name = type_object.Name
                    if hasattr(type_object, "PredefinedType"):
                        pipe_type = type_object.PredefinedType
        
        # Verificar geometria
        shape = pipe.Representation
        if shape:
            for rep in shape.Representations:
                if rep.is_a("IfcShapeRepresentation"):
                    for item in rep.Items:
                        if item.is_a("IfcExtrudedAreaSolid") and hasattr(item, "Depth"):
                            length = item.Depth
        
        total_length += length
        if (family_name, pipe_type) in data:
            data[(family_name, pipe_type)] += length
        else:
            data[(family_name, pipe_type)] = length
    
    # Exportar para CSV
    output_csv = "pipe_lengths.csv"
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Family", "Type", "Total Length (m)"])
        for (family, ptype), length in data.items():
            writer.writerow([family, ptype, round(length, 3)])
    
    print(f"Total de tubos: {len(pipes)}")
    print(f"Comprimento total dos tubos: {round(total_length, 3)} m")
    print(f"Dados exportados para {output_csv}")
    
    return data, total_length

# Exemplo de uso
if __name__ == "__main__":
    ifc_path = "Caminho do seu ifc"  # Substituir pelo caminho real
    
    # Debug para verificar os tipos disponíveis
    debug_ifc(ifc_path)
    
    # Extrair comprimentos dos tubos
    pipe_data, total_length = extract_pipe_lengths(ifc_path)
    for (family, ptype), length in pipe_data.items():
        print(f"Família: {family}, Tipo: {ptype}, Comprimento Total: {round(length, 3)} m")
