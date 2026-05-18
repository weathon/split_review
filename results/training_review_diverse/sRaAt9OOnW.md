Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This benchmark paper identifies an important methodological flaw in the evaluation of continuous Gromov-Wasserstein (GW) solvers: existing evaluations overwhelmingly use "correlated" data setups (where source and target samples have a statistical relationship, e.g., dictionary pairs), which masks the failure of solvers on standard uncorrelated i.i.d. data. The authors formalize this (un)correlatedness concept and test three existing continuous GW solvers (StructuredGW, FlowGW, AlignGW) on GloVe word embeddings with a controlled parameter α that varies the level of correlation. All three baselines perform well at α=1 (totally correlated) but degrade sharply as α→0 (uncorrelated). As a first step toward addressing this, the authors propose NeuralGW—a min-max-min adversarial solver that avoids discrete coupling matrices—and show initial results on the same benchmark.

## Strengths

- **Identifies a genuine and actionable methodological blind spot.** The paper formalizes the concept of (un)correlatedness in GWOT training data (Section 4.1) and correctly observes that most existing work evaluates on setups where source and target samples are linked by a non-independent coupling (e.g., dictionary pairs in word alignment, same-donor gene profiles). This is a clean, reproducible insight that the community would benefit from grappling with.

- **Provides controlled quantitative evidence that the correlatedness issue is real.** The GloVe experiment (Section 4.2, Figure 2) systematically varies α from 0 to 1 and shows that all three baseline solvers—StructuredGW, FlowGW, and AlignGW—under identical training conditions (3K samples each) suffer a sharp performance drop as α decreases. This evidence is self-contained and does not depend on the proposed method. It convincingly demonstrates that existing methods fail on uncorrelated data.

- **Principled mathematical foundation for NeuralGW.** Lemma 1 and Theorem 1 (Section 5.1) provide a sound equivalence between the innerGW problem and a minimax objective, showing that optimal GW maps emerge from the optimization. This theoretical grounding distinguishes NeuralGW from ad-hoc discrete-to-continuous heuristics.

- **Candid discussion of limitations.** The paper transparently acknowledges NeuralGW's high variance, training instability, large data requirements, and the unfairness of the 3K-vs-200K comparison (Sections 5.2, 6). This honesty adds credibility and helps set realistic expectations.

## Weaknesses

### Fatal

None.

### Major

- **Unfair comparison undermines the claimed superiority of NeuralGW at α=0.** The headline result that NeuralGW "outscores competitors by a large barrier" at α=0 (Section 5.2) compares baselines trained on 3K samples with NeuralGW trained on 200K samples—a ~67× disparity in training data. The paper acknowledges this but still presents the comparison as evidence of superiority. While it is true that the baseline methods cannot scale to 200K samples due to their discrete backend, the paper provides no attempt to either (a) scale baselines up to even 10K–20K using computational tricks (e.g., minibatching, entropic regularization) or (b) scale NeuralGW down to 3K and show it still performs reasonably. Without such controls, the performance gap at α=0 cannot be attributed to the method's design rather than simply to dataset size. This is the paper's most significant weakness and directly affects the claim that NeuralGW "partially solves some of the problems."

- **Insufficient empirical validation of NeuralGW.** The method is presented as a key contribution, yet it is tested on only one real dataset (GloVe) and one qualitative toy experiment (3D→2D mixture of Gaussians, with no quantitative metric). The GloVe results show high variance across runs (large error bars). No ablation studies are provided (e.g., what happens without the P matrix? without the f network?). No convergence analysis, no comparison on other domains (e.g., single-cell data, shape data) that would demonstrate generality. For a method claimed to be "the first known solver for the GWOT problem that does not rely on discrete approximations," the empirical support is thin. The paper would be considerably stronger as a pure benchmark/analysis paper, treating NeuralGW as a preliminary proof-of-concept.

### Minor

- **The evaluation metric is not defined.** The y-axis of Figures 2 and 3 is labeled only "Metric" (and captions refer to "Performance"). The paper states that "metrics are computed on (unseen) test data" (line 250) but never specifies what the metric is. In the context of innerGW, the natural candidate is the GW distance (innerGW²₂) between the mapped source and target distributions. This must be stated explicitly for reproducibility.

- **The α-correlatedness construction description is unclear.** The index-shifting procedure (Section 4.1, paragraph "Modeling (un)correlatedness in practice") is hard to parse: "Indices from 0 to N_train/2 are taken from the source while indices from target are shifted, we take the ⌈(1-α)(N_train/2)⌉ to ⌈(1-α)N_train⌉ indices." The accompanying figures (Figure 4–6) help, but a precise mathematical description of how α controls the overlap between source and target training sets would improve clarity. Additionally, it would be helpful to explicitly note that the marginal distributions are preserved under this construction.

- **NeuralGW is developed only for the inner product cost (innerGW).** The paper focuses on innerGW, which is a commonly studied case, but practical GW applications often use squared Euclidean distance. The paper does not discuss whether the correlatedness findings or the NeuralGW approach transfer to other cost functions. This limits the scope of the conclusions, though the paper is transparent about the scope.

### Trivial

- None.

## Nice-to-Haves

- Test on at least one additional uncorrelated dataset (e.g., single-cell multi-omics data from demetci2022scot, or the Gaussian experiments from Delon & Desolneux 2022) to demonstrate that the baseline failure pattern generalizes beyond GloVe.
- Attempt to scale baselines to larger N (e.g., 10K–20K) using entropic regularization or stochastic approximations, even if not to 200K, to provide a more informative comparison.
- Ablation studies on NeuralGW components (the P matrix, the f network, the min-max-min structure).
- Report training times and scalability characteristics.
- Explicitly relate NeuralGW to adversarial OT methods (e.g., Kanotorovich, WGAN) to clarify novelty.

## Removed Points

These points are flagged for removal; treat them with caution.

- **Criticism that the paper does not cite adversarial word translation methods or that baselines are not SOTA for unsupervised alignment.** The paper is about GWOT solvers, not general alignment. The selection of StructuredGW, FlowGW, and AlignGW as baselines is appropriate because these are the existing continuous GWOT methods. Scope creep.

- **Claim that "(un)correlatedness is not properly defined."** The paper defines both concepts clearly in Section 4.1 (lines 182–193): uncorrelated = independent samples from P and Q; correlated = samples from a coupling π ≠ P⊗Q, then permuted. The definition is present and coherent. The α construction could be clearer, but the concept itself is properly defined.

- **Criticism that the paper's flow is disorganized.** The structure (Intro → Background → Related Work → Limitations with experiments → Proposed Method → Discussion) is standard for a benchmark+criterion+method paper and is coherent.

- **Complaints about plot resolution, missing legends, or formatting.** These are parser artifacts from the PDF extraction; the original submission does not have these issues. Per hard rules, remove pure formatting nitpicks.

- **Request for "more comprehensive survey" of continuous GW solvers.** The paper identifies three existing continuous GW solvers, which is a complete and appropriate set for this benchmark.

## Novel Insights

The harsh critic's observation that the paper conflates two different questions—"do baselines fail on uncorrelated data?" (well-supported by Figure 2) and "does NeuralGW solve this better?" (not well-supported due to the 3K vs 200K disparity)—is an insightful framing. The paper's real contribution is in cleanly demonstrating the first question, and the review should treat these as two separate claims with different evidentiary standards. Additionally, the strength finder correctly notes that the paper's candid acknowledgment of its own limitations (NeuralGW's instability, data hunger, unfair comparison) is a strength that future work can build on, even if the method's current validation is insufficient.

## Suggestions

1. **Clarify what the paper's core contribution is.** The benchmark finding (baselines fail on uncorrelated data) stands on its own evidence and is the paper's strongest result. Consider reframing NeuralGW as a preliminary proof-of-concept rather than a validated solver, and downplay direct cross-comparison claims until the comparison can be made fair.

2. **Define the evaluation metric explicitly.** State whether it is the GW distance (innerGW²₂), the test-set GW objective value, or some other measure.

3. **Either scale baselines up or NeuralGW down** to enable a controlled comparison at the same training set size. An experiment with NeuralGW at 3K samples (even if performance is poor, as the paper hints) would be informative as an ablation.

4. **Clarify the α construction mathematically** and verify that the marginal distributions are preserved across all α values.

5. **Discuss scope limitations regarding the cost function.** Explicitly state whether the correlatedness findings are expected to hold for squared Euclidean GW or other cost functions.

## Score and Decision

**Originality**: 6/10 — The correlatedness insight is novel and useful.
**Importance of research question**: 7/10 — Timely for the growing GWOT community.
**Claims support**: 5/10 — Benchmark claims are well-supported; method claims are not.
**Soundness of experiments**: 5/10 — Baseline experiments are sound; NeuralGW comparison is not controlled.
**Clarity of writing**: 4/10 — Undefined metric, unclear α description.
**Value to research community**: 6/10 — Useful benchmark results that can inform future work.

The paper's core contribution—identifying and demonstrating the correlatedness dependency of existing GWOT solvers—is genuine and supported by controlled experiments. However, the proposed NeuralGW method is insufficiently validated, and its comparison against baselines uses a ~67× data-size disparity that invalidates claims of superiority. The paper would be stronger as a pure benchmark paper. I recommend borderline acceptance for the benchmark contribution, conditional on the authors addressing the metric definition and toning down claims about NeuralGW's superiority.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>