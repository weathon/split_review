## Summary

This paper proposes DDCFR, a framework that replaces the fixed, manually-specified discounting schemes used in prior CFR variants (CFR+, DCFR) with a dynamic, learned discounting policy trained via evolution strategies. The authors formalize CFR's iteration process as a Markov decision process, train a game-agnostic policy on small games, and demonstrate generalization to larger unseen games. The core idea — learning discounting weights dynamically rather than fixing them — is well-motivated and novel.

## Strengths

- **42% average reduction in exploitability over DCFR on eight unseen testing games** (Section 4.2, line 186), demonstrated across a diverse set including Battleship-2/3, Goofspiel-4, Liar's Dice-4, Leduc Poker, Big Leduc Poker, and HUNL Subgame-3/4. The improvement over a strong baseline on games unseen during training directly supports the generalization claim.

- **Systematic ablation study** (Table 1, Section 4.3) isolates the contribution of each design decision: number of training games, state representation components (iteration vs. exploitability), continuous vs. discrete actions, and ES vs. PPO optimization. This goes beyond a single final-number comparison and provides genuine insight into what drives performance.

- **Negligible inference-time overhead quantified at 0.22%** (Section 3.4, line 161), addressing a practical concern common to learned-optimizer frameworks and making the deployability claim verifiable.

- **Theorem 1 states convergence bounds** (Section 3.2, line 128) for the dynamic discounting scheme under specified ranges of α_t, β_t, γ_t, and directly informs the action-space bounds used during training (line 179), connecting theory to practice.

## Weaknesses

### Major

1. **No statistical uncertainty reported anywhere.** The ES training procedure (Section 3.3) is inherently stochastic — it relies on random perturbations ε_i ~ N(0,I), random network initialization, and a population of 100 perturbed parameter sets per epoch. Yet Figures 2–3 and Table 1 contain no error bars, confidence intervals, or variance measures. The text never specifies whether results come from a single trained policy or multiple runs. For a method whose optimization involves significant randomness, the absence of any variance reporting makes it impossible to assess whether the claimed improvements are reliable or within noise level. This is a significant evidential gap for a top-tier venue.

2. **DCFR baseline comparison conflates dynamic adjustment with access to a wider parameter range.** DDCFR is compared against DCFR with a single fixed setting (α=1.5, β=0, γ=2 — the default from Brown & Sandholm, 2019b, line 89). Meanwhile DDCFR's policy can select α_t ∈ [0,5], β_t ∈ [−5,0], γ_t ∈ [0,5] dynamically per iteration. The comparison conflates two distinct advantages: (a) dynamic vs. fixed weighting, and (b) access to a wider effective range of discounting parameters. A meaningful comparison would need to establish that the *dynamic* aspect — not merely having access to better hyperparameters — drives the improvement. A straightforward control would be tuning DCFR's α, β, γ per game via grid search over the same ranges available to DDCFR, or comparing against a version where the learned policy's first output is frozen. Without this, the headline 42% improvement could partially or wholly reflect that the default DCFR parameters are suboptimal for these specific games.

### Minor

1. **PPO ablation lacks sufficient detail to be interpretable.** Section 4.3 (line 209) reports that PPO "underperforms in all testing games" but provides no hyperparameter information: network architecture, learning rate, clip range, value function coefficient, training steps, or whether any hyperparameter tuning was performed. Given that PPO is notoriously sensitive to configuration, and that ES is the authors' chosen method, this comparison as presented does not support rigorous conclusions.

2. **DPCFR+ claim presented without supporting results.** Section 4.4 asserts that the framework generalizes to PCFR+, producing DPCFR+, and that "these results demonstrate the general applicability" — yet no quantitative results are shown. This is a dangling claim that should either be supported with evidence or removed.

3. **Greedy Weights dismissed via speculation rather than evidence.** Line 194 dismisses a directly related approach (Zhang et al., 2022) based on "suspicion" ("We suspect that when faced with a large number of information sets, the computed weights might not be appropriate"), without any empirical comparison. Even a small-scale comparison would strengthen rigor.

4. **"0.22% increase in time" stated without measurement methodology.** No information is given about how this was measured, on which games, over how many runs, or whether the measurement accounts for exploitability computation (which is itself non-trivial for larger games). The precision is not credible without such details.

5. **Exploitability computation in the state representation is not discussed for large games.** The state (line 111) includes normalized exploitability, requiring its computation each iteration. For HUNL Subgame-3/4, the paper does not clarify whether exact exploitability (full best-response computation) or approximations are used. This affects both metric reliability and the feasibility of the state representation at test time.

### Trivial

None.

## Nice-to-Haves

- Tuning DCFR per game via grid search over the same α, β, γ ranges available to DDCFR to isolate the dynamic advantage.
- Reporting mean and standard deviation of exploitability over 5–10 independent training runs.
- Including Greedy Weights as an empirical baseline, at least on smaller games.
- Providing a proof sketch or clear citation for Theorem 1 to substantiate the claimed theoretical analysis.

## Removed Points

These points are flagged for removal; treat them with caution.

- **Theorem 1 lacks proof / "theoretical analysis is vacuous"** (Harsh Critic #1). The critic notes the theorem is stated without proof or derivation. Per the hard rules, the parser strips appendices and references to them from all papers; the proof may have existed in the original submission. Additionally, criticisms about "absent references" are removed per rule. The theorem statement itself is informative and connects to practice, so this is not retained as a weakness. (The authors would nonetheless benefit from including a sketch or citation in the main text.)
- **"Small Matrix" description is vague.** This is a minor presentational point about the training game description that does not affect the paper's core claims.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add error bars.** Report exploitability with standard deviations across multiple independent training runs with different random seeds. This is essential for a method whose training is explicitly stochastic.
2. **Control for hyperparameter quality.** Compare DDCFR against DCFR with per-game grid-searched α, β, γ over the ranges [0,5], [−5,0], [0,5] respectively. Alternatively, ablate the "dynamic" advantage by comparing against a frozen version of the learned policy's first-step output.
3. **Provide full PPO configuration details** or remove the comparison if insufficient tuning was performed.
4. **Support or remove the DPCFR+ claim** — a single data point would suffice.
5. **Clarify exploitability computation** for HUNL subgames (exact or approximate?).

## Score and Decision

Score: 5.0
Decision: Reject

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>