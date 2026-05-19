- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 8, 6
Now I have a thorough understanding of the paper and both reviews. Let me produce the consolidated review.

## Summary

This paper proposes the Shape-Memory Network (SMN), which combines (1) a conditional neuron mechanism that gates activations based on a linear combination of predicted per-class densities, and (2) a self-supervised test-time adaptation (TTA) loss that minimizes the structural similarity between an entropy-map derived from the segmentation pipeline and an entropy-map reconstructed from class activation maps (CAMs). The claimed contributions include emulating the brain's connectome via dynamic structural adaptation and explicitly incorporating contextual semantic information during inference. Evaluations are reported across six segmentation datasets (Inria, LoveDA, ADE20K, YouTube-VOS, BDD100K, GTA5).

## Strengths

1. **Mathematically formalized control neuron (Section 3.3, Theorem II)**: The paper provides a concrete mathematical specification for a control neuron whose output is a sigmoid-relaxed gating of inputs, controlled by a trainable threshold λₙ and driven by a linear combination of predicted class densities. Theorem II formulates the differentiable approximation that makes the threshold trainable via backpropagation, and this formulation is specific enough to constitute a definable architectural primitive.

2. **Entropy-map reconstruction via CAM integration (Section 3.2, Theorem I)**: The paper proposes a specific mechanism to reconstruct an entropy-map from stacked CAMs by normalizing the CAM values with softmax and computing pixel-wise entropy. Using this as a self-supervised TTA target via structural similarity (SSIM) loss is a concrete technical idea that differs from standard entropy-minimization approaches (e.g., TENT) because it derives the target distribution from density-based CAMs rather than from the segmentation output alone.

3. **Self-activation ablation provides some internal validation (Table 1, Ours-SA)**: The comparison of SMN with vs. without the self-activation path in control neurons (up to 7.51% IoU degradation when removed) provides controlled evidence that the self-activation mechanism meaningfully contributes to performance, supporting the design rationale that it prevents sparsity-induced information loss.

4. **Computational complexity is discussed with concrete metrics (Section 5)**: The paper reports 32.8 FPS, 47.5M parameters, and 549.8G FLOPs, and proposes specific optimization strategies (early stopping, pruning, quantization) with estimated 30–40% overhead reduction at 1–2% performance cost. This transparency about efficiency is valuable for assessing practical feasibility.

## Weaknesses

### Fatal
None. The core ideas are coherent enough that they could, with proper validation, constitute a contribution.

### Major

1. **No ablation isolating the paper's core claimed contributions.** The only ablation provided is Ours-SA (removing the self-activation path). This tests a secondary design choice (preventing sparsity), not the primary claims. There is no ablation that:
   - Removes the density-prediction branch (L₃ loss) while keeping everything else,
   - Removes the entropy-map consistency loss (L₂) while keeping everything else,
   - Disables the control signal mechanism entirely (i.e., runs the backbone without any density-driven gating),
   - Compares against standard multi-task learning with density prediction but without control neurons.

   Without these, it is impossible to attribute the reported performance to "explicit utilization of contextual semantic information" or "dynamic structural adaptation" rather than to multi-task regularization or better optimization. As the paper itself states, the experiment "did not aim to find the best-performing model with the fully searched parameters" — the admission that hyperparameters weren't even tuned further weakens any claim of superiority.

2. **Evaluation lacks statistical rigor and proper baselines.** The paper reports no standard deviations, no multiple-run statistics, and no per-class IoU breakdown for any dataset. The baseline set is problematic: it includes video object segmentation (VOS) models (Cheng & Schwing, 2022; Yang et al., 2022) which are not designed for general semantic segmentation, yet standard segmentation models (e.g., DeepLabv3+, PSPNet, SegFormer, Mask2Former) are absent. It is unclear which baselines are compared on which datasets and whether comparisons use the same backbones, training splits, and evaluation protocols. The paper does not describe the evaluation protocol (single/multi-scale inference, post-processing, etc.), making the reported numbers unverifiable.

3. **Method description is insufficiently specified for reproducibility.** Several critical architectural and procedural details are missing:
   - No backbone architecture is named (e.g., ResNet-50/101, ViT-B/L, MiT-Bx).
   - It is unclear where control neurons are inserted in the network (all layers? specific blocks? what density/spacing?), how many control neurons there are (N_cn), and whether they gate individual neurons, channels, or entire feature maps.
   - During TTA, the paper states that "θ'^M represents the parameters for the condition signals" is optimized — but what exactly are these parameters? The matrix v? The thresholds λₙ? All of the above? The TTA learning rate and stopping criterion are not given.
   - Training hyperparameters (learning rate, batch size, optimizer, schedule, number of epochs) are not reported.

### Minor

4. **Overclaimed framing relative to actual mechanism.** The paper claims to "faithfully emulat[e] the intricate mechanism of the brain's connectome" and "provide a foundational next-generation network," but the actual mechanism is a density-driven gating function with a TTA loss. The connectome and shape-memory analogies are metaphors without algorithmic correspondence. The "ensemble model" formalism in Section 2 is introduced but never realized — the SMN is a single network with TTA, not an ensemble of multiple models. This framing inflates expectations and obscures what the method actually does.

5. **No comparison to standard TTA baselines.** The paper explicitly frames its contribution in terms of test-time adaptation (Section 2: "we integrate the ensemble model with the TTA method"), yet no TTA-specific baselines (TENT, SHOT, or any self-supervised adaptation method) are included in the comparison. This makes it impossible to assess whether the proposed TTA mechanism is better than existing approaches.

### Trivial
None.

## Nice-to-Haves

- A derivation of the sigmoid approximation in Theorem II from the hard threshold in Definition VI would improve clarity, though the current description is already sufficient for understanding the approach.
- Per-class IoU breakdowns and failure-case analysis (e.g., what happens when density predictions are wrong) would strengthen the paper.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Contradiction about λₙ trainability" (from Harsh Critic)**: The reviewer claims the paper contradicts itself about whether λₙ is trainable. In fact, the paper describes a standard technique: the hard threshold in Definition VI is not differentiable, so it is approximated with sigmoids in Theorem II, making λₙ trainable. The text at lines 121–125 makes this logical flow clear. This is a correct resolution, not a contradiction.

- **"Figures are missing" (from Harsh Critic)**: Figures 4 and 5 are embedded as images in the PDF and are clearly referenced in the text. Their absence in the extracted text is a parser artifact, not a paper flaw.

- **"Evaluation protocol is not described" (from Harsh Critic — partially retained)**: This concern is partially valid but was framed too broadly. I have retained the specific, verifiable gaps (no backbone specification, no training hyperparameters) in the major weaknesses above.

- **Strength about "consistent and substantial quantitative gains" (from Strength Finder)**: This strength conflicts with the verified weaknesses about evaluation rigor (no standard deviations, no proper baselines). Per the merging rules, the weakness wins and this strength is removed. The reported numbers exist but are insufficiently validated to count as a confirmed strength.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any unexpected observations that reframe or deepen understanding of the paper beyond what the authors state.

## Suggestions

1. **Provide a complete ablation study**: Compare (a) baseline backbone without any SMN components, (b) backbone + density regression (multi-task, no control neurons), (c) backbone + control neurons but no L₂ TTA, (d) full SMN. This would causally isolate each claimed contribution.

2. **Report standard deviations across multiple runs** (at least 3) and per-class IoU for the key datasets. Include a comparison against standard semantic segmentation methods (DeepLabv3+, PSPNet, SegFormer) using the same backbone.

3. **Specify architectural details precisely**: state the backbone, where control neurons are placed, how many, what they gate, and all training/inference hyperparameters.

4. **Add TTA baselines** (e.g., TENT, SHOT, or simple entropy minimization) to contextualize the proposed self-supervised adaptation loss.

5. **Tone down the biological framing**: Replacing "connectome emulation" with "density-conditioned gating" would align the claims with the actual mechanism and avoid setting false expectations.
