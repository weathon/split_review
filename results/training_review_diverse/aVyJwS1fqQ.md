Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper proposes Mani-WM, a Diffusion Transformer-based world model that generates realistic videos of a robot arm executing a given action trajectory from a single initial frame (the "trajectory-to-video" task). The key technical contribution is a **frame-level conditioning mechanism (Frame-Ada)** that encodes each action individually and applies per-frame scale/shift parameters, achieving precise action-to-frame alignment. The method is validated on four real-robot datasets (RT-1, Bridge, Language-Table, RoboNet) with human evaluation, scaling analysis, flexible controllability demos, and a real-robot model-based planning experiment.

---

## Strengths

1. **Frame-level conditioning is a clean and well-motivated contribution that demonstrably improves alignment.** The paper shows Frame-Ada consistently outperforms the Video-Ada variant on Latent L2 loss and PSNR across all three main datasets (Table 1), directly validating that per-frame action conditioning matters. The design is technically sound — encoding each action individually instead of collapsing the trajectory into a single embedding is a natural architectural choice for this task.

2. **Scaling behavior is clearly demonstrated.** Figure 5 tracks Latent L2 loss across model sizes from 33M to 679M parameters and multiple training steps on three datasets, showing monotonic improvement. This is a strong signal that the method benefits from additional compute, which is important for a generative model of this class.

3. **Human preference evaluation cross-validates the primary metrics.** The user study (Figure 4) shows Mani-WM-Frame-Ada is preferred over all baselines on all datasets, and the paper demonstrates that this aligns with Latent L2 loss and PSNR. This provides meaningful external validation of the evaluation protocol.

4. **Comparisons against domain-specific baselines on RoboNet.** Unlike many video prediction papers that only compare against text-to-video models, Mani-WM benchmarks against iVideoGPT and MaskViT on RoboNet (Table 3), showing superiority on FVD (156.7 vs. 172.0 for iVideoGPT). This grounds the work in the robotics video prediction literature.

5. **Flexible action controllability is demonstrated across diverse input sources.** Figure 6 shows Mani-WM generating accurate videos from keyboard inputs (Language-Table), VR controller inputs (RT-1, Bridge), and policy-generated trajectories — all distributionally different from training data. This supports the claim of robust generalization.

---

## Weaknesses

### Fatal
None.

### Major
- **Real-robot planning experiment is underspecified.** The model-based planning experiment (Table 4) reports accuracy values (e.g., 83.3% MSE vs. 25% Random) but does **not state the number of trials** per task, making it impossible to assess statistical reliability. "Accuracy" is not formally defined (though clearly interpretable as success rate from context). There is no baseline using an alternative world model for planning. While the experiment serves as a useful proof-of-concept, the evidence for "significantly improving success rates" (paper's claim) is weakened by these omissions. This is the most significant gap in the paper.

### Minor
- **No uncertainty quantification on any quantitative result.** Every table reports point estimates without error bars, confidence intervals, or significance tests. While multi-seed evaluation of large diffusion models is expensive, even reporting variance across dataset splits or bootstrapped confidence intervals would substantially strengthen the reader's ability to assess whether observed differences (some of which are small) are meaningful. This is a widely noted community practice gap rather than a flaw unique to this paper, but it remains a weakness.

- **Baseline comparisons on the main datasets are limited to adapted text-to-video models.** On RT-1, Bridge, and Language-Table, the only baselines are VDM and LVDM — text-to-video models adapted by encoding the full trajectory into one embedding. iVideoGPT (which is directly designed for action-conditioned video prediction) is only compared on RoboNet, not on the three main datasets. The paper claims general "superiority," but the strongest domain-specific baseline (iVideoGPT) is absent from the main evaluation. This limits the strength of the superiority claim on these datasets.

- **The planning experiment does not compare against a simple open-loop policy without a world model.** The baseline is a "random trajectory selection" policy. A more informative baseline would be a policy that directly outputs actions without planning through Mani-WM, to isolate whether the world model adds value beyond the policy itself.

- **No quantitative analysis of error accumulation in autoregressive rollouts.** The long-video experiments use autoregressive feedback of predicted frames, but there is no frame-wise analysis of drift (e.g., PSNR or Latent L2 as a function of rollout step). This would help assess practical usability for long-horizon tasks.

### Trivial
- The method description of frame-level adaptation (Section 3.3) could benefit from a more formal mathematical specification of how scale/shift parameters interact with spatial vs. temporal attention blocks. A diagram is provided (Figure 2) but the text remains somewhat vague.

---

## Nice-to-Haves
- Comparing against VLP (Du et al., 2024), which is cited in related work and also uses text-to-video models as dynamics models for robot planning, would strengthen the baseline set. However, this is concurrent work and the omission is understandable.
- Reporting the number of trials for the real-robot planning experiment is not optional — it should be a required fix rather than a "nice-to-have," but it belongs in the Major weaknesses above.

---

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"The paper should include VLP as a baseline"** — cited as a weakness by the harsh critic. Kept as a Nice-to-Have above rather than a weakness, since VLP is concurrent work (Du et al., 2024) and the paper's baseline set is already reasonable. Not a core flaw.
- **"Tasks are not named"** (in the planning experiment) — The specific task names (Push Button, Move Cup, Close Drawer) are visible in Table 4's image, which is a parser artifact that the text cannot reproduce. The paper refers to "three manipulation tasks" in the body, which is sufficient given the table labels.
- **"No code or model release"** — the paper explicitly states: "We opensource the code at https://anonymous.4open.science/r/Mani-WM." This criticism questions a release that the paper confirms exists.
- **"The paper should report results with standard deviations across multiple seeds"** — Moved to Minor above (it's valid but ranked appropriately). Not removed, just downgraded.
- **Strength Finder claims that are generic** — The Strength Finder's "Outperforms both diffusion and non-diffusion baselines" is partially retained but contextualized under Minor weaknesses regarding baseline limitations.

---

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a pattern of results or a meta-observation that the paper itself does not articulate. The Frame-Ada vs. Video-Ada comparison is the paper's own analysis, and the reviewers' concerns about evaluation rigor are standard methodological critiques.

---

## Suggestions
1. **Report number of trials per task and define "Accuracy" for the planning experiment.** Without this, the results in Table 4 are uninterpretable for assessing statistical significance.
2. **Add error bars or confidence intervals** to at least the primary metrics in Table 1 and Table 2. Bootstrapping over test-set samples is straightforward and would address the most common reproducibility concern.
3. **Include a frame-wise drift analysis** for autoregressive rollouts (e.g., PSNR as a function of frame index) to quantify how prediction quality degrades over time.
4. **Extend the iVideoGPT comparison** to at least one of the main datasets (RT-1 or Bridge) to strengthen the claim of superiority over domain-specific baselines.
5. **Add an open-loop policy baseline** to the planning experiment to isolate the value added by the world model.
6. **Clarify in the method description** whether scale/shift parameters are shared across patches within a frame or computed per-patch, and how the timestep embedding interacts with the action embedding.

---

## Score and Decision

This paper presents a novel and well-motivated method for the trajectory-to-video task. The core contribution — frame-level conditioning in a Diffusion Transformer — is technically sound and empirically validated through multiple lenses (quantitative metrics, human evaluation, scaling analysis, controllability). The weaknesses are real but addressable: the planning experiment needs more rigor, error bars are absent, and the baseline set on the main datasets could be stronger. None of these undermine the core technical contribution, and the evidence supporting frame-level conditioning's advantage is clear. The paper would benefit from a major revision focused on evaluation rigor, but the contribution is already substantive enough for acceptance.

**Score:** 7.0

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>