Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated review.

## Summary

This paper introduces "causal exploration," a framework for task-agnostic reinforcement learning that leverages causal knowledge to improve both data collection efficiency and world model reliability. The approach combines three components: (1) an online causal discovery method with selective data collection, (2) a sharing-decomposition architecture for incorporating causal structure into the world model without explosive parameter growth, and (3) an exploration policy driven by intrinsic rewards that combine prediction error and an active reward measuring data quality. Theoretical analysis (Theorem 1) claims an exponential convergence advantage when the causal graph is sparse, and experiments on synthetic data, traffic signal control, and MuJoCo tasks show consistent improvements over non-causal and causal baselines.

## Strengths

1. **Comprehensive empirical validation across diverse domains.** The paper evaluates on synthetic environments with varying state/action dimensions, a traffic signal control task (Table 1), and MuJoCo tasks including high-dimensional Humanoid-v2 (Figure 6). Results consistently show lower prediction errors and better downstream policy performance compared to Curiosity, Plan2Explore, CID, ASR, and CDL. This breadth of evaluation strengthens the claim of general applicability.

2. **Sharing-decomposition architecture (Section 4.1).** The paper identifies a practical obstacle — training n separate networks for n state dimensions would be computationally prohibitive — and proposes a weight-sharing scheme (shared embedding layers + decomposed per-dimension heads) that makes causal structural constraints feasible in the world model without parameter explosion. This is a concrete engineering contribution that addresses a real bottleneck.

3. **Efficient online causal discovery (Section 4.2).** The use of gradient-based minibatch similarity and diversity criteria to selectively collect data for causal discovery is a practical innovation. Figure 3 shows that this selective approach achieves higher F1 scores than alternatives (ASR, CDL, random selection), demonstrating that data quality can compensate for quantity in causal structure learning.

4. **Honest scope and baseline characterization.** Table 1 explicitly catalogs which attributes (causal knowledge, explicit structural embedding, online causal discovery, non-random data collection) each method possesses, providing readers with a clear understanding of where the proposed method differs from prior work and where it does not claim novelty.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims — that causal knowledge can improve world model learning efficiency — are supported by consistent empirical evidence across multiple domains. The weaknesses below are addressable in a revision.

### Minor

1. **Missing measures of variability in experimental results.** Figures 4, 5, and 6 plot only mean curves over 10 runs without error bars, confidence intervals, or statistical significance tests. Without this information, the reader cannot assess whether the reported improvements (e.g., the gap between Causal Exploration and CDL in Figure 4) are reliable or within run-to-run noise. The paper states "10 experiments and take the average value to reduce the impact of randomness" but does not report the variance. This is the most impactful weakness because it weakens the central empirical claim.

2. **Active reward formulation is underspecified in key details.** The active reward (Eq. 7–8) is defined as the change in mean prediction error on a test set $\mathcal{D}_h$ before and after training on a new sample. However:
   - The exact mechanism for collecting $\mathcal{D}_h$ ("episodes unseen before training" collected "at the start of each episode") is ambiguous: are these held-out episodes collected once at the beginning, or freshly collected each episode? The latter would introduce distribution shift.
   - The paper provides no analysis of the noise or stability of this reward signal. Since $r^a$ is a difference of two test-set averages, its magnitude and sign depend on the size and composition of $\mathcal{D}_h$.
   
   This does not invalidate the method (ablation studies are mentioned), but it makes reproduction harder than necessary.

3. **The gradient-based data selection for causal discovery could be clearer about potential feedback loops.** Section 4.2 uses gradients $\nabla f_{\boldsymbol{w}^c}(b^i_t)$ from the world model to select data for conditional independence testing. Since the same world model is being trained on data selected by its own gradients, there is a potential feedback loop that could bias the identified causal graph toward the model's current (possibly incorrect) beliefs. The paper does not discuss this or provide analysis of its impact. This is not a fatal flaw — many active learning methods share this property — but it should be acknowledged.

### Trivial

- The paper notes in Section 6.1 that the lower $y$-intercept of causal exploration curves is due to the causal model having fewer input dimensions. This is an honest acknowledgement, but the framing in the abstract ("causal exploration aids in learning accurate world models using fewer data") could more clearly separate this architectural advantage from the exploration advantage.

## Nice-to-Haves

- A wall-clock time comparison or complexity analysis would help contextualize the computational cost of the KCI-based causal discovery step, especially in high-dimensional MuJoCo tasks.
- An ablation isolating the effect of the active reward ($r^a$) from the prediction-error reward ($r^i$) would clarify which component drives the improvement.
- Brief summary of the key ablation findings (mentioned in Section 5.1 but whose details appear deferred) in the main text would help readers assess robustness claims without consulting supplementary materials.

## Removed Points

The following criticisms from the reviews were removed or downgraded per the filtering rules:

- **Theorem 1 missing proof / insufficiently justified.** The critic claimed the theorem is presented without proof or sketch and that the bound conflates δ with the convergence rate. The proof existed in the appendix (which is stripped by the parser; rule explicitly requires removing weaknesses about missing proofs in appendix). The bound's structure — two inequalities where the second follows from substituting the standard GD bound into the first — is algebraically coherent; the substantive claim is the first inequality, whose justification resides in the now-stripped appendix.

- **Pseudocode "bug" ($t=0 \pmod N$).** The notation $\texttt{\$t=0 \pmod N\$}$ is standard LaTeX for "t ≡ 0 (mod N)" and is mathematically correct. The reviewer's suggested "t mod N == 0" describes the same condition in a different syntax.

- **Initial iteration advantage is an artifact.** The paper explicitly acknowledges and explains this (Section 6.1: "This is because the integration of causal matrix $D$ into the model exclusively incorporates the parent nodes and eliminates extraneous input information"). The reviewer's characterization as a hidden flaw misreads the paper's own transparent discussion.

- **Sharing-decomposition is a standard multi-head design.** This is an opinion, not a weakness. The contribution is not claiming architectural novelty at the neuron level but rather showing that causal constraints can be made computationally feasible via weight sharing.

- **Comparison with CID/CDL is uneven.** The paper's Table 1 honestly catalogs differences across all methods. The reviewer's critique amounts to saying the baselines have different design goals — which is precisely why the table exists, and why the paper does not claim superiority on every axis.

- **Active reward per-step overhead not discussed.** The test set $\mathcal{D}_h$ is collected "at the start of each episode," not at every step. The overhead is bounded per-episode and the paper presents this as part of the algorithm's cost, which is standard.

## Novel Insights

The key insight that emerges across both reviews is that the paper's integration of causal knowledge operates at two distinct levels — architectural (reducing the input space of the world model via the causal matrix) and behavioral (guiding exploration via gradients and active rewards) — but the empirical evaluation does not fully disentangle their contributions. The consistent improvements at the *first* iteration (before any exploration has occurred) suggest that a substantial portion of the reported benefit may stem from the architectural advantage of the causal world model rather than the exploration policy itself. A cleaner separation of these two sources of improvement would strengthen the paper's central narrative about *exploration* efficiency specifically.

## Suggestions

1. **Add error bars or confidence bands to all experimental figures.** At minimum, report standard deviation or standard error across the 10 runs. Where feasible, include a statistical significance test (e.g., paired t-test or Mann-Whitney U) for the primary comparisons with the strongest baseline (CDL).

2. **Clarify the active reward mechanism.** Specify (a) whether $\mathcal{D}_h$ is collected once at the beginning or freshly each episode, (b) its size relative to the training buffer, and (c) its stability across training. A brief empirical characterization (e.g., distribution of $r^a$ values over time) would suffice.

3. **Acknowledge the feedback loop in online causal discovery.** Add a sentence in Section 4.2 noting that using the world model's gradients for data selection creates a dependency between the model and the discovered graph, and discuss (or reference an ablation showing) whether this has observable effects on the identified causal structures.

## Score and Decision

This paper presents a well-motivated integration of causal knowledge into task-agnostic RL with a practical architectural contribution (sharing-decomposition), a sensible online causal discovery pipeline, and consistent empirical improvements across multiple domains. The theoretical analysis is a stated contribution but cannot be fully assessed from the main text alone. The primary weakness is the absence of error bars, which makes it harder to gauge the reliability of the reported improvements, but this is addressable and does not invalidate the consistent directional evidence. The paper makes a real contribution to the intersection of causal discovery and exploration in RL.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>