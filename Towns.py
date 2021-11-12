import re

towns = '''Albertson
Amagansett
Amityville
Aquebogue
Atlantic Beach
Babylon
Baldwin
Bayport
Bayshore
Bayville
Bellerose Terrace
Bellmore
Bellport
Bethpage
Blue Point
Bohemia
Brentwood
Bridgehampton
Brightwaters
Brookhaven
Brookville
Calverton
Carle Place
Cedarhurst
Center Moriches
Centereach
Centerport
Central Islip
Cold Spring Harbor
Commack
Copiague
Coram
Cutchogue
Deer Park
Dix Hills
East Hampton
East Islip
East Marion
East Meadow
East Moriches
East Northport
East Norwich
East Patchogue
East Quogue
East Rockaway
East Setauket
Eastport
Elmont
Elwood
Farmingdale
Farmingville
Fishers Island
Floral Park
Franklin Square
Freeport
Garden City
Glen Head
Glenwood Landing
Great Neck
Great River
Greenlawn
Greenport
Greenvale
Hampton Bays
Hauppauge
Hempstead
Hewlett
Hicksville
Holbrook
Holtsville
Huntington
Huntington Station
Inwood
Island Park
Islandia
Islip
Islip Terrance
Jamesport
Jericho
Kings Park
Kings Point
Lake Grove
Laurel
Lawrence
Levittown
Lindenhurst
Lloyd Harbor
Locust Valley
Lynbrook
Malverne
Manhasset
Manorville
Massapequa
Massapequa Park
Mastic
Mastic Beach
Mattituck
Medford
Melville
Merrick
Middle Island
Mill Neck
Miller Place
Mineola
Montauk
Moriches
Mount Sinai
Nesconset
New Hyde Park
New Suffolk
North Amityville
North Babylon
North Lynbrook
North New Hyde Park
North Patchogue
North Valley Stream
North Woodmere
Northport
Oakdale
Ocean Beach
Oceanside
Old Bethpage
Old Westbury
Orient
Oyster Bay
Patchogue
Peconic
Plainview
Point Lookout
Port Jefferson
Port Jefferson Station
Port Washington
Quogue
Remsenburg
Ridge
Riverhead
Rockville Centre
Rocky Point
Ronkonkoma
Roosevelt
Roslyn
Roslyn Heights
Sag Harbor
Sagaponack
Saint James
Sands Point
Sayville
Sea Cliff
Seaford
Selden
Shelter Island
Shelter Island Heights
Shirley
Shoreham
Smithtown
Sound Beach
South Hempstead
South Jamesport
Southampton
Southold
Speonk
Stony Brook
Syosset
Uniondale
Upton
Valley Stream
Wading River
Wainscott
Wantagh
Water Mill
West Babylon
West Hempstead
West Islip
West Sayville
Westbury
Westhampton
Westhampton Beach
Williston Park
Woodbury
Woodmere
Wyandanch
Yaphank'''

towns.replace('Scroll back up', '')