Now I have solid comparisons. Let me synthesize everything.

**Round 1 bracket:** INFOToK sits above ElasticTok (6.00) and AVT (5.75), and below the 7.5+ tier. Plausible range: **6.0–7.5**.

**Round 2 narrowing:** The "Role of Discrete Tokenization" paper (7.00) has theoretical contributions but limited experiments. NeuroQuant (7.20) has strong results but missing baselines and misleading claims. INFOToK has stronger empirical results than the 7.00 paper but has a real reproducibility gap (per-token ELBO unexplained). Compared to NeuroQuant, INFOToK's weaknesses are different in kind — a mechanism left unspecified vs. baselines omitted — but both are real.

INFOToK lands at **6.5**: clearly stronger than ElasticTok (theory + results + efficiency), roughly comparable to the Discrete Tokenization paper (7.00) in overall quality, but held back by the unexplained per-token ELBO decomposition that affects reproducibility of a core component.

---

## Summary

INFOToK introduces an adaptive video tokenizer grounded in Shannon's source coding theorem. It uses an ELBO-based router to allocate tokens proportional to each video's estimated information complexity, paired with a transformer-based adaptive compressor that selects which tokens to retain based on per-token information content. Empirical results on TokenBench and DAVIS show substantial improvements over ElasticTok (the main adaptive baseline) — e.g., FVD reduced by 40–60% at matched compression — while requiring only 1 additional decoder forward pass vs. ElasticTok's 11-pass binary search. The ELBO router is validated as near-optimal against an exhaustive per-dataset search strategy.

## Strengths

- **Strong, consistent empirical margin over ElasticTok (Table 1, Figure 4).** At matched BPP_16 levels (0.81, 0.56), INFOToK reduces FVD by 40–60% and LPIPS by 25–40% relative to ElasticTok on both TokenBench and DAVIS. INFOToK at BPP_16=0.56 matches or exceeds ElasticTok at 0.81, demonstrating ~30% additional compression savings. Figure 4 shows INFOToK-Flex dominates ElasticTok's full Pareto frontier across PSNR, LPIPS, and FVD.

- **ELBO-based router is near-indistinguishable from exhaustive optimal search (Table 2).** The "Optimal" strategy that brute-forces per-video token allocation via per-dataset optimization achieves nearly identical metrics to INFOToK-Flex (e.g., PSNR 29.86 vs. 29.92, FVD 54 vs. 54 at BPP_16=0.81 on TokenBench). This directly validates the central theoretical claim that ELBO is a sufficient proxy for −log p(x) in routing decisions.

- **11× inference efficiency gain (Figure 4g).** ElasticTok requires an 11-pass binary search per 4096-token block to determine token lengths; INFOToK needs only 1 additional decoder forward pass. This is a concrete practical advantage for deployment.

- **Rigorous theoretical scaffolding (Theorems 2.1, 2.2, 3.1).** The paper builds a coherent chain: restates the Shannon source coding lower bound (Thm 2.1), proves uniform data-agnostic routers can be arbitrarily suboptimal (Thm 2.2), and proves the ELBO-based router achieves near-optimal expected length (Thm 3.1). This grounding distinguishes INFOToK from prior heuristic adaptive methods.

- **Mechanism portability across architectures (Table 3 Right).** The INFOToK adaptive mechanism (ELBO router + compressor) outperforms ElasticTok's uniform-router mechanism on both the Cosmos CNN backbone and a pure ViT backbone (e.g., on ViT: PSNR 28.64 vs. 27.21, FVD 114 vs. 198), suggesting the approach generalizes beyond a specific encoder/decoder.

- **ELBO-based compressor design matters empirically (Table 3 Left).** Masking tokens by per-token ELBO outperforms right-to-left masking (PSNR 29.30 vs. 27.43; FVD 71 vs. 137) and a spatially-dispersed "Jump" strategy, validating that information-guided selection is superior to heuristic masking.

## Weaknesses

### Fatal
None.

### Major

- **Per-token ELBO decomposition is never explained (Section 3.2, line 162).** The adaptive compressor selects which tokens to keep by ranking them according to "per-token log-likelihood, which is also approximated via the ELBO values." But the ELBO is defined in Eq. (3) as a single scalar for the entire video — a sum of reconstruction and KL terms, neither of which trivially decomposes into per-token contributions. The paper claims this incurs no extra network evaluation "since the log-likelihood term has been computed in the router," but the router computes only one scalar ELBO per video (line 138, Eq. 4). How this scalar is decomposed into N per-token scores is unspecified. This is not a minor implementation detail: the compressor design depends on it, and Table 3 (Left) attributes substantial performance gains to this selection strategy. Without this specification, the method as described is not fully reproducible.

- **Theorem 2.2 addresses a simplified version of the baseline, not the baseline itself (Section 2.3).** The theorem assumes a router that samples sequence length uniformly from {1,…,N} and proves this can be arbitrarily suboptimal. But ElasticTok uses nested dropout — each token is independently masked with some probability during training, not uniform length sampling. The paper acknowledges simplifying the inference stage (line 108: "we simplify their inference stage") but then uses the theorem to claim ElasticTok's training is "biased" (line 28). The theorem's premise does not match ElasticTok's actual training mechanism. The theoretical critique would be more informative if it addressed nested dropout directly or if the claim were narrowed to data-agnostic routers as a class rather than positioned as a direct critique of ElasticTok.

### Minor

- **KL-term proportionality claim is unverified (line 156).** The paper states that in practice the KL term is dropped using only reconstruction error, claiming "the KL term is approximately proportional to the reconstruction error." No empirical evidence is provided for this proportionality. Theorems 2.1 and 3.1 rely on ELBO being a valid lower bound, and while the practical success (Table 2) mitigates this concern, the theory-practice link is weakened.

- **Train/test split not stated in the main experimental section (Section 4.1).** The paper names the datasets (TokenBench, DAVIS) but does not specify how they are partitioned for training vs. evaluation, which matters for assessing generalization.

### Trivial

- **"Approximately 50% tokens" overstates the saving (line 38).** Cosmos-DV uses BPP_16=1.00 and INFOToK achieves 0.56, which is a ~44% reduction. "Approximately 50%" rounds up somewhat generously.

## Nice-to-Haves

- Per-video variance in reconstruction quality would directly support the core motivation that adaptive methods reduce quality variation across videos of differing complexity.
- A scatter plot of N_x vs. reconstruction error per video would visually demonstrate whether the router correctly identifies hard cases.
- Ablation on the number of transformer layers in the adaptive compressor to illuminate the cost-quality tradeoff.
- Empirically verify the KL/reconstruction-error proportionality claim with a correlation analysis.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Different codebook sizes across baselines make cross-baseline comparisons less informative** — BPP_16 already accounts for codebook size via the log(C) term, so this does not create an unfair comparison. The harsh critic acknowledged this. Removed.
- **5% mask overhead impact on BPP_16 should be more prominently documented** — the paper explicitly documents this at lines 162-163 and includes the 1/16 term in the BPP calculation (line 199: "β can be computed as N_max · (BPP_16 − 1/16), where 1/16 is the cost of binary mask"). Already addressed in the paper. Removed.

## Novel Insights

The paper's most interesting empirical finding is that a single scalar ELBO — computed by the fixed-length tokenizer without the adaptive compressor — serves as an almost-perfect routing signal, matching exhaustive per-video search (Table 2). This is not obvious a priori: one might expect that introducing the adaptive compressor would change reconstruction quality rankings enough to break the correlation. The empirical result suggests that information complexity as estimated by reconstruction difficulty under a fixed-rate codec transfers well to variable-rate coding, which has implications beyond video tokenization.

## Suggestions

- Specify the per-token ELBO decomposition mechanism explicitly. If it works by attributing pixel-wise reconstruction error back to token positions through the decoder architecture, describe that mapping. If it uses token ablation, state the cost. This is essential for reproducibility.
- Either extend Theorem 2.2 to nested dropout, or narrow the framing so the theorem critiques uniform-length routers as a class rather than ElasticTok specifically. Currently the paper's strongest theoretical critique of the baseline applies to a mechanism ElasticTok does not actually use.
- Report training dataset splits in the main experimental section.

---

**Calibration anchors considered:**

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| ElasticTok (tFV5GrWOGm) | 6.00 | R1 | Direct baseline; INFOToK has theory + better results + efficiency |
| AVT / "How many tokens" (mb2ryuZ3wz) | 5.75 | R1 | Image variable-length tokens; INFOToK stronger theory and results |
| Discrete Tokenization in MIM (WNLAkjUm19) | 7.00 | R2 | Good theory, limited experiments; INFOToK stronger empirically but has reproducibility gap |
| NeuroQuant (44cMlQSreK) | 7.20 | R2 | Strong PTQ method, some missing baselines; INFOToK comparable quality but different weakness profile |

Round 1 bracket: 6.0–7.5. Round 2 narrowed to: INFOToK sits above ElasticTok (6.00) and slightly below or at the Discrete Tokenization paper (7.00) due to the unexplained per-token ELBO mechanism. Final score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>