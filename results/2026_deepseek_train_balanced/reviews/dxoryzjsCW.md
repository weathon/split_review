## Summary

This paper proposes Diff-II, a diffusion-based data augmentation method that improves upon prior work (Da-Fusion, Diff-Mix) by generating synthetic training images that are *both* faithful to their category *and* diverse in context. The method has three stages: (1) learning per-category concept embeddings via LoRA + textual inversion, (2) computing DDIM inversions of training images and randomly interpolating pairs from the same category using spherical interpolation/extrapolation, and (3) two-stage denoising where an early stage uses a context-injecting suffix prompt and a later stage refines category details. Experiments on few-shot (4 datasets × 2 backbones), long-tailed (CUB-LT, Flower-LT at IF 10/20/100), and OOD (Waterbird) classification show consistent improvements over six prior diffusion-based DA methods.

---

## Strengths

- **Inversion interpolation within same-category pairs is a genuinely novel approach to the faithfulness–diversity trade-off.** Unlike intra-category DA (faithful but homogeneous) or inter-category DA (diverse but suffers from soft-label ambiguity), interpolating DDIM inversions of two same-category images preserves semantic consistency while generating new contexts. The ablation (Table 4) confirms that the interpolation component independently improves accuracy, and adding extrapolation further boosts both LPIPS diversity and accuracy.

- **Two-stage denoising with a controllable split ratio provides a practical faithfulness–diversity control mechanism.** Figure 6 empirically demonstrates that increasing the split ratio *s* raises LPIPS substantially while CLIP score declines only slowly, allowing practitioners to tune the augmentation's behavior per task. This design capability is absent in prior diffusion-based DA methods.

- **Consistent empirical improvements across a broad evaluation suite.** Across all 10 few-shot configurations (Table 1), all 6 long-tail configurations (Table 2), and all 4 OOD groups (Table 3), Diff-II outperforms every comparison method in every reported setting. The gains are non-trivial (e.g., +3.6% over Diff-Mix on CUB-LT, +11.39% over no augmentation on Waterbird), and the performance advantage is systematic rather than cherry-picked.

- **The paper honestly characterizes its limitation with single-sample categories.** The authors transparently show that the gain shrinks as the imbalance factor increases (from 5.8% at IF=10 to 0.86% at IF=100), providing a clear failure-mode analysis that strengthens the paper's credibility.

---

## Weaknesses

### Major

1. **The DDIM inversion update equation (Eq. 4) is mathematically incorrect as written.** The paper states:

   $$x_t = \frac{\sqrt{\bar{\alpha}_t}}{\sqrt{\bar{\alpha}_t}-1}(x_{t-1} - \sqrt{1-\bar{\alpha}_{t-1}}\epsilon_\theta(x_t, c, t)) + \sqrt{1-\bar{\alpha}_t}\epsilon_\theta(x_t, c, t)$$

   The correct inversion formula derived from the DDIM reverse step (Eq. 3) is:

   $$x_t = \sqrt{\frac{\bar{\alpha}_t}{\bar{\alpha}_{t-1}}}(x_{t-1} - \sqrt{1-\bar{\alpha}_{t-1}}\epsilon_\theta) + \sqrt{1-\bar{\alpha}_t}\epsilon_\theta$$

   The paper's coefficient $\frac{\sqrt{\bar{\alpha}_t}}{\sqrt{\bar{\alpha}_t}-1}$ is always negative for $t>0$ (since $\sqrt{\bar{\alpha}_t} < 1$) and differs structurally from the correct $\sqrt{\bar{\alpha}_t/\bar{\alpha}_{t-1}}$. This is verifiable from the paper's own LaTeX—it is not a parsing artifact. The entire method depends on computing DDIM inversions correctly. If this equation reflects the actual implementation, the inversion latents would be erroneous, undermining all downstream claims. If it is only a presentation typo (the implementation uses the correct formula), the authors must correct it. Either way, this is a serious error that must be fully resolved.

2. **The Gaussian justification for preferring circle interpolation over linear interpolation is mathematically flawed.** The paper claims (Section 3.2.2): "Since each inversion in $\mathcal{T}^i$ is in a Gaussian distribution, the common linear interpolation will lead to a result that is not in Gaussian distribution." This is incorrect. If $I_a$ and $I_b$ are (jointly) Gaussian, then any linear combination $aI_a + bI_b$—including both linear interpolation and spherical interpolation—is also Gaussian. Both Eq. (5) (circle interpolation) and standard linear interpolation are linear operations on the input vectors, so both preserve Gaussianity. The real advantage of spherical interpolation may lie in norm/angle preservation or in the larger range provided by extrapolation, but the paper's stated distributional motivation does not hold. Since this claim is core to the method design (introducing circle interpolation over simpler alternatives), this gap weakens the paper's theoretical grounding.

3. **The long-tail classification comparison relies on baseline numbers cited from Wang et al. (2024) rather than fair re-evaluation under identical conditions.** The caption of Table 2 explicitly states: "Ours results are averaged on three trials, and other results are from (Wang et al., 2024)." This means the baselines were not re-run in the same codebase, with the same training hyperparameters, random seeds, or data splits. Without controlling for these factors, the reported advantages (e.g., $3.\bar{6}\%$ over Diff-Mix) could partially reflect implementation or evaluation differences rather than genuine methodological gains. The few-shot and OOD experiments do not have this issue, but the long-tail experiment is the paper's primary demonstration on imbalanced data.

4. **No standard deviations or confidence intervals are reported anywhere in the paper.** Results are described as "averaged over three trials" (e.g., Tables 1, 2), but no error bars or variances are given. Given the well-known high variance of few-shot learning and the reliance on three-trial averages, the reader cannot assess whether the reported improvements are statistically significant. This is a basic evidential requirement for empirical ML papers.

### Minor

1. **For the long-tail experiments, $s=1.0$ effectively disables the two-stage denoising component.** With $s=1.0$, the first-stage timestep range $(sT, T] = (T, T]$ is empty, so only the plain prompt (without suffix) is used throughout. The long-tail results therefore test only the circle interpolation component, not the two-stage denoising. This should be explicitly stated and discussed, as it means the long-tail benefits are attributable solely to the interpolation step.

2. **The suffix generation pipeline lacks reproducibility details.** The paper mentions using "a large language model (e.g., GPT-4)" to summarize captions into suffixes but provides no prompt template, no examples of generated suffixes, no specification of how many suffixes were produced per dataset, and no analysis of suffix quality or coverage. Without these details, this component cannot be reproduced or assessed.

3. **The hyperparameter choices for the split ratio $s$ (0.3 for 5-shot, 0.1 for 10-shot) are stated without justification.** Why these specific values? A brief sensitivity analysis (beyond the single ablation in Figure 6) would strengthen the paper. The replacement probability of 0.5 for joint training is also stated without explanation.

4. **The ablation study is limited to one dataset (Aircraft) with one backbone (ResNet50).** No ablation is performed on the number of concept tokens $n$, the LoRA rank, the number of suffixes, or the choice of VLM/LLM. The paper would benefit from ablating circle interpolation vs. linear interpolation on distribution metrics (not just downstream accuracy).

### Trivial

- None beyond the standard formatting artifacts present in the extracted text.

---

## Nice-to-Haves

- A direct faithfulness metric (e.g., per-class FID or a human evaluation of category preservation) would directly substantiate the paper's central faithfulness claim rather than relying on downstream accuracy as a proxy.
- A direct comparison between circle interpolation and linear interpolation on distributional metrics (e.g., norm preservation, distance from Gaussian via statistical tests) would clarify whether the Gaussian concern or another property is the real advantage.
- Running the long-tail baselines under identical conditions would substantially strengthen the experimental claims.

---

## Removed Points

These points were flagged by one or both reviewers but are removed or demoted per the filtering rules:

- **Criticism that the DDIM inversion claim is unverifiable because tables are embedded as images**: REMOVED. The paper's abstract, introduction, and method sections state the numerical results in text (e.g., "+3.6% over Diff-Mix," "+11.39% over Original"), and these quoted values can be verified against the tables once rendered. This is a PDF-extraction limitation, not a paper error.

- **Concern that Da-Fusion also produces diversity through variable noise levels, weakening the dichotomy**: REMOVED. The paper's dichotomy (intra-category ≈ faithful but homogeneous, inter-category ≈ diverse but unfaithful) is an acknowledged simplification used to motivate the method. The paper does not claim these are absolute; they are relative tendencies.

- **Concern that the method is non-reproducible because suffix generation prompt is missing**: DEMOTED to Minor (listed above). This is a reproducibility concern but a minor one (the core method of inversion interpolation does not depend on it).

- **Criticism about the OOD experiment having only C(5,2)=10 pairs per category**: REMOVED. The interpolation strength $\lambda$ is sampled randomly, so each interpolation produces a different result even from the same pair. Multiple distinct synthetic images can be generated from 10 pairs.

- **Strength about circle interpolation being a "principled technical choice... mathematically justified"**: REMOVED due to conflict with verified weakness #2 (the Gaussian justification is flawed). The empirical effectiveness stands, but the mathematical justification is not sound as presented.

- **Strength about "consistent state-of-the-art results with comprehensive baselines"**: PARTIALLY DEMOTED. The few-shot and OOD comparisons are well-controlled; the long-tail comparison relies on cited numbers (noted in Major weakness #3).

---

## Novel Insights

The harsh critic's observation that $s=1.0$ for all long-tail experiments collapses the two-stage denoising to single-stage (and thus the long-tail gains are attributable solely to inversion interpolation) is a genuinely insightful finding not discussed by the authors. Additionally, the meta-observation that the paper's Gaussian-based justification for circle interpolation does not hold up mathematically (since linear combinations of Gaussians remain Gaussian) reveals a gap between the paper's theoretical framing and what actually drives the empirical success—likely norm/angular properties rather than distributional ones.

---

## Suggestions

1. **Correct Eq. (4)** to the standard DDIM inversion formula. Verify that the implementation matches the corrected equation and state this explicitly.

2. **Re-frame the justification for circle interpolation.** Remove or correct the Gaussian argument. Provide the actual reason (e.g., norm preservation on the sphere, the ability to do extrapolation beyond the convex hull, or empirical evidence that spherical interpolation better explores the latent manifold) and support it with distributional analysis (e.g., PCA projections of inversion latents, comparison of linear vs. spherical interpolation outputs).

3. **Re-run long-tail baselines** under exactly the same experimental conditions as Diff-II, or clearly acknowledge the limitation and present the long-tail results as preliminary comparisons.

4. **Report standard deviations** for all three-trial averages, at least for the main claims.

5. **Provide the GPT-4 prompt template, example suffixes, and the number of suffixes used per dataset** in an appendix or supplementary.

6. **Explicitly discuss the implications of $s=1.0$ for long-tail experiments** and clarify that those results isolate the contribution of the interpolation component.

---

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>