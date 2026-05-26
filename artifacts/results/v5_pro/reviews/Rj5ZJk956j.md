Now I have a thorough understanding of the paper and calibration anchors. Let me write the final review.

---

## Summary

This paper introduces a weight-based method for analyzing the read-write (RW) functionality of gated MLP neurons in transformers, using cosine similarities between gate, input, and output weight vectors. The method reveals a cross-model pattern: early-middle layers are dominated by "strengthening" neurons (whose input and output weights are positively aligned), while late layers contain a small but influential class of "weakening" neurons (negatively aligned). Through ablation experiments on OLMo-7B, the paper shows that weakening neurons disproportionately affect model behavior, and introduces conditional ablation to demonstrate that a significant portion of this effect comes from activations with negative gate values — a previously undocumented functional role for the Swish activation's negative regime.

## Strengths

- **Cross-model validation of the strengthening-to-weakening shift**: Figure 1(a) shows the median of cos(w_in, w_out) across layers for nine different LLMs (Gemma, Llama, OLMo, Mistral, Qwen, Yi), with a consistent pattern: positive in early layers, negative in late layers. This robust, multi-model finding is the paper's strongest empirical contribution and does not depend on the arbitrary classification threshold.

- **Novel weight-based method for neuron classification**: The idea of using cosine similarities among the three weight vectors (gate, input, output) to characterize read-write functionality is simple, principled, and generates testable hypotheses. The taxonomy in Table 1 provides a clear vocabulary for discussing neuron behavior, and the scatter plots in Figure 2 show structured clusters that are genuinely informative.

- **Ablation experiments demonstrate causal influence of weakening neurons**: Ablating all 243 weakening neurons causes a visible drop in attribute rate (Figure 3a) and shifts the entropy distribution (Figure 3b), while ablating random neurons from the same layers has negligible effect. The paper also reports that other RW classes are indistinguishable from the clean baseline. Mean ablation results (referenced in Section 6.1) provide a secondary validation that the effect is not purely an artifact of zeroing.

- **Discovery that weight geometry predicts activation frequency**: The strong negative correlation (r = -0.97 in layer 15, Figure 4) between cos(w_in, w_out) and activation frequency connects the static weight-based classification to dynamic neuron behavior, and is consistent with prior findings (Gurnee et al., 2024) extended to gated architectures.

- **Well-structured and clearly written**: The paper follows a logical progression from method → pattern discovery → causal ablation → mechanistic analysis → case study, and the writing is accessible even to readers without deep mechanistic interpretability background.

## Weaknesses

### Fatal

None.

### Major

- **Conditional ablation (Section 6.2) lacks activation magnitude and proportion statistics**: The paper's most ambitious claim — that negative gate values constitute a functionally important mechanism — rests on the conditional ablation experiment showing that the gate-negative/in-negative condition drives most of the entropy-sharpening effect. However, the paper does not report the proportion of activations falling into each of the four sign conditions, nor the total activation magnitude (e.g., L1 mass) removed by each condition. Because Swish outputs for negative inputs are bounded in magnitude (roughly [-0.28, 0)), the direct contribution of these activations to the residual stream can be small. It is therefore impossible to tell whether the observed effect arises because the model genuinely relies on those small negative-gate signals, or simply because zeroing even tiny perturbations degrades a finely balanced computation. The paper acknowledges that negative gate activations are "relatively rare" and "relatively small" but does not provide the quantitative statistics needed to rule out alternative explanations. This is an evidential gap that directly weakens the paper's strongest claim.

- **The neuron classification threshold (±0.5) is arbitrary and its sensitivity is unexplored**: Section 4.2 chooses τ = ±0.5 to map continuous cosine values to discrete RW categories, but provides no motivation for this choice. The discrete categories then drive the ablation experiments (selecting "weakening neurons") and quantitative claims such as "more than 80% of input manipulators belong to conditional strengthening." The consequences of shifting the threshold for the size and composition of the weakening class are not explored. While the paper also presents continuous distributions (Figures 1, 2) that are threshold-independent, the ablation-based claims about weakening neurons specifically depend on which neurons are classified as weakening. A sensitivity analysis or robustness check would substantially strengthen the findings.

### Minor

- **Ablation comparison does not control for per-neuron activation magnitude or layer concentration**: Weakening neurons are concentrated in later layers (Section 5) and activate more frequently (Section 7). The ablation compares all 243 weakening neurons against 243 random neurons from the same layers, but does not control for the total activation mass removed per class. If weakening neurons fire more often or contribute more total activation magnitude, their larger effect could partly reflect that they simply contribute more total signal, rather than being more influential per activation. The paper partially addresses this by noting that activation frequency does not fully explain the effect (since negative-gate activations are also influential), and by reporting mean ablation results. However, a within-class comparison at matched total activation mass would strengthen the "outsize influence" claim.

- **Attribute rate measurement protocol is underspecified in the main text**: The paper states it follows Geva et al. (2023) for attribute rate but does not summarize the key details (e.g., whether the y-axis reflects per-layer probing or the model's final output when cut off at that layer). This makes Figure 3(a) slightly harder to interpret; the interpretation matters because if it is per-layer probing, then late-layer neuron ablations cannot affect early-layer probes, and the "effect from layer ≈10 onward" must come from the few weakening neurons in those earlier layers. A one-sentence clarification would resolve this.

- **The conditional ablation finding would be strengthened by a magnitude-controlled baseline**: The paper uses mean ablation as an alternative to zero ablation, but does not apply a magnitude-controlled baseline to the conditional ablation specifically (e.g., randomizing which activations are zeroed while keeping total L1 mass constant across conditions). Such a control would directly test whether the gate-negative condition is special beyond its magnitude.

### Trivial

- Section 3.2 (weight preprocessing) defers its full justification to Appendix C. A brief one-sentence motivation in the main text would help readers assess whether the preprocessing could systematically affect the cosine distributions.

## Nice-to-Haves

- A sensitivity analysis varying the ±0.5 classification threshold and reporting how the weakening neuron count and ablation results change.
- Reporting the proportion of activations and total L1 mass for each of the four sign conditions in the conditional ablation.
- A magnitude-controlled baseline for the conditional ablation (randomizing which activations are zeroed while preserving total mass per condition).
- Extending the cross-model validation to the ablation experiments, rather than limiting them to a single model (OLMo-7B).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's claim that "the weight-cosine taxonomy uses arbitrary thresholds whose functional significance is not validated" — partially kept but softened**: The core of this criticism (arbitrary threshold, no sensitivity analysis) is valid and retained as a Major weakness. However, the harsh critic's framing that the taxonomy "lacks validation" overstates the issue — the paper validates the taxonomy through the universal pattern finding (Figure 1a, which is threshold-independent), the clustering in Figure 2, and the ablation results showing differential effects across classes. The threshold concern is real but the taxonomy is not unvalidated.

- **Harsh critic's claim that Section 6.3 (entropy reduction case study) is "only loosely connected"**: This is retained only as a characterization, not as a weakness. The paper presents Section 6.3 as a case study, which is inherently exploratory. The connection is acknowledged as loose by the paper itself.

- **Harsh critic's point about Section 7 "complicating the ablation interpretation"**: REMOVED. The paper explicitly addresses this concern by noting that "activation frequencies do not fully explain their effect, since we found that even their negative gate values are influential" (Section 7, line 247). The paper already disentangles these factors.

- **Harsh critic's claim that Section 8 "illustrates the gap between weight-based classification and practical interpretability"**: REMOVED as a weakness. The paper openly acknowledges this limitation in Section 8 ("weakening neuron 31.9634 is much harder to interpret"), and it is a single case study, not a general claim.

- **Harsh critic's point about the preprocessing step (Section 3.2) not being explained in the main text**: DEMOTED to Trivial. Deferring detailed justification to the appendix is standard practice in conference submissions with page limits.

- **Harsh critic's point about Section 4.2 taxonomy not being "derived"**: REMOVED. The taxonomy is presented as prototypical/intuitive cases, which is appropriate for a conceptual framework. The paper explicitly notes the limitations (line 129: "These prototypical classes are limited in scope: Many cosines will not be close to 0 or ±1") and provides continuous alternatives.

- **Harsh critic's claim about the abstract being "premature"**: REMOVED. This is an assessment, not a specific weakness grounded in the paper text.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Add magnitude statistics to the conditional ablation**: Report (1) the proportion of activations in each of the four sign conditions, (2) the total L1 or L2 mass removed under each condition, and (3) ideally a control where activations are randomly zeroed while preserving the total mass per condition. This would transform the negative-gate finding from a suggestive pattern into a causally grounded result.

- **Add a sensitivity analysis for the classification threshold**: Show how the count of weakening neurons and the ablation results change as τ varies from, e.g., 0.3 to 0.7. If the findings are robust to threshold choice, this strengthens the paper. If they are sensitive, the paper should report the sensitivity and discuss its implications.

- **Clarify the attribute rate measurement in the main text**: Add a sentence explaining whether Figure 3(a) shows per-layer probing (tuned lens style) or the model's output when the forward pass is cut off at that layer.

- **Provide a one-sentence summary of the weight preprocessing justification in Section 3.2**: Even something like "We flip the signs of w_in and w_out to ensure cos(w_gate, w_in) ≥ 0, which simplifies the taxonomy without changing model behavior (see Appendix C)."

- **Consider extending ablation experiments to at least one additional model** to demonstrate that the weakening neuron effect is not specific to OLMo-7B, which would leverage the paper's cross-model strength.

---

## Score and Decision

### Anchor comparison

All anchors retrieved across both rounds:

| Anchor | Score | Round | Source | Comparison |
|--------|-------|-------|--------|------------|
| Tnd3dZxyEv | 2.83 | R1 | topic-low | Clearly worse: narrow MLP initialization method, no interpretability findings |
| puGvShnqeA | 3.00 | R1 | topic-low | Clearly worse: limited scope, no cross-model validation |
| fSbPwHjdDG | 3.00 | R1 | topic-low | Worse: single-model causal intervention, narrower findings |
| NSBP7HzA5Z | 3.00 | R1 | topic-low | Worse: proposal-level, no empirical validation |
| dDLGZTKZYZ | 3.75 | R1 | topic-mid | Similar tier: mechanistic analysis of MLPs but narrower scope and weaker evidence |
| CN2bmVVpOh | 4.33 | R1/R2 | topic-mid | Comparable: interesting gating findings but limited to toy tasks and small models; our paper has stronger cross-model validation but similar methodological gaps |
| nUGFpDCu3W | 4.00 | R1 | topic-mid | Our paper is stronger: broader scope, cross-model, causal ablation; nUGFpDCu3W is a single-model case study on short sequences |
| rfSfDSFrRL | 5.50 | R1 | topic-mid | Slightly stronger: cleaner methodology (reverse-engineering trained RNNs), but narrower domain |
| y3CdSwREZl | 4.80 | R1/R2 | weakness-abl | Comparable: neuron class discovery with ablation but weaker cross-model evidence |
| SMYEApLhyx | 5.67 | R1/R2 | weakness-abl | Slightly stronger: more thorough ablation controls (magnitude-aware), but vision domain, single architecture |
| 8sKcAWOf2D | 5.67 | R2 | narrow | Comparable quality: good circuit analysis but single-model; our paper has broader scope but weaker controls |
| cif0JVXJ3b | 5.25 | R2 | narrow | Comparable: knowledge neuron analysis with some methodological concerns |
| f6r1mYwM1g | 5.75 | R1/R2 | weakness-abl | Slightly stronger: cleaner localization experiments |
| EytBpUGB1Z | 8.00 | R1 | topic-high | Clearly stronger: extremely thorough methodology, strong causal evidence, multi-model, well-defined properties |
| STUGfUz8ob | 7.60 | R1 | topic-high | Clearly stronger: theoretical + empirical, clean methodology |
| RBqvU12SHz | 3.25 | R1 | weakness-cond | Worse: more fundamental methodological issues |
| fdvSCcB7i8 | 3.00 | R1 | weakness-cond | Worse: limited scope and evaluation |

**Round 1 bracket: 4.0 – 6.5**

The paper sits above the low-band anchors (2.83–3.00, which had fundamental scope or evaluation problems) and well below the high-band anchors (7.60–8.00, which had extremely thorough methodology and unambiguous causal evidence). Within the mid-band, it is comparable to CN2bmVVpOh (4.33) and y3CdSwREZl (4.80) in terms of methodological gaps, but stronger in cross-model scope. It is somewhat weaker than SMYEApLhyx (5.67) in terms of ablation controls.

**What did the low-band anchors fail at, and does the paper under review share any of those failures?** The low-band anchors (Tnd3dZxyEv, puGvShnqeA, fSbPwHjdDG, NSBP7HzA5Z) all failed at providing strong empirical evidence for their central claims — either through narrow scope, insufficient evaluation, or lack of causal experiments. The paper under review does NOT share these failures: it provides cross-model validation, causal ablation experiments, and multiple complementary analyses (weight geometry, activation frequency, case studies). However, the weakness-anchored hits (RBqvU12SHz at 3.25, fdvSCcB7i8 at 3.00) highlight that papers with incomplete methodological controls in ablation/attribution analyses score low. Our paper has related gaps (missing magnitude controls in conditional ablation) but compensates with stronger overall scope and the mean ablation alternative. The paper's score must reflect these gaps, but it is clearly above the 3.0–3.5 band because its core pattern-finding claims are independently supported by continuous metrics and cross-model evidence.

**Final score: 5.0**. The paper makes a genuine contribution — the universal strengthening-to-weakening pattern across models and the weight-based method are valuable. The ablation evidence for weakening neurons' outsized influence is suggestive and directionally convincing. However, two Major weaknesses (missing magnitude controls in the conditional ablation, arbitrary classification threshold without sensitivity analysis) mean the paper's strongest claim — that negative gate values constitute a previously unseen functional mechanism — is not yet conclusively established. These gaps are addressable with targeted additional experiments, which is why the score sits in the middle of the bracket rather than at the bottom. The paper is a borderline case: interesting and novel enough to merit attention, but lacking the methodological rigor its strongest conclusions require.

**Decision: Reject**. While the paper has clear merit, the Major weaknesses mean the central claim about negative gate mechanisms is insufficiently supported in its current form. The authors could realistically address these gaps with additional experiments (magnitude statistics, threshold sensitivity), which would substantially strengthen the paper.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>