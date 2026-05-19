- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6
Now I have enough information. Let me synthesize the final review.

## Summary

This paper studies the complementarity of different CLIP vision backbones (ResNets and ViTs) and proposes an adaptive ensembling method (Neural Logit Controller, NNC) that learns instance-dependent temperature weights via a one-layer MLP trained on as few as one labeled example per class. The key findings are: (1) different CLIP backbones exhibit strong complementarity (an oracle selecting the best backbone per test sample would improve accuracy by up to 43.5 percentage points); (2) NNC substantially outperforms static ensembling baselines (+9.1% average over the best single backbone across 21 datasets in zero-shot); and (3) NNC can be combined with existing few-shot adapters (e.g., Tip-Adapter) for further gains.

## Strengths

- **Quantified oracle upper bound for backbone complementarity.** The paper computes an oracle that selects the best backbone per test sample and demonstrates improvements of up to 43.5 percentage points (EuroSAT) over the best single backbone (Section 2). This concrete, dataset-specific evidence goes beyond prior comparisons by directly measuring untapped synergy among CLIP backbones trained with the same data and objective.

- **Consistent and meaningful improvements from NNC across 21 datasets in a well-controlled zero-shot comparison.** Against proper baselines (logit averaging, voting, calibrated averaging), NNC achieves up to +39.1% (EuroSAT) and an average +9.1% over the best individual backbone, while all non-parametric baselines show negligible or no improvement (Section 4.1). This demonstrates that the method successfully exploits backbone diversity beyond what simple averaging can capture.

- **Complementarity with existing few-shot adapters is validated.** When NNC is applied on top of Tip-Adapter (per-backbone), it yields additional improvements — e.g., over 15% on EuroSAT with 16 shots (Section 4.3, Figure 3). This shows NNC is not just a standalone method but also boosts state-of-the-art adapter techniques, which is an unusual and useful property for an ensembling approach.

- **Computational efficiency is explicitly considered.** The paper demonstrates that using the four most efficient backbones in NNC outperforms the best single backbone while requiring ~300 fewer GFLOPs (Figure wrap-fig:accuracy_vs_flops), addressing the practical concern that ensembling multiple models is too expensive.

- **Sound analysis of backbone diversity.** The Venn diagrams, oracle analysis, and diversity measure (Section 2) are well-conceived and convincingly show that different backbones have complementary correct predictions, even within the same architecture family (ViTs or ResNets).

## Weaknesses

### Fatal
None.

### Major

- **The few-shot comparison (Table 2) compares NNC using all 9 backbones against single-backpoint adapter methods.** NNC achieves 78.2% average accuracy with 1 shot vs. Tip-Adapter-F at 61.3%, but these baselines use a single backbone. This conflates the benefit of multi-backbone access with the benefit of the NNC weighting mechanism itself, and the framing as "consistently outperforming state-of-the-art few-shot methods" (line 105) overstates the evidence. A more informative comparison would be an ensemble of the same adapter across all 9 backbones, or a single-backbone version of NNC. The paper partially addresses this by later showing NNC+Tip-Adapter on multiple backbones (Section 4.4), but the headline comparison in Table 2 remains misleading as presented.

- **The NNC method is underspecified, hindering reproducibility.** The method is described as a "one-layer MLP" taking concatenated representations from up to 9 backbones (feature dimensions would be ~10,000–14,000) and outputting B temperature values, but no details are provided on: the MLP's hidden dimension (or lack thereof), regularization (dropout, weight decay), optimizer, learning rate, number of training epochs, or how the training/validation split is determined in the zero-shot setting (Section 4.1). For the few-shot setting this is clearer (k shots per class), but for the main zero-shot results the paper says "the training split of each target dataset" is used without specifying the proportion (line 290–291). Without these details the method cannot be reproduced or fairly compared against. The "as few as one labeled example per class" claim (abstract, intro) and the actual validation splits used in different experiments need to be explicitly reconciled.

### Minor

- **The claim that NNC "never degrade[s] the performance" (lines 85, 315) is stated categorically without error bars or confidence intervals.** A learned method with small training sets can overfit; even with regularization there is no guarantee on every dataset. A table showing per-dataset performance relative to the best backbone — ideally with confidence intervals — would be needed to rigorously support a "never" claim. The current presentation (a correlation plot, Figure wrap-fig:improvement_vs_diversity) is suggestive but insufficient for a categorical assertion.

- **The abstract uses "over 40 percentage" (line 10) which is ambiguous — it should be "over 40 percentage points" to clarify it is an absolute gain, not relative improvement. Similarly the oracle improvement figures (43.5%, 36.0%) should be explicitly labeled as absolute percentage-point improvements.**

- **The MoE degradation of up to -20.9% (line 345) is noted but not analyzed.** This is an interesting finding — it suggests the feature space is not naturally partitionable into expert regions — but the paper does not discuss why MoE fails so dramatically while NNC succeeds.

- **The Cascade integration is referenced in the introduction and Figure 2 but receives no dedicated quantitative evaluation or discussion beyond the accuracy-vs-FLOPs plot.** The paper mentions it "maintains computational efficiency" but does not present results comparing Cascade+NNC vs. standard NNC in a separate table or section.

### Trivial
None.

## Nice-to-Haves

- An ensemble of Tip-Adapter-F across all 9 backbones as an additional few-shot baseline would cleanly isolate the benefit of the NNC weighting mechanism from the benefit of multi-backbone access.
- A per-dataset breakdown showing which backbones are weighted heavily by NNC (beyond the single CLEVR example in Figure 4) would strengthen understanding of the method's behavior.
- Explicitly labeling oracle improvements as "percentage points" throughout would avoid ambiguity.

## Removed Points

- **Criticism that Cascade is "never evaluated quantitatively."** The Cascade evaluation appears in Figure wrap-fig:accuracy_vs_flops, which plots accuracy vs. GFLOPs for Cascade using 2–9 backbones. This is a quantitative evaluation, albeit a limited one. Demoted to Minor.
- **Criticism about missing error bars as a major omission.** Single-run evaluation without confidence intervals is standard practice in large-scale zero-shot CLIP benchmarking. This is a minor concern, not a major weakness. Moved to Minor (under the "never degrade" claim).
- **Strength about "effective few-shot learning with as few as one labeled example per class."** This strength is retained but qualified by the major weakness about the unfair comparison.
- **Strength about "NNC obtains 78.2% average accuracy with only 1 shot, far exceeding prior few-shot methods."** Same — retained but tempered by the comparison issue.
- **Generic strengths about addressing an important problem, targeting an interesting question.** These were not raised by the Strength Finder, so no removal needed.
- The harsh critic's "Strengthening the Paper" suggestions are incorporated into the Weaknesses and Nice-to-Haves rather than added as standalone points.

## Novel Insights

None beyond the paper's own contributions. One observation from the review process: the MoE degradation (-20.9%) is an under-explored finding — it suggests that while backbone features are complementary at the prediction level, they are not easily partitionable into distinct expert regions, which contrasts with NNC's instance-level temperature mechanism that smoothly weights all backbones. This comparison could be a fruitful direction for understanding when late fusion with learned weights succeeds or fails.

## Suggestions

1. **Reframe the few-shot comparison.** Either remove Table 2 or add a multi-backbone baseline (e.g., ensemble of Tip-Adapter-F across all 9 backbones with logit averaging) so that the benefit of NNC's adaptive weighting is isolated from the benefit of having access to 9 backbones. Alternatively, add a single-backbone version of NNC as a control.

2. **Add complete training details for NNC** — MLP architecture (input size, hidden dimensions, output size), regularization, optimizer, learning rate, number of epochs, and crucially, the training data regime used for each experiment (zero-shot main results, linear classifier experiments, few-shot experiments). The relationship between "as few as one labeled example per class" and "10% of the training split" must be explicitly clarified.

3. **Replace the "never degrade" claim with a measured statement** such as "NNC consistently improves or matches the best single backbone across all evaluated datasets" and report the worst-case relative change.

4. **Explicitly label oracle improvements as absolute percentage-point gains** throughout the paper to avoid ambiguity.

5. **Discuss the MoE failure case** to provide insight into why instance-level temperature scaling succeeds where hard gating fails.

6. **Include confidence intervals** for at least the main accuracy comparisons (zero-shot and linear probe), or justify their absence with a reference to community norms.
