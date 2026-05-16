Now I have verified all the claims against the paper. Let me synthesize the final review.

## Summary

The paper proposes learning joint representations from multiple sensors (images and proprioception) in RL by combining reconstruction-based losses for low-dimensional proprioception with contrastive losses for high-dimensional images within Recurrent State Space Models (RSSMs). It systematically evaluates this approach against the common practice of concatenating image-only representations with proprioception across a wide range of tasks including DMC variants with video backgrounds and occlusions, a new locomotion suite, and a mobile manipulation task.

## Strengths

1. **Clear empirical superiority of joint representations over concatenation across diverse domains.** The paper's central claim — that learning a joint representation within an RSSM outperforms the standard practice of concatenating image representations with proprioception for the policy — is convincingly supported. On the Occlusion suite (Fig. 3), joint approaches more than double the score of any concatenation baseline; on the Locomotion suite (Fig. 4), Joint(CPC+R) significantly outperforms all Concat variants; on OpenCabinetDrawer (Fig. 5), joint methods maintain performance under changing backgrounds while concatenation baselines degrade.

2. **Well-motivated per-modality loss assignment that is empirically validated.** The paper's key insight — using reconstruction for clean low-dimensional proprioception and contrastive losses for noisy high-dimensional images — is tested systematically. The comparisons Joint(CV+R) vs. Joint(CV+CV) and Joint(CPC+R) vs. Joint(CPC+CPC) in Figs. 2-3 directly show that the mixed-loss assignment outperforms fully contrastive variants, especially for model-based RL where the gap is dramatic (e.g., Joint(CPC+R) more than doubles Joint(CPC+CPC) on Occlusions).

3. **Comprehensive evaluation across challenging new benchmarks.** The paper contributes a DMC Occlusion suite and a Locomotion suite with obstacles, neither of which can be solved by image-only methods. These tasks probe precisely the scenario where fusing vision and proprioception is necessary. The inclusion of a realistic mobile manipulation task (OpenCabinetDrawer) with both color and depth images further strengthens the generality of the findings.

4. **Demonstrated mitigation of a known limitation in contrastive model-based RL.** The paper shows that joint representations almost close the performance gap between model-free and model-based agents for contrastive image objectives (Figs. 2-3), directly addressing a weakness noted by Ma et al. (2020). This is a practically significant finding.

5. **Qualitative analysis corroborates quantitative results.** The saliency maps (Fig. 6, left) show Joint(CV+R) focusing on the task-relevant cheetah while Img-Only(CV) is distracted by the video background. The occlusion-free ground-truth reconstruction analysis (Fig. 6, right) shows that Joint(CPC+R) captures both cart position and pole angle from the latent state while Img-Only(CPC) fails, providing mechanistic support for the quantitative improvements.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Potential parameter-capacity confound between Joint and Concat baselines.** In the Joint approach, both image encodings and proprioception are concatenated and fed to the RSSM, giving it a larger input dimension (and thus more parameters in the first recurrent layer). In the Concat approach, only image encodings enter the RSSM, and proprioception is appended later for the policy. The paper does not discuss whether observed gains could partly reflect different parameter counts rather than the fusion mechanism itself. While this does not invalidate the main claims (the Concat approach could in principle have more total parameters overall due to separate components), a discussion or controlled comparison (e.g., scaling the image-only RSSM) would strengthen the analysis.

2. **Cropping augmentation applied only to contrastive methods.** The paper states (line 104): "Following prior work... we include cropping-based image augmentation for contrastive approaches." This introduces an asymmetry: contrastive methods receive an additional augmentation that reconstruction methods do not. The paper does not discuss whether this could affect the comparison. If reconstruction methods were also given augmentation (or the paper explained why it cannot be applied), the comparisons would be cleaner. This is a minor confound that does not threaten the main conclusions — the key Joint vs. Concat comparisons hold within the same loss family — but deserves acknowledgment.

3. **Framing of Dreamer-v3 comparisons.** The paper states that its approach "outperforms several SOTA baselines" (abstract) and compares Joint approaches to Dreamer-v3. Since Dreamer-v3 is image-only and does not use proprioception at all, outperforming it with methods that do use proprioception is expected and says little about the fusion mechanism. The controlled comparisons (Joint vs. Concat, Joint vs. Joint with different loss assignments) are the paper's real strength, and the framing should more clearly separate these. The paper's conclusion appropriately focuses on the takeaways about joint representations, so this is a presentation issue in the abstract and introduction rather than a methodological flaw.

4. **Number of random seeds not stated in the main text.** The paper reports IQM with 95% stratified bootstrapped CIs (following Agarwal et al., 2021), which implies multiple runs, but the exact number of seeds is not given in the main body. Adding "averaged over N seeds" would improve transparency.

### Trivial

1. The phrasing "novel combination of reconstruction-based and contrastive losses" (abstract, introduction) is slightly inflated — each individual loss is standard, and the novelty lies in the per-modality assignment within the RSSM framework. The conclusion's more measured framing better reflects the contribution.

## Nice-to-Haves

- **Quantitative probing of what the joint latent state encodes.** The saliency maps and reconstruction analysis (Fig. 6) are suggestive but qualitative. A linear probe to measure how well the joint representation predicts ground-truth non-proprioceptive state variables (e.g., ball position, pole angle) compared to image-only or Concat representations would sharpen the mechanistic argument.
- **Ablation of the augmentation asymmetry.** Testing whether applying cropping to reconstruction-based methods (or removing it from contrastive methods) changes the ranking would cleanly address the potential confound.

## Removed Points

The following points from the reviewer inputs are removed with justification:

- **Architectural confound labeled as "Critical Issue" (harsh critic Item 1):** Downgraded from critical to minor. The Joint and Concat approaches are architecturally different by design — fusing modalities within the dynamics model is the intervention being tested. A parameter-count confound would only matter if the paper claimed that *how* the modalities are combined (not just that they are combined) drives gains, and even then the parameter difference is inherent to the architectural choice. The point is kept as a minor request for discussion, not a structural flaw.
- **Dreamer-v3 comparison labeled as "Critical Issue" (harsh critic Item 2):** Downgraded from critical to minor. The harsh critic's own analysis acknowledges that "this does not invalidate the many other controlled comparisons." The paper's main claims rest on the Joint vs. Concat comparisons, not on Dreamer-v3. The framing issue is real but minor.
- **"Novel combination" wording (section notes):** Removed to Trivial. This is a semantic preference, not a substantive weakness.
- **CPC derivation / mechanism analysis request:** Removed. The paper's claim about improved dynamics learning is sufficiently supported by the performance results; demanding direct analysis of the mechanism is a nice-to-have, not a weakness.
- **Occlusion details not in main text:** Removed. The harsh critic acknowledges these are likely in the appendix (which is present but stripped by the parser). This is a parser artifact, not an author error.
- **Hyperparameter details not in main text:** Removed. The paper references code availability and follows prior work; these details are standard to defer. Not a genuine weakness.
- **"Missing parts and places to improve" — seeds count:** Kept as minor (Item 4).
- **"Missing parts" — augmentation asymmetry:** Kept as minor (Item 2).

## Novel Insights

Beyond the paper's own contributions, the reviews surface two useful observations. First, the structural asymmetry between Joint and Concat architectures (Joint feeds both modalities into the RSSM, Concat only feeds images) means the comparison tests a bundled intervention — more capacity early in the dynamics model plus cross-modal fusion — rather than fusion alone. Second, the cropping-augmentation asymmetry (contrastive methods only) is a subtle but real confound that prior work in this line (Srivastava et al., 2021; Deng et al., 2022) also inherits without discussion. Neither undermines the paper's conclusions, but both identify clean-up opportunities for future work in this area.

## Suggestions

1. Add a brief discussion of parameter counts between Joint and Concat variants, or include a control experiment that scales the image-only RSSM to match the Joint RSSM's input-layer parameters.
2. Add a sentence in the experimental setup clarifying the number of seeds/runs used for each approach.
3. Add a brief note discussing the cropping-augmentation asymmetry (why it is used, whether it could affect results, and whether reconstruction methods were considered with augmentation).
4. In the abstract and introduction, temper claims about "outperforming SOTA baselines" to clarify that the strongest evidence comes from the controlled Joint vs. Concat comparisons, not from comparisons to image-only SOTA methods.

## Score and Decision

This is a solid, well-executed empirical paper. The core claim — that learning joint representations within an RSSM with per-modality loss assignment outperforms concatenation — is convincingly demonstrated across multiple challenging task domains. The identified weaknesses are minor presentation and framing issues, none of which threaten the central contribution. The paper introduces useful new benchmarks (Occlusion suite, Locomotion suite) and provides a systematic evaluation that the community will find actionable.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>