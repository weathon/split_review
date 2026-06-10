Now I have a thorough understanding of the paper and the reviews. Let me produce the consolidated review.

---

## Summary

This paper observes that universal adversarial perturbations (UAPs) cause a measurable drop in layer-wise entropy at deep layers of neural networks, and proposes "Democratic Training"—a defense that fine-tunes models on synthetically generated low-entropy samples (not actual UAPs) to suppress this effect. Evaluated across 7 models, 5 datasets, and 5 UAP attack methods, the method reduces attack success rate from 79.4% to 2.8% while preserving clean accuracy within ~2%, and does so without modifying model architecture or requiring target-class knowledge.

## Strengths

- **Novel empirical finding with clear diagnosis.** Section 3.2 and Figure 2 systematically document that UAPs cause a progressive, deep-layer entropy drop, with clear separation (16.7% on average) at deep layers. This provides a measurable signature of UAP behavior that prior work mostly treats as a black-box phenomenon, and it directly motivates the defense. The analysis is principled, replicable, and a genuine contribution in itself.

- **Attack-agnostic defense with practical advantages.** Unlike methods requiring precomputed UAPs per target class (SFR needs 25+2000 UAPs; methods scaling with class count), Democratic Training generates low-entropy samples without knowing the attack target. Its time complexity O(n·m·|I|) does not depend on the number of classes—a concrete advantage for large-class datasets like ImageNet (1000 classes). The method also requires no architecture modification and repairs a model within 10 minutes versus SFR's >40 min per UAP.

- **Broad and strong quantitative results.** Across 7 neural networks, 5 datasets, and 5 UAP attack methods (DF-UAP, sPGD, LaVAN, GAP, SGA), the attack success rate drops from 79.4%→2.8% on average (Table 2), with all four additional attack methods showing SR below 2.9% (Table 3). Adversarial accuracy improves from 12.6% to 69.3%. This evaluation breadth substantially exceeds most UAP defense papers.

- **Controlled comparison with adversarial training.** RQ3 (Table 4) compares Democratic Training against non-targeted PGD, targeted PGD, and UAP finetuning under matched compute and data budgets—all three baselines keep SR >16%, while Democratic Training achieves SR <3%. This controlled setup rules out the explanation that any fine-tuning with perturbed samples suffices.

## Weaknesses

### Major

- **No evaluation against adaptive attacks.** This is the most significant gap. All UAPs are generated on the *original* model and tested on the *defended* model—a transfer-based evaluation. An attacker aware of Democratic Training could craft UAPs that do not reduce entropy (e.g., by adding an entropy-preservation term to the UAP objective), or find alternative mechanisms to cause misclassification. The paper claims the method is "not limited to specific UAP attacks" (line 137), which implies generality, but without adaptive evaluation this claim is untested. For a defense paper at a top venue, this is a standard expectation (Carlini et al., 2019; Athalye et al., 2018).

### Minor

- **Threat model wording is self-contradictory.** Section 2.4 states: "The defender... cannot interfere with the training process" (line 83), yet the defense goals explicitly say "adjusting the model parameters" (line 82) and the entire method fine-tunes the model. While the intended meaning is clear (the defender did *not train the model from scratch*; it was obtained from a third party), the text as written directly contradicts itself. This needs to be resolved.

- **Entropy measurement lacks theoretical grounding.** The paper applies softmax to hidden-layer pre-activations and computes Shannon entropy (Equation 5), treating neuron activations as probabilities. The "probability" interpretation of softmax is information-theoretically meaningful for the final classification layer, but not for hidden layers. The paper provides *empirical* justification (Section 3.2 shows the measure separates clean from UAP-perturbed samples), but the conceptual foundation is weak. An ablation showing that this specific entropy measure outperforms simpler alternatives (e.g., feature norm, activation magnitude) would substantially strengthen the work.

- **Key hyperparameters not reported.** The paper omits essential details: the number of iterations *m* for the Sample Generator, the perturbation bound ε, the value of α (trade-off parameter in Equation 6), number of fine-tuning epochs, learning rate, and batch size. These are necessary for reproducibility and for understanding the method's sensitivity.

- **Only average results reported, no per-dataset breakdown.** Results are reported as averages across 7 models and 5 datasets (Table 2). It is impossible to assess whether the method works uniformly well or struggles on certain datasets (e.g., ImageNet with 1000 classes vs. CIFAR-10 with 10). The 2% average clean accuracy drop could hide significant variation.

- **Missing ablations on key design choices.** (a) No sensitivity analysis on α—the central trade-off parameter. (b) No ablation on which layer(s) to use for entropy calculation (the paper uses only the last pooling/dense layer; using multiple layers might improve or degrade performance). (c) No test of whether the entropy-based objective is necessary, or whether a simpler perturbation objective would achieve similar results.

- **TRADES baseline hyperparameters not discussed.** TRADES (Table 4, last row) shows a ~10% clean accuracy drop. The paper does not report whether this could be improved with tuning. A single hyperparameter setting for a strong baseline is potentially misleading.

### Trivial

- No limitations section or discussion of failure cases.

## Nice-to-Haves

- Reporting standard deviations or confidence intervals across target classes and UAP seeds would strengthen the quantitative claims.
- Per-dataset results (especially ImageNet vs. CIFAR-10) would substantially improve interpretability.
- A discussion of potential adaptive attacks as future work would be appropriate.

## Removed Points

The following points from the inputs were filtered out for the stated reasons:

1. **"Core mechanism is underspecified" / "structurally identical to adversarial training"** — The paper clearly distinguishes the objective (entropy minimization vs. classification loss maximization) and the practical advantage (no target class needed, no architecture modification). The critic's framing conflates "generating perturbations" (which any defense method does) with "generating UAPs" (which this method explicitly avoids). The distinction is meaningful and the method is adequately specified (Algorithm 2).

2. **"No theoretical or empirical justification" for entropy** — The paper does provide empirical justification in Section 3.2 (Figure 2 shows clean separation). The statement "no...empirical justification" is factually incorrect. The theoretical grounding is weak, which I retain above as a Minor weakness, but the claim of zero justification is removed.

3. **"Comparison guarantees the proposed method looks better"** (unfair comparison framing) — The paper uses matched compute budget and data amount. The adversarial training baselines are evaluated under their standard formulation. While the comparison could be extended (more UAPs for pretrained finetuning, tuned TRADES), the setup is not deliberately stacked; the asymmetry is discussed transparently.

4. **"Non-targeted focus gap is overstated"** — A minor literature characterization quibble. The paper's claim about existing methods focusing on non-targeted attacks is debatable but not central to the paper's contribution.

5. **"Tables are raster images"** — This is a PDF parsing artifact, not an author error.

6. **Strength: "Favorable comparison against adversarial training"** — Retained but qualified as a strength only under the matched-budget framing. The critic's counterarguments about fairness are partially valid and are reflected in the Minor weaknesses above (TRADES tuning, small UAP set for pretrained finetuning).

## Novel Insights

The most striking observation from the combined reviews is that this paper's central empirical finding—UAPs produce a measurable entropy collapse in deep layers—is simultaneously its strongest contribution and its weakest link. The entropy analysis (Section 3.2) is genuinely novel and visually compelling, but the method builds on treating softmax of hidden activations as a probability distribution, which lacks information-theoretic justification. This creates an unusual situation where the paper's core insight (low entropy → UAP) is clearly demonstrated empirically, but the defense mechanism built on it rests on a conceptually shaky foundation. The paper would be significantly strengthened by decoupling these two contributions: the diagnostic finding stands on its own; the defense needs either a theoretical grounding for the entropy measure or an ablation showing it outperforms simpler alternatives.

## Suggestions

1. **Add adaptive attack evaluation.** This is the single highest-priority addition. Craft UAPs with an entropy-maintenance term in the loss function and test whether Democratic Training remains effective.
2. **Report per-dataset results** (at least for ImageNet and CIFAR-10 separately) to reveal any variation in performance.
3. **Report all hyperparameters** (α, ε, m, epochs, learning rate, batch size) and add an ablation on α over at least 3–4 values.
4. **Resolve the threat model contradiction** by clarifying "cannot interfere with the training process" to mean "cannot retrain the model from scratch" rather than "cannot fine-tune."
5. **Add an ablation replacing the entropy objective** with a simpler alternative (e.g., norm-based perturbation) to verify that entropy is the right signal.
6. **Include a limitations section** acknowledging the lack of theoretical grounding for the entropy measure and the absence of adaptive evaluation.

## Score and Decision

This paper identifies a genuinely interesting empirical phenomenon (entropy collapse under UAPs) and builds a defense that achieves strong results across an impressively broad evaluation. The core idea is novel and the practical advantages (no architecture modification, no target class knowledge, fast repair) are real.

However, the absence of adaptive attack evaluation is a significant gap for a defense paper at a top venue. Combined with the weak theoretical grounding of the central entropy measure, missing hyperparameters for reproducibility, and the unresolved threat model contradiction, the paper is not yet ready for acceptance. With the additions outlined above (especially adaptive attacks and proper ablations), it could become a strong paper.

**Score: 5.0** — Borderline; interesting contribution but requires substantial strengthening to meet top-venue standards.

**Decision: Reject** — In its current form, the weaknesses (particularly the lack of adaptive evaluation) prevent acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>