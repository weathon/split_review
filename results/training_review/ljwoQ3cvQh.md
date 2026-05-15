Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

The paper presents evidence for the "reversion to the OCS" hypothesis: as inputs become increasingly out-of-distribution (OOD), neural network predictions tend to converge toward the optimal constant solution (OCS)—the best input-independent prediction for the training loss. The authors demonstrate this phenomenon across 8 datasets, 3 loss functions (cross-entropy, MSE, Gaussian NLL), and both CNN and transformer architectures. They propose a mechanistic explanation (OOD features have smaller norms, making outputs dominated by accumulated biases that approximate the OCS), supported by empirical analysis and informal theory. Finally, they show that choosing a loss function whose OCS aligns with cautious behavior leads to automatically cautious decisions on OOD inputs in a selective classification setting.

## Strengths

- **Extensive empirical demonstration across diverse settings**: The paper systematically evaluates the reversion phenomenon on 8 datasets (CIFAR10/CIFAR10-C, ImageNet variants, DomainBed OfficeHome, SkinLesionPixels, UTKFace, BREEDS, WILDS Amazon), three loss functions (cross-entropy, MSE, Gaussian NLL), and both CNNs (ResNet, VGG) and transformers (DistilBERT). Figure 2 shows a consistent monotonic decrease in distance to the OCS as OOD score increases, with error bars over 5 runs. This breadth of evidence directly supports the paper's central hypothesis.

- **Combined empirical and theoretical mechanistic analysis**: The paper proposes a concrete mechanism—OOD representations have smaller norms and align less with weight matrices, so outputs are dominated by accumulated biases that approximate the OCS. Empirical evidence (Figure 3) shows feature norm collapse and decreasing subspace alignment with distribution shift, while the theoretical analysis (Propositions 1–2 and Theorem 1) provides conditional bounds on why this can occur in deep homogeneous ReLU networks. The bias accumulation closely matches the OCS (Figure 3, columns 3–4).

- **Practical demonstration of concept**: The selective classification experiment (Section 5) shows that the choice of loss function (and hence its OCS) materially affects OOD decision-making. A reward-prediction model (MSE loss, whose OCS favors abstention) increasingly abstains on OOD inputs, while a standard cross-entropy classifier (whose OCS never prefers abstention) does not. The gap in performance is substantial compared to an oracle upper bound.

- **Clear, well-structured presentation**: The paper is well-written, the figures are informative, and the paper is transparent about its limitations ("do not yet have a complete characterization").

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The decision-making comparison does not perfectly isolate the role of the OCS.** The reward-prediction (MSE) and standard classification (CE) approaches differ in both their loss function and their OCS. The result—that the MSE model abstains more on OOD inputs—is consistent with the OCS hypothesis, but one cannot fully rule out confounding factors (e.g., differences in training dynamics between MSE and CE). A cleaner test would compare two models trained with the same loss function but different reward structures (yielding different OCS values). That said, the paper's claims are appropriately modest (Section 5: "the goal of our experiments was not to demonstrate that our approach is the best possible method ... but rather to highlight how the OCS ... can influence ... OOD decision-making behavior"), and the results are genuinely consistent with the hypothesis.

2. **The framing of standard classification as "not leveraging reversion to the OCS" is slightly imprecise.** Standard classifiers also revert to their OCS (the class marginal) on OOD inputs; the difference is simply that their OCS does not include abstain. The paper acknowledges this implicitly ("the OCS for this approach corresponds to a policy that never chooses to abstain"), but the "does/does not leverage" framing could mislead a casual reader into thinking the phenomenon itself is absent rather than the OCS being differently aligned.

3. **The empirical evidence is fundamentally correlational.** The x-axis in Figure 2 is a learned OOD score from a low-capacity discriminator rather than a directly controlled independent variable (e.g., rotation angle, noise level). The paper uses controlled shifts for the motivating examples (Figure 1, Figure 3 with rotation/noise for MNIST and CIFAR-10), but the main experimental figure (Figure 2) relies on a derived score that confounds shift type and severity. The observed monotonic trend is compelling but would be strengthened by additional plots using directly controlled shift magnitudes as the independent variable.

4. **The theoretical analysis is informal and does not prove the mechanism.** Propositions and Theorem 1 are explicitly labeled "informal" and provide conditional bounds (e.g., "if representations lie outside a rank-1 subspace, then outputs become small") rather than establishing that OOD inputs *provably* cause feature collapse. The paper states this honestly ("Because neural networks are not optimized on OOD inputs, we *hypothesize* that..."), but the theoretical section consequently adds limited evidential weight beyond what the empirical analysis already shows.

### Trivial

- The paper could report the distance to OCS for extreme shifts in absolute terms (e.g., "predictions close to X% of the OCS value") rather than only relative trends, to better characterize the strength of the phenomenon.

## Nice-to-Haves

- A controlled ablation comparing two reward-prediction models with different reward structures (one with cautious OCS, one without) would strengthen the causal interpretation of the decision-making experiment.
- Using directly controlled shift magnitudes (noise level, rotation angle) as x-axis variables for more datasets would complement the discriminator-based OOD score metric.
- Investigating failure cases—datasets or shift types where reversion does not occur—would help bound the hypothesis and make the claim more falsifiable.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The paper only uses two datasets (MNIST, CIFAR-10)"** — Factually wrong. The paper uses 8 datasets spanning vision and NLP (Table 1 lists 9 settings).
- **"Key details are deferred to an appendix"** — The extracted paper text does not mention an appendix. The parser may have stripped an appendix section; in any case, this is a known parser artifact, not an author error.
- **"The oracle policy has an unfair advantage"** — The paper explicitly acknowledges this: "Note that the oracle policy has access to... the OOD evaluation dataset for calibration, which the other two approaches do not have access to."
- **"The paper does not report correlation coefficients/p-values"** — The paper reports standard deviations over 5 runs and shows consistent monotonic trends. Formal significance tests are not standard for this type of observational empirical observation in ML.
- **"The analysis should be extended to more settings"** for the empirical analysis in Section 4.1 — The paper does extend the main observation (Figure 2) to 8 datasets; the mechanistic analysis (Figure 3) uses MNIST and CIFAR-10, which is a reasonable scope for an analysis that requires per-layer feature extraction.
- **Several formatting/style nitpicks and generic requests** (e.g., "include datasets where reversion fails," "analyze dependence on network depth") — These are either scope creep (the paper acknowledges incomplete characterization) or generic suggestions not grounded in specific failures of the presented evidence.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel observation or alternative interpretation not already present in the paper.

## Suggestions

- Tighten the framing of the decision-making experiment to avoid the implication that standard classification "does not leverage" the OCS phenomenon. Clarify that both methods revert to their respective OCS; the contribution is engineering the OCS to align with cautious behavior.
- Add a controlled shift (noise/rotation) version of Figure 2 for at least 2–3 datasets, even if only in the main text, to complement the discriminator-based metric and address correlational concerns.
- If the theoretical analysis cannot be made non-conditional, consider moving it to a more clearly supporting role rather than a standalone evidence section. The empirical analysis (Figure 3) is the stronger evidence for the mechanism.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>