## Summary

ProteinVista introduces a full-atom 3D CNN that voxelizes protein structures (encoding five heavy-atom types as continuous density fields), pre-trains on ~500k AlphaFold-2 structures via contrastive alignment to ESM-2 embeddings, and fine-tunes on protein–ligand interaction tasks. The core contributions are: (1) demonstrating that a 3D CNN operating on dense voxel grids can be compute-practical at scale (adaptive boxing, 123M params), (2) showing that the resulting structure embeddings outperform ESM-2 on structure-sensitive tasks (transporter/enzyme substrate classification, IC₅₀ regression), and (3) establishing that the sequence and structure signals are complementary — a simple ensemble further boosts accuracy and reaches state-of-the-art on two substrate prediction benchmarks.

## Strengths

- **Full-atom 3D CNN that is genuinely practical at scale.** ProteinVista processes proteins through 5 convolutional blocks with adaptive boxing (choosing the smallest of 64³–160³ grids that enclose all atoms). This configuration keeps FLOPs manageable (415 GFLOPs/input), pre-training uses ~1% of the GPU-hours of ESM-2₆₅₀M, and inference on 1,000 proteins takes ~20s on one A100 — directly rebutting the prior belief that full-atom 3D CNNs are too sparse and memory-intensive to be useful at scale.

- **Concrete evidence that structure adds signal beyond sequence.** The comparison is clean: ProteinVista (123M params, ~500k pre-training structures) vs. ESM-2₁₅₀M and ESM-2₆₅₀M (150M/650M params, 250M sequences) under identical prediction heads and hyperparameter search. ProteinVista achieves R²=0.69 vs. 0.61 (ESM-2₆₅₀M) on BindingDB IC₅₀ regression (p<10⁻³⁰⁴, Wilcoxon), matches or exceeds ESM-2 on transporter/enzyme substrate classification, and the ESM-ProteinVista ensemble further improves all metrics — the McNemar tests confirm these gains are highly significant (p<10⁻¹³, p<10⁻¹⁷).

- **Honest analysis of when structure helps and when it does not.** Section 4.1 stratifies performance by sequence identity, structural similarity, and AlphaFold confidence (pLDDT), showing that ProteinVista's advantage concentrates in high-similarity/high-confidence regimes. Section 3.4 reports that ProteinVista underperforms ESM-2 on GO annotation (Fmax 0.57 vs. 0.62), a homology-driven task where structure adds limited value. This nuanced characterization strengthens rather than weakens the paper.

- **Ablation studies that validate design choices.** Each key component is ablated on IC₅₀ regression: contrastive vs. Rosetta pre-training (+1.0%), 1.0Å vs. 1.5Å voxel resolution (+1.1%), test-time multi-view averaging (6.4% drop with 1 view). These are concrete numbers that support the architectural decisions.

- **Open-source implementation promised.** The paper states that an open-source Python implementation is released, which supports reproducibility and practical use.

## Weaknesses

### Major

- **No variance estimates for the main task-specific results.** Tables 1 and 2 report point estimates (accuracy, R², MCC, etc.) without standard deviations or multi-seed results. On the transporter-substrate task the gap is 90.8% (ProteinVista) vs. 89.3% (ESM-2₆₅₀M) — a 1.5% difference that could be within random seed variation. The paper does run statistical tests (McNemar, Wilcoxon) but only for the *ensemble* vs. ESM-2 comparison and for IC₅₀ regression, not for the direct ProteinVista-vs-ESM-2 classification head-to-head that many readers will focus on. Without variance bounds, the reader cannot assess whether the claimed improvements are stable or noisy. Given that these are the headline results, this is the paper's most significant evidential gap.

### Minor

- **No comparison against graph-based structure-aware models.** The paper's title and core claim target *sequence transformers* (ESM-2), which it validates. However, the introduction discusses GearNet, ESM-GearNet, and GPS-Fun as related structural approaches and argues they "omit atom-level details." Without a direct comparison to at least one such model on the same benchmarks, the paper does not establish whether the dense voxelization approach is actually superior to residue-level or atom-level GNNs — only that it beats a sequence-only baseline. The contribution would be substantially stronger with this comparison.

- **Data-efficiency framing understates the role of ESM-2 knowledge.** The paper repeatedly says ProteinVista uses "two orders of magnitude less pre-training data" (500k structures vs. 250M sequences). But the contrastive pre-training objective (Section 2.3) aligns ProteinVista embeddings to ESM-2 embeddings via InfoNCE loss — this is effectively knowledge distillation that lets the model piggyback on ESM-2's pre-training on 250M sequences. The claim is not wrong (the raw data count is indeed 500k), but it is incomplete without acknowledging that the *information content* used during pre-training includes ESM-2's learned representations. The Rosetta-based pre-training alternative (which does *not* use ESM-2) achieves nearly the same downstream performance (-1.0% R²), showing the model can learn from structures alone, but the contrastive version used for all experiments does benefit from ESM-2's priors.

- **The compute-efficiency timing numbers lack sufficient methodological detail.** ProteinVista's 20s vs. ESM-2₁₅₀M's 215s on 1,000 proteins (A100) despite 415 vs. 140 GFLOPs is a striking speedup. The paper attributes this to better parallelism of shallow CNNs vs. deep transformers — a plausible explanation. However, no details are given about batch sizes, precision (FP16 vs FP32), data-loading pipeline, whether ESM-2 was run with optimal batching, or whether the timings include the voxelization preprocessing for ProteinVista. The pre-training compute comparison (48h on 4×A100 vs. 7 days on 128×H100) is clearer because it is apples-to-apples in terms of being actual training runs. The inference timings should be reported under a controlled, well-documented setup.

- **Rotation robustness is achieved via test-time ensemble, not learned invariance.** The paper claims "rotation-robust representations" (abstract) and "rotation-invariant predictions" (Section 2, with hedging: "aimed to achieve"). The ablation shows that dropping test-time multi-view averaging (5→1 views) causes a 6.4% R² drop. This means the model is not intrinsically rotation-invariant; it relies on an inference-time ensemble. The claim is not fraudulent (the paper is transparent about this), but the terminology could be more precise.

### Trivial

- Figure 3's caption says "Inference Time on Single A100" but the text in Section 4.3 says "during training." The distinction matters — if these are training timings (forward+backward), the comparison is different from inference-only timings.
- Table 1's value for "ESM-ProteinVista" under TSP Precision: the bold formatting is ambiguous about which values are best (multiple entries bolded in some columns).

## Nice-to-Haves

- Incorporate Graph-based structure models (e.g., GearNet-Edge or ESM-GearNet) on at least one benchmark to situate the 3D CNN approach relative to the GNN structural encoding literature.
- Report mean ± std over 3–5 random seeds for all task-specific results.
- Provide a more detailed benchmarking setup for the timing comparison in Section 4.3 (batch sizes, precision, preprocessing costs).
- Discuss the chirality issue noted by the section-by-section review: 90° rotations and mirrors can invert chirality; since proteins use L-amino acids, this is a physically meaningful absence.

## Novel Insights

The reviews surface one insight that goes beyond the paper's own framing: the **asymmetry between the structure-model's data footprint in compute vs. storage** is a practical consideration that the paper's "compute-efficient" framing glosses over. The 75 GB for 5,800 proteins (NumPy float32) vs. 3 MB for FASTA means that any large-scale deployment of ProteinVista will shift the bottleneck from compute to storage and I/O — a trade-off that users need to evaluate for their own setup. This is not a weakness but a useful characterization that the paper partially reports and could emphasize more.

## Suggestions

1. **Run 3–5 random seeds** for all experiments (Tables 1 and 2, GO Fmax) and report mean ± std. This is the single most impactful fix.
2. **Add at least one graph-based structural baseline** — GearNet-Edge or ESM-GearNet — on the transporter or enzyme substrate task to clarify where the 3D CNN stands relative to alternative structural encoders.
3. **Revise the data-efficiency framing** to explicitly state that the contrastive pre-training aligns to ESM-2 embeddings, which means the effective information used during pre-training goes beyond the 500k raw structures.
4. **Provide full experimental details** for the timing benchmark in Section 4.3: batch sizes, precision mode, whether preprocessing/voxelization time is included, and whether ESM-2 was run with optimized batching for its sequence lengths.

## Score and Decision

**Calibration anchors consulted:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Ligand Conformation Generation (Reject) | m9zWBn1Y2j | 3.00 | 1 (bracket) | Much weaker — no competitive results, purely generative task |
| 3D Molecular Pretraining via Localized Geometric Generation (Reject) | rEQ8OiBxbZ | 3.00 | 1 (bracket) | Weaker — more niche molecular pretraining, fewer tasks evaluated |
| ProteinAdapter (Reject) | jqx5XI4Yr3 | 3.40 | 1 (bracket) | Weaker — adapter-based fine-tuning, less novel contribution |
| ProteiNexus (Reject) | iBAWiEjogY | 3.67 | 1 (bracket) | Weaker — structural pretraining with fewer benchmarks, missing compute analysis |
| BindNet (Accept) | AXbN2qMNiW | 5.67 | 1+2 | **Comparable** — protein-ligand representation learning paper, similar task scope, but had data leakage concerns that ProteinVista avoids. ProteinVista has cleaner comparisons but lacks error bars. |
| Dual Flows (Reject) | hiciJQdmpw | 4.75 | 1+2 | Weaker — protein design paper with score variance (3–6), less direct comparison |
| EBMDock (Accept) | qg2boc2AwU | 5.75 | 2 (narrow) | Comparable — docking paper with scores 3/6/8, one very low outlier. ProteinVista's evidence is more consistent. |
| ProteinWorkshop (Accept) | sTYuRVrdK3 | 6.25 | 2 (narrow) | **Somewhat stronger** — comprehensive benchmark infrastructure, but different contribution type (benchmark, not method). More thorough evaluation but different goals. |
| AtomSurf (Accept) | ARQIJXFcTH | 6.75 | 2 (narrow) | Stronger — careful surface-vs-graph comparison, well-controlled experiments. |

**Round 1 bracket:** Between ~3.5 and ~6.5 — clearly above the Reject-level protein papers (3.0–3.67) and below the strong Accepts (6.75–8.0).

**Round 2 narrowing:** The paper is most comparable to BindNet (5.67) — both are method papers showing gains on protein-ligand tasks. ProteinVista has a broader experimental scope (3 tasks + GO, SOTA comparison, compute analysis, ablation) and avoids the data leakage issues that lowered confidence in BindNet. However, BindNet's reviewers did not flag missing error bars as a primary concern (they flagged leakage and missing baselines), whereas ProteinVista's missing variance is a clear weakness. Against EBMDock (5.75, scores 3/6/8) the comparison is favorable — ProteinVista's evidence is more consistent (no 3/8 split). ProteinWorkshop (6.25) is a more comprehensive infrastructure contribution but a different paper type.

**Final score: 5.5** — a solid paper with clear contributions (first practical full-atom 3D CNN for proteins, strong evidence of sequence-structure complementarity, careful ablation) held back by the missing variance estimates on core results and the absence of a graph-based structural baseline that would contextualize the contribution against the most directly relevant line of work. The paper's strongest results (SOTA on substrate prediction via ESM-ProteinVistaOP, R²=0.69 on IC₅₀, compute analysis) are genuine, but the error-bar gap prevents full confidence in the stability of the individual comparisons.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>