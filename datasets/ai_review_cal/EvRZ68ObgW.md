- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 6, 3
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes controlling reward over-optimization in RL fine-tuning of LLMs by replacing direct reward maximization with an L2 regression objective that matches the reward distribution of generated sentences to a target distribution derived from human demonstrations. Instead of maximizing R(x,ŷ), the method maximizes -||R(x,ŷ)-R(x,y)||₂² where R(x,y) is the reward of a human reference. The approach is evaluated across three use cases: calibrating sequence-level log-likelihood, mitigating over-specialization on a sentiment classifier, and multi-reward summarization with length constraints.

## Strengths

1. **Simple, well-motivated approach that eliminates β tuning**: The core idea — penalizing squared deviation from a human-derived reward rather than maximizing reward — is intuitive and practically motivated. In Use Case 2 (IMDB sentiment), R_target achieves an alignment score of A=0.04 matching the best-tuned R_reg (β=0.3) without requiring any cross-validation over β, which is computationally expensive for large models. This is the paper's strongest empirical result (Figure 2, Table 2, Section 5.2).

2. **Demonstrated generality across three diverse use cases**: The method is validated on three qualitatively different RL fine-tuning challenges — self-RM for log-likelihood calibration (Section 5.1), a classifier reward prone to hacking (Section 5.2), and multi-reward RLHF summarization (Section 5.3) — each using a distinct reward model and evaluation protocol. This diversity supports the claim that the approach is broadly applicable rather than tailored to a single setting.

3. **Simplifies multi-reward optimization**: In Use Case 3, specifying two separate R_target terms (one for preference, one for length) naturally balances competing objectives without the trial-and-error weight tuning that standard multi-reward RL requires (Section 5.3). The resulting model achieves the best alignment (A=0.11 vs. 0.45 for direct maximization) and ~90% win rate against human summaries, demonstrating a genuine practical advantage.

4. **Preserves task success while avoiding reward hacking**: Across all experiments, R_target maintains task success rates comparable to the best baselines (e.g., 0.92 in IMDB, Table 2) while achieving far higher naturalness and diversity than direct reward maximization (e.g., S-Diversity 0.35 vs. 0.09 for R in Table 2), confirming the method avoids the degenerate solutions that naive maximization produces.

## Weaknesses

### Major

- **No human evaluation for the central claim about human alignment**: The paper uses chat-LlaMa2-13B to evaluate task success and naturalness (Section 4.4), but reports no human evaluation and no analysis of agreement between the AI judge and human judgments. Given that the paper's motivation is alignment with human preferences, and the headline claims concern producing "more human-aligned" generations, the absence of any human validation is a significant gap. The alignment metric (A, KL between reward distributions) is computed on the same reward model used for training, so it primarily confirms that the training objective was met rather than providing independent evidence of human preference. This limits the strength of the conclusions that can be drawn from the evaluation.

### Minor

- **The "parameter-free" claim is overstated**: The paper repeatedly describes the method as "parameter-free" (Abstract, Section 1, Section 3, Section 7) because it eliminates the KL coefficient β. However, the method introduces design choices about the target distribution — which data to use, how to filter it, how to construct prompts — that are not ablated or discussed for sensitivity. In Use Case 1, the target comes from Wikipedia; in Use Case 2, from IMDB reviews; in Use Case 3, from filtered TL;DR summaries. These are non-trivial decisions that could affect outcomes just as much as β does. The method is hyperparameter-free in the narrow sense of not needing β search, but the paper's framing suggests a stronger form of a priori control than is actually demonstrated.

- **The method assumes upward deviations from the human reward are always harmful**: By penalizing any deviation from R(x,y), R_target prevents the model from discovering generations that the RM scores higher than the human reference. While this is reasonable when RMs are imperfect proxies prone to over-optimization, the paper does not discuss cases where the RM might be reasonably well-aligned and some upward deviation could be legitimate. This assumption is plausible but unargued (Section 3.2).

- **No statistical significance or variance reported**: The paper does not report whether experiments were run with multiple random seeds or provide any confidence intervals for the reported metrics. Given the stochasticity of RL fine-tuning (policy initialization, sampling, PPO), single-run results leave uncertainty about the robustness of the reported alignment, success, and naturalness scores.

- **Multi-reward baseline tuning description is vague**: In Use Case 3 (Section 5.3), the authors state they "performed such tuning and came up with a model that produces generations with quite similar lengths as the target distribution." The description does not specify the tuning procedure (e.g., grid size, search range, selection criterion), making it difficult to assess whether the comparison is fully equitable. The authors could clarify whether the baseline weights were selected via systematic grid search or iteratively adjusted toward the reported configuration.

- **Target distribution in Use Case 2 may be an easy setup**: The prompts are the first 10 tokens of IMDB positive reviews, and the target reward comes from the human-written continuations in the same dataset. A harder test would use a separate corpus for the target distribution (e.g., general-domain text) to test robustness to distribution mismatch.

### Trivial

- None that pass the filtering criteria; minor presentation issues are parser artifacts.

## Nice-to-Haves

- A human evaluation on a subset of outputs (e.g., from Use Cases 2 and 3) to validate whether the improvements in AI-feedback metrics correspond to actual human preference. This is the single highest-leverage addition.
- Ablation of the target distribution itself (e.g., using a Dirac at the mean human reward vs. the full empirical distribution) to clarify whether the distributional shape or simply avoiding the maximum drives the improvement.
- A clearer description of the multi-reward baseline tuning procedure, including the grid range and selection criterion.

## Removed Points

These points were surfaced by reviewers but removed after verification against the paper:

- **"Unfair baseline in multi-reward experiment"** (criticized as tuned using knowledge of target distribution): The paper describes tuning a standard R+R_reg baseline and finding a configuration that produces good results. This is standard practice — reporting a strong baseline after tuning it — not an unfair comparison. The R_target advantage is that it achieves similar outcomes without this tuning, which is the stated contribution. The description could be more precise, but the criticism that this is "unfair" is not supported by the text.

- **"Win rate figure caption missing / baseline unclear"**: The text (line 180) clearly describes what Figure 5 compares: R_target^{pref+length} against human summaries, R^{pref}, and R_target^{pref}. The missing caption is a parser artifact.

- **"Temperature/nucleus sampling undercut the claimed advantage"**: The paper explicitly acknowledges these decoding heuristics work and explains why R_target remains valuable — it is model-independent and requires no search over sampling hyperparameters (line 150-151). This is already addressed.

- **Criticism that the method uses a frozen LM as RM in Use Case 1**: The paper clearly states this is a "proof of concept" (Section 4.1), and the experimental design is appropriate for testing the mechanism in isolation.

- **Criticism that the method is evaluated on a single seed**: This is subsumed under the more general "no statistical significance" point above. The specific claim about a single seed is speculative — the paper doesn't state the number of seeds.

## Novel Insights

The most interesting observation from the reviewer synthesis is a limitation not discussed in the paper: by penalizing any deviation from the human reward, R_target imposes a ceiling on the policy that prevents it from discovering generations the RM scores higher than the human reference. This creates an implicit trust assumption about the RM that may not hold symmetrically — the method trusts the RM enough to define the target distribution, but doesn't trust it enough to allow higher scores. This asymmetry is worth discussing in future work.

## Suggestions

1. **Add a human evaluation** on a subset of generations (e.g., 200 examples from Use Cases 2 and 3) or at minimum report correlation between the AI judge (chat-LlaMa2-13B) and human judgments. This is the single change that would most strengthen the paper.

2. **Softening of the "parameter-free" claim**: Replace "parameter-free" with more precise language such as "eliminates the need for KL coefficient tuning" or "reduces hyperparameter search to optimization-only choices," and add a brief discussion of how target distribution design choices affect outcomes.

3. **Clarify the multi-reward baseline tuning**: Specify the range and granularity of the grid search over α_pref and α_L, and state whether the selection was based on alignment, task success, or another criterion.

4. **Add variance or runs with multiple seeds**, at least for the main experiment (Use Case 2), to establish robustness.

5. **Discuss the upward-deviation limitation**: Acknowledge that R_target prevents discovery of genuinely better generations (by the RM's own scoring) and discuss scenarios where this might be undesirable.
