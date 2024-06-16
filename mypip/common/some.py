import importlib.metadata
if importlib.metadata.version('pymupdf') >= '1.24.3':
    import pymupdf as fitz
else:
    import fitz
def open(path):
    # 湿哒哒
    doc = fitz.open(path)
    return doc
