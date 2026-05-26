Now I have enough information to write the final review. Let me compose it.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
// List only reasonable points. Rank by severity.
// Not every paper has weaknesses at every tier. Leave a tier empty (or write "None") if nothing qualifies.

...

Let me write the comprehensive review now.## Summary

This paper introduces a weight-based method for analyzing gated neurons in transformers: computing cosine similarities between the three weight vectors (w_gate, w_in, w_out) of SwiGLU/GEGLU neurons to characterize their read-write (RW) functionality. Applying this method across 12 LLMs reveals a consistent pattern — early-middle layers are dominated by "conditional strengthening" neurons, while late layers contain a small but influential class of "weakening" neurons (cos(w_in, w_out) < -0.5). Ablation experiments on OLMo-7B suggest that zero-ablating these few weakening neurons has a disproportionately large effect on attribute rate and output entropy, and a conditional ablation analysis indicates that part of this effect is driven by cases where the gate value is negative — a surprising finding since negative gate values in Swish were previously considered relevant only for training dynamics.

---

## Strengths

1. **Novel weight-based method for gated neuron analysis.** Computing cosine similarities between the three weight vectors of gated neurons is a genuinely new approach that goes beyond prior neuron analysis (which focused on activation contexts or output weights alone). The method is validated by showing that many neurons have cosine values significantly outside random baselines (Section 4.3). This is a simple but productive lens for understanding gated activation functions that are used in most recent LLMs.

2. **Cross-model universality of the strengthening-then-weakening pattern.** The paper demonstrates across 12 LLMs (Gemma-2-2B/9B, Llama-2/3 variants, OLMo-1B/7B, Mistral-7B, Qwen2.5-0.5B/7B, Yi-6B) that the median cos(w_in, w_out) starts positive in early layers and ends negative in late layers (Figure 1a). This is a striking observational finding that holds across model families, sizes, and gating variants (SwiGLU and GeGLU).

3. **Discovery that weakening neurons are a small but influential class.** The paper identifies that weakening neurons — despite numbering only a few hundred in a 7B model — have a measurable effect when ablated: zero-ablating all 243 weakening neurons in OLMo-7B produces a clear drop in attribute rate starting from layer ~10 onward, while ablating the same number of random neurons from the same layers produces no effect (Figure 3a). Other RW classes (strengthening, conditional strengthening) show no comparable effect. This finding opens a new direction for understanding MLP layer specialization in late layers.

4. **First observation that negative gate values have mechanistic importance.** The conditional ablation analysis (Section 6.2) shows that the entropy-sharpening effect of weakening neurons is concentrated in the x_gate < 0, x_in < 0 regime (case iii), where the negative gate flips the neuron's behavior into a strengthening-like mode. This is genuinely surprising given the conventional view that negative Swish values matter only for training dynamics, and it demonstrates that Swish is not reducible to ReLU for mechanistic interpretability purposes.

5. **Activation frequency analysis provides converging evidence.** The paper demonstrates an almost linear negative correlation between cos(w_in, w_out) and activation frequency (correlations at least -0.71 in most layers; Figure 4), showing that weakening neurons activate very often while the much more numerous strengthening/conditional strengthening neurons activate rarely. This provides an independent line of evidence consistent with weakening neurons having a large per-neuron impact.

---

## Weaknesses

### Major

1. **Ablation experiments do not control for activation frequency, confounding the "outsize influence" claim.** The paper shows that weakening neurons activate very often (Section 7) and that ablation of weakening neurons produces larger effects than ablating random neurons from the same layers (Section 6.1). However, the random baseline is not matched on activation frequency. Since the paper itself demonstrates a strong negative correlation between cos(w_in, w_out) and activation frequency (Figure 4), weakening neurons are *by construction* the most active neurons. The observed ablation effect could therefore be driven by how often a neuron fires rather than by its RW class. The paper notes that "activation frequencies do not fully explain their effect, since we found that even their negative gate values are influential" (Section 7), but this is an argument, not a controlled experiment. Without a control comparing weakening neurons to other neurons with similar activation rates (if such neurons exist) or a more direct deconfounding analysis, the central claim that weakening *as an RW class* has uniquely large influence is not fully settled. *Evidence: Sections 6.1, 7; Figure 4.*

2. **The conditional ablation analysis lacks quantitative grounding.** The paper asserts that "a large part of the sharpening effect of weakening neurons is due to case (iii)" (Section 6.2) but provides no quantification: what fraction of the total entropy change is attributable to case (iii)? What are the mean entropy changes per condition with error bars? How does the effect size compare across the four conditions? The support is a visual comparison of histograms (Figure 3b) and a single anecdotal example (Section 6.3). Since the claim about negative gate values is presented as a headline contribution ("for the first time, we observe a mechanism involving negative values of the Swish activation function"), the lack of quantitative support is a significant gap. *Evidence: Section 6.2, Figure 3b.*

### Minor

3. **Taxonomy thresholds are untested for robustness.** The RW classification uses a threshold of ±0.5 for cosine similarities (Table 1). The paper acknowledges that "many cosines will not be close to 0 or ±1" (Section 4.2), but the ablation set size and composition depend on this threshold. No robustness check is performed — e.g., varying the threshold to 0.4 or 0.6 and recomputing the ablation effect. Without this, it is unclear whether the results are an artifact of a particular cutoff. *Evidence: Section 4.2, Table 1.*

4. **Ablation experiments are limited to a single model (OLMo-7B).** All activation-based experiments (Sections 6–8) use OLMo-7B on a Dolma subset. The paper explicitly acknowledges this limitation ("to save resources, we focus on a single model") but the "outsize influence" claim would be substantially strengthened by replication on at least one additional model, even a smaller one. The cross-model patterns in Section 5 establish universality only for weight-based patterns, not for the causal influence claims. *Evidence: Section 6, first paragraph.*

5. **No statistical testing for ablation results.** The ablation results (attribute rate, entropy differences) are presented without confidence intervals, significance tests, or standard deviations. The histograms in Figure 3(b) suggest a distributional shift, but a permutation test comparing the mean entropy change under weakening ablation vs. random ablation would provide a quantitative measure of significance. Given the 20M-token dataset, small effects could be statistically significant, and the absence of any testing makes it difficult to assess the reliability of the findings. *Evidence: Section 6.1, Figure 3.*

6. **The "outsize influence" claim depends partly on comparing against other RW classes that are not visible in the main text.** The paper states that results for other neuron classes are "indistinguishable from clean" and references appendix figures 14–16. While the appendix exists in the original submission, the main text lacks any quantitative comparison showing that the effect is unique to weakening neurons beyond a single figure for the random baseline. A table or summary statistic in the main paper would help readers assess this claim without consulting the appendix. *Evidence: Section 6.1.*

### Trivial

7. **The weight preprocessing rationale (multiplying w_in and w_out by the sign of cos(w_gate, w_in)) is deferred to the appendix.** While the main text references Section C, a brief sketch of the reasoning would improve readability. *Evidence: Section 3.2.*

---

## Nice-to-Haves

- **Explore the continuous relationship between cos(w_in, w_out) and ablation effect.** Instead of dichotomizing at ±0.5, plotting the ablation effect as a function of the continuous cosine value could reveal whether the effect is truly concentrated in the extreme negative region or varies smoothly.
- **Investigate whether the magnitude of negative gate values matters.** The conditional ablation only considers sign (x_gate < 0 vs. > 0), but the magnitude of negative gate values could also be relevant. Binning by the absolute value of x_gate would clarify this.
- **Test on a second domain.** The ablation and case study use news-like Dolma text. Testing on code or technical text would assess domain generality.
- **Check robustness to the weight preprocessing step.** While theoretically neutral, confirming that the main ablation results hold without preprocessing would be reassuring.

---

## Removed Points

*These points were flagged by reviewers but are removed or downgraded per the filtering rules. They are listed here for transparency but should be treated with caution.*

- **Missing related works.** Rule: "DO NOT mention missing related works, as you do not have external sources to confirm their existence." The harsh critic's comment about missing related work on attention-head ablation (conditional ablation not being novel) is partially removed — the conditional ablation method is indeed simple, but the paper is transparent about this and the novelty lies in its application to gated neurons, not in the method itself. This is addressed in Minor weakness 6 above.
- **"The paper does not discuss the possibility that observed effects could be partly due to the weight preprocessing step."** This is speculative — the paper states the preprocessing does not change model output. The preprocessing is mathematically neutral, so this concern is not a grounded weakness.
- **"Activation frequency analysis model not stated."** The paper states "We show the most striking result in figure 4" with the caption specifying OLMo-7B-0424-hf. The model is stated in the figure caption. This is a misread.
- **"Missing table summarizing 12 models."** The models are listed in the text of Section 5. A table would be nice-to-have but is not a weakness.
- **"The dataset for ablation is 20M tokens from Dolma, but the paper does not specify whether these are training-domain tokens."** The paper states "a random subset of 20M tokens from Dolma" and notes Dolma is OLMo's training dataset. The domain is adequately specified.

---

## Novel Insights

The reviews surface two observations that go beyond the paper's own contributions. First, the confound between activation frequency and the weakening neuron class (noted by the harsh critic) points to a general challenge in neuron-level interpretability: when a neuron class is defined by a property that correlates with activation statistics, ablation experiments cannot cleanly separate "class identity" from "usage frequency." This is a methodological issue that applies to any neuron-taxonomy work, not just this paper. Second, the conditional ablation method — while simple — has the potential to become a standard tool for gated activation analysis, analogous to how activation patching became standard for attention heads. The paper's specific finding that negative gate values matter mechanistically (not just for training dynamics) is the kind of surprising empirical observation that can reshape how the field thinks about SwiGLU, and it directly challenges the implicit assumption in many interpretability studies that Swish ≈ ReLU for post-training analysis.

---

## Suggestions

1. **Control for activation frequency in ablation.** The most impactful improvement would be to match weakening neurons against non-weakening neurons with similar activation rates from the same layers (e.g., from layers where cosine values are near zero but activation rates are comparable). If the effect persists after this control, the case for weakening as the causal factor is much stronger.
2. **Quantify the conditional ablation results.** Report the mean and standard deviation of entropy change for each condition, and compute the fraction of the total entropy effect attributable to case (iii). A simple decomposition would provide the rigor needed to support the negative-gate claim.
3. **Test threshold robustness.** Vary the ±0.5 threshold and recompute the ablation effect for the resulting set of weakening neurons to show the finding is not an artifact of a particular cutoff.
4. **Add statistical testing.** At minimum, report standard errors or confidence intervals for the ablation effects. A permutation test comparing the weakening ablation to the random baseline would be straightforward and informative.
5. **Replicate ablation on at least one additional model.** Even a smaller model (e.g., Llama-3.2-1B) on a smaller dataset would significantly strengthen the external validity of the "outsize influence" claim.

---

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round & Query | Comparison |
|--------|-----------|---------------|-----------|
| fSbPwHjdDG | 3.00 | R1-topic-low | Weaker — narrower scope, confounded intervention, poorer presentation |
| puGvShnqeA | 3.00 | R1-topic-low | Different topic, not comparable |
| NSBP7HzA5Z | 3.00 | R1-topic-low | Different topic, not comparable |
| 9L9j5bQPIY | 2.50 | R1-topic-low | Different topic, not comparable |
| CN2bmVVpOh | 4.33 | R1-topic-mid | Comparable — similar novelty/scope tradeoff, our paper has broader scope but similar methodological gaps |
| rfSfDSFrRL | 5.50 | R1-topic-mid | Stronger — tighter evidence for core claim |
| wnT8bfJCDx | 6.25 | R1-topic-mid | Stronger — better supported contributions |
| vVxeFSR4fU | 6.50 | R1-topic-mid | Stronger — cleaner analysis |
| Ebt7JgMHv1 | 6.33 | R1-weakness | Stronger — clear problem framing, rigorous |
| B9XP2R9LtG | 5.25 | R1-weakness | Different domain |
| UoGv8d3MMy | 3.00 | R1-weakness | Different domain |
| SMYEApLhyx | 5.67 | R2 | Stronger — more thorough ablation controls |
| y3CdSwREZl | 4.80 | R2 | Comparable — similar methodology for neuron classification |
| f6r1mYwM1g | 5.75 | R2 | Comparable in methodology, different domain |
| rIx1YXVWZb | 5.50 | R2 | Comparable — mixed reviews, some rigor concerns |

**Round 1 bracket:** 4.0–6.0  
**Round 2 narrowing:** The weakness-anchored queries confirm that papers with confounded ablation evidence and qualitative conditional analyses tend to score at the lower end of this bracket. The topic-band mid-range anchors (4.33–5.50) provide the closest comparisons. The paper sits below the 5.50-level anchors (which have tighter evidence) and above the 3.00-level anchors (which have more severe issues). The two retained Major weaknesses — the activation frequency confound and the lack of quantification in conditional ablation — place the paper at 4.5.

**What did the low-band anchors and weakness-anchored hits fail at, and does the paper under review share any of those failures?**  
The low-band anchors (≈3.0) typically failed at providing convincing evidence for central claims, due to either confounded experimental designs or very narrow scope. The paper under review shares the confounded-evidence failure (activation frequency confound), but unlike the low-band papers, it has genuinely novel methodology, broad cross-model observational support, and an interesting mechanistic finding (negative gate values). The weakness-anchored hits show that papers with similar confound issues (e.g., insufficient controls in ablation) tend toward the 4–5 range. The paper's score of 4.5 reflects that it is above "clear reject" territory due to its genuine novelty and well-supported observational findings, but below the threshold where the central causal claims can be considered settled.

**MY FINAL SCORE: <score>4.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**