## Summary

This paper proposes INFO-SEDD, a discrete diffusion-based method for estimating KL divergences and mutual information (MI) between high-dimensional discrete random variables. The method leverages Continuous Time Markov Chains (CTMCs) and score functions trained via the DWDSE loss to compute information-theoretic quantities without requiring continuous embeddings of discrete data. The paper introduces two variants (joint: INFO-SEDD-J and conditional: INFO-SEDD-C), provides an error bound, and validates the approach on synthetic benchmarks, text summarization model selection, and genomics motif discovery.

## Strengths

1. **Impressive synthetic benchmark results.** Table 1 shows that INFO-SEDD recovers near-exact MI values across a sweep from MI=10/D=10 through MI=50/D=50 (e.g., 39.11±0.65 vs true 40, 47.77±1.18 vs true 50), while every competing method degrades substantially at higher MI and dimensionality. The advantage is large and consistent over 10 seeds. This directly supports the core claim that the method handles high-dimensional discrete MI estimation where existing approaches fail.

2. **Practical utility demonstrated on real-world model selection.** In the SUMMEVAL text summarization experiment (Table 2), INFO-SEDD-C achieves Pearson correlation of 0.740 with the human "consistency" metric, far exceeding KL-DIME (0.214) and HD-DIME (0.331). The fact that MI correlates most strongly with consistency—a metric measuring factual entailment between summary and source—is conceptually coherent and provides evidence that INFO-SEDD estimates contain meaningful signal for downstream tasks.

3. **Clever absorbing-state design for computational efficiency.** Equation (6) shows that by choosing an absorbing transition matrix, marginal scores can be obtained from a single model trained on the joint distribution. This eliminates the need for separate models for joint and marginal distributions, which is both a practical advantage and a genuine methodological insight.

4. **Native support for variable-subset MI.** The motif discovery experiment (Section 4.3) demonstrates that a single INFO-SEDD-J model, trained once on full sequence–label pairs, can compute MI between a sliding window and the label by masking out other positions. The resulting MI profile correctly localizes the TATA-box motif. This capability is difficult to replicate with variational estimators that would require retraining for each window.

## Weaknesses

### Major

1. **The derivation from Equations (2)–(3) to Equation (4) is not shown in the main text, and the relationship between the DWDSE-trained scores and the ratio terms in the estimator is not clearly justified.**   
   The paper writes "By combining the result from Equation (3) with Equation (2)" and directly presents Equation (4), which combines forward generators $\overleftarrow{Q}_t$ with forward-time ratios $p_t(x)/p_t(\tilde{X}_t)$. The backward operator $\mathcal{B}$ in Equation (3) uses the *reverse-time* generator $\overrightarrow{Q}_t$, which involves ratios at time $T{-}t$ (Equation 1). A nontrivial algebraic conversion is required to express the KL divergence in terms of forward-time quantities. The paper does not sketch this conversion or explain how the specific function $f$ in Dynkin's formula is chosen. Similarly, the transition from Equation (4) to the practical estimator (5)—replacing $\frac{p_t(b)}{p_t(a)}$ with the DWDSE-trained score $s_\phi^p(\tilde{X}_t)_x$—is stated without clarifying whether the DWDSE loss learns the raw ratio or a quantity that also involves $\overleftarrow{Q}_t$, and how the absorbing process simplifies this mapping. These gaps make it difficult for a reader to verify the estimator's correctness without consulting the (unavailable) appendix. This undermines the self-containedness of the theoretical contribution.

2. **The consistency bound (Equation 7) is presented as a stronger theoretical guarantee than it supports.**   
   The bound contains an estimation error term $\bar{\sigma}(T) D |\chi| (1 + C_2/C_1^*)(\epsilon_p + \epsilon_q)$ and a truncation bias $(1 - \vec{p}_T(\emptyset^D))(D C_2 \log|\chi|)$. The paper claims the bias "vanishes exponentially" as $p_T(\emptyset^D)\to 1$ and calls INFO-SEDD "a consistent estimator up to this exponentially decaying bias." However: (a) the estimation error term scales with $\bar{\sigma}(T)$, which grows with $T$, creating a trade-off with the truncation bias that is not discussed; (b) the score errors $\epsilon_p,\epsilon_q$ are treated as $T$-independent, but score approximation typically degrades at larger diffusion times; (c) the constants $C_1,C_2$ depend on the data distribution in unspecified ways. The bound is useful as an error decomposition but does not establish standard statistical consistency (error → 0 as sample size → ∞). The claims should be appropriately qualified.

3. **The text summarization consistency test (Figure 1) has significant unaddressed issues.**  
   At $\rho=0$ (random pairing), MI should be approximately 0, but both INFO-SEDD variants report ~$10^2$ nats. While the paper notes that INFO-SEDD-C is "closer to zero" than INFO-SEDD-J, the non-zero baseline is not explained or justified. The "Empirical MI estimate" (grey line) is plotted alongside but its computation is never described in the main text, making it an opaque reference. The claimed ground-truth range of 256–303 nats is derived by multiplying English entropy-rate estimates from 1978 and 2016 studies by average summary length—an approximation the paper acknowledges is rough, but then uses it to conclude that INFO-SEDD is "more consistent" than alternatives. A method that reports ~100 nats when the true MI is zero needs more scrutiny before being validated against this approximate reference.

### Minor

4. **The motif discovery experiment (Section 4.3) lacks comparison to any alternative method.**  
   The experiment shows that INFO-SEDD produces an MI profile that correctly peaking near the TATA-box. But there is no quantitative comparison against a standard motif discovery tool (e.g., MEME, HOMER) or even a simple classifier-accuracy baseline. While the paper frames this as a "demonstration," the claim that this "unlocks applications" would be stronger with evidence that the MI signal provides information beyond what simpler methods already offer.

5. **The synthetic comparison's framing overstates the contrast with competitors.**  
   The paper acknowledges that variational estimators (MINE, NWJ, SMILE) are limited by the $\log(\text{batch size})$ bound at high MI, which is known from McAllester & Stratos (2020). Yet the comparison is presented as "our method outperforms alternatives" without making explicit that INFO-SEDD sidesteps a fundamental limitation that ties the competitors' hands. Including this context would make the comparison more informative and less prone to misinterpretation as a general superiority claim.

6. **Model selection correlations (Table 2) are reported without confidence intervals on a small sample (15 models).**  
   The Pearson correlations are striking (0.740 vs 0.214 for the nearest competitor), but with only 15 data points the uncertainty is large. Reporting bootstrap confidence intervals or p-values would help assess robustness.

7. **No discussion of computational cost or limitations.**  
   Training a discrete diffusion model is computationally heavier than training a simple critic network. The paper does not report training time, inference cost, or discuss settings where INFO-SEDD may not be practical (e.g., very large state spaces, very long sequences). A dedicated limitations section is absent.

### Trivial

- The derivation of Equation (6) (marginal scores from joint model) is relegated entirely to Appendix A.3; a brief sketch in the main text would improve readability.
- The "same backbone for all methods" claim in Section 4.1 is ambiguous, since INFO-SEDD uses a score model while variational methods use a critic network. The appendix presumably clarifies this, but the main text could be more precise.

## Nice-to-Haves

- Provide the derivation from Equation (3) to Equation (4) in the main text (or a clear sketch) so readers can follow the logic without consulting the appendix.
- Quantify the $\rho=0$ bias for the text summarization experiment: why do both INFO-SEDD variants and the empirical estimate report ~100 nats when MI should be zero?
- For the motif discovery experiment, compare against at least one simple baseline (e.g., classifier accuracy per window, or a standard motif discovery tool) to calibrate what value the MI signal adds.
- Report training/inference time and model size for INFO-SEDD vs. competitors.
- Add bootstrap confidence intervals to Table 2.

## Removed Points

These points were raised by the reviewers but are excluded from the main weaknesses for the following reasons:

- **"Derivation of Equation (4) relies on Appendix (not provided)"** — The paper states the derivation is in the appendix. The parser strips appendices from all papers; they exist in the original submission. This is a presentation concern, not a correctness concern. (The related criticism about insufficient explanation in the main text is retained as Major #1.)
- **"Synthetic comparison is stacked because variational methods are batch-size limited"** — The paper explicitly acknowledges this limitation (lines 143–145) and includes F-DIME methods designed for high MI. The criticism restates what the paper already discloses.
- **"The paper should explore more sophisticated embeddings for competitors"** — Scope creep; the paper's contribution is avoiding embeddings entirely, not finding optimal embeddings for competitors.
- **"The empirical derivation of 256–303 nats is not rigorous ground truth"** — The paper presents it as an "order-of-magnitude estimate" and is transparent about the approximation. This is retained as part of Major #3 but the specific charge of "misleading ground truth" is overstated given the paper's caveats.
- **"MINDE not providing meaningful MI estimates is due to high embedding dimensionality"** — The paper already offers this explanation.
- **"Missing related works"** — Cannot verify.

## Novel Insights

The key insight that emerges from this review is that INFO-SEDD's ability to estimate MI beyond the $\log(\text{batch size})$ barrier that fundamentally limits variational estimators is not merely an incremental improvement but a paradigm shift for discrete data. The paper demonstrates this clearly in Table 1, and the text summarization model selection results provide genuine evidence that the method works on real-world discrete data at scale. However, the theoretical presentation is notably less polished than empirically comparable work (e.g., MINDE for continuous data), and several experimental design choices (the unexplained $\rho=0$ bias, the opaque "Empirical MI estimate" baseline) weaken what could otherwise be a very strong empirical package. The synthesis suggests the paper has a real contribution that is somewhat undermined by presentation gaps that the authors could address with a revision.

## Suggestions

1. Provide a self-contained derivation of Equation (4) in the main text, showing how Dynkin's formula applied to a specific $f$ yields the KL expression in forward-time quantities.
2. Clarify the mapping from the DWDSE-trained score to the ratio $\frac{p_t(b)}{p_t(a)}$, especially for the absorbing process.
3. Reframe the consistency bound as a controlled-bias result under stated assumptions, rather than calling it "consistency" in the statistical sense.
4. Explain what the "Empirical MI estimate" in Figure 1 is and why both it and INFO-SEDD report ~100 nats at $\rho=0$.
5. Add a simple baseline to the motif discovery experiment.
6. Include a limitations section and report computational costs.

## Score and Decision

**Calibration anchors consulted:**

| Anchor | Avg Score | Round/Bucket | Comparison to this paper |
|--------|-----------|--------------|--------------------------|
| MINDE (0kWd8SJq8d) | 6.50 | R1-mid, R2 | Continuous diffusion MI estimator. Stronger theory presentation, weaker real-world experiments. Comparable overall quality. |
| Letizia et al. f-DIME (KC2MViQASx) | 5.60 | R1-mid, R2 | Variational MI estimator, batch-size limited. This paper clearly outperforms it empirically. |
| Flow Variational MI (spDUv05cEq) | 6.00 | R1-mid | Flow-based estimator, similar niche. Comparable quality and acceptance outcome. |
| InfoNet (PyHRUMxKbT) | 5.75 | R2 | Feed-forward neural MI estimator. Less ambitious scope than INFO-SEDD. |
| Discrete Diffusion Conv. (pq1WUegkza) | 7.00 | R1-mid | Theoretical analysis of discrete diffusion convergence. More rigorous theory but no MI estimation. |

**Round 1 bracket:** The paper was placed between 5.0 and 7.0 based on comparison with MINDE (6.50, continuous diffusion MI estimation) and the Letizia et al. paper (5.60, variational MI estimation). The paper is empirically stronger than the Letizia paper but has a weaker theoretical presentation than MINDE.

**Round 2 narrowing:** Anchors within the (5.0, 7.0) bracket confirmed the paper sits between the 5.60 (rejected competitor) and 6.50 (accepted MINDE) anchors. The paper's empirical strengths push it above the Letizia paper, but the theoretical gaps and unaddressed $\rho=0$ bias prevent it from reaching MINDE's level.

**What low-band anchors failed at:** The lower-scoring anchors in this space (scores 3–5) typically had weak or missing real-world validation, unsupported claims, or fundamental methodological flaws. The INFO-SEDD paper avoids the most serious of these pitfalls (the synthetic validation is solid, the real-world experiments are present) but shares with them a tendency to overclaim (consistency bound, motif discovery language) and to present derivations without sufficient justification.

**Final score rationale:** The paper presents a novel, well-motivated method with strong synthetic validation and promising real-world results. However, the main theoretical derivation is not self-contained, the consistency bound is weaker than claimed, the text consistency experiment has unexplained biases, and several experiments could be strengthened with additional baselines or uncertainty quantification. The paper makes a clear contribution but needs revision to fully substantiate its claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>