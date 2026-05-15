Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes DisCo-DSO, a deep reinforcement learning method that jointly samples discrete tokens and their associated continuous parameters in hybrid optimization spaces via an autoregressive generative model. Instead of first generating a discrete skeleton and then optimizing continuous parameters separately (decoupled approach), DisCo-DSO emits both discrete logits and continuous distribution parameters at each step, enabling joint exploration. The method is demonstrated on three tasks: a pedagogical parameterized bitstring problem, symbolic regression with constants, and decision tree policy optimization for RL, where it achieves strong results—particularly on the DT task, outperforming prior specialized methods across all four Gym environments.

## Strengths

- **Clear and well-motivated framing**: The inefficiency of decoupled optimization in hybrid spaces is convincingly argued (each discrete skeleton requires many evaluations from a black-box optimizer to complete), and the joint optimization solution is presented as a natural extension of parameterized action-space RL (Hausknecht & Stone, 2016).

- **Principled and flexible method**: The autoregressive model emitting both logits ψ⁽ⁱ⁾ for discrete tokens and distribution parameters φ⁽ⁱ⁾ for continuous values (Equation 4) is a clean extension of prior deep combinatorial optimization methods to hybrid spaces. The conditional sampling scheme (continuous parameter distribution conditioned on the chosen discrete token) is well-specified.

- **Strong empirical results on decision tree policies**: DisCo-DSO achieves the highest mean reward on all four Gym environments (MountainCar, CartPole, Acrobot, LunarLander) while maintaining comparable or lower tree complexity than prior DT-specific methods (Figure 6). This is a clear and practically relevant demonstration of the method's value. The sample-efficiency comparisons (Figure 5) directly support the central claim that joint sampling reduces total environment interactions.

- **Generality across diverse problem classes**: The same joint optimization framework is applied to three structurally different tasks (parameterized bitstring, symbolic regression, decision tree policies) with minimal problem-specific tuning, demonstrating broad applicability.

- **Controlled pedagogical task**: The Parameterized Bitstring problem cleanly isolates the effects of discrete vs. continuous contributions to reward, making the efficiency advantage of joint sampling transparent. The two landscapes f₁ (oscillatory) and f₂ (step-function) demonstrate robustness to non-differentiable objectives.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by evidence; no single flaw invalidates the central contribution.

### Minor

- **Vague symbolic regression experimental details**: The SR section (Section 4.2) never names the specific benchmark datasets used, making it impossible to assess problem difficulty, domain sizes, or the number of constants. Results are reported as an aggregate average across datasets with no per-dataset breakdown, and the text only discusses Decoupled-GP baselines in the SR results without mentioning Decoupled-RL variants. (The figure may contain more information, but the text alone leaves the SR evidence weaker than it could be.)

- **Unspecified training budgets for DT literature baselines**: In the final comparison (Figure 6) against Custode & Iacca (2023), Ding et al. (2020), and Silva et al. (2020), the paper does not state the number of training episodes or computational budget allocated to each baseline. While the primary sample-efficiency claim is already supported by Figure 5 (controlled against Decoupled baselines), the literature comparison's fairness would be strengthened by specifying budgets. The paper states that methods marked with an asterisk were "trained locally" but provides no training protocol details.

### Trivial
- Figure 7's DT visualizations are described as "too small to read"; larger annotated trees would improve readability.

## Nice-to-Haves
- Per-dataset SR results with standard errors and explicit dataset names.
- An ablation directly comparing joint vs. decoupled sampling within the *same architecture and RL objective* (controlling for the risk-seeking prior), to isolate the gap due to joint optimization alone—particularly on the SR task where Decoupled-RL results are not discussed in the text.
- Convergence visualization of the learned continuous distributions over training to confirm that the RL gradient is shaping the continuous sampling (e.g., narrowing D(β|l, φ) toward optimal values).
- Varying the number of continuous parameters in SR to directly test the claim that the advantage grows with problem complexity.

## Removed Points
These points are flagged to be removed; treat them with caution:

1. **Garbled gradient derivation (Section 3.2)** — The harsh critic claims the risk-seeking policy gradient equation is garbled and omits continuous-parameter gradients. **Removed because:** The garbled formatting (e.g., `\left.\mathrm{if}\left.l_{i}\in\bar{\mathcal{L}}\right|}A(\tau,\varepsilon,\theta)>0\right]`) is a parser artifact from PDF extraction; the original submission does not have these issues. The paper states it uses the risk-seeking policy gradient (Petersen et al., 2021a) and provides an entropy bonus term (Equation for Hᵢ) that accounts for both discrete and continuous distributions.

2. **Questioning the existence of SR benchmarks or per-dataset results possibly in stripped figures** — **Removed because:** The parser strips figures, so per-dataset visualizations that may have appeared in Figure 3 are not available. Weaknesses about "missing" content that was in stripped sections are not valid criticisms of the submitted paper.

3. **Overblown "uncontrolled budgets" for DT literature baselines** — The harsh critic presents this as a significant evidential weakness. **Removed because:** The primary sample-efficiency claim is demonstrated in Figure 5 against controlled Decoupled-RL and Decoupled-GP baselines (same architecture, same RL method, same evaluation protocol). Figure 6 compares final solution *quality*, not training efficiency, and the paper states that prior methods' provided tree structures or open-source code were used. The concern about unequal budgets is valid as a *minor* point (moved above) but does not rise to the level of an evidential weakness threatening the core claims.

## Novel Insights
None beyond the paper's own contributions. The reviews largely corroborate the paper's framing and findings.

## Suggestions
1. **Name the SR benchmarks** and provide a per-dataset breakdown (with standard errors) in the main paper to strengthen the SR evidence.
2. **For the DT literature comparison**, add a short statement about the training budget (e.g., number of episodes or function evaluations) used for each baseline, or clarify that the comparison is about final solution quality only.
3. **Consider adding an ablation** that compares DisCo-DSO against a version using the *same architecture* but decoupled continuous optimization, to directly measure the benefit of joint sampling separate from the risk-seeking objective.
4. **Improve readability of Figure 7** with larger, annotated tree visualizations.

## Score and Decision

This paper presents a well-motivated, technically sound method for joint discrete-continuous optimization with strong experimental results on decision tree policy learning. The SR evidence is the weakest part of the paper due to underspecified experimental details, but this does not undermine the core contribution, which is most convincingly demonstrated on the DT tasks. The paper is clearly written (modulo parser artifacts), the method is principled, and the empirical results on interpretable DT policies are compelling.

**Originality**: Good — extending generative discrete optimization to hybrid spaces with joint sampling is novel and practically useful.  
**Importance of research question**: High — hybrid optimization arises in many applications.  
**Claims well supported**: Mostly yes; strongest on DT tasks, weaker on SR.  
**Soundness of experiments**: Solid overall; sample-efficiency comparisons are well-controlled.  
**Clarity of writing**: Good (parser artifacts notwithstanding).  
**Value to community**: Positive — the method and DT results are likely to be useful.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>