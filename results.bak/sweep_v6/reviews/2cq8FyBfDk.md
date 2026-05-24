Now I have enough information to write the consolidated review. Let me compose it.

---

## Summary

ProteinVista introduces a 123M-parameter full-atom 3D CNN that voxelizes protein heavy atoms at 1.0 Å resolution, uses adaptive cubic grids to reduce memory waste, and is pre-trained contrastively against ESM-2 (or via Rosetta score regression) on ~500k AlphaFold2 structures. On transporter-substrate classification, enzyme-substrate classification, and drug-target IC₅₀ regression, ProteinVista alone outperforms ESM-2 (650M parameters) while using ~1% of the GPU-hours and two orders of magnitude less pre-training data. An ensemble with ESM-2 further improves accuracy on the classification tasks, demonstrating that sequence and structure signals are complementary.

## Strengths

- **Outperforms sequence transformers on structure-dependent tasks.** Table 1 shows ProteinVista alone achieves higher accuracy (90.8% vs. 89.3%), MCC (0.77 vs. 0.74), and precision (0.85 vs. 0.79) than ESM-2₆₅₀M on transporter-substrate prediction; Table 2 shows ProteinVista’s IC₅₀ R² (0.69) clearly exceeds both ESM-2 variants (0.60–0.61) with a Wilcoxon p-value < 10⁻³⁰⁴. This is the paper's core empirical contribution and is well supported by the evidence.

- **Dramatic compute and data efficiency.** ProteinVista (123M params) pre-trains in 48 hours on 4 A100 GPUs vs. ESM-2₆₅₀M requiring ~7 days on 128 H100 GPUs. Per-sample inference is ~20× faster (20 vs. 426 seconds per 1k proteins on an A100). These efficiency claims are clearly quantified in Section 4.3 and Figure 3.

- **Demonstrated complementarity with sequence models.** The ESM-ProteinVista ensemble in Table 1 improves over either model alone (MCC 0.79 vs. 0.74 on TSP; 0.82 vs. 0.79 on ESP), with McNemar’s tests giving p < 10⁻¹³ and p < 10⁻¹⁷. The stratified analysis in Figure 2 (by sequence identity, TM-score, and pLDDT) further corroborates that the two modalities capture non-redundant information.

- **Well-designed architectural choices.** The adaptive voxel grid (choosing the smallest of four box sizes) is a sensible engineering advance over fixed-size 3D grids. Continuous Gaussian density voxelization (σ=1 Å) reduces discretization artifacts compared to binary occupancy grids. The ablation study (Figure 2e) cleanly isolates which design decisions matter most.

- **Open-source release.** The paper commits to an easy-to-use Python implementation, which would enable community adoption.

## Weaknesses

### Fatal
None.

### Major

- **No comparison against any structure-aware baseline.** The introduction positions ProteinVista relative to graph-based structure encoders (GearNet, ESM-GearNet), arguing they "omit atom-level details" and "only slightly outperformed the sequence-only ESM-2 baseline" (citing Zhang et al., 2023b). Yet the paper never evaluates against any of these methods. Without this comparison, the reader cannot assess whether the 3D CNN adds value beyond existing structural approaches or merely matches what graph-based models already achieve. This is the most significant gap in the evaluation.

### Minor

- **Point estimates without variance.** All results are reported as single-point estimates without standard deviations or confidence intervals across random seeds. While significance tests (McNemar's, Wilcoxon) are provided, single-run results make it difficult to assess robustness of small improvements (e.g., 0.5–1% gaps on ESP).

- **Abstract slightly overclaims the standalone model's SOTA status.** The abstract says ProteinVista "surpasses current best methods" for transporter/enzyme substrate prediction, but the standalone model achieves 90.8% accuracy on TSP vs. SPOT's 92.4% (Table 1). The SOTA results (93.2% TSP, 94.4% ESP) come from the ESM-ProteinVista_OP ensemble, not ProteinVista alone. This mismatch is clarified in the main text but the abstract's phrasing is imprecise.

- **Pre-training objective conflates structure and sequence signals.** The contrastive pre-training aligns ProteinVista's embeddings to ESM-2's, which is effectively a form of knowledge distillation from a sequence model. The ablation showing that Rosetta-only pre-training yields nearly identical downstream performance (only ~1% worse) mitigates this concern but does not fully resolve it. A cleaner control (e.g., contrastive pre-training against a random ESM-2 mapping, or no pre-training) would more convincingly attribute gains to 3D geometry.

- **Limited task scope.** The paper evaluates on three binding-related tasks (all requiring pocket-level recognition) plus one GO term prediction task where ProteinVista underperforms ESM-2. This is a narrow slice of protein function tasks. Demonstrating value on additional structure-sensitive problems (e.g., mutation stability prediction, protein-protein interaction scoring) would strengthen the generality claim.

- **SOTA comparison pipeline differs substantially from the direct comparison.** The optimized pipeline (OP) in Section 3.3 involves joint fine-tuning of the small-molecule encoder and a contrastive network on top, making it difficult to isolate ProteinVista's contribution from the improved training protocol. The SOTA methods SPOT and ProSmith-ESP are not characterized in terms of their own pipeline details (e.g., whether they use experimental or predicted structures, what protein encoder they employ).

### Trivial

- The five heavy-atom channels (C, N, O, S, P) omit halogens and metal ions that are important in drug-target interactions. This is acknowledged implicitly but not discussed as a limitation.

- Only discrete 90° rotations and axis-mirroring are used for augmentation. The ablation shows that at inference time, averaging five views is essential, suggesting rotational invariance is not fully learned.

- GO term prediction results (Section 3.4) are under-reported — only Fmax is given without dataset details or significance tests for the gap.

## Nice-to-Haves

- An ablation that disentangles structure from pre-training supervision: pre-train ProteinVista with contrastive alignment to random-sequence ESM-2 embeddings (or without any alignment) to measure how much performance comes from 3D geometry vs. the injected ESM-2 signal.
- Grad-CAM or saliency maps on the voxel grid to directly visualize which 3D regions drive predictions.
- Analysis of IC₅₀ performance stratified by pocket size, ligand flexibility, or pLDDT (extending the analysis done for TSP).
- Including protein dynamics (multiple conformations) as the discussion suggests.

## Removed Points

- *"No comparison against structure-aware baselines is fatal."* — Downgraded from Fatal to Major because the paper's explicit claims are about outperforming sequence transformers, not graph models. The introduction's discussion of graph methods is motivation, not a central claim.
- *"IC50 ensemble performs worse contradicts complementarity narrative."* — Removed because the paper already discusses this (Section 3.2, lines 437: "sequence- and homology-based information is relevant for broad classification problems, whereas detailed affinity prediction requires high-resolution structural context").
- *"Ablation showing 1.5Å resolution only loses 1.1% contradicts importance of resolution."* — Removed because this is simply a finding about robustness; it does not invalidate any claim.
- *"Ablation showing no effect of training augmentation contradicts importance of augmentation."* — Removed because the paper isolates where augmentation matters (pre-training, not fine-tuning), which is a nuanced finding, not a contradiction.
- *"GPS-Fun operates at sub-residue granularity, so claim about omitting atom-level details is too sweeping."* — Removed because the characterization is generally correct; GPS-Fun still uses a graph abstraction.
- *"Compute comparison lacks profiling details."* — Removed because the comparison is at the systems level, not a profiling study.
- *Strength Finder's generic strengths about "important problem"* — Removed generic phrasing; only specific strengths with concrete evidence are kept.

## Novel Insights

The most interesting finding is that structure and sequence complementarity is task-dependent and asymmetric. On broad classification tasks (TSP, ESP), the ensemble outperforms either modality alone. On the more fine-grained IC₅₀ regression, the sequence model actually *hurts* performance when combined (ensemble R² 0.68 vs. ProteinVista alone 0.69), which the paper attributes to sequence noise. This suggests that high-resolution affinity prediction is dominated by geometric signal and that sequence-level homology information can be distracting — a useful counterpoint to the prevailing trend of always fusing modalities. The stratified analysis by pLDDT further reveals that ProteinVista's advantage is concentrated on high-confidence structures, indicating that future improvements in structure prediction quality (from better AlphaFold versions or experimental structures) would directly translate to downstream gains.

## Suggestions

1. **Add at least one structure-aware baseline** (GearNet, ESM-GearNet, or equivariant GNN) under identical conditions. This is the single change that would most strengthen the paper.
2. **Report means and standard deviations** over 3–5 random seeds for all main results.
3. **Tone down the abstract's SOTA claim** to distinguish standalone ProteinVista from the ensemble.
4. **Add a control pre-training objective** (e.g., contrastive against random ESM-2 alignments, or no pre-training) to better attribute gains to 3D geometry.

## Score and Decision

**Calibration anchors (from retrieval):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| /home/.../6MRm3G4NiU.md (SaProt) | 7.33 | Stronger: evaluates on 10 diverse tasks with cleaner structural integration; the current paper has narrower scope |
| /home/.../sTYuRVrdK3.md (ProteinWorkshop) | 6.25 | Comparable depth but different contribution (benchmark vs. method); the current paper has stronger per-task results |
| /home/.../BEH4mGo7zP.md (Seq/Struct/Surface pretraining) | 5.75 | Similar contribution: multi-modal pretraining, accepted. Current paper has clearer improvements vs. baselines but fewer tasks |
| /home/.../itGkF993gz.md (MAPE-PPI) | 5.67 | Similar tier: structure-aware method with solid evaluation. Current paper has stronger compute efficiency results |
| /home/.../iBAWiEjogY.md (ProteiNexus) | 3.67 | Weaker: data leakage concerns, missing baselines, unclear improvements. Current paper is substantially stronger |
| /home/.../5lUdTogEL3.md | 1.00 | Not comparable (unrelated topic, score-1 paper) |

The paper is clearly better than ProteiNexus (3.67) and sits in the same band as the 5.5–6.0 anchor papers. It provides convincing evidence for its core claim (outperforming sequence transformers), but the missing structure-aware baseline and narrow task scope prevent it from reaching the level of SaProt (7.33). Relative to the anchors, a score of **5.5** best reflects the paper's strengths and limitations.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>