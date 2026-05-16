Now I have thoroughly read the paper and verified all claims against the source. Let me produce the final consolidated review.

## Summary

This paper proposes VIRT, a Transformer-based robotic manipulation policy that replaces conventional text instructions with vision instructions. It introduces two cognitive-science-inspired techniques: (1) Robotic Imagery Pre-training (RIP), which trains the policy to predict full trajectories from only first and last frame observations, enabling large-scale pre-training without text annotations; and (2) Robotic Gaze (RG), which crops and enlarges the target object region using a lightweight detector guided by predicted manipulation stages. Experiments on three real-robot and three simulated tasks show VIRT substantially outperforming ACT, Diffusion Policy, and ConvMLP.

## Strengths

- **Novel and well-motivated vision-instruction paradigm.** The paper makes a compelling conceptual argument — grounded in the observation that policy backbones (e.g., DINOv2) are pre-trained on image data, not text — that vision instructions are more comprehensible to robotic policies than text. This cognitive-science framing (infant vision, motor imagery, gaze anchoring) gives the work a clear intellectual identity and is explicitly stated in Sections 1 and 3.

- **RIP enables pre-training without task annotations.** The RIP paradigm (Section 3.3) uses only first and last frame observations to predict full trajectories, eliminating the need for text descriptions. This is a practical contribution that allows pre-training on diverse datasets like DROID (76k trajectories), many of which lack task labels. The ablation (Table 3) shows that adding RIP improves success on Transport the Specified Box from 0.47→0.64 and Open the Lid from 0.39→0.45.

- **Empirically strong system-level results.** VIRT achieves 71% success on opening a tightly sealed bottle (vs. ACT's 1%), 42% on pouring blueberries (vs. 0% for all baselines), and 37% on Clean the Table (vs. 0%). These are genuinely difficult bimanual and multi-object tasks, and the margin of improvement is striking. On simulated tasks, VIRT achieves 0.69 vs. ACT's 0.12 on Transport the Specified Box, where instruction following is required.

- **RG with efficient region enlarging addresses a real architectural challenge.** The paper correctly identifies that Transformer resolution is limited by quadratic attention cost and proposes cropping only the relevant object region (Section 3.4). The ablation confirms that adding "enlarge" to RG improves Transport from 0.32→0.47 and Stack from 0.24→0.41 (Table 3).

- **Laplacian uncertainty prediction is a principled enhancement.** The loss function (Eq. 1) adaptively weights action prediction errors by per-timestep uncertainty, which concentrates training on more deterministic action segments. The full model with uncertainty improves Open the Lid success from 0.45→0.71 (Table 3).

## Weaknesses

### Fatal

None.

### Major

1. **The core thesis ("vision > text instructions") is confounded with architecture, pre-training, and supervision — not directly tested.** The paper's central claim (stated in the abstract and conclusion) is that vision instructions are more suitable than text. Yet the main experiments (Tables 1–2) compare VIRT (vision instructions + RG + Transformer + RIP pre-training + stage labels) against baselines that differ in architecture (CNN for ACT/ConvMLP, CNN+diffusion for Diffusion Policy), pre-training, and supervision. **No experiment holds the policy architecture fixed while varying only the instruction modality** (e.g., VIRT's Transformer taking text via CLIP vs. visual instructions via RG). Without this control, the performance gap could arise from any combination of: Transformer vs. CNN backbone, RIP pre-training, stage labels, object-detection-based cropping, or the Laplacian uncertainty loss — none of which are about instruction modality per se. The conclusion "we have demonstrated vision observations are more suitable" (Section 5) overstates what the evidence supports.

2. **Asymmetric stage supervision: baselines do not receive VIRT's stage labels, creating a confound.** VIRT's policy predicts a one-hot status vector $s$ indicating the manipulation stage, and the trajectory is "manually segmented into multiple stages" (Section 3.2, line 85). This provides explicit sub-task supervision (e.g., "now you are in stage 1: grasp the blue plate"). The baselines (ACT, Diffusion Policy, ConvMLP) are not described as receiving equivalent stage labels — they receive only the text instruction via CLIP (Section 4.2, line 205). The paper does not discuss whether providing similar stage decomposition to baselines would shrink the performance gap, nor does it analyze how much of VIRT's advantage comes from this additional per-timestep supervisory signal. This is a critical omission because the resulting performance differences (0% vs. 71% on Open the Lid) could partially reflect a supervision-level mismatch rather than a modality advantage.

3. **Clean the Table task with random test-time ordering: mechanism is unexplained.** The Clean the Table task (Section 4.2, line 158) requires the robot to move plates to a cabinet "in a color order that is randomly specified during test." The paper explains that for baselines, the text instruction encoding the order is provided via CLIP. For VIRT, which relies on learned stage labels and the detector to determine which object to focus on, it is unclear how the random order is communicated at test time. If stages are fixed per demonstration, the policy would need to handle novel orderings at test time — but this generalization capability is not discussed. If stages dynamically adapt to the order, the mechanism for doing so is not described. This is a significant gap in the experimental explanation.

### Minor

1. **The ablation study does not isolate the effect of instruction modality.** The ablation (Table 3) adds components cumulatively (RG → enlarge → RIP → uncertainty), but never tests VIRT with text instructions instead of RG, nor tests a version of RG that simply overlays a bounding box without crop/enlarge. The contribution of "vision instruction" as a concept is conflated with the specific mechanism of cropping+enlarging the object region. The paper would benefit from a row that replaces RG with a text-conditioned variant of VIRT (same Transformer architecture, same RIP pre-training, same stage loss) to directly assess the modality claim.

2. **Missing failure analysis.** On Open the Lid, VIRT achieves 71% success — meaning 29% of trials fail. The paper does not analyze failure modes (detection errors? stage misclassification? manipulation precision?). Such analysis would strengthen the claim that improvements come from the proposed mechanisms and would help identify which component is the bottleneck.

3. **No discussion of the annotation cost of manual stage segmentation.** The paper states trajectories are "manually segmented into multiple stages" (line 85) but does not report how much additional human effort this requires, whether it scales, or whether it could be automated. Since baselines do not receive this signal, the practical overhead of this supervision should be acknowledged.

4. **RIP pre-training analysis is shallow.** The ablation shows RIP provides improvements (e.g., 0.47→0.64 on Transport), but the paper does not analyze what RIP actually learns — e.g., does the gain come from learning general visual features, or from learning task-specific action priors that happen to transfer? Given that the DROID dataset is diverse (76k trajectories), understanding the source of improvement would strengthen the contribution.

### Trivial

- The paper says RIP "eliminates the need for task descriptions" (Section 3.3) — this is accurate in the sense of text annotations. The critic's semantic point that first/last frames "implicitly encode the task" is correct but does not diminish the practical value of avoiding text labeling.

## Nice-to-Haves

- A controlled experiment holding VIRT's architecture fixed while varying only whether the instruction modality is text (via CLIP) vs. vision (via RG) would directly test the paper's central thesis and significantly strengthen the contribution.
- A "gaze-only" baseline (same stage supervision, same detector, but overlay a bounding box without crop/enlarge) would isolate the benefit of increased object resolution from the benefit of vision instruction itself.
- A discussion of how the Clean the Table random order is mapped to VIRT's stage mechanism, including whether stages are learned per-object and can generalize to arbitrary orderings at test time.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The motivation paragraph is presented as fact without citation"** — This is a framing preference, not a technical weakness. The paper provides citations (colombo2009infant, radford2021learning, etc.) for its claims. Removed as a non-substantive style critique.

2. **"RIP first/last frames implicitly encode the task" as a criticism of the paper's wording** — The paper says "eliminates the need for task descriptions" which is accurate (it eliminates text descriptions). The critic's observation that the frames contain task information is a semantic nuance, not a methodological flaw. Removed as a trivial word-level quibble.

3. **"The claim of 'unexplored' is too strong" regarding visual instructions** — The paper explicitly qualifies this to "task-unspecified pre-training and task-specified training of robotic manipulation" (line 55) and acknowledges prior work in navigation and game-based RL. The critic's cited works (Lynch et al., goal-conditioned IL) are in a different sub-problem setting. Removed as the paper's claim is appropriately scoped.

4. **Criticisms from the human finder for other papers** — These were from different papers and are not relevant here. Removed entirely.

5. **"The paper should also cover Y / domain Z / additional tasks"** — The critic's suggestions about broader comparisons are scope-creep demands that would turn this into a different paper rather than strengthening the one written.

## Novel Insights

None beyond the paper's own contributions. The harsh critic raises valid methodological concerns about experimental design but does not introduce any novel positive insight not already present in the paper's framing.

## Suggestions

1. **Add a controlled modality experiment.** Take VIRT's Transformer architecture (with RIP pre-training and stage loss, but remove RG) and feed it text instructions via a compatible text encoder (e.g., CLIP tokens fused into the Transformer). Compare this against VIRT-with-RG. This directly tests whether the modality (vision vs. text) is the driver of improvement, controlling for architecture and pre-training.

2. **Address the stage supervision confound.** Either: (a) provide equivalent stage decomposition to baselines and re-run experiments, or (b) explicitly acknowledge this as a known asymmetry and discuss how much of the performance gap it could explain. Even a single ablation that removes stage labels from VIRT would be informative.

3. **Explain the Clean the Table mechanism.** Describe how VIRT handles randomly specified color orders at test time — specifically how the stage mechanism adapts to unseen orderings and whether the detector is used to identify which plate corresponds to the next step in the random sequence.

4. **Add failure analysis.** For the 29% failed Open the Lid trials and other tasks, categorize failure modes (e.g., detection failure vs. grasp failure vs. stage misclassification). This would strengthen the claim that improvements come from the proposed mechanisms.

## Score and Decision

The paper presents a well-motivated system with genuinely novel components (RIP, RG) and impressive empirical results on challenging tasks. However, its central claim that "vision instructions are more suitable than text" is not properly isolated from confounding factors (architecture differences, asymmetric stage supervision, RIP pre-training). The most critical issue is the asymmetric stage supervision — baselines do not receive VIRT's per-timestep stage labels, which could explain a substantial portion of the performance gap. Additionally, the mechanism for the Clean the Table task (randomized test-time orders with VIRT's fixed-stage architecture) is not explained. These are fixable issues, but in its current form the experimental design does not support the paper's headline conclusion. The technical contributions are real and the method is effective, but the overclaiming combined with uncontrolled confounds prevents acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>