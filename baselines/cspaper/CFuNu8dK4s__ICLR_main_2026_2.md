---
job_id: 20da1c39-ae46-4257-a2de-72e95ae95f72
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: CFuNu8dK4s.pdf
paper: Vidar: Embodied Video Diffusion Model for Generalist Manipulation
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining generative modeling, transfer learning, representation learning for robotics, and embodied control.

## Minimum Quality
Pass ✅. The submission contains the expected components, including abstract, introduction, method, experiments with quantitative and qualitative results, related work, and conclusion, and it presents a coherent research contribution with nontrivial empirical content.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious review-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes Vidar, a two-stage manipulation framework that factorizes policy learning into a video generation model and a masked inverse dynamics model. The approach starts from an Internet-pretrained video diffusion backbone, continues embodied pre-training on about 750K multi-view robot episodes from three platforms using a unified observation space, and then adapts to a new embodiment with a small amount of demonstration data. Experiments on RoboTwin and real-world Aloha-style bimanual manipulation report improved success rates over several video-based and VLA baselines, along with ablations on embodied pre-training, test-time scaling, and the masked inverse dynamics module.

## Strengths
1. The paper tackles an important problem, namely low-shot adaptation of manipulation policies to a new embodiment, and the high-level decomposition into a transferable video prior plus a lightweight embodiment-specific action decoder is sensible. The central idea in Section 2.1, namely factorizing $\pi = I \circ G$ with $G:\mathcal{L}\times\mathcal{O}\rightarrow \mathbb{P}(\mathcal{V})$ and $I:\mathcal{V}\rightarrow\mathcal{A}$, is easy to understand and gives a clear conceptual structure to the system.

2. The empirical headline results are promising. In **Table 1** on RoboTwin, Vidar improves over Pi0.5 in all reported aggregate settings, often by a large margin, especially in the low-data clean case, 60.0% vs 25.0%, and the standard clean case, 65.8% vs 44.8%. In the real-world setting, **Table 2** shows a large gap over UniPi and VPP, especially on unseen tasks, 66.7% vs 6.7% and 13.3%, respectively. Even allowing for variance concerns, these are nontrivial gains.

3. The paper includes ablations that are directionally useful. **Table 5** suggests that both MIDM and test-time scaling matter, and **Table 4** shows a substantial generalization gap improvement for MIDM over a plain ResNet inverse dynamics baseline, 49.0% vs 24.3% testing accuracy. This supports the claim that the masking mechanism is not merely cosmetic.

4. The visualization of the method pipeline in **Figure 1** is genuinely helpful. It makes clear the intended separation between pre-training, low-shot fine-tuning, test-time video selection, and video-to-action grounding. For a paper that combines several moving parts, this figure does real explanatory work.

5. The qualitative examples in **Figure 2** and the learned masks in **Figure 3** support the paper’s narrative that the method can be robust to background changes and that the inverse dynamics model does not simply key off the entire frame. In **Figure 3**, the masked images concentrate around the arms and interaction region even under reflective backgrounds, which is consistent with the intended role of MIDM.

6. The paper is reasonably well motivated from the robotics perspective. It explains why internet video alone is not enough for actionability, and why robot-specific end-to-end policies are expensive to adapt. That motivation is consistent across the introduction, method, and experiments.

## Weaknesses
1. The core methodological claim of embodiment transfer through a robot-agnostic video prior is undercut by an internal inconsistency about what the video model actually conditions on. On **Page 3**, immediately below **Figure 1**, the paper states that “$G$ is conditioned on proprioceptive traces and embodiment tokens,” but in the “Unified Observation Space” subsection on **Page 4** it explicitly says “The space does not include actions” and defines $\mathcal{U}\subseteq \mathcal{L}\times\mathcal{O}$ only through aggregated images and concatenated language fields in **Equation (3)**. It is unclear whether proprioception is part of $\mathcal{O}$ and actually used by $G$, whether it is only available at fine-tuning, or whether the diffusion prior is visually conditioned only. This matters because the main scientific claim is about action-feasible rollouts across embodiments. If the model uses proprioceptive traces, that should be formalized in the conditioning variable $c$ in **Equations (1)-(2)** and in **Equation (3)**; if it does not, then the feasibility claim is substantially weaker than advertised.

2. The mathematical specification of MIDM is too underspecified and arguably problematic as written. On **Page 5**, the model is defined by
\[
m = U(x), \qquad \hat a = R(\mathrm{Round}(m)\odot x),
\]
with loss
\[
L_I = \mathbb E_{x,a}[\, l(\hat a-a)+\lambda \|m\|_1 \,].
\]
Several key details are missing:
   - Is $x$ a single frame or a short temporal window? The text first says “input frame $x$,” but elsewhere the inverse dynamics model is described as mapping “short video windows” to actions in Section 2.1.
   - If actions are continuous multi-joint controls, what exact output dimensionality and time horizon are predicted? One step, multi-step chunk, or open-loop sequence?
   - How is the straight-through estimator implemented for $\mathrm{Round}(m)$, and how stable is training?
   - Is the mask shared across views or predicted separately for the concatenated image?
These are not cosmetic omissions. MIDM is a major contribution of the paper, and the current formulation is too vague to establish what is actually being optimized.

3. The use of hard rounding in MIDM is especially questionable for optimization and likely unnecessary. If the objective is sparsity and interpretability, one can use a continuous mask during training and perhaps threshold at inference. Here, the paper commits to $\mathrm{Round}(m)$ in the forward pass and says only “We train it using straight-through estimators” on **Page 5**. This creates a brittle discrete bottleneck, but no comparison is provided against the obvious softer alternative
\[
\hat a = R(m\odot x), \qquad m\in[0,1]^{H\times W},
\]
possibly with temperature annealing or entropy regularization. Given that **Table 4** is one of the central empirical supports for MIDM, it is surprising that there is no ablation on hard versus soft masking, nor on the choice of $\ell_1$ weight beyond the appendix-only sweep.

4. The experimental evidence for the claimed real-world robustness is quite thin in terms of sample size. **Table 2** reports average success rates over only 6 seen tasks, 5 unseen tasks, and 6 unseen-background tasks, and **Table 11** reveals that many entries are based on coarse increments of 33.3%, implying only three trials per task. This is a serious issue. With such tiny denominators, the difference between 66.7% and 33.3% is literally one success, and aggregate averages can swing dramatically. The paper makes strong generalization claims, but the real-world evidence is statistically fragile.

5. The comparisons are not fully fair, and in some cases the setup favors the proposed method. In **Section 3.1.3**, VPP is reproduced on the same Vidu 2.0 checkpoint, but VPP uses closed-loop control while Vidar uses open-loop control plus test-time scaling with GPT-4o. This means the systems differ not only in model structure but also in inference protocol, compute budget, and external evaluator usage. The paper does not normalize for test-time budget. Moreover, simulation disables test-time scaling “for better reproducibility” on **Page 6**, while real-world experiments keep it. This makes it difficult to separate the contribution of the model from the contribution of extra inference-time selection.

6. The test-time scaling component introduces an external multimodal judge, GPT-4o, in the control loop, but the paper treats it almost as a minor engineering detail. On **Page 4**, the evaluator is introduced abstractly as “a pretrained evaluator (e.g., CLIP or a vision-language model) $q_\eta$,” but on **Page 6** and **Figure 4** the actual real-world setup uses GPT-4o to select among $K=3$ generated videos. This matters for both scientific attribution and reproducibility. The gains in **Table 5** are not negligible, especially on unseen tasks, 66.7% with TTS vs 33.3% without. So the paper is partly a story about outsourcing trajectory ranking to a powerful external VLM. That is not necessarily illegitimate, but it should be foregrounded and evaluated more rigorously. For instance, does CLIP perform similarly? How much of the gain comes from the evaluator quality rather than the diffusion prior itself?

7. The “unified observation space” is conceptually central but technically weakly defined. **Equation (3)** introduces
\[
\mathcal U = \{\langle \mathbf o, \mathbf l\rangle \mid \mathbf o = \mathrm{aggregate}(\mathbf I^{(1)},\dots,\mathbf I^{(V)}), \mathbf l = \mathrm{concatenate}(l_r,l_c,l_t)\},
\]
and then says concretely that $\mathbf o = \bigoplus_{k=1}^V \phi_{r_k}(\mathbf I^{(k)})$. This is basically resized concatenation with textual descriptors. There is no mechanism ensuring camera calibration consistency, view alignment, robot morphology normalization, or temporal synchronization beyond hoping the foundation video model learns to absorb them. The empirical gain in **Table 3** is real, but from the main paper alone it is hard to tell whether this gain comes from the “unified observation space” concept or simply from additional robotics-domain pre-training. The current presentation overclaims a principled representation where the implementation seems fairly simple.

8. The video generation objective does not clearly support several claims made in the prose. **Equation (2)** is standard rectified flow matching,
\[
L_G=\mathbb E_{c,t,x_0,x_1}\left[\| (x_1-x_0)-v(tx_1+(1-t)x_0,t,c)\|^2\right],
\]
but the text repeatedly claims that the model learns “physically plausible,” “contact-consistent,” and “actionable” rollouts. None of those properties is encoded in the objective in the main paper. There is no contact loss, no action-consistency loss, no temporal dynamics regularizer beyond what the pretrained model already provides, and no explicit embodiment constraint. This gap between the mathematical objective and the verbal claims should be narrowed. At present, the method seems more empirical than the exposition admits.

9. The interpretation of **Table 3** is overstated. The table shows better VBench scores after embodied pre-training, but the metrics are “Subject Consistency,” “Background Consistency,” and “Imaging Quality.” These are generic generative video quality proxies, not measures of actionability or control usefulness. Yet the text on **Page 7** says these are “important for robot control tasks,” which may be directionally true, but it is not enough to establish that the generated videos are better for inverse dynamics decoding. A more convincing connection would require correlating VBench improvements with downstream control or using robot-relevant video metrics.

10. Some of the strongest claims are undermined by the appendix task-level breakdowns. In **Table 9**, even under the clean standard setting, Vidar underperforms Pi0.5 on some tasks, for example “Adjust Bottle” 63.0% vs 98.0%, “Handover Block” 2.0% vs 4.0%, “Handover Mic” 24.0% vs 31.0%, and “Hanging Mug” 1.0% vs 8.0%. In **Table 10**, randomized performance remains quite low overall, 17.5% average in the standard regime. This does not invalidate the average gain, but it tempers the “generalist manipulation” framing. The method looks useful, but still brittle.

11. The qualitative evidence is somewhat selective. **Figure 2** showcases successful unseen-task and unseen-background cases, and **Figure 3** shows favorable masks, but the main paper does not include failure taxonomies or cases where the masks attend to the wrong regions. Since MIDM is a major selling point, seeing only successful masks and successful executions makes the story cleaner than the evidence likely is. The appendix apparently has failures, but the main paper would benefit from at least one explicit failure mode analysis.

12. The paper’s positioning against related work is incomplete in one important respect. The authors argue for an open-loop video prior plus inverse dynamics decomposition, but they do not discuss close relatives in embodied video diffusion and world-model-based control that would help clarify what is specifically new here beyond scale and engineering. The related work section on **Pages 9-10** cites UniPi, VPP, VidMan, and others, which is good, but the contrast between “decoupled video generation and action prediction” versus more action-aware or closed-loop video-control formulations is still somewhat shallow. Given how central this design choice is, a sharper comparison would help.

## Questions
1. Please clarify the conditioning variables of the video generator precisely. In **Section 2.1** you say $G$ is conditioned on proprioceptive traces and embodiment tokens, but **Equation (3)** only defines conditioning through multi-view images plus concatenated language descriptors. What exactly is the conditioning tuple $c$ in **Equations (1)-(2)**? Is proprioception used during pre-training, fine-tuning, both, or neither?

2. What exactly is the input-output mapping of MIDM? Is $x$ a single image, a stacked multi-view frame, or a temporal clip? Is $\hat a$ a one-step action, a chunk of actions, or a horizon-conditioned sequence? Please specify the tensor shapes and time indexing clearly.

3. Can you provide an ablation comparing hard masking with straight-through rounding versus soft masking, for example using $R(m\odot x)$ without $\mathrm{Round}(\cdot)$? This would materially increase my confidence that the proposed MIDM formulation itself, rather than just any sparsity-biased attention mechanism, is responsible for the gains in **Table 4** and **Table 5**.

4. For the real-world results in **Table 2** and **Table 11**, how many trials were run per task, and can you report confidence intervals or binomial standard errors? The current granularity strongly suggests only three trials per task in many cases, which is too small to support strong generalization claims.

5. How much of the TTS improvement depends on GPT-4o specifically? Could the authors report results with CLIP or another frozen open evaluator, or at least show that the ranking quality is not uniquely dependent on a proprietary model? This matters because **Table 5** shows large gains from TTS.

6. In **Table 3**, can you connect the VBench improvements to downstream control more directly? For example, is there a correlation between per-task video quality improvements and action success, or an ablation showing downstream performance without embodied pre-training but with the same MIDM?

7. Since Vidar is open-loop at deployment, what is the failure profile on long-horizon tasks? The paper mentions 60-frame videos over 7.5 seconds on **Page 6**. How often do execution errors compound because the robot cannot replan mid-trajectory, especially compared with the closed-loop VPP baseline?

8. The task-level breakdowns in **Tables 9-10** show several tasks where Pi0.5 is better. Can the authors characterize what kinds of tasks remain hard for Vidar, for example handover, articulation, or precise contact tasks? A structured failure analysis would strengthen the paper.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications  

## Details Of Ethics Concerns
The ethics statement in **Section 6** is brief and acknowledges privacy and safety in human-robot interaction, which is appropriate, but the paper uses real-world robot manipulation with increasingly capable bimanual control and minimal adaptation data. Such systems can create safety risks during deployment in cluttered environments or around humans, especially because the method is explicitly **open-loop** at inference, as stated on **Page 6**, meaning there is limited opportunity for corrective replanning once execution starts. In addition, the use of Internet-pretrained video models and public robotics videos raises the usual data provenance and privacy considerations, although the paper does not indicate a direct misuse. I do not see a reason to block the paper on ethics grounds, but these concerns deserve at least brief discussion in the final version.

## Soundness Rating
2: fair. The empirical results are interesting and several design choices are supported by ablations, but key parts of the method, especially the conditioning of the video model and the exact MIDM formulation, are underspecified, and the real-world evaluation is too small to fully support the breadth of the claims.

## Presentation Rating
3: good. The paper is generally readable and the high-level story is easy to follow, with useful figures such as **Figure 1** and convincing qualitative examples, but several important technical details and mathematical definitions are missing or inconsistent.

## Contribution Rating
2: fair. The paper addresses an important problem and shows promising empirical gains, but the current evidence does not yet fully justify the scope of the claims around generalist, cross-embodiment manipulation, and some of the contribution appears to come from a combination of pretraining scale, external test-time ranking, and a lightweight masking module rather than a clearly isolated conceptual advance.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with the relevant literature on robot learning, video generation, and inverse dynamics, though some implementation details are omitted in the paper and limit absolute certainty.