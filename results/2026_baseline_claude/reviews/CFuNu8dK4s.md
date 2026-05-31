## Summary

Vidar is a framework for bimanual robotic manipulation that leverages video diffusion as a cross-embodiment prior. The system consists of: (1) an embodied video diffusion model continuously pre-trained on ~750K multi-view trajectories from three robot platforms using a unified observation space that encodes robot, camera, task, and scene context without action labels; and (2) a Masked Inverse Dynamics Model (MIDM) that learns action-relevant pixel masks via implicit regularization rather than dense supervision. With only ~20 minutes of human demonstration on an unseen robot, Vidar achieves large margins over strong baselines on both the RoboTwin simulation benchmark and real-world bimanual manipulation tasks.

---

## Strengths

- **Large empirical gains with minimal data**: Vidar achieves 68.2% vs. 36.4% (UniPi) and 4.5% (VPP) on seen real-world tasks, and 66.7% vs. 6.7%/13.3% on unseen tasks—margins that are large enough to be convincing even given potential confounds. The simulation results (60% vs. 25% Pi0.5 in low-data clean setting) are similarly compelling.
- **MIDM is novel and principled**: Learning action-relevant spatial masks purely from action regression supervision via L1 regularization and straight-through estimators is elegant. Table 4 shows a 2× improvement in testing accuracy over the ResNet baseline (49.0% vs. 24.3%), and Figure 3 shows the masks meaningfully localize end-effectors and joints on reflective, unseen backgrounds.
- **Unified observation space without actions**: The design choice to exclude action labels from the video diffusion model's conditioning—instead encoding robot type, camera description, and task—is well-motivated. Table 3 confirms that embodied pre-training substantially improves subject consistency (0.565 → 0.855) and imaging quality (0.345 → 0.667) as measured by VBench.
- **Multi-backbone and multi-domain validation**: Vidar is validated on Wan2.2, Vidu 2.0, and HunyuanVideo, across both simulation and real-world settings, lending credibility to the generality of the approach rather than tying results to a single model.
- **Ablation covers all key components**: Table 5 cleanly isolates the contributions of MIDM and test-time scaling in a consistent evaluation setting.

---

## Weaknesses

### Fatal
None.

### Major

- **Open-loop control is a serious limitation inadequately addressed**: Vidar generates an entire 60-frame video in one shot and executes it without feedback. Errors in early frames propagate unchecked—a design choice that is particularly problematic for contact-rich bimanual manipulation. The 25-second generation time per video (on 8×80GB GPUs) makes reactive replanning impractical. The paper acknowledges "distillation or quantization" as future work but does not quantify how often open-loop failures occur or whether TTS compensates for this structurally (it only selects better initial rollouts, not corrected ones). Given the small per-task success counts (few episodes per task), the impact of open-loop execution on reliability is unclear.

- **MIDM testing accuracy of 49% is low and its connection to task success is unclear**: Even with MIDM, roughly half of predicted action sequences fall outside the acceptance threshold (∞-norm < 0.06 for joints). Yet the system achieves 68.2% task success. The paper does not explain this apparent gap—it's possible that only a subset of frames are critical, or that the threshold is conservative, but without this analysis the reader cannot assess MIDM's actual reliability in the control loop.

- **Fairness of real-world baselines is questionable**: The comparison with VPP and UniPi involves re-implementing these methods on Vidu 2.0, a backbone the original authors did not design for. Vidar benefits from 750K episodes of embodied pre-training while UniPi gets none. These differences are not fully factored into the framing of the comparison. Pi0.5 is relegated to Appendix D for real-world results (with a different base model), leaving the headline comparison without a fully trained VLA baseline.

### Minor

- **Test-time scaling depends on GPT-4o**: Using a closed-source API model as the reranker introduces cost, latency, and reproducibility concerns. The paper does not report how sensitive results are to the choice of evaluator or what failure modes GPT-4o exhibits when scoring robot videos.

- **Target platform "unseen" claim needs clarification**: Pre-training includes RDT episodes, which were collected on Aloha robots. The fine-tuning target is described as "Aloha (agilex)"—it is not fully clear whether the morphology is genuinely novel or merely a camera-adjusted variant of a seen platform. This affects the interpretation of cross-embodiment generalization.

- **Real-world evaluation scale**: The real-world test covers 17 distinct tasks but with only ~3 demonstrations each and 6 or fewer episodes per scenario group in Table 2. With 6 episodes in "Seen Tasks & Backgrounds" (at 68.2% ≈ 4.1/6), the confidence intervals are wide and differences of a few successes change the relative rankings meaningfully.

### Trivial
None.

---

## Nice-to-Haves

- Reporting per-task results in the main paper (rather than aggregated averages) would help identify where Vidar specifically succeeds or struggles.
- A qualitative analysis of when TTS improves or fails—e.g., whether GPT-4o reranking helps more on semantically ambiguous than on motor-precision tasks—would strengthen the test-time scaling contribution.

---

## Novel Insights

The most genuinely novel observation in this work is that separating world-model learning from action-space learning—by keeping the video diffusion model action-agnostic and offloading embodiment adaptation entirely to a lightweight, sparsity-regularized inverse dynamics module—enables surprisingly efficient cross-embodiment transfer. The implicit spatial attention learned by MIDM from pure action supervision, without any segmentation annotation, generalizes to novel backgrounds and reflective surfaces in a way that off-the-shelf segmentation methods (reported to fail in ablations) do not. This suggests that the inductive bias of sparsity regularization in the visual domain may be a more robust signal for robot-relevant region discovery than appearance-based segmentation at the scale of limited demonstration data. Additionally, the application of test-time scaling (via rejection sampling over video rollouts with a VLM ranker) to robot video generation—rather than answer selection in LLMs—is a concrete, transferable design pattern for stochastic robot planners.

---

## Suggestions

- Report closed-loop vs. open-loop comparisons for the same method (e.g., using a simple replanning schedule) to isolate how much performance is lost/gained by open-loop execution.
- Characterize the MIDM accuracy–task success correlation explicitly: show that tasks with higher MIDM accuracy also have higher execution success.
- Provide confidence intervals or episode counts per cell in Tables 2 and 5 so readers can assess statistical significance.
- Ablate the GPT-4o ranker with a simpler alternative (e.g., CLIP score) to establish that TTS does not require a closed-source model.

---

## Score and Decision

Vidar presents a coherent, well-motivated system for data-efficient bimanual manipulation with genuinely large empirical gains. The MIDM contribution is novel and lightweight, the unified observation space design is principled, and the multi-platform evaluation is more thorough than much prior work. The key open issues—open-loop execution reliability and the opacity of the MIDM-accuracy/task-success gap—weigh against a high accept, but the large performance margins and practical impact of the "one prior, many embodiments" recipe make this a solid borderline accept.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>