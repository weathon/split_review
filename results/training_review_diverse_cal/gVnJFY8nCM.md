I now have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes Residual-MPPI, an online planning algorithm for continuous-control policy customization. It combines the Residual Q-learning (RQL) framework with Model Predictive Path Integral (MPPI) control to customize a pre-trained prior policy to satisfy new add-on objectives at execution time, using only the prior policy's action distribution and a dynamics model. The method is evaluated in MuJoCo environments (zero-shot) and on the Gran Turismo Sport racing simulator with the champion-level GT Sophy 1.0 agent, demonstrating significant improvements on add-on tasks with minimal performance degradation on the original task, using orders of magnitude less data than RL fine-tuning baselines.

## Strengths

- **Novel combination of RQL and MPPI for online policy customization in continuous control**: The paper bridges the RQL framework (which previously required offline SAC training for continuous actions) with MPPI's sampling-based MPC, enabling customization at execution time without additional policy training. This is a principled and practically useful synthesis that goes beyond prior work.

- **Strong empirical results across multiple domains**: In all four MuJoCo environments (HalfCheetah, Swimmer, Hopper, Ant), Residual-MPPI achieves the highest total reward and best add-on task performance among all methods, including Guided-MPPI which has access to the true combined reward (Table 1). For example, in HalfCheetah, total reward improves from 1,004.79 (prior policy) to 1,948.14 (Residual-MPPI), and from 1,821.19 (Guided-MPPI with full reward access).

- **Successful real-world-scale demonstration with GT Sophy 1.0**: The GTS experiment (Table 2) shows Residual-MPPI reduces off-course steps of a champion-level racing agent from 93.13 to 36.60 (few-shot) with only a ~2.5% lap time increase (117.77→120.75 seconds). The data cost (~2,100 laps total) is orders of magnitude less than the RL baseline Residual-SAC (80,000+ laps), demonstrating the practical advantage of planning over training for customization.

- **Only requires the prior policy's action distribution**: The method does not need access to the original reward function, training scheme, or policy parameters — only \(\log \pi(\boldsymbol{u}_t|\boldsymbol{x}_t)\). This makes it applicable to prior policies obtained through any method (RL, IL, or demonstrations).

- **Sample efficiency advantage clearly demonstrated**: The GTS comparison concretely shows the data advantage: Residual-MPPI uses ~2,000 laps for dynamics training + ~100 for fine-tuning, vs. 80,000+ laps for Residual-SAC to achieve its performance.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The derivation from Theorem 1 to Residual-MPPI is under-explained.** The paper states "We can then derive Residual-MPPI straightforwardly" (line 148) after Theorem 1, but the logical chain is not explicitly spelled out. Theorem 1 shows MPPI can approximate the optimal max-entropy policy distribution for a given reward, and RQL shows the optimal customized policy's objective involves \(r_R + \omega' \log \pi\). The missing step is a clear statement that MPPI with the RQL-derived reward approximates the optimal solution to the augmented MDP. While the reasoning is fundamentally sound, the "straightforwardly" gloss papers over a non-trivial intellectual connection. The paper would benefit from a short paragraph making this chain explicit rather than leaving it implicit.

2. **The comparison with Residual-SAC in GTS is presented with a one-sided framing.** Residual-SAC reduces off-course steps to near zero (0.87) while Residual-MPPI achieves a ~60% reduction (93→36.60). These represent different points on a safety-speed Pareto front: Residual-MPPI adds ~2.5% lap time for substantial safety gains; Residual-SAC adds ~10% lap time for near-perfect safety. The paper dismisses Residual-SAC as "overly conservative" and "sub-optimal" without acknowledging that depending on the application's safety requirements, near-zero off-course steps may be preferable. A more balanced discussion of this trade-off would strengthen the paper. (That said, the data-efficiency advantage of Residual-MPPI is real and correctly emphasized.)

3. **The hyperparameter \(\omega'\) (weight on the log-likelihood) is not discussed.** This parameter controls the critical trade-off between preserving prior behavior and satisfying the add-on objective. The paper neither reports what value was used, how it was chosen, whether it was tuned per environment, nor shows any sensitivity analysis. For a method claimed to be generic, such information is essential for reproducibility and for readers to assess robustness.

4. **The correction term \(-\lambda \hat{\boldsymbol{u}}_t^T \Sigma^{-1} \boldsymbol{\epsilon}^k_t\) in Algorithm 1 (line 114) is used but never explained.** The original MPPI weight formula in Eq. (8) contains a related correction term, but the algorithm incorporates this term differently (accumulated stepwise in \(S(\mathcal{E}^k)\) with \(\gamma^t\) discounting). The paper does not discuss why this particular form is used, whether it correctly handles the modified score (which now includes \(\log \pi\)), or whether omitting it would change results. This leaves a gap in the method's presentation.

5. **The explanation for why Residual-MPPI outperforms Guided-MPPI lacks direct evidence.** The paper argues that Residual-MPPI "implicitly inherits the original task reward through the prior policy log likelihood, which is informed by the Q functions optimized over an infinite horizon" (line 246), while Guided-MPPI suffers from finite-horizon limitations. This is a plausible mechanism but is presented without verification (e.g., measuring how the log-likelihood correlates with the true basic reward across states, or showing how the performance gap varies with planning horizon). An ablation isolating the mechanism would make the claim more convincing.

### Trivial
None.

## Nice-to-Haves

- **Runtime information**: The GTS environment runs at 60 Hz, but the paper does not state how many MPPI samples can be evaluated within one control cycle, or what hardware was used. This is important for assessing real-time deployability.
- **Ablation on the log-likelihood term**: Comparing Residual-MPPI against variants using (a) the true basic reward ("Oracle-MPPI") and (b) a constant/uniform log-likelihood would clarify whether the method works because it recovers the true combined reward or because it regularizes planning.
- **Few-shot ablation for Guided-MPPI**: When the dynamics model is fine-tuned with 100 laps for Residual-MPPI, the same could be done for Guided-MPPI to isolate whether the benefit of few-shot comes from better dynamics or from the interaction with the log-likelihood term.
- **Planning horizon analysis**: Varying \(T\) and measuring the gap between Residual-MPPI and Guided-MPPI would concretely test the claimed infinite-horizon advantage.

## Removed Points

The following points from the reviews are removed with justification:

- **Criticism about the zero-shot claim conflating the dynamics model requirement**: The paper explicitly states "zero-shot policy customization **with a provided offline trained dynamics model**" (line 31). The qualification is already present. Removed per hard rule about factually incorrect criticisms.
- **Claim that the 80,000 lap figure includes prior policy training data**: The paper states "over 80,000 laps of roll-outs are collected to achieve the current performance of **Residual-SAC**" (line 295). This clearly refers to Residual-SAC's training data. The reviewer's speculation is unsupported by the text. Removed.
- **Complaint about large standard deviations for baselines**: This is an observation about results, not a paper weakness. Removed.
- **Criticism that few-shot improvement in GTS is modest**: The paper reports an improvement (43→36 off-course steps, 121.99→120.75 lap time). Whether this justifies the additional 100 laps is a subjective judgment that the paper's readers can make for themselves. Removed.
- **Request for a "proper few-shot baseline" (fine-tuning dynamics for Guided-MPPI)**: Moved to Nice-to-Haves as a reasonable suggestion, not a weakness.
- **Formatting/presentation nitpicks**: Removed per hard rules.

## Novel Insights

Beyond the paper's own contributions, a notable pattern emerges across the reviews: the method's success may stem from the log-likelihood term serving dual roles — it both encodes infinite-horizon value information (as the paper claims) and acts as a regularizer that anchors planning to the prior policy's action distribution, reducing sample variance in MPPI's importance sampling. The fact that Residual-MPPI has consistently lower standard deviations than Guided-MPPI (34 vs 285 in HalfCheetah total reward; 104 vs 1,605 in Hopper) suggests the regularization effect is substantial and may itself be a significant contributor to the performance improvement, independent of the infinite-horizon argument. Future work could usefully disentangle these two effects.

## Suggestions

1. Add a brief subsection or paragraph explicitly connecting Theorem 1 to the Residual-MPPI objective: Theorem 1 shows MPPI ≈ max-entropy policies; RQL shows optimal augmented policies maximize \(r_R + \omega' \log \pi\); therefore MPPI with this reward approximates the optimal customized policy.
2. Report the value of \(\omega'\) used in each experiment and include a sensitivity analysis (even a single plot of total reward vs. \(\omega'\) for one environment).
3. Explain the correction term in Algorithm 1: state its origin in the MPPI importance-sampling derivation and whether the form used is correct for the modified score.
4. Re-frame the GTS comparison with Residual-SAC to acknowledge the safety-speed trade-off: both methods achieve different operating points on the Pareto front, with Residual-MPPI offering better lap time at the cost of imperfect safety, and Residual-SAC offering near-perfect safety at higher lap-time cost. The data-efficiency advantage of Residual-MPPI is a separate and stronger argument.
5. Add a short discussion of computational requirements (samples per control cycle, hardware used) to assess real-time feasibility.

## Score and Decision

**Originality**: Good — combining RQL with MPPI for online continuous-action customization is novel and distinct from prior work. **Importance**: High — online policy customization without retraining is practically important. **Claims support**: Mostly well-supported by experiments, though the theoretical derivation is glossed over and the mechanism for outperforming Guided-MPPI lacks direct evidence. **Soundness**: Solid experimental design with multiple environments and baselines; missing ablations and hyperparameter reporting. **Clarity**: Generally clear, but Sections 3.1 could be more explicit about the derivation. **Value**: Strong — the GTS demonstration with GT Sophy 1.0 is a compelling real-world validation.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>