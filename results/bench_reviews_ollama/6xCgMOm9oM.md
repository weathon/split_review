Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

The paper introduces Learned Farthest Point Sampling (LFPS), a method that bridges algorithmic and learned point cloud downsampling by proposing a loss function designed to enforce FPS-like uniformity while allowing task-adaptive point selection. A selection network predicts per-point scores, and the loss combines a uniformity-enforcing term (penalizing nearby selected points) with a score-enforcing term. The authors present a theoretical argument (termed a "theoretical sketch") that the loss minima reproduce FPS-equivalent distance properties in the 2D continuous case, and extend the loss with importance-weighted sampling for adaptive density.

## Strengths

- **Well-motivated problem framing and clean loss design**: The gap between algorithmic sampling (uniform but non-adaptive) and learned sampling (adaptive but lacking uniformity guarantees) is genuine and clearly articulated. The loss function (Eq. 4) elegantly combines a similarity-weighted neighbor penalty with a score enforcement term `(1-s_i)²`, and the reasoning behind each component is clearly explained. The loss encourages points to be spread out like FPS while being trainable end-to-end.

- **Plug-in compatibility with architectures where sampling precedes feature computation**: Unlike prior learned methods (S-Net, SampleNet, APES) that require features at sampling time, LFPS decouples importance value computation from point selection (Section 3.3), enabling integration into architectures like Point-M2AE where downsampling occurs before feature extraction. This is demonstrated by replacing FPS in Point-M2AE and improving accuracy from 92.4% to 92.8%.

- **Substantial runtime improvement for large-scale point clouds**: Section 4.1.4 reports sampling 25K points from 100K takes ~5s with FPS versus 46ms with LFPS (a >100× speedup). This directly supports the claim that LFPS is a practical alternative for large cloud processing where FPS is a bottleneck.

- **Systematic ablation studies validating parameter behavior**: Fig. 5 shows the empirically optimal range for `k` (24–32) aligns with the theoretically predicted range for `R_E`. Fig. 6 confirms the weighting parameter space behaves as expected—excessive `p_u/p_l` deviation increases variance, while insufficient deviation prevents learning. These ablations provide useful practical guidance and connect theory to practice.

- **Qualitative evidence showing meaningful LFPS vs. FPS differences**: Fig. 7 effectively illustrates that while LFPS closely approximates FPS coverage, it avoids sampling uninformative regions (e.g., between stool legs), providing an intuitive demonstration of the method's advantage.

## Weaknesses

### Fatal
None

### Major

- **Theoretical contribution is overstated relative to what is actually proven**: The abstract claims "theoretical proof that its minima guarantee a uniformity comparable to FPS" without any dimensional qualification. The Theorem in Section 3.2 is explicitly restricted to a "bounded R² region" (2D continuous case), while all experiments are on 3D discrete point clouds. Even within this restricted setting, the paper itself labels the argument a "theoretical sketch" (Section 3, p. 43), yet the conclusion calls it a "rigorous theoretical framework" (p. 182). Critically, the actual loss used in experiments—Eq. 4 (discrete, kNN-based) and Eq. 5 (weighted with per-point `R_E` and importance weights)—deviates substantially from the continuous Voronoi-based form analyzed in the theorem, and no argument connects the 2D continuous result to the 3D discrete regime. This is not a fatal flaw—the loss design is still well-motivated and the intuitions are sound—but the paper significantly oversells the theoretical grounding.

- **Experimental validation is narrow for the breadth of claims made**: The paper claims LFPS provides "enhanced performance across various tasks" and is a "plug-in alternative for algorithmic sampling methods." The evidence supporting this consists of replacing only the **last** sampling layer in two architectures on one dataset each, with modest improvements (68.3%→70.2% mIoU on S3DIS with PTv2; 92.4%→92.8% on ModelNet with Point-M2AE). The M2AE improvement of 0.4% is well within typical run-to-run variance for this benchmark, and no standard deviations or confidence intervals are reported for any downstream result. Only one learned sampling baseline (APES) is compared in architecture integration, and APES performs poorly—leaving the question of whether LFPS's advantage comes from the method itself or from APES's specific weaknesses. The experiments replacing only the last layer (where point clouds are already small) do not demonstrate the claimed runtime benefit in the architecture setting.

### Minor

- **R_E estimation heuristic lacks principled justification**: The paper estimates R as the 1st quartile of kNN distances to ensure "R_E slightly overestimates R" (p. 92), but this choice is driven by initial experiments rather than theoretical analysis. The degree of overestimation affects whether the theorem's ε condition holds, and no analysis is provided for why the 1st quartile is the right quantile. This is a practical concern rather than a theoretical one since the ablations empirically validate the k range.

- **O(n) complexity claim is potentially misleading**: The paper states LFPS is O(n) "excluding the k-nearest neighbor computations." While the paper argues kNN is "generally required for network operations regardless," the ResNet processes k neighbors per point, giving O(nk) complexity. The 100× speedup claim over FPS is valid in practice but the complexity characterization should be more precise.

### Trivial
None

## Nice-to-Haves

- Extending the theoretical analysis to the 3D discrete case, even partially (e.g., showing gradient properties), would substantially strengthen the bridge between theory and practice.
- Reporting standard deviations across multiple runs for downstream task results and comparing against additional learned sampling baselines beyond APES.
- Replacing FPS in earlier (larger) downsampling layers where LFPS's speed advantage would be more impactful, demonstrating the runtime claim in an end-to-end architecture.
- Convergence analysis: reporting training loss values and comparing them to the predicted minimum would more directly connect theory and practice.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh critic: "The proof itself is a narrative sketch, not a rigorous derivation"** — While the proof is indeed informal, the paper itself labels it a "theoretical sketch." The real issue is the *overclaiming* (calling it "rigorous" in the conclusion), not that a sketch is presented as a sketch. Subsumed into the Major weakness about overstated theory.

- **Harsh critic: APES being the only baseline, no comparison with S-Net, SampleNet, etc., in integration** — Subsumed into Major weakness on narrow experimental validation. However, note that the paper does provide a reasonable argument for why some methods (S-Net, SampleNet, ADS) cannot integrate into these architectures (Section 2, p. 36).

- **Strength Finder: "Theoretical guarantee that the proposed loss function reproduces FPS-like uniformity at its minima"** — This is overstated. The theorem covers only 2D continuous, not the discrete kNN-based or weighted losses used in experiments. Kept as a weakened version noting the qualification.

- **Harsh critic: "2000 training steps with no convergence analysis"** — The paper does report metrics averaged over the last 100 steps (p. 153), providing some convergence evidence. Whether 2000 steps is sufficient is debatable but not clearly insufficient.

## Novel Insights

The most interesting tension in this paper is the mismatch between its clean intuitions and its inability to formally close the loop from theory to practice. The loss function design is genuinely elegant—the combination of a similarity-weighted neighbor penalty with score enforcement is a principled way to enforce FPS-like spread in a differentiable pipeline. But the theoretical result, while providing intuition, applies to a regime (2D continuous, Voronoi neighborhoods, unweighted) that differs from every experimental configuration tested. The paper would be stronger if it presented the theory as motivation and intuition (which it does well) rather than as a proof of guarantee (which it does not deliver), and if it invested more in empirical validation that compensates for the theoretical gap.

## Suggestions

- Rewrite the abstract and conclusion to accurately scope the theoretical contribution: replace "theoretical proof that its minima guarantee a uniformity comparable to FPS" with language like "we provide a theoretical argument showing that in the 2D continuous case, loss minima reproduce FPS-equivalent distance properties, and we empirically validate that this intuition extends to 3D discrete point clouds."
- Report mean ± std over at least 3 runs for Table 1 and the M2AE accuracy comparison, so readers can assess whether the 0.4% improvement is statistically meaningful.
- Replace FPS in at least one earlier downsampling layer (handling more points) to demonstrate that the runtime advantage materializes in an end-to-end setting, not just in standalone benchmarks.

## Score and Decision

The paper presents a well-motivated and elegant loss function design for learned point cloud downsampling, with strong ablation studies and a compelling runtime advantage. However, the theoretical contribution is significantly overstated (2D continuous only, labeled as a sketch yet claimed as rigorous), and the experimental validation is too narrow for the breadth of the claims (two architectures, one dataset each, last layer only, no variance reporting, single weak baseline). The core idea is sound and useful, but the paper needs to be more honest about the scope of its theory and provide more comprehensive empirical evidence.

**Originality**: Moderate — the loss function design is novel and elegant, but the theoretical contribution is limited in scope.  
**Research question importance**: High — bridging algorithmic and learned sampling is a practical need.  
**Claims support**: Weak — the main theoretical claim is overstated and experiments are narrow.  
**Experimental soundness**: Moderate — ablations are thorough but downstream validation is thin.  
**Clarity**: Good — well-structured and clearly written.  
**Community value**: Moderate — the loss design and plug-in capability are useful contributions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>