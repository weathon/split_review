Now I have enough information to write the consolidated review. Let me compile my analysis.

**Round 1 bracket**: After the initial calibration, I found that InnoGym sits above FEABench (4.50), BioKGBench (4.75) and RD2Bench (5.25) in the quality of its framework and task curation, but below ScienceAgentBench (6.00), MLE-Bench (8.00), and AgentBench (6.20) which have larger scale and/or more rigorous validation. Initial bracket: **4.5–5.5**.

**Round 2 narrowing**: The round-2 searches confirmed that papers in the 5–6 range that propose new evaluation frameworks with unvalidated metrics (e.g., "Hallucinating LLM Could Be Creative" at 5.00) tend to receive Reject decisions due to the gap between the claim and the evidence. InnoGym is closer to the 5.0 anchor than to the 6.0+ anchors: the novelty metric is its central contribution but is not validated in the main paper. The paper is stronger than FEABench (4.5) because the task curation pipeline is more principled and the framework is more formal. It is weaker than ScienceAgentBench (6.0) which has 102 expert-validated tasks and more thorough evaluation.

**Final score: 5.0 / Reject**.

All anchor papers:
| Paper | Score | Round | Comparison |
|---|---|---|---|
| FEABench | 4.50 | R1 | InnoGym is stronger — more principled framework, better task curation |
| RD2Bench | 5.25 | R1 | Comparable — both have targeted benchmarks with validation gaps |
| BioKGBench | 4.75 | R1 | InnoGym is stronger — broader scope, more formal framework |
| ScienceAgentBench | 6.00 | R1 | InnoGym is weaker — smaller scale, less validation of core metric |
| MLE-Bench | 8.00 | R1 | InnoGym is much weaker — less mature benchmark, unvalidated metric |
| "Hallucinating LLM..." | 5.00 | R2 | Similar — both propose creativity/novelty metrics without adequate validation |
| AgentBench | 6.20 | R2 | InnoGym is weaker — smaller scale, fewer environments tested |
| VisualAgentBench | 5.75 | R2 | InnoGym is weaker — less comprehensive evaluation |
| AutoAdvExBench | 6.17 | R2 | InnoGym is weaker — less rigorous task construction |
| DataSciBench | 3.20 | R1 | InnoGym is much stronger — better formal framework |

Now I'll write the final review.## Summary

InnoGym proposes a framework and benchmark for evaluating AI agents on two dimensions: performance gain (improvement over best-known solutions) and novelty (methodological dissimilarity from prior work). It curates 18 "Improvable Tasks" from real-world engineering and scientific competitions through a rigorous multi-stage filtering pipeline (197→72→18), provides a unified execution environment (iGym), and evaluates three agent frameworks on 10 tasks. The central finding is that current agents achieve moderate novelty but uniformly negative performance gains, revealing a gap between creative idea generation and robust execution.

## Strengths

- **Principled two-dimensional innovation framework.** The formalization of tasks as quadruples \((P, S, V, D)\) and the complementary metrics \(G(s)\) and \(N(s)\) (Equations 2–3) provide a clear, extensible language for evaluating innovation beyond correctness. This is a genuine conceptual contribution over existing single-axis benchmarks.

- **Rigorous task curation pipeline.** The two-stage filtering (resource availability → evaluator quality & domain balance) with explicit criteria for executable evaluators, leaderboard consistency verification (Pearson ≥ 0.9, Kendall-τ ≥ 0.8), and solution collection is described in sufficient detail to be reproducible (Section 3.1–3.2). The transparency about which tasks failed which stage is a methodological strength.

- **Empirical evidence for the novelty–robustness gap.** Table 2 concretely shows that across all 10 tasks, every tested agent achieves negative performance gains (e.g., MLAB average gain −24.32, CODEACT −41.58, AIDE −42.68) while simultaneously achieving moderate novelty scores (averages 56.55, 54.86, 46.67). The specific cases where high novelty coincides with severely negative gains (e.g., CODEACT on RCIC: novelty 83.33, gain −99.67) directly support the paper's central claim that novelty without robustness is insufficient.

- **Controlled analytical experiments on Circle Packing.** The temporal dynamics analysis (Figure 6a), foundation model ablation (Figure 6b), and temperature sweep (Figure 6c) provide interpretable demonstrations that the metrics behave sensibly (performance improves with time, stronger models score higher, novelty increases with temperature). The identified "sweet spot" at temperature 0.5–0.75 is a concrete, actionable finding.

## Weaknesses

### Fatal

None.

### Major

1. **The novelty metric is not validated, and the paper's core claims depend on it.** The novelty score \(N(s)\) is computed via an LLM-as-judge pipeline (Codex extraction → GPT-5 scoring on six rubric dimensions) with no validation presented in the main paper. The paper states "We provide a more detailed analysis of the behavior and reliability of \(D\) in Appx. F" (Section 4.1) but the main text contains zero summary of any such analysis — no human correlation, no inter-rater agreement, no sensitivity analysis to prompt changes or judge model, no calibration against baselines. The abstract claims "some agents produce novel approaches" and Section 4.2 argues that "the primary bottleneck for agents on complex tasks is not a deficit of novel ideas" — both conclusions presuppose that the novelty scores actually measure methodological novelty. Without at least a summary of validation evidence in the main paper, the benchmark's central contribution (two-dimensional innovation evaluation) rests on an ungrounded metric. This is not a trivial omission for a paper whose primary innovation *is* this metric.

2. **The evaluated scale is small relative to the claims.** Of the 18 curated tasks, only 10 are evaluated (Section 4.1), and of those, many entries are "/" (all three runs failed to produce a valid submission — 6 of 30 cells in Table 2). The main comparison involves only 3 agent frameworks (MLAB, CODEACT, AIDE) with one backbone model (DeepSeek-v3.1). Variation in novelty across frameworks is modest (56.55 vs. 54.86 vs. 46.67), and given the unvalidated metric, these differences are uninterpretable. The controlled experiments (Figures 5–6) are confined to a single task (Circle Packing). While the paper is transparent about these constraints, the scope of evidence is thin for the breadth of claims about "innovation potential."

### Minor

3. **The min-distance formulation of novelty has known limitations that are not discussed.** Equation (3) defines \(N(s) = C(s) \cdot \min_{h \in S_{\text{known}}} D(s, h)\). If \(S_{\text{known}}\) is large and diverse, a genuinely novel solution may resemble one particular prior solution closely, yielding low novelty. Conversely, a trivially different solution that happens to be unlike any single known solution could score high. The paper does not acknowledge this limitation or discuss alternatives (e.g., average distance to K nearest neighbors). The rubric dimensions for \(D\) could mitigate this, but without validation of \(D\) (see Major point 1) the concern remains.

4. **The characterization of innovation regimes (breakthrough, performance, conceptual) lacks operational thresholds.** Section 2.2 describes these regimes (e.g., "high \(G\) and high \(N\)") but never specifies what counts as "high." Without thresholds, the taxonomy is descriptive rather than operational, and the paper does not use it to classify any of the experimental results.

5. **The analysis of the robustness–novelty gap conflates two possible explanations.** The claim that agents have "novel ideas" but cannot "translate them into correct implementations" (Section 4.2) is one interpretation. An alternative, equally consistent with the data, is that the LLM-as-judge novelty metric is capturing spurious variation (e.g., formatting differences, verbosity, coding style) that has nothing to do with genuine methodological novelty, while the uniformly negative performance gains simply reflect that the tasks are hard. The paper does not disentangle these.

### Trivial

6. Table 2 would benefit from a clearer visual separation between frameworks and from indicating that "Highest"/"Lowest" come from human leaderboards (this is stated in the text but not obvious from the table alone).
7. Figure 4 (iGym architecture) is dense and hard to parse at the printed size; a simplified schematic focusing on the key differences from existing SDKs would be more informative.

## Nice-to-Haves

- A human evaluation study correlating LLM-as-judge novelty scores with domain-expert ratings, even on a small subset of solution pairs, would transform the paper's core contribution from a promising proposal into a validated measurement.
- Sensitivity analysis of \(N(s)\) to the choice of judge model (e.g., comparing GPT-5 against GPT-4o, Claude, or open-weight models) would clarify how robust the metric is.
- Reporting variance across the three runs (not just the best score) would help readers assess the stability of the results.
- Including an ablation where \(S_{\text{known}}\) is expanded or contracted would clarify whether the min-distance measure is sensitive to the completeness of the reference set.

## Removed Points

These points are flagged for removal; treat them with caution.

- *Strength: "Novelty evaluation via Agent-as-judge"* — This was listed as a strength by the Strength Finder, but it conflicts with the verified weakness that the metric is not validated. Having a concrete procedure is not the same as having a valid one. Removed per the rule that when a strength and weakness disagree, the weakness wins.
- *Weakness about missing reproducibility details for Codex/GPT-5* — The harsh critic raised concern about proprietary model deprecation. This is a generic concern applicable to nearly every paper using proprietary APIs and does not specifically harm the paper's claims. Moved here.
- *Weakness about temporal dynamics generalizability* (harsh critic's point that Circle Packing findings might not generalize) — The paper explicitly scopes this as "controlled experiments on the challenging Circle Packing problem" (Section 4.3), so the criticism is scope creep. Moved here.
- *Weakness about S_known completeness affecting scores* — The paper describes its solution collection pipeline (Section 3.2) and the harsh critic's concern about incomplete S_known inflating novelty is speculative without evidence that the collected S_known is incomplete. Moved here.

## Novel Insights

None beyond the paper's own contributions. The review process surfaces one notable framing: the paper's core empirical finding (negative gains + moderate novelty) is simultaneously its strongest evidence and the observation most vulnerable to the unvalidated-metric problem. If the novelty scores are measuring something other than genuine methodological novelty, the central conclusion about a "novelty–robustness gap" collapses into the simpler observation that agents fail at hard tasks. This tension does not originate from the reviewers but is inherent in the paper's design.

## Suggestions

1. **Validate the novelty metric in the main paper.** Add a compact table or figure showing: (a) correlation (Spearman/Kendall) between LLM-as-judge novelty scores and human expert ratings on 20–30 solution pairs, drawn from at least 3 tasks; (b) agreement statistics (e.g., Krippendorff's alpha) across multiple judge models; (c) 2–3 concrete examples of high-scoring and low-scoring solution pairs with expert commentary. This single change would address the paper's most critical weakness.

2. **Acknowledge the min-distance limitation** and either justify the choice with evidence or compare against an alternative aggregation (e.g., mean distance to K=3 nearest neighbors) on a representative subset.

3. **Expand the evaluation scope** even modestly — adding one more backbone model (e.g., GPT-5, Gemini-2.5-Pro) across all 10 tasks would substantially strengthen the claims about framework differentiation.

## Score and Decision

**Bracketing (Round 1):** Three queries on "benchmark for evaluating AI agents on scientific problems innovation" with anchors at <3.5 (n=5, mean scores 2.00–3.20), 3.5–7.5 (n=5, mean scores 4.00–7.00), and >7.5 (n=5, mean scores 8.00–8.67). The paper clearly sits above the weak band (tasks are well-curated, framework is coherent) and below the strong band (scale and validation are insufficient). Initial bracket: **4.5–5.5**.

**Narrowing (Round 2):** Two targeted queries on "benchmark novelty metric LLM evaluation two dimensions" and "benchmark LLM agent evaluation scientific tasks novel methodology" within (3.5, 6.5) and (4.0, 6.5). Anchors included ScienceAgentBench (6.00, Accept), AgentBench (6.20, Accept), "Hallucinating LLM Could Be Creative" (5.00, Reject), and FEABench (4.50, Reject). The paper is clearly stronger than FEABench (better framework, more rigorous curation) and comparable to "Hallucinating LLM" (both propose unvalidated novelty/creativity metrics). It is weaker than ScienceAgentBench (which has 102 expert-validated tasks and more thorough evaluation). Final bracket: **4.75–5.25**.

**Final score: 5.0** — placed relative to the round-2 anchors, closest to "Hallucinating LLM Could Be Creative" (5.00) which shares the same structural gap (claims about creativity/novelty without metric validation). The paper's task curation is stronger than that anchor, but the centrality of the unvalidated metric to the paper's claims makes the comparison apt.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>