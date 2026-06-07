Now I have enough calibration anchors. Let me finalize the review.

**Round 1 bracket**: Based on weak anchors (3.00–3.20), middle anchors (4.40–6.00), and strong anchors (8.00), this paper clearly sits in the middle band. Narrow bracket: **5.0–6.5**.

**Round 2 narrowing**: Compared to `thbtoAkCe9` (D² Pruning, 5.60, Accept) — similar profile: novel method for data selection, marginal but consistent gains, broad evaluation. Compared to `Fty0wTcemV` (DELIFT, 6.00, Accept) — more sophisticated method but narrower paradigm coverage. Compared to `FAfxvdv1Dy` (STAFF, 6.50, Accept) — clearly stronger methodology and results. The paper is comparable to the 5.60 anchor but has a significant weakness (no variance) that the D² Pruning paper also shared. Final score: **5.5**.

---

## Summary
This paper proposes High-Entropy Sum (HES), a training-free metric that sums the entropy of the top 0.5% highest-entropy tokens in a reasoning trajectory, and uses it to select training data across SFT, RFT, and RL paradigms. The key empirical finding is that pruning the lowest-HES data and training on the remaining subset consistently outperforms full-dataset training across multiple models, datasets, and domains.

## Strengths
- **Three-paradigm validation**: HES is validated across SFT (Tables 1–4), RFT (Table 5), and RL (Table 6) with consistent improvements over random selection and heuristic baselines. This breadth of applicability is unusual for a training-free selection method.
- **Replicated "prune low-HES to beat full-dataset" result**: The finding that training on the top 80% HES-ranked data surpasses full-dataset training is replicated across four settings: Qwen3-8B on Open-Math-Reasoning (35.36 vs 32.61), DeepSeek-R1-Distilled-7B on OpenR1-Math-220k (32.35 vs 30.22), Code domain (39.51 vs 36.28), and STEM domain (45.48 vs 44.42). This provides converging evidence that HES identifies genuinely harmful samples.
- **Thorough ablation design**: The SFT experiments (Table 1) compare HES against four entropy variants (AvgE, AvgHE, Entropy Sum, HES_absolute), plus difficulty-based, length-based, and forking-only baselines—11 comparison settings total. The systematic degradation from HES → ES → AvgHE → AvgE validates each design choice.
- **Small-to-large model transfer**: A 0.6B proxy model selecting data for 8B training achieves comparable performance to 8B self-selection (32.12 vs 31.14), demonstrating HES captures data-intrinsic complexity rather than model-specific artifacts, enabling cost-effective curation.
- **Training-free with zero marginal cost**: HES uses token log-probabilities from the generation pass—no external reward models, no auxiliary training, no additional forward passes.

## Weaknesses

### Fatal
None.

### Major
- **No variance or statistical significance reported**: All results are point estimates from pass@1 over 16 samples with no confidence intervals, standard errors, or multi-seed replication. Several headline claims rest on small differences: RL gains (21.30 vs 20.63, +0.67), RFT per-query k=2 (31.38 vs 30.37, +1.01). Across 7–8 benchmarks with no correction for multiple comparisons, some per-benchmark "wins" could be within sampling noise. Without any variance estimates, the reader cannot assess whether the reported gaps are meaningful. This substantially undermines confidence in the central empirical claims and is the paper's most significant weakness.

### Minor
- **Conceptual tension in Figure 1 motivation is not addressed**: Figure 1 shows incorrect samples have *much higher* HES than correct ones (normalized means 0.68 vs 0.29). The method then proposes selecting *highest-HES* samples for training. The resolution (selecting highest-HES from within already-correct pools in RFT/RL, or from reference solutions in SFT) is implicit but never explicitly grappled with. The paper does not discuss whether borderline-correct, high-uncertainty solutions might reinforce fragile reasoning patterns, leaving a gap in the conceptual justification.
- **Flat sensitivity curves in non-math domains**: Figure 4 shows identical performance across all entropy ratios (0.005, 0.05, 0.5, 1.0) for MMLU STEM (flat at 0.855) and LiveCodeBench (flat at 0.544). This means the specific high-entropy-token focus provides no discriminative benefit over any other entropy aggregation in those domains. This qualifies the paper's claim that HES specifically "captures intrinsic reasoning quality signals common across diverse logic-intensive tasks."
- **Forking-Only not compared at equivalent data budgets**: The Forking-Only baseline (loss-weighting on high-entropy tokens, from Wang et al. 2025) achieves 32.51, nearly matching Full-Dataset (32.61), but is always run on 100% data. Without running Forking-Only on HES-selected subsets, the paper cannot determine whether data selection provides benefits beyond what loss-weighting already captures.
- **Missing specification of entropy-computation model in SFT**: For the SFT setting where data consists of pre-written reference solutions (not model-generated), the paper never states which model is used to compute token entropies. This affects reproducibility and practical cost assessment.
- **RL selection strategy underspecified**: The RL section says "select half with the highest HES from the pool of successful trajectories" but does not clarify whether this selection is done per GRPO step (from each batch's rollouts) or globally (across a pre-generated pool), which matters for both practicality and interpretation.

### Trivial
- **Abstract overclaim**: The abstract states HES-20% "matches full-dataset performance," which holds for Table 2 (34.61 vs 30.22) but not Table 1 (31.14 vs 32.61, a 1.47-point gap). The claim should be qualified.
- **Small-model proxy outperforms self-selection without explanation**: The 0.6B and 1.7B proxy models select better data for 8B training than the 8B model does for itself (32.12 and 31.28 vs 31.14). The paper treats this as an unalloyed positive but does not explore why a weaker model's uncertainty signal might be superior, which is a missed analytical opportunity.

## Nice-to-Haves
- A qualitative analysis comparing high-HES vs low-HES correct reasoning paths (are they more thorough, contain more verification steps, more backtracking?) would strengthen the explanatory contribution.
- Intermediate entropy ratios between 0.005 and 0.05 in the sensitivity analysis would better justify the 0.5% choice.
- Running at least one replication seed for the RL experiments (where gains are narrowest) would substantially strengthen confidence.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "HES provides zero discriminative power in non-math domains" based on flat Figure 4 curves**: The flat curves indicate that the entropy ratio hyperparameter doesn't matter for MMLU STEM and LiveCodeBench, not that HES data selection fails. Tables 3–4 show HES outperforms baselines in code and STEM domains. This criticism was an overstatement of what the flat curves actually show. Removed.
- **Harsh Critic: repeated paragraph (lines 232–236 duplicated)**: This is a parser formatting artifact, not an author error. Removed per hard rules.
- **Harsh Critic: notation error on line 127 ("different from AvgHE" should be "different from AvgE")**: A minor typo/formatting issue. Removed per hard rules.
- **Harsh Critic: GRPO description is "boilerplate"**: The GRPO preliminaries section is standard background that provides necessary context. Criticizing its presence is scope creep. Removed.
- **Strength Finder: "Sensitivity analysis confirms robustness to hyperparameter choices"**: Partially invalidated by the flat curves in Figure 4 for non-math domains, where all entropy ratios perform identically. The robustness may simply reflect that the entropy ratio doesn't matter in those domains rather than confirming HES is well-tuned. Kept the relevant concern, removed the blanket strength claim.
- **Strength Finder: generic strengths about problem importance**: Removed as not concrete or specific enough to this paper.

## Novel Insights
The most interesting insight from the paper—and one that distinguishes it from prior work—is the asymmetric treatment of positive and negative samples in RL: curating positives for quality (high HES) while preserving negatives for diversity (random) outperforms both full-batch training and any symmetric curation strategy. The ablation showing that curated negative samples (Neg-Low) degrade performance provides concrete evidence that exposure to diverse failure modes is critical. This principle—that selection quality matters differently for positive and negative examples—has implications beyond HES.

## Suggestions
- Report binomial confidence intervals for all pass@1 results and run at least one multi-seed replication for the RL experiments where gains are narrowest.
- Add an explicit discussion of why high-HES correct trajectories are valuable training data despite high HES being characteristic of incorrect trajectories in aggregate.
- Run Forking-Only on HES-selected data subsets to enable fair comparison between loss-weighting and data-selection approaches.
- Specify which model computes token entropies in the SFT setting and clarify whether RL selection is per-step or global.

---

**Calibration anchors consulted:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| `z3DMFpaP6m` (Entropy of LMs) | 3.00 | R1 | Weaker — proposed a metric but had fundamental issues |
| `EOPLy80bBm` (Data Pruning) | 3.00 | R1 | Weaker — systematic study but limited novelty |
| `OdoS6cH8MP` (Data Valuation) | 2.00 | R1 | Much weaker |
| `qUJsX3XMBH` (Random Selection is All You Need) | 4.40 | R1 | Our paper is stronger — HES demonstrably beats random across paradigms |
| `DKkQtRMowq` (DS² Curation) | 5.75 | R1 | Comparable — our paper has broader paradigm coverage but weaker experimental rigor |
| `7qMrDf9zFU` (Priority on High-Quality) | 4.75 | R1 | Our paper is stronger in breadth and methodological clarity |
| `Fty0wTcemV` (DELIFT) | 6.00 | R1/R2 | Slightly stronger — more sophisticated method but narrower coverage |
| `mMPMHWOdOy` (WizardMath) | 8.00 | R1 | Much stronger — SOTA results, significant method |
| `f4gF6AIHRy` (Submodular File Selection) | 8.00 | R1 | Much stronger |
| `FAfxvdv1Dy` (STAFF) | 6.50 | R2 | Stronger — better methodology and results |
| `thbtoAkCe9` (D² Pruning) | 5.60 | R2 | Closest comparison — similar profile: novel method, broad evaluation, modest gains, no variance reporting. Accepted. |
| `diKRhKs5yl` (FEEDER) | 5.25 | R2 | Our paper is stronger in contribution breadth |
| `I5p1Gm8GFS` (3DS) | 5.75 | R2 | Comparable methodological sophistication |
| `SpTzsQjgxF` (Rule-Based Rating) | 5.75 | R2 | Our paper is simpler and more broadly validated |

**Round 1 bracket**: 5.0–6.5. **Round 2 narrowed to**: 5.5 — closest to D² Pruning (5.60, Accept) in contribution profile, with similar strengths (broad evaluation, novel method) and weaknesses (marginal gains, no variance). Scored slightly below D² Pruning due to the unresolved conceptual tension in Figure 1.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>