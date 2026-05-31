Now let me write the final consolidated review.

## Summary

The paper introduces a weight-based cosine-similarity method to classify gated neurons in transformers into read-write (RW) functionality types (strengthening, weakening, conditional strengthening, etc.). Applying this to 12 LLMs (different families and sizes), the authors find a universal pattern: early-middle layers are dominated by conditional strengthening neurons while weakening neurons appear mostly in late layers. Through ablation experiments on OLMo-7B, they show that the tiny class of weakening neurons (~0.2% of MLP neurons) has outsized influence on attribute rate and output entropy, and they use a novel conditional ablation method to trace part of this effect to negative gate values—a mechanism previously assumed unimportant for model behavior.

## Strengths

1. **Systematic taxonomy for gated neurons based on weight cosine similarities** (Table 1, Section 4.2): Prior work computed cosine similarities for non-gated neurons but did not interpret them (Gurnee et al., 2024) or only mentioned the idea in a footnote (Elhage et al., 2021). The paper introduces a clear, threshold-based classification specifically for gated activation functions, which is a genuine methodological advance for neuron-level interpretability.

2. **Universal cross-model pattern of strengthening-then-weakening across layers** (Figure 1a, Section 5): The median of cos(w_in, w_out) is positive in early layers and negative in late layers across all nine larger LLMs tested (2B–9B parameters, spanning Llama, OLMo, Gemma, Mistral, Qwen, Yi). This is a striking empirical regularity that holds across different model families, and it is the paper's strongest evidence for generality. The pattern is further confirmed in the fine-grained scatter plots (Figure 2) and class-distribution bar charts (Figure 1b).

3. **Discovery that a small class of weakening neurons has outsized influence** (Figure 3a, Section 6.1): Zero-ablating all 243 weakening neurons (~0.2% of MLP neurons) causes a large, layer-dependent drop in attribute rate that is clearly distinguishable from baseline ablations of random neurons from the same layers. No other RW class shows a comparable effect. This demonstrates that the weight-based taxonomy identifies functionally important neurons that prior output-based or activation-based analyses would not single out.

4. **Conditional ablation revealing that negative gate-value activations drive the functional effect** (Section 6.2, Figure 3b): The paper introduces a conditional ablation variant that ablates only subsets of activations based on the signs of x_gate and x_in. It shows that the entropy-sharpening effect of weakening neurons is largely due to the (x_gate < 0, x_in < 0) case, providing the first evidence that negative Swish values have a substantive functional role in transformer behavior. The finding is accompanied by a concrete case study (the *Omicron* example, Section 6.3) that illustrates the mechanism.

5. **Negative correlation between activation frequency and cos(w_in, w_out)** (Figure 4, Section 7): The paper shows that weakening neurons activate very often while strengthening neurons activate rarely, with correlations ≤ −0.71 in most layers of OLMo-7B. This independently corroborates the outsized influence finding using a different metric and extends Gurnee et al.'s result to gated activation functions.

## Weaknesses

### Major

1. **Generality gap between the most striking mechanistic claims and their supporting evidence**: The ablation experiments that establish that (a) weakening neurons have outsized influence, and (b) negative gate values play a mechanistic role, are performed on a single model (OLMo-7B) with a single dataset (20M tokens from Dolma). The weight-based analysis in Section 5 spans 12 models, but it is purely correlational. The paper's title, abstract, and conclusion frame these as broadly applicable discoveries about transformer architecture ("a newly discovered read-write functionality in transformers with outsize influence"), but the causal/mechanistic evidence comes from one model. The paper does acknowledge the resource-driven choice to focus on one model for ablations, but the rhetoric still overreaches. Strengthening this would require either (a) running ablation experiments on at least one additional model family, or (b) explicitly reframing the paper's scope in the abstract and conclusion.

### Minor

2. **Preprocessing step may affect the taxonomy classification**: Section 3.2 multiplies w_in and w_out by sign(cos(w_gate, w_in)), which the authors argue does not change model behavior. However, cos(w_gate, w_out)—used in the taxonomy of Table 1—is not invariant under this transformation. The classification into strengthening/weakening/etc. could therefore differ under a different sign convention or without the preprocessing. The paper does not show that the main results (layerwise patterns, existence of weakening neurons) are robust to omitting or varying this preprocessing step. This is not fatal because the preprocessing is applied uniformly, but it deserves clarification.

3. **Conditional ablation implementation is underspecified**: Section 6.2 introduces conditional ablation but does not explicitly state in the main text whether it uses zero ablation or mean ablation, nor whether the entire neuron output is zeroed out or only the contribution from the specific activation when the condition is met. The figure caption says the histograms show "entropy(clean) - entropy(ablated)" but does not describe the ablation type for the conditional subplots. While Section 6.1 mentions "zero ablation" and "mean ablation" for the overall ablation, it is unclear which was used for the conditional variant. This makes the method harder to reproduce.

4. **Layer-by-layer correlation data from Section 7 is not provided**: The paper states "correlations are at least −0.71 in all layers except the last two" but only shows the full data for Layer 15 (Figure 4). A table of layer-wise correlations for the activation frequency analysis would be straightforward to include and would allow readers to verify this claim.

### Trivial

5. **Figure 3(b) histograms are difficult to read quantitatively**: The y-axis uses a log scale and the x-axis range is [−10, 10], but most mass appears concentrated near 0. A quantitative measure (e.g., mean entropy change per activation with confidence intervals) would be more informative than histograms alone for the conditional ablation comparisons.

## Nice-to-Haves

- Running the ablation experiments on at least one additional model (e.g., Llama-3.2-3B) would transform the paper's strongest claims from a detailed study of OLMo-7B into genuinely general findings about transformer architecture.
- A direct intervention on the gate value (e.g., clamping x_gate to a positive value when it is naturally negative) could more directly isolate the causal role of negative gate values, complementing the correlation-based conditional ablation analysis.
- Reporting bootstrapped confidence intervals for the entropy differences in Figure 3(b) would improve quantitative rigor.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Missing model evaluation table** (Harsh Critic): The paper explicitly distinguishes between "nine larger models" (Figure 1a) and the full set of 12 models. Three smaller models are mentioned but not plotted in that figure — this is not an omission, as the paper clearly describes what Figure 1a shows.
- **Statistical significance / confidence intervals for ablation results** (Harsh Critic): The results in Figure 3(a) show a clear separation between weakening and baseline; requesting confidence intervals is a nice-to-have improvement, not a genuine weakness.
- **Section 6.3 case study is "entirely qualitative"** (Harsh Critic): The case study is presented as illustrative, which is standard practice in interpretability research. The paper does not claim it as quantitative evidence.
- **"Missing related work" or claims about lack of novelty**: The paper clearly distinguishes its contribution from prior work (Gurnee et al., Elhage et al.) and the taxonomy is a genuine advance.
- **Generic complaints about "missing baselines" that would go beyond standard practice**: The paper includes random-neuron-from-same-layers baselines for all ablation experiments. Requesting additional model families for ablations is a legitimate suggestion but is captured in the Major weakness above.
- **"A proper mechanistic analysis would need to intervene on the gate value"**: This is a valid future direction but is presented by the Harsh Critic as a current flaw; it is moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The synthetic review does not surface any observation about the paper that goes beyond what the authors themselves state. The cross-model consistency of strengthening-then-weakening is the paper's most surprising result, and the reviewers' perspectives confirm its novelty.

## Suggestions

1. Explicitly qualify in the abstract and conclusion that the ablation/mechanistic findings are demonstrated on OLMo-7B, while the weight-based patterns are cross-model, to better match the rhetoric to the evidence.
2. Provide an analysis showing that the taxonomy is robust to omitting the preprocessing step or to randomizing the sign convention, or alternatively explain why the current convention is the natural one.
3. Clarify in the main text whether the conditional ablation uses zero or mean ablation, and whether per-neuron or per-activation ablation.
4. Include a table of layer-by-layer activation-frequency correlation values for the OLMo-7B analysis.

## Calibration Anchors

**Round 1 — Bracketing (all queries parallel):**

| Query / Band | Retrieved Papers | Avg Score | Comparison |
|---|---|---|---|
| mechanistic interpretability of transformer MLP neurons (high_score=3.5) | Knot-Gathering Initialization (2.83), Llamas think in English (3.00), Structural Probing (3.25), Meta-Models for Auto-Interpretability (3.00) | 2.83–3.25 | These papers are substantially weaker — they have less clear contributions, weaker empirical support, or narrower scope. The current paper is clearly above this band. |
| neuron analysis cosine similarity weight interpretability (low=3.5, high=7.5) | DOCS (6.60), Tracing Rep Progression (6.50), Uncovering Self-Emergent Similarity (6.00), Maximal Cosine Pruning (5.00) | 5.00–6.60 | These papers are at a comparable level of rigor. The current paper's contribution is more discovery-oriented than DOCS but its single-model ablation limits it relative to the stronger papers in this band. |
| interpretability analysis gated neurons ablation (low=7.5) | Small-scale proxies (8.00), Sparse Feature Circuits (8.00), Retrieval Head (8.00), When can transformers reason (7.60) | 7.60–8.00 | These papers are clearly stronger — they have more extensive experiments, broader generality, or deeper theoretical grounding. The current paper does not reach this tier. |

**Round 1 Bracket:** 4.5–7.0

**Round 2 — Narrowing:**

| Query / Band | Retrieved Papers | Avg Score | Comparison |
|---|---|---|---|
| ablation study neuron interpretability (low=4.5, high=6.5) | CD-T (6.33), Interpretability Illusions (5.60), Influential Neuron Path Vision (6.00), Fine-tuning Entity Tracking (5.67) | 5.60–6.33 | The current paper is stronger than Entity Tracking (5.67), which was criticized for single-model analysis similar to this paper's ablation limitation but lacks the cross-model weight analysis. Comparable to CD-T (6.33) and Influential Neuron Path (6.00). |
| cosine similarity weight analysis (low=5.5, high=7.5) | DOCS (6.60), Geometry of Tokens (6.00), Tracing Rep (6.50), Induction Heads (6.20) | 6.00–6.60 | The current paper is slightly below DOCS (6.60) because DOCS has cleaner theoretical grounding (proofs of mathematical properties), but above Geometry of Tokens (6.00) because its causal/ablation experiments provide stronger evidence than the purely correlational analysis in that paper. |

**Compared to read-in-full anchors:**
- **DOCS (6.60)**: The current paper's contribution is more discovery-oriented (it finds something new about models) whereas DOCS is metric-focused. The current paper has weaker theoretical grounding but stronger empirical discovery. Slightly weaker overall.
- **CD-T (6.33)**: Both introduce new methods for mechanistic interpretability. CD-T focuses on runtime efficiency for circuit discovery while this paper focuses on neuron classification. Comparable in rigor. Slightly weaker because CD-T's runtime claims are verified across tasks while this paper's strongest claims are on one model.
- **Influential Neuron Path Vision (6.00)**: Both discover neuron-level functional patterns. The current paper is comparable in contribution, with the edge going to the cross-model analysis.
- **Fine-tuning Entity Tracking (5.67)**: Similar single-model limitation for the causal analysis. The current paper is stronger because it also provides multi-model weight-based evidence that the Entity Tracking paper lacks.

## Score and Decision

Based on calibration against these anchors, the paper sits near the upper end of the 5.5–6.5 range but below 6.5. It is stronger than Entity Tracking (5.67) and comparable to Influential Neuron Path (6.00) and CD-T (6.33), but weaker than DOCS (6.60) in theoretical grounding. The paper has a clear methodological contribution, striking empirical findings, and reasonable awareness of its limitations. The main factor preventing a higher score is the single-model basis for the most novel mechanistic claims, which creates a gap relative to the paper's broad framing.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>