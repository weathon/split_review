- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 6, 5
Now let me write the final consolidated review.

## Summary

This paper introduces CuDeRes (Cubic Decay Reservoir Network), a reservoir-computing model with three direction-specific reservoirs and exponential spatial decay for anomaly detection in 3D Ground Penetrating Radar (GPR) data within the Learning in Model Space (LMS) framework. Each 3D GPR data block is fitted by CuDeRes to produce a compact readout model that captures multi-directional dynamics, and anomaly detection is performed via nearest-neighbor distance in model space using only normal training data. The method is evaluated on real-world 3D GPR data (cement and asphalt roads) and achieves an F1-score of 0.9789 for anomaly detection and clustering accuracy of 0.9537 for anomaly type identification, substantially outperforming the reported baselines.

## Strengths

1. **Three-reservoir architecture with direction-specific spatial decay is a novel and well-motivated design for 3D GPR data.** Section 3.1.1 (Equations 1–4) defines separate reservoir weight matrices for x-, y-, and z-directions and an exponential decay matrix **E** that differentially weights each direction. This directly addresses the paper's motivation that GPR data exhibit distinct spatial scales and dynamics in different directions — a genuine gap in prior LMS methods for 3D data (Section 2.2).

2. **Compact readout model enables practical model-space learning.** Section 4.2 explicitly notes that a standard ESN readout would be size 200×16×reservoir size (impractical), whereas CuDeRes produces a readout of size 3×reservoir size. This compactness makes nearest-neighbor search (Section 3.3.1) and clustering (Section 3.3.2) computationally feasible and is a concrete engineering improvement.

3. **Strong anomaly detection performance using only 100 normal training blocks.** Table 2 reports CuDeRes at F1=0.9789. The method demonstrably outperforms both voxel-based (Patchcore-3D, STEAL, 3D-VAE, MemAE) and image-based (f-AnoGAN, SimpleNet) anomaly detection baselines by a large margin, despite those methods also operating in the few-normal-sample regime.

4. **Category-discriminative model space enables effective clustering of anomaly types.** Table 3 shows CuDeRes with K-Means achieving Accuracy=0.9537, ARI=0.9291, NMI=0.9428, while the best pre-trained 3D CNN feature (R(2+1)D with AC) achieves at most 0.6109, 0.5829, and 0.5843 respectively. This directly supports the claim that different subsurface anomalies produce distinct dynamics captured by CuDeRes.

5. **Distance metric between fitted models is closed-form and directly computable.** Equation 9 derives a p-norm distance proportional to (1/3)‖W₁^{out}−W₂^{out}‖² + (β₁−β₂)², enabling straightforward nearest-neighbor discrimination without additional learning or model inversion.

## Weaknesses

### Fatal

None.

### Major

1. **Insufficiently documented baseline comparisons undermine the reported performance gap.** Section 4.2 lists seven baselines (Patchcore-3D, STEAL, 3D-VAE, MemAE, f-AnoGAN, SimpleNet, and CuDeRes w/o E) but provides **no details** on how each was adapted to 3D GPR data (16×200×200 blocks). Critical missing information includes: (a) how image-based methods (SimpleNet, f-AnoGAN) were applied to 3D data — as multi-channel images? with what preprocessing? (b) what hyperparameters, architectures, or training procedures were used for each baseline, and whether any tuning was performed for the GPR domain; (c) confirmation that all baselines received the same 100 normal training blocks under identical data splits. Without this information, the reported superiority (CuDeRes F1=0.9789 vs. best baseline f-AnoGAN F1=0.585) is unverifiable — the gap could simply reflect suboptimal baseline configuration rather than genuine methodological advantage.

2. **No uncertainty/confidence estimates despite stochastic components.** The paper states "we report the mean metric under five different random seed settings" (Section 4), but Tables 2 and 3 show no standard deviations, confidence intervals, or per-seed breakdowns. Since reservoir weights are randomly initialized (standard normal distribution, Section 4), results may vary across runs. Reporting means without variance is insufficient to establish reliability.

### Minor

3. **Spatial decay mechanism is described imprecisely, though it functions as claimed through recurrence.** The critic claims the decay is merely a per-direction constant scaling factor. This is **incorrect**: through the recurrence in Equation (1), the decay factor e^{−θΔx} is applied at every step along the traversal path, so the contribution of a point k steps back is approximately multiplied by e^{−kθΔx}. The mechanism **is** distance-dependent through cumulative recurrence. However, the paper's description (e.g., "the introduced spatial decay reduces the influence of distant points and assigns greater importance to nearby points" on line 109, and "automatically adapt to varying scales" on line 117) could be more precise. The effect emerges from the recurrent architecture, not from a direct distance-weighted kernel as the phrasing might suggest. Clarifying this would strengthen the paper.

4. **Anomaly detection threshold is a fixed heuristic without validation.** The threshold is set as "the average of the pairwise distances between normal models" (Section 4). No sensitivity analysis is provided, and it is not checked whether this threshold generalizes across different road types or data conditions. Since the threshold directly determines precision/recall trade-off, this weakens the reported F1-score as a reliable performance measure. Reporting AUC-ROC (which does not require a threshold) or a precision-recall curve would be more informative.

5. **No hyperparameter sensitivity analysis.** Key hyperparameters (reservoir size=50, decay rate θ=1, regularization λ=1, spectral radius=0.9) are set to defaults without any ablation or sensitivity study. Given that these parameters control the core dynamics of CuDeRes, understanding their effect on downstream anomaly detection performance is important.

6. **No analysis of the Echo State Property (ESP) for the modified hidden-state dynamics.** The paper mentions ESP for standard ESNs (Section 2.3) but does not analyze whether CuDeRes's non-standard hidden-state equation (three reservoirs, spatial decay matrix, specific iteration order) satisfies the ESP. This is a gap in theoretical grounding.

### Trivial

7. Equation (5) in the extracted text shows only one component [h(x_a, y_{b-1}, z_c)] rather than the full concatenation of three previous hidden states from all three directions. This is a formatting/presentation issue; the surrounding text correctly describes a 3-direction concatenation.

## Nice-to-Haves

- **Include a simple data-space baseline** (e.g., nearest-neighbor in raw 3D patches after normalization, or PCA + k-NN) to calibrate how much the model-space transformation improves over direct comparison.
- **Density-based clustering** (e.g., DBSCAN) would be more appropriate than K-Means/AC/FCM for anomaly clustering, since the number of anomaly types may be unknown in practice.
- **Quantify separability** in model space (e.g., Silhouette score on the unclustered models) rather than relying solely on qualitative t-SNE visualization (Figure 6).

## Removed Points

- "Spatial decay is a structural flaw / does not implement distance-dependent decay" — REMOVED. Through recurrence in Equation (1), the decay factor is applied at every step, making the effective influence of a point k steps back proportional to e^{−kθΔx}. The mechanism works as claimed, though the description could be clearer.
- "Equation (5) is garbled" — REMOVED (formatting artifact, per rules).
- "Iteration order imposes a strict causal order that is arbitrary" — REMOVED. The described order (x-innermost, z-outermost) ensures all three predecessors are available at each point; this is standard and functional.
- Several generic criticisms (e.g., "the evaluation lacks rigor" phrased broadly without specific anchor) merged into the documented specifics above.
- Strength Finder item about "visualization confirms separation" — demoted from a core strength; Figure 6 is qualitative and would benefit from quantitative metrics (kept in Nice-to-Haves).

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses did not surface a perspective not already present in the paper or naturally following from it. The spatial-decay-via-recurrence clarification noted above is a detail of mechanism, not a novel insight about the problem or method.

## Suggestions

1. **Document every baseline's adaptation to 3D GPR data** in detail: data preprocessing, hyperparameter search ranges, training procedures, and the specific data split used. Add a supplement with full configuration details.

2. **Report standard deviations** (or per-seed results) for all main experiments, especially given the reservoir's random initialization.

3. **Include AUC-ROC** as a threshold-free metric, or validate the chosen threshold via cross-validation within the normal training set using synthetic outlier injection.

4. **Add a hyperparameter sensitivity study** for reservoir size, decay rate θ, and regularization λ to demonstrate robustness.

5. **Clarify the spatial decay description** in Section 3.1.1: explicitly note that the per-step decay factor e^{−θΔx} accumulates over the recurrence, so the effective weighting of a point decays exponentially with its distance from the current position.
