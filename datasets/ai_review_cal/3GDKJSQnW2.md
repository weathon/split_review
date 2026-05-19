- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
Now I have all the information needed. Let me produce the consolidated review.

---

## Summary

This paper proposes PDEdit, a text-based video editing framework that performs spatial-temporal non-rigid edits (e.g., motion changes) using only the input video and a target text prompt, without requiring source captions or masks. The key ideas are (1) **prompt pivoting** — deriving a "pivotal prompt" from the target prompt by masking out editing-factor words, so the model can be tuned without a source caption — and (2) **temporal dynamic editing** with spatial-temporal attention reweighting to localize and smooth motion changes across frames. The paper reports CLIP similarity, FVD, and a human evaluation on 21 DAVIS videos against two baselines.

## Strengths

- **Prompt pivoting eliminates dependency on source prompts**: The method derives a tuning prompt from the target text alone, removing the need for source captions or object masks that prior work (e.g., Tune-A-Video) requires. This is clearly articulated in Section 4.1 and illustrated in Figure 2(c). This is a genuinely useful conceptual contribution — source prompts are often unavailable and their choice can bias editing results.

- **Distributional pivoting provides a principled alternative to a fixed heuristic**: The paper proposes two pivoting strategies. Editing factor pivoting masks the bottom-*k* words by CLIP score, which requires choosing *k* arbitrarily. Distributional pivoting instead derives a threshold *s** from the intersection of positive/negative CLIP-score distributions on Charades-STA, adaptively determining which words are editing factors. The ablation (Figure 8a) shows a concrete case where the fixed-*k* approach mistakenly masks "bench" while distributional pivoting does not, providing evidence that the adaptive approach has practical benefit.

- **Spatial-temporal focusing components are validated by ablation**: The ablation in Figure 8b demonstrates that removing temporal focusing causes a desired "jump" edit to produce unrealistic levitation (the motion change is not properly timed), and removing spatial focusing weakens the editing effect. This directly supports the claim that both components contribute to successful non-rigid editing.

## Weaknesses

### Fatal
None. The core ideas (prompt pivoting, spatial-temporal focusing) are coherent, and the paper contains evidence that the components function as intended.

### Major

- **Evaluation is too narrow to support the claimed advances**: The experiments use only 21 videos from DAVIS and compare against only two baselines (Text2Video-Zero and Tune-A-Video). The paper itself cites Gen-1, VideoComposer, and Control-A-Video in the Related Works (Section 2.2) as methods that also perform video editing, but does not compare against them. With a 21-video evaluation set and only two comparison methods, the quantitative results (CLIP similarity, FVD) lack statistical reliability and are insufficient to substantiate claims of state-of-the-art non-rigid editing.

- **No metric directly measures the core claim (motion change success)**: CLIP similarity measures global semantic alignment but cannot distinguish whether a specific motion verb (e.g., "jump" vs. "walk") is correctly realized. FVD measures distributional frame quality, not edit fidelity. The paper has no motion-focused evaluation — no optical flow comparison, no pose accuracy, no action recognition on edited frames. The user study (36 participants, no protocol details, no significance test) provides some support but does not fill this gap. The central contribution of the paper is enabling dynamic motion changes, yet there is no quantitative evidence that the intended motion change actually occurred in the edited video.

- **Key method components are underspecified and lack sensitivity analysis**: The editing factor pivoting relies on a heuristic *k* (only the value *k*=3 is shown in the ablation, no systematic study). The spatial-temporal focusing uses coefficients *α* (stated as "1 < *α* < 2") and *β* ("0 < *β* < 1") but no specific values are reported and no sensitivity analysis is provided. The temporal weights *γ* are described as "smoothly blending along the frames using a Gaussian curve" but the curve parameters are not given. The predicate-detection rule for assigning extra weight to motion subjects (Section 4.2: "when the editing factor includes a 'predicate'") is stated but not defined or validated. The distributional threshold *s** is derived from Charades-STA; no analysis shows whether this threshold transfers to the DAVIS test domain. These underspecifications prevent assessment of whether the method is principled or tuned per-example.

### Minor

- **Missing implementation details for video tuning**: The per-video fine-tuning step (Section 4.1) does not report optimization steps, learning rate, or compute cost. This is a practical limitation (tuning a diffusion model per video is expensive) that should be disclosed and discussed.

- **Section 3.2 is referenced but missing from the paper**: The text at the end of Section 4.1 (line 107) says "As explained in Section 3.2," but the paper jumps from Section 3.1 directly to Section 3.3 (DDIM Sampling and Inversion). The content that should be in Section 3.2 (likely the T2V model training objective) is absent, making the method description incomplete.

- **No failure case analysis or discussion of limitations**: The paper presents only successful editing examples. There is no discussion of failure modes (e.g., complex motions, multiple objects, ambiguous prompts) or limitations of the approach, which would strengthen credibility.

### Trivial
None.

## Nice-to-Haves

- Provide user study details (protocol, per-category breakdown, inter-rater reliability, significance tests).
- Report computational cost: video tuning time/memory per video, inference time.
- Discuss scope limitations and failure cases explicitly.

## Removed Points

These points from the raw reviews were filtered out per the review policy:

1. **"DDIM inversion equation appears to contain an error"** — The equation in Section 3.3 follows a known parameterization of DDIM; the claim of an error is speculative and cannot be confirmed from the paper as written.
2. **"Abstract/introduction overstates novelty"** — The paper claims "non-rigid video editing based only on the target text... has never been attempted before," which the paper's own Related Works section supports by distinguishing prior work as limited to rigid edits. This criticism is not strongly anchored.
3. **"Missing related works"** — The paper actually cites Gen-1, VideoComposer, and Control-A-Video in its Related Works section. The issue is their absence from the *experimental comparison*, which is already covered under "Major" weaknesses.
4. **"Text2Video-Zero vs Tune-A-Video are not apples-to-apples"** — While these methods have different design points, the comparison is standard practice in this field; asymmetry favoring baselines is not a valid weakness.
5. **Strengths from Strength Finder removed as generic or invalid**: None of the Strength Finder's claims were removed — all four were concrete and evidence-grounded.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not synthesize a perspective not already present in the paper. One observation that emerges from cross-referencing is that the paper's two central claims — (a) prompt pivoting eliminates source-prompt dependency, and (b) spatial-temporal focusing enables motion edits — are supported at the component level (by ablation) but are not backed at the system level (by a thorough comparison against contemporary methods on appropriate metrics). This asymmetry between component-level validation and system-level evidence is the paper's main structural weakness.

## Suggestions

1. **Expand the experimental comparison** to at least 3–4 additional baselines (e.g., Gen-1, VideoComposer, Control-A-Video) on a larger benchmark, using standard text prompts.
2. **Introduce a motion-focused evaluation metric** — for example, per-frame action classification accuracy, pose similarity to a synthetic ground-truth, or optical flow consistency with the target motion verb.
3. **Report specific values and ablations** for all key hyperparameters: *k* in editing factor pivoting (systematically vary and measure), *α* and *β* in spatial focusing, the Gaussian curve parameters for *γ*, and a cross-domain test of the threshold *s**.
4. **Reinstate or flag the missing Section 3.2** and provide implementation details (learning rate, optimization steps, compute cost) for the per-video tuning step.
5. **Include a dedicated limitations section** with representative failure cases.

**Originality**: The prompt pivoting idea is genuinely novel and well-motivated.  
**Importance of research question**: Non-rigid video editing from text is an important open problem.  
**Claims support**: The core claims are only weakly supported due to limited evaluation scope, underspecified method details, and lack of task-appropriate metrics.  
**Soundness of experiments**: Below the bar — 21 videos, 2 baselines, no motion-focused metric.  
**Clarity of writing**: Generally clear on the conceptual level; the method description has gaps (missing Section 3.2, unspecified hyperparameters).  
**Value to the community**: The prompt pivoting idea could be useful, but in its current form the paper does not provide convincing evidence that the method works robustly.
