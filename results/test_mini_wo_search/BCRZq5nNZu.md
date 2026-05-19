Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper decomposes continual learning (CL) into two sub-problems — task shift and the "chunking" problem (learning from a stream of data chunks without revisitation) — and studies the latter in isolation. The authors show that chunking alone accounts for ~50% of CL's performance drop relative to offline learning, that forgetting occurs even without any distribution shift, and that current CL methods (at least the replay-based ones tested) perform no better than plain SGD in the chunking setting. They propose per-chunk weight averaging as a simple mitigation, motivated by a Bayesian linear regression analysis, and demonstrate that it improves performance in both the chunking setting and the full CL setting.

## Strengths

1. **Clear decomposition and quantification of chunking's role.** Table 1 quantifies that chunking accounts for ~50% of the performance gap between offline learning and CL (50.05% on CIFAR-100, 46.69% on Tiny ImageNet), providing a concrete motivation for studying this sub-problem.

2. **Convincing evidence that popular CL methods do not address chunking.** Figures 2 and 3 show that DER++, ER, ER-ACE, AGEM, and GSS all perform comparably to plain SGD in the task-shift-free chunking setting across three datasets, with accuracy degrading as chunk size decreases. This is a clean empirical result.

3. **Demonstration that forgetting occurs without task shift.** Figure 5 tracks per-chunk training accuracy over time: each chunk is fit perfectly (100% training accuracy) but then rapidly forgotten, while test accuracy slowly improves. This directly challenges the common narrative that forgetting is primarily caused by distribution shift (Lee et al., 2021; Ramasesh et al., 2020).

4. **Simple, effective, and transferable mitigation.** Per-chunk weight averaging (especially the mean) yields accuracy gains of +4.32% to +11.73% in the chunking setting (Figure 6) and transfers to full CL settings, improving average accuracy by +6–12% in standard CL and +3–9% in online CL across multiple methods (Table 2). The method is straightforward and easy to implement.

5. **Principled theoretical motivation.** Section 4.2 derives the connection between weight averaging and Bayesian linear regression, showing that weight averaging approximates the Bayesian posterior when chunks are large enough for precision estimates to be accurate. This provides a clear rationale for the approach, even if the analogy does not perfectly hold for neural networks.

## Weaknesses

### Fatal
None.

### Major
None. No identified weakness threatens the paper's core claims.

### Minor

1. **The claim that "current CL methods do not tackle chunking" is broader than the evidence.** The paper tests five methods — all memory/replay-based (DER++, ER, ER-ACE, AGEM, GSS) — but does not evaluate regularization-based methods such as EWC, SI, or MAS. While the tested set represents the dominant family in modern CL and the conclusion is plausible, the claim as stated in the abstract and Section 4.1 ("current CL algorithms do not address the chunking sub-problem") is an overgeneralization. The paper should either test a broader set or add an explicit qualifier (e.g., "the replay-based methods we tested"). This does not invalidate the insight but oversells the result.

2. **Memory overhead of weight averaging is not discussed.** Per-chunk weight averaging requires storing a second copy of the model parameters throughout training (doubling parameter memory from ~44 MB to ~88 MB for ResNet-18). For larger models this overhead grows accordingly. The paper should acknowledge this cost, especially since CL methods often operate under tight memory budgets, and could note that the overhead is modest for the architectures used but may be relevant for scaling.

3. **The chunking proportion estimate (Table 1) is based on a single method (DER++).** The headline claim that chunking accounts for ~50% of the CL-offline gap rests on one method and two datasets. The paper is transparent about this, and it serves well as a motivating observation, but it should be explicitly flagged as preliminary rather than a general finding.

### Trivial

4. **Statistical reporting uses only 3 runs.** This is standard practice in CL, and standard errors are reported. Nonetheless, some improvements (e.g., DER++ on CIFAR-10 in online CL: 35.87 vs 36.26) fall within overlapping error bars. A brief acknowledgment of this limitation would be appropriate.

## Nice-to-Haves

- **Test weight averaging under imbalanced chunks.** The paper uses class-balanced chunks to isolate the chunking effect from class imbalance, which is a clean design choice. Testing with naturally imbalanced streaming data would strengthen claims about real-world generality.
- **Compare to simple variance-reduction baselines.** For instance, training with a very small learning rate might also reduce chunk-wise forgetting. A comparison would clarify whether weight averaging provides unique benefits or acts primarily as variance reduction.
- **Explicitly discuss limitations of the linear analogy.** While the paper does ask whether the analysis "still holds true for neural networks" (Section 4.2), it could go further by noting that neural network loss landscapes are nonconvex and overparameterized, so the "least squares solution per chunk" is not well-defined.

## Removed Points

These points from the inputs were removed with justification:

- **Criticism about linear analysis limitations being unaddressed** — The paper explicitly says in Section 4.2: "the question arises if this analysis showing weight averaging improving performance, assuming the chunks are large enough, still holds true for neural networks. We look at this in the next section." The paper does acknowledge the gap; the critic's framing as an omission is incorrect.
- **Criticism about class-balanced chunk assumption limiting generality** — The paper clearly justifies this design choice in Section 3 ("to control for class imbalance effects... ensure the results are solely due to the effects of limited data availability"). This is a controlled experiment, not a flaw. Moved to Nice-to-Haves as a suggestion for future work.
- **Criticism about missing hyperparameter details (learning rate schedule, optimizer settings)** — The paper states it uses the public Mammoth library (Buzzega et al., 2020) and provides code. Hyperparameter details are standard for the field and available through the cited library. The parser may also have stripped supplementary material.

## Novel Insights

The most novel insight from reading the reviews together is the observation that the paper's per-chunk weight averaging is fundamentally orthogonal to existing CL algorithms — it modifies only the evaluation weights without altering training dynamics. This means it can be straightforwardly combined with any CL method as a post-hoc improvement, which is both a practical strength (easy adoption) and a conceptual limitation (it does not address why chunk-level forgetting occurs during training). The fact that the method still yields consistent gains despite being a simple averaging of checkpoints suggests that chunk-level forgetting is largely about the variance of the final iterate rather than a structural collapse of knowledge, a distinction worth exploring further.

## Suggestions

- Qualify the claim about CL methods not addressing chunking to reflect the set of methods actually tested. A one-sentence caveat ("among the replay-based methods we evaluated") would resolve this cleanly.
- Add a brief paragraph discussing the memory overhead of weight averaging (one additional copy of model parameters) and note that this is acceptable for common CL architectures but worth considering when scaling.
- Acknowledge the statistical limitations of 3 runs in a limitations paragraph and consider reporting results over more seeds for the main experiments.
- Flag the single-method basis of the chunking proportion estimate (Table 1) as preliminary and suggest multi-method verification as future work.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>