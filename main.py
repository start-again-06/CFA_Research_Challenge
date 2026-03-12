import yaml
from src.financial_model.revenue_model import RevenueModel
from src.valuation.dcf_model import DCFModel
from src.reporting.report_generator import ReportGenerator
from src.reporting.pdf_exporter import PDFExporter


def load_config():

    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)


def run_pipeline():

    config = load_config()

  
    revenue_model = RevenueModel(
        base_revenue=100,
        growth_rate=config["forecast"]["revenue_growth"],
        years=config["forecast"]["years"]
    )

    revenue_forecast = revenue_model.forecast()

    
    fcff = [r * 0.15 for r in revenue_forecast]

    dcf = DCFModel(
        fcff,
        config["valuation"]["wacc"],
        config["valuation"]["terminal_growth"]
    )

    enterprise_value = dcf.compute_enterprise_value()

    equity_value = enterprise_value * 0.8

    price_target = equity_value / 100

    # Generate report
    report = ReportGenerator()

    report.add_company_overview(
        config["company"]["name"],
        config["company"]["industry"],
        "Automated research pipeline valuation."
    )

    report.add_financial_summary(
        revenue=revenue_forecast,
        ebitda=[r * 0.25 for r in revenue_forecast],
        net_income=[r * 0.12 for r in revenue_forecast]
    )

    report.add_dcf_valuation(
        enterprise_value,
        equity_value,
        price_target
    )

    report_data = report.generate()

    PDFExporter().export(report_data, config["output"]["report_file"])


if __name__ == "__main__":
    run_pipeline()
