Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

TAPE3D introduces a feed-forward method for dense 3D pixel tracking from monocular video. It employs a coarse-to-fine strategy: tracking at reduced resolution using a joint global-local spatial attention mechanism (with sparse anchor tracks providing global context and local self-attention capturing fine detail), followed by a transformer-based upsampler to recover high-resolution predictions. The paper further identifies log-depth as the optimal depth representation for 3D tracking through systematic analysis. The method runs over 8× faster than prior 3D trackers and achieves state-of-the-art results on CVO (2D dense tracking), Kubric3D (dense 3D tracking), and competitive results on TAP-Vid3D and LSFOdyssey.

## Strengths

- **Large efficiency gain without sacrificing accuracy:** TAPE3D completes dense tracking of 100 frames in under two minutes, 8× faster than SceneTracker and 30× faster than SpatialTracker (Table 3), while simultaneously achieving better accuracy. The speedup stems from a well-motivated coarse-to-fine design and the proposed attention architecture, not from engineering tricks.

- **Joint global-local spatial attention is a concrete architectural innovation:** The design (Figure 3③) combines global cross-attention via sparse anchor tracks (providing scene-level context) with dense local self-attention (capturing fine spatial details). The ablation in Table 6b shows both components are necessary (EPE worsens from 1.25 to 1.48 without local attention). The anchor-track variant matches CoTracker's global-only accuracy (EPE 1.37 vs 1.40) at lower computational cost and, critically, enables end-to-end patchwise training without train-test resolution mismatch.

- **Attention-based upsampler outperforms standard alternatives:** The transformer-based upsampler (Section 3.3) with spatial bias (Alibi-style) substantially outperforms RAFT's CNN upsampler (EPE 1.25 vs 1.62, Table 6c) and all non-learnable baselines. Figure 4 provides supporting visual evidence of sharper motion boundaries.

- **Log-depth identified as the optimal representation for 3D tracking:** Section 3.4 provides a principled analysis comparing raw depth, inverse depth, and log-depth, and Table 6a confirms log-depth yields substantially higher 3D tracking accuracy (AJ 20.7 vs 16.2 for inverse depth, vs 13.9 for raw depth). The rationale — scale invariance of depth-change ratios, alignment with monocular depth estimation training, and connection to optical expansion — is well articulated.

- **Consistent results across diverse benchmarks:** TAPE3D achieves SOTA on CVO (Table 2, >10% EPE improvement over DOT), Kubric3D (Table 3, >15% improvement in AJ and APD_3D), and generalizes to in-the-wild videos on TAP-Vid3D (Table 5) and LSFOdyssey (Table 4). The 2D-only results on CVO usefully isolate the architectural contribution from the depth-related components.

## Weaknesses

### Fatal
None.

### Major

- **TAP-Vid3D comparison transparency is insufficient.** The paper re-evaluates SpatialTracker and SceneTracker using their public code and notes that results "differ slightly from the numbers reported in the TAP-Vid3D paper" (line 163). While the internal comparison across methods is fair (all run under the same pipeline), the paper does not explain what causes the discrepancy — different depth estimator version, frame sampling, pre/post-processing, visibility threshold, or something else. This omission undermines confidence in the precise magnitude of improvement, particularly when margins are narrow (e.g., DriveTrack with ZoeDepth: 32.8 vs 32.1 AJ; DriveTrack with UniDepth: 33.2 vs 32.2 AJ). Without documenting the standardized evaluation protocol, a reader cannot assess whether the advantage is robust or an artifact of the evaluation setup.

### Minor

- **No variance or confidence information reported.** All tables report single numbers without error bars, standard deviations, or multiple-seed results. While deterministic evaluation on fixed benchmarks is standard in this field, several comparisons involve small margins (e.g., 1-point AJ differences on sub-datasets in Table 5), and some ablation differences are also modest. A brief statement about result stability (e.g., bootstrapping over test videos or reporting training seed variance for one key benchmark) would substantially strengthen confidence in the reported numbers.

- **Loss weighting is asymmetric and not ablated or justified.** The loss uses λ₂d=100, λ_depth=1, λ_vis=0.1 (line 134) — a 100:1 ratio favoring 2D over depth supervision. The paper states these were set "empirically" but provides no ablation showing that this imbalance does not harm 3D accuracy or that alternative weightings perform similarly. Given that the method is called TAPE*3D*, the lack of analysis for a design choice that heavily prioritizes 2D coordinates is a gap.

- **Missing key numerical specifications for reproducibility.** The patch size h′×w′ used for training and the number of anchor tracks M are not given concrete values (M is only "≈10²," and h′×w′ is left as N′ without a number). These are first-order parameters: patch size directly determines training resolution, and M controls global context quality. A brief sensitivity analysis for M would also be informative.

- **Ablation studies are limited to single benchmarks.** The depth representation ablation (Table 6a) is performed only on TAP-Vid3D, and the attention/upsampler ablations (Tables 6b, 6c) only on CVO-Extended. Showing that the log-depth advantage and attention design conclusions also hold on Kubric3D (the dense 3D benchmark) would strengthen the claims, especially since the latter is the paper's own controlled dataset.

### Trivial
- Notation inconsistency: the depth correlation term in Eq. 1 (line 48) uses `D_t^i` (consistent with trajectory index i), but the text description (line 54) uses `D_t^m` with subscript m.
- The △ notation in Table 1 marks prior methods as "extremely time-consuming" for dense tracking, but no approximate runtime is given for those methods at dense resolution to contextualize "extremely."

## Nice-to-Haves
- Release the exact evaluation pipeline (data loading, depth estimator version, frame selection, visibility threshold) used for all methods on TAP-Vid3D to resolve the comparison-transparency concern.
- Provide a runtime breakdown showing time per component (coarse tracking, upsampling, depth loading) to help readers understand where the 8× speedup originates.
- Add a failure case analysis (e.g., examples of tracking failure under extended occlusion, with error distributions) as a complement to the limitations discussion in the Conclusion.

## Removed Points

The following points from the input reviews are removed or substantially weakened:

- **"First feed-forward dense 3D tracker" claim needs sharper framing.** *Removed.* The paper already qualifies this with "efficiently" (lines 18, 37) and Table 1 marks prior methods with △ ("technically applicable but extremely time-consuming"). The claim is accurate as stated. The reviewer's concern about "unnecessary contention" is speculative and not grounded in a factual error in the paper.

- **CVO-Extended validation / selection concern.** *Removed.* The paper states (line 151) that this split is used "following the comparison in DOT (Le Moing et al., 2024)" — the split was introduced by prior work, not by this paper. This is not a weakness attributable to the authors.

- **Missing training hyperparameters and training data diversity concerns.** *Removed.* The paper's "Training details." paragraph (line 136) appears to contain a table or figure stripped by the PDF parser. Details such as learning rate, batch size, and optimizer are likely there. Diversity of synthetic training data is standard practice and not a substantive weakness.

- **Upsampler comparison misses FlowFormer/VideoFlow upsamplers.** *Removed.* The comparison includes non-learnable baselines and RAFT's CNN-based upsampler, which is the most common baseline in this line of work. The scope of comparison is adequate to demonstrate the proposed upsampler's advantage.

- **"△ notation not quantified" / "qualitative comparison missing same-video baselines" / "runtime breakdown" / "failure case analysis."** *Moved to Nice-to-Haves or Trivial.* These are genuine suggestions for improvement but not weaknesses in the current work; several are explicitly noted as limitations by the authors (Conclusion, line 195).

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an unanticipated implication, limitation, or connection that the paper itself does not address or that provides a genuinely new perspective.

## Suggestions

1. **Document the TAP-Vid3D evaluation pipeline** — provide the exact configuration used for all methods (depth estimator version, frame selection, visibility threshold, any post-processing) in detail or via a code release. If the re-evaluated numbers differ from the original papers, explain the likely cause.

2. **Add a multi-run or bootstrapped variance estimate** for at least one key comparison to establish that the reported improvements are outside the noise level of the evaluation. This need not be extensive — a single benchmark with 3 training seeds or video-level bootstrapping would suffice.

3. **Ablate the loss weighting** (λ₂d:λ_depth:λ_vis) to verify the 100:1 ratio does not sacrifice 3D accuracy, and provide the concrete training patch size h′×w′ and anchor-track count M (or a sensitivity curve for M).

4. **Run the depth representation ablation (Table 6a) on Kubric3D** to confirm the log-depth advantage is not dataset-specific.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>