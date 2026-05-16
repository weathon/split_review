Now I have all the information needed. Let me produce the consolidated final review.

## Summary

This paper studies post-deployment deterioration (PDD) monitoring of ML models when deployment labels are unavailable. It formalizes disagreement-based PDD (D-PDD), proposes the D-PDDM algorithm with provable false positive rate (FPR) and true positive rate (TPR) guarantees, and validates empirically on synthetic data, CIFAR-10.1, and the GEMINI healthcare dataset. The algorithm operates in two stages: pre-training compresses training data into a hypothesis subset H_p and a disagreement distribution Φ; deployment monitors disagreement without requiring training data.

## Strengths

- **Formal equivalence between PDD and D-PDD under explicit assumptions.** Lemma 2.1 shows that under identical labeling functions and bounded TV-distance between marginals, PDD and D-PDD are equivalent with high probability (1 − 2ε_f − κ). This provides a principled foundation for using disagreement as a proxy for performance deterioration, going beyond prior heuristic uses.

- **Provable guarantees for both FPR and TPR.** Theorem 4.2 bounds the FPR under non-deteriorating shifts at significance level α by α plus an exponentially decaying term in training sample size, independent of deployment sample size. Theorem 4.4 gives a lower bound on TPR under deteriorating shifts with sample complexity scaling inversely with the degree of deterioration ξ. These are the first such guarantees for unsupervised deployment monitoring without training data.

- **Training-data-free monitoring via a decoupled pre-training/deployment protocol.** The algorithm compresses information from training data into H_p and Φ during pre-training, so deployment requires only f, H_p, and Φ — not the original training data. This addresses privacy and scalability desiderata not satisfied by listed baselines in Table 1.

- **Clear characterization of failure regimes with mitigation strategies.** Theorem 4.5 identifies Regime 2 (ε_q ≤ ε_p despite deterioration), and Section 4.3.1 illustrates how lowering ε_f (better-trained base classifier) can recover to a solvable regime, offering actionable guidance for practitioners.

- **Sample complexity bounds depending on VC dimension of the restricted class H_p (d_p) rather than the full class H.** Theorem 4.4 shows required deployment sample size m scales with d_p, which can be much smaller than d when f is well-trained. This explains the method's effectiveness in few-shot settings (e.g., 50–200 samples on CIFAR-10.1).

## Weaknesses

### Fatal
None.

### Major

- **Gap between theoretical formulation of H_p and practical implementation is not analyzed.** The theory (Def. 2, Theorems 4.2–4.5) assumes the set H_p = {h ∈ H: err(h; P_g) ≤ ε_f} is constructed exactly. Algorithm 1 is described as if this set can be directly formulated, and the paper's practical consideration mentions Bayesian posterior sampling as an approximation. For neural networks (even small ones), exact construction of H_p is intractable. The paper provides **no analysis** of how this approximation affects the composition of H_p (e.g., whether sampled hypotheses satisfy the error constraint) or how it impacts the FPR/TPR guarantees. The theorems' VC-dimension bounds apply to the exact H_p; under an approximate sampling scheme those bounds are not directly operational. This does not invalidate the theoretical contribution (the idealized guarantees are still correct), but it creates a significant disconnect between the theory and the empirical validation, weakening the claim of "provable monitoring in experiments."

- **CIFAR-10.1 experiments do not report ε_f (in-distribution error of the deployed classifier f), making regime analysis opaque.** The theory's guarantees depend critically on ε_f being small (Def. 2, Theorem 4.4–4.5). The paper uses neural networks with ~32 hidden nodes — a very small architecture for 32×32 color images — but never reports the in-distribution error of f on CIFAR-10. Without this number, the reader cannot determine whether the experiment falls in Regime 1 (where D-PDDM should succeed) or Regime 2 (where it may fail by Theorem 4.5). The TPR results in Table 2 are thus difficult to interpret as supporting the theory; they show relative competitiveness against baselines but leave the regime unspecified. The paper does report ε_f = 0.1 for the synthetic experiment (line 243), so the omission on CIFAR-10 is a gap the authors could easily fill.

### Minor

- **Lemma 2.1 slack parameters (ε_f, κ) are not quantified in experiments.** The equivalence between PDD and D-PDD holds with probability 1 − 2ε_f − κ. These parameters are never estimated or reported for the real datasets, so the reader cannot assess how tight the monitoring is. Estimating TV(P_x, Q_x) and reporting ε_f would give practitioners a principled sense of when to trust the method.

- **GEMINI temporal shift characterization as "non-deteriorating" is based on visual inspection of error trends rather than a direct check of ξ = 0.** The paper states (line 250): "we observe that there is little to no apparent trend in performance degradation across time, thus it could be understood that this temporal data shift is non-deteriorating." This is a reasonable interpretation given the data, and the key result (D-PDDM has low FPR while baselines flag everything) is consistent with this interpretation. However, without a ground-truth verification or a synthetic control where ξ is known exactly, the characterization relies on visual judgment. The claim that D-PDDM "achieves low false positive rates" on this data is supported by the monitoring results in Figure 5(b), but the strength of the support would be improved by a more principled characterization of the shift.

- **Algorithm 2's hypothesis testing procedure is described only in prose.** The paper says "D-PDD happens when dis_Q lies in the top α of Φ" but does not formally state the empirical quantile comparison procedure (e.g., compute the empirical 1−α percentile from Φ and compare dis_Q against it). Stating the exact decision rule would improve reproducibility.

- **The O(·) notation in sample complexity bounds suppresses constants**, making it hard to sanity-check against the experimental sample sizes. For instance, the paper uses m = 4,000 in synthetic experiments and 50–200 in CIFAR-10.1 shots, but without knowing the constants behind O(·) and the VC dimension d_p, the reader cannot assess whether m satisfies the theoretical requirements.

### Trivial
None.

## Nice-to-Haves

- **Comparison with Podkopaev & Ramdas (2021).** The paper discusses this work in Related Work and correctly notes it requires delayed labels (a different setting). A comparison on synthetic data where labels are available after monitoring would contextualize D-PDDM against a method designed for the related sequential setting, but its absence is not a weakness given the different assumptions.

- **Runtime and memory measurements.** A short table reporting pre-training time, monitoring time per sample, and storage requirements for H_p and Φ would help practitioners evaluate feasibility.

- **Explicit constants in sample complexity bounds** (even if loose) for a simplified setting, enabling sanity checks against experimental sample sizes.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that Proposition 4.1 derivation is missing because it "refers to an appendix that was stripped."** The hard rules instruct that complaints about missing appendix content should be removed — the parser strips appendices from all papers, and the derivation exists in the original submission.

- **Criticism about Theorem 4.5 (TPR = O(α) in Regime 2) as if the paper obscures this limitation.** The paper explicitly acknowledges this limitation in Section 4.3.1 ("Solutions for FNR/FPR tradeoff") and discusses how lowering ε_f can mitigate it. The reviewer correctly notes the limitation but it is already addressed by the paper's own analysis.

- **Criticism about the synthetic experiment not verifying ξ = 0 for the non-deteriorating shift.** The paper designs the shift by stretching features away from the decision boundary, which by construction does not increase f's error. The reviewer acknowledges this shift "indeed does not increase the error of f." The claim that "it is plausible that some auxiliary h could disagree more on the stretched distribution" is speculative and not supported by evidence that the experimental results are misleading.

- **Strength Finder strength about "sample complexity bounds that depend on the VC dimension of the restricted class"** — This is kept in Strengths as it is substantive, not removed.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight about the paper that the authors did not already articulate.

## Suggestions

1. **Report ε_f for the CIFAR-10 experiments** and state which regime (Regime 1 vs. Regime 2) the experiment falls into. This is essential for connecting the empirical results to the theoretical guarantees.
2. **Discuss the theory-practice gap more explicitly** — acknowledge that the practical construction of H_p requires approximation for neural network classes, and provide (even informal) reasoning about why the guarantees are expected to approximately hold under the approximation. If possible, bound the error introduced by the approximation.
3. **Quantify ε_f and κ for the real datasets**, or at least provide bounds, to help readers assess the slack in Lemma 2.1's equivalence probability.
4. **State the empirical decision rule of Algorithm 2 formally** (e.g., "reject if dis_Q exceeds the ⌈(1−α)·|Φ|⌉-th order statistic of Φ").
5. **For the GEMINI temporal experiment**, either provide a more rigorous justification for the non-deteriorating classification (e.g., a statistical test that err(f; Q_g') does not significantly exceed err(f; P_g)) or add a synthetic control experiment with known ξ to validate the low-FPR claim under a verifiable non-deteriorating shift.

## Score and Decision

The paper makes a genuine theoretical contribution — formalizing deterioration monitoring via disagreement with provable FPR/TPR guarantees in the unsupervised setting — and the decoupled pre-training/deployment protocol is a practical advance. The GEMINI experiments provide real-world validation. However, the gap between the theoretical algorithm (exact H_p) and practical approximation is not analyzed, and the CIFAR-10 experiments do not report ε_f, making it impossible to verify which regime the experiments operate in. These issues are addressable in revision and do not undermine the core theoretical contribution, but they limit the strength of the empirical support.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>