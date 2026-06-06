## Summary

This paper introduces a weight-based method for classifying gated MLP neurons in transformers by computing cosine similarities between their weight vectors (w_gate, w_in, w_out). The method yields a taxonomy of "read-write" functionalities and reveals a class of "weakening neurons" (cos(w_in, w_out) ≈ −1) that is universally present in late layers across 12 LLMs and has disproportionate influence on model behavior in OLMo-7B. A complementary contribution is a conditional ablation technique showing that negative gate values — previously considered a training-dynamics artifact — play a genuine mechanistic role.

---

## Strengths

1. **Novel weight-based taxonomy with principled baselines**: Table 1 defines six prototypical RW classes from the three pairwise cosine similarities of neuron weight vectors. Figure 2 validates the taxonomy against a 95% randomness boundary (two variants), demonstrating that the identified clusters are non-random, not artifacts of chance alignment.

2. **Robust cross-model structural universality**: Figure 1(a) shows the median cos(w_in, w_out) turning from positive to negative in late layers for all nine models plotted (2B–9B, across OLMo, Llama, Gemma, Mistral, Qwen, Yi families), with the pattern also verified in Figure 1(b) and Appendix J across 12 models total. The consistency is striking given the diversity of architectures and training data.

3. **Ablation experiments demonstrating outsized functional influence**: Figure 3(a) shows a clear drop in attribute rate from layer ~10 onward when 243 weakening neurons are zero-ablated, while ablating 243 randomly sampled neurons from the same layers leaves the curve unchanged. Figure 3(b) shows that weakening neurons sharpen the output distribution (entropy(clean) − entropy(ablated) >> 0 in ~10^6 predictions), which is surprising and would not be predicted from their minority status.

4. **Novel conditional ablation isolates negative-gate-value mechanism**: By conditioning ablations on the signs of x_gate and x_in, Section 6.2 shows that case (iii) (x_gate < 0, x_in < 0) produces entropy effects similar to ablating all weakening neurons — despite negative gate activations being relatively rare among weakening neurons. This is a methodological contribution independent of the taxonomy itself, and the finding that Swish is not reducible to ReLU for mechanistic purposes is a genuine new insight.

5. **Case study anchors the negative-gate finding at the neuron level**: Section 8 connects the aggregate conditional-ablation result to individual neuron behavior: neuron 31.9634's most interpretable activations occur exactly in the x_gate < 0 regime (token "once" in "once again"), echoing the aggregate finding and providing a mechanistic account of the "surprising" sharpening effect.

6. **Use of publicly available training data**: OLMo-7B experiments use Dolma as the dataset, enabling exact replication of the distribution on which ablation effects are measured.

---

## Weaknesses

### Fatal
None.

### Major

- **Activation frequency as an uncontrolled confound in the ablation comparison** — Section 7 establishes a strong negative correlation (r ≈ −0.97 in layer 15) between cos(w_in, w_out) and activation frequency: weakening neurons fire very often. The baseline in Figure 3 consists of randomly sampled neurons from the same *layers*, but these likely have substantially lower activation frequencies than the weakening neurons. If so, part of the outsized effect of ablating weakening neurons could be explained by their higher activation frequency rather than their RW class specifically. The paper notes (Section 7) that frequency "does not fully explain their effect" because the negative-gate activation finding cannot be frequency-driven (negative gate activations are *rare* among weakening neurons), which is a partial rebuttal. However, the positive-gate regime ablation effect (Figure 3a, attribute rate) is not similarly insulated from the frequency confound, and the paper does not perform a frequency-matched control or even report the frequency distribution of the baseline neurons. A frequency-matched ablation experiment — or at minimum an explicit acknowledgment of this limitation — is needed to support the headline claim that RW class (not activation frequency) is the driver.

- **Functional universality claimed but demonstrated for only one model** — The abstract states weakening neurons "have a large influence on model behavior" as a general property, and Section 5 frames the cross-model structural pattern as a universal organizing principle. Yet the functional influence (attribute rate, entropy sharpening, conditional ablations) is demonstrated exclusively on OLMo-7B (Section 6). These are distinct claims: structural ubiquity does not entail functional universality. The paper would need ablation experiments on at least one additional model (e.g., Llama-3.2-3B, which is already analyzed structurally) before the abstract's framing is fully warranted.

### Minor

- **Early-layer effect of late-layer neurons is left unexplained** — Figure 3(a) shows that ablating 243 mostly late-layer weakening neurons depresses attribute rate from layer ~10 onward, even though "there are very few weakening neurons in these early-middle layers" (paper's own words). The paper correctly identifies this as "particularly interesting" but offers no mechanism. This is one of the most intriguing findings in the paper and deserves at least a brief mechanistic hypothesis (e.g., the few early-layer weakening neurons are individually powerful, or the effect propagates through residual stream influence on attention).

- **Section 6.3 uses the single most extreme case study** — The case study of entropy reduction is explicitly drawn from "the text example where the entropy reduction was most extreme" among 20M tokens. The paper does not contextualize this (e.g., noting how unusual this case is relative to the distribution of effects) or caution the reader that the mechanism illustrated there may not represent typical weakening-neuron behavior.

- **Lack of quantitative decomposition of case-iii contribution** — The paper says "a large part of the sharpening effect" is due to case (iii), supported by the visual comparison of histograms in Figure 3(b). However, the paper does not report what fraction of total entropy-reduction events are attributable to case (iii) versus cases (i)/(ii)/(iv), nor the proportion of activations that fall into the negative-gate regime. A quantitative statement (e.g., "X% of total entropy reduction from case iii, which represents Y% of activations") would significantly strengthen this novel finding.

### Trivial
None.

---

## Nice-to-Haves

- A frequency-matched ablation (sampling baseline neurons by activation frequency rather than layer) would cleanly separate the RW-class effect from the frequency effect in the positive-gate regime, strengthening the paper on its own terms.
- Even a lightweight ablation on one additional model (e.g., Llama-3.2-3B attribute rate) would provide cross-model evidence for functional universality, not just structural universality.
- A brief intuition for the weight preprocessing step (Section 3.2) in the main text — not just deferred to Appendix C — would help readers understand why the sign flip is the "right" normalization before the taxonomy is applied.
- A systematic quantitative analysis across multiple weakening neurons in Section 8 (e.g., descriptive statistics on the proportion with interpretable x_gate < 0 activations) would bolster the claim that the case study is representative.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh critic: "Histograms in Figure 3(b) are all centered around 0, undermining the conditional ablation claim."** — The figure description cited is a PDF parser artifact. The paper's caption explicitly states "weakening neurons decrease the entropy by about 10 nats, whereas they increase it much more rarely," and the text confirms case (iii) produces effects similar to the full weakening ablation. There is a direct conflict between the automated description and the paper's text; per the rules, parser artifacts are not author errors. Removed.

- **Harsh critic: "Rationale for preprocessing step should appear in the main text; Appendix C is absent."** — The appendix is stripped by the parser; it exists in the original submission. The paper explicitly says "See section C for our argument." Removed as a complaint about missing appendix content.

- **Harsh critic: "Two case studies are insufficient; the analysis of neuron 31.9634 shows only complex behavior."** — The paper analyzes two neurons in the main text and notes more in Appendix I. The claim about complexity being "due to the nature of weakening" is at least partially grounded in the broader finding (Section 6.2) that the gate < 0 regime is mechanistically important — neuron 31.9634's most interpretable activations come from exactly this regime. The paper does not overstate this single neuron as representative of all weakening neurons. Downgraded to minor nice-to-have.

- **Strength Finder: "Use of publicly available training data enhances reproducibility over closed data."** — While technically accurate, this is a fairly generic strength about data availability, not a property specific to the scientific contribution. Retained but not featured prominently.

---

## Novel Insights

The most genuinely novel insight synthesized from the reviews and paper is the following: the weight-based RW taxonomy, when combined with conditional ablation, reveals that a disproportionate share of weakening neurons' functional influence comes from the *negative* gate-value regime — a regime that fires rarely but, when it fires, inverts the neuron's nominal weakening behavior into effective strengthening. This is counter-intuitive on two levels: (1) negative Swish values were expected to be near-zero and functionally inert; (2) the activations responsible for the surprising entropy-sharpening effect are the *least frequent* activation type of these already-small-count neurons. The structural universality finding (strengthening → weakening across layers) combined with this functional inversion under negative gates opens a research question about whether gated architectures deliberately develop this inversion as a late-layer specialization.

---

## Suggestions

1. Run an activation-frequency-matched ablation baseline for the attribute rate experiment: sample baseline neurons with the same empirical frequency distribution as weakening neurons. If weakening neurons still dominate the effect, the RW-class interpretation is clean.
2. Replicate the attribute rate ablation on Llama-3.2-3B (or any model with a publicly documented evaluation setup) to demonstrate cross-model functional universality, even at a lightweight level.
3. In Section 6.3, explicitly state that the case study was selected as the maximum-effect example and provide a brief characterization of the broader distribution (e.g., "this is the 99th percentile of case-iii entropy reductions across 20M tokens").
4. Add a quantitative breakdown of the case-iii contribution to total entropy reduction in Section 6.2.
5. Add a 1–2 sentence intuition for the preprocessing step (Section 3.2) in the main text so readers can follow the taxonomy immediately without turning to the appendix.
6. In Section 6.1, offer a brief mechanistic hypothesis for the early-layer effect — even a speculative one — since it is one of the most intriguing empirical results in the paper.

---

## Evaluation on Key Axes

**Originality**: High. The RW taxonomy for gated neurons is new, the conditional ablation technique is new, and the negative-gate-value finding is novel (the paper correctly notes concurrent but independent work on a different aspect of this phenomenon by Kong et al., 2025).

**Importance of research question**: High. Understanding how gated activation functions create functional neuron classes directly addresses a gap in mechanistic interpretability as gated LLMs have become dominant.

**Claims supported**: Moderate-to-high for structural claims (universal across 12 models); moderate for functional claims (single-model, frequency confound unaddressed). The negative-gate finding is compelling but lacks full quantitative support.

**Soundness of experiments**: Mostly sound. The ablation design with same-layer random baselines is appropriate but incomplete (frequency-matching missing). The conditional ablation technique is methodologically clean and novel.

**Clarity of writing**: Good. The paper is well-organized and the RW framework is explained clearly. The connection between individual-neuron analysis and aggregate ablation effects is effectively drawn.

**Value to the research community**: High. The method is simple, transparent, and immediately applicable to any gated LLM. The universal structural finding is directly actionable for future interpretability work.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>