Now I have sufficient calibration data. Let me write the consolidated review.

---

## Summary

This paper addresses causal confusion in imitation learning for autonomous driving. The authors propose 3CIL, a conditional IL method that uses a causal diagram to motivate three design traits, implemented via future image reconstruction (ℒ_fo), action residual prediction (ℒ_ar), supervised contrastive learning (ℒ_RNC), and a sample-weighting term. Experiments in CARLA across 6 scenarios show that 3CIL achieves the highest accumulated reward in 5 of 6 settings, outperforming several IL baselines.

## Strengths

1. **Causal-reasoning-driven trait identification with concrete loss mapping.** Section 3.1 derives three specific traits (T1/T2/T3) from the causal diagram (Figure 1b), and each is addressed by a distinct loss term: future reconstruction for T1, action residual prediction + RNC for T2, sample weighting for T3. This tight coupling between analysis and algorithm design is clearer than in prior causal-motivated IL work (e.g., DIGIC, PALR) which either only masks features or regularizes one dependence.

2. **Strong accumulated reward across diverse scenarios.** In Table 1, 3CIL achieves the highest accumulated reward in 5 of 6 scenarios (Scenarios 1–5), outperforming all baselines including Premier-TACO, DIGIC, and PALR. Notably, in the unseen-town scenario (Scenario 5), 3CIL obtains 538.50 vs. the next-best 516.70.

3. **Action residual prediction without explicit previous-action input.** The representation model deliberately eliminates the explicit use of a_{t-1} (Section 3.2), instead capturing its effect by predicting Δa_t = a_t − a_{t-1} from the inferred state ŝ_t (Eq. 2). This directly targets the copycat/inertia problem and is grounded in the causal graph's structure where a_{t-1} informs s_t, not directly a_t.

4. **Ablation variants validate multi-directional supervision.** The paper includes RNC (contrastive only) and RAP (residual prediction only) as baselines in Table 1. The drop from 3CIL to RNC/RAP shows that both causal-direction (ℒ_ar) and anti-causal-direction (ℒ_RNC) regularization are necessary for the best performance.

## Weaknesses

### Major

1. **Factually incorrect claim about collision rates.** The paper states "3CIL is one of the most cautious drivers with the lowest collision rate in half settings (3 of 6)" (Section 4.2, p.8 line 231). This is **not supported** by Table 1. Verifying against the paper's own data: in Scenario 1, the lowest collision rate is 0.55‰ (RNC/RAP) vs. 3CIL's 0.60‰; Scenario 2 lowest is 0.36‰ (CIL) vs. 3CIL's 0.53‰; Scenario 3 lowest is 1.31‰ (Premier-TACO) vs. 3CIL's 3.15‰ (the *highest* in that scenario); Scenario 4 lowest is 0.31‰ vs. 3CIL's 0.35‰; Scenario 5 lowest is 0.29‰ (CIL) vs. 3CIL's 0.59‰; Scenario 6 lowest is 0.34‰ (CIL) vs. 3CIL's 0.63‰. In **no** scenario does 3CIL have the lowest collision rate. This is not a minor exaggeration — it is a direct misstatement of the quantitative results the paper itself reports. A correction is necessary, but more importantly, it forces the reader to re-evaluate what the method actually achieves on safety.

2. **No statistical reliability — single-run results without variance.** All metrics in Table 1 appear to come from a single evaluation run. In CARLA, stochasticity from weather, traffic density, and environment initialization produces significant variance. Without multiple seeds (3–5) and standard deviations, there is no way to determine whether observed differences (e.g., 3CIL's 521.26 vs. Premier-TACO's 469.99 in Scenario 1) are significant or within noise. This is a structural weakness for any empirical paper making comparative claims in a stochastic simulator.

3. **Unacknowledged reward–safety trade-off and missing failure analysis.** 3CIL achieves high accumulated reward but sometimes at substantially higher collision rates (Scenario 3: 3.15‰ vs. CIL's 1.35‰). The reward function (described as combining speed, position, rotation, and action terms) may reward speed or forward progress disproportionately, creating an incentive for policies that drive fast but collide more. The paper does not discuss this trade-off, present a safety-weighted metric, or analyze why 3CIL fails on Scenario 6 (reward 195.53 vs. RAP's 447.44). There is no limitations section. This weakens the claim of "robust" driving.

### Minor

4. **Causal framing is somewhat overstated.** The paper is titled "Causality-Inspired" and motivates losses with a causal diagram, which is legitimate. However, no actual causal inference (interventions, counterfactuals, do-calculus) is performed — the diagram motivates the loss design but does not constrain learning or generate testable causal predictions. The claim that "variations in δa_t can be seen as performing interventions on Δa_t" (Section 3.3, line 182) overreaches: this is a sample-weighting heuristic, not an intervention. The paper would benefit from a more measured framing that acknowledges the method as causality-**inspired** representation learning rather than implying deeper causal machinery.

5. **Key hyperparameters lack sensitivity analysis.** The sample-weighting formula (Eq. 4) uses γ = 6.67 and bounds [−0.3, 0.3] without any justification or sensitivity study. These values directly control which samples get up-weighted and by how much, yet the paper provides no analysis of how varying them affects results.

6. **Limited discussion of the reward function composition.** The reward function is described only as "R = T_speed + T_position + T_rotation + T_action" with details deferred to an appendix (which was stripped by the parser). Without understanding the relative weights of the speed term, it is difficult to interpret whether high reward reflects good driving or simply aggressive speed.

### Trivial

None.

## Nice-to-Haves

- Reporting multiple seeds (3–5) with standard deviations for all metrics.
- A safety-weighted metric (e.g., reward minus collision penalty) or Pareto analysis of the reward–collision trade-off.
- Sensitivity analysis on the sample-weighting hyperparameters γ and the bound range.
- A brief limitations paragraph acknowledging the single-run evaluation, the reward–collision trade-off, and the Scenario 6 failure.

## Removed Points

These points were raised by reviewers but are removed or downgraded for the reasons given:

- **"Missing recent SOTA baselines (Transfuser, IRIS, LAV)"** — The paper's scope is methods addressing causal confusion in imitation learning, not general end-to-end driving. The baselines included (CIL, PALR, DIGIC, Keyframe, Premier-TACO) are all directly relevant to this focus.
- **"No code release"** — Per the hard rule, questioning the existence/availability of cited artifacts is not permitted.
- **"RNC loss taken verbatim from Zha et al."** — The paper explicitly cites Zha et al. and uses their loss as one of several components. Using existing losses as building blocks is standard practice.
- **"Dataset too large (1.125M samples)"** — This size is not a weakness for a driving dataset. It is a strength that the paper uses a large-scale dataset.
- **"Causal diagram not used to derive quantitative constraints"** — While true, the paper says "causality-inspired," not "causal inference." The diagram is used to motivate trait identification, which is a legitimate use of causal reasoning.
- **Strength Finder item about "problem importance"** — Generic. Only strengths that are concrete and specific to the paper are kept.
- **"The causal motivation is not operationalized — could perform an intervention experiment"** — This asks the paper to solve a different, more difficult problem than it claims. The paper is evaluated on what it does, not on what it could additionally do.

## Novel Insights

None beyond the paper's own contributions. The reviews raise standard concerns about experimental rigor and framing calibration but do not uncover a fundamentally different interpretation of the method or results.

## Suggestions

1. **Correct the collision claim.** The sentence "3CIL is one of the most cautious drivers with the lowest collision rate in half settings (3 of 6)" must be replaced with an honest characterization: 3CIL achieves the highest accumulated reward in most settings but does **not** achieve the lowest collision rates. Discuss this trade-off explicitly.
2. **Add multiple seeds (3–5) with standard deviations.** This is essential for a comparative evaluation in a stochastic simulator.
3. **Include a safety-weighted metric** to disentangle the reward–collision trade-off, or present a Pareto frontier showing both dimensions.
4. **Add a limitations section** that acknowledges the single-run evaluation, the reward composition ambiguity, the anomalous Scenario 6 result, and the absence of sensitivity analysis on key hyperparameters.
5. **Tone down the causal framing** where it overreaches (particularly the "interventions" claim in Section 3.3), or add a discussion of what would be needed to move from "causality-inspired" to actual causal inference.

## Score and Decision

**Round 1 bracket (wide):** The low-score band (avg ≤ 3.5) contained papers with minimal empirical validation or fundamental flaws (e.g., STL-Drive at 2.5, commonsense reasoning paper at 2.5). The middle band (3.5–7.5) contained semantically similar papers like GAP (5.25, rejected), GPT-Driver (5.0, rejected), IQ-MPC (5.75, rejected), and LAW (7.0, accepted poster). The high band (≥ 7.5) contained papers with rigorous methodology and extensive evaluation (e.g., Data Scaling Laws at 8.0). The paper under review clearly does not belong in the low band (it has a real method and experiments) or the high band (it lacks statistical rigor), so the bracket is **(3.5, 7.0)**.

**Round 2 narrowing:** Anchors within this range:
- **GPT-Driver** (5.0, rejected): Novel application of LLMs to motion planning but limited novelty and open-loop only. 3CIL has more architectural novelty and closed-loop evaluation, but GPT-Driver had no factual errors. Slightly comparable overall.
- **GAP** (5.25, rejected): GPT-2 for end-to-end driving with competitive CARLA results. Somewhat similar contribution level, but GAP lacked the factual error problem. 3CIL is slightly weaker due to the collision claim issue.
- **IQ-MPC** (5.75, rejected): Model-based imitation learning with reasonable experiments but some theoretical concerns and limited novelty. 3CIL has clearer novelty but weaker experimental rigor — the factual error makes it clearly worse.

**Final placement:** The paper has a genuine contribution (the method design is thoughtful and the reward results impressive in 5/6 scenarios). However, the factually incorrect collision-rate claim directly undermines trust in the authors' reporting, and the single-run evaluation means the quantitative results cannot be verified as statistically reliable. These are serious enough to place the paper below the acceptance threshold despite its strengths.

**Score: 4.5**

**Decision: Reject**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>