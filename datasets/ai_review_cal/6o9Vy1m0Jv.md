- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3
Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

---

## Summary

This paper proposes VIRT (Vision Instructed Transformer for Robotic Manipulation), a Transformer-based policy with two main innovations: (1) **Robotic Imagery Pre-training (RIP)**, which pre-trains a policy using only first and last frame observations without requiring text task descriptions, and (2) **Robotic Gaze (RG)**, which uses a lightweight object detector to focus the policy's attention on the manipulated object region via cropping and enlargement. The paper argues that vision instructions are more suitable for robotic policies than text instructions. Experiments on three real-robot tasks (Pour Blueberries, Open the Lid, Clean the Table) and three simulated tasks show that VIRT substantially outperforms baselines including ACT and Diffusion Policy, and the ablation study demonstrates the individual contributions of RIP, RG, and the enlargement/uncertainty components.

## Strengths

1. **RIP pre-training meaningfully boosts performance on top of a strong baseline (Table 3)**: Adding RIP to a policy that already includes RG+enlarge raises Transport the Specified Box success from 0.47 to 0.64, Stack the Specified Boxes from 0.41 to 0.53, and Open the Lid from 0.39 to 0.45. This directly demonstrates that pre-training without text annotations improves downstream task performance.

2. **RG alone lifts performance from near-zero to non-trivial levels (Table 3)**: Adding only RG (no enlargement, no RIP, no uncertainty) to a baseline with 0.11/0.05/0.00 success rates on TS/SS/OL yields 0.32/0.24/0.26 respectively. This provides strong evidence that the gaze mechanism effectively resolves the ambiguity that prevents learning in these tasks.

3. **VIRT outperforms all compared policies by large margins across both real and simulated tasks (Tables 1, 2)**: On Open the Lid, VIRT achieves 0.71 success vs 0.01 for ACT. On Transport the Specified Box, 0.69 vs 0.12 for ACT. Results are from 100 trials each with both success rate and completion score reported.

4. **Introduction of the completion score metric (Section 4.2)**: The paper defines a completion score (i/k for completing i of k steps), which provides more informative evaluation than binary success/failure for multi-step tasks. This is a useful methodological contribution evidenced by its use throughout the experiments.

5. **Identifies and empirically demonstrates the failure mode of text-based instruction in ambiguous tasks (Table 2)**: ACT's success drops from 0.90 (Move a Single Box, no ambiguity) to 0.12 (Transport the Specified Box, five boxes with instruction), while VIRT retains 0.69. This supports the paper's motivating observation about text instruction struggling with ambiguity.

6. **Realistic teleoperation setup in simulation (Section 4.1)**: The paper builds a real-time hand pose acquisition system using Leap Motion rather than scripted rules, improving ecological validity of the simulated experiments.

## Weaknesses

### Fatal
None.

### Major

- **The paper's central claim—that vision instruction is superior to text instruction—is not directly tested.** The paper concludes that "vision observations are more suitable for serving as manipulation instructions than text descriptions," and this claim is threaded throughout the introduction and conclusion as a central finding. However, the experiments compare VIRT (a complete system with RIP, RG, and a Transformer architecture) to baselines that happen to use text (ACT with CLIP text encoder). These baselines differ in architecture, capacity, and training setup. A proper test would fix the policy architecture and vary only the instruction modality (vision vs. text). Without such a controlled comparison, the paper cannot claim to have demonstrated that vision instructions are superior to text instructions—only that the VIRT system as a whole outperforms other systems. This is a significant gap between the paper's stated conclusions and the evidence provided. The paper's technical contributions (RIP, RG) remain valuable regardless, but the framing needs adjustment and the claim needs to be either supported with a direct ablation or tempered.

### Minor

- **The RG strategy introduces an annotation burden that the paper's framing underplays.** The paper criticizes text instructions for requiring annotation and being difficult for policies to understand. However, RG requires (a) manual segmentation of trajectories into stages ("the trajectory is manually segmented into multiple stages," Section 3.1), and (b) a pre-trained object detector. While stage labels are arguably cheaper than full text descriptions, the paper consistently frames vision instructions as avoiding annotation entirely without acknowledging or quantifying the stage-labeling effort. This tension in framing weakens the paper's internal coherence.

- **Baseline tuning and implementation details are not reported.** No hyperparameter search is described for any baseline method (ACT, Diffusion Policy, ConvMLP). The paper analyzes why baselines struggle (e.g., Diffusion Policy's SpatialSoftmax compression), but without knowing whether these methods were tuned, the performance gap may partly reflect differing optimization effort rather than algorithmic superiority. The ablation study (Table 3) partially mitigates this by showing controlled comparisons between VIRT variants and a shared baseline, but the main comparison (Tables 1, 2) remains vulnerable to this concern.

- **The role of the learned uncertainty values during inference is not clarified.** Equation 1 describes a Laplacian uncertainty-weighted training loss, and the ablation shows that including the "uncern" component improves performance (Table 3, last row vs. second-to-last row). However, the paper does not state whether the learned σ values are used during inference (e.g., to weight or filter action predictions) or whether they only serve as an adaptive training-weighting mechanism. While the latter interpretation is standard for this loss formulation, a brief clarification would improve reproducibility.

### Trivial
None.

## Nice-to-Haves

- **Qualitative analysis of RIP pre-trained predictions**: Showing examples of what intermediate actions the policy "imagines" when given only first and last frames would increase trust in the imagery mechanism and help distinguish meaningful intermediate prediction from collapsed/coarse motion.
- **Stage segmentation statistics**: Reporting the number of stages per task, inter-annotator consistency (if multiple annotators), and accuracy of the learned status prediction logit would improve understanding of RG's practical requirements.
- **Parameter count comparison**: Reporting model sizes for VIRT vs. baselines would help disentangle whether performance gains come from architectural capacity vs. the proposed techniques.
- **Action chunk size for VIRT**: The paper reports n=10 for ConvMLP but does not state what n is used for VIRT. Since action chunking affects performance, this should be specified.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Boost from nearly 0% to more than 65%" framing nitpick**: The critic claimed this phrasing was imprecise. Checking the paper: baseline in Table 3 row 1 has 0.00 on OL, VIRT has 0.71. "Nearly 0%" to "more than 65%" is factually accurate. **Removed** (factually wrong criticism).

- **Diffusion Policy performance "far below reported literature"**: The critic asserted this without evidence that the paper's specific tasks, setup, and data regime are comparable to those in prior literature. The paper provides a reasoned explanation (SpatialSoftmax compression). **Removed** (speculative, not anchored in the paper).

- **RIP being "conceptually challenging" and lacking qualitative analysis**: The critic claimed RIP is a "very high-degree-of-freedom prediction problem" and the paper does not analyze whether the policy "learns meaningful imagery." The entire experiment section is the analysis—RIP improves downstream task performance. Requesting additional qualitative analysis is a nice-to-have, not a weakness. **Removed** (not a genuine flaw; the empirical evidence validates the approach).

- **Missing discussion of goal-conditioned policies in related work**: The paper explicitly discusses goal images in game-based RL and navigation (Section 2.3, line 55). While a deeper comparison with manipulation-specific goal-conditioned methods could strengthen positioning, its absence is not a flaw—the paper's scope vis-à-vis this literature is a matter of emphasis, not omission. **Removed** (scope creep).

- **Number of demonstrations being "on the lower end"**: 100 real-robot demos and 50-100 simulated demos is standard for imitation learning in manipulation. **Removed** (generic criticism not grounded in any standard the paper violates).

- **Inference speed comparison as "overstated"**: VIRT runs at 39.22 Hz and ACT at 43.48 Hz. Calling 39.22 Hz "rapid" is accurate—real-time manipulation typically requires ~30 Hz. **Removed** (nitpick).

- **Uncertainty loss inference criticism**: The reviewer asked "how learned uncertainties σ are used during inference." The standard interpretation is that the loss acts as an adaptive training-weighting mechanism (larger σ → smaller penalty for prediction error), allowing the model to focus on more deterministic action segments during training. The ablation proves its empirical value. The paper could be clearer, but this is at most a minor missing clarification (already noted above). **Demoted** from the critic's framing to a minor point above.

- **Criticism about stage labels not being automatically derived**: The critic asked "whether automatic segmentation was attempted." Requiring the authors to explore alternative (and likely inferior) labeling methods is outside the scope of evaluation. **Removed**.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the paper not already present in the paper itself.

## Suggestions

1. **Directly test vision vs. text within the same architecture.** Modify VIRT to accept text-encoded instructions (e.g., via CLIP features) and compare against the current vision-instruction version, keeping all other factors fixed. This would directly support the paper's central claim.

2. **Acknowledge and quantify the annotation overhead of RG** (number of stages, how they are defined, approximate labeling effort per trajectory). This would address the tension between the paper's critique of text annotation and RG's own annotation requirements.

3. **Report hyperparameter search details for baselines.** At minimum state the search ranges and best configurations found. If no search was performed, acknowledge this limitation.

4. **Clarify whether σ values are used during inference.** A single sentence stating whether σ influences action selection at test time (and if so, how) would resolve ambiguity.
