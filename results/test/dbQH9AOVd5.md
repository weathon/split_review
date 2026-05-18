Now I have a thorough understanding of the paper and can verify the reviewers' claims. Let me construct the final consolidated review.

## Summary

This paper proposes I-STAR, a regularization method that uses IsoScore$^{\star}$—a modified version of the IsoScore metric that incorporates RDA shrinkage for mini-batch stability—to adjust the isotropy of LLM representations during fine-tuning. The paper makes three contributions: (1) IsoScore$^{\star}$, a stable, differentiable isotropy measure; (2) I-STAR regularization that can push isotropy up or down; and (3) an empirical finding that *decreasing* isotropy (making representations more anisotropic) tends to improve downstream performance across three LLMs and nine tasks, contradicting a prevailing belief in NLP that isotropy is beneficial.

## Strengths

- **Introduces a mini-batch-stable isotropy measure via RDA shrinkage.** The paper demonstrates clearly (Figure 1) that vanilla IsoScore systematically underestimates isotropy when the number of samples is small relative to dimensionality (|X| < d). The shrinkage-based stabilization in IsoScore$^{\star}$ is a practical methodological advance that enables isotropy to be used as a differentiable regularizer during training, which was not previously feasible with vanilla IsoScore due to instability. Algorithm 1 and the stability analysis in Section 3 are well-presented.

- **Shows that CosReg does not actually affect isotropy.** The paper provides evidence (Figure 3, line 184) that CosReg alters the *mean* of embeddings rather than the covariance structure: after CosReg with λ=1, IsoScore$^{\star}$ values for BERT, ALBERT, and DistilBERT on SST-2 are 0.004, 0.007, and 0.007, respectively—essentially zero. This is a valuable finding because CosReg has been used as an isotropy-enforcing regularizer in prior work, and the paper explains why its reported benefits may be unrelated to isotropy.

- **Connects isotropy to intrinsic dimensionality.** Figure 6 shows that decreasing isotropy (negative λ) lowers the TwoNN intrinsic dimension estimate, while increasing isotropy raises it. This provides a mechanistic link between the paper's findings and the broader ML literature on intrinsic dimensionality and generalization (e.g., dim_compression_nn, intrinsic_dim_nn).

## Weaknesses

### Fatal
None.

### Major

1. **Unclear justification for differentiability claim over vanilla IsoScore.**  
   The paper repeatedly states that IsoScore is "neither differentiable nor stable" (Abstract, Sections 1 and 3) and positions differentiability as a key motivation for IsoScore$^{\star}$. However, vanilla IsoScore computes eigenvalues of a covariance matrix and applies algebraic normalizations—operations that are standardly differentiable (the paper itself acknowledges at line 83 that "PCA is a differentiable function"). If vanilla IsoScore uses the same core operations (covariance → eigendecomposition → normalization), then the claim that it is *not* differentiable requires a specific explanation of what makes it non-differentiable (e.g., eigenvector sign ambiguity in the reorientation step, gradient instability from close eigenvalues, or the non-smoothness of eigenvalue sorting). The paper provides none, leaving the novelty argument partially unsubstantiated. The contribution does *not* depend on being the "first differentiable isotropy measure"—the stability contribution via shrinkage stands on its own—but the paper's framing needs correction or clarification.

2. **Empirical evidence for the core claim is modest and lacks statistical rigor.**  
   The paper's headline finding—that decreasing isotropy improves performance—is supported by Table 1, but most comparisons show I-STAR vs. Base within overlapping standard deviations. For example, BERT I-STAR vs. Base on SST-2 (92.65±0.18 vs. 92.40±0.41), QNLI (89.51±0.69 vs. 89.49±0.30), and RTE (62.53±0.70 vs. 62.24±0.48) all show overlap. DistilBERT QNLI is a counterexample where Base (87.40±0.34) clearly outperforms I-STAR (86.25±0.32). The strongest signal comes from SQUAD (e.g., BERT F1: 87.76±0.11 vs. 87.02±0.11), but only for one of three models on one task. No formal statistical tests (e.g., paired t-tests, confidence intervals, correction for multiple comparisons) are reported. The Discussion (line 200) calls this "strong empirical evidence," which overstates the case. The paper's conclusion about anisotropy being beneficial is suggestive and interesting, but the onus is on the authors to demonstrate reliability beyond seed variation, especially when challenging a large body of work.

### Minor

1. **Only one isotropy regularizer baseline (CosReg).** The paper compares I-STAR only to CosReg. The related work mentions ISO-BN (Isotropic Batch Normalization) and other methods (e.g., whitening penalties). While the paper's goal is to introduce I-STAR rather than exhaustively benchmark, including at least one additional isotropy-related baseline would significantly strengthen the claim that I-STAR provides a novel capability. This is not fatal—CosReg is the most directly related—but it limits the strength of the comparative claims.

2. **Claims occasionally overreach the fine-tuning scope.** The paper acknowledges in the Limitations (line 208) that the study is limited to fine-tuning, but the Discussion uses general language like "anisotropy is essential for a model's downstream performance" (line 200–201) and the Conclusion says "decreasing isotropy improves downstream model performance" (line 214) without consistently hedging to the fine-tuning context. Since models are not pre-trained from scratch with I-STAR, the broader claims go beyond what the experiments directly support.

3. **Shrinkage matrix update frequency and non-stationarity not discussed.** The paper updates Σ_S after each epoch (line 97), meaning the reference covariance for the isotropy penalty is itself moving during training. This non-stationarity could affect the optimization dynamics, and the paper does not analyze sensitivity to update frequency or whether the moving reference causes training instability.

4. **Rotation invariance of IsoScore$^{\star}$ not discussed.** The original IsoScore reorients data via PCA projection to ensure basis independence (line 52). IsoScore$^{\star}$ (Algorithm 1) omits this step but computes eigenvalues of the covariance matrix, which are inherently rotation-invariant. The paper should clarify this to avoid the impression that a desired property was lost.

### Trivial
None that survive filtering—presentation issues appear to be parser artifacts rather than author errors.

## Nice-to-Haves

- Provide statistical significance tests (paired t-tests or confidence intervals) for the isotropy–performance relationship in Table 1, with correction for multiple comparisons across model–task pairs. This would meaningfully strengthen the central claim.
- Include an ablation on the shrinkage parameter ζ in the main text (not just the appendix) to demonstrate that I-STAR's benefits degrade without shrinkage. The paper mentions a 6% drop (line 97) but defers to the appendix.
- Report the best hyperparameter (λ, ζ) choices per model and task in the main text for reproducibility.
- Extend the intrinsic dimensionality analysis (TwoNN) to at least one additional task beyond SST-2 to demonstrate generality.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Criticism about IsoScore$^{\star}$ not being released or unavailable* — The paper states a pip-installable release is available (line 220). Per hard rules, cited entities are assumed to exist; this criticism is removed.
- *Strength Finder's claim that the paper provides "strong empirical evidence"* — This conflicts with verified weakness #2 (limited statistical rigor); per rules, the weakness wins, and this strength is downgraded.
- *Strength Finder's "comprehensive experimental design with rigorous hyperparameter tuning"* — This is generic; tuning batch size, LR, epochs, λ, ζ and averaging over 5 seeds is standard practice, not exceptional. Moved here as it does not add discriminating value.
- *Harsh critic's request for deriving differentiability vs. non-differentiability proofs from scratch* — The core issue is that the paper overclaims; the fix is clarifying the claim, not a formal proof. The request as stated is disproportionate.
- *Harsh critic's complaint about missing "strong empirical evidence" phrasing* — The phrasing is indeed in the paper at line 200; the criticism is valid (see Major #2). The specific wording complaint is absorbed into the more substantive statistical-rigor weakness.
- *Demands for positive-λ results in table format* — Figure 4 already shows the full λ sweep visually. A separate table would be redundant; this is a nice-to-have at best.

## Novel Insights

The most genuinely novel observation emerging from this review—beyond what the paper itself claims—is the following tension: the paper's core message (anisotropy helps) directly challenges a large body of NLP work, yet the empirical support relies on modest improvements that are not statistically tested. This makes the paper's contribution more fragile than its framing suggests. Simultaneously, the methodological contribution (shrinkage-stabilized isotropy estimation) is clean and likely useful regardless of whether the isotropy–performance relationship holds as broadly as claimed. The review reveals that the paper could be stronger by decoupling these two contributions more explicitly: the stable isotropy measure is a standalone advance, and the empirical finding is a suggestive but not-yet-definitive application of it.

## Suggestions

1. **Clarify the differentiability claim.** Explain specifically what operations in vanilla IsoScore make it non-differentiable in practice (e.g., eigenvector computation for the reorientation step and its associated gradient instabilities), or acknowledge that both methods are differentiable through PCA and reposition the contribution as primarily about *stability* rather than differentiability per se.

2. **Add statistical significance tests** for the main result (Table 1). Report whether the difference between the best negative-λ run and the baseline is significant for each model–task pair at a conventional level, with multiple-comparison correction. This does not require re-running experiments—the 5-seed data already available can be used for t-tests.

3. **Hedge the general claims** in the Discussion and Conclusion to consistently refer to the fine-tuning setting, or add a caveat about the scope. The empirical design supports claims about fine-tuning; statements about "anisotropy being essential" overreach.

4. **Add ablation study on ζ prominently** to the main text to make the case for shrinkage's importance transparent, as the paper itself says it is "crucial" (line 97).

## Score and Decision

**Originality:** Good. IsoScore$^{\star}$ is a novel combination of existing ideas (shrinkage estimation + eigenvalue-based isotropy scoring), and the finding that CosReg operates on the mean rather than covariance is a useful clarification.

**Importance of research question:** High. The role of isotropy in LLM representations is actively debated, and a stable, differentiable measure enables new investigations.

**Claims supported:** Partially. The methodological claims about stability are well-supported. The empirical claim that decreasing isotropy improves performance is suggestive but lacks statistical rigor and is overstated.

**Soundness of experiments:** Moderate. The experimental design is reasonable (3 models × 9 tasks, 5 seeds), but the lack of statistical testing and only one baseline regularizer weaken the empirical conclusions.

**Clarity of writing:** Generally clear. The differentiability claim could be more precise and the hedging could be more consistent.

**Value to the research community:** The stable isotropy measure (IsoScore$^{\star}$) is a practically useful tool. The empirical results, while not definitive, provide a valuable counterpoint to prevailing assumptions and should stimulate further investigation.

I recommend acceptance contingent on the authors addressing the two major weaknesses: clarifying (or correcting) the differentiability claim and adding statistical rigor to the main empirical results. The paper's value does not hinge on rejecting all prior work—IsoScore$^{\star}$ and I-STAR can stand on their methodological merits alone.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>