from unstructured.partition.pdf import partition_pdf
import re

# Function to parse a PDF and chunk its contents into meaningful text blocks
def parse_pdf(file_path):
    chunks = partition_pdf(
        filename=file_path,
        strategy="fast",  # <<< change here
        extract_images_in_pdf=False  # <<< avoid needing poppler
    )
    return chunks

def extract_citations(text):
    import re
    return re.findall(r"\[(\d+)\]", text)

def get_text_metrics(texts):
    total_words = sum(len(text.split()) for text in texts)
    estimated_time = total_words // 200
    return total_words, estimated_time