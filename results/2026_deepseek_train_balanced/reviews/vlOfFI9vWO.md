Now I'll produce the final consolidated review.

## Summary

This paper proposes RL4DViT, which applies Multi-Agent PPO (MAPPO) to dynamic token selection in Vision Transformers. Each token is mapped to an independent RL agent that decides whether to keep or discard it, with reward shaping trading off computational cost against classification accuracy. Experiments on ImageNet report a 39% reduction in GFLOPs with a 0.17% accuracy drop after fine-tuning.

## Strengths

- **First application of RL to dynamic token selection in ViT:** Prior work (DynamicViT, A-ViT, AdaViT) relied on Gumbel-Softmax or halting mechanisms. The paper explicitly identifies this gap (lines 10, 28) and formulates the problem as a Markov Game with MAPPO — a genuinely different approach from the differentiable relaxation strategies that dominate the literature.

- **Parameter efficiency and training speed relative to prior architectures:** The decision network is a single MLP (0.1M parameters), which the paper states is 9× smaller than DynamicViT's decision layers (line 123). Training the RL agents requires only one epoch with the ViT backbone frozen, plus one epoch of fine-tuning — substantially lighter than training selection modules jointly with the backbone from scratch.

- **Qualitatively different token selection policy discovered by RL:** Visualizations (Figure 2, lines 212–213) show that RL4DViT discards the majority of tokens in the first decision block, while prior methods (DynamicViT, A-ViT) discard tokens step-by-step across blocks. This aggressive early-pruning strategy is a genuinely distinct behavior that emerges from the RL formulation, suggesting the policy captures a different notion of token redundancy.

- **Two-phase training effectively mitigates distribution shift:** The paper separates RL training (ViT frozen) from ViT fine-tuning (agents frozen) and reports that fine-tuning recovers accuracy from −0.5% to −0.17% (Table 2, lines 130–131, 203). This explicitly addresses the distribution shift problem that arises when pruning tokens in a pre-trained ViT.

## Weaknesses

### Fatal
None.

### Major

- **The "multi-agent" framing is not validated against simpler alternatives.** Each of the 197 agents observes only its own 768-dim token embedding, uses the same shared policy network, and makes independent decisions without any communication or coordination mechanism (Section 3.1, line 37: "one agent can only observe one single token"). This setup is functionally equivalent to applying a per-token binary classifier trained with PPO. The paper does not include any ablation comparing the MAPPO formulation to (a) single-agent PPO scoring tokens independently, (b) a supervised binary classifier trained on kept/discarded labels, or (c) a simple attention-weight-based heuristic. Since the paper's claimed contribution hinges on the MARL framing being meaningful, the absence of this validation is a significant evidential gap.

- **1 epoch of RL training is insufficient to demonstrate meaningful policy learning, and no convergence evidence is provided.** The RL agents are trained for a single epoch over ImageNet (line 121: "We train the MARL agents with ViT weights fixed for one epoch"). For a 197-agent system with a 768-dim observation space, this is far below typical RL convergence requirements. The paper presents no learning curves, reward convergence plots, policy entropy trends, or token-keep-rate trajectories over training steps. It does not ablate whether training for additional epochs changes the results. Without this evidence, it is unclear whether the policy has learned anything beyond a near-constant discard heuristic that happens to work adequately at 1 epoch.

- **Comparisons against prior methods are not substantiated with readable numerical results.** The paper claims to compare with DynamicViT and A-ViT in Table 1 and asserts state-of-the-art status (line 33), but the actual comparison numbers are embedded in an image and are not presented as readable text. The only detailed quantitative baseline discussed in the text is against random token selection (Section 4.5). The paper also does not provide matched-budget comparisons (same GFLOPs, same training protocol) that would allow readers to isolate whether any accuracy advantage stems from the RL formulation itself or from differences in training duration, backbone initialization, or architectural choices.

### Minor

- **Key reward function parameters are not reported.** The reward function uses variables `R` (line 91: "a variable designed to encourage the agents to discard tokens that contain redundant or noisy information"), α, and β (line 96–99). None of these values are given numerically. Figure 3 qualitatively shows the effect of varying α/β, but the actual experimental values are missing. This hinders reproducibility.

- **Standard RL hyperparameters are underspecified.** The discount factor γ (appears in the objective at line 46), GAE parameter λ (used in advantage estimation at line 73), entropy coefficient c (line 70), and other PPO hyperparameters are mentioned in formulas but their numeric values are not reported in the main text. The paper states "More implement details can be found in the supplementary material" (line 121), but the supplementary is not present in the extracted text.

- **No statistical significance or multi-seed results.** All reported results appear to come from a single training run. RL methods are inherently noisy, and without error bars or multiple seeds, it is impossible to assess the stability and reliability of the reported accuracy/GFLOPs trade-offs.

- **CLS token handling is ambiguous.** The paper states that there are 197 tokens (196 patches + [CLS], line 63) and that an agent is created for each token. However, it never clarifies whether there is an agent for the [CLS] token, whether it is always kept, or how its inclusion/exclusion affects the classification head's input.

- **Credit assignment in the reward structure is not discussed.** The reward for correct classification (reward2) is shared equally among all surviving agents at the end of the forward pass. The paper does not discuss how agents that kept informative tokens are credited differently from agents that kept noisy tokens when all share the same classification outcome — a known challenge in MARL with joint rewards.

- **Missing controlled ablations.** The paper does not ablate the number of decision blocks L (fixed at 3 following prior work), the effect of using a single MLP vs. a deeper policy network, or the sensitivity of results to the initial random seed.

### Trivial
- The paper does not clarify whether the [CLS] token has an associated agent or is always retained (noted above; this is small enough to fix in one sentence).

## Nice-to-Haves
- Wall-clock inference speed (images/second) would be more informative than GFLOPs alone, since the masking operations and agent forward pass add overhead.
- Comparison with a deterministic heuristic baseline (e.g., keeping tokens with the highest class-attention weights) would strengthen the case that RL is learning something nontrivial.
- A discussion of why 1 epoch of RL might be sufficient (e.g., the observation space is low-dimensional relative to the data, or the reward signal is dense enough for rapid convergence) would address a reader's natural skepticism.

## Removed Points
*These points were flagged for removal from the harsh critic's review. They are presented for completeness but should be treated with caution.*

- **Criticism that the paper "overstates limitations of Gumbel-Softmax approaches" without specific evidence:** This is a rhetorical claim about the paper's framing, not a verifiable weakness. The paper references known challenges (regularization difficulties, stochasticity in training, premature convergence) in the context of motivating an alternative approach — this is standard positioning in a new-method paper.
- **Criticism that the observed aggressive early-discard policy "could equally indicate that the policy is collapsing to a simple early-exit heuristic":** This is a speculation about the policy's nature. The paper presents this behavior as a discovery; the critic offers a plausible alternative interpretation, but there is no evidence in the paper to adjudicate between them. Absent analysis (e.g., per-image retention rate variance, or correlation with attention scores), this is a potential future investigation direction, not a confirmed weakness.
- **Claim that the paper provides "no comparison with prior work" because only random baseline is shown in text:** The paper claims to include DynamicViT and A-ViT comparisons in Table 1 (line 194). The table is an image and the numbers are not readable in the text extract, but the paper asserts the comparison exists. The verifiable weakness is that the comparison is not substantiated with readable numbers, not that it is absent.
- **Criticism about the state definition being "problematic" because each agent observes only its own token:** This is a design choice rather than a flaw. The observation space includes tokens processed by prior attention layers, which carry relational information. The paper could discuss limitations, but the critic's framing as a "problematic" design is too strong.
- **Criticism about the "speed alone is not a virtue" framing:** The paper's claim of fast training is presented as a practical advantage alongside the parameter efficiency argument. This is not a weakness — it is a claimed strength whose validity would be bolstered by learning curves. The core issue (missing convergence evidence) is already captured above.
- **"No comparison with Gumbel-Softmax approaches at matched GFLOPs budgets":** The paper claims to include DynamicViT (which uses Gumbel-Softmax) in Table 1. The criticism is partially contradicted by the paper's claims, though the unreadable table makes verification impossible.
- **Strengths from the Strength Finder that were dropped:** "Reward engineering with competitive-cooperative design" — This is a description of the design choice, not an empirically validated strength. No analysis demonstrates that the competitive-cooperative framing produces different results from a shared-reward baseline.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Provide learning curves and convergence evidence.** Show reward, token-keep rate, and accuracy over training steps for at least 3–5 epochs of RL training to demonstrate that the policy actually improves beyond the first epoch.
2. **Ablate the MARL framing directly.** Compare MAPPO (per-token reward, individual agents) against a single-agent PPO that scores each token using the same policy network but with a shared reward. If the results are identical, the MARL framing adds complexity without benefit.
3. **Report Table 1 numbers in readable text form.** The comparison with DynamicViT and A-ViT is the central experimental claim and must be verifiable directly from the text, not only from an unreadable image.
4. **Report all missing hyperparameters:** α, β, R, γ, λ, entropy coefficient c, learning rates, and number of training steps. The supplementary material does not count if it is not included.
5. **Run experiments with multiple random seeds and report mean ± std.** This is standard practice for RL work.
6. **Clarify the CLS token's role** in the token selection process.

## Score and Decision

This paper identifies a genuine gap — RL has not been seriously explored for dynamic token selection in ViT — and presents a reasonable first formulation. The discovered aggressive early-pruning policy and the two-phase training scheme for mitigating distribution shift are interesting contributions. However, the experimental validation falls substantially short of the standard expected at a top-tier venue. The three major issues — unvalidated MARL framing, one epoch of RL training without convergence evidence, and unsubstantiated comparisons with prior methods — collectively mean that the paper's core claims are not convincingly supported by the evidence presented. Strong revision and additional experiments could make a credible case.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>