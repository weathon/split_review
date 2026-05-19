- Decision: Accept
- Avg Score: 6.00
- Scores: 3, 8, 5, 8
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes DICE, a method that leverages the implicit reward model from a DPO-trained LLM to iteratively construct preference datasets for further self-alignment without external feedback. DICE applies length-regularized reward shaping (to mitigate length bias) and experience replay (to prevent catastrophic forgetting). On AlpacaEval 2, DICE achieves 8–9% length-controlled (LC) win rate improvements over strong 7B/8B base models, with the best DICE-Llama3 8B model reaching 27.55% LC win rate.

## Strengths

- **Novel bootstrapping with DPO implicit rewards without external feedback.** The core idea — using the implicit reward from DPO (Equation 2: \(r(\mathbf{x},\mathbf{y})=\beta \log \pi_\theta/\pi_{\text{ref}}\)) to construct preference data for iterative self-alignment — is a clear departure from prior methods that require external reward models or LLM-as-a-judge. This is evidenced by the 9.35% LC win rate improvement on Llama3-8B (Table 1) and the algorithm in Section 4.

- **Length-regularized reward shaping with automatic α selection.** The paper introduces a length penalty term in the implicit reward (\(r_{\text{LR}} = \beta \log \pi_\theta/\pi_{\text{ref}} - \alpha|\mathbf{y}|\)) and optimizes α via random search to minimize the absolute length difference between winning and losing responses (Equation 4). This reduces the average length difference from 1031 to −21 (Figure 1), effectively mitigating length exploitation.

- **Experience replay balances offline and generated data.** Mixing a fraction γ of high-quality offline preference data with on-policy generated data prevents catastrophic forgetting. The ablation (Figure 2/3) shows γ=0.5 yields the best LC win rate, demonstrating the benefit of this balance.

- **Strong empirical results on a standard leaderboard.** DICE-Llama3 8B achieves 27.55% LC win rate on AlpacaEval 2, outperforming Gemini Pro (24.38%) and many larger models, using only 8B parameters and no additional human annotations (Table 2). The improvement over the base model (18.20 → 27.55) is substantial and well-documented.

- **Compatibility with other direct alignment algorithms.** The generated preference dataset from DICE also improves KTO, IPO, and Hinge loss algorithms, showing the dataset is not tied to DPO (Section 5.3).

## Weaknesses

### Fatal

None.

### Major

- **Evaluation on a single benchmark.** The paper's core claims about "significantly improves alignment" rest entirely on AlpacaEval 2 results. While this is a standard leaderboard, a single evaluation setting — especially one using GPT-4 as judge — cannot fully validate that the method improves alignment quality broadly. Without additional evidence (e.g., MT-Bench, human evaluation, or at least another automated benchmark), it is unclear whether the gains generalize or are specific to this evaluation configuration. The prominent claim in the abstract ("superior performance than Gemini Pro") is based on this single benchmark. The method would be significantly strengthened by multi-faceted evaluation.

- **No uncertainty or variance reporting.** All experimental results appear to be from single runs. AlpacaEval evaluations have known variance due to GPT-4 judge stochasticity and sampling temperature. Without confidence intervals or results from multiple seeds, it is impossible to assess whether reported improvements (e.g., 8.02% and 9.35%) or ablation differences of ~1% (Figure 3) are statistically significant. At minimum, bootstrapped confidence intervals or results from 3 seeds should be reported.

### Minor

- **LLM-as-a-Judge baseline uses a simplified setup.** The paper compares DICE to "LLM-as-a-Judge," where the base model is directly prompted for preference scores (0–5) without the supervised fine-tuning on evaluation data used in the original Self-Rewarding LM (Yuan et al., 2024). The authors acknowledge this difference, but the baseline likely underperforms due to weaker judging capability rather than a failure of the self-rewarding paradigm. A comparison with a properly fine-tuned judge would make the case for DICE stronger.

- **Gemini Pro comparison deserves clearer caveats.** The abstract states DICE "achieves superior performance than Gemini Pro," but this is a leaderboard comparison across different model families, training data, and training setups — not a controlled experiment. While the paper frames this appropriately in the main text as a leaderboard comparison, the abstract's framing is disproportionately strong for an uncontrolled comparison. The more meaningful result (DICE vs. its own base model, 18.20 → 27.55) is already impressive and should be the headline.

- **Limited diagnostic analysis of iteration saturation.** The paper notes that improvement stops after 2–3 iterations (and acknowledges this in the limitations) but does not analyze *why* — e.g., whether the implicit reward degrades (reward saturation), whether the policy collapses to a narrow output distribution, or whether the generated preference data loses diversity. Such analysis would sharpen the contribution and inform future work.

- **Ablation on α uses only three values.** The α ablation tests α=0, α=α\*=0.023, and α=2α\*. A finer-grained sweep at values between α\* and 2α\* would increase confidence that the proposed objective reliably selects the optimal α for downstream performance.

### Trivial

None.

## Nice-to-Haves

- A human evaluation on a subset of prompts would directly validate whether the LC win rate improvements correspond to genuine preference improvements, especially given known issues with GPT-4-as-judge.
- Testing on diverse tasks (reasoning, coding, math) would demonstrate generality or reveal limitations of the method.
- A control experiment comparing DPO training on the debiased dataset vs. a dataset with random length-matching would strengthen the case that the debiasing procedure preserves preference signal quality (though the downstream results already partially address this).

## Removed Points

These points were raised by reviewers but are removed or demoted after verification against the paper:

- *"The on-policy analysis is heuristic and not a formal proof"* — The paper does not claim a formal proof; it presents a conceptual analysis to motivate the method. This is a reasonable level of theoretical support for an empirical systems paper.
- *"The offline data for experience replay is a subset of the data used to train the base model"* — The paper explicitly acknowledges this design choice and frames the contribution as improvement without new human data. This is the intended setup, not a flaw.
- *"The paper does not evaluate whether the debiased dataset retains preference signal quality"* — The downstream experiment (LC win rate with α\*) directly evaluates this; α\* achieves the best performance, demonstrating the debiased data retains useful signal.
- *"The LLM-as-a-Judge baseline is not fairly configured" (as a major criticism)* — The paper transparently describes the baseline setup and notes the difference from Self-Rewarding LM. The baseline is labeled "LLM-as-a-Judge" not "Self-Rewarding LM." This is a limitation acknowledged by the authors, not a deception. Demoted to minor.

## Novel Insights

The reviewers' analyses converge on a key insight not fully articulated in the paper: DICE's success depends on a critical assumption — that the DPO implicit reward, despite being trained on (potentially stale) offline data, generalizes well enough to score on-policy samples from an improved policy. The paper does not directly validate this assumption (e.g., by correlating implicit reward scores with human judgments on held-out data). The length-regularization component partially addresses the known failure mode (length exploitation) of such reward-based self-bootstrapping, but the deeper question of reward quality drift across iterations remains unexamined. This insight suggests a natural extension: periodically recalibrating the implicit reward against human judgments or using ensemble-based reward aggregation across iterations.

## Suggestions

1. **Expand evaluation** to at least one additional benchmark (e.g., MT-Bench or Chatbot Arena) and ideally include a human evaluation on a sample of prompts. This is the single most impactful change.
2. **Report confidence intervals** for all main results and ablations, using at least 3 random seeds or bootstrapping.
3. **Add a diagnostic analysis** of why improvement saturates after 2–3 iterations — e.g., compute implicit reward variance, response diversity (distinct n-grams), or probe for policy collapse across iterations.
4. **Soften the Gemini Pro comparison** in the abstract and introduction, or at minimum add a caveat about differing training setups.
5. **Include a properly configured Self-Rewarding LM baseline** (with SFT on evaluation data) for a fairer comparison.
