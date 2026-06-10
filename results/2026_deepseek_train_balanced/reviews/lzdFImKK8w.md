Here is my final consolidated review:

## Summary
This paper proposes Boltzmann Alignment, a method that derives the change in binding free energy (ΔΔG) upon mutation from inverse folding model log-likelihoods by explicitly modeling both bound and unbound protein states through the Boltzmann distribution and thermodynamic cycle. The unsupervised variant (BA-Cycle) computes ΔΔG from a pre-trained ProteinMPNN, while the supervised variant (BA-DDG) fine-tunes the model on labeled data. On SKEMPI v2, BA-DDG achieves Spearman 0.5134 (vs. prior SoTA 0.4324) and BA-Cycle achieves 0.3201 (vs. prior best ML method 0.2632), with additional applications to binding energy prediction, docking selection, and antibody optimization.

## Strengths
- **Principled derivation connecting ΔΔG to inverse folding log-likelihoods**: The derivation in §3.1 (Eq. 1–7) starts from the Boltzmann distribution, uses Bayes' theorem to avoid estimating intractable conformational probabilities, and expresses ΔΔG as a ratio of sequence likelihood ratios. This provides formal thermodynamic justification for a correlation that prior work only observed empirically.
- **Explicit modeling of the unbound state (thermodynamic cycle) which prior inverse folding methods neglect**: Previous inverse-folding-based methods only consider the bound-state probability p(S_AB|X_bnd). The paper models the unbound state as two independent chains (Eq. 9), introducing a physically motivated inductive bias. The ablation in Table 3 shows BA-Cycle (with cycle) achieves Per-Structure Spearman 0.3201 vs. ProteinMPNN's 0.2741 and ESM-IF's 0.2019 (both without the cycle), and Overall Spearman 0.4097 vs. 0.3112 and 0.2806.
- **State-of-the-art results across all 7 metrics on SKEMPI v2**: BA-DDG leads on every metric (Per-Structure Spearman 0.5134 vs. prior best 0.4324, Overall Pearson 0.7118 vs. 0.6772) and substantially surpasses prior methods. The ablation in Table 4 confirms that Boltzmann supervision drives the gain over SFT (Per-Structure Spearman 0.5134 vs. 0.4769) and DPO (0.3913) under identical settings.
- **Robust performance with AlphaFold3-predicted structures nearly matching crystal structure results**: Table 5 shows that using predicted structures yields Per-Structure Pearson 0.8017 vs. 0.8057 with crystal structures, a minimal drop that demonstrates practical utility when crystal structures are unavailable.

## Weaknesses

### Fatal
None.

### Major
- **Sign of the KL divergence term in the supervised loss (Eq. 8) appears to contradict the stated objective**: The loss is written as L = ||ΔΔG − ΔΔĜ|| − β·D_KL(p_θ || p_ref). The paper states this term is a "distributional penalty" to "maintain the distribution of the original pre-trained model." However, with a minus sign in a minimization objective, this term is maximized when KL is large — the optimization would actively push p_θ *away* from p_ref, the opposite of what is claimed. Standard regularized objectives have the form: minimize regression_error + β·KL (KL enters with a plus sign). This is likely a typo in the equation — if the actual implementation uses +β·KL, the paper needs to state this. If the minus sign reflects the implementation, the method does not work as described. The unsupervised BA-Cycle is unaffected, but this issue undermines the stated mechanism of the supervised method.

- **No uncertainty or variance reported for any result**: All tables report "mean results of 3-fold cross-validation" without standard deviations, per-fold values, or confidence intervals. Given that several differences between methods are modest (e.g., Per-Structure Spearman 0.4769 for SFT vs. 0.5134 for Boltzmann in Table 4 — a gap of ~0.037), the reader cannot assess whether the claimed improvements are statistically reliable or within the noise of the 3-fold splits. For a paper claiming "significant" superiority, this is a notable gap.

### Minor
- **"SoTA" claim for the unsupervised method needs careful scoping**: The abstract foregrounds the comparison against RDE-Linear's Spearman 0.2632, but FoldX (also unsupervised, listed in Table 1) achieves Per-Structure Spearman 0.3693 vs. BA-Cycle's 0.3201, and Per-Structure Pearson 0.3789 vs. 0.3722. BA-Cycle beats FoldX on overall metrics (Overall Spearman 0.4097 vs. 0.4071), but the abstract should qualify that traditional energy functions remain competitive on per-structure metrics. The paper's body text ("comparable performance to empirical energy functions") is appropriately scoped; the abstract and conclusion should be as well.

- **Antibody optimization experiment (Table 6) is too small to support the strong conclusion drawn**: The paper concludes that "fine-tuning for ΔΔG prediction can enhance the design of more effective antibody sequences" based on 5 mutations. While averages favor BA-DDG, per-mutation results are mixed — ProteinMPNN wins on 2/5 mutations for perplexity (AH53F, NH57L) and 1/5 for preference (NH57L). With only n=5, the results are suggestive but do not support the definitive conclusion. The TH31W mutation alone drives much of the average improvement in perplexity (6.018→1.979).

- **"Minimized" RMSE/MAE metrics are not explained**: The evaluation includes "minimized RMSE" and "minimized MAE" (line 230) without stating whether a linear transformation is applied to predictions before computing these errors. If predictions are on an arbitrary scale (as is typical when k_B T is a learnable or scaling parameter), this is appropriate but must be explicitly disclosed for reproducibility and fair comparison.

- **ΔG prediction application (§4.3) acknowledges incomplete justification**: The paper states "we lack a comprehensive explanation for canceling out p(X_bnd) and p(X_unbnd) in Eq. 5" and presents ΔG prediction results without comparison to clear baselines, making it difficult to interpret whether the Spearman 0.385 is strong relative to alternatives.

### Trivial
- The paper replaces a partition-function ratio over conformational ensembles with a single-structure likelihood ratio — a coarse approximation that is standard in the field but should be more prominently caveated in the derivation.

## Nice-to-Haves
- Reporting per-fold results or standard deviations for Tables 1 and 4 would substantially strengthen the paper.
- Clarify whether k_B T is set to 1, a fixed physical constant, or absorbed as a scaling factor in the unsupervised BA-Cycle setting (Eq. 9).
- A more systematic analysis of when the fixed-backbone approximation causes the largest errors would be valuable.

## Removed Points
These points are flagged to be removed; treat them with caution:
- **Missing hyperparameters (β, learning rate, optimizer, epochs)**: Removed per instructions — these details may exist in the appendix, which is stripped by the parser. The paper references an appendix (§App. DPO).
- **SFT baseline ambiguous**: The paper states "training and inference settings are the same as in the main results" (line 330), which adequately clarifies the comparison.
- **Reviewer claim that results would favor ProteinMPNN without TH31W**: Recalculating averages excluding TH31W shows BA-DDG still has better averages on both perplexity (1.162 vs. 1.499) and preference (49.47% vs. 47.08%). The evidence is mixed but not inverted.
- **"Physics framing overselling"**: This is a matter of rhetorical taste rather than a verifiable weakness.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Fix the sign in Eq. 8** — change −β·KL to +β·KL if that reflects the implementation. Confirm the corrected loss in the main text and clarify the analogy to standard regularized objectives.
2. **Add standard deviations or per-fold results** to at least Table 1 and Table 4 to enable assessment of statistical reliability.
3. **Qualify the unsupervised SoTA claim** in the abstract to acknowledge that FoldX is competitive on per-structure metrics, or reframe the claim around ML-based unsupervised methods specifically.
4. **Either expand the antibody optimization experiment** (more mutations) or soften the conclusion to match the limited evidence.
5. **Explicitly describe the "minimized" RMSE/MAE procedure** — state whether a linear calibration is applied and how.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>