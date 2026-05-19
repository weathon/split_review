- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 6, 8
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces STAR (Self-play muTuAl Reasoning), a method that improves small language model (SLM) reasoning at inference time without fine-tuning. STAR decouples reasoning into: (1) a generator that augments MCTS with five human-like reasoning actions (e.g., decompose, rephrase, propose sub-question) to construct reasoning trajectories, and (2) a discriminator (another SLM) that verifies trajectories via "mutual consistency" — masking part of a trajectory and checking if the discriminator arrives at the same answer when completing it. Experiments across 5 SLMs (LLaMA2-7B, Mistral-7B, LLaMA3-8B, etc.) and 5 reasoning tasks show large gains — e.g., LLaMA2-7B on GSM8K from 12.51% (few-shot CoT) to 63.91% (STAR), and LLaMA3-8B-Instruct from 74.53% to 91.13%.

## Strengths

- **Large and consistent accuracy gains across weak SLMs**: STAR boosts LLaMA2-7B on GSM8K from 12.51% (few-shot CoT) to 63.91% — a >51 point gain with only 32 MCTS rollouts and no fine-tuning (Table 1, rows 190 vs 198). The gains are consistent across all 5 SLMs and all 4 main benchmarks, whereas baselines like SC and RAP sometimes regress (e.g., SC@128 on StrategyQA for LLaMA3-8B-Instruct drops below few-shot CoT: 66.67% vs 68.41%, while STAR reaches 71.57%).

- **Mutual consistency outperforms standard verification**: The discriminator ablation (Table 4 left) shows that on SC-generated trajectories for LLaMA3-8B on GSM8K, mutual consistency yields 85.06% vs 74.00% for self-verification and 67.55% for majority voting — direct evidence that the proposed verification mechanism is more effective than existing alternatives for SLMs.

- **Rich action space provides measurable improvement over single-action MCTS**: The action-space ablation (Table 2) on LLaMA3-8B (200 GSM8K samples) shows the full 5-action set achieves 75.0% vs 70.5% for RAP's single action (A3) — a +4.5 point improvement attributable specifically to the richer action design.

- **Low-resource effectiveness**: Figure 2 shows that even with only 2 MCTS rollouts, STAR improves LLaMA3-8B-Instruct GSM8K accuracy to ~86%, far above 2-rollout SC (~68%) and RAP (~72%), demonstrating effectiveness under tight inference budgets.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Fine-tuning comparison not in the main results table**: The abstract and teaser figure claim that STAR "matching or even surpassing the reasoning performance achieved after domain-specialized SFT." The paper mentions in text (line 255) that Mistral+STAR outperforms fine-tuned MetaMath by +4.18%, and references a teaser figure for LLaMA2-7B comparison. However, no fine-tuned baseline numbers appear in the main comparison tables (Table 1). For a headline claim that motivates the paper's significance, the comparison should be directly transparent in the main results table — either by adding SFT rows or by including a dedicated table. This does not undermine the paper's core contribution (inference-time improvement without fine-tuning) but it limits how fully the reader can evaluate this particular claim.

2. **No variance or confidence intervals reported**: Key results (Table 1, Table 4, ablation studies) are reported as single numbers without error bars or variance estimates. Given the stochastic nature of MCTS rollouts and sampling-based methods, some measure of stability (e.g., 3-run means with std dev) would strengthen confidence in the results, especially for the discriminator ablation where some margins are narrow.

3. **Discriminator analysis could be deeper**: The mutual consistency filter shows a striking 17.5% absolute improvement on random SC trajectories (67.55% → 85.06% for LLaMA3-8B). The paper does not report what fraction of trajectories pass the consistency check, or the accuracy of accepted vs. rejected trajectories. While the aggregate results convincingly show the discriminator's value, such analysis would help the community understand *when and why* mutual consistency works.

### Trivial
None.

## Nice-to-Haves

- **Cost/efficiency analysis**: The paper uses 32 MCTS rollouts plus discriminator runs. A comparison of total inference cost (tokens generated, latency) relative to SC@128 or SC@64 would help practitioners contextualize the gains.
- **MATH-500 evaluation on more base models**: Only two instruction-tuned models are evaluated on MATH-500 (due to LaTeX challenges). Adding a fine-tuned base model or discussing the limitation more thoroughly would strengthen the generalization claim.
- **Analysis of failure modes**: The discriminator may struggle on tasks with very long or technical reasoning chains (e.g., code generation). A limitations discussion would be useful for future work.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Reward function definition contains a potential circularity"** — The paper uses the likelihood (confidence) of self-consistency majority voting from the terminal node as the reward. This is standard MCTS practice (analogous to Monte Carlo rollouts in AlphaGo). Multiple completions from a terminal state to estimate its value is a well-understood estimation technique, not a circular reference. Removing this criticism (it is based on a misunderstanding of standard MCTS rollouts).

- **"RAP and ToT baselines may have unfair hyperparameters"** — The paper states it follows the original implementations for both (line 252). The ablation study (Table 3) further directly compares STAR's generator to RAP and SC generators under identical answer-verification conditions, which is more informative than tuning baselines. Removing this criticism (standard practice).

- **"MATH-500 results use only two models and gains are modest"** — The paper explicitly explains the LaTeX difficulty for non-instruction-tuned models (line 267). The gains (+9.14% for LLaMA3-8B-Instruct) are substantive. Removing this criticism (scope is stated and justified).

- **"No cost or efficiency analysis"** — This is a nice-to-have, not a weakness. Moved to Nice-to-Haves.

- **"Discriminator self-discrimination when target is Phi3"** — The paper acknowledges this explicitly (line 246). Removing (already addressed).

- **Generic speculative concerns from the harsh critic about whether the mutual consistency mechanism "exploits a statistical regularity"** — No evidence is presented for this speculation; the mechanism is well-described and empirically validated to outperform alternatives. Removing (speculative, not evidenced).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add explicit fine-tuned baseline rows (e.g., MetaMath, MathCoder) to Table 1 or create a dedicated comparison table to fully substantiate the abstract's claim about matching/surpassing SFT.
2. Include variance estimates (e.g., mean ± std over 3 runs) for key results, especially for the stochastic MCTS generator and discriminator ablations.
3. Add an analysis of what fraction of trajectories pass the mutual consistency filter, and the accuracy of accepted vs. rejected trajectories, to help the community understand the discriminator's behavior.
4. Add a brief limitations discussion covering settings where the method may be less effective (e.g., very long reasoning chains, or when both SLMs are too weak).
