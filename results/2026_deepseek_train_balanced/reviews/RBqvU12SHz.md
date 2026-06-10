## Summary

This paper applies Shapley Taylor Interaction Indices (STII), an existing method for measuring nonlinear feature interactions, to analyze how model representations reflect underlying data structure across language models (BERT, GPT-2) and a speech model (Wav2Vec 2.0). The core thesis is that interpretability should be grounded in domain-specific knowledge. The strongest evidence comes from the speech analysis, where phonological principles (vowel-formant theory, the sonority/manner-of-articulation hierarchy) yield concrete, testable predictions that the STII measurements confirm. The language experiments study how syntactic distance and multiword expression membership correlate with interaction patterns, controlling for positional confounds.

---

## Strengths

1. **Domain-grounded predictions in speech experiments.** The paper derives specific, falsifiable predictions from established phonetic theory and confirms them with STII measurements. Section 4.1 predicts and confirms higher interaction at consonant-vowel boundaries than consonant-consonant boundaries (Figure 4). Section 4.2 predicts and confirms a gradient of interaction matching the phonological sonority hierarchy from stops to approximants (Figure 5, mapped onto a traditional IPA consonant chart). This goes beyond correlational probing — it genuinely tests domain-derived hypotheses against model representations.

2. **Systematic stratification to control for positional confounds.** Section 3.1 first establishes that STII monotonically decreases with both interacting pair distance and prediction distance (Figure 1). The paper then explicitly stratifies by these distances in all subsequent language analyses (Figures 2 and 3 for syntax and MWEs, respectively), ensuring effects attributed to syntactic distance or MWE membership are not artifacts of trivial positional proximity. This is a stronger methodological control than prior Shapley interaction work on LSTMs.

3. **Extension of Shapley interaction analysis to Transformer LMs with a novel MWE dimension.** Prior work studied Shapley interactions primarily in LSTMs and focused on syntax. This paper extends the analysis to Transformer-based models (GPT-2, BERT) and introduces multiword expressions as a new analytical dimension (Section 3.3, Figure 3). The finding that tokens within idiomatic MWEs exhibit higher STII than arbitrary token pairs — and that this holds across both MLMs and ALMs — connects nonlinear interaction to non-compositionality in a novel way.

4. **Comparative architectural insight.** Section 3.2 (Figure 2) reveals that MLMs exhibit both positive and negative correlations between syntactic distance and STII, while ALMs show only negative correlations. This provides evidence that the two architectures handle syntactic structure differently, going beyond a surface-level comparison of their training objectives.

5. **Normalization for cross-example comparability.** The paper adapts the STII formulation by scaling the residual by the norm of the full unablated sequence (Eq. 6, line 40–41), making interaction magnitudes comparable across different input sequences. This practical detail strengthens the validity of cross-sample comparisons.

---

## Weaknesses

### Fatal

None.

### Major

1. **Image classifier findings are claimed but no experiments are presented.** The introduction (line 12) lists "distinctions between edges, foreground, and background pixels in image classifiers" as a modality studied. The conclusions (line 200) present specific empirical findings: "pixels on object boundaries interact most with nearby pixels in the object foreground" and "pixels closer to an object boundary are more locally linear." However, the paper body contains no section describing image experiments — no dataset, model, setup, figure, or table. The section headings run from §4 (Speech) directly to §5 (Related Work) without any image experiments section. A reader cannot evaluate these claims. The abstract does not mention images (it covers only language and speech), so the core contribution is not invalidated, but claiming experimental results in the introduction and conclusions without presenting the evidence is a serious omission. The paper must either add the full experimental setup and results or retract all image-related claims.

2. **MWE conclusion directly contradicts the paper's own hypothesis and results.** The paper clearly defines the framing: "The extreme case where there is no Shapley residual would imply perfect compositionality... so our hypothesis is that MWEs have a larger than average residual" (line 104). Higher STII = less compositional. The results confirm this: "STII is higher when the interacting pair is in a MWE" (line 116). Yet the conclusion states: "multiword expressions are handled well compositionally both in MLMs and ALMs" (line 200). This is the opposite of what the evidence shows. The conclusion requires correction to be consistent with the paper's own definitions and evidence.

### Minor

1. **Monte Carlo approximation details are underspecified.** The paper states it approximates Shapley values using Monte Carlo Permutation Sampling (line 43) but does not report the number of samples, the sampling strategy, or any convergence criterion. Since the entire empirical contribution rests on the reliability of these approximations — and the feature spaces are not trivial (20 tokens for language, high-resolution acoustic features for speech) — this omission hinders reproducibility and assessment of estimate quality.

2. **Notation ambiguity in the STII definition.** Equation (4) (line 40) uses $\phi(\emptyset)$ in the numerator and as the normalization denominator. From the standard Shapley definition in Equation (1), $\phi(\emptyset)$ would be zero (the Shapley value of the empty set). However, the paper clearly intends it to represent the value of the full (unablated) input. The surrounding text (line 31: "$\phi(\emptyset) \approx \sum_{i \in S} v(\{i\})$") further confuses the notation. This is not fatal because the formula itself (a standard interaction index) is recognizable, but it should be cleaned up for clarity.

3. **One model per training objective limits generalization.** The paper compares only one MLM (BERT) and one ALM (GPT-2). As the authors acknowledge in the future work section, this design cannot distinguish between properties of the training objective class and idiosyncrasies of the specific architectures. Claims about "MLMs" and "ALMs" as classes (e.g., "ALMs show only negative correlations," "MLMs exhibit both positive and negative") are not supported by the evidence — only claims about BERT and GPT-2 are supported.

4. **Value function inconsistency.** The background section defines the value function $v$ as "the logit outputs of a neural network" (line 25), but the experimental setup (line 54) states "We apply softmax to logit outputs to ensure interactions across examples are comparable." The paper should clarify whether the value function uses logits or probabilities, as this choice affects the interaction measurements.

### Trivial

1. **Parser-mangled bullet list in the introduction.** Lines 14–16 contain orphaned fragments ("1)." and "2).") that appear to be artifacts of a malformed enumerated list. This is a formatting issue but makes the introduction hard to parse.

---

## Nice-to-Haves

- Report effect sizes with confidence intervals for the speech findings (e.g., how much of the variance in STII is explained by phonological features vs. purely positional ones) rather than relying primarily on visual inspection of heatmaps and line plots.
- Discuss cases where the phonological predictions fail (e.g., /w/ as an approximant that is "unusually interpretable in isolation," line 157) more explicitly — are these noise or genuine counterexamples?
- The language section would be stronger if it tested a specific linguistic hypothesis (e.g., about dependency length minimization or another structural prediction) rather than reporting correlations post hoc. The MWE analysis is better in this regard because it tests a specific prediction.

---

## Removed Points

These points were raised but removed after verification against the paper:

- **"The abstract promises image experiments."** The abstract (lines 3–5) mentions only language and speech modalities; image classifiers are not mentioned. Removed: factually incorrect.
- **"Missing related work on Shapley approximations (KernelSHAP, FastSHAP)."** The paper's contribution is not about developing new approximation methods; it uses a standard approach (Castro et al., 2009) and STII (Agarwal et al., 2019). This omission does not weaken the paper. Removed: scope creep.
- **"Alternative interpretation of MLM syntax correlations not considered."** The critic suggested that bidirectional attention could create different interaction patterns. This is a valid alternative hypothesis but not a weakness — the paper cannot test every possible interpretation. Removed: speculative, not a concrete flaw.
- **"Image experiments are a fatal flaw that invalidates core claims."** The abstract does not mention images, and the language and speech analyses stand independently. The missing image section is a serious omission (listed as Major above) but does not invalidate the paper's core contributions. Removed: overclassification of severity.
- **"Speech analysis needs more quantitative comparison."** This is a suggestion for improvement, not a demonstrated weakness. Moved to Nice-to-Haves.
- **The critic cited "line 4" for image classifiers in the abstract — this is incorrect; line 4 contains no such mention.**

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Remove all image classifier claims** from the introduction and conclusions, or add the full experimental section (dataset, model, setup, results, figures) that supports them. There is no middle ground: claiming specific findings without presenting evidence is not acceptable.
2. **Correct the MWE conclusion** to be consistent with the paper's own definitions: the results show MWEs are handled *less* compositionally (higher STII), not "well compositionally."
3. **Report the Monte Carlo sample count** used for Shapley approximation in all experiments.
4. **Resolve the notation for $\phi(\emptyset)$** so it is clear whether it represents the full-input value or the empty-set value.
5. **Acknowledge the one-model-per-objective limitation** more directly in the body of the paper rather than deferring it entirely to future work, and qualify claims about "MLMs" and "ALMs" as claims about BERT and GPT-2 specifically.

---

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>