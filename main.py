from instructions import industries, instruction_prompts, row_headers
from ai import create_content
from creator import PDFDocument, create_csv, store_ids
from config import tearup
from nanoid import generate

batch_id = "nov24"
by_category = True
docs_per_category = 10

if __name__ == "__main__":
    tearup(batch_id, industries)
    for index, industry in enumerate(industries):
        category_ids = []
        store_url = f"./data/{batch_id}"
        store_url = store_url if not by_category else f"{store_url}/{industry}"
        headers = row_headers[index]
        prompt = instruction_prompts[index]
        for _ in range(docs_per_category):
            file_id = generate()
            col_results, contents = create_content(headers, prompt)
            file_name = f"{industry}_{file_id}"
            file_url = f"{store_url}/{file_name}"
            PDFDocument(contents, file_id).save(f"{file_url}.pdf")
            create_csv(f"{file_url}.csv", headers, col_results)
            category_ids.append(file_name)
        store_ids(f"{store_url}/processed_ids.csv", category_ids)
