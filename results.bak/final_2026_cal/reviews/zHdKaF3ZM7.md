Now I have sufficient calibration data. Let me write the final consolidated review.

Here is my bracket analysis:
- **Round 1 bracket**: 4.0–6.0 (comparing weak-anchor papers <3.5 vs strong-anchor papers >7.5)
- **Round 2 narrowing**: Focused on 4.5–6.5 range
- **Round 2 anchors**: MoM (5.50, Accept Poster), Memory Caching (4.67, Reject), TTT Done Right (5.60, Accept Poster), TTT3R (6.00, Accept Poster)

Comparing: WARP has stronger novelty than Memory Caching (4.67) and RSSM (4.00), and is comparable in architectural novelty to MoM (5.50). However, WARP has more evaluation concerns than MoM (which had comprehensive LM experiments), but its classification benchmarks are solid with modern SSM baselines. The physics-informed results are a genuine differentiator. I place WARP at **5.0** — marginal accept territory, novel architecture with solid classification evidence but some evaluation gaps that need addressing.

---

## Summary

This paper introduces WARP (**W**eight-space **A**daptive **R**ecurrent **P**rediction), a sequence model that treats the *weights of an auxiliary MLP* as the hidden state of a linear recurrence driven by input differences. The recurrence $\theta_t = A\theta_{t-1} + B\Delta x_t$ updates a high-dimensional weight vector $\theta_t$, which is then unflattened and used as the decoder network to produce outputs $y_t = \text{MLP}_{\theta_t}(\tau)$. This formulation combines the efficiency of linear recurrence (parallel scan) with the expressivity of nonlinear decoding, enables gradient-free test-time adaptation, in-context learning, and physics-informed variants. Experiments span image completion, traffic/energy forecasting, dynamical system reconstruction, multivariate time series classification, and in-context learning.

## Strengths

- **Genuinely novel architectural paradigm.** WARP's core idea — using a linear recurrence to update the *weights of an auxiliary network* as the hidden state, driven by input differences $\Delta x_t$ rather than $x_t$ directly — is distinct from prior RNNs, SSMs, and weight-space approaches. Equation (1) and Figure 1 clearly articulate this formulation. No prior work combines weight-space hidden states, linear recurrence, and input-difference driving in this way.

- **Gradient-free test-time adaptation is cleanly realized.** The paper explicitly states (Section 2.3) that fast weights $\theta_t$ are updated $T-1$ times via Eq. (1), *not* via gradient descent, while only the slow parameters $(A,B,\phi)$ are trained. This directly delivers one of the paper's headline capabilities without additional machinery.

- **Strong physics-informed results (WARP-Phys).** Table 3 shows WARP-Phys achieving MSE $0.03\pm0.04$ on Mass-Spring-Damper vs. $0.34\pm0.12$ for the next-best Transformer (10× better), and $0.04\pm0.01$ on MSD-Zero vs. $0.48\pm0.24$ (12× better). This demonstrates a genuine advantage of the weight-space framework for incorporating domain knowledge.

- **Solid classification results against modern SSM baselines.** Table 4 compares WARP against a strong lineup including Mamba, S5, LRU, S6, Griffin, and FACTS across six UEA classification datasets. WARP sets new state-of-the-art on Ethanol (36.49%) and Heartbeat (80.65%), and lands top-three on four of six datasets. These comparisons include the modern SSMs that the paper is fairly measured against.

## Weaknesses

### Major

- **PEMS08 traffic forecasting results need stronger verification.** Table 2 reports WARP halving the error of the best graph-based method (MAE 6.59 vs. STDCN 13.45). However, the baselines (GMAN, D²STGNN, STDCN) are taken from a single external paper [62] without re-running under identical conditions. Different train/test splits, prediction horizons, or preprocessing pipelines could materially affect the comparison. The paper also mentions preprocessing with a "non-causal convolution" (deferred to the stripped Appendix D), leaving the reader unable to verify potential information leakage. An improvement of this magnitude on a well-studied benchmark requires a controlled re-evaluation or, at minimum, explicit confirmation that the comparison protocol is identical.

- **BPD values in Table 1 require clarification.** On CelebA, baseline BPD values vary wildly and implausibly (LSTM: 3869 at $L=100$ vs. 7.276 at $L=300$; GRU: 24.14, 60.39, 71.51) despite MSEs staying in a narrow 0.027–0.064 range. While WARP's own negative BPD values are *mathematically possible* with a Gaussian likelihood on normalized continuous data (density can exceed 1 when predicted variance is small), the erratic baseline values suggest disparities in how uncertainty calibration or the BPD computation was handled across models. The paper states all models were trained with the NLL loss, but does not discuss calibration quality or report whether the same $\sigma_{\min}$ and positivity-enforcement were used. A clearer statement of the exact BPD formula and a check on calibration are needed before this table can be taken at face value.

### Minor

- **Dynamical system reconstruction lacks modern SSM baselines.** Table 3 compares against only GRU, LSTM, and a Transformer. Given that the paper prominently cites S4, Mamba, S5, and LRU in other sections, their absence from these forecasting benchmarks weakens the claim of "superior expressivity" for black-box forecasting. The strong classification comparisons in Table 4 mitigate this concern but do not fully address it, since the DSR tasks (OoD generalization, long-horizon prediction) stress-test different capabilities.

- **Selective claim inconsistency on MSD (Table 3).** The paper states (Section 3.2) that "weight-space linear RNNs consistently outperform all baseline models across problem domains." On the MSD dataset, black-box WARP (MSE 0.94) is *worse* than the Transformer (0.34). The overall statement holds only when including WARP-Phys in the comparison. This should be qualified.

- **In-context learning experiment is a weak demonstration.** The ICL setup (Section 3.4) is a linear regression on random keys with a cumulative sum transformation that substantially simplifies the problem. No comparison to a Transformer or gradient-based baseline is provided. The sub-quadratic efficiency claim is not empirically supported with wall-clock or FLOPs measurements. This experiment is at best a proof-of-concept.

### Trivial

- The conclusion refers to "infinite-dimensional RNN hidden states," but $\theta_t$ is finite-dimensional (bounded by $D_\theta$). This is a minor rhetorical overreach.
- Section 2.2 describes the coordinate system $\tau$ but the paper never fully specifies which variant was used for each experiment in the main text (deferred to Appendix C).

## Nice-to-Haves

- An ablation comparing input differences $\Delta x_t$ against direct inputs $x_t$ would validate a core design claim.
- An analysis of the learned transition matrix $A$ (e.g., eigenvalue spectrum visualization) would illuminate whether the model deviates from the identity initialization and what dynamics it learns.
- Reporting $D_\theta$ and root network depth/width for each experiment in the main text (even briefly) would help readers assess computational cost and capacity.
- A controlled comparison on PEMS08 where baselines are re-run under identical conditions would significantly strengthen the traffic forecasting claims.

## Removed Points

- *"Root network architecture not reported"* and *"D_θ values not given"* — Deferred to Appendix C.2/D (stripped from the parser). Standard practice for conference submissions; the main text provides the architecture type (fixed-width MLP) and input/output dimensions.
- *"Non-causal convolution leaks future info"* — Speculative without access to Appendix D. The paper mentions this preprocessing step but the details are in the stripped appendix.
- *"Negative BPD is physically nonsensical"* — Incorrect. With a continuous Gaussian likelihood on normalized data, probability density can exceed 1 in localized regions, producing negative log-density and thus negative BPD. The issue is not negative BPD per se but the erratic baseline values.
- *"No variance reported for ETT"* — The paper states "mean MSE across three runs."
- *"Missing related work"* — Cannot be verified without external sources.
- *Formatting/typo complaints* — Parser artifacts.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the BPD computation and baseline calibration.** Provide the exact formula, discuss whether the same $\sigma_{\min}$ and positivity-enforcing function were used for all models, and explain why baseline BPD values vary so widely despite similar MSEs. Consider reporting a calibration metric (e.g., expected calibration error for uncertainty estimates).

2. **Strengthen the PEMS08 evidence.** Either re-run the best graph-based baseline under identical conditions (same train/val/test split, same prediction horizon) or acknowledge the limitation explicitly and provide a confirmatory experiment on another traffic benchmark with controlled baselines.

3. **Add modern SSM baselines to the DSR experiments** (S4, S5, or Mamba) to substantiate the expressivity claims on the forecasting tasks where they are currently absent.

4. **Qualify the "consistently outperforms" claim** in Section 3.2 to distinguish black-box WARP vs. WARP-Phys performance on MSD.

## Score and Decision

**Calibration Summary:**

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|--------------------------|
| DREAMSTATE (HHsD970kdE) | 3.00 | R1-bracket | Less novel; diffusion-based state editing for RNNs |
| NeuMa (clCsSQ5rKg) | 2.00 | R1-bracket | Bio-plausible SSM, less relevant |
| RSSM (azNpwiObPp) | 4.00 | R1-bracket | Less novel (reservoir + SSM); WARP is more original |
| SSM reprs (R5xBLfD9Dv) | 5.00 | R1-bracket | Comparable in novelty; WARP has broader evaluation |
| MoM (3PdOq8Rgue) | 5.50 | R2-narrow | Slightly stronger evaluation (language tasks); comparable architectural novelty |
| Memory Caching (R3EJ2IjgOI) | 4.67 | R2-narrow | Less novel; WARP's core idea is more distinctive |
| TTT Done Right (Tb9qAxT3xv) | 5.60 | R2-narrow | Stronger empirical scale; different approach to fast weights |
| TTT3R (aMs6FtNaY5) | 6.00 | R2-narrow | Stronger evaluation rigor; different task focus |

**Round 1 bracket**: 4.0–6.0.  
**Round 2 narrowing**: Against MoM (5.50) and Memory Caching (4.67), WARP's core architectural novelty is comparable to or greater than both, but its evaluation has more loose ends (BPD clarity, PEMS08 verification, missing DSR baselines). Against TTT Done Right (5.60), WARP has a more novel core architecture but less rigorous empirical validation on large-scale tasks.  
**Final placement**: 5.0 — the core idea is genuinely novel and interesting, classification results are solid against modern SSMs, and the physics-informed variant shows a clear advantage. However, the evaluation gaps (especially around PEMS08 and BPD) prevent a stronger score. The paper is above the reject threshold but would benefit from tightening the identified issues.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>