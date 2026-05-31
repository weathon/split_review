## Summary
IterRef introduces a test-time scaling method for discrete diffusion models that uses Multiple-Try Metropolis (MTM) to iteratively refine intermediate denoising states toward a reward-aligned distribution. The method formulates a noising-denoising transition kernel and a carefully chosen balancing function that yields uniform importance weights and a simple reward-gap acceptance ratio, offering a provably convergent MCMC procedure. Experiments cover MDLM and LLaDA-8B for language and MaskGIT for image generation, consistently outperforming importance-sampling, SMC, and FK-Steering baselines across diverse reward functions.

## Strengths
- **Principled MTM derivation with clean closed forms:** The choice of the balancing function in Eq. 2 collapses importance weights to uniform ($w_n = N^{-1}$) and reduces the acceptance ratio to a single reward-gap term (Eq. 3). This is non-trivial: it enables efficient rejection sampling without resampling auxiliary proposals, reducing per-iteration cost by ~50% while preserving the MTM theoretical guarantee. The derivation is clean and the result is practically significant.
- **Consistent, substantial empirical gains:** IterRef is evaluated across five reward functions, two language backbones (MDLM, LLaDA-8B) and one image backbone (MaskGIT), and outperforms all baselines uniformly. The "8× faster" claim (matching FK at 32T NFEs using only 4T) is supported by Figure 2 and Table 1, and the effect holds at both low- and high-budget regimes.
- **Convergence guarantee (Proposition 1):** The paper formally proves that the MTM chain with the proposed kernel satisfies detailed balance and converges to $p^*(x_t)$ as iterations $k \to \infty$. While the proof depends on the reversibility assumption for $q$ and $p_\theta$, this is still a stronger guarantee than is typical for inference-time guidance papers.
- **Actionable empirical insights:** Two findings go beyond standard benchmark comparisons. First, increasing iteration count $k$ is consistently more effective than increasing particle count $N$ at equal NFE budget (Table 3, Figure 4), which directly informs practical deployment. Second, late-stage denoising steps are the most impactful refinement sites for discrete diffusion (Table 2), contrary to the early-stage importance observed in continuous diffusion.
- **Cross-modal generalization:** The method is applied unchanged to a VQ-token image diffusion model (MaskGIT) with CLIPScore, achieving +1.0–1.6 CLIPScore improvement over FK and BoN at equal budgets (Table 1). This demonstrates the method is not tailored to text.

## Weaknesses

### Fatal
None.

### Major
- **NFE aggregation ambiguity in practice:** Section 3.3 explicitly acknowledges that "aggregating [diffusion-model calls and reward-model calls] into a single NFE value may obscure meaningful differences," yet the main results (Figure 2, Table 1) appear to use a single combined NFE count. For IterRef with parameters $(N, k)$, the per-refinement cost is $N(s-t)$ diffusion calls plus $N$ reward calls. If baselines (BoN, FK) have different mixes of diffusion vs. reward evaluations, equal-NFE comparisons can systematically favor whichever method's ratio aligns with cheaper component. The wall-clock analysis is relegated to Appendix C.4 rather than verified alongside the main results, making it difficult to confirm that the "8×" speedup claims survive wall-clock scrutiny.
- **Diversity and generation quality are not evaluated alongside reward:** Reward-guided generation methods can reward-hack—producing repetitive or degenerate text that scores well on a narrow classifier without genuine semantic quality. The paper reports only the reward metric as the primary outcome; perplexity is used as a reward signal in one task, not as an independent diversity/fluency measure of outputs from other tasks. Showing that IterRef maintains generation diversity (e.g., unique n-grams, or self-BLEU) as rewards improve would substantially strengthen the claims, particularly for the toxicity and sentiment tasks.

### Minor
- **Reversibility assumption for $p_\theta$:** Proposition 1 requires that "q and $p_\theta$ form a reversible Markov kernel." In practice, $p_\theta$ is an imperfect learned approximation; its forward-backward symmetry is not guaranteed. The paper does not discuss how close to reversible real models are or what the practical implication of violation is. A brief discussion would clarify the gap between theory and empirics.
- **CoLA exception on LLaDA-8B:** The paper attributes BoN outperforming IterRef on the CoLA task with LLaDA-8B to LLaDA's already high grammatical quality, making intermediate-state corrections destabilizing. This is an important caveat: IterRef's benefit diminishes when the base model is strong and the reward is easily satisfied. The scope of this limitation could be discussed more directly rather than in passing.
- **Effective timestep choice left heuristic:** Table 2 shows that "Evenly" achieves the best aggregate results, but uniform application multiplies cost. The paper discusses selective refinement via $\mathcal{U}$ as a compute knob, but does not provide a principled criterion for selecting which timesteps to include given a fixed budget. This leaves a practical gap the user must resolve by task-specific search.

### Trivial
- Figure captions appear duplicated in the parsed version (parser artifact).

## Nice-to-Haves
- A diversity metric (e.g., distinct-n, self-BLEU) plotted alongside reward across NFE budgets would help confirm that IterRef avoids reward-hacking.
- A brief discussion of what model-size regime makes the reward-call vs. diffusion-call tradeoff non-trivial, to help readers decide when wall-clock time will track NFE closely.

## Novel Insights
The most genuinely novel insight is the equivalence derived from the choice of balancing function: by selecting $\lambda$ as in Eq. 2, the noising-denoising kernel makes all candidate proposals equally weighted at selection time, and the entire correctness burden is absorbed into the single scalar acceptance test $\beta = \min(1, \exp((r(x_t') - r(x_t))/\alpha))$. This is mathematically clean and practically powerful—it eliminates the need to normalize over exponentially large discrete state spaces during selection and avoids auxiliary re-sampling during acceptance. The secondary insight—that discrete diffusion's reward-critical timesteps lie in the *late* denoising stages, opposite to continuous diffusion—is empirically well-supported and has implications for where to allocate test-time compute in masked language models generally.

## Suggestions
- Report wall-clock times alongside NFE curves in the main body for at least one backbone, or decompose the NFE axis into (diffusion calls, reward calls) to make the fairness of comparisons unambiguous.
- Add a diversity measurement (distinct-n or entropy of reward-optimized outputs) to Figure 2 or as a separate figure, to address the reward-hacking concern.
- Briefly address the reversibility assumption for $p_\theta$ either empirically (how close is a trained MDLM to satisfying it) or with a robustness discussion for when approximate reversibility holds.
- Provide a lightweight heuristic or criterion for selecting the effective timestep set $\mathcal{U}$ given a fixed budget, making the method more immediately deployable without extensive tuning.

## Score and Decision
IterRef addresses a real and underserved problem (test-time scaling for discrete diffusion), proposes a theoretically grounded method with provable convergence, demonstrates consistent large empirical gains across modalities, and contributes actionable insights about iteration vs. particle tradeoff and the importance of late denoising steps. The main concerns—NFE aggregation fairness and lack of diversity evaluation—are significant enough to warrant attention but not fatal: the qualitative examples and the pattern of results across diverse tasks make reward-hacking unlikely as the sole explanation, and the wall-clock analysis reportedly exists in the appendix. The work is solidly above the conference median.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>