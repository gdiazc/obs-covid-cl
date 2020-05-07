URLS = {
    # comunales:
    'p1_casos_acumulados_comuna': 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto1/Covid-19_T.csv',
    #regionales:
    'casos_totales_cumulativo_t': 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/CasosTotalesCumulativo_T.csv',
    'casos_nuevos_cumulativo_t': 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto13/CasosNuevosCumulativo_T.csv',
    'uci_t': 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto8/UCI_T.csv',
    'numero_ventiladores_t': 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto20/NumeroVentiladores_T.csv',
    'pcr_t': 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto7/PCR_T.csv',
    'fallecidos_cumulativo_t': 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto14/FallecidosCumulativo_T.csv',
    'fallecidos_etario_t': 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto10/FallecidosEtario_T.csv',
}

REGIONS_SORTED = [
'Arica y Parinacota',
'Tarapacá',
'Antofagasta',
'Atacama',
'Coquimbo',
'Valparaíso',
'Metropolitana',
'O’Higgins',
'Maule',
'Ñuble',
'Biobío',
'Araucanía',
'Los Ríos',
'Los Lagos',
'Aysén',
'Magallanes',
]

REGIONS_TO_ABBR = {
'Arica y Parinacota': 'AP',
'Tarapacá': 'TA',
'Antofagasta': 'AN',
'Atacama': 'AT',
'Coquimbo': 'CO',
'Valparaíso': 'VA',
'Metropolitana': 'RM',
'O’Higgins': 'OH',
'Maule': 'MA',
'Ñuble': 'NB',
'Biobío': 'BI',
'Araucanía': 'AR',
'Los Ríos': 'LR',
'Los Lagos': 'LL',
'Aysén': 'AI',
'Magallanes': 'MG',
}

COMUNAS_DROPDOWN_OPTIONS = [{'label': 'Reg. Arica y Parinacota',
  'value': 'Arica y Parinacota',
  'disabled': True},
 {'label': '  Arica', 'value': 'Arica'},
 {'label': '  Camarones', 'value': 'Camarones'},
 {'label': '  General Lagos', 'value': 'General Lagos'},
 {'label': '  Putre', 'value': 'Putre'},
 {'label': 'Reg. Tarapacá', 'value': 'Tarapacá', 'disabled': True},
 {'label': '  Alto Hospicio', 'value': 'Alto Hospicio'},
 {'label': '  Camina', 'value': 'Camina'},
 {'label': '  Colchane', 'value': 'Colchane'},
 {'label': '  Huara', 'value': 'Huara'},
 {'label': '  Iquique', 'value': 'Iquique'},
 {'label': '  Pica', 'value': 'Pica'},
 {'label': '  Pozo Almonte', 'value': 'Pozo Almonte'},
 {'label': 'Reg. Antofagasta', 'value': 'Antofagasta', 'disabled': True},
 {'label': '  Antofagasta', 'value': 'Antofagasta'},
 {'label': '  Calama', 'value': 'Calama'},
 {'label': '  Maria Elena', 'value': 'Maria Elena'},
 {'label': '  Mejillones', 'value': 'Mejillones'},
 {'label': '  Ollague', 'value': 'Ollague'},
 {'label': '  San Pedro de Atacama', 'value': 'San Pedro de Atacama'},
 {'label': '  Sierra Gorda', 'value': 'Sierra Gorda'},
 {'label': '  Taltal', 'value': 'Taltal'},
 {'label': '  Tocopilla', 'value': 'Tocopilla'},
 {'label': 'Reg. Atacama', 'value': 'Atacama', 'disabled': True},
 {'label': '  Alto del Carmen', 'value': 'Alto del Carmen'},
 {'label': '  Caldera', 'value': 'Caldera'},
 {'label': '  Chanaral', 'value': 'Chanaral'},
 {'label': '  Copiapo', 'value': 'Copiapo'},
 {'label': '  Diego de Almagro', 'value': 'Diego de Almagro'},
 {'label': '  Freirina', 'value': 'Freirina'},
 {'label': '  Huasco', 'value': 'Huasco'},
 {'label': '  Tierra Amarilla', 'value': 'Tierra Amarilla'},
 {'label': '  Vallenar', 'value': 'Vallenar'},
 {'label': 'Reg. Coquimbo', 'value': 'Coquimbo', 'disabled': True},
 {'label': '  Andacollo', 'value': 'Andacollo'},
 {'label': '  Canela', 'value': 'Canela'},
 {'label': '  Combarbala', 'value': 'Combarbala'},
 {'label': '  Coquimbo', 'value': 'Coquimbo'},
 {'label': '  Illapel', 'value': 'Illapel'},
 {'label': '  La Higuera', 'value': 'La Higuera'},
 {'label': '  La Serena', 'value': 'La Serena'},
 {'label': '  Los Vilos', 'value': 'Los Vilos'},
 {'label': '  Monte Patria', 'value': 'Monte Patria'},
 {'label': '  Ovalle', 'value': 'Ovalle'},
 {'label': '  Paiguano', 'value': 'Paiguano'},
 {'label': '  Punitaqui', 'value': 'Punitaqui'},
 {'label': '  Rio Hurtado', 'value': 'Rio Hurtado'},
 {'label': '  Salamanca', 'value': 'Salamanca'},
 {'label': '  Vicuna', 'value': 'Vicuna'},
 {'label': 'Reg. Valparaíso', 'value': 'Valparaíso', 'disabled': True},
 {'label': '  Algarrobo', 'value': 'Algarrobo'},
 {'label': '  Cabildo', 'value': 'Cabildo'},
 {'label': '  Calera', 'value': 'Calera'},
 {'label': '  Calle Larga', 'value': 'Calle Larga'},
 {'label': '  Cartagena', 'value': 'Cartagena'},
 {'label': '  Casablanca', 'value': 'Casablanca'},
 {'label': '  Catemu', 'value': 'Catemu'},
 {'label': '  Concon', 'value': 'Concon'},
 {'label': '  El Quisco', 'value': 'El Quisco'},
 {'label': '  El Tabo', 'value': 'El Tabo'},
 {'label': '  Hijuelas', 'value': 'Hijuelas'},
 {'label': '  Isla de Pascua', 'value': 'Isla de Pascua'},
 {'label': '  Juan Fernandez', 'value': 'Juan Fernandez'},
 {'label': '  La Cruz', 'value': 'La Cruz'},
 {'label': '  La Ligua', 'value': 'La Ligua'},
 {'label': '  Limache', 'value': 'Limache'},
 {'label': '  Llaillay', 'value': 'Llaillay'},
 {'label': '  Los Andes', 'value': 'Los Andes'},
 {'label': '  Nogales', 'value': 'Nogales'},
 {'label': '  Olmue', 'value': 'Olmue'},
 {'label': '  Panquehue', 'value': 'Panquehue'},
 {'label': '  Papudo', 'value': 'Papudo'},
 {'label': '  Petorca', 'value': 'Petorca'},
 {'label': '  Puchuncavi', 'value': 'Puchuncavi'},
 {'label': '  Putaendo', 'value': 'Putaendo'},
 {'label': '  Quillota', 'value': 'Quillota'},
 {'label': '  Quilpue', 'value': 'Quilpue'},
 {'label': '  Quintero', 'value': 'Quintero'},
 {'label': '  Rinconada', 'value': 'Rinconada'},
 {'label': '  San Antonio', 'value': 'San Antonio'},
 {'label': '  San Esteban', 'value': 'San Esteban'},
 {'label': '  San Felipe', 'value': 'San Felipe'},
 {'label': '  Santa Maria', 'value': 'Santa Maria'},
 {'label': '  Santo Domingo', 'value': 'Santo Domingo'},
 {'label': '  Valparaiso', 'value': 'Valparaiso'},
 {'label': '  Villa Alemana', 'value': 'Villa Alemana'},
 {'label': '  Vina del Mar', 'value': 'Vina del Mar'},
 {'label': '  Zapallar', 'value': 'Zapallar'},
 {'label': 'Reg. Metropolitana', 'value': 'Metropolitana', 'disabled': True},
 {'label': '  Alhue', 'value': 'Alhue'},
 {'label': '  Buin', 'value': 'Buin'},
 {'label': '  Calera de Tango', 'value': 'Calera de Tango'},
 {'label': '  Cerrillos', 'value': 'Cerrillos'},
 {'label': '  Cerro Navia', 'value': 'Cerro Navia'},
 {'label': '  Colina', 'value': 'Colina'},
 {'label': '  Conchali', 'value': 'Conchali'},
 {'label': '  Curacavi', 'value': 'Curacavi'},
 {'label': '  El Bosque', 'value': 'El Bosque'},
 {'label': '  El Monte', 'value': 'El Monte'},
 {'label': '  Estacion Central', 'value': 'Estacion Central'},
 {'label': '  Huechuraba', 'value': 'Huechuraba'},
 {'label': '  Independencia', 'value': 'Independencia'},
 {'label': '  Isla de Maipo', 'value': 'Isla de Maipo'},
 {'label': '  La Cisterna', 'value': 'La Cisterna'},
 {'label': '  La Florida', 'value': 'La Florida'},
 {'label': '  La Granja', 'value': 'La Granja'},
 {'label': '  La Pintana', 'value': 'La Pintana'},
 {'label': '  La Reina', 'value': 'La Reina'},
 {'label': '  Lampa', 'value': 'Lampa'},
 {'label': '  Las Condes', 'value': 'Las Condes'},
 {'label': '  Lo Barnechea', 'value': 'Lo Barnechea'},
 {'label': '  Lo Espejo', 'value': 'Lo Espejo'},
 {'label': '  Lo Prado', 'value': 'Lo Prado'},
 {'label': '  Macul', 'value': 'Macul'},
 {'label': '  Maipu', 'value': 'Maipu'},
 {'label': '  Maria Pinto', 'value': 'Maria Pinto'},
 {'label': '  Melipilla', 'value': 'Melipilla'},
 {'label': '  Nunoa', 'value': 'Nunoa'},
 {'label': '  Padre Hurtado', 'value': 'Padre Hurtado'},
 {'label': '  Paine', 'value': 'Paine'},
 {'label': '  Pedro Aguirre Cerda', 'value': 'Pedro Aguirre Cerda'},
 {'label': '  Penaflor', 'value': 'Penaflor'},
 {'label': '  Penalolen', 'value': 'Penalolen'},
 {'label': '  Pirque', 'value': 'Pirque'},
 {'label': '  Providencia', 'value': 'Providencia'},
 {'label': '  Pudahuel', 'value': 'Pudahuel'},
 {'label': '  Puente Alto', 'value': 'Puente Alto'},
 {'label': '  Quilicura', 'value': 'Quilicura'},
 {'label': '  Quinta Normal', 'value': 'Quinta Normal'},
 {'label': '  Recoleta', 'value': 'Recoleta'},
 {'label': '  Renca', 'value': 'Renca'},
 {'label': '  San Bernardo', 'value': 'San Bernardo'},
 {'label': '  San Joaquin', 'value': 'San Joaquin'},
 {'label': '  San Jose de Maipo', 'value': 'San Jose de Maipo'},
 {'label': '  San Miguel', 'value': 'San Miguel'},
 {'label': '  San Pedro', 'value': 'San Pedro'},
 {'label': '  San Ramon', 'value': 'San Ramon'},
 {'label': '  Santiago', 'value': 'Santiago'},
 {'label': '  Talagante', 'value': 'Talagante'},
 {'label': '  Tiltil', 'value': 'Tiltil'},
 {'label': '  Vitacura', 'value': 'Vitacura'},
 {'label': 'Reg. O’Higgins', 'value': 'O’Higgins', 'disabled': True},
 {'label': '  Chepica', 'value': 'Chepica'},
 {'label': '  Chimbarongo', 'value': 'Chimbarongo'},
 {'label': '  Codegua', 'value': 'Codegua'},
 {'label': '  Coinco', 'value': 'Coinco'},
 {'label': '  Coltauco', 'value': 'Coltauco'},
 {'label': '  Donihue', 'value': 'Donihue'},
 {'label': '  Graneros', 'value': 'Graneros'},
 {'label': '  La Estrella', 'value': 'La Estrella'},
 {'label': '  Las Cabras', 'value': 'Las Cabras'},
 {'label': '  Litueche', 'value': 'Litueche'},
 {'label': '  Lolol', 'value': 'Lolol'},
 {'label': '  Machali', 'value': 'Machali'},
 {'label': '  Malloa', 'value': 'Malloa'},
 {'label': '  Marchihue', 'value': 'Marchihue'},
 {'label': '  Mostazal', 'value': 'Mostazal'},
 {'label': '  Nancagua', 'value': 'Nancagua'},
 {'label': '  Navidad', 'value': 'Navidad'},
 {'label': '  Olivar', 'value': 'Olivar'},
 {'label': '  Palmilla', 'value': 'Palmilla'},
 {'label': '  Paredones', 'value': 'Paredones'},
 {'label': '  Peralillo', 'value': 'Peralillo'},
 {'label': '  Peumo', 'value': 'Peumo'},
 {'label': '  Pichidegua', 'value': 'Pichidegua'},
 {'label': '  Pichilemu', 'value': 'Pichilemu'},
 {'label': '  Placilla', 'value': 'Placilla'},
 {'label': '  Pumanque', 'value': 'Pumanque'},
 {'label': '  Quinta de Tilcoco', 'value': 'Quinta de Tilcoco'},
 {'label': '  Rancagua', 'value': 'Rancagua'},
 {'label': '  Rengo', 'value': 'Rengo'},
 {'label': '  Requinoa', 'value': 'Requinoa'},
 {'label': '  San Fernando', 'value': 'San Fernando'},
 {'label': '  San Vicente', 'value': 'San Vicente'},
 {'label': '  Santa Cruz', 'value': 'Santa Cruz'},
 {'label': 'Reg. Maule', 'value': 'Maule', 'disabled': True},
 {'label': '  Cauquenes', 'value': 'Cauquenes'},
 {'label': '  Chanco', 'value': 'Chanco'},
 {'label': '  Colbun', 'value': 'Colbun'},
 {'label': '  Constitucion', 'value': 'Constitucion'},
 {'label': '  Curepto', 'value': 'Curepto'},
 {'label': '  Curico', 'value': 'Curico'},
 {'label': '  Empedrado', 'value': 'Empedrado'},
 {'label': '  Hualane', 'value': 'Hualane'},
 {'label': '  Licanten', 'value': 'Licanten'},
 {'label': '  Linares', 'value': 'Linares'},
 {'label': '  Longavi', 'value': 'Longavi'},
 {'label': '  Maule', 'value': 'Maule'},
 {'label': '  Molina', 'value': 'Molina'},
 {'label': '  Parral', 'value': 'Parral'},
 {'label': '  Pelarco', 'value': 'Pelarco'},
 {'label': '  Pelluhue', 'value': 'Pelluhue'},
 {'label': '  Pencahue', 'value': 'Pencahue'},
 {'label': '  Rauco', 'value': 'Rauco'},
 {'label': '  Retiro', 'value': 'Retiro'},
 {'label': '  Rio Claro', 'value': 'Rio Claro'},
 {'label': '  Romeral', 'value': 'Romeral'},
 {'label': '  Sagrada Familia', 'value': 'Sagrada Familia'},
 {'label': '  San Clemente', 'value': 'San Clemente'},
 {'label': '  San Javier', 'value': 'San Javier'},
 {'label': '  San Rafael', 'value': 'San Rafael'},
 {'label': '  Talca', 'value': 'Talca'},
 {'label': '  Teno', 'value': 'Teno'},
 {'label': '  Vichuquen', 'value': 'Vichuquen'},
 {'label': '  Villa Alegre', 'value': 'Villa Alegre'},
 {'label': '  Yerbas Buenas', 'value': 'Yerbas Buenas'},
 {'label': 'Reg. Ñuble', 'value': 'Ñuble', 'disabled': True},
 {'label': '  Bulnes', 'value': 'Bulnes'},
 {'label': '  Chillan', 'value': 'Chillan'},
 {'label': '  Chillan Viejo', 'value': 'Chillan Viejo'},
 {'label': '  Cobquecura', 'value': 'Cobquecura'},
 {'label': '  Coelemu', 'value': 'Coelemu'},
 {'label': '  Coihueco', 'value': 'Coihueco'},
 {'label': '  El Carmen', 'value': 'El Carmen'},
 {'label': '  Ninhue', 'value': 'Ninhue'},
 {'label': '  Niquen', 'value': 'Niquen'},
 {'label': '  Pemuco', 'value': 'Pemuco'},
 {'label': '  Pinto', 'value': 'Pinto'},
 {'label': '  Portezuelo', 'value': 'Portezuelo'},
 {'label': '  Quillon', 'value': 'Quillon'},
 {'label': '  Quirihue', 'value': 'Quirihue'},
 {'label': '  Ranquil', 'value': 'Ranquil'},
 {'label': '  San Carlos', 'value': 'San Carlos'},
 {'label': '  San Fabian', 'value': 'San Fabian'},
 {'label': '  San Ignacio', 'value': 'San Ignacio'},
 {'label': '  San Nicolas', 'value': 'San Nicolas'},
 {'label': '  Treguaco', 'value': 'Treguaco'},
 {'label': '  Yungay', 'value': 'Yungay'},
 {'label': 'Reg. Biobío', 'value': 'Biobío', 'disabled': True},
 {'label': '  Alto Biobio', 'value': 'Alto Biobio'},
 {'label': '  Antuco', 'value': 'Antuco'},
 {'label': '  Arauco', 'value': 'Arauco'},
 {'label': '  Cabrero', 'value': 'Cabrero'},
 {'label': '  Canete', 'value': 'Canete'},
 {'label': '  Chiguayante', 'value': 'Chiguayante'},
 {'label': '  Concepcion', 'value': 'Concepcion'},
 {'label': '  Contulmo', 'value': 'Contulmo'},
 {'label': '  Coronel', 'value': 'Coronel'},
 {'label': '  Curanilahue', 'value': 'Curanilahue'},
 {'label': '  Florida', 'value': 'Florida'},
 {'label': '  Hualpen', 'value': 'Hualpen'},
 {'label': '  Hualqui', 'value': 'Hualqui'},
 {'label': '  Laja', 'value': 'Laja'},
 {'label': '  Lebu', 'value': 'Lebu'},
 {'label': '  Los Alamos', 'value': 'Los Alamos'},
 {'label': '  Los Angeles', 'value': 'Los Angeles'},
 {'label': '  Lota', 'value': 'Lota'},
 {'label': '  Mulchen', 'value': 'Mulchen'},
 {'label': '  Nacimiento', 'value': 'Nacimiento'},
 {'label': '  Negrete', 'value': 'Negrete'},
 {'label': '  Penco', 'value': 'Penco'},
 {'label': '  Quilaco', 'value': 'Quilaco'},
 {'label': '  Quilleco', 'value': 'Quilleco'},
 {'label': '  San Pedro de la Paz', 'value': 'San Pedro de la Paz'},
 {'label': '  San Rosendo', 'value': 'San Rosendo'},
 {'label': '  Santa Barbara', 'value': 'Santa Barbara'},
 {'label': '  Santa Juana', 'value': 'Santa Juana'},
 {'label': '  Talcahuano', 'value': 'Talcahuano'},
 {'label': '  Tirua', 'value': 'Tirua'},
 {'label': '  Tome', 'value': 'Tome'},
 {'label': '  Tucapel', 'value': 'Tucapel'},
 {'label': '  Yumbel', 'value': 'Yumbel'},
 {'label': 'Reg. Araucanía', 'value': 'Araucanía', 'disabled': True},
 {'label': '  Angol', 'value': 'Angol'},
 {'label': '  Carahue', 'value': 'Carahue'},
 {'label': '  Cholchol', 'value': 'Cholchol'},
 {'label': '  Collipulli', 'value': 'Collipulli'},
 {'label': '  Cunco', 'value': 'Cunco'},
 {'label': '  Curacautin', 'value': 'Curacautin'},
 {'label': '  Curarrehue', 'value': 'Curarrehue'},
 {'label': '  Ercilla', 'value': 'Ercilla'},
 {'label': '  Freire', 'value': 'Freire'},
 {'label': '  Galvarino', 'value': 'Galvarino'},
 {'label': '  Gorbea', 'value': 'Gorbea'},
 {'label': '  Lautaro', 'value': 'Lautaro'},
 {'label': '  Loncoche', 'value': 'Loncoche'},
 {'label': '  Lonquimay', 'value': 'Lonquimay'},
 {'label': '  Los Sauces', 'value': 'Los Sauces'},
 {'label': '  Lumaco', 'value': 'Lumaco'},
 {'label': '  Melipeuco', 'value': 'Melipeuco'},
 {'label': '  Nueva Imperial', 'value': 'Nueva Imperial'},
 {'label': '  Padre Las Casas', 'value': 'Padre Las Casas'},
 {'label': '  Perquenco', 'value': 'Perquenco'},
 {'label': '  Pitrufquen', 'value': 'Pitrufquen'},
 {'label': '  Pucon', 'value': 'Pucon'},
 {'label': '  Puren', 'value': 'Puren'},
 {'label': '  Renaico', 'value': 'Renaico'},
 {'label': '  Saavedra', 'value': 'Saavedra'},
 {'label': '  Temuco', 'value': 'Temuco'},
 {'label': '  Teodoro Schmidt', 'value': 'Teodoro Schmidt'},
 {'label': '  Tolten', 'value': 'Tolten'},
 {'label': '  Traiguen', 'value': 'Traiguen'},
 {'label': '  Victoria', 'value': 'Victoria'},
 {'label': '  Vilcun', 'value': 'Vilcun'},
 {'label': '  Villarrica', 'value': 'Villarrica'},
 {'label': 'Reg. Los Ríos', 'value': 'Los Ríos', 'disabled': True},
 {'label': '  Corral', 'value': 'Corral'},
 {'label': '  Futrono', 'value': 'Futrono'},
 {'label': '  La Union', 'value': 'La Union'},
 {'label': '  Lago Ranco', 'value': 'Lago Ranco'},
 {'label': '  Lanco', 'value': 'Lanco'},
 {'label': '  Los Lagos', 'value': 'Los Lagos'},
 {'label': '  Mafil', 'value': 'Mafil'},
 {'label': '  Mariquina', 'value': 'Mariquina'},
 {'label': '  Paillaco', 'value': 'Paillaco'},
 {'label': '  Panguipulli', 'value': 'Panguipulli'},
 {'label': '  Rio Bueno', 'value': 'Rio Bueno'},
 {'label': '  Valdivia', 'value': 'Valdivia'},
 {'label': 'Reg. Los Lagos', 'value': 'Los Lagos', 'disabled': True},
 {'label': '  Ancud', 'value': 'Ancud'},
 {'label': '  Calbuco', 'value': 'Calbuco'},
 {'label': '  Castro', 'value': 'Castro'},
 {'label': '  Chaiten', 'value': 'Chaiten'},
 {'label': '  Chonchi', 'value': 'Chonchi'},
 {'label': '  Cochamo', 'value': 'Cochamo'},
 {'label': '  Curaco de Velez', 'value': 'Curaco de Velez'},
 {'label': '  Dalcahue', 'value': 'Dalcahue'},
 {'label': '  Fresia', 'value': 'Fresia'},
 {'label': '  Frutillar', 'value': 'Frutillar'},
 {'label': '  Futaleufu', 'value': 'Futaleufu'},
 {'label': '  Hualaihue', 'value': 'Hualaihue'},
 {'label': '  Llanquihue', 'value': 'Llanquihue'},
 {'label': '  Los Muermos', 'value': 'Los Muermos'},
 {'label': '  Maullin', 'value': 'Maullin'},
 {'label': '  Osorno', 'value': 'Osorno'},
 {'label': '  Palena', 'value': 'Palena'},
 {'label': '  Puerto Montt', 'value': 'Puerto Montt'},
 {'label': '  Puerto Octay', 'value': 'Puerto Octay'},
 {'label': '  Puerto Varas', 'value': 'Puerto Varas'},
 {'label': '  Puqueldon', 'value': 'Puqueldon'},
 {'label': '  Purranque', 'value': 'Purranque'},
 {'label': '  Puyehue', 'value': 'Puyehue'},
 {'label': '  Queilen', 'value': 'Queilen'},
 {'label': '  Quellon', 'value': 'Quellon'},
 {'label': '  Quemchi', 'value': 'Quemchi'},
 {'label': '  Quinchao', 'value': 'Quinchao'},
 {'label': '  Rio Negro', 'value': 'Rio Negro'},
 {'label': '  San Juan de la Costa', 'value': 'San Juan de la Costa'},
 {'label': '  San Pablo', 'value': 'San Pablo'},
 {'label': 'Reg. Aysén', 'value': 'Aysén', 'disabled': True},
 {'label': '  Aysen', 'value': 'Aysen'},
 {'label': '  Chile Chico', 'value': 'Chile Chico'},
 {'label': '  Cisnes', 'value': 'Cisnes'},
 {'label': '  Cochrane', 'value': 'Cochrane'},
 {'label': '  Coyhaique', 'value': 'Coyhaique'},
 {'label': '  Guaitecas', 'value': 'Guaitecas'},
 {'label': '  Lago Verde', 'value': 'Lago Verde'},
 {'label': '  OHiggins', 'value': 'OHiggins'},
 {'label': '  Rio Ibanez', 'value': 'Rio Ibanez'},
 {'label': '  Tortel', 'value': 'Tortel'},
 {'label': 'Reg. Magallanes', 'value': 'Magallanes', 'disabled': True},
 {'label': '  Antartica', 'value': 'Antartica'},
 {'label': '  Cabo de Hornos', 'value': 'Cabo de Hornos'},
 {'label': '  Laguna Blanca', 'value': 'Laguna Blanca'},
 {'label': '  Natales', 'value': 'Natales'},
 {'label': '  Porvenir', 'value': 'Porvenir'},
 {'label': '  Primavera', 'value': 'Primavera'},
 {'label': '  Punta Arenas', 'value': 'Punta Arenas'},
 {'label': '  Rio Verde', 'value': 'Rio Verde'},
 {'label': '  San Gregorio', 'value': 'San Gregorio'},
 {'label': '  Timaukel', 'value': 'Timaukel'},
 {'label': '  Torres del Paine', 'value': 'Torres del Paine'}]

REGION_TO_POPULATION = {
    'Arica y Parinacota': 226_068,
    'Tarapacá': 581_802,
    'Antofagasta': 607_534,
    'Atacama': 286_168,
    'Coquimbo': 757_586,
    'Valparaíso': 1_815_902,
    'Metropolitana': 7_112_808,
    'O’Higgins': 914_555,
    'Maule': 1_044_950,
    'Ñuble': 480_609,
    'Biobío': 1_556_805,
    'Araucanía': 957_224,
    'Los Ríos': 384_837,
    'Los Lagos': 828_708,
    'Aysén': 103_158,
    'Magallanes': 166_533,
}
REGION_TO_POPULATION['Total'] = sum(REGION_TO_POPULATION.values())

COMUNA_TO_REGION = {
    'Arica': 'Arica y Parinacota',
    'Camarones': 'Arica y Parinacota',
    'General Lagos': 'Arica y Parinacota',
    'Putre': 'Arica y Parinacota',
    'Alto Hospicio': 'Tarapacá',
    'Camina': 'Tarapacá',
    'Colchane': 'Tarapacá',
    'Huara': 'Tarapacá',
    'Iquique': 'Tarapacá',
    'Pica': 'Tarapacá',
    'Pozo Almonte': 'Tarapacá',
    'Antofagasta': 'Antofagasta',
    'Calama': 'Antofagasta',
    'Maria Elena': 'Antofagasta',
    'Mejillones': 'Antofagasta',
    'Ollague': 'Antofagasta',
    'San Pedro de Atacama': 'Antofagasta',
    'Sierra Gorda': 'Antofagasta',
    'Taltal': 'Antofagasta',
    'Tocopilla': 'Antofagasta',
    'Alto del Carmen': 'Atacama',
    'Caldera': 'Atacama',
    'Chanaral': 'Atacama',
    'Copiapo': 'Atacama',
    'Diego de Almagro': 'Atacama',
    'Freirina': 'Atacama',
    'Huasco': 'Atacama',
    'Tierra Amarilla': 'Atacama',
    'Vallenar': 'Atacama',
    'Andacollo': 'Coquimbo',
    'Canela': 'Coquimbo',
    'Combarbala': 'Coquimbo',
    'Coquimbo': 'Coquimbo',
    'Illapel': 'Coquimbo',
    'La Higuera': 'Coquimbo',
    'La Serena': 'Coquimbo',
    'Los Vilos': 'Coquimbo',
    'Monte Patria': 'Coquimbo',
    'Ovalle': 'Coquimbo',
    'Paiguano': 'Coquimbo',
    'Punitaqui': 'Coquimbo',
    'Rio Hurtado': 'Coquimbo',
    'Salamanca': 'Coquimbo',
    'Vicuna': 'Coquimbo',
    'Algarrobo': 'Valparaíso',
    'Cabildo': 'Valparaíso',
    'Calera': 'Valparaíso',
    'Calle Larga': 'Valparaíso',
    'Cartagena': 'Valparaíso',
    'Casablanca': 'Valparaíso',
    'Catemu': 'Valparaíso',
    'Concon': 'Valparaíso',
    'El Quisco': 'Valparaíso',
    'El Tabo': 'Valparaíso',
    'Hijuelas': 'Valparaíso',
    'Isla de Pascua': 'Valparaíso',
    'Juan Fernandez': 'Valparaíso',
    'La Cruz': 'Valparaíso',
    'La Ligua': 'Valparaíso',
    'Limache': 'Valparaíso',
    'Llaillay': 'Valparaíso',
    'Los Andes': 'Valparaíso',
    'Nogales': 'Valparaíso',
    'Olmue': 'Valparaíso',
    'Panquehue': 'Valparaíso',
    'Papudo': 'Valparaíso',
    'Petorca': 'Valparaíso',
    'Puchuncavi': 'Valparaíso',
    'Putaendo': 'Valparaíso',
    'Quillota': 'Valparaíso',
    'Quilpue': 'Valparaíso',
    'Quintero': 'Valparaíso',
    'Rinconada': 'Valparaíso',
    'San Antonio': 'Valparaíso',
    'San Esteban': 'Valparaíso',
    'San Felipe': 'Valparaíso',
    'Santa Maria': 'Valparaíso',
    'Santo Domingo': 'Valparaíso',
    'Valparaiso': 'Valparaíso',
    'Villa Alemana': 'Valparaíso',
    'Vina del Mar': 'Valparaíso',
    'Zapallar': 'Valparaíso',
    'Alhue': 'Metropolitana',
    'Buin': 'Metropolitana',
    'Calera de Tango': 'Metropolitana',
    'Cerrillos': 'Metropolitana',
    'Cerro Navia': 'Metropolitana',
    'Colina': 'Metropolitana',
    'Conchali': 'Metropolitana',
    'Curacavi': 'Metropolitana',
    'El Bosque': 'Metropolitana',
    'El Monte': 'Metropolitana',
    'Estacion Central': 'Metropolitana',
    'Huechuraba': 'Metropolitana',
    'Independencia': 'Metropolitana',
    'Isla de Maipo': 'Metropolitana',
    'La Cisterna': 'Metropolitana',
    'La Florida': 'Metropolitana',
    'La Granja': 'Metropolitana',
    'La Pintana': 'Metropolitana',
    'La Reina': 'Metropolitana',
    'Lampa': 'Metropolitana',
    'Las Condes': 'Metropolitana',
    'Lo Barnechea': 'Metropolitana',
    'Lo Espejo': 'Metropolitana',
    'Lo Prado': 'Metropolitana',
    'Macul': 'Metropolitana',
    'Maipu': 'Metropolitana',
    'Maria Pinto': 'Metropolitana',
    'Melipilla': 'Metropolitana',
    'Nunoa': 'Metropolitana',
    'Padre Hurtado': 'Metropolitana',
    'Paine': 'Metropolitana',
    'Pedro Aguirre Cerda': 'Metropolitana',
    'Penaflor': 'Metropolitana',
    'Penalolen': 'Metropolitana',
    'Pirque': 'Metropolitana',
    'Providencia': 'Metropolitana',
    'Pudahuel': 'Metropolitana',
    'Puente Alto': 'Metropolitana',
    'Quilicura': 'Metropolitana',
    'Quinta Normal': 'Metropolitana',
    'Recoleta': 'Metropolitana',
    'Renca': 'Metropolitana',
    'San Bernardo': 'Metropolitana',
    'San Joaquin': 'Metropolitana',
    'San Jose de Maipo': 'Metropolitana',
    'San Miguel': 'Metropolitana',
    'San Pedro': 'Metropolitana',
    'San Ramon': 'Metropolitana',
    'Santiago': 'Metropolitana',
    'Talagante': 'Metropolitana',
    'Tiltil': 'Metropolitana',
    'Vitacura': 'Metropolitana',
    'Chepica': 'O’Higgins',
    'Chimbarongo': 'O’Higgins',
    'Codegua': 'O’Higgins',
    'Coinco': 'O’Higgins',
    'Coltauco': 'O’Higgins',
    'Donihue': 'O’Higgins',
    'Graneros': 'O’Higgins',
    'La Estrella': 'O’Higgins',
    'Las Cabras': 'O’Higgins',
    'Litueche': 'O’Higgins',
    'Lolol': 'O’Higgins',
    'Machali': 'O’Higgins',
    'Malloa': 'O’Higgins',
    'Marchihue': 'O’Higgins',
    'Mostazal': 'O’Higgins',
    'Nancagua': 'O’Higgins',
    'Navidad': 'O’Higgins',
    'Olivar': 'O’Higgins',
    'Palmilla': 'O’Higgins',
    'Paredones': 'O’Higgins',
    'Peralillo': 'O’Higgins',
    'Peumo': 'O’Higgins',
    'Pichidegua': 'O’Higgins',
    'Pichilemu': 'O’Higgins',
    'Placilla': 'O’Higgins',
    'Pumanque': 'O’Higgins',
    'Quinta de Tilcoco': 'O’Higgins',
    'Rancagua': 'O’Higgins',
    'Rengo': 'O’Higgins',
    'Requinoa': 'O’Higgins',
    'San Fernando': 'O’Higgins',
    'San Vicente': 'O’Higgins',
    'Santa Cruz': 'O’Higgins',
    'Cauquenes': 'Maule',
    'Chanco': 'Maule',
    'Colbun': 'Maule',
    'Constitucion': 'Maule',
    'Curepto': 'Maule',
    'Curico': 'Maule',
    'Empedrado': 'Maule',
    'Hualane': 'Maule',
    'Licanten': 'Maule',
    'Linares': 'Maule',
    'Longavi': 'Maule',
    'Maule': 'Maule',
    'Molina': 'Maule',
    'Parral': 'Maule',
    'Pelarco': 'Maule',
    'Pelluhue': 'Maule',
    'Pencahue': 'Maule',
    'Rauco': 'Maule',
    'Retiro': 'Maule',
    'Rio Claro': 'Maule',
    'Romeral': 'Maule',
    'Sagrada Familia': 'Maule',
    'San Clemente': 'Maule',
    'San Javier': 'Maule',
    'San Rafael': 'Maule',
    'Talca': 'Maule',
    'Teno': 'Maule',
    'Vichuquen': 'Maule',
    'Villa Alegre': 'Maule',
    'Yerbas Buenas': 'Maule',
    'Bulnes': 'Ñuble',
    'Chillan': 'Ñuble',
    'Chillan Viejo': 'Ñuble',
    'Cobquecura': 'Ñuble',
    'Coelemu': 'Ñuble',
    'Coihueco': 'Ñuble',
    'El Carmen': 'Ñuble',
    'Ninhue': 'Ñuble',
    'Niquen': 'Ñuble',
    'Pemuco': 'Ñuble',
    'Pinto': 'Ñuble',
    'Portezuelo': 'Ñuble',
    'Quillon': 'Ñuble',
    'Quirihue': 'Ñuble',
    'Ranquil': 'Ñuble',
    'San Carlos': 'Ñuble',
    'San Fabian': 'Ñuble',
    'San Ignacio': 'Ñuble',
    'San Nicolas': 'Ñuble',
    'Treguaco': 'Ñuble',
    'Yungay': 'Ñuble',
    'Alto Biobio': 'Biobío',
    'Antuco': 'Biobío',
    'Arauco': 'Biobío',
    'Cabrero': 'Biobío',
    'Canete': 'Biobío',
    'Chiguayante': 'Biobío',
    'Concepcion': 'Biobío',
    'Contulmo': 'Biobío',
    'Coronel': 'Biobío',
    'Curanilahue': 'Biobío',
    'Florida': 'Biobío',
    'Hualpen': 'Biobío',
    'Hualqui': 'Biobío',
    'Laja': 'Biobío',
    'Lebu': 'Biobío',
    'Los Alamos': 'Biobío',
    'Los Angeles': 'Biobío',
    'Lota': 'Biobío',
    'Mulchen': 'Biobío',
    'Nacimiento': 'Biobío',
    'Negrete': 'Biobío',
    'Penco': 'Biobío',
    'Quilaco': 'Biobío',
    'Quilleco': 'Biobío',
    'San Pedro de la Paz': 'Biobío',
    'San Rosendo': 'Biobío',
    'Santa Barbara': 'Biobío',
    'Santa Juana': 'Biobío',
    'Talcahuano': 'Biobío',
    'Tirua': 'Biobío',
    'Tome': 'Biobío',
    'Tucapel': 'Biobío',
    'Yumbel': 'Biobío',
    'Angol': 'Araucanía',
    'Carahue': 'Araucanía',
    'Cholchol': 'Araucanía',
    'Collipulli': 'Araucanía',
    'Cunco': 'Araucanía',
    'Curacautin': 'Araucanía',
    'Curarrehue': 'Araucanía',
    'Ercilla': 'Araucanía',
    'Freire': 'Araucanía',
    'Galvarino': 'Araucanía',
    'Gorbea': 'Araucanía',
    'Lautaro': 'Araucanía',
    'Loncoche': 'Araucanía',
    'Lonquimay': 'Araucanía',
    'Los Sauces': 'Araucanía',
    'Lumaco': 'Araucanía',
    'Melipeuco': 'Araucanía',
    'Nueva Imperial': 'Araucanía',
    'Padre Las Casas': 'Araucanía',
    'Perquenco': 'Araucanía',
    'Pitrufquen': 'Araucanía',
    'Pucon': 'Araucanía',
    'Puren': 'Araucanía',
    'Renaico': 'Araucanía',
    'Saavedra': 'Araucanía',
    'Temuco': 'Araucanía',
    'Teodoro Schmidt': 'Araucanía',
    'Tolten': 'Araucanía',
    'Traiguen': 'Araucanía',
    'Victoria': 'Araucanía',
    'Vilcun': 'Araucanía',
    'Villarrica': 'Araucanía',
    'Corral': 'Los Ríos',
    'Futrono': 'Los Ríos',
    'La Union': 'Los Ríos',
    'Lago Ranco': 'Los Ríos',
    'Lanco': 'Los Ríos',
    'Los Lagos': 'Los Ríos',
    'Mafil': 'Los Ríos',
    'Mariquina': 'Los Ríos',
    'Paillaco': 'Los Ríos',
    'Panguipulli': 'Los Ríos',
    'Rio Bueno': 'Los Ríos',
    'Valdivia': 'Los Ríos',
    'Ancud': 'Los Lagos',
    'Calbuco': 'Los Lagos',
    'Castro': 'Los Lagos',
    'Chaiten': 'Los Lagos',
    'Chonchi': 'Los Lagos',
    'Cochamo': 'Los Lagos',
    'Curaco de Velez': 'Los Lagos',
    'Dalcahue': 'Los Lagos',
    'Fresia': 'Los Lagos',
    'Frutillar': 'Los Lagos',
    'Futaleufu': 'Los Lagos',
    'Hualaihue': 'Los Lagos',
    'Llanquihue': 'Los Lagos',
    'Los Muermos': 'Los Lagos',
    'Maullin': 'Los Lagos',
    'Osorno': 'Los Lagos',
    'Palena': 'Los Lagos',
    'Puerto Montt': 'Los Lagos',
    'Puerto Octay': 'Los Lagos',
    'Puerto Varas': 'Los Lagos',
    'Puqueldon': 'Los Lagos',
    'Purranque': 'Los Lagos',
    'Puyehue': 'Los Lagos',
    'Queilen': 'Los Lagos',
    'Quellon': 'Los Lagos',
    'Quemchi': 'Los Lagos',
    'Quinchao': 'Los Lagos',
    'Rio Negro': 'Los Lagos',
    'San Juan de la Costa': 'Los Lagos',
    'San Pablo': 'Los Lagos',
    'Aysen': 'Aysén',
    'Chile Chico': 'Aysén',
    'Cisnes': 'Aysén',
    'Cochrane': 'Aysén',
    'Coyhaique': 'Aysén',
    'Guaitecas': 'Aysén',
    'Lago Verde': 'Aysén',
    'OHiggins': 'Aysén',
    'Rio Ibanez': 'Aysén',
    'Tortel': 'Aysén',
    'Antartica': 'Magallanes',
    'Cabo de Hornos': 'Magallanes',
    'Laguna Blanca': 'Magallanes',
    'Natales': 'Magallanes',
    'Porvenir': 'Magallanes',
    'Primavera': 'Magallanes',
    'Punta Arenas': 'Magallanes',
    'Rio Verde': 'Magallanes',
    'San Gregorio': 'Magallanes',
    'Timaukel': 'Magallanes',
    'Torres del Paine': 'Magallanes'
 }

REGION_TO_COMUNAS = {'Atacama': ['Alto del Carmen',
  'Caldera',
  'Chanaral',
  'Copiapo',
  'Diego de Almagro',
  'Freirina',
  'Huasco',
  'Tierra Amarilla',
  'Vallenar'],
 'Coquimbo': ['Andacollo',
  'Canela',
  'Combarbala',
  'Coquimbo',
  'Illapel',
  'La Higuera',
  'La Serena',
  'Los Vilos',
  'Monte Patria',
  'Ovalle',
  'Paiguano',
  'Punitaqui',
  'Rio Hurtado',
  'Salamanca',
  'Vicuna'],
 'Biobío': ['Alto Biobio',
  'Antuco',
  'Arauco',
  'Cabrero',
  'Canete',
  'Chiguayante',
  'Concepcion',
  'Contulmo',
  'Coronel',
  'Curanilahue',
  'Florida',
  'Hualpen',
  'Hualqui',
  'Laja',
  'Lebu',
  'Los Alamos',
  'Los Angeles',
  'Lota',
  'Mulchen',
  'Nacimiento',
  'Negrete',
  'Penco',
  'Quilaco',
  'Quilleco',
  'San Pedro de la Paz',
  'San Rosendo',
  'Santa Barbara',
  'Santa Juana',
  'Talcahuano',
  'Tirua',
  'Tome',
  'Tucapel',
  'Yumbel'],
 'Aysén': ['Aysen',
  'Chile Chico',
  'Cisnes',
  'Cochrane',
  'Coyhaique',
  'Guaitecas',
  'Lago Verde',
  'OHiggins',
  'Rio Ibanez',
  'Tortel'],
 'Arica y Parinacota': ['Arica', 'Camarones', 'General Lagos', 'Putre'],
 'Valparaíso': ['Algarrobo',
  'Cabildo',
  'Calera',
  'Calle Larga',
  'Cartagena',
  'Casablanca',
  'Catemu',
  'Concon',
  'El Quisco',
  'El Tabo',
  'Hijuelas',
  'Isla de Pascua',
  'Juan Fernandez',
  'La Cruz',
  'La Ligua',
  'Limache',
  'Llaillay',
  'Los Andes',
  'Nogales',
  'Olmue',
  'Panquehue',
  'Papudo',
  'Petorca',
  'Puchuncavi',
  'Putaendo',
  'Quillota',
  'Quilpue',
  'Quintero',
  'Rinconada',
  'San Antonio',
  'San Esteban',
  'San Felipe',
  'Santa Maria',
  'Santo Domingo',
  'Valparaiso',
  'Villa Alemana',
  'Vina del Mar',
  'Zapallar'],
 'Antofagasta': ['Antofagasta',
  'Calama',
  'Maria Elena',
  'Mejillones',
  'Ollague',
  'San Pedro de Atacama',
  'Sierra Gorda',
  'Taltal',
  'Tocopilla'],
 'O’Higgins': ['Chepica',
  'Chimbarongo',
  'Codegua',
  'Coinco',
  'Coltauco',
  'Donihue',
  'Graneros',
  'La Estrella',
  'Las Cabras',
  'Litueche',
  'Lolol',
  'Machali',
  'Malloa',
  'Marchihue',
  'Mostazal',
  'Nancagua',
  'Navidad',
  'Olivar',
  'Palmilla',
  'Paredones',
  'Peralillo',
  'Peumo',
  'Pichidegua',
  'Pichilemu',
  'Placilla',
  'Pumanque',
  'Quinta de Tilcoco',
  'Rancagua',
  'Rengo',
  'Requinoa',
  'San Fernando',
  'San Vicente',
  'Santa Cruz'],
 'Ñuble': ['Bulnes',
  'Chillan',
  'Chillan Viejo',
  'Cobquecura',
  'Coelemu',
  'Coihueco',
  'El Carmen',
  'Ninhue',
  'Niquen',
  'Pemuco',
  'Pinto',
  'Portezuelo',
  'Quillon',
  'Quirihue',
  'Ranquil',
  'San Carlos',
  'San Fabian',
  'San Ignacio',
  'San Nicolas',
  'Treguaco',
  'Yungay'],
 'Tarapacá': ['Alto Hospicio',
  'Camina',
  'Colchane',
  'Huara',
  'Iquique',
  'Pica',
  'Pozo Almonte'],
 'Magallanes': ['Antartica',
  'Cabo de Hornos',
  'Laguna Blanca',
  'Natales',
  'Porvenir',
  'Primavera',
  'Punta Arenas',
  'Rio Verde',
  'San Gregorio',
  'Timaukel',
  'Torres del Paine'],
 'Los Ríos': ['Corral',
  'Futrono',
  'La Union',
  'Lago Ranco',
  'Lanco',
  'Los Lagos',
  'Mafil',
  'Mariquina',
  'Paillaco',
  'Panguipulli',
  'Rio Bueno',
  'Valdivia'],
 'Araucanía': ['Angol',
  'Carahue',
  'Cholchol',
  'Collipulli',
  'Cunco',
  'Curacautin',
  'Curarrehue',
  'Ercilla',
  'Freire',
  'Galvarino',
  'Gorbea',
  'Lautaro',
  'Loncoche',
  'Lonquimay',
  'Los Sauces',
  'Lumaco',
  'Melipeuco',
  'Nueva Imperial',
  'Padre Las Casas',
  'Perquenco',
  'Pitrufquen',
  'Pucon',
  'Puren',
  'Renaico',
  'Saavedra',
  'Temuco',
  'Teodoro Schmidt',
  'Tolten',
  'Traiguen',
  'Victoria',
  'Vilcun',
  'Villarrica'],
 'Los Lagos': ['Ancud',
  'Calbuco',
  'Castro',
  'Chaiten',
  'Chonchi',
  'Cochamo',
  'Curaco de Velez',
  'Dalcahue',
  'Fresia',
  'Frutillar',
  'Futaleufu',
  'Hualaihue',
  'Llanquihue',
  'Los Muermos',
  'Maullin',
  'Osorno',
  'Palena',
  'Puerto Montt',
  'Puerto Octay',
  'Puerto Varas',
  'Puqueldon',
  'Purranque',
  'Puyehue',
  'Queilen',
  'Quellon',
  'Quemchi',
  'Quinchao',
  'Rio Negro',
  'San Juan de la Costa',
  'San Pablo'],
 'Maule': ['Cauquenes',
  'Chanco',
  'Colbun',
  'Constitucion',
  'Curepto',
  'Curico',
  'Empedrado',
  'Hualane',
  'Licanten',
  'Linares',
  'Longavi',
  'Maule',
  'Molina',
  'Parral',
  'Pelarco',
  'Pelluhue',
  'Pencahue',
  'Rauco',
  'Retiro',
  'Rio Claro',
  'Romeral',
  'Sagrada Familia',
  'San Clemente',
  'San Javier',
  'San Rafael',
  'Talca',
  'Teno',
  'Vichuquen',
  'Villa Alegre',
  'Yerbas Buenas'],
 'Metropolitana': ['Alhue',
  'Buin',
  'Calera de Tango',
  'Cerrillos',
  'Cerro Navia',
  'Colina',
  'Conchali',
  'Curacavi',
  'El Bosque',
  'El Monte',
  'Estacion Central',
  'Huechuraba',
  'Independencia',
  'Isla de Maipo',
  'La Cisterna',
  'La Florida',
  'La Granja',
  'La Pintana',
  'La Reina',
  'Lampa',
  'Las Condes',
  'Lo Barnechea',
  'Lo Espejo',
  'Lo Prado',
  'Macul',
  'Maipu',
  'Maria Pinto',
  'Melipilla',
  'Nunoa',
  'Padre Hurtado',
  'Paine',
  'Pedro Aguirre Cerda',
  'Penaflor',
  'Penalolen',
  'Pirque',
  'Providencia',
  'Pudahuel',
  'Puente Alto',
  'Quilicura',
  'Quinta Normal',
  'Recoleta',
  'Renca',
  'San Bernardo',
  'San Joaquin',
  'San Jose de Maipo',
  'San Miguel',
  'San Pedro',
  'San Ramon',
  'Santiago',
  'Talagante',
  'Tiltil',
  'Vitacura']}

MARKER_SYMBOLS = {
    'Arica y Parinacota': 'triangle-up',
    'Tarapacá': 'triangle-left',
    'Antofagasta': 'triangle-down',
    'Atacama': 'triangle-right',
    'Coquimbo': 'triangle-ne',
    'Valparaíso': 'triangle-sw',
    'Metropolitana': 'star',
    'O’Higgins': 'hexagram',
    'Maule': 'star-diamond',
    'Ñuble': 'diamond-tall',
    'Biobío': 'diamond-wide',
    'Araucanía': 'star-triangle-up',
    'Los Ríos': 'star-triangle-down',
    'Los Lagos': 'star-square',
    'Aysén': 'bowtie',
    'Magallanes': 'hourglass',
    'Total': 'x'
}
