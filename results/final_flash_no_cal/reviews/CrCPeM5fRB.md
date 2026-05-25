## Summary

The paper proposes the Signal Dice Similarity Coefficient (SDSC), a structure-aware metric and differentiable loss for time-series self-supervised representation learning. SDSC extends the Dice Similarity Coefficient from segmentation to continuous signed signals by measuring pointwise sign agreement and magnitude overlap. The authors replace only the reconstruction loss (MSE) in SimMTM with SDSC (or a hybrid SDSC+MSE loss) while keeping the contrastive objective fixed, and evaluate on forecasting and classification benchmarks. The core claim is that structure-aware reconstruction produces representations with better semantic fidelity than amplitude-focused MSE, while achieving comparable or better downstream performance.

## Strengths

- **SDSC demonstrably separates signals that MSE treats as equivalent (Table 1, Figure 1).** An inverted signal, a zero constant, and a 2×-scaled signal all yield nearly identical MSE values (0.020–0.500) but sharply different SDSC scores (0.000–0.667). This provides direct evidence that SDSC captures polarity and structural mismatches that distance-based metrics miss.

- **SDSC-based pre-training improves frozen-encoder in-domain classification (Table 5).** SDSC achieves 76.38% accuracy vs. MSE's 75.45% (+0.93%), with consistent gains in precision, recall, and F1. This is the clearest empirical signal that optimising structural fidelity yields more linearly separable representations.

- **The hybrid loss (SDSC+MSE) achieves the best overall reconstruction trade-off (Table 2).** On forecasting datasets, Hybrid attains the lowest MSE (0.4783) and the highest SDSC (0.7841), outperforming both pure MSE and pure SDSC on both metrics. This demonstrates that the two objectives are complementary rather than competing.

- **SDSC-based models match MSE in downstream forecasting despite higher reconstruction MSE (Table 4).** Average forecasting MSE for SDSC (0.294) and Hybrid (0.294) is essentially identical to MSE (0.295). This supports the claim that beyond a certain threshold, further MSE minimization provides diminishing returns and that structural alignment is sufficient for good forecasting representations.

- **SDSC is linear-time, alignment-free, and can be used as a differentiable loss (Sections 2.1, 3.3).** Unlike alignment-based objectives (e.g., SoftDTW with quadratic complexity), SDSC is O(n) and the smooth Heaviside approximation (Equation 7) makes it compatible with gradient-based optimization.

- **Controlled experimental design isolates the effect of the reconstruction loss (Section 4).** Only the reconstruction objective changes across experiments; the contrastive loss (InfoNCE) and backbone (SimMTM) are fixed. This ensures that observed differences are attributable to the reconstruction loss.

- **SDSC-based training yields more consistent structural alignment at the same MSE level (Figure 3, Table 3).** At a fixed MSE of 1.5±ε, the SDSC-trained model shows higher mean SDSC and lower variance (std 0.0249) than the MSE-trained model (std 0.0280).

## Weaknesses

### Fatal
None.

### Major

- **Empirical improvements are concentrated in one setting and marginal overall.** The only scenario where SDSC shows a non-trivial advantage is frozen-encoder in-domain classification (+0.93% accuracy, Table 5). In forecasting (Table 4), all methods cluster within 0.001–0.016 MSE of each other — effectively identical. In fine-tuning classification (Table 6), SDSC underperforms MSE in cross-domain settings (83.27% vs. 83.74% accuracy) and is comparable in-domain (79.60% vs. 79.66%). For a paper whose central thesis is that a different reconstruction loss produces better representations, the downstream evidence is too thin to be fully convincing.

- **No statistical significance assessment.** The paper states "fixed random seeds across all runs to ensure reproducibility" (line 147), which indicates single-seed experiments. Given that the reported differences are tiny (e.g., 0.001 MSE; 0.93% accuracy), it is impossible to tell whether these reflect genuine systematic effects or random variation. Multiple trials with confidence intervals are standard practice when claiming improvements of this magnitude, and their absence undermines confidence in the results.

### Minor

- **Single backbone limits generalization claims.** All experiments use only SimMTM. While this is a deliberate choice to isolate the reconstruction loss, the title and framing reference "Semantic Signal Representation Learning" broadly. Without evidence from at least one additional framework (e.g., TI-MAE, TS2Vec), it is unclear whether the findings transfer. The authors acknowledge this as future work (line 273) but the scope of the claims outruns the evidence.

- **Questionable inclusion of poorly-suited baselines.** SoftDTW, PCC, and SI-SNR are included as reconstruction objectives but are not designed for pointwise signal recovery in SSL. Unsurprisingly, they produce very poor reconstruction errors (Table 2: SI-SNR MSE = 34.9 on forecasting data vs. MSE's 0.49). The paper's main comparison is MSE vs. SDSC, so these baselines are largely irrelevant; their inclusion inflates SDSC's relative standing without providing a meaningful comparison. Omitting them or replacing them with natural alternatives (e.g., ℓ₁ loss, cosine similarity) would make for a cleaner evaluation.

- **Unsupported interpretive claim about why MSE "works."** The introduction states that "MSE-based models achieve competitive results not due to accurate semantic preservation but due to incidental alignment with signal structure" (line 22). This is a strong causal claim that the experiments do not directly test. SDSC and MSE produce similar downstream performance, but this does not prove that MSE succeeds through incidental alignment — it could simply mean both losses learn similar features on these datasets. The paper would benefit from representation-level analysis (e.g., linear probing, feature visualization) to substantiate this interpretation.

### Trivial

- **Heaviside at zero is not specified.** The discrete SDSC approximation uses H(S(s)) where H is the Heaviside step function. Common conventions define H(0) as 0, 0.5, or 1; the paper should state which is used and justify it, as it affects the gradient when signals cross zero.

- **No sensitivity analysis for the sharpness parameter α.** The paper sets α=10 (Appendix A.3) but provides no ablation showing how varying α affects training stability, convergence, or downstream performance.

- **No wall-clock runtime comparison.** The paper claims linear complexity but does not report actual training time per step for SDSC vs. MSE vs. SoftDTW, which would substantiate the efficiency claim.

## Nice-to-Haves

- Direct representation analysis: t-SNE plots of learned embeddings, linear probing experiments, or a synthetic task where semantic structure (phase vs. amplitude) is explicitly defined would strengthen the claim that SDSC preserves semantic information differently from MSE.
- Ablation on the hybrid loss weighting (fixed λ vs. uncertainty-based weighting) to understand when the added complexity of uncertainty tuning is beneficial.
- A per-dataset breakdown of the frozen-encoder classification results to verify the claim that SDSC "consistently" outperforms MSE across individual datasets, and to analyse which signal types (e.g., gesture vs. epilepsy) benefit most.

## Removed Points

These points from the inputs are excluded with justification:

- **"Overclaiming relative to evidence" (Harsh Critic, point 5):** On re-reading, the paper's language is appropriately measured ("Although the improvements are moderate," "comparable or improved performance," "position SDSC as a promising metric"). The claim that MSE may "overestimate reconstruction quality" is directly supported by the Table 1 / Figure 1 analysis. This criticism is not consistent with the paper's actual tone and has been removed.
- **"Weakness 2 in Harsh Critic about 'baselines that stack the deck':** Retained in weakened form (see Minor weaknesses above). The original framing as a deliberate deck-stacking tactic is too strong; the baselines are supplementary to the main MSE comparison, and the paper acknowledges SI-SNR convergence issues. However, their inclusion is still questionable and has been kept as a Minor weakness.
- **Strength Finder — generic/superficial strengths:** None found; all listed strengths are concrete and anchored in specific tables or figures. All kept.

## Novel Insights

The main insight from the review process is that SDSC's value may be more as a complementary diagnostic metric and a tool for understanding the structure-amplitude trade-off in reconstruction losses than as a drop-in replacement that will yield large accuracy gains. The weak correlation between MSE and SDSC during training (Pearson –0.324, Figure 3) and the fact that the hybrid loss consistently balances both metrics suggest that the community might benefit from reporting both amplitude and structure metrics rather than defaulting to MSE alone. The pattern across tables — comparable forecasting, small frozen gains, erased fine-tuning advantage — points to an interpretation worth spelling out: SDSC may primarily affect the linear separability of pretrained features rather than the quality of features accessible through full fine-tuning.

## Suggestions

1. **Add multi-seed experiments** with confidence intervals, at least for the central comparisons (Tables 4, 5, 6). This is the single most important improvement, as the current margins are too small to assess without error bars.
2. **Include at least one additional SSL backbone** (TI-MAE or TS2Vec) to demonstrate that the findings are not specific to SimMTM's architecture. The paper already cites compute constraints as a reason not to do this, even a limited replication on one dataset would substantially strengthen the claims.
3. **Remove or replace SoftDTW/PCC/SI-SNR baselines** from the main tables, or add simpler baselines such as ℓ₁ loss and cosine similarity. Alternatively, clearly relegate these to an appendix and explicitly note they are included for completeness rather than as competitive baselines.
4. **Perform a simple ablation on α** (e.g., α ∈ {1, 5, 10, 20}) on one dataset and report the effect on training stability and downstream accuracy.
5. **Add a wall-clock timing table** comparing SDSC, MSE, and SoftDTW per-iteration cost on a fixed input size to substantiate the linear-complexity claim.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Weak Accept</decision>