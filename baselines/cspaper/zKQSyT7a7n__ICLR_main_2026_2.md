---
job_id: d1df3c65-f9cc-4714-bfed-42a32bff095d
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: zKQSyT7a7n.pdf
paper: Visuo-Tactile World Models
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically multimodal representation learning, generative/world models, and applications to robotics and planning.

## Minimum Quality
Pass ✅. The paper contains the expected core sections, presents a concrete method with equations and experiments, and is understandable enough for full review, even though I have substantial concerns about evaluation design, methodological specification, and strength of evidence.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions to reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes a multi-task visuo-tactile world model, VT-WM, that combines exocentric vision latents and tactile latents from fingertip sensors within an action-conditioned transformer dynamics model. The paper compares VT-WM against a vision-only world model on contact-perception metrics, real-robot zero-shot planning with CEM, and low-data adaptation to a new task, arguing that tactile grounding improves object permanence, causal compliance, and planning success in contact-rich manipulation.

## Strengths
1. The paper addresses a meaningful and timely problem. The core motivation, namely that vision-only world models struggle under occlusion and contact ambiguity, is well articulated and highly relevant for robot manipulation. This is not a contrived multimodal add-on, the paper is targeting a real failure mode of existing robot world models.

2. The paper presents a reasonably clean multimodal architecture. The design in **Figure 3** is intuitive and easy to follow: pretrained vision and tactile encoders produce latent tokens, which are fused and processed by a transformer with spatio-temporal self-attention and action cross-attention. Even though some details are underspecified, the high-level modeling choice is sensible and matches the problem setting.

3. The qualitative evidence is compelling in places. In particular, **Figure 5** and **Figure 7** make the paper’s central claim concrete. In **Figure 5**, the contrast between V-WM losing or deforming objects and VT-WM preserving hand-object interaction is visually persuasive, especially in the cube transport/placement example. In **Figure 7**, the non-contact wiping case is a good stress test for whether the model confuses proximity with contact, and the VT-WM rollout indeed appears better behaved than the vision-only baseline.

4. The real-robot planning evaluation is more valuable than purely offline video metrics. The bar plot in **Figure 8 (left)** shows that the claimed gains are not limited to rollout appearance, VT-WM also improves task success in several contact-rich settings. I appreciate that the paper includes multi-step tasks rather than only trivial one-shot reaching.

5. The paper is reasonably clear at the narrative level. The introduction, problem framing, and experimental questions are easy to understand. The distinction between “contact perception,” “zero-shot planning,” and “data efficiency” gives the experimental section a coherent structure.

6. The work uses a multi-task dataset rather than training per-task dynamics models. That gives the paper somewhat broader relevance than many earlier visuo-tactile dynamics papers focused on a single task or object family.

## Weaknesses
1. **The technical formulation is underspecified at key points, especially around the predictor and training objective.**  
   The model description in **Section 3.2** is too loose for a paper whose main contribution is a new world model. The paper writes
   \[
   (s_{k+1}, t_{k+1}) \sim P_\phi(s_k,t_k \mid a_k),
   \]
   on **Page 4**, but this expression is malformed as written: the next-state distribution should condition on current states and actions and output next states, something like
   \[
   P_\phi(s_{k+1}, t_{k+1}\mid s_{\le k}, t_{\le k}, a_{\le k})
   \]
   or, if Markov, \(P_\phi(s_{k+1}, t_{k+1}\mid s_k,t_k,a_k)\). The current notation confuses inputs and outputs. That may look cosmetic, but here it matters because the paper repeatedly emphasizes autoregressive prediction with temporal context, so the formal object should match the actual architecture.

   The same issue appears in the losses in **Equations (1) and (2)** on **Page 5**. The notation for \(\hat{s}_{k+1}\) and \(\hat{t}_{k+1}\) does not specify whether predictions are tokenwise, framewise, or pooled latents; nor is it clear how the loss aggregates across spatial tokens, vision patches, tactile sensors, and time. The paper earlier says the representation is projected into \(\mathbb{R}^{(b,t,s,d)}\), but the loss is written as a simple \(\ell_1\) norm over latent states. This is a nontrivial omission because the exact target granularity strongly affects stability and what is actually being predicted.

2. **The sampling-loss training procedure is not specified precisely enough to evaluate correctness or reproducibility.**  
   In **Equation (2)**, the paper says sampled states are generated autoregressively “without gradients” for \(H=3\) to \(5\) steps, and then a sampling loss is computed. But it is unclear what exactly is fed back as model input: raw predicted latents, discretized tokens, detached continuous embeddings, or something else. It is also unclear whether the autoregressive rollout is anchored by the full ground-truth prefix or whether model predictions fully replace future context within the sampled horizon. This matters because there are very different failure modes depending on whether one uses scheduled sampling, detached latent rollouts, or multi-step consistency training. Right now the description is too hand-wavy for the reader to determine what training signal is actually applied.

3. **The experimental evidence is suggestive, but not yet strong enough to isolate the source of gains.**  
   The main comparison is VT-WM versus V-WM, but many things differ implicitly besides just “adding tactile grounding.” On **Page 4**, VT-WM uses tactile tokens concatenated with visual tokens, which changes the model’s input bandwidth, number of tokens, and effective conditioning information. The paper does not include a control baseline that matches this extra input capacity without meaningful tactile semantics, for example shuffled tactile streams, zeroed tactile tokens at test time, or another contact proxy such as proprioception-only augmentation. Without such controls, it is hard to know whether gains come from tactile contact reasoning specifically or just from more information and better state disambiguation in a generic sense.

4. **The planning evaluation is too small and statistically weak for the paper’s stronger claims.**  
   On **Page 9**, the real-robot planning results in **Figure 8 (left)** are averaged over only **five trials per task** from distinct initial conditions. That is a very small sample size for drawing strong conclusions about zero-shot planning performance, especially when reported improvements include values like \(10\%\) and \(11\%\), which correspond to half-trial granularity if interpreted literally from five runs, or at best one-trial differences under rounding. The figure is visually striking, but the evidence base is thin. There are no confidence intervals, no statistical tests, and no breakdown of failure modes per method in the main paper. For a robotics paper this may be understandable, but for ICLR-level claims about planning improvements, it is not enough.

5. **The paper leans heavily on qualitative examples and bar plots, but omits important quantitative details that would make the results more convincing.**  
   The contact-perception section reports average relative improvements and paired \(t\)-tests in text, and **Figures 4 and 6** show bar charts with 95% CI, but the paper never states the underlying number of evaluated trajectories per task in the main paper. That omission makes the significance discussion hard to assess. Relatedly, **Figure 4** and **Figure 6** show substantial variance for some tasks, especially stacking and wiping, and one task even degrades in causal compliance (“scribble with marker”). The paper acknowledges this, but does not analyze why tactile hurts there, or when the tactile branch becomes unreliable. A world model paper should not only celebrate the average gain; it should explain the failure regime.

6. **The evaluation metrics only partially support the claims about “laws of motion” and physical grounding.**  
   The paper equates causal compliance with low normalized Fréchet distance for keypoints on objects that should remain stationary, as described on **Pages 6-7**. That is a useful heuristic, but calling this “compliance with physical laws” is too strong. Low trajectory error on passive objects measures one narrow aspect of physical plausibility, namely not hallucinating motion for selected tracked points. It does not test contact force consistency, momentum changes, or whether the manipulated object’s motion is dynamically plausible. This matters because the abstract and conclusion use language that sounds broader than what the metric actually validates.

7. **The planning objective is purely visual, which weakens the paper’s claim that tactile information is crucial at planning time.**  
   In **Section 3.2.3** on **Page 5**, the planner’s cost is
   \[
   \|s_{k+H} - s_{\mathrm{goal}}\|_2,
   \]
   using only the final visual latent. The tactile branch influences planning only indirectly through improved rollout quality and initial-state disambiguation. That is a perfectly reasonable design choice, but the paper’s rhetoric sometimes overstates this into “touch reasoning” in planning. As written, the planner is still solving a vision-goal optimization problem using a multimodal dynamics prior. The distinction matters, especially because no experiment compares visual-goal planning versus visuo-tactile-goal planning, or investigates whether tactile predictions themselves correlate with successful plans.

8. **The data-efficiency claim is currently the weakest part of the paper.**  
   The comparison in **Section 4.3** and **Figure 8 (right)** is between a fine-tuned multi-task VT-WM planner and a task-specific BC policy trained on the same 20 demonstrations. This is not a fair apples-to-apples comparison if the claim is about sample efficiency of the modeling paradigm rather than reuse of prior pretraining. VT-WM benefits from a sizable multi-task pretraining corpus, while BC is trained from scratch on the new task. Unsurprisingly, the pretrained model transfers better. That result is not useless, but it supports “benefit of prior multi-task world-model pretraining” more than “data efficiency versus BC” in the abstract sense. A fairer test would compare against a multi-task pretrained visuo-tactile policy, a fine-tuned V-WM, or at least a stronger imitation baseline using the same prior data.

9. **The paper does not sufficiently position itself against prior visuo-tactile dynamics/control work.**  
   The related work mentions only one prior vision-and-touch world-model style paper, **Zhang & Demiris (2023)**, and a few tactile dynamics papers. That discussion feels thin given the paper’s claim of being the first multi-task visuo-tactile world model. Even if the exact setting is new, the paper should do a better job differentiating itself from broader visuo-tactile dynamics modeling and visuo-tactile control literature. Right now the novelty claim is stronger than the comparative discussion supporting it.

10. **Some important implementation choices are buried or missing from the main paper.**  
   For example, the tactile input is described as “two frames per Digit 360 sensor” covering 0.16 seconds, while the model uses a maximum context length of 9 frames for both modalities on **Page 5**. It is not obvious how these asynchronous modalities are aligned in the transformer input. Are tactile tokens repeated, temporally pooled, or inserted only at the latest step? Similarly, **Algorithm 1** on **Page 16** gives planning hyperparameters \(H=2\), \(P=36\), \(N=10\), but the main paper does not discuss sensitivity to these choices or whether both V-WM and VT-WM receive equal planning budgets and tuning. For planning papers, these choices can move results materially.

## Questions
1. Please clarify the precise predictive distribution and training targets. Is the model predicting per-token future latent embeddings, pooled frame embeddings, or some modality-specific summary? A clearer mathematical statement of the predictor and a token-level version of **Equations (1)-(2)** would increase my confidence.

2. In the sampling loss, what exactly is fed back into the model during the \(H\)-step detached rollout? Are predicted latents inserted in place of ground-truth latent tokens for all modalities and all spatial locations, or is there some mixed teacher-forcing schedule? This is central to understanding the training recipe.

3. Can the authors report the number of trajectories used for the object-permanence and causal-compliance statistics in **Figures 4 and 6**, and ideally provide per-task confidence intervals or significance tests directly tied to those counts? Right now the statistical evidence is difficult to calibrate.

4. For the planning results in **Figure 8 (left)**, can the authors provide raw successes over trials and some uncertainty estimate? With only five trials per task in the main paper, the gains are hard to interpret robustly.

5. Can the authors add a control showing whether the benefit is truly tactile semantics rather than simply extra conditioning information? Examples that would help are shuffled tactile inputs, stale tactile context, ablated tactile channels, or a proprioception-matched baseline.

6. The degradation on “scribble with marker” in **Figure 6** deserves analysis. Why does VT-WM underperform there? Is this due to noisy or intermittent contact, tracking issues, or the tactile modality being less informative for that task?

7. The data-efficiency claim would be much stronger with a better-matched baseline. Can the authors compare against at least one pretrained/fine-tuned policy baseline, or a fine-tuned V-WM on the same 20 demonstrations, to separate the effect of prior multi-task pretraining from the effect of the visuo-tactile world-model formulation?

8. Since the planning cost is purely visual, do the authors have evidence that predicted tactile trajectories correlate with successful plans, or examples where tactile rollout quality changes the action ranking within CEM? This would directly support the claim that tactile grounding improves planning rather than just rollout aesthetics.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond standard robot deployment considerations. The paper uses teleoperated manipulation and real-robot evaluation, but I did not identify a specific ethics issue that requires escalation based on the provided main paper.

## Soundness Rating
2: fair. The core idea is plausible and supported by some evidence, but important methodological details are underspecified and the empirical validation is not yet strong enough to fully support several central claims.

## Presentation Rating
3: good. The paper is readable and the qualitative figures are useful, but the mathematical formulation and several experimental details need sharper specification.

## Contribution Rating
2: fair. The problem is relevant and the multimodal direction is promising, but the current paper does not yet make a sufficiently well-isolated or thoroughly validated contribution for ICLR main track.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a good instinct, some convincing qualitative evidence, and an interesting application of tactile grounding to world models. Still, the current version overclaims relative to the experimental support, leaves important parts of the method underspecified, and relies on evaluations that do not yet fully isolate why VT-WM works or establish the strength of its planning and data-efficiency claims.

## Reviewer Confidence
4: confident. I am confident in this assessment and familiar with the relevant world-model and robot-learning setting, though some implementation details are missing from the paper and therefore cannot be fully verified.