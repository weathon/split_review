Now I have carefully verified all mathematical claims and reviewer assertions against the paper. Here is my consolidated review.

---

## Summary

This paper proposes Vlearn, an off-policy actor-critic algorithm that learns only a state-value function (V-function) as the critic, eliminating the state-action-value (Q) function. The core technical contribution is adapting a weighted importance sampling (WIS) loss — previously studied only for linear methods — to deep RL, supported by Theorem 1 (WIS loss as an upper bound on the naive importance-weighted Bellman error with the same minimizer). To make the WIS loss work with deep networks, the paper introduces design choices including trust-region policy updates (TRPL), twin V-networks, and importance weight clipping. The main empirical claim is that Vlearn performs particularly well on high-dimensional action spaces (up to 39-dim MyoHand and 38-dim DMC dog locomotion), where Q-function-based methods degrade.

## Strengths

1. **Principled theoretical grounding for the WIS loss (Theorem 1)**: The paper proves that the proposed WIS loss (Eq. 4) is an upper bound on the naive importance-weighted Bellman error (Eq. 2) and shares the same minimizer. The claim is mathematically sound — the key insight (which the paper attributes to Jensen's inequality in the main text and defers the full proof to the appendix) is that for each state, the difference between the two losses equals Var_{a~π}[r + γV_θ̄(s')] ≥ 0, and this variance term depends only on the frozen target network, not on the learned parameters θ, so both losses share the same optimum. This provides a principled foundation for using the WIS objective with deep value networks, going beyond the linear-domain results of Mahmood et al. (2014).

2. **Variance analysis in the bandit setting**: Section 3.2 derives closed-form estimators for the base, V-trace, and WIS losses in a bandit simplification. The WIS loss yields the self-normalized importance-sampling estimator, which is known to have lower variance than the standard IS estimator (base) and the squared self-normalized estimator (V-trace). This analysis directly supports the claim that the proposed estimator is more robust in fully off-policy settings.

3. **Consistent strong empirical results on high-dimensional tasks**: The evidence is compelling across three high-dimensional task families:
   - **Humanoid-v4 (17-dim)**: Vlearn achieves ~25% improvement over SAC (Figure 2).
   - **DMC dog locomotion (38-dim)**: Vlearn learns reliably while SAC and MPO fail to obtain stable policies (Figure 2).
   - **MyoSuite myoHand (39-dim)**: Vlearn achieves the highest aggregated IQM performance across all 10 tasks (Figure 3).
   These results directly demonstrate the core claim that eliminating the Q-function is particularly beneficial in high-dimensional action spaces.

4. **Systematic ablation study**: Figure 4 (right) isolates each design choice. Removing importance sampling → failure to learn; replacing TRPL with PPO loss → degraded performance; increasing truncation threshold to 20 → destabilization; removing twin critics → reduced performance. This validates that multiple non-trivial design choices are jointly necessary for the WIS objective to work in deep RL.

5. **Honest self-assessment and transparent limitations**: The paper acknowledges that sample efficiency remains a challenge (Section 5), that Vlearn is not always best on low-dimensional tasks (HalfCheetah-v4, Figure 5), and that the approach benefits from further stability improvements. This transparency is commendable.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Main text provides insufficient detail of the Theorem 1 proof.** The paper states the proof "relies on Jensen's Inequality" in a single sentence (line 94) and defers the full derivation to the appendix (stripped). While the claim is mathematically valid (verified: using 𝔼[ρ]=1 and the reweighting identity 𝔼_{π_b}[ρ·f] = 𝔼_π[f], the difference reduces to a variance term under the target policy), the main-text justification is too terse for a skeptical reader. A concise 3–4 line sketch in the main text would significantly strengthen the theoretical narrative and avoid the appearance of a gap.

2. **The V-trace comparison is transparent but framed somewhat over-broadly.** The paper explicitly states it uses 1-step returns for both Vlearn and V-trace to "eliminate any external factors" and isolate the effect of importance-weight placement. This is a methodologically sound ablation. However, the introduction claims V-trace methods are "less effective in a completely off-policy context" as a general statement about V-trace, when the experiments only test the 1-step V-trace loss variant — not the full n-step V-trace algorithm (which is designed for multi-step targets). The paper would benefit from clarifying that the comparison specifically targets the loss structure, and noting that n-step V-trace might perform differently.

3. **Sample complexity claim is not rigorously quantified.** The abstract states Vlearn "improves sample complexity as well as final performance," but no AUC (area under learning curve) or time-to-threshold metrics are provided. The learning curves (Figures 2, 3, 5) visually support faster convergence on some tasks (e.g., Humanoid-v4) but not others (e.g., HalfCheetah-v4 where SAC converges faster). Quantifying sample complexity would make this claim more precise.

4. **No runtime or memory comparison.** The paper motivates V-functions as more efficient than Q-functions in high-dimensional action spaces, but provides no measurements of wall-clock time, parameter count, or memory usage. A comparison of trainable parameters for Vlearn (two V-networks + policy) vs. SAC (two Q-networks + policy) would substantiate the efficiency claim.

5. **Importance weight clipping threshold could use more discussion.** The paper uses ε_ρ=1 by default, which caps the importance weight at 1 — effectively discarding any correction when ρ > 1. The ablation (Figure 4 right) shows ε_ρ=20 destabilizes learning, but the bias–variance trade-off of this aggressive truncation is not discussed. Since ρ > 1 occurs frequently when the current policy assigns higher probability to an action than the behavior policy did, the effects of truncating at 1 merit deeper analysis.

### Trivial

- Line 72: "the inner expectation with one Monte Carlo sample" — the equation numbering in the paper internally references "Equation 2" and "Equation 4" but the text occasionally refers to equation numbers that were reordered during drafting (minor inconsistency between text citations and displayed equation numbers).

## Nice-to-Haves

- **Include Retrace (Munos et al., 2016) as a baseline.** Retrace is a natural off-policy V-function method with multi-step corrections and is mentioned in the paper's related work. Adding it would strengthen the empirical positioning.
- **Add n-step V-trace experiment**: Running the V-trace baseline with its default n-step returns (e.g., 5-step) would isolate whether the advantage of WIS over V-trace persists when V-trace is used at its full potential. If results still favor Vlearn, this would considerably strengthen the paper's claims.
- **AUC or time-to-threshold metrics**: A supplemental table reporting these for key tasks would rigorously substantiate the "improved sample complexity" claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Twin V-functions contradict the simplicity claim"** (from Harsh Critic): The paper's contribution is eliminating the *Q-function* (state-action-value function), not minimizing network count. Twin V-functions are still V-functions, not Q-functions. The paper explicitly addresses this: "While the overestimation bias is not a direct problem when using just state-value functions, we found twin critics beneficial in practice... a form of regularization." Removed as it mischaracterizes the paper's central claim.

- **"Theorem 1 proof is suspect/flawed"** (from Harsh Critic): Verified directly. For a fixed state s_t: 𝔼[ρ]=1 and 𝔼_{π_b}[ρ·f] = 𝔼_π[f] by the definition of importance sampling. The difference between the WIS and base inner expectations reduces to V^2(𝔼[ρ]−1) + 𝔼[ρ\bar{V}^2] − (𝔼[ρ\bar{V}])^2 = 0 + Var_{a~π}[\bar{V}] ≥ 0, where \bar{V} uses the *frozen target network* — so this variance term does not depend on θ, meaning both losses share the same minimizer. The claim is mathematically sound. Removed as factually incorrect.

- **"Hyperparameter tuning may be unfair to SAC/MPO"** (from Harsh Critic): The paper is transparent about keeping hyperparameters constant and "only adjusted appropriately for the higher dimensional dog and MyoSuite tasks." This is standard practice in RL benchmarking. Generic concern that applies to nearly all RL comparisons. Downgraded to removed — insufficient specificity to constitute a real weakness.

- **"Missing related works about Retrace"** (from Harsh Critic): Retrace is already cited in the paper. Removed per instructions (we cannot verify existence of uncited works).

- **"Missing appendix content / not verifiable"** (from Harsh Critic): Per instructions, the appendix is stripped by the parser and exists in the original submission. Removed.

- **Strength: "Direct head-to-head comparison with V-trace"** (from Strength Finder): This strength is valid and kept in the main review. It does not conflict with the verified weakness about the V-trace comparison — the strength is about the *isolation* of the weight placement effect, which is methodologically sound; the weakness is about the *scope of claims drawn from that comparison*. Both can coexist.

- **Strength Filter drops**: Several generic strengths from the Strength Finder ("this paper addressed an important problem," "targeted an interesting question") are dropped as they lack specific content. They are not included here as they add no value.

## Novel Insights

The reviews surface a useful observation not explicit in the paper: the WIS loss's variance reduction in the bandit setting (self-normalized estimator) and its robustness to target-critic errors (Figure 1) can be understood through complementary lenses — the IS perspective and the "no optimum shift for small ρ" perspective — yet both trace back to the same structural property: moving the importance weight outside the square removes the dependence on the target-network value function as an interpolation target. This connection between variance reduction and the loss geometry is worth making more explicit in future work.

## Suggestions

1. Add a 3–4 line sketch of the Theorem 1 proof in the main text (using the identity 𝔼[ρ]=1 and showing the difference reduces to a target-policy variance term that does not depend on θ).
2. Add an experiment with n-step V-trace (e.g., 5-step) to verify that the advantage of WIS over V-trace is not an artifact of restricting V-trace to 1-step returns.
3. Include a table comparing trainable parameter counts for Vlearn vs. SAC/MPO to substantiate the efficiency claim.
4. Provide AUC or time-to-threshold metrics for key tasks to rigorously support the "improved sample complexity" claim.
5. Discuss the bias–variance trade-off of importance weight clipping at ε_ρ=1, particularly when ρ > 1 occurs frequently.

## Score and Decision

**Overall assessment**: The paper makes a clear contribution. The theoretical foundation (Theorem 1) is mathematically sound, the empirical results on high-dimensional tasks are strong and well-demonstrated across multiple benchmarks, and the ablation study convincingly justifies the design choices. The weaknesses are minor and primarily concern presentation details and the scope of the V-trace comparison. The paper is honest about its limitations. I find no fatal flaws.

On the evaluation axes:
- **Originality**: Good — extending WIS to deep V-function learning with careful design choices is novel and practically motivated.
- **Importance of research question**: Good — high-dimensional action spaces are a real bottleneck for Q-function-based methods.
- **Claims well-supported**: Mostly — the central empirical claim is well-supported; the "improved sample complexity" claim is somewhat undersupported.
- **Soundness of experiments**: Good — 10 seeds, proper CIs, IQM aggregation, controlled ablations.
- **Clarity**: Good — well-structured, transparent about limitations and experimental design.
- **Value to community**: Good — provides a practical alternative to Q-function methods with a clean algorithm.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>