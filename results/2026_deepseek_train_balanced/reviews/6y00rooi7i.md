## Summary

This paper proposes IHAC (Imitation Hierarchical Actor-Critic), a two-phase HRL framework that uses an LLM to provide high-level option guidance during an early imitation learning phase (Phase I), then transitions to standard PPO (Phase II). Key design choices include: (1) an adaptive sampling strategy that mixes LLM and learned policy with an annealed mixing ratio λ_t, (2) a loss function that trains both the policy (via KL regularization toward the LLM policy) and value function, and (3) limiting LLM queries to Phase I (≤20% of training) for token efficiency. Experiments on MiniGrid, NetHack, and Crafter compare against two LLM-augmented HRL baselines.

## Strengths

- **Quantified token-efficiency advantage**: The paper reports that IHAC consumes 90% fewer tokens than LLM×HRL and 95% fewer than LLM4Teach in the LavaCross environment (line 155). This is a direct, measured result supporting the core design claim that confining LLM queries to early training yields substantial cost savings.

- **Measurably faster convergence**: In KeyInBox and TwoDoorKey (MiniGrid), IHAC reaches good performance after ~2,500 iterations while baselines converge at ~4,500 iterations (line 134). This provides concrete evidence that early LLM-guided imitation accelerates learning.

- **Informative ablation study**: Section 4.5 compares five variants (Base → NP → NP+NS → NP+NS+IIL → full model) and shows monotonic improvement with each added component—optimized prompting, annealed sampling, policy-only imitation learning, and combined policy+value imitation learning. The full model outperforms all partial variants.

- **Validation of the annealing strategy**: The ablation shows NP+NS (with annealed λ_t) outperforms NP (fixed sampling) in both success rate and training speed (lines 197–198), giving empirical support to the claim that decaying the LLM's influence over time is beneficial.

- **Evaluation across three diverse environments**: MiniGrid (discrete grid navigation), NetHack (complex roguelike), and Crafter (2D survival/crafting) cover procedurally generated and stochastic settings with different state representations, strengthening generality.

## Weaknesses

### Fatal
None.

### Major

- **Evaluation protocol biases comparison in favor of IHAC**: The paper explicitly states that baselines "had not fully converged by the time they reached the predetermined number of iterations" but training was terminated at the same iteration count for all methods (line 126). This systematically disadvantages slower-converging methods — a baseline that would match or surpass IHAC given more iterations is penalized by early termination. The paper claims "superior performance," but the evidence conflates faster convergence with better final performance. This undermines the central empirical claim.

- **Missing non-LLM control to isolate the LLM's contribution**: The paper compares IHAC only against other LLM-augmented HRL methods (LLM4Teach, LLM×HRL). There is no ablation that replaces the LLM option selector with a random or rule-based alternative while keeping the IHAC training framework intact. Without this control, it is impossible to attribute gains to the LLM's reasoning versus the IHAC training framework itself (two-phase design, annealed sampling, KL regularization). Since the LLM only selects from a small hand-crafted list of 5–6 options ("go to target, pick up, drop, open, wait, and explore," line 126), the marginal value of the LLM over a simple heuristic is unexamined.

- **The value loss in Equation 1 introduces a KL divergence inside the TD target without explanation**: The loss function (lines 98–100) minimizes `α[Q_w(s,a) - (r + γE_{a'~π̃_θ}Q̅_w(s',a') - KL(π̃_θ(·|s')||π_LL^α(·|s')))]²`. The KL term is subtracted inside the TD target, a non-standard construction that acts as a next-state policy regularizer on the value target. The paper's only explanation (line 102) describes the policy KL term's purpose but says nothing about why a KL divergence appears inside the value target or how this relates to the Bellman equation. Combined with the notational issue `π_LL^α` (likely `π_LLM`), this makes the Phase I objective difficult to interpret and reproduce.

### Minor

- **No explicit numerical results with variance**: The paper reports only relative improvement percentages (e.g., "14.75% improvement over LLM×HRL," line 155) and relies on figures for absolute numbers. No standard deviations, confidence intervals, or raw success rates are provided in text or a table. With only 5 random seeds (lines 126, 144), the statistical significance of reported improvements cannot be assessed.

- **Different LLMs used across environments without justification**: MiniGrid uses Vicuna 7b (line 126), NetHack uses ChatGPT-3.5-turbo (line 144), and Crafter does not specify the LLM. This inconsistency makes cross-environment comparisons uninterpretable — performance differences could reflect the method, the LLM quality, or both.

- **Annealing schedule for λ_t is underspecified**: The paper states λ_t is "gradually annealed" from an initially high value (line 92) but does not specify the schedule type (linear, exponential), initial value, final value, or decay rate relative to Phase I iterations. This is a key hyperparameter necessary for reproducibility.

- **Limited generality given domain-specific engineering**: The method depends on a hand-crafted ActionNet (A* for navigation, hard-coded "pick up," "open"), a per-environment Trans module, and a predefined option set (5–6 items). These components require substantial per-environment engineering, narrowing the scope of the claimed generality.

### Trivial

- The notation `π_LL^α` in Equation 1 appears to be a typo for `π_LLM`.

## Nice-to-Haves

- Add an ablation where the LLM is replaced by a random/rule-based option selector to directly test whether the LLM's reasoning provides the claimed benefit.
- Report absolute success rates with standard deviations in a formatted table.
- Clarify the derivation of Equation 1 — why is a KL divergence inside the value TD target? Relate it to a soft Bellman equation or known objective.
- Specify the full λ_t annealing schedule (initial value, decay function, final value).
- Use a consistent LLM across all environments or justify the variation.

## Removed Points

These points from the inputs were filtered per the review guidelines:
- **"Missing quantitative results — Table 1 and Figures 9/10/11 not present"**: These are PDF parser artifacts; the figures and table exist in the original submission. The legitimate concern about absent variance reporting is retained in Minor weaknesses.
- **"Related work section is thin, cites only 4 papers"**: Per guidelines, I cannot penalize missing related works without external sources to verify gaps.
- **"Hyperparameter choices not reported (learning rates, network architectures)"**: These implementation details are commonly placed in appendices which are stripped by the parser.
- **"Token efficiency claim is expected by design, not a finding"**: A measured result emerging from a design choice is still a finding; this criticism is removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the evaluation protocol**: Run all methods to convergence and compare final performance, or separate claims into "faster convergence" (supported) and "better final performance" (requires rerunning baselines to convergence).
2. **Add the critical control**: Replace the LLM option selector with a random/rule-based selector in the IHAC framework. If performance drops significantly, the LLM's contribution is confirmed; if not, the gains come from the training framework.
3. **Rewrite the explanation of Equation 1**: Clarify whether the KL in the value target is intentional, and if so, derive it from a principle such as a soft Bellman equation. If included in error, correct it.
4. **Report absolute numbers with variance**: For every environment and metric, report mean ± std in a table.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>