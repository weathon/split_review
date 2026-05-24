## Summary

This paper addresses Variable Subset Forecasting (VSF), where test-time observations contain only a small subset of training variables. It proposes SRDI, a diffusion-based imputation framework that: (1) decomposes time series into "invariant" (stable inter-series correlations) and "variant" (dynamic) patterns via a divide-conquer denoising process, and (2) uses a meta-learning paradigm treating each time window as a task to handle intra-series distribution shift. Experiments on four datasets with four forecasting backbones show consistent improvements over the no-imputation baseline and often exceed the Oracle (full-data) setting.

## Strengths

- **Clear problem taxonomy and targeted design.** The paper identifies two distinct types of distribution shift in VSF (inter-series and intra-series) and designs separate modules targeting each. This decomposition of the problem is well-motivated and goes beyond prior work that treats distribution shift monolithically.

- **Strong empirical results against the Partial (no-imputation) baseline.** Table 1 shows SRDI improves average MAE by 20–33% over the Partial setting across four datasets, using four different forecasting backbones. These improvements are consistent and the comparison is straightforward: without any imputation, forecasting on a 15% subset performs poorly, and SRDI substantially recovers performance.

- **Comprehensive imputation baseline comparison.** The paper compares against 12 imputation methods spanning statistical (MICE, Gaussian Copula), GAN-based (SSGAN), matrix-factorization (TRMF), and diffusion-based (CSDI, PRISTI) approaches. SRDI achieves the lowest MAE/RMSE on the reported radar charts (ECG5000 and METR-LA). The breadth of baselines substantiates the claim of consistent superiority over existing imputation techniques.

- **Ablation study isolating both components.** The ablation on ECG5000 (Figure 4) shows that removing the invariant-variant dispatcher (SRDI-IV → MAE 3.64 vs 3.28) and removing the meta-learning structure (SRDI-M → MAE 3.52) both degrade performance, providing evidence that each module contributes.

- **First diffusion-based method specifically designed for VSF.** While CSDI and PRISTI could be adapted to VSF by conditioning on observed subsets, the paper formulates the problem as a conditional diffusion process over missing variables and designs the denoising function with explicit shift-handling mechanisms, which is a nontrivial adaptation.

## Weaknesses

### Major

- **The beating-Oracle result lacks analysis and undermines evaluation credibility.** In Table 1, SRDI frequently outperforms the Oracle (full-data) setting on the same forecasting backbone (e.g., MTGNN on METR-LA: SRDI MAE 3.43 vs Oracle 3.49; MTGNN on SOLAR: 2.65 vs 2.94). The paper attributes this to "successful handling of the interference caused by distribution shift" (lines 263–264) without any supporting analysis. This explanation is inadequate because: (a) the Oracle model trained on the same data should be equally exposed to distribution shift; (b) if the Oracle is trained independently without the benefit of joint meta-training with the imputation model, the comparison is confounded. The more likely explanations (the imputation model provides a regularization/denoising effect, or the meta-learning pipeline offers test-time adaptation unavailable to Oracle) are not discussed, let alone tested. This is the most serious weakness — it raises questions about whether the evaluation protocol is fair and whether the primary empirical claim is sound.

- **The invariant-variant decomposition is validated circularly.** The dispatcher (Section 4.2.1) explicitly regularizes the invariant pattern's correlation matrix to be stable across time via Eq. 6: $\mathcal{L}_m^{\text{disp}} = \sum_{t=1}^{T-1} \|\mathbf{C}_{t+1} - \mathbf{C}_t\|_2^2$. The visualization (Figure 5) then shows that the invariant pattern fluctuates less — which is exactly what the regularization enforces. This is circular validation, not evidence that the decomposition isolates meaningful "stable inter-series correlations" as opposed to simply subtracting low-frequency signal content. The ablation (SRDI-V, which uses only invariant patterns) underperforms the full model, but this only shows that discarding the variant component hurts — it does not validate that the decomposition mechanism correctly identifies sources of inter-series shift. A proper controlled experiment (e.g., artificially shifting correlation structures at test time and verifying that the invariant pattern remains stable) is absent.

- **Ablation study is limited to a single dataset.** The entire ablation analysis (Figure 4, Section 6.3) is conducted only on ECG5000. The paper states "Due to space constraints, we present only the results for the ECG5000 dataset here" (line 307). While space is a real constraint, the central claims about the contribution of each module cannot be assessed across domains without replication on at least one additional dataset (e.g., METR-LA, where the main results show the largest improvements).

- **No sensitivity analysis on the subset size.** All main experiments use S=15% of variables. The paper does not report performance for any other subset size (e.g., 5%, 25%, 50%). Since the core claim is about handling missing variables at test time, the method's behavior across different missingness levels is critical for understanding its practical range and robustness.

### Minor

- **The meta-learning contribution is not clearly disentangled from simple fine-tuning.** The ablation SRDI-M removes the meta-learning structure and adaption phase. However, a more informative comparison would be against a version that simply fine-tunes the pretrained diffusion model on the test window using the same pseudo-missing procedure, without the meta-training outer loop. The current ablation conflates the meta-learning paradigm with the adaptation procedure itself.

- **Problem formulation inconsistency.** Equation 1 treats the forecasting model $\mathcal{F}_\Theta$ as fixed (minimization is over $\Phi$ only), but Algorithm 1 jointly trains $\Theta$ and $\Phi$ in the outer loop. This inconsistency is not addressed.

- **Imputation comparison reported only on 2 of 4 datasets with 1 backbone.** The main text shows imputation baseline comparisons (Figures 2–3) only for ECG5000 and METR-LA with MTGNN. The paper references Appendix B.1 for full results, but the main evidence for the imputation superiority claim is incomplete.

- **Large standard deviations relative to reported improvements.** In Table 1, standard deviations frequently overlap between SRDI and Oracle (e.g., MTGNN on TRAFFIC: SRDI MAE 11.55±1.17 vs Oracle 11.45±0.57). Statistical significance is not reported for any comparison.

### Trivial

- The correlation matrix loss (Eq. 6) refers to the appendix for calculation details, which were stripped by the parser. A brief explanation in the main text would improve readability.

## Nice-to-Haves

- Sensitivity analysis for different subset sizes (5%, 25%, 50%).
- Statistical significance tests for the main results.
- Runtime and parameter count comparison against baselines, to inform practitioners about the cost of the meta-learning pipeline.
- Comparison against simple imputation methods (mean, linear interpolation, KNN) as practical lower bounds.

## Removed Points

*These points are flagged to be removed, treat them with caution:*
- Criticisms about missing appendix content, missing proofs, or absent references — these sections were stripped by the PDF parser and exist in the original submission.
- Criticisms about formatting, typos, or grammar — these are parser artifacts, not author errors.
- Criticisms that demand the paper address problems outside its stated scope (e.g., that the method should handle entirely new missing patterns not seen during training) — the paper scopes its contribution to VSF with the stated setup.
- The claim that "the reader is referred to an appendix no longer available" — the appendix was removed by the PDF extraction process.
- Criticisms about missing related works — cannot be verified without external sources.
- The strength that "visualization validates invariant-variant pattern separation" — this is weakened by the circularity issue noted above; it is kept only as an observation about what the paper reports.
- The strength that "comprehensive comparison against 12 imputation baselines" — valid but should be contextualized by the limited reporting in the main text; retained as a strength with this caveat.
- The suggestion that "the correlation matrix loss (Equation 6) is not clearly explained" is moved to Trivial.
- The concern that "the dispatcher uses subtraction (variant = input - invariant) which is a strong inductive bias not discussed" — this is an architectural choice common in decomposition methods; calling it an unexamined bias is overstated.

## Novel Insights

None beyond the paper's own contributions. The two-reviewer input did not surface a perspective on the paper that is not already present in the authors' framing or in the weaknesses above. The "beating-Oracle as denoising regularization" hypothesis — which the paper does not explore — is the closest thing to a novel lens, but it remains speculative.

## Suggestions

1. **Analyze the beating-Oracle result.** Perform a controlled experiment comparing SRDI against an Oracle that also receives test-time adaptation (e.g., fine-tuning the Oracle model on the available subset). Report whether the improvement is driven by the imputation model's denoising effect, the meta-learning adaptation, or both. If the result stands, provide a rigorous explanation rather than a hand-wavy attribution.

2. **Validate the invariant-variant decomposition with a synthetic experiment.** Create data where inter-series correlations are known to change at test time (e.g., periodic switching between two correlation matrices). Show that the invariant pattern remains stable, the variant pattern captures the change, and SRDI degrades less than a non-decomposed baseline.

3. **Extend the ablation study to at least one more dataset** (e.g., METR-LA). The ablation on ECG5000 alone is insufficient to support the claim that each module is necessary across domains.

4. **Report sensitivity to subset size.** Show how performance changes at S=5%, 25%, 50% to establish the method's practical operating range.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Three queries on "time series imputation with diffusion models variable subset forecasting" across score bands.

| Anchor | Avg Score | Round | Band | Comparison |
|--------|-----------|-------|------|------------|
| uAp7YdKrlx (RBF imputation) | 3.00 | 1 | Weak | Weaker than SRDI — simple method, no shift handling |
| zB6uMznFuZ (TimeAutoDiff) | 3.00 | 1 | Weak | Weaker than SRDI — latent diffusion for generation, not VSF |
| 4u0ruVk749 (DFITE) | 3.00 | 1 | Weak | Weaker — different problem (treatment effect) |
| dUCWpEUrWo (AGG) | 3.40 | 1 | Weak | Weaker than SRDI — transductive graph generation, less structured |
| FvBTy5Dz9C (TimeDiT) | 5.25 | 1 | Middle | Comparable — SRDI has better ablation but worse unexplained Oracle result |
| gVbPYihQag (StochDiff) | 5.00 | 1 | Middle | SRDI is slightly stronger — StochDiff has clear mathematical errors |
| PyyoSwPaSa (MissDiff) | 5.75 | 1 | Middle | MissDiff has stronger theory but comparable evaluation gaps |
| mmjnr0G8ZY (mr-Diff) | 6.50 | 1 | Middle | Stronger than SRDI — accepted paper with fewer structural concerns |
| nHESwXvxWK (MC-guided diffusion) | 8.50 | 1 | Strong | Much stronger — oral paper with theoretical guarantees |
| 6EUtjXAvmj (Variational DPS) | 8.00 | 1 | Strong | Much stronger — oral paper with rigorous evaluation |

**Round-1 bracket:** The paper sits between 4.0 and 6.5 — clearly above the weak anchors (~3.0-3.4) but well below the strong anchors (~8.0+).

**Round 2 (Narrowing):** Two queries inside the bracket on "distribution shift robust time series forecasting imputation missing variables."

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| JHE4w8q2G2 (Merlin) | 4.50 | 2 | Weaker — Merlin had training fairness concerns; SRDI has stronger architecture |
| UCeZMMyjm2 (TSRM) | 4.50 | 2 | Weaker — representation learning without explicit shift handling |
| jo36Mzwuvf (GP corruption-resilience) | 4.75 | 2 | Weaker — GP-based denoising, less targeted to VSF |
| qVyjN01x4P (TFPS) | 5.40 | 2 | Comparable — TFPS has similar evaluation gaps but different problem setting |
| K1mcPiDdOJ (Conditional IB) | 6.50 | 2 | Stronger — accepted paper with strong theoretical grounding |
| GsR3zRCRX5 (SBI under missing data) | 6.17 | 2 | Stronger — accepted paper with cleaner evaluation |
| zwMfg9PfPs (Out-of-variable) | 6.75 | 2 | Stronger — accepted paper with tight experimental design |
| kat8uANDlU (HGNN imputation) | 5.60 | 2 | Comparable — similar evaluation rigor, different architecture |

The round-2 narrowing confirms that SRDI sits around the 5.0 mark. It is stronger than Merlin (4.50) which had comparably serious evaluation issues, comparable to TFPS (5.40) and TimeDiT (5.25), but clearly weaker than mr-Diff (6.50), Conditional IB (6.50), and other accepted papers at 6+. The central unaddressed issue (unexplained beating-Oracle result) and the circular validation of the core decomposition mechanism make the paper weaker than those accepted anchors.

**Final Score:** 5.0 — The paper addresses a practical and well-motivated problem with a technically detailed solution, but the evaluation has structural gaps that undermine the central claims in their current form. The beating-Oracle result requires proper analysis, the invariant-variant decomposition needs non-circular validation, and the experimental scope needs broadening.

**MY FINAL SCORE:** <score>5.0</score>
**MY FINAL DECISION:** <decision>Reject</decision>