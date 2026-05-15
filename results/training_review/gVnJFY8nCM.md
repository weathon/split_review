Now I have a thorough understanding of the paper and all claims. Let me write the consolidated review.

## Summary

The paper proposes Residual-MPPI, an online planning algorithm for customizing pre-trained continuous-control policies at execution time without retraining. The method integrates Residual Q-Learning (RQL) into the MPPI framework by using the prior policy's log-likelihood as a surrogate for the original task reward, combined with an add-on reward for new requirements. Experiments in MuJoCo (zero-shot) and Gran Turismo Sport (zero-shot and few-shot) demonstrate the approach, including customization of the champion-level GT Sophy 1.0 racing agent to reduce off-course steps.

## Strengths

- **Novel integration of RQL with MPPI for online policy customization**: Residual-MPPI is the first algorithm to combine the RQL framework with sampling-based MPC, enabling customization at execution time without retraining. The algorithm requires only access to the prior policy's action distribution and a dynamics model, without knowledge of the original reward function.

- **Successful customization of a champion-level racing agent in a high-fidelity simulator**: In Gran Turismo Sport, Residual-MPPI reduces off-course steps from 93.13 (GT Sophy 1.0) to 36.60 (few-shot) with only a 2.5-second lap-time increase (Table 2). The few-shot variant uses only ~100 laps of online dynamics fine-tuning versus 80,000 laps for Residual-SAC, demonstrating a dramatic sample efficiency advantage. The average off-course distance also drops from 0.69m to 0.37m.

- **Well-motivated problem and practical framing**: The paper identifies a genuine deployment challenge — adapting a trained policy to unforeseen requirements at runtime — and proposes a solution that works with black-box prior policies (no reward or training access needed).

## Weaknesses

### Fatal
None.

### Major

1. **Theoretical justification does not rigorously connect Theorem 1 to the implemented algorithm.** Theorem 1 (Section 3.1) restates a known maximum-entropy RL property (action-sequence distribution has form exp((Σ r + V*)/α)). The paper then claims MPPI approximates this when noise is uniform (infinite-variance Gaussian) and γ≈1. However, Algorithm 1 uses finite-variance Gaussian noise, a discount factor γ<1 that is absent from the theory, and the connection is never formally derived — the paper states "We can then derive Residual-MPPI straightforwardly" (line 148) without providing the derivation. This gap means the paper's central claim that Residual-MPPI approximates the optimal max-entropy customized policy is not theoretically supported. The algorithm may still work empirically, but its theoretical motivation is substantially weaker than presented.

2. **MuJoCo experimental comparisons lack statistical rigor, undermining the claim that Residual-MPPI "outperforms" Guided-MPPI.** In 3 of 4 environments, the performance gaps between Residual-MPPI and Guided-MPPI fall within one standard deviation on the key metric (e.g., Ant total reward: Residual-MPPI 6808 ± 599, Guided-MPPI 5485 ± 1773; Hopper total: 7398 ± 103 vs 6146 ± 1605; HalfCheetah total: 1948 ± 34 vs 1821 ± 285). No statistical significance tests, confidence intervals, or multiple-seed evaluations are reported. The paper needs to demonstrate that the advantage is robust, not driven by noise.

3. **Missing runtime analysis for the GTS real-time claim.** The paper states GTS runs at 60 Hz (≈16.7ms per control step, line 261) and that Residual-MPPI operates "online." However, no wall-clock timing measurements are reported. Without confirming that the planning loop (including sampling, dynamics rollouts, and evaluation) completes within the 60 Hz budget, the feasibility claim for real-time control is unsubstantiated.

### Minor

1. **The comparison with Residual-SAC in GTS is presented with a framing bias.** The paper describes Residual-SAC's policy as "overly conservative" and "sub-optimal" (line 295), but Residual-SAC achieves 0.87 off-course steps vs. 36.60 for few-shot Residual-MPPI — a ~40× safety improvement, with only a ~10-second lap-time penalty. The paper would benefit from a more balanced discussion of this safety-performance trade-off and clearer acknowledgment that which approach is preferable depends on the application's risk tolerance.

2. **No ablation or sensitivity analysis of the key hyperparameter ω'** (the weight on log π in Algorithm 1). The log π term is the crucial mechanism claimed to implicitly encode the original task reward, yet the paper provides no study of how varying ω' affects performance (including ω'=0, which would reduce to MPPI with only the add-on reward). This makes it difficult to assess how critical the log π term actually is.

3. **The "off-course steps" metric in GTS is not precisely defined.** The paper reports this as a primary safety metric (Table 2) but does not specify what constitutes an off-course step (e.g., any tire beyond track boundary? center of mass? distance threshold?).

4. **Insufficient detail about the ω weighting between basic and add-on reward** used by the Guided-MPPI and Full-MPPI baselines (which use ω r + r_R). The paper does not specify how ω is set or whether it was tuned.

5. **No robustness test against a sub-optimal prior policy.** The paper acknowledges in Limitations (Section 7) that Residual-MPPI is bottlenecked by prior policy quality, but never tests this empirically (e.g., by using a deliberately degraded prior).

### Trivial
- The paper's discussion of the MPPI importance-weight formula (Section 2.2) and Algorithm 1's implementation are actually consistent with standard MPPI (the constant term -(λ/2)û^T Σ^{-1} û cancels in the softmax), but the presentation could be clearer to avoid confusion.

## Nice-to-Haves
- A comparison with MPPI augmented by a learned terminal value function (e.g., a small online-learned Q-function) would help isolate whether log π's benefit comes from providing better long-horizon value information or from some other mechanism.
- A plot of performance vs. planning horizon T for both Residual-MPPI and Guided-MPPI in MuJoCo would substantiate the paper's "finite horizon" explanation for Guided-MPPI's limitations.
- Reporting the number of transition tuples (not just laps) for GTS dynamics training would clarify the data requirement more precisely.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Criticism about Eq. (5) / line 81 being "inconsistent" with standard MPPI and Algorithm 1**: The paper's Eq. (5) correctly includes λ/2. Algorithm 1's `-λ û^T Σ^{-1} ϵ` is consistent because the `-(λ/2) û^T Σ^{-1} û` term is constant across noise samples and cancels in the softmax normalization. This is a factually incorrect criticism.
- **Criticism about "zero-shot" terminology being misleading because a pre-trained dynamics model is used**: "Zero-shot" in policy customization refers to no additional training for the customization task itself. The dynamics model is pre-trained infrastructure, consistent with standard usage in the literature.
- **Criticism about "missing related works"**: Per guidelines, I cannot verify existence of unmentioned works.
- **Criticism about dynamics model details being "relegated to the appendix"**: Standard practice for page-limited conference papers.
- **Criticism about Full-MPPI not being a meaningful baseline**: Full-MPPI failing demonstrates the value of prior-policy guidance, which is a useful ablation.

## Novel Insights

None beyond the paper's own contributions. The two-reviewer process did not surface a new perspective that the paper itself does not already articulate.

## Suggestions

1. **Strengthen the theoretical framing**: Either (a) provide a proper derivation showing how Algorithm 1 follows from the max-entropy objective under standard MPPI assumptions, or (b) reframe the theory as intuition/justification rather than claiming a formal equivalence. An honest "heuristic derivation" would be more credible than the current hand-wavy claim.

2. **Add statistical rigor to MuJoCo experiments**: Report results over multiple random seeds (at least 5) with confidence intervals or pairwise significance tests (e.g., bootstrap or t-test) for the Residual-MPPI vs. Guided-MPPI comparison. The large standard deviations of Guided-MPPI suggest the results may not be stable.

3. **Report wall-clock timing for GTS**: Measure and report the average, max, and p99 planning-loop completion time per control step. If the method does not meet the 60 Hz budget, discuss the gap and hardware specifications.

4. **Include an ablation on ω'** (weight on log π) across a range including ω'=0, and show how performance degrades without the log π term.

5. **Define "off-course steps" precisely** and consider reporting complementary safety metrics (max off-course distance, fraction of time off-course) for a more complete picture.

6. **Present the Residual-SAC comparison more neutrally**: Acknowledge that Residual-SAC achieves far better safety at the cost of speed, and that the choice between methods depends on whether safety or performance is prioritized.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>