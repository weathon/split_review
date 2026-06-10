## Summary

This paper investigates global unstructured magnitude pruning through the lens of cosine similarity between a parent network's parameter vector and its pruned version. It proves that L1 pruning (removing smallest-magnitude parameters) maximizes cosine similarity, empirically shows that post-pruning accuracy/loss correlates with cosine similarity much better than with sparsity percentage, and proposes a Pareto-front method to determine optimal pruning amounts. The paper also introduces kurtosis of the parameter distribution as a predictor of pruning tolerance and identifies a failure mode for networks with high "kurtosis of kurtoses" (e.g., MobileNetV2).

## Strengths

- **Figures 1–2 provide strong quantitative evidence that cosine similarity organizes pruning outcomes better than sparsity.** The paper shows that when accuracy/loss is plotted against pruning percentage, Random and L1 pruning follow vastly different trajectories; when plotted against cosine similarity, the trajectories collapse onto each other across three architectures (ResNet18, VGG11 BN, LeNet Small) with standard deviations from 10 runs. This is the paper's most compelling empirical finding and directly answers its first motivating question (Section 5.1, lines 106–118).

- **The loss landscape comparison in Figure 5 quantifies network "brittleness" in a visually striking way.** L1 pruning to cosine similarity 0.99 removes 70% of parameters with an ℓ∞ landscape distance of 65.28 from the parent, while Random pruning to the same cosine similarity removes only ~2% but changes the landscape by ℓ∞ distance 484.03 (~7.4× larger perturbation from 28× fewer parameters removed). This provides concrete evidence that networks are dominated by their high-magnitude parameters (Section 5.3, lines 148–159).

- **Honest identification and diagnosis of the MobileNetV2 failure mode.** The paper identifies a concrete case where global L1 pruning fails (disconnects entire low-magnitude layers), introduces "kurtosis of kurtoses" (κ^(2)=64.40 for MobileNetV2 vs. 1.42–5.81 for well-behaved models) as a diagnostic, and suggests local pruning as an alternative (Section 5.4, lines 183–186). This intellectual honesty strengthens the analysis.

- **Clean geometric framing of the pruning problem.** The reformulation of pruning as a Pareto-optimal trade-off between cosine similarity and sparsity, with L1 pruning as the Pareto frontier, provides a conceptually useful way to think about the problem (Section 5.4, lines 165–178).

## Weaknesses

### Fatal
None.

### Major

- **The central claim that cosine similarity is a "good proxy for functional similarity" (abstract, line 21; Section 5.2, line 126) rests on qualitative evidence only.** The paper uses t-SNE projections of model predictions (Figure 3) and loss-landscape visualizations (Figures 4–5) to support this claim, but these are at best suggestive. t-SNE preserves local neighborhood structure but does not provide a quantitative measure of functional distance. The paper never computes a direct functional similarity metric — such as prediction agreement rate, Jensen-Shannon divergence between output distributions, or centered kernel alignment (CKA) of representations — and shows that it correlates with cosine similarity. The paper itself acknowledges the counterexample (small-magnitude weights connecting a layer could be pruned while preserving cosine similarity, Section 5.2, lines 126–127) and finds a real instance in MobileNetV2. Without quantitative bounds on when and how strongly the proxy holds, this central conceptual claim remains a hypothesis supported by suggestive but non-rigorous evidence. The paper's empirical findings about accuracy loss vs. cosine similarity (Figures 1–2) are separate and do not by themselves establish functional similarity.

### Minor

- **The Pareto-optimal pruning procedure (Section 5.4) is not directly validated against accuracy outcomes.** The paper claims the closest-to-utopia point is "the optima point for pruning while maintaining the highest accuracy" (line 165), but the validation consists only of stating that performance "remains high" (line 179) for one model. The paper does not compare accuracy at the optimal pruning amount vs. accuracy at nearby pruning amounts, leaving the reader to trust that the geometric Pareto point has a special relationship to performance rather than demonstrating it. The logic is plausible given the correlation shown in Figures 1–2, but a direct comparison would substantially strengthen the practical recipe.

- **The paper makes a specific claim about 10-epoch fine-tuning without experimental support.** Section 5.2 (line 139) states: "After a small prune, 10 epochs of fine tuning result in a network which is more similar to the parent than 1 epoch of fine-tuning. Conversely, after a big prune, 10 epochs of fine-tuning leads to a bigger functional change w.r.t. the parent than 1 epoch of fine-tuning." This is presented as a conclusion ("The conclusion is that more fine-tuning amplifies what we observe...") but no experiment with 10 epochs is shown. For a paper that explicitly scopes itself to one epoch of fine-tuning (line 4, line 95), making unsupported claims about what would happen with more epochs undermines the paper's empirical rigor.

- **The kurtosis-to-pruning-capacity correlation (lines 170–172) has potential confounds that are not controlled.** The paper reports that VGG11 BN (kurtosis 8.53) can be pruned more than LeNet Small (4.82), which can be pruned more than ResNet18 (3.79). However, these models differ in architecture size, depth, and capacity — not just kurtosis. A controlled experiment varying kurtosis (e.g., through initialization or weight decay) while holding architecture constant would substantially strengthen the causal claim that kurtosis drives pruning tolerance rather than being a confounded correlate.

### Trivial
None.

## Nice-to-Haves

- **Test with additional pruning criteria beyond L1 and Random.** Showing that gradient-based pruning methods (SNIP, GraSP) or movement pruning also collapse onto the cosine-similarity curves would substantially strengthen the claim that cosine similarity is a universal organizing principle (Figure 2 only tests two extremes).
- **Calibrate the ℓ∞ loss landscape distance.** The paper reports 65.28 vs. 484.03 as evidence of "largely unchanged" vs. "dramatically" changed landscapes (Section 5.3, line 152–154), but does not establish what constitutes a meaningful ℓ∞ distance relative to the loss values themselves.
- **Systematic accuracy comparison at the Pareto-optimal point vs. nearby points** would convert a plausible heuristic into a validated practical tool.

## Removed Points
These points were removed from the harsh critic or strength finder inputs because they violated the filtering rules:

- **Lottery Ticket Hypothesis omission** — Removed per hard rules: missing related works cannot be flagged without external verification.
- **Theorem 1 being "not a novel result"** — Removed: the theorem correctly applies a known property in a new framing context; this is not a genuine weakness.
- **"Only L1 vs Random pruning" as a weakness** — Demoted to nice-to-have: comparing two extremes (systematic vs. random) is a valid experimental design within the paper's scope.
- **"Pareto front on synthetic distributions is insufficient"** — Removed: the synthetic data (Figure 6) is used for illustration; the method is applied to real networks (Figures 7–8).
- **"MobileNetV2 failure not cured"** — Removed: the paper honestly identifies the limitation and provides diagnostics; this is appropriate intellectual framing, not a weakness.
- **Strength Finder: generic/overclaimed strengths** — Removed: superficial statements about the problem being important or the paper being well-written, which lack specific anchorable evidence.

## Novel Insights

The two reviewer inputs largely recapitulate the paper's own contributions (cosine similarity as a better organizing principle, brittleness via loss landscapes, kurtosis as predictor) rather than generating an unexpected synthesis. The most notable cross-review observation is the consensus that the paper's core evidence (Figures 1–2) is genuinely strong, but that the functional-similarity proxy and the Pareto-optimal procedure overreach relative to the evidence provided — i.e., the paper's best contribution is its empirical finding about cosine similarity organizing pruning outcomes, but it would benefit from framing the functional similarity and optimal-pruning claims more cautiously.

## Suggestions

1. **Provide quantitative functional similarity evidence.** Compute prediction agreement rate, CKA, or Jensen-Shannon divergence between parent and pruned network outputs, and plot against cosine similarity. This would either confirm or bound the central proxy claim.
2. **Validate the Pareto-optimal point against accuracy.** For the models in Figures 7–8, plot accuracy as a function of pruning percentage alongside cosine similarity, and verify that the chosen point is at or near the knee of accuracy degradation.
3. **Remove or experimentally support the 10-epoch claim in Section 5.2.** Either run the experiment or clearly label the statement as speculation.
4. **Consider a controlled experiment for kurtosis** — e.g., regularizing a single architecture to achieve different kurtosis values — to separate the causal effect from architectural confounds.

## Score and Decision

**Score:** 5

**Decision:** Reject

**Rationale:** The paper has a genuine insight and one strong piece of evidence (Figures 1–2), but it makes two central claims — that cosine similarity proxies functional similarity, and that a specific Pareto point is "optimal" for accuracy — that are incompletely supported by the evidence presented. The functional similarity claim in particular is a conceptual backbone of the paper (abstract, line 21) and relies on qualitative t-SNE visualizations rather than quantitative measurement. At the ICLR standard, a paper advancing a new conceptual lens for pruning should provide tighter quantitative evidence for its core conceptual claims, not just their downstream correlates. The paper's contributions are real but preliminary, and the overclaiming relative to evidence prevents acceptance in current form. A revised version that adds quantitative functional similarity analysis, validates the Pareto procedure, and removes unsupported speculation could be a strong submission.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>