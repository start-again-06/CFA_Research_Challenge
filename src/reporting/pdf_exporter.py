from fpdf import FPDF


class PDFExporter:
    def __init__(self, title="Equity Research Report"):

        self.title = title

    def export(self, report_dict, filename="research_report.pdf"):

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial", "B", 16)

        pdf.cell(0, 10, self.title, ln=True)

        pdf.ln(5)

        pdf.set_font("Arial", size=12)

        for section, content in report_dict.items():

            pdf.set_font("Arial", "B", 14)
            pdf.cell(0, 10, section, ln=True)

            pdf.set_font("Arial", size=11)

            if isinstance(content, dict):

                for key, value in content.items():

                    pdf.cell(0, 8, f"{key}: {value}", ln=True)

            else:

                pdf.cell(0, 8, str(content), ln=True)

            pdf.ln(3)

        pdf.output(filename)

        print(f"Report exported to {filename}")
