Now I have sufficient calibration data. Let me write the consolidated review.

## Summary

CBGBench unifies structure-based drug design (SBDD) tasks as a "fill-in-the-blank" graph completion problem on 3D protein-molecule complexes. It provides a modular codebase implementing 12 SBDD methods under a common framework, extends evaluation to four lead-optimization subtasks (linker, fragment, side-chain, and scaffold design) beyond standard *de novo* generation, introduces novel metrics (LBE, MPBG, interaction-pattern analysis via PLIP), and conducts case studies on two GPCR targets. The benchmark is a substantial service contribution to the community.

## Strengths

- **Unified task formulation and taxonomy.** The paper formalizes SBDD as fill-in-the-blank of a 3D complex binding graph and provides a three-axis taxonomy (voxelized/continuous, one-shot/autoregressive, domain-knowledge/data-driven) that cleanly categorizes 12 methods (Table 1, Figure 2). This is the first systematic categorization enabling modular extensibility.

- **Extension to four practically relevant lead-optimization subtasks.** The benchmark adapts methods to linker, fragment, side-chain, and scaffold design with dedicated datasets from CrossDocked2020 (Table 2, Figure 3), evaluating 6 methods per task (Table 8). This goes well beyond the de-novo-only scope of prior SBDD benchmarks and provides the first structured comparison across these tasks.

- **Novel and interaction-aware evaluation metrics.** Beyond standard metrics, CBGBench introduces LBE (ligand binding efficacy) to correct for molecule-size bias in Vina scores, MPBG to measure binding-gap improvement, and JSD/MAE over 7 PLIP interaction-type distributions. These address known confounds (e.g., Pearson correlation of -0.67 between Vina energy and atom count, Section 4) and provide richer signal than raw docking scores alone.

- **Public, modular, unified codebase.** The codebase at https://github.com/EDAPINENUT/CBGBench implements all 12 methods with shared data preprocessing, training, sampling, and evaluation pipelines. This substantially lowers the barrier to entry and supports reproducible future research in a field where method-specific codebases have been a persistent obstacle.

## Weaknesses

### Fatal
None.

### Major

- **Training-protocol confounds undermine the cross-method rankings.** The paper trains all methods for 5M iterations but acknowledges that "autoregressive methods exhibit a faster convergence rate of loss, typically requiring only a few tens of thousands of epochs to reach the final best checkpoint" (Section 5.1.1). This means one-shot diffusion models receive orders of magnitude more training signal relative to convergence while autoregressive models are overtrained. Further, different message-passing backbones are used for different method classes — "GVP and EGNN with GAT, as message-passing modules of auto-regressive and diffusion-based models, respectively" (Section 5.1.1) — which method identity with architecture choice. The paper states this is done "to eliminate the effect brought about by the architecture of GNNs," but the actual effect is that method comparisons conflate generation paradigm with backbone choice. The aggregated rankings in Table 7 cannot be unambiguously attributed to the methods' generation strategies.

- **Subtask experiments use inconsistent training regimes.** For the four lead-optimization subtasks, autoregressive methods are "pretrained on *de novo* generation and finetuned" while diffusion-based models are "trained from scratch because the zero-center-of-mass technique is shifted from employing protein geometric centers to using molecule context's ones" (Section 5.2). This introduces an uncontrolled confound: the autoregressive methods have seen orders of magnitude more data. The reported rankings across subtasks (Table 8) are therefore not comparable among methods using different training protocols. The paper acknowledges this difference in passing but does not assess its impact.

- **The ranking methodology depends on arbitrary weights.** The overall ranking (Table 7) uses ad-hoc weights of 0.2 (substructure), 0.2 (chemical), 0.4 (interaction), and 0.2 (geometry). These weights are not justified. LiGAN ranks 5th overall but 1st in interaction; a small shift in interaction weight would change rankings materially. The paper presents MOLCRAFT as the clear winner, but this depends entirely on the chosen weighting scheme. Per-aspect rankings are transparently reported, but the strong "winner" claims outrun the methodology.

### Minor

- **Real-world consistency claim is overstated.** The paper concludes that benchmark results are "mainly consistent with those obtained on real-world disease targets" (Section 5.3). However, in the ADRB1 case study, D3FG (ranked 6th in *de novo* generation) "exhibits superior performance" on binding affinity (Section 5.3.1), while the benchmark leader MOLCRAFT performs comparably to TARGETDIFF (ranked 3rd). The degree of consistency is partial, and the paper's hedge ("mainly") does not fully address the gap. The t-SNE overlap conclusions (Figure 4) are based on visual inspection without quantitative distributional distance measures.

- **Case-study evidence is qualitative and limited.** The t-SNE visualizations (Figure 4) are interpreted visually without quantitative metrics (e.g., KL divergence of fingerprint distributions). The case study covers only two GPCRs (ADRB1, DRD3), which are structurally related, limiting diversity. The GEOM-DRUG random control uses 100 molecules, but sampling representativeness is not discussed.

- **No variance or statistical significance reported.** No standard deviations or confidence intervals are reported across multiple runs or seeds. Given the stochasticity of generative models, it is unclear whether observed differences (e.g., between TARGETDIFF and DECOMPDIFF) are meaningful or noise.

- **The key diagnostic insight about incorrect binding-site localization is plausible but unvalidated.** The paper attributes autoregressive methods' high clash ratios to "incorrect binding site localization" (Section 5.1.2), but no ablation isolates this mechanism.

### Trivial

- Figure 4 (t-SNE) and Figure 5 (violin plots) are referenced in the text as separate "Conclusions and Discussions" sections but their discussion interleaves observations across models without systematic comparison.
- The explanation of the "LogP reference range" ranking rule (LogP within [-0.4, 5.6] gets rank 1, outside gets rank 2) is given only in the de novo setup but not explained in the evaluation protocol section.

## Nice-to-Haves

- Reporting computational cost (training time, inference speed) per method would help practitioners understand practical trade-offs.
- An ablation comparing a diffusion method under both GVP and EGNN backbones on a single task would isolate whether backbone choice dominates method differences.
- For the subtask experiments, a controlled comparison with all methods trained from scratch (or all finetuned) would remove the training-regime confound.
- A sensitivity analysis of the ranking weights (e.g., reporting top-3 under weight perturbations) would increase robustness of the ranking claims.

## Removed Points

- *Missing validity rate*: The paper references Appendix E.4 for validity rate details; the appendix is stripped by the parser. Removed per hard rule.
- *Missing 2D/SMILES baselines*: The paper scopes itself to 3D-conditioned generation and acknowledges this boundary. Removed as scope creep.
- *Cross-contamination in subtask datasets*: Speculative concern without evidence. Removed.
- *Taxonomy not exhaustive*: No taxonomy is exhaustive; this is not a meaningful weakness. Removed.
- *"Fill-in-the-blank not leveraged for theoretical insights"*: Asks the paper to be something it is not. Removed.
- *Missing code link or reproducibility concerns*: The code link is provided in the abstract. Removed per hard rule.
- *Typo/formatting nitpicks*: Removed per hard rules on formatting artifacts.

## Novel Insights

The reviews surface an interesting tension: the harsh critic identifies several genuine experimental-control issues (training-protocol asymmetry, backbone substitution, arbitrary ranking weights), while the strength finder characterizes the paper's training standardization as a strength ("eliminating confounds that plagued prior comparisons"). Both observations are partially correct — the paper's attempt to standardize training (same iteration count, unified docking engine) is a real step forward, but it introduces new confounds (overtraining autoregressive methods, swapping architectures) that are not present in the original method implementations. This suggests that truly fair SBDD benchmarking may require a multi-axis design: (1) a "as-published" comparison using each method's original architecture and training protocol, and (2) a "controlled" comparison using a common backbone and protocol, with the gap between the two explicitly characterized. The paper's framework provides the infrastructure to do this, but currently only executes the second axis imperfectly.

## Suggestions

1. **For the subtask experiments, retrain all methods from scratch under a common protocol**, or alternatively finetune all methods from a common pretrained checkpoint. Either choice removes the training-regime confound.
2. **Report per-metric rankings as the primary result** and relegate the weighted overall rank to a secondary analysis. The field would benefit from seeing "MOLCRAFT best on geometry, LiGAN best on interaction" rather than a single aggregate winner.
3. **Quantify the case-study comparisons** using distributional distance metrics (e.g., Wasserstein distance on Vina energy, KL divergence on fingerprint histograms) instead of visual t-SNE inspection.
4. **Add variance estimates** (standard deviations across 3-5 seeds) for key metrics to determine whether method differences are statistically meaningful.
5. **Provide a simple ablation** comparing one diffusion method under both GVP and EGNN backbones to show whether architecture choice dominates method differences.

## Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/review_agent/human_reviews/xoUUCS9IGl.md` (PoseCheck) | 4.75 | 1 | Less comprehensive benchmark (fewer methods, fewer metrics, no subtasks, no codebase). CBGBench is substantially stronger. |
| `/home/wg25r/review_agent/human_reviews/IjiIPQcLbV.md` (SDDBench) | 4.00 | 1 | Narrower scope (single metric, SBDD evaluation only). CBGBench is much more comprehensive. |
| `/home/wg25r/review_agent/human_reviews/S8gbnkCgxZ.md` (Bioactivity Prediction) | 7.00 | 1 | Dataset + benchmark paper with rigorous evaluation, accepted. Cleaner evaluation but different subfield. |
| `/home/wg25r/review_agent/human_reviews/KSLkFYHlYg.md` (ShEPhERD) | 8.00 | 1 | Novel method + application, Oral. Different paper type. |
| `/home/wg25r/review_agent/human_reviews/9qS3HzSDNv.md` (DynamicFlow) | 6.20 | 2 | Method paper (accepted). Cleaner experimental design than CBGBench. |
| `/home/wg25r/review_agent/human_reviews/qH9nrMNTIW.md` (IPDiff) | 6.25 | 2 | Method paper (accepted). Focused method contribution with proper controls. |
| `/home/wg25r/review_agent/human_reviews/p5VDaa8aIY.md` (Small Mol. Optim. w/ LLMs) | 5.75 | 2 | Method paper (rejected). Similar score range. |
| `/home/wg25r/review_agent/human_reviews/g3VCIM94ke.md` (DrugFlow) | 6.67 | 2 | Method paper (accepted). Strong experimental rigor. |

**Round 1 bracket:** The paper sits above the weak anchors (PoseCheck at 4.75, SDDBench at 4.00) but below the strong anchors (ShEPhERD at 8.00, Bioactivity Prediction at 7.00). Initial bracket: 5.0–7.0.

**Round 2 narrowing:** Compared to accepted method papers (DynamicFlow at 6.20, IPDiff at 6.25, DrugFlow at 6.67), CBGBench has more experimental confounds in its central comparisons (training protocol asymmetry, backbone substitution, arbitrary ranking weights). These confounds prevent it from reaching the 6+ acceptance level typical of well-controlled method or benchmark papers. However, CBGBench's scope and infrastructure contribution are larger than the rejected method paper at 5.75. This places it at approximately 5.5.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>