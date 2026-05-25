Now I'll write the final consolidated review.

## Summary

This paper introduces a cosine-similarity-based method for categorizing gated neurons (SwiGLU/GEGLU) in transformers according to their "read-write" functionality — i.e., the relationship between what a neuron reads (its gate and input weight vectors) and what it writes (its output weight vector). Applying this method to 9 LLMs reveals a universal pattern: early-middle layers are dominated by *conditional strengthening* neurons, while late layers contain a small but consistent class of *weakening* neurons (where the input and output weights are roughly anti-aligned). Through ablation experiments on OLMo-7B, the authors show that these few weakening neurons have outsized influence on attribute rate and output entropy. A novel *conditional ablation* method further demonstrates that a substantial part of this effect comes from activations with negative gate values — a regime previously assumed to be unimportant beyond training dynamics. The paper also finds that weakening neurons activate far more often than strengthening neurons, explaining their disproportionate influence.

## Strengths

1. **Universal weight-based pattern across 9 LLMs.** Figure 1(a) shows that the median of cos(w_in, w_out) is positive in early layers and negative in late layers for all nine models examined (Llama-2/3, OLMo, Gemma, Mistral, Qwen, Yi), demonstrating a consistent strengthening-to-weakening shift across architectures. This is the paper's strongest empirical finding, as it shows the pattern is not an artifact of a single model.

2. **Weakening neurons have outsized influence on OLMo-7B.** Zero-ablating the 243 weakening neurons causes a visible degradation in attribute rate from layer ~10 onward and shifts the next-token entropy distribution, whereas ablating the same number of random neurons from the same layers has no such effect (Figure 3a, 3b top row). This directly supports the claim that weakening neurons, despite their small number, are disproportionately influential.

3. **Conditional ablation reveals negative gate values as functionally important.** By ablating only activations with x_gate < 0, x_in < 0 (case iii), the paper reproduces the entropy effect of full weakening ablation, while the other three sign combinations show little effect (Figure 3b bottom row). This is the first clear evidence that negative Swish values encode a functionally relevant mechanism in gated transformers, beyond their well-known role in training dynamics.

4. **Strong negative correlation between activation frequency and cos(w_in, w_out).** Figure 4 shows a correlation of -0.97 in layer 15 of OLMo-7B, meaning the few weakening neurons activate orders of magnitude more often than the many strengthening neurons. This provides a mechanistic explanation for their outsized influence.

## Weaknesses

### Fatal

None.

### Major

1. **Functional importance demonstrated on only one model (OLMo-7B).** The weight-based pattern analysis covers 9 models, which is convincing. However, the ablation experiments that demonstrate "outsized influence" — the paper's most striking contribution — are performed exclusively on OLMo-7B. The title and abstract imply general properties of transformers, but the evidence for functional significance (and the discovery about negative gate values) rests on a single architecture, training dataset (Dolma), and scale (7B). Without similar ablation on at least one other model (e.g., Llama-3.2-3B or Gemma-2B), the generality of the functional claims remains unsupported. The paper acknowledges this as a resource constraint (§6), but the issue is too central to the contribution to be deferred.

### Minor

1. **Ambiguity about the vector space for cosine similarities.** The paper states that all weight vectors have dimensionality d_model, but w_gate and w_in operate on the layer-normalized input (x_norm) while w_out writes to the unnormalized residual stream. TransformerLens typically folds layer norms into adjacent weights (which would place all vectors in the same space), but the paper never explicitly confirms this. The statement that TransformerLens applies "preprocessing steps to make the weights more interpretable without changing model behavior" (§3.2) is too vague to resolve the question. This does not invalidate the method (the cosine similarity is still a meaningful geometric measure in R^d_model regardless of whether LN is folded), but the paper should clearly state whether LN is folded so readers can assess whether the cosine similarities compare vectors that operate on the same space.

2. **Sign-flip preprocessing and conditional ablation interpretation.** The paper multiplies w_in and w_out by sign(cos(w_gate, w_in)) so that cos(w_gate, w_in) ≈ 1 for all neurons. The conditional ablation conditions (x_gate < 0, x_in < 0, etc.) are defined in this transformed space. For neurons where the sign was flipped, the condition "x_in < 0" in the transformed model corresponds to "x_in > 0" in the original model. The paper discusses the interpretation in the transformed space (e.g., §6.2: "When x_gate < 0, the usual neuron behavior gets a minus sign in front"), which is valid, but it never explicitly maps the conditions back to the original weights. This leaves room for confusion about what the "negative gate values" finding actually means in terms of the original model parameters.

3. **Arbitrary classification thresholds without sensitivity analysis.** The taxonomy uses ±0.5 as thresholds for categorizing neurons into strengthening, weakening, conditional strengthening, etc. The core claim about the *existence* of weakening neurons is robust (they form a visible cluster in scatter plots, Figure 2), but the quantitative distribution claims (e.g., "conditional strengthening dominates early-middle layers") depend on the threshold. No sensitivity analysis is provided to show whether the layer-wise trends hold under different cutoffs (e.g., ±0.4 or ±0.6). The paper does offer continuous alternatives (scatter plots, median analysis), which partially mitigates this concern.

4. **No variance measures for ablation results.** The ablation experiments (Figure 3) are reported as single runs with no error bars, confidence intervals, or standard errors. The histograms in Figure 3b show aggregate counts across model predictions but do not convey uncertainty about the effect size. While single-run evaluations are common in interpretability work, the quantitative nature of the claims (e.g., "weakening neurons decrease entropy by about 10 nats") would benefit from some measure of variability.

5. **No dedicated limitations section.** The paper does not explicitly discuss its limitations. Key constraints — the single-model ablation, the threshold sensitivity, the reliance on TransformerLens preprocessing defaults — are mentioned only in passing or deferred to the appendix. A brief limitations section would help readers calibrate the scope of the claims.

### Trivial

None.

## Nice-to-Haves

- Extend ablation to at least one additional model (e.g., Llama-3.2-3B). A smaller-scale replication would substantially strengthen the claim that the findings generalize beyond OLMo-7B.
- Provide a robustness analysis for the ±0.5 classification thresholds, showing that the qualitative layer-wise trends hold when varying the cutoff.
- Report mean entropy change and standard error for each conditional ablation condition (Figure 3b) to let readers assess effect size and variability more precisely.
- Add a brief comparison explaining what new insights the RW perspective yields that prior neuron taxonomies (Voita et al., 2024; Gurnee et al., 2024) could not, to help readers appreciate the added value.

## Removed Points

These points were raised by the harsh critic but are removed after verification against the paper:

- **"The vector space issue is foundational — if LN is not folded, the entire taxonomy collapses."** The paper states all weight vectors have dimensionality d_model (§3.1). TransformerLens standard preprocessing does fold layer norms; this is well-documented in their codebase. Even without folding, the cosine similarity between R^d_model vectors is geometrically meaningful. The claim that the taxonomy would "collapse" is disproportionate. Downgraded to Minor weakness #1.
- **"The paper never explicitly explains what new findings the RW perspective yields that prior taxonomies could not."** The introduction and §2 contrast the RW approach with prior activation-based and output-weight-only analyses, and the results (weakening neurons, negative gate values) are findings that prior methods had not surfaced. The comparison is implicit but present.
- **"Missing reproducibility details (Dolma subset size, seed, token count)."** The paper states 20M tokens from Dolma (§6) and follows the setup of Voita et al. (2024). The appendix (removed by parser) likely contains further details.
- **"The strength about strong empirical results."** This strength was not present in the Strength Finder's output as formulated; no removal needed.
- **"Case studies do not add strong evidence."** The case studies are presented as qualitative illustrations, not as primary evidence. The paper does not rely on them for its core claims.

## Novel Insights

The paper's key novel insight — that weakening neurons exist as a distinct functional class in gated transformers, that they cluster in late layers across 9 architectures, and that a significant part of their influence operates through negative gate values — is genuinely new. The conditional ablation technique is itself a methodological contribution, as it allows attribution of neuron-level effects to specific activation regimes (sign combinations of gate and input values) rather than the neuron as a whole. The discovery that negative Swish values, often dismissed as a training-dynamics artifact, encode a functionally important mechanism in trained models is noteworthy and opens a new direction for interpretability research on gated activations.

Beyond the paper's own contributions, the review points to a broader question: why do models consistently learn a strengthening-to-weakening layer profile? Is this forced by the residual stream dynamics (early layers build representations, late layers sharpen predictions), or does it reflect something fundamental about how gated MLPs process information? The paper does not (and need not) answer this, but the empirical pattern is provocative.

## Suggestions

1. **Clarify the vector space.** Explicitly state whether TransformerLens folds layer norms into w_gate and w_in (so that all vectors live in the residual-stream space), or explain why the cosine similarity is meaningful regardless.
2. **Run ablation on one additional model**, even at smaller scale (e.g., Llama-3.2-3B with the same 20M-token setup). This single addition would substantially strengthen the generality claim.
3. **Map the conditional ablation conditions back to the original weights.** Show an explicit example of a neuron where the sign was flipped and explain what the "gate < 0, in < 0" condition means in the original (pre-transformation) model.
4. **Add a sensitivity analysis** for the ±0.5 threshold, showing how neuron class proportions vary with the cutoff, or shift focus to the continuous analysis (scatter plots, median trends) which does not depend on thresholds.
5. **Add a brief limitations paragraph** acknowledging the single-model ablation, threshold arbitrariness, and ambiguity about the vector space.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round / Bucket | Comparison |
|--------|-----------|----------------|------------|
| DOCS (XBHoaHlGQM) - weight similarity | 6.60 | R1 topic-mid | Stronger paper with similar weight-analysis methodology; better evaluation breadth but weaker ablation content. Paper under review is slightly weaker due to single-model limitation. |
| NeurFlow (GdbQyFOUlJ) - neuron groups | 6.50 | R1 topic-mid | More rigorous evaluation with multiple validation experiments. Paper under review has more novel findings but less rigorous evaluation. |
| Influential Neuron Path (WQQyJbr5Lh) - ViT neurons | 6.00 | R2 narrow | Similar in type (identifying influential neurons) and of comparable quality. Paper under review has stronger novelty but weaker breadth. |
| What Makes a Good Prune (jsvvPVVzwf) - cosine similarity | 5.00 | R2 narrow | Less relevant topic but similar score band. Paper under review is stronger in contribution novelty. |
| Identifying Sub-networks (sp9irsV1yq) - GW distance | 4.60 | R2 narrow | Rejected, weaker execution and unclear contributions. Paper under review is stronger. |
| Interpretability Illusions (v675Iyu0ta) - simplified models | 5.60 | R1 weakness (single model) | Rejected but had mixed reviews (5,8,6,6,3). The single-model concern is different in nature from this paper's limitation. |
| Principled Eval Framework (todLTYB1I7) - neuron explanations | 5.00 | R1 weakness (neuron classification) | Rejected; different focus but same score band. Paper under review has clearer contributions. |
| Metanetwork (9L9j5bQPIY) - weak interpretability | 2.50 | R1 topic-low | Clearly weaker paper. Paper under review has much stronger methodology and results. |

**Round 1 bracket:** 4.5 – 6.0. The paper is clearly stronger than the low-band anchors (1.67–3.40) but has significant enough limitations (single-model functional evidence, presentation gaps) to sit below the strongest mid-band anchors (6.50–6.60).

**Round 2 narrowing:** Compared against anchors in the 4.6–6.6 range, the paper under review is most comparable to the Influential Neuron Path paper (6.00) and the DOCS paper (6.60), but with a more limited evaluation scope than either. It is stronger than the rejected papers in the 4.6–5.6 range. The single-model functional evidence is the primary factor preventing a higher score.

**Final score:** 5.5. The paper makes genuine novel contributions (weakening neuron discovery, conditional ablation, negative gate value mechanism) supported by strong cross-model weight analysis. However, the functional claims rest on experiments with a single model, several methodological details are underspecified, and the presentation would benefit from sensitivity analysis and explicit limitations. These issues are addressable and do not invalidate the work, but they prevent it from being a strong accept in its current form.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>