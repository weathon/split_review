## Summary
ProteinVista is a 3D CNN pre-trained on ~500K AlphaFold-2-predicted structures that represents proteins as full-atom 5-channel voxel grids (C, N, O, S, P) at 1.0 Å resolution. It employs a contrastive pre-training objective aligning its 3D embeddings to ESM-2 sequence embeddings, uses random 90°-rotation/mirror augmentations for approximate rotational robustness, and achieves state-of-the-art performance on enzyme-substrate (ESP), transporter-substrate (TSP), and IC50 drug-target prediction tasks with dramatically less pre-training compute (~1% of ESM-2's GPU-hours).

## Strengths
- **Compelling SOTA results with favorable compute trade-off**: ESM-ProteinVista_OP surpasses prior SOTA on both TSP (93.2% acc, 0.83 MCC vs. SPOT's 92.4%, 0.80) and ESP (94.4% acc, 0.86 MCC vs. ProSmith-ESP and Fusion-ESP's 0.85 MCC), while ProteinVista was pre-trained in ~48 A100-GPU-hours versus ESM-2 650M's ~21,500 H100-GPU-hours. The IC50 regression improvement from R²=0.61 to R²=0.69 is substantial and statistically significant (p<10⁻³⁰⁴).
- **Well-designed complementarity analysis**: Stratification by sequence identity, TM-score, and pLDDT (Figure 2a–d) clearly delineates when 3D structure outperforms sequence (high similarity to training set, high confidence structures) versus when sequence is competitive (low similarity). McNemar and Wilcoxon testing are appropriately applied.
- **Informative ablations**: The 5-view averaging ablation (−6.4% R² with single view) cleanly justifies the multi-view inference strategy. The resolution ablation (−1.1% at 1.5 Å) confirms that atom-level resolution matters but can be relaxed slightly. The finding that fine-tuning augmentation matters minimally (−0.1%) while pretraining augmentation drove robustness is a useful architectural insight.
- **Honest scope: the paper reports the GO task where ProteinVista (F_max=0.57) clearly underperforms ESM-2 (0.62), grounding the claimed advantages correctly in structure-sensitive tasks rather than claiming universal superiority.

## Weaknesses

### Fatal
None.

### Major
- **Rotation invariance is approximate and coarsely discretized**: The paper applies 90° rotations and axis-aligned mirror reflections, covering the 48-element hyperoctahedral group—a very small subset of SO(3). A protein in an arbitrary orientation not aligning to these discrete symmetries can still produce materially different embeddings. The 6.4% R² drop from single-view inference highlights real sensitivity to orientation; the 5-view average mitigates but does not eliminate this. The paper never reports the variance across random orientations of held-out proteins, leaving the practical degree of rotation-robustness quantitatively unmeasured.
- **Missing ESM-2_OP baseline**: The optimized pipeline (Section 3.3) shows ESM-ProteinVista_OP surpassing SPOT and ProSmith-ESP, but does not include a standalone ESM-2_OP (i.e., ESM-2 alone in the identical optimized contrastive training pipeline). Without this, it is impossible to determine how much of the improvement in ESM-ProteinVista_OP is attributable to ProteinVista versus the optimized pipeline design. A fair ablation would show ESM-2_OP, ProteinVista_OP, and ESM-ProteinVista_OP separately.
- **No dedicated DTI baselines for IC50**: For the BindingDB IC50 benchmark (Table 2), the only comparisons are to ESM-2 variants. Numerous dedicated drug-target interaction (DTI) methods exist that combine protein and ligand information (DeepDTA, MolTrans, etc.), and omitting them makes it impossible to assess ProteinVista's standing in the broader DTI landscape, which is a central use case.

### Minor
- **Large protein cropping unanalyzed**: Proteins exceeding the 160³ Å³ bounding box are cropped, but the paper provides no statistics on how frequent this is in the benchmarks or whether cropped proteins show degraded performance.
- **5-view inference cost not included in inference timing**: Figure 3c reports single-pass inference time (~20s per 1k proteins), but all predictions use 5 randomly augmented views. The real inference cost for deployment is ~5× higher, which weakens the compute-efficiency claim at test time.
- **Contrastive pretraining and the supervision loop**: ProteinVista is pre-trained to align with ESM-2 embeddings, then shown to outperform ESM-2 downstream. The paper should clarify more explicitly that the 3D CNN learns geometric structure not captured in ESM-2's embedding space even while being attracted to that space—otherwise the result appears paradoxical.

### Trivial
- The density formula in Section 2.1 appears to have a typo: the expression for the voxel density contribution mixes notation (the type `c ∈ ℝ³` should be an index, not a vector, and the formula exponent form is garbled in the parsed text).

## Nice-to-Haves
- Reporting variance across model runs (multiple random seeds) for ablation results, as ablation differences (e.g., −1.0% for Rosetta vs. contrastive pretraining) are small and might not be statistically significant.
- Analysis of large proteins that were cropped, quantifying how often cropping occurs in benchmark datasets and whether it degrades performance.
- Grad-CAM visualization on concrete binding site examples (mentioned in the discussion but absent from experiments).

## Novel Insights
ProteinVista's most genuinely novel finding is the quantitative characterization of where and when full-atom 3D structure outperforms sequence: the model is strictly better when test proteins have high sequence or structural similarity to training proteins (high-identity bins, Figure 2a–b), while under true distributional shift both models converge and only their ensemble provides lift. This suggests that 3D CNN advantages are primarily precision-based (correctly encoding fine active-site geometry for known fold families) rather than generalization-based, a nuance absent from prior literature. The contrastive pretraining against ESM-2 as a supervisory signal—using sequence information to bootstrap structural representations—is a clean cross-modal learning design that is more data-efficient than prior structure-only pretraining schemes and could be broadly applicable.

## Suggestions
- Include a standalone ESM-2_OP condition in Table 1 to isolate ProteinVista's contribution in the optimized pipeline.
- Add even a few representative DTI method baselines for the IC50 task to anchor the performance within the DTI field.
- Provide a quantitative rotation-sensitivity analysis: compute embedding distance or prediction variance for the same protein under N uniform random SO(3) rotations to report actual rotation robustness rather than assuming 5-view averaging suffices.
- Report inference timing for the 5-view setting used in practice, not single-pass timing.

## Score and Decision
ProteinVista is a solid, well-executed empirical contribution demonstrating that compute-efficient full-atom 3D CNNs are a viable and complementary alternative to large protein language models for structure-sensitive tasks. The SOTA results, compute analysis, and stratified performance analysis are genuine contributions. The main limitations—coarse rotation invariance, missing ESM-2_OP baseline, and absent DTI comparators—are significant but addressable, and do not fundamentally undermine the core empirical finding.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>