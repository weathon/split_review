Now I have enough calibration data. Let me compose the final review.

**Round 1 bracket assessment:** The paper sits between the low-band (< 3.5) and mid-band (3.5-7.5) of mechanistic interpretability papers. The low-band anchors (avg 3.0) share key failure modes: single-model evidence supporting broad claims, uncontrolled ablation confounds, and overclaimed conclusions. The mid-band anchors (4.3-6.5) have stronger methodology or more comprehensive experiments.

**Round 2 narrowing:** The weakness-anchored queries converge around 4.0-5.0. The "Functional segregation of inputs" paper (5.67) shares a structural concern: its classification scheme (positive vs. negative weights) might be an artifact of the softmax layer rather than revealing intrinsic functional segregation — directly analogous to the sign-invariance concern here.

**What low-band anchors failed at:** The 3.0-level papers had (a) conclusions that didn't follow from the experiments due to confounds, (b) single-model evidence for universal claims, and (c) classification schemes whose interpretation was ambiguous. This paper shares (a) and (b) to a meaningful degree. Its main advantage over those low-band anchors is the multi-model weight analysis (12 models for the purely weight-based findings) and the genuinely novel observation about negative gate values.

**Final score: 4.5**

---

## Summary

This paper introduces a weight-based cosine-similarity method for analyzing the read-write functionality of gated neurons (SwiGLU/GeGLU) in transformer LLMs. The authors classify neurons into functional categories (strengthening, weakening, conditional strengthening, etc.) based on cosine similarities between their input, gate, and output weight vectors. Applying this method to 12 LLMs reveals a universal pattern: early-middle layers are dominated by conditional strengthening neurons, while late layers contain more weakening neurons. The paper further demonstrates through ablation experiments that weakening neurons — though few in number — have disproportionately large effects on model behavior, and introduces conditional ablations to show that some of this effect is mediated by negative gate values.

## Strengths

1. **Novel weight-based method for gated neuron analysis.** The paper proposes a simple, purely weight-based approach (cosine similarities of weight vectors) to analyze gated neurons, which complements existing activation-based and output-based methods. The method is architecture-agnostic and reveals structure that would not be visible through either approach alone.

2. **Universal strengthening-to-weakening pattern across 12 LLMs.** Figure 1(a) demonstrates a consistent pattern across models from different families (OLMo, Llama, Gemma, Mistral, Qwen, Yi): the median cos(w_in, w_out) is strongly positive in early layers and becomes slightly negative in late layers. This finding is robust (it is invariant under the paper's preprocessing) and provides genuinely new insight into how gated neurons organize across layers.

3. **First evidence of functional importance of negative gate values.** The conditional ablation experiments (Section 6.2) isolate the effect of activations with x_gate < 0 and x_in < 0 and show that this condition accounts for much of the entropy-sharpening effect of weakening neurons. This is a novel finding that challenges the common assumption that negative Swish values are only relevant for training dynamics.

4. **Conditional ablation as a methodological innovation.** The technique of selectively ablating activations based on sign patterns of x_gate and x_in enables fine-grained attribution that standard ablations cannot provide, and is reusable by the community.

## Weaknesses

### Major

1. **Classification categories depend on an arbitrary sign convention.** The preprocessing (Section 3.2) multiplies w_in and w_out by sign(cos(w_gate, w_in)) to make cos(w_gate, w_in) > 0. This is a valid behavior-preserving transformation. However, the classification into weakening/strengthening/conditional strengthening depends on cos(w_gate, w_out), which *flips sign* under this transformation (because w_out is flipped while w_gate is not). An equally valid convention (e.g., ensuring cos(w_gate, w_in) < 0 by flipping when cos > 0 instead) would reclassify neurons: a neuron labeled "weakening" under one convention could become "atypical weakening" under another, despite identical behavior. The paper does not analyze whether the key patterns (distribution of classes across layers, composition of the weakening class, ablation results) are robust to alternative conventions. This undermines the claim that these categories are *intrinsic properties* of neurons rather than artifacts of a chosen convention. The core finding about cos(w_in, w_out) layer trends (Figure 1a) is unaffected, but the specific "weakening neuron" class as defined is on shaky conceptual ground.

2. **Ablation experiments do not control for activation frequency.** Section 7 shows that weakening neurons activate far more often than other neurons (gate value > 0). The ablation experiments (Section 6) compare weakening neurons to random neurons from the same layers — but random neurons activate far less often, so ablating them removes far fewer activations. The paper mentions mean ablation in the appendix (Section F.4) but the main text's claims of "outsized influence" rely heavily on zero-ablation results, and even mean ablation does not equate the total number of ablated activations. Without a control that matches activation counts (e.g., randomly subselecting weakening neuron activations or artificially increasing the baseline's ablated activations), the observed effect could largely reflect the number of activations removed rather than a special functional role of weakening neurons.

3. **Single-model ablation evidence for universal claims.** The weight-based analysis spans 12 models, but the ablation experiments (the main evidence for the "outsized influence" claim) are performed on only one model (OLMo-7B) with one dataset. While resource constraints are acknowledged, the paper's title and abstract frame the findings as universal ("A Newly Discovered Read-Write Functionality in Transformers with Outsize Influence"), creating a gap between the scope of the claims and the breadth of the causal evidence.

### Minor

1. **Arbitrary classification thresholds.** The ±0.5 thresholds used to map continuous cosine similarities to discrete categories (Table 1) are not justified with sensitivity analysis. The paper could strengthen confidence by showing that the distribution of neurons across layers and the composition of the weakening class are stable across reasonable threshold choices (e.g., ±0.4, ±0.6).

2. **Variation across models understated.** Figure 1(a) shows non-trivial variation across models in the median cos(w_in, w_out) trajectory (e.g., some models near zero in early layers). The text glosses over this variation, treating all models as exhibiting the same pattern.

3. **Small quantitative effect sizes in entropy analysis.** The entropy effects are presented as "about 10 nats over ~10⁶ predictions," which corresponds to an average of 10⁻⁵ nats per prediction. While the direction of the effect (sharpening vs. flattening) is interesting, the practical significance is unclear without reporting mean and variance of the per-prediction entropy difference.

4. **Activation frequency metric is one-sided.** The paper defines activation frequency as the proportion of tokens where gate value > 0, but the conditional ablation results show that negative gate values are functionally important. Including statistics on negative-gate activations would give a more complete picture.

### Trivial

- The paper would benefit from a dedicated limitations section acknowledging the sign-convention issue, single-model ablation, and arbitrary thresholds.

## Nice-to-Haves

- Robustness check of the classification under alternative sign conventions (e.g., making cos(w_gate, w_out) > 0 instead, or using the raw weights without preprocessing).
- Ablation control matching activation counts between weakening and baseline groups.
- Ablation of conditional strengthening neurons with matching activation frequency to distinguish the effect of neuron class from activation rate.
- Even a second model (e.g., Llama-3.2-3B) for ablation experiments would strengthen generalizability.
- Sensitivity analysis of the ±0.5 threshold.

## Removed Points

These points are flagged to be removed; treat them with caution:
- **"Missing related works"** — The rules prohibit mentioning missing related works.
- **"Reproducibility concerns about missing code/hyperparameters"** — Code is promised and these are standard reproducibility details that don't warrant weakness status.
- **"Formatting/style nitpicks"** — Parser artifacts, not author errors.
- **"Criticism about missing appendix content"** — The parser strips appendix content; it exists in the original submission.
- **Harsh Critic's claim about the ablation effect being "very small" (10⁻⁵ nats per prediction)** — This is reframed as a Minor weakness about reporting effect sizes rather than a major flaw.
- **Strength Finder's generic strengths** ("addresses an important problem," "the method is novel," "the area is impactful") — These lack specific artifact anchors in the paper and do not meet the independence/non-conditionality criteria.

## Novel Insights

The harsh reviewer's observation that the sign-invariance problem is structural — not a missing experiment but a flaw in the classification scheme itself — is the most penetrating insight across both inputs. The strength finder correctly identifies that the cos(w_in, w_out) layer-trend pattern (Figure 1a) is the most robust finding because it is invariant under the preprocessing. Together, these suggest the paper's strongest contribution is the RW cosine-similarity *method* and the discovery of the layer-wise cos(w_in, w_out) trend, not the specific "weakening neuron" classification. The conditional ablation method and the negative-gate-value finding are also robust contributions independent of the classification debate.

## Suggestions

1. **Address the sign-invariance issue directly:** Either (a) show that the classification is robust under alternative conventions, (b) redefine the categories in convention-invariant terms (e.g., using only cos(w_in, w_out) or other invariant quantities), or (c) explicitly acknowledge the convention-dependence as a limitation and adjust claims accordingly.

2. **Control for activation frequency in ablation:** Match the number of ablated activations between the weakening and baseline groups (e.g., by subselecting weakening neuron activations to match baseline frequency, or artificially increasing baseline ablation count).

3. **Add a second model to ablation experiments** to support the universality claim for functional results.

4. **Include sensitivity analyses** for the ±0.5 classification threshold and consider continuous representations of the cosine relationships alongside discrete categories.

5. **Report quantitative effect sizes** (mean, variance, Cohen's d or similar) for the entropy ablation results.

## Score and Decision

Based on calibration against human-reviewed anchors:
- Low-band topic anchors (avg 3.0) share the paper's failure modes: uncontrolled confounds in causal experiments, single-model evidence for broad claims, classification schemes with ambiguous interpretation.
- Mid-band topic anchors (4.3-6.5) have more comprehensive experiments or stronger methodological controls.
- The weakness-anchored "Functional segregation of inputs" paper (5.67) shares a structural concern about whether its classification scheme reveals intrinsic properties or methodological artifacts — directly analogous to the sign-invariance issue here.

**What the low-band anchors failed at:** Papers scoring ≤ 3.0 had conclusions that didn't follow from experiments due to confounds, single-model evidence for universal claims, and classification schemes with ambiguous grounding. This paper shares all three to a meaningful degree, though its multi-model weight analysis and the negative-gate-value finding are genuine contributions that lift it above the lowest band.

The two Major weaknesses — sign-convention dependence of the classification and the activation-frequency confound in ablations — are structural problems that undermine the paper's central claims about "weakening neurons as a distinct class with outsized influence." These are not minor gaps but issues that require substantial revision. Score reflects that the paper has valuable components but needs significant strengthening before its core claims are well-supported.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>