- Decision: Accept
- Avg Score: 5.25
- Scores: 1, 6, 8, 6
Now I have all the information I need. Let me synthesize the final review.

## Summary
This paper proposes Equilibrium Ranking (ER), a training-free game-theoretic decoding method for language models. It casts LM decoding as a regularized signaling game between a generator and discriminator, and uses no-regret learning (piKL) to find approximate regularized Nash equilibria that reconcile generative and discriminative LM predictions. Evaluated on six QA benchmarks (MMLU, ARC, RACE, HHH, TruthfulQA, GSM8K) with LLaMA-7B/13B, ER consistently improves over standard baselines and, on several benchmarks, enables the 13B model to match or exceed much larger models (LLaMA-65B, PaLM-540B).

## Strengths
- **First game-theoretic formulation of LM decoding as a regularized signaling game.** Section 2 explicitly states this is the first proposal to use regularized equilibrium concepts in signaling games for language generation (line 90). The formalization cleanly operationalizes the twin desiderata of coherence (Nash equilibrium) and reasonableness (KL regularization toward initial LM policies) in a single principled framework.
- **Consistent accuracy gains across six diverse benchmarks.** Table 1 shows that ER-D (Equilibrium Ranking Discriminator) outperforms Generative, Mutual Information, Self-Contrastive, and Discriminative ranking on nearly all dataset–model combinations. On ARC-Challenge, ER-D with LLaMA-13B (61.4%) surpasses LLaMA-65B (56.0%) and PaLM-540B (53.0%) by 5–8 percentage points (lines 173–174), demonstrating that the method extracts substantially more correct signal from a smaller model without additional training.
- **Training-free and computationally efficient.** The method modifies only signaling policies, not LM weights (line 99). Each iteration costs ~40 microseconds and is linear in the number of candidate sequences (line 136, footnote on line 146), making it far cheaper than deliberation methods like multi-step self-refinement or tree-of-thought.
- **Rigorous regret bounds and convergence guarantees.** Section 2.2 provides three formal properties: convergence of average play to regularized coarse-correlated equilibria, bounded divergence from initial policies (controlled by λ), and logarithmic regret growth. These ground the approach in established game-theoretic learning theory.
- **Composability with deliberation methods.** GSM8K experiments (Section 3) show ER can be combined with chain-of-thought and self-consistency, achieving slight gains over majority vote alone. This demonstrates the method is not orthogonal to existing techniques but can be layered on top.
- **Mitigation of negative scaling on TruthfulQA.** The paper reports that while generative ranking (Greedy) drops from 7B to 13B (a known negative scaling issue), ER-based ranking improves across model sizes, directly countering this problem (line 188).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Hyperparameter sensitivity undermines a robustness claim.** The paper states that ER "consistently yields improved results, surpassing or at least matching the performance of all baseline approaches" (line 214). However, on HHH with LLaMA-13B and default parameters (λ=0.1), ER-D (69.2%) underperforms the discriminative ranking baseline D (69.5%) (line 180). The paper notes that tuning λ_gen=0.01, λ_dis=1.0 recovers a lead (70.6%), but this counterexample shows the method is not universally robust at default parameters. Since all hyperparameters are fixed at 0.1 across all tasks with no sensitivity analysis, it is unclear whether other reported gains are similarly contingent on fortuitous parameter choices. An analysis of how performance varies with λ values on a few tasks would substantially strengthen the paper.

- **Uneven evaluation settings in large-model comparisons.** The paper highlights that ER on LLaMA-13B "outperforms the much larger LLaMA-65B and PaLM-540B models" on ARC-Challenge (lines 173–174). However, the cited LLaMA-65B and PaLM-540B scores (56.0 and 53.0) are few-shot results from the original papers, while ER uses zero-shot prompts (line 171). While still impressive, the comparison is not apples-to-apples. The paper should explicitly note the different evaluation settings when making these comparisons.

- **No ablation isolating the contribution of equilibrium search vs. normalization.** The initial policy normalization (dividing LM probabilities by sums over v and y, lines 103–111) is critical for calibration and resembles contrastive decoding. Without an ablation comparing "π_gen^(1) ranking with vs. without normalization," the marginal contribution of the equilibrium search itself is not isolated from the normalization technique. Including this ablation would clarify exactly where the gains come from.

- **No empirical convergence visualization.** The paper claims "good convergence properties in practice" (line 134) but provides no plot of regret, policy divergence, or the objective over iterations. A figure showing the evolution of policies or consensus would strengthen the empirical grounding of the convergence claim.

- **GSM8K gains are marginal.** ER yields only small improvements over self-consistency majority vote (e.g., LLaMA-13B: 31.8% MV vs 33.1% ER-D), with overlapping confidence intervals (line 202, Table 3). The paper acknowledges this ("on par or slightly better"), but it does temper the "substantial improvements" language used elsewhere.

### Trivial
- The paper lacks a dedicated limitations section. Important failure modes worth noting: (a) if both initial generator and discriminator are poor, the equilibrium will also be poor; (b) the method assumes a fixed candidate set, which may exclude the correct answer entirely; (c) the uniform prior over vtrue/vfalse is unrealistic for domains where correct answers are rare.

## Nice-to-Haves
- Adding contrastive decoding (Li et al. 2022) as a standalone baseline would further clarify whether the equilibrium machinery adds value over a simpler two-model contrastive approach (though the paper's SC baseline already captures the essential idea).
- Providing the exact prompt templates used for conditioning on vtrue and vfalse in an appendix would improve reproducibility (the current description of "Answer:" vs "Incorrect Answer:" is brief but arguably sufficient).
- Testing whether the uniform prior over vtrue/vfalse could be replaced with a data-derived prior.

## Removed Points
These points are flagged to be removed, treat them with caution:
1. **"Baseline selection too narrow" (missing contrastive decoding, verifier re-ranking, self-consistency on MC tasks)** — Removed because: (a) the SC baseline is explicitly described as resembling contrastive decoding and captures the essential idea; (b) verifier-based re-ranking requires training a separate model and is out of scope for a training-free method; (c) self-consistency is designed for free-form generation with CoT, not for standard multiple-choice with fixed candidates.
2. **"Lack of statistical significance for multiple-choice tasks"** — Removed because for fixed candidate sets with deterministic scoring procedures, variance is zero or negligible. The paper already provides standard deviations for the generative tasks (TruthfulQA, GSM8K) where sampling variance exists. This is standard practice in the field.
3. **"Computational cost phrasing is misleading"** — Removed because the paper's claim is accurate: the equilibrium search does eliminate the need for *repetitive* LM queries (it requires one forward pass per candidate per mode, comparable to mutual information or discriminative ranking). The phrasing is not misleading.
4. **"Prompt template details insufficient"** — Removed because "standard zero-shot prompt" with "Answer:" vs "Incorrect Answer:" is sufficiently specific for reproducibility.
5. **Various generic section-by-section nitpicks about missing proofs in the appendix, contrastive decoding not being a separate entry, etc.** — These reflect the stripped appendix (standard parser issue) or are overly demanding.

## Novel Insights
None beyond the paper's own contributions. However, one insight that emerges from considering the strengths and weaknesses together is that the value of the game-theoretic framework may lie less in the equilibrium search per se (the gains over the already-normalized SC and D baselines are modest in some settings) and more in providing a principled, theoretically grounded justification for an iterative reconciliation procedure. Whether practitioners would realize equivalent gains from a simpler fixed-point iteration (without the game-theoretic machinery) is an open question the paper does not address, but the theoretical guarantees are a genuine differentiator.

## Suggestions
1. Add a sensitivity analysis for λ_gen and λ_dis on 2–3 tasks (e.g., fixing all but one parameter and sweeping over {0.01, 0.1, 1.0}). This would clarify whether the default 0.1 is generally reasonable or luckily chosen.
2. Add an ablation comparing "normalized SC/D ranking" vs "raw LM probability ranking" to isolate the contribution of the equilibrium search from the normalization.
3. Add a convergence plot showing regret or policy divergence over iterations for one example from ARC and TruthfulQA.
4. When comparing to larger models, explicitly state the evaluation settings (e.g., "zero-shot ER on LLaMA-13B vs. 5-shot LLaMA-65B vanilla decoding").
5. Add a brief limitations paragraph discussing when ER might fail (poor initial policies, fixed candidate set, uniform prior).
