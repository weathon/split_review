I have thoroughly verified all reviewer claims against the paper. Now I'll produce the final consolidated review.

---

## Summary

This paper identifies that training deep kernel MMD for machine-generated text (MGT) detection with data from multiple LLMs (populations) causes the variance of MMD to inflate sharply, degrading detection reliability. To address this, the authors propose MMD-MP, a multi-population aware optimization that removes the intra-class MGT term $k_\omega(y, y')$ during training (using a Multi-Population Proxy, MPP) while still using the full MMD at test time. Experiments across paragraph-based (two-sample test) and sentence-based (single-instance detection) settings on HC3 and multiple LLM families show consistent gains over strong baselines, with especially striking improvements of 23–27% absolute test power on unknown LLMs.

## Strengths

1. **Identifies a genuine and previously underexplored problem in deep kernel MMD training.** The paper clearly demonstrates — through variance decomposition (Section 2.2) and empirical observations (Section 2.3, Figures 1–2) — that $k_\omega(y,y')$, the intra-class term for machine-generated texts, becomes the dominant source of variance when training data comes from multiple LLM populations. This analysis is novel within the MMD-based detection literature and well-supported by the paper's figures and decomposition.

2. **Consistent and often large empirical gains, especially on unknown LLMs.** The most compelling evidence is in the transferability experiments (Tables "Test Power on Unknown LLMs" and "AUROC on Unknown LLMs"): MMD-MP achieves 61.79% vs. 38.18% (GPT-Neo-L), 59.57% vs. 31.92% (GPT-j-6b), and 77.69% vs. 51.28% (GPT4all-j) in test power over MMD-D — absolute improvements of 23.6–27.6%. These gains are far beyond what margin-of-error or random variation could explain. Gains in multi-population paragraph detection (Tables 1–2, average 8.2–14.0% improvements with limited data) further support the method's value.

3. **Provides theoretical infrastructure for the proposed MPP objective.** The paper proves asymptotic normality of the $\widehat{\mathrm{MPP}}_u$ estimator (Proposition 1) and a uniform convergence bound (Theorem 1) showing $\hat{J}$ converges to the optimal $J$ as $n$ grows. These results give the proposed objective formal statistical grounding beyond a purely heuristic modification.

4. **Comprehensive evaluation across diverse detection scenarios.** Experiments cover paragraph-based and sentence-based detection, full vs. limited training data, unbalanced training (2000 HWT vs 400 MGT), and five LLM families (ChatGPT, GPT2, GPT3, GPT-Neo, GPT4all-j), with results consistently favoring MMD-MP.

## Weaknesses

### Fatal
None.

### Major

1. **Training-testing objective mismatch lacks a formal theoretical link.** The paper trains the kernel using MPP (which excludes $k_\omega(y, y')$) but tests using the full MMD (which includes it). The paper acknowledges this gap explicitly (Remark 2, lines 285–288; Algorithm 2 vs. Algorithm 1) and provides heuristic justification via the "pairing rules" argument in Section 2.3. However, there is no formal argument — not even a bound or an approximate guarantee — showing that optimizing $\widehat{\mathrm{MPP}}_u/\hat{\sigma}$ during training yields a kernel that is near-optimal for the full MMD test power at test time. Corollary 1 reveals that the test power of MPP depends on $R(S_\mathbb{Q})$ (the excluded term) as an additive component, so the training objective is optimizing a lower bound on the quantity actually used at test time. The paper's empirical success suggests the approach works, but the reasoning remains heuristic. This gap weakens the claim of a "pioneering exploration of the optimization mechanism of kernel-based MMD."

### Minor

1. **Single-population gains are modest.** In the single-population setting (Table 1, full data), MMD-MP's test power improvements over MMD-D are 1–4%; AUROC gains (Table "AUROC 3000") are 0.2–0.9%. While these are consistent positive deltas, the paper does not foreground that its primary advantage materializes in multi-population and transfer scenarios. This is not a contradiction of the paper's scope (the title and abstract clearly target multi-population), but it would strengthen the paper to explicitly state where the method excels and where gains are marginal.

2. **Explanation for transferability is heuristic and undersupported.** The paper claims (Section 3.3) that MMD-MP "prioritizes fitting HWTs … reducing reliance on MGTs," providing the mechanism for the impressive transferability results. However, no direct evidence is presented that the learned kernel actually focuses more on HWT structure — the t-SNE visualization (Figure 7) shows improved two-way separability but does not reveal what the kernel has learned about HWT vs. MGT features. A controlled analysis (e.g., measuring how kernel features change when training MGT populations are systematically varied, or spectral analysis of the kernel) would substantially strengthen this claim.

3. **The frozen feature extractor $\hat{f}$ is not specified.** The paper defines the deep kernel in Eqn. (4) using a fixed feature extractor $\hat{f}$, and Algorithm 1 lists it as input, but never states what $\hat{f}$ is in the experiments (e.g., BERT embeddings, sentence transformers). This is a simple implementation detail that affects reproducibility.

### Trivial

- None beyond what has been addressed above.

## Nice-to-Haves

- A synthetic experiment that varies the number of mixture components (analogous to varying the number of LLM populations) would further validate the core intuition. The current synthetic setup varies $\mu$ but not the component count.
- A limitations section discussing the reliance on a fixed feature extractor, the need for i.i.d. reference HWTs, and the computational cost of permutation-based null distribution estimation would improve completeness.

## Removed Points

- **Comparison to watermarks (Kirchenbauer et al., 2023) and Fast-DetectGPT (Bao et al., 2024):** Removed per the "missing related works" rule — these methods operate under different assumptions (e.g., watermarking requires access to the source model). The critic acknowledges the potential incomparability.
- **"Notation confusion" in Section 2.2 decomposition:** Removed as a subjective presentation preference. The decomposition is mathematically sound even if dense.
- **Complaint that "title and abstract imply a general solution":** Factually incorrect — the title says "Multi-Population Aware Optimization" and the abstract explicitly scopes to the multi-population variance problem.
- **Synthetic experiment only tests $\mu$:** Scope creep for a toy experiment meant to validate one dimension.
- **Missing limitations section / missing appendix / missing proofs:** Per instructions, parser-stripped sections (appendices, proofs) exist in the original submission and should not be flagged as absent.

## Novel Insights

The central insight — that the intra-class MGT term $k_\omega(y,y')$ in MMD's optimization objective creates a "pairing rules" conflict that inflates variance when MGT data are drawn from heterogeneous populations — is genuinely useful and likely to generalize beyond MGT detection to any MMD-based two-sample test with multi-population training data. The paper's most impressive result (23–27% absolute gains on unseen LLMs) is surprising in magnitude and suggests that variance reduction in the training kernel translates far more strongly to generalization than prior work would predict. This deserves deeper theoretical analysis in future work.

## Suggestions

1. **Formalize the MPP-full-MMD link.** At minimum, show empirically (via a controlled sweep) that the solutions found by optimizing MPP consistently yield higher full-MMD test power than those found by optimizing MMD-D. A theoretical bound relating $J_{\mathrm{MPP}}$ to $J_{\mathrm{MMD}}$ would be stronger but even empirical tracking would substantially raise confidence in the approach's principled nature.

2. **Specify $\hat{f}$** in the experiments section, and briefly discuss whether the method's advantages hold across different feature extractors (or note this as future work).

3. **Provide a direct analysis of transferability.** One concrete step: measure test power as the training MGT distribution is systematically varied away from the test MGT distribution to empirically characterize MMD-MP's generalization advantage over MMD-D.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>