Now I have a thorough understanding of the paper and all claims. Let me compose the final review.

## Summary

This paper studies offline change point localization and inference in dynamic multilayer random dot product graphs (D-MRDPGs). It proposes a two-stage algorithm combining seeded binary segmentation for coarse detection with low-rank tensor estimation via TH-PCA for refinement, establishes consistency for the number and locations of change points, and derives limiting distributions for the refined estimators. A data-driven confidence interval construction procedure is also developed and empirically evaluated.

## Strengths

1. **First offline change-point detection for dynamic multilayer networks** — Section 1.1 explicitly claims this, and the paper delivers a systematic treatment of the problem (Algorithm 1, Section 2.2). The extension from single-layer (Wang et al., 2021) to multilayer settings is nontrivial and practically motivated.

2. **First derivation of limiting distributions for change-point estimators in network data** — Theorem 2 (Section 3) provides the limit distribution in the vanishing-jump regime, characterized by a two-sided Brownian motion. The paper is upfront that this is a first result of its kind in the network literature.

3. **Strong empirical performance across diverse scenarios** — Table 1 shows CPDmrdpg achieving substantially lower absolute error in estimating the number of change points and higher time-segment coverage than both gSeg and kerSeg across four scenarios, including two (Scenarios 2 and 3) that violate Model 1 assumptions, demonstrating robustness.

4. **Novel combination of seeded binary segmentation and tensor-based refinement** — Algorithm 1's two-stage architecture (SBS for coarse detection, TH-PCA for refinement) is well-motivated, and the paper provides computational complexity \(O(T n^2 L r \log^2(T \vee n))\).

5. **Fully data-driven confidence interval construction** — Section 3.1 describes an actionable 4-step procedure (estimate jump size → estimate variances → simulate limiting distribution → build CI). Table 2 shows it achieving 95–100% coverage in most settings, a capability none of the compared methods offer.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between theoretical assumptions and practical implementation.** The theory (Algorithm 1 input, Theorem 1, Theorem 2) assumes *four* mutually independent tensor sequences \(\{\mathbf{A}(t)\},\{\mathbf{A}'(t)\},\{\mathbf{B}(t)\},\{\mathbf{B}'(t)\}\). However, Section 2.2 (line 119) states: "In practice (and in our numerical experiments in Section 4), Stage I and Stage II are implemented using the same two split tensor sequences via the odd-even splitting approach." The two sequences from odd-even splitting are not independent (they partition a single sequence), and the algorithm uses two rather than four. The paper acknowledges this gap but does not bridge it — no theoretical result covers the actual implementation. This means the consistency and distributional guarantees in Theorems 1 and 2 do not directly apply to the procedure as evaluated. This is a structural limitation that would require either adapting the theory to the odd-even split scheme or redesigning the algorithm to match the four-sequence assumption.

2. **Simulation results reported without any measure of variability.** Table 1 reports only means over 100 Monte Carlo trials — no standard errors, standard deviations, or interquartile ranges. The proposed method achieves near-perfect scores (0.00 or 0.01 error) in many settings, and the near-zero variability across trials is unusual enough that variance information is essential for interpretation. Without it, the reader cannot assess whether the performance is genuinely reliable or whether the specific threshold/tuning choices produce near-perfect results by construction. Reporting variability is standard practice and its omission here weakens the empirical evidence.

### Minor

1. **Confidence interval coverage not theoretically justified for the plug-in procedure.** Section 3.1 constructs CIs using plug-in estimates \(\hat{\kappa}_k, \hat{\Psi}_k, \hat{\sigma}^2_{k,k'}\) and simulates the limiting distribution with estimated parameters. The paper does not prove that the plug-in estimators converge fast enough for the resulting quantiles to yield asymptotically valid coverage. The empirical evaluation (Table 2) is encouraging, but a theoretical justification or a bootstrap calibration study would substantially strengthen the inference claims.

2. **DDM simulation setup is not fully aligned with Model 1/Definition 1.** In the DDM (line 289), the edge probability is \(\mathbf{P}_{i,j,l}(t) = X_i^\top W_{(l)}(t) Y_j\) using *two* independent sets of latent positions \(\{X_i\}\) and \(\{Y_i\}\), whereas Definition 1 uses a single set \(\{X_i\}\) with \(\mathbf{P}_{i,j,l} = X_i^\top W_{(l)} X_j\). This is a different parameterization, and the paper does not clarify whether the DDM is a special case of the assumed model or a deliberate departure. The theoretical results are proved for Definition 1, so the connection to the DDM experiments should be explicitly stated.

3. **SNR condition mixes terms with different scalings without explanation.** Assumption 2 (line 213) involves \(\sqrt{nL^{1/2} + d^2 m_{\max} + nd + L m_{\max}}\). The term \(nL^{1/2} = n\sqrt{L}\) has a different rate structure from \(nd\) and \(L m_{\max}\). No derivation or intuition is given for how these terms combine, making it difficult to interpret the condition's implications.

4. **Inner product notation in Stage I not explicitly defined.** Algorithm 1 (line 155) uses \(|(\tilde{\mathbf{A}}^{\alpha,\beta}(t), \tilde{\mathbf{B}}^{\alpha,\beta}(t))|\) where \((\cdot,\cdot)\) is not formally defined as an inner product. Section 1.2 defines \(\langle \mathbf{M}, \mathbf{Q} \rangle\) as the inner product, but the parentheses notation is used without comment. This is minor as the meaning is clear from context.

### Trivial
- "Inf" values for gSeg in Table 1 are explained only loosely (lines 336–337 state "they often detect spurious change points" but "Inf" for \(d(\hat{\mathcal{C}},\mathcal{C})\) actually indicates the estimated set is empty — this should be clarified).

## Nice-to-Haves
- Include standard deviations or interquartile ranges alongside means in Table 1.
- Add trajectory plots or boxplots of localization errors across trials to visualize performance distribution.
- Provide a sensitivity summary (at least a brief table or paragraph) for the threshold \(\tau\) and input ranks \(r_1, r_2, r_3\) in the main paper rather than deferring entirely to Appendix G.1.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Missing appendix content (Criticism 3 from harsh critic):** The reviewer faults the paper for deferring robustness checks, online-method comparisons, and non-vanishing regime results to Appendix G.1. Per the review guidelines, appendices are stripped by the parser from all submissions and exist in the original; this is not a valid weakness.
- **Low-rank assumption not grounded (Criticism 5):** The paper states the rank assumption (Assumption 1(ii)–(iii)) and justifies it by noting that the Tucker ranks are bounded by rank\((Q(\eta_k)) +\) rank\((Q(\eta_{k+1}))\) in working intervals containing a single change point (lines 205–209). The assumption is stated transparently, which is standard practice. The critic's demand for a generative process that makes weight matrices low-rank goes beyond what assumptions sections typically require. The paper also notes (line 209) that "such ambiguity is common in tensor-based models (e.g. Jing et al., 2021)."
- **Non-vanishing regime deferred to appendix:** The paper explicitly states (line 251) that non-vanishing regime results are in Appendix A. The appendix exists in the original submission.
- **Real-data intervals "suspiciously narrow":** The critic characterizes the narrow CIs as "suspicious" — this is a speculative claim, not a verifiable weakness. The intervals are what the procedure outputs, and the paper reports them straightforwardly.
- **Three-decimal reporting:** This is a style nitpick; decimal precision in reporting is a presentational choice.
- **Definition 5 formula garbled:** The critic notes the formula appears garbled. This is a parser artifact from LaTeX extraction; the original submission does not have this issue.
- **"First" novelty claim concern:** The critic suggests the claim of being "first" on offline D-MRDPG CPD should be qualified. This is a generic speculation about a missing comparison; per guidelines, I cannot confirm or deny the novelty claim without external knowledge.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Bridge the theory-practice gap.** Two options: (a) adapt the theoretical analysis to cover the odd-even splitting scheme, or (b) redesign Algorithm 1 to use four genuinely independent sequences (e.g., by splitting the data into four folds) and update the experiments accordingly. Either approach would make the theory and experiments coherent.
2. **Add variability measures** (standard errors, SDs, or IQRs) to Table 1 so readers can assess the reliability of the near-perfect results.
3. **Clarify the DDM model class** — explicitly state whether the DDM (using two independent position sets \(X_i, Y_j\) with \(X_i^\top W Y_j\)) is a special case of Definition 1 or a separate generative model, and explain how the theoretical guarantees apply.
4. **Provide analytic justification** for the plug-in CI procedure or add a bootstrap calibration study on simulated data to demonstrate coverage validity.
5. **Include a sensitivity summary** for the threshold constant and input ranks in the main paper, at least as a brief paragraph.

## Score and Decision

**Originality:** Good — first to tackle offline CPD in D-MRDPGs, with novel combination of methods.

**Importance of research question:** Good — multilayer dynamic networks are practically relevant.

**Claims supported:** Moderate — theory and experiments are mismatched (four-sequence assumption vs. two-sequence implementation); missing variability measures weaken empirical support.

**Soundness of experiments:** Moderate — diverse scenarios and strong results, but lack of variance measures and misalignment between theory and practice are notable gaps.

**Clarity of writing:** Moderate — generally well-structured, but some notation could be clearer and definition parsing artifacts hinder reading.

**Value to the research community:** Good — novel limiting distribution results and CI construction procedures would be useful contributions if properly validated.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>