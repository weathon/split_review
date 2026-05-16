Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes MöbiusAttention, a novel attention mechanism that replaces the standard linear query function with an element-wise Möbius transformation applied to a complex-valued token+position representation. The authors integrate this mechanism into BERT and RoFormer (forming MöbiusBERT and MobRoFormer), pre-train the models on C4, and fine-tune on GLUE. The paper reports competitive average GLUE scores with marginally fewer parameters (104M vs 110M) and provides an analysis of the learned geometric properties.

## Strengths

- **Novel integration of Möbius transformations into the attention mechanism.** The paper introduces a genuinely new idea — using the fractional linear (Möbius) transform over complex token-position vectors as the query function — which goes beyond prior non-linear attention approaches (RoPe, NeuralAttention) that operate in a single geometric space. The connection to the projective linear group PGL(2,ℂ) and the Riemann sphere provides a mathematically grounded framing.

- **Analysis of learned geometry distributions.** The paper empirically shows (Figure 4, Section 6.1.1) that the model learns a diverse range of geometries (Circular, Elliptic, Hyperbolic, etc.) with layer-level and head-level specialization. This analysis offers a novel lens for understanding what the attention mechanism captures, and demonstrates that the model extends beyond the purely circular geometry of RoPe.

- **Competitive GLUE performance with fewer parameters.** MöbiusBERT variants achieve slightly higher average GLUE scores (83.85, 83.82 vs. 83.64 for BERT) using 104M parameters versus 110M, with the same pre-training duration (26 hours). This is a non-trivial demonstration — the models were pre-trained from scratch, not fine-tuned from existing checkpoints.

## Weaknesses

### Fatal
None.

### Major

- **The attention computation with complex-valued logits is not fully specified (method-definition gap).** The paper defines (Section 5, lines 315–319) `Att = softmax(O/√d)V` where `O = QK^T` and both Q and K are complex-valued matrices. Softmax is not defined on complex numbers — it requires real-valued inputs. The paper provides no mechanism (e.g., taking the real part, magnitude, or some other operation) for converting the complex attention logits to real values before softmax. This omission makes the core method as currently described mathematically incomplete and not reproducible. While this is likely a fixable oversight (e.g., one would take the real part of QK^T), the choice of conversion matters for the method's behavior and must be explicitly stated.

- **No statistical significance or variance reporting.** The reported GLUE gains are small (average +0.2 to +0.5 points over BERT). The paper reports only single-run scores without any confidence intervals, standard deviations, or multi-seed fine-tuning results. Given that pre-training and fine-tuning involve substantial randomness, these small differences could easily fall within run-to-run variation. Without some measure of variance, the reader cannot assess whether the improvement is meaningful.

### Minor

- **Element-wise Möbius transformation partially decouples the geometric motivation from the actual computation.** The Möbius transformation is applied independently to each of the d complex dimensions (Eq. 4). The geometric properties of Möbius transformations (acting on the Riemann sphere as a 2D surface) are not preserved when each complex number is treated in isolation. The paper's heavy emphasis on projective geometry and Riemann-sphere visualization is thus partly decoupled from the actual element-wise operation, weakening the claimed connection between the mathematical motivation and the implementation.

- **Overclaimed efficiency benefits.** The paper states its approach "requires fewer layers than the vanilla model and is more efficient in memory and time." In practice, MöbiusBERT uses 11 layers vs. BERT's 12 — a trivial difference that could be matched by simply removing one vanilla layer. The only memory comparison offered is the parameter count (104M vs. 110M); no actual throughput, memory footprint, or latency benchmarks are provided. The claim of efficiency gains is overstated relative to the evidence.

- **Marginal and inconsistent performance gains.** The average GLUE improvement over BERT is ~0.2 points for MöbiusBERT H&T and ~0.2 for the Ortho variant. Gains are concentrated on a few tasks (QQP, QNLI, CoLA) while performance degrades on others (STS-B, MRPC). The paper does not discuss where or why MöbiusAttention helps versus hurts, which limits the insight the community can extract from the results.

- **The "learning to forget" claim is qualitatively stated but not quantitatively supported.** The paper asserts (Section 6.1.1) that MöbiusAttention assigns zero attention scores to many token pairs, unlike vanilla attention. However, no quantitative comparison of attention sparsity, distribution statistics, or head-level analysis between vanilla and Möbius attention is provided. The claim remains an interesting observation without empirical backing.

### Trivial

- Model variant abbreviations (H, T, Ortho) are only defined in the table caption; a brief textual explanation in the body would improve readability.

- The softmax non-linearity discussion in the introduction (lines 82–84) makes a nuanced claim ("softmax is only used to produce a probability distribution... not to introduce non-linear interdependencies") that could be better clarified. Softmax is a non-linear operation on each row, so the distinction the paper intends is about the *query/key computation* being linear, not about the overall attention function being linear.

## Nice-to-Haves

- Multi-seed fine-tuning (even 3 seeds) with reported means and standard deviations would substantially strengthen the experimental evidence.
- A controlled comparison isolating a single Möbius layer against a single vanilla layer (holding all else equal) would more directly test whether the transformation itself is beneficial, independent of the architectural scaffolding.
- Actual wall-clock time and peak memory benchmarks comparing MöbiusAttention to vanilla attention at the same hidden dimension and sequence length.
- A discussion of the design choice for real-to-complex conversion before softmax (e.g., why taking the real part vs. magnitude vs. some other function), as this affects both the geometry and the training dynamics.

## Removed Points

- **Missing ablation table / SST-2 table**: The reviewer criticized the absence of these tables in the provided text. The parser strips appendix sections from all papers; these tables likely exist in the original submission. Removed per instructions.
- **"Baseline scores lower than typical reported numbers"**: The authors trained baselines themselves under identical conditions for fair comparison, which is standard practice. Removed per instructions.
- **"Incomplete references to figures (attention heatmaps)"**: The incomplete figure references may point to appendix figures. Removed per instructions.
- **Missing related works**: Per instructions, I do not have external sources to verify the existence of missing references. Removed.
- **Reproducibility nitpicks about undisclosed hyperparameters / implementation details**: The paper provides sufficient experimental setup (batch size, steps, framework, GPU type, etc.) for the scale of the experiments. Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews identify significant gaps (complex softmax, missing variance, element-wise disconnect) but do not generate new interpretations of the method or its results.

## Suggestions

1. **Define the complex-to-real conversion for softmax explicitly.** State clearly whether the real part, magnitude, or squared modulus of `QK^T` is used before softmax. This is non-negotiable for the method to be reproducible.
2. **Report variance.** Even a simple statement of mean and standard deviation over 3–5 fine-tuning seeds would dramatically improve the credibility of the results.
3. **Address the element-wise disconnect.** Either justify why element-wise application preserves the geometric properties, or reframe the motivation to focus on complex-valued representational capacity rather than Riemann-sphere geometry.
4. **Add timing/memory benchmarks.** Provide a simple table comparing training throughput, peak memory, and inference speed for MöbiusAttention vs. vanilla attention at equivalent settings.
5. **Quantify the "learning to forget" claim.** Provide a histogram or summary statistic of attention-weight sparsity comparing vanilla and Möbius attention heads.

## Score and Decision

The paper introduces a genuinely novel idea — using Möbius transformations for the attention query function — with a mathematically grounded motivation and some interesting geometric analysis. However, the core method definition is incomplete (complex softmax not specified), the experimental evidence for improvement is thin (marginal gains without variance), and the geometric motivation is partially disconnected from the element-wise implementation. The paper has clear potential but requires major revisions to be convincing.

**Score:** 5.5  
**Decision:** Reject

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>