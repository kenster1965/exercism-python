"""Protein Translation"""


def proteins(strand):
    """Translate RNA strand to protein list
    :param strand: str rna strand to translate to protein list of str proteins
    :return: list of str proteins translated from rna strand
    """
    protein_list = []
    codon_protein_map = { # map of codon to protein
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP"
    }

    # Check in groups of 3
    for i in range(0, len(strand), 3):
        codon = strand[i:i + 3]
        protein = codon_protein_map.get(codon)
        if protein == "STOP":
            break
        if protein:
            protein_list.append(protein)

    return protein_list
