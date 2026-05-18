Now I have a comprehensive understanding of the paper. Let me write the consolidated review.

## Summary

The paper proposes Stochastic Gradient Discrete Langevin Dynamics (SGDLD), the first practical method for stochastic gradient MCMC sampling in discrete spaces. The core algorithmic innovations are: (1) a gradient caching scheme that accumulates mini-batch evaluations across consecutive rejected steps to obtain an asymptotically unbiased estimate of the probability ratio, and (2) a modified Polyak step-size adaptation that normalizes simulation time by the local jump rate to handle enormous variance in stochastic gradients. Experiments on two synthetic tasks and three real-world applications (Bayesian logistic regression, stochastic facility location, approximate computing, prompt tuning) show that SGDLD matches or outperforms strong baselines with substantially lower computational cost.

## Strengths

1. **Gradient caching corrects the bias in naive stochastic ratio estimation.** The paper clearly identifies that a naive stochastic gradient does not yield an unbiased estimator of the rate matrix in discrete spaces (Eq. 10–11), since expectation and the nonlinear weight function \(g\) do not commute. The cache accumulates mini-batch evaluations across consecutive steps where the state does not change (Eq. 12), effectively expanding the batch size without additional computation. Proposition 4.1 states asymptotic unbiasedness, and Figure 2 confirms empirically that SGDLD's total variation decreases with step size while the no-cache variant's does not — direct evidence that caching resolves the bias.

2. **Polyak step-size adaptation addresses the multi-order-of-magnitude variance in jump rates.** The paper motivates this with empirical evidence (Figure 1) showing that the stochastic jump rate can vary by \(\sim 10^{30}\) across mini-batches, making a fixed step size infeasible. The Polyak normalization (Eq. 14) adapts \(\epsilon_t\) to the local jump rate \(Z(x)\). The ablation study (Figure 3) shows SGDLD dramatically outperforms SGDLD-noP, and the paper notes SGDLD-noP cannot produce reasonable solutions in the three real applications, underscoring the practical necessity of this component.

3. **Broad empirical validation across diverse discrete-space problems.** SGDLD is evaluated on two synthetic tasks (Gaussian-Bernoulli, Bayesian logistic regression) and three real applications (facility location, approximate computing, prompt tuning). In each case it matches or surpasses strong baselines (DLMC, Gibbs, Gurobi, SLS, continuous relaxation), often using orders of magnitude fewer function evaluations (e.g., 10k vs. 100M for training-based methods in approximate computing).

4. **Clear problem formulation.** The paper formally defines "stochastic distribution" (Eq. 6) with illustrative examples (quenched model, Bayesian learning), precisely identifies the two obstacles (bias from non-exchangeability and variance from exponential-scale gradients), and provides a principled convergence analysis for the naive stochastic DLD under an unbiased estimator.

## Weaknesses

### Fatal

None.

### Major

1. **Gap between advertised convergence claim and delivered theoretical content.** The introduction states: "With proper annealing, we can prove that SGDLD samples from the correct distribution." However, the main text does not state a theorem about the convergence of the **full SGDLD algorithm** (caching + Polyak step size + schedule). The paper provides: (a) a convergence analysis for naive DLD assuming an unbiased rate matrix estimator exists (Section 3.2), and (b) Proposition 4.1 asserting asymptotic unbiasedness of the caching scheme (proof deferred). But there is no theorem that combines these components, specifies conditions on the schedule \(h_t\), and characterizes the limiting distribution of the full algorithm. Even a theorem statement (with proof in appendix) would bridge this gap. As presented, the theoretical framing in the introduction oversells what the main text delivers, which weakens the paper's claimed contribution.

### Minor

1. **Connection between step-size decay and effective cache size is asserted but not argued.** The paper's intuition is that as \(\epsilon \to 0\), the chain remains at the same state for many steps, allowing the cache to accumulate. Proposition 4.1 claims asymptotic unbiasedness under this dynamic. However, no argument is given for how the step-size decay schedule connects to the effective cache size or the bias decay rate. The claim that the bias vanishes with \(\epsilon\) requires linking the Polyak-controlled step size to the number of cached mini-batches, which is not addressed.

2. **Polyak step-size schedule is underspecified.** The paper says: "set a threshold \(h^*\) and gradually decrease \(h_t\) until it reaches \(h^*\)." How \(h_t\) is decreased (linearly, exponentially, or otherwise) is not stated. Since the algorithm's behavior depends on this choice, this omission hurts reproducibility.

3. **Prompt tuning experiment lacks details on discrete representation.** The paper samples "text prompts \(x\)" in a discrete space but does not describe how prompts are represented as elements of \(\mathcal{X}\), what the neighborhood structure \(N(x)\) is, or how the gradient approximation \(\exp(\langle \nabla\log\pi(x), y-x\rangle)\) is computed over token sequences. This information is essential for reproducibility.

4. **The \(10^{30}\) claim about jump-rate ratios lacks quantitative backing.** The paper states that "the largest jump rate can be \(10^{30}\) times the smallest jump rate" (Figure 1 caption and line 137) based on 200 mini-batches in the Bayesian logistic regression task. No computation or derivation is provided to support this striking figure, making it unverifiable from the main text.

5. **Gradient approximation for \(Z(x)\) is acknowledged but its effect is unexplored.** The paper notes that calculating \(Z(x)\) exactly is expensive, so a gradient approximation is used (following Grathwohl et al., 2021). The Discussion (Section 7) explicitly states that this approximation breaks the unbiasedness guarantee. This is an honest limitation, but the paper does not investigate empirically how this approximation affects sampling quality or whether it introduces systematic bias in practice.

### Trivial

None.

## Nice-to-Haves

- The pseudo-marginal MCMC baseline is mentioned as an "extra experiment" but not included in the main text. Including it (or a brief summary) would strengthen the empirical comparison.
- A small-scale analytical verification of the caching bias reduction (e.g., computing the bias of the naive and cached estimators on a tiny problem where the expectation is tractable) would provide a clean proof of concept complementing the empirical results.
- More details on the neighborhood structures used in the three real applications would improve reproducibility.

## Removed Points

These points from the reviews are removed with justification:

- **"No proof or proof sketch for Proposition 4.1 in main body."** — Removed per rules: proofs deferred to appendix are standard and the parser strips appendix content. The proposition statement itself is in the main text.
- **"Section 3.2 assumes an unbiased estimator of R exists, which does not hold."** — Removed: the paper is explicitly setting up the naive baseline and then identifying why it fails (Eq. 10–11). This is problem setup, not a flaw.
- **"The caching estimator is not unbiased (only asymptotically)."** — Removed: Proposition 4.1 claims *asymptotic* unbiasedness, which is precisely what caching achieves. The reviewer conflates finite-sample bias with asymptotic bias.
- **Pure formatting/style nitpicks and wording complaints.** — Removed per Hard Rules.
- **"The paper should cover additional tasks/domains."** — Removed as scope creep; the paper already covers 5 distinct tasks across diverse domains.

## Novel Insights

The reviews surface an interesting observation beyond the paper's own contributions: the paper's two techniques (caching and Polyak step size) address two fundamentally different failure modes of naive stochastic DLD — bias and variance — and these are somewhat orthogonal. The caching scheme targets the non-exchangeability of expectation and nonlinearity (the bias problem), while the Polyak adaptation targets the exponential-scale variation in jump rates (the variance problem). This decomposition suggests that future improvements could address each axis independently: variance-reduced gradient estimators could further improve the caching scheme, and more sophisticated adaptive step-size rules (beyond the simple Polyak schedule) could further stabilize the variance. The paper's framework cleanly separates these concerns, which is a valuable conceptual contribution in itself.

## Suggestions

1. **Add a theorem statement for the full SGDLD algorithm** in the main text (even if the proof is deferred to the appendix). Specify: (a) conditions on the schedule \(h_t\) and the likelihood ratio bound, (b) the claim about the limiting distribution, and (c) any caveats about the gradient approximation for \(Z(x)\). This would align the introduction's promise with the paper's content.

2. **Specify the Polyak schedule** (e.g., linear decay, exponential decay, or cosine schedule) and provide the default parameters used in experiments.

3. **Provide reproducibility details for the prompt tuning experiment:** how prompts are tokenized, the neighborhood structure over prompt sequences, and how the gradient approximation is computed.

4. **Include a brief computation or reference** supporting the \(10^{30}\) claim, or soften the phrasing.

5. **Add a small experiment** investigating whether the gradient approximation for \(Z(x)\) introduces measurable bias compared to exact computation, at least on one of the synthetic tasks where exact computation is feasible.

## Score and Decision

The paper addresses an important and genuinely open problem — stochastic gradient MCMC in discrete spaces — with a well-motivated algorithm and strong empirical validation across diverse tasks. The caching scheme and Polyak adaptation are simple, practical, and clearly shown to address the identified challenges. The main weakness is a gap between the introduction's promise of a convergence proof for the full algorithm and the theoretical content actually presented. However, this gap is bridgeable (it requires stating a theorem that likely exists in the appendix), and the empirical evidence convincingly demonstrates the algorithm's practical effectiveness. The contributions are significant enough to warrant acceptance.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>