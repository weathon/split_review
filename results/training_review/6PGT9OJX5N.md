Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper addresses data pruning in the presence of noisy labels — an under-studied but practically important problem. It proposes RoP, a two-stage framework that (1) selects clean samples using a Neighborhood Label Inconsistency (NLI) Score, computed from the JS divergence between a sample's label and its neighbors' predictions (refined via feature and label propagation), and (2) re-labels the selected subset with a robust learning method (SOP+). The method is evaluated on CIFAR-10N, CIFAR-100N, WebVision, and ImageNet-N across multiple pruning rates and compared against 10 baselines.

## Strengths

- **Novel NLI-Score effectively distinguishes clean from noisy labels.** Table 3 provides strong direct evidence: when selecting 10K images from CIFAR-10N, the subset chosen by RoP contains only 4.8% noisy labels, versus ~17% for other methods. This is a substantial gap that directly validates the method's central claim of reducing selection bias under label noise.
- **Two-stage framework consistently outperforms prior pruning methods on noisy benchmarks.** RoP achieves state-of-the-art or competitive results on CIFAR-10N, CIFAR-100N, WebVision, and ImageNet-N across multiple pruning rates. For example, on CIFAR-10N worst-case at 20% pruning, RoP_B improves 1.5% over the best baseline (Table 1). On WebVision (Fig. 4), the advantage is sustained and even grows with subset size.
- **Feature and label propagation improve selection quality.** The ablation (Table 6) shows that using propagation ("Rec.") yields higher accuracy than omitting it ("No-Rec.") across all settings, both with and without re-labeling. This empirically confirms the value of the rectification step.
- **Density-based coverage sampling improves robustness at high pruning rates.** RoP_B (with coverage) consistently outperforms RoP (without coverage), especially at high pruning rates (e.g., CIFAR-10N worst at 80%: 85.3 vs 83.4 in Table 1), addressing a known failure mode of score-based pruning.
- **Comprehensive evaluation across diverse settings.** The method is tested on three real-world noisy datasets (CIFAR-10N, CIFAR-100N, WebVision) and one large-scale synthetic noisy dataset (ImageNet-N), with two different re-labeling methods (SOP+, DivideMix) and 10 baselines. This breadth strengthens the generality of the findings.
- **Efficiency analysis demonstrates scalability.** Figure 5 shows RoP's selection time on ImageNet-N is comparable to efficient methods like GraNd and far lower than optimization-based methods like KCenter.

## Weaknesses

### Fatal
None.

### Major

- **No measures of variance in any experimental result.** All tables report only single average numbers over 3 runs, without standard deviations, confidence intervals, or any indication of spread. The paper states "every experiment is run 3 times, and the average of the last accuracy is reported" (Sec. 4.2), but never shows the variance. Many comparisons involve margins of 0.5–1.5% (e.g., Table 1, CIFAR-10N Random1 at 0.2 pruning: RoP_B 88.6 vs. Pr4ReL 87.6). Without error bars, the reader cannot assess whether these differences are reliable or due to random seed variation. This is the single most important evidential gap in the paper. While 3-run averaging is a common practice, the complete absence of any dispersion metric limits the persuasiveness of the claimed improvements, especially for the finer-grained comparisons where margins are small.

### Minor

- **The propagation step's validation is limited to an ablation against a "no-rectification" baseline that also uses the same noisy FC layer.** The paper claims feature/label propagation "rectifies" predictions, but the ablation (Table 6) only shows that propagation helps relative to using raw predictions from the same noisy model. The FC layer weights \(W_n\) (Eq. 6) are learned on noisy data and may encode systematic biases. The paper does not analyze whether predictions actually move *toward true labels* or simply become smoother. A comparison against an alternative prediction source (e.g., a model trained with a noise-robust loss, or an oracle) would more directly validate the rectification claim. The ablation is encouraging but not conclusive on the mechanism.
- **The initial pre-trained model \(\theta_{\tilde{\mathcal{D}}}\) used for feature extraction and FC weights is underspecified.** The paper does not describe how this model is trained: from scratch on the full noisy dataset? With what training procedure (epochs, learning rate, optimizer)? The quality of this model directly affects the reliability of nearest-neighbor search and the FC layer's predictions. Since the method's effectiveness depends on these features, the lack of detail hampers reproducibility.
- **The empirical analysis linking NLI-Score to re-labeling accuracy (Fig. 3) is conducted on a single dataset (CIFAR-10N) with one random subset.** While this plot is a genuine strength of the paper, replicating it on additional datasets (e.g., CIFAR-100N or WebVision) would strengthen the motivation for the two-stage design.

### Trivial
- None.

## Nice-to-Haves
- Reporting error bars / standard deviations across multiple seeds would substantially strengthen the paper's empirical claims.
- An analysis of failure cases of NLI-Score (samples with high NLI-Score that are actually clean, or low NLI-Score that are noisy) would clarify where the metric breaks.
- Visualizing the selected subsets in feature space (e.g., t-SNE) for different methods would intuitively illustrate why RoP selects cleaner subsets.
- Ablating the number of propagation steps (only one step is used) would test whether more steps improve or degrade performance.
- A quantitative analysis of the selection-bias vs. re-labeling-difficulty trade-off mentioned qualitatively in the introduction would further validate the motivation.

## Removed Points
*These points are flagged to be removed, treat them with caution:*

- "No mention of work on neighborhood-based noise detection in noisy label learning" — Removed per rule: do not mention missing related works (cannot verify existence of such works).
- "The normality assumption (ReLU features) means the method may fail with models using different activations" — The paper explicitly acknowledges this scope (line 81-82: "in all backbone architectures utilized in our experiments, the penultimate layers are activated using a ReLu function"). This is a known and stated limitation, not an oversight.
- "The comparison between GraNd and KCenter is only supported by a single comparison; the claim that geometry-based methods exhibit greater resilience is too broad" — This is an illustrative motivating observation (Fig. 1), not a rigorous claim that all geometry-based methods are universally better. The paper's core contribution is the RoP method, not a survey of geometry-based methods.
- Several suggestions in the harsh critic's "Missing Parts" and "Deeper Analysis Needed" sections (oracle comparisons, alternative initializations, iterative application) are speculative nice-to-haves rather than weaknesses of the presented work.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. **Add standard deviations to all main tables (Tables 1–5).** This is the most impactful improvement the authors can make. Reporting the spread over 3+ seeds would address the single biggest concern about the reliability of the claimed improvements.
2. **Provide training details for the initial model \(\theta_{\tilde{\mathcal{D}}}\)** (epochs, optimizer, learning rate schedule) in the experimental setup section to improve reproducibility.
3. **Strengthen the propagation validation** by showing that predictions after propagation correlate better with true labels (e.g., on a small clean holdout set) than raw predictions from the noisy FC layer.
4. **Extend the empirical analysis of Fig. 3** to at least one additional dataset (e.g., CIFAR-100N) to strengthen the motivation for the two-stage design.

## Score and Decision

The paper addresses an important and under-explored problem (data pruning under noisy labels), proposes a sensible and well-motivated two-stage framework, and provides broad experimental evaluation across multiple datasets, baselines, and pruning rates. The core idea — using neighbor label inconsistency as a selection signal — is validated by the striking result in Table 3 (4.8% vs 17% noisy labels in the selected subset). The paper is clearly written and the methodology is coherent.

The main weakness is the absence of any measure of variance in the experimental results. While this does not invalidate the paper's core claims (especially given the large margin in Table 3 and the consistency across settings), it limits the reader's ability to assess the reliability of finer-grained comparisons. The propagation validation could also be more incisive.

Overall, this is a solid contribution that advances the state of the art in noisy-label data pruning, with clear practical relevance. The weaknesses are addressable and do not undermine the core contribution.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>