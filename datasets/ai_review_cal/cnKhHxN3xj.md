- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8
Now I have a thorough understanding of the paper. Let me compose the consolidated review.

## Summary

This paper investigates the relationship between the shape of individual neurons' output distributions — quantified by the 1-Wasserstein distance to a Gaussian — and their behavior under weight sparsity in LLMs. The authors identify a small set of "Wasserstein neurons" with highly non-Gaussian outputs, show they are disproportionately sensitive to SparseGPT pruning (Figure 3), and introduce Sparse Expansion, an input-clustering + per-cluster pruning framework that recovers much of the lost performance, especially for these neurons. The key empirical finding is that Wasserstein distance predicts a neuron's sensitivity to sparsification and its improvement from input-conditional pruning, beyond what other simple metrics (mean, variance, weight magnitude) capture.

## Strengths

1. **Novel metric with predictive power for sparsity.** The 1-Wasserstein distance between a neuron's normalized output distribution and a standard Gaussian (Equation 1) is a simple, interpretable, and computationally efficient measure. The paper demonstrates that this metric is not merely descriptive but *predictive*: it correlates with sensitivity to SparseGPT pruning (Figure 3), and it is the best predictor of improvement from Sparse Expansion among several tested metrics (mean, variance, GMM components; Figure 7, R² > 0.16 vs. < 0.001).

2. **Striking empirical identification of Wasserstein neurons.** The finding that the top 3% of neurons by WD in Llama 3 8B cause a collapse in perplexity and reasoning benchmarks when pruned, far more than the same fraction selected by output variance, mean, or weight magnitude (Figure 3), is novel and compelling. This is the first work to tie individual-neuron distribution shape to sparsity resilience and the result is demonstrated across multiple benchmarks (GSM8K, BBH, SQuAD, TriviaQA, MMLU).

3. **Sparse Expansion as an analysis tool.** The framework (Section 3.1, Figure 4) — clustering inputs via PCA+K-means and running SparseGPT independently per cluster without retraining — is a clean experimental design that generates mechanistic insight. The observation that 98% of Wasserstein neurons reduce their weighted WD by a median of 42% after expansion (Figure 5b), and that expert specialization is visible (Figure 1f), provides direct evidence linking distribution shape to the benefits of input-conditional computation.

4. **Empirical connection to theoretical superposition bounds.** The paper makes a reasonable attempt to connect its findings to theoretical work on bounds of neural computation under superposition (Hänni et al., 2024; Adler & Shavit, 2024). The observation of a log-log trend between effective feature count and sparse reconstruction error (Figure 8) is a useful empirical bridge, even if the "bound" claim is qualitative.

5. **Thorough model coverage for performance comparisons.** Sparse Expansion is evaluated across the Pythia family (70M–12B) and Llama 2 family, consistently outperforming baselines (Figure 9), and the analysis covers three model families (Pythia 1.4B, Llama 2 7B, Llama 3 8B) for the core phenomena.

## Weaknesses

### Fatal
None.

### Major

1. **Central interpretive claim ("entanglement"/"disentanglement") outruns the evidence.** The paper proposes MD (Mapping Difficulty, Equation 2) as a definition of entanglement, validates WD against MD (Figure 2e), and then uses strong claims about "disentangling" the input-output relationship (abstract, conclusion). However, MD itself is a novel, unvalidated construct — there is no external anchor to established polysemanticity measures (e.g., sparse autoencoder feature counts, toy models with known feature superposition). The paper's interpretive chain (MD → entanglement → WD measures entanglement) is internally consistent but **self-referential**: entanglement is defined in terms of a specific mathematical property, and then WD is shown to correlate with that same property. By the paper's own framing, a neuron is "entangled" because it has high WD, and WD is said to measure entanglement. This does not invalidate the empirical findings (WD predicts sparsity sensitivity regardless of what it is called), but the paper's title, abstract, and conclusion make claims about entanglement that the experimental design does not independently ground. The empirical contribution would be clearer and stronger if the entanglement/disentanglement framing were replaced with more neutral, operational language (e.g., "distribution shape complexity" or "non-Gaussianity as a predictor of sparsity difficulty").

2. **Sparse Expansion's "disentanglement" mechanism lacks a critical control.** The paper claims that Sparse Expansion "disentangles" the input-output relationship, but the observed improvements could be explained by a simpler mechanism: each expert sees a narrower input distribution, making Hessian-based pruning (SparseGPT) more accurate regardless of any "disentanglement" of features. The paper shows specialization (Figure 1f) and that Wasserstein neurons benefit more, but does **not** include a control experiment (e.g., clustering inputs randomly or by a non-content criterion) to demonstrate that the benefit is specific to content-based input grouping. Without this control, attributing the improvement to "disentanglement" rather than to the narrower input distribution per expert is an overinterpretation.

3. **Confound in the Figure 3 ablation experiment.** The paper acknowledges (line 80) that Wasserstein neurons have lower mean weight magnitudes and "are actually sparsified more by SparseGPT during unstructured sparsity" (Figure A4b). This means that when SparseGPT is applied to the selected neuron rows, Wasserstein neuron rows have a higher fraction of their weights zeroed than random neuron rows. The comparison of "3% Wasserstein neurons" vs. "3% random neurons" therefore conflates neuron identity with effective sparsity level. The paper partially addresses this by also comparing to high-magnitude and high-variance neurons, which helps. But without controlling for the actual sparsity fraction achieved on each neuron set (or equivalently, without showing the degradation persists when sparsity fractions are equalized), the conclusion that Wasserstein neurons are "inherently" more important under sparsity is on weaker ground than claimed.

### Minor

1. **Key analyses are from a single layer of a single model.** Figures 5b and 5c (weighted WD/MD decrease after expansion, reported as percentages: 98% of neurons, 42% median decrease) are collected from "the up projection matrix in the second FFN of Pythia 1.4B." Similarly, Figure 7 (WD best explains improvement) uses the same single layer. While the paper shows other results across models (Figures 3, 5a, 9), these specific mechanistic claims rely on a narrow empirical base that should be broadened for confidence.

2. **The "linear frontier" bounds in Figure 8 are qualitatively described without statistical rigor.** The paper states "there is a linear front that emerges in log-log scale" (Section 3.5) but reports no regression fit, confidence intervals, or goodness-of-fit measures for these frontiers. Given the scatter in the data, the claim that these represent "bounds of both loss and improvement of sparse computation under entanglement" is weaker than the language suggests.

3. **The Figure 3 ablation protocol is underspecified.** The paper says neurons "are sparsified via SparseGPT" but does not clarify the exact mechanism: is SparseGPT applied to the entire weight matrix and then only the rows corresponding to selected neurons are zeroed? Or is SparseGPT applied only to the selected rows? The distinction matters for interpreting whether the result reflects SparseGPT's algorithmic properties or neuron-level importance. This should be explicitly stated.

4. **Choice of 16 clusters is not justified in the main text.** The paper uses 16 clusters throughout but only mentions tuning this in an appendix reference (Figure A3). A brief justification in the main text (or a sensitivity analysis showing the main results are robust to cluster count) would strengthen the presentation.

5. **Resource overhead of Sparse Expansion acknowledged but not quantified.** The paper says the method "is likely not practically implementable" (Section 3.6) but does not report the concrete memory overhead (total nonzero parameters across experts plus routing matrices) or inference latency compared to SparseGPT in the main text. This information is important for a complete assessment of the method's practical significance.

### Trivial

- The MD normalization choices (max for input differences, median for output differences) are stated but not motivated. Clarifying the design rationale would improve reproducibility.

## Nice-to-Haves

- A random-clustering control for Sparse Expansion to directly test whether content-based grouping is necessary for the observed improvements.
- Reporting error bars or repeat-run variance for key results (e.g., perplexity curves in Figure 3, correlations in Figure 7).
- A brief analysis of how the Wasserstein distance relates to established polysemanticity measures from the sparse autoencoder literature (e.g., does high WD correlate with higher feature counts?).

## Removed Points

- **"Circular reasoning" accusation (Harsh Critic #1):** The paper is internally consistent: it defines entanglement operationally via MD, and validates WD against MD. The criticism conflates "self-referential validation" with actual circularity. The real issue (lack of external grounding) is retained as Major #1.
- **"Scale is discarded" criticism:** The paper explicitly justifies normalizing to unit variance to focus on distribution shape. This is a deliberate design choice, not a flaw.
- **"GMM baseline is a strange choice" criticism:** The GMM comparison is a sensible baseline — it measures distribution complexity, just like WD does. The negative result (R² < 0.001) is informative and strengthens rather than weakens the paper.
- **"No connection to input-conditional pruning prior work":** Removed per instructions (do not mention missing related works).
- **"Drop MD metric entirely" suggestion:** This is editorial advice, not a weakness of the paper as submitted.
- **Pure formatting/style nitpicks and speculative concerns about missing appendix content:** Removed per instructions.
- **Generic "evaluation lacks rigor" / "claims may not hold" statements** without specific concrete anchor in the paper text: Removed.

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface a genuinely novel observation about the paper that the authors themselves have not already made. The harsh critic's suggestion that the paper should be reframed around the predictive power of WD rather than entanglement is a valid presentational insight but not a discovery about the paper's content.

## Suggestions

1. **Reframe the contribution around the predictive power of Wasserstein distance for sparsity.** The paper's strongest and most novel finding is that neuron-level WD to Gaussian predicts sparsification difficulty and improvement from input-conditional pruning. Trading the entanglement/disentanglement narrative for more neutral, operational language would make the paper stronger and less open to criticism.

2. **Add a random-clustering control for Sparse Expansion** to directly test whether the benefits are specific to content-based input grouping.

3. **Clarify the Figure 3 protocol** (how exactly SparseGPT is applied to 3% of neurons), and **report the effective sparsity fractions** achieved for each neuron selection criterion to address the confound.

4. **Broaden the single-layer analyses** (Figures 5b,c, 7) to at least 2–3 layers and 2 models to increase confidence in the mechanistic claims.

5. **Quantify the resource overhead** of Sparse Expansion in the main text and tone down claims about it being a "leading" approach given its acknowledged impracticality.

6. **Fit regressions** (or at least report confidence intervals) for the frontiers in Figure 8 to substantiate the "bound" language.
