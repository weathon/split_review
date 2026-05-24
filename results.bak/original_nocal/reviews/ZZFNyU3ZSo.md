Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper presents UniMoD, a task-aware Mixture-of-Depths (MoD) method for unified multimodal transformers. Through empirical analysis of attention weights, ARank metrics, and task interactions across models like Show-o and Emu3, the authors find that token redundancy varies significantly by both task and layer. They propose separate routers per task with ARank-guided layer selection and pruning ratios. Experiments on Show-o and Emu3 show 15–40% FLOP reduction while maintaining or improving most benchmark scores.

## Strengths

- **Systematic empirical analysis across tasks and layers in unified transformers (Sec. 3).** The paper examines attention weight patterns (Fig. 2), ARank redundancy metrics (Fig. 3), layer-skipping experiments (Table 1), and task interactions (Sec. 3.4) across Show-o, JanusFlow, Emu3, and Lumina-mgpt. Observations 3 and 4 directly show that generation and understanding tasks have different redundancy levels and that redundancy varies with layer depth — these findings are novel for unified transformers and directly motivate the task-specific router design.

- **The competitive pruning experiment (Sec. 3.4, Fig. 4) provides concrete evidence for asymmetric token importance.** Using Gumbel-Softmax with limited capacity (0.5), the paper demonstrates that generation tokens are almost always retained while understanding tokens are more aggressively pruned. This is a direct empirical justification for separate task routers rather than a single shared router.

- **UniMoD achieves meaningful FLOP reduction (15–40%) with generally modest performance impact across two diverse architecture families.** Table 3 shows reductions from 51.1→43.3 TFLOPs (Show-o) and 89.0→53.5 TFLOPs (Emu3) while most benchmark scores remain within a small margin of the full-computation baseline. The method scales to larger models (8B, 20% FLOP reduction) and extends to pure diffusion models (DiT, PixArt).

- **Ablation studies (Table 5) decompose the contribution of each design component.** Removing the task-aware router (single router, same layers) degrades GenEval from 0.61 to 0.50, and removing the ARank-based layer switch module drops it further to 0.50 with worse understanding scores, supporting both design choices.

## Weaknesses

### Major
*None*

### Minor

- **The "maintaining or improving performance" claim is somewhat overstated.** Several understanding benchmarks show small drops: Show-o GQA 56.3→54.5, VQAv2 68.3→66.2; Emu3 GQA 46.0→45.2, POPE 76.0→74.7, VQAv2 54.8→53.9 (Table 3). While the drops are small (1–3 points) and some other benchmarks improve, the paper would benefit from more precise language such as "maintaining performance within a small margin on most benchmarks."

- **The Basic MoD ablation's GenEval collapse (0.62→0.15, Table 5) is unexplained.** This extreme drop from the standard single-router MoD baseline is not diagnosed — it could indicate an implementation issue (e.g., routing capacity set too aggressively), a training stability problem, or a genuine limitation. Since the "w/o task-aware router" ablation (also a single router at specific layers) achieves GenEval 0.50, the collapse appears specific to the Basic MoD configuration rather than a general failure of single-router approaches. The paper should explain this discrepancy.

- **Training speed improvements are modest relative to FLOP reductions, and "x/iter" is undefined.** FLOPs drop 15% for Show-o but training speed improves only ~2–4% (1.30→1.27/1.25 x/iter); for Emu3, FLOPs drop 40% but speed improves 21% (3.56→2.80 x/iter). The unit "x/iter" is never defined in the paper (Table 4). The paper notes overhead as the reason but provides no profiling or wall-clock measurements to substantiate this. Clarifying the metric and explaining the gap (perhaps with a breakdown of compute vs. overhead costs) would significantly strengthen the efficiency claims.

- **Ablation TFLOPs differ despite claiming identical pruning rate.** The paper states "each ablation experiment maintains the same pruning rate as our method" (Sec. 5.3), yet Table 5 shows Basic MoD at 40.8 TFLOPs and "w/o task-aware router" at 40.8 TFLOPs while UniMoD is at 43.3 TFLOPs. If the pruning rate is truly the same, the TFLOPs should match; this discrepancy needs explanation (e.g., task-specific routers having different parameter counts or capacity distributions).

- **Main baselines operate at very different FLOP budgets.** Interleaved Layer Skipping and EarlyExit (Table 3) prune ~50% of FLOPs (25.6 vs. 51.1 TFLOPs baseline), while UniMoD prunes ~15%. The severe performance collapse of these aggressive baselines is expected — comparing them against a 15%-pruning method is not an apples-to-apples evaluation of routing strategy quality. The ablation table (Table 5) provides more comparable baselines and should be emphasized as the primary evidence; the main table should ideally include a single-router MoD at comparable FLOP reduction.

### Trivial

- Table 3: "UniMod" has inconsistent capitalization (should be "UniMoD" to match the paper's convention).

## Nice-to-Haves

- An iso-FLOP comparison between UniMoD and alternative pruning strategies (e.g., uniform token dropout, learned token merging) at the same TFLOPs would further isolate the benefit of task-aware routing.
- Statistical significance / error bars on the main results (Table 3) would help assess whether small benchmark differences are meaningful.

## Removed Points

*These points were raised by reviewers but are removed from the main evaluation for the reasons noted.*

- **"First work" claim is inaccurate (MoMa).** Removed: The paper claims "first work to propose a *task-aware* token pruning method." MoMa (Lin et al., 2024b) uses a single shared router for pruning, not task-specific routers. The paper explicitly discusses MoMa and distinguishes its own contribution (Sec. 2.2). The claim is defensible.
- **Layer importance inconsistency (early layers important, method prunes late layers).** Removed: This misreads the paper. Table 1 shows early layers are *critical* (don't prune them), late layers are *less important* (have more redundancy per ARank, Fig. 3). Pruning tokens in late layers is fully consistent with this finding.
- **Competitive pruning experiment confounded by loss weighting.** Removed: This is speculation. The paper does not report loss weighting that would bias the result; the auxiliary loss is symmetric.
- **Emu3 re-implementation is not reproducible.** Removed: The paper transparently discloses the dataset substitution and acknowledges results differ from the original Emu3 paper. The internal consistency of the comparison (UniMoD vs. its own full-computation baseline) is what matters for evaluating the method.
- **Attention weight analysis is never used to inform the method.** Removed: The paper explicitly states (Sec. 3.2) that the analysis shows "the importance of image and text tokens varies across tasks" and concludes "during pruning, we consider redundancy in tokens from all modalities" — directly informing the design.
- **Missing wall-clock measurements.** Removed: TFLOPs-based efficiency reporting is standard practice for training-time evaluation (following DiT, Peebles & Xie, 2023). Wall-clock would be a nice addition but is not a required standard.
- **ARank selection not ablated.** Removed: The "w/o layer switch module" ablation (Table 5) explicitly replaces ARank-guided selection with interleaved layers. This is an ablation of the layer selection heuristic.

## Novel Insights

None beyond the paper's own contributions. The synthesis of the two reviews does not surface an unexpected observation that the paper itself does not already make.

## Suggestions

- **Clarify the "x/iter" metric** in Table 4 and provide a breakdown of why FLOP reduction does not translate linearly into speedup (e.g., profiling of compute vs. overhead costs).
- **Diagnose the Basic MoD GenEval collapse** (0.15 in Table 5): is it due to over-aggressive pruning of generation tokens, training instability, or a routing misconfiguration? This diagnosis would strengthen the paper's central argument for task-aware routers.
- **Resolve the TFLOPs discrepancy** in the ablation table: explain why "same pruning rate" produces different TFLOPs across configurations.
- **Tone down the "maintaining or improving" claim** to "maintaining performance within a small margin on most benchmarks" to better match the empirical results.
- **Add error bars or multiple-run statistics** to the main benchmark results (Table 3) to establish whether the small drops on some understanding benchmarks are statistically significant.

## Score and Decision

**Originality:** The paper's core idea — task-aware MoD routers for unified transformers — is a novel adaptation of existing MoD techniques, grounded in a systematic analysis of task-specific redundancy patterns. The innovation is incremental but not trivial.

**Importance of research question:** Unified transformers are an active and important area, and improving their training efficiency is a meaningful contribution.

**Claims support:** Mixed. The central claim (task-aware routing outperforms task-agnostic pruning) is supported by ablation studies, but the "maintaining or improving performance" claim is slightly overstated, and efficiency claims would benefit from better-justified metrics.

**Soundness of experiments:** Adequate architecturally (two model families, ablation studies, scaling experiments) but has notable gaps: unexplained Basic MoD collapse, TFLOPs discrepancy in ablations, undefined speed metric.

**Clarity:** Generally clear, though the "x/iter" notation is confusing and the ablation TFLOPs inconsistency is unexplained.

**Value to community:** Moderate. The empirical analysis of redundancy patterns is useful, and the task-aware routing design is a practical contribution that others building unified transformers could adopt or build upon.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>