Now I have a thorough understanding of the paper and all claims. Let me compose the final consolidated review.

---

## Summary

This paper proposes a dual-stream network for micro-expression recognition (MER). The main stream uses a Continuous Vertical Attention (CVA) block operating on the apex-onset difference to capture motion features, while the sub-stream uses a Swin Transformer-based Facial Position Focalizer (FPF) to encode spatial position from both frames separately. A 21-dimensional binary Action Unit (AU) vector is concatenated with the fused features before the classifier. The model is evaluated on CASME II and SAMM under leave-one-subject-out (LOSO) cross-validation, reporting 94.35% and 86.76% accuracy respectively.

## Strengths

- **Comprehensive ablation study isolating each component**: Table 2 decomposes the contribution of AU, CVA, and FPF individually against a ResNet-18 baseline. The full model surpasses the baseline by ~13.2% in accuracy and ~18.2% in F1 on both datasets, demonstrating that each block meaningfully contributes to the overall gain.

- **Swin Transformer-based FPF clearly outperforms ViT for position encoding**: Table 5 shows that replacing ViT with Swin Transformer in the position-estimation branch improves accuracy by over 2% and F1 by over 7% on SAMM, confirming the paper's claim about Swin's shifted-window mechanism being more effective for capturing spatial dependencies in MER.

- **Vertical attention design empirically validated over alternatives**: Table 3 shows that vertical-only attention outperforms both horizontal-only and bidirectional attention, providing empirical evidence supporting the paper's design choice. The continuous (recurrent) attention also shows consistent gains in Table 4.

- **AU embedding provides consistent improvements**: Table 7 shows that adding binary AU vectors improves both accuracy and F1-score across datasets, supporting the argument that AU information helps the model focus on active facial regions.

- **State-of-the-art results on standard benchmarks**: The model achieves 94.35% on CASME II (6% over MMNet, 10.87% over μ-BERT) and 86.76% on SAMM, with F1-scores also exceeding prior work.

## Weaknesses

### Fatal
None.

### Major

1. **Dimension mismatch in the fusion stage makes the architecture ambiguous**: The paper states that the CVA block yields $F_M$ with dimensions $512 \times 14 \times 14$ (line 69), while the Swin Transformer outputs $512 \times 196$ reshaped to $196 \times 14 \times 14$ (line 85). These two tensors have incompatible channel dimensions (512 vs. 196) for elementwise addition as described in §3.3 ("after adding $F_{POS}$ and $F_M$ together"). Although line 85 states that after downsampling "their channel dimensions match those of the $F_M$," the downstream dimensionalities given are inconsistent. This prevents an independent reader from knowing the actual tensor shapes in the fusion pipeline.

2. **No statistical reliability measures despite large claimed improvements on small datasets**: The paper reports very high accuracies (94.35% on 255-video CASME II, 86.76% on 159-video SAMM) under LOSO cross-validation. LOSO on 26–32 subjects typically produces high-variance estimates, yet the paper provides **no error bars, no standard deviations, no per-subject breakdowns, and no significance tests**. A single point estimate is insufficient to determine whether the 6–10% improvements over prior methods are systematic or due to a favorable split or random seed. This is the most significant methodological gap.

3. **AU-emotion correlation unanalyzed; dependency on AU annotations at test time undiscussed**: The ablation in Table 7 shows that adding AU embedding improves accuracy by substantial margins. Since Action Units are definitionally correlated with emotion categories, the model may be partially shortcutting by exploiting this correlation rather than learning from facial imagery. The paper never analyzes the AU-label correlation in either dataset, never checks whether a classifier trained on AU vectors alone achieves nontrivial accuracy, and never discusses the practical limitation that the method requires AU annotations during inference. While using AU features is a legitimate design choice, the magnitude of the gain warrants rigorous analysis that is absent.

4. **No direct comparison against standard coordinate attention (CA) as a baseline**: The CVA module is presented as a key contribution and is explicitly derived from coordinate attention (Figure 2). Yet the ablation (Table 3) only compares vertical-only vs. horizontal-only vs. bidirectional attention — not against the standard CA module itself (without vertical restriction or recurrence). Without this comparison, it is difficult to assess whether the design changes (vertical-only + recurrence + custom activation) collectively improve upon the off-the-shelf CA, or whether they merely shuffle performance among variants on these specific datasets.

### Minor

1. **Claim that vertical facial muscles are more important for MER is stated without support**: The paper asserts that "vertical facial muscle movement plays a more significant role in MER than horizontal movement" (line 55) but provides no anatomical citation, no prior literature reference, and no visualization of attention maps to substantiate this. The empirical results show vertical attention works better, but the claim as a principled motivation is ungrounded.

2. **Limited scope of SOTA comparison**: Table 1 includes only six methods, two of which (MMNet, μ-BERT) are from the last two years. For a paper claiming state-of-the-art results, a broader comparison including more recent approaches would strengthen the evaluation.

3. **Custom activation function $F_{act}(x)=x\cdot\text{ReLU}(x+3)/6$ is introduced without justification or analysis**: This non-standard activation appears in the CVA module but is not motivated, cited, or ablated. Given that the rest of the network uses standard ReLU and sigmoid, its role is unclear.

### Trivial

1. **Naming inconsistency**: "CAV block" and "CAV modules" appear on line 69, while the module is called "CVA" everywhere else in the paper. This suggests hasty editing.

2. **Model parameters and FLOPs not reported**, which would be useful for assessing practical utility.

## Nice-to-Haves

- A standard CA baseline (without vertical restriction or recurrence) in the attention ablation would isolate the benefit of each design choice.
- Per-class accuracy or confusion matrices would help assess how the model handles the imbalanced "others" class.
- Visualizing CVA attention maps on sample facial images would help validate the claim that the model focuses on relevant vertical muscle regions.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **FPF input inconsistency (Critic's Point 1a)**: The critic claimed the introduction contradicts §3.2 about whether FPF processes the difference frame or separate frames. In fact, the paper is consistent: the *introduction*'s mention of "the starting frame" is a simplification, while §3.2 clarifies that both frames are input *separately* to FPF and *added* (not subtracted). The critic conflated the CVA stream (which processes the apex-onset *difference*) with the FPF stream. The paper's overview on line 45 unambiguously separates the two streams. — *Removed as a misreading/strawman.*

- **Criticism about missing appendix, proofs, or references**: Removed per instructions (parser strips these; they exist in the original submission).

- **Criticism about "not yet released" or unverifiable models**: Removed per instructions (all cited models assumed to exist).

- **Generic formatting/style nitpicks**: Removed per instructions (parser artifacts, not author errors).

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension that the reviewers did not articulate: the paper's core strength — a well-structured ablation showing all three components contribute — is partially undercut by the fact that the component with the least novelty (AU embedding) may be driving most of the gain, and the component with the most novelty (CVA) lacks a direct comparison against its closest prior art (standard coordinate attention). Resolving this would require either (a) showing that CVA+FPF alone (without AU) already beats prior methods that do not use AU, or (b) demonstrating that the AU-aware model outperforms prior AU-aware models by a margin attributable to CVA/FPF.

## Suggestions

1. **Resolve the dimension inconsistency** by providing a clear tensor-flow diagram with exact channel, height, and width dimensions at each processing stage, including the fusion point.

2. **Report statistical variability**: At minimum, provide per-subject accuracy breakdowns or standard deviations over multiple LOSO runs with different random seeds.

3. **Analyze the AU contribution rigorously**: Compute AU-label correlation matrices for both datasets; report accuracy of a classifier trained on AU vectors alone; ablate AU while keeping CVA and FPF fixed to isolate their contributions; and explicitly discuss the dependency on AU annotations at test time as a limitation.

4. **Include a standard CA baseline** in the attention ablation (Table 3) to directly measure the improvement from the vertical-only and recurrent design choices.

5. **Expand the SOTA comparison** to include more recent methods, particularly those that also use AU information or Swin Transformer backbones.

6. **Either justify or remove the custom activation function** $F_{act}$, and fix the CVA/CAV naming inconsistency.

## Score and Decision

**Originality**: Moderate. The CVA module is a modest adaptation of coordinate attention (vertical restriction + recurrence), and the FPF module replaces ViT with Swin Transformer — incremental but sensible modifications.

**Quality of research**: The ablation study is thorough, but the evaluation is weakened by the absence of statistical reliability measures and the unanalyzed AU-emotion correlation.

**Clarity**: The architecture is broadly understandable but contains a concrete dimension inconsistency that prevents exact reproduction.

**Importance**: MER is practically important, and SOTA results on standard benchmarks are valuable.

**Value to community**: The ablations provide useful insights (e.g., vertical-only attention, Swin vs. ViT for position encoding), but the presentation and evaluation gaps limit immediate utility.

The paper has genuine contributions — a well-ablated architecture with strong empirical results — but the evaluation is hampered by three significant issues: an architectural ambiguity that prevents reproduction, a complete absence of statistical reliability measures for unusually large claimed improvements on tiny datasets, and an unanalyzed potential shortcut through AU embeddings. These are addressable but require substantial revision rather than a short rebuttal.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>