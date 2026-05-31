Now I have sufficient calibration data. Let me construct the final review.

## Summary

Pi-CCA proposes a replay-free continual learning framework for vision-language models that directly preserves the canonical correlation structure (spectrum and subspaces) of cross-modal alignment via a compact sketched certificate, rather than relying on proxy signals like logit distillation or similarity matching. The method achieves SOTA results among replay-free methods across four VL-CL benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL), including surpassing a synthetic-replay method on retrieval.

## Strengths

1. **Principled and novel formulation.** The idea of preserving the CCA invariants (canonical correlations and subspaces) rather than proxy signals is conceptually clean and well-motivated. The use of randomized sketches to keep the certificate constant-size ($h \times k$ rather than $d_v \times d_t$) is a practical touch that makes the approach implementable.

2. **Broad and competitive empirical results.** Tables 1 and 2 show Pi-CCA achieving the top replay-free results across all four tracks: MTIL (Avg 76.8, Last 75.5), X-TAIL (Avg 68.1), VLCL (I2T R@1 48.6±1.0), and ConStruct-VL (FA 75.2±1.3, AF 2.7±0.2). It even beats the synthetic-replay method GIFT on retrieval. These results are reported with standard deviations for VLCL and ConStruct-VL, and the method outperforms a strong set of recent baselines.

3. **Ablation study (Table 3) cleanly validates the design.** Removing either the spectral term ($\lambda_1=0$) or the subspace term ($\lambda_2=0$) causes the largest drops (MTIL Avg -2.5 and -2.2 respectively, VLCL R@1 -2.3 and -2.7), confirming that both components are necessary. Disabling prompt invariance, certificate EMA, and covariance EMA all degrade performance in sensible ways. This systematic ablation substantiates the architecture.

4. **Pareto analysis of certificate capacity (Figure 2) is informative.** The sweep over $k \in \{16,\dots,128\}$ and $h \in \{128,\dots,384\}$ reveals a broad Pareto ridge near $(k,h)=(64,256)$, providing practical guidance for deployment. The fact that performance is robust over a range of capacities rather than a single spike supports the "small yet sufficient" claim.

5. **Robustness analysis.** Task-order sensitivity over 20 random orders (Figure 5) shows narrow IQRs, demonstrating the method does not rely on a lucky sequence. Prompt invariance stress curves (Figure 4) show tangible benefits at high perturbation strengths.

## Weaknesses

### Fatal

None.

### Major

1. **Figure 3 reports implausibly perfect correlations that undermine its evidential value.** The paper reports Pearson $r = 1.00$ and Spearman $\rho = 1.00$ for three of four panels ($r=0.99$ for the fourth). These values imply every data point lies exactly on the regression line with perfect monotonic ordering. The text simultaneously claims "realistic scatter" (line 245). The sweep covers multiple heterogeneous hyperparameters (certificate size, EMA rates, invariance strength, whitening, pairing, LoRA capacity, LR, sketch type), so measurement noise and stochasticity should produce non-trivial scatter. The number of data points and raw values are not stated. Since this figure is presented as direct evidence that "preserving CCA geometry … predicts retention," the perfect correlations raise legitimate concerns about the analysis. This does not invalidate the method (Tables 1–2 and the ablation are independent evidence), but it damages the paper's strongest mechanistic claim and must be corrected — either by replacing the figure with properly documented scatter, explaining why the relationship is definitional rather than empirical, or by honestly acknowledging the limited number of configurations.

2. **Variance is not reported for the classification tracks (MTIL, X-TAIL).** Table 2 (retrieval/ConStruct-VL) includes $\pm$std, but Table 1 (MTIL/X-TAIL) reports only point estimates. The gains over the next-best methods are modest (MTIL Avg +1.6 p.p., X-TAIL Avg +0.7 p.p.), and without variance or confidence intervals the reader cannot assess whether these differences are statistically significant. This is especially important given the narrow margins.

### Minor

1. **Several experimental specifications are absent from the main text.** The backbone model (e.g., CLIP ViT-B/16?) and LoRA rank are not stated in §4.1 or the main results section. The batch size for the main results (as opposed to the Pareto analysis where $B=1024$ is given) is not reported. While the reproducibility statement says these appear in Appendix §A.2, the main text should at least identify the backbone and LoRA rank for basic transparency.

2. **The prompt-invariance "practical operating range $s \leq 0.6$" claim is not backed by a specific threshold analysis.** The curves in Figure 4 show a gradual degradation, and the $s \leq 0.6$ claim in line 253 ("performance remains close to nominal with invariance") is stated without a formal criterion. This is a minor presentation issue.

3. **Figure 3 does not state the number of configurations plotted.** Given the central role of this figure in the mechanistic claim, the number of data points, hyperparameter settings, and whether multiple seeds are shown should be explicit.

### Trivial

None.

## Nice-to-Haves

- A sensitivity analysis for the two EMA parameters ($\beta$ for covariance EMAs, $\alpha$ for the certificate refresh rate) would sharpen practical guidance, though the paper notes these are in Appendix §A.3.
- Additional clarity on how the random orthonormal sketches $R_v, R_t$ are constructed (fixed once? resampled?) and whether gradients flow through the EMA covariance updates or only through current mini-batch estimates would help reproducibility.

## Removed Points

- **Criticism about missing related work.** Removed per instructions (cannot verify what is missing without external sources).
- **Criticism that questions the release status of code/models/references.** Removed per instructions (all cited entities are assumed to exist).
- **Formatting/typo/style nitpicks.** Removed per instructions (parser artifacts).
- **Criticism about missing appendix content.** Removed per instructions (appendix content exists in original submission but is stripped by the parser).
- **Strength from Strength Finder about Figure 3's correlations.** Removed because this strength conflicts with a verified weakness (the correlations are implausibly perfect, and the weakness takes priority per instructions).
- **Strength Finder generic strengths about "addressing an important problem."** Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface any novel interpretation that the paper itself does not articulate.

## Suggestions

1. **Fix Figure 3.** Either (a) replace it with a properly scattered plot showing 10–20+ configurations with reported confidence intervals on the correlations, or (b) if the perfect correlations arise from a small number of points or a definitional relationship, acknowledge this explicitly and temper the claim from "strong positive linear correlation" to "consistent trend." Without this correction, the paper's central mechanistic claim is weakened.
2. **Add variance bars to Table 1** (MTIL, X-TAIL) to enable readers to assess the reliability of the reported gains, especially given the modest margins.
3. **State the backbone and LoRA rank** explicitly in §4.1 rather than deferring entirely to the appendix.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/.../mDuton6Tg7.md` | 3.00 | R1 (weak) | Weaker motivated/poorer results than Pi-CCA |
| `/home/.../fQTw3w3hnA.md` | 3.00 | R1 (weak) | Weaker method/evaluation than Pi-CCA |
| `/home/.../HeGMugkCOH.md` | 3.00 | R1 (weak) | Test-time adaptation, different problem; less comprehensive |
| `/home/.../wowBEOijWh.md` | 3.00 | R1 (weak) | Narrower VQA-only scope than Pi-CCA |
| `/home/.../HN18kuyf4o.md` | 4.00 | R1 (mid) | Uses costly generative replay; less novel; Pi-CCA is stronger |
| `/home/.../xp7wDU9JBW.md` | 5.00 | R1 (mid) | Graph-memory approach; comparable novelty; Pi-CCA similarly strong |
| `/home/.../rMHZfCznhZ.md` | 6.00 | R1 (mid) | Uses exemplar buffers (not replay-free); Pi-CCA on harder setting |
| `/home/.../Hc71kKCEFG.md` | 4.80 | R1 (mid) | Niche unlabeled-data setting; Pi-CCA has broader scope |
| `/home/.../tucuU4sQ3s.md` | 5.50 | R2 | NuSA-CL (null-space method); comparable motivation; Pi-CCA has broader evaluation |
| `/home/.../T3Vc5fkTzV.md` | 5.50 | R2 | KeepLoRA (subspace in parameter space); comparable quality; Pi-CCA evaluates retrieval too |
| `/home/.../eiTy6AYeQi.md` | 6.00 | R2 | Compo-ReAlign (compositional alignment); no suspicious evidence issues |
| `/home/.../5xOh6xNY8z.md` | 4.67 | R2 | MePo (meta-learning); less direct empirical validation than Pi-CCA |
| `/home/.../NE2yIxdo1w.md` | 5.50 | R2 | Theoretical NTK analysis; different genre, not directly comparable |

**Round-1 bracket:** The paper is clearly above the weak-band anchors (3.00) which are papers with serious flaws, and clearly below the strong-band anchors (8.00) which are outstanding papers in different areas. Initial bracket: [3.5, 7.5].

**Round-2 narrowing:** Within the bracket, Pi-CCA is comparable to or slightly stronger than the 5.00–5.50 anchors (CoMem, NuSA-CL, KeepLoRA) due to broader evaluation across retrieval + classification and a genuinely novel geometry-preservation formulation. It is slightly weaker than the 6.00 anchors (Compo-ReAlign, RLAP-CLIP) because the Figure 3 issue damages a supporting claim in a way those papers do not suffer from. The Figure 3 problem is significant but fixable — it does not invalidate the method or its SOTA results, which are verified independently.

**Final score: 5.5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>