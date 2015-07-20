


from Bio import AlignIO
from Bio import SeqIO


# concatenated = AlignIO.read(open("aligned_concatenated.fasta"), "fasta")
# record_dict = SeqIO.to_dict(SeqIO.parse(handle, "fasta"))
#

concatenated = SeqIO.to_dict(SeqIO.parse(open("aligned_concatenated.fasta"), "fasta"))
ITS = SeqIO.to_dict(SeqIO.parse(open("aligned_ITS.fasta"), "fasta"))
rbcL = SeqIO.to_dict(SeqIO.parse(open("aligned_rbcL.fasta"), "fasta"))
trnLF = SeqIO.to_dict(SeqIO.parse(open("aligned_trnL-trnF.fasta"), "fasta"))
matK = SeqIO.to_dict(SeqIO.parse(open("aligned_matK.fasta"), "fasta"))

concatenated_trimmed = []
ITS_trimmed = []
rbcL_trimmed = []
trnLF_trimmed = []
matK_trimmed = []

for species, record in concatenated.iteritems():
    seq = str(record.seq)
    seq = seq.replace("-", "")
    seq = seq.replace("?", "")
    seq = seq.replace("N", "")
    seq = seq.replace("n", "")
    if seq != "":
        concatenated_trimmed.append(concatenated[species])

for species, record in ITS.iteritems():
    seq = str(record.seq)
    seq = seq.replace("-", "")
    seq = seq.replace("?", "")
    seq = seq.replace("N", "")
    seq = seq.replace("n", "")
    if seq != "":
        ITS_trimmed.append(ITS[species])

for species, record in rbcL.iteritems():
    seq = str(record.seq)
    seq = seq.replace("-", "")
    seq = seq.replace("?", "")
    seq = seq.replace("N", "")
    seq = seq.replace("n", "")
    if seq != "":
        rbcL_trimmed.append(rbcL[species])

for species, record in trnLF.iteritems():
    seq = str(record.seq)
    seq = seq.replace("-", "")
    seq = seq.replace("?", "")
    seq = seq.replace("N", "")
    seq = seq.replace("n", "")
    if seq != "":
        trnLF_trimmed.append(trnLF[species])

for species, record in matK.iteritems():
    seq = str(record.seq)
    seq = seq.replace("-", "")
    seq = seq.replace("?", "")
    seq = seq.replace("N", "")
    seq = seq.replace("n", "")
    if seq != "":
        matK_trimmed.append(matK[species])


SeqIO.write(concatenated_trimmed, open("aligned_concatenated_trimmed.phy","w"), "phylip-relaxed")
SeqIO.write(concatenated_trimmed, open("aligned_concatenated_trimmed.fasta","w"), "fasta")
SeqIO.write(ITS_trimmed, open("aligned_ITS_trimmed.fasta","w"), "fasta")
SeqIO.write(rbcL_trimmed, open("aligned_rbcL_trimmed.fasta","w"), "fasta")
SeqIO.write(trnLF_trimmed, open("aligned_trnLF_trimmed.fasta","w"), "fasta")
SeqIO.write(matK_trimmed, open("aligned_matK_trimmed.fasta","w"), "fasta")

