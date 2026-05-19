- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6
Here is the final consolidated review.

---

## Summary

This paper studies why synthetic data fine-tuning succeeds or fails for long-context LLMs, using *retrieval heads* (attention heads that attend to relevant tokens in context) as a mechanistic lens. The authors construct synthetic datasets for three long-context tasks (MDQA, MuSiQue, SummHay Citation) by systematically varying concept expression and context diversity, fine-tune Llama-3-8B and Mistral-7B, and analyze the retrieval heads induced by each variant. They find that the overlap between retrieval heads learned on synthetic data and those learned on real data correlates with downstream performance, and provide causal evidence through activation masking (showing retrieval heads are necessary) and cross-model patching (showing intersection heads can improve synthetic-trained models).

---

## Strengths

1. **Systematic variation of synthetic data along two well-defined axes** (Section 3.1, Table 1). By independently controlling concept expression and context diversity across 5 variants per task, the paper goes significantly beyond prior work (e.g., xiong2024artificial) which considered only a single symbolic variant. This design enables informative comparisons even with limited data points.

2. **Causal evidence from activation masking** (Figure 4). Masking the top-10 retrieval heads causes a sharp performance drop across all three tasks on both models, while masking 10 random heads causes negligible (<0.05 F1) or no drop. This cleanly demonstrates that the identified retrieval heads are causally important for the observed downstream performance, not merely correlated artifacts.

3. **Cross-model patching reveals insufficiency of synthetic training** (Table 3). Patching intersection heads (shared between real and synthetic) from the real-data model into the synthetic-data model improves performance in most conditions (e.g., MDQA Symbolic: F1 from 0.48 → 0.73, a +0.25 gain), while patching complement or random heads gives smaller or negative gains. This goes beyond correlation to demonstrate that synthetic data activates the right heads but teaches them less effectively.

4. **Multi-task, multi-model evaluation** across three retrieval/reasoning tasks and two model families (Llama-3-8B, Mistral-7B). This scope strengthens the generality of the findings beyond a single task-model combination.

---

## Weaknesses

### Fatal

None.

### Major

1. **Correlation analysis rests on very few data points (N=5) and fails on one task without explanation.** The Spearman correlations between retrieval head recall and F1 (Table 4) are computed from only 5 synthetic variants per task. With N=5, a single outlier can flip sign or magnitude, and none of these correlations are statistically significant at standard thresholds. The paper acknowledges MDQA's near-zero correlation (ρ=0.23 for Llama3, ρ=−0.27 for Mistral) but does not analyze *why* the relationship breaks down on this task. Is MDQA (single-hop) simple enough that other mechanisms dominate? Is the retrieval head detection noisier here? Without understanding this failure case, the claimed general relationship is substantially weaker than the paper suggests.

2. **Patching results contain counterexamples that the paper's narrative glosses over.** The paper asserts "patching intersection heads outperforms patching both random and complement heads" (Section 5). However, in Table 3: (a) MDQA "High concept, Low context": random patching (0.70) beats intersection (0.51); (b) MuSiQue "High concept, High context": complement (0.33) beats intersection (0.29), and *both* decrease performance relative to the original model (0.37); (c) SummHay "High concept, High context": random (0.79) beats intersection (0.75). Intersection patching wins in ~75% of conditions, which is a meaningful trend, but the claim should be presented as a tendency, not an across-the-board result. The negative or neutral cases deserve explicit discussion to define the boundary conditions of the approach.

3. **"Strict subset" claim in Figure 1 caption is not verified.** The caption states "the synthetic data is found to induce strict subsets of the retrieval heads identified on the real data." A *strict* subset requires that every synthetic-data retrieval head is also a real-data head, with no synthetic-only heads. The paper reports counts (e.g., 112 vs. 129 heads for MuSiQue) but does not verify set containment. The abstract uses the softer phrasing "mostly subsets," which is more appropriate. This overclaim should be corrected.

4. **Training data size is not reported or controlled as a potential confound.** The paper does not specify how many training examples are used per synthetic variant or how these counts compare to the "Real Data (Limited)" baseline. The footnote in Section 2.2 suggests that example count matters (citing xiong2024artificial's different results with fewer examples), but without reporting per-variant sizes or matching them, performance differences across variants could reflect dataset size rather than data quality. This is a critical missing control for a paper whose central claim is that retrieval head overlap *explains* performance differences.

### Minor

1. **No variance estimates on main fine-tuning results** (Table 1). F1 scores are reported to two decimal places with no error bars, confidence intervals, or multiple-seed results. While single-run fine-tuning of 8B models is common practice, the reported 2–4% gaps between synthetic variants and real data could be within the noise of individual runs. Reporting at least 2–3 seeds would substantially improve confidence.

2. **The "necessary" claim is stronger than the masking evidence strictly supports.** The conclusion states retrieval heads are "necessary (but not sufficient) for a strong downstream model" (Section 6). The masking experiments (Figure 4) show that removing top-k retrieval heads degrades performance — suggesting heads are *important* — but do not prove the model *cannot* do the task without them; performance degrades gradually rather than catastrophically. A more precise characterization (e.g., "highly important") would better match the evidence.

3. **MDQA's anomalously large real-vs-synthetic gap not discussed.** Table 1 shows real-data F1 of 0.83 (Llama3) vs. best synthetic of 0.49 — a 34-point gap. For MuSiQue and SummHay, the gap is only 2–4 points. The paper acknowledges this (footnote, Section 2.2) but does not explain *why* synthetic data catastrophically underperforms on MDQA relative to the other tasks. Since MDQA is also the task where the correlation with retrieval heads breaks down, this is a missed opportunity to understand the limits of the theory.

### Trivial

- Labeling inconsistency: SummHay concept expression uses "Simplified" in Table 1 but "Low" in Table 3, creating unnecessary confusion.

---

## Nice-to-Haves

- **More synthetic variants** (e.g., 3+ levels per dimension or random sampling within each cell) would allow a statistically meaningful N for correlation analysis.
- **Multiple fine-tuning seeds** (3 per condition) would enable variance reporting and increase the effective N for correlations.
- **A dedicated analysis of the MDQA failure case** — why does retrieval head overlap not predict performance on this task? This would define boundary conditions for the theory and substantially strengthen the paper.
- **A table of dataset statistics** (number of training/eval examples, context length distribution per variant) would improve reproducibility and enable readers to assess the training-size confound.

---

## Removed Points

These points were flagged by a reviewer but are removed from the main evaluation because they are factually incorrect, nitpicks, or not verifiable from the paper:

- *Criticism that symbolic tasks are described only in a small figure caption.* They are described in Section 3.1 (paragraph "Symbolic Tasks"), lines 80–81.
- *Criticism that retrieval head identification location (synthetic vs. real eval data) is unclear.* This is explicitly addressed in Section 4.1, lines 156–157.
- *Criticism about missing related works.* I do not have external sources to verify this.
- *Formatting nitpicks (typos, spacing, garbled characters).* These are parser artifacts from PDF extraction.
- *Concerns about GPT-4o-mini / GPT-4 generator specificity.* Demanding justification for specific model choice is scope creep beyond what this paper sets out to do.
- *Reproducibility complaints about undisclosed hyperparameters or missing appendix content.* The appendix is stripped by the submission system; this is not an author error.

---

## Novel Insights

Beyond the paper's own contributions, the main insight that emerges from the review is the asymmetry between tasks where retrieval heads are predictive (MuSiQue, SummHay) and the single-hop task where they are not (MDQA). This suggests a potential **task-complexity boundary** for the theory: retrieval heads may explain synthetic-data effectiveness primarily for multi-hop or citation reasoning tasks, while single-hop retrieval may be bottlenecked by other model components (e.g., representation quality, positional encoding adaptation). Testing this hypothesis would significantly deepen the contribution.

---

## Suggestions

1. **Soften overclaims.** Replace "strict subsets" with "largely overlapping sets." Qualify the patching claim from "outperforms" to "tends to outperform." Replace "necessary" with "highly important" unless stronger evidence is provided.
2. **Report training data sizes** for each synthetic variant and the real-data baselines. If they are not matched, discuss the implications explicitly.
3. **Run at least 3 fine-tuning seeds** for the main conditions and report means ± standard deviations. This would also make the correlation analysis more robust by increasing effective N.
4. **Add a dedicated analysis of MDQA** as a contrasting case. Why does the relationship fail to hold? Analyzing this would strengthen the paper's theory by defining its scope.
5. **Address the patching counterexamples explicitly** in Section 5. Acknowledging conditions where intersection heads do *not* outperform random/complement heads — and speculating why — would make the paper more rigorous.
6. **Resolve the "Simplified" vs. "Low" labeling inconsistency** for SummHay across tables.

---
