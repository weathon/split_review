Here is my final consolidated review.

---

## Summary

This paper introduces a controlled experimental framework using formal grammars (random and hierarchical) to disentangle two modes of learning in LLMs: learning by rote (memorization) and learning with understanding (generalization). By training models (Pythia-1B, Llama3-8B, Mistral-Nemo-12B) on small datasets of grammar-generated strings and tracking train/test loss divergence, the authors make several empirical observations: (1) memorization and generalization phases overlap but eventually become adversarial, (2) training-set-only metrics cannot determine whether recollection is due to memorization or generalization, and (3) lower-entropy distributions are easier to generalize to but harder to memorize, while higher-entropy distributions show the opposite pattern.

---

## Strengths

- **Novel experimental framework using formal grammars to isolate memorization from generalization.** By generating training data from probabilistic formal grammars (random and hierarchical), the paper creates a "laboratory" setting where the underlying data distribution is exactly known and test data from the same distribution can be generated. This is a genuine methodological advance over work in natural language where the true distribution is unknown, and it enables clean measurement of the test–train loss gap. (Sections 1–2; Figures 1–2)

- **Clean demonstration that training loss alone cannot diagnose memorization.** Figure 3 shows two models (different training set sizes) achieving identical training loss (~0.6 for Pythia-1B) while one is still generalizing (test loss ~0.6, n=64) and the other has entered the memorization phase (test loss ~0.8, n=8). This is a concrete counterexample to the intuition that recollection accuracy on training data suffices to measure memorization. (Section 3.2, Figure 3)

- **Discovery that entropy governs the trade-off between generalization and memorization ease.** Across three model families and two grammar types, with three different methods of manipulating entropy (alphabet size reduction, token oversampling, production rule skewing), the paper consistently finds that lower-entropy distributions are easier to generalize to but harder to memorize, and vice versa. The consistency across the three control methods strengthens the finding. (Section 5, Figure 5)

- **Identification of an asymmetric forgetting dynamic in sequential memorization.** When models are trained on a second dataset from the same distribution after memorizing the first, they briefly re-generalize to both datasets before forgetting the first. This is a non-obvious observation about how memorized information is overwritten. (Section 4, Figure 4)

- **Consistency across diverse model families and scales.** The observed dynamics hold for Pythia-1B, Llama3-8B, and Mistral-Nemo-12B across both grammar types, supporting the generality of the conclusions. (Figures 2, 4, 5)

---

## Weaknesses

### Fatal
None.

### Major

- **The proposed memorization measure (1 − Loss(train)/Loss(test)) is presented without validation.** The paper proposes this ratio as a candidate memorization metric (line 109) but provides no evaluation of whether it correlates with any ground-truth behavior (e.g., actual verbatim string extraction, token-level recall analysis, or comparison with existing measures). Without validation, the measure remains an ad hoc heuristic. The paper acknowledges practical challenges (line 116) but does not address the more basic question of what this ratio means empirically.

- **The core definition equating "learning by rote" with test–train loss divergence is reasonable but unverified against mechanistic evidence.** The paper defines memorization onset as the epoch where test loss > 1.05× training loss (line 83). While a natural operationalization, there is no evidence that this threshold corresponds to actual rote recall (e.g., the model outputting training-specific n-grams rather than distribution-typical completions). The paper does not present token-level case studies or extraction experiments to verify that the "memorization phase" involves different token-generation mechanisms than the "generalization phase." The internal behavior remains a black box.

### Minor

- **The claim that prior work "erred" (line 33) is overstated and the characterization of existing measures is reductive.** The paper states that prior work (Carlini et al., Tirumala et al., Biderman et al.) "use the recollection accuracy of tokens" to define memorization (line 97) and that they "erred by failing to distinguish cleanly between the two types of learning" (line 33). Carlini et al.'s extraction measure, for instance, evaluates whether a model can generate 50 consecutive correct tokens given a variable-length prefix — this is more nuanced than the paper's characterization. The core point (that training-set-only metrics cannot distinguish memorization from generalization) is valid, and Figure 3 cleanly illustrates this, but the paper's framing of prior work is unnecessarily dismissive and oversimplifies a body of work that uses varying methodologies.

- **The sequential memorization experiment (Section 4) demonstrates a phenomenon related to well-known catastrophic forgetting dynamics.** While the observation that models briefly re-generalize before forgetting is a novel nuance, the core finding — that training on new data erases previously learned information — has extensive precedent in the continual learning and catastrophic forgetting literature. The paper does not engage with this literature or explain how its findings go beyond what is already known about catastrophic interference in neural networks.

- **The entropy experiments, while using multiple controls, do not fully isolate entropy from confounded factors.** The three manipulation methods (alphabet size reduction, token oversampling, production rule skewing) show consistent results, which is good. However, changing the alphabet size from ℓ=26 to ℓ=2 also changes the minimum achievable loss and the output space complexity, making it hard to attribute effects solely to "entropy" as an abstract property. The oversampling control (same ℓ=26, lower entropy via non-uniformity) partially addresses this, but the paper does not show whether the quantitative magnitude of the effect is the same across manipulation types at matched entropy levels, nor does it report a control like relative improvement over a random-guessing baseline.

- **The artificial regime (8–64 training strings of length ~64–72, entire dataset in one batch) limits claims about transferability to natural language.** The paper acknowledges this in the limitations section (line 159) but repeatedly asserts that findings "should also apply to natural language data" (line 24) without any supporting evidence or argument beyond wishful extrapolation. The observed dynamics may well be artifacts of the extreme small-data, full-memorization regime.

### Trivial
None.

---

## Nice-to-Haves

- A token-level analysis showing examples where the model generates training tokens via different mechanisms (e.g., high confidence from grammar context vs. high confidence due to rote recall of a specific training string) would significantly strengthen the claim that test–train divergence truly indicates a different mode of learning.
- A small-scale natural language experiment (e.g., fine-tuning on a set of sentences with a controlled syntactic template) to test whether similar dynamics emerge outside the grammar setting.

---

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Criticism that the paper's framing is "overblown" and findings are "well-known."** — This is a subjective assessment of presentation style, not a factual weakness. The paper's findings about entropy's opposing effects on generalization vs. memorization and the re-generalization dynamic are not trivial.
2. **Criticism that the impossibility argument is "trivial."** — While the characterization of prior work is reductive (retained above as a minor weakness), the core demonstration (Figure 3) is a non-trivial illustration of a real problem with training-set-only metrics.
3. **Criticism that test loss can increase due to "overfitting to idiosyncratic sampling noise" rather than rote memorization.** — In this controlled formal grammar setting where the test set is from the same distribution, fitting noise in the training set IS the memorization phenomenon the paper is studying. The random-string baseline (Figure 1) already demonstrates that the model learns the grammar distribution. This criticism conflates overfitting with a different notion of "rote learning" than the paper's definition.
4. **Criticism about missing experiments with natural language or missing related works.** — The limitations are openly acknowledged, and the paper is appropriately scoped as a controlled study. Demanding natural language experiments is scope creep.
5. **Criticism about missing appendix content.** — The parser strips these sections; they exist in the original submission.
6. **Formatting/style nitpicks and complaints about "overblown" language.** — Subjective and do not affect the paper's technical contribution.
7. **Claim that the entropy manipulation methods are "not equivalent" and the grouping is an "oversimplification."** — The paper explicitly uses three different methods, including a control (oversampling at ℓ=26) that holds the output space fixed. The consistency across methods is a strength, not a weakness.

---

## Novel Insights

None beyond the paper's own contributions. The reviewers' comments do not surface a new angle that the paper itself does not already present or that significantly reframes the contribution.

---

## Suggestions

1. **Validate the memorization measure** against a concrete behavioral ground truth — e.g., show that the 1 − Loss(train)/Loss(test) metric correlates with the model's ability to reproduce training-specific n-grams that do not appear in test data. This would transform the measure from a heuristic into a validated tool.
2. **Tone down the characterization of prior work.** The paper's core point (training-loss-only measures are insufficient) does not require claiming prior work "erred." A more precise framing — "prior measures answer a different question; they do not distinguish memorization from generalization, which requires contrasting train and test performance" — is both more accurate and more constructive.
3. **Add a relative-improvement-over-baseline control for the entropy experiments** (e.g., normalize by the cross-entropy of the true distribution or a random-guess baseline) to show that the entropy effect is not driven purely by changes in the minimum achievable loss.
4. **Include a small illustrative natural-language experiment** to probe whether the same train/test divergence dynamics appear outside synthetic grammars, even if only as a proof-of-concept in the Appendix.

---

## Score and Decision

The paper makes a genuine contribution through its clean experimental framework and several carefully documented empirical findings. The weaknesses are real but addressable — the core methodology is sound, the results are consistent across architectures, and the entropy finding is genuinely interesting. The paper would be strengthened by validating its proposed measure, toning down claims about prior work, and adding a minimal bridge to natural language. However, in its current form, the paper's contribution is meaningful enough for publication.

**Originality:** Good — the formal grammar framework is a novel methodological contribution.  
**Importance of question:** High — understanding memorization vs. generalization is a central concern for LLM privacy, copyright, and capabilities.  
**Claims supported:** Partially — the main empirical claims are supported, but the stronger claims about prior work are overstated, and the proposed measure is unvalidated.  
**Soundness:** Solid for the empirical observations; weaker for the proposed measure and the attack on prior work.  
**Clarity:** Generally clear, though some claims are presented more strongly than the evidence warrants.  
**Value to community:** Moderate to high — the framework is useful, and the findings can inform future work on measuring memorization in more realistic settings.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>