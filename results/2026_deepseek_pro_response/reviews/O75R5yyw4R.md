Now let me compare IterRef against the key Round 2 anchors:

- **DDPP (6.25)**: Also steers discrete diffusion for reward alignment, but requires fine-tuning. IterRef is purely test-time, has more thorough scaling analysis (NFE curves, k vs N, timestep analysis), and better baselines. IterRef is stronger.
- **Discrete Guidance (6.50)**: CTMC-based guidance for discrete diffusion. More theoretical but weaker empirical validation. IterRef has stronger, more comprehensive experiments across modalities with better baselines. IterRef is comparable or slightly stronger.
- **SEDD (6.60, Rejected)**: More foundational contribution (new training objective). Rejected due to incomplete experiments and theoretical gaps. IterRef's execution is more solid even if the contribution is less foundational.
- **Planned Denoising (5.75)**: Similar topic but IterRef has stronger empirical validation. IterRef is clearly stronger.
- **Fine-Tuning Discrete Diffusion (6.00)**: Different approach, narrower domain. IterRef is more general and better executed.

IterRef sits clearly above the 6.0–6.5 cluster but below the 8.0 architecture/model contributions. The method is well-motivated, theoretically grounded, empirically thorough, and the weaknesses are all addressable (not structural). I'll place it at **7.0**.

---

## Summary
This paper proposes IterRef, a test-time scaling method for discrete diffusion models that uses Multiple-Try Metropolis (MTM) with a noising-denoising transition kernel to iteratively refine intermediate states toward a reward-aligned distribution. The key insight is a carefully chosen balancing function that simplifies the MTM acceptance rule to a pure reward comparison, making the algorithm practical. The method is evaluated across two language models (MDLM, LLaDA-8B) and an image model (MaskGIT) with multiple reward functions, showing consistent gains over baselines, especially at low compute budgets.

## Strengths
- **Elegant balancing function design**: The choice of λ in Equation 2 causes importance weights to collapse to uniform selection (w_n = N⁻¹) and the acceptance ratio to simplify to β = min(1, exp((r(x_t') − r(x_t))/α)). This eliminates the need for backward auxiliary proposal generation and makes the MTM framework computationally tractable for discrete diffusion (Section 3.1).
- **Formal per-step convergence guarantee**: Proposition 1 proves that the MTM chain at a single timestep satisfies detailed balance and asymptotically converges to p*(x_t) as k → ∞, grounding the method in MCMC theory rather than heuristics.
- **Consistent empirical gains across modalities and scales**: Figure 2 shows IterRef outperforming BoN, FK, SVDD, and SoP on all four language tasks under both MDLM and LLaDA-8B. Table 1 extends this to MaskGIT image generation. Gains are most dramatic at low NFE: on MDLM, IterRef at 2T NFEs surpasses all baselines at 32T NFEs on Sentiment, CoLA, and Perplexity.
- **Novel insight that later denoising stages dominate reward alignment in discrete diffusion**: Table 2 shows that applying IterRef at 0.1T (late) consistently outperforms 0.9T (early) across all tasks — e.g., 37.6 vs. 7.0 on Toxicity. This contrasts with continuous diffusion where early steps dominate, providing new understanding of discrete diffusion dynamics.
- **Ablation validating iterative refinement over parallel exploration**: Table 3 and Figure 4 demonstrate that, under fixed total compute (k × N constant), larger k with smaller N substantially outperforms the reverse — e.g., (k=8, N=4) achieves 85.3 on CoLA vs. (k=1, N=32) at 8.7. This validates the core claim that iterative in-situ refinement is more effective than drawing more candidate particles.
- **Practical cost optimizations grounded in theory**: The balancing function design eliminates backward auxiliary proposals (nearly halving cost), and pool reuse on rejection further amortizes overhead. These are principled optimizations, not ad hoc hacks (Section 3.3).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Noising magnitude s is not specified in the main text**: The transition kernel K(x_t, x_t') = Σ q(x_s|x_t) p_θ(x_t'|x_s) depends on s (where t < s), which controls how many forward-noising steps are applied before denoising. The computational cost also depends on (s − t) as noted in Section 3.3. The paper never states what value of s (or s − t) is used in experiments, nor does it include a sensitivity analysis over this parameter. This is a reproducibility gap — the reader cannot assess whether results depend on careful tuning of an undisclosed hyperparameter.
- **Reward function and evaluation metric are the same in most experiments**: Toxicity, Sentiment, CoLA, Perplexity, and CLIPScore serve simultaneously as guidance signals and evaluation metrics. While this is standard practice in controlled generation, it limits the strength of evidence — the results primarily show that IterRef optimizes the given reward well, not necessarily that outputs are better by an independent quality standard. The detoxification case study (Section 4.5) is particularly vulnerable to reward overoptimization concerns.
- **No variance estimates reported**: With 15 prompts × 20 samples = 300 generations per data point, there is meaningful uncertainty. Figures 2, 4, and 5(a) show no error bars, standard errors, or confidence intervals, making it difficult to assess whether performance gaps — especially at low NFE budgets — are statistically meaningful.
- **Convergence claim scope could be more precise**: Proposition 1 proves per-step convergence of the MTM chain to p*(x_t) at a single timestep. The abstract states "proving convergence to the reward-aligned distribution" without clarifying the per-step scope. The paper does not actually claim full-trajectory convergence, but a casual reader could be misled. Scoping this more explicitly would prevent misinterpretation.
- **Key optimization justified only in stripped appendix**: The elimination of backward auxiliary proposals — which nearly halves computational cost — is asserted in the main text (Section 3.3) but the theoretical justification is deferred to Appendix D.2 (stripped). This optimization is important enough that a sketch of the justification belongs in the main text.

### Trivial
None.

## Nice-to-Haves
- An ablation comparing the noising-denoising kernel to a simpler kernel (e.g., direct sampling from p_θ(x_t'|x_{t+1}) without explicit noising) would quantify how much the noising step contributes versus the MTM acceptance mechanism alone.
- A sensitivity analysis over the noising magnitude s − t would help characterize the exploration-exploitation trade-off in the kernel.
- An explicit limitations section would improve the paper's completeness (e.g., reliance on reward model access, reduced effectiveness when base model already produces high-quality outputs as seen on CoLA with LLaDA-8B).
- Evaluating with a held-out reward model on at least one task (e.g., a different sentiment classifier) would strengthen evidence against reward overoptimization.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic claim that the convergence claim is presented as a full-trajectory guarantee**: The paper does not claim full-trajectory convergence. Proposition 1 is explicitly about the MTM chain at a single timestep converging to p*(x_t). The abstract's phrasing could be more precise but does not overclaim. The critic's assertion that "the paper presents it as a guarantee for the overall method" is not supported by the text.
- **Harsh Critic complaint about Algorithm 1 being "dense and difficult to parse"**: This is a subjective presentation preference. The algorithm is standard MTM formalism and is adequately explained in the surrounding text.
- **Harsh Critic critique that "the NFE accounting deserves scrutiny" for the Evenly vs. point comparison in Table 2**: The paper states that total computational budget is fixed by allocating 4T NFEs at each selected step. The comparison is fair as described.
- **Strength Finder "the problem is important" / "timely and well-justified" type claims**: These are generic framing strengths, not concrete evidence-bound strengths. Removed.

## Novel Insights
The most genuinely novel observation is that later denoising stages (near t=0) dominate reward alignment in discrete diffusion, in contrast to continuous diffusion where early stages are most influential (Table 2). This finding has practical implications for how to allocate refinement compute and suggests fundamental differences in how information is encoded across the denoising trajectory between discrete and continuous diffusion. A second insight is the empirical demonstration that iterative refinement (increasing k) is substantially more effective than parallel exploration (increasing N) at fixed compute, which provides concrete guidance for practitioners designing test-time scaling strategies.

## Suggestions
- Report the noising magnitude s − t used in experiments and include a brief sensitivity analysis, even if just in a single-task ablation. This is the single most important missing detail for reproducibility.
- Elevate the ImageReward results from Appendix C.1 to the main paper (or evaluate with an independent metric on at least one language task) to address the reward-evaluation circularity concern.
- Add a sentence to the abstract and introduction clarifying that Proposition 1 proves per-step MTM chain convergence, and that full-trajectory convergence properties are an open question.
- Add standard errors or confidence intervals to the main figures to help readers assess statistical significance of the reported gaps.

## Score and Decision

**Calibration anchors reviewed:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| DPMC (D7PQ54l5Q1) | 4.75 | R2 | MCMC for inverse problems; weaker contribution, narrower scope. IterRef is clearly stronger. |
| Planned Denoising (MJNywBdSDy) | 5.75 | R2 | Similar discrete diffusion topic but weaker empirical validation. IterRef is stronger. |
| Fine-Tuning Discrete Diff (G328D1xt4W) | 6.00 | R2 | Fine-tuning approach, narrower domain. IterRef is more general and better executed. |
| Scalable Discrete Diff Samplers (peNgxpbdxB) | 6.00 | R2 | Different domain (combinatorial optimization). Not directly comparable. |
| DDPP (Ombm8S40zN) | 6.25 | R1/R2 | Closest comparator. Requires fine-tuning; IterRef is test-time. IterRef has better scaling analysis and more baselines. IterRef is slightly stronger. |
| Discrete Guidance (XsgHl54yO7) | 6.50 | R1/R2 | More theoretical, weaker empirical validation. IterRef has stronger experiments. Comparable or IterRef slightly stronger. |
| SEDD (71mqtQdKB9) | 6.60 | R2 | More foundational (new training objective) but rejected for incomplete experiments and theoretical gaps. IterRef is more solidly executed. |
| SDXL / Würstchen / Shortcut Models | 8.00 | R1 | Major architecture/model contributions. IterRef is a methods paper, not at this tier. |
| SVDD (2fgzf8u5fP) | 3.80 | R1 | Fundamental issues with bias and experimental settings. IterRef is much stronger. |

**Round 1 bracket:** 5.5–7.5
**Round 2 narrowing:** IterRef sits above the 6.0–6.5 cluster of discrete diffusion guidance papers but below the 8.0 architecture contributions. The method is clean, well-executed, with thorough empirical validation and novel insights. Weaknesses are real but minor and addressable.

**Final score: 7.0**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>