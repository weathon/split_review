Now I have a clear picture. Let me synthesize the final review.

## Calibration Report

**Round 1 — Bracketing:**
- Weak anchors (<3.5): Retrieved topic-related papers scoring 2.0–3.33 (rejected). InfoTok is clearly stronger.
- Middle anchors (3.5–7.5): AdapTok (4.0, adaptive video tokenizer), TivTok (4.5, video tokenization), AToken (6.5, unified vision tokenizer). InfoTok is stronger than AdapTok and TivTok but narrower than AToken.
- Strong anchors (>7.5): Papers on unrelated topics — not applicable for calibration.

**Initial bracket:** [5.0, 6.5]

**Round 2 — Narrowing:**
- WeTok (5.0, accept poster) — discrete visual tokenization; InfoTok has stronger novelty and theory.
- AliTok (5.5, accept poster) — tokenizer alignment; comparable quality of contribution.
- Latent Denoising Tokenizer (6.5, accept poster) — broader tokenizer improvement; InfoTok is less complete (no downstream).
- FLoC (5.0, accept poster) — video token compression for LMMs; InfoTok is stronger conceptually.
- VideoChat-Flash (6.5, accept poster) — hierarchical video compression for LMMs; different sub-area.

**Final score rationale:** 5.5. InfoTok is stronger than 5.0-level papers (WeTok, FLoC) due to cleaner theoretical framing, more thorough ablations (Table 2 vs optimal is compelling), and stronger empirical gains. However, the underspecified per-token ELBO mechanism, the lack of downstream generation evaluation, and the slightly overstated theoretical claims prevent it from reaching the 6.0–6.5 tier.

---

## Summary

This paper proposes InfoTok, an adaptive discrete video tokenizer that replaces fixed-rate compression with a content-dependent token budget determined by each video's ELBO (evidence lower bound). The framework consists of two core components: (1) an ELBO-based router that predicts the number of tokens a video needs, and (2) a transformer-based adaptive compressor that selects which tokens to retain via an information-content mask. The paper provides theoretical analysis (Theorems 2.2 and 3.1) motivating why data-agnostic routers are suboptimal and why an ELBO-based router approaches optimality. Empirically, InfoTok achieves substantial gains over the prior adaptive method ElasticTok — e.g., FVD of 49 vs 141 at the same compression rate (BPP₁₆=0.81) on TokenBench — while requiring only 1 additional network forward evaluation compared to ElasticTok's 11.

## Strengths

- **Strong empirical gains with clean ablations.** Table 1 shows 1–2 dB PSNR improvements over ElasticTok at matched compression rates (e.g., 30.08 vs 28.26 at BPP₁₆=0.81), with FVD reductions of 40–65%. Table 2 is particularly convincing: the ELBO-based router nearly matches an exhaustive optimal search across all compression rates, validating the information-theoretic proxy.

- **Inference efficiency is a concrete advantage.** Figure 4(g) quantifies the overhead cleanly: InfoTok requires 1 additional NFE vs ElasticTok's 11. This is a practical win over binary-search-based adaptive methods.

- **Ablation demonstrating architecture-agnostic benefit.** Table 3 (Right) shows InfoTok's adaptive mechanism improves both Cosmos (+1.95 PSNR) and ViT (+1.43 PSNR) backbones relative to ElasticTok's uniform mechanism, confirming the improvement is from the mechanism, not the architecture.

- **Clean framework that builds on existing tokenizers.** Algorithm 1 provides a unified view of adaptive tokenization, and the design of reusing a fixed tokenizer's encoder/decoder with minimal addition (router + compressor/decompressor) makes the approach practical.

## Weaknesses

### Major

None.

### Minor

- **Per-token ELBO estimation is underspecified, creating a reproducibility gap.** The paper states that the adaptive compressor "preserves the top N_x tokens according to their corresponding per-token log-likelihood, which is also approximated via the ELBO values" (Section 3.2). However, ELBO is defined as a scalar per video (Equation 3), and no derivation or description is given for how per-token importance is obtained from this global quantity. The most natural interpretation is that per-patch reconstruction error serves as a proxy, but this is never stated explicitly. Since the token selection mechanism is central to the method, this missing detail is the paper's most significant weakness. The authors should clarify the exact computation in a revision.

- **Theorem 2.2 is an existence proof, not a universal characterization of suboptimality.** The theorem constructs a specific adversarial distribution where uniform routing leads to arbitrarily poor expected token length. The paper's abstract and introduction frame this as proving existing methods are "inherently biased" and "suboptimal," which overstates what a counterexample establishes. The theorem correctly demonstrates a fundamental limitation in the *worst case*, but it does not prove that all practical configurations exhibit this behavior. The empirical results are strong enough that this overclaiming is not fatal, but the paper would benefit from more precise hedging.

- **Adaptive compressor architecture is incompletely described.** The paper specifies that the compressor is an 8-layer transformer with block-causal attention and that it "transforms information appropriately" to output variable-length sequences. The mechanism by which a fixed-length input becomes a variable-length output — whether through attention-based pooling, causal truncation, or some other operation — is left implicit. The binary mask described in Section 3.2 suggests the approach is: process the full sequence, mask the lowest-ELBO tokens, and train the model to compress information into the remaining tokens. This should be stated explicitly in the main text.

### Trivial

- **Overhead figure.** The paper claims the binary mask adds "approximately 5%" overhead in token length. The precise figure is 1/16 = 6.25% (1 bit mask per token, where each token covers 256 pixels; this is straightforward to verify). The approximation is close but should be corrected for accuracy.

## Nice-to-Haves

- Report wall-clock inference latency (ms per video) rather than just NFE ratios, to give a complete efficiency picture.
- Extend evaluation to downstream video generation — the paper acknowledges this as out of scope, but it would substantially strengthen the contribution.
- Reconcile the notation: the router is deterministic at test time (delta distribution in Eq. 4), which is fine; Algorithm 1's "sample" language could be clarified to reflect this.

## Removed Points

The removed points are flagged to be removed; treat them with caution.

- *Critique about Figure 1 being "cluttered"* — pure formatting/style nitpick, removed.
- *Critique about ElasticTok reproduction being unclear* — the paper clearly states they ran ElasticTok on their own data splits for fair comparison; concern was based on misreading.
- *Critique about the delta distribution conflicting with "sampling" in Algorithm 1* — sampling from a delta distribution is deterministic; no actual conflict exists.
- *Strength Finder's claim that "Rigorous proof of suboptimality" is a top strength* — kept but qualified in the main review with the Theorem 2.2 caveat.
- *Strength Finder's claim about "Theoretical optimality guarantee"* — kept but qualified in the minor weaknesses.
- Several generic strengths from the Strength Finder (e.g., "the problem is important," "framework generalizes across architectures") — these are either already covered or are generic.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Explicitly state how per-token importance is derived from the global ELBO (e.g., per-patch reconstruction loss as a proxy). This is the single most important clarification for reproducibility.
2. Add a paragraph after Theorem 2.2 acknowledging it is a worst-case construction, and clarify that the practical motivation comes from combining the theoretical counterexample with strong empirical validation.
3. Describe the adaptive compressor's variable-length output mechanism explicitly in the main text (not just in the appendix).

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>