import sys
from stats import base_count

if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_genome>")
	sys.exit(1)
     
def get_genome(path):
    with open(path) as f:
        next(f)
        return f.read().replace("\n", "").replace("\r", "")
    
def main():
    genome_path = sys.argv[1]
    genome = get_genome(genome_path).rstrip()
    bases = base_count(genome)
    print(f"--------------Reading genome of {genome_path[8:]}--------------")
    print("")
    print(f"Genome lenght: {len(genome)}")
    print(f"Base count: {bases}")
    print("")
    print(f"---------------------Genome sequence:-------------------------")
    print(genome[:100])

main()
