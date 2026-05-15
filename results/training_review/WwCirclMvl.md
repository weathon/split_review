Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes LMC-PPS, the first framework using Langevin Monte Carlo for approximate posterior sampling in offline RL. For linear (low-rank) MDPs, it provides frequentist sub-optimality bounds that are data-adaptive, interpolating between worst-case and best-case scenarios, and improve over LCB-based methods by a √d factor in confidence scaling. For general MDPs with overparameterized neural network function approximation, it introduces a creative two-phase algorithm (training the network with GD, then applying LMC on an auxiliary linear model for perturbation) and proves bounds scaling with the effective dimension. Empirical results show competitive performance on linear MDPs and non-linear contextual bandits.

## Strengths

- **First LMC-based algorithm for offline RL with frequentist guarantees**: Prior posterior-sampling work for offline RL (Uehara & Sun, 2021) provided only Bayesian bounds and no tractable algorithm. This paper introduces a concrete, implementable approach using Langevin Monte Carlo and proves high-probability frequentist (worst-case) sub-optimality bounds — a strictly stronger guarantee than the Bayesian bounds of prior work. (Abstract, Section 1)

- **Tighter confidence scaling and data-adaptive bounds for linear MDPs**: The confidence parameter √τ scales as √d (not d), saving a √d factor over LCB-based methods (e.g., PEVI). The bound depends on the eigenvalue structure of the empirical covariance matrix, interpolating from Õ(H²d√(Cπ/K)) to Õ(H²√(dCπ/K)), which nearly matches the tabular lower bound in the best-case scenario. The explanation — that PPS avoids function-space enlargement required by LCB bonus functions — is insightful. (Section 4.1)

- **Creative two-phase algorithmic design for neural networks**: The paper identifies a genuine technical obstacle (adding LMC noise directly to overparameterized network weights destroys the NTK regime) and addresses it by decoupling training (GD) from perturbation (LMC on an auxiliary linear model operating on neural tangent features). This is a novel and thoughtful solution, even if the posterior sampling interpretation is heuristic. (Section 3.2)

- **Neural network bound that avoids scaling with network width**: Theorem 2 yields a bound of Õ(H²d̃√(Cπ/K)) (ignoring lower-order terms) that depends on the effective dimension d̃ rather than the network width m or feature dimension md. This is a meaningful theoretical achievement for a challenging setting. (Section 4.2)

## Weaknesses

### Major

- **Theory-experiment disconnect for the neural algorithm**: Theorem 2 analyzes Algorithm 3, which uses an auxiliary linear model trained with GD+LMC on neural tangent features. However, Section 5 states: "For Neural-LMC-PPS, we directly apply noisy gradient updates to the network, instead of using an auxiliary linear model, to approximate posterior samples." This is a fundamentally different algorithm. The paper claims to "corroborate our theoretical results with numerical evaluations," but the neural experiments do not validate the algorithm analyzed in Theorem 2. This undermines the empirical support for the paper's main neural theoretical contribution. The linear MDP experiments (Figure 1) are correctly aligned with theory, but the neural experiments validate a different heuristic.

- **Overclaimed "posterior sampling" framing for the neural algorithm**: For linear MDPs, LMC with a regularized squared TD loss and Gaussian noise has a plausible connection to Gaussian posterior sampling under a standard prior. For the neural case, the auxiliary linear model approach is a heuristic perturbation method; the paper provides no argument that its outputs correspond to samples from any Bayesian posterior over network parameters given the data. The theoretical analysis (Theorem 2) does not rely on a posterior sampling interpretation — it proceeds via algorithmic stability and concentration. The title and persistent "posterior sampling" framing therefore overstate the contribution. Reframing as "perturbation-based exploration via LMC" would be more accurate for the neural algorithm.

- **Significant practical cost of data splitting not discussed**: The neural algorithm uses data splitting with K′ = ⌊K/H⌋, reducing effective sample size by a factor of H. This introduces an extra √H factor in the bound (H² vs H²·⁵ compared to the linear case). The paper acknowledges the use of data splitting (citing [NTA23]) but does not discuss whether this overhead is avoidable or whether it limits practical applicability. Given that this is a first-order engineering concern, the omission is notable.

### Minor

- **PPS mechanism of pessimism is underspecified in the main text**: The paper states "taking multiple posterior samples and acting pessimistically according to them" but does not clearly specify whether pessimism is enforced by taking the minimum value across samples, constructing a lower confidence bound, or some other mechanism. The bound in Theorem 1 depends on M (number of samples), but the exact decision rule connecting samples to the output policy is not stated in the main text (Algorithm 1 is referenced but not shown; the details may be in the supplementary). This makes the framework harder to evaluate independently.

- **Comparison with [NTA23] is stated without derivation**: The paper claims improvement by a factor of √Cπ over [NTA23] but does not show the baseline bound or provide a side-by-side comparison. While this is common practice, the claim would be strengthened by including the relevant expression from [NTA23] for easy verification.

- **The extra √H gap from data splitting in the neural bound is acknowledged but not analyzed**: As noted above, the H²·⁵ term in the neural bound (vs. H² in the linear bound) stems from K′ = K/H. The paper mentions the gap to optimal bounds in the conclusion but does not discuss whether the data splitting overhead is fundamental or an artifact of the analysis technique. This would be a useful discussion point.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- Evaluating the auxiliary-linear-model algorithm (Algorithm 3) directly, rather than direct-LMC-on-weights, to align experiments with Theorem 2.
- Including standard offline RL benchmarks (e.g., D4RL) to demonstrate scalability to richer domains.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- The harsh critic's claim that "the claimed improvement over [NTA23] is unverifiable" — while the paper does not reproduce the NTA23 bound verbatim, comparative claims against prior work are standard practice and verifiable by consulting the cited paper. This is not a genuine weakness.
- The critic's claim that "the bound in the abstract is an oversimplification" — abstracts are by nature condensed summaries; the full bound with all error terms is in Theorem 2. This is a formatting/presentation nitpick.
- The critic's claim that "the experimental evaluation does not test the proposed algorithm" as a fatal flaw — while the disconnect is real and significant (kept as a major weakness above), the linear experiments do correctly validate the linear algorithm, and the neural experiments validate the general LMC approach even if they test a different variant of it. The severity assessment was overstated.
- The critic's claim that posterior sampling for the linear case is standard — the paper's contribution is in using LMC specifically, which is novel for offline RL. The linear case's connection to posterior sampling is well-established; this doesn't diminish the contribution.
- The Strength Finder's claim of "first tractable posterior-sampling algorithm for offline RL" — this is real but the wording overstates: exact posterior sampling IS tractable for linear MDPs (closed form). The novelty is in using LMC. The strength as stated is kept but reframed appropriately.

## Novel Insights

The most interesting observation that emerges from the reviews is the tension between two design goals in neural offline RL: (1) adding sufficient noise for meaningful exploration/pessimism, and (2) staying within the NTK regime where theoretical control is possible. The paper's auxiliary linear model is a clever resolution of this tension, but the fact that the experiments abandon it in favor of direct LMC on network weights suggests that the theory-practice gap in neural NTK-based analysis remains large. This raises a broader question for the community: are NTK-based analyses of neural RL algorithms describing the actual mechanism by which these algorithms work, or are they providing formal guarantees for a sanitized proxy that practitioners rightfully bypass?

## Suggestions

- Align the neural experiments with the theoretical analysis by implementing and testing Algorithm 3 (auxiliary linear model with GD+LMC) as described in Section 3.2. If the direct-LMC-on-weights heuristic works better in practice, that is itself an interesting finding — but then the paper should explicitly discuss the divergence and its implications.
- Reframe the neural algorithm's description to avoid claiming "posterior sampling" without qualification. The two-phase procedure perturbs the network via LMC on an auxiliary linear model; calling this "approximate posterior sampling" or "perturbation-based exploration via LMC" would be more accurate.
- Clarify the PPS decision rule in the main text: given M posterior samples (or approximate samples), what exactly is the output policy (minimum value over samples? Lower confidence bound?).
- Discuss whether the data splitting overhead (K′ = K/H, adding a √H factor) is fundamental or could be removed by a more refined analysis, since it is a first-order practical limitation.

## Score and Decision

The paper introduces a novel and interesting framework (LMC for offline RL) with a clean linear MDP analysis and a creative auxiliary-linear-model design for neural networks. However, two major issues prevent acceptance: (1) the neural experiments validate a different algorithm than the one analyzed in Theorem 2, breaking the claim of empirical corroboration for the paper's central neural contribution; and (2) the "posterior sampling" framing overreaches for the neural algorithm, which is best described as a perturbation-based heuristic with LMC. These issues are significant enough that they cannot be fully resolved in a rebuttal — they would require either new experiments or substantial reframing. The paper has real research value and could become a strong contribution with revisions, but in its current form, the flaws outweigh the merits.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>