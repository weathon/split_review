Now I have a clear picture. Let me compile the final review.

**Round 1 bracket:** 5.5 – 7.0 (bounded below by weak anchors at 3.0–3.4 and above by strong anchors at 8.0)

**Round 2 narrowing:** 6.0 – 6.75. Compared to specific anchors:
- EquiPocket (5.50, Reject) → weaker, rejected partly on rotation issues among others
- Protein-ligand binding (5.67, Accept) → comparable or slightly weaker
- ProteinWorkshop (6.25, Accept) → comparable quality, ProteinVista has stronger novelty
- All-Atom GNN (6.50, Accept) → comparable, different domain
- SaProt (7.33, Accept) → stronger, broader evaluation and larger scale

ProteinVista sits between the 6.0 and 6.5 anchors, closer to 6.25.

---

## Summary

ProteinVista introduces a full-atom 3D CNN that voxelizes protein heavy atoms, is pre-trained on ~500K AlphaFold2 structures, and fine-tuned on protein–ligand prediction tasks. The core claim is that explicit 3D geometry from a compute-efficient 3D CNN can outperform sequence transformers on structure-dependent tasks while requiring far less pre-training data and compute. The paper demonstrates this on transporter-substrate classification, enzyme-substrate classification, and IC50 regression.

## Strengths

- **First compute-efficient full-atom 3D CNN with large-scale pre-training on AF2 structures.** The adaptive boxing (selecting among 64³, 96³, 128³, 160³ grids) directly addresses the sparsity problem that previously made full-atom 3D CNNs impractical for proteins. Processing 1,000 proteins in 20 seconds on a single A100 vs. 215–426 s for ESM-2 variants (Figure 3c) substantiates the tractability claim concretely.

- **Clear improvements on structure-dependent tasks.** On IC50 regression, ProteinVista alone achieves R²=0.69 vs. 0.61 for ESM-2₆₅₀M (p<10⁻³⁰⁴). On transporter-substrate classification, it reaches 90.8% accuracy vs. 89.3% for ESM-2₆₅₀M (Table 1). These comparisons use identical prediction heads and fixed MolFormer embeddings, isolating the encoder effect.

- **Demonstrated complementarity with sequence models.** The ESM-ProteinVista ensemble consistently improves over both single models across all metrics on TSP and ESP (Table 1), and the stratification by sequence identity and TM-score (Figure 2a–b) shows concrete evidence of complementarity: ProteinVista excels when similar structures exist in training, while ESM-2 performs better on remote homologs.

- **Thorough ablation and diagnostic analysis.** Section 4 systematically ablates ensemble size, pre-training objective, voxel resolution, and rotation augmentation. The analysis stratified by pLDDT (Figure 2c) honestly shows where the method works best (high-confidence structures) and where it doesn't (low-confidence structures, where it matches but doesn't exceed ESM-2).

- **Honest reporting of failures.** The GO annotation experiment (Section 3.4) shows ProteinVista underperforming ESM-2 (Fmax 0.57 vs. 0.62), correctly interpreted as "when functional inference depends mainly on conserved motifs or overall homology, structure encoders add limited value." This strengthens credibility.

## Weaknesses

### Major

- **Rotation robustness is tested only on a finite 90° subgroup.** The augmentation uses rotations by 90° about Cartesian axes and mirror reflections — a finite subset of SO(3). During inference, predictions are averaged over five random views drawn from this same discrete set. The paper claims "rotation-robust representations" and that the model is "less affected by arbitrary rotations of the input protein" (Section 2.4), but never tests on continuously rotated structures (e.g., random rotations by arbitrary angles). The ablation shows that using a single view vs. five views at inference hurts R² by 6.4%, confirming the network is orientation-sensitive even within the limited set. Without testing on arbitrary rotations — or stating that the test benchmarks use a canonical orientation — the claimed rotation robustness is untested for the vast majority of 3D rotations that real-world unaligned PDB inputs could present. This gap does not invalidate the benchmark results (which use realistic PDB inputs), but it does mean the method's robustness claims are over-extrapolated relative to the evidence.

- **The state-of-the-art comparison on substrate prediction (Section 3.3) lacks a controlled abalation.** The optimized pipeline (OP) fine-tunes the small-molecule encoder jointly with ProteinVista, trains a separate contrastive network, and then ensembles with ESM-2 predictions. The resulting ESM-ProteinVista_OP is compared against published numbers for SPOT, ProSmith-ESP, and Fusion_ESP. Because the OP result is an ensemble that includes ESM-2, and because no version of ESM-2 alone is evaluated through the same OP pipeline, the reported improvements over these SOTA methods cannot be cleanly attributed to ProteinVista's architecture. This does not affect the paper's main controlled comparisons (Tables 1–2, which use identical simple pipelines), but the SOTA claims in Section 3.3 are not supported by a controlled experiment.

### Minor

- **Abstract overstates single-model results on enzyme-substrate prediction.** The abstract states "ProteinVista outperforms sequence transformers on three benchmarks." On the enzyme-substrate task, ProteinVista alone achieves 91.8% accuracy vs. ESM-2₆₅₀M's 91.9% — it does not outperform. The ensemble (93.0%) does, but the abstract is ambiguous. This is a factual inaccuracy that should be corrected.

- **The contrastive pre-training uses ESM-2 as a teacher, somewhat softening the "structure-only" framing.** The paper's most effective pre-training aligns ProteinVista embeddings with ESM-2 sequence embeddings via InfoNCE loss. The Rosetta-score-only ablation (Section 4.2) shows only a 1% relative R² drop on IC50, which is reassuring, but this ablation is only reported for one task. Reporting it across all tasks would more convincingly demonstrate that the structure encoder's value is independent of sequence-model distillation.

### Trivial

- The paper states "23 Rosetta scores" in Section 2.3 but "33 Rosetta scores" in the Discussion. This inconsistency should be resolved.
- The compute efficiency analysis (Section 4.3) attributes the speedup to being "parallelized more efficiently" without further detail. A brief architectural explanation (fewer sequential operations vs. deep transformer stacks) would help.

## Nice-to-Haves

- Test rotation robustness directly by applying arbitrary continuous rotations to a subset of the test set and measuring performance drop.
- Report Rosetta-only pre-training results on all three downstream tasks (not just IC50) to substantiate structure-independence from the ESM-2 teacher.
- For the SOTA comparison, evaluate ESM-2₆₅₀M through the same optimized pipeline as a control.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Strength Finder's claim about "orders of magnitude less data"**: Re-worded to "two orders of magnitude" which is accurate (0.5M vs 250M) and not removed — kept as part of the compute efficiency strength.
- **Harsh critic's "missing ESM-2 embedding dimensions"**: The input size to the prediction head differs because ProteinVista outputs 1024-dim vectors and ESM-2 outputs different dimensions, but this is handled by the shared prediction head design. Removed because this is a standard design choice that doesn't create unfairness.
- **Harsh critic's point about ESM-ProteinVista ensemble being worse than ProteinVista alone on IC50**: The paper acknowledges this and correctly interprets it ("the sequence model contributes little additional information"). The critic's speculation about "miscalibration" is not supported by evidence in the paper. Removed because the paper already addresses this.
- **Harsh critic's point about rotation augmentation during fine-tuning having no effect**: The paper reports this honestly as -0.1% change. The critic's claim that "this does not test invariance to arbitrary rotations" is restating the same point already made in the rotation robustness section above — merged into the Major weakness.
- **Strength Finder's claim that ProteinVista "requires 5× fewer parameters"**: Kept as "requires fewer parameters" — this is factually correct (123M vs 650M).

## Novel Insights

None beyond the paper's own contributions. However, a noteworthy pattern emerges from the stratified analysis (Figure 2a–b): the method's complementarity with sequence models is not uniform but strongly conditioned on structural similarity to the training set. This is a more specific characterization than the generic "sequence and structure are complementary" claim common in the literature, and it offers practical guidance for when to prefer or combine the two modalities.

## Suggestions

1. **Correct the abstract** to say "outperforms or matches" on three benchmarks, or clarify that the ensemble outperforms.
2. **Add a rotation-robustness experiment:** take a subset of the test set, apply random continuous rotations (not just 90° multiples), and measure ProteinVista's performance with and without multi-view averaging.
3. **For the SOTA comparison, add a control** where ESM-2₆₅₀M is processed through the same optimized pipeline, so readers can see what fraction of the improvement comes from the pipeline vs. the encoder.
4. **Resolve the 23 vs. 33 Rosetta score discrepancy.**

## Score and Decision

**Round 1 bracket (bracketing pass):** 5.5 – 7.0  
Anchors consulted:
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| LEGO (rEQ8OiBxbZ) | 3.00 | R1 | Much weaker — limited evaluation, rejected |
| ProteinAdapter (jqx5XI4Yr3) | 3.40 | R1 | Much weaker — no novel architecture |
| ProteiNexus (iBAWiEjogY) | 3.67 | R1 | Weaker — structural pre-training but no 3D CNN |
| EquiPocket (umUIYdLtvh) | 5.50 | R2 | Slightly weaker — rejected partly on rotation issues |
| Protein-ligand binding (AXbN2qMNiW) | 5.67 | R2 | Comparable — accepted, similar scope |
| ProteinWorkshop (sTYuRVrdK3) | 6.25 | R2 | Comparable quality — benchmark paper |
| **ProteinVista (this paper)** | **~6.25** | — | — |
| All-Atom GNN (4S2L519nIX) | 6.50 | R2 | Comparable — different domain (small molecules) |
| Group ligands docking (zDC3iCBxJb) | 6.75 | R2 | Slightly stronger — broader impact |
| SaProt (6MRm3G4NiU) | 7.33 | R2 | Stronger — larger scale, more tasks |

**Narrowing:** Round 2 placed ProteinVista close to the 6.25–6.50 level. It is stronger than the 5.5–5.67 papers (clearer contributions, better-controlled evaluation) but not at the 7.33 level of SaProt (which trains on 40M proteins and evaluates on 10 tasks). Within the bracket, it aligns most closely with the 6.25 anchor in terms of overall quality and contribution density.

**Final score: 6.25**

MY FINAL SCORE: <score>6.25</score>
MY FINAL DECISION: <decision>Accept</decision>