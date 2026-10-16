import os

def calculate_gc(sequence:str) -> float:
    """ Calculate the GC content of a DNA sequence."""
    if not sequence:
        return 0.0
    else:
        sequence = sequence.upper()
        gc_count = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
        return gc_count
    

def check_gc(sequence: str, gc_bound: tuple[float,float] | float) -> bool:
    """Check whether GC content is within the specified bounds."""
    if not sequence:
        return False
    gc_count = calculate_gc(sequence)
    if isinstance(gc_bound, (int, float)):
        lower_bound = 0
        upper_bound = gc_bound
    else:
        lower_bound = gc_bound[0]
        upper_bound = gc_bound[1]
    return lower_bound <= gc_count <= upper_bound
    
def check_length(sequence: str, length_bounds: tuple[int,int] | int) -> bool:
      """Check whether sequence length falls within the specified bounds."""
      if not sequence:
        return False

      sequence_length = len(sequence)

      if isinstance(length_bounds, int):
          lower_bound = 0
          upper_bound = length_bounds
      else:
          lower_bound = length_bounds[0]
          upper_bound = length_bounds[1]
      return lower_bound <= sequence_length <= upper_bound

def calculate_average_quality(quality: str) -> float:
    """Calculate average Phred quality score."""
    if not quality:
        return 0.0

    scores = [ord(char) - 33 for char in quality]
    return sum(scores) / len(scores)

def check_quality(quality: str, quality_threshold: float) -> bool:
    """Check whether average quality meets the threshold."""
    average_quality = calculate_average_quality(quality)
    return average_quality >= quality_threshold

def filter_fastq(
    input_fastq: str,
    output_fastq: str,
    gc_bounds: tuple[float, float] | float = (0, 100),
    length_bounds: tuple[int, int] | int = (0, 2**32),
    quality_threshold: float = 0
) -> None:
    """Filter FASTQ reads by GC content, length and quality."""
    os.makedirs("filtered", exist_ok=True)
    output_path = os.path.join("filtered", os.path.basename(output_fastq))
    with open(input_fastq, "r") as input_file:
        with open(output_path, "w") as output_file:
            while True:
                header = input_file.readline()
                if not header:
                    break

                sequence = input_file.readline().strip()
                separator = input_file.readline()
                quality = input_file.readline().strip()

                if not quality or len(sequence) != len(quality):
                    continue
                
                if (
                    check_gc(sequence, gc_bounds)
                    and check_length(sequence, length_bounds)
                    and check_quality(quality, quality_threshold)
                ):
                    output_file.write(header)
                    output_file.write(sequence + "\n")
                    output_file.write(separator)
                    output_file.write(quality + "\n")

