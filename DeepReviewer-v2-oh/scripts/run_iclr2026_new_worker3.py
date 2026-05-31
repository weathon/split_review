from __future__ import annotations

import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATASET = Path('/home/wg25r/split_review/datasets/iclr2026_new')
WORKERS = 1

os.chdir(ROOT)
sys.path.insert(0, str(ROOT))
os.environ['PARSED_PAPERS_DIR'] = str(DATASET / 'papers')
os.environ['PAPER_SEARCH_ENABLED'] = 'false'
os.environ['PAPER_SEARCH_PROVIDER'] = 'offline'
os.environ['MIN_PAPER_SEARCH_CALLS_FOR_PDF_ANNOTATE'] = '0'
os.environ['MIN_PAPER_SEARCH_CALLS_FOR_FINAL'] = '0'
os.environ['MIN_DISTINCT_PAPER_QUERIES_FOR_FINAL'] = '0'


def run_pdf(pdf_path_text: str) -> dict:
    os.chdir(ROOT)
    sys.path.insert(0, str(ROOT))
    os.environ['PARSED_PAPERS_DIR'] = str(DATASET / 'papers')
    os.environ['PAPER_SEARCH_ENABLED'] = 'false'
    os.environ['PAPER_SEARCH_PROVIDER'] = 'offline'
    os.environ['MIN_PAPER_SEARCH_CALLS_FOR_PDF_ANNOTATE'] = '0'
    os.environ['MIN_PAPER_SEARCH_CALLS_FOR_FINAL'] = '0'
    os.environ['MIN_DISTINCT_PAPER_QUERIES_FOR_FINAL'] = '0'

    from main import _create_job
    from deepreview.runner import run_job
    from deepreview.state import load_job_state

    pdf_path = Path(pdf_path_text)
    job = _create_job(pdf_path, title=pdf_path.stem)
    print(json.dumps({'event': 'sample_start', 'paper_id': pdf_path.stem, 'job_id': str(job.id)}), flush=True)
    run_job(str(job.id))

    state = load_job_state(job.id)
    if state is None:
        raise RuntimeError(f'Job state missing after run: {job.id}')
    if state.status.value != 'completed':
        raise RuntimeError(f'Job failed: {job.id}: {state.error}')

    return {
        'event': 'sample_done',
        'paper_id': pdf_path.stem,
        'job_id': str(job.id),
        'status': state.status.value,
        'annotation_count': state.annotation_count,
        'final_markdown_path': state.artifacts.final_markdown_path,
        'report_pdf_path': state.artifacts.report_pdf_path,
        'usage': state.usage.model_dump(mode='json'),
        'completed_at': datetime.now(timezone.utc).isoformat(),
    }


pdfs = sorted((DATASET / 'pdfs').glob('*.pdf'))
if not pdfs:
    raise RuntimeError(f'No PDFs found: {DATASET / "pdfs"}')

missing = [str(DATASET / 'papers' / f'{pdf_path.stem}.txt') for pdf_path in pdfs if not (DATASET / 'papers' / f'{pdf_path.stem}.txt').exists()]
if missing:
    raise RuntimeError('Missing parsed paper files:\n' + '\n'.join(missing))

started_at = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
out_path = ROOT / 'data' / 'batch_runs' / 'iclr2026_new_worker3_20260523T020740Z.jsonl'
out_path.parent.mkdir(parents=True, exist_ok=True)

done_papers = set()
if out_path.exists():
    for line in out_path.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row['event'] == 'sample_done' and row['status'] == 'completed':
            done_papers.add(row['paper_id'])

pdfs_to_run = [pdf_path for pdf_path in pdfs if pdf_path.stem not in done_papers]

start = {
    'event': 'batch_start',
    'dataset': str(DATASET),
    'workers': WORKERS,
    'count': len(pdfs),
    'resume_completed': len(done_papers),
    'remaining': len(pdfs_to_run),
    'output': str(out_path),
    'started_at': started_at,
}
print(json.dumps(start, ensure_ascii=False), flush=True)
with out_path.open('a', encoding='utf-8') as f:
    f.write(json.dumps(start, ensure_ascii=False) + '\n')

with ProcessPoolExecutor(max_workers=WORKERS) as pool:
    futures = [pool.submit(run_pdf, str(pdf_path)) for pdf_path in pdfs_to_run]
    for future in as_completed(futures):
        row = future.result()
        print(json.dumps(row, ensure_ascii=False), flush=True)
        with out_path.open('a', encoding='utf-8') as f:
            f.write(json.dumps(row, ensure_ascii=False) + '\n')

done = {
    'event': 'batch_done',
    'count': len(pdfs),
    'resume_completed': len(done_papers),
    'ran': len(pdfs_to_run),
    'output': str(out_path),
    'completed_at': datetime.now(timezone.utc).isoformat(),
}
print(json.dumps(done, ensure_ascii=False), flush=True)
with out_path.open('a', encoding='utf-8') as f:
    f.write(json.dumps(done, ensure_ascii=False) + '\n')
