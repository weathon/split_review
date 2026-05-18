Now I have a thorough understanding of the paper. Let me produce the consolidated review.

---

## Summary

This paper proposes Diffusion Implicit Policy (DIP), a framework for scene-aware human motion synthesis that requires no paired motion-scene data during training. The core idea is to disentangle interaction learning from motion learning — training a motion diffusion model on unpaired motion data (AMASS/Babel) and using hand-designed interaction-based reward functions as an implicit policy during inference. The method integrates diffusion denoising with reward-guided optimization of the sampling distribution in a GAN-inversion style, and introduces rotation-matrix power-space blending for long-term multi-task motion synthesis. Experiments on ShapeNet scenes, PROX, and Replica show that DIP achieves competitive or superior results to paired-data baselines (SAMP, GAMMA, DIMOS) across locomotion, interaction, and long-term synthesis.

## Strengths

- **Unpaired training eliminates dependency on scarce motion-scene data.** The framework disentangles interaction from motion synthesis during training, using only pure motion datasets (AMASS/Babel) for the diffusion model and applying scene-based reward functions only at inference (Sec. 3.3–3.5). Despite this training-data restriction, it achieves results competitive with or exceeding paired-data methods (Tabs. 1–3), which is a genuine advance for the field.

- **Joint optimization of motion naturalness and interaction plausibility via iterative denoising + implicit policy.** The DIP integrates a motion diffusion model (providing a naturalness prior) with interaction-based rewards (providing plausibility) into a single iterative loop (Eq. 7–9, Sec. 3.5). The user study (Tab. 3) shows DIP obtains the highest overall and interaction plausibility scores across PROX and Replica while maintaining motion naturalness on par with DIMOS — all without paired data.

- **Rotation matrix power-space blending for smooth multi-task transitions.** The blending strategy (Sec. 3.6) interpolates rotations in the power space of the rotation matrix rather than naively in axis-angle space, avoiding interpolation artifacts. This is a technically sound design choice that contributes to the strong user-study diversity and overall scores (Tab. 3).

- **Comprehensive evaluation across three settings.** The paper evaluates on locomotion (Tab. 1), atomic interaction (Tab. 2), and long-term multi-task synthesis via user study (Tab. 3), using both synthetic (ShapeNet) and real scanned scenes (PROX, Replica). This breadth convincingly demonstrates the method's generalization ability.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Abstract overstates motion naturalness results relative to the paper's own conclusions.** The abstract claims "better motion naturalness … than cutting-edge methods," but the paper's own discussion (Sec. 4.4, line 266) states: "For motion naturalness, our proposed method is on par with DIMOS." The user study table (Tab. 3, \input{tables/user_study}) is not visible in the extracted text, but the paper's textual summary explicitly avoids claiming superiority on this dimension. This is a factual inaccuracy in the most prominent part of the paper. The authors should correct the abstract (e.g., "comparable motion naturalness and better interaction plausibility and diversity").

- **The "unpaired" framing, while accurate, would benefit from a clearer discussion of the reward-engineering trade-off.** The paper is transparent that reward functions are hand-designed (Sec. 3.4), and the "unpaired" claim refers specifically to not requiring paired motion-scene training data — which is technically correct. However, the current framing strongly emphasizes the absence of supervision without acknowledging that the hand-designed rewards encode substantial domain knowledge (contact geometry, penetration avoidance, goal conditioning) that must be manually specified per interaction type. Adding a brief limitations paragraph discussing this trade-off, and when the reward-engineering burden may become prohibitive, would improve the paper's intellectual honesty without weakening its contribution.

- **The contact score gap is acknowledged but not fully supported with alternative evidence.** The paper's lower contact scores (Tabs. 1–2) are attributed to a metric mismatch (foot-vertex vs. foot-joint contact). The explanation is plausible, but the paper could strengthen it by reporting vertex-based contact scores alongside the joint-based metric, or by showing that the method's explicit foot-vertex contact reward (mentioned in Sec. 3.4) actually works as intended. As it stands, readers cannot distinguish between a genuine weakness and a measurement artifact.

### Trivial

- The notation in Eq. (6) (line 171) is slightly ambiguous: it is not immediately clear whether gradients of the scene information \(\mathcal{S}\) flow through the diffusion model \(\varphi\) or only through the reward function. Clarifying this would help reproducibility.

- The LLM-based sub-task decomposition (mentioned in Sec. 3.2, line 96) is not evaluated, and the experiments use predefined sub-tasks. This is fine — the LLM component is inessential to the core contribution — but a brief note confirming this scope would prevent confusion.

## Nice-to-Haves

- An ablation study comparing (a) pure diffusion (no optimization), (b) direct optimization of \(\mu_t\), and (c) the proposed GAN-inversion-style optimization via \(\hat{x}_0^\varphi\) would directly validate the core technical claim. The paper references supplementary material for ablations (these exist in the original submission but were not evaluable here due to parser stripping). Moving the key ablation table into the main paper would strengthen the presentation.

- A convergence trajectory analysis showing how \(\mathcal{R}_{ip}\) evolves during the denoising/optimization loop would address curiosity about gradient stability and optimization behavior, but is not needed to validate the central claims.

- Reporting velocity distributions for the locomotion experiments would clarify whether the faster finish time (3.35s vs. DIMOS's 4.02s) reflects more natural walking speed or unnaturally fast motion.

## Removed Points

These points were flagged by reviewers but are removed or downgraded for the following reasons:

- **"Core technical move is under-justified theoretically and lacks ablation in the main paper"** — Partially removed. The demand for theoretical proof of gradient meaningfulness is beyond what an empirical systems paper should provide; the GAN-inversion analogy and empirical claim of better performance (Sec. 3.5) constitute adequate justification for a paper of this class. The complaint about missing main-paper ablation is removed per the rule that supplementary material (referenced at line 272) exists in the original submission and was stripped by the parser. A reduced version of this concern remains in Minor (the lack of a dedicated ablation table in the main paper is a presentation limitation, not a fatal gap).

- **"The paper should also cover additional tasks/domains"** — Scope creep. The paper evaluates on three settings (locomotion, interaction, long-term) across two scene types (synthetic, real), which is a thorough evaluation for a single paper.

- **"Method relies on LLMs but this component is not evaluated"** — This is noted in Trivial but the criticism is downgraded because the contribution does not depend on the LLM component; the paper's core pipeline works with predefined sub-tasks.

- **"SMPL-X axis-angle representation may have discontinuities"** — A known property of the representation. The paper's power-space blending (Sec. 3.6) explicitly addresses this for transitions, and this is a standard representation in the field. Removed as a non-issue.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any observation about the work that is not already present in the paper's narrative.

## Suggestions

1. **Correct the abstract** to replace "better motion naturalness" with "comparable motion naturalness" or "on par with state-of-the-art methods in motion naturalness," matching the actual conclusions in Sec. 4.4.
2. **Add a short limitations paragraph** in the conclusion or a dedicated limitations section discussing the reward-engineering burden, potential failure cases when the diffusion prior conflicts with reward signals, and the inference-time cost of the optimization loop.
3. **Move the key ablation** (GAN-inversion optimization vs. direct \(\mu_t\) optimization vs. no optimization) from supplementary to the main paper, even if as a small table. This directly validates the central technical claim.
4. **Report vertex-based contact scores** alongside the joint-based metric in Tables 1–2 to support the explanation for the contact-score gap.

## Score and Decision

**Originality:** The framework's core idea — decoupling motion prior from interaction knowledge via unpaired diffusion training + inference-time reward optimization — is genuinely novel and moves beyond the paired-data paradigm that dominates the field.  
**Quality:** The method is technically coherent with reasonable design choices. The evaluation is solid but would benefit from a main-paper ablation of the key technical move.  
**Clarity:** The paper is generally well-written and the method is clearly explained. The abstract contains a factual inaccuracy that should be corrected.  
**Significance:** The contribution is valuable: demonstrating that competitive scene-aware motion synthesis is possible without paired training data opens up practical applications where such data is scarce. This is likely to be influential.

The paper presents a solid, novel contribution with no fatal flaws. The identified issues are all addressable without re-running experiments. The most impactful change would be correcting the abstract's inaccurate claim about motion naturalness, which is a simple textual fix.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>