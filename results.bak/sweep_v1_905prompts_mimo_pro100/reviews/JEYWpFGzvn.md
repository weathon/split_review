Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper introduces InfoTok, an information-theoretic framework for adaptive video tokenization that proves data-agnostic routers (as used in ElasticTok) are suboptimal and proposes an ELBO-based router with near-optimal compression guarantees. The method converts existing fixed-length tokenizers (e.g., Cosmos) into adaptive counterparts using a router that dynamically allocates token lengths based on estimated information complexity, and a transformer-based adaptive compressor that selects tokens by per-token ELBO. Empirical results demonstrate ~20% token savings matching Cosmos quality, 2.3× better compression than ElasticTok, and 11× fewer inference NFEs.

## Strengths

- **Rigorous theoretical grounding**: The paper provides formal proofs (Theorem 2.2, Theorem 3.1) that data-agnostic uniform routers are suboptimal and that the ELBO-based router achieves near-optimal compression up to the ELBO–log-likelihood approximation error. This information-theoretic framing is novel and well-executed, elevating the contribution above heuristic alternatives.

- **Strong empirical results over the direct predecessor**: Table 1 shows InfoTok substantially outperforms ElasticTok at matched compression rates (e.g., FVD reduced 40–60%, LPIPS reduced 25–40%, PSNR improved 1–2 dB), while Figure 4g shows 11× fewer inference NFEs. Table 3 (right) demonstrates the ELBO-based mechanism generalizes across both Cosmos and ViT architectures.

- **Validated router via optimal search ablation**: Table 2 directly compares the ELBO-based router against an exhaustive search-based optimal strategy across two datasets and three compression levels, showing near-identical performance. This is the central empirical evidence that the ELBO proxy works in practice and it is convincing.

- **Clean method with practical value**: The framework seamlessly extends existing fixed-length tokenizers, requires only one additional decoder forward pass for routing, and includes mask-storage overhead in the BPP calculation (β = N_max · (BPP₁₆ − 1/16) as stated in Section 4.1). The design is both principled and practically convenient.

## Weaknesses

### Fatal
None.

### Major

- **Inconsistent token-savings claims across the paper**: The abstract claims "saving 20% tokens without influence on performance" (comparing to Cosmos at BPP₁₆=1.00 with matched quality at BPP₁₆=0.81). The introduction claims "save approximately 50% tokens without loss of reconstruction quality compared to state-of-the-art fixed-length tokenizers." Looking at Table 1, InfoTok at BPP₁₆=0.56 achieves PSNR 29.27 vs. Cosmos's 30.01 — a measurable 0.74 dB drop. The body text in Section 4.2 itself states "INFOTOK performs similarly to Cosmos-DV with 20% tokens saved," directly contradicting the introduction's 50% claim. This selective inconsistency undermines trust in the headline numbers and needs reconciliation. — *Matters because it affects the paper's central empirical claim about compression efficiency.*

### Minor

- **Theorem 2.2 generality overstated in the introduction**: The abstract and introduction claim to "rigorously prove that existing data-agnostic training methods are suboptimal," but Theorem 2.2 is an existence result: "there exists a data distribution D and a sufficiently large N" where the gap is arbitrary. This is a worst-case result, not a general statement about all distributions. The theoretical section itself is precise, but the introduction overstates its scope. — *Matters for accurately representing the theoretical contribution.*

- **ELBO–log-likelihood gap not directly measured**: Theorem 3.1's bound H_C(D) + β − E[−log p(x)] depends on how close ELBO is to log-likelihood. The paper justifies this by noting "large-scale neural networks" make ELBO "close enough" and Table 2 empirically validates router quality, but the actual gap is never measured. Directly quantifying this gap on the test set would strengthen the theoretical narrative. — *Table 2 provides indirect validation, so this is about strengthening rather than a fundamental gap.*

- **Unsubstantiated claim about KL term**: Section 3.1 states "the KL term is approximately proportional to the reconstruction error, and the ratio is similar" as justification for using reconstruction error alone. This claim is made without supporting evidence or empirical verification. — *Minor practical concern since the method works, but the claim should either be supported or removed.*

### Trivial
None.

## Nice-to-Haves
- Expanding Table 2 (the "Optimal" routing ablation) with per-video token allocation distributions and additional compression levels would most directly validate the core contribution.
- Adding a brief downstream evaluation (e.g., video generation conditioned on InfoTok tokens) would strengthen the claim of practical value, though the authors transparently note this is outside scope.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh critic's concern about mask-storage overhead not being included in BPP**: This is addressed directly in the paper. Section 4.1 explicitly states β = N_max · (BPP₁₆ − 1/16), where 1/16 is "the cost of binary mask." The concern is unfounded.
- **Harsh critic's concern about "future work generalization to audio/3D presented as contribution"**: The paper presents this only in Section 6 (Discussions & Limitations) as future work, not as a contribution. The concern mischaracterizes the paper.
- **Strength finder's claim about "strong theoretical foundation" as separate from verified weaknesses**: The theoretical foundation is indeed strong but the overstatement of Theorem 2.2 generality (verified) tempers this somewhat. The strength is kept but noted with the caveat.
- **Strength finder's generic claims about importance of the problem**: These are surface-level observations, not specific to this paper's evidence.

## Novel Insights

The paper's central novel insight is that the ELBO of a pre-trained fixed-length tokenizer can serve as an effective router for adaptive compression without requiring the expensive binary search over token lengths used by prior methods (ElasticTok). The theoretical contribution — proving that uniform routers are provably suboptimal while ELBO-proportional routers are near-optimal — provides a clean information-theoretic justification that was absent from prior heuristic approaches. The practical insight that likelihood-based token selection (preserving tokens with highest per-token ELBO) outperforms spatial alternatives (right-to-left masking, random masking) is well-supported by ablation in Table 3.

## Suggestions
- Reconcile the "20%" and "50%" claims: the body (Section 4.2) already correctly states "20% tokens saved" when matching Cosmos quality; the introduction (line 49) should be revised to match.
- Either provide empirical evidence for the "KL term proportional to reconstruction error" claim or remove it — using reconstruction error alone is justified pragmatically by the results but the theoretical justification is unsubstantiated.
- Elevate Table 2 from an ablation to a central result by adding analysis of the ELBO–log-likelihood gap and per-video allocation statistics.

## Calibration Anchors Retrieved

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Balancing Token Efficiency (VQ-VAE+Diffusion) | 2.50 | 1 | Much weaker — ad-hoc dual-token approach with no theory |
| Window-Based Hierarchical Dynamic Attention | 3.40 | 1 | Much weaker — incremental LIC improvement |
| TextEconomizer (lossy text compression) | 3.00 | 1 | Much weaker — different domain, limited contribution |
| DM-Codec (speech tokenization) | 3.00 | 1 | Much weaker — multimodal speech tokens |
| **ElasticTok (adaptive tokenization)** | **6.00** | **1 & 2** | **Direct predecessor; InfoTok clearly stronger in theory, efficiency, and empirical results** |
| How many tokens is an image worth? | 5.75 | 2 | Similar topic but image-only; InfoTok has stronger theory and video results |
| Image/Video Tokenization with BSQ | 5.75 | 2 | Different approach (BSQ quantization); complementary contribution |
| Improved Video VAE (IV-VAE) | 5.33 | 2 | Rejected paper; weaker contribution |
| From Pixels to Tokens (BPE tokenizer) | 6.00 | 1 | Different approach; comparable quality level |
| **LARP (learned AR prior for video tokenization)** | **7.50** | **2** | **Broader scope (AR generation); InfoTok has stronger theory but narrower focus** |
| On the Role of Discrete Tokenization | 7.00 | 2 | Different focus (theoretical analysis of discrete tokens in SSL) |
| MotionAura (discrete diffusion video) | 7.33 | 2 | Different approach; generation-focused |
| TokenFlow (video editing) | 7.00 | 2 | Different domain (editing, not tokenization) |
| Progressive Compression with UQ Diffusion | 8.00 | 1 | Much stronger — novel diffusion framework with universal quantization |
| Vision Transformers Need Registers | 8.00 | 1 | Field-transforming; much stronger |

**Round-1 bracket**: Between 5.5 and 7.5. InfoTok clearly surpasses ElasticTok (6.00) in both theory and practice, and is more focused than the 7.50 anchors.

**Round-2 narrowing**: Between 6.5 and 7.5. InfoTok sits between ElasticTok (6.00, direct baseline it improves upon) and LARP (7.50, broader scope with generation). InfoTok has stronger theoretical grounding than LARP but narrower scope (reconstruction only).

**Final score reasoning**: InfoTok is clearly stronger than ElasticTok (6.00) — it proves ElasticTok's approach is suboptimal, achieves significantly better results, and does so more efficiently. It is comparable to the 7.00 anchors in contribution quality. The inconsistent claims (20% vs 50%) and the minor theoretical overstatement prevent a higher score, but the overall contribution — principled theory, validated method, strong empirical results, and practical efficiency gains — warrants a score of 7.0.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>