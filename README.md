# README - Script de Transformação de Geometria Raster

Este script em Python utiliza as bibliotecas `rasterio`, `shapely`, e `pyproj` para realizar a transformação de uma geometria em um raster e calcular o comprimento de linhas antes e depois da transformação de coordenadas.

## Pré-requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

- `rasterio`
- `shapely`
- `pyproj`

Você pode instalar estas dependências utilizando pip:

```bash
pip install rasterio shapely pyproj
```

## Descrição

O script realiza as seguintes operações:

1. **Abre o arquivo raster**: Utiliza `rasterio` para abrir um arquivo TIFF raster e obtém suas dimensões e limites.
2. **Define os pontos de limite**: Calcula os pontos de limite do raster para criar uma geometria `LineString`.
3. **Define sistemas de referência**: Estabelece o sistema de referência original (WGS 84) e o sistema de referência de destino (exemplo fictício).
4. **Transforma a geometria**: Converte as coordenadas da `LineString` original para o sistema de referência de destino utilizando `pyproj`.
5. **Calcula comprimentos**: Calcula e exibe o comprimento da linha original e da linha transformada.

## Código

```python
import rasterio
from shapely.geometry import LineString, Point
from shapely.ops import transform
from shapely.wkt import loads as wkt_loads
import pyproj

# Abre o arquivo raster
caminho_raster = 'C:\\Users\\RibeiroF\\Downloads\\2010_pr.tif'
with rasterio.open(caminho_raster) as raster:
    
    # Obtém as dimensões do raster
    x_size = raster.res[0]
    y_size = raster.res[1]

    bounds = raster.bounds

    # Define os pontos de limite do raster
    p1 = Point(bounds.left, bounds.top)
    p2 = Point(bounds.left, bounds.top - y_size)
    p3 = Point(bounds.left + x_size, bounds.top - y_size)
    p4 = Point(bounds.left + x_size, bounds.top)

    # Cria a geometria LineString
    line = LineString([p1, p2])

    # Define o sistema de referência original (WGS 84)
    src_srid = 4326

    # Define o sistema de referência de destino (exemplo fictício)
    dst_srid = 5880

    # Cria o transformador para converter as coordenadas
    conversor = pyproj.Transformer.from_crs(src_srid, dst_srid, always_xy=True)

    # Função de transformação
    def transform_geometry(geom):
        return transform(conversor.transform, geom)

    # Aplica a transformação à geometria LineString
    line_transformed = transform_geometry(line)

    # Mostra a geometria transformada
    print(line_transformed)

    # Calcula o comprimento da linha original e da linha transformada
    print("Comprimento da linha original:", line.length)
    print("Comprimento da linha transformada:", line_transformed.length)
```

## Como Usar

1. Substitua o caminho do arquivo raster em `caminho_raster` pelo caminho do seu arquivo TIFF raster.
2. Ajuste os sistemas de referência (`src_srid` e `dst_srid`) conforme necessário.
3. Execute o script para visualizar a geometria transformada e o comprimento das linhas.

## Notas

- O sistema de referência de destino (`dst_srid`) deve ser alterado para um código SRID válido de acordo com o sistema desejado.
- A transformação pode não ser exata se os sistemas de referência forem muito diferentes.
