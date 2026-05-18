I have thoroughly verified the paper text against every reviewer claim. Now I will produce the final consolidated review.

## Summary

This paper proposes Channel-Wise Parameter Sharing (CWPS), a method for knowledge transfer that shares parameters at the channel/neuron level rather than at the layer or individual-weight level. For each new task, a Composite Parent Model Search (CPMS) finds the most similar pre-trained channel for each child channel, and a learnable mask controls which channels are shared vs. task-specific. The method is evaluated on ImageNet-to-Sketch (incremental learning) and DomainNet (multi-task learning) benchmarks with ResNet-18, ResNet-50, and DenseNet-121 backbones, achieving competitive precision-to-parameter ratios.

## Strengths

- **State-of-the-art precision-to-parameter ratio**: Table 1 shows CWPS achieving a mean Top-1 accuracy of 83.51 with only 1.20× backbone parameters on the ImageNet-to-Sketch benchmark, outperforming parameter-efficient methods like TAPS (80.64, 1.50×) and PackNet (81.01, 1.60×) in both accuracy and parameter count. This directly supports the central claim that channel-level granularity yields a better balance than coarser approaches.

- **Interpretable task-relationship visualization**: Figure 4 (right) quantifies shared neurons between task pairs, producing interpretable relationship strengths (e.g., Sketch↔Flowers is stronger than Cars↔Flowers, and ImageNet has the strongest connections to all tasks). This aligns with domain intuition and demonstrates that the per-channel similarity matching (Eq. 3–5) captures semantically meaningful structure without heuristic assumptions.

- **Broad architectural and task-setting generality**: The method is validated across ResNet-18, ResNet-50, and DenseNet-121 in both incremental learning (Table 1) and multi-task learning (Table 2, Algorithm 1), showing composability across backbones and extension from MDL to MTL.

- **Ablation on λ provides practical guidance**: Table 3 and Figure 5 explore the λ trade-off, showing that values between 0.3 and 0.7 give a good balance while extremes cause overfitting or parameter waste. (Note: this strength is weakened by the fact that λ is never formally defined — see Weaknesses.)

## Weaknesses

### Fatal
None.

### Major

- **The mask learning procedure is fundamentally underspecified.** The paper introduces a channel mask $mask_{t,i}$ as the core mechanism controlling which channels are shared and which are task-specific (Section 3.2.3), and mentions "soft mask training stage" and "hard mask training stage" (line 155). However, it never defines:
  - How the mask values are parameterized (continuous via sigmoid? binary?).
  - The loss function or training objective for the mask itself.
  - Any regularization term (e.g., L1 sparsity) that would drive the mask toward 0/1 values.
  - How the transition from soft to hard occurs (thresholding? Gumbel softmax? annealed temperature?).
  - The training schedule for the two stages (how many epochs per stage?).
  
  The paper merely states it is "Motivated by the mask generation method of Yan et al. (2021)" (line 135) without explaining how that method is adapted to this setting. Since the mask is the central mechanism that determines parameter sharing, a reader cannot reproduce the method or understand its training dynamics from the current description.

- **λ is ablated (Table 3, Figure 5) but never defined anywhere in the paper.** λ is treated as a key hyperparameter controlling the trade-off between parameter reduction and performance, with detailed discussion of its effect across values from 0 to 1. Yet the paper provides no definition of what λ represents — is it a sparsity regularization weight? A mask loss coefficient? A threshold? This makes the ablation study uninterpretable as presented.

### Minor

- **Per-task storage cost is not precisely defined.** The paper reports "Avg. Params per task" (Tables 1, 2) as a proportion of backbone parameters, and claims that after inference, "we can integrate the child parameters into a single set of weights through Eq. (6, 7) to get faster inference performance and fewer parameters" (line 155). However, it never explicitly states: which parameters are stored per task after training? Are child weights for non-shared (mask=0) channels discarded, or retained but unused? How is the mask stored? Without this definition, the comparison to baselines like PackNet and Piggyback is ambiguous — the paper counts their mask parameters as full-sized (1.0×) but does not provide a comparable breakdown for CWPS.

- **Missing training hyperparameters.** No learning rate, batch size, optimizer, weight decay, scheduler, or training epochs are reported in the main text. This is a basic reproducibility requirement.

- **No variance reporting.** Standard deviations or number of independent runs are absent from all tables, making it impossible to assess the statistical reliability of the reported improvements.

- **CPMS search cost and implementation details are insufficiently characterized.** The paper states the warm-up takes "one-quarter of the total training epochs" (line 108), but provides no analysis of: (a) how many similarity computations are performed per task, (b) how the cost scales with the number of prior tasks, (c) how kernels of different shapes (especially convolutional kernels with spatial dimensions) are compared for similarity — are they flattened? aligned by input channel? and (d) how the search handles layers that do not exist in prior models. These details are needed to substantiate the claim that the search "minimizes computational costs."

- **No ablation isolating granularity.** The paper claims that weight-wise methods "neglect the atomic nature of the neuron" (line 21), but provides no controlled experiment that isolates the effect of sharing granularity (channel vs. weight vs. layer) while holding all other factors fixed. Such an ablation would substantially strengthen the paper's core argument.

### Trivial

- **The bias mask formulation (Eq. 5) is notationally unclear.** Equation 7 applies the mask to bias as $mask_{t,i} \cdot b_{t,i} + (1-mask_{t,i}) \cdot b'_{t,i}$, but $mask_{t,i}$ is described as being of size $C_i$ (output channels), while bias is typically per-output-channel as well. The text does not clarify this dimension alignment.

- **Section 5 comparisons with MoE, model merging, and prompt methods are qualitative and lack empirical grounding.** While this is a discussion section (not an experimental one), several claims about relative advantages could be misleading without quantitative backing.

## Nice-to-Haves

- An algorithm pseudo-code block covering the warm-up, CPMS search, mask training, and soft-to-hard conversion would resolve most specification issues.
- A per-task storage breakdown (mask size, child weight entries for non-shared channels, total parameter count formula) would make the efficiency claim testable.
- Reporting a single run with standard deviation across 3–5 seeds would improve confidence in the results.
- A controlled ablation comparing channel-wise, weight-wise, and layer-wise sharing granularity under otherwise identical conditions would directly validate the paper's central thesis.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The related work section conflates MDL, MTL, and incremental learning without clear delineation."** — The paper explicitly distinguishes these in Section 2.3 ("MDL is MTL in very restricted situations") and clarifies how the method addresses each setting. The reviewer appears to have overlooked this section.

2. **"The treatment of batch normalization layers is unspecified."** — Line 87 directly states: "some layers, such as Batchnorm2d... Thus, we do not need to exchange their parameters among tasks." The paper does address this.

3. **"The paper should include a direct comparison with Piggyback or PackNet in terms of per-task storage."** — This is a reasonable suggestion but framed as a missing comparison when the paper already includes these methods in Table 1. The request is for a different format of comparison, not a missing baseline.

4. **Criticisms about missing appendix content, formatting/style nitpicks, and the "not yet released" concerns.** — These are either parser artifacts (the original submission contains the appendix/figures) or not applicable (all cited references and benchmarks exist).

## Novel Insights

The reviews surface an interesting tension: the paper's core conceptual contribution (channel-level sharing via similarity-guided parent selection) is clear and well-motivated, but its implementation-level contribution (the mask training mechanism that actually realizes the sharing) is opaque. This suggests the paper would benefit from a structural reframing — either present the mask training as a straightforward application of Yan et al. (2021) with explicit adaptation details, or elevate it to a separately described contribution. The current middle ground leaves readers unsure which parts are novel and which are inherited from prior work.

## Suggestions

1. **Specify the mask training procedure completely**: define the mask parameterization, training loss, regularization terms (especially any sparsity objective), and the exact soft-to-hard conversion mechanism (threshold, Gumbel, annealing schedule). This is the single most impactful fix.

2. **Define λ in the text** — state what it controls (mask regularization weight? loss coefficient?), ideally before or alongside the ablation study.

3. **State per-task storage cost explicitly**: after hard mask conversion, what exactly is stored per task? How many floats for the mask, how many for child weights, and how does this sum produce the reported parameter ratios?

4. **Report basic training hyperparameters** (learning rate, batch size, optimizer, epochs, scheduler) either in the main text or a clear table.

5. **Add a granularity-controlled ablation** that varies only the sharing unit (channel vs. weight vs. layer) under otherwise identical settings to directly support the "atomic neuron" claim.

## Score and Decision

The paper introduces a well-motivated idea (channel-wise parameter sharing) and shows competitive empirical results on standard benchmarks. However, the core mechanism — the mask learning procedure — is critically underspecified, and a key hyperparameter (λ) that is the subject of an ablation study is never defined. These are not minor presentation issues; they prevent a reader from understanding, reproducing, or building upon the method. The paper has a clear conceptual contribution but requires major revision in its specification and reproducibility before it can be accepted.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>