from __future__ import annotations

def svg2pdf(svg_file, pdf_file):
    from svglib.svglib import svg2rlg
    from reportlab.graphics import renderPDF

    drawing = svg2rlg(svg_file)
    renderPDF.drawToFile(drawing, pdf_file)

def gif2pdf(gif_file, pdf_file):
    from PIL import Image

    img = Image.open(gif_file)
    img.save(pdf_file, "PDF", resolution=100.0)

def webp2pdf(webp_file, pdf_file):
    from PIL import Image

    img = Image.open(webp_file)
    img.save(pdf_file, "PDF", resolution=100.0)

def convert_images_to_pdfs(app):
    import os

    # Check if building LaTeX
    if app.builder.format != 'latex':
        return

    # Optional deps are only needed for LaTeX builds.
    # Keep HTML builds working even if svglib/reportlab aren't installed.
    try:
        import svglib  # noqa: F401
        import reportlab  # noqa: F401
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "La construction LaTeX requiert 'svglib' et 'reportlab' pour convertir les images. "
            "Installe les dépendances manquantes ou retire l'extension 'conversions' de conf.py."
        ) from exc

    # Get the path to the build directory
    build_dir = app.outdir

    # Conversion functions
    conversions = {
        '.svg': svg2pdf,
        '.gif': gif2pdf,
        '.webp': webp2pdf,
    }

    # Walk the source directory

    for root, dirs, files in os.walk(app.srcdir):
        for file in files:
            file_ext = os.path.splitext(file)[1]

            if file_ext not in conversions.keys():
                continue
            
            src_path = os.path.join(root, file)
            pdf_path = os.path.join(build_dir, file[:-len(file_ext)] + '.pdf')

             # Check if the pdf exists and is newer than the source file
            if os.path.exists(pdf_path):
                if os.path.getmtime(pdf_path) > os.path.getmtime(src_path):
                    continue
            
            # Convert the image
            conversions[file_ext](src_path, pdf_path)

def setup(app):
    app.connect('builder-inited', convert_images_to_pdfs)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }