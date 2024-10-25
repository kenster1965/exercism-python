"""
determine the RNA complement of a given DNA sequence.
"""


def to_rna(dna_strand):
    """
    Transcribe a DNA sequence to its RNA complement.

    :param dna_strand: str - a DNA sequence.
    :return: str - the RNA complement of the DNA sequence.
    :raises ValueError: If the DNA sequence contains invalid nucleotides.
    """
    dna_to_rna = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }

    try:
        rna_strand = ''.join(dna_to_rna[nucleotide] for nucleotide in dna_strand)
    except KeyError:
        raise ValueError("Invalid DNA sequence")

    return rna_strand
