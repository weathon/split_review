Now I have all the information needed. Let me produce the consolidated review.

## Summary

The paper introduces LieRE (Lie group Relative position Encodings), which generalizes Rotary Position Encodings (RoPE) to n-dimensional inputs by replacing RoPE's block-diagonal 2×2 rotation matrices with dense, high-dimensional rotation matrices generated from learned skew-symmetric basis matrices. The core technical claim is that relaxing the commutative constraint of RoPE (via denser rotations) yields better positional encoding for higher-dimensional data. The paper evaluates LieRE on 2D (CIFAR-100, ImageNet-1k) and 3D (UCF101) image/video classification, reporting relative accuracy improvements and data/compute efficiency gains.

## Strengths

1. **Principled theoretical extension of RoPE to n-dimensions.** The paper clearly identifies that RoPE-Mixed's block-diagonal 2×2 rotations form a commutative Lie group (Equation 2), and LieRE relaxes commutativity by learning a dense skew-symmetric basis using the matrix exponential. This provides a mathematically grounded framework that subsumes RoPE-Mixed as a special case (block size 2), which is a clean and intellectually satisfying contribution.

2. **Consistent accuracy improvements across 2D and 3D tasks.** The paper reports relative accuracy improvements of 10.0% over DeiT on CIFAR-100 and 15.1% on UCF101 (Table 1), with 95% confidence intervals stated in the table. The improvements also hold against stronger baselines (2.2% relative over RoPE-Mixed on CIFAR-100, 1.5% on UCF101), demonstrating robustness across modalities.

3. **Data and compute efficiency gains.** The paper shows LieRE can match the DeiT baseline accuracy using only 70% of training data (Figure 3b) and achieve comparable performance with ~3.9× fewer training steps (Figure 4b). These efficiency claims are practically relevant beyond raw accuracy.

4. **Systematic ablations on capacity.** The paper varies block size (2→8→64), tests parameter sharing across heads/layers (Table 2), and evaluates three backbone scales (ViT-T, ViT-B, ViT-L). The block-size ablation (Figure 4a) directly addresses whether performance comes from added capacity or the Lie group structure.

5. **Multi-resolution generalization.** LieRE maintains higher accuracy than RoPE-Mixed at inference resolutions not seen during training (196×196 to 448×448, Figure 2), a concrete advantage for real-world deployment.

## Weaknesses

### Fatal
None.

### Major

1. **The parameter-vs-structure confound is not fully resolved.** The paper acknowledges the question ("LieRE adds a small amount of capacity (580k parameters)" and varies block size to address it (Figure 4a), but does not include the obvious control experiment: adding equivalent extra parameters to the backbone (e.g., wider MLP or more heads) of the RoPE-Mixed baseline. Since block size 2 = RoPE-Mixed and block size 64 adds 580k parameters (~0.68% of 85.1M total), the block-size ablation mostly shows denser rotations help, but doesn't prove the non-commutative Lie group structure is the cause rather than simply more expressive rotations. This is the most significant gap in the paper's experimental support for its core scientific claim.

2. **Internal inconsistency in efficiency numbers.** Section 5.4 states "3.9 times less training epochs" and "3.9X reduction in training compute," while the Conclusion states "3.5 times less training compute." These are inconsistent for the same claimed result, suggesting sloppiness in how the numbers were computed or reported.

3. **Missing training hyperparameters for reproducibility.** The paper states training duration (200 epochs) and image size, but omits learning rate schedule, warmup steps, weight decay, batch size, optimizer, and RandAugment magnitude/number of operations. These are critical for reproducing the results and for assessing whether the baselines were fairly tuned. The statement "we did not optimize any hyperparameters for the LieRE model" (Section 4.1.2) is good practice, but the hyperparameters themselves must be reported.

### Minor

1. **ImageNet-1k results are underreported in prose.** The paper says "similar accuracy trends observed on ImageNet (table 1)" without any numerical detail in the text. Given that ImageNet from scratch is a challenging evaluation, the actual numbers (positive or negative) should be discussed explicitly.

2. **The compute and data efficiency experiments lack error bars and procedural detail.** The paper does not report multiple seeds or describe how the "comparable performance" threshold was chosen for the training time comparison (Figure 4b). While 95% CI are stated for Table 1 accuracy, the efficiency figures do not include them.

3. **No analysis of computational overhead.** The matrix exponential used in LieRE adds computational cost per forward pass compared to RoPE-Mixed's simple 2×2 rotations. The paper does not measure or discuss this overhead, which is directly relevant to its "compute efficiency" claims (which focus on training steps, not per-step cost).

### Trivial

None.

## Nice-to-Haves

- A parameter-matched ablation where RoPE-Mixed's backbone is widened to match LieRE's total parameter count (rather than just varying the PE block size) would strengthen the core claim about the Lie group structure.
- Reporting full training curves (accuracy vs. steps) for all methods on the data efficiency experiment, with multiple seeds and confidence bands.
- Measuring and reporting the per-step FLOP/runtime overhead of the matrix exponential in LieRE relative to RoPE-Mixed.

## Removed Points

These points were raised by reviewers but are removed as either factually incorrect, noise, or scope creep:

- **"The paper does not specify that the accuracy gains are relative."** The abstract explicitly says "marked relative improvements in accuracy (10.0% for 2D and 15.1% for 3D)." This claim is factually wrong.
- **"No confidence intervals reported."** Table 1 caption states "95% confidence intervals." Removed as factually wrong.
- **"30% less training data vs 70% of data is an inconsistency."** These are equivalent statements (30% less = using 70%). Not an inconsistency.
- **"Patch shuffling interpretation is wrong / could indicate less robustness."** The paper's interpretation (larger drop = more positional reliance) is standard in the field. The alternative offered is speculative.
- **"Baselines may be undertuned because hyperparameters aren't optimized for each method."** The paper uses identical hyperparameters for all methods and does not tune LieRE specifically. This is standard practice for fair comparison.
- **"Lie group exposition is unnecessary."** It provides useful mathematical context for the method and is not excessively long.
- **"Broader impacts are generic."** This is standard practice and not a weakness of the technical contribution.
- **"Table 1 not rendered (parser issue)."** The table exists in the original submission; parser limitations are not an author error.
- Several generic strengths from the Strength Finder ("addresses an important problem," "provides valuable insights") are dropped as lacking concrete anchor to specific content.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear tension: the paper makes ambitious claims (10-15% relative accuracy gains, 3.9× compute reduction) for what is conceptually a small change (denser rotation blocks), and the experimental design does not fully rule out capacity-driven explanations. This tension is the review's main insight, and it is fundamentally about the paper's evaluation design rather than a novel observation about the method itself.

## Suggestions

1. Fix the inconsistency between Section 5.4 (3.9×) and the Conclusion (3.5×) for the compute reduction claim.
2. Add a parameter-matched control: widen the MLP or increase head dimension in RoPE-Mixed to match LieRE's total parameter count, and report whether the accuracy gap persists.
3. Report all training hyperparameters (learning rate, schedule, warmup, weight decay, batch size, optimizer, RandAugment settings) in a table or appendix.
4. Discuss ImageNet-1k numerical results explicitly in prose, even if the gains are modest.
5. Add error bars to the efficiency figures (multiple seeds) and describe the threshold procedure for the training time comparison.
6. Measure and report the per-step computational overhead of the matrix exponential to contextualize the "3.9× fewer steps" claim.

## Score and Decision

**Originality (6/10):** The idea of densifying RoPE's rotation blocks is a natural extension of prior work, but the Lie group framing is a clean contribution.

**Importance of research question (8/10):** Positional encoding for multi-dimensional data is a relevant problem.

**Claims supported by evidence (5/10):** The accuracy improvements are reported with CIs, but the parameter confound is partially addressed but not fully resolved, and the efficiency claims lack procedural rigor.

**Soundness of experiments (6/10):** Reasonable breadth across 2D/3D and ablations, but missing controls and reproducibility details weaken confidence.

**Clarity of writing (7/10):** The method is clearly explained; the mathematical exposition is appropriate.

**Value to community (6/10):** If the claims hold, this is a useful contribution; the code release commitment is noted.

The paper has a solid core idea and a reasonable set of experiments, but the evidence is not as strong as the ambitious claims suggest. The parameter confound and the sloppiness in reporting efficiency numbers are the main concerns. The contribution is real but the evaluation needs tightening. This is a borderline paper with genuine strengths; a thorough revision could make it a solid acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>