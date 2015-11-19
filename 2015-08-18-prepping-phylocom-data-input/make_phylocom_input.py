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
#all1985   50  Adenaria_floribunda
#all1985   2   Pemphis_acidula
#native1985   50  Adenaria_floribunda
#native1985   2   Pemphis_acidula
#nonnative1985   50  Adenaria_floribunda
#nonative1985   2   Pemphis_acidula
#all1986   60  Adenaria_floribunda
#all1986   90  Pemphis_acidula
#native1986   60  Adenaria_floribunda
#native1986   90  Pemphis_acidula
#nonnative1986   60  Adenaria_floribunda
#nonnative1986   90  Pemphis_acidula

years = ['1985', '1986', '1988', '1989', '1991', '1993', '1995', '1998', '2000', 
         '2003', '2005', '2007', '2009', '2011', '2013']

for year in years:
    with open('final_fqa_data/' + year + '.csv') as f:
        content = f.readlines()
        taxa = []
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
        all_sample = ''
        native_sample = ''
        nonnative_sample = ''
        for species in species_list:
            # get the cover weight
            values = species.split(',')
            weight = str(int(float(values[11]) * 100))
            if weight == '0':
                weight = '1'
            # get the taxon name
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
                all_sample += 'all' + year + '\t' + weight + '\t' + taxon + '\n'
                if 'non-native' in words[2]:
                    nonnative_sample += 'nonnative' + year + '\t' + weight + '\t' + taxon + '\n'
                else:
                    native_sample += 'native' + year + '\t' + weight + '\t' + taxon + '\n'
        output = open('sample', 'a')
        output.write(all_sample + native_sample + nonnative_sample)
        output.close()
