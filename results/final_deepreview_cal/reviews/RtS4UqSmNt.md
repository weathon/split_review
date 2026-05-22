Now let me write the consolidated review.

## Summary

This paper introduces a formal model of controlled sequential social learning in which an information-mediating planner (e.g., an LLM) controls the precision of each agent's private signal while agents also learn from predecessors' actions. The planner can be altruistic (maximizing social welfare) or biased (inducing a specific action). The paper proves convexity of the altruistic value function (Theorem 2) and derives threshold-based optimal policies with distinct regimes for both planner types (Theorems 3, 5). LLM-based simulations show qualitative alignment with theoretical predictions, with some emergent strategic deviations attributed to non-Bayesian agent behavior.

## Strengths

- **Novel integration of dynamic signal-precision control with sequential social learning.** The model (Section 3) is the first to let a planner choose a *new* signal precision each period while agents observe predecessors' actions, going beyond prior work that required two-way communication (Wei & Anastasopoulos 2022) or direct action modification (Smith et al. 2021). The framework is clean, well-motivated, and opens a tractable path for studying algorithmic information mediation under realistic transparency constraints (Remark 2).

- **Non-trivial theoretical characterization.** Proving convexity of the altruistic value function (Theorem 2) is a genuine technical challenge because agents' actions depend on public belief, breaking the linearity that typically yields convexity in belief-state MDPs. The paper leverages this convexity to extract a precise three-phase optimal policy (Theorem 3: no investment / maximum investment / precision set to max(b, 1-b)), and gives an equally structured characterization for the biased planner (Theorem 5) with five distinct phases including intentional obfuscation. These characterizations are sharp and testable.

- **Systematic comparison to myopic baselines.** The paper cleanly isolates the value of dynamic, forward-looking control by contrasting optimal policies with their myopic counterparts (Theorems 1, 4) and showing that neglecting social learning substantially worsens planner outcomes (Figure 2c).

- **Concrete welfare quantification of planner bias.** Section 6.3 measures that a biased planner can reduce social welfare by 40–50% relative to the no-control baseline, even while obeying strong transparency constraints. This provides a concrete, large effect size that underscores the practical risks of misaligned LLM mediators.

## Weaknesses

### Major

- **The claim that the LLM planner "adapts to non-Bayesian agents" is not supported by the evidence presented.** The paper states (Section 6.2–6.3) that the LLM planner's deviations from the optimal Bayesian policy "account for the non-Bayesian nature of the LLM agents" and that the LLM policy is "better adjusted to non-Bayesian agents with human-like biases." The evidence offered is that the policies *differ* in interpretable ways (less extreme precision, gradual tapering, continued investment at low beliefs). However, the paper never reports the critical comparison: the actual utility achieved by the LLM planner *vs.* the optimal Bayesian policy when *both* face the same LLM agents. The hybrid setting (optimal policy + LLM agents) is mentioned in Section 6.3 but no quantitative results are shown—only a qualitative statement that the optimal policy is "brittle." Without this comparison, the paper cannot distinguish between "the LLM planner adapted to non-Bayesian agents" and "the LLM planner simply behaved noisily or suboptimally." This is the paper's most striking empirical claim and it lacks direct evidence. The authors should either provide the missing hybrid comparison or rein in the adaptation language to "qualitative resemblance with deviations consistent with non-Bayesian agent patterns."

- **No proof sketch or intuition for Theorem 2 (convexity of the value function) in the main text.** The convexity result is foundational—it underpins the entire characterization of optimal altruistic policies (Theorem 3). The paper says the proof is "quite involved and may be of independent interest" but provides no outline, no key lemma, and no explanation of why convexity holds despite the dependence of actions on public belief. Since the appendix is stripped at submission, readers cannot assess the proof. A theoretical paper should at minimum sketch the argument's structure (e.g., properties of the Bellman operator that preserve convexity, the role of specific assumptions).

### Minor

- **No error bars or uncertainty quantification for LLM simulation results.** The simulation results in Figures 2a–c are reported as point estimates. Given that LLM outputs are stochastic and the setup involves random sampling (agent profiles, signals), confidence intervals or replication statistics are needed to assess the reliability of the claimed strategic deviations. This is standard practice for experiments with stochastic LLM-based setups.

- **The cost function for the biased planner assumes decreasing precision costs money (β(|q_i−p|)).** The paper's justification (research to tailor an ad) is reasonable, but this modeling choice is not discussed as a potential limitation. Since the biased planner's "obfuscation" behavior (lowering precision to prevent cascade-breaking signals) is a headline result, the paper should acknowledge that if decreasing precision were costless, the dynamics might differ (e.g., the planner might always use minimal precision rather than the threshold-based pattern in Theorem 5).

- **The hybrid setting (optimal policy + LLM agents) is mentioned but results are absent.** Section 6.3 lists three settings (analytical, LLM, hybrid) but only reports results for the first two. The claim that the optimal policy is "brittle" when applied to LLM agents cannot be evaluated.

### Trivial

- Section 5: The non-existence region in Theorem 5(E) (optimal policy does not exist for b∈(t₂,p]; ε-optimal policies take the form b−ε) is technically correct but could use a sentence of intuition to help readers unfamiliar with semi-continuous control.
- The paper does not discuss computational complexity or algorithms for computing the thresholds (d_A, t_A, etc.) that define the optimal policies.

## Nice-to-Haves

- A sketch of the convexity proof (even two sentences on which Bellman-operator properties are used) would significantly strengthen the theoretical contribution.
- Reporting the hybrid comparison quantitatively would either substantiate or remove the need for the "adaptation" claim.
- An experiment varying the baseline precision p systematically would test the sensitivity of the results to this parameter.
- A parametric model of the LLM agent belief-updating bias (e.g., an overreaction coefficient for counter-evidence) would make the NB1–NB3 observations more concrete and testable.

## Removed Points

The following points from the harsh critic review were removed after cross-checking against the paper:

- *"No error bars or statistical significance"* — this is a valid point and is kept in the Minor section above (not removed).
- *"Myopic planner in LLM simulation: how was it operationalized?"* — The paper describes myopic as δ=0 (analytical), and the LLM comparison in Figure 2c uses analytical myopic policies, not LLM myopic policies. The critic may have conflated the two. However, it's not entirely clear from the paper text, so I've not included this as a weakness since the paper's main LLM comparisons are about the optimal (long-term) policy.
- *"No computational complexity discussion"* — This is a nice-to-have, not a weakness. The paper is a theoretical framework paper; computing thresholds is a straightforward numerical optimization problem given the characterization.
- *"Cost function for biased planner (decreasing precision costs money) is strained"* — The paper provides a justification. This is a modeling choice, not a flaw. Demoted to a Minor point above acknowledging it as a limitation worth discussing.
- *"Non-existence region exposition"* — The paper explains this reasonably in Section 5 prose. Demoted to Trivial.
- *"No ablation on cost function"* — Nice-to-have, not a weakness.
- *"Sensitivity to baseline precision p"* — Nice-to-have.
- *"No mention of computational cost"* — Nice-to-have.
- *"No sketch for Theorem 2"* — This is kept as a Major weakness above (not removed).

## Novel Insights

The harsh critic correctly identifies the evidential gap in the LLM "adaptation" claim, which is the paper's most overreaching assertion. The rest of the paper is sounder than the critic portrays: the core theory is genuinely novel, the convexity result is non-trivial, and the policy characterizations are sharp. The strength finder correctly highlights these theoretical contributions but overstates the empirical case. The key insight that emerges from reading both sides is that the paper would be nearly as strong if it simply weakened the adaptation claim and presented the LLM results as "qualitative alignment with interpretable deviations" rather than "superior adaptation to non-Bayesian agents." The theory stands on its own.

## Suggestions

1. Either provide the hybrid-setting utility comparison (optimal policy + LLM agents) to substantiate the "adaptation" claim, or reframe the claim as "qualitative resemblance with deviations consistent with observed non-Bayesian agent patterns."
2. Add a brief proof sketch for Theorem 2 in the main text—even 3–4 sentences describing the Bellman operator's properties that preserve convexity.
3. Report variance or confidence intervals for the LLM simulation results.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Queried for papers on social learning, information design, and control. Weak anchors (score < 3.5): mostly rejects with scores 2–3 (e.g., ILtA2ebLYR at 3.00, y2ch7iQSJu at 2.00). Middle anchors (3.5–7.5): "Steer a Crowd" (4.00, Reject), "Generalized Principal-Agent" (7.25, Accept), "Learning to Steer Markovian Agents" (6.33, Accept), "Bayesian Experimental Design via Contrastive Diffusions" (7.33, Accept). Strong anchors (> 7.5): "Hidden Cost of Waiting" (8.00, Accept), "Syntactic and Semantic Control of LLMs via SMC" (8.00, Accept). Initial bracket: **5.5–7.0**.

**Round 2 (Narrowing):** Two queries with scores in (4.5, 6.5). Results included "Learning to Steer Markovian Agents" (6.33, Accept) and "Evidence from the Synthetic Laboratory" (6.25, Reject).

Anchors read in full:
- **JJ46kIfPio** (4.00, Reject) — "Steer a Crowd": information design in Markov games; incremental theory, no empirical validation. Our paper is substantially stronger in theory depth and has an empirical component.
- **IzYczpPqKq** (6.33, Accept) — "Learning to Steer Markovian Agents": RL-based steering framework with identifiability theory and algorithms. Comparable in scope but our paper's convexity result and sharp policy characterizations represent deeper theory; however, our empirical component is less rigorous (no error bars, missing hybrid comparison). Roughly comparable overall.
- **XZ71GHf8aB** (6.25, Reject) — "Evidence from the Synthetic Laboratory": LLMs as auction participants; purely empirical, no new theory. Our paper has substantially more theoretical depth.
- **LqTz13JS2P** (7.25, Accept) — "Generalized Principal-Agent": clean theoretical reductions. Stronger presentation of results, but our paper's model is arguably more novel.

Final score: **6.5**. The paper is above the typical acceptance bar due to its genuinely novel theoretical framework and non-trivial characterizations. The score reflects the strong theory while accounting for the evidential gap in the LLM "adaptation" claim and lack of proof sketch in the main text.

### Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>