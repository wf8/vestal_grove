
import math
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']
import matplotlib.pyplot as plt
import numpy
from scipy.stats import linregress


## 1985

total_pd_1985 = 2576.84	

taxa_1985 = [ "Rhamnus_cathartica", "Geum_canadense", "Circaea_canadensis", "Arisaema_triphyllum", "Vitis_riparia", "Solanum_dulcamara", "Cornus_racemosa", "Prunella_vulgaris", "Toxicodendron_radicans", "Maianthemum_racemosum", "Geranium_bicknellii", "Oxalis_stricta", "Epilobium_coloratum", "Rubus_occidentalis", "Prunus_virginiana", "Parthenocissus_inserta", "Quercus_macrocarpa", "Carex_blanda", "Allium_canadense", "Prunus_serotina", "Ranunculus_hispidus", "Taraxacum_officinale", "Lonicera_tatarica", "Crataegus_mollis", "Potentilla_simplex", "Allium_cernuum", "Fragaria_virginiana", "Populus_deltoides", "Poa_pratensis", "Cirsium_discolor", "Rubus_idaeus", "Aquilegia_canadensis", "Viola_sororia", "Ribes_americanum", "Arctium_minus", "Cirsium_vulgare", "Smilax_hispida", "Andropogon_gerardii", "Smilax_lasioneuron", "Epipactis_helleborine", "Solidago_juncea", "Sonchus_asper", "Erigeron_annuus", "Frangula_alnus", "Viburnum_acerifolium", "Verbena_hastata", "Nabalus_albus", "Agrimonia_gryposepala", "Populus_tremuloides" ]	

cover_1985 = [ 17.2, 5.7, 6.3, 5.3, 4.5, 4.1, 4.8, 3.6, 2.2, 2.6, 3, 2.3, 2.6, 3, 2.6, 1.6, 3.3, 1.2, 1.3, 1.3, 2.3, 1.6, 1.6, 1, 2, 1.3, 0.7, 0.7, 0.7, 0.7, 0.7, 1, 0.7, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.2 ]	

pd_by_taxon_1985 = [ 2573.2, 2557.94, 2557.02, 2475.31, 2571.94, 2521.56, 2500.55, 2549.64, 2509.61, 2538.24, 2508.51, 2517.94, 2557.02, 2571.93, 2572.69, 2571.94, 2519.31, 2512.11, 2569.17, 2572.69, 2531.42, 2565.29, 2529.24, 2557.47, 2561.56, 2569.17, 2561.56, 2570.8, 2549.01, 2572.57, 2571.93, 2531.42, 2532.96, 2494.65, 2564.4, 2572.57, 2572.3, 2549.01, 2572.3, 2511.74, 2569.63, 2560.06, 2569.63, 2573.2, 2529.24, 2549.64, 2565.29, 2560.66, 2570.8 ]

#per_pd_by_taxon_1985 = [ (total_pd_1985 - pd)/total_pd_1985  for pd in pd_by_taxon_1985 ]
per_pd_by_taxon_1985 = [ (total_pd_1985 - pd)  for pd in pd_by_taxon_1985 ]

## 2013

total_pd_2013 = 3381.79 

taxa_2013 = [ "Helianthus_strumosus", "Zizia_aurea", "Solidago_ulmifolia", "Leersia_virginica", "Eutrochium_purpureum", "Amphicarpaea_bracteata", "Arisaema_triphyllum", "Solidago_altissima", "Triosteum_perfoliatum", "Impatiens_capensis", "Smilax_lasioneuron", "Helianthus_decapetalus", "Geranium_bicknellii", "Ranunculus_hispidus", "Silene_stellata", "Maianthemum_racemosum", "Smilax_hispida", "Bromus_latiglumis", "Lithospermum_latifolium", "Camassia_scilloides", "Cinna_arundinacea", "Ageratina_altissima", "Allium_canadense", "Carex_blanda", "Thalictrum_revolutum", "Circaea_canadensis", "Arisaema_dracontium", "Sanguinaria_canadensis", "Symphyotrichum_shortii", "Carex_pensylvanica", "Trillium_recurvatum", "Thalictrum_dioicum", "Rudbeckia_hirta", "Solidago_caesia", "Elymus_hystrix", "Rubus_flagellaris", "Viola_sororia", "Potentilla_simplex", "Cardamine_concatenata", "Helianthus_divaricatus", "Carex_acutiformis", "Polygonatum_biflorum", "Floerkea_proserpinacoides", "Symphyotrichum_lateriflorum", "Fragaria_virginiana", "Thalictrum_dasycarpum", "Cryptotaenia_canadensis", "Brachyelytrum_erectum", "Maianthemum_stellatum", "Nabalus_albus", "Penstemon_digitalis", "Lespedeza_virginica", "Heracleum_maximum", "Carex_cephalophora", "Aquilegia_canadensis", "Persicaria_virginiana", "Rhamnus_cathartica", "Vitis_riparia", "Oxypolis_rigidior", "Coreopsis_tripteris", "Festuca_subverticillata", "Hydrophyllum_virginianum", "Galium_triflorum", "Geum_canadense", "Galium_aparine", "Alisma_triviale", "Hackelia_virginiana", "Glyceria_striata", "Boehmeria_cylindrica", "Pedicularis_canadensis", "Poa_compressa", "Iodanthus_pinnatifidus", "Taenidia_integerrima", "Bromus_pubescens", "Perideridia_americana", "Elymus_canadensis", "Taraxacum_officinale", "Plantago_rugelii", "Potentilla_recta", "Cirsium_altissimum", "Uvularia_grandiflora", "Carex_rosea", "Symphyotrichum_drummondii", "Oxalis_stricta" ]

cover_2013 = [ 16.4, 9.6, 6.6, 4.8, 4.2, 4.5, 2.1, 2.3, 3.3, 2.6, 2.3, 2.5, 1.7, 1.7, 1.7, 0.8, 1.3, 1.3, 2, 1.2, 0.5, 1, 0.9, 0.6, 1.4, 0.6, 0.8, 0.7, 1.3, 1.3, 0.7, 0.8, 1.1, 1, 0.4, 0.3, 0.6, 0.7, 0.2, 0.9, 0.9, 0.5, 0.5, 0.3, 0.3, 0.7, 0.3, 0.2, 0.7, 0.7, 0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.2, 0.3, 0.3, 0.2, 0.2, 0.2, 0.01, 0.01, 0.1, 0.1, 0.1, 0.01, 0.1, 0.1, 0.01, 0.1, 0.01, 0.01, 0.1, 0.1, 0.01]

pd_by_taxon_2013 = [ 3380.79, 3376.74, 3380.79, 3354.98, 3371.05, 3362.48, 3377.1, 3380.59, 3325.59, 3299.31, 3377.25, 3381.32, 3313.46, 3336.38, 3287.3, 3378.43, 3377.25, 3381.38, 3349.83, 3354.11, 3376.01, 3371.05, 3343.19, 3375.16, 3381.46, 3314.56, 3377.1, 3266.06, 3381.15, 3376.38, 3318.92, 3377.83, 3374.22, 3380.79, 3380.21, 3362.89, 3322.9, 3373.37, 3374.8, 3381.32, 3376.38, 3375.27, 3333.39, 3381.15, 3366.52, 3381.46, 3371.96, 3361.48, 3378.43, 3370.25, 3351.44, 3362.48, 3373.85, 3376.08, 3370.66, 3287.3, 3340.03, 3302.57, 3371.96, 3366.09, 3372.29, 3336.17, 3375.8, 3362.89, 3375.8, 3287, 3349.83, 3364.88, 3340.03, 3346.29, 3376.01, 3374.8, 3376.74, 3381.38, 3370.09, 3380.21, 3370.25, 3351.44, 3373.37, 3352.19, 3321.08, 3376.08, 3379.83, 3322.9 ]

#per_pd_by_taxon_2013 = [ (total_pd_2013 - pd)/total_pd_2013  for pd in pd_by_taxon_2013 ]
per_pd_by_taxon_2013 = [ (total_pd_2013 - pd)  for pd in pd_by_taxon_2013 ]


#log_per_pd_by_taxon_1985 = [ math.log( (total_pd_1985 - pd)/total_pd_1985 ) for pd in pd_by_taxon_1985 ]
#log_cover_1985 = [ math.log(x) for x in cover_1985 ]
#log_cover_2013 = [] 
#for x in cover_2013:
#    if x == 0: 
#        log_cover_2013.append(math.log(0.01)) 
#    else: 
#        log_cover_2013.append(math.log(x))


#linregress output:
#slope : float
#slope of the regression line
#intercept : float
#intercept of the regression line
#r-value : float
#correlation coefficient
#p-value : float
#two-sided p-value for a hypothesis test whose null hypothesis is that the slope is zero
#stderr : float
#Standard error of the estimate

print(linregress(cover_2013,per_pd_by_taxon_2013))
print(linregress(cover_1985,per_pd_by_taxon_1985))

cover_by_pd_1985 = []
for i, cover in enumerate(cover_1985):
    cover_by_pd_1985.append( cover / per_pd_by_taxon_1985[i] )

cover_by_pd_2013 = []
for i, cover in enumerate(cover_2013):
    cover_by_pd_2013.append( cover / per_pd_by_taxon_2013[i] )

#print(cover_by_pd_1985)
#print(cover_by_pd_2013)
print(numpy.mean( cover_by_pd_1985 ) )
print(numpy.mean( cover_by_pd_2013 ) )


props = dict(alpha=0.5, edgecolors='none' )
plt.scatter(cover_2013, per_pd_by_taxon_2013, c="blue", **props)
plt.scatter(cover_1985, per_pd_by_taxon_1985, c="magenta", **props)
plt.axis([0, 19, 0, 120.0])
plt.show()

all_taxa = []
for taxon in taxa_2013:
    if taxon not in all_taxa:
        all_taxa.append(taxon)
for taxon in taxa_1985:
    if taxon not in all_taxa:
        all_taxa.append(taxon)

thru_time_1985 = []
thru_time_2013 = []
for taxon in all_taxa:
    
    if taxon in taxa_1985:
        thru_time_1985.append(per_pd_by_taxon_1985[ taxa_1985.index( taxon ) ] )
        #thru_time_1985.append(cover_by_pd_1985[ taxa_1985.index( taxon ) ] )
    else:
        thru_time_1985.append( 0.0 )
    
    if taxon in taxa_2013:
        thru_time_2013.append(per_pd_by_taxon_2013[ taxa_2013.index( taxon ) ] )
        #thru_time_2013.append(cover_by_pd_2013[ taxa_2013.index( taxon ) ] )
    else:
        thru_time_2013.append( 0.0 )

#plt.scatter(thru_time_1985, thru_time_2013, c="magenta", **props)
#plt.show()
