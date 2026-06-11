## Summary

This paper introduces IterRef, a test-time scaling method for discrete diffusion models that uses Multiple-Try Metropolis (MTM) with a noising-denoising transition kernel to iteratively refine intermediate states toward a reward-aligned distribution. The key idea is to apply MCMC corrections at intermediate denoising steps — rather than only guiding the next-step transition — which allows the model to correct errors that have already occurred. The paper provides convergence guarantees and evaluates across two language backbones (MDLM, LLaDA-8B) and one image backbone (MaskGIT), showing consistent improvements over existing guidance methods.

## Strengths

1. **Principled MTM framework with tractable acceptance rule (Section 3.1, Eq. 2–3).** The design of the balancing function $\lambda(x_t, x_t') = 1/[p(x_t)K(x_t, x_t')\exp((r(x_t)+r(x_t'))/\alpha)]$ is non-trivial: it cancels the intractable marginal $p(x_t)$ and the kernel evaluation, yielding a Metropolis acceptance ratio $\beta = \min(1, \exp((r(x_t')-r(x_t))/\alpha))$ that depends only on the *difference* in intermediate rewards. This makes MTM practically executable for discrete diffusion while preserving theoretical guarantees.

2. **Consistent and often large-margin empirical superiority across tasks, backbones, and modalities (Figures 2, 5; Table 1).** On MDLM, IterRef at **4T** NFEs matches FK at **32T** NFEs on Toxicity (8× compute efficiency). On Sentiment, CoLA, and Perplexity, IterRef at **2T** NFEs outperforms all baselines at **32T** NFEs. On MaskGIT, IterRef achieves 35.8 CLIPScore at 16 NFEs vs. 34.8 for the best baseline. These span 3 backbones, 5 reward functions, and 2 modalities.

3. **Formal convergence guarantee to the reward-aligned distribution (Proposition 1).** The paper proves that under the assumption of a reversible Markov kernel $q, p_\theta$, the MTM chain satisfies detailed balance and converges to $p^*(x_t) \propto p(x_t)\exp(r(x_t)/\alpha)$. This goes beyond prior work (FK steering, SVDD, SMC) which lacks such guarantees that iterative refinement drives the distribution toward the exact target.

4. **Systematic ablation showing iterative depth ($k$) matters more than particle breadth ($N$) (Table 3, Figure 4).** Holding compute roughly constant, $k=8,N=4$ achieves 54.0 Toxicity and 85.3 CoLA on LLaDA, while $k=1,N=32$ achieves only 3.3 Toxicity and 8.7 CoLA. This directly validates the core thesis — that *iterative* refinement, not just access to more candidates, drives improvement.

5. **Effective timestep analysis revealing that later-stage refinement is more impactful in discrete diffusion (Table 2).** This finding contrasts with continuous diffusion where content is determined early, providing new insight into discrete diffusion dynamics.

6. **Practical efficiency via rejected-proposal pool reuse (Section 3.3).** When a proposal is rejected, the i.i.d. candidate pool from the same kernel remains valid, avoiding repeated forward passes and reducing per-iteration cost.

## Weaknesses

### Fatal
None.

### Major

1. **Transition kernel's noising schedule is underspecified (Section 3.1, Eq. 2; Section 3.3 cost analysis).** The kernel $K(x_t, x_t') = \sum_{x_s} q(x_s|x_t)p_\theta(x_t'|x_s)$ depends on an intermediate timestep $s$ (where $t < s$), but the paper never specifies how $s$ is chosen. The cost analysis states "each proposal must be refined over the remaining $(s-t)$ steps, resulting in $N(s-t)$ diffusion-model calls" — without knowing $s$, this cost formula cannot be evaluated and the experimental results (NFEs reported in Figures 2, 4) are not reproducible. This is the single most important missing implementation detail.

2. **Main results lack variance or error bars (Figures 2, Table 1).** The language evaluation uses 3 seeds and 15 prompts (each sampled 20 times), reported only as point estimates. With 3 seeds, run-to-run variance could be substantial, and claims such as "IterRef achieves higher reward scores with only 2T NFEs than all baselines obtain with 32T NFEs" need some measure of statistical reliability. This is standard practice for the field and should be addressed.

### Minor

3. **Theory-practice gap in the convergence guarantee (Section 3.1, lines 117–118 vs. Proposition 1).** Proposition 1's convergence guarantee targets the exact intermediate reward $r(x_t) = \alpha \log \mathbb{E}_{x_0 \sim p_\theta(\cdot|x_t)}[\exp(r(x_0)/\alpha)]$, which requires an expectation over all completions. In practice (line 117), $r(x_t)$ is approximated by evaluating the reward on a single-step prediction of $x_0$. The paper mentions this approximation in passing but does not analyze whether or how the convergence guarantee carries over. This gap is a standard limitation shared with prior work (Li et al., 2024; Singhal et al., 2025), but it should be acknowledged and discussed.

4. **Tension between Algorithm 2 and Section 3.3's efficiency claim.** Algorithm 2 (Line 8) generates $N-1$ auxiliary proposals $x_t''$, but Section 3.3 states "the practical implementation eliminates the resampling step." If the balancing function makes the auxiliary proposals unnecessary for evaluating $\beta$, the algorithm and text should be reconciled — either the algorithm should note they are optional, or the text should clarify they are retained for theoretical completeness.

5. **SoP baseline adaptation to discrete diffusion not explained (Section 4.1).** SoP (Ma et al., 2025) was designed for continuous diffusion. The paper does not explain how it was adapted to discrete tokens or whether this adaptation is fair to the method.

6. **No limitations section.** The method's dependence on reward model quality, the approximation gap in the intermediate reward, the choice of noising depth, and potential for reward over-optimization are all unaddressed.

### Trivial

7. **The "8x faster" framing in Figure 1(b) generalizes a single-task, single-backbone result** (MDLM, Toxicity reward). The paper does qualify with "up to 8×" in the caption, but the figure's prominent labeling risks overstating the average-case improvement.

## Nice-to-Haves

- A study varying the noising depth $s-t$ in the transition kernel would resolve the underspecification and add insight into how exploration depth interacts with iteration count $k$.
- An intuitive explanation of *why* the specific balancing function in Eq. 2 works would help readers who find the derivation dense.

## Removed Points

- **"Detoxification examples may be incoherent"** (Harsh Critic): The paper provides quantitative toxicity scores showing improvement. The qualitative examples are illustrative and the quantitative trajectory in Figure 5(a) is the main evidence. Removed because the criticism targets an illustrative example without evidence of systematic degradation.
- **"No discussion of missing related works"**: Cannot verify existence of unspecified related works as per instructions.
- **"Formatting/presentation nitpicks"**: Parser artifacts, not author errors.
- **"SoP disadvantage due to continuous gradient assumption"**: Speculative — the paper doesn't make this claim and the critic is inferring without evidence.
- **Strength Finder's generic strengths** (e.g., "addresses an important problem"): Removed because these are not specific to this paper.

## Novel Insights

None beyond the paper's own contributions. The finding that later-stage refinement is more impactful in discrete diffusion than early-stage (contrasting with continuous diffusion) is an interesting observation from the paper itself, not something synthesized from the reviews.

## Suggestions

1. **Specify the noising schedule.** State how $s$ is chosen relative to $t$ in $K(x_t, x_t')$ — is it always $t+1$, or is it a fixed offset, or adaptive? This is essential for reproducibility.
2. **Add error bars or standard deviations** to Figures 2 and Table 1. Even reporting standard deviations from the 3 seeds would help readers assess significance.
3. **Add a limitations section** addressing the exact/approximate reward gap, dependence on reward model quality, and choice of noising depth.
4. **Reconcile Algorithm 2 with the efficiency claims** in Section 3.3 — either note that auxiliary proposals are optional in practice, or clarify why they are retained.
5. **Tone down the "8x faster" framing** or add explicit caveats about which comparison it comes from.

## Score and Decision

### Calibration Anchors

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| DDPP (Steering Masked Discrete Diffusion) | 6.25 | R1 | Requires secondary model training; IterRef is inference-only with convergence theory. Weaknesses comparable. IterRef slightly stronger. |
| Unlocking Guidance for Discrete SS (guidance) | 6.50 | R1 | CTMC-based approach, different technical stack. Similar quality. |
| DAS (Alignment without Over-optimization) | 7.25 | R2 | Stronger theory but continuous-only, differentiable rewards required. IterRef tackles harder discrete setting. |
| DDPD (Planned Denoising) | 5.75 | R2 | Different problem (sampling efficiency vs. reward guidance). Comparable quality. |
| DNO (Direct Noise Optimization) | 5.50 | R2 | Continuous diffusion only, reward hacking issues. IterRef is stronger. |
| SVDD (Derivative-Free Guidance) | 3.80 | R1 | Fundamental issues with α=0 and biased estimates. IterRef is substantially stronger. |

### Calibration Summary

Round 1 bracketing placed IterRef in the 4.5–7.5 range based on topic similarity. Round 2 narrowing used anchors at 5.75 (DDPD), 5.50 (DNO), 6.25 (DDPP), 7.25 (DAS) to calibrate. Compared to DDPP (6.25), IterRef contributes a novel inference-only approach with convergence theory — a genuine advance over training-dependent methods — but has concrete reproducibility gaps (noising schedule, error bars). These weaknesses are addressable and do not undermine the core contribution. The paper is clearly stronger than methods with fundamental flaws (SVDD at 3.80, DNO at 5.50) and comparable to or slightly stronger than DDPP at 6.25. It falls below DAS (7.25) primarily due to missing variance reporting and a less thorough theoretical analysis of the approximation gap.

**Score: 6.0** — A solid contribution with clear novelty, broad empirical validation, and a well-motivated theoretical framework. The weaknesses are real but addressable and do not threaten the paper's core claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>