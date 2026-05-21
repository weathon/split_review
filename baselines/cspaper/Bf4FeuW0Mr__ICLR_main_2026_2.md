---
job_id: cb2905a4-9708-43e1-9fbc-ad98fb2a8d30
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Bf4FeuW0Mr.pdf
paper: DemoGrasp: Universal Dexterous Grasping from a Single Demonstration
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, centered on reinforcement learning, visuomotor policy learning, sim-to-real transfer, and robotic grasping.

## Minimum Quality
Pass ✅. The paper contains the necessary research components, including abstract, introduction, method, experiments with quantitative results, and conclusion/limitations; while there are important weaknesses in methodological clarity and evaluation fairness, they do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I do not see evidence in the provided paper content of hidden prompts, manipulative instructions to automated reviewers, or other concealed review-targeting content.

# Expected Review Outcome:
## Summary
This paper proposes DemoGrasp, a framework for universal dexterous grasping that starts from a single successful demonstration and learns, via reinforcement learning, how to edit that demonstration using an end-effector transformation and hand-joint offsets. The authors cast this as a single-step MDP, optimize the editing policy in simulation with a simple success-plus-collision reward, and then distill successful rollouts into a vision-based flow-matching policy for sim-to-real transfer. Experiments cover large-scale simulation on DexGraspNet, cross-dataset and cross-embodiment evaluations, real-robot tests on 110 unseen objects, and several ablations.

## Strengths
1. The paper has a clear and intuitively appealing core idea. Replacing low-level long-horizon exploration with demonstration editing in a compact action space is a sensible design choice for dexterous grasping, where standard RL is notoriously brittle. The formulation in Section 2.3 is easy to understand conceptually, and **Figure 2** does a good job showing the overall pipeline from single demonstration, to RL-based editing, to vision-based distillation for sim-to-real transfer.

2. The empirical scope is strong. The paper evaluates on a large DexGraspNet setup, multiple unseen datasets, several embodiments, and a real robot. This breadth is a real asset, especially in a robotics paper where many submissions stop at simulation or only show a narrow embodiment. The results in **Table 1** are particularly strong numerically: DemoGrasp improves over UniGraspTransformer on all six entries, with gains that are not tiny noise-level differences. If these comparisons are under matched settings, this is meaningful evidence that the formulation is effective.

3. The cross-embodiment story is interesting and practically valuable. The claim that the same framework extends to Shadow, Inspire, Allegro, Schunk, DClaw, and even a parallel gripper, with no hyperparameter tuning, is one of the more compelling parts of the paper. **Figure 3** and the associated discussion in Section 3.3 make the embodiment-generalization argument visually and quantitatively plausible.

4. The real-world evaluation is broader than usual. Testing on 110 unseen objects is a serious effort, and **Table 3** suggests the method is not only working on easy “demo-friendly” objects. The inclusion of small and thin objects is especially valuable because tabletop dexterous grasping papers often quietly avoid this regime. **Figure 7** also helps here, since it shows not only standard successful grasps but also examples involving slight table contact and recovery behavior.

5. The ablations are reasonably informative. **Table 5** addresses the necessity of RL relative to simple sampling plus behavior cloning, and **Table 8** isolates the contributions of translation, rotation, and hand-joint editing. This is better than the usual single ablation table with vague conclusions. In particular, **Table 8** supports the paper’s central premise that the chosen demonstration-editing action space is not arbitrary, since expanding it yields substantial gains.

6. The paper is generally readable. The high-level narrative is straightforward, the motivation is easy to follow, and the figures are well chosen. **Figure 4**, while qualitative, is useful because it grounds the abstract claim about hand-DoF editing in visible grasp differences rather than just aggregate scores.

## Weaknesses
1. The technical formulation around the edited trajectory is underspecified and somewhat sloppy mathematically, especially in **Equations (1) and (2)** on **Page 5**.  
   - In **Equation (1)**, the notation
     \[
     [\,\mathbf{0}\ \Delta \mathbf{z}\,]\, p_{T_{\text{lift}}}^{*\prime\text{ee-obj}}
     \]
     is not a standard or self-explanatory way to denote a rigid transform. It is unclear whether this is meant to be a homogeneous transform with identity rotation and translation \(\Delta \mathbf z\), or an overwrite of only the translation component, or something else entirely. Since the policy action space explicitly includes orientation editing before \(T_{\text{lift}}\), the exact post-lift pose update matters.
   - In **Equation (2)**, the factor
     \[
     \Bigg(\frac{q_{T_{\text{lift}}}^{*\text{hand}}+\Delta q^{\mathrm{G}}-q_{0}^{*\text{hand}}}{q_{T_{\text{lift}}}^{*\text{hand}}-q_{0}^{*\text{hand}}}\Bigg)
     \]
     is said to be applied elementwise, but this raises immediate edge-case questions. What happens when a joint has \(q_{T_{\text{lift}}}^{*\text{hand}} = q_{0}^{*\text{hand}}\)? Then the denominator is zero. Given the hand has many joints, some joints staying unchanged over the demo is not some pathological corner case, it is likely. The paper should specify an \(\epsilon\)-stabilized form, a masking rule, or a different interpolation parameterization. As written, the core hand-editing equation is incomplete.
   - More broadly, the action \(T^{\text{ee}} \in SE(3)\) is later represented with Euler angles in the action space, while observation uses quaternions. The paper never explains how the composed transform is implemented, how angle wrapping is handled, or whether discontinuities near \(\pm\pi\) affect learning. This does not invalidate the method, but it is part of the core mechanism and should be stated more carefully.

2. The “single-step MDP” simplification is conceptually useful, but it also hides important control assumptions that are not sufficiently discussed in the main paper. In Section 2.3, the policy acts once and the system then replays the edited demonstration open-loop. That means the actual success depends heavily on the tracking controller, initial motion planning to the edited start pose, and simulator dynamics. Yet these ingredients are mostly deferred to later implementation details. This matters scientifically because the paper’s contribution is not only the policy parameterization; it is the interaction between trajectory editing, controller smoothness, and physical execution. Without making that dependence more explicit in the main text, the method risks looking more universally applicable than it may actually be.

3. The comparison protocol against prior work is not fully convincing in places. The paper repeatedly emphasizes simplicity, especially relative to baselines with dense rewards or more elaborate pipelines, but several comparisons are not apples-to-apples enough to cleanly support the stronger claims.
   - In **Table 1** on **Page 6**, the numbers are impressive, but the paper also notes that baseline methods do not randomize object initial positions whereas DemoGrasp does. That strengthens the paper in one sense, but it also makes direct benchmarking less controlled, because training conditions differ. If the message is “our method is better even under harder spatial randomization,” then I buy that directionally, but the paper should be more cautious when converting this into a clean SOTA claim.
   - In **Table 2** on **Page 7**, the comparison to RobustDexGrasp is explicitly under different training object datasets. The authors argue the test sets are unseen for both methods and therefore the comparison is fair. I do not think that fully follows. Training distribution matters a lot for universal grasping; unseen test objects are not enough to guarantee fairness if one model was trained on a materially more favorable or broader set. This table is suggestive, but it is weaker evidence than the paper presents it as.
   - Similar concerns apply to the real-world comparisons, which are mostly framed against prior papers qualitatively rather than under matched protocols.

4. The paper leans very hard on the claim that a single demonstration is enough, but the evidence for the limits of that claim is thinner than it should be. **Table 9** shows robustness to four successful demonstrations with different object sizes and grasp directions, which is useful, but all demonstrations are still successful and still come from a fairly similar grasping family. The paper does not test sensitivity to a genuinely poor or awkward demonstration, nor does it characterize what properties the demonstration must satisfy. This matters because “single demonstration” is the eye-catching claim, and in practice the hidden requirement may be “single carefully chosen canonical demonstration that already contains the right temporal structure and kinematic affordances.”

5. The reported generalization claims are somewhat overstated relative to the evidence. For example, Section 3.3 says the method achieves “average success rate of \(84.6\%\) on six unseen object datasets across various embodiments,” which sounds broad and robust, but **Table 10** shows substantial spread across embodiments and datasets. The FR3+Gripper result is far from universal, and even among multi-fingered hands the DGA and ModelNet40 numbers vary quite a lot. This does not negate the contribution, but the phrasing in the paper often slides from “works well in many cases” to “universal” without enough caveats.

6. Some ablation interpretations are too confident for the evidence shown. In Section 3.5, the explanation for **Table 5** is that sampling creates a multimodal, inconsistent dataset that hurts BC, whereas RL yields a more unimodal policy. That is a plausible hypothesis, but the table itself only shows outcome differences, not the mechanism. There is no analysis of action-distribution entropy, clustering of successful edits, or BC training instability to support that causal story. The paper should separate “what the ablation demonstrates” from “our conjecture about why.”

7. The real-world evaluation is strong in breadth but still thin in statistical depth. In **Table 3**, each object is tested for only five trials. That means several category-level percentages are based on rather small absolute counts, especially the categories with 10 or 12 objects. For a robotics demo paper this is acceptable, but for stronger claims about reliable sim-to-real generalization and robustness to hard object classes, confidence intervals or per-object distributions would help substantially. Right now, the real-world section is persuasive but somewhat presentation-heavy.

8. The paper claims the simple reward is a key advantage, but the actual setup is less simple than the prose suggests. The reward in **Equation (3)** is binary, yes, but the method also uses a mixed training regime where collision detection is disabled in half the environments, and collisions are assessed via hand-keypoint penetration rather than physical contact events. That is a reasonable engineering choice, but it is already a form of environment and objective design. I would recommend the authors tone down the contrast with prior “complex reward shaping” papers and describe this more precisely as minimalist task reward plus asymmetric collision handling.

9. The vision-based policy section is comparatively underdeveloped in the main paper, despite being critical for real deployment. Section 2.4 says the authors train a flow-matching policy on successful rollouts with action chunking, but key ingredients are not described in the main text: what exactly is the action chunk, how long is the prediction horizon, how are proprioception and vision fused, what loss is optimized, and why flow matching is preferable here over diffusion or standard BC? Since the real-robot success depends entirely on this second stage, the main paper gives it less space than it deserves.

10. There are several presentation issues and citation/reference sloppiness that reduce confidence. The references section contains formatting inconsistencies and duplicated-year oddities, and some entries are clearly malformed. More importantly, the main text occasionally overstates claims like “state-of-the-art” and “to our knowledge, the first” without the kind of careful qualification I would expect in a top-tier conference paper. This is not fatal, but it contributes to a recurring sense that the paper is stronger empirically than it is careful rhetorically.

## Questions
1. Please clarify the exact implementation of **Equation (2)** when
   \[
   q_{T_{\text{lift}}}^{*\text{hand}} - q_0^{*\text{hand}} = 0
   \]
   for some joints. Do you mask such joints, add an \(\epsilon\) in the denominator, or use another interpolation rule? This is central to the hand-editing mechanism.

2. Please rewrite **Equation (1)** more explicitly using standard rigid-transform notation. For the post-lift phase, is the intended operation something like
   \[
   p_{t}^{*\prime\text{ee-obj}} = T_z(\Delta z_t)\, p_{T_{\text{lift}}}^{*\prime\text{ee-obj}}
   \]
   with \(T_z(\Delta z_t)\in SE(3)\), or is the orientation frozen while only the position is changed? A precise definition would help.

3. For the comparisons in **Table 2**, can you provide more evidence that the training-distribution mismatch does not materially affect conclusions? Even a short discussion of object diversity, scale ranges, or matched subset results would increase confidence.

4. The “single demonstration” claim would be much stronger if you could characterize failure modes. What kinds of demonstrations lead to poor learning? For example, does a demonstration with awkward contact timing, excessive wrist rotation, or a highly object-specific approach still work?

5. In the real-world results in **Table 3**, can you report variance or confidence intervals, or alternatively per-object success histograms? Five trials per object gives only a coarse estimate, and more granular statistics would help assess robustness.

6. For **Table 5**, can you provide evidence for the proposed explanation that sampling causes multimodal supervision harmful to BC? For instance, showing variance in successful edit parameters or BC loss curves would make the argument much stronger.

7. The vision-based stage is crucial for deployment, but Section 2.4 is brief. What are the action chunk length, supervision target format, and training loss for the flow-matching policy? Why was flow matching preferred over simpler BC or diffusion-style action modeling?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics issues are apparent from the submission itself. The work is a robotics manipulation paper using simulation and real-robot experiments, and I did not identify human-subject, privacy, or sensitive-data concerns that require escalation based on the main paper.

## Soundness Rating
3: good. The core empirical claims are supported by substantial experiments, but there are important issues in mathematical specification, comparison fairness, and under-explained implementation details that prevent a higher score.

## Presentation Rating
3: good. The paper is generally clear and well organized, with useful figures and tables, but the exposition around the core equations and some of the benchmarking claims needs tightening.

## Contribution Rating
3: good. The demonstration-editing formulation is a meaningful contribution with practical significance for dexterous grasping, though I am less convinced by some of the stronger universality and simplicity claims than the paper suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a strong experimental package and a compelling central idea, and I can see clear value to the community. At the same time, the technical specification of the editing mechanism, the fairness of some comparisons, and the overstatement of several claims keep this from being an easy accept for me.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I am familiar with the dexterous grasping and robot learning literature, and I checked the main technical and experimental details carefully, but some implementation specifics are not fully available in the main paper.