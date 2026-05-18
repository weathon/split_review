Now I have all the information needed. Let me compile the final consolidated review.

## Summary

This paper proposes GravMAD, a sub-goal-driven action diffusion framework for 3D robotic manipulation that bridges imitation learning and foundation models. During training, it discovers sub-goal keyposes from demonstrations; during inference, VLMs predict sub-goals. These sub-goals are converted into grounded spatial value maps (GravMaps) that guide a diffusion policy for end-effector pose prediction. Evaluated on RLBench, GravMAD shows strong generalization to novel tasks (28.63% absolute gain over VoxPoser in the VLM setting) while remaining competitive on training tasks.

## Strengths

- **Novel sub-goal bridging mechanism**: The paper introduces a principled approach to connect foundation models with imitation learning through sub-goal keypose discovery (training) and VLM-based sub-goal prediction (inference), clearly described in Sections 3.2 and Figure 2. This addresses a real gap between the two paradigms.

- **Strong empirical generalization on novel tasks**: GravMAD (VLM) achieves 62.92% average success on 8 novel RLBench tasks vs. VoxPoser's 34.29% (+28.63% absolute) and outperforms all baselines on every individual novel task (Table 1). This is the paper's most compelling result and is obtained using a realistic VLM-based setting, not the oracle Manual setup.

- **GravMaps provide meaningful spatial guidance beyond fixed coordinates**: The genuine ablations in Figure 5 show that replacing GravMaps with raw sub-goal positions causes a significant performance drop, confirming the value-based representation's robustness to positional inaccuracies. The ablation of cost map vs. gripper map further demonstrates the design's internal consistency.

- **Controlled evaluation with two informative settings**: By reporting both Manual (oracle object positions) and VLM (realistic detection) settings, the paper provides a clear upper bound on performance and an honest assessment of current VLM limitations, allowing readers to separate the core GravMap mechanism from detection quality issues.

- **Comprehensive genuine component ablations**: Figure 5 systematically ablates GravMap removal, cost/gripper map decomposition, contrastive loss, auxiliary losses, guided rotation, and point cloud encoders, providing evidence for the method's key design choices.

## Weaknesses

### Major

- **Ablation tables (Tables 3 and 4) contain structurally inconsistent data.** The column headers (*Multi-Stage, Parameter Rational., Loc. Cond. Rot, Point Render, Convex Upsamp., Mixed Prec., 8-bit Opt. + Fast Attn., # of Views*) do not correspond to any component described in the GravMAD method section (Section 3). The reported success rates (81.4–82.0%) are substantially higher than any GravMAD result in the main tables (max 69.17% for Manual on base tasks). The table also appears twice with identical content and the same label (Table 3 and Table 4). While the caption describes these as "architectural and system-level improvements in GravMAD," the lack of correspondence between the ablated factors and anything in the method section makes it impossible to assess what these tables actually measure or how they relate to GravMAD's claims. The paper does provide genuine component ablations in Figure 5, which mitigates the overall concern, but the presence of these unexplained tables undermines experimental rigor and presentation quality.

- **The headline claims disproportionately emphasize the oracle Manual setting without qualification.** The abstract and contributions section state "a 13.36% gain on tasks encountered during training" without clarifying that this refers to GravMAD (Manual), which uses human-provided ground-truth 3D object coordinates. The realistic VLM setting achieves only 0.91% over the 3D Diffuser Actor baseline on the same 12 base tasks and underperforms the baseline on 5 of 12 individual tasks (Open Drawer: -29.33, Put in Drawer: -33.34, Place Wine: -49.34, Meat off Grill: -17.33, Slide Block: -4.00 in Table 2). The body text (line 384) correctly attributes the 13.36% to the Manual setting, but the abstract and contribution bullets do not, creating a misleading first impression of the method's practical performance on training tasks.

- **Sub-goal keypose discovery is underspecified for a claimed contribution.** The paper presents this as contribution item 1, but the discovery constraints are described only qualitatively: grasping tasks require "a change in the gripper's open/close state and a significant change in touch force"; contact-based tasks require "significant changes in touch force" alone (lines 97–98). No quantitative thresholds, learned criteria, or algorithmic procedure for determining "significant change" are provided. Since RLBench is a simulation environment, the simulation-specific force thresholds or detection procedure should be specifiable. This opacity makes the contribution difficult to reproduce or assess.

### Minor

- **Rotation denoising does not use GravMap tokens, and the design rationale is undiscussed.** Equation (1) shows that position denoising conditions on the GravMap token $t_m$, while rotation denoising does not. The ablation in Figure 5 ("w. Guided Rot.") confirms that adding GravMap conditioning to rotation actually hurts performance. The paper reports this as an empirical finding but does not analyze *why* value-map-based spatial guidance is beneficial for translation but detrimental for rotation, or whether this is a fundamental limitation of the value-map representation for orientation.

- **Contrastive loss is introduced but its mechanism is not analyzed.** The paper applies a contrastive loss (Eq. 4) to enhance GravMap feature representations and ablate it in Figure 5, but provides no analysis of what the loss actually accomplishes — e.g., whether it improves feature separability across different sub-goals, whether it affects different task types differently, or what the learned feature space looks like. The ablation shows it helps, but the mechanism is opaque.

- **VLM pipeline computational cost is not reported.** Running Semantic-SAM + GPT-4o for each inference step adds significant latency and API cost. The paper does not quantify this, making it difficult for practitioners to assess the method's practicality.

- **Baseline set is adequate but narrow.** The paper compares against Act3D, 3D Diffuser Actor, and VoxPoser. Several recent RLBench baselines (e.g., Perceiver-Actor, RVT/RVT-2) are absent. Given that GravMAD builds on the 3D Diffuser Actor architecture, including one additional independent baseline would strengthen the comparison.

### Trivial

- Tables 3 and 4 are exact duplicates with the same label (a paper preparation or parser artifact). The caption misattributes the table's content as improvements in GravMAD when the column headers are not described in the method.

## Nice-to-Haves

- An analysis of per-task sub-goal prediction quality (e.g., what fraction of VLM-predicted sub-goals fall within a tolerance of the ground-truth sub-goal from training demonstrations) would help separate detection errors from action diffusion errors.
- A discussion of whether rotation guidance from value maps is inherently limited, or whether an alternative spatial representation could be designed for orientation.
- Reporting GravMAD (VLM) results on novel tasks with the same per-task detail as in the novel-task table would strengthen the comparison — the 28.63% gain is already present in Table 1, but additional analysis of where VLM sub-goal errors occur would be informative.

## Removed Points

- **Criticism about "Open Drawer" appearing as both a base and novel task**: Removed because the novel task is "Open Drawer Small" (Table 1) while the base task is "Open Drawer" (Table 2) — they are distinct tasks. The critic misread the task name.
- **Criticism about missing related works**: Removed per instructions — I cannot verify the existence of unmentioned works from my knowledge alone.
- **Criticism about typo in contrastive loss denominator**: The reviewer noted a potential issue, but upon inspection, Eq. (4) uses a standard InfoNCE formulation. The "typo" is the reviewer's misreading — the denominator summing over $N$ samples is standard for the numerator's positive-pair term, and the overall formulation is correct. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface clarity and framing issues rather than uncovering unexpected insights about the method's behavior.

## Suggestions

1. **Replace or clearly explain Tables 3 and 4.** If these tables ablate engineering optimizations (mixed precision, 8-bit optimizer, etc.) that are orthogonal to the GravMAD method but part of the training pipeline, say so explicitly in the caption and text. Better yet, move them to an appendix. If they are from a different system, remove them entirely. The duplicate must be fixed, and the caption must accurately describe what is being ablated.

2. **Qualify the 13.36% claim in the abstract and contributions.** Replace the unqualified "a 13.36% gain on tasks encountered during training" with "a 13.36% gain in an oracle setting with ground-truth object coordinates (GravMAD-Manual), and a 0.91% gain in a realistic VLM-based setting (GravMAD-VLM)." The body already does this; the abstract should match.

3. **Provide precise, reproducible criteria for sub-goal keypose discovery.** Specify the threshold for "significant change in touch force" as used in the RLBench simulation, or describe a learned/adaptive procedure. Even a heuristic threshold makes the method reproducible; keeping it qualitative does not.

4. **Add a brief analysis of why rotation does not benefit from GravMap conditioning** and whether this is a fundamental limitation or a representation-design choice.

## Score and Decision

The paper's core idea — bridging foundation models and imitation learning via sub-goal-derived spatial value maps — is sound and produces impressive generalization on novel tasks. The genuine ablations (Figure 5) are informative, and the main experimental results (Tables 1 and 2) appear valid. However, the presentation is compromised by the unexplained/duplicate ablation tables that do not correspond to any described component and report inconsistent success rates, and the abstract's unqualified 13.36% claim overstates the VLM-based method's practical performance on base tasks. These issues are addressable in revision but are significant enough in a submission that they undermine confidence in experimental rigor. A clean revision that replaces the spurious tables, qualifies the claims, and specifies the sub-goal discovery criteria would be publishable, but the current submission does not meet the bar.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>