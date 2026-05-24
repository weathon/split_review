I have thoroughly analyzed the paper and all reviewer claims. Let me now write the consolidated review.

## Summary

This paper proposes a lightweight, architecture-agnostic regularizer for dynamic NeRFs that uses sliced-Wasserstein distance to penalize divergence between pixel intensity distributions rendered from a fixed camera pose at nearby timestamps. The core hypothesis is that under smooth motion, pixel intensity distributions from a fixed camera remain approximately stable over short intervals, so enforcing this via optimal transport provides a simple, model-free training signal. The method renders random pixels (not full images), uses bilinear interpolation to full resolution, then computes the sliced-Wasserstein distance between distributions at different timestamps. Experiments integrate the regularizer into DNeRF, HyperNeRF, Nerfies, TiNeuVox, and Hexplanes on the iPhone dataset and the HyperNeRF interpolation dataset.

## Strengths

- **Architecture-agnostic and lightweight design, clearly demonstrated.** The regularizer requires no external models (no depth estimator, no optical flow, no LPIPS network) and integrates into five distinct dynamic NeRF backbones without modifying their architectures. This is a genuine practical advantage over prior regularizers that depend on off-the-shelf deep models.

- **Consistent improvements on the challenging iPhone dataset across multiple architectures.** Table 1 reports that the regularizer improves performance across DNeRF, HyperNeRF, Nerfies, TiNeuVox, and Hexplanes. The paper shows the regularizer helps across a diverse set of backbones (MLP-based, voxel-based, hybrid), supporting the claim of broad applicability.

- **Outperforms prior regularization approaches that use external models.** Table 4 compares against depth-based, LPIPS-based, scene-flow, sparsity, and random-background regularizers on TiNeuVox. The OT regularizer achieves better performance without the computational overhead and domain-gap risks of external-model-based regularizers. This directly validates the paper's core motivation.

- **Practical sampling strategy is a meaningful engineering contribution.** Rendering random pixels (256–512) instead of full-resolution images and then interpolating to full resolution before computing the sliced-Wasserstein distance avoids the prohibitive cost of full-image rendering while maintaining distributional signal. This design choice is nontrivial — the paper shows it works better than alternatives (Table 3) and explains why standard LPIPS/structured-patch methods cannot use random sampling.

- **Clear ablation on distance metrics validates the choice of sliced-Wasserstein.** Table 5 compares MMD, Sinkhorn, and sliced-Wasserstein, showing sliced-Wasserstein yields best performance while also being computationally cheaper than MMD ($O(n\log n)$ vs. $O(n^2)$).

## Weaknesses

### Fatal

None.

### Major

- **Title claims "convergence" but the paper never measures convergence.** The paper's title is "Improving the Convergence of Dynamic NeRFs via Optimal Transport," yet there are zero training curves, loss-vs-iteration plots, PSNR-vs-iteration plots, or any measurement of convergence speed. All experiments report final quality metrics (likely PSNR/LPIPS). The "convergence" in Theorem 1 refers to sampling convergence (empirical distribution → population distribution), not training convergence of the NeRF. The paper does not actually show that the regularizer helps models converge faster or to a better solution trajectory — only that the final output is better. This is a significant disconnect between the title and the evidence presented.

- **Efficiency claims are unsubstantiated by runtime or memory measurements.** The paper repeatedly claims the regularizer is "lightweight," "efficient," and avoids "substantial computational overhead," but provides no runtime (seconds per iteration) or memory (GPU memory usage) comparisons. The $O(n\log n)$ complexity of sliced-Wasserstein is stated but never benchmarked against the actual wall-clock overhead of the full NeRF pipeline. Without measurement, it is impossible to assess whether the computational savings over LPIPS or depth-based regularizers are practically meaningful or swamped by NeRF's own rendering cost.

- **Theorem 1 does not ground the core claim about NeRF convergence.** The theorem is a standard finite-support concentration bound for the 1-Wasserstein distance (the empirical estimate converges to the population distance at rate $O(\sqrt{|\Omega|^2/n})$). It bounds *sampling error*, not the effect of the regularizer on training dynamics or final reconstruction quality. The paper frames the theory as providing "theoretically grounded" support for the regularization strategy, but the theorem is disconnected from why minimizing OT distance between pixel distributions should improve NeRF optimization. Additionally, the bound depends on $|\Omega|$ (the number of distinct pixel intensities), which is implicitly assumed to be finite — a strong assumption for continuous rendered values. This overclaiming weakens the paper's framing.

### Minor

- **No per-scene breakdown or error bars for Table 1.** Results are reported only as averages across 10 iPhone sequences. Without per-scene numbers or variance estimates, the reader cannot tell whether the gains are consistent across scenes or driven by a few outliers. This is standard practice for the field and should be included.

- **Pixel-distribution invariance assumption validated on only one toy example.** The central hypothesis ($\mathcal{P}(\mathbf{r}_{t,p}) \approx \mathcal{P}(\mathbf{r}_{t+\Delta t,p})$) is illustrated with a single sequence (Figure 1). The paper acknowledges in Limitations that it "assumes smooth motions and can fail with abrupt scene dynamics," but provides no quantitative analysis of when or how badly the assumption degrades, and no experiment showing the regularizer's performance under controlled violations of the assumption (e.g., fast motion, lighting change, occlusion onset). The limitations mention "a pixel averaging effect" and "slight blur" but these are never quantified.

- **Some implementation details are underspecified.** (a) How the "fixed camera pose" is selected during training is not stated — is it a random training pose, a specific held-out pose, or the pose from the current batch? (b) "Bilinear interpolation with soft smoothing" (used to interpolate random pixel samples to full resolution) is vague; what exactly "soft smoothing" means is not defined. (c) The regularizer weight $\beta=0.1$ is given, but how it interacts with the NeRF's primary losses (e.g., rendering MSE, flow loss for some models) is not discussed. These details matter for reproducibility.

- **Limited benefit on strong baselines for the HyperNeRF interpolation dataset.** The paper honestly notes that on this dataset, "HyperNeRF and Nerfies baselines already performed well in this setting and our regularization did not have much effect." While TiNeuVox benefited significantly, the regularizer's impact on already-strong models was negligible. This tempers the generality claim somewhat.

### Trivial

None.

## Nice-to-Haves

- A controlled experiment varying model capacity (e.g., TiNeuVox with fewer channels) to test whether the regularizer's benefit correlates with baseline quality would be informative.
- Reporting the $\Delta t$ scheduling strategy (the paper mentions tuning per scene would improve results but fixes it to 0.1 for robustness) would help practitioners.

## Removed Points

These points were removed from the review for the reasons stated below; they should be treated with caution if referenced in discussion.

1. *"The claim that existing regularizers 'enforce priors that are averaged over large datasets, which may lead to domain gaps' is not supported"* — Removed. This is a motivation statement in the Introduction, not an empirical claim requiring experimental validation. It describes a known weakness of pretrained models generally, not a specific result being asserted.

2. *"Ignores prior work that uses optimal transport for video or image sequence regularization"* — Removed per hard rule: "DO NOT mention missing related works, as you do not have external sources to confirm their existence." This cannot be verified from the paper alone.

3. *"Algorithm 1 pseudocode was stripped by the parser, so the exact loss computation loop is invisible"* — Removed per hard rule: parser artifacts (stripped figures, missing formatting) should not be treated as author errors. Algorithm 1 exists in the original submission as a figure.

4. *"The experimental validation is dominated by a single model (TiNeuVox)"* — Removed as an overstatement. While TiNeuVox shows the largest gains, on the iPhone dataset (Table 1) all five architectures show improvement. The claim that results are "dominated by a single model" misrepresents the iPhone dataset results.

5. *"Results are too small to distinguish from noise"* — Removed. This is speculative without error bars. The lack of error bars is a genuine weakness (kept above), but the specific claim of noise-level results is not substantiated.

6. *Strength Finder: "Theoretically grounded convergence rate"* — Partially removed from Strengths. The theorem exists and is correct, but it bounds sampling convergence, not training convergence. Included as a qualified strength above but not as strongly as the Strength Finder claimed.

7. *Strength Finder: "Table 2 shows similar gains on the HyperNeRF interpolation dataset"* — Tempered. The paper itself states HyperNeRF and Nerfies baselines "already performed well and our regularization did not have much effect." The strength overstated the benefit.

8. *"The $O(|\Omega|^2 / n)$ rate is not obviously favorable"* — Removed. This is an opinion without analysis showing the bound is actually problematic at practical image sizes. The bound is what it is for a concentration inequality of this type.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a recurring pattern: the paper proposes a genuinely simple and useful idea but would benefit from more rigorous evaluation (convergence curves, runtime analysis, per-scene breakdowns) to match the scope of its claims.

## Suggestions

1. **Add convergence curves.** Show PSNR/LPIPS vs. training iteration with and without the regularizer for at least 2–3 architectures/scenes. This directly supports the paper's title and quantifies whether the benefit is faster convergence, better final quality, or both.
2. **Report runtime and memory overhead.** Measure seconds-per-iteration and peak GPU memory with and without the regularizer, and compare against at least the LPIPS regularizer baseline. This substantiates the efficiency claims.
3. **Provide per-scene results with variance.** For Table 1, include per-sequence metrics alongside the average, or show error bars across multiple runs. This allows readers to assess consistency.
4. **Clarify implementation details.** Specify: (a) how the fixed camera pose is selected each iteration; (b) what "soft smoothing" means in the bilinear interpolation; (c) how $\beta=0.1$ balances with the NeRF's other losses (is the OT loss added directly? scaled by a factor?).
5. **Re-title or re-scope the paper.** Either add convergence experiments and keep the title, or retitle to something like "Improving Dynamic NeRF Quality via Optimal Transport Regularization" to match the actual evidence.

## Score and Decision

The paper presents a clean, intuitive idea with a practical design (random sampling + sliced-Wasserstein) that demonstrably improves multiple dynamic NeRF architectures and outperforms existing regularization approaches. The core contribution is real and well-motivated. However, there is a meaningful gap between the claims and the evidence: the title promises "convergence" analysis but provides none, the efficiency claims lack runtime measurements, and the theoretical framing overstates the connection between Theorem 1 and the method's effectiveness. These are addressable issues — the idea is sound — but in its current form, the evidence is not fully commensurate with the claims made.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>