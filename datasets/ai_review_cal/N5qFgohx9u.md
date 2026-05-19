- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3
Now I have a thorough understanding of the paper and both reviews. Let me construct the final consolidated review.

---

## Summary

This paper proposes MöbiusAttention, a novel attention mechanism that replaces the linear query transformation with an elementwise complex-valued Möbius transformation (a rational function of the form (az+b)/(cz+d) per dimension). The authors integrate this into BERT and RoFormer architectures, pre-train on C4, and evaluate on GLUE. Their best variant (MöbiusBERT, 104M params) achieves an average GLUE score of 83.85 vs. BERT baseline (110M params) at 83.64. They also analyze the learned Möbius geometries and find that the model learns diverse transformation types (circular, elliptic, hyperbolic, etc.) beyond the purely circular geometry of RoPE.

## Strengths

1. **Novel integration of Möbius transformations into attention.** The idea of replacing the linear query projection with per-dimension Möbius transformations is mathematically well-specified (§4) and clearly distinct from prior work on non-linear attention (RoPE, NeuralAttention). The paper connects this to the rich mathematical structure of the Möbius group and projective linear group PGL(2,ℂ).

2. **Evidence that the model learns diverse geometries beyond circular.** The analysis in §5 (Fig. 6) shows that the learned Möbius matrices span multiple transformation types (circular, elliptic, hyperbolic, loxodromic, parabolic) and exhibit both layer-level and head-level specialization. This goes beyond RoFormer's purely circular geometry and provides a concrete, observable difference between the proposed method and prior work.

3. **Competitive efficiency with fewer parameters.** MöbiusBERT achieves comparable or slightly better GLUE scores with 104M parameters vs. 110M for the BERT baseline, with the same reported pre-training time (26 hours). The space and time complexities remain O(n²d + nd²) (§4.5). This suggests the added expressivity does not come at prohibitive computational cost.

4. **Systematic ablation of MöbiusAttention placement.** The ablation study (§5.4) tests four configurations (top, stacked, framed, alternating) and identifies the framed design (first and last layers) as best. This provides practical architectural guidance.

## Weaknesses

### Major

1. **Marginal improvements without statistical validation.** The best MöbiusBERT variant averages 83.85 vs. BERT at 83.64 — a gain of **0.21 points on average**. On individual tasks, differences are often within a few tenths of a point (MNLI-m: +0.03, QQP Acc: +0.36, QNLI: +0.56). No confidence intervals, per-seed variance, or statistical significance tests are reported. For a new method to convincingly establish its value, the improvements need to be clearly outside the noise range — especially with only a single run per configuration.

2. **Architectural confound prevents clean attribution to Möbius.** The Möbius models differ from the baselines in multiple ways beyond the Möbius transformation itself: (a) different number of layers (11 vs. 12), (b) a 50/50 split of Möbius and vanilla attention heads within layers (vs. all vanilla), and (c) architectural modifications for complex channels (doubled linear layers, separate residual connections). The ablation study only compares MöbiusBERT variants against each other — it never includes a control where the *same* layer/head configuration uses vanilla attention everywhere (with matched parameter count). Without this, the ~0.2 point improvement cannot be confidently attributed to the Möbius transformation specifically rather than to the architectural changes (e.g., the 50/50 head split, the channel doubling, or simply having fewer layers).

### Minor

3. **"Learning to forget" claim uses technically imprecise language about zero weights.** The paper states (§5): "MöbiusAttention gives most of the pairs zero score and only a few a non-zero one" and "Möbius can give a zero value to elements." Since attention weights are computed via softmax (Equation 2), no weight can be *exactly* zero unless the corresponding logit is −∞. The paper's intended point — that MöbiusAttention produces highly sparse attention patterns with many near-zero weights — may still be valid and interesting, but the literal claim of exact zeros is mathematically incorrect and should be corrected to "near-zero" or "extremely small."

4. **Geometric interpretation is somewhat disconnected from the per-dimension computation.** The paper motivates MöbiusAttention through rich geometric concepts (Riemann sphere, SL(2,ℂ) volume preservation, mapping between line and circle geometries), but the transformation is applied independently per dimension (§4: "element-wise Möbius transformation"). Volume preservation under SL(2,ℂ) is a property of the per-dimension 2×2 matrices acting on individual complex scalars, not a property relating tokens to each other. The claim that this "maps the set of source token-position pairs to the set of target token-position pairs" (§4.4) inflates the geometric interpretation beyond what the per-dimension operation actually provides. The core mechanism — non-linear elementwise query transformation — is valid on its own merits and does not need this geometric framing.

5. **Method description has underspecified details.** Several aspects are unclear: (a) The key/value functions in §4 are written as scalar multiplications $\mathbf{w}_{kj} \rho_{ij}$ but the architecture description mentions "separate layers for the imaginary and real channels" (§5), suggesting full matrices; this inconsistency is never resolved. (b) The "Low-Dimensional Möbius Models" variant (applying Möbius after a linear query transformation) is mentioned but never formally specified. (c) The table notation (H, T, Ortho) is defined only in the caption, making the main text hard to follow. (d) The paper mentions quality issues with SST-2 and CoLA and reports results on "revised" versions in a referenced table, but never describes what revisions were made or why.

6. **The "Overall (Möbius)" and "Overall (others)" rows in Table 1 cherry-pick the best score per task across multiple model variants.** The average of 84.17 for Möbius vs. 84.03 for baselines is misleading because no single model achieves either number. The paper does label these rows transparently ("best performers across the two model categories"), but presenting them alongside individual model rows invites overinterpretation. The fair comparison is between individual models (e.g., MöbiusBERT H&T Ortho at 83.85 vs. BERT at 83.64).

### Trivial

- The paper states "we pretrain for 70,000 steps with a batch size of 4096" using the MosaicBERT framework. This differs from BERT's original 1M steps and uses C4 instead of BookCorpus+Wikipedia. While the baselines are retrained under the same conditions (making the comparison internally fair), it means results are not directly comparable to published BERT scores.

## Nice-to-Haves

- A control experiment matching the Möbius architecture (layer count, head split, channel doubling) but using vanilla attention with added parameters would isolate the Möbius effect.
- Per-seed variance or confidence intervals for the GLUE results would help assess whether the 0.21-point average gain is statistically meaningful.
- Learning curves during pre-training (MLM loss) would strengthen the analysis.

## Removed Points

- **Criticism about missing figures** (attention heatmaps, architecture diagram) — REMOVED. These are stripped by the PDF parser; they exist in the original submission per the instructions.
- **Criticism about missing comparison to NeuralAttention** — REMOVED. Per instructions, missing related works should not be mentioned.
- **Criticism that the "geometric motivation is disconnected" is a non-sequitur** — This point is kept but downgraded to Minor. The paper explicitly says the transformation is elementwise; the critic's framing as a "non-sequitur" overstates the issue.
- **Reproducibility nitpicks about singularities in Möbius backpropagation** — REMOVED. This is a minor implementation detail beyond what a conference paper typically specifies.
- **Claims about "modified datasets breaking comparability"** — REMOVED from main weaknesses. The main results (Table 1) use standard GLUE tasks. The mention of revised versions is for additional analysis in a missing table. The concern is more about clarity than credibility.
- **Strength: "Improved GLUE performance with fewer parameters"** — KEPT but qualified. The improvement is real (+0.21) but marginal.
- **Strength: "Empirically observed learning to forget"** — WEAKENED in the strength list below. The claim about exact zeros is imprecise; the paper does not show the actual heatmaps in the extracted text.

## Novel Insights

The harsh critic correctly identifies the core experimental weakness (marginal gains + architectural confound) and the inflated geometric framing, but overstates several points into "fatal" territory. The strength finder correctly identifies the genuine novelty and the interesting geometry analysis, but overstates the experimental evidence. The deeper issue is a calibration gap: the paper makes ambitious theoretical claims (geometric expressivity, learning to forget) that its modest experiments (0.21 point gain, no controls) do not adequately support. The method itself is novel and the geometry analysis is a genuine contribution, but the paper would benefit from either stronger evidence (controlled experiments, significance testing) or more modest claims. The most interesting finding — that the model learns multiple geometric types beyond circles — is undersold in the current presentation relative to the attention to mathematical background.

## Suggestions

1. Add a control experiment: same architecture (11 layers, 50/50 head split, channel doubling) with vanilla attention everywhere, matched parameter count.
2. Report per-seed variance or at minimum run each configuration 3 times with different seeds.
3. Correct the "zero weight" claim to "near-zero weight" and provide quantitative evidence (e.g., histogram of attention weights showing mass near zero).
4. Clarify the SST-2/CoLA "quality issues" — either report only standard GLUE results or clearly describe any modifications.
5. Tone down the geometric framing to match what the per-dimension elementwise operation actually delivers.
