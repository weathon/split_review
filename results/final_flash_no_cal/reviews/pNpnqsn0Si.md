Now let me compile the final review after thoroughly cross-checking every claim against the paper.

---

## Summary

This paper introduces **Thoughtbubbles**, a transformer variant that learns to dynamically fork (duplicate) and prune residual streams during standard language model pretraining, using only the language modeling loss. The forking is controlled by learned scoring functions: streams with high scores are duplicated to create "bubbles" of parallel latent computation, while low-scoring streams are deleted. The paper reports consistent perplexity and zero-shot evaluation improvements over a standard transformer baseline and a non-adaptive computation-matched baseline (Copy-N) at 150M–772M scales, along with analysis showing that forks are allocated to tokens with higher uncertainty and that parent tokens preferentially attend to their forked children.

---

## Strengths

- **First architecture for unsupervised dynamic parallel computation in latent space.** The paper correctly claims to be the first to enable learned, dynamic allocation of parallel residual streams during pretraining without chain-of-thought tokens or manual placement of pause tokens (Section 1). The forking mechanism (Section 2.3) and score-attenuated attention (Section 2.4) are well-specified.

- **Consistent empirical outperformance across scales and metrics.** Table 1 shows that Thoughtbubbles (κ=4L) achieves the best perplexity across all model sizes (150M–772M) and both datasets (OpenWebText and peS2o). It also leads on LAMBADA and HellaSwag in most settings. Notably, a 319M Thoughtbubbles model achieves lower perplexity on OpenWebText than the 772M baseline (Figure 3), demonstrating effective use of additional compute.

- **Interpretable allocation of computation without supervision.** The entropy-fork analysis (Figure 5) shows that the model allocates more forks to tokens with higher output entropy (measured both by the forking model and an independent baseline LM), and the attention analysis (Figure 4) confirms that forked children receive substantially higher attention from their parent token than unrelated tokens. These analyses directly validate that the forking mechanism is being used meaningfully.

- **Flexible inference-time budget control.** Section 5.1 demonstrates that dynamic forking (scaling the budget proportionally to input length) mitigates the distribution shift between blockwise forward passes and autoregressive generation, maintaining the performance gains over the baseline (Figure 6).

- **Compatible with standard pretraining pipelines.** The model trains with standard cross-entropy loss (Section 2.1, Section 3.1), requiring no changes to the training loop or additional supervision.

---

## Weaknesses

### Fatal

None.

### Major

- **Missing comparisons against pause-token baselines.** The introduction frames pause-token / thinking-token methods (Goyal et al., 2024; Herel & Mikolov, 2024; Sun et al., 2025) as the primary prior approach and criticizes them for requiring manual placement and lacking dynamic mid-network allocation. Yet the evaluation includes no comparison against any pause-token baseline. Implementing pause-token training is non-trivial, but given the paper's motivational framing, this is the single most directly relevant comparison. Without it, the reader cannot assess whether the improvements come from dynamic allocation specifically, or simply from having *some* form of parallel compute at the right layers (which pause tokens could also provide, albeit with manual placement).

- **Insufficient clarity on gradient flow through the discrete top‑k selection.** The forking decision uses a hard top‑k operation (Eq. 5–6) that determines which residual streams survive. The paper does **not** specify how gradients flow through this discrete selection. The score-attenuated attention (Eq. 8) and residual updates (Eq. 9–10) provide a differentiable pathway for the scores of *surviving* streams, but the paper never explains this, leaving readers uncertain about whether a straight-through estimator, soft top‑k, or some other relaxation is used. The Limitations section (Section 8) acknowledges a "Top‑K Gradient Bottleneck" and suggests "training time randomization and noise" as a mitigation, but does not state what was actually implemented. This is a significant methodological clarity gap. The empirical results show the mechanism *works*, but the paper should be transparent about the gradient pathway to enable reproduction and full evaluation.

### Minor

- **No error bars or multiple seeds reported.** All results in Table 1 are single floats. At the 150M–772M scale with only 2.5B tokens of pretraining, variance is non-negligible. The headline result ("319M beats 772M") would be substantially strengthened by confidence intervals or results from multiple seeds.

- **The Copy‑N baseline is an imperfect computation match.** The paper describes Copy‑N as "roughly FLOPs-matched," but copying the input residuals from layer 0 causes the early layers to process a much longer sequence (3L or 5L) than Thoughtbubbles, which starts with length L and forks only in later layers (3, 7, 11). This puts the baseline's extra compute in less context-aware layers, which likely disadvantages it. The fact that Copy‑N often underperforms even the standard baseline (Table 1) suggests adding non-adaptive compute in early layers can hurt—which *supports* the paper's thesis that adaptive allocation matters—but it weakens the claim of a fair computation-matched comparison.

- **Forking layer placement lacks thorough ablation in the main text.** The paper places forking before layers 3, 7, and 11 and refers to Appendix B for discussion. While the choice is motivated ("first forking layer after a few regular blocks to ensure broader context"), the main text would benefit from a sensitivity analysis (e.g., forking at different depths, or across all layers vs. selective layers).

- **The "Top‑K Gradient Bottleneck" mitigation is vaguely described.** The Limitations section mentions that randomization and noise can mitigate the bottleneck, but does not specify whether this was used in the presented experiments or is only a suggestion for future work. This matters because if no mitigation was used, the gradient issue is more acute.

### Trivial

None.

---

## Nice-to-Haves

- **A uniform‑forking ablation** (fork every token equally, without learned scores, at the same budget) would directly test whether the *dynamic* nature of the allocation drives the gains, versus simply having multiple parallel streams at the right layers.
- **Actual FLOPs counts or wall-clock times** for each method, beyond the "roughly FLOPs-matched" claim, would strengthen the computation-matched comparison.
- **Reporting the specific gradient handling mechanism** (e.g., whether straight-through estimation, score-attenuated attention gradients alone, or a soft relaxation was used) is essential for reproducibility and should be moved from "nice-to-have" to "required" in any revision.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The gradient-flow problem is structural/fatal" (Harsh Critic, Critical Issue 1).** The critic claims the training procedure is a "black box" whose results "may rely on a flawed or non‑functional gradient." This is overblown: a clear differentiable gradient pathway exists through the score-attenuated attention (Eq. 8: scores appear in log-space addition to attention logits and as multiplicative gates on V, both differentiable w.r.t. the scores) and residual update modulation (Eq. 9–10). The empirical results demonstrate that learning occurs. The lack of clarity is a *major* weakness, not a fatal structural flaw.*[Removed: severity inflation]*

2. **"Score-attenuated attention is a strong bias that may limit revision" (Harsh Critic, Section-by-Section).** This is a speculative concern about a potential limitation; no evidence is provided that the model actually struggles from this, and the results show the mechanism works as intended.*[Removed: speculative]*

3. **"Output averaging is computationally expensive" (Harsh Critic, Section-by-Section).** The paper already acknowledges efficiency limitations in Section 8 ("Time-matched evaluations"). This adds no new information.*[Removed: already addressed]*

4. **"Copy‑N is uninformative / straw man" (Harsh Critic, Critical Issue 2).** The critic claims the baseline is "not a valid computation-matched comparison." While the match is imperfect, Copy‑N serves as a non-adaptive parallel computation baseline. The fact that it *underperforms* the standard transformer on many metrics actually strengthens the paper's claim that adaptive allocation matters; calling it "uninformative" ignores the evidence it provides.*[Removed: characterization too strong / ignores evidence]*

5. **"Analysis is correlational, not causal" (Harsh Critic, Analysis section).** The paper does not claim that the entropy-fork analysis (Fig. 5) or attention analysis (Fig. 4) are causal experiments. They are presented as supplementary interpretability analyses, not as the primary evidence for the method's effectiveness.*[Removed: criticism misaligned with paper's own claims]*

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation about the method or results that the paper itself does not already contain.

---

## Suggestions

1. **Clarify the gradient flow in the main text.** Explicitly state how the top‑k forking selection is handled during backpropagation. If the score-attenuated attention and residual updates provide the sole gradient pathway (i.e., the top‑k is a non-differentiable selection and only surviving scores receive gradients through Eq. 8–10), say so. If any relaxation (e.g., straight-through, soft top‑k) is used, specify it. Also clarify whether the randomization/noise mitigation from Section 8 was used in the reported experiments.

2. **Add pause-token baselines or explicitly justify their absence.** If the computational cost of pretraining pause-token models is prohibitive, a smaller-scale comparison or a discussion of why Copy‑N subsumes the pause-token comparison would strengthen the paper.

3. **Report error bars or multi-seed results** for at least the key comparison (319M vs. 772M, Table 1).

4. **Provide FLOPs counts** for each method (Baseline, Copy‑3, Copy‑5, Ours κ=2L, Ours κ=4L) to make the computation-match explicit.

5. **Add a uniform‑forking ablation** where every token is forked equally at the same layers and budget, to isolate the benefit of learned dynamic allocation.

---

## Score and Decision

This paper presents a genuinely novel architecture for learned dynamic parallel computation, with clear empirical evidence that it outperforms standard transformers and a non-adaptive parallel baseline across multiple scales and datasets. The interpretability analysis (entropy-fork correlation, parent-child attention) convincingly shows the mechanism is active and well-behaved. The main weaknesses—missing pause-token baselines, insufficient clarity on gradient flow, and lack of error bars—are addressable and do not undermine the core contribution.

**Score: 6.5**

**Decision: Accept**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>