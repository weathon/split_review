## Summary

This paper introduces Self-Rationalization, an iterative training recipe that improves LLM-as-judge models by: (1) generating multiple rationale–score pairs from the model itself for the same input, (2) curating preference pairs from those self-generated judgments (using ground-truth labels from the seed dataset as selection signal), and (3) fine-tuning via DPO. After two iterations on the Llama-3.1-8B-Instruct backbone, the resulting model ($J_\text{SRE}$, 8B parameters) achieves competitive or superior scores on Reward Bench, BigGen Bench, and Feedback Bench relative to similarly sized models (Prometheus-2 7B) and even the larger MoE Prometheus-2 8x7B on several metrics.

## Strengths

- **Competitive empirical results on multiple benchmarks.** $J_\text{SRE}$ (Iter 2) achieves the highest total score on Reward Bench (0.76), ties for best Human Pearson on BigGen Bench (0.52), and reaches the highest GPT4 Pearson on Feedback Bench (0.93), outperforming Prometheus-2 7B across the board and matching or exceeding Prometheus-2 8x7B on several metrics (Table 1, lines 238–244). This demonstrates that iterative DPO on self-generated rationale-score pairs yields real improvements over SFT baselines.

- **Clean ablation isolating the contribution of rationales.** Table 2 (lines 277–278) compares $J_\text{SRE}$ prompted with rationales (0.76 Reward Bench total) vs. prompted without (0.74), and both outperform $J_\text{SFT}$ (0.69). This decomposition shows that DPO itself improves scoring (0.74 vs. 0.69) and that rationale conditioning adds a further gain (0.76 vs. 0.74) — a useful separation not always shown in prior work.

- **Data efficiency relative to post-SFT alternatives.** The method uses only 5,000 samples for Iteration 1 and 500 for Iteration 2 (line 156), yet matches or exceeds methods requiring full-dataset sampling or multiple inference passes (self-consistency, Best-of-N). This is a concrete practical advantage.

- **Systematic comparison of preference curation strategies.** Table 3 (lines 297–304) tests four preference selection methods with diagnostic findings: high-margin threshold ($\geq 2$) outperforms low-margin ($\geq 1$), meta-judge suffers from score bias, and majority-voting underperforms due to noisy labels. These are practically useful results for practitioners.

- **Desiderata profile unmatched by prior work.** Table 1 (lines 127–143) shows that Self-Rationalization is the only method among six competitors that simultaneously checks all four boxes (rationales, no extra training data, <10B parameters, customizable scoring criteria) — a genuinely different point in the design space.

## Weaknesses

### Major

None. The method is sound, the results are positive, and no single issue invalidates the core claims.

### Minor

- **The "3% to 9%" improvement claim in the abstract is not uniformly supported across the results.** The abstract states that SRE "outperforms even bigger sized models trained using SFT with rationale, self-consistency or best-of-$N$ sampling by 3% to 9%." However, looking at Table 1: on BigGen Bench Human Pearson, SRE and Prometheus-2 8x7B tie at 0.52; on BigGen Bench GPT4 Pearson, SRE scores 0.65 vs. Prometheus-2 8x7B's 0.67 — SRE *loses* by ~3%. The 3–9% range cherry-picks the favorable comparisons (e.g., SRE 0.93 vs. Prometheus-2 8x7B 0.84 on Feedback Bench ≈ +10.7% relative) while ignoring metrics where the gap is smaller, zero, or negative. The paper would be stronger if it characterized the improvement honestly — e.g., "competitive with or better than larger models on most metrics" — rather than overselling a single range.

- **Novelty framing is somewhat inflated relative to the closest prior work.** The core recipe — iterative DPO on self-generated data for judge models — was previously explored in Self-taught Evaluators (Wang et al., 2024), and iterative reasoning preference optimization appears in IRPO (Pang et al., 2024). The paper differentiates itself via the combination of rationales, pointwise fine-grained evaluation, customizability, and sub-10B scale (Table 1). This is a real but incremental position: the differentiation is narrower than the paper's framing of a gap. The claim "no research has explored using DPO to specifically and automatically enhance the quality of rationales" (line 349) should be softened to acknowledge that prior work used DPO for judges — the novelty is the specific setting (fine-grained pointwise + rationales), not the overall approach.

- **The human evaluation supporting improved rationale quality is thin.** The reported 62% average win rate (55% over $J_\text{SFT}$, 69% over $J_\text{Best-of-N}$) is averaged across only 3 annotators (Figure 2 caption, line 192). The paper provides no description of who the annotators were, what instructions they received, whether they were blinded to model identity, or what the inter-annotator agreement was. Without these details and without any variance measure, the reported percentages could be within noise range. This does not invalidate the paper's main claims (the automated benchmark results are the primary support), but it cannot serve as strong standalone evidence for improved rationale quality.

- **The comparison supporting DPO over SFT for rationale-based training is confounded.** The paper argues that DPO overcomes "signal dilution" from long rationales (lines 181–185), citing Table 2 where SRE (SFT + DPO with rationales) outperforms SFT (trained without rationales). However, this comparison conflates two differences: the training objective (SFT vs. DPO) *and* the data used (original seed data vs. self-generated preference data). A cleaner test would compare: (a) SFT on seed data → (b) additional SFT on self-generated data vs. (c) DPO on the same self-generated preference pairs — to attribute gains specifically to DPO's properties rather than to additional training on more targeted data.

- **No statistical significance or variance reported.** None of the tables (1–4) include standard deviations, confidence intervals, or significance tests. Given that many of the reported improvements are small (2–4% absolute on several metrics), it is impossible to know whether these differences are meaningful or within run-to-run noise. This is a meaningful gap for a paper making comparative claims.

### Trivial

- **Weight-merging procedure for the base SFT model is underspecified.** Line 154 states that two separately trained models (pointwise and pairwise) are weight-merged to produce $J_\text{SFT}$, but no details are given about the merging method, ratio, layers, or rationale. This hinders exact reproduction.

## Nice-to-Haves

- A controlled experiment comparing SRE using preference pairs constructed from (rationale + score) vs. (score only) would more directly test whether the rationale is the source of improvement.
- A discussion of potential train/evaluation overlap would be useful: the training datasets (Feedback-Collection, Preference-Collection) and evaluation benchmarks (Feedback Bench, BiGGen Bench) come from the same research lineage.
- A computational cost comparison (total FLOPs or training time across iterations vs. baselines) would strengthen the claimed efficiency advantage.

## Removed Points

These points from the inputs were removed with brief justification:

- **"No extra training data claim is misleading" (Harsh Critic #3):** The paper is transparent that Correct-Answer Preference Pairing uses ground-truth labels from the *existing* seed dataset to construct preference pairs. "No extra training data" means no additional human annotations beyond the initial seed set — a standard and reasonable usage in self-training literature. The method includes alternatives (meta-judge, majority-voting) that do not use labels at all. This criticism misinterprets what is claimed.
- **"Meta-judge creates circular evaluation" (Harsh Critic):** The paper honestly reports that the meta-judge variant performs poorly because the model "exhibits a bias towards judgements with higher score" (line 204). Transparently reporting a failure mode is not a weakness.
- **"Histograms described only qualitatively" (Harsh Critic):** Qualitative description of figure trends is standard practice. The figure serves as visual illustration; the quantitative scores are in the tables.
- **Strength Finder's claim that "human evaluation confirms improved rationale quality":** Dropped because the strength is overstated given the thin methodology (3 annotators, no protocol detail). The human eval is a *suggestive* result but not a confirmed finding.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface a gap between the paper's strong framing and its incremental evidence, but do not identify a fundamentally new angle or unrecognized implication of the work.

## Suggestions

1. Recalibrate the abstract and introduction claims. Replace "outperforms... by 3% to 9%" with a more precise characterization (e.g., "achieves competitive or better results on most metrics, matching or exceeding larger models on several benchmarks").
2. Add standard deviations or confidence intervals for at least the main benchmark results (Table 1).
3. Expand the human evaluation: report inter-annotator agreement, describe the annotation protocol (annotator background, instructions, blinding), and ideally increase the number of annotators.
4. Add a controlled ablation: train SRE with preference pairs using (score only) vs. (rationale + score) to directly attribute the gain to rationale conditioning.
5. Provide details of the weight-merging procedure for reproducibility.
6. Soften the novelty claim in Section 5 to explicitly acknowledge that iterative DPO for judge models appears in Self-taught Evaluators, and clarify that the contribution is the specific combination with fine-grained pointwise evaluation and rationales.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>