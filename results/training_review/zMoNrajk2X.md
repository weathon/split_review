Now I have all the information needed. Let me construct the final review, carefully verifying every claim.

---

## Summary

This paper proposes CADS (Condition-Annealed Diffusion Sampler), a sampling-side modification that adds monotonically decreasing Gaussian noise to conditioning signals during inference. The method requires no retraining, works with any pretrained conditional diffusion model and sampler, and aims to increase output diversity—particularly at high classifier-free guidance scales where diversity typically collapses. Experiments across class-conditional ImageNet, pose-to-image, identity-conditioned face, and text-to-image generation show consistent improvements in FID and Recall, with the paper claiming a new state-of-the-art FID of 1.70 on ImageNet 256×256.

## Strengths

- **Simple, model-agnostic, and practical.** CADS requires no retraining, no architectural changes, and adds only an additive Gaussian noise operation at each sampling step. It integrates with DDPM, DDIM, and DPM-Solver (Table 2, reported). This practical simplicity is a genuine advantage over prior work requiring architectural modifications or retraining.

- **Consistent diversity gains across diverse tasks and conditioning modalities.** The paper evaluates on four distinct tasks: class-conditional generation (ImageNet, DiT-XL/2), pose-to-image (DeepFashion, SHHQ), identity-conditioned face generation (ID3PM), and text-to-image (Stable Diffusion). In all settings, CADS improves FID, Recall, MSS, and Vendi Score relative to DDPM sampling at the same guidance scale (Section 4, main results). The improvement on ImageNet 256×256 at a high guidance scale—Recall from 0.32 to 0.62, FID from 20.83 to 9.47—is substantial.

- **Thorough ablation of key hyperparameters.** The paper systematically ablates noise scale *s*, cut-off threshold τ₁, and rescaling factor ψ, providing practical guidance for users (Section 4.2). The rescaling mechanism's role as a regularizer is clearly explained.

- **State-of-the-art FID via sampling alone.** CADS achieves FID 1.70 on ImageNet 256×256 and 2.31 on ImageNet 512×512 (Section 4.1), surpassing prior methods like MDT that required architectural innovations and retraining. This is achieved purely through an improved sampling strategy applied to a pretrained DiT-XL/2 model.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contributions are supported by evidence across multiple tasks. The weaknesses below are substantive but do not invalidate the main claims.

### Minor

- **The main text does not specify the guidance scales used for the baseline comparisons (FID 20.83) or the SOTA results (FID 1.70).** The paper states "fixed high guidance scale" (Section 4) and "higher guidance values" (Section 4.1), but never reports the actual numeric guidance values in the main text. This makes it difficult for the reader to assess whether the FID 20.83 baseline is at a reasonable (if high) guidance scale or an extreme one, and whether the SOTA FID 1.70 is obtained at a guidance scale that would be infeasible without CADS. *The paper promises hyperparameter details in the appendix (line 194: "Further implementation details as well as the exact hyperparameters used to obtain the results presented in this paper are outlined in \Cref{sec:imp-detail-sup}"). This is standard practice, but the main text should briefly state the guidance scale for the headline results to allow in-text evaluation.*

- **Comparison with prior diversity-enhancing methods is limited.** The paper compares CADS only against standard DDPM and its own Dynamic CFG baseline. While the paper discusses Sehwag et al. (2022) in related work (line 30) as a method that "samples from low-density regions," it does not provide a quantitative comparison. Other relevant techniques from the literature (e.g., conditioning dropout at inference time, truncation-like approaches) are not compared. A direct comparison would strengthen the paper's positioning.

- **The claim that CADS "resolves a long-standing trade-off" (line 19) is overstated.** CADS *alleviates* the diversity-quality trade-off at high guidance scales, which is a genuine contribution. However, the paper's own ablations show that at very high noise scales or extreme parameter choices, quality degrades (Section 4.2). The trade-off is improved, not resolved. Similarly, framing the paper as a "comprehensive investigation of the diversity and distribution coverage of conditional diffusion models" (line 17) overstates the scope; the paper primarily proposes and evaluates one method.

- **Potential class drift is not fully characterized.** The paper reports top-1 accuracy dropping from 0.98 to 0.96 for class-conditional ImageNet (Table: alignment), and notes this small drop is "likely due to increased output variation." However, the paper does not measure whether CADS shifts the *distribution* of generated classes (e.g., class-level entropy) or whether the diversity gains partially come from producing images from semantically nearby classes that remain correctly classified. This is a reasonable concern, though the small magnitude of the accuracy drop (2%) and the identical alignment metrics on pose and text tasks partially mitigate it.

- **The piecewise linear schedule γ(t) is presented without justification** for why it is preferable to alternatives (e.g., cosine, exponential). While the paper references additional ablations in the appendix, the main text's rationale is limited to empirical effectiveness. A brief motivation would strengthen the method section.

- **Ablation studies are conducted only on ImageNet 256×256** (Section 4.2). The hyperparameter sensitivity of CADS on other tasks (pose-to-image, text-to-image) is not explored. While ImageNet is a natural choice, demonstrating that the trends generalize would increase confidence in the method's robustness.

### Trivial

- None.

## Nice-to-Haves

- **Statistical significance / variance** for FID and Recall improvements. Reporting results from multiple runs or bootstrapped confidence intervals would strengthen the quantitative claims. (Not standard for this scale of benchmark, but would be a nice addition.)
- **Class entropy analysis** for class-conditional generation, to directly measure whether CADS causes off-class generation or shifts the semantic distribution.
- **Failure case visualization.** The paper shows only positive examples. Understanding when CADS fails (e.g., generates low-quality samples or breaks condition alignment) would help users apply the method appropriately.
- **Comparison with conditioning dropout** (randomly dropping the condition during inference) as an additional baseline.

## Removed Points

These points were flagged by the reviewers but have been removed or relocated for the reasons stated below:

- **"Baseline FID 20.83 is implausible / an order of magnitude worse than known results."** — Removed. The reviewer compares this to DiT-XL/2's published FID of ~2.27 at guidance scale 4, but the paper explicitly states it uses a "fixed high guidance scale" (Section 4) where FID is known to degrade substantially. The paper itself explains: "both FID and Recall exhibit less drastic deterioration as the guidance scale increases" (line 113), confirming this is expected behavior at high guidance. The implausibility claim is based on comparing to an apples-to-oranges setting. The valid core—that the exact guidance scale isn't specified—is moved to Minor weaknesses.

- **"The SOTA claim demands more evidence in the main text than currently provided."** — Weakened. The paper promises hyperparameter details in the appendix (line 194), which is standard practice. The main-text omission is a minor presentation gap, not an evidential failure.

- **"The intuition is not formalized"** (Section-by-Section Notes) — Removed. Section 3.2 (line 72-75) provides a formalization using Bayes' rule and score decomposition, showing that early noise makes the condition independent of the sample.

- **"Framing of 'comprehensive investigation' is overstated"** — Moved to Minor weaknesses (overclaiming).

- **"Dynamic CFG is a weak baseline"** — Removed as a standalone criticism. The paper positions Dynamic CFG as a "naive" approach (line 79) and shows CADS outperforms it. This is an appropriate comparison to demonstrate the value of stochastic noise addition over pure guidance modulation.

- **Missing related works** — Removed per instructions (cannot verify existence of missing references without external sources).

- **Reproducibility concerns about undisclosed hyperparameters** — Removed. The paper states hyperparameters are in the appendix (line 194), which is standard practice.

## Novel Insights

None beyond the paper's own contributions. The synthesis reveals that the harsh critic's most significant concern—the implausibility of the FID 20.83 baseline—is invalid when the paper's stated setting ("fixed high guidance scale") is taken into account. The remaining issues are primarily about presentation completeness (guidance scale values in main text) and scope of baselines, rather than methodological soundness.

## Suggestions

1. **Add the guidance scale value** used for the main results (Table 1) and the SOTA results (Table 5) directly in the main text or table captions, even briefly. This single change would resolve the most impactful weakness.
2. **Include a quantitative comparison with at least one prior diversity-enhancing method** (e.g., Sehwag et al. 2022) to better contextualize the contribution.
3. **Tone down claims like "resolves a long-standing trade-off"** to "substantially alleviates" or "improves," which better match the experimental evidence.
4. **Add a brief justification** for the choice of piecewise linear γ(t) over alternatives in the main text.
5. **Compute class-level entropy** for class-conditional ImageNet to explicitly verify that diversity gains are not accompanied by semantic drift.

## Score and Decision

**Originality:** 7/10 — The idea of adding decaying noise to conditioning during inference is simple and elegant, though building on well-known principles.
**Importance of question:** 8/10 — The diversity-quality trade-off is a central problem in conditional diffusion models, and a sampling-only solution is practically valuable.
**Claims supported:** 6/10 — The core claim (CADS improves diversity at high guidance scales) is well-supported. The SOTA claim is plausible but lacks specification of the exact experimental conditions in the main text.
**Soundness of experiments:** 7/10 — Experiments span multiple tasks and include ablations. The main gap is missing specification of guidance scales and limited comparison to other diversity methods.
**Clarity of writing:** 7/10 — The method is clearly explained with intuitive motivation. Some overclaiming in the introduction.
**Value to community:** 7/10 — The method is simple to implement, requires no retraining, and could become a standard tool for practitioners.

The paper presents a simple, practical, and effective method for improving diversity in conditional diffusion models. The core idea is sound, and the experimental evaluation across multiple tasks provides consistent evidence of its effectiveness. The main weaknesses are presentation-related (unspecified guidance scales in main text) and scope-related (limited baseline comparisons). These are addressable in revision. The paper makes a genuine contribution that would be useful to the community.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>