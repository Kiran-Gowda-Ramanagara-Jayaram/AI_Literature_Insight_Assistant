from unstructured.partition.pdf import partition_pdf
import re

# Function to parse a PDF and chunk its contents into meaningful text blocks
def parse_pdf(file_path):
    chunks = partition_pdf(
        filename=file_path,
        infer_table_structure=True,
        strategy="hi_res",
        extract_image_block_types=["Image"],
        extract_image_block_to_payload=True,
        chunking_strategy="by_title",
        max_characters=10000,
        combine_text_under_n_chars=2000,
        new_after_n_chars=6000,
    )
    return chunks

# Function to extract citations from a full text
def extract_citations(text):
    citation_pattern = r"\[(\d+)\]"  # Matches [1], [2], etc.
    citations = re.findall(citation_pattern, text)
    return list(set(citations))

# Function to calculate word count and estimate reading time
def get_text_metrics(texts):
    total_words = sum(len(t.split()) for t in texts)
    estimated_read_time = total_words / 250  # 250 words per minute
    return total_words, round(estimated_read_time)
