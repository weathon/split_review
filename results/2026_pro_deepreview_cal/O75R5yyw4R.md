Now I have a thorough understanding of the paper and calibration anchors. Let me compile the final review.

## Summary

This paper proposes IterRef, a test-time scaling method for discrete diffusion models that uses Multiple-Try Metropolis (MTM) with a noising-denoising transition kernel to iteratively refine intermediate states toward a reward-aligned distribution. The method can be applied selectively at chosen timesteps, allowing flexible compute allocation. Experiments span text generation (MDLM, LLaDA-8B) on four reward tasks and image generation (MaskGIT) with CLIPScore, consistently outperforming baselines including FK Steering, SVDD, SoP, and Best-of-N.

## Strengths

- **Strong, broad empirical validation**: IterRef consistently outperforms all baselines across text generation (MDLM and LLaDA-8B on Toxicity, Sentiment, CoLA, Perplexity) and image generation (MaskGIT with CLIPScore). On MDLM with Toxicity, IterRef matches the best baseline at 8× lower NFE (4T vs. 32T). Table 1 shows clear margins on MaskGIT across all NFE budgets (e.g., 33.7 vs. 32.1 at NFE=2).

- **Principled kernel design with practical simplification**: The specific choice of transition kernel $K$ and balancing function $\lambda$ (Eq. 2) yields uniform proposal weights and a simple reward-ratio acceptance rule $\beta = \min(1, \exp((r(x_t') - r(x_t))/\alpha))$ (Eq. 3), eliminating the need for backward auxiliary proposals in practice and making the method computationally tractable while retaining MTM structure.

- **Valuable insight about effective refinement timesteps**: Table 2 demonstrates that applying IterRef at later denoising stages (e.g., 0.1T) yields substantially higher reward improvement than early stages, and on CoLA, late-stage-only application even surpasses evenly-distributed application. This contrasts with continuous diffusion where early steps dominate, providing actionable guidance for discrete diffusion sampling.

- **Strong evidence for iterative refinement over larger particle sets**: Table 3 shows that increasing iterations $k$ with fewer particles $N$ (e.g., $k=8, N=4$) outperforms one-shot configurations with the same budget (e.g., $k=1, N=32$), directly validating the core claim that progressive refinement is more effective than single-pass particle search.

## Weaknesses

### Fatal

None.

### Major

- **Theoretical scope is narrower than implied by the framing**: Proposition 1 guarantees convergence of the MTM chain to $p^*(x_t)$ at a single timestep, assuming reversibility of $q$ and $p_\theta$. The paper does not provide a guarantee for the full denoising trajectory, since after MTM refinement the algorithm uses the base denoiser $p_\theta(x_{t-1}|x_t)$ rather than the optimal transition $p^*(x_{t-1}|x_t)$. The abstract's claim of "convergence to the reward-aligned distribution" is ambiguous about whether this refers to per-timestep or full-trajectory convergence. The empirical results are strong regardless, but the theoretical claims should be scoped more precisely to match what is actually proven.

- **Unverified reversibility assumption in Proposition 1**: The convergence proof assumes that $q$ (the forward noising process) and $p_\theta$ (the learned reverse process) form a reversible Markov kernel. In discrete diffusion with absorbing states, this condition is not generally satisfied, and the paper provides no justification or empirical verification. While assuming reversibility is common in MCMC-inspired methods, the strength of the theoretical contribution depends on this assumption, and its plausibility in the discrete diffusion setting is not discussed.

### Minor

- **The noise level $s$ in the transition kernel is underspecified**: Equation 2 defines $K(x_t, x_t') = \sum_{x_s} q(x_s|x_t) p_\theta(x_t'|x_s)$ with only the condition "$t < s$." It is not stated whether $s$ is a specific fixed offset (e.g., $s = t + \delta$) or sampled from a distribution, which affects reproducibility. Section 3.3 references remaining $(s-t)$ steps of refinement, suggesting a particular choice, but this should be made explicit in the method definition.

- **Algorithm 2 includes auxiliary proposals that Section 3.3 says are eliminated**: The practical simplification in Section 3.3 states that the balancing function choice eliminates the need for backward auxiliary proposals $x_t''$, yet Algorithm 2 Line 8 still generates them. The algorithm should either reflect the practical implementation or the text should clarify that Algorithm 2 shows the general MTM procedure and that Line 8 is omitted in practice.

- **No diversity evaluation**: The paper evaluates primarily on reward scores (the optimization target), with Perplexity and CoLA as partial quality proxies. However, for a reward-guided generation method, it is important to assess whether the method merely collapses to a narrow set of high-reward modes. The detoxification examples in Figure 5(b) show outputs that become semantically unrelated to the input ("so over this place called Trinidad" from "I hate you..."), which raises the question of whether reward optimization trades off relevance. Diversity metrics (e.g., self-BLEU, distinct-$n$) or a small human evaluation would strengthen confidence that the method preserves output variety.

### Trivial

- The "8× faster" label in Figure 1(b) and the "2× improvement" claim in the introduction rely on specific NFE points and should be qualified with the specific comparison point (e.g., "8× faster to reach the same reward as FK at 32T NFE").

## Nice-to-Haves

- A controlled experiment replacing the MTM kernel with a simpler perturbation (e.g., random remasking with uniform re-denoising) would isolate the benefit of the reward-guided design and demonstrate that the performance comes from the specific kernel and acceptance step, not just from adding noise.
- Guidance on how to choose the effective timestep set $\mathcal{U}$ for a new task or model would improve practical applicability beyond the empirical findings in Table 2.
- Reporting generative-model calls and reward-model calls separately (as the paper itself suggests in Section 3.3) would give a clearer picture of compute trade-offs, especially since the dominant cost differs between small models (MDLM) and large models (LLaDA-8B).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh critic: "The algorithmic structure does not sample from the intended reward-aligned distribution over the whole trajectory" (claimed as fatal).** REMOVED as a fatal claim because the paper's Proposition 1 is explicitly scoped to convergence of $x_t$ to $p^*(x_t)$ at each timestep (Section 3.1: "our goal is to sample each intermediate state $x_t$ in the denoising process from the optimal distribution $p^*(x_t)$"). The paper does not claim the full trajectory samples from $p^*(x_0)$. The abstract's phrasing could be more precise, but this is a scoping clarity issue, not a fundamental error. Retained above as a Major weakness concerning scoping precision.

- **Harsh critic: "The missing appendix prevents verification" of derivations.** REMOVED per hard rules — the parser strips appendices; they exist in the original submission.

- **Harsh critic: "The relationship between MTM refinement and effective timestep set is described as flexible, but no guidance is given on how to choose $\mathcal{U}$."** MOVED to Nice-to-Haves — the paper provides empirical guidance in Section 4.4 (Table 2) showing that later timesteps work better, which is substantive practical guidance.

- **Harsh critic: Comparison with DSearch and PG-DLM should be more clearly contrasted.** REMOVED — the paper's Related Work section (Section 5) already explicitly contrasts IterRef with these methods: "IterRef does not search over trajectories nor maintain multiple trajectories. Instead, it leverages the noising-denoising structure...to iteratively refine the current state itself." This is a clear positioning statement.

- **Strength Finder: "Theoretical grounding and convergence guarantee."** Downgraded from core strength — the convergence guarantee is per-timestep only and depends on an unverified reversibility assumption. Retained as qualified above.

- **Harsh critic: NFE counting aggregates reward and generative model costs.** MOVED to Nice-to-Haves — the paper already acknowledges this issue explicitly in Section 3.3 and states that Appendix C.4 provides wall-clock time analysis.

- **Harsh critic: "8× faster" should be further qualified.** Retained as Trivial — the paper does qualify it in context but the phrasing could be more precise.

## Novel Insights

The finding that late-stage refinement is more effective than early-stage refinement in discrete diffusion (Table 2) is genuinely novel and contrasts with the well-known pattern in continuous diffusion where early steps dominate content formation. This observation, combined with the finding that iterative refinement (higher $k$, lower $N$) outperforms one-shot particle search (Table 3), provides actionable design principles for future test-time scaling methods in discrete diffusion that go beyond the specific MTM implementation.

## Suggestions

- Clarify the scope of Proposition 1 explicitly in the abstract and introduction: the convergence guarantee applies to intermediate states $x_t$ at each timestep, not to the full trajectory distribution $p^*(x_0)$. This would preempt the most significant theoretical concern.
- Either simplify Algorithm 2 to reflect the practical implementation (removing Lines 8 and the auxiliary proposal generation) or add a note in the caption explaining that the auxiliary proposals are shown for completeness of the MTM description but are not needed in practice due to the balancing function choice.
- Specify the noise level $s$ used in the kernel $K$ explicitly (e.g., $s = t + \delta$ with $\delta$ stated, or describe the sampling procedure for $s$).
- Add a brief discussion of the reversibility assumption — even a sentence acknowledging it as a limitation and noting that in practice the MTM chain still empirically improves alignment would address the concern.

## Score and Decision

**Round 1 bracket:** 5.5–7.0, based on comparison with low-band anchors (1.50–3.20, clearly weaker), middle-band anchors (4.00–6.80 range), and high-band anchors (8.00+, clearly stronger).

**Round 2 narrowing anchors:**
- DDPP (6.25): Steering MDMs via posterior prediction — comparable scope, training-based. IterRef is test-time only and has broader empirical evaluation (LLaDA-8B, MaskGIT). Marginally stronger.
- Demons (6.20): Training-free diffusion alignment — comparable. IterRef has more comprehensive evaluation (text + image, multiple backbones). Slightly stronger.
- DAS (7.25): SMC-based training-free alignment for continuous diffusion — stronger theoretical framing but evaluated on only one model (SD v1.5). IterRef has broader empirical coverage but weaker theoretical precision. Slightly weaker.
- ScaleCrafter (6.50): Training-free higher-res generation — different domain, comparable quality level. IterRef is similar in contribution weight.

IterRef falls between DDPP/Demons (6.20–6.25) and DAS (7.25). It is stronger than the 6.2-range papers in empirical breadth but has theoretical imprecisions that keep it below the 7.25 anchor. The closest match is DDPP (6.25) — IterRef offers a test-time alternative to DDPP's training-based approach, with comparably strong results and a comparably strong-but-imperfect theoretical story. I place IterRef at 6.0, acknowledging that the empirical results are slightly broader than DDPP's but the theoretical presentation has minor imprecisions that DDPP largely avoids.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>