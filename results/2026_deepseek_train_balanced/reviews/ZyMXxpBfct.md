Here is my final consolidated review.

---

## Summary

This paper proposes "Forward Explanation," a conceptual framework that re-describes neural network training through new terminology (Interleaved Representation, Memory Trace, Forward-Interleaved Memory Encoding) and claims to "fundamentally answer why catastrophic forgetting occurs." The paper presents empirical observations about decoder weight convergence and representation separation, then uses these to argue that forgetting stems from gradient updates only affecting the "memory trace" of current data, causing historical representations to collapse.

## Strengths

- **Empirical observation of decoder-to-class-mean convergence across architectures.** The paper reports that after training, decoder weight parameters converge to class-mean representations, and a new decoder trained on just these means matches the original (e.g., 10 samples replacing 60,000 on MNIST). This is tested across ResNet18/34/50, ViT-B-16, CIFAR-10/100, and cross-dataset pretraining (ImageNet1k), showing reasonable breadth.

- **Visual demonstration of distinguishable weight traces from different training phases.** The zero-initialized weight experiment (Section 3, Figure 9) provides an intuitive visualization showing that weight parameters develop distinct "traces" corresponding to different training phases, and that these traces are not simply overwritten by later training.

- **Step-by-step analysis of how representation divergence initiates.** The gradient-game derivation (Section 2.4) traces how initially similar higher-layer representations diverge through first-layer gradient competition driven by differences in raw input activations, offering a more granular mechanistic description than broad "overlap interference" accounts.

## Weaknesses

### Fatal

1. **The core "explanation" is a re-description of standard gradient-based learning, not a new theory.** The paper introduces "memory trace" (the sequence of layer inputs during a forward pass) and "Forward-Interleaved Memory Encoding" (how input differences propagate through gradient updates) and claims these "fundamentally explain catastrophic forgetting." However, Equation 6 ($\nabla w_{jk}^l = \sum_i t_{x_i k}^l \delta_{x_i j}^l$) is the standard backpropagation update. The gradient-game analysis describes how SGD learns discriminative features — a basic consequence of gradient-based optimization known since the earliest days of neural networks. The paper's central claim — that forgetting occurs because gradient updates for new data interfere with old data — is the standard understanding of the problem (McCloskey & Cohen, 1989; Ratcliff, 1990; French, 1999). No formal theorem, no testable prediction that distinguishes this account from existing theories, and no novel mechanism is offered. The contribution is terminological rather than explanatory.

2. **The paper explicitly states it cannot support its own theoretical claims.** Line 65: *"However, we have not provided an explanation for these phenomenon. On one hand, we do not have the time to provide a comprehensive mathematical proof, and on the other hand, this is not the focus of this article."* The Task Representation Convergence Phenomena — which the paper uses to argue that "the essence of model training is equivalent to training an encoder" — is explicitly left unexplained. A paper that claims to "fundamentally answer why catastrophic forgetting occurs" cannot simultaneously disclaim responsibility for explaining the key phenomena it introduces as evidence. This undermines the entire theoretical contribution.

### Major

3. **No quantitative results are reported in the text.** The paper repeatedly refers to figures without reporting a single accuracy value, forgetting rate, correlation coefficient, or confidence interval. Claims such as "the decoder's performance... remains consistent" (line 45) and "TRS is positively correlated with model performance" (line 32) are asserted without numerical support. For a paper making strong empirical claims, the absence of any concrete numbers makes the experiments unverifiable through the text alone.

4. **The experiments do not specifically test the Forward Explanation mechanism for catastrophic forgetting.** The experiments demonstrate that (a) representation separation correlates with performance (TRS, Figure 3), (b) decoder weights converge to class means (Section 2.2), and (c) weight patterns reflect training data (Section 3). These are well-known properties of gradient-based learning on classification tasks — they are consistent with the proposed framework but do not distinguish it from any standard account. There is no experiment that would differentiate the Forward Explanation from existing theories (e.g., parameter-overlap accounts like EWC, gradient interference accounts, or simply the standard understanding that sequential gradient updates overwrite previous knowledge). The paper claims a "fundamental" explanation but provides no causal evidence for its specific mechanism.

5. **No engagement with existing theoretical frameworks.** The paper cites French (1999) but does not discuss it or any other theoretical account of catastrophic forgetting. There is no comparison or contrast with frameworks such as the stability-plasticity dilemma, task-specific vs. shared representation analyses, loss landscape geometry, or gradient interference theories. A paper claiming a "fundamental" explanation should situate itself within and distinguish itself from the substantial existing theoretical literature.

### Minor

6. **Restrictive assumptions in the gradient-game derivation.** The analysis (Section 2.4) assumes all variables on the memory trace are non-negative and that $\delta$ magnitudes are similar. The derivation is informal, and the resulting conclusions ("the essence of backpropagation is fundamentally a form of forward propagation") are non-technical and unclear.

7. **Tension in the forgetting explanation.** Section 3 argues that (a) old memory traces persist on weights (Figure 9, point 2: "the memory trace for the 0-number data on w is not erased"), yet (b) old representations still collapse toward new ones. How persistent weight traces produce collapsing representations is not clearly resolved.

### Trivial

None.

## Nice-to-Haves

- Derive at least one empirically testable prediction that follows uniquely from the Forward Explanation framework (e.g., a prediction about first-layer activation replay vs. standard replay).
- Provide a mathematical account of the Task Representation Convergence Phenomena or properly attribute it to known results, rather than acknowledging it cannot be explained.
- Report quantitative results (accuracy, forgetting rates, correlation coefficients) for all experimental claims.

## Removed Points

The following points from the input reviews were identified as less reasonable or filtered per the merging guidelines:
- Several of the harsh critic's generic area-of-concern sweeps ("could the metric be measuring a proxy?", "are confounders controlled?") were removed as speculative — they lacked specific anchors in the paper.
- Formatting/style nitpicks and typo concerns were removed per the parser-error rule.
- Criticisms about missing related works beyond the cited French (1999) were removed per the rule against external verification; the verified lack of engagement with the cited works themselves is retained as Weakness #5.
- The harsh critic's reproducibility concerns were removed as they demanded trivial implementation details.
- Generic strengths from the Strength Finder (e.g., "addressed an important problem") were removed as superficial.
- The Strength Finder's claim that experiments demonstrated "identical performance" was qualified downward since no accuracy numbers appear in the text.

## Novel Insights

None beyond the paper's own contributions. The synthesis of the reviews confirms that the paper's central claim cannot be sustained: what is presented as a fundamental explanation is a terminological re-description of known dynamics, and the paper explicitly acknowledges its inability to prove the key phenomena it relies on.

## Suggestions

1. Report quantitative results (accuracy, forgetting rates, correlation coefficients) for all experiments rather than relying solely on figure references.
2. Derive at least one falsifiable prediction that distinguishes the Forward Explanation from existing theoretical accounts of catastrophic forgetting.
3. Engage with the existing theoretical literature on catastrophic forgetting (e.g., parameter importance accounts, gradient interference theories, stability-plasticity analyses) and explicitly contrast the proposed framework.
4. Either provide a mathematical account of the Task Representation Convergence Phenomena or properly attribute it to known results rather than acknowledging it cannot be explained.

---

MY FINAL SCORE: <score>2.5</score>
MY FINAL DECISION: <decision>Reject</decision>