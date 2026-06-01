#!/usr/bin/env python3

import json
from pathlib import Path
from collections import defaultdict

with open('meta/ac_issues_all.json', 'r') as f:
    ac_issues = json.load(f)

with open('all_notes.json', 'r') as f:
    all_notes = json.load(f)

accepted_papers = set()
for paper in all_notes:
    if 'Accept' in paper.get('decision', ''):
        accepted_papers.add(paper['paper_id'])

print(f"Total accepted papers: {len(accepted_papers)}")

models = [
    '2026_baseline_claude',
    '2026_sonnet_repro',
    '2026_deepseek_response',
    '2026_qwen_repro',
]

papers_with_remaining = [pid for pid, data in ac_issues.items()
                         if data['remaining_count'] > 0 and pid in accepted_papers]
papers_with_resolved = [pid for pid, data in ac_issues.items()
                       if data['resolved_count'] > 0 and pid in accepted_papers]

print(f"Accepted papers with remaining issues: {len(papers_with_remaining)}")
print(f"Accepted papers with resolved issues: {len(papers_with_resolved)}")

coverage_stats = defaultdict(lambda: {
    'remaining_found': 0,
    'remaining_total': 0,
    'resolved_found': 0,
    'resolved_total': 0,
    'papers_reviewed': 0,
})

for model in models:
    review_dir = Path('results') / model / 'reviews'

    if not review_dir.exists():
        print(f"⚠ {model}: reviews dir not found")
        continue

    remaining_total = 0
    remaining_found = 0
    resolved_total = 0
    resolved_found = 0
    papers_reviewed = 0

    for paper_id in papers_with_remaining + papers_with_resolved:
        review_file = review_dir / f"{paper_id}.md"

        if not review_file.exists():
            continue

        papers_reviewed += 1
        review_text = review_file.read_text()

        if paper_id in ac_issues and ac_issues[paper_id]['remaining_count'] > 0:
            for issue in ac_issues[paper_id]['remaining_issues']:
                remaining_total += 1
                keywords = [word for word in issue.split() if len(word) > 5]
                if any(keyword.lower() in review_text.lower() for keyword in keywords[:3]):
                    remaining_found += 1

        if paper_id in ac_issues and ac_issues[paper_id]['resolved_count'] > 0:
            for issue in ac_issues[paper_id]['resolved_issues']:
                resolved_total += 1
                keywords = [word for word in issue.split() if len(word) > 5]
                if any(keyword.lower() in review_text.lower() for keyword in keywords[:3]):
                    resolved_found += 1

    coverage_stats[model] = {
        'remaining_found': remaining_found,
        'remaining_total': remaining_total,
        'resolved_found': resolved_found,
        'resolved_total': resolved_total,
        'papers_reviewed': papers_reviewed,
    }

print("\n" + "="*80)
print("COVERAGE RESULTS (Accepted Papers Only)")
print("="*80)
print(f"{'Model':<30} {'Remaining (high↑)':<25} {'Resolved (low↓)':<25}")
print("-"*80)

for model in models:
    stats = coverage_stats[model]
    if stats['papers_reviewed'] == 0:
        print(f"{model:<30} No reviews found")
        continue

    remaining_rate = stats['remaining_found'] / max(1, stats['remaining_total'])
    resolved_rate = stats['resolved_found'] / max(1, stats['resolved_total'])

    print(f"{model:<30} {remaining_rate*100:>6.1f}% ({stats['remaining_found']}/{stats['remaining_total']:<5})    {resolved_rate*100:>6.1f}% ({stats['resolved_found']}/{stats['resolved_total']:<5})")

with open('meta/issue_coverage_results.json', 'w') as f:
    json.dump({
        'test_scope': 'accepted_papers_only',
        'coverage_by_model': dict(coverage_stats)
    }, f, indent=2)

print("\n✓ Saved to meta/issue_coverage_results.json")
