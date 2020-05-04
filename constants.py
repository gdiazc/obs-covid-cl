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