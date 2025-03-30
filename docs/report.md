# 📋 Informe Consolidado de Auditoría

## 🔹 Ingesta

```
📋 Informe de Ingesta Global de Países

🌍 Total países: 250
📝 Columnas: pais, capital, region, subregion, poblacion, area
```

## 🔹 Limpieza

```
📋 **Informe de Limpieza de Datos**

Número total de registros: 250
Número de valores nulos por columna:
pais         0
capital      4
region       0
subregion    5
poblacion    0
area         0
dtype: int64
Número de registros duplicados: 0

✅ Número de registros después de limpieza: 250
```

## 🔹 Enriquecimiento

```
📋 **Informe de Enriquecimiento de Datos**

🔢 Registros base: 250
🌍 Enriquecimiento con coordenadas geográficas aplicado.
🔢 Registros finales: 250
```

## 🔍 Vista Previa de la Tabla Enriquecida

A continuación se muestra una vista previa de los primeros registros del dataset enriquecido:


| pais                                         | capital                   | region    | subregion                 |   poblacion |             area |    latitud |     longitud |
|----------------------------------------------|---------------------------|-----------|---------------------------|-------------|------------------|------------|--------------|
| South Georgia                                | King Edward Point         | Antarctic | nan                       |          30 |   3903           |  76.1367   |  -81.0516    |
| Grenada                                      | St. George's              | Americas  | Caribbean                 |      112519 |    344           |  12.0535   |  -61.7518    |
| Switzerland                                  | Bern                      | Europe    | Western Europe            |     8654622 |  41284           |  46.9485   |    7.45217   |
| Sierra Leone                                 | Freetown                  | Africa    | Western Africa            |     7976985 |  71740           |   8.479    |  -13.268     |
| Hungary                                      | Budapest                  | Europe    | Central Europe            |     9749763 |  93028           |  47.4814   |   19.1461    |
| Taiwan                                       | Taipei                    | Asia      | Eastern Asia              |    23503349 |  36193           |  25.0375   |  121.564     |
| Wallis and Futuna                            | Mata-Utu                  | Oceania   | Polynesia                 |       11750 |    142           | -13.282    | -176.174     |
| Barbados                                     | Bridgetown                | Americas  | Caribbean                 |      287371 |    430           |  13.0978   |  -59.6184    |
| Pitcairn Islands                             | Adamstown                 | Oceania   | Polynesia                 |          56 |     47           | -25.0667   | -130.1       |
| Ivory Coast                                  | Yamoussoukro              | Africa    | Western Africa            |    26378275 | 322463           |   6.82001  |   -5.2776    |
| Tunisia                                      | Tunis                     | Africa    | Northern Africa           |    11818618 | 163610           |  36.8002   |   10.1858    |
| Italy                                        | Rome                      | Europe    | Southern Europe           |    59554023 | 301336           |  41.8933   |   12.4829    |
| Benin                                        | Porto-Novo                | Africa    | Western Africa            |    12123198 | 112622           |   6.49907  |    2.62534   |
| Indonesia                                    | Jakarta                   | Asia      | South-Eastern Asia        |   273523621 |      1.90457e+06 |  -6.1754   |  106.827     |
| Cape Verde                                   | Praia                     | Africa    | Western Africa            |      555988 |   4033           |  14.9163   |  -23.5095    |
| Saint Kitts and Nevis                        | Basseterre                | Americas  | Caribbean                 |       53192 |    261           |  17.2961   |  -62.7223    |
| Laos                                         | Vientiane                 | Asia      | South-Eastern Asia        |     7275556 | 236800           |  17.9641   |  102.613     |
| Caribbean Netherlands                        | Kralendijk                | Americas  | Caribbean                 |       25987 |    328           |  12.1473   |  -68.274     |
| Uganda                                       | Kampala                   | Africa    | Eastern Africa            |    45741000 | 241550           |   0.317714 |   32.5814    |
| Andorra                                      | Andorra la Vella          | Europe    | Southern Europe           |       77265 |    468           |  42.4979   |    1.50323   |
| Burundi                                      | Gitega                    | Africa    | Eastern Africa            |    11890781 |  27834           |  -3.4285   |   29.925     |
| South Africa                                 | Pretoria                  | Africa    | Southern Africa           |    59308690 |      1.22104e+06 | -25.7459   |   28.1879    |
| France                                       | Paris                     | Europe    | Western Europe            |    67391582 | 551695           |  48.8535   |    2.34839   |
| Libya                                        | Tripoli                   | Africa    | Northern Africa           |     6871287 |      1.75954e+06 |  32.8967   |   13.1778    |
| Mexico                                       | Mexico City               | Americas  | North America             |   128932753 |      1.96438e+06 |  19.3208   |  -99.1515    |
| Gabon                                        | Libreville                | Africa    | Middle Africa             |     2225728 | 267668           |   0.408652 |    9.44188   |
| Northern Mariana Islands                     | Saipan                    | Oceania   | Micronesia                |       57557 |    464           |  15.191    |  145.747     |
| North Macedonia                              | Skopje                    | Europe    | Southeast Europe          |     2077132 |  25713           |  41.9962   |   21.4319    |
| China                                        | Beijing                   | Asia      | Eastern Asia              |  1402112000 |      9.70696e+06 |  40.1906   |  116.412     |
| Yemen                                        | Sana'a                    | Asia      | Western Asia              |    29825968 | 527968           |  15.35     |   44.2       |
| Saint Barthélemy                             | Gustavia                  | Americas  | Caribbean                 |        4255 |     21           |  17.8957   |  -62.8508    |
| Guernsey                                     | St. Peter Port            | Europe    | Northern Europe           |       62999 |     78           |  49.4568   |   -2.539     |
| Solomon Islands                              | Honiara                   | Oceania   | Melanesia                 |      686878 |  28896           |  -9.43108  |  159.955     |
| Svalbard and Jan Mayen                       | Longyearbyen              | Europe    | Northern Europe           |        2562 |  61399           |  78.2232   |   15.6464    |
| Faroe Islands                                | Tórshavn                  | Europe    | Northern Europe           |       48865 |   1393           |  62.0101   |   -6.77157   |
| Uzbekistan                                   | Tashkent                  | Asia      | Central Asia              |    34232050 | 447400           |  41.3123   |   69.2787    |
| Egypt                                        | Cairo                     | Africa    | Northern Africa           |   102334403 |      1.00245e+06 |  30.0444   |   31.2357    |
| Senegal                                      | Dakar                     | Africa    | Western Africa            |    16743930 | 196722           |  14.6934   |  -17.4479    |
| Sri Lanka                                    | Sri Jayawardenepura Kotte | Asia      | Southern Asia             |    21919000 |  65610           |   6.88832  |   79.9187    |
| Palestine                                    | Ramallah                  | Asia      | Western Asia              |     4803269 |   6220           |  31.8978   |   35.1924    |
| Bangladesh                                   | Dhaka                     | Asia      | Southern Asia             |   164689383 | 147570           |  23.7644   |   90.389     |
| Peru                                         | Lima                      | Americas  | South America             |    32971846 |      1.28522e+06 | -12.0621   |  -77.0365    |
| Singapore                                    | Singapore                 | Asia      | South-Eastern Asia        |     5685807 |    710           |   1.28992  |  103.852     |
| Turkey                                       | Ankara                    | Asia      | Western Asia              |    84339067 | 783562           |  39.9208   |   32.854     |
| Afghanistan                                  | Kabul                     | Asia      | Southern Asia             |    40218234 | 652230           |  34.5266   |   69.1849    |
| Aruba                                        | Oranjestad                | Americas  | Caribbean                 |      106766 |    180           |  12.5201   |  -70.0371    |
| Cook Islands                                 | Avarua                    | Oceania   | Polynesia                 |       18100 |    236           | -21.2075   | -159.771     |
| United Kingdom                               | London                    | Europe    | Northern Europe           |    67215293 | 242900           |  51.5074   |   -0.127765  |
| Zambia                                       | Lusaka                    | Africa    | Eastern Africa            |    18383956 | 752612           | -15.4163   |   28.2818    |
| Finland                                      | Helsinki                  | Europe    | Northern Europe           |     5530719 | 338424           |  60.1675   |   24.9427    |
| Niger                                        | Niamey                    | Africa    | Western Africa            |    24206636 |      1.267e+06   |  13.5248   |    2.10982   |
| Christmas Island                             | Flying Fish Cove          | Oceania   | Australia and New Zealand |        2072 |    135           | -10.4213   |  105.674     |
| Tokelau                                      | Fakaofo                   | Oceania   | Polynesia                 |        1411 |     12           |  -9.37356  | -171.241     |
| Guinea-Bissau                                | Bissau                    | Africa    | Western Africa            |     1967998 |  36125           |  11.8613   |  -15.5831    |
| Azerbaijan                                   | Baku                      | Asia      | Western Asia              |    10110116 |  86600           |  40.3756   |   49.8328    |
| Réunion                                      | Saint-Denis               | Africa    | Eastern Africa            |      840974 |   2511           |  48.9358   |    2.35802   |
| Djibouti                                     | Djibouti                  | Africa    | Eastern Africa            |      988002 |  23200           |  11.8146   |   42.8453    |
| North Korea                                  | Pyongyang                 | Asia      | Eastern Asia              |    25778815 | 120538           |  39.0168   |  125.747     |
| Mauritius                                    | Port Louis                | Africa    | Eastern Africa            |     1265740 |   2040           | -20.1625   |   57.5028    |
| Montserrat                                   | Plymouth                  | Americas  | Caribbean                 |        4922 |    102           |  50.3714   |   -4.14245   |
| United States Virgin Islands                 | Charlotte Amalie          | Americas  | Caribbean                 |      106290 |    347           |  18.3419   |  -64.9307    |
| Colombia                                     | Bogotá                    | Americas  | South America             |    50882884 |      1.14175e+06 |   4.65338  |  -74.0836    |
| Greece                                       | Athens                    | Europe    | Southern Europe           |    10715549 | 131990           |  37.9756   |   23.7348    |
| Croatia                                      | Zagreb                    | Europe    | Southeast Europe          |     4047200 |  56594           |  45.8131   |   15.9773    |
| Morocco                                      | Rabat                     | Africa    | Northern Africa           |    36910558 | 446550           |  33.9852   |   -6.84614   |
| Algeria                                      | Algiers                   | Africa    | Northern Africa           |    44700000 |      2.38174e+06 |  36.7729   |    3.05884   |
| Antarctica                                   | Algiers                   | Antarctic | Northern Africa           |        1000 |      1.4e+07     |  36.7729   |    3.05884   |
| Netherlands                                  | Amsterdam                 | Europe    | Western Europe            |    16655799 |  41850           |  52.3731   |    4.89245   |
| Sudan                                        | Khartoum                  | Africa    | Northern Africa           |    43849269 |      1.88607e+06 |  15.5636   |   32.5349    |
| Fiji                                         | Suva                      | Oceania   | Melanesia                 |      896444 |  18272           | -18.1416   |  178.442     |
| Liechtenstein                                | Vaduz                     | Europe    | Western Europe            |       38137 |    160           |  47.1393   |    9.5228    |
| Nepal                                        | Kathmandu                 | Asia      | Southern Asia             |    29136808 | 147181           |  27.7083   |   85.3206    |
| Puerto Rico                                  | San Juan                  | Americas  | Caribbean                 |     3194034 |   8870           |  18.3842   |  -66.0534    |
| Georgia                                      | Tbilisi                   | Asia      | Western Asia              |     3714000 |  69700           |  41.6935   |   44.8014    |
| Pakistan                                     | Islamabad                 | Asia      | Southern Asia             |   220892331 | 881912           |  33.6938   |   73.0652    |
| Monaco                                       | Monaco                    | Europe    | Western Europe            |       39244 |      2.02        |  43.7311   |    7.41976   |
| Botswana                                     | Gaborone                  | Africa    | Southern Africa           |     2351625 | 582000           | -24.6581   |   25.9088    |
| Lebanon                                      | Beirut                    | Asia      | Western Asia              |     6825442 |  10452           |  33.8892   |   35.5026    |
| Papua New Guinea                             | Port Moresby              | Oceania   | Melanesia                 |     8947027 | 462840           |  -9.47433  |  147.16      |
| Mayotte                                      | Mamoudzou                 | Africa    | Eastern Africa            |      226915 |    374           | -12.7804   |   45.228     |
| Dominican Republic                           | Santo Domingo             | Americas  | Caribbean                 |    10847904 |  48671           |  18.4802   |  -69.9421    |
| Norfolk Island                               | Kingston                  | Oceania   | Australia and New Zealand |        2302 |     36           |  17.9712   |  -76.7928    |
| Bouvet Island                                | Kingston                  | Antarctic | Australia and New Zealand |           0 |     49           |  17.9712   |  -76.7928    |
| Qatar                                        | Doha                      | Asia      | Western Asia              |     2881060 |  11586           |  25.2856   |   51.5264    |
| Madagascar                                   | Antananarivo              | Africa    | Eastern Africa            |    27691019 | 587041           | -18.91     |   47.5256    |
| India                                        | New Delhi                 | Asia      | Southern Asia             |  1380004385 |      3.28759e+06 |  28.6431   |   77.2193    |
| Syria                                        | Damascus                  | Asia      | Western Asia              |    17500657 | 185180           |  33.5131   |   36.3096    |
| Montenegro                                   | Podgorica                 | Europe    | Southeast Europe          |      621718 |  13812           |  42.4415   |   19.2621    |
| Eswatini                                     | Mbabane                   | Africa    | Southern Africa           |     1160164 |  17364           | -26.3257   |   31.1447    |
| Paraguay                                     | Asunción                  | Americas  | South America             |     7132530 | 406752           | -25.28     |  -57.6344    |
| El Salvador                                  | San Salvador              | Americas  | Central America           |     6486201 |  21041           |  13.699    |  -89.1914    |
| Ukraine                                      | Kyiv                      | Europe    | Eastern Europe            |    44134693 | 603500           |  50.45     |   30.5241    |
| Isle of Man                                  | Douglas                   | Europe    | Northern Europe           |       85032 |    572           |  39.7628   |  -88.2171    |
| Namibia                                      | Windhoek                  | Africa    | Southern Africa           |     2540916 | 825615           | -22.5776   |   17.0773    |
| United Arab Emirates                         | Abu Dhabi                 | Asia      | Western Asia              |     9890400 |  83600           |  24.4538   |   54.3774    |
| Bulgaria                                     | Sofia                     | Europe    | Southeast Europe          |     6927288 | 110879           |  42.6977   |   23.3217    |
| Greenland                                    | Nuuk                      | Americas  | North America             |       56367 |      2.16609e+06 |  64.1767   |  -51.7359    |
| Germany                                      | Berlin                    | Europe    | Western Europe            |    83240525 | 357114           |  52.5109   |   13.3989    |
| Cambodia                                     | Phnom Penh                | Asia      | South-Eastern Asia        |    16718971 | 181035           |  11.5683   |  104.922     |
| Iraq                                         | Baghdad                   | Asia      | Western Asia              |    40222503 | 438317           |  33.3062   |   44.3872    |
| French Southern and Antarctic Lands          | Port-aux-Français         | Antarctic | Western Asia              |         400 |   7747           | -49.3498   |   70.22      |
| Sweden                                       | Stockholm                 | Europe    | Northern Europe           |    10353442 | 450295           |  59.3251   |   18.0711    |
| Cuba                                         | Havana                    | Americas  | Caribbean                 |    11326616 | 109884           |  23.1353   |  -82.359     |
| Kyrgyzstan                                   | Bishkek                   | Asia      | Central Asia              |     6591600 | 199951           |  42.8778   |   74.6067    |
| Russia                                       | Moscow                    | Europe    | Eastern Europe            |   144104080 |      1.70982e+07 |  55.6256   |   37.6064    |
| Malaysia                                     | Kuala Lumpur              | Asia      | South-Eastern Asia        |    32365998 | 330803           |   3.15266  |  101.702     |
| São Tomé and Príncipe                        | São Tomé                  | Africa    | Middle Africa             |      219161 |    964           |   0.338924 |    6.7313    |
| Cyprus                                       | Nicosia                   | Europe    | Southern Europe           |     1207361 |   9251           |  35.1747   |   33.3639    |
| Canada                                       | Ottawa                    | Americas  | North America             |    38005238 |      9.98467e+06 |  45.4209   |  -75.6901    |
| Malawi                                       | Lilongwe                  | Africa    | Eastern Africa            |    19129955 | 118484           | -13.9875   |   33.7681    |
| Saudi Arabia                                 | Riyadh                    | Asia      | Western Asia              |    34813867 |      2.14969e+06 |  24.6389   |   46.716     |
| Bosnia and Herzegovina                       | Sarajevo                  | Europe    | Southeast Europe          |     3280815 |  51209           |  43.852    |   18.3867    |
| Ethiopia                                     | Addis Ababa               | Africa    | Eastern Africa            |   114963583 |      1.1043e+06  |   9.03583  |   38.7524    |
| Spain                                        | Madrid                    | Europe    | Southern Europe           |    47351567 | 505992           |  40.4167   |   -3.70358   |
| Slovenia                                     | Ljubljana                 | Europe    | Central Europe            |     2100126 |  20273           |  46.05     |   14.5069    |
| Oman                                         | Muscat                    | Asia      | Western Asia              |     5106622 | 309500           |  23.5882   |   58.3829    |
| Saint Pierre and Miquelon                    | Saint-Pierre              | Americas  | North America             |        6069 |    242           |  48.3833   |    7.47187   |
| Macau                                        | Saint-Pierre              | Asia      | Eastern Asia              |      649342 |     30           |  48.3833   |    7.47187   |
| San Marino                                   | City of San Marino        | Europe    | Southern Europe           |       33938 |     61           |  43.9364   |   12.4467    |
| Lesotho                                      | Maseru                    | Africa    | Southern Africa           |     2142252 |  30355           | -29.3101   |   27.4782    |
| Marshall Islands                             | Majuro                    | Oceania   | Micronesia                |       59194 |    181           |   7.09099  |  171.382     |
| Sint Maarten                                 | Philipsburg               | Americas  | Caribbean                 |       40812 |     34           |  18.0251   |  -63.0483    |
| Iceland                                      | Reykjavik                 | Europe    | Northern Europe           |      366425 | 103000           |  64.146    |  -21.9422    |
| Luxembourg                                   | Luxembourg                | Europe    | Western Europe            |      632275 |   2586           |  49.8159   |    6.12968   |
| Argentina                                    | Buenos Aires              | Americas  | South America             |    45376763 |      2.7804e+06  | -34.6084   |  -58.4441    |
| Turks and Caicos Islands                     | Cockburn Town             | Americas  | Caribbean                 |       38718 |    948           |  21.4608   |  -71.14      |
| Nauru                                        | Yaren                     | Oceania   | Micronesia                |       10834 |     21           |  -0.547106 |  166.916     |
| Cocos (Keeling) Islands                      | West Island               | Oceania   | Australia and New Zealand |         544 |     14           | -12.1459   |   96.8423    |
| Western Sahara                               | El Aaiún                  | Africa    | Northern Africa           |      510713 | 266000           |  27.1545   |  -13.1954    |
| Dominica                                     | Roseau                    | Americas  | Caribbean                 |       71991 |    751           |  48.771    |  -95.7698    |
| Costa Rica                                   | San José                  | Americas  | Central America           |     5094114 |  51100           |  37.3362   | -121.891     |
| Australia                                    | Canberra                  | Oceania   | Australia and New Zealand |    25687041 |      7.69202e+06 | -35.2976   |  149.101     |
| Thailand                                     | Bangkok                   | Asia      | South-Eastern Asia        |    69799978 | 513120           |  13.7525   |  100.494     |
| Haiti                                        | Port-au-Prince            | Americas  | Caribbean                 |    11402533 |  27750           |  18.5473   |  -72.3396    |
| Tuvalu                                       | Funafuti                  | Oceania   | Polynesia                 |       11792 |     26           |  -8.51996  |  179.198     |
| Honduras                                     | Tegucigalpa               | Americas  | Central America           |     9904608 | 112492           |  14.1057   |  -87.204     |
| Equatorial Guinea                            | Malabo                    | Africa    | Middle Africa             |     1402985 |  28051           |   3.74188  |    8.77407   |
| Saint Lucia                                  | Castries                  | Americas  | Caribbean                 |      183629 |    616           |  43.6779   |    3.98689   |
| French Polynesia                             | Papeetē                   | Oceania   | Polynesia                 |      280904 |   4167           | -17.5374   | -149.566     |
| Belarus                                      | Minsk                     | Europe    | Eastern Europe            |     9398861 | 207600           |  53.9025   |   27.5618    |
| Latvia                                       | Riga                      | Europe    | Northern Europe           |     1901548 |  64559           |  56.9494   |   24.1052    |
| Palau                                        | Ngerulmud                 | Oceania   | Micronesia                |       18092 |    459           |   7.50064  |  134.624     |
| Guadeloupe                                   | Basse-Terre               | Americas  | Caribbean                 |      400132 |   1628           |  16.0001   |  -61.7333    |
| Philippines                                  | Manila                    | Asia      | South-Eastern Asia        |   109581085 | 342353           |  14.5904   |  120.98      |
| Gibraltar                                    | Gibraltar                 | Europe    | Southern Europe           |       33691 |      6           |  36.1286   |   -5.34748   |
| Denmark                                      | Copenhagen                | Europe    | Northern Europe           |     5831404 |  43094           |  55.6867   |   12.5701    |
| Cameroon                                     | Yaoundé                   | Africa    | Middle Africa             |    26545864 | 475442           |   3.86899  |   11.5213    |
| Guinea                                       | Conakry                   | Africa    | Western Africa            |    13132792 | 245857           |   9.51706  |  -13.6998    |
| Bahrain                                      | Manama                    | Asia      | Western Asia              |     1701583 |    765           |  26.2235   |   50.5822    |
| Suriname                                     | Paramaribo                | Americas  | South America             |      586634 | 163820           |   5.82418  |  -55.1663    |
| DR Congo                                     | Kinshasa                  | Africa    | Middle Africa             |   108407721 |      2.34486e+06 |  -4.3197   |   15.3424    |
| Somalia                                      | Mogadishu                 | Africa    | Eastern Africa            |    15893219 | 637657           |   2.03493  |   45.3419    |
| Czechia                                      | Prague                    | Europe    | Central Europe            |    10698896 |  78865           |  50.0596   |   14.4465    |
| New Caledonia                                | Nouméa                    | Oceania   | Melanesia                 |      271960 |  18575           | -22.2745   |  166.442     |
| Vanuatu                                      | Port Vila                 | Oceania   | Melanesia                 |      307150 |  12189           | -17.7415   |  168.315     |
| Saint Helena, Ascension and Tristan da Cunha | Jamestown                 | Africa    | Western Africa            |       53192 |    394           |  37.2089   |  -76.7783    |
| Togo                                         | Lomé                      | Africa    | Western Africa            |     8278737 |  56785           |   6.13042  |    1.21583   |
| British Virgin Islands                       | Road Town                 | Americas  | Caribbean                 |       30237 |    151           |  18.4258   |  -64.6231    |
| Kenya                                        | Nairobi                   | Africa    | Eastern Africa            |    53771300 | 580367           |  -1.28325  |   36.8172    |
| Niue                                         | Alofi                     | Oceania   | Polynesia                 |        1470 |    260           | -19.0534   | -169.919     |
| Heard Island and McDonald Islands            | Alofi                     | Antarctic | Polynesia                 |           0 |    412           | -19.0534   | -169.919     |
| Rwanda                                       | Kigali                    | Africa    | Eastern Africa            |    12952209 |  26338           |  -1.88596  |   30.1297    |
| Estonia                                      | Tallinn                   | Europe    | Northern Europe           |     1331057 |  45227           |  59.4372   |   24.7454    |
| Romania                                      | Bucharest                 | Europe    | Southeast Europe          |    19286123 | 238391           |  44.4361   |   26.1027    |
| Trinidad and Tobago                          | Port of Spain             | Americas  | Caribbean                 |     1399491 |   5130           |  10.6573   |  -61.518     |
| Guyana                                       | Georgetown                | Americas  | South America             |      786559 | 214969           |   6.81374  |  -58.1624    |
| Timor-Leste                                  | Dili                      | Asia      | South-Eastern Asia        |     1318442 |  14874           |  -8.55368  |  125.578     |
| Vietnam                                      | Hanoi                     | Asia      | South-Eastern Asia        |    97338583 | 331212           |  21.0283   |  105.854     |
| Uruguay                                      | Montevideo                | Americas  | South America             |     3473727 | 181034           | -34.9059   |  -56.1913    |
| Vatican City                                 | Vatican City              | Europe    | Southern Europe           |         451 |      0.44        |  41.9034   |   12.4529    |
| Hong Kong                                    | City of Victoria          | Asia      | Eastern Asia              |     7500700 |   1104           | -37        |  145         |
| Austria                                      | Vienna                    | Europe    | Central Europe            |     8917205 |  83871           |  48.2084   |   16.3725    |
| Antigua and Barbuda                          | Saint John's              | Americas  | Caribbean                 |       97928 |    442           |  17.1185   |  -61.8449    |
| Turkmenistan                                 | Ashgabat                  | Asia      | Central Asia              |     6031187 | 488100           |  37.9378   |   58.2359    |
| Mozambique                                   | Maputo                    | Africa    | Eastern Africa            |    31255435 | 801590           | -25.9662   |   32.5675    |
| Panama                                       | Panama City               | Americas  | Central America           |     4314768 |  75417           |   8.97145  |  -79.5342    |
| Micronesia                                   | Palikir                   | Oceania   | Micronesia                |      115021 |    702           |   6.92074  |  158.163     |
| Ireland                                      | Dublin                    | Europe    | Northern Europe           |     4994724 |  70273           |  53.3494   |   -6.26056   |
| Curaçao                                      | Willemstad                | Americas  | Caribbean                 |      155014 |    444           |  12.1067   |  -68.9351    |
| French Guiana                                | Cayenne                   | Americas  | South America             |      254541 |  83534           |   4.93715  |  -52.3259    |
| Norway                                       | Oslo                      | Europe    | Northern Europe           |     5379475 | 323802           |  59.9133   |   10.739     |
| Åland Islands                                | Mariehamn                 | Europe    | Northern Europe           |       29458 |   1580           |  60.1024   |   19.9413    |
| Central African Republic                     | Bangui                    | Africa    | Middle Africa             |     4829764 | 622984           |   4.36351  |   18.5836    |
| Burkina Faso                                 | Ouagadougou               | Africa    | Western Africa            |    20903278 | 272967           |  12.3682   |   -1.52709   |
| Eritrea                                      | Asmara                    | Africa    | Eastern Africa            |     5352000 | 117600           |  15.339    |   38.9327    |
| Tanzania                                     | Dodoma                    | Africa    | Eastern Africa            |    59734213 | 945087           |  -6.17912  |   35.7468    |
| South Korea                                  | Seoul                     | Asia      | Eastern Asia              |    51780579 | 100210           |  37.5667   |  126.978     |
| Jordan                                       | Amman                     | Asia      | Western Asia              |    10203140 |  89342           |  31.9516   |   35.924     |
| Mauritania                                   | Nouakchott                | Africa    | Western Africa            |     4649660 |      1.0307e+06  |  18.0792   |  -15.978     |
| Lithuania                                    | Vilnius                   | Europe    | Northern Europe           |     2794700 |  65300           |  54.687    |   25.2829    |
| United States Minor Outlying Islands         | Washington DC             | Americas  | North America             |         300 |     34.2         |  38.895    |  -77.0365    |
| Slovakia                                     | Bratislava                | Europe    | Central Europe            |     5458827 |  49037           |  48.1517   |   17.1093    |
| Angola                                       | Luanda                    | Africa    | Middle Africa             |    32866268 |      1.2467e+06  |  -8.82727  |   13.244     |
| Kazakhstan                                   | Nur-Sultan                | Asia      | Central Asia              |    18754440 |      2.7249e+06  |  51.1282   |   71.4307    |
| Moldova                                      | Chișinău                  | Europe    | Eastern Europe            |     2617820 |  33846           |  47.0245   |   28.8323    |
| Mali                                         | Bamako                    | Africa    | Western Africa            |    20250834 |      1.24019e+06 |  12.6493   |   -8.00034   |
| Falkland Islands                             | Stanley                   | Americas  | South America             |        2563 |  12173           | -51.6931   |  -57.8565    |
| Armenia                                      | Yerevan                   | Asia      | Western Asia              |     2963234 |  29743           |  40.1777   |   44.5126    |
| Samoa                                        | Apia                      | Oceania   | Polynesia                 |      198410 |   2842           | -13.8345   | -171.763     |
| Jersey                                       | Saint Helier              | Europe    | Northern Europe           |      100800 |    116           |  47.3849   |    4.6832    |
| Japan                                        | Tokyo                     | Asia      | Eastern Asia              |   125836021 | 377930           |  35.6769   |  139.764     |
| Bolivia                                      | Sucre                     | Americas  | South America             |    11673029 |      1.09858e+06 |   9        |  -75         |
| Chile                                        | Santiago                  | Americas  | South America             |    19116209 | 756102           |   9.86948  |  -83.7981    |
| United States                                | Washington, D.C.          | Americas  | North America             |   329484123 |      9.37261e+06 |  38.895    |  -77.0365    |
| Saint Vincent and the Grenadines             | Kingstown                 | Americas  | Caribbean                 |      110947 |    389           |  13.1562   |  -61.228     |
| Bermuda                                      | Hamilton                  | Americas  | North America             |       63903 |     54           |  43.2561   |  -79.8729    |
| Seychelles                                   | Victoria                  | Africa    | Eastern Africa            |       98462 |    452           | -36.5986   |  144.678     |
| British Indian Ocean Territory               | Diego Garcia              | Africa    | Eastern Africa            |        3000 |     60           |  -7.33836  |   72.4718    |
| Guatemala                                    | Guatemala City            | Americas  | Central America           |    16858333 | 108889           |  14.6416   |  -90.5133    |
| Ecuador                                      | Quito                     | Americas  | South America             |    17643060 | 276841           |  -0.220164 |  -78.5123    |
| Martinique                                   | Fort-de-France            | Americas  | Caribbean                 |      378243 |   1128           |  14.6028   |  -61.0677    |
| Tajikistan                                   | Dushanbe                  | Asia      | Central Asia              |     9537642 | 143100           |  38.5763   |   68.7864    |
| Malta                                        | Valletta                  | Europe    | Southern Europe           |      525285 |    316           |  35.899    |   14.5137    |
| Gambia                                       | Banjul                    | Africa    | Western Africa            |     2416664 |  10689           |  13.441    |  -16.5628    |
| Nigeria                                      | Abuja                     | Africa    | Western Africa            |   206139587 | 923768           |   9.06433  |    7.4893    |
| Bahamas                                      | Nassau                    | Americas  | Caribbean                 |      393248 |  13943           |  40.7353   |  -73.5616    |
| Kosovo                                       | Pristina                  | Europe    | Southeast Europe          |     1775378 |  10908           |  42.6639   |   21.1641    |
| Kuwait                                       | Kuwait City               | Asia      | Western Asia              |     4270563 |  17818           |  29.3797   |   47.9734    |
| Maldives                                     | Malé                      | Asia      | Southern Asia             |      540542 |    300           |  46.3516   |   10.9129    |
| South Sudan                                  | Juba                      | Africa    | Middle Africa             |    11193729 | 619745           |   4.84592  |   31.5959    |
| Iran                                         | Tehran                    | Asia      | Southern Asia             |    83992953 |      1.6482e+06  |  35.6893   |   51.3896    |
| Albania                                      | Tirana                    | Europe    | Southeast Europe          |     2837743 |  28748           |  41.3281   |   19.8184    |
| Brazil                                       | Brasília                  | Americas  | South America             |   212559409 |      8.51577e+06 | -10.3333   |  -53.2       |
| Serbia                                       | Belgrade                  | Europe    | Southeast Europe          |     6908224 |  88361           |  44.8178   |   20.4569    |
| Belize                                       | Belmopan                  | Americas  | Central America           |      397621 |  22966           |  17.2502   |  -88.77      |
| Myanmar                                      | Naypyidaw                 | Asia      | South-Eastern Asia        |    54409794 | 676578           |  19.7753   |   96.1033    |
| Bhutan                                       | Thimphu                   | Asia      | Southern Asia             |      771612 |  38394           |  27.4714   |   89.6337    |
| Venezuela                                    | Caracas                   | Americas  | South America             |    28435943 | 916445           |  10.5061   |  -66.9146    |
| Liberia                                      | Monrovia                  | Africa    | Western Africa            |     5057677 | 111369           |   6.32803  |  -10.7978    |
| Jamaica                                      | Kingston                  | Americas  | Caribbean                 |     2961161 |  10991           |  17.9712   |  -76.7928    |
| Poland                                       | Warsaw                    | Europe    | Central Europe            |    37950802 | 312679           |  52.232    |   21.0067    |
| Cayman Islands                               | George Town               | Americas  | Caribbean                 |       65720 |    264           |   5.41416  |  100.329     |
| Brunei                                       | Bandar Seri Begawan       | Asia      | South-Eastern Asia        |      437483 |   5765           |   4.88955  |  114.942     |
| Comoros                                      | Moroni                    | Africa    | Eastern Africa            |      869595 |   1862           | -11.6931   |   43.2543    |
| Guam                                         | Hagåtña                   | Oceania   | Micronesia                |      168783 |    549           |  13.4748   |  144.752     |
| Tonga                                        | Nuku'alofa                | Oceania   | Polynesia                 |      105697 |    747           | -21.1343   | -175.202     |
| Kiribati                                     | South Tarawa              | Oceania   | Micronesia                |      119446 |    811           |   1.34908  |  173.039     |
| Ghana                                        | Accra                     | Africa    | Western Africa            |    31072945 | 238533           |   5.55711  |   -0.201238  |
| Chad                                         | N'Djamena                 | Africa    | Middle Africa             |    16425859 |      1.284e+06   |  12.1192   |   15.0503    |
| Zimbabwe                                     | Harare                    | Africa    | Southern Africa           |    14862927 | 390757           | -17.8567   |   31.0602    |
| Saint Martin                                 | Marigot                   | Americas  | Caribbean                 |       38659 |     53           |  18.0669   |  -63.0849    |
| Mongolia                                     | Ulan Bator                | Asia      | Eastern Asia              |     3278292 |      1.56411e+06 |  47.9185   |  106.918     |
| Portugal                                     | Lisbon                    | Europe    | Southern Europe           |    10305564 |  92090           |  38.7078   |   -9.13659   |
| American Samoa                               | Pago Pago                 | Oceania   | Polynesia                 |       55197 |    199           | -14.2755   | -170.705     |
| Republic of the Congo                        | Brazzaville               | Africa    | Middle Africa             |     5657000 | 342000           |  -4.26944  |   15.2712    |
| Belgium                                      | Brussels                  | Europe    | Western Europe            |    11555997 |  30528           |  50.8466   |    4.3517    |
| Israel                                       | Jerusalem                 | Asia      | Western Asia              |     9216900 |  20770           |  31.7788   |   35.2258    |
| New Zealand                                  | Wellington                | Oceania   | Australia and New Zealand |     5084300 | 270467           | -41.2888   |  174.777     |
| Nicaragua                                    | Managua                   | Americas  | Central America           |     6624554 | 130373           |  12.1544   |  -86.2738    |
| Anguilla                                     | The Valley                | Americas  | Caribbean                 |       13452 |     91           |  51.4864   |    0.0361585 |