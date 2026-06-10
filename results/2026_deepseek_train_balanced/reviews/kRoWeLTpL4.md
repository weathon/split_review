Now I have all the verification I need. Let me produce the final consolidated review.

---

## Summary

This paper introduces CP-Fuse, an inference-time method that adaptively fuses two language models trained on disjoint copyrighted data to prevent verbatim reproduction of protected content. At each decoding step, CP-Fuse performs a lightweight grid search over fusion weights to equalize each base model's cumulative log-probability — a "balancing property" whose theoretical justification is the paper's core conceptual contribution. Evaluated on overfitted LLaMa2-7B and StarCoder-7B models across text (MathAbstracts, WritingPrompts) and code (Python instructions, APPS) benchmarks, CP-Fuse reduces exact-match lengths by 20–48× against the unfused overfitted models while preserving pass@1 and fluency scores.

## Strengths

1. **Strong and consistent copyright protection across diverse tasks and metrics.** Table 1 shows that CP-Fuse reduces exact-match (EM) lengths from ~1300–1500 (overfitted models) to ~25–70 across all datasets and splits, outperforming every baseline (SystemPrompt, MemFree, CP-Delta) on essentially every metric. The improvement is not marginal — on MathAbstracts Split 2, EM drops from 1570.88 to 48.74 (~32× reduction). The JPlag plagiarism scores (0.03 for CP-Fuse vs. 0.96–1.00 for all baselines) provide direct evidence that the method suppresses both verbatim and near-verbatim copying.

2. **Principled theoretical grounding via the balancing property (Lemma 1).** Lemma 1 (lines 146–152) proves that CP-Fuse's adaptive weighting ensures neither base model's cumulative log-probability dominates the generated sequence. Figure 1 (lines 156–160) validates this empirically by showing that under CP-Fuse the two models' cumulative log-likelihoods track each other closely, whereas the token-wise CP-Delta baseline lets one model dominate. This property goes beyond prior fusion methods (DExperts, contrastive decoding) which offer no such provable anti-regurgitation guarantee.

3. **Utility preservation with concrete, illustrated evidence.** Table 2 shows CP-Fuse achieves pass@1 scores on APPS (0.47), MBPP (0.43), HumanEval (0.28), and fluency on WritingPrompts (2.17) that are essentially equal to or better than the overfitted models. MemFree degrades utility substantially (APPS pass@1 drops from 0.43 to 0.32). Figure 3 provides concrete side-by-side code examples showing MemFree introduces syntax/logic errors while CP-Fuse generates correct solutions — an unusually specific and convincing illustration of quality preservation.

4. **Seamless composability with training-time methods.** Section 3.3 (lines 376–413) demonstrates that wrapping goldfish-loss-trained models with CP-Fuse further reduces EM from 84.68 to 20.68 on Split 1 of the WritingPrompts task. This shows CP-Fuse compounds with existing memorization-mitigation techniques rather than being redundant with them.

5. **Robustness evaluation against adversarial prefix-prompting.** Section 3.4 (lines 414–417) tests a realistic threat model (black-box access with partial story prefixes) and shows CP-Fuse's EM remains stable and BLEU stays far below the overfitted models as prefix length increases — going beyond standard benchmarking.

## Weaknesses

### Major

1. **The separability assumption — on which the method's entire logic depends — is never stress-tested.** CP-Fuse only works because each copyrighted work appears in exactly one model's training split. The paper states this assumption in Section 3.1 (lines 93–95) and acknowledges in the Conclusion (line 427) that future work should investigate partial violations. But no experiment evaluates even a controlled violation (e.g., injecting 10–50% of copyrighted samples into both splits). In real deployments, the same copyrighted content often appears across multiple data sources (e.g., the same book in BookCorpus and The Pile). If both models memorize the same passage, the balancing property equalizes their log-probabilities and could still assign high probability to infringing text. This is not a speculative edge case but a structural limitation of the approach. The paper needs at minimum a controlled overlap experiment to bound how degradation scales with overlap percentage.

2. **No statistical uncertainty reported anywhere.** Every result in Tables 1 and 2 is a point estimate without confidence intervals, bootstrap estimates, or standard deviations. The copyright metrics (average above the 95th percentile) are inherently noisy — especially given only 3,000 training samples per split and greedy decoding. Without variance estimates, the reader cannot assess whether the differences between CP-Fuse and the next-best baseline (MemFree or CP-Delta) are stable or could shift with a different random seed or data split. Given that the paper's central claim rests on quantitative comparisons, this is an evidential gap that should be straightforward to fill.

### Minor

1. **The "over 25×" reduction claim in the abstract and main text is imprecise.** Computing from Table 1: Python instructions Split 1 is 1469.80 → 69.58 ≈ 21×, Split 2 is 1393.88 → 68.04 ≈ 20×. Only MathAbstracts (~25×) and WritingPrompts (~48×) meet the "over 25×" threshold. The claim should be qualified as "20–48×" or "up to 48×."

2. **The experimental setup uses pathologically overfitted models (3,000 samples per split, training to near-complete memorization).** The paper frames this as a "challenging setting" (line 176), which is a defensible stress-test methodology. However, memorization in large-scale pre-training (1–3 epochs on billions of tokens) follows different patterns — it is sparser and concentrated on rare or duplicated sequences. Whether CP-Fuse's advantage carries over to realistic memorization regimes is not directly tested. The utility evaluation partially mitigates this concern (models that memorize less also have less to suppress), but the paper's central copyright claim is only validated in a worst-case regime whose relation to practical deployment is unclear.

3. **The characterization of MemFree's failure mode ("often avoids exact copying simply by inserting spaces or spelling mistakes") is stated informally (line 234) without systematic quantification.** The JPlag scores (0.99/0.96) support the claim that MemFree outputs remain plagiarized, but how often the specific "spaces or spelling mistakes" strategy occurs is not measured. The paper refers to an appendix for examples, which is reasonable for a conference paper, but the claim would be stronger with a simple frequency count.

### Trivial

- None (the paper is well-written and free of formatting issues that would affect evaluation).

## Nice-to-Haves

- **Computational overhead**: The paper does not report wall-clock time or FLOPs overhead of CP-Fuse relative to standard greedy decoding. The grid search (361 weight pairs evaluated via log-probabilities from both models at each step) is presumably modest, but a concrete number would help practitioners decide whether the method is practical for latency-sensitive applications.
- **Direct head-to-head comparison with goldfish loss alone**: The wrapping experiments (Figure 4a) show CP-Fuse + goldfish loss improves over goldfish loss alone. But a standalone comparison between CP-Fuse (without goldfish loss) and goldfish loss alone on the same copyright metrics would clarify whether the paper's method is competitive with training-time approaches on its own terms. Currently the reader must cross-reference different tables to make this comparison.

## Removed Points

These points were raised in the input reviews but removed after verification against the paper:

- **"The log-linear form is identical to standard logit blending"**: The paper explicitly acknowledges this connection (lines 132–138) and clearly distinguishes its contribution as the *adaptive* weighting guided by the balancing property. This is proper positioning, not a weakness.
- **"Proofs are in the appendix"**: This is standard for ICLR (page limit). The main text gives clear intuitive explanations of Lemma 1 and Lemma 2.
- **"Missing analysis of grid resolution sensitivity"**: The paper promises this in the appendix (line 191, "see ablation studies in \Cref{app:ablation_grid}"). Stripped by the parser.
- **"Prefix prompting attack model is too restrictive"**: The paper explicitly defines its threat model (black-box access to CP-Fuse, not individual base models). Criticizing the absence of a different threat model is scope creep.
- **"Transition from Eq. (3) to Lemma 1 is too large"**: A presentation preference, not an error. The KKT argument is gestured at but the result is stated clearly; a non-specialist might need to consult standard convex optimization references, which is acceptable.

## Novel Insights

The harsh critic identifies the separability assumption as the method's Achilles' heel, and the strength finder correctly recognizes the balancing property as the paper's key conceptual contribution. The merger's genuinely novel synthesis is this: CP-Fuse's strength and its limitation are two sides of the same coin. The balancing property *requires* that the copyrighted domains be disjoint — it works by suppressing whichever model has been "winning" the generation so far, relying on the other model to assign negligible probability to that protected content. This means CP-Fuse is provably effective exactly when the data partitioning is clean, and its guarantee weakens in proportion to overlap between the two copyrighted sets. The paper would benefit from formalizing this trade-off: "if the overlap ratio is r, the worst-case regurgitation probability is bounded by f(r)," turning the current vulnerability into a quantifiable property. This framing would transform the limitation from a gap into a research direction rather than leaving it as an untested assumption.

## Suggestions

1. **Add one experiment with controlled overlap.** Keep the current setup but inject 10%, 25%, and 50% of the copyrighted samples from one split into the other (or duplicate them in both training sets). Measure how EM and BLEU degrade as overlap increases. This directly addresses the most serious practical concern and would strengthen rather than dilute the paper's core contribution.
2. **Report bootstrap confidence intervals** (or at least standard deviations over multiple random seeds) for the main copyright metrics in Table 1. The 95th-percentile metric is noisy; even 100 bootstrap resamples would give the reader a sense of the comparisons' reliability.
3. **Quality the "25×" claim** in the abstract to "20–48×" or "up to 48×" to match the actual data.
4. **Add a sentence on computational overhead** in the experimental setup section (e.g., "CP-Fuse adds approximately X ms per token compared to greedy decoding").

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>