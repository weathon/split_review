I have now read the full paper. Let me conduct calibration search to determine the score range.Round 1 bracket: **5.5–7**. Now narrowing within this range.Now I have enough anchors to write the final review. Let me synthesize.

---

## Summary

This paper introduces *Submodular RL* (SubRL), a new paradigm for reinforcement learning where the reward is a monotone submodular set function over the trajectory — naturally capturing diminishing returns. It proves the problem is inapproximable to any constant factor in general (reducing to the hard submodular orienteering problem), proposes SubPO (a marginal-gain policy gradient algorithm), derives a provable (1−1/e) guarantee under an ε-bandit MDP assumption via DR-submodularity, and a curvature-based (1−c) guarantee for tabular SMDPs. Six experiments (informative path planning, item collection, experimental design, building exploration, car racing, MuJoCo Ant) demonstrate practical utility.

---

## Strengths

- **Novel, well-scoped framework with connections to prior work**: SubRL is the first to embed submodular reward optimization into the full policy-gradient RL framework with stochastic transitions, cleanly distinguishing itself from convex RL (which optimizes over state visitation distributions, not trajectory sequences), adaptive submodularity (which does not handle complex MDP constraints), and the submodular orienteering problem (a special case, as shown in Section 2).

- **Genuine inapproximability result (Theorem 1)**: The reduction from the submodular orienteering problem establishes that SubRL cannot be approximated within a factor of Ω(log^{1−γ} OPT) unless NP ⊆ ZTIME(n^{polylog(n)}). This is a non-trivial, well-grounded hardness result that applies even to deterministic SMDPs.

- **Provable (1−1/e) guarantee under the ε-bandit assumption (Theorem 2)**: Showing that J(π) is monotone DR-submodular over a down-closed convex polytope under the ε-bandit assumption — and applying the Frank-Wolfe variant of Bian et al. (2017) — is technically sound. This also establishes that any gradient-based optimizer achieves ≥ 1/2-optimal policies at stationary points (via Hassani et al. 2017), generalizing submodular bandit results to stochastic transitions.

- **Principled gradient estimator for non-additive rewards (Eq. 4 / Theorem PG)**: The causal policy gradient estimator using marginal gains F(s_{j+1}|τ_{0:j}) instead of per-step additive rewards is a clean, well-motivated contribution that directly extends the REINFORCE identity to submodular returns. The history-dependent baseline for variance reduction is correctly justified.

- **Curvature-based constant-factor guarantee (Proposition 3)**: For tabular SMDPs with bounded curvature c ∈ (0,1), SubPO achieves (1−c)J(π*). This quantitatively connects to the modular special case (c=0) and aligns with known curvature-based hardness results (Vondrák 2010).

- **Empirical breadth across six diverse domains**: Experiments span discrete/continuous, deterministic/stochastic, small/high-dimensional settings. The car racing and MuJoCo Ant results (6D+2D and 30D+8D) are genuine demonstrations of scalability.

---

## Weaknesses

### Fatal
None.

### Major

- **Experimental baseline is a straw man throughout**: The only comparison in all six experiments is against *Modular RL* (MRL), defined as standard RL where the reward for state s is F({s}). This is not a meaningful competitor — it is RL given the structurally wrong reward signal and predictably fails by fixating on high-singleton-value states (verified in Section 6, line 297–298: "we always compare with modular RL (MRL)…"). For the informative path planning, experimental design, and coverage control environments, natural and well-studied alternatives exist: greedy adaptive coverage planners, entropy-maximizing scan heuristics, and informative path planning methods from the cited literature (e.g., Singh et al. 2009 is cited in Section 2). None appear. The positive empirical conclusion — that SubPO is a practically useful method — is therefore unsupported by the experimental design; all that is demonstrated is that SubPO solves the right problem while MRL solves the wrong one.

### Minor

- **Theory-practice gap is acknowledged but under-addressed in framing**: The ε-bandit assumption (Definition 1) and the tabular curvature guarantee (Proposition 3) apply to regimes entirely disconnected from the six experiments, all of which use neural network policies on continuous or discrete state spaces not matching the ε-bandit structure. The paper notes on line 292 "our experiments mainly focus on the first aspect" but does not make explicit that the theoretical guarantees do not carry over to these experiments. Framing Section 6 as "validation of SubPO" without clarifying *what is being validated* creates a misleading impression of theory-experiment coherence.

- **Curvature guarantee (Proposition 3) relies on unargued global convergence**: The proof in the appendix (referenced at line 232) inherits global convergence from Bhandari & Russo (2019), which is established for the standard (modular) policy gradient. Line 234 states "with tabular policy parameterization, under mild regularity assumptions, any stationary point of the modular PG cost function is a global optimum." Whether these conditions extend to SubPO's marginal-gain gradient estimator — which defines a different optimization landscape — is not argued. This potentially weakens the stated (1−c) guarantee.

- **Normalization convention unexplained across all experiment figures**: The y-axis "normalized J(π)" is used in Figures 3, 5, and 6 throughout, but the normalization reference (asymptote of SubPOnm, theoretical maximum, or domain-specific quantity) is never stated, making absolute performance uninterpretable from the plots.

### Trivial

- The claim "this is the first work to consider submodular objectives in RL" (abstract, line 22) is slightly over-stated given the connections to adaptive submodularity and submodular orienteering discussed in the paper's own related work section. A more precise framing — "first to embed submodular objectives into the policy gradient RL framework with stochastic transitions" — would be more accurate.

---

## Nice-to-Haves

- Including at least one natural domain-specific baseline per experiment (e.g., greedy coverage planner for informative path planning, entropy-maximizing scan pattern for Bayesian experimental design) would convert the experimental section from demonstrative to genuinely informative.
- Computing or bounding the curvature c for the specific reward functions used in experiments would bridge the theory and empirical sections; for coverage functions, curvature can often be analytically bounded.
- The observation that SubPOm ≈ SubPOnm across three environments (despite the theoretical necessity of non-Markovian policies in general) is a surprising empirical finding that deserves dedicated investigation. The paper notes this (line 292) but treats it as a side observation rather than a result; even an informal characterization of when Markovian policies suffice would constitute original contribution.
- Confidence intervals for the car racing and MuJoCo experiments (lines 368–373), where stochasticity in training could affect conclusions; this is standard in continuous-control RL evaluation.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **Harsh critic: "gradient estimator presented without formal statement/proof in main text"** — Removed per hard rule: the proof (Theorem PG) is in the appendix, which the parser strips; it exists in the original submission.
- **Harsh critic: "reference to Theorem PG in Algorithm 1 only in appendix"** — Same rule applies.
- **Harsh critic: car racing/MuJoCo missing confidence intervals as a main weakness** — Demoted to Nice-to-Have; single-run evaluation is the norm in continuous-control RL benchmarks.
- **Harsh critic: "first work" framing is a section-level flaw"** — Demoted to Trivial; the paper explicitly discusses prior related work in detail.
- **Strength finder: "strong empirical performance across diverse domains"** — Retained but significantly qualified, since performance is only measured relative to a straw-man baseline.
- **Strength finder: SubPOnm uses RNNs/transformers** — The non-Markovian experiments use simple history-concatenation, not RNNs; the footnote in Section 4 mentions this but the experiments don't demonstrate it. Dropped this specific claim.

---

## Novel Insights

The most interesting observation to emerge from the review — which the paper treats as an aside — is that SubPOm (Markovian) matches SubPOnm (non-Markovian) in five out of six environments, despite the theoretical necessity of history-dependent policies for submodular objectives. This empirically suggests a gap between worst-case theory and typical-case structure: the time-augmented state space used in the formulation (S = H × V) may implicitly encode enough trajectory information for a Markovian policy to recover near-optimal behavior on commonly studied objectives. If true, this would be a substantive simplification with practical implications for the design of submodular RL agents — one that the paper leaves unexplored.

---

## Suggestions

1. Add at least one domain-appropriate baseline per experiment — greedy coverage planner for informative path planning, a simple entropy-maximizing scan for Bayesian experimental design — to make the empirical contribution informative beyond its comparison to a straw man.
2. State the normalization reference for all experimental y-axes explicitly (in captions or experimental setup).
3. In Section 5, add a sentence clarifying that Proposition 3's convergence argument is borrowed from the modular PG literature and may require additional conditions for the marginal-gain objective; or provide a brief argument that the conditions carry over.
4. Dedicate a paragraph (or a small ablation) to the SubPOm ≈ SubPOnm finding — characterizing empirically the conditions under which Markovian policies suffice would make the work more impactful.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `i8dYPGdB1C.md` (Multi-agent submodular) | 6.80 | R1/R2 | Real baseline comparisons, tight theory-experiment connection; SubRL is broader in scope but weaker experimentally |
| `1DEEVAl5QX.md` (Mini-batch submodular) | 4.67 | R1 | Incremental; SubRL is clearly more novel |
| `REKRLIXtQG.md` (Supermodular rank) | 5.00 | R1 | Narrower scope; SubRL contributes more |
| `vtCkb4KJxr.md` (Noisy submodular) | 5.50 | R2 | Incremental improvement; SubRL's new framework is substantially more ambitious |
| `tijmpS9Vy2.md` (BAMDP Shaping) | 7.00 | R2 | Comparable: unified RL framework + theory + limited experiments; BAMDP is more tightly written but SubRL is broader |
| `DFTHW0MyiW.md` (Robust RL) | 7.00 | R2 | Strong framework + theory + experiments with real baselines; SubRL lacks real baselines |
| `wPhbtwlCDa.md` (STARC reward framework) | 6.50 | R2 | Similar: general RL reward framework with theory; STARC has clearer experimental grounding |

**Round 1 bracket: 5.5–7**

**Round 2 narrowing**: The paper's theoretical contributions (inapproximability + 1-1/e + curvature bound + marginal-gain gradient estimator) are on par with the 6.5–7.0 anchors. The framework novelty is real. However, the single major weakness — experiments only compare to a straw man (MRL) rather than to any method a practitioner would actually use — is a meaningful gap compared to the 6.80–7.00 anchors, which all have proper baselines. The SubRL experiments demonstrate that the algorithm solves the right problem but not that it does so competitively with existing approaches. This pulls the paper below the 7.0 anchors and closer to the 6.0–6.5 range. The paper is above the 5.5 anchors (which are more incremental). **Final score: 6.0** — the theoretical and framework contributions are strong enough to warrant acceptance, but the experimental thinness prevents a higher score.

**Originality**: High — first unified policy gradient framework for submodular RL with inapproximability and constant-factor guarantees.  
**Importance of research question**: High — submodular objectives arise naturally in coverage, experiment design, and informative path planning.  
**Support for claims**: Partial — theoretical claims are well-supported; empirical claims of practical utility need stronger baselines.  
**Soundness of experiments**: Moderate — the environments are diverse and well-chosen, but the baseline is too weak to draw strong conclusions.  
**Clarity of writing**: Good — the paper is well-organized, with clear definitions and algorithm description.  
**Value to research community**: Moderate-to-high — the framework and theoretical tools are a genuine contribution; the empirical baseline weakness limits immediate practical impact.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>