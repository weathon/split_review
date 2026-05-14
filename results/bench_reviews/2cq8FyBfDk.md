Now let me write the final consolidated review.

## Summary

ProteinVista introduces a 3D CNN operating on voxelized full-atom protein structures. Pre-trained on ~500K AlphaFold2 structures (two orders of magnitude fewer than sequence PLMs), it achieves better or comparable performance to ESM-2 on binding-related tasks (IC50 R²=0.69 vs 0.61 for ESM-2₆₅₀M; transporter-substrate accuracy 90.8% vs 89.3%) while using 5× fewer parameters and offering faster inference (20s vs 426s per 1,000 proteins). An ensemble with ESM-2 shows complementarity between sequence and structure signals. The model is less effective on homology-driven tasks like GO annotation, which the paper honestly reports.

## Strengths

1. **Genuine demonstration that 3D CNNs on full-atom voxel grids are practically tractable at scale.** Despite the conventional wisdom that such models are computationally prohibitive, ProteinVista's 123M-parameter 3D CNN achieves inference throughput ~20× faster than ESM-2₆₅₀M on an A100 (20s vs 426s per 1K proteins, Section 4.3). The adaptive boxing (64³–160³ grids) and 5-block architecture are sensible design choices validated by ablation.

2. **Strong controlled experimental design isolates the effect of the protein encoder.** The prediction head and small-molecule encoder (MolFormer) are held fixed across ProteinVista and ESM-2 variants (Section 3.1), making the benchmark comparisons clean and interpretable. The inclusion of an optimized pipeline (Section 3.3) further shows performance can improve under less constrained settings.

3. **The Rosetta pre-training ablation directly addresses the "trained on ESM-2" concern.** The contrastive (ESM-aligned) objective gives only a 1.0% relative R² gain over the purely structure-based Rosetta regression objective (Section 4.2). This demonstrates that ProteinVista's performance does *not* depend on mimicking ESM-2 — the structural information itself drives the gains, even if alignment gives a small extra boost.

4. **Honest failure analysis and task-dependent evaluation.** The GO annotation results (Fmax 0.57 vs ESM-2's 0.62) are reported without spin (Section 3.4), and the stratification by sequence identity, TM-score, and pLDDT (Section 4.1) honestly maps where structure helps. This transparency is rare and valuable.

5. **Compute-efficient pre-training.** Pre-training on 4 A100s for 48 hours (vs. 128 H100s for ~7 days for ESM-2₆₅₀M) is a genuine practical advantage, and the 500K vs 250M pre-training data comparison is fair since AFDB structures are freely available.

## Weaknesses

### Fatal

None.

### Major

1. **The "compute-efficient" claim compares model forward-pass only, omitting structure prediction costs.** The 20s vs 426s comparison (Section 4.3) is for the model forward pass only. For any protein not already in AlphaFold DB (or for which a novel sequence requires structure prediction), running AlphaFold2 adds hours per protein. The title's "compute-efficient" and the forward-pass-centric framing obscure this pipeline cost. While AFDB covers much of UniProt, the paper should explicitly acknowledge that the end-to-end compute cost for novel sequences is radically different. This does not invalidate the model-efficiency result, but it narrows the scope of the compute-efficiency claim considerably.

2. **The "outperforms sequence transformers" framing is partially weakened by the contrastive pre-training to ESM-2.** Although the Rosetta ablation (1% gap) shows the model does not *require* ESM-2 alignment to work well, the paper's headline uses the contrastively aligned model as its primary result while simultaneously claiming to "outperform" the very model used for alignment. This creates an awkward narrative inconsistency. The paper would be stronger if it led with the Rosetta-only model as the primary structure encoder and presented the ESM-aligned version as an optional enhancement.

### Minor

1. **The "atom-level" detail is coarser than the term suggests.** The 5-channel encoding (C, N, O, S, P) collapses the ~20+ chemically distinct atom environments in proteins (e.g., carbonyl vs. hydroxyl oxygen, sp² vs. sp³ carbon, amide vs. aromatic nitrogen) into five broad categories. Gaussian density spreading at σ=1Å further blurs atom positions. The paper is transparent about these choices, but the terminology "full-atom 3D CNN" and "atom-level" overstate the effective resolution. An ablation varying the number of atom-type channels would clarify whether finer-grained encoding matters.

2. **No atom-type channel ablation.** The ablation study (Section 4.2) varies voxel resolution and pre-training objective but does not test whether distinguishing more atom types (e.g., 10–15 channels) improves performance. Since this directly bears on the claim of "atom-level" detail, it is a notable gap in the experimental analysis.

3. **On Enzyme-Substrate Prediction (ESP), ProteinVista alone does not beat ESM-2₆₅₀M.** Table 1 shows ProteinVista achieves 91.8% accuracy vs. ESM-2₆₅₀M's 91.9% — a tie within noise. The paper accurately states "surpasses or equals," but the text's emphasis on "surpasses" downplays that on this task the advantage only appears in the ensemble. This is a minor over-claim.

### Trivial

- The density formula in Section 2.1 ("∝ exp(-||v - r||/σ²)") is missing the square in the numerator (should be ||v - r||²) — likely a parser rendering issue.
- The figure axis values in the paper do not always match the text description (e.g., text says 20s, figure shows ~10s for inference time), though the relative ordering is consistent.

## Nice-to-Haves

- **Full pipeline compute audit:** Report the total time (AF2 inference + voxelization + CNN forward pass) for a representative set of novel proteins to contextualize the "compute-efficient" claim.
- **Atom-type resolution ablation:** Compare 5-channel encoding against a finer-grained scheme (e.g., distinguishing carbonyl vs. hydroxyl oxygen, sp² vs. sp³ carbon) to validate whether the coarse grouping is sufficient.
- **Case studies of complementary predictions:** Analyze specific examples where ProteinVista succeeds and ESM-2 fails (and vice versa) to build intuition about what structural information matters.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Storage comparison criticism (Harsh Critic point)**: The critic claims storing 3D coordinates is prohibitive. The paper already acknowledges this explicitly: "ProteinVista is cheaper in compute and data, but requires larger storage for 3D inputs" (Section 4.3). The paper transparently reports both the advantage and the trade-off. Removed as already addressed.
- **p-value suspiciousness (p < 10⁻³⁰⁴)**: The critic calls this "suspiciously extreme." With a test set of typical BindingDB size (tens of thousands of examples), such p-values are entirely expected for a real effect of the reported magnitude. This reflects a misunderstanding of large-sample statistics. Removed as factually wrong.
- **"Pre-train without ESM-2 alignment" as missing experiment**: The paper already does this — the Rosetta-only ablation (Section 4.2) is precisely this experiment. Removed as strawman.
- **GO results as undermining "universal encoder" claim**: The paper itself states "when functional inference depends mainly on conserved motifs or overall homology, structure encoders add limited value" (Section 3.4). The paper does not claim to be a universal encoder; it identifies its scope. Removed as already addressed.
- **Formatting nitpicks about formula rendering and garbled text**: These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Restructure the narrative around structure-only pre-training.** Lead with the Rosetta-only model as the primary ProteinVista encoder and present ESM-2 alignment as an optional enhancement. This would eliminate the narrative tension of "outperforming the model you trained to mimic."
2. **Add a "total pipeline cost" analysis** for a realistic deployment scenario: for N novel proteins, report (AF2 time + voxelization + CNN) vs. (ESM-2 forward pass). This would make the compute-efficiency claim properly scoped.
3. **Add an atom-type ablation** comparing 5 channels vs. finer-grained groupings to justify or qualify the "atom-level" language.
4. **Add correlation analysis between ProteinVista and ESM-2 predictions** to quantify the degree of complementarity vs. redundancy in the ensemble, beyond the aggregate accuracy improvements already reported.

## Score and Decision

**Calibration anchors:**

| Path | Avg Human Score | Comparison to this paper |
|---|---|---|
| `/home/wg25r/review_agent/human_reviews_2026/vbc5JyzNE0.md` (Geometric SSL on 3D Proteins) | 2.80 | Much weaker: limited evaluation (2 tasks), no controlled encoder comparison, weaker baselines. ProteinVista has far more thorough experiments. |
| `/home/wg25r/review_agent/human_reviews_2026/CrXcfMLR9q.md` (PairMixer) | 4.00 | Similar tier, but PairMixer was criticized for incremental novelty (deleting attention). ProteinVista has more architectural novelty but also more framing issues. Comparable overall. |
| `/home/wg25r/review_agent/human_reviews_2026/9EBW65ZdJN.md` (Structure-Aligned PLM) | 4.00 | Similar score band. Both papers use contrastive alignment between sequence and structure representations. The PLM paper was criticized for marginal gains; ProteinVista shows clearer binding-task improvements but has its own framing problems. |
| `/home/wg25r/review_agent/human_reviews_2026/kIxAQxUZHq.md` (Bento) | 5.00 | Similar tier. Bento is a benchmarking paper (no new method); ProteinVista introduces a new architecture. Both have careful experimental design but differ in contribution type. |
| `/home/wg25r/review_agent/human_reviews_2026/f12Lo7ZUX5.md` (Reverse Distillation) | 6.50 | Stronger: clean theoretical framing, well-controlled experiments, no overclaiming issues. ProteinVista's narrative problems and scoping issues keep it below this level. |
| `/home/wg25r/review_agent/human_reviews_2026/RDerF20JYT.md` (La-Proteina) | 8.00 | Much stronger: SOTA results, novel architecture, extensive evaluation. ProteinVista is not in this tier. |

The paper has genuine contributions — demonstrating that a 3D CNN on full-atom voxel grids is tractable at scale and provides complementary signal to sequence models on binding tasks. The controlled experimental design, honest failure reporting, and informative ablations are strengths. However, the framing overreaches: "compute-efficient" is scoped to the model rather than the full pipeline, "outperforms sequence transformers" is narratively at odds with the contrastive alignment objective, and "atom-level" overstates the 5-channel resolution. These issues are repairable but material. Relative to the anchors, the paper sits above the weak papers (~2.8) and in the same band as the mid-tier papers (4.0–5.0), with genuine novelty that distinguishes it from purely incremental work but framing issues that prevent it from reaching the 6+ tier.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>