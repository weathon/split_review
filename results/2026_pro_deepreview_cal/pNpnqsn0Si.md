Now I have enough calibration data to form a judgment. Let me synthesize everything into the final review.

---

## Summary

This paper introduces **Thoughtbubbles**, a transformer architecture variant that learns to dynamically fork (duplicate) or delete residual streams in latent space during pretraining. A forking decision function produces keep/fork scores for each token; a top-k selection determines which residuals survive; score-attenuated attention and residual updates train the scores through the standard LM loss. The method achieves consistent perplexity improvements over parameter-matched and computation-matched baselines across 150M–772M scales on two datasets, with the forking behavior emerging to concentrate on high-uncertainty tokens.

## Strengths

- **Novel architecture for unsupervised adaptive parallel computation**: Thoughtbubbles is the first architecture that learns to allocate latent parallel computation during pretraining using only the LM loss, without auxiliary signals. This is a genuine conceptual advance over prior work that requires explicit pause-token insertion or post-hoc computation allocation.

- **Consistent and scaling performance improvements**: Table 1 and Figure 3 show that Thoughtbubbles outperforms both the parameter-matched standard transformer and the computation-matched copy-k baseline on validation perplexity, LAMBADA, and HellaSwag across three model scales (150M, 319M, 772M) and two datasets (OpenWebText, peS2o). A 319M Thoughtbubbles model surpasses the 772M baseline on OpenWebText perplexity, suggesting favorable scaling.

- **Interpretable emergent computation allocation**: Figure 5 demonstrates that the number of forks concentrates around tokens with higher output entropy — measured both by the forking model and an independently trained baseline — showing the model learns to allocate extra computation to regions of higher uncertainty without explicit supervision. Figure 4 further confirms that forked children meaningfully influence the parent token's computation through attention.

- **Robust autoregressive generation**: Section 5.1 and Figure 6 show that dynamic forking (budget proportional to sequence length) resolves the distribution shift between blockwise and autoregressive evaluation, preserving the gains in a practical generation setting.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **No ablation isolating adaptivity from extra compute**: The copy-k baseline duplicates all input tokens uniformly, providing a computation-matched but non-adaptive comparison. However, a control where the same total fork budget is allocated uniformly across tokens (rather than via learned scoring) would isolate whether the learned adaptive allocation itself — as opposed to simply having extra residual streams — drives the gains. The copy-k baseline partially addresses this but conflates "extra compute" with "extra streams per token." This limits confidence that adaptivity specifically is beneficial.

- **No comparison against pause-token baselines**: The paper positions itself against pause-token methods (Goyal et al., 2024; Herel & Mikolov, 2024) and claims advantages (no need to insert tokens explicitly, mid-network allocation). A head-to-head comparison against at least one such method, FLOPs-matched, would substantially strengthen the claim that Thoughtbubbles offers a meaningful advantage over existing adaptive-computation approaches, rather than only over naive duplication.

- **FLOPs analysis is imprecise**: The characterization of κ=4L as "roughly FLOPs-matched" against copy-5 is vague. A proper FLOPs accounting for each method, and ideally a perplexity-vs-FLOPs plot, would make the efficiency claims more credible and help readers assess the practical trade-off.

- **Gradient flow through top-k could be more explicit**: The paper describes the forking mechanism and score attenuation in detail (Sections 2.3–2.4), and the gradient path through surviving tokens is present via the attenuation multipliers. However, the paper never explicitly states which gradient estimator is used for the discrete top-k selection (e.g., implicit straight-through where only selected tokens receive gradients). The limitation is acknowledged in Section 8 ("Top-K Gradient Bottleneck"), but the main method section would benefit from one sentence clarifying the gradient flow.

### Trivial

- Mixed results on BLiMP and PIQA (Table 1) are acknowledged in the text but could be discussed more frankly in the abstract, which claims broad improvement.
- No wall-clock runtime measurements (acknowledged as a limitation in Section 8).

## Nice-to-Haves

- A sensitivity analysis of forking layer placement (currently deferred to appendix B) would help practitioners apply the method.
- Evaluation on a reasoning benchmark at a feasible scale would broaden the evidence, though the authors plausibly cite hardware constraints.

## Removed Points

These points are flagged as removed; treat them with caution.

- **"Core training mechanism is not explained / untrainable" (Harsh Critic)**: The paper describes the forking function, top-k selection, and score-attenuated updates in Sections 2.3–2.4. Gradients flow from the LM loss through the attenuation multipliers (Eq. 8–10) back to the cumulative scores and the forking decision function, for all selected tokens. Non-selected tokens naturally receive no gradient. The gradient bottleneck for early-layer tokens dropped by later top-k is explicitly acknowledged in Section 8. The mechanism is adequately described; the harsh critic's claim that it is fundamentally untrainable is incorrect.

- **"Parameters of forking decision function cannot be trained" (Harsh Critic)**: Factually wrong. The forking function's parameters receive gradients through the surviving tokens' scores via the attenuation mechanism in Eqs. 8–10. The discrete top-k means non-surviving tokens contribute no gradient, which is a standard pattern, not a fatal gap.

- **"COPY-k is extremely weak as a representative of non-adaptive parallel computation" (Harsh Critic)**: The copy-k baseline allocates the same total residual streams uniformly across all tokens — it is a fair computation-matched non-adaptive baseline. Whether stronger baselines exist is a matter of completeness, not a fatal weakness. The point about missing pause-token comparisons is retained as a minor weakness.

- **"Claims outperforms non-adaptive parallel computation approaches" is not adequately supported (Harsh Critic)**: The paper's only non-adaptive baseline is copy-k, which the paper explicitly compares against. The paper never claims comparison against all possible non-adaptive approaches. This is a scope issue, not an unsupported claim.

- **"Missing appendix details make the paper incomplete" (Harsh Critic)**: The appendix is stripped by the parser, not missing from the submission. Removed per hard rules.

- **"The training budget scaling description is ambiguous (Section 2.6)" (Harsh Critic)**: The paper clearly describes both fixed and dynamic forking modes in Section 2.6, with further details in Appendix E.1 (stripped). The main text is sufficient.

## Novel Insights

The reviewers' analyses converge on an interesting observation: Thoughtbubbles demonstrates that a transformer can learn meaningful, interpretable compute-allocation policies (forking at high-entropy tokens) purely from the LM loss, without any auxiliary objectives, reinforcement learning, or architectural regularization toward interpretability. This is a stronger result than simply showing perplexity gains — it suggests that the LM objective itself provides a sufficient training signal for meta-reasoning about where computation is needed, at least in the latent space.

## Suggestions

- Add a uniform-fork ablation: use the same total fork budget but allocate forks uniformly across all tokens (no learned scoring), to isolate whether the adaptive scoring mechanism specifically drives the gains.
- Compare against at least one pause-token baseline (e.g., Goyal et al., 2024) with FLOPs matching, or explicitly scope the contribution as not requiring such a comparison and explain why copy-k suffices.
- Report total FLOPs for each method in Table 1 and add a perplexity-vs-FLOPs figure.
- Add one sentence in Section 2.3 explicitly describing gradient flow through the top-k (e.g., "gradients flow to f_θ only through the scores of surviving tokens via the attenuation in Eq. 8–10").

## Score and Decision

**Round 1 bracket**: Based on calibration anchors, the paper sits between CoTFormer (5.75) and Adaptive Transformer Programs (7.00), with APE (6.20) and "Learning How Hard to Think" (6.50) nearby.

**Round 2 narrowing**: Compared to CoTFormer (5.75, similar architecture-novelty paper, weaker empirical evidence), Thoughtbubbles has cleaner and more consistent results. Compared to "Learning How Hard to Think" (6.50, different but related adaptive-computation paper), Thoughtbubbles has greater architectural novelty but slightly less thorough baselines. Compared to MatFormer (6.00, elastic inference architecture), Thoughtbubbles has a more novel core mechanism.

**Final score**: 6.5. The paper makes a genuine architectural contribution with consistent empirical support and compelling interpretability analysis. The missing pause-token comparison and uniform-fork ablation are real gaps that prevent a higher score, but neither is fatal and both are addressable. The paper is above the bar for acceptance.

**Calibration anchors referenced**:
| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| 7igPXQFupX (CoTFormer) | 5.75 | R1, R2 | Similar architecture-novelty paper; Thoughtbubbles has stronger empirical evidence |
| yUC8pU508S (APE) | 6.20 | R1 | Training-free encoding modification; Thoughtbubbles has greater architectural novelty |
| W8K8slZ73R (Adaptive Transformer Programs) | 7.00 | R1 | Better ablations and more thorough experiments; Thoughtbubbles less comprehensive |
| iOy2pITOoH (Spark Transformer) | 5.50 | R2 | Top-k sparsity architecture; Thoughtbubbles more novel, better evaluations |
| 89XNDtqhpL (MatFormer) | 6.00 | R2 | Elastic inference architecture; Thoughtbubbles has more novel mechanism |
| 6qUUgw9bAZ (Learning How Hard to Think) | 6.50 | R2 | Adaptive compute at test-time; Thoughtbubbles has greater architectural novelty, similar empirical thoroughness |
| T26f9z2rEe (Dynamic MoE) | 7.00 | R2 | More thorough evaluations and ablations |
| oQ4igHyh3N (TokenFormer) | 7.50 | R2 | Significantly more comprehensive evaluations |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>