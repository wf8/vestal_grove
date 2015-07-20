import csv

species = open("species.csv", "w")
with open('Chicago_USACE_01.16.14.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    binomials = []
    for row in csvreader:
        if row[3] == "native":
            # agalinis paupercula var. borealis; agalinis purpurea parviflora
            names = row[0].split(";")
            accepted_name = names[0].strip().split(" ")
            binomial = accepted_name[0].strip().capitalize() + " " + accepted_name[1].strip()
            if binomial not in binomials:
                binomials.append(binomial)
                synonyms = ""
                for i in range(1,len(names)):
                    if names[i] != None and names[i].strip() != "":
                        synonym = names[i].strip().split(" ")
                        if synonym[0].strip().capitalize() + " " + synonym[1].strip() != binomial:
                            synonyms += "," + synonym[0].strip().capitalize() + " " + synonym[1].strip()
                species.write(binomial + synonyms + "\n")
species.close()
