Now I have all the information I need. Let me synthesize the final review.

**Calibration Round 1 Bracket:** Based on the initial search, I placed this paper between 3.5 and 7.5 — clearly stronger than rejected papers around 3.0, but not as strong as the top-tier papers above 7.5.

**Calibration Round 2 Narrowing:** Comparing against anchors within my bracket:
- BMPC (avg 7.0, Accept): More thorough evaluation, clearer advantages across all environments — current paper is weaker
- MPC^2 (avg 6.25, Accept): Comparable overall quality; current paper has stronger ML contribution but weaker theory
- DLPA (avg 6.2, Reject): Current paper is stronger
- Efficient Planning with Latent Diffusion (avg 6.75, Accept): Stronger paper empirically

The paper sits near the lower end of the 6-range anchors, around 6.0.

---

## Summary

This paper proposes Residual-MPPI, which integrates Residual Q-learning (RQL) into the Model Predictive Path Integral (MPPI) framework to enable online (zero-shot and few-shot) customization of continuous-control policies toward additional objectives (e.g., safety, behavioral preferences) without requiring knowledge of the prior task's reward function. The method combines a learned prior policy, a learned dynamics model, and MPPI-based planning, evaluated on MuJoCo benchmarks and on the realistic Gran Turismo Sport (GTS) simulator with the champion-level GT Sophy 1.0 agent.

## Strengths

- **Novel and well-motivated problem framing.** The paper addresses a practically important setting: adapting a pre-trained continuous-control policy to new objectives at execution time without access to the original reward or value function. The combination of RQL with MPPI is a natural and original integration that extends RQL from discrete (MCTS) to continuous action spaces without requiring training a new policy network.

- **Impressive demonstration on a real-world-grade simulator.** In GTS, Residual-MPPI reduces off-course steps of GT Sophy 1.0 from 93.13 to 9.03 (zero-shot) and 4.43 (few-shot), with lap time increasing from 117.77s to only 123.34s and 122.93s respectively. Both Greedy-MPPI and Guided-MPPI fail to complete a lap entirely, making this a compelling demonstration of the method's effectiveness in a challenging, high-fidelity environment.

- **Substantial sample efficiency advantage over RL-based customization.** In MuJoCo, Residual-MPPI (trained on 2K steps for dynamics) achieves total rewards comparable to Residual-SAC trained for 4M steps (e.g., HalfCheetah: 1936 vs 2184; Ant: 6847 vs 6963), while dramatically outperforming Residual-SAC trained on the same limited budget of 200K steps. In GTS, Residual-SAC required 80K laps and still yielded an overly conservative 130s lap time.

- **Prior-policy-based initialization is a practical contribution.** Algorithm 1's use of the prior policy to recursively initialize the nominal action trajectory (lines 1–4) and the inclusion of this nominal sequence as a candidate in evaluation are simple but effective design choices that improve planning stability, validated by the failure of Full-MPPI (which lacks this initialization) across all tasks.

## Weaknesses

### Fatal

None.

### Major

- **Residual-MPPI and Greedy-MPPI are nearly indistinguishable in 3 of 4 MuJoCo tasks.** In HalfCheetah (1936.2±109.3 vs 1939.9±134.7), Swimmer (−60.0±5.2 vs −58.9±5.4), and Hopper (7363.0±254.9 vs 7367.0±199.4), the two methods produce total rewards within one standard deviation of each other across all metrics. Only in Ant (6846.7±647.8 vs 6104.2±1532.0) does Residual-MPPI show a clear advantage. The paper's central claim that the `log π` term is critical ("the key factor in addressing the policy customization problem," Sec. 5.2) rests primarily on the Ant and GTS results; the simpler MuJoCo tasks provide at best weak support. This does not invalidate the method, but it narrows the evidence base for the claimed importance of the `log π` term to settings where the add-on is orthogonal to the basic reward.

- **The GTS evaluation lacks a systematic trade-off analysis.** The paper reports a single operating point (one add-on reward weight) and characterizes the ~4-5% lap-time increase as "marginal" while still claiming "superior racing performance." Without varying the add-on reward weight and plotting the Pareto frontier of lap time vs. off-course steps, it is difficult for the reader to assess where this operating point sits relative to the best achievable trade-off. The claim that the method "strikes a better trade-off" would be significantly strengthened by quantifying the frontier and including Greedy-MPPI's frontier (if it can complete a lap under any weight).

### Minor

- **The theoretical connection between Proposition 1 (infinite-variance condition) and the practical algorithm (finite-variance Gaussian noise) is a heuristic, not a derivation.** The paper honestly acknowledges the gap: Proposition 1 requires a Gaussian with infinite variance (i.e., uniform noise), while the algorithm uses standard finite-variance Gaussian noise. The analysis then says "it suggests that MPPI can well approximate... with a large noise variance" — but no analysis is provided of how large is sufficient, or how approximation error scales. The step from Proposition 1 to Eq. 6 is described as "straightforwardly derived," which overstates the formal connection. The paper's empirical contribution does not depend on this theoretical claim, but the framing could be more measured.

- **No analysis of the `log π` term's role in MuJoCo beyond aggregate metrics.** Since the advantage over Greedy-MPPI is only clearly visible in Ant, the paper would benefit from analyzing *why* the term matters in that setting (e.g., breaking down reward by planning horizon, or visualizing how the planning distribution differs). This would help the reader understand when the `log π` term is essential vs. when greedy optimization suffices.

### Trivial

None.

## Nice-to-Haves

- Varying the add-on reward weight in GTS and plotting the resulting lap-time vs. off-course Pareto frontier (including Greedy-MPPI at weights where it can complete a lap).
- Reporting wall-clock planning time per step to help readers assess real-time deployability.
- Adding statistical significance testing (e.g., bootstrap tests) for the MuJoCo comparisons between Residual-MPPI and Greedy-MPPI.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No statistical significance tests are reported"** — Removed per filtering rules. Reporting mean ± std over multiple seeds is the standard in the RL community for benchmark evaluations; statistical significance testing is not a required norm and demanding it here is a formatting standard mismatch.
- **"Missing hyperparameters / appendix content"** — Removed. The paper states that configurations are in Appendices C and D. The parser strips these sections from the extracted text; they exist in the original submission.
- **"GTS comparison with Residual-SAC is not apples-to-apples"** — Removed. The paper explicitly discusses the comparison, noting that Residual-SAC yields an "overly conservative" policy and requires far more data. The framing acknowledges the differences rather than claiming a direct matched comparison.
- **"Table 1 is cluttered"** — Removed as a formatting nitpick.
- **"The add-on reward function for GTS is not clarified"** — Removed. The task is clearly described as staying on course and the metric (off-course steps) is well-defined and measured. The reward formulation in MPPI flows from this description.

## Novel Insights

None beyond the paper's own contributions. The cross-reviews surface a useful observation that the paper's two empirical settings (MuJoCo and GTS) tell somewhat different stories about the value of the `log π` term — it matters little when the add-on reward is aligned or dense (3/4 MuJoCo tasks), but becomes essential when the add-on is orthogonal (Ant) or when greedy optimization leads to catastrophic local optima (GTS, where Greedy-MPPI fails entirely). This insight is latent in the paper's own discussion but could be made more explicit to strengthen the narrative.

## Suggestions

1. Rephrase the method's theoretical justification as a *heuristic motivated by maximum-entropy principles* rather than a derivation, to match the honest acknowledgment of the infinite-variance gap.
2. Add a brief analysis (even in the supplement) explaining why the `log π` term matters in Ant but not in the other MuJoCo environments — this would substantially strengthen the paper's narrative about when Residual-MPPI's key mechanism is valuable.
3. Include a Pareto frontier plot for the GTS experiment, varying the add-on reward weight, to move the trade-off claim from qualitative to quantitative.

## Score and Decision

I now present the final calibration anchors and score derivation.

**Round 1 (Bracketing) anchors:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 1MHgMGoqsH.md (MPC training) | 3.00 | R1 low | Much weaker; withdrawn paper |
| Q8ypeYHKFO.md (SafeDiffuser) | 3.33 | R1 low | Much weaker; withdrawn reject |
| MWHIIWrWWu.md (MPC^2) | 6.25 | R1 mid | Comparable; both accepted poster |
| i7jAYFYDcM.md (BMPC) | 7.00 | R1 mid | Stronger; more thorough evaluation |
| HL5P4H8eO2.md (DiffTOP) | 8.00 | R1 high | Stronger overall, but rejected venue mismatch |

**Round 2 (Narrowing) anchors:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| MWHIIWrWWu.md (MPC^2) | 6.25 | R2 | Similar tier; current paper has stronger ML contribution but weaker empirical coverage |
| pBQs8kQm63.md (Continuous-time LTI) | 5.50 | R2 | Different paper type; current paper is stronger |
| wQkERVYqui.md (C-TRPO) | 5.40 | R2 | Weaker empirical validation |
| i7jAYFYDcM.md (BMPC) | 7.00 | R2 | Stronger; clearer advantage over baselines across all tasks |
| w3iM4WLuvy.md (SRL) | 7.00 | R2 | Stronger; cleaner evaluation |
| btpgDo4u4j.md (Latent Diffusion Planning) | 6.75 | R2 | Stronger; more thorough |
| YH9tnuUYds.md (DLPA) | 6.20 | R2 | Slightly weaker overall |

**Round-1 bracket stated:** between 3.5 and 7.5.

**Narrowing reasoning:** The paper is clearly above the 3-4 range (rejected/withdrawn papers with weak or misaligned contributions) but below BMPC (7.0) and Latent Diffusion Planning (6.75), which have more comprehensive evaluations and clearer empirical advantages across all tasks. The paper is comparable to MPC^2 (6.25) — both have clear contributions qualified by evaluation limitations — and stronger than DLPA (6.2, rejected). The MuJoCo weakness (≈ Greedy-MPPI in 3/4 tasks) and the missing Pareto analysis in GTS prevent the paper from reaching the 6.5-7.0 range, while the novel problem framing and strong GTS results keep it above 5.5. I assign **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>