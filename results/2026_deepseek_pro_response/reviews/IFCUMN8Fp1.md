Now let me finalize by comparing against these round-2 anchors:

- **Q00CO1Tm6M (5.75)**: POMDP hardness/tractability theory paper. Deep theoretical contributions, lower bounds, regret analysis. Purely theoretical. Our paper has empirical validation but weaker theory depth. Comparable overall quality.
- **B5kAfAC7hO (5.33)**: POMDP representation learning with theory + experiments. Reviewers flagged limited novelty (heavily builds on prior work) and presentation issues. Our paper has more novel technical contribution but weaker experiments. Comparable.

Our paper sits between these — stronger technical novelty than B5kAfAC7hO (5.33), but not as theoretically deep as Q00CO1Tm6M (5.75). Given the two major weaknesses (missing baselines, toy-scale experiments), I'd place it at **5.5**.

---

## Summary

This paper presents a method for learning discrete POMDP transition and observation matrices from action-observation sequences collected under random exploration. The key technical insight is connecting Predictive State Representations (PSRs) — which learn the POMDP up to an unknown similarity transform — with tensor decomposition methods to recover that transform via joint diagonalization of matrices derived from full-rank actions. The method recovers parameters up to a "full-rank observability partition": states sharing identical observation distributions across all full-rank actions are grouped, and transitions between partitions are recovered. Theorem 1 formalizes the precise guarantees of what is and is not recoverable.

## Strengths

- **Relaxation of per-action observation uniqueness (Section 4.2, Lemma 1).** Prior tensor decomposition methods (Azizzadenesheli et al., 2016; Guo et al., 2016) require distinct observation distributions for every state under each individual action. This paper's joint diagonalization across all full-rank actions simultaneously (Eq. 18) weakens the condition to requiring distinct aggregated observation distributions. Sense-Float-Reset (Figure 1) illustrates a domain where individual actions have repeated observation likelihoods but the method still recovers partition-level parameters.

- **Theorem 1 provides a precise, honest characterization of recoverability.** Rather than hand-waving about limitations, the theorem establishes exactly what the algorithm can and cannot disambiguate: when states share identical observation distributions across all full-rank actions, transitions are recovered correct up to summing over partition indices (Eqs. 13-15). When partitions are singletons, the full POMDP is recovered. This is a clean theoretical contribution.

- **Reward-specification in the noisy hallway domain demonstrates a genuine advantage over PSRs (Figure 4, bottom row).** In the noisy domain, the middle state emits ambiguous observations under both left and right actions, so observation-based reward assignment (the only option for PSR-based planners) cannot distinguish the middle state from a uniform belief — PSR_obs achieves near-zero reward. The paper's state-based reward assignment eventually succeeds once transition matrices converge. This directly validates the claim that explicit transition/observation likelihoods enable post-hoc task specification that PSRs cannot support.

- **Well-constructed running example (Sense-Float-Reset, Figures 1-2).** The domain compactly illustrates all the key challenges: a singular transition matrix (reset), a full-rank transition with non-unique per-action observations (float), and a sensing action that emits different observations without changing state. Figure 2 concretely illustrates Theorem 1.

- **Practical grounding of theoretical assumptions (Section 4.1.1).** The full-rank transition assumption is motivated by standard robotics failure models (p_succ · T + (1−p_succ) · I), and ergodicity is justified by passive sensing actions that break periodic cycles — both common in robot manipulation.

## Weaknesses

### Fatal

None.

### Major

- **Missing empirical comparison against the tensor decomposition methods the paper claims to improve upon.** The paper explicitly positions itself as relaxing the per-action observation-uniqueness assumption of Azizzadenesheli et al. (2016) and Guo et al. (2016) (lines 21-23). Yet neither method appears as a baseline. The only comparisons are against linear PSRs (which do not recover explicit transition/observation parameters and therefore answer a different question) and EM (a decades-old baseline prone to local optima). The core comparative claim — that the method learns a broader class of POMDPs — is empirically unevaluated. Showing that the proposed method succeeds on POMDPs where these prior tensor methods fail (e.g., on Sense-Float-Reset where per-action observations are not unique) would directly validate the central contribution.

- **All experiments are on toy-scale POMDPs (2–4 states) with no evidence of scalability.** The paper is motivated by robot manipulation scenarios (furniture with hidden locking mechanisms, cabinet inference) but the largest experiment uses 4 states. There is no discussion of computational complexity, no runtime measurements, and no diagnostic experiments (e.g., Hankel matrix size vs. state count, memory requirements) that would help a reader assess whether the approach is plausibly extensible. The paper acknowledges scale as future work (line 255) but provides no empirical scaffolding toward that goal. For a learning algorithm paper, some characterization of computational cost is expected.

### Minor

- **L1 transition error metric is ambiguous under partition-level recovery.** Theorem 1 establishes recovery only up to a block-diagonal ambiguity within each observability partition. Computing L1 error against ground-truth transition matrices requires aligning learned states to ground-truth states, but within a partition this alignment is fundamentally arbitrary — there is no observation-based criterion to distinguish states in the same partition. The paper reports transition-matrix L1 error (Figure 3, Row 3) without explaining how states are matched. This does not invalidate the results (planning performance provides an independent evaluation), but the L1 curves should not be taken at face value without a description of the alignment procedure.

- **The directional hallway domain complicates the reward-specification narrative.** In the directional domain (Figure 4, top row), observation-based reward assignment (Ours_obs, PSR_obs) succeeds with far less data than state-based assignment (Ours_state), which requires ~10^7 interactions before achieving parity. The paper attributes this to slow transition convergence (line 243), which is a reasonable explanation, but the result means that in some domains explicit transitions provide no practical advantage — and the paper does not characterize when this crossover occurs. A more nuanced discussion of when state-based rewards are worth the extra data cost would strengthen the contribution.

### Trivial

- **Naming confusion in the hallway domains (lines 229-230).** The domain called "noisy hallway" has directional observations, and the domain called "directional hallway" has noisy (random) observations. This inverted naming makes the experiment harder to follow.

- **No algorithm pseudocode.** The full procedure — Hankel estimation, SVD, PSR construction, joint diagonalization with random weights, and block-diagonal correction — is described entirely in prose across Sections 3-4. A concise pseudocode block would substantially improve clarity and reproducibility.

## Nice-to-Haves

- A complexity analysis (even asymptotic) of Hankel matrix construction, SVD, and eigendecomposition costs.
- Discussion of how the maximum sequence length L in Eq. 6 is chosen and how estimator variance interacts with the SVD threshold.
- Extending experiments beyond 4-state domains to at least moderate size (e.g., 8-12 states) to demonstrate scaling trends.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic claim: "The reward-specification experiment undermines rather than supports the paper's motivation."** REMOVED as an overstatement. The noisy hallway domain (Figure 4, bottom row) clearly demonstrates the claimed advantage: PSR_obs fails because ambiguous observations prevent distinguishing the middle state, while Ours_state succeeds once transitions converge. The paper's narrative is supported by the noisy domain results. The directional domain does complicate the story (retained as a Minor weakness above), but it does not invalidate the motivation.

- **Harsh Critic claim: "EM baseline is advantaged by receiving state count from truncated SVD."** REMOVED — factually incorrect. The proposed method also discovers the state count from the same truncated SVD of the Hankel matrix (this is the PSR learning step in Section 3.2). Both methods have access to the same information; there is no asymmetry favoring EM.

- **Harsh Critic claim: "Figure 3 planning parity reinforces the question of what the method buys."** REMOVED — the paper explicitly acknowledges parity with PSRs as the baseline expectation and uses the reward-specification experiments (Figure 4) as the differentiator. The parity result is correctly presented as a sanity check, not a claim of advantage.

- **Harsh Critic: formatting/style nitpicks and typos.** REMOVED per hard rules.

- **Harsh Critic: concerns about stripped Appendix B.1 and C.5.3.** REMOVED — the parser strips appendices from all papers; they exist in the original submission.

- **Harsh Critic: "The paper does not discuss how the maximum sequence length L is chosen."** Demoted to Nice-to-Have — this is a reasonable implementation detail but not a flaw in the contribution.

## Novel Insights

The key conceptual move — using random-weighted joint diagonalization (Eq. 18, Lemma 1) to aggregate observation information across all full-rank actions simultaneously rather than per-action — is genuinely clever and may have implications beyond POMDP learning for any setting where multiple noisy views of the same latent structure need to be aligned. The honest characterization of what is recoverable (full-rank observability partitions) rather than claiming full recovery is also a refreshingly mature approach to a hard problem.

## Suggestions

- Add the Azizzadenesheli et al. and/or Guo et al. tensor method as a baseline, at minimum on domain(s) where their per-action uniqueness assumption is violated (e.g., Sense-Float-Reset). Demonstrating that they fail while the proposed method succeeds would directly validate the central comparative claim.
- Include a half-page pseudocode block covering the full procedure.
- Describe the state-alignment procedure used for computing L1 transition error, or replace with partition-level aggregate metrics where within-partition alignment is ill-defined.
- Add at least one experiment on a moderately larger domain (e.g., 8-12 states) or provide diagnostic data on runtime/Hankel matrix size scaling to give readers evidence about extensibility.

## Score and Decision

### Calibration Anchors

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| 5AbtYdHlr3 (Stochastic Safe Action Model Learning) | 3.00 | R1 | Our paper is substantially stronger — genuine theory + experiments vs. limited contribution. |
| VRRuYBaq9u (Guided Policy Optimization for POMDPs) | 3.25 | R1 | Our paper has a cleaner, more novel technical contribution. |
| fnO5h1CFyh (Distributed Hebbian Temporal Memory) | 3.00 | R1 | Our paper is far more rigorous theoretically. |
| B7cZvTQsUN (Structured World Models) | 3.00 | R1 | Our paper has stronger theoretical foundations. |
| wCUw8t63vH (Spectral Learning of Shared Dynamics) | 6.80 | R1 | This paper has better experimental validation (real neural data) and similar theory depth. Our paper is weaker. |
| mbo4YnWCHd (Non-negative Tensor Mixture) | 4.25 | R1 | Our paper has a cleaner theoretical contribution. Our paper is stronger. |
| kyVzYpDxHg (Equivariant Tensor Functions) | 5.75 | R1 | Different topic; comparable novelty. |
| 8BAkNCqpGW (Policy Gradient for Confounded POMDPs) | 8.00 | R1 | Clearly stronger — deep theory with finite-sample bounds. Our paper is far weaker. |
| Q00CO1Tm6M (POMDP Hardness and Tractability) | 5.75 | R2 | Purely theoretical POMDP paper. Our paper has empirical validation but less theoretical depth. Roughly comparable. |
| B5kAfAC7hO (Provable Representation for POMDP RL) | 5.33 | R2 | Builds heavily on prior work per reviewers. Our paper has more novel technical contribution but weaker experiments. Comparable. |
| KrtGfTGaGe (Wasserstein Believer) | 4.50 | R2 | Our paper has cleaner theory. Our paper is somewhat stronger. |

**Round 1 bracket: 4.5 – 6.5.** Round 2 narrowed this to approximately 5.0 – 6.0. Our paper sits between B5kAfAC7hO (5.33) and Q00CO1Tm6M (5.75) — stronger technical novelty than the former, but weaker empirical validation than both due to missing baselines and toy-scale experiments. The core PSR + tensor decomposition connection is genuinely novel, but the empirical case is too thin to push into clear accept territory. **Final score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>