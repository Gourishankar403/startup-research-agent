import PyPDF2

def extract_text_from_pdf(filepath:str)-> str:
    try:
        with open(file_path,'rb')as file:
            reader=PyPDF2.PdfFileReader(file)
            text=""
            for page in reader.pages():
                text+=page.extractText()
            return text

    except Exception as e:
        return f"Error reading PDF:{str(e)}"