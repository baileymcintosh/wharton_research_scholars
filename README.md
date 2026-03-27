# Wharton Research Scholars

Repository structure:

- `docs/project_outline.pdf`: your original project outline
- `research/literature_map.md`: synthesized literature review and project-positioning note
- `research/build_paper_library.py`: rebuilds the paper catalog and downloads open PDFs where available
- `papers/`: categorized paper library
- `papers/metadata/paper_catalog.json`: full metadata catalog
- `papers/metadata/paper_catalog.csv`: spreadsheet-friendly version of the catalog

The paper library is grouped into:

- `costly_information`
- `value_of_information`
- `prediction_asset_pricing`
- `alternative_data`
- `crowding_alpha_decay`

To refresh the library metadata, run:

```powershell
python research\build_paper_library.py
```
