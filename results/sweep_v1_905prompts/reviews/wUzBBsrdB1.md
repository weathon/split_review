Now I have a comprehensive understanding of the paper and the calibration landscape. Let me write the final consolidated review.

My round-1 bracket placed this paper between approximately 5.5 and 7.5 — clearly above the 4.5–5.0 range of weaker SAE analysis papers, but below the 8.0+ level of the Scaling SAEs paper. Round 2 narrowed this: comparing against "Sparse Autoencoders Do Not Find Canonical Units of Analysis" (7.0), "A is for Absorption" (7.5 but rejected), "Towards Principled Evaluations" (7.0), and "Compute Optimal Inference" (4.67), this paper sits solidly in the 6.0–7.0 range. It's cleaner than the 4.67 paper, slightly less ambitious than the Canonical Units paper, and more actionable than the Absorption paper. Score: 6.5.

---

## Summary

This paper studies how the L₀ sparsity hyperparameter in Sparse Autoencoders (SAEs) affects the quality of learned features. Through controlled toy model experiments, the authors demonstrate that setting L₀ too low forces the SAE to mix correlated features together (feature hedging), while setting it too high also produces degenerate solutions. A key result is that at low L₀, a trained SAE with demonstrably incorrect latents achieves *better* reconstruction than the ground-truth SAE with correct latents (MSE 2.73 vs 4.88), proving that sparsity-reconstruction tradeoff plots are an unsound evaluation metric. The paper proposes a practical diagnostic metric — decoder pairwise cosine similarity (c_dec) — that practitioners can use to select an appropriate L₀, and validates it on Gemma-2-2b and Llama-3.2-1b SAEs, showing that the c_dec "elbow" coincides with peak sparse probing performance.

---

## Strengths

1. **Controlled toy-model demonstration that low L₀ forces feature mixing (Section 3.1, Figures 2–3).** The paper uses a principled setup with orthogonal ground-truth features and a controllable correlation structure, and shows that when the SAE's L₀ is below the true generative L₀, decoder latents systematically merge correlated (and anti-correlated) features. This provides a clean causal link between incorrect L₀ and corrupted SAE features.

2. **Direct MSE comparison proves gradient pressure to mix (Section 3.3).** The measurement that a trained low-L₀ SAE achieves MSE 2.73 while the ground-truth SAE achieves a *worse* MSE of 4.88 on the same data is the concrete evidence that the reconstruction loss itself incentivizes incorrect, mixed latents. This is the single most convincing piece of evidence in the paper.

3. **Sparsity-reconstruction tradeoff shown to be an unsound evaluation metric (Section 3.4, Figure 4–5).** The paper demonstrates that at every L₀ below the true L₀, the trained SAE with mixed features outperforms the ground-truth SAE in variance explained, while the resulting latents are highly polysemantic. This directly contradicts the implicit assumption that better reconstruction at a given sparsity implies a better or more faithful SAE — an important methodological corrective for the field.

4. **c_dec validated as a practical diagnostic (Sections 3.5, 4).** In toy models, c_dec is minimized at the true L₀ (Figure 6). On real LLM SAEs (Gemma-2-2b, Llama-3.2-1b), the "elbow" of the c_dec curve coincides with peak k-sparse probing performance (Figure 8), providing a geometry-based heuristic that practitioners can use without ground-truth features.

5. **JumpReLU vs. BatchTopK comparison (Sections 3.6, 4.1, Figure 9).** The finding that JumpReLU SAEs achieve lower c_dec and better sparse-probing F₁ than BatchTopK at high L₀, and that JumpReLU's L₀ "sticks" near the correct value across a wide range of sparsity coefficients, provides a mechanistic explanation for why per-latent thresholds mitigate feature mixing.

---

## Weaknesses

### Fatal

None.

### Major

None. No weakness threatens the paper's core claims.

### Minor

1. **The claim "most commonly used SAEs have an L₀ that is too low" is not well-supported by the paper's own evidence.** This appears in the abstract ("We find that most commonly used SAEs have an L₀ that is too low"), the introduction, and the discussion. The only evidence offered is a "cursory search of open source SAEs on Neuronpedia" showing "L₀ less than 100 is very common" (Section 6, referencing Appendix A.13). A systematic survey or quantitative citation is absent. This does not invalidate the core contribution — the paper's main point is that L₀ *matters* and can be too low, not that most existing SAEs are wrong — but the claim is overstated relative to the evidence. The authors could either remove it or back it with a focused survey.

2. **Limited LLM validation scope.** The paper studies only two models (Gemma-2-2b and Llama-3.2-1b) at one or two layers each. While the toy model experiments are thorough and the LLM results are consistent with them, the number of LLM evaluations is modest. This limits certainty about how broadly the findings generalize across models, layers, and SAE configurations. The authors acknowledge this implicitly, but the limitation is worth stating explicitly as a scope condition.

3. **c_dec's computational cost for very wide SAEs is not discussed.** The metric sums over all \( \binom{h}{2} \) pairs of latents, making it \( O(h^2) \) in the hidden dimension. For very wide SAEs (e.g., \( h = 2^{17} \)), this could be expensive. The paper would benefit from noting this and suggesting mitigations (e.g., random subsampling of latent pairs).

4. **Missing variance/error bars in some LLM experiments.** While Figure 8 shows 3 seeds per L₀ and the toy model plots include standard deviation shading (Figure 6), other LLM results (Figure 9) do not report variance. Adding error bars or noting that only single runs were performed would improve transparency.

### Trivial

None.

---

## Nice-to-Haves

- The paper could provide a more prescriptive practical recommendation: e.g., train SAEs at a few L₀ values, compute c_dec, and pick the L₀ at the elbow. The paper already moves toward this (Figure 8 finds "peak sparse probing occurs in the elbow") but stops short of making it a concrete protocol.
- The observation that JumpReLU SAEs' L₀ "sticks" near the correct value (Section 3.6) is interesting and could benefit from deeper discussion: is this a known property of JumpReLU training, or is it specific to these toy models?

---

## Removed Points

- **"No theoretical bound or guarantee for c_dec (Appendix A.6)"** — Removed because Appendix A.6 is stripped by the parser. The paper's original submission contains this content, so it cannot be evaluated as a weakness.
- **"Insufficient comparison to competing metrics"** — The harsh critic mentioned this as a possible concern, but the paper does compare against alternative metrics in Appendix A.9 (stripped). Without being able to verify, this is not a supported weakness.
- **Strength: "This paper addressed an important problem"** — Removed as generic. Many papers address important problems; this is not a specific strength.

---

## Novel Insights

None beyond the paper's own contributions. The core claim (incorrect L₀ → feature mixing) and the c_dec diagnostic are the paper's own novel contributions, and no reviewer identified an unexpected implication that the authors themselves missed.

---

## Suggestions

1. Either remove the "most commonly used SAEs have too low L₀" claim or back it with a systematic survey (e.g., compute c_dec on a representative sample of public Neuronpedia SAEs and report the distribution).
2. Add a brief discussion of c_dec's \( O(h^2) \) computational cost and suggest practical mitigations (subsampling, mean cosine similarity to a random subset).
3. Add error bars or variance information to Figure 9 and any other single-seed LLM plots.

---

## Score and Decision

Calibration anchors (all rounds):

| Anchor path | Avg score | Round | Comparison |
|---|---|---|---|
| Wxl0JMgDoU | 2.50 | R1 (low) | Much weaker — chess SAE paper, poorly reviewed |
| 89wVrywsIy | 3.40 | R1 (low) | Weaker — circuit tracing, mixed reviews |
| UbLvSPMvMA | 1.67 | R1 (low) | Much weaker — binary SAE paper, poorly reviewed |
| zgHamUBuuO | 3.00 | R1 (low) | Weaker — sparsling paper, sparsity bottleneck |
| 9ca9eHNrdH | 7.00 | R1 (mid) | Similar — SAE critique paper, broad acceptance. Current paper is cleaner in execution but narrower in scope |
| ghH6YYDs15 | 4.67 | R1 (mid) | Weaker — amortisation gap paper, flawed theory and limited experiments |
| F76bwRSLeK | 4.80 | R1 (mid) | Weaker — original SAE paper, foundational but mixed reviews |
| NB8qn8iIW9 | 4.00 | R1 (mid) | Weaker — feature-aligned SAEs, limited evaluation |
| tcsZt9ZNKD | 8.20 | R1 (high) | Stronger — TopK SAE scaling paper, highly influential methods contribution |
| I4e82CIDxv | 8.00 | R1 (high) | Stronger — sparse feature circuits, multiple evaluations |
| 1Njl73JKjB | 7.00 | R2 (narrow) | Similar — principled SAE evaluations framework, comparable quality |
| LC2KxRwC3n | 7.50 | R2 (narrow) | Slightly stronger — feature absorption paper (but was rejected) |
| MDvecs7EvO | 6.50 | R2 (narrow) | Similar — SAE feature matching across layers, comparable quality |
| v675Iyu0ta | 5.60 | R2 (narrow) | Weaker — interpretability illusions, not directly comparable |
| B9XP2R9LtG | 5.25 | R2 (narrow) | Weaker — activation sparsity scaling laws, less relevant |

**Round 1 bracket:** Between 3.5 and 7.5 (clearly above the weak anchors, below the strong 8+ anchors).

**Round 2 narrowing:** Compared against Canonical Units (7.0), Principled Evaluations (7.0), Feature Absorption (7.5), and Compute Optimal Inference (4.67), the paper sits between 6.0–7.0. It is cleaner than the 4.67 paper, about on par with the 6.5–7.0 papers in quality, and less ambitious than the 8.0+ papers. The core contribution is well-evidenced and practically useful, with minor weaknesses that do not threaten acceptance.

**Final score:** 6.5 — a solid paper with a clear, important finding that will affect SAE training practice. The toy model experiments are rigorous, the c_dec diagnostic is practical, and the limitations (modest LLM scope, an overclaimed generality statement) are addressable.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>