**Wat ik graag zou willen doen tijdens de WOO scriptie en hoe?**

Ramon Duursma (12851779)

Tijdens de eerste meeting zijn alle WOO-monitoring deelnemers als het ware omgepraat tot aanhakers. Nou moet ik persoonlijk zeggen dat beiden interessante scriptie
onderdelen zijn en dat dit mij dus niet heel veel uitmaakt. Maarten Marx stelde echter dat het WOO-monitoring onderdeel alsnog deel uit kan maken van het platform
wat gecreëerd zou moeten worden bij het aanhaken. Aangezien ik in eerste instantie niet voor niets heb gekozen voor het monitoring deel ben ik ook zeker geïnteresseerd
in het implementeren van dit onderdeel.

**Hoe zou ik dit willen doen?**

– In de scriptie omschrijving staat dat gegevensextractie om op basis van woo-brieven vrijwel onmogelijk is om foutloos te doen. Dus gegevensextractie lijkt
me niet bepaald van belang voor implementatie van deze taak. Hoewel het wellicht wel kan helpen om verzoeken makkelijker te maken. Wellicht dat sommige delen
van de brieven wel altijd in een bepaalde structuur staan en dat als een brief wordt ingevoerd dat bepaalde data al automatisch wordt verzameld. Data waarvan
het niet mogelijk is om te extracten zal waarschijnlijk gewoon handmatig in moeten worden gevuld, maar een deel van de gegevens zal altijd hetzelfde zijn
en dat zou gewoon gekoppeld moeten worden aan het account waardoor weer een ander deel van de gegevens ook automatisch ingevuld kan worden. 
Door zo veel mogelijk gegevens automatisch in te voeren kan het process natuurlijk zo makkelijk mogelijk worden gemaakt,
wat het voor de gebruikers makkelijker en minder tijdrovend maakt om zo het gebruik te stimuleren.
Verder zijn er ook al gegevens te vinden op Woogle dus kijken wat daarmee moet gebeuren.

Nadat de data is ingevoerd wordt deze verzameld in een SQL table en deze table wordt als men naar de statistieken pagina (met seaborn plots)
wilt gaan omgezet tot een panda's dataframe. Op basis van dit dataframe is het dan relatief eenvoudig om allerlei verschillende plots te maken vergelijkbaar
met de plots uit het Britse alternatief.

**Technische details:** Flask wordt gebruikt voor het inladen van de verschillende url's. 
Automatisch in te vullen gegevens worden via flask doorgevoerd door middel van een script met GetElementById() geshowcased aan de gebruiker.
Data uit de forms wordt opgevraagd door middel van de ''request.form.get'' functie, en vervolgens door middel van db.execute() geinsert in een SQL table.
Deze table wordt omgezet naar panda's hoe dat moet wordt omschreven in link (1) onderaan deze text.

**Knelpunten:** Persoonlijk klinkt het automatisch verzamelen van data in een pdf of ander soort file als de grootste uitdaging
en wellicht is dit dan ook niet mogelijk, maar het zou de kwaliteit wel een stuk beter maken.

MySQL ik heb zelf afgelopen vrijdag al geprobeerd MySQL te installeren en te gebruiken op in mijn VScode ik kwam een heel eind,
maar het lukte me nooit om de database daadwerkelijk te gebruiken in Flask. Dus wellicht zie ik iets over het hoofd.
Als er SQL gebruikt wordt in een Flask project val ik daarom vaak nog terug op de ingebouwde SQL database van cs50.

Verder zou het maken van de Seaborn plots voor er daadwerkelijk data is ook getest kunnen worden met de britse data.
Het kan natuurlijk ook zo zijn dat andere deelnemers van deze WOO-scriptie al op een degelijke manier hebben verzameld.
Sowieso is integratie met de andere mensen belangrijk want een gemaakt account moet op het hele platform werken en er moet telkens met dezelfde data worden gewerkt.

**Design:** Volgens de omschrijving van het monitoring project is het grotendeels het volgen van het Brits ontwerp.
Persoonlijk vind ik de ''endless scroll'' waarvoor gekozen is bij de britten niet optimaal. En dus kan het design wel iets verbeterd worden, dit lijkt me wel echter wel pas werk voor later. Omdat het werkend krijgen van functies een stuk belangrijker is dan het ontwerp. Persoonlijk denk ik aan een navbar voor de verschillende punten zoals in het britse model zodat je niet steeds naar boven hoeft te scrollen.

**Andere elementen platform:** Verder heb ik best wel wat ervaring met Flask. Voor het webprogrammeren project had ons groepje een platform
voor beginnende investeerders gemaakt. Dus ik ben al bekend met het maken van een platform en ik had hierbij zelf het comments systeem gemaakt.
Dus ik zou eventueel ook kunnen mee kunnen werken aan andere delen van het platform.

**Doel:** Een werkend project creëren zonder bugs die het platform duidelijk negatief beïnvloeden.
Projecten tijdens een projectperiode zijn vaak wel redelijk af, maar aan het einde heb je altijd toch nog het idee van "had ik nog maar een week extra gehad"
en dan was het project echt af geweest.

**Links:** (1) [https://datatofish.com/sql-to-pandas-dataframe/](https://datatofish.com/sql-to-pandas-dataframe/)
