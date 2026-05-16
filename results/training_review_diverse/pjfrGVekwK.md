Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

The paper proposes Variational Bayes Gaussian Splatting (VBGS), which frames Gaussian splat learning as variational inference over a generative mixture model with conjugate priors. By exploiting conjugacy between multivariate Normal likelihoods and Normal-Inverse-Wishart priors, the authors derive closed-form coordinate-ascent variational updates that naturally accumulate sufficient statistics across sequential observations, enabling continual learning without replay buffers. Experiments on Tiny ImageNet (2D), Blender objects (3D), and Habitat rooms evaluate both static reconstruction and continual learning performance against a gradient-based baseline.

## Strengths

- **Closed-form variational updates from conjugacy**: The core theoretical contribution is clearly derived (Eq. 11–12 and Section 3.3). The use of conjugate Normal-Inverse-Wishart priors yields analytic updates that aggregate sufficient statistics across observations, which is both elegant and practically useful. This is the central enabler of the paper's claims.

- **Theoretical guarantee of batch-sequential equivalence**: The paper proves (Section 3.3, line 233) that when assignments are computed using the initial variational parameters, the streaming update produces a posterior identical to batch processing. This is a strong theoretical property that Gradient descent cannot match, and the 2D image experiments (Figure 2a–b) verify it empirically — VBGS's final PSNR after sequential patch observation matches its static counterpart.

- **Competitive static 3D reconstruction**: Table 1 shows VBGS (Data Init) achieves the best PSNR on 5 of 8 Blender objects (drums 19.50, ficus 22.06, hotdog 23.62, lego 22.53, materials 20.55), matching or exceeding the Gradient baseline. This demonstrates that the variational formulation does not sacrifice static reconstruction quality.

- **Clear 2D continual learning demonstration**: In the 2D continual setting (Figure 2a–b), VBGS maintains stable PSNR across sequential image patches while the Gradient baseline catastrophically forgets. Here the comparison is well-controlled (same input modality, same data), and the advantage is substantial and unambiguous.

## Weaknesses

### Fatal
None.

### Major

- **Confusing and potentially contradictory 3D continual learning results (Section 4.2, lines 332–334).** The paper reports average PSNR of "11.19 ± 3.53 dB for VBGS (Random Init) and 21.26 ± 1.76 dB for Gradient (Random Init)" in the 3D continual setting. This is directly at odds with the paper's narrative that VBGS is superior in continual learning — Gradient is reported as ~10 dB higher. The text says "the same properties from the 2D experiment hold" and claims Gradient "deteriorates" (Figure 6b), yet the reported numbers tell the opposite story. If these are averages over the training trajectory (rather than final validation performance), this needs to be clearly stated and justified. If they are final PSNR values, they contradict Figure 6b which allegedly shows VBGS rising to ~20 dB and Gradient dropping. This discrepancy undermines confidence in the 3D continual experiments and must be resolved. The paper's central claim that VBGS "enables continual learning" for 3D data cannot be fully assessed from the current reporting.

- **Input modality asymmetry in 3D experiments not controlled.** As the paper explicitly states (line 294): "VBGS is trained on the 3D point cloud... In contrast, the gradient-based approach is optimized using multi-view image reconstruction." This means VBGS receives direct 3D coordinates while Gradient must infer 3D structure from 2D projections. While the paper acknowledges this as a limitation in the Discussion (lines 369–376), the acknowledgment does not resolve the confounding factor in the experiments. The static 3D comparison in Table 1 still favors VBGS in terms of information available, and the 3D continual comparison inherits the same confound. The 2D experiments do control for this, so the core continual learning claim is not invalidated, but the 3D-specific claims are weaker than they appear.

### Minor

- **Number of CAVI iterations in the static setting is never stated.** The paper says VBGS uses "a single update per observation" in the continual setting (line 273), but it is unclear whether the static results use one CAVI pass or multiple iterations until convergence. Since standard variational GMM fitting requires multiple E/M-style iterations, this matters for both reproducibility and for interpreting the "single update" claim. If the static results also use a single pass, how does that compare to multiple CAVI iterations? If they use multiple iterations, the "single update" characterization is only about the continual setting and should be clarified.

- **No ablation of the fixed color covariance.** The paper fixes \(\Sigma_{k,\vec{c}} = \varepsilon I\) with the justification that it "assures that the mixture components commit to a particular color" (line 138). No ablation is provided to quantify the impact of this design choice. A standard approach would be to compare against a learned color covariance (via NIW prior) or test sensitivity to the hyperparameter \(\varepsilon\).

- **The reassignment heuristic (Section 3.4) is ad hoc and not validated against alternatives.** The component reassignment mechanism is a practical engineering fix, not grounded in the variational objective. While Figure 5(b) shows it helps, there is no comparison to simpler alternatives (e.g., random reassignment, periodic reset of unused components) to isolate whether the ELBO-weighted sampling is crucial.

- **The reported "p=0" for the wall-clock t-test** (line 271) is technically not correct for continuous data — it should be \(p < 10^{-something}\). Moreover, the time difference (0.03 vs 0.05 seconds) is small enough that it may not be practically meaningful, especially since the Gradient method was not optimized for per-update efficiency (it uses 100 fixed steps).

- **The 3D continual experiment uses frames "randomly sampled from the environment"** rather than a trajectory (line 360). This is acknowledged but not discussed as a limitation. Sequential trajectories with spatial correlation (as in real SLAM) could produce different forgetting dynamics for both methods, potentially favoring or disfavoring either approach.

### Trivial

- The x-axis of Figure 1(a) is labeled "Number of components" but the specific component counts tested are not stated in the text or caption.
- The spatial-color conditional independence assumption (Section 3.1) is noted but not discussed as a limitation that may require more components when color varies systematically with position within a region.

## Nice-to-Haves

- Including a Gradient baseline with a replay buffer (e.g., keep last N frames, retrain with few steps) would directly test whether VBGS's closed-form accumulation is meaningfully better than the simplest practical alternative. The paper's current claim is that VBGS "eliminates the need for replay buffers," but the baseline to substantiate this (Gradient + replay) is absent.
- Ablating the fixed color covariance (e.g., allowing NIW on \(\Sigma_c\)) to isolate the effect on both reconstruction quality and forgetting.

## Removed Points

These points are flagged to be removed by the reviewer instructions; treat them with caution.

- **Criticism about "unfair comparison" as a fatal flaw**: The harsh critic frames the input modality asymmetry as a structural issue invalidating the paper's central claims. However, (1) the 2D continual experiments are well-controlled and already demonstrate the core claim, (2) the static 3D comparison (Table 1) is asymmetric but VBGS still performs competitively on most objects despite Gradient having less information to work with, and (3) the paper openly acknowledges this as a limitation. The asymmetry is a Major weakness, not Fatal.

- **Criticism that "continual learning baseline is a strawman" because no replay buffer is used**: The Gradient baseline represents naive continual learning (SGD without memory), which is the standard reference point for demonstrating catastrophic forgetting. The paper's contribution is that VBGS does not *need* replay buffers — comparing against naive SGD is the appropriate first step. Including a replay baseline would strengthen the paper, but its absence does not make the comparison invalid or a "strawman." This is a Nice-to-Have, not a weakness.

- **Criticism about missing related work**: Removed per instructions as I cannot verify related work coverage without external sources.

- **Formatting/style nitpicks and complaints about missing appendix content**: Removed per instructions (parser artifacts).

- **Criticism about code existence/release status**: Removed per instructions (do not question availability of cited artifacts).

- **Criticism about the 2D experiment not specifying which component counts are used in Figure 1(a)**: Downgraded to Trivial (minor presentation gap).

- **The harsh critic's claim that "the gradient method must infer 3D structure from 2D projections alone, whereas VBGS has direct 3D coordinates" makes the comparison invalid**: As noted above, this is a real asymmetry but does not invalidate the paper — the static results show VBGS is competitive despite (or because of) this, and the 2D continual results control for it entirely.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear tension between the paper's strong theoretical contribution and the messiness of its 3D experimental reporting, but do not generate insights outside what the authors themselves provide.

## Suggestions

1. **Resolve the PSNR discrepancy in 3D continual results**: Clarify whether "average reconstruction error over all objects of 11.19 ± 3.53 dB" refers to final validation PSNR or an average over the training trajectory. If the latter, state this explicitly and also report final PSNR. If the former, explain why VBGS achieves 11.19 dB when Figure 6b suggests ~20 dB. Ensure the numbers and figures tell a consistent story.

2. **State the number of CAVI iterations used in the static setting explicitly** in Section 4.1. If it's a single pass, say so; if multiple, state how many.

3. **Add a replay buffer baseline** for at least the 2D continual setting to substantiate the "without replay buffers" claim against a practical alternative.

4. **Add an ablation of the fixed color covariance** (e.g., allow \(\Sigma_c\) to be learned) to justify the design choice empirically, or at minimum state that this is a design choice and leave sensitivity analysis for future work.

## Score and Decision

The paper presents a clean theoretical idea (variational Bayes for Gaussian splats with closed-form continual updates) and provides reasonable evidence for its 2D continual learning claims. However, the 3D continual learning results contain a confusing numerical discrepancy that directly contradicts the paper's narrative and prevents proper evaluation of the claimed 3D advantage. Combined with the input modality asymmetry in 3D comparisons and the absence of a replay buffer baseline, the experimental evidence for the 3D claims is not yet convincing. The paper's theoretical contribution is real, but its empirical validation — particularly for 3D continual learning — needs substantial cleanup before acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>