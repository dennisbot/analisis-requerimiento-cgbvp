import mammoth
import markdownify

with open("RIF_VERSION_2025_trimeado.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value

markdown = markdownify.markdownify(html, heading_style="ATX")

with open("RIF_VERSION_2025-mammoth.md", "w", encoding="utf-8") as f:
    f.write(markdown)
