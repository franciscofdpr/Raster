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

