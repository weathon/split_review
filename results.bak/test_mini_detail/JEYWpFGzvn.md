Now I have all the information I need. Let me write the final consolidated review.

## Summary
This paper introduces InfoTok, an adaptive discrete video tokenization framework that uses an evidence lower bound (ELBO)-based router to dynamically determine token lengths per video, combined with a transformer-based adaptive compressor. Built on top of existing fixed-length tokenizers (Cosmos-DV), InfoTok achieves 20% token savings at matching reconstruction quality and demonstrates a 1 NFE inference overhead versus ElasticTok's 11 NFEs.

## Strengths
- **Principled theoretical motivation with empirical validation**: Theorem 2.2 formally shows that data-agnostic (uniform) routers can be arbitrarily suboptimal in an idealized setting. Theorem 3.1 provides a theoretical bound on expected token length for the proposed ELBO-based router. While these theorems operate under strong assumptions, the paper backs them with empirical evidence: InfoTok's ELBO-based routing closely matches an "optimal" search-based routing strategy across multiple compression levels (Table 2), confirming that the theory translates into practice.

- **Strong empirical compression-quality results**: Table 1 shows InfoTok at BPP₁₆=0.81 achieves PSNR 30.08 and FVD 49 on TokenBench, matching Cosmos-DV at BPP₁₆=1.00 (PSNR 30.01, FVD 49) — a genuine 19% token savings at essentially identical quality. At BPP₁₆=0.56, InfoTok (PSNR 29.27, FVD 70) still outperforms ElasticTok at BPP₁₆=0.81 (PSNR 28.26, FVD 141), demonstrating a better compression-quality trade-off.

- **Inference efficiency**: Figure 4g shows InfoTok requires only 1 additional network forward evaluation (NFE) per video versus ElasticTok's 11 NFEs for binary search over token lengths. This is a concrete and practically meaningful advantage.

- **Ablation studies isolate the contribution of each component**: Table 3 (Left) compares per-token ELBO masking against R2L and Jump strategies, showing the compressor design matters. Table 3 (Right) shows the InfoTok adaptive mechanism outperforms ElasticTok's uniform mechanism on two different backbone architectures (Cosmos and ViT), indicating architecture-agnostic benefits.

## Weaknesses

### Fatal
None.

### Major
- **Per-token ELBO computation is not defined**: The paper's core mechanism (Section 3.2) requires per-token ELBO values to compute a binary mask, but only a scalar ELBO(x) for the entire video is defined in Section 3.1 (Eq. 3). The statement "it does not incur extra network evaluation since the log-likelihood term has been computed in the router" does not explain how per-token values are derived from the single scalar. While one can infer that per-pixel reconstruction errors from the decoder pass could be spatially aggregated per token region, the paper never specifies this. This is a meaningful reproducibility gap in the central component of the method.

- **Contradictory headline claims**: The abstract states "saving 20% tokens without influence on performance" (supported by Table 1: 0.81 vs 1.00 BPP). However, the introduction claims "save approximately 50% tokens without loss of reconstruction quality compared to state-of-the-art fixed-length tokenizers." This 50% figure is not supported — at BPP₁₆=0.56 (closest to 50% savings), PSNR drops from 30.01 (Cosmos-DV) to 29.27 (InfoTok), a clear quality loss. Such inconsistency undermines trust in the paper's numerical claims and should be corrected.

### Minor
- **Limited adaptive baselines**: Only ElasticTok is compared among adaptive methods. Other adaptive tokenizers (ALIT, CAT, One-D-Piece, FlexTok) are discussed in related work but receive no empirical comparison. While some target images rather than video, the claim of "state-of-the-art" is only supported against one competitor.

- **No statistical uncertainty reported**: All metrics in Tables 1–3 are single point estimates without standard deviations, confidence intervals, or multiple seeds. Given that the core comparison (InfoTok at 0.81 BPP vs Cosmos-DV at 1.00 BPP, 30.08 vs 30.01 PSNR) is extremely tight, the absence of variance information makes it hard to assess whether the "matching" claim is robust.

- **Theoretical gap between theorems and method**: Theorem 2.1 addresses lossless source coding, but video tokenization is lossy. Theorem 3.1's bound requires strong assumptions (tokenizer minimizing reconstruction loss exactly, ELBO approximating log-likelihood perfectly) that are not met in practice. The paper acknowledges this ("believed to be close enough") but the gap between "provable guarantee" and "reasonable heuristic" is wider than the presentation suggests.

### Trivial
- Algorithm 1 writes `N_x ∼ r(N|x)` suggesting sampling, but Eq. 4 defines `r` as a deterministic delta distribution. This is not a contradiction (sampling from a delta always gives the same value), but the notation is inconsistent.
- The "2.3× compression rates" claim in the abstract is not clearly tied to a specific table entry in the main text.

## Nice-to-Haves
- A wall-clock speed comparison (ms/video) would be more informative than the NFE ratio, since InfoTok's extra decoder pass could be slower per-pass than ElasticTok's forward passes.
- Evaluating InfoTok's tokens in a downstream task (e.g., a lightweight video classifier or generative model) would strengthen the claim that the tokens preserve semantic content, not just reconstruction fidelity.

## Removed Points
These points were considered but excluded from the main weaknesses for the reasons noted:

- *Harsh critic's claim that "the method cannot be reproduced from the description" (Critical Issue 1)* — Kept but downgraded from "structural flaw/fatal" to Major. The per-token ELBO computation is unspecified, but the high-level pipeline (encode, compute reconstruction error, use it for per-token selection, compress) is described. A practitioner familiar with Cosmos could reconstruct the likely approach. The gap is significant but not fatal.

- *Harsh critic's claim about "delta distribution conflicts with Algorithm 1 suggesting sampling"* — Moved to Trivial. Sampling from a delta distribution is deterministic by definition; the notation is slightly confusing but not incorrect.

- *Harsh critic's claim that "compared methods (ALIT, CAT, One-D-Piece, FlexTok) are mentioned in related work but not compared"* — Kept but placed as Minor. These are mostly image-domain methods; a direct video comparison may not be fair.

- *Harsh critic's claim about "Theorem 2.1 is about lossless compression"* — Acknowledged but not a fatal weakness. The paper uses it as motivation for adaptive tokenization, which is reasonable.

- *Strength Finder's claim about "Theorem 2.2 establishes a fundamental flaw in prior heuristic approaches"* — This overstates the claim. Theorem 2.2 proves suboptimality in an idealized setting with strong assumptions; it does not directly prove ElasticTok is bad in practice. The paper is careful about this, but the Strength Finder inflates it.

- *Strength Finder's claim about "Theorem 3.1 achieves near-optimal compression in theory"* — This is technically what the paper states, but the bound depends on assumptions not met in practice. Included as a strength with appropriate caveats.

- *Strength Finder's generic/delusional strengths about "important problem" and "clear motivation"* — Removed as generic or superficial.

## Novel Insights
None beyond the paper's own contributions. The two reviewers' analyses largely converge on the paper's strengths (principled motivation, strong empirical compression-quality trade-off, efficiency) and weaknesses (incomplete method specification, inconsistent claims, limited baselines). The review process did not surface unexpected findings about the work.

## Suggestions
1. **Clarify the per-token ELBO computation** in Section 3.2. State explicitly how per-token values are derived (e.g., from per-pixel reconstruction loss aggregated over each token's spatial-temporal region in the Cosmos tokenizer's latent grid).
2. **Correct the inconsistent 50% claim** in the introduction to match the data in Table 1. Replace "50% tokens without loss" with the actual supported figure (~20%).
3. **Add error bars** (or at minimum, results from 2-3 seeds) to the main tables, especially for the tight Cosmos-DV comparison at 0.81 BPP.
4. **Include at least one additional adaptive baseline** (e.g., apply a simple adaptive mechanism from ALIT or FlexTok to video as a sanity check) to substantiate the "state-of-the-art" claim.
5. **Soften the theoretical claims** in the presentation — avoid "rigorously prove" and "near-optimal" when the gap between theory and practice is acknowledged.

## Score and Decision

**Bracketing (Round 1):** Three queries on "video tokenization adaptive compression" returned weak anchors (avg 2.5–3.0, rejected/withdrawn), middle anchors (avg 4.0–7.0), and strong anchors (avg 8.0–9.0, oral/posters). The paper clearly sits above the weak cluster (rejected papers with limited contributions) and below the strong cluster (major foundation-model-level contributions like SAM 2). Initial bracket: **4.0 – 7.0**.

**Narrowing (Round 2):** Two queries targeting the 4.5–7.5 range retrieved four key anchors:

- **BSQ-ViT** (avg 6.0, poster) — Complete video tokenizer with comprehensive benchmarking; more polished methodologically but addresses fixed-length tokenization, not adaptivity. InfoTok is less complete but addresses a harder problem (variable-length).
- **AVT — Adaptive Length Image Tokenization** (avg 5.75, poster) — Most directly comparable: similar scope (adaptive tokenization), similar issues (limited baselines, unclear gradient flow). InfoTok has stronger empirical comparisons and theoretical grounding but a method description gap. *InfoTok is comparable to AVT, slightly stronger on empirical evidence.*
- **SeTok** (avg 6.2, poster) — Adaptive tokenization for MLLMs with broader downstream evaluation; different application domain.
- **ε-VAE** (avg 5.67, rejected) — Variable scores ranging 3–8; method had limited novelty.

Comparing against the most relevant anchor (AVT, 5.75): InfoTok has a more rigorous theoretical framing and stronger empirical results (matching a strong SOTA at 20% savings), but suffers from an inconsistent headline claim (50% vs 20%) and an underspecified method component. The similarities in both contributions and issues are striking; InfoTok is marginally stronger empirically but has a more consequential presentation flaw. The per-token ELBO gap is roughly equivalent in severity to AVT's unclear gradient flow.

**Final score:** 5.5 — The paper makes a genuine contribution (principled adaptive video tokenization with solid empirical evidence and practical efficiency gains) but is held back by a meaningful method description gap and inconsistent claims that need to be resolved. This places it slightly below the polished BSQ-ViT (6.0) and on par with or slightly below AVT (5.75), in the borderline accept range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>