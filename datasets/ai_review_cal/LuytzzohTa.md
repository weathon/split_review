- Decision: Reject
- Avg Score: 5.60
- Scores: 5, 5, 5, 5, 8
Now I have thoroughly verified the paper content against all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper proposes **Agent Q**, a pipeline that combines Monte-Carlo Tree Search (MCTS) with step-level Direct Preference Optimization (DPO) and AI self-critique for process supervision, to improve web agent performance. The method uses MCTS to explore trajectories, derives step-level preference pairs from the search tree (using both empirical Q-values from rollouts and AI feedback rankings), and fine-tunes the policy via node-level DPO. Experiments are conducted on WebShop (simulated e-commerce, 1,087 held-out tasks) and a live OpenTable booking website. Results show LLaMA-3-70B zero-shot success rate improving from 18.6% → 81.7% on OpenTable (surpassing GPT-4's 62.6%), and 95.4% with MCTS at test time.

## Strengths

- **Large improvement on a real, live website**: On OpenTable, the LLaMA-3-70B zero-shot rate jumps from 18.6% to 81.7% after a single round of fine-tuning with MCTS-collected data, surpassing GPT-4's zero-shot 62.6% (Section 6.2, Figure 6). The 95.4% success rate with search at test time is especially striking. Demonstrating this on a live, dynamic booking site (average 13.9 steps per task) rather than a simulated environment is a strong point.

- **Clean ablation isolating AI process supervision**: The paper compares Agent Q (with AI feedback, 81.7%) against MCTS+DPO with outcome rewards only (75.2%), isolating a 6.5% gain from the AI self-critique mechanism (Section 6.2). This directly supports the claim that step-level AI feedback helps credit assignment in long-horizon tasks.

- **Theoretical connection**: Theorem 1 shows that optimizing the step-level DPO objective with preferences proportional to sigmoid(Q-differences) recovers the optimal RL policy, grounding the algorithm in a principled RL framework rather than pure heuristics (Section 5, Theorem 1).

- **Dual evaluation in simulated and real environments**: The method is validated on WebShop (simulated, with 1,087 held-out test tasks, achieving 50.5% beating average human 50.0% with search) and on a live website, demonstrating generalization beyond scripted benchmarks.

## Weaknesses

### Fatal
None.

### Major
- **OpenTable evaluation lacks basic statistical reporting.** The paper reports no test set size for OpenTable (only "programmatically generate a diverse set of user queries"), no confidence intervals or variance estimates for any result, and no accuracy/calibration numbers for the GPT-4-V evaluator against human labels (only "as measured by human validation" without a number, Section 6.1). This makes it impossible to assess whether the reported gaps (e.g., 71.8% ↔ 81.7% or 81.7% ↔ 95.4%) are statistically significant, especially given the stochasticity of both the model and the live website. For the headline claims of the paper, this is a significant evidential gap that must be filled.

### Minor
- **AI self-critique mechanism is under-analyzed.** The ablation (75.2% vs 81.7%) shows the mechanism helps, but the paper does not analyze the quality of the action rankings (e.g., correlation between AI ranking and eventual outcome), nor does it report sensitivity to the mixing coefficient α (Eq. 9). Without this analysis, it is unclear whether the improvement comes from better credit assignment or simply from generating more preference pairs from the same trajectories. This does not threaten the core claim but limits understanding of *why* the method works.

- **Key hyperparameter values are not reported.** The numerical values of α, θ_threshold, c_exp, K (number of sampled actions), B (batch size), T (tree depth) are specified as algorithm inputs (Algorithm 1, line 188) but their actual settings are not given anywhere in the paper. For a method with several tunable knobs, this omission hinders reproduction.

- **The GPT-4 comparison could be more precisely framed.** The paper states "outperforming GPT-4" (abstract, intro) comparing Agent Q (fine-tuned LLaMA-3-70B, zero-shot) against GPT-4 (zero-shot). While this is a valid comparison demonstrating the value of domain-specific training, the phrasing could mislead a casual reader into thinking the model is architecturally superior. Framing it as "our training pipeline enables a much weaker base model to surpass GPT-4 on this task" would be more precise.

### Trivial
None.

## Nice-to-Haves
- An analysis of failure modes of the trained Agent Q model (e.g., categories of tasks where it still fails) would add depth.
- A controlled comparison between step-level DPO and trajectory-level DPO on the same MCTS-collected data (not just different data sources) on WebShop would clarify whether the benefit is from the step-level formulation or the richer preference set.

## Removed Points

- **"Comparison against GPT-4 is misleading/unfair"** (Harsh Critic Point 1, in strong form): The comparison is between a fine-tuned model and GPT-4 zero-shot. This is a standard and informative comparison in ML — it shows what domain-specific training can achieve from a weaker base. The paper does not claim architectural superiority. The criticism's demand for a "GPT-4 fine-tuned baseline" is scope creep. Weakened to a minor framing point in the main review.

- **"Contributions are incremental relative to concurrent work"** (Harsh Critic Point 3): The paper explicitly acknowledges concurrent works (Section 2.1, line 45: "A number of concurrent works…"; line 210: "Our approach is most similar to…") and clearly states its novel contribution as scaling these methods to a *realistic agent setting* on a *live website* — a genuine extension beyond prior math/code domains. The critic's assertion that the paper "often presents the method as if it were the first" is not supported by the text.

- **"The proof is not given"** (from Section-by-Section notes): The paper states "The proof follows directly from the proof of Theorem 6.1 in [setlur2024rlincorrectsyntheticdata]" — this is standard practice for conference papers referencing known results.

- **"WebShop improvement from training is small"** / "Main gain comes from search": The paper openly acknowledges this (Section 5.3: "the improvement is modest on WebShop") and correctly motivates the long-horizon OpenTable experiments as the setting where training matters more. This is honest framing, not a weakness.

- **Several generic or speculative concerns** from the Harsh Critic (e.g., "could the AI feedback amplify biases?", "does the benefit come from more preference pairs rather than better credit assignment?") are not specific errors but open research questions. The paper's ablation (75.2% vs 81.7%) already partially addresses this; deeper analysis is noted under Minor weaknesses.

## Novel Insights

The reviews surface an important tension that the paper itself partially acknowledges: on the short-horizon WebShop task, the main gain comes from search, not training, while on the long-horizon OpenTable task, training with AI process supervision contributes meaningfully. This suggests that the value of step-level DPO with search-collected preferences scales with task horizon — a finding that future work could formalize. The reviews do not identify any unclaimed insight beyond what the paper already provides.

## Suggestions

1. **Report the OpenTable test set size, accuracy of the GPT-4-V evaluator against human labels, and confidence intervals** for all reported success rates. This is the single most impactful improvement the paper could make.

2. **Report the numerical values of all key hyperparameters** (α, θ_threshold, c_exp, K, B, T) and the total number of MCTS rollouts/trajectories collected in "a single day of data collection."

3. **Add an analysis of AI feedback quality**: compute agreement between the critic's action rankings and final outcome, and show performance as a function of α to demonstrate robustness.

4. **Rephrase the GPT-4 comparison** in the abstract/intro to emphasize that training enables a weaker base model to outperform a frontier model zero-shot on this specific task, rather than the model generically "outperforming GPT-4."
