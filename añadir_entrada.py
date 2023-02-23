import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import ttk, StringVar, messagebox


departamentos = {
    'Amazonas': ['LETICIA', 'PUERTO NARIÑO'],
    'Antioquia': ['MEDELLÍN', 'BELLO', 'ITAGÜÍ', 'ENVIGADO', 'APARTADÓ', 'TURBO', 'RIONEGRO', 'SABANETA', 'CAUCASIA', '', 'COPACABANA', 'CHIGORODÓ', 'LA ESTRELLA', 'NECOCLÍ', 'PUERTO BERRÍO', 'LA CEJA', 'MARINILLA', 'GIRARDOTA', 'BARBOSA', 'CAREPA', 'ANDES', 'EL CARMEN DE VIBORAL', 'GUARNE', 'EL BAGRE', 'SONSÓN', 'SEGOVIA', 'URRAO', 'YARUMAL', 'ARBOLETES', 'SANTA ROSA DE OSOS', 'TARAZÁ', 'AMAGÁ', 'SAN PEDRO DE URABÁ', 'CÁCERES', 'BOLÍVAR', 'SANTUARIO', 'SAN PEDRO DE LOS MILAGROS', 'ZARAGOZA', 'SAN VICENTE', 'ITUANGO', 'SANTA BÁRBARA', 'ANTIOQUIA', 'FREDONIA', 'CONCORDIA', 'SAN JUAN DE URABÁ', 'REMEDIOS', 'AMALFI', 'YOLOMBÓ', 'ABEJORRAL', 'DABEIBA', 'FRONTINO', 'SALGAR', 'SAN ROQUE', 'LA UNIÓN', 'NECHÍ', 'DONMATÍAS', 'EL RETIRO', 'PUERTO NARE', 'BETULIA', 'CAÑASGORDAS', 'VALDIVIA', 'PUERTO TRIUNFO', 'TÁMESIS', 'EL PEÑOL', 'JARDÍN', 'COCORNÁ', 'YONDÓ', 'SOPETRÁN', 'VENECIA', 'TITIRIBÍ', 'SAN RAFAEL', 'JERICÓ', 'ANGOSTURA', 'EBÉJICO', 'SAN CARLOS', 'SAN JERÓNIMO', 'SANTO DOMINGO', 'GÓMEZ PLATA', 'VEGACHÍ', 'SAN LUIS', 'BETANIA', 'MUTATÁ', 'ANORÍ', 'CISNEROS', 'GRANADA', 'LIBORINA', 'NARIÑO', 'ENTRERRÍOS', 'PUEBLORRICO', 'SABANALARGA', 'BRICEÑO', 'CAICEDO', 'ANGELÓPOLIS', 'ANGELÓPOLIS', 'PEQUE', 'MONTEBELLO', 'ANZÁ', 'URAMITA', 'GUATAPÉ', 'TARSO', 'LA PINTADA', 'ARGELIA', 'HELICONIA', 'BURITICÁ', 'VALPARAÍSO', 'SAN FRANCISCO', 'YALÍ', 'BELMIRA', 'GUADALUPE', 'CARAMANTA', 'VIGÍA DEL FUERTE', 'TOLEDO', 'ARMENIA', 'HISPANIA', 'CARACOLÍ', 'SAN ANDRÉS DE CUERQUIA', 'CONCEPCIÓN', 'GIRALDO', 'CAROLINA DEL PRÍNCIPE', 'ALEJANDRÍA', 'MURINDÓ', 'CAMPAMENTO', 'SAN JOSÉ DE LA MONTAÑA', 'OLAYA', 'ABRIAQUÍ'],
    'Arauca': ['ARAUCA', 'ARAUQUITA', 'CRAVO NORTE', 'FORTUL', 'PUERTO RONDON', 'SARAVENA', 'TAME'],
    'Atlántico' : ['BARRANQUILLA', 'BARANOA', 'CAMPO DE LA CRUZ', 'CANDELARIA', 'GALAPA', 'JUAN DE ACOSTA', 'LURUACO', 'MALAMBO', 'MANATI', 'PALMAR DE VARELA', 'PIOJO', 'POLONUEVO', 'PONEDERA', 'PUERTO COLOMBIA', 'REPELON', 'SABANAGRANDE', 'SABANALARGA', 'SANTA LUCIA', 'SANTO TOMAS', 'SOLEDAD', 'SUAN', 'TUBARA', 'USIACURI'],
    'Bolívar' : ['CARTAGENA DE INDIAS', 'MAGANGUÉ', 'EL CARMEN DE BOLÍVAR', 'TURBACO', 'ARJONA', 'MARÍA LA BAJA', 'SANTA CRUZ DE MOMPOX', 'SAN JUAN NEPOMUCENO', 'SAN PABLO', 'SANTA ROSA DEL SUR', 'MAHATES', 'PINILLOS', 'SAN JACINTO', 'CALAMAR', 'ACHÍ', 'TIQUISIO', 'SANTA ROSA', 'SIMITÍ', 'VILLANUEVA', 'SAN ESTANISLAO', 'RÍO VIEJO', 'BARRANCO DE LOBA', 'BRAZUELO DE PAPAYAL', 'NOROSÍ', 'SAN MARTÍN DE LOBA', 'TURBANÁ', 'MORALES', 'CÓRDOBA', 'SAN FERNANDO', 'SANTA CATALINA', 'CLEMENCIA', 'HATILLO DE LOBA', 'MONTECRISTO', 'CICUCO', 'TALAIGUA NUEVO', 'ALTOS DEL ROSARIO', 'ZAMBRANO', 'MARGARITA', 'ARROYOHONDO', 'SOPLAVIENTO', 'EL PEÑÓN', 'CANTAGALLO', 'EL GUAMO', 'ARENAL', 'SAN JACINTO DEL ', 'SAN CRISTÓBAL', 'REGIDOR'],
    'Boyacá': ['TUNJA', 'ALMEIDA', 'AQUITANIA', 'ARCABUCO', 'BELEN', 'BERBEO', 'BETEITIVA', 	'BOAVITA', 	'BOYACA', 'BRICEÑO', 'BUENAVISTA', 'BUSBANZA', 'CALDAS', 'CAMPOHERMOSO', 'CERINZA', 'CHINAVTA', 'CHIQUINQUIRA', 'CHISCAS', 	'CHITA', 'CHITARAQUE', 	'CHIVATA',	'CIENEGA', 	'COMBITA', 	'COPER', 	'CORRALES', 	'COVARACHIA', 	'CUBARA', 	'CUCAITA', 	'CUITIVA', 	'CHIQUIZA',	'CHIVOR', 	'DUITAMA', 	'EL COCUY', 	'EL ESPINO', 	'FIRAVITOBA', 	'FLORESTA', 	'GACHANTIVA', 	'GAMEZA', 	'GARAGOA', 	'GUACAMAYAS', 	'GUATEQUE', 	'GUAYATA', 	'GUICAN',	'IZA',	'JENESANO', 	'JERICO', 	'LABRANZAGRANDE', 	'LA CAPILLA', 	'LA VICTORIA',	'LA UVITA', 	'VILLA DE LEYVA',	'MACANAL', 	'MARIPI', 	'MIRAFLORES',	'MONGUA',	'MONGUI', 	'MONIQUIRA', 	'MOTAVITA', 'MUZO', 'NOBSA', 'NUEVO COLON', 'OICATA', 'OTANCHE' 'PACHAVITA', 'PAEZ', 'PAIPA', 'PAJARITO', 'PANQUEBA', 	'PAUNA', 	'PAYA', 'PAZ DE RIO',  	'PESCA' ,	'PISBA', 	'PUERTO BOYACA', 'QUIPAMA', 'RAMIRIQUI', 	'RAQUIRA', 	'RONDON', 'SABOYA', 'SACHICA', 	'SAMACA', 'SAN EDUARDO', 'SAN JOSE DE PARE', 	'SAN LUIS DE GACENO', 	'SAN MATEO',	'SAN MIGUEL DE SEMA', 	'SAN PABLO BORBUR', 'SANTANA',	'SANTA MARIA',	'SAN ROSA VITERBO',		'SANTA SOFIA',	'SATIVANORTE', 	'SATIVASUR'	,	'SIACHOQUE',	'SOATA',	'SOCOTA',	'SOCHA',	'SOGAMOSO',	'SOMONDOCO', 	'SORA',	'SOTAQUIRA',	'SORACA',	'SUSACON', 	'SUTAMARCHAN',	'SUTATENZA', 	'TASCO', 	'TENZA', 	'TIBANA', 	'TIBASOSA',	'TINJACA', 'TIPACOQUE', 'TOCA', 'TOGUI', 	'TOPAGA', 	'TOTA', 'TUNUNGUA', 	'TURMEQUE', 'TUTA',	'TUTAZA', 	'UMBITA', 	'VENTAQUEMADA', 'VIRACACH', 'ZETAQUIRA'],
    'Caldas': ['MANIZALES', 	'AGUADAS', 	'ANSERMA', 	'ARANZAZU', 'BELALCAZAR', 	'CHINCHINA', 'FILADELFIA', 	'LA DORADA', 'LA MERCED', 	'MANZANARES', 	'MARMATO', 	'MARQUETALIA', 	'MARULANDA', 	'NEIRA', 	'NORCASIA', 'PACORA', 	'PALESTINA', 	'PENSILVANIA', 	'RIOSUCIO',	'RISARALDA', 	'SALAMINA', 	'SAMANA', 'SAN JOSE', 	'SUPIA', 'VICTORIA',	'VILLAMARIA', 	'VITERBO',],
    'Caquetá': ['FLORENCIA', 	'ALBANIA', 	'BELEN DE LOS ANDAQUIES', 	'CARTAGENA DEL CHAIRA', 	'CURRILLO', 	'EL DONCELLO',	'EL PAUJIL', 	'LA MONTAÑITA', 	'MILAN', 	'MORELIA', 	'PUERTO RICO', 	'SAN JOSE DEL FRAGUA', 	'SAN VICENTE DEL CAGUAN', 	'SOLANO',	'SOLITA',	'VALPARAISO'],
    'Casanare': ['YOPAL', 	'AGUAZUL', 	'CHAMEZA', 	'HATO COROZAL', 'LA SALINA', 'MANI', 	'MONTERREY', 	'NUNCHIA', 	'OROCUE', 	'PAZ DE ARIPORO', 	'PORE', 'RECETOR', 	'SABANALARGA',	'SACAMA', 	'SAN LUIS DE PALENQUE', 	'TAMARA', 	'TAURAMENA', 	'TRINIDAD', 'VILLANUEVA'],
    'Cauca': ['POPAYAN', 'ALMAGUER', 	'ARGELIA', 	'BALBOA', 	'BOLIVAR', 	'BUENOS AIRES', 'CAJIBIO', 	'CALDONO',	'CALOTO',	'CORINTO',	'EL TAMBO', 	'FLORENCIA',	'GUACHENE',	'GUAPI',	'INZA',	'JAMBALO',	'LA SIERRA','LA VEGA', 	'LOPEZ', 'MERCADERES','MIRANDA','MORALES',	'PADILLA',	'PAEZ','PATIA',	'PIAMONTE',	'PIENDAMO','PUERTO TEJADA',	'PURACE',	'ROSAS',	'SAN SEBASTIAN',	'SANTANDER DE QUILICHAO',	'SANTA ROSA',	'SILVIA',	'SOTARA',	'SUAREZ',	'SUCRE',	'TIMBIO','TIMBIQUI','TORIBIO','TOTORO',	'VILLA', 'RICA'],
    'Cesar': ['VALLEDUPAR',	'AGUACHICA', 	'AGUSTIN CODAZZI',	'ASTREA',	'BECERRIL',		'BOSCONIA',		'CHIMICHAGUA',		'CHIRIGUANA',		'CURUMANI',		'EL COPEY',		'EL PASO',		'GAMARRA',		'GONZALEZ',		'LA GLORIA',		'LA JAGUA DE IBIRICO',		'MANAURE',		'PAILITAS',		'PELAYA',		'PUEBLO BELLO',		'RIO DE ORO',		'LA PAZ',		'SAN ALBERTO', 		'SAN DIEGO',	'SAN MARTIN',	'TAMALAMEQUE'],
    'Chocó': ['QUIBDO',	'ACANDI',	'ALTO BAUDO',	'ATRATO',	'BAGADO', 	'BAHIA SOLANO',		'BAJO BAUDO', 	'BOJAYA', 	'CANTON DE SAN PABLO',		'CARMEN DEL DARIEN', 	'CERTEGUI', 	'CONDOTO',  'EL CARMEN DE ATRATO', 	'EL LITORAL DEL SAN JUAN', 		'ITSMINA',	'JURADO', 	'LLORO',	'MEDIO ATRATO',		'MEDIO BAUDÓ', 	'MEDIO SAN JUAN',	'NOVITA',	'NUQUI',	'RIO IRO',	'RIO QUITO',	'RIOSUCIO',	'SAN JOSE DEL PALMAR', 'SIPI',	'TADO',	'UNGUIA',	'UNION PANAMERICANA'],
    'Córdoba': ['MONTERIA',    'AYAPEL',	'BUENAVISTA',	'CANALETE',	'CERETE',	'CHIMA',	'CHINU',	'CIENAGA DE ORO',	'COTORRA',	'LA APARTADA',	'LORICA',	'LOS CORDOBAS',	'MOMIL',	'MONTELIBANO',	'MOÑITOS',	'PLANETA RICA', 'PUEBLO NUEVO', 	'PUERTO ESCONDIDO',		'PUERTO LIBERTADOR', 	'PURISIMA',		'SAHAGUN',		'SAN ANDRES SOTAVENTO',		'SAN ANTERO',		'SAN BERNARDO DEL VIENTO',		'SAN CARLOS',		'SAN JOSE DE URE',		'SAN PELAYO',		'TIERRALTA',	'TUCHIN',	'VALENCIA'],
    'Cundinamarca': ['AGUA DE DIOS',	'ALBAN',	'ANAPOIMA',	'ANOLAIMA',	'ARBELAEZ',	'BELTRAN',	'BITUIMA',  'BOGOTÁ', 'BOJACA', 	'CABRERA',	'CACHIPAY',	'CAJICA',	'CAPARRAPI',	'CAQUEZA',	'CARMEN DE CARUPA',	'CHAGUANI',	'CHIA', 'CHIPAQUE',	'CHOACHI',	'CHOCONTA',	'COGUA',	'COTA',	'CUCUNUBA',		'EL COLEGIO',	'EL PEÑON',	'EL ROSAL',	'FACATATIVA',	'FOMEQUE',	'FOSCA',	'FUNZA',	'FUQUENE',	'FUSAGASUGA',	'GACHALA',	'GACHANCIPA',	'GACHETA',	'GAMA',	'GIRARDOT',	'GRANADA',	'GUACHETA',	'GUADUAS',	'GUASCA',	'GUATAQUI',	'GUATAVITA',	'GUAYABAL DE SIQUIMA',	'GUAYABETAL', 'GUTIERREZ',	'JERUSALEN',	'JUNIN',	'LA CALERA',	'LA MESA',	'LA PALMA',	 'LA PEÑA',	'LA VEGA',	'LENGUAZAQUE',	'MACHETA',	'MADRID',	'MANTA',    'MEDINA',	'MOSQUERA',	'NARIÑO', 	'NEMOCON',	'NILO', 'NIMAIMA', 	'NOCAIMA',   'VENECIA',	'PACHO',	'PAIME',	'PANDI',	'PARATEBUENO',	'PASCA', 	'PUERTO SALGAR',	'PULI',	'QUEBRADANEGRA',	'QUETAME',	'QUIPILE',	'APULO',	'RICAURTE',	'SAN ANTONIO DE TEQUENDAMA', 	'SAN BERNARDO',	'SAN CAYETANO', 	'SAN FRANCISCO',	'SAN JUAN DE RIO SECO', 	'SASAIMA', 	'SESQUILE', 	'SIBATE',	'SILVANIA', 'SIMIJACA', 	'SOACHA', 	'SOPO', 'SUBACHOQUE', 	'SUESCA', 	'SUPATA', 	'SUSA',		'SUTATAUSA', 'TABIO', 	'TAUSA', 	'TENA',	'TENJO', 	'TIBACUY',	'TIBIRITA',	'TOCAIMA',	'TOCANCIPA',	'TOPAIPI',	'UBALA',	'UBAQUE',	'UBATE','UNE',	'UTICA',	'VERGARA',	'VIANI',	'VILLAGOMEZ',	'VILLAPINZON',	'VILLETA',	'VIOTA',	'YACOPI',	'ZIPACON',	'ZIPAQUIRA'],
    'Guainía': ['INIRIDA',		'BARRANCOMINAS',	'MAPIRIPANA',	'SAN FELIPE',	'PUERTO COLOMBIA',	'LA GUADALUPE',	'CACAHUAL',	'PANA PANA',	'MORICHAL'],
    'Guaviare': ['SAN JOSÉ DEL GUAVIARE', 'CALAMAR', 'EL RETORNO', 'MIRAFLORES'],
    'Huila': ['NEIVA',	'ACEVEDO',	'AGRADO',	'AIPE',	'ALGECIRAS',	'ALTAMIRA',	'BARAYA',	'CAMPOALEGRE',	'COLOMBIA',	'ELIAS',	'GARZON',	'GIGANTE',	'GUADALUPE',	'HOBO',	'IQUIRA',	'ISNOS',	'LA ARGENTINA',	'LA PLATA',	'NATAGA',	'OPORAPA',	'PAICOL',	'PALERMO',	'PALESTINA',	'PITAL',	'PITALITO',	'RIVERA',   'SALADOBLANCO',		'SAN AGUSTIN',	'SANTA MARIA',	'SUAZA',	'TARQUI', 	'TESALIA',	'TELLO',	'TERUEL',	'TIMANA',	'VILLAVIEJA',	'YAGUARA'],
    'Guajira': ['RIOHACHA',	'ALBANIA',	'BARRANCAS',	'DIBULLA',	'DISTRACCION',	'MOLINO',	'FONSECA',	'HATONUEVO',	'JAGUA DEL PILAR',	'MAICAO', 	'MANAURE',	  'SAN JUAN DEL CESAR',	   'URIBIA', 	'URUMITA',    'VILLANUEVA'],
    'Magdalena': ['SANTA MARTA','ALGARROBO', 	'ARACATACA', 	'ARIGUANI', 	'CERRO SAN ANTONIO', 	'CHIVOLO', 	'CIENAGA', 	'CONCORDIA', 	'EL BANCO', 	'EL PIÑON', 	'EL RETEN', 	'FUNDACION', 	'GUAMAL', 	'NUEVA GRANADA', 	'PEDRAZA', 	'PIJIÑO DEL CARMEN', 	'PIVIJAY', 	'PLATO', 	'PUEBLOVIEJO', 	'REMOLINO', 	'SABANAS DE SAN ANGEL', 	'SALAMINA', 	'SAN SEBASTIAN DE BUENAVISTA', 	'SAN ZENON', 	'SANTA ANA',	'SANTA BARBARA DE PINTO',	'SITIONUEVO', 	'TENERIFE', 	'ZAPAYAN', 	'ZONA BANANERA'],
    'Meta': ['VILLAVICENCIO', 	'ACACIAS', 	'BARRANCA DE UPIA', 	'CABUYARO', 	'CASTILLA LA NUEVA', 	'CUBARRAL', 	'CUMARAL', 	'EL CALVARIO', 	'EL CASTILLO', 		'EL DORADO', 	'FUENTE DE ORO', 	'GRANADA', 	'GUAMAL',   'MAPIRIPAN', 	'MESETAS', 	'LA MACARENA', 	'LA URIBE', 	'LEJANIAS', 	'PUERTO CONCORDIA', 	'PUERTO GAITAN',   	'PUERTO LOPEZ', 	'PUERTO LLERAS', 	'PUERTO RICO', 	'RESTREPO', 	'SAN CARLOS GUAROA', 	'SAN JUAN DE ARAMA', 	'SAN JUANITO', 	'SAN MARTIN',	'VISTA HERMOSA'],
    'Nariño': ['PASTO',	'ALBAN', 'ALDANA', 	'ANCUYA', 	'ARBOLEDA', 'BARBACOAS', 	'BELEN', 	'BUESACO', 	'COLON', 	'CONSACA', 	'CONTADERO', 	'CORDOBA',	'CUASPUD', 	'CUMBAL',	'CUMBITARA', 	'CHACHAGUI', 	'EL CHARCO', 	'EL PEÑOL', 'EL ROSARIO',	'EL TABLON DE GOMEZ', 	'EL TAMBO', 	'FUNES',	'GUACHUCAL',	'GUAITARILLA',	'GUALMATAN',	'ILES',  'IMUES', 	'IPIALES',	'LA CRUZ', 	'LA FLORIDA', 	'LA LLANADA', 	'LA TOLA',	'LA UNION',	'LEIVA', 	'LINARES', 	'LOS ANDES', 	'MAGUI',	'MALLAMA',	'MOSQUERA', 'OLAYA HERRERA', 	'OSPINA',	'FRANCISCO PIZARRO', 	'POLICARPA',	'POTOSI', 	'PROVIDENCIA', 	'PUERRES', 	'PUPIALES', 	'RICAURTE',	'ROBERTO PAYAN', 	'SAMANIEGO', 	'SANDONA', 	'SAN BERNARDO',     'SAN LORENZO', 	'SAN PABLO',	'SAN PEDRO DE CARTAGO',	'SANTA BARBARA',    'SANTACRUZ', 	'SAPUYES', 	'TAMINANGO', 	'TANGUA',   'TUMACO', 'TUQUERRES', 'YACUANQUER'],
    'Norte de Santander': ['CUCUTA',	'ABREGO',	'ARBOLEDAS', 	'BOCHALEMA', 	'BUCARASICA', 	'CACOTA', 	'CACHIRA', 	'CHINACOTA', 	'CHITAGA', 	'CONVENCION', 	'CUCUTILLA', 	'DURANIA', 	'EL CARMEN', 	'EL TARRA',		'EL ZULIA',	'GRAMALOTE', 	'HACARI', 	'HERRAN', 	'LABATECA',	'LA ESPERANZA',	'LA PLAYA',		'LOS PATIOS',	'LOURDES', 	'MUTISCUA', 	'OCAÑA',	'PAMPLONA', 'PAMPLONITA', 	'PUERTO SANTANDER',		'RAGONVALIA',		'SALAZAR',		'SAN CALIXTO',	'SAN CAYETANO', 	'SANTIAGO', 	'SARDINATA', 	'SILOS', 	'TEORAMA', 	'TIBU',	'TOLEDO',	'VILLA CARO', 	'VILLA DEL ROSARIO'],
    'Putumayo': ['MOCOA', 	'COLON', 	'ORITO', 	'PUERTO ASIS', 	'PUERTO CAICEDO', 	'PUERTO GUZMAN', 	'LEGUIZAMO', 	'SIBUNDOY', 	'SAN FRANCISCO',	'SAN MIGUEL', 	'SANTIAGO', 	'VALLE DEL GUAMUEZ', 	'VILLAGARZON'],
    'Quindío': ['ARMENIA', 	'BUENAVISTA', 	'CALARCÁ',	'CIRCASIA',	'CÓRDOBA',	'FILANDIA',	'GÉNOVA',	'LA TEBAIDA',	'MONTENEGRO',	'PIJAO','QUIMBAYA', 'SALENTO'],
    'Risaralda': ['PEREIRA', 'APIA', 'BALBOA', 'BELEN DE UMBRIA', 'DOS QUEBRADAS', 	'GUATICA', 	'LA CELIA', 	'LA VIRGINIA', 	'MARSELLA', 'MISTRATO', 	'PUEBLO RICO', 	'QUINCHIA', 	'SANTA ROSA DE CABAL', 	'SANTUARIO'],
    'San Andrés y Providencia': ['SAN ANDRÉS', 'PROVIDENCIA'],
    'Santander': ['BUCARAMANGA', 'AGUADA', 'ALBANIA', 'ARATOCA', 'BARBOSA', 'BARICHARA', 'BARRANCABERMEJA', 'BETULIA', 'BOLIVAR', 'CABRERA', 'CALIFORNIA', 'CAPITANEJO', 'CARCASI', 'CEPITA', 'CERRITO', 'CHARALA', 'CHARTA', 'CHIMA', 'CHIPATA', 'CIMITARRA', 'CONCEPCION', 'CONFINES', 'CONTRATACION', 'COROMORO', 'CURITI', 'EL CARMEN DE CHUCURI', 'EL GUACAMAYO', 'EL PEÑON', 'EL PLAYON', 'ENCINO', 'ENCISO', 'FLORIAN', 'FLORIDABLANCA', 'GALAN', 'GAMBITA', 'GIRON', 'GUACA', 'GUADALUPE', 'GUAPOTA', 'GUAVATA', 'GUEPSA', 'HATO', 'JESUS', 'MARIA', 'JORDAN', 'LA BELLEZA','LANDAZURI', 'LA PAZ', 'LEBRIJA', 'LOS SANTOS', 'MACARAVITA', 'MALAGA', 'MATANZA', 'MOGOTES', 'MOLAGAVITA', 'OCAMONTE', 'OIBA', 'ONZAGA', 'PALMAR', 'PALMAS DEL SOCORRO', 'PARAMO PIEDECUESTA', 'PINCHOTE', 'PUENTE NACIONAL', 'PUERTO PARRA', 'PUERTO WILCHES', 'RIONEGRO', 'SABANA DE TORRES', 'SAN ANDRES', 'SAN BENITO', 'SAN GIL', 'SAN JOAQUIN', 'SAN JOSE DE MIRANDA', 'SAN MIGUEL', 'SAN VICENTE DE CHUCURI', 'SANTA BARBARA', 'SANTA HELENA DEL OPON', 'SIMACOTA', 'SOCORRO', 'SUAITA', 'SUCRE', 'SURATA', 'TONA', 'VALLE DE SAN JOSE', 'VELEZ', 'VETAS', 'VILLANUEVA', 'ZAPATOCA'],
    'Sucre': ['SINCELEJO',	'BUENAVISTA',	'CAIMITO',	'COLOSO',	'COROZAL',	'COVEÑAS',	'CHALAN',	'EL ROBLE',	'GALERAS',	'GUARANDA',	'LA UNION',	'LOS PALMITOS',	'MAJAGUAL',	'MORROA',	'OVEJAS',	'PALMITO',	'SAMPUES',	'SAN BENITO ABAD', 	'SAN JUAN BETULIA',	'SAN MARCOS',	'SAN ONOFRE',	'SAN PEDRO', 	'SINCE','SANTIAGO DE TOLU', 'TOLU VIEJO'],
    'Tolima': ['IBAGUÉ',	'ALPUJARRA',	'ALVARADO',	'AMBALEMA',	'ANZOÁTEGUI',	'ARMERO', 	'ATACO',	'CAJAMARCA',    'CARMEN DE APICALÁ',	'CASABIANCA',	'CHAPARRAL',	'COELLO',  	'COYAIMA', 	'CUNDAY', 	'DOLORES',    'ESPINAL', 	'FALAN', 	'FLANDES',	'FRESNO',	'GUAMO',	'HERVEO', 	'HONDA',	'ICONONZO',	'LÉRIDA',	'LÍBANO',	'MARIQUITA',	'MELGAR', 'MURILLO',	'NATAGAIMA', 	'ORTEGA', 	'PALOCABILDO', 	'PIEDRAS', 	'PLANADAS', 'PRADO',	'PURIFICACIÓN', 	'RIOBLANCO', 	'RONCESVALLES',	'ROVIRA',	'SALDAÑA', 	'SAN ANTONIO', 	'SAN LUIS', 	'SANTA ISABEL', 	'SUÁREZ', 	'VALLE DE SAN JUAN',	'VENADILLO',	'VILLAHERMOSA',	'VILLARRICA'],
    'Valle del Cauca': ['CALI',	'ALCALA', 	'ANDALUCIA',	'ANSERMANUEVO',		'ARGELIA',	'BOLIVAR',	'BUENAVENTURA',	'BUGA',	'BUGALAGRANDE',	'CAICEDONIA',	'CALIMA',	'CANDELARIA',	'CARTAGO',	'DAGUA',	'EL AGUILA',	'EL CAIRO',	'EL CERRITO',	'EL DOVIO',	'FLORIDA',	'GINEBRA', 	'GUACARI',	'JAMUNDI',	'LA CUMBRE',	'LA UNION',	'LA VICTORIA',	'OBANDO',	'PALMIRA',	'PRADERA',	'RESTREPO', 'RIOFRIO', 	'ROLDANILLO', 	'SAN PEDRO', 	'SEVILLA',	'TORO', 	'TRUJILLO',	'TULUA', 	'ULLOA', 	'VERSALLES', 	'VIJES', 	'YOTOCO', 	'YUMBO',	'ZARZAL'],
    'Vaupés': ['MITU',	'CARURU',	'PACOA', 	'TARAIRA', 	'PAPUNAHUA', 	'YAVARATE'],
    'Vichada': ['CUMARIBO', 'LA PRIMAVERA', 'PUERTO CARREÑO', 'SANTA ROSALIA'],
}

nombres = {
    "rojo": "manzana",
    "naranja": "naranja",
    "amarillo": "limón",
    "verde": "kiwi",
    "azul": "arándano",
    "morado": "uva"
}


class Ventana():
    num_ventana = 0
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    nosemanas = ['SEM 1', 'SEM 2', 'SEM 3', 'SEM 4']
    presentacion = ['PP', 'BLOQUE', 'TROCEADA']

    def __init__(self, parent=None, root=None):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.frame.pack()

        # Creamos el canvas y la scrollbar
        self.canvas = tk.Canvas(self.frame, bg="white", width=580, height=800, scrollregion=(0, 0, 1000, 1800))
        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # TITULO AÑADIR ENTRADA
        self.titulo = tk.Label(self.canvas, text="AÑADIR ENTRADA", font=('Freehando521 BT', 24, 'bold'), bg='#28811D', fg='white', width='31', height='2')


        # CAPTURA DE DATOS
        semana = tk.StringVar()
        receptor = tk.StringVar()
        rmsk = tk.StringVar()
        talonario = tk.StringVar()
        remision = tk.StringVar()
        nombre = tk.StringVar()
        entidad = tk.StringVar()
        registro = tk.StringVar()
        vereda = tk.StringVar()
        transportador = tk.StringVar()
        placa = tk.StringVar()
        proveedor = tk.StringVar()
        self.id = 1
        self.calibre = tk.StringVar()
        self.ancho = tk.StringVar()
        self.largo = tk.StringVar()
        self.unds = tk.StringVar()


        # FORMULARIO TEXT
        #Autoincrementable
        self.num_ventana += 1
        self.lote_num = str(self.num_ventana).zfill(5)

        self.lote_label = tk.Label(self.canvas, text=f"LOTE N°: {self.lote_num}", font=('Freehando521 BT', 18), bg='white', fg='dark grey', width='15', height='2')
        
        self.mesingreso_label = tk.Label(self.canvas, text="Mes Ingreso:", font=('Freehando521 BT', 14), bg='white', fg='black', width='12', height='2')
        self.mesingreso_combobox = ttk.Combobox(self.canvas,values=self.meses, state="readonly")
        
        self.fechaingresoplanta_label = tk.Label(self.canvas, text="Fecha Ingreso a la Planta:", font=('Freehando521 BT', 14), bg='white', fg='black', width='20', height='2')
        self.fechaingresoplanta_entry = DateEntry(self.canvas, date_pattern='yyyy-mm-dd')
        
        self.fecharegistra_label = tk.Label(self.canvas, text="Fecha de la Operacion que se Registra:", font=('Freehando521 BT', 14, 'bold'), bg='white', fg='black', width='30', height='2')
        self.fechadesde_label = tk.Label(self.canvas, text="Desde", font=('Freehando521 BT', 14), bg='white', fg='black', width='5', height='2')
        self.fechadesde_entry = DateEntry(self.canvas, date_pattern='yyyy-mm-dd')
        self.fechahasta_label = tk.Label(self.canvas, text="Hasta", font=('Freehando521 BT', 14), bg='white', fg='black', width='5', height='2')
        self.fechahasta_entry = DateEntry(self.canvas, date_pattern='yyyy-mm-dd')

        self.semana_label = tk.Label(self.canvas, text="Semanas:", font=('Freehando521 BT', 14), bg='white', fg='black', width='8', height='2')
        self.semana_entry = tk.Entry(self.canvas, textvariable=semana, width="16", bg='light grey')
        self.ejemplosemana_label = tk.Label(self.canvas, text="Ej: SEM 01-09", font=('Freehando521 BT', 9, "italic"), bg='white', fg='black', width='11', height='2')

        self.nosemana_label = tk.Label(self.canvas, text="Semanas N°:", font=('Freehando521 BT', 14), bg='white', fg='black', width='10', height='2')
        self.nosemana_combobox = ttk.Combobox(self.canvas,values=self.nosemanas, state="readonly")

        self.receptor_label = tk.Label(self.canvas, text="Receptor:", font=('Freehando521 BT', 14), bg='white', fg='black', width='10', height='2')
        self.receptor_entry = tk.Entry(self.canvas, textvariable=receptor, width="30", bg='light grey')

        self.rmsk_label = tk.Label(self.canvas, text="RM SK N°:", font=('Freehando521 BT', 14), bg='white', fg='black', width='8', height='2')
        self.rmsk_entry = tk.Entry(self.canvas, textvariable=rmsk, width="15", bg='light grey')

        self.talonario_label = tk.Label(self.canvas, text="Consecutivo de Talonario N°:", font=('Freehando521 BT', 14), bg='white', fg='black', width='22', height='2')
        self.talonario_entry = tk.Entry(self.canvas, textvariable=talonario, width="20", bg='light grey')

        self.remision_label = tk.Label(self.canvas, text="Remision N°:", font=('Freehando521 BT', 14), bg='white', fg='black', width='10', height='2')
        self.remision_entry = tk.Entry(self.canvas, textvariable=remision, width="20", bg='light grey')

        self.nombre_label = tk.Label(self.canvas, text="Nombre o Razon Social del Titular del Registro:", font=('Freehando521 BT', 14), bg='white', fg='black', width='36', height='2')
        self.nombre_entry = tk.Entry(self.canvas, textvariable=nombre, width="40", bg='light grey')

        self.entidad_label = tk.Label(self.canvas, text="Entidad que Expide:", font=('Freehando521 BT', 14), bg='white', fg='black', width='15', height='2')
        self.entidad_entry = tk.Entry(self.canvas, textvariable=entidad, width="10", bg='light grey')

        self.registro_label = tk.Label(self.canvas, text="Registro N°:", font=('Freehando521 BT', 14), bg='white', fg='black', width='9', height='2')
        self.registro_entry = tk.Entry(self.canvas, textvariable=registro, width="32", bg='light grey')

        self.procedencia_label = tk.Label(self.canvas, text="Procedencia:", font=('Freehando521 BT', 14, 'bold'), bg='white', fg='black', width='10', height='2')
        self.departamento_label = tk.Label(self.canvas, text="Departamento", font=('Freehando521 BT', 14), bg='white', fg='black', width='11', height='2')
        self.departamento_combobox = ttk.Combobox(self.canvas,values=list(departamentos.keys()), state="readonly")
        self.municipio_label = tk.Label(self.canvas, text="Municipio", font=('Freehando521 BT', 14), bg='white', fg='black', width='7', height='2')
        self.municipio_combobox = ttk.Combobox(self.canvas,values=self, state="readonly")
        self.vereda_label = tk.Label(self.canvas, text="Vereda", font=('Freehando521 BT', 14), bg='white', fg='black', width='5', height='2')
        self.vereda_entry = tk.Entry(self.canvas, textvariable=vereda, width="32", bg='light grey')

        self.transportador_label = tk.Label(self.canvas, text="Transportador:", font=('Freehando521 BT', 14), bg='white', fg='black', width='11', height='2')
        self.transportador_entry = tk.Entry(self.canvas, textvariable=transportador, width="32", bg='light grey')

        self.placa_label = tk.Label(self.canvas, text="Placa Vehiculo:", font=('Freehando521 BT', 14), bg='white', fg='black', width='11', height='2')
        self.placa_entry = tk.Entry(self.canvas, textvariable=placa, width="12", bg='light grey')

        self.proveedor_label = tk.Label(self.canvas, text="Proveedor para M.I:", font=('Freehando521 BT', 14), bg='white', fg='black', width='15', height='2')
        self.proveedor_entry = tk.Entry(self.canvas, textvariable=proveedor, width="25", bg='light grey')

        self.especie_label = tk.Label(self.canvas, text="Especie:", font=('Freehando521 BT', 14, 'bold'), bg='white', fg='black', width='6', height='2')
        self.comun_label = tk.Label(self.canvas, text="Nombre Común", font=('Freehando521 BT', 14), bg='white', fg='black', width='12', height='2')
        self.nombres = list(nombres.keys())
        self.comun_combobox = ttk.Combobox(self.canvas,values=self.nombres, state="readonly")
        self.presentacion_label = tk.Label(self.canvas, text="Presentacion:", font=('Freehando521 BT', 14), bg='white', fg='black', width='12', height='2')
        self.presentacion_combobox = ttk.Combobox(self.canvas,values=self.presentacion, state="readonly")
        self.cientifico_label = tk.Label(self.canvas, text="Nombre Cientifico", font=('Freehando521 BT', 14), bg='white', fg='black', width='14', height='2')
        self.cientificoname_label = tk.Label(self.canvas, text="", font=('Freehando521 BT', 14), bg='white', fg='black', width='14', height='2')


        self.medidas_label = tk.Label(self.canvas, text="Medidas:", font=('Freehando521 BT', 14, 'bold'), bg='white', fg='black', width='7', height='2')
        self.calibre_label = tk.Label(self.canvas, text="Calibre", font=('Freehando521 BT', 13), bg='white', fg='black', width='7', height='2')
        self.calibre_entry = tk.Entry(self.canvas, textvariable=self.calibre, width="12", bg='light grey')
        self.ancho_label = tk.Label(self.canvas, text="Ancho", font=('Freehando521 BT', 13), bg='white', fg='black', width='7', height='2')
        self.ancho_entry = tk.Entry(self.canvas, textvariable=self.ancho, width="12", bg='light grey')
        self.largo_label = tk.Label(self.canvas, text="Largo", font=('Freehando521 BT', 13), bg='white', fg='black', width='7', height='2')
        self.largo_entry = tk.Entry(self.canvas, textvariable=self.largo, width="12", bg='light grey')
        self.unidades_label = tk.Label(self.canvas, text="Unidades", font=('Freehando521 BT', 13), bg='white', fg='black', width='7', height='2')
        self.unidades_entry = tk.Entry(self.canvas, textvariable=self.unds, width="12", bg='light grey')
        self.agregar_btn = tk.Button(self.canvas, text="Agregar", command=self.agregar_dato)
        self.eliminar_btn = tk.Button(self.canvas, text="Eliminar", command=self.delete_row)

        self.entrada_btn = tk.Button(self.canvas, text="AÑADIR", font=('Freehando521 BT', 10, 'bold'), command=self, bg='#28811D', bd=0, fg='white' ,width=14, height=2)


        def on_select_departamento(event):
            # Si el departamento seleccionado es válido
            if self.departamento_combobox.get() in departamentos:
                # Vaciamos el combobox de municipios
                self.municipio_combobox.set('')
                self.municipio_combobox['values'] = departamentos[self.departamento_combobox.get()]

        # Añadimos un callback para actualizar los municipios cuando se cambia el departamento
        self.departamento_combobox.bind("<<ComboboxSelected>>", on_select_departamento)


        def mostrar_nombres(*args):
            comun = self.comun_combobox.get().lower()
            cientifico = nombres.get(comun)
            if cientifico:
                self.cientificoname_label.config(text=cientifico)
            else:
                self.cientificoname_label.config(text="No se encontró ninguna fruta para ese color.")
        self.comun_combobox.bind("<<ComboboxSelected>>", mostrar_nombres)



         # Creamos el treeview y definimos las columnas
        self.treeview = tk.ttk.Treeview(self.canvas, columns=("calibre", "ancho", "largo", "unidades"), selectmode="browse")

        # Definimos los encabezados de las columnas
        self.treeview.heading("#0", text="ID", anchor="center", command=lambda: self.treeview.focus(""))
        self.treeview.column("#0", width=70)
        self.treeview.heading("calibre", text="Calibre", anchor="center", command=lambda: self.treeview.focus(""))
        self.treeview.column("calibre", width=106)
        self.treeview.heading("ancho", text="Ancho", anchor="center", command=lambda: self.treeview.focus(""))
        self.treeview.column("ancho", width=106)
        self.treeview.heading("largo", text="Largo", anchor="center", command=lambda: self.treeview.focus(""))
        self.treeview.column("largo", width=106)
        self.treeview.heading("unidades", text="Unidades", anchor="center", command=lambda: self.treeview.focus(""))
        self.treeview.column("unidades", width=106)
        


        # Agregamos los elementos al canvas
        self.canvas.create_window((0, 0), window=self.titulo, anchor="nw")
        self.canvas.create_window((40, 80), window=self.lote_label, anchor="nw")
        self.canvas.create_window((25, 150), window=self.mesingreso_label, anchor="nw")
        self.canvas.create_window((180, 165), window=self.mesingreso_combobox, anchor="nw")
        self.canvas.create_window((35, 200), window=self.fechaingresoplanta_label, anchor="nw")
        self.canvas.create_window((280, 215), window=self.fechaingresoplanta_entry, anchor="nw")
        self.canvas.create_window((40, 250), window=self.fecharegistra_label , anchor="nw")
        self.canvas.create_window((100, 290), window=self.fechadesde_label , anchor="nw")
        self.canvas.create_window((290, 290), window=self.fechahasta_label , anchor="nw")
        self.canvas.create_window((180, 305), window=self.fechadesde_entry, anchor="nw")
        self.canvas.create_window((370, 305), window=self.fechahasta_entry, anchor="nw")
        self.canvas.create_window((35, 360), window=self.semana_label, anchor="nw")
        self.canvas.create_window((140, 375), window=self.semana_entry, anchor="nw")
        self.canvas.create_window((250, 365), window=self.ejemplosemana_label, anchor="nw")
        self.canvas.create_window((40, 400), window=self.nosemana_label, anchor="nw")
        self.canvas.create_window((165, 415), window=self.nosemana_combobox, anchor="nw")
        self.canvas.create_window((25, 445), window=self.receptor_label, anchor="nw")
        self.canvas.create_window((150, 460), window=self.receptor_entry, anchor="nw")
        self.canvas.create_window((40, 490), window=self.rmsk_label, anchor="nw")
        self.canvas.create_window((150, 505), window=self.rmsk_entry, anchor="nw")
        self.canvas.create_window((40, 530), window=self.talonario_label, anchor="nw")
        self.canvas.create_window((300, 545), window=self.talonario_entry, anchor="nw")
        self.canvas.create_window((40, 575), window=self.remision_label, anchor="nw")
        self.canvas.create_window((170, 590), window=self.remision_entry, anchor="nw")
        self.canvas.create_window((40, 620), window=self.nombre_label, anchor="nw")
        self.canvas.create_window((60, 665), window=self.nombre_entry, anchor="nw")
        self.canvas.create_window((40, 690), window=self.entidad_label, anchor="nw")
        self.canvas.create_window((220, 705), window=self.entidad_entry, anchor="nw")
        self.canvas.create_window((40, 730), window=self.registro_label, anchor="nw")
        self.canvas.create_window((160, 745), window=self.registro_entry, anchor="nw")
        self.canvas.create_window((40, 785), window=self.procedencia_label, anchor="nw")
        self.canvas.create_window((50, 820), window=self.departamento_label, anchor="nw")
        self.canvas.create_window((185, 835), window=self.departamento_combobox, anchor="nw")
        self.canvas.create_window((340, 820), window=self.municipio_label, anchor="nw")
        self.canvas.create_window((430, 835), window=self.municipio_combobox, anchor="nw")
        self.canvas.create_window((130, 860), window=self.vereda_label, anchor="nw")
        self.canvas.create_window((200, 875), window=self.vereda_entry, anchor="nw")
        self.canvas.create_window((40, 910), window=self.transportador_label, anchor="nw")
        self.canvas.create_window((190, 925), window=self.transportador_entry, anchor="nw")
        self.canvas.create_window((40, 945), window=self.placa_label, anchor="nw")
        self.canvas.create_window((190, 960), window=self.placa_entry, anchor="nw")
        self.canvas.create_window((40, 985), window=self.proveedor_label, anchor="nw")
        self.canvas.create_window((230, 1000), window=self.proveedor_entry, anchor="nw")
        self.canvas.create_window((40, 1045), window=self.especie_label, anchor="nw")
        self.canvas.create_window((60, 1085), window=self.comun_label, anchor="nw")
        self.canvas.create_window((200, 1100), window=self.comun_combobox, anchor="nw")
        self.canvas.create_window((60, 1135), window=self.cientifico_label, anchor="nw")
        self.canvas.create_window((220, 1135), window=self.cientificoname_label, anchor="nw")

        self.canvas.create_window((55, 1185), window=self.presentacion_label, anchor="nw")
        self.canvas.create_window((200, 1200), window=self.presentacion_combobox, anchor="nw")


        self.canvas.create_window((40, 1250), window=self.medidas_label, anchor="nw")
        self.canvas.create_window((65, 1290), window=self.calibre_label, anchor="nw")
        self.canvas.create_window((65, 1330), window=self.calibre_entry, anchor="nw")
        self.canvas.create_window((185, 1290), window=self.ancho_label, anchor="nw")
        self.canvas.create_window((185, 1330), window=self.ancho_entry, anchor="nw")
        self.canvas.create_window((305, 1290), window=self.largo_label, anchor="nw")
        self.canvas.create_window((305, 1330), window=self.largo_entry, anchor="nw")
        self.canvas.create_window((425, 1290), window=self.unidades_label, anchor="nw")
        self.canvas.create_window((425, 1330), window=self.unidades_entry, anchor="nw")
        self.canvas.create_window((220, 1380), window=self.agregar_btn, anchor="nw")
        self.canvas.create_window((300, 1380), window=self.eliminar_btn, anchor="nw")
        self.canvas.create_window((40, 1430), window=self.treeview, anchor="nw")
        self.canvas.create_window((240, 1720), window=self.entrada_btn, anchor="nw")



        # Colocamos el canvas y la scrollbar en el frame
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Centramos la ventana en la pantalla
        window_width = root.winfo_screenwidth()
        window_height = root.winfo_screenheight()
        x_cordinate = int((window_width / 2) - (500 / 2))
        y_cordinate = int((window_height / 2) - (800 / 2))
        root.geometry("{}x{}+{}+{}".format(600, 750, x_cordinate, y_cordinate))

    def agregar_dato(self):
        # Obtener los datos ingresados en la entrada de calibre y ancho
        calibre = self.calibre.get()
        ancho = self.ancho.get()
        largo = self.largo.get()
        unds = self.unds.get()

        # Insertar los datos en el treeview
        self.treeview.insert("", "end", text=str(self.id), values=(calibre, ancho, largo, unds, ""))
        self.id += 1
        self.calibre_entry.delete(0, "end")
        self.ancho_entry.delete(0, "end")
        self.largo_entry.delete(0, "end")
        self.unidades_entry.delete(0, "end")

    def delete_row(self):
        selected = self.treeview.selection()
        for item in selected:
            self.treeview.delete(item)



root = tk.Tk()
root.title("Maderas Industriales")
root.config(bg='white')
root.iconbitmap("C:/Users/Usuario/Desktop/Proyecto INCO/M.I software/logoico.ico")
root.resizable(False, False)
root = Ventana()
root.mainloop()