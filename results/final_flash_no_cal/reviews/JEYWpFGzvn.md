Now I have a thorough understanding of the paper. Let me synthesize the final consolidated review.

---

## Summary

This paper introduces InfoTok, an adaptive discrete video tokenizer that uses an ELBO-based router to dynamically determine per-video token lengths, coupled with a transformer-based adaptive compressor that discards low-information tokens. Grounded in Shannon's source coding theorem, the paper proves that data-agnostic routing (as used by prior methods like ElasticTok) can be arbitrarily suboptimal in expected token length, and that the proposed ELBO-based routing achieves near-optimal compression. Empirically, InfoTok matches fixed-length Cosmos-DV quality with ~20% fewer tokens and significantly outperforms ElasticTok at equivalent compression rates while requiring only 1 additional NFE (vs. 11 for ElasticTok's binary search).

## Strengths

- **Principled theoretical analysis of uniform routing suboptimality.** Theorem 2.2 proves that a data-agnostic uniform router (as employed by ElasticTok) can force the expected token length to be arbitrarily larger than the Shannon lower bound, establishing a concrete flaw in prior heuristic approaches.

- **Near-optimal ELBO-based router validated against exhaustive search.** Theorem 3.1 provides a theoretical guarantee that the ELBO-based router (Eq. 4) approaches optimality, and Table 2 confirms this empirically — InfoTok-Flex performs within <0.1 PSNR of an exhaustive optimal search over all token lengths across two datasets and three compression levels.

- **Clear and substantial improvement over ElasticTok.** At BPP₁₆=0.56, InfoTok-Flex surpasses ElasticTok by +1.96 PSNR on TokenBench (29.30 vs. 27.34) and reduces FVD by 64% (71 vs. 194). Remarkably, InfoTok at BPP₁₆=0.56 even outperforms ElasticTok at BPP₁₆=0.81 (29.30 vs. 28.26 PSNR), demonstrating a better rate-distortion trade-off across the board (Table 1, Figure 4).

- **Inference efficiency advantage.** InfoTok requires only one additional decoder forward pass to compute the ELBO for length selection, versus ElasticTok's 11 forward passes via binary search — an 11× reduction in overhead (Figure 4g).

- **Multi-rate single-model capability.** InfoTok-Flex, trained with a set of β values simultaneously, performs nearly as well as individually trained InfoTok models (e.g., PSNR 29.86 vs. 30.08 at BPP₁₆=0.81), enabling practical deployment at varying compression budgets without retraining.

- **Architecture-agnostic effectiveness.** The InfoTok adaptive mechanism consistently outperforms ElasticTok's uniform mechanism on two different backbone architectures (Cosmos and pure Vision Transformer), with PSNR improvements of 1.95 and 1.43 respectively (Table 3 Right).

## Weaknesses

### Fatal
None.

### Major

- **Per-token ELBO computation is not defined.** The adaptive compressor's core operation (Section 3.2) is to preserve the top N_x tokens based on "per-token log-likelihood, which is also approximated via the ELBO values" and to compute a mask where "N_x tokens with the lowest ELBO values are 1." However, ELBO(x) is defined in Eq. 3 as a *video-level* scalar — the paper never explains how it is decomposed into per-token values. Whether this is the reconstruction MSE contributed by each latent token's spatial region, a norm-based heuristic, or something else is left unspecified. Since the compressor's masking decisions depend entirely on these per-token scores, the central operation of the adaptive compressor is underspecified. This is a reproducibility-critical gap that undermines the "information-theoretic" grounding claim for the token-selection step and must be clarified.

### Minor

- **Inconsistent compression-rate claims across abstract and introduction.** The Introduction claims "save approximately 50% tokens without loss of reconstruction quality compared to state-of-the-art fixed-length tokenizers." The Abstract claims "saving 20% tokens without influence on performance." Table 1 supports the ~20% figure (BPP₁₆=0.81 vs. Cosmos-DV at 1.00, with comparable PSNR: 30.08 vs. 30.01), but the 44% token reduction (BPP₁₆=0.56) shows clear quality degradation (PSNR drops from 30.01 to 29.27, SSIM from 0.885 to 0.854). The Introduction's stronger claim is not supported by the data and should be corrected for consistency.

- **Theorem 2.2 scope could be framed more precisely.** The theorem states that there exists a data distribution for which the uniform router leads to arbitrarily suboptimal expected token length (an existential proof). The paper's high-level language ("proves that existing tokenizers...are biased" in the Abstract and "prove that existing data-agnostic training methods are suboptimal" in Section 2) reads as a universal statement, when the actual result is an existence proof for a *particular* constructed distribution. The theorem itself is correctly stated; the surrounding exposition could better distinguish existential from universal claims.

- **ElasticTok comparison details are somewhat underspecified.** The paper states that "All results below are reported on our processed datasets for fair comparisons" and that ElasticTok's loss thresholds were "aligned" to match target BPP values. However, the procedure for calibrating ElasticTok's continuous loss threshold to the discrete average BPP₁₆ values of 0.81 and 0.56 is not described, nor is any variance in ElasticTok's per-sample BPP reported. While not a fatal omission, this limits the reader's ability to assess whether the comparison is fully rate-matched.

### Trivial

- **Mask semantics unclear in compressor description.** Section 3.2 states the compressor "preserve[s] the top N_x tokens" but then writes the mask such that "N_x tokens with the lowest ELBO values are 1" — the relationship between mask bit value and token retention (whether 1 means "keep" or "discard") is ambiguous and should be clarified.

## Nice-to-Haves

- The ablation comparing per-token ELBO masking against R2L and Jump masking (Table 3 Left) convincingly shows the ELBO-based criterion is best, but the comparison would be even stronger if R2L and Jump were also tested at the same BPP₁₆ values to verify the advantage holds across multiple operating points, not just at 0.56.

- The wall-clock inference latency comparison (deferred to Appendix D per the paper) would be a useful addition to the main paper alongside the NFE bar chart.

## Removed Points

These points were raised by reviewers but are removed from the main assessment for the reasons below, and should be treated with caution:

- **"NFE comparison mixes definitions because InfoTok's total compute is higher"** (Harsh Critic). The paper's Figure 4g clearly labels the metric as "Additional NFEs / Standard NFEs" — it measures the *overhead* of determining token length, not total compute. InfoTok's compressor module adds compute during the standard forward pass, but that is part of the baseline architecture for both methods. The comparison is correctly scoped.

- **"Missing training details (learning rate, batch size, etc.)"** (Harsh Critic). The paper states "For more details about training, inference, and resource consumption, please refer to Appendix C." Per review guidelines, missing appendix content is not a valid weakness — the appendix exists in the original submission and was stripped by the parser.

- **"Dataset descriptions are insufficient"** (Harsh Critic). TokenBench and DAVIS are cited with references to their original publications. This is standard practice and sufficient for the purposes of this paper.

- **"The theorems do not directly prove practical fixed-length tokenizers are suboptimal"** (Harsh Critic). The theorems correctly establish existence of suboptimality under stated assumptions — this is standard in theoretical ML and provides a rigorous motivation. The empirical results (Table 1) provide the practical evidence. The theoretical framing is appropriate.

- **Strength Finder's generic strengths**: Generic statements such as "this paper addressed an important problem" were removed. Only evidenced, paper-specific strengths are retained.

## Novel Insights

The most novel synthesis emerging from the reviews is that InfoTok's contribution is best understood as a *two-level* information-theoretic mechanism: the router determines how many tokens a video needs (video-level ELBO), and the compressor decides *which* specific tokens to keep (per-token ELBO). The gap in defining the latter creates an asymmetry — the router is rigorously grounded (Theorem 3.1, validated by Table 2), but the compressor's token-selection criterion lacks a commensurate theoretical justification and empirical decomposition. Addressing this asymmetry (e.g., by proving that per-token reconstruction error is a valid ELBO decomposition under the decoder's factorized output distribution) would significantly strengthen the paper's information-theoretic narrative. The empirical results themselves are robust enough that even a simpler per-token criterion would still support the main claims.

## Suggestions

1. **Explicitly define the per-token ELBO computation.** If it is the reconstruction MSE contribution from each latent token's corresponding spatio-temporal region, state this clearly and justify why it approximates per-token log-likelihood. Provide the derivation or cite the relevant factorization property of the decoder.

2. **Correct the Introduction's "50% tokens" claim** to match the Abstract's supported "20% tokens" figure, or qualify it with the corresponding quality level.

3. **Clarify the ElasticTok alignment protocol** — describe how loss thresholds were calibrated to match the target average BPP₁₆ values, and report the standard deviation of ElasticTok's per-sample BPP₁₆ for the chosen thresholds.

4. **Clarify mask semantics** in the compressor description — explicitly state whether mask=1 indicates "keep" or "discard" to avoid ambiguity.

5. **Consider adding a brief analysis** of the relationship between per-token reconstruction error and per-token ELBO (or state that the reconstruction term alone is used, as suggested in Section 3.1).

## Score and Decision

This paper makes a solid contribution: it provides a principled information-theoretic framing for adaptive video tokenization, proves suboptimality of existing heuristic approaches, and demonstrates clear empirical improvements over the state-of-the-art adaptive baseline (ElasticTok) with substantial efficiency gains. The main weakness — an underspecified per-token ELBO computation — is significant for reproducibility but likely addressable in a rebuttal. The 50% vs. 20% inconsistency is a presentation issue that should be corrected. Overall, the core contributions are well-supported and the weaknesses do not invalidate the paper's results.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>