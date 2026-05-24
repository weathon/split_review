## Summary

This paper presents PELICAN, a two-stage adaptive tutoring framework that (1) collaboratively diagnoses a student's cognitive state via a successor-first questioning strategy with an expert-assistant-verifier pipeline, then (2) selects teaching strategies using a fast/slow-thinking mechanism (Simulated Teaching Tree) that simulates future dialogue paths. Experiments on the Gaokao dataset (184 exam questions) with simulated students show improvements in diagnosis accuracy (F1=94.31 vs. 79.83 for CoT) and tutoring coverage/quality. A real-world evaluation with 169 high school students (1,335 reports) shows PELICAN achieving the highest success rate (86.8%) and human-rated quality scores among baselines.

## Strengths

- **Well-motivated two-stage framework with clear methodology.** The successor-first diagnostic strategy (Section 3.2) exploits hierarchical knowledge structure to efficiently assess mastery, and the addition of the expert-assistant-verifier pipeline demonstrably improves diagnostic accuracy (Table 1: F1=94.31 vs. 93.08 without pipeline). This is a concrete, verifiable improvement over the Free-Prompt and CoT baselines.

- **Inclusion of a real human evaluation with 169 high school students.** Table 6 shows PELICAN achieving the highest scores across all human-rated dimensions (Appropriateness 4.23, Sentiment 4.42, Inspiration 4.33, Overall 4.39) and the highest success rate (86.8% vs. 85.2% for Free-Prompt). This provides ecological validity beyond simulated experiments and is a significant effort for an education paper.

- **Comprehensive ablation and backbone analysis.** Tables 3 and 4 decompose the contributions of cognitive diagnosis and slow thinking, and demonstrate functionality across four different LLM backbones (LLaMA-3.1-8B, GLM-4-PLUS, Qwen-max, GPT-4o), supporting generalizability beyond a single model.

- **Strategy adaptation analysis (Figure 4)** confirms that the diagnosed cognitive state drives meaningful personalization: analogies are used more for low-level students (22%) than high-level (15%), aligning with pedagogical theory. This provides evidence that the framework's personalization is operational, not just claimed.

## Weaknesses

### Major

- **Unsubstantiated abstract claims.** The abstract states "significant improvements in critical thinking stimulation (+18.7%) and task completion rates (+22.4%) compared to baseline models." These specific percentages do **not** appear in any table, figure, or text of the experimental section. The paper's reported results (Table 2, Table 6) show different margins: e.g., Overall score 4.33 vs. 3.60 (+20.3% relative over Free-Prompt), success rate 86.8% vs. 85.2% (+1.6% absolute). The source of +18.7% and +22.4% cannot be determined from the paper as written. This is a serious credibility issue — the abstract makes concrete quantitative claims that the paper does not substantiate.

- **Unexplained inconsistency between main results and ablation/backbone tables.** PELICAN's own numbers differ dramatically between Table 2 and Tables 3/4. In Table 2, PELICAN achieves R_coverage = **72.36** and F_frequency = **72.06**. Yet in Table 3 (module ablation, "PELICAN" row) and Table 4 (backbone ablation, "Ours(GPT-4o)" row), the same method achieves R_coverage = **54.84** and Frequency = **61.47** — a gap of roughly 17–24 points. The paper does not explain whether the ablation experiments were run on a different subset, with different configurations, or under different conditions. This undermines confidence in the quantitative evidence, because the reader cannot tell which set of numbers reflects the true performance of the method.

- **Circularity of the coverage/frequency metrics not acknowledged.** R_coverage and F_frequency measure "the proportion and frequency of non-mastered knowledge points addressed by the teacher." PELICAN explicitly diagnoses which points are not mastered and then targets them in tutoring. It is therefore nearly tautological that it scores higher on these metrics than methods without diagnosis. The paper presents the large coverage/frequency advantages (Table 2, 72.36 vs. 59.81 for Free-Prompt) as strong evidence of superior tutoring, without acknowledging that the metric primarily rewards doing what PELICAN was designed to do. The GPT-based quality scores (Suitability, Logic, Inspiration, Overall) are more meaningful, and PELICAN's advantages there are more modest.

### Minor

- **LLM-as-judge bias unaddressed.** All GPT-based evaluations (Tables 2, 3, 4) are performed by an LLM judge where the method itself uses GPT-4o as the backbone. It is well-documented that LLM judges exhibit a preference for outputs matching their own generation style. The paper does not mention this potential bias, nor does it provide calibration, human-validation of the GPT scores, or any discussion of why this concern may not apply here. The human evaluation (Table 6) partially mitigates this issue, but uses different metrics, and the paper does not explicitly reconcile the two evaluation regimes.

- **Human evaluation gains are modest in practical terms.** While PELICAN leads in all human-rated dimensions, the success rate improvement over Free-Prompt is only +1.6 percentage points (86.8% vs. 85.2%), and Stepwise achieves 86.5%. The paper does not discuss effect sizes, confidence intervals, or the practical significance of these margins. The claims of "strong consistency with the GPT-based evaluation" (Section 4.6) are not backed by a quantitative analysis of the relationship between the two evaluations.

- **No limitations or failure analysis section.** The paper concludes without any discussion of limitations, failure cases, or conditions under which the method might underperform. For a system that depends on an LLM backbone, a simulated student model (described only in a stripped appendix), and a modest slow-thinking budget (M=1, k=2, m=2), the absence of any critical self-assessment is notable.

### Trivial

- In Table 3, the column header reads "Frequency" while Table 2 uses "F_frequency" — minor naming inconsistency for what appears to be the same metric.

## Nice-to-Haves

- Justification or sensitivity analysis for the slow-thinking parameters (M=1, k=2, m=2). With M=1, slow thinking activates after a single round — this is a very low threshold for "persistent cognitive challenges."
- A cost-benefit discussion: slow thinking consumes ~40% of tokens (230k out of 580k), yet the paper does not analyze whether the improvements justify the overhead.
- A formal description (pseudocode) of the successor-first diagnostic strategy would improve reproducibility.

## Removed Points

The following points from the reviewers were removed after verification:

- **"Related work is thin / does not critically evaluate"** — This is a subjective characterization, not an error. The related work adequately covers the key areas (personalized tutoring, cognitive diagnosis) and cites relevant prior work. While deeper critical engagement would strengthen the paper, this is a matter of degree, not a substantive flaw.
- **"Successor-first strategy not formally defined"** — The paper provides a clear natural-language description (Section 3.2: "prioritizes assessing leaf nodes or nodes whose successors have already been evaluated"). Pseudocode would be helpful but is not required for reproducibility of the core idea.
- **"Simulated student model is critical but in appendix"** — Appendix content is stripped by the parser, not absent from the original submission.
- **"Variance discrepancy in Table 2 standard errors"** — While the SE for R_coverage (±4.69) is indeed much larger than for GPT scores (±0.003), this is not necessarily suspicious: coverage is a behavioral metric computed over interactions and subject to student-model variance, while GPT scores are averages over a deterministic judge. The paper could explain this, but the disparity itself is not inherently problematic.
- **"Table 4 GPT-4o trails Qwen-max on coverage"** — The text notes "the GPT-4 model excels in suitability, logic, inspiration," which is accurate; the coverage comparison is a secondary observation that does not contradict the main claims.
- **"No statistical tests for Figure 4 strategy distribution"** — Figure 4 is presented as a descriptive analysis of strategy usage, not a hypothesis test. The values are stated as exact percentages, but this is a common reporting convention for categorical distributions over a fixed sample. Asking for statistical testing on every figure is scope creep.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Remove or trace the abstract's quantitative claims.** Either provide the exact metric, baseline, and computation that yields +18.7% and +22.4%, or remove these numbers from the abstract. They currently create an expectation the paper does not fulfill.

2. **Explain the Table 2 vs. Tables 3/4 discrepancy.** If the ablation experiments used a different subset (e.g., a smaller development set for efficiency), state this explicitly and justify why the comparison is still informative. If the settings are the same, the inconsistency must be resolved before the numbers can be trusted.

3. **Acknowledge and contextualize the coverage metric circularity.** Clarify that R_coverage and F_frequency are diagnostic metrics that measure alignment between teacher focus and diagnosed gaps, not tutoring quality per se. Reframe the paper's claims accordingly, emphasizing the GPT-based quality scores and human evaluation as the primary evidence of tutoring effectiveness.

4. **Add a Limitations section** discussing at minimum: (a) reliance on GPT-4o as both backbone and judge, (b) dependence on a simulated student model whose fidelity is unvalidated, (c) narrow scope (Gaokao math only), and (d) shallow slow-thinking budget.

## Score and Decision

**Bracket**: Round 1 placed the paper between weak anchors (avg 2.33–3.25) and middle anchors (avg 4.0–5.33). Round 2 narrowed to 4.5–5.5 by comparing against TestAgent (4.75), CITING (5.0), KCQRL (5.33), and SOE (5.0) — all rejected but with recognizable contributions.

**Anchors consulted**:
- iucVyVC8jQ (3.25): Dual-fusion CDM framework; weaker methodology and unclear contributions than PELICAN.
- s6X3s3rBPW (4.00): Adaptive testing for LLMs; good idea but unclear motivation, similar severity of issues to PELICAN but less experimental depth.
- lXwhR7uci1 (4.75): TestAgent for human assessment; comparable framework novelty and evaluation breadth, similar missing-detail problems.
- BzvVaj78Jv (5.00): SOE for virtual student agents; comparable AI4Education contribution with human evaluation, but PELICAN has stronger methodological novelty.
- nLxH6a6Afe (5.00): CITING for instruction tuning; similar "promising framework with presentation issues" profile.
- M4fhjfGAsZ (5.33): KCQRL for knowledge tracing; solid empirical work with cleaner presentation than PELICAN.

PELICAN has genuine contributions (well-motivated framework, real human evaluation, diagnostic improvements) that place it above the 2.33–4.0 range. However, the unsubstantiated abstract claims and the unexplained main-vs-ablation metric inconsistency are more severe than any single issue in the 5.0+ anchors. The paper falls between these bands.

**Final score**: 5.0

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>