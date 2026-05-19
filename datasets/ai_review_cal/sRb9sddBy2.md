- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5
Now I have all the information needed to write the final review. Let me compose it.

## Summary

This paper introduces the concept of *distributionally diverse (DD) risk* — the worst-case expected loss over all test distributions with entropy above a threshold — as a framework for out-of-distribution generalization. The authors prove three main theoretical results: (1) training on a uniform distribution minimizes DD risk in a worst-case sense over classifiers with the same expected risk (Theorem 1), and a non-vacuous bound connects uniform expected risk to DD risk (Theorem 2); (2) a PAC-Bayesian bound shows that gentle finetuning (staying close to a pretrained model's weights) controls DD risk (Theorem 3); (3) a Wasserstein-based generalization bound captures the trade-offs in rebalancing training data toward uniformity (Theorem 4). Experiments on synthetic data and three real-world benchmarks (iWildCam, PovertyMap, ColoredMNIST) provide partial empirical support.

## Strengths

- **Theorem 1 (uniform is optimal) is a genuine theoretical contribution.** The result — that among all training distributions achieving fixed expected risk ε, the uniform distribution minimizes the worst-case DD risk over the set of classifiers — is non-trivial and conceptually elegant. The paper correctly notes key caveats (inductive bias, finite-sample generalization, availability of test information), preventing the claim from being overstated in context.

- **Theorem 2 gives a non-vacuous bound connecting uniform expected risk to DD risk.** The bound has two regimes (additive for small γ, inverse-log for small expected risk) and is empirically non-vacuous in Figure 1, where the empirical DD risk lies below the theoretical bound across training set sizes and entropy gaps. This is a genuinely useful theoretical tool.

- **Theorem 4 (rebalancing bound) provides a principled trade-off analysis.** The Wasserstein-based bound jointly captures estimation error, rebalancing mismatch (ℓ₁ distance to uniform), and classifier complexity (Lipschitz constant), formally justifying why reweighting toward uniformity can help but also may hurt when the weight function has high complexity. This is a clean theoretical contribution.

- **The controlled synthetic experiments are well-designed and directly validate the theory.** Figures 1–3 systematically vary training uniformity and dataset size, showing that DD risk decreases with more uniform sampling and that rebalancing measurably reduces both uniform expected risk and DD risk. The experimental setup is carefully disclosed (e.g., greedy approximation of DD risk, 35 task repeats).

- **The paper openly discusses its failure modes.** Section 5.3 candidly acknowledges that density estimation can be brittle, that some datasets resist improvement, and that the framework assumes covariate shift within the same domain. This candor strengthens the credibility of the positive results.

## Weaknesses

### Fatal
None.

### Major

- **The gentle finetuning theory (Section 4.2 / Theorem 3) lacks credible empirical validation.** The only empirical test is on ColoredMNIST (Table 3), where the standalone WDL2 model selection improves the -90% group from 10.0% to 11.0% — a 1% absolute gain. The more dramatic result (37.0%) combines WDL2 with rebalancing, UMAP-8 dimensionality reduction, and label conditioning, making it impossible to attribute the improvement to the gentle finetuning theory alone. The PAC-Bayesian bound itself is not directly evaluated (e.g., by computing δ(π_Z,π) or the KL divergence). The authors acknowledge that "it is impractical to estimate the ℓ₁ distance" (line 167), which further severs the link between theory and experiment. As presented, the gentle finetuning section is a theoretical suggestion with no standalone empirical support.

- **The claim that "rebalancing consistently improves performance in scenarios with significant covariate shift" (line 208) is contradicted by the paper's own data on PovertyMap.** On the PovertyMap test OOD split (Table 2), rebalancing achieves a Pearson correlation of 0.75 vs. ERM's 0.78 (overall) and 0.44 vs. 0.45 (worst-group) — i.e., rebalancing *hurts* performance relative to the ERM baseline. The best variant (Rebalancing + UMAP-64) ties ERM on overall (0.78) but this is not an improvement. While the paper later explains (line 285) that the PovertyMap OOD set has domain shift beyond covariate shift, this conflicts with the "consistently improves" framing. The paper would be stronger if the empirical summary matched the nuanced results.

- **The headline ColoredMNIST result (37.0% ± 10.7 on the -90% group) has very high variance that raises reliability concerns.** The standard deviation of 10.7 on a mean of 37.0 (across what appears to be 3 replicates, though the number is not stated in the caption) means individual runs could span a 20+ percentage point range. All standard baselines cluster tightly around 10% with standard deviations ≤ 0.3. The paper should provide per-seed numbers and explain why this particular configuration (WDL2 + rebalancing + UMAP-8 + label conditioning) produces both the large improvement and the high variance.

### Minor

- **The textual framing of Theorem 1 slightly overstates what is proven.** The theorem statement (line 82) reads: "A classifier optimized for the uniform distribution will yield the smallest DD risk." What is actually proven is that the *worst-case* DD risk over the set of classifiers achieving ε on uniform is no larger than the worst-case DD risk over the set achieving ε on any other p. These are subtly different: a realistically trained classifier may not be the worst in its set, and the best classifier on a non-uniform p could have lower DD risk than any classifier trained on uniform (since uniform may be harder to learn). The paper does discuss caveats (lines 93-95), and the mismatch is not large, but the central claim as phrased in the abstract and introduction could mislead casual readers.

- **The curse of dimensionality for DD risk, while acknowledged (line 120), is a significant practical limitation that deserves more prominence.** The bound requires γ = O(1) for non-vacuous guarantees, meaning the test distribution must be close to uniform in high dimensions. Since most real-world data lives on low-dimensional manifolds in high-dimensional spaces, this constraint is non-trivial and limits the framework's applicability to settings where the domain of interest is genuinely low-dimensional or where entropy constraints are realistic.

- **The practical weighting schemes recommended (w(x) = min{1/p(x), β} and w(x) = p(x)^τ) are intuitions motivated by, but not directly derived from, Theorem 4.** The paper is transparent about this, but the link between theory and practice in Section 4.3 remains heuristic rather than deductive.

### Trivial
None that survived filtering (see Removed Points).

## Nice-to-Haves

- A direct evaluation of the PAC-Bayesian bound on a small-scale model (e.g., linear probe or small MLP) where the ℓ₁ distance between posterior and prior can be computed or bounded via KL. This would substantially strengthen the gentle finetuning story.
- An ablation of the different terms in the rebalancing bound (effect of β, effect of Lipschitz constant, correlation between density estimation accuracy and OOD improvement) to tighten the theory-practice connection.
- A discussion of when the entropy-based DD risk is the right objective vs. scenarios requiring different formalizations (concept shift, systematic domain shift).

## Removed Points

These points from the original reviews are removed per the filtering criteria (treated as parser artifacts, speculative claims, or scope creep). Treat them with caution if revisiting:

1. **Citation mangling ("1214/17-AAP1326" on line 178) and typos ("syntetic", "miss-classifier", double "risk risk")** — Removed as PDF-parser artifacts per Hard Rules. The original submission does not have these issues.
2. **Speculation about data leakage or overfitting to the validation set through the density estimator on ColoredMNIST** — Removed as speculative; not verifiable from the paper as written. The core observation (high σ = 10.7) is retained above.
3. **"Missing related works"** — Removed per Hard Rules (no external sources to confirm what is missing).
4. **The harsh critic's area-of-concern framing about confounders not being controlled** — This was a general sweep rather than a specific, anchored problem; not retained.
5. **Softened criticisms about not testing on additional datasets for gentle finetuning** — Moved to Nice-to-Haves; the core issue (essentially no standalone validation) is the real weakness.
6. **Strength Finder's claim that Table 3 "validates" the gentle finetuning bound via WDL2** — Partially removed because the 1% gain (10.0% → 11.0%) is too small to constitute strong validation; the theory is kept as a strength but the strength is noted as having limited empirical support.

## Novel Insights
None beyond the paper's own contributions. The reviewers did not surface an observation about the work that the paper itself does not already articulate or imply.

## Suggestions

1. **Reframe the Theorem 1 claim.** Change "A classifier optimized for the uniform distribution will yield the smallest DD risk" to something closer to "Among all classifiers that achieve the same expected risk ε on their training distribution, the worst-case DD risk is minimized when the training distribution is uniform." This aligns the textual claim with the mathematics.

2. **Either substantially expand the gentle finetuning experiments or explicitly re-scope it as a theoretical suggestion without empirical validation.** Adding even a small-scale experiment (e.g., verifying the PAC-Bayes bound on a tractable model) would greatly strengthen this section.

3. **Provide per-seed results for the ColoredMNIST 37.0% ± 10.7 result** and discuss why this particular configuration exhibits such high variance. This would address legitimate reader skepticism about reliability.

4. **Tone down the "consistently improves" claim in the experimental summary (line 208).** Replace it with a statement that acknowledges both the positive results (iWildCam, some ColoredMNIST configurations) and the negative/mixed result (PovertyMap), which the paper already does later in the text.

5. **Add the number of replicates to the ColoredMNIST table caption** for consistency with the other tables.
