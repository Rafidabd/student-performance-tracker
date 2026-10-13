from pathlib import Path

def ensure_reports_folder():
  
    reports_folder = Path(__file__).resolve().parent.parent / "Reports"
    reports_folder.mkdir(parents=True, exist_ok=True)
    return reports_folder    