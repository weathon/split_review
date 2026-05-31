Now let me finalize the comprehensive review.

## Summary

ProteinVista introduces ProteinVista, a compute-efficient full-atom 3D CNN that voxelizes protein heavy atoms into density grids, pre-trains on ~500K AlphaFold2 structures via contrastive alignment with ESM-2 embeddings, and achieves strong results on three structure-dependent benchmarks (enzyme-substrate classification, transporter-substrate classification, and IC50 regression), outperforming or matching ESM-2 while using fewer parameters (123M vs 650M) and orders of magnitude less pre-training data. The paper also shows that an ensemble with ESM-2 yields further gains, confirming complementarity between sequence and structure representations, and provides an open-source implementation.

## Strengths

1. **Strong empirical results on structure-dependent tasks with far less data**: ProteinVista (123M params, ~500K pre-training structures) achieves R²=0.69 on IC50 regression vs ESM-2₆₅₀M's 0.61, and competitive accuracy on TSP/ESP (Tables 1, 2). This directly supports the claim that full-atom 3D CNNs are a viable and efficient alternative for structure-sensitive tasks. The pre-training used ~1% of the GPU-hours of ESM-2₆₅₀M.

2. **Demonstrated complementarity between sequence and structure**: The ESM-ProteinVista ensemble significantly outperforms both individual models on TSP (91.5% vs 89.3% for ESM-2₆₅₀M) and ESP (93.0% vs 91.9%), with highly significant McNemar's test p-values (Table 1). This provides concrete, statistically validated evidence that sequence and structure information are partly complementary.

3. **Systematic analysis of when structure helps**: The stratification by sequence identity, TM-score, and pLDDT (Figure 2a-c) rigorously characterizes the regimes where ProteinVista excels (high homology, high-confidence structures) vs where it is on par with ESM-2, adding useful insight beyond aggregate metrics. This analysis is thorough and helps the community understand the scope of applicability.

4. **Honest reporting of limitations**: The paper transparently reports that ProteinVista underperforms ESM-2 on GO term annotation (F_max 0.57 vs 0.62), acknowledges the single-snapshot limitation, discusses the storage overhead of 3D representations, and notes the comparison to structure-aware graph models as future work. This strengthens the paper's credibility.

## Weaknesses

### Fatal

None.

### Major

1. **Missing ablation for classification tasks**: The paper ablates pre-training objectives only on the IC50 regression task (showing Rosetta-only pre-training drops R² by only ~1%), but does not test the Rosetta-only (or another structure-only) pre-training variant on the TSP and ESP classification benchmarks. Since the contrastive pre-training explicitly aligns with ESM-2 embeddings, the contribution of structure *per se* to the classification results is not fully disentangled from knowledge distilled from ESM-2 during pre-training. While the IC50 ablation suggests structure carries most of the signal, the classification tasks could behave differently — the paper's central claim about "outperforming sequence transformers" on these tasks would be strengthened by showing that a structure-only pre-training variant also outperforms ESM-2. The authors should provide this ablation or clearly discuss this limitation in their conclusions.

### Minor

1. **Inconsistencies in reported ablation numbers**: The text (Section 4.2) reports replacing contrastive pre-training with Rosetta regression as a "1.0% relative decrease" in R², while the figure table (Figure 2e) lists "~1.2%." Similarly, the resolution ablation is reported as "1.1%" in the text but "~0.8%" in the figure table. These numeric discrepancies should be resolved.

2. **Runtime comparison lacks sufficient detail**: The paper reports that ProteinVista processes 1,000 proteins in 20s vs 426s for ESM-2₆₅₀M on an A100 (Figure 3c), an ~21× speedup at comparable FLOPs (415 vs 520 GFLOPs). The batch sizes used for each model are not stated, and it is unclear whether the timing includes data loading and voxelization preprocessing. The FLOPs comparison provides a hardware-agnostic reference point, but the wall-time claim needs tighter specification to be reproducible.

3. **Voxelization implementation details underspecified**: The paper specifies a Gaussian splatting with σ=1Å but does not state the cutoff radius (hard truncation) for the density contribution, how boundary atoms near the adaptive box edges are handled, or what padding is used. These details affect grid sparsity and reproducibility. The paper notes the appendix contains architecture details (Table S1), but the main text should include a brief summary of these implementation choices.

4. **Classification results lack confidence intervals**: The modest accuracy improvements on TSP (90.8% vs 89.3%) and ESP (91.8% vs 91.9%) are supported by McNemar's test with highly significant p-values, but confidence intervals on the metrics themselves would help quantify the reliability of the reported values, especially given the small absolute differences.

### Trivial

1. The paper refers readers to Table S3 for dataset details (test set sizes, splits, homology filtering), but these details are in the appendix which is not available in the extracted main text. A brief summary of dataset sizes and split criteria in the main body would improve self-containedness.

## Nice-to-Haves

- Compare against graph-based structure-aware models (e.g., GearNet, GVP) on the same tasks to contextualize whether the advantage comes from atom-level detail or from the CNN architecture itself.
- Report the batch size used during contrastive pre-training (InfoNCE typically benefits from large batch sizes).
- Briefly summarize the dataset construction and homology filtering in the main text rather than deferring entirely to the appendix.
- Mention the voxelization cutoff radius for the Gaussian splatting.

## Removed Points

These points were flagged by the input reviewers but are removed from the main weaknesses for the following reasons:

- **"Fixed MolFormer embeddings may disadvantage the model"**: The paper explicitly acknowledges this design choice and its rationale (isolating the protein encoder effect, applied identically to all compared models). The optimized pipeline results (Section 3.3) show the gap *widens* when the small-molecule encoder is also fine-tuned. This is a deliberate methodological choice, not a flaw.
- **"Runtime advantage is startling/implausible"**: Without evidence that the stated numbers are incorrect, this is speculation. The FLOPs comparison (415 vs 520 GFLOPs) provides a hardware-agnostic benchmark consistent with the reported wall-time.
- **"GO term prediction needs more detail about ontology/metric/split"**: The paper states "molecular-function GO terms" and reports F_max, which is sufficient to interpret the comparison. The critic's request is reasonable but not substantive enough to warrant inclusion as a weakness.
- **"Missing comparison to other structure-aware models"**: Moved to Nice-to-Haves. This would strengthen the paper but is not a core flaw, and the paper's main comparison (against ESM-2) is well-motivated.
- **Generic strengths from Strength Finder**: All kept strengths are specific and evidenced. The generic "this addresses an important problem" type strengths were dropped.
- **Various formatting/parser issues**: Artifacts of the extraction process, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily validate and refine the paper's existing claims rather than providing new interpretations. The harsh critic's observation about the need for a classification ablation is the most substantive novel insight.

## Suggestions

1. **Run the Rosetta-only (or structure-only) pre-trained variant on TSP and ESP classification tasks** to fully disentangle the structural contribution from knowledge distilled via contrastive alignment with ESM-2. If the structure-only variant still competes with or beats ESM-2, this solidifies the paper's central claim. If it does not, the conclusions should be appropriately reframed.
2. **Resolve the numeric inconsistencies** between the text and the figure table for the ablation percentages (1.0% vs ~1.2% for Rosetta vs CL; 1.1% vs ~0.8% for resolution).
3. **Specify the batch sizes used** in the runtime comparison and clarify whether timing includes data loading and voxelization.
4. **Add confidence intervals** (e.g., bootstrap or cross-validation) to the main classification results in Table 1.

**Round 1 — Bracketing:**
Bracket: between 4 and 7 (clearly above the reject-level papers at 3.0–3.4, clearly below the exceptional 8.0 papers).

Anchors consulted (Round 1):
- Low band: Ligand Conformation Generation (3.00), 3D Molecular Pretraining via LEGO (3.00), GNNAS-Dock (3.00), ProteinAdapter (3.40)
- Middle band: ProteinWorkshop (6.25), ProteinINR (5.75), AtomSurf (6.75), 3D Interaction Geometric Pre-training (4.00)
- High band: ProtComposer (8.00), SE(3)-Stochastic Flow Matching (8.00), Discrete Walk-Jump Sampling (8.00), Never Train from Scratch (8.00)

**Round 2 — Narrowing within (5.0, 7.5):**

Anchors consulted (Round 2):
- BindNet: Protein-ligand binding representation learning (5.67) — This paper has data leakage concerns, missing baselines, and reproducibility issues. ProteinVista is stronger: it has no leakage concerns, directly controls for the protein encoder effect, and provides an open-source implementation.
- PPIformer: Learning to design PPIs (5.80) — Solid contribution with good evaluation. ProteinVista is comparable in quality, possibly slightly stronger in evaluation rigor (controlled comparisons, statistical tests, honest limitation reporting).
- ProteinWorkshop (6.25) — Benchmark paper with a different type of contribution. ProteinVista's contribution (new architecture + empirical results) is more directly substantive.
- AtomSurf (6.75) — Strong surface representation paper with systematic ablations. ProteinVista is slightly less polished in presentation but has a clearer bottom-line result.

The paper is comparable to the stronger middle-band anchors (around 5.75–6.75). It is better than BindNet (5.67) because of cleaner evaluation and no leakage concerns. It is slightly less polished than AtomSurf (6.75), which has more thorough ablations. ProteinVista's main gap is the missing classification ablation, which keeps it from reaching the 7+ range.

**Final score relative to anchors:** The paper sits between the ~5.75 and ~6.75 anchors, closer to the upper end given its clear architecture, controlled experiments, statistical tests, and honest limitation reporting. I assign **6.0**.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>