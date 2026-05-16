I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces the problem of communicating through actions within an MDP, treating the environment as a finite-state channel (FSC). It makes two contributions: (1) an information-theoretic characterization of the capacity-reward trade-off — a single-letter capacity expression (Theorem 1) and a convex optimization over occupation measures (Theorem 2) — and (2) Act2Comm, a transformer-based practical coding scheme that embeds messages into decision rules while approximately maintaining a target policy's reward. The theoretical work is novel and sound; the practical scheme is clever but insufficiently validated.

## Strengths

- **Single-letter capacity characterization for the action-state channel (Theorem 1)**: Derives capacity as conditional mutual information \(I(X;S^{+}|S)\) — a non-trivial result given that exact single-letter expressions for general FSC capacities are rare and typically unavailable. The insight that capacity can be achieved by a stationary randomized policy, without history dependence, is clean and surprising.

- **Convex formulation of the capacity–reward trade-off (Theorem 2, Lemma 1, Lemma 2)**: Formulates the trade-off as a convex optimization over occupation measures with a closed-form gradient (equation 9), enabling efficient numerical solution. Lemma 1's concavity proof implies the achievable rate-reward region is convex — theoretically elegant and practically useful for navigation of the trade-off surface.

- **Act2Comm framework for non-differentiable FSCs**: The channel transform to an extended action-state (EAS) channel combined with the iterative training strategy (critic network estimating gradients through the non-differentiable channel and quantizer) is a clever architectural contribution that addresses a genuinely hard problem: joint encoder-decoder training over a non-differentiable channel.

- **Realistic communication model**: By assuming the receiver sees only the state sequence (not actions), the paper departs from prior work (e.g., Sokota et al. 2022) that required action observability, broadening applicability to settings where actions are private — a well-motivated and practical modeling choice.

- **Block-attention feedback coding mechanism**: The partitioning of messages into blocks with feedback matrices (Section 5.2) is a thoughtful design grounded in established coding theory for the finite-blocklength regime.

## Weaknesses

### Fatal

None. The theoretical results are valid and no claims are fabricated.

### Major

- **No baselines in the experiments**: Act2Comm is evaluated in isolation. There is no comparison to any alternative scheme — not a repetition code, not a block code, not a random coding baseline, not even the trivial stationary-policy-with-no-communication case (beyond the \(\lambda \to \infty\) limit already shown). Without baselines, the reader cannot judge whether Act2Comm's trade-off curves (e.g., rate 0.2 bit/step with BER near zero at reward 1.5 from Fig. 4a) represent good performance or not. The paper's claim that experiments "validate Act2Comm's capability" is uncalibrated without a reference point. This is the single biggest gap in the evaluation.

- **No comparison to the paper's own theoretical bound**: Theorem 2 provides an upper bound \(C(V)\) on achievable rate for a given reward constraint. The natural and expected validation is to plot Act2Comm's achieved rate-reward pairs against this bound to show how close the practical scheme gets to optimality. This comparison is entirely absent. The theoretical and experimental halves of the paper are disconnected — the theory section stands alone and the experiments never reference it back. Adding this comparison would both validate Act2Comm and demonstrate the practical relevance of the theoretical characterization.

- **Insufficient experimental rigor**: Only two small MDPs are tested (3 states/2 actions, 27 states/3 actions). No error bars, confidence intervals, or standard deviations are reported for any metric. The paper does not state how many random seeds or independent runs were used. Given the stochasticity of both the environment and neural network training, single-point curves without variance estimates are not trustworthy. For a paper presenting a learning-based coding scheme, this level of validation falls below the norms of the field.

### Minor

- **Limited scope of experimental validation**: Both environments are small tabular MDPs. The paper speculates about Act2Comm as a "plug-in component" for general MDP/RL applications (Section 7), but provides no evidence on larger domains, continuous states, or more complex dynamics. A single larger MDP (e.g., 50+ states) would substantially strengthen the scalability claim.

### Trivial

- **"Optimal" wording in the introduction** (line 18): "We first characterize the optimal information theoretic trade-off" — the characterization is given as a convex optimization (Theorem 2) rather than a closed-form expression. The capacity is indeed the fundamental limit, so the statement is accurate in spirit, but the phrasing slightly oversells.

## Nice-to-Haves

- **Plot Act2Comm's rate-reward against the theoretical bound** \(C(V)\) from Theorem 2 — the single highest-impact addition.
- **Add a simple baseline**: e.g., a repetition code that repeats the target-policy action n times, with majority-vote decoding from observed states.
- **Report error bars** across at least 5 independent seeds for all figures.
- **Include one larger MDP** (50+ states, 5+ actions) to demonstrate scalability.
- **Clarify whether the receiver knows the codebook** — standardly assumed in channel coding, but stating it explicitly would help.
- **Add a limitations paragraph** discussing key assumptions (receiver knows codebook, need for pre-determined target policy, sensitivity to \(\lambda\), decoder access to exact state sequence).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Critic network — why is this needed?"**: The paper clearly explains (Section 5.5(a)) that the critic estimates gradients through the non-differentiable EAS channel. This is a strawman.
- **"Decoder loss not specified in main text"**: The paper specifies \(\mathcal{L}_{com}\) as cross-entropy (line 198). The claim is inaccurate.
- **Missing appendix / architecture details**: Per instructions, parser-stripped appendix material is assumed present in the original submission; these are not missing from the paper.
- **Reproducibility hyperparameter nitpicks**: Per instructions, removed as nitpicks about undisclosed hyperparameters that would appear in the appendix.
- **Missing related works**: Per instructions, I cannot confirm the existence of omitted references.
- **Formatting/typo/style nitpicks**: Per instructions, removed as parser artifacts.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the striking gap between the paper's strong theoretical contribution (a computable single-letter bound for a non-trivial FSC class) and its practical evaluation, which entirely fails to connect back to that theory. It is unusual — and a missed opportunity — to derive a tractable bound and then not use it as a benchmark for one's own method. This disconnect suggests that the paper is effectively two separate contributions; bridging them with a bound-comparison plot would dramatically strengthen the manuscript.

## Suggestions

1. **Add baselines** — a repetition code baseline is the most natural and would require minimal implementation. It would immediately contextualize Act2Comm's performance.
2. **Plot Act2Comm results against the theoretical bound** \(C(V)\) from Theorem 2, solving it via the gradient in Lemma 2. This directly connects the two halves of the paper and quantifies the optimality gap.
3. **Report variance** across multiple seeds for all experiments.
4. **Add one larger MDP** to demonstrate scalability.
5. **Add a limitations paragraph** to the conclusion.

## Score and Decision

The theoretical contribution is genuinely novel and well-executed. The problem formulation is interesting and underexplored. The Act2Comm scheme is architecturally clever. However, the experimental evaluation is substantially below the standard expected for a paper that claims both theoretical and practical contributions: no baselines, no connection to the paper's own theoretical bound, no statistical rigor, and only two tiny MDPs. The empirical claims made in the abstract and conclusion are not adequately supported. In its current form, the paper does not meet the bar for acceptance. The authors should either (a) substantially strengthen the experiments with baselines, bound comparison, error bars, and at least one larger domain, or (b) reframe the paper as primarily a theoretical characterization with a preliminary proof-of-concept and adjust the claims accordingly.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>