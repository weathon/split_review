Now I have all the calibration I need. Let me write the final review.

---

## Summary

AdaSVD proposes two complementary techniques for SVD-based LLM compression: (1) adaComp, which compensates for SVD truncation errors by alternately updating truncated U and V^T matrices using Moore-Penrose pseudoinverse, and (2) adaCR, which assigns layer-specific compression ratios based on cosine similarity between layer input and output. Extensive experiments on 4 LLMs and 8 benchmarks demonstrate consistent improvements over SVD-LLM, with particularly strong gains at high compression ratios (e.g., 44% perplexity reduction at 60% compression on LLaMA2-7B).

## Strengths

- **Substantial and consistent improvements over SVD-LLM at high compression ratios**: Table 1 shows that at 60% compression on LLaMA2-7B, AdaSVD achieves WikiText-2 PPL of 50.33 vs SVD-LLM's 89.90 (44% reduction) and C4 PPL of 239.18 vs 561.00 (57% reduction). These margins grow with compression ratio, precisely where prior SVD methods struggle most.

- **Well-motivated numerical stability solution**: The paper identifies that naive matrix inverse updates (Equations 6-7) produce unstable, fluctuating compression errors, and resolves this via LSE reformulation solved with Moore-Penrose pseudoinverse (Equations 8-13). Figure 3(a) provides clear empirical evidence of smooth convergence for the pseudoinverse approach versus oscillation for the naive approach.

- **Thorough ablation studies**: Table 3 provides four independent ablation tables isolating adaComp (3a), adaCR (3b), iteration count (3c), and minimum retention ratio (3d). This allows clear attribution of performance gains to each component across three compression ratios.

- **Generalizability across model families and VLMs**: Evaluated on LLaMA2-7B, OPT-6.7B, Vicuna-7B, and Mistral-7B (Table 2), plus LLaVA-7B for image captioning (Figure 5). AdaSVD consistently outperforms baselines across architectures, and the paper notes that FWSVD and ASVD fail at 60% compression on some models while AdaSVD remains stable (Section 4.2, line 307).

- **Orthogonality with quantization validated**: Table 4 shows AdaSVD+GPTQ-INT4 consistently outperforms SVD-LLM+GPTQ-INT4 across all compression ratios (40%–80%), demonstrating practical composability with other compression techniques.

- **Practical stack-of-batch strategy**: Addresses a genuine memory bottleneck (fitting even 32 calibration samples on an 80GB GPU is challenging, line 177) with a simple, memory-efficient approach (Equations 14-15, Figure 3b).

## Weaknesses

### Fatal

None

### Major

- **Paper misrepresents its own iteration ablation data** — Table 3c shows that 1 iteration of adaComp is optimal at every compression ratio tested (40%: 14.76, 50%: 25.58, 60%: 50.33), with more iterations consistently degrading perplexity. Yet Section 4.3 states: *"In contrast, under higher compression ratios, additional iterations lead to performance improvements."* At 60% CR, going from 1 to 3 iterations increases PPL by 27% (50.33→64.12). The only partial support is 3→15 iterations at 60% (64.12→62.34), which is a marginal recovery but still leaves 15 iterations far worse than 1 iteration (62.34 vs 50.33). The framing of adaComp as an iterative convergence procedure (Equation 16, the update sequence over τ iterations) is misleading when the method effectively works best as a single-step correction. This claim-evidence mismatch should be corrected to honestly reflect that 1 iteration is consistently sufficient.

- **No runtime or memory analysis** — For a compression paper targeting resource-constrained deployment, the paper reports no inference latency, model size in MB, peak memory usage, or wall-clock time for the compensation step. The paper claims AdaSVD "significantly reduces memory requirements" (abstract) but never quantifies this. Without these numbers, it is impossible to assess the practical tradeoff between AdaSVD's perplexity gains and their cost. This gap was also flagged by reviewers of the ASVD baseline (score 6.25, rejected).

### Minor

- **adaCR alone can hurt performance at 50% compression** — Table 3a shows that at 50% CR, AdaSVD without adaComp (i.e., using adaCR for ratio assignment but no compensation) yields WikiText-2 PPL of 30.00, worse than SVD-LLM's 27.19. Meanwhile Table 3b shows AdaSVD with constant CR (no adaCR) achieves 27.33 at 50%. This means adaCR without compensation actively degrades quality at this operating point, while the full method (with compensation) achieves 25.58. The two components interact non-trivially, and the paper does not acknowledge this fragility or analyze why the importance-based allocation fails without compensation at certain compression ratios.

- **MMLU evaluation appears anomalous** — LLaMA2-7B's original MMLU accuracy is reported as 7.34% (Table 1), well below random chance of 25% for 4-choice questions. Compressed models score 22–27%, which is actually *higher* than the "original" model, suggesting either an evaluation setup issue or a non-standard MMLU variant. If this is a known issue with the evaluation protocol, it should be disclosed; otherwise the MMLU column is misleading.

- **Cosine similarity as importance metric lacks theoretical or empirical justification** — The paper uses cosine similarity between layer input and output to define importance (Equation 17), acknowledging "for simplicity" (line 226). No theoretical argument is given for why this metric captures compression-relevant importance (e.g., why identity-preserving layers should retain more parameters). No alternative metrics are compared. The empirical importance patterns in Figure 4 are interesting but don't establish that cosine similarity tracks what it should (e.g., per-layer reconstruction error or downstream degradation).

## Nice-to-Haves

- Reframe adaComp as a single-step post-truncation correction rather than an iterative convergence procedure, given that 1 iteration is consistently optimal.
- Compare against quantization-only methods (GPTQ, AWQ) at similar compression ratios to clarify when SVD-based compression is preferable.
- Analyze the information loss from the stack-of-batch averaging strategy.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Dimensional inconsistency in Equation 13**: The harsh critic flagged potential dimensional mismatch. However, this appears to be a notational convention issue (V_k^σ dimensions vary depending on whether Σ^{1/2} is absorbed from left or right, and the paper may implicitly use the transpose convention). The underlying optimization derivation is sound. Not worth flagging.
- **Comparison scope narrow (only SVD baselines)**: The paper explicitly scopes itself to SVD-based compression methods and positions against SOTA SVD methods. Comparing against quantization-only methods is mentioned as a nice-to-have.
- **Equation 13 potential parsing issue**: Flagged by harsh critic but appears to be a parser artifact given the mathematical context.

## Novel Insights

The paper's most practically valuable finding — somewhat obscured by the paper's own framing — is that a single-step Moore-Penrose pseudoinverse correction after SVD truncation provides large perplexity gains at minimal computational cost. This is a simple, effective post-processing step that could be applied to any SVD-based compression pipeline. The empirical observation that the first transformer layer consistently carries the most importance across all tested LLMs (Figure 4) is also noteworthy and warrants further investigation.

## Suggestions

- **Fix the iteration claims**: The text in Section 4.3 should state that 1 iteration is consistently optimal and explain why, rather than claiming more iterations help at high compression ratios.
- **Add wall-clock runtime and peak memory measurements**: Compare AdaSVD, SVD-LLM, and the original model in terms of inference latency, model size in MB, and peak GPU memory.
- **Acknowledge and investigate the 50% CR adaCR failure mode**: Explain why the importance-based allocation can hurt without compensation at certain operating points.
- **Verify and fix the MMLU evaluation**: 7.34% for LLaMA2-7B is implausible and needs to be corrected or explained.

## Reporting — Anchor Papers

| Path | Avg Human Score | Round | Comparison |
|------|----------------|-------|------------|
| 3KEwJGYNzH (AutoTrunc) | 4.00 | R1 | Similar topic (SVD truncation for LLMs); AdaSVD has broader eval and clearer method |
| ho7ZUS1z8A (MoE-SVD) | 5.00 | R1 | SVD for MoE; AdaSVD is more polished with better ablations |
| FA3iYp1y6z (LRC) | 5.00 | R1 | Low-rank correction; AdaSVD has clearer standalone contribution |
| nMbWsXPUVL (LLM-Codebook) | 4.75 | R2 | Extreme compression; different approach but similar level of incremental contribution |
| vzvCaYFTLq (Sapling) | 4.75 | R2 | Layer dropping; similar empirical breadth |
| YLTWwEjkdx (What Matters) | 5.50 | R1 | Attention pruning; similar breadth and contribution level |
| B8aHIDSi7E (Free Bits) | 6.00 | R2 | Novel compression insight; AdaSVD has stronger practical impact |
| HyPofygOCT (ASVD) | 6.25 | R1 | **The exact baseline**; AdaSVD improves on it with broader eval but adds claim-evidence issues |
| DwiwOcK1B7 (DSF) | 6.33 | R2 | Double sparse factorization; similar contribution level, was accepted |
| gp32jvUquq (Basis Sharing) | 6.50 | R1 | Cross-layer SVD; has throughput analysis AdaSVD lacks, was accepted |
| B9klVS7Ddk (Compressing LLMs: Truth) | 6.75 | R2 | Evaluation/benchmark paper; different type, accepted |

**Round 1 bracket: 5.0–6.5.** AdaSVD is clearly above AutoTrunc (4.0), MoE-SVD (5.0), and LRC (5.0). It's comparable to ASVD (6.25, the baseline, rejected) with broader evaluation but with the added issue of misleading iteration claims. Basis Sharing (6.50, accepted) and DSF (6.33, accepted) are slightly above AdaSVD, partly because they include throughput/runtime analysis. The paper sits at **5.5** — genuine contributions with real improvements, but the claim-evidence mismatch on iterations and missing practical runtime/memory analysis are meaningful concerns that would need to be addressed.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>