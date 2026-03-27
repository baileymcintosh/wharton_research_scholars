from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any

import requests


ROOT = Path(__file__).resolve().parents[1]
PAPERS_DIR = ROOT / "papers"
METADATA_DIR = PAPERS_DIR / "metadata"

OPENALEX_URL = "https://api.openalex.org/works"
USER_AGENT = "wharton-research-scholars/1.0"


PAPERS: list[dict[str, Any]] = [
    {
        "category": "costly_information",
        "title": "On the Impossibility of Informationally Efficient Markets",
        "year": 1980,
        "filename": "1980_grossman_stiglitz_impossibility_of_informationally_efficient_markets",
        "preferred_pdf_url": "https://academiccommons.columbia.edu/doi/10.7916/D8ZP4H27/download",
    },
    {
        "category": "costly_information",
        "title": "Information Markets and the Comovement of Asset Prices",
        "year": 2006,
        "filename": "2006_veldkamp_information_markets_and_comovement_of_asset_prices",
        "preferred_pdf_url": "https://business.columbia.edu/sites/default/files-efs/imce-uploads/lveldkamp/papers/comovement.pdf",
    },
    {
        "category": "costly_information",
        "title": "Information acquisition and mutual funds",
        "year": 2009,
        "filename": "2009_garcia_vanden_information_acquisition_and_mutual_funds",
        "preferred_pdf_url": "https://leeds-faculty.colorado.edu/garcia/paper22v14.pdf",
    },
    {
        "category": "costly_information",
        "title": "Information Immobility and the Home Bias Puzzle",
        "year": 2009,
        "filename": "2009_van_nieuwerburgh_veldkamp_information_immobility_and_home_bias",
        "preferred_pdf_url": "https://business.columbia.edu/sites/default/files-efs/citation_file_upload/Van_Nieuwerburgh_Information_Immobility.pdf",
    },
    {
        "category": "costly_information",
        "title": "Information tradeoffs in dynamic financial markets",
        "year": 2016,
        "filename": "2016_goldstein_yang_information_tradeoffs_in_dynamic_financial_markets",
        "preferred_pdf_url": "https://financetheory.org/public/storage/working_paper/00013-00.pdf",
    },
    {
        "category": "costly_information",
        "title": "Are there too many safe securities? Securitization and the incentives for information production",
        "year": 2013,
        "filename": "2013_hanson_sunderam_too_many_safe_securities",
        "preferred_pdf_url": "http://nrs.harvard.edu/urn-3:HUL.InstRepos:10578869",
    },
    {
        "category": "value_of_information",
        "title": "Estimating the Value of Information",
        "year": 2018,
        "filename": "2018_yang_estimating_the_value_of_information",
        "preferred_pdf_url": None,
    },
    {
        "category": "prediction_asset_pricing",
        "title": "Digesting Anomalies: An Investment Approach",
        "year": 2015,
        "filename": "2015_hou_xue_zhang_digesting_anomalies",
        "preferred_pdf_url": "https://www.nber.org/system/files/working_papers/w18435/w18435.pdf",
    },
    {
        "category": "prediction_asset_pricing",
        "title": "Empirical Asset Pricing via Machine Learning",
        "year": 2020,
        "filename": "2020_gu_kelly_xiu_empirical_asset_pricing_via_machine_learning",
        "preferred_pdf_url": "https://www.nber.org/system/files/working_papers/w25398/w25398.pdf",
    },
    {
        "category": "prediction_asset_pricing",
        "title": "The Characteristics that Provide Independent Information about Average U.S. Monthly Stock Returns",
        "year": 2017,
        "filename": "2017_green_hand_zhang_characteristics_independent_information",
        "preferred_pdf_url": None,
    },
    {
        "category": "alternative_data",
        "title": "Giving Content to Investor Sentiment: The Role of Media in the Stock Market",
        "year": 2007,
        "filename": "2007_tetlock_giving_content_to_investor_sentiment",
        "preferred_pdf_url": "https://business.columbia.edu/sites/default/files-efs/pubfiles/3097/Tetlock_Media_Sentiment_JF.pdf",
    },
    {
        "category": "alternative_data",
        "title": "More Than Words: Quantifying Language to Measure Firms' Fundamentals",
        "year": 2008,
        "filename": "2008_tetlock_saar_tsechansky_macskassy_more_than_words",
        "preferred_pdf_url": "https://business.columbia.edu/sites/default/files-efs/pubfiles/3096/More_Than_Words_tetlock.pdf",
    },
    {
        "category": "alternative_data",
        "title": "Big data in finance and the growth of large firms",
        "year": 2018,
        "filename": "2018_begenau_farboodi_veldkamp_big_data_in_finance",
        "preferred_pdf_url": "https://business.columbia.edu/sites/default/files-efs/citation_file_upload/BFV_BigDataBigFirm.pdf",
    },
    {
        "category": "alternative_data",
        "title": "Valuing Financial Data",
        "year": 2021,
        "filename": "2021_farboodi_singal_veldkamp_venkateswaran_valuing_financial_data",
        "preferred_pdf_url": "https://business.columbia.edu/sites/default/files-efs/pubfiles/28402/FSVV_Oct2021.pdf",
    },
    {
        "category": "alternative_data",
        "title": "Applied AI for finance and accounting: Alternative data and opportunities",
        "year": 2024,
        "filename": "2024_bhattacharya_et_al_applied_ai_alternative_data_and_opportunities",
        "preferred_pdf_url": None,
    },
    {
        "category": "alternative_data",
        "title": "Alternative data and sentiment analysis: Prospecting non-standard data in machine learning-driven finance",
        "year": 2022,
        "filename": "2022_franco_cestero_alternative_data_and_sentiment_analysis",
        "preferred_pdf_url": "https://journals.sagepub.com/doi/pdf/10.1177/20539517211070701",
    },
    {
        "category": "crowding_alpha_decay",
        "title": "The Limits of Arbitrage",
        "year": 1997,
        "filename": "1997_shleifer_vishny_limits_of_arbitrage",
        "preferred_pdf_url": "https://pages.stern.nyu.edu/~cedmond/phd/Shleifer%20Vishny%20JF%201997.pdf",
    },
    {
        "category": "crowding_alpha_decay",
        "title": "Mutual Fund Flows and Performance in Rational Markets",
        "year": 2004,
        "filename": "2004_berk_green_mutual_fund_flows_and_performance",
        "preferred_pdf_url": "https://www.nber.org/system/files/working_papers/w9275/w9275.pdf",
    },
    {
        "category": "crowding_alpha_decay",
        "title": "Does Fund Size Erode Mutual Fund Performance? The Role of Liquidity and Organization",
        "year": 2004,
        "filename": "2004_chen_hong_huang_kubik_fund_size_erodes_performance",
        "preferred_pdf_url": "https://www.aeaweb.org/articles/pdf/doi/10.1257/0002828043052277",
    },
    {
        "category": "crowding_alpha_decay",
        "title": "Presidential Address: Asset Price Dynamics with Slow-Moving Capital",
        "year": 2010,
        "filename": "2010_duffie_asset_price_dynamics_with_slow_moving_capital",
        "preferred_pdf_url": None,
    },
    {
        "category": "crowding_alpha_decay",
        "title": "Deliberate Limits to Arbitrage",
        "year": 2012,
        "filename": "2012_gromb_vayanos_deliberate_limits_to_arbitrage",
        "preferred_pdf_url": "https://personal.lse.ac.uk/makarov1/index_files/DelibArbLimits.pdf",
    },
    {
        "category": "crowding_alpha_decay",
        "title": "Does Academic Research Destroy Stock Return Predictability?",
        "year": 2016,
        "filename": "2016_mclean_pontiff_research_destroy_stock_return_predictability",
        "preferred_pdf_url": "https://www.fmg.ac.uk/sites/default/files/2020-08/Jeffrey-Pontiff.pdf",
        "authors_override": ["R. David McLean", "Jeffrey Pontiff"],
    },
    {
        "category": "crowding_alpha_decay",
        "title": "Comomentum: Inferring Arbitrage Activity from Return Correlations",
        "year": 2021,
        "filename": "2021_lou_polk_skouras_comomentum",
        "preferred_pdf_url": "https://researchonline.lse.ac.uk/id/eprint/109318/1/Comomentum.pdf",
    },
    {
        "category": "crowding_alpha_decay",
        "title": "Crowded Trades and Tail Risk",
        "year": 2021,
        "filename": "2021_barroso_chaudhury_crowded_trades_and_tail_risk",
        "preferred_pdf_url": "https://uncipc.org/wp-content/uploads/2019/02/CTTR.pdf",
    },
    {
        "category": "crowding_alpha_decay",
        "title": "Is There a Replication Crisis in Finance?",
        "year": 2023,
        "filename": "2023_jensen_kelly_pedersen_is_there_a_replication_crisis_in_finance",
        "preferred_pdf_url": "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jofi.13249",
    },
]


def reconstruct_abstract(inverted_index: dict[str, list[int]] | None) -> str:
    if not inverted_index:
        return ""
    max_position = max(max(positions) for positions in inverted_index.values())
    words = [""] * (max_position + 1)
    for word, positions in inverted_index.items():
        for position in positions:
            words[position] = word
    return re.sub(r"\s+([,.;:!?])", r"\1", " ".join(words)).strip()


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def score_candidate(target_title: str, target_year: int, result: dict[str, Any]) -> tuple[int, int]:
    title_score = 0
    if normalize(target_title) == normalize(result.get("display_name", "")):
        title_score = 2
    elif normalize(target_title) in normalize(result.get("display_name", "")):
        title_score = 1
    year = result.get("publication_year") or 0
    year_gap = abs(target_year - year) if year else 99
    return title_score, -year_gap


def search_openalex(title: str, year: int) -> dict[str, Any] | None:
    response = requests.get(
        OPENALEX_URL,
        params={
            "search": title,
            "per-page": 5,
            "select": ",".join(
                [
                    "display_name",
                    "publication_year",
                    "doi",
                    "ids",
                    "open_access",
                    "primary_location",
                    "authorships",
                    "abstract_inverted_index",
                    "biblio",
                    "cited_by_count",
                ]
            ),
        },
        headers={"User-Agent": USER_AGENT},
        timeout=30,
    )
    response.raise_for_status()
    results = response.json().get("results", [])
    if not results:
        return None
    results.sort(key=lambda result: score_candidate(title, year, result), reverse=True)
    return results[0]


def try_download_pdf(url: str | None, destination: Path) -> tuple[bool, str]:
    if not url:
        return False, "no url provided"
    try:
        response = requests.get(
            url,
            headers={"User-Agent": USER_AGENT},
            timeout=45,
            allow_redirects=True,
        )
        response.raise_for_status()
        content_type = response.headers.get("content-type", "").lower()
        if "pdf" not in content_type and not response.content.startswith(b"%PDF"):
            return False, f"not a pdf response ({content_type or 'unknown content type'})"
        destination.write_bytes(response.content)
        return True, "downloaded"
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)


def build_catalog() -> list[dict[str, Any]]:
    METADATA_DIR.mkdir(parents=True, exist_ok=True)
    catalog: list[dict[str, Any]] = []
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    for paper in PAPERS:
        result = search_openalex(paper["title"], paper["year"])
        authors = []
        abstract = ""
        doi = None
        oa_url = None
        landing_page_url = None
        cited_by_count = None
        openalex_id = None

        if result:
            authors = [
                authorship["author"]["display_name"]
                for authorship in result.get("authorships", [])
                if authorship.get("author")
            ]
            abstract = reconstruct_abstract(result.get("abstract_inverted_index"))
            doi = result.get("doi")
            cited_by_count = result.get("cited_by_count")
            oa_url = (result.get("open_access") or {}).get("oa_url")
            landing_page_url = (result.get("primary_location") or {}).get("landing_page_url")
            openalex_id = (result.get("ids") or {}).get("openalex")
        if paper.get("authors_override"):
            authors = paper["authors_override"]

        category_dir = PAPERS_DIR / paper["category"]
        category_dir.mkdir(parents=True, exist_ok=True)
        pdf_path = category_dir / f"{paper['filename']}.pdf"

        download_url = paper.get("preferred_pdf_url") or oa_url
        downloaded, download_status = try_download_pdf(download_url, pdf_path)
        if not downloaded and pdf_path.exists():
            pdf_path.unlink()

        catalog.append(
            {
                "category": paper["category"],
                "title": paper["title"],
                "year": paper["year"],
                "authors": authors,
                "doi": doi,
                "openalex_id": openalex_id,
                "cited_by_count": cited_by_count,
                "abstract": abstract,
                "preferred_pdf_url": paper.get("preferred_pdf_url"),
                "open_access_url": oa_url,
                "landing_page_url": landing_page_url,
                "stored_pdf": str(pdf_path.relative_to(ROOT)) if downloaded else "",
                "download_status": download_status,
            }
        )

    return catalog


def write_json(catalog: list[dict[str, Any]]) -> None:
    path = METADATA_DIR / "paper_catalog.json"
    path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False), encoding="utf-8")


def write_csv(catalog: list[dict[str, Any]]) -> None:
    path = METADATA_DIR / "paper_catalog.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "category",
                "title",
                "year",
                "authors",
                "doi",
                "openalex_id",
                "cited_by_count",
                "preferred_pdf_url",
                "open_access_url",
                "landing_page_url",
                "stored_pdf",
                "download_status",
                "abstract",
            ],
        )
        writer.writeheader()
        for row in catalog:
            row = dict(row)
            row["authors"] = "; ".join(row["authors"])
            writer.writerow(row)


def main() -> None:
    catalog = build_catalog()
    write_json(catalog)
    write_csv(catalog)


if __name__ == "__main__":
    main()
