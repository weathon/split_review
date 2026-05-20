## Summary

This paper proposes INFO-SEDD, a method for estimating KL divergences and mutual information (MI) for high-dimensional discrete data using Continuous Time Markov Chains (CTMCs) and discrete diffusion models. The key ideas are: (1) linking KL divergence estimation to CTMC dynamics via Dynkin's formula, (2) using an absorbing-state design so a single score model trained on the joint distribution suffices for both joint and marginal scores, and (3) evaluating on synthetic benchmarks, text summarization model selection, and genomics motif discovery.

---

## Strengths

- **Dominant performance on challenging synthetic benchmarks (Table 1).** INFO-SEDD estimates MI within ~0.5 nats of ground truth for MI values up to 50 and dimensions up to 50, while competitors (GAN-DIME, HD-DIME, MINDE, MINE, NWJ, SMILE) deviate by tens of nats. At MI=50/D=50, INFO-SEDD reports 47.77±1.18 versus the next best (MINDE) at 32.60±3.93. This is a clean, compelling result that directly supports the method's core claim.

- **Single-model marginal extraction via absorbing-state design (Equation 6).** The observation that an absorbing CTMC lets a single score model trained on the joint distribution compute marginal scores (by zeroing out variables with the absorbing token) is architecturally elegant and well-motivated. This eliminates the need for separate joint/product-of-marginals models, a concrete advantage over naive CTMC-based approaches.

- **Real-world validation beyond synthetic benchmarks.** The paper validates on two real discrete-data domains:
  - *Text summarization:* INFO-SEDD-C achieves Pearson correlation r=0.740 with human consistency scores (Table 2), substantially higher than KL-DIME (0.214), HD-DIME (0.331), or SMILE (-0.074). The monotonic relationship with consistency is visually confirmed (Figures 2–3).
  - *Genomics motif discovery:* A single INFO-SEDD-J model identifies the TATA-box promoter motif (positions -39 to -26 relative to TSS) via subset-wise MI profiling without retraining per window (Figure 5), which competing estimators cannot do natively.

- **Theoretical error bound (Equation 7).** The paper provides an explicit decomposition into estimation error (linear in score approximation error) and truncation bias (exponentially decaying with T), establishing consistency up to an asymptotically vanishing bias.

---

## Weaknesses

### Fatal
None.

### Major

- **The derivation of the KL estimator is presented in a way that is mathematically unsound in the main text.** Equation (2) states:
  \[
  \text{KL}[\vec{p}_0 \parallel \vec{q}_0] = \mathbb{E}\left[ \log \frac{\vec{p}_0}{\vec{q}_0}(\vec{X}_T) \right] = \mathbb{E}\left[ \log \frac{\vec{p}_T}{\vec{q}_T}(\vec{X}_T) \right]
  \]
  The first equality is problematic: KL divergence between \(\vec{p}_0\) and \(\vec{q}_0\) is an expectation over \(X_0\sim\vec{p}_0\), not over \(X_T\sim\vec{p}_T\). The second equality is similarly unjustified as presented. These equalities are not standard identities and the paper does not provide the necessary justification in the main text. While a corrected derivation may exist in the appendix (which is stripped by the parser), the main text as written is confusing and mathematically questionable on a central claim. This is not fatal — the empirical results are strong and the underlying idea (using Dynkin's formula with shared-generator CTMCs) can be correctly justified — but the exposition requires a major rewrite. The statement "We omit the term \(\mathbb{E}[\log(\vec{p}_0/\vec{q}_0)(\vec{X}_0)]\), as both \(\vec{p}_0\) and \(\vec{q}_0\) converge to \(\pi\)" is additionally unclear, since \(\vec{p}_0\) and \(\vec{q}_0\) are the *initial* distributions; it is \(\vec{p}_T,\vec{q}_T\) that converge to \(\pi\).

### Minor

- **No computational cost discussion.** INFO-SEDD requires training a discrete diffusion score model, which is substantially more expensive than the variational baselines (MINE, SMILE, etc.). The paper provides no runtime, parameter count, or convergence speed comparisons. This is important for practitioners deciding whether the improved accuracy is worth the cost.

- **No discussion of limitations or failure modes.** The paper does not address sensitivity to the time horizon T and noise schedule, the assumption that the absorbing state probability approaches 1 (finite T may cause residual bias), or the fact that the method requires a pretrained backbone (CADUCEUS, MDLM-SMALL) that may not exist for arbitrary discrete data.

- **Model selection experiment uses only 15 data points.** The Pearson correlations in Table 2 (e.g., r=0.740 for INFO-SEDD-C vs. consistency) lack confidence intervals or p-values, making it difficult to assess sampling uncertainty. With n=15, a single outlier could substantially affect the correlation.

- **Missing comparison with simple discrete estimators in low dimensions.** The paper could include a small-scale experiment (low D, small |χ|) comparing INFO-SEDD against plug-in estimators (e.g., empirical MI with Miller–Madow correction) to demonstrate that the method recovers known ground truth in a regime where classical methods are viable. This would strengthen the paper's generality claim.

### Trivial

- The phrase "both \(\vec{p}_0\) and \(\vec{q}_0\) converge to \(\pi\)" (line 69) is a notational error — it should refer to \(\vec{p}_T\) and \(\vec{q}_T\) converging to \(\pi\) (the stationary distribution of the forward CTMC).

---

## Nice-to-Haves

- A more self-contained derivation sketch in the main text from the correct starting point (KL as expectation over X₀) through Dynkin's formula to the final estimator, without requiring the reader to reconstruct the argument from the appendix.
- A brief description of the synthetic benchmark construction in the main text (how the ground-truth MI is achieved) for reader convenience.
- Confidence intervals (e.g., bootstrap) for the model selection correlations, especially given the small sample size.

---

## Removed Points

These points from the inputs are removed with brief justification:

1. *"The synthetic benchmark construction is not described, making results unverifiable"* (Harsh Critic) — The paper states "full details are in Appendix C.1" and gives a clear sketch of the setup (two vectors X,Y, dimension D, support |χ|). Deferring generative details to the appendix is standard practice in 8-page conference papers. This is not a genuine weakness.

2. *"The text summarization reference line (256ρ–303ρ) is not properly justified"* (Harsh Critic) — The paper explicitly describes this as an "order-of-magnitude estimate" and provides the reasoning (entropy rates × average summary length). It is presented as a consistency check, not a rigorous ground-truth bound. The paper does not overclaim here.

3. *Unsupported criticisms about appendix content* (Harsh Critic: "the entire argument is deferred to the appendix"; "no proof in main text" for Equation 6) — The parser strips appendices from all papers. The original submission contains these proofs.

4. *Generic "could improve with user studies / more models / larger dataset" style suggestions* from both reviewers that do not identify concrete flaws.

5. *Strength Finder claims about the paper's Definition/Equation (6) being "proven" and "concrete architectural advantage"* — These are retained in Strengths as they are factually correct.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Rewrite the derivation in Section 2.2.** Start from the correct identity: for two CTMCs with the same generator, apply Dynkin's formula to \(f(x,t)=\log(p_t/q_t)(x)\) to relate \(\mathbb{E}[\log(p_T/q_T)(X_T)]\) to \(\text{KL}[p_0\|q_0]\) plus an integral. Then argue that the \(\mathbb{E}[\log(p_T/q_T)(X_T)]\) term vanishes as \(T\to\infty\) (since \(p_T,q_T\to\pi\)). This would put the derivation on solid footing without requiring major changes to the final estimator.

2. **Add a "Limitations and Computational Cost" section.** Discuss runtime relative to variational baselines, sensitivity to hyperparameters (T, noise schedule), and scenarios where the method might fail (e.g., when the score model is poorly trained).

3. **Add bootstrap confidence intervals** to the Pearson correlations in Table 2.

4. **Include a low-dimensional sanity check** comparing INFO-SEDD against a classical plug-in estimator to demonstrate the method works in a well-understood regime.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| InfoBridge (y8Kzu9SKpv) | 5.00 | 1 (middle) | Similar topic (diffusion-based MI). INFO-SEDD has stronger benchmarks and real applications but weaker theoretical presentation. Slightly stronger overall. |
| FlashMI (dB6DYLpjw4) | 5.33 | 1 (middle) | MI estimation via hypernetwork. Different methodology. Similar experimental strength. |
| Error Analysis Discrete Flow (EFYb8SsRi7) | 6.50 | 2 (narrow) | Pure theory, CTMC KL analysis. Much stronger theoretical rigor but zero experiments. Not directly comparable. |
| Complexity Analysis Norm. Const. (96fJALwotm) | 5.50 | 2 (narrow) | Theory paper on annealing. INFO-SEDD has more experimental breadth but less theoretical depth. |
| Accurate MI Est. (x3c4um7jJX) | 3.00 | 1 (weak) | Evaluation-focused MI paper. Much weaker on novel methodology. |
| Kelly Gamblers (IaeZcYpRxD) | 3.00 | 1 (weak) | Theory/conceptual diffusion paper with limited experiments. |

**Round-1 bracket:** [3.5, 7.5] anchored by middle-band papers. **Round-2 bracket:** narrowed to [5.0, 6.0] based on InfoBridge (5.00) and Complexity Analysis (5.50) as the closest topical matches. **Final placement:** The paper's strong empirical validation and real-world applications push it above InfoBridge (5.00), while the problematic theoretical presentation prevents it from reaching the 6+ range of papers with sounder derivations. It is most comparable to the Complexity Analysis paper at 5.50.

**Score: 5.5**

**Decision: Accept (Poster)**

The paper makes a genuine contribution — a new method for discrete MI estimation that demonstrably outperforms existing approaches on high-dimensional benchmarks — but the theoretical derivation in the main text needs a significant rewrite. The empirical evidence is strong enough to warrant acceptance with the expectation that the authors address the theoretical presentation concerns in the final version.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>