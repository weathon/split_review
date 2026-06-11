## Summary

This paper identifies the **priming vulnerability** in Masked Diffusion Language Models (MDLMs): affirmative tokens appearing at intermediate denoising steps steer generation toward harmful responses, even in safety-aligned models. The authors quantify this via an anchoring attack (Section 4.1) and propose First-Step GCG (Section 4.2), a ~20× faster optimization-based attack. They then propose **Recovery Alignment (RA)**, which trains models from intentionally contaminated intermediate states to recover safe responses. Experiments on three MDLMs (LLaDA, LLaDA 1.5, MMaDA) show RA reduces ASR to near zero at early intervention steps while preserving general capability across 11 benchmarks, and it also generalizes to conventional jailbreak attacks.

## Strengths

1. **First systematic quantification of the priming vulnerability in MDLMs.** The anchoring attack (Section 4.1, Figure 2) cleanly demonstrates that even a single injected affirmative token at step 1 increases ASR from 2% to 21% on LLaDA Instruct, and ASR exceeds 80% by step 16 across all three models. This is a controlled, measurable demonstration of a previously uncharacterized failure mode.

2. **First-Step GCG achieves ~20× speedup and up to 4× ASR improvement over Monte Carlo GCG** (Table 1: 58.0% vs. 20.0% on LLaDA Instruct, 0.2h vs. 4.3h per prompt). Theorem 4.1 provides a principled lower-bound surrogate, and the practical results are compelling regardless of the bound's tightness.

3. **RA dramatically reduces ASR across all three models while outperforming all baselines.** Key results from Table 2: at t_inter=1, RA achieves 0.0% ASR vs. 17.3% (original), 6.0% (next-best MOSA); at t_inter=4, RA achieves 1.3% vs. 44.0% (original), 24.0% (MOSA). The RA w/o inter ablation cleanly isolates the benefit of training from contaminated intermediate states.

4. **RA generalizes to conventional jailbreak attacks** (Table 3), reducing ASR on PAIR from 44.3% to 10.0% on LLaDA, and on Crescendo from 81.3% to 45.0%. This cross-task generalization is a meaningful finding beyond just mitigating the specific vulnerability.

5. **General capability is preserved** across 11 diverse benchmarks (Table 4): average performance is essentially unchanged for LLaDA (52.2% → 52.6%) and LLaDA1.5 (52.7% → 52.8%), with the main trade-off being a slight PIQA decrease.

6. **The ablation study on intervention step scheduling** (Figure 3b) provides clean evidence that the linear curriculum is critical — constant scheduling yields ~80-90% ASR while linear scheduling stays below 40%, validating a nontrivial training design choice.

## Weaknesses

### Fatal
None.

### Major

1. **SFT baseline behavior needs clarification.** The "No Attack" ASR increases under SFT on aligned models (LLaDA: 2.0% → 8.3%; LLaDA1.5: 1.0% → 6.3%), which is unusual for a safety alignment baseline. However, on MMaDA (unaligned), SFT *reduces* ASR from 79.7% to 46.0%, showing SFT is genuinely doing safety alignment there — contradicting the claim that it was trained on harmful-query–harmful-response pairs. This discrepancy demands explanation: why does SFT hurt aligned models but help the unaligned one? The paper defers baseline configurations to Appendix D.6 (stripped from this version). The authors must clarify what data SFT and DPO were trained on, and explain the anomalous No Attack ASR increases, for the comparison in Table 2 to be fully interpretable.

### Minor

1. **Theorem 4.1's monotonicity assumption is not validated in the main text.** The assumption that the log-probability of the exact target response monotonically increases over denoising steps is non-obvious and does work for the theoretical framing. The factor 1/T also makes the bound quite loose for T=128. The paper defers empirical validation to Appendix C.2. While the practical success of First-Step GCG does not depend on this theorem being tight, the theoretical framing oversells its rigor. A brief main-text validation (e.g., a small figure showing log-probability over steps) would strengthen the paper.

2. **BeaverTails dataset description is ambiguous.** The paper states the dataset "consists of harmful queries paired with harmful responses" (Section 6.1). BeaverTails actually contains both safe and unsafe responses per query with safety labels. Clarifying how the dataset was filtered is necessary to assess what data each method (RA, SFT, DPO) was trained on.

3. **The PIQA decrease under RA (~3 points on LLaDA and LLaDA1.5) merits more substantive discussion** as a potential safety-utility trade-off. The paper attributes it to "potential forgetting effects or output style shifts" but this is a concrete capability regression that could matter in deployment.

### Trivial
None.

## Nice-to-Haves
- **Mechanistic analysis of how RA works at the token level.** Does RA-trained LLaDA actually re-mask affirmative tokens at later steps? A small-scale analysis tracing the denoising trajectory (masking ratio or token-level entropy over steps) would strengthen the claim that RA teaches genuine *recovery* rather than just a more conservative refusal policy.
- **Ablation of reward model choice.** RA uses DeBERTaV3. Sensitivity to the choice of reward model is not examined; if the reward model has biases (e.g., over-rejecting benign responses), RA could propagate them.
- **Discussion of what happens when the reward model itself is attacked** or when the contaminated state includes tokens the reward model misclassifies as safe.

## Removed Points
These points were flagged to be removed; treat them with caution:
- **"SFT baseline is a straw-man (Structural/Fatal)"** — Demoted to Major (above). The critic's strong claim that SFT must have been trained on harmful pairs is contradicted by the MMaDA results (SFT reduces ASR from 79.7% to 46.0% there). The increase on aligned models may be due to distribution shift disrupting existing alignment, not straw-man configuration. Without the appendix (stripped), the claim cannot be verified as fatal.
- **"Unmasked tokens claim is misleading"** — The paper explicitly says "In typical implementations" (Section 3), framing it as an implementation choice, not a universal definitional property.
- **"Anchoring attack should better distinguish diagnostic from practical"** — The paper explicitly frames it as "a hypothetical attacker who can directly intervene" (Section 4.1).
- **"MC-GCG comparison is lopsided"** — The speedup (~20×) is the fundamental advantage being demonstrated; controlling for compute budget would defeat the purpose.
- **"Statistical rigor: only 3 runs"** — 3 runs with standard deviation reported is standard for this type of work.
- Missing related works — Cannot verify without external sources.
- Formatting/typography criticisms — Parser artifacts.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Clarify the SFT/DPO baseline data configurations.** What data were they trained on? Explain the asymmetric effect: why does SFT reduce No Attack ASR on MMaDA (79.7% → 46.0%) but increase it on LLaDA (2.0% → 8.3%) and LLaDA1.5 (1.0% → 6.3%)? This is the single most important clarification needed.
2. **Include a brief main-text validation of Theorem 4.1's monotonicity assumption** (e.g., a figure showing log π_θ over steps for a sample of query-response pairs).
3. **Clarify the BeaverTails filtering procedure** — specify which responses were used for RA, SFT, and DPO.
4. **Discuss the ~3-point PIQA decrease more substantively** as a potential safety-utility trade-off.

---

### Calibration Anchors

All anchors retrieved across all rounds:

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|------------------------|
| Bo62NeU6VF (Backtracking) | 8.00 | R1 | Stronger — cleaner execution, no baseline issues; this paper has more evaluation breadth but also more ambiguity |
| 6Mxhg9PtDE (Safety Tokens Deep) | 9.50 | R1 | Stronger — more comprehensive theoretical + empirical analysis of a unified phenomenon |
| r42tSSCHPh (Catastrophic Jailbreak) | 7.00 | R2 | Comparable — similar scope (vulnerability + mitigation); this paper has more novel vulnerability but also unresolved SFT issue |
| hXA8wqRdyV (Adaptive Attacks) | 6.14 | R2 | Weaker — less novelty, missing baselines; this paper has stronger contributions |
| G7gvaoX9AW (Vulnerabilities via Debiasing) | 5.80 | R2 | Weaker — limited experiments, unclear contributions; this paper is substantially stronger across all dimensions |
| u08UxVNdIo (Diffusion Attacker) | 4.75 | R1 | Weaker — questionable methodology, limited evaluation |
| Qn4HEhezKW (Diffusion LMs Scaling) | 5.00 | R1 | Not directly comparable (not about safety) |
| EEWpE9cR27 (VLM Safety Degradation) | 4.50 | R1 | Not directly comparable (different modality) |
| BeOEmnmyFu (Language Game Jailbreak) | 2.50 | R1 | Much weaker — limited contribution |
| KyKTjRtyNG (Multi-round Jailbreak) | 3.00 | R1 | Much weaker — limited generalizability |

**Round 1 bracket**: 6.5 – 8.0  
**Round 2 narrowing**: Compared directly to Catastrophic Jailbreak (7.00) and Adaptive Attacks (6.14). This paper is slightly stronger than Catastrophic Jailbreak in core novelty but has the SFT clarification issue, placing it at the same level. Clearly above Adaptive Attacks (6.14) and well above the 4.5–5.8 cluster.

**Final score**: 7.0

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>