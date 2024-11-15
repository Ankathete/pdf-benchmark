from fpdf import FPDF
from ftfy import fix_text
import csv


class PDFDocument:

    def __init__(self, contents, document_name="Document"):
        self.contents = contents
        self.document_name = document_name
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("Arial", "", 12)

        # Set left and right margins to ensure text is nicely bounded
        self.pdf.set_left_margin(15)
        self.pdf.set_right_margin(15)

    def _sanitize_text(self, text):
        # Clean up text, preserving characters like è
        text = text.replace("—", "-").replace("–", "-")
        return fix_text(text)

    def create_pdf(self):
        # Document title
        self.pdf.set_font("Arial", "B", 14)
        self.pdf.cell(0, 10, self.document_name, 0, 1, "C")
        self.pdf.ln(5)  # Add space after the title

        # Process each section
        for index, content in enumerate(self.contents):
            # Sanitize section title and content text
            section_title = self._sanitize_text(
                content['content_section_title'])
            section_text = self._sanitize_text(content['content_section_text'])

            # Section title formatting
            self.pdf.set_font("Arial", "B", 12)  # Bold font for section title
            self.pdf.multi_cell(0, 10,
                                section_title)  # Use multi_cell for wrapping
            self.pdf.ln(2)  # Small space after title

            # Section content formatting
            self.pdf.set_font("Arial", "", 12)  # Regular font for content
            self.pdf.multi_cell(0, 10,
                                section_text)  # Use multi_cell for wrapping
            self.pdf.ln(8)  # Space after each section for clarity

    def save(self, filename):
        self.create_pdf()
        self.pdf.output(filename)
        print(f"PDF saved as {filename}")


def create_csv(filename, row1, row2):
    # Check if both rows are lists
    if not isinstance(row1, list) or not isinstance(row2, list):
        raise ValueError("Both row1 and row2 must be lists.")

    # Write to CSV
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the two rows
        writer.writerow(row1)
        writer.writerow(row2)

    print(f"CSV saved as {filename}")


def store_ids(filename: str, ids: list):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(ids)
    print(f"IDs saved as {filename}")
