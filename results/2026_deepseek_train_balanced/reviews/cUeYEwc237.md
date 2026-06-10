Here is the consolidated final review.

---

## Summary

This paper proposes the Intrinsic Feature Representation (IFR) method, which trains extraction models on neural network activations to quantify feature representations, using a raw-input baseline as a control. Applied to a gridworld theory-of-mind task (Standoff), the paper maps computational features to three ToM strategies (non-mindreading, low-mindreading, high-mindreading) and examines how feature representations relate to task accuracy across architectures (MLP, CNN, CLSTM) and training regimes. The core claim is that IFR can discriminate between hypothesized ToM strategies and that model architecture matters more than curriculum for generalization.

## Strengths

- **Raw-input baseline control for IFR (Section 3.2, line 66).** Comparing activation IFR scores against IFR scores computed from raw perceptual inputs provides a cleaner signal than plain probing: when activation IFR exceeds raw-input IFR, this constitutes evidence that the network is performing useful computation toward that feature, not just reflecting information already present in the input. This control addresses a known limitation of standard probing approaches.

- **Theory-grounded feature set enabling strategy discrimination (Sections 4.1–4.2).** The paper maps three psychological theories of ToM (behavior reading, minimal ToM/perception-goal psychology, full-blown ToM) to a set of 10 features with distinct, falsifiable predictions about familiar vs. novel task performance. The empirical results (Figure 2) show that IFR scores differentiate the strategies in a pattern consistent with the theoretical predictions — non-mindreading features generalize robustly across architectures while mindreading features do not. This goes beyond prior computational ToM work that typically tests one strategy at a time.

- **Per-datapoint sufficiency/necessity analysis (Section 5).** The conditional probability metrics P(A|F) and P(¬A|¬F) provide a more fine-grained view of feature–accuracy relationships than aggregate correlation. The finding that b-loc provides the most sufficiency across all models while few features provide both sufficiency and necessity (Section 5.1, line 134) is a non-obvious insight about the compositional nature of ToM reasoning in these models.

- **Multi-factorial design isolating architecture vs. curriculum effects.** The 3 architectures × 3 training stages × 3 random seeds design enables the paper to separate architectural from training effects. The finding that "the training regime has a strong effect on the features represented for familiar tasks, but its effect on novel task features is weak relative to that of model architecture" (Section 6.1, line 146) is a non-trivial result with practical implications.

## Weaknesses

### Major

1. **Task-model accuracy is never reported.** This is the single most consequential omission. The paper investigates IFR scores and their relationship to accuracy (Experiment 3) but never states the actual task accuracy for any model × training condition — not overall accuracy, not broken down by familiar vs. novel, not by training stage. Without knowing whether the CLSTM achieves 95% or 55% accuracy, the IFR results are largely uninterpretable. High IFR for a feature in a model that fails the task tells a completely different story from the same IFR in a high-performing model. The claim that "Models that represent low- and high-mindreading features do perform better on the task overall" (line 146) cannot be verified from the paper as written. The P(A|F) values in Experiment 3 are similarly uninterpretable without base accuracy rates — a model correct on 90% of datapoints will show high P(A|F) for any feature regardless of that feature's relevance.

2. **IFR is presented as a novel method but is standard probing, and the probing literature is uncited.** The abstract states "We introduce a novel method for quantifying feature representation within neural networks." The method — training auxiliary models on internal activations to predict features of interest and using prediction accuracy as a quantification metric — is precisely the probing / diagnostic classifier approach that has been standard practice in neural network interpretability for nearly a decade (Alain & Bengio, 2016; Belinkov, 2022; and a large literature on probing representation models). The paper frames it as more sophisticated than "correlation analysis or mutual information measurements" (line 62), but probing is far more established than those comparisons suggest. This matters because (a) it overstates the paper's contribution, and (b) the paper independently rediscovers well-known methodological issues (e.g., the probing vs. usage distinction, Section 6.2) without drawing on that literature, missing established solutions and controls.

### Minor

3. **No probing validation controls.** The paper acknowledges the overestimation problem — nonlinear extractors may find information the task model does not functionally use (Section 6.2) — but does not run standard control analyses: training extractors on shuffled labels, training on random features that should not be represented, or systematically comparing linear vs. nonlinear probe divergence to bound the issue. These controls are standard practice in the probing literature and would substantially strengthen confidence in the IFR results.

4. **Strategy-to-feature mapping is asserted rather than formally derived.** The paper defines three ToM strategies and assigns features to each based on informal reasoning. For instance, "treat-loc" is assigned as a non-mindreading feature, but tracking treat locations could be part of any strategy. The connection between cognitive theories (simulation theory, theory theory, Section 1.2) and specific computational features is never made explicit — the features are grounded more in what is computationally convenient in the Standoff environment than in a formal mapping from cognitive theory to computational test. The paper frames this as hypothesis testing, which is appropriate, but the derivation could be substantially tightened.

5. **Results are described qualitatively without numerical values.** The text repeatedly uses "much less robust" (line 71), "clear advantage" (line 73), "surprisingly poorly" (line 113), "well" (multiple) without reporting actual IFR scores or accuracy numbers. The figures presumably contain this information, but the text should present key values to support its claims.

6. **No statistical testing.** Claims such as "the training regime effect on novel task features is weak relative to that of model architecture" (line 146) are made qualitatively. With 3 seeds per condition, the paper could report effect sizes or at least variance across seeds, but results are presented as means across extraction-models without clear attribution of variance sources (task-model seed vs. extractor seed).

7. **Architecture comparison confounded by model capacity.** The CLSTM has substantially more parameters (three LSTM layers of 32 units + convolutional layer) than the MLP (two hidden layers of 32 units) or CNN. The paper attributes the CLSTM's advantage to "its ability to handle sequential data" (line 73) without discussing the capacity confound or controlling for parameter count.

8. **No dataset statistics reported.** Total number of trials, class balance, distribution of opponent states, and how the 20% test split is stratified are not provided.

9. **Composition of internal activations for IFR is underspecified.** Section 3.2 says activations "might be sourced from all hidden layers, or any specific hidden layer" without stating which was used for the reported results. "All hidden layers" is ambiguous — activations from different layers have different dimensionalities and would need to be concatenated or otherwise combined.

### Trivial

None.

## Nice-to-Haves

- Compare IFR scores against a model with known, explicit ToM representations (e.g., ToMnet) as an upper-bound calibration.
- Extend to transformer architectures (mentioned as future work in Section 6.4) to test the generality of the architecture-dominates-curriculum finding.

## Removed Points

The following points from the inputs were removed with justification:

- **Broken citation "(?)" in Section 1.2** — Parser formatting artifact, not an author error. Removed per formatting/syle nitpick rule.
- **Table 1 being an image** — The table is an image in the original PDF; text extraction cannot render it. Not an author error. Removed.
- **"CLSTM does not generalize particularly well" vs. "clear advantage" being contradictory** — Re-reading lines 72–73, the sentence says CLSTM does not generalize well *in absolute terms* but has a *relative* advantage over CNN/MLP. Not contradictory. Removed.
- **Complaint about missing explicit ToM baseline (ToMnet) as a comparison** — Scope creep; the paper's stated goal is analysis of standard architectures, not comparison to specialized ToM models. Moved to Nice-to-Haves.
- **Strength Finder's generic claim "this paper addressed an important problem"** — Generic and superficial. Removed.
- **Criticism about "predictions" feature being circular** — The paper explicitly describes this as a "sanity check for the IFR extraction technique" (Section 4.2, line 102). The criticism ignores this acknowledgment. Removed.
- **"No comparison to ToMnet" (from Harsh Critic)** — Same as above; moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report task accuracy immediately.** Add a table showing accuracy for every model architecture × training stage × novelty condition. This is essential context for all other results and is the single most impactful change the authors could make.

2. **Reframe the contribution honestly.** Drop the claim of a "novel method." Acknowledge the probing literature and position IFR as an application of probing with a useful raw-input baseline control. The genuine contribution is the empirical analysis of ToM strategies, not the method itself.

3. **Add probing validation controls.** Train extractors on (a) activations with shuffled labels, (b) random synthetic features that should not be represented, and (c) compare linear vs. nonlinear probe divergence systematically. These are standard practices.

4. **Report numerical IFR values** in the text alongside qualitative descriptions so claims can be quantitatively evaluated.

5. **Clarify which layers contribute to IFR scores** and how multi-layer activations are combined when "all hidden layers" are used.

6. **Add statistical measures** (variance across seeds, effect sizes) to support qualitative claims about architecture vs. curriculum effects.

## Score and Decision

The paper investigates an interesting question with a thoughtfully designed multi-factorial experiment and a theory-grounded feature set. However, the central omission of task-model accuracy — the essential context for interpreting every result — combined with the overclaimed novelty of the method and the lack of probing validation controls, leaves the paper's claims insufficiently supported for a top venue. The core analysis is salvageable with revisions, but in its current form the evidence does not convincingly support the conclusions about ToM strategies or the relative importance of architecture vs. curriculum.

**Score:** 4.5  
**Decision:** Reject

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>