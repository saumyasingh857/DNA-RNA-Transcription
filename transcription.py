#DNA to RNA Transcription
dna = input("Enter DNA Sequence:").upper()
transcription = {
    "A":"U",
    "T":"A",
    "G":"C",
    "C":"G"
}
rna ="" 
for base in dna:
     rna +=transcription[base]

print("DNA Sequence:",dna)
print("RNA Sequence:",rna)