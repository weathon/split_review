Now I have a comprehensive picture. Let me synthesize the final review.

## Summary

The paper proposes Causal Transfer Learning (CTL), a framework that uses pre-trained language models (PLMs) to learn robust causal representations for OOD generalization. The core idea is to leverage pre-trained and fine-tuned PLMs as paired representations to identify causal features C, then use token-level local features Φ as a mediator to construct a front-door adjustment estimator P(y|do(x)). The paper presents a theoretical identification argument (Theorem 2), a training algorithm, and experiments on semi-synthetic and real-world sentiment analysis datasets.

## Strengths

1. **Novel application of causal front-door adjustment to PLM fine-tuning.** The idea of using a pre-trained model (M0) and its fine-tuned version (M1) as two "environments" to identify invariant causal features is creative and practically appealing. This operationalizes the theoretical framework of Von Kügelgen et al. (2021) for the PLM setting, which prior work does not provide.

2. **Consistent and measurable OOD improvements.** Across two semi-synthetic datasets (Amazon, Yelp) and one real-world setup (Amazon+Yelp platform shift), CTL consistently outperforms strong baselines (SFT, SWA, WISE) as spurious correlations weaken. For example, CTL achieves 58.40 F1 vs SFT's 49.24 on Yelp at 10% spurious correlation — a ~9 point improvement (Table 1). The pattern is consistent across all OOD levels (70%, 50%, 30%, 10%).

3. **Informative ablation study.** The comparison of CTL with CTL-N (no front-door adjustment), CTL-C (causal features only), and CTL-Φ (spurious features only) provides clear evidence about which components contribute to robustness. CTL-Φ degrades sharply OOD, confirming spurious features are the source of the problem. CTL-C performs well but CTL (full method) consistently outperforms it, especially in the real-world experiment (49.22 vs 42.25 at 10% OOD, a ~7 point gap).

## Weaknesses

### Fatal
None.

### Major

1. **Algorithm violates the paired-representations assumption that underpins theoretical identification.** Assumption 2 states: "For each input text X, we can obtain a pair of variations of its representations, R0 and R1, where their causal factors C remain the same." This requires two representations of the *same* text. However, Algorithm 1 (Step 2–4) samples two *different* texts with the same label (x̃_i and x̄_i) and uses M0(x̃_i) and M1(x̄_i) as the paired representations. The invariance objective in Equation 3 (which expects paired representations of the same input) is then applied to representations of different texts. Two different texts with the same label could have different causal features C. The paper provides no justification for this substitution and does not discuss how it affects the validity of the learned C. Without this alignment, the theoretical grounding for identifying causal features via Theorem 1 / Von Kügelgen et al. (2021) is compromised as implemented.

2. **The derivation of Theorem 2 (identification via front-door adjustment) is imprecise.** The proof sketch goes from P(y|do(x)) → P(y|do(s,c)) with the justification "Assumption 1" (X = f(S,C)). Under this functional decomposition, do(X=x) fixes X to value x, which imposes a joint constraint on (S,C); it does *not* correspond to independently intervening on S and C. The step from do(x) to do(s,c) is not formally justified via do-calculus. The subsequent application of Rule 3 also requires careful checking of the graph structure. While a proof sketch is acceptable in an ML paper, the gaps here are large enough to make the identification claim unsupported by the provided reasoning.

3. **Inference-time shuffling of Φ makes predictions batch-dependent.** Algorithm 2 shuffles Φ within the mini-batch during *inference* to approximate the marginalization over Φ' in Equation 1. This means the prediction for a single test input depends on which other test points happen to be in the same batch — changing the batch composition would change the prediction. The paper does not discuss this property, its sensitivity to batch size, or whether this approximation converges to the true front-door estimand in the large-batch limit.

### Minor

4. **The gap between CTL and CTL-C is modest in some settings.** On the Yelp semi-synthetic dataset at 10% OOD, CTL achieves 58.40 vs CTL-C's 57.75 (a 0.65 point difference), suggesting that most of the gain comes from learning C rather than from the front-door adjustment via Φ. The gap is larger in the real-world experiment (6.97 points) and on Amazon (3.00 points), but the variability weakens the paper's claim that the front-door adjustment provides substantial additional benefit.

5. **No uncertainty reported in main tables.** Tables 1 and 2 report only the mean F1 across 5 runs, with no standard deviations or confidence intervals. Figure 2 shows box plots (for 5 runs) but only for a subset of methods. Given the modest scale of some improvements, readers need uncertainty estimates to assess significance.

6. **The notation and presentation of Table 2 has inconsistencies.** The column header reads "Train FI 90%" instead of "Train F1 90%" for the SFT0 row. Additionally, Figure 3's caption states the y-axis ranges from 0.00 to 0.50 (fractional F1), while Table 2 reports values like 94.01 and 91.39 (percentage F1). If only the OOD scenarios are plotted (where values are 15–49), those do fall in the 0.00–0.50 range, but the caption lists ID 90% as one of the subplots, which would be off-scale. This needs clarification.

### Trivial
- The proof of Theorem 2 (Section 4.2) uses notation `P(Φ')` and `P(Φ̂'|x')` — the hat notation on Φ is introduced without definition.
- The "FI" vs "F1" typo in Table 2's first column header.

## Nice-to-Haves
- Analysis of how batch size affects the Φ-shuffling approximation during inference and training would strengthen the paper's methodological rigor.
- A discussion of how the weight between the L2 term and entropy terms in Equation 3 is set, and its sensitivity, would be valuable.
- Including statistical significance measures (e.g., std dev, confidence intervals) in the main tables.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Weak baselines (DRO, adversarial training missing):** The critic claims the baselines are "weak" and DRO/adversarial training/Mixout are missing. However, (a) SWA and WISE are strong, recent baselines specifically for PLM fine-tuning; (b) DRO requires group annotations which are not available in the single-domain setting studied; (c) the paper's setting is single-domain OOD, not the multi-domain setting where DRO typically applies. This criticism is scope creep. **Removed.**

- **"Theorem 2 proof is likely incorrect":** The proof is imprecise (noted in Major weakness 2), but the critic's stronger claim that it is "likely incorrect" overstates the issue. The sketch could be made rigorous with proper do-calculus, and the front-door formula is a standard result. The problem is incomplete justification, not an incorrect result. **Demoted from the reviewer's severity to Minor/Major.**

- **"CTL-C vs CTL shows front-door adjustment isn't providing much benefit":** This is unevenly true. The gap varies from 0.65 (Yelp 10%) to 6.97 (Real-world 10%). The critic selectively cited the smallest gap. The real-world experiment shows a clearly meaningful gap. **Retained as Minor weakness 4 but weakened from the critic's framing.**

- **"Figure 3 inconsistency — y-axis vs table values":** As analyzed, the y-axis 0.00–0.50 (fractional) is consistent with the OOD values (e.g., 0.49 for CTL at 10%); the ID 90% subplot label in the caption may be a copy-paste error from Figure 2. **Demoted to a minor presentation note.**

- **"Missing related work":** Removed per hard rule — I cannot verify which related works exist or are missing.

- **"Computational cost comparison":** The critic suggests comparing training time. This is a reasonable request but not a core weakness. **Moved to Nice-to-Haves.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Align the algorithm with the theoretical assumption.** Either change the algorithm to use two representations of the *same* text (e.g., M0(x_i) and M1(x_i) for the same x_i) as the paired representations in Equation 3, or provide a separate justification for why same-label, different-text pairs still satisfy the paired-representations requirement (e.g., arguing that texts with the same label share identical causal features under the assumed generative process, and validating this with synthetic data where C is known).

2. **Provide a rigorous do-calculus derivation for Theorem 2** or restructure the identification argument to reference known front-door results rather than attempting a novel proof sketch that has gaps.

3. **Replace the inference-time Φ shuffling** with a more principled marginalization (e.g., using the empirical distribution of Φ from the training set, or explicitly computing the expectation over the learned P(Φ|x) for each test point individually). Alternatively, discuss the approximation quality as a function of batch size.

4. **Report standard deviations** for all main results and discuss the practical significance of the observed improvements.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak band (<3.5): y2qZhSTtzU (3.0), InWaCoIMMN (3.0), 7LZjuA4AB2 (3.0) — Rejected/Withdrawn papers with limited contributions. Current paper clearly stronger.
- Middle band (3.5–7.5): OatZMyMuIo (4.0), mb9oOA3rD9 (4.5), 9ljHiYuRHl (4.25), wsjNCPqziJ (4.5). Current paper is comparable to slightly above the lower end of this band.
- Strong band (>7.5): 3cuJwmPxXj (8.0), MO5PiKHELW (7.75), TjhUtloBZU (8.5), PdaPky8MUn (8.0). Current paper significantly weaker — these have rigorous theory and clean execution.

**Initial bracket:** 3.5 – 6.0

**Round 2 (Narrowing):**
- oKglS1cFdb (5.67) — Reject. Stronger theoretical contribution but less practical. Current paper is weaker than this anchor.
- v1VvCWJAL8 (5.75) — Accept (poster). Stronger theoretical grounding. Current paper is weaker.
- SksPFxRRiJ (5.0) — Reject. Comparable methodology gaps but different domain. Current paper similar quality.
- BlzBcWYmdB (5.0) — Reject. Similar approach-level contribution with gaps. Current paper comparable.
- F7XPZnIUHh (4.2) — Reject. Treatment effect estimation. Current paper is slightly stronger.

**Final positioning:** The paper has a novel and appealing core idea with consistent empirical results, but the theory-implementation gap (Assumption 2 vs Algorithm 1) and imprecise derivations are substantial weaknesses that prevent acceptance. It is somewhat stronger than the 4.0 anchor (OatZMyMuIo) but clearly weaker than the 5.67 anchor (oKglS1cFdb). Placing it at 4.5 reflects a paper with identifiable merit that is not yet ready for publication.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>