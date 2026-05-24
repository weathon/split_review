# Prompt Combination Sweep

Backup created: `prompts.bak.sweep_1779405851`

## Recon

Canonical active prompt files checked against `prompts.bak/` and `prompts.bak.2/`.

Files identical across all three canonical versions:
`bare_baseline.md`, `cal_without.md`, `claims.md`, `find_human_match.md`,
`harsh_critic_position.md`, `merger_agent.md`, `merger_position.md`,
`neutral_reviewer_position.md`, `related_work.md`, `related_work_filter.md`,
`scorer.md`, `spark_finder.md`, `timeline.md`.

Non-canonical extras:
`prompts/harsh_critic.md.soft`, `prompts/harsh_critic.md.old`,
`prompts/cal_with.md.2.round`, `prompts.bak/harsh_critic.md.new`,
`prompts.bak/cal_with.md.2`, `prompts.bak.2/harsh_critic.md.new`,
`prompts.bak.2/cal_with.md.2`.

Runtime-relevant sweep dimensions:

| File | v0 = `prompts/` | v1 = `prompts.bak/` | v2 = `prompts.bak.2/` | Difference summary |
| --- | --- | --- | --- | --- |
| `cal_with.md` | 3 score-band queries: high >7.5, mid 3.5-7.5, low <3.5; must read at least one paper per bin | Same as v0 but also asks for 2-3 unrestricted pattern queries | Asks for 2-3 unrestricted pattern queries plus 2-3 broader score-band queries: >=8, 5-8-ish, 3-5, <3 | v0 is cheapest and most forced-anchor; v1 adds paper-specific retrieval; v2 is broader and less exact about bins |
| `harsh_critic.md` | Same as v2 | Softer/fairer critic: judge within paper class, avoid inflating minor concerns, prose improvement sections instead of nested checklists | Harsher critic: explicitly critical, structured missing-experiment/checklist categories, stronger accept/reject stance | v1 should improve diversity/fairness across paper types; v2 may catch more fatal flaws but risks checklisty generic reviews |
| `neutral_reviewer.md` | Same as v1 | Requires concrete section/equation/table/claim evidence; contribution restatement is not itself a strength | Looser evidence requirement; restating supported contributions can count | v0/v1 are stricter and should reduce generic praise; v2 may raise scores by keeping more strengths |
| `merger.md` | v1 plus aggressive filtering discipline and stronger high-score calibration language | Adds inaccessible-paper error, stricter invalid-strength removal, speculative-fatal demotion, and own-terms improvement handling | Less filtering; old strength filtering has commented-out stricter text; fatal handling is less calibrated | v0 should reduce duplicated/speculative weaknesses; v1 is less aggressive; v2 likely keeps more input noise |

Existing baseline:

| CSV | Papers | Spearman raw | Pearson raw | MAE raw | Decision accuracy | AUROC |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `results/test_mini_detail_one_search.csv` | 40 | 0.5378 | 0.6074 | 1.6517 | 70.0% | 0.7835 |

## Experiments

| Experiment | Prompt combo | Output | Metric | Observations |
| --- | --- | --- | --- | --- |
| `sweep_v1` | active at run time: `cal_with` v0, `harsh_critic` v0/v2, `neutral_reviewer` v0/v1, `merger` v0 | `results/sweep_v1/scores.csv` | 99 papers: Spearman raw 0.5433, Pearson raw 0.5559, MAE raw 1.5645, decision accuracy 74.7%, AUROC 0.8025 | One failed/generated-bad row was removed before metric calculation. Going forward, if a few papers fail, do not retry by default; calculate metrics on completed rows as-is. |
| `sweep_v3` | hybrid: `cal_with` v1, `harsh_critic` v1, `neutral_reviewer` v0/v1, `merger` v0 | `results/sweep_v3/scores.csv` | 99 papers: Spearman raw 0.5998, Pearson raw 0.6279, MAE raw 1.6484, decision accuracy 75.8%, AUROC 0.8546 | Stronger correlation but qualitatively too sycophantic/high-biased. Likely cause: `harsh_critic` v1 softens the critic, ignores the anti-downgrading paragraph via `&&`, and adds own-class/own-terms language that over-excuses weak papers. |
| `sweep_v4` | hybrid: `cal_with` v1, `harsh_critic` v0/v2, `neutral_reviewer` v0/v1, `merger` v0 | `results/sweep_v4/scores.csv` | 100 papers: Spearman raw 0.5572, Pearson raw 0.5080, MAE raw 1.5359, decision accuracy 77.0%, AUROC 0.7941 | Less sycophantic than `sweep_v3`; best MAE and decision accuracy so far, but rank correlation drops. Expanded calibration alone helps MAE/bias more than Spearman. |
| `sweep_v5` | hybrid: `cal_with` v2, `harsh_critic` v0/v2, `neutral_reviewer` v0/v1, `merger` v0 | `results/sweep_v5/scores.csv` | 100 papers: Spearman raw 0.6164, Pearson raw 0.6341, MAE raw 1.5143, decision accuracy 77.0%, AUROC 0.8079 | Best Spearman, Pearson, and MAE so far. Broader calibration recovers rank correlation with the strict critic, but bias rises to +1.1861 and AUPRC drops to 0.5812. |
| `sweep_v6` | hybrid: `cal_with` v2, `harsh_critic` v0/v2, `neutral_reviewer` v0/v1, `merger` v1 | `results/sweep_v6/scores.csv` | 97 papers: Spearman raw 0.4775, Pearson raw 0.4867, MAE raw 1.4648, decision accuracy 74.2%, AUROC 0.7158 | Calculated as-is on completed rows. The middle merger lowers bias to +0.8413 but loses too much ranking and decision signal, so it is worse than `sweep_v5` overall. |

## Prompt Direction

For the final installed prompt, reduce preference for my own accept/reject decision and make the merger follow paper-grounded review quality checks more directly. Use the following error types as filters when they make sense for weaknesses or strengths, not as a mandatory checklist:

- Misunderstanding: reviewer misreads the paper's claims or ideas.
- Neglect: reviewer overlooks details explicitly stated in the paper.
- Vague critique: reviewer claims something is missing without identifying what.
- Out-of-scope: reviewer asks for work beyond the paper's stated scope.
- Invalid criticism: reviewer suggests impractical experiments or trivializes valid results.
- Misinterpret novelty: reviewer questions novelty without relevant references.
- Superficial review: reviewer gives generic unsupported comments.
- Writing: reviewer praises writing when the paper needs more clarity or explicitness.
- Inexpert statement: reviewer raises concerns that reveal lack of domain knowledge.
- Experiment: reviewer praises experiments when more baselines or tests are needed, or criticizes experiment design incoherently.
- Unstated statement: reviewer says something unsupported by the paper.
- Contradiction: reviewer contradicts itself.

Active prompt after `sweep_v6`: restored to the best evaluated base combo from `sweep_v5`
(`cal_with` v2, `harsh_critic` v0/v2, `neutral_reviewer` v0/v1, `merger` v0), then edited
`prompts/merger.md` to add the error-type filters above as optional review-quality criteria and
to reduce reliance on any supplied/preferred decision when assigning the final score.
