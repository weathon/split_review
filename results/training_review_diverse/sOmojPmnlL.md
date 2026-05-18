Here is my final consolidated review.

---

## Summary

This paper proposes **AnyExpress**, a ReferenceNet-free framework for audio-driven portrait animation. The key idea is to replace the heavy ReferenceNet module (used by prior methods for identity preservation) with a lightweight, frozen IP-Adapter-Face, and train only a compact "Audio-Motion Adapter" that handles lip-sync and motion dynamics. This yields a **7× reduction in trainable parameters** while supporting three capabilities the authors term "Freeform Portrait Animation": (1) any face pose, (2) any animated context, and (3) text-based control of identity/background. The paper also introduces Progressive Prefix Conditioning for smooth long-video generation.

## Strengths

1. **7× parameter reduction by removing ReferenceNet** — The paper demonstrates that a full 2D-UNet ReferenceNet can be replaced with a much lighter frozen identity controller (IP-Adapter-Face), reducing trainable parameters from ~7× the base model size down to just the Audio-Motion Adapter (abstract; Section 1). This is a concrete architectural improvement over prior work.

2. **Quantitative advantage on pose diversity with competitive standard metrics** — Table 2 shows AnyExpress achieving the highest Pose Diversity Score (ΔP) on both HDTF and CelebV among all compared methods, while maintaining competitive lip-sync (Sync-C, Sync-D), identity preservation (FaceSim, CLIP-I), and video quality (DOVER). This establishes that flexibility does not come at a catastrophic quality cost — a finding directly verified from the reported numbers.

3. **Progressive Prefix Conditioning improves long-video consistency** — The ablation in Section 4.4 (Fig. 7a) shows that the proposed Progressive Prefix Conditioning with anchor alignment eliminates window-boundary artifacts and color drift that occur with Progressive Fusion, a meaningful engineering contribution validated qualitatively.

4. **Modular design compatible with personalized T2I models** — The adapter framework is demonstrated to work with multiple base model styles (realistic, Asian-style) and to support additional control signals (pose, text, identity) without retraining (Fig. 6b, Section 3.4), which is a genuine practical advantage over tightly-coupled ReferenceNet approaches.

5. **Entropy analysis provides architectural insight** — Figure 3 quantitatively characterizes how weak control (Text-FaceID) yields higher and more gradually increasing attention-head entropy compared to strong control (ReferenceNet), offering an evidence-based rationale for the design choice.

## Weaknesses

### Fatal
None.

### Major

1. **"Any Animated Contexts" and "Any Text-Based Control" lack quantitative validation.** Section 4.3 presents only a handful of qualitative frames (Figure 6) for these two claimed capabilities, which are stated as primary contributions of the Freeform Portrait Animation task. There are no CLIP relevance scores between generated frames and text prompts, no user studies on whether text-described attributes are recognizable, and no quantitative measure of background coherence or diversity. While these are genuinely novel capabilities that no prior open-source method supports, the evidence remains anecdotal. For text-based control specifically, reporting CLIP scores comparing generated frames against the prompt (and against a baseline T2I model's output on the same prompts) would directly validate that the adapter does not suppress the base model's text-driven generation.

### Minor

2. **Baseline comparison on "Any Face Pose" would benefit from a standard-pose sanity check.** The paper evaluates ReferenceNet-based methods (AniPortrait, MegActor, EchoMimic, V-Express) on a task that deliberately deviates pose control from the reference image — which is precisely the setting those methods were not designed for. The paper acknowledges this (Section 4.2), and Table 2 *does* include standard quality metrics (FaceSim, CLIP-I, Sync-C/D, DOVER) where AnyExpress remains competitive. However, including a direct comparison where *all* methods operate in their intended regime (pose control matching the reference) would cleanly isolate whether AnyExpress sacrifices any basic quality for its flexibility, making the case for its advantage more airtight.

3. **Pose Diversity Score (ΔP) is insufficiently specified.** The metric is cited to Xu et al. (2024a) and described as measuring "head motion intensity" (Section 4.1), but the exact formula, the pose estimator used, and the range of possible values are not stated. While citing existing metrics is standard practice, ΔP is one of the two primary quantitative claims in Table 2, and its current under-specification makes it harder for readers to interpret the results or reproduce them. At minimum, the exact computation should be given; a validation showing that higher scores correlate with plausible, natural motion (not jitter) would further strengthen the claim.

4. **Entropy analysis (Fig. 3) lacks statistical grounding.** The paper plots distributions of entropy across attention heads but does not report statistical significance, effect sizes, or whether the pattern holds across multiple random seeds. Framing this as "Proposition 3.2" is inflated for what is an interesting but preliminary empirical observation. Adding confidence intervals or a simple statistical test would raise this from a qualitative insight to a reliable finding.

### Trivial
- The training set includes HDTF (28k clips), which is also one of the two evaluation datasets. The potential for evaluation-set leakage or domain mismatch with CelebV is not discussed.

## Nice-to-Haves
- Inclusion of inference speed and GPU memory benchmarks relative to baselines (the paper claims reduced parameters but does not measure wall-clock time or memory).
- CLIP scores and/or a small user study for the text-based control capability.
- A standard pose-locked comparison (all methods matching reference pose) to complement the "any face pose" comparison.
- Statistical tests (e.g., effect size, confidence intervals) for the entropy analysis in Figure 3.

## Removed Points

The following points from the reviewers were removed after cross-checking against the paper:

- **"Baseline comparison is structurally unfair and incomplete ... the reader cannot tell whether the flexibility comes at a cost"** — Factually corrected: Table 2 *does* report standard quality metrics (FaceSim, CLIP-I, Sync-C/D, DOVER) alongside pose diversity, and AnyExpress is competitive on all of them. The claim that no cost-information exists is inaccurate. The core concern (lack of a pose-locked sanity check) is retained as Minor weakness #2 above.
- **"Why would fine-tuning the motion module cause identity overfitting if identity is controlled via a frozen IP-Adapter?"** — The paper already explains this in Section 3.4: the motion module overfits to the *training dataset's specific identities and motions* (not to identity features from the IP-Adapter), and the two-stage strategy mitigates this. The criticism reflects a misunderstanding of the mechanism described.
- **"The paper does not discuss inference speed or memory consumption"** — Moved to Nice-to-Haves; it is a reasonable extension but not a weakness of the current submission.
- **Training data domain gap** — Standard practice; the evaluation datasets (HDTF, CelebV) are widely used benchmarks in this area, and the training set composition is similar to that of comparable methods. This is not a meaningful weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Strengthen Sections 4.3 with quantitative metrics: CLIP scores for text-based control (comparing generated frames to the text prompt) and a diversity/coherence metric for animated backgrounds. Even a small user study (20–30 participants rating whether text attributes are recognizable) would substantially raise the credibility of these claims.
2. Add a supplementary experiment where all methods are evaluated with the pose control signal matching the reference image, to establish that AnyExpress does not sacrifice basic quality. Report the same metrics as Table 2.
3. Specify the exact formula and pose estimator used for ΔP; optionally include a visualization correlating ΔP values with representative frames to validate that higher scores correspond to natural, diverse motion.
4. Add statistical significance measures (e.g., 95% confidence intervals or effect sizes) to the entropy analysis in Figure 3 and tone down the "Proposition" framing.
5. Provide inference speed/memory benchmarks to complement the parameter-count advantage.

## Score and Decision

The paper makes a genuine architectural contribution — demonstrating that ReferenceNet can be eliminated in favor of a lightweight adapter without sacrificing core quality, while gaining flexibility. The quantitative evidence for the "any face pose" capability is solid. However, two of the three claimed capabilities (animated contexts, text-based control) are supported only by qualitative examples, which weakens the empirical foundation for the paper's full scope of claims. The deficiencies are correctable with additional experiments (CLIP scores, user study, standard-pose baseline) and do not undermine the core ReferenceNet-free contribution.

**Score**: 6.0 — a paper with a solid core contribution but incomplete evaluation of some claimed capabilities. Acceptable with the expectation that the authors strengthen the evaluation in a revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>