Now I have a thorough understanding of the paper and the calibration anchors. Let me produce the final consolidated review.

## Summary

The paper introduces a weight-based method for analyzing gated neurons in transformers by computing cosine similarities between their input, gate, and output weight vectors, creating a taxonomy of "read-write" (RW) functionalities. Applying this to 9-12 LLMs, the authors observe a universal pattern: early-middle layers are dominated by conditional strengthening neurons, while late layers shift toward weakening neurons. They further find that a small class of 243 "weakening" neurons in OLMo-7B has a disproportionate effect on attribute rate and output entropy when ablated, and that part of this effect stems from activations where the gate value is negative — a novel observation since negative SwiGLU gate values were previously assumed unimportant for model functionality.

## Strengths

1. **Universal cross-model pattern of neuron RW functionality.** The paper demonstrates across 9-12 models (Llama, Gemma, OLMo, Mistral, Qwen, Yi) that early-middle layers are dominated by conditional strengthening neurons, while late layers shift toward weakening neurons (Figure 1a, Section 5). This consistency is striking and suggests a fundamental architectural property of gated transformers, uncovered with a simple weight-based method.

2. **First evidence of a functional role for negative gate values.** Using conditional ablation (a novel analysis tool introduced as contribution iv), the paper shows that a large part of the entropy-sharpening effect of weakening neurons comes from activations with \(x_{\text{gate}} < 0\) and \(x_{\text{in}} < 0\) (Figure 3b, Section 6.2). This is genuinely surprising because the Swish function's negative region was previously assumed to be only useful for training dynamics. The paper explicitly acknowledges concurrent work by Kong et al. (2025) on a different phenomenon.

3. **Novel read-write analysis method for gated neurons.** The cosine-similarity-based taxonomy (Table 1, Section 4.2) provides a principled way to categorize neurons by their weight geometry. This neuron-based approach is simpler than SAE-based methods and, as the results show, can reveal meaningful structure even without activation data.

## Weaknesses

### Major

- **Activation frequency confound in ablation experiments.** The paper's central claim that weakening neurons have "outsize influence" rests on comparing ablation of all 243 weakening neurons against 243 random neurons from the same layers (Figure 3). However, Section 7 establishes a strong negative correlation between \(\cos(\mathbf{w}_{\text{in}},\mathbf{w}_{\text{out}})\) and activation frequency — weakening neurons activate very often, while random neurons from the same layers (which likely include many strengthening neurons with positive cosine) activate rarely. The observed ablation effect could therefore be driven by activation frequency rather than by the "weakening" property (negative cosine) per se. The paper acknowledges this partially ("activation frequencies do not fully explain their effect") but does not control for it — e.g., by selecting baseline neurons matched on activation frequency but differing in \(\cos(\mathbf{w}_{\text{in}},\mathbf{w}_{\text{out}})\) sign. Until this is controlled, the evidence that the weakening *class* (defined by weight geometry) is causally responsible for the outsize influence remains unconvincing.

### Minor

- **Activation-based validation of the RW classification is limited.** The paper's taxonomy (strengthening, weakening, etc.) is derived purely from weight cosine similarities, but the behavioral interpretation — that "weakening" neurons actually reduce the presence of a concept — is not systematically validated against activation-level behavior. Only a single qualitative case study of one weakening neuron (Section 8) is provided. A systematic correlation between weight-based classes and activation-level effects (e.g., whether a neuron's output tends to increase or decrease the logit of tokens corresponding to its input direction) would substantially strengthen the foundation of the analysis.

- **Comparison across RW classes is unclearly specified in the main text.** The paper states that results for other neuron classes are "indistinguishable from the clean line" (Figure 3 caption) and refers to the appendix. It is not clear from the main text whether, for classes with many more members (e.g., conditional strengthening has thousands of neurons), the same fixed number (243) was ablated, or all members of each class were ablated. If only 243 were ablated, the comparison may be too weak to reveal an effect for larger classes. The main text should clarify the protocol.

- **Conditional ablation results demonstrated only on one model and one metric.** The finding that negative gate values contribute to entropy sharpening is shown only for OLMo-7B using entropy as the metric (Section 6.2). While this is a valuable first observation, the paper's broader claim that this mechanism is "important for transformer functionality" would be stronger if replicated on at least 1-2 additional model families and with other metrics (e.g., attribute rate under the same conditional ablation).

- **Attribute rate is not defined in the main text.** The paper references Geva et al. (2023) but does not define "attribute rate" in the main body, requiring readers to consult the appendix. A one-sentence definition would improve readability.

- **Threshold \(\tau = \pm 0.5\) is used without justification.** The choice of threshold for classifying neurons into prototypical RW classes (Section 4.2) is stated but not motivated or tested for sensitivity. A brief sensitivity analysis or citation for the choice would help.

### Trivial

- The abstract claims "for the first time" regarding negative gate values, while the main text (Section 6.2) correctly qualifies this as "concurrently with Kong et al. (2025)." The abstract should match this qualification.
- Figure 1(a) shows only 9 of the 12 models listed in Section 5; this is acceptable (the other 3 are in the appendix) but the caption could note this.

## Nice-to-Haves

- **Scale the conditional ablation analysis.** Replicating the conditional ablation on at least one other model (e.g., Llama-3.2-3B) and testing whether the same negative-gate mechanism affects other metrics (e.g., attribute rate on factual recall tasks) would substantially strengthen the paper's most novel claim.
- **Control for activation frequency in ablation.** Running the weakening ablation alongside a baseline matched on activation frequency (sampled from the same layers but with positive \(\cos(\mathbf{w}_{\text{in}},\mathbf{w}_{\text{out}})\)) would either confirm or delimit the claim of "outsize influence."
- **Provide aggregate statistics for the ablation results.** The entropy histograms in Figure 3(b) would benefit from reporting mean effect sizes and standard errors, not just distributions.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The main text does not define 'attribute rate'"** — This is actually correct: the paper cites Geva et al. (2023) but does not define the term in the main text. However, I've kept this as a Minor weakness above since it's a presentation issue.
- **"The paper does not discuss whether observed patterns might be an artifact of weight parameterization"** — This is speculative and the paper does address potential geometric biases through random baselines (Section 4.3). Removed.
- **"The claim that the pattern holds across all 12 models, but Figure 1(a) shows only 9 models"** — The paper clearly states "three representative plots" and references the appendix for others. Removed.
- **"No justification for the choice of threshold (τ=±0.5)"** — This is a legitimate but minor point. I've kept it as a trivial weakness.
- Strength Finder's claim about "First evidence of a mechanism involving negative gate values" — This is a genuine strength supported by the conditional ablation experiment. Kept.
- **"Universal cross-model pattern"** from Strength Finder — This is supported by Figure 1(a) across 9 models. Kept.

## Novel Insights

The reviews surface one observation that goes beyond the paper's own contributions: the activation frequency confound identified by the harsh critic is not just a methodological nitpick but directly questions whether the "weakening" property (negative \(\cos(\mathbf{w}_{\text{in}},\mathbf{w}_{\text{out}})\)) is causally responsible for the observed influence, or whether the effect is driven by the strong correlation between negative cosine and high activation frequency. The paper's own Section 7 shows this correlation is nearly linear (e.g., \(-0.97\) in Layer 15). This means the paper is essentially arguing for the causal significance of a property that is tightly entangled with a simpler, more direct measure (activation frequency). The negative-gate-value finding partially disentangles this because it is specifically about weakening neurons and is not explained by activation frequency alone, but the central "outsize influence" claim needs the confound resolved.

## Suggestions

1. **Add an activation-frequency-matched control ablation.** This is the single most impactful improvement: select 243 neurons from the same layers as the weakening neurons that match them in activation frequency but have positive \(\cos(\mathbf{w}_{\text{in}},\mathbf{w}_{\text{out}})\). If the effect disappears, the claim should be reframed; if it persists, the evidence for "weakening" as a causal class is much stronger.
2. **Extend conditional ablation to at least one more model** (e.g., Llama-3.2-3B) and at least one more metric (e.g., attribute rate under conditional ablation) to demonstrate generality.
3. **Clarify the ablation protocol for other RW classes** in the main text: state explicitly how many neurons were ablated for each class (fixed number vs. all members) and why.
4. **Include behavioral validation** for a random sample of neurons from each RW class by checking whether the neuron's output direction aligns with the predicted strengthening/weakening effect on token logits.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Query Bucket | Comparison |
|--------|-----------|--------------|------------|
| Retrieval Head (EytBpUGB1Z) | 8.00 | Topic-high | More rigorous evaluation across more models and tasks; cleaner causal evidence |
| NeurFlow (GdbQyFOUlJ) | 6.50 | Topic-mid | Better-evaluated but focused on vision CNNs; comparable contribution level |
| Discovering Influential Neuron Path (WQQyJbr5Lh) | 6.00 | Topic-mid | More rigorous ablations but limited to ViT; similar "small set of important units" framing |
| Neuron to Graph (JBLHIR8kBZ) | 4.00 | Topic-mid | Limited to single SoLU model, weaker evaluation; paper under review is stronger |
| Automatically Identifying Sparse Circuits (89wVrywsIy) | 3.40 | Topic-low | Lacked baselines, qualitative only; paper under review has more substance |
| Llamas think in English (fSbPwHjdDG) | 3.00 | Topic-low | Weak causal evidence; paper under review has better methodology |
| Is This the Subspace (Ebt7JgMHv1) | 6.33 | Weakness-query | About interpretability illusions; rigorous methodology |

The low-band topic anchors (3.00-3.40) were rejected primarily for lacking proper baselines, limited model scope, or weak causal evidence. The paper under review shares some of these weaknesses (limited causal evidence on one model for the conditional ablation claim, no activation frequency control) but avoids the most severe ones (it has proper random baselines, covers many models for the cross-model analysis, and provides multiple metrics). The mid-band anchors (4.00-6.50) show that papers with clear but incompletely validated findings typically score in the 4-5 range, while papers with more rigorous controls reach 6+. The paper under review has a clear methodological contribution and an interesting discovery (negative gate values), but the activation frequency confound undermines the central causal claim to a degree that keeps it below the 6.0 threshold.

The paper shares some of the failures of the low-band topic anchors (incomplete causal evidence, claims slightly ahead of what the experiments rigorously show) but improves on them with broader model coverage and better baselines. It does not fully match the rigor of the 6+ anchors.

Score: 5.0 — Above reject range, but the activation frequency confound is a real weakness that prevents confident acceptance. The paper makes a genuine contribution (the cross-model pattern and negative-gate-value finding are interesting), but the central claim about "outsize influence" needs stronger controls.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>