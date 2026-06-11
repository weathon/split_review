Now let me finalize. Let me compile the complete review with all the calibration information.

**Round 1 bracket**: Based on comparison with anchors across all bands, ProteinVista sits between the Pre-training Sequence/Structure/Surface paper (5.75) and AtomSurf (6.75). The initial bracket is **5.5–6.5**.

**Round 2 narrowing**: Comparing within this bracket, ProteinVista is stronger than the lower anchors (Protein-ligand binding at 5.67, Pre-training Sequence/Structure/Surface at 5.75) due to more comprehensive evaluation, honest failure analysis, and the strong IC50 result — but notably weaker than AtomSurf (6.75) which achieves SOTA across all Atom3D tasks with a more principled approach. ProteinVista is broadly comparable to the All-Atom Geometric GNN paper (6.50) but with a clearer contribution and more downstream tasks, offset by the distillation confound and marginal classification results.

Final score: **6.0**. The paper has genuine merits (strong IC50 result, thorough ablations, honest failure analysis, compute efficiency) but the contrastive pretraining confound weakens the central "outperforms sequence transformers" claim, and the classification improvements are marginal. The Rosetta ablation partially addresses the confound for IC50, showing the structural signal is independently strong, but the ablation is not extended to classification tasks.

---

## Summary

ProteinVista introduces a compute-efficient 3D CNN that voxelizes full-atom protein structures at 1.0Å resolution, processes them through five convolution blocks, and is pre-trained on ~500K AlphaFold-2 structures via contrastive alignment against ESM-2 embeddings. The central claim is that explicit 3D atomic coordinates encoded by a compact (123M-parameter) CNN outperform much larger sequence transformers (ESM-2 650M, 650M parameters) on structure-dependent prediction tasks. The strongest evidence is on drug-target affinity regression (IC₅₀, R²=0.69 vs. 0.61, p<10⁻³⁰⁴), with weaker but still positive results on enzyme-substrate and transporter-substrate classification, and an honest characterization of failure on homology-driven GO annotation.

## Strengths

- **Compelling IC₅₀ regression result with rigorous statistics**: On BindingDB drug-target affinity prediction (Table 2), ProteinVista achieves R²=0.69 vs. ESM-2 650M's 0.61, with a Wilcoxon signed-rank test yielding p<10⁻³⁰⁴. This task is well-aligned with the paper's motivation that atom-level binding-pocket geometry matters, and the statistical validation is airtight.
- **Honest complementarity analysis**: Section 4.1 and Figure 2 stratify performance by sequence identity, TM-score, and pLDDT, revealing that ProteinVista excels when similar folds are in the training set while ESM-2 holds an edge for novel folds. The ensemble outperforms both across all bins, providing genuine evidence of complementary signals rather than merely claiming it.
- **Well-characterized failure mode**: Section 3.4 shows ProteinVista underperforms ESM-2 on GO molecular-function prediction (Fmax 0.57 vs. 0.62), correctly delineating when structural encoding adds no value (homology-driven tasks). This honest reporting strengthens the credibility of the positive results on structure-sensitive tasks.
- **Thorough ablation study**: Section 4.2 systematically isolates contributions: multi-view inference is critical (−6.4% R² when reduced to 1 view), voxel resolution matters (−1.1% at 1.5Å), and pre-training augmentation transfers to fine-tuning (disabling during fine-tuning has negligible impact). The Rosetta-vs-CL ablation shows the structure signal itself is strong even without ESM-2 distillation (−1.0% R²).
- **Concrete compute-efficiency measurements**: Section 4.3 and Figure 3 show ProteinVista processes 1000 proteins in 20s on one A100 vs. 426s for ESM-2 650M, with pre-training using ~1% of ESM-2's GPU-hours and ~500× less training data. These are practically meaningful efficiency gains backed by specific numbers.

## Weaknesses

### Fatal
None.

### Major
- **Contrastive pretraining confound weakens the central claim**: ProteinVista is pre-trained via contrastive alignment against ESM-2 embeddings (Section 2.3). The InfoNCE loss explicitly pulls ProteinVista toward representations ESM-2 already produces from sequence alone, meaning the model is trained partially to distill ESM-2 rather than independently extract structural information. The Rosetta-pretrained ablation (Section 4.2) shows only a −1.0% R² difference on IC₅₀, which suggests the structure signal itself is strong, but this ablation is reported for IC₅₀ only — not the full classification benchmark suite (TSP, ESP). The headline claim that a 3D CNN "outperforms sequence transformers" therefore conflates architectural advantage with knowledge distillation. The paper should report Rosetta-pretrained variant performance across all tasks to cleanly attribute gains to structure encoding.

### Minor
- **Marginal classification improvements**: On TSP, ProteinVista achieves 90.8% vs. ESM-2 650M's 89.3% (+1.5pp); on ESP, the models are tied (91.8% vs. 91.9%). The SOTA comparison (Section 3.3) shows ESM-ProteinVista_OP at 93.2% TSP vs. SPOT's 92.4% and 94.4% ESP vs. ProSmith-ESP/Fusion_ESP's 94.2% — improvements under one percentage point, with Fusion_ESP actually having higher ROC-AUC (0.972 vs. 0.967). The IC₅₀ result is the stronger demonstration and would benefit from being foregrounded as the primary result.
- **Rotational augmentation restricted to finite subgroup, not full SO(3)**: Section 2.4 applies only 90° rotations around Cartesian axes plus mirror reflections (the 48-element octahedral group). The paper acknowledges the model is "less affected by arbitrary rotations" rather than invariant to them. For a method motivated by capturing fine 3D geometry, dependence on a canonical orientation frame is a limitation. The multi-view test-time averaging (5 views from the same finite group) mitigates but does not solve this. No evaluation of performance degradation under arbitrary continuous rotations is provided.
- **No comparison against graph-based structure models**: The introduction critiques residue-level GNNs (DeepFRI, GearNet) and finer-grained graphs (GPS-Fun) for omitting atom-level detail (lines 17–25), setting up an expectation of empirical comparison. However, all experiments compare only against sequence models (ESM-2) and task-specific SOTA methods (SPOT, ProSmith-ESP, Fusion_ESP). Comparing against at least one graph-based structure encoder would strengthen the claim that 3D CNNs are a superior structural encoding approach.
- **Missing statistical tests for classification**: The paper reports McNemar's test for the ensemble vs. ESM-2 on TSP and ESP (p<10⁻¹³ and p<10⁻¹⁷) and Wilcoxon for IC₅₀ (p<10⁻³⁰⁴), but no equivalent test comparing ProteinVista alone vs. ESM-2 on the binary classification tasks where margins are narrow. This makes it difficult to assess whether the 1.5pp TSP gap exceeds run-to-run variance.

### Trivial
- **Numerical discrepancies between text and Figure 2e**: The text (line 168) states multi-view ablation reduces R² by 6.4%, while Figure 2e table shows "~−5.5%." Similarly, text (line 170) states Rosetta vs. CL changes R² by 1.0%, while Figure 2e shows "~1.2%." These should be reconciled.

## Nice-to-Haves
- The GPU comparison for pre-training (Section 4.3) uses different hardware types (4×A100 for ProteinVista vs. 128×H100 for ESM-2) without normalization. Acknowledging this or normalizing to a common GPU would improve precision.
- Reporting run-to-run variance (e.g., standard deviation across random seeds) on key metrics would help contextualize the narrow classification margins.
- The paper could report how many proteins fall into each adaptive box size (64³, 96³, 128³, 160³) and what fraction of proteins exceed the 160³ limit and are cropped.

## Removed Points
These points were flagged and removed with justification:

- **"The Gaussian σ=1 choice lacks justification"** — REMOVED. This is a design nitpick; the paper provides a clear rationale (reduces discretization artifacts, preserves local geometry, creates smoother gradients) in Section 2.1.
- **"Shallow depth may limit receptive field for allosteric effects"** — REMOVED. Speculative concern not anchored in any evidence from the paper's tasks (which are binding-site focused, not allosteric). The paper acknowledges the model's simplicity as a feature.
- **"τ=0.07 borrowed from CLIP without justification"** — REMOVED. Borrowing established hyperparameters from prior work (Radford et al., 2021, cited in the paper) is standard practice.
- **"Parameter count comparison glosses over ESM-2 150M (123M vs. 150M is similar)"** — REMOVED. The paper explicitly notes ESM-2 ranges "up to 15 billion" parameters (line 69), and the 150M variant is directly compared in all experiments. The claim "much fewer" is literally true for the most common comparison target (650M).
- **"No discussion of whether ESM-2 is frozen during pretraining"** — REMOVED. Trivial implementation detail.
- **"Missing Table S1, S2, S3"** — REMOVED per hard rule: the parser strips appendix/references; these exist in the original submission.
- **"Box size distribution not reported"** — MOVED to Nice-to-Haves as a minor presentation suggestion.
- **Strength Finder: 'Contrastive pre-training against ESM-2 is a pragmatic design'"** — This strength conflicts with the verified Major weakness about the distillation confound. The weakness wins: the pragmatic design also creates a claim-support gap.

## Novel Insights
None beyond the paper's own contributions. The paper's core insight — that a straightforward 3D CNN on full-atom voxel grids is a viable and compute-efficient protein encoder that can complement sequence models — is well-supported by the experiments, particularly the IC₅₀ regression and complementarity analysis. The finding that rotational augmentation during pre-training transfers to fine-tuning (disabling augmentation during fine-tuning has negligible impact, Section 4.2) is an interesting and well-supported secondary insight.

## Suggestions
- Report Rosetta-pretrained ProteinVista performance on the full benchmark suite (TSP, ESP, and IC₅₀) to decouple the structural encoding contribution from ESM-2 distillation. This would substantially strengthen or appropriately temper the central claim.
- Add an arbitrary-rotation stress test by evaluating ProteinVista on test proteins rotated by non-90° angles, quantifying the practical cost of the finite augmentation group.
- Include statistical significance tests comparing ProteinVista alone vs. ESM-2 on the binary classification tasks.
- Reconcile the numerical discrepancies between the main text and Figure 2e.

## Calibration Details

**Round 1 (Bracketing)**: Searched across five score bands for protein structure 3D CNN voxel representation papers. Initial bracket: 5.5–6.5.

**Round 2 (Narrowing)**: Searched within 5.0–6.25 and 6.25–7.5 bands. Compared against specific anchors:

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| EquiPocket (umUIYdLtvh) | 5.50 | R1 | ProteinVista has more comprehensive evaluation, honest failure modes, and clearer contribution |
| Protein-ligand binding (AXbN2qMNiW) | 5.67 | R1/R2 | ProteinVista stronger: more tasks, no data leakage concerns, better ablation |
| Pre-training Seq/Struct/Surface (BEH4mGo7zP) | 5.75 | R1/R2 | ProteinVista slightly stronger: more tasks, better ablation, honest failure analysis; both have marginal improvements on some tasks |
| PPIformer (xcMmebCT7s) | 5.80 | R2 | Comparable: PPIformer has better dataset novelty; ProteinVista has more comprehensive evaluation |
| MolSpectra (xJDxVDG3x2) | 6.33 | R2 | MolSpectra has more principled multi-modal approach; ProteinVista has clearer contribution and honest failure analysis |
| All-Atom Geometric GNN (4S2L519nIX) | 6.50 | R2 | Comparable in quality; All-Atom paper has more novelty in scaling investigation; ProteinVista has clearer contribution and more downstream tasks |
| AtomSurf (ARQIJXFcTH) | 6.75 | R1/R2 | AtomSurf clearly stronger: SOTA across all Atom3D tasks, more principled approach, no distillation confound |

ProteinVista is stronger than the 5.50–5.80 anchors (more comprehensive evaluation, stronger IC₅₀ result, honest failure analysis, compute comparisons) but notably weaker than the 6.75 anchor (less principled approach, distillation confound, marginal classification improvements). It is comparable to the 6.33–6.50 anchors. Final score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>