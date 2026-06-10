## Summary
This paper proposes RoPE++, an extension to Rotary Position Embeddings that re-incorporates the discarded imaginary component of the complex-valued attention score. The method derives imaginary attention (the negative imaginary part of RoPE's complex dot product), shows it has a sine-based characteristic curve that decays more slowly than cosine-based real attention, and offers two configurations: RoPE++_EC (equal cache, doubled heads, doubled W_o) and RoPE++_EH (equal heads, halved cache). Experiments at 376M and 776M scales on short- and long-context benchmarks show improvements over standard RoPE and other position embedding methods.

## Strengths
- **Clean mathematical insight with rigorous derivation (Eq. 2–4):** The observation that standard RoPE discards the imaginary component of its complex-valued attention is genuinely elegant. Equations 2-4 rigorously demonstrate that imaginary attention can be expressed in the same rotation/relative-position form as real attention, requiring only a −π/2 rotation of q_t while keeping k_s embeddings unchanged. This preserves RoPE's unified absolute–relative position-embedding format with minimal modification.

- **Characteristic curve analysis provides theoretical grounding (Eq. 5, §3.2):** Equation 5 derives the imaginary attention's characteristic curve as a sine integral function (Si(Δt)) and contrasts it with the cosine integral governing real attention. The argument that the sine integral "declines very slowly beyond a certain distance" provides a concrete, testable explanation for why imaginary attention captures longer-range dependencies.

- **RoPE++_EH delivers practical cache-efficiency gains (Tables 1–2, Fig. 4):** Table 1 shows RoPE++_EH achieves comparable short-context scores (42.5 vs 42.0 at 776M) and Table 2 shows RULER average (28.6 vs 27.4 at 776M) while halving KV cache and QKV parameters. Figure 4 validates memory and throughput improvements at inference, with the gap widening at longer contexts.

- **Gaussian noise ablation provides direct evidence for imaginary heads' role (§5.2, Fig. 5):** Adding noise with σ=1.0 to imaginary attention degrades RULER-4k performance by 5–8 points more than the same perturbation to real attention, confirming that imaginary heads play a more dominant role in long-context modeling.

- **Compatibility with existing long-context techniques (Table 3):** RoPE++ combined with Linear PI and YaRN consistently achieves the highest scores on RULER, BABILong, and short-context averages across both model sizes, demonstrating orthogonal gains.

- **Length extrapolation improvement with concrete mechanism (§3.4, Fig. 3):** The paper explains how imaginary attention exposes q/k dimensions to both positive and negative position embedding values during pre-training, reducing OOD behavior at longer contexts by achieving full positional value range training when context exceeds half the sinusoidal period.

## Weaknesses

### Fatal
None

### Major
- **EC variant's comparison is confounded by parameter count:** RoPE++_EC has a doubled output projection W_o (line 101: "W_o in RoPE++EC is double-sized") while sharing W_q, W_k, W_v. EC shows the most dramatic improvements (RULER avg 25.0 vs 18.8 at 376M, 29.4 vs 27.4 at 776M). No ablation compares EC against a standard RoPE model with similarly expanded W_o and doubled attention heads, making it impossible to disentangle whether gains stem from the imaginary information mechanism or from the additional capacity in the output projection. This undermines the headline EC results.

- **Sub-LLM scale only in main body:** The paper's title and motivation frame the contribution for "Long-Context LLMs," citing million-token-scale models (Llama, Qwen, etc.). Yet the main body only reports experiments at 376M and 776M parameter scales — scales no one would call "large language models." The paper references Appendix C for larger-scale analysis, but the main text does not substantiate the title's scope. At these small scales, attention dynamics and the relative importance of architectural choices can behave differently than at 7B+ scale.

### Minor
- **No variance reporting:** All results in Tables 1–3 are single-run numbers with no reported variance. Short-context differences are often small (e.g., 376M short avg: 39.7–41.0, a 1.3-point spread), making it difficult to assess whether some improvements are real or noise. While common in the field, even two seeds would substantially strengthen confidence.

- **Long-context comparison limited to RoPE only (Table 2):** FoPE, Pythia, and ALiBi are compared only in short-context settings (Table 1). For long-context evaluation (Table 2), only RoPE is compared, not the other PE baselines. It is unclear whether RoPE++'s long-context gains are specific to the imaginary extension or could be achieved by other PE designs when paired with the same continuous pre-training.

- **Figure 1 framing slightly misleading:** The "Imaginary Attention" section of Figure 1 lists "Cache & Parametric Efficiency" as a general advantage, but this only applies to the EH configuration. EC actually increases parameters via the doubled W_o (acknowledged on line 101). The figure should distinguish between configurations more clearly.

### Trivial
None

## Nice-to-Haves
- A parameter-matched ablation for EC (e.g., standard RoPE with doubled attention heads and doubled W_o) would cleanly disentangle the imaginary information contribution from additional capacity.
- Emphasizing the EH result more prominently would strengthen the paper — "comparable performance with half the cache" is the cleanest practical contribution.
- Including FoPE and ALiBi in the long-context comparison (Table 2) would clarify generalizability of the gains.
- Reporting variance over 2–3 seeds for short-context results where differences are small.

## Removed Points
These points are flagged to be removed, treat them with caution.
- Error bars / variance as a major concern: while valid, this is standard practice in large-scale pretraining benchmarks and should be a nice-to-have, not a major weakness.
- Formatting/style nitpicks: parser artifacts, not author issues.
- Missing related works: cannot verify external references; this is standard reviewer speculation.
- The harsh critic's concern about "missing appendix content" regarding larger-scale experiments: the paper explicitly references Appendix C, which exists in the original submission.

## Novel Insights
The core novel insight from this paper is the identification that standard RoPE discards exactly the imaginary component of its complex-valued computation, and that recovering this component via a simple −π/2 rotation of q yields attention heads with a fundamentally different characteristic curve (sine integral vs cosine integral) that preferentially attend to longer-range dependencies. This is not just a trick — the mathematical equivalence established in Equations 2–4, combined with the characteristic curve analysis in Equation 5, provides a principled understanding of *why* the imaginary component is valuable. The noise-injection analysis (Section 5.2) further provides a methodologically interesting way to validate the functional specialization of different attention head types. The practical cache-efficiency angle (EH variant using half the KV cache for comparable performance) is a genuinely useful contribution for deployment-constrained settings.

## Suggestions
- Add a parameter-matched ablation for EC to validate that gains come from imaginary information, not extra parameters.
- Emphasize EH results more prominently in the narrative — the cache-efficiency story without confounds is the paper's strongest practical contribution.
- Expand long-context evaluation to include FoPE and ALiBi baselines with continuous pre-training.
- Report variance over 2–3 seeds for short-context benchmarks.

## Calibration Report

**Round 1 — Bracketing anchors (topic: RoPE/position embedding/long-context):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| jp4pxKqCRW "Long-context Extrapolation via Periodic Extension" | 2.50 | 1 | Poorly written, weak experiments. RoPE++ is clearly much better. |
| 5dDYhvt6dY "Efficient transformer with reinforced PE" | 3.00 | 1 | Weak translation paper. RoPE++ clearly better. |
| 56mg1JFd3n "Writing in the Margins" | 3.00 | 1 | Long-context inference pattern, not PE-focused. Less relevant. |
| sIGWTd1DcW "Contextual Position Encoding (CoPE)" | 5.25 | 1 | Interesting idea but rejected for novelty/marginal improvements. RoPE++ is somewhat better. |
| JO7k0SJ5V6 "Scaling Laws of RoPE-based Extrapolation" | 5.00 | 1 | Tested on 7B/13B but only ppl evaluation. RoPE++ has broader evaluation but smaller scale. |
| GtvuNrk58a "Round and Round We Go!" | 6.20 | 1 | Deep RoPE analysis on Gemma 7B. Comparable insight depth but RoPE++ is more actionable. |
| eoln5WgrPx "Why Does Effective Context Length Fall Short?" (STRING) | 6.50 | 1 | Training-free, tested on 70B models with 10+ point gains. RoPE++ is clearly weaker in scale/impact. |
| OvoCm1gGhN "Differential Transformer" | 8.00 | 1 | Major contribution at scale. RoPE++ clearly below this. |

**Round 1 bracket: 4.5 to 6.5**

**Round 2 — Narrowing anchors:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 4GD7a9Bo9A "Bias Learning" | 4.50 | 2 | Position sensitivity in embeddings. Less technically interesting than RoPE++. |
| OhauMUNW8T "Wavelet-based Positional Representation" | 5.25 | 2 | RoPE-as-wavelet insight, marginal improvements. RoPE++ is better (cleaner theory, stronger results). |
| t717joHHSc "Mitigate Position Bias" | 4.75 | 2 | Scaling single dimension for position bias. Less relevant. |
| cqTUJRlcLU "Benign Overfitting in Attention" | 5.80 | 2 | Theoretical attention analysis. Different focus; not directly comparable. |
| 16kG5aNleS "Transformer Meets Twicing" | 6.25 | 2 | Attention mechanism modification (2A-A²) with modest practical gains. Comparable to RoPE++. |
| DVlPp7Jd7P "Attention layers solve single-location regression" | 6.50 | 2 | Theoretical attention analysis. Different focus. |

**Final assessment:** RoPE++ is clearly better than the 5.0–5.25 anchors (Scaling Laws, Wavelet, CoPE) due to its cleaner mathematical theory, broader evaluation suite (10 short-context + RULER + BABILong benchmarks), and the practical cache-efficiency contribution. It is comparable to the 6.0–6.25 anchors (Twicing, Round and Round) in insight quality but held back by the sub-LLM experimental scale and the EC parameter confound. It is clearly below the 6.5 anchor (STRING) which tested on 70B+ models with huge practical gains and required no training. I position the score at **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>