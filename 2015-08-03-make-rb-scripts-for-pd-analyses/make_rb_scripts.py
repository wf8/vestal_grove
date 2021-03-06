#! /usr/bin/python

taxa_in_tree = []
with open('taxa_in_tree.txt') as f:
    for line in f.readlines():
        taxon = line.strip().replace('\n', '')
        taxa_in_tree.append(taxon)

print('List of all taxa not found in tree and replaced with members of the same genera:')
print('missing taxon,replacement taxon')
missing_taxa = []

# output needed:
# clade_all = clade("Adenaria_floribunda","Pemphis_acidula")
# clade_natives = clade("Adenaria_floribunda","Pemphis_acidula")
# clade_nonnatives = clade("Adenaria_floribunda","Pemphis_acidula")

years = ['1985', '1986', '1988', '1989', '1991', '1993', '1995', '1998', '2000', 
         '2003', '2005', '2007', '2009', '2011', '2013']

for year in years:
    with open('final_fqa_data/' + year + '.csv') as f:
        content = f.readlines()
        taxa = []
        all_species = ''
        natives = ''
        nonnatives = ''
        start = 0
        end = 0
        for i, line in enumerate(content):
            if 'Species' in line and '"Relative Importance Value"' in line:
                start = i + 1
            if start > 0 and '"Quadrat Level Metrics:"' in line:
                end = i - 2
                break
        species_list = content[start:end]
        taxon = ''
        for species in species_list:
            words = species.split('"')
            taxon = words[1]
            if ';' in taxon:
                synonyms = taxon.split(';')
                taxon = synonyms[0]
            taxon = taxon.strip().replace(' ', '_').replace('.', '')
            if taxon.find('_var_') != -1:
                taxon = taxon[:taxon.find('_var_')]
            if taxon.find('_ssp_') != -1:
                taxon = taxon[:taxon.find('_ssp_')]
            if taxon not in taxa_in_tree:
                # get a member of the same genera that is in the tree
                genus = taxon.split('_')[0]
                for tip in taxa_in_tree:
                    if genus in tip:
                        if taxon not in missing_taxa:
                            print(taxon + ',' + tip)
                            missing_taxa.append(taxon)
                        taxon = tip
                        break
            if taxon not in taxa:
                taxa.append(taxon)
                all_species += '"' + taxon + '",'
                if 'non-native' in words[2]:
                    nonnatives += '"' + taxon + '",'
                else:
                    natives += '"' + taxon + '",'
        all_species = all_species[:-1]
        natives = natives[:-1]
        nonnatives = nonnatives[:-1]
        script = open('rev_scripts/' + year + '_clades.Rev', 'w')
        script.write('clade_all = clade(' + all_species + ')\n')
        script.write('clade_natives = clade(' + natives + ')\n')
        script.write('clade_nonnatives = clade(' + nonnatives + ')\n')
        script.close()
