Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper addresses the problem of learning representations from multiple sensor modalities (images and proprioception) in reinforcement learning. Building on Recurrent State Space Models (RSSMs), the authors propose assigning different loss functions to different sensors — reconstruction for clean/low-dimensional proprioception and contrastive losses (either variational or CPC-based) for images with distractors — and learning a joint latent state. They conduct an extensive empirical evaluation across DMC tasks with video backgrounds and occlusions, a new Locomotion suite, and a realistic mobile manipulation task, demonstrating that their joint representation approach consistently outperforms both image-only methods and the common practice of concatenating image representations with raw proprioception.

## Strengths

- **Core empirical finding holds across diverse settings.** The paper shows that joint representations with per-modality loss choices (Joint(CV+R) and Joint(CPC+R)) consistently outperform both single-modality and concatenation baselines across all four task suites. The most dramatic evidence is the Occlusion suite (Fig. 3), where all image-only SOTA methods (Dreamer-v3, DreamerPro, DrQ-v2, DBC, TIA, DenoisedMDP) and concatenation baselines score near zero while Joint(CPC+R) achieves meaningful scores. This directly validates the paper's central claim.

- **Joint representations systematically outperform concatenation.** Across Video Background (Fig. 2), Occlusion (Fig. 3), Locomotion (Fig. 4), and OpenCabinetDrawer (Fig. 5), every Joint variant outperforms its corresponding Concat counterpart. The gap is often large — on Locomotion, Joint(CPC+R) far exceeds all Concat approaches — providing concrete evidence that learning a shared state space is better than late fusion of independently learned features.

- **Rigorous statistical methodology.** Following Agarwal et al. (2021), the paper reports Interquartile Means with 95% stratified bootstrapped confidence intervals throughout. This makes the comparisons reliable and avoids overinterpreting point estimates — a standard that many empirical RL papers do not meet.

- **Systematic comparison of variational and CPC paradigms.** The paper evaluates both Joint(CV+R) and Joint(CPC+R) across all tasks and finds that neither paradigm dominates universally (CV is better on Video Background and OpenCabinetDrawer; CPC is better on Occlusion and Locomotion). This nuanced finding is valuable for practitioners and is backed by per-task performance profiles (Figs. 10–12).

- **Challenging new benchmarks.** The Occlusion suite and Locomotion suite are genuine contributions that expose failure modes of existing methods. The paper shows that image-only SOTA approaches fail on these tasks while joint representations succeed, validating the paper's motivation.

## Weaknesses

### Major

- **DMC "proprioception" is not realistic proprioception.** The paper splits ground-truth simulator states into "proprioceptive entries" and "non-proprioceptive entries" — e.g., in Ball-in-Cup, the cup's position is labeled "proprioceptive" while the ball's position is not. This results in clean, noiseless, low-dimensional access to task-relevant environmental variables. Real robot proprioception (joint angles, velocities, torques) is noisy, high-dimensional, and does not directly expose environmental state like a cup's location. The reconstruction-based losses succeed here because the signal is clean and concise; in realistic settings, contrastive losses might be needed even for proprioception. The OpenCabinetDrawer experiments (which use a proper robot simulator) partially mitigate this concern, but the DMC experiments drive most of the paper's claims and conclusions (Figs. 2–4). **The central recommendation — "use reconstruction for proprioception" — is not yet validated for the sensor noise levels present in actual robotic systems.** The paper should discuss this limitation explicitly and ideally include at least one experiment with noisy proprioception.

### Minor

- **Cropping augmentation asymmetry creates a confound.** The paper states: "Following prior work … we include cropping-based image augmentation for contrastive approaches" (Section 4). Contrastive methods receive cropping augmentation; reconstruction methods do not. This affects comparisons like Joint(CV+R) vs. Joint(R+R) and Img-Only(CV) vs. Img-Only(R), where the loss type and augmentation vary simultaneously. The main Joint-vs-Concat comparisons within the same loss type are unaffected (e.g., Joint(CV+R) vs. Concat(CV)), but the asymmetry weakens some supporting comparisons.

- **Novelty framing is inflated.** The "novel combination" (Abstract, Introduction) is a straightforward per-modality assignment of existing reconstruction and contrastive losses within a multi-modality RSSM extension that is itself standard (Section 3: "we extend it to K models, one for each observation modality"). Equations 3 and 4 are per-modality instantiations of previously published variational and CPC losses. The paper's real value is empirical — it systematically demonstrates that the simple design choice of matching loss types to sensor properties pays off across diverse settings. The framing should be recalibrated to match this.

- **No analysis of why fully contrastive approaches fail.** The paper reports that Joint(CV+CV) and Joint(CPC+CPC) often perform poorly, particularly on OpenCabinetDrawer (Fig. 5), but offers no explanation for this failure. The reader is left wondering whether the issue is representation collapse, insufficient negatives, insufficient dynamics learning, or something else entirely. Since the failure of fully contrastive two-modality training is both interesting and somewhat surprising, a brief discussion would strengthen the paper.

- **Loss combination effect not fully isolated.** The paper compares Joint(CV+R) to Joint(CV+CV) and Joint(CPC+R) to Joint(CPC+CPC), showing the combination helps. However, it does not compare Joint(CV+R) to Joint(R+CV) — swapping which modality gets which loss. Without this comparison, the paper cannot distinguish whether the benefit comes from having *different* losses for the two modalities, or from the *specific assignment* (reconstruction for proprioception, contrastive for images). This is a gap in the ablation logic.

### Trivial

- **Saliency map analysis (Fig. 6) is under-explained.** The paper does not specify how these maps are generated for RSSM-based methods (gradients? attention? decoder outputs?). The conclusions drawn are purely qualitative ("Joint(CV+R) clearly focuses better on the task-relevant cheetah") without any supporting metric. This figure adds little rigor and could be removed or better contextualized.

- **Task descriptions for Locomotion and Occlusion suites are sparse in the main text.** Obstacle properties, randomization details, disk sizes/transparencies/speeds for occlusions are not specified. While the appendix presumably contains these details, the main text should provide enough information for a reader to assess the challenge without cross-referencing.

## Nice-to-Haves

- An experiment adding Gaussian noise to DMC proprioception would directly address the realistic-proprioception concern and would be a relatively low-cost addition.
- A wall-clock time or parameter count comparison between Joint and Concat methods would help practitioners assess the overhead of using multiple encoders/decoders/score functions.
- An ablation controlling for latent capacity (e.g., does a larger image-only RSSM catch up to a joint one?) or measuring mutual information between latent state and each modality could clarify *why* joint representations help.
- A comparison of Joint(CV+R) vs. Joint(R+CV) to isolate whether the benefit is from the specific loss assignment or just from having two different losses.

## Removed Points

These points were raised by reviewers but are removed or downgraded per the review guidelines:

- **"Common practice is a straw man"** — Removed. The paper's Related Work explicitly acknowledges the exceptions (Wu et al., 2022; Hafner et al., 2022, 2023; Becker & Neumann, 2022) and correctly notes they focus on purely model-based reconstruction settings. The "common practice" claim refers to the broader visual RL and robotics literature (Finn et al., 2016; Levine et al., 2016; Kalashnikov et al., 2018; Xiao et al., 2022; Fu et al., 2022), where concatenation is indeed the standard. The paper's self-positioning is accurate.
- **"No principled criterion for loss assignment"** — Removed. The paper states a clear heuristic criterion: reconstruction for "clean low-dimensional sensors" and contrastive for "high-dimensional noisy sensor signals" (Section 1, conclusion). While heuristic, this is a stated principle, not an absence of one.
- **Criticism that Joint(R+R) uses reconstruction for both modalities and thus comparison is unfair** — The paper does compare Joint(R+R) as a baseline; the asymmetric comparison (where the author's method benefits from the design choice) is intentional and valid for demonstrating the advantage.
- **Suggestions that the paper should add entirely new task domains or datasets** — Removed as scope creep. The paper already covers 4 task suites + mobile manipulation with two visual modalities.
- **Demands for theoretical proofs** — Removed as inappropriate for an empirical systems paper.

## Novel Insights

The reviews surface an interesting tension: the paper's strongest claims rest on DMC experiments where "proprioception" is clean simulator state, yet the same design choice (reconstruction for low-dimensional signals) is independently validated on the more realistic OpenCabinetDrawer task. This suggests the paper's recommendation may be more robust than the DMC limitation implies — the principle (reconstruction for low-dimensional/noiseless sensors) holds even when the sensor modality changes from idealized state variables to actual simulated joint readings. The key missing piece is not whether the principle works, but where the boundary between "clean enough for reconstruction" and "noisy enough to need contrastive" lies, and whether that boundary shifts in real hardware. This is a well-scoped open question that the paper's framework is well-positioned to address in future work.

## Suggestions

1. **Add a discussion of the DMC proprioception limitation** (it is ground-truth state, not simulated sensor readings) and its implications for real-world transfer. Even a paragraph in the Limitations section would suffice.
2. **Add at least one experiment with noise added to DMC proprioception** (e.g., Gaussian noise on joint angles/velocities) to validate that reconstruction remains beneficial under realistic noise levels.
3. **Recalibrate the novelty language** in the abstract and introduction to match the empirical contribution rather than claiming methodological invention.
4. **Add a brief discussion of why fully contrastive approaches fail** on OpenCabinetDrawer and other tasks.
5. **Either describe how the saliency maps are generated** (method, what they visualize) or remove Figure 6.
6. **Correct the cropping augmentation asymmetry** by either applying augmentation to reconstruction methods as well, or adding an ablation without augmentation for contrastive methods.

## Score and Decision

The paper makes a solid empirical contribution. It demonstrates convincingly that learning joint RSSM representations from images and proprioception — with the specific design choice of reconstruction for proprioception and contrastive losses for images — consistently outperforms both concatenation and single-modality approaches across a diverse set of challenging tasks. The experiments are extensive (four task suites, two RL paradigms, two contrastive learning paradigms, two visual modalities), the statistical methodology is rigorous, and code is provided. The main weaknesses are (i) the DMC "proprioception" is not realistic, which limits the strength of real-world conclusions but does not invalidate the paper's core claims, and (ii) a set of addressable presentation and analysis gaps (augmentation asymmetry, missing ablations, inflated novelty framing). These are not fatal — the paper's contribution stands on its empirical evidence.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>