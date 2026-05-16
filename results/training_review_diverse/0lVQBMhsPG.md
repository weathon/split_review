Now I have a complete picture. Let me produce the final consolidated review.

## Summary

This paper proposes ETC, a text-to-video diffusion framework that removes all temporal attention layers and instead relies solely on spatial attention from a pre-trained T2I model. To adapt video data to spatial-only processing, the authors: (1) stitch video frames into a spatial grid (temporal-to-spatial transfer), (2) introduce Spatial-Temporal Mixed Embedding (ME) to distinguish intra- vs. inter-frame tokens, and (3) use a Triple-Data training strategy (caption-image, label-image, caption-video) to reduce reliance on expensive text-video pairs. The paper claims dramatic training efficiency (99% less data, 96% fewer training samples) and a 49% average FVD improvement over SOTA.

## Strengths

- **Spatial-only video generation is conceptually clean and practically motivated.** Removing temporal attention modules—which require training from scratch on large video datasets—directly addresses a real bottleneck in T2V. The approach is novel in taking this to a trained (not zero-shot) setting and is supported by a clear rationale: if zero-shot methods already exploit spatial attention for temporal coherence, a properly designed trained model should do even better.

- **Spatial-Temporal Mixed Embedding (ME) is a simple and demonstrably effective component.** The ablation (Table 2) shows that without ME the model produces a 17% error rate in stitching (incorrectly merging across frame boundaries), which drops to 0% with ME. FVD improves from 72.3 to 54.5. This is concrete evidence that the embedding solves a real failure mode and is not generic.

- **Training efficiency gains are empirically demonstrated.** Figure 2 shows the spatial-only model converges at ~15K steps vs. ~25K for the temporal-attention counterpart. The model uses only 0.9B parameters, achieves 1.92 FPS inference (~3× faster than LVDM), and the ablation on dataset size (Figure 7) shows that 100K videos are sufficient with no significant gain from scaling to 300K. These efficiency claims are supported by the data presented.

- **Triple-Data Driven Training (TDT) is a practical contribution for resource-limited settings.** By incorporating label-image data (FPS=0) and caption-image data (FPS=120) alongside video data, the method exploits abundant image data to reduce video requirements. FPS embedding sharing parameters with timestep embedding is a clean design choice.

## Weaknesses

### Major

- **The FVD results in Table 1 are not credible as reported and directly contradict the user study.** The paper claims ETC achieves dramatically better FVD than all baselines (e.g., a 49% average improvement). Yet the user study shows ETC and VideoCrafter2 as nearly tied, with VideoCrafter2 slightly preferred. If the FVD gap were as large as the numbers suggest, human evaluators would overwhelmingly favor ETC. This contradiction—an order-of-magnitude metric gap that evaporates in human preference—strongly suggests either the FVD computation is flawed (different resolution, frame count, feature extractor, or sampling protocol for baselines vs. ETC) or the numbers are not directly comparable. The paper's description of the baseline evaluation ("We equally sample 10k 256×256 videos for each baseline") is too vague to rule out a protocol mismatch, and no Section F appendix is available to verify the user study methodology or the reconciliation. This is the single most serious issue: if the FVD numbers are wrong, the paper's headline quantitative claims collapse.

- **Internal inconsistency between main results and ablation study erodes confidence.** The ablation on dataset size (Figure 7) reports FVD values in the range of ~300–400 (the y-axis label is not visible due to a parser artifact, but the text describes values in this range). Yet the main results (Table 1) report a zero-shot MSR-VTT FVD of ~25–65 depending on configuration. A model cannot have an order-of-magnitude *lower* FVD on an out-of-domain dataset (MSR-VTT, zero-shot) than on whatever evaluation set is used in the ablation, unless the metrics are computed under fundamentally different conditions. The paper never specifies the evaluation dataset for Figure 7, making this impossible to resolve from the text alone. This inconsistency needs to be explained before any quantitative claim can be trusted.

- **The core claim—that spatial attention alone learns temporal information—rests on a weak theoretical argument.** Section 3's "theoretical observation" merely notes that both spatial attention and spatial+temporal attention perform linear combinations of input tokens. This is true of almost any attention mechanism and does not establish that a single spatial attention layer can represent the same function class as spatial+temporal attention. The formulas presented ($\chi_s$ and $\chi_{st}$) are not derived and the substantive proof is deferred to Appendix B.2 (not available). The receptive field argument conflates spatial expansion (stitching frames enlarges spatial context) with temporal reasoning. The empirical evidence (Figure 2) compares differently initialized models (fine-tuning existing weights vs. training new layers from scratch), so faster convergence of the spatial-only model is expected and does not specifically demonstrate temporal modeling capability. The paper would benefit from controlled experiments isolating temporal coherence (e.g., frame consistency metrics, motion smoothness).

- **The "49% on average" claim is vague and undefined.** This number appears in the abstract and introduction but is never tied to a specific baseline or aggregation. The text says "improving FVD by 49% on average with only 1% training dataset" — it is unclear what "on average" averages over (datasets? baselines? metrics?). The introduction says "improves FVD by 49%" with reference to Figure 1, which only shows MSR-VTT. The lack of precision on the central quantitative claim is a significant presentation flaw.

### Minor

- **Baseline evaluation details are insufficient for reproducibility.** The paper states it "equally sample[s] 10k 256×256 videos for each baseline" but does not specify which checkpoints were used, what inference hyperparameters (sampling steps, classifier-free guidance scale, seed), or how baselines were configured for zero-shot evaluation. Since the reported baseline FVD values (e.g., LVDM at ~566 according to the reviewer) are far higher than typical reported results (~200–300), it is unclear whether the baselines were run suboptimally or under a different evaluation protocol. This makes the comparison unverifiable.

- **The framing of the training efficiency claim mixes incompatible comparisons.** The paper claims "99% reduction in training datasets" and "96% reduction in training samples" compared to "the optimal value of each metric." This is circular—the optimal metric value is from ETC itself—and conflates data volume (dataset size) with optimization cost (training steps × batch size). The claims are attention-grabbing but the comparison is apples-to-oranges since different methods use different datasets, different training budgets, and different hardware.

- **No statistical significance or variance reported.** All quantitative results (FVD, CLIP, user study percentages) are presented as point estimates with no error bars, confidence intervals, or runs. Given the small size of the filtered training set (100K), variance could be substantial, and single-run results are not reliable for drawing strong conclusions.

- **The limitation about resolution/frame-rate adaptation is handled inconsistently.** The method section (line 122) acknowledges that resolution changes require a "warmup process of several hundred steps," while the conclusion (line 267) states the model does "not support changes in resolution and frame rate without additional training." There is no actual contradiction—both say additional training is needed—but the wording in the conclusion sounds more restrictive than the method section, and the "warmup" vs. "additional training" framing is confusing. The paper should clearly state what it can and cannot do.

### Trivial

- The equation for spatial attention output (Section 3) appears to contain formatting artifacts (line 67: `\chi_{s t}(x)=\sum_{i=1}^{t}W_{s}^{T}\cdot x_{i}\cdot W_{T i}`) — the dimensions and indices are ambiguous.
- The FPS embedding description could benefit from a clearer explanation of why 7 specific FPS values [1,2,4,8,15,30,60] were chosen and how the model generalizes to unseen frame rates.

## Nice-to-Haves

- Provide FVD with confidence intervals and with standard evaluation protocols matched exactly across all baselines.
- Add quantitative temporal consistency metrics (e.g., frame-wise CLIP feature similarity, flow warping error) to directly measure temporal coherence.
- Clarify the evaluation dataset for the ablation study in Figure 7.
- Release evaluation code to allow independent verification of the FVD numbers.
- Tone down the comparative framing: the training efficiency gains are genuinely impressive even without claiming implausible FVD improvements.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing related works (AnimateDiff, VideoComposer, etc.)."** Per hard rules, I cannot confirm the existence/omission of specific related works, and this criticism demands breadth outside the paper's scope.
- **"The conclusion contradicts the earlier claim about resolution adaptation."** The paper says "warmup required" in both sections; there is no contradiction.
- **"The theoretical derivation is too vague (missing appendix B.2)."** The appendix exists in the original submission; reviewer complaints about deferred content are about parser-stripped sections, not author error.
- **"The 'overstates novelty' claim about related work."** Subjective opinion, not a verifiable weakness.
- **"User study missing Section F details."** Section F exists in the original submission; the core criticism (user study contradicts FVD) is retained separately.
- **"FPS values [1,2,4,8,15,30,60] are arbitrary."** The paper explains these are discrete values sampled from the dataset's 1–60 FPS range for convenience; this is a defensible implementation choice.
- **"No statistical significance for any metric."** This is a minor methodological gap but not fatal; kept in Minor above.
- **"The paper should use more methods/models preferred by the reviewer."** Disagreement on baseline selection is not a weakness.
- **"The 49% claim should be clarified"** — this is retained in Major as a real issue about precision of claims.

## Novel Insights

None beyond the paper's own contributions. The reviews largely amplify concerns the paper's own data creates (the FVD/user-study tension) and question the depth of the theoretical justification. Neither reveals a fundamentally new perspective that the authors themselves do not already discuss.

## Suggestions

1. **Recompute FVD under a fully matched evaluation protocol** — same frame count (e.g., 16), same resolution, same I3D feature extractor, same number of real video samples, and report all baseline numbers using their official checkpoints and recommended inference settings. If the FVD numbers change substantially, present the corrected results honestly.

2. **Reconcile the user study with the objective metrics** — either demonstrate that FVD is poorly correlated with human perception for this setting (which itself is valuable science) or acknowledge that the FVD advantage is smaller than claimed.

3. **Specify the evaluation set for Figure 7** and explain why the FVD range differs from Table 1.

4. **Run controlled experiments** that isolate temporal coherence: e.g., train two models with identical initialization, data, and compute—one with spatial-only attention (ETC) and one with a standard temporal attention baseline—and compare frame consistency quantitatively.

5. **Replace the weak theoretical argument** with a simple empirical demonstration (controlled ablation, temporal metrics) that directly supports the core claim rather than relying on the shallow linear-mapping argument.

## Score and Decision

The paper presents a genuinely interesting idea and several well-engineered components (ME, TDT) that clearly contribute to training efficiency. However, the evaluation is fatally undermined by an internal contradiction between the reported FVD numbers and the user study results, and by an unexplained inconsistency between the main results and ablation FVD ranges. Until these are resolved, the quantitative claims cannot be trusted. The paper also overclaims with vague percentages and lacks the controlled experiments needed to substantiate its core theoretical premise.

The contributions are promising enough to warrant a major revision and re-evaluation, but not acceptance in the current form.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>