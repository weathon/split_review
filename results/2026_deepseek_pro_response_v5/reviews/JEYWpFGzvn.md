Now I have a clear picture from the calibration. Let me compile the final review.

**Round 1 Bracket**: Based on comparison across all bands, INFOToK sits clearly above the weak-reject / borderline band (2.5–4.5) and well above the middle band anchored by ElasticTok (6.00). It is below the strong-accept band (7.0+), where papers have either broader scope (MotionAura 7.33, TokenFlow 7.00) or flawless theoretical contributions (Role of Discrete Tokenization 7.00). The bracket is approximately **6.0–7.0**.

**Round 2 Narrowing**: Within (5.5, 6.5), INFOToK is better than ElasticTok (6.00) — it addresses ElasticTok's key weaknesses (inefficient binary search, naive R2L masking, no optimality analysis) and delivers 40–60% FVD reduction with 11× inference efficiency. Within (6.5, 7.5), papers like TokenFlow and MotionAura have broader, more mature contributions. INFOToK's Theorem 3.1 issue and presentation gaps place it below 7.0. **Final score: 6.5.**

---

## Summary
This paper introduces INFOToK, an adaptive discrete video tokenizer that uses an ELBO-based router to allocate tokens proportionally to each video's information complexity, plus a transformer-based adaptive compressor that masks low-likelihood tokens. The method builds on prior adaptive tokenizers (particularly ElasticTok) but replaces their data-agnostic uniform routing with a theoretically motivated, information-theoretic approach. Empirical results show substantial improvements over ElasticTok at matched compression rates, near-optimal performance compared to exhaustive search (Table 2), and 11× fewer inference-time network evaluations.

## Strengths
- **Theorem 2.2 formally proves suboptimality of uniform routers**: Shows that for any κ > 1 there exist distributions where uniform-routed adaptive tokenizers produce κ times the optimal expected token length. The four-data counterexample (lines 114–118) with probabilities {½, ¼, ⅛, ⅛} makes the failure mode concrete and specific.
- **Substantial empirical margin over ElasticTok**: Table 1 shows FVD reduced by 40–60% at matched BPP₁₆ (e.g., TokenBench at BPP₁₆=0.56: FVD 70–71 vs. 194; DAVIS at BPP₁₆=0.81: FVD 408–441 vs. 754), with PSNR gains of 1.0–2.0 dB. Figure 4 confirms advantage across the full compression-rate range.
- **ELBO router validated as near-optimal via exhaustive search**: Table 2 compares INFOToK-Flex against "Optimal" (brute-force evaluation of all compression levels with constrained optimization over the dataset). The gap is negligible (e.g., TokenBench BPP₁₆=0.81: PSNR 29.86 vs. 29.92; FVD 54 vs. 54), confirming the ELBO approximation costs essentially nothing in practice.
- **11× inference efficiency advantage**: Figure 4g quantifies that ElasticTok requires 11 additional network forward evaluations for binary search, while INFOToK needs exactly 1. This makes adaptive tokenization practically viable.
- **Architecture-agnostic design validated**: Table 3 (Right) demonstrates the ELBO router + compressor outperforms ElasticTok's uniform router on both Cosmos CNN and pure ViT backbones (Cosmos: PSNR 29.30 vs. 27.35; ViT: PSNR 28.64 vs. 27.21).
- **Single-model multi-rate capability**: INFOToK-Flex, trained with an ensemble of β values, performs on par with individually trained rate-specific models (Figure 4), eliminating the need for separate models per compression budget.

## Weaknesses

### Fatal
None.

### Major
- **Log-base mismatch in Theorem 3.1 undermines the claimed optimality guarantee**: The inequality (line 148) states $\mathbb{E}[N_{\mathbf{x}}] \leq H_C(\mathbb{D}) + \beta - \mathbb{E}[-\log p(\mathbf{x})]$, where $H_C(\mathbb{D}) = \mathbb{E}[-\log_C p(\mathbf{x})]$ is in base-$C$ log units while $\beta$ and $\mathbb{E}[-\log p(\mathbf{x})]$ are in natural-log units. With the router from eq. (4), $\mathbb{E}[N_{\mathbf{x}}] = \beta$, reducing to $\beta \leq \beta - \mathbb{E}[-\log p(\mathbf{x})] \cdot (1 - 1/\log(C))$. For $C = 2^{16}$ this requires $\mathbb{E}[-\log p(\mathbf{x})] \leq 0$, satisfied only by a degenerate distribution. Natural-log and base-$C$ quantities are incommensurable — the theorem as written does not hold. The paper further compounds this on line 128 by stating that optimality requires $N_{\mathbf{x}} = -\log p(\mathbf{x})$ (natural log) when the Source Coding Theorem actually requires $N_{\mathbf{x}} = -\log_C p(\mathbf{x})$. Since the paper's primary differentiator from prior heuristic methods is its "principled information-theoretic" framing, and this theorem is the key bridge between the router design and the Shannon optimality claim, this is a significant issue. The empirical method still functions (β absorbs the log-base constant in practice, and Table 2 validates the approach independently), but the theoretical guarantee as stated is incorrect. This requires either a corrected theorem or recalibrated optimality claims.

### Minor
- **Continuous-to-integer token count mapping is unspecified**: Equation (4) produces a continuous value via the delta distribution, but $N_{\mathbf{x}}$ must be an integer. The paper never describes rounding, flooring, or clipping. This is a reproducibility gap — different discretization strategies could produce meaningfully different allocations at low compression rates.
- **Per-token ELBO decomposition mechanism is not explained**: Section 3.2 states the compressor preserves the top $N_{\mathbf{x}}$ tokens "according to their corresponding per-token log-likelihood" and claims this "does not incur extra network evaluation since the log-likelihood term has been computed in the router" (line 162). But the router computes a single scalar ELBO per video (eq. 3–4). How this scalar decomposes into per-token scores is never described, leaving a key component of the adaptive compressor opaque.
- **Cosmos-DV comparison fairness needs clarification**: The paper says the Cosmos encoder/decoder are used to "initialize" (line 164) INFOToK's components. It is not stated whether these are frozen or fine-tuned during INFOToK training, nor whether the Cosmos-DV baseline was re-evaluated under the same data processing pipeline. This affects interpretation of Table 1 comparisons.
- **Lossless-to-lossy bridge is assumed rather than argued**: Section 2 invokes Shannon's Source Coding Theorem (a lossless compression result) to motivate adaptive lossy video tokenization. The connection between lossless information-theoretic bounds and lossy reconstruction quality is not examined. This does not invalidate the method — the motivation is reasonable — but it weakens the theoretical narrative that is central to the paper's framing.

### Trivial
- DAVIS dataset is cited as "Caelli et al. (2019)" (line 172) rather than the standard attribution (Perazzi et al., 2016 / Pont-Tuset et al., 2017).

## Nice-to-Haves
- No error bars, confidence intervals, or standard deviations are reported for any metric. While single-run evaluation is standard in large-scale video tokenization benchmarks, variance on the smaller DAVIS dataset could be informative.
- The binary mask overhead is claimed as "approximately 5%" (line 162); the actual overhead varies with compression rate, and reporting the range would be more precise.
- A sensitivity analysis of the router to the EMA decay rate for $\mathbb{E}[\text{ELBO}(\mathbf{x})]$ and to the β discretization choices would strengthen confidence in the method's robustness.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"Theorem 2.2 is stated without proof in the main text"** — REMOVED per hard rule: the proof is deferred to Appendix B, and appendix stripping means we cannot verify its presence or absence. Providing theorem statements with proof sketches in the main text and full proofs in the appendix is standard practice.
- **"2.3× compression rates phrasing is ambiguous enough to mislead"** — REMOVED: context resolves the ambiguity. Figure 4 and the surrounding text (lines 221–222) make clear this means ElasticTok needs 2.3× higher BPP to match INFOToK's quality.
- **"ELBO router uses non-adaptive tokenizer error, creating systematic bias"** — REMOVED as a standalone weakness: the paper is transparent about this (lines 138–139: "we first encode x and decode back to \tilde{x} without using the adaptive compressor") and Table 2 empirically validates that the approximation gap is negligible.

## Novel Insights
The combination of Table 2 (near-optimal routing) and Figure 4g (11× inference efficiency) reveals a genuinely novel finding: an ELBO-based router, requiring only one extra decoder pass, achieves routing decisions indistinguishable from exhaustive brute-force search while being an order of magnitude cheaper than the binary search used in ElasticTok. This means the practical bottleneck in adaptive tokenization — selecting the right compression rate per video — can be solved with a simple, theoretically motivated proxy rather than expensive search. This finding is independently convincing even aside from the theoretical claims.

## Suggestions
- Fix or reframe Theorem 3.1: either redefine the router using base-$C$ log (absorbing $\log(C)$ into β) or recalibrate the optimality claim to what the experiments actually demonstrate — that the ELBO router empirically approaches optimal allocation (Table 2) without claiming Shannon-theoretic guarantees that don't hold as stated. Correct line 128 to state $N_{\mathbf{x}} = -\log_C p(\mathbf{x})$ rather than $N_{\mathbf{x}} = -\log p(\mathbf{x})$.
- Specify the per-token ELBO decomposition mechanism explicitly, since it is essential to reproducing the adaptive compressor.
- State how the continuous router output is discretized to an integer token count.
- Clarify the training status of the Cosmos encoder/decoder (frozen vs. fine-tuned) and whether baseline comparisons use the same data pipeline.

## Calibration Anchors
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/MI0UiWeqOl.md` (avg 2.33, Round 1): Strong-reject anchor — unrelated topic, far below INFOToK.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/aQ7qYnY2nF.md` (avg 4.00, Round 1): Weak anchor — macro-block rate control; INFOToK has stronger theory and cleaner results.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/gZnBI7WS1K.md` (avg 3.50, Round 1): Weak anchor — LLaVA-PruMerge; different domain, INFOToK is stronger.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/tFV5GrWOGm.md` (avg 6.00, Rounds 1&2): **ElasticTok** — direct predecessor. INFOToK is clearly better in results, theory, and efficiency.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/yGnsH3gQ6U.md` (avg 5.75, Rounds 1&2): **BSQ-ViT** — quantization-focused tokenizer; INFOToK has comparable quality with clearer ablation story.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/mb2ryuZ3wz.md` (avg 5.75, Rounds 1&2): **ALIT-like** — image-only adaptive tokenizer; INFOToK handles video (harder), has stronger baselines.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/FlvtjAB0gl.md` (avg 6.25, Round 1): **LaVIT** — broader VLM framework; INFOToK is more focused with deeper analysis of its specific contribution.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/WNLAkjUm19.md` (avg 7.00, Rounds 1&2): **Role of Discrete Tokenization** — theoretical paper with correct analysis; INFOToK's theorem issue places it below this.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/bW9fGYo44s.md` (avg 7.33, Rounds 1&2): **MotionAura** — broader multi-contribution paper; INFOToK is narrower in scope.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/lKK50q2MtV.md` (avg 7.00, Round 2): **TokenFlow** — video editing; unrelated domain, higher score reflects mature contribution.

INFOToK improves substantially on ElasticTok (6.00) in every dimension while having a genuine but fixable theoretical issue. It does not reach the 7.0+ tier where papers have either flawless theory or broader, multi-contribution scope. Final score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>