Now I have everything I need. Here is my consolidated meta-review:

---

## Summary

This paper introduces a weight-based cosine-similarity method for analyzing gated neurons (SwiGLU/GEGLU) in transformers. By computing cosine similarities between the gate (w_gate), input (w_in), and output (w_out) weight vectors, the authors define a taxonomy of "read-write" (RW) functionalities—including "weakening" neurons (where w_in and w_out are negatively correlated) and "conditional strengthening" neurons. The key findings are: (1) median cos(w_in, w_out) follows a consistent positive-to-negative trajectory across layers in 12 LLMs, (2) a small class of ~243 weakening neurons (in OLMo-7B) has outsized influence on attribute rate and output entropy when ablated, and (3) part of this influence is driven by a mechanism involving negative gate values (x_gate < 0), which were previously assumed unimportant for model functionality. The paper also introduces conditional ablation as a methodological contribution.

## Strengths

- **Cross-model consistency of the strengthening-then-weakening pattern.** The median cos(w_in, w_out) across layers follows the same trajectory in all 12 models studied (Figure 1a, Figure 40)—positive in early-middle layers, crossing to negative in late layers. This is a novel, clean empirical finding obtained with a simple weight-only method, demonstrated across OLMo, Llama, Gemma, Mistral, Qwen, and Yi families.

- **Ablation evidence that a small neuron class has outsized influence.** Zero-ablating only 243 weakening neurons (out of tens of thousands) produces large, asymmetric effects on attribute rate and output entropy, while ablating the same number of random neurons from the same layers has negligible effect (Figure 3a,b). Other RW classes (conditional strengthening, conditional weakening, proportional change) show no comparable impact, establishing that this class is functionally distinct.

- **Conditional ablation as a methodological contribution.** The paper introduces a technique to ablate only activations satisfying specific sign conditions on x_gate and x_in, enabling attribution of neuron effects to particular activation regimes. This goes beyond standard ablation and is reusable by other interpretability work.

- **First evidence of a mechanism involving negative gate values.** Using conditional ablation, the paper shows that the entropy-sharpening effect of weakening neurons is largely driven by the case x_gate < 0 and x_in < 0 (leading to x_post > 0). This is surprising because negative gate values were widely assumed to be negligible for model functionality beyond training dynamics. The finding is corroborated by a concrete case study (Section 8) and the concurrent citation of Kong et al. (2025) supports the timeliness of this observation.

- **Honest reporting of limitations.** The paper explicitly acknowledges that many neurons are not prototypical (Section 4.2), that the weakening neuron is hard to interpret in its positive-gate regime (Section 8), and that mean ablation produces different results (Appendix F.4).

## Weaknesses

### Fatal
None.

### Major

- **Behavioral (causal) experiments performed on only one model (OLMo-7B).** The weight-based analysis (Section 5) convincingly covers 12 models. However, all ablation experiments (Section 6), entropy analysis, conditional ablation findings, the case study (Section 8), and activation frequency results (Section 7) come from OLMo-7B on its training distribution (Dolma). The paper explicitly acknowledges this ("to save resources, we focus on a single model"), but its central causal claims—that weakening neurons have "outsized influence" and that negative gate values encode functionality—are supported only by single-model evidence. Without replication on at least one additional model (e.g., Llama-3.2-3B, which has similar weight patterns), it is unclear whether these behavioral properties are general or idiosyncratic to OLMo. This substantially limits the generality of the paper's headline claims.

- **Absolute entropy values not reported, making effect magnitudes uninterpretable.** The y-axis of Figure 3(b) shows entropy differences (clean minus ablated) of up to ~10 nats. Without reporting the absolute entropy of the clean model's output distribution, the reader cannot assess whether a 10-nat difference represents a meaningful sharpening or a catastrophic collapse into a degenerate regime. This is a significant evidential gap for a central quantitative claim.

### Minor

- **The "weakening" label is potentially misleading.** The paper's own key finding (Section 6.2) is that the most important behavioral effect of weakening neurons—sharpening the output distribution—is driven by case (iii) where x_gate < 0, in which the neuron "takes on a strengthening behavior" (the negative gate flips the effective sign). The paper concedes that in the positive-gate regime (which is more frequent), weakening neurons are "much harder to interpret" (Section 8). While the naming is geometrically motivated (cos(w_in, w_out) < 0), it creates a persistent dissonance between the label and the mechanism driving the paper's most striking result. A more descriptive geometric term (e.g., "negatively collinear neurons") would better serve clarity.

- **Conditional ablation definitions depend on the preprocessing convention.** The four cases in Section 6.2 (e.g., "gate+_post+") are defined relative to the preprocessed weights (multiplying w_in and w_out by sign(cos(w_gate, w_in))). As the paper notes in Appendix C, without this preprocessing the equivalent conditions would need to reference the sign of cos(w_gate, w_in). While the symmetry argument is valid and the preprocessing does not change model behavior, this dependence means the ablation conditions are not uniquely determined by model parameters alone—they are a joint property of the model and the convention. This is not a fatal flaw but should be more prominently acknowledged.

- **Threshold τ = ±0.5 for classification is arbitrary.** The paper acknowledges that "many cosines will not be close to 0 or ±1" but does not analyze sensitivity of the main conclusions to this threshold. The "atypical" subcategories partially address this, but the core classification into weakening vs. strengthening depends on a single hyperparameter without principled justification. Given the small absolute count of weakening neurons (243 in OLMo-7B), small threshold changes could materially affect the set.

- **Activation frequency finding does not control for confounds.** The strong negative correlation between cos(w_in, w_out) and activation frequency (Table 5, Figure 4) replicates Gurnee et al. (2024)'s finding on gated architectures. However, the paper does not control for layer depth, which independently correlates with both variables (weakening neurons concentrate in late layers, and activation patterns differ by layer). The claim that this "explains" weakening neurons' influence is therefore speculative.

### Trivial

None that survive filtering.

## Nice-to-Haves

- Report absolute entropy values for the clean model alongside ablation differences to make effect magnitudes interpretable.
- Replicate the core ablation experiments (at least for entropy and conditional ablation) on one additional model (e.g., Llama-3.2-3B) to establish generality.
- Consider renaming "weakening" to a geometrically descriptive term (e.g., "negatively collinear") and treating the sign-dependent functional interpretation separately.
- Analyze sensitivity of the neuron taxonomy to the classification threshold τ.

## Removed Points

- **Criticism that the taxonomy depends on an arbitrary sign convention and is not invariant.** REMOVED as factually wrong regarding the primary classification: the weakening/strengthening distinction is based on cos(w_in, w_out), which is invariant under the simultaneous flip of w_in and w_out. The preprocessing only affects scatter plot positioning and the conditional ablation case definitions, which the paper transparently documents. The taxonomy itself (based on cos(w_in, w_out) < -0.5) is unaffected.

- **Criticism that the paper should not be accepted in its current form due to structural issues with taxonomy.** REMOVED as it overstates the severity of the preprocessing concern, which is a transparent convention with a valid symmetry argument.

- **Various formatting and style nitpicks.** Removed per instructions (parser artifacts).

- **Criticism about missing appendix content.** Removed per instructions (parser strips appendix content; it exists in the original submission).

- **Strength Finder's generic/conflicting strengths.** Filtered: strengths that were purely generic ("this paper addressed an important problem") or that conflict with verified weaknesses have been removed or merged into the main strengths above.

## Novel Insights

The reviews surface an interesting tension in the paper between its two contributions. The weight-based cross-model analysis (Section 5) is clean, well-evidenced, and stands independently: the observation that median cos(w_in, w_out) transitions from positive to negative across layers in every model studied is a genuinely robust finding. However, the paper's more ambitious claims about "discovering" weakening neurons as a distinct functional class with a "newly observed mechanism" involving negative gate values rest on a much narrower evidential base (one model, ablation-sensitive, naming-convention-dependent). This creates an asymmetry where the strongest contribution (the geometric cross-model pattern) is underemphasized relative to the weaker one (the functional interpretation). The reviews collectively suggest that the paper would be strengthened by promoting the cross-model geometric finding as its primary contribution and treating the functional claims about weakening neurons as promising but preliminary.

## Suggestions

1. **Run the key ablation experiment (conditional ablation on entropy) on at least one additional model** (e.g., Llama-3.2-3B). This single addition would transform the paper's main limitation into a strength.
2. **Report absolute entropy of the clean model** alongside the ablation differences to make effect sizes interpretable.
3. **Consider re-labeling the taxonomy** with geometrically descriptive terms (e.g., "negatively collinear" for weakening, "positively collinear" for strengthening) and presenting the gate-sign-dependent behavior as a separate finding rather than conflating it with the name.
4. **Analyze sensitivity of the weakening neuron count to the τ = 0.5 threshold** and report how many neurons change class under modest threshold variations.
5. **Control for layer depth** when reporting activation-frequency correlations with cos(w_in, w_out).

---

**Calibration anchors used for scoring:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/pJoSE7Cvj0.md` | 5.00 | Achilles' Heel paper — similar genre (identifying important neuron subsets). That paper had much broader model coverage (21 models) but weaker novelty. Current paper has narrower behavioral validation but cleaner method and more surprising findings. Comparable quality. |
| `/home/wg25r/review_agent/human_reviews_2026/JenMBia97B.md` | 5.50 | Unified neuron interpretation/control — rejected despite good motivation, due to methodological issues with the core framework. Current paper has a cleaner, more defensible method. |
| `/home/wg25r/review_agent/human_reviews_2026/6fmQJGaA8p.md` | 5.00 | MoE MUI paper — rejected despite thorough multi-model analysis, criticized for overclaimed novelty. Current paper is comparably thorough on weight analysis but similarly limited on causal validation. |
| `/home/wg25r/review_agent/human_reviews_2026/0OxJ4mzaHB.md` | 4.00 | Interpretability prediction paper — weaker empirical contribution. Current paper is stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/EbSkBZQF9g.md` | 0.50 | Single-layer knapsack MI — very weak evidence for strong claims. Current paper is substantially stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/tAiQpjAZ0Z.md` | 5.50 | Value-State Gated Attention — withdrawn/rejected. Comparable score range. |
| `/home/wg25r/review_agent/human_reviews_2026/UJ2UUjT2ko.md` | 8.00 | Mixing Mechanisms — strong, well-evidenced mechanistic interpretability. Current paper is weaker on causal generalization. |

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>