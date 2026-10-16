def convert_multiline_fasta_to_oneline(
    input_fasta: str,
    output_fasta: str | None = None
) -> None:
    """Convert multiline FASTA sequences to single-line sequences."""

    if output_fasta is None:
        output_fasta = input_fasta.replace(".fasta", "_oneline.fasta")

    with open(input_fasta, "r") as infile:
        with open(output_fasta, "w") as outfile:
            sequence = ""

            for line in infile:
                line = line.strip()

                if line.startswith(">"):
                    if sequence:
                        outfile.write(sequence + "\n")

                    outfile.write(line + "\n")
                    sequence = ""
                else:
                    sequence += line

            if sequence:
                outfile.write(sequence + "\n")