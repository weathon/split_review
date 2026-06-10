## Summary

This paper formulates the dynamic pricing of sequentially displayed complementary items (e.g., flight tickets with ancillary baggage fees) under sales constraints and unknown demand as an online Constrained Markov Decision Process (CMDP). It proposes PD-DP, a primal-dual algorithm combining online mirror descent on occupancy measures with projected gradient descent on the Lagrangian multiplier, with an optimistic biased estimator and confidence-set-based transition estimation. The environment parameters are estimated from ~4M rows of real user data from lastminute.com.

## Strengths

- **First CMDP formulation for this specific problem domain.** The paper identifies a genuine gap: existing dynamic pricing work does not model the sequential display of complementary items under sales constraints as a CMDP. The MDP structure with 7 states across 4 layers (Section 2.1) is a non-trivial modeling choice that captures the pricing funnel for complementary products, including the partial observability between states x₁ and x₂.

- **Concrete algorithmic adaptation for the partial observability issue.** The paper identifies that during inference, the website cannot distinguish between states x₁ and x₂ (the purchase decision is only revealed at episode end). The convex-combination policy weighted by a dynamically estimated α (Section 3.3.3, Section 4.3) is a specific, problem-driven adaptation not present in standard CMDP algorithms.

- **Evaluation grounded in real-world data.** The simulation parameters are estimated from ~4 million rows of actual user data from lastminute.com (Section 4.1), with described preprocessing, K-Means clustering, and estimation of transition probabilities from the "status" feature (Sections 4.1–4.3). This grounds the experiments in industry data rather than purely synthetic settings.

## Weaknesses

### Major

- **Abstract promises baseline comparisons that do not exist.** The abstract explicitly states the approach is evaluated "against well-known baselines optimizing each state singularly" (line 4). Section 4.5 contains only a single figure showing the proposed algorithm's own cumulative regret and violation curves — no baselines, no alternative methods, no comparisons. This means there is zero empirical evidence that the proposed algorithm outperforms simpler alternatives (e.g., independent pricing per item, static pricing from historical data, or unconstrained variants). For a paper whose central methodological claim is that "optimizing the pricing of each item individually is ineffective" and that the CMDP formulation is superior, the absence of any comparison to individual optimization is a critical evidential gap.

- **Extremely thin empirical evaluation.** The entirety of the experimental results is one figure (Figure 2) covering a single configuration: 2 discretized prices per item, 2 clusters (70%/30% split), no error bars, no multiple random seeds, no statistical tests. The action space is 2×2 = 4 state-action pairs, trivializing the learning problem. With only one figure and no replication information, the reader cannot assess the stability or reliability of the reported results. For a paper at a top conference, this level of empirical evidence is far below the standard.

- **Non-stationarity claimed but not tested.** The abstract and introduction prominently claim the approach handles non-stationary demand (lines 4, 14, 16), and the paper notes that rewards and constraints "may be stochastic...or highly non-stationary" (line 42, 47). However, the experimental setup (Section 4.3) estimates all parameters from historical data and fixes them for the simulation. There is no description of how non-stationarity is induced, what form it takes, how the algorithm responds differently under stationary vs. non-stationary conditions, or any experiment involving drifting or shifting demand. A central claimed capability is left entirely unvalidated.

- **No theoretical guarantees.** The paper defines cumulative regret and cumulative constraint violation (Section 4.4) and states "in an online learning algorithm, $R_T = o(T)$ and $\bar{V}_T = \bar{o}(T)$" — but provides no theorem, no bound, and no proof. For a paper positioned within the online CMDP literature, where regret and violation bounds are standard currency, the absence of any formal analysis is a major omission. The observation that regret "grows sublinearly" in one experiment (Section 4.5) is an empirical claim, not a theoretical guarantee, and conflates two different standards of evidence.

### Minor

- **No conclusion or discussion section.** The paper ends abruptly at the end of Section 4.5 (line 269). There is no summary of findings, discussion of limitations, acknowledgment of the thin evaluation, or directions for future work. This makes the paper feel incomplete.

- **"Rewards affect transitions" — ambiguous modeling description.** The paper states "rewards affect transitions" (line 42) and then describes how zero vs. non-zero reward determines the next state (lines 44–45). In a standard MDP, the transition function $P$ encodes dynamics and rewards are consequences. The paper's description conflates the two, suggesting the reward *is* the observation revealing the transition. This is more like a partially-observable or stochastic-reward setting than the paper acknowledges. The model can be clarified: the purchase event determines both reward and transition jointly, which is fine, but the presentation invites confusion about whether this is a standard MDP or a different structure.

- **Novelty slightly overstated given component-wise provenance.** The paper claims "the first work to employ the online CMDP mathematical framework to solve dynamic pricing scenarios" (line 16). The algorithmic components are adapted from (Jin et al., 2020) for the primal optimizer, (Stradi et al., 2024b) for the Lagrangian framework structure, and standard OGD for the dual. The novel elements are the specific CMDP formulation, the optimistic biased estimator adapted for bandit feedback with unknown transitions, and the partial-observability convex combination. The paper does not clearly delineate what is novel versus what is adapted, and the contribution is more in the application and integration than in fundamentally new algorithmic ideas.

### Trivial

- The phrase "sample experiment" (Section 4.5, line 264) suggests there may be additional experiments not shown, which is confusing given this is the only evaluation section.

## Nice-to-Haves

- Add baseline comparisons against independent pricing per item, static pricing, and unconstrained variants.
- Expand experiments with multiple seeds, error bars, more price points, longer horizons, and explicit non-stationary demand regimes.
- Provide at least a coarse theoretical regret/violation bound ($O(\sqrt{T})$ or similar) connecting the algorithm to the online CMDP theory it builds on.
- Ablate the partial observability convex-combination mechanism by comparing against fixed α values and merged-state alternatives.
- Add a conclusion/discussion section.

## Removed Points

The following points from the inputs were removed with justification:
- *Pseudocode rendering / missing Algorithm 1* — Text-extraction artifacts from PDF parsing; the original PDF likely contains clearly formatted algorithms.
- *OCR artifacts in Section 4.4* — Parser artifacts, not author errors.
- *Missing related works* — Per instructions, cannot judge related work completeness without external knowledge.
- *Formatting/style nitpicks* — Parser-induced issues, not author errors.
- *Strength: "Empirical demonstration of sublinear regret"* — Conflicts with verified weakness (no baselines, single figure, no error bars); the demonstration is insufficiently evidenced to count as a strength.
- *Strength: "Rigorous confidence-set estimation"* — Follows (Jin et al., 2020) closely; describes standard methodology rather than a distinctive contribution.
- *Criticisms about missing appendix content / proofs not included* — Parser strips appendices; these exist in original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews predominantly surface concerns about insufficient evidence rather than providing novel analytical perspectives on the work.

## Suggestions

1. **Add baseline comparisons as a bare minimum.** Without comparisons to independent pricing optimization, static policies, or simpler bandit approaches, the paper cannot support its central claim that the CMDP formulation is beneficial. This is the single most critical missing piece.

2. **Substantially expand the evaluation** to include multiple random seeds (with error bars/confidence intervals), more than 2 price levels per item, explicit non-stationary demand scenarios, and at least one additional dataset or configuration.

3. **Add a theoretical section** with regret and violation bounds, even if coarse. The paper defines the metrics and borrows machinery from Jin et al. (2020); it should connect the algorithm to the theoretical framework.

4. **Add a conclusion section** discussing limitations, the scope of the evaluation, the scalability of the approach, and directions for future work.

5. **Clearly delineate novel contributions** from off-the-shelf components, and tone down claims about handling non-stationarity until it is experimentally demonstrated.

## Score and Decision

The core formulation and algorithm are reasonable, and grounding in real-world data is a positive. However, the paper suffers from critical evidential gaps: the abstract promises baseline comparisons that never appear, the evaluation is limited to a single figure with no error quantification, the central claim about handling non-stationarity is untested, and no theoretical guarantees are provided despite the paper's positioning in the online learning literature. The paper is not ready for publication at a top conference in its current form.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>