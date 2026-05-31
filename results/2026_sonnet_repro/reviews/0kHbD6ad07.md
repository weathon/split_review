Now let me perform the calibration search.**Round 1 bracket:** The paper is well-positioned between 5 and 7.5. It has rigorous theoretical contribution (better than the 3.0 rejects), but with some gaps that prevent it from hitting the 7.5+ tier. Let me narrow.Now I have enough to write the full review.

---

## Summary
This paper proves that decoder-only Transformer language models are almost surely injective: distinct input prompts yield distinct last-token representations for essentially all parameter settings, and this property is preserved throughout gradient-based training. The paper supports this with formal proofs using real-analytic function theory (Theorems 2.1–2.3), large-scale empirical collision search across 5 billion pairwise comparisons with zero collisions across six model families, and introduces SIFT/SIpIT, an algorithm that recovers the exact input sequence from intermediate hidden states in provable linear time.

---

## Strengths

- **Rigorous training-preservation result**: Theorems 2.1–2.3 give a complete chain: (i) Transformers are real-analytic in parameters, (ii) collision sets are measure-zero at initialization, (iii) gradient-descent steps preserve absolute continuity of the parameter distribution, so injectivity holds after any finite number of training steps with probability one. This is a legitimate advance over Sutter et al. (2025), which established injectivity only at initialization.

- **Massive, zero-collision empirical validation**: Approximately 5 billion pairwise comparisons across GPT-2 S/M/L and Gemma-3 1B/4B/12B yield zero collisions (Figure 3, Table 1). The margin above the collision threshold is orders of magnitude (e.g., 0.001–9.0 across models and layers). Tables 2–3 extend this to 70B-parameter models under FP4/INT8 quantization with continued zero collisions.

- **Provably exact and efficient inversion**: SIpIT (Algorithm 1) is proved correct in at most T|𝒱| steps (Theorem 3.1) and noise-robust (Theorem 3.2). Empirically, it achieves 100% token-level accuracy on GPT-2 Small in 28 s mean time (Table 5), while the gradient-based policy explores < 0.22% of the vocabulary even on 128K-vocabulary Llama-3.1-8B under FP4 quantization (Table 4).

- **Corollaries strengthen scope**: Corollary 2.3.1 extends injectivity preservation to SGD and arbitrary mini-batch GD; Corollary 2.3.2 establishes global distinctness for any finite prompt set—both are clean, immediate consequences of the core argument.

- **Graceful scaling with depth**: Figure 6 shows inversion time increases only mildly from layer 1 to layer 12 on GPT-2 Small, confirming no prohibitive overhead from depth.

---

## Weaknesses

### Fatal
None.

### Major

- **No empirical comparison with Thomas et al. (2025), the paper's self-identified closest prior work.** §5 (line 339) explicitly describes Thomas et al. (2025) as "most closely related," noting it "recover[s] prompts from hidden states via a sequential algorithm" — the exact same setting as SIpIT. The paper explains the qualitative difference (Thomas et al. lacks formal exactness guarantees and scores all vocabulary tokens before committing), but provides no empirical comparison. Given the paper's claim of practical advance, situating SIpIT's efficiency (0.19–0.21% vocabulary explored) against Thomas et al.'s procedure would be the most direct validation available, yet it is entirely absent.

- **Optimizer restriction**: Theorem 2.3 assumes step sizes η ∈ (0, 1). This covers vanilla SGD and mini-batch GD, but all the models tested empirically — GPT-2, Gemma-3, Llama-3.1, Mistral-7B, Phi-4 — are trained with Adam or its variants, where per-coordinate updates can violate this constraint and the update map is not φ(θ) = θ − η∇L(θ). The paper does not acknowledge this gap between the theoretical setting and the actual training procedure of every model in its experiments. A brief discussion of why the argument might (or might not) extend to adaptive optimizers would substantially strengthen the claim that "injectivity is preserved under training."

### Minor

- **Unexplained quantization distance inflation (Table 2).** FP4 and INT8 quantization consistently *increase* minimum pairwise distances relative to FP32 (e.g., Llama-3.1-8B: 1.274 → 2.281 (FP4), 6.597 (INT8)). The paper states this "more than doubles the minimum distance" without mechanistic explanation. A plausible confound is that quantization changes representation scale/norm, inflating raw L2 distances without any semantic separation benefit. The paper should either normalize by representation magnitude or provide a brief mechanistic account of why quantization increases separability.

- **ε = 10^{-6} collision threshold lacks dimensional grounding.** This single threshold is applied across models ranging from GPT-2 Small (d=768) to Llama-3.1-70B (d=8192) under FP32 and FP4 precision. In practice the values are far above threshold (minimum distances of 0.001–18+ in Tables 1–3), so the conclusion is unaffected, but a brief justification of the threshold's scale-independence would improve rigor.

### Trivial

- **Algorithm naming inconsistency.** The algorithm appears as "SIFT" in the abstract (line 9), "SIPIT" in §3's prose introduction (line 45), "SIpIT" in Algorithm 1 (line 171), and "SiPT"/"SIpT" variously throughout §4 (lines 234, 292, 309, 313). This appears to be an editing artifact and should be standardized throughout.

---

## Nice-to-Haves

- It would strengthen the paper's own case to show whether SIpIT can be modified to operate from the last-token representation alone (as the injectivity theorem targets), rather than requiring the full per-position hidden-state matrix H^(ℓ). The paper explicitly acknowledges this is left to future work (§3, line 141), which is appropriate — but even a brief discussion of why efficient last-token inversion is nontrivial would clarify the gap between the theoretical guarantee and the practical algorithm.
- The "Jacobian det Dφ(θ) is not identically zero" claim in the sketch of Theorem 2.3 is delegated to "one can check this by evaluating at a simple parameter setting." Sketching that parameter setting in the main text (even briefly) would make the core step of the training-preservation argument more transparent.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"HARDPROMPTS comparison is uninformative"** (Harsh Critic): The paper explicitly explains (§4.2, §5) that HardPrompts operates in a fundamentally different setting (gradient-based prompt optimization, not inversion from hidden states). The paper does not present this as the primary evidence of recovery quality — it is included as a natural foil to show that gradient-guided optimization does not recover prompts in this setting. Removed: the comparison is not misleading and the paper acknowledges the difference.

- **"The real-analytic argument is not transformer-specific"** (Harsh Critic): The critic notes that the proof strategy (real-analytic function on finite domain, not identically zero, hence zero set is measure-zero) applies to any real-analytic map on a finite discrete input space, not just transformers. This is technically true, but the paper's architecture-specific contribution is Theorem 2.1 (establishing real-analyticity of the transformer, including LayerNorm with ε > 0, causal attention, GELU/tanh activations). The proof of non-collapse (Theorem 2.2) and training preservation (Theorem 2.3) do leverage the transformer's structure through this analyticity. The criticism overstates the generality as a weakness.

- **"Privacy stakes are overstated because white-box access is required"** (Harsh Critic): This is scope creep. The paper's discussion section accurately states the threat model requires white-box access to activations and discusses practical settings (leaked KV-cache, shared-inference pipelines). The privacy argument is proportionate.

- **"Missing appendix proofs"**: The parser strips appendices; criticisms about absent formal proofs in appendices are REMOVED per hard rules.

- **"The Strength Finder claim that HardPrompts is beaten on recovery"**: This is valid — Table 5 shows 0% vs 100% token accuracy. Kept as a strength since the comparison is grounded.

---

## Novel Insights

The paper's most intellectually substantive contribution is less the injectivity result itself (which, as the harsh critic notes, reduces to a tidy application of real-analytic function theory on a finite domain) and more the *training-preservation* result: that gradient descent, being a real-analytic map with non-zero Jacobian determinant, preserves absolute continuity of the parameter distribution, thereby ensuring that injectivity never deteriorates during finite-horizon training. This argument is clean and has broader applicability — it could potentially be used to prove other "generic" properties of neural architectures are stable under training, not just injectivity. The sequential inversion algorithm's key insight — exploiting causal structure to reduce a global T×d inversion problem into T independent 1-token lookups — is also practically elegant and may be useful for other interpretability or probing applications.

---

## Suggestions

1. Include even an informal comparison with Thomas et al. (2025) on a shared benchmark (e.g., a small set of prompts) — not to beat it, but to establish that the < 0.22% vocabulary exploration rate in Table 4 represents a practical improvement over vocabulary-scoring approaches.
2. Add a paragraph in §2 or §4.1 addressing adaptive optimizers: explain why the step-size restriction matters (or argue why the conclusion likely holds under Adam, even without formal proof).
3. Normalize pairwise distances by representation norm (or report cosine distances alongside L2) in Table 2 to decouple the quantization distance-inflation observation from scale effects.
4. Standardize the algorithm name throughout the paper (pick one: SIpIT, SIFT, SiPT).

---

## Calibration and Score

**Anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| NHhjczmJjo.md | 7.00 | R2 | Accept. Theory + empirical on transformers (ICL + sparse recovery). Rigorous but several gaps between theory and practice; comparable depth and scope to the paper under review. |
| 6S4WQD1LZR.md | 6.67 | R2 | Accept. Universal approximation of transformers, mainly theoretical with few practical implications. Weaker practical grounding than the paper under review. |
| 1lFZusYFHq.md | 6.20 | R2 | Borderline reject. Transformer theory (induction heads); similar theoretical flavor but narrower scope. |
| YE6N8htoFQ.md | 6.00 | R2 | Reject. Transformer ICL theory with positional encoding; weaker empirical validation. |
| uBai0ukstY.md | 7.00 | R1 | Accept. Equivariant functional networks for transformers; comparable theoretical depth. |
| 5EtSvYUU0v.md | 6.00 | R1 | Reject. NTK/NNGP theoretical framework; broadly similar profile. |
| STUGfUz8ob.md | 7.60 | R1 | Strong accept. Transformer reasoning theory; stronger on novelty and significance. |
| SPS6HzVzyt.md | 8.00 | R1 | Strong accept. Mechanistic interpretability; different domain. |

**Round 1 bracket:** 5–7.5 (clearly above the 3.0 rejects; below the 7.5+ tier of highly significant results).

**Round 2 narrowing:** The paper is stronger than the 6.0–6.2 papers (weaker empirical grounding, less actionable results). It is comparable to NHhjczmJjo (7.0): both have rigorous theory + empirical validation + practical algorithm, and both have gaps between their theoretical assumptions and practical deployment. The paper under review has a cleaner single-thread argument (injectivity → SIFT) but the missing Thomas et al. comparison and the optimizer gap pull it slightly below the 7.0 level. The paper is stronger than 6S4WQD1LZR (6.67) — it has more practical grounding and a concrete algorithm.

**Final score:** **6.5**. The paper makes a real, rigorous, and practically grounded contribution. The weaknesses (acknowledged theory-algorithm gap, absent Thomas et al. comparison, optimizer restriction) are genuine but do not invalidate the core claims. The paper falls between the 6.67 and 7.0 anchors, closer to 6.5 due to the missing empirical comparison with the most directly relevant prior work.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>