Now I have a clear picture. Let me write the final review.

**Bracket:** Based on Round 1, the paper sits between the weak-anchor band (2.5–4.5) and the middle-anchor band (4.5–6.1). The closest comparable anchors are HelloBench (4.75), M4LE (4.75), and AcademicEval (4.00). Round 2 narrows this to [3.5, 5.0].

**Final Score rationale:** VOLTBench's volatility-focused design is genuinely novel compared to HelloBench (4.75) and addresses a real gap. However, the paper's method evaluation has significant problems not present in comparable benchmarks: the SCA metric is tautological given SELB's design, the headline 148% claim uses the wrong reference point, and decoding baselines are not directly compared. These issues are more severe than HelloBench's incremental-novelty concern, pushing the score below 4.75. The paper is stronger than AcademicEval (4.00), which has limited novelty and poor evaluation metrics. Score: **4.0**.

---

## Summary
This paper investigates output length volatility in LLM long-form generation through three components: VOLTBench (a benchmark quantifying volatility via repeated sampling with metrics like LSD, LVC, and FAD), attention trace analysis (identifying two internal failure patterns), and SELB (a training-free decoding intervention that forces structural adherence). VOLTBench introduces a genuinely novel focus on generation stability as a core evaluation dimension, confirmed by Table 1 showing no prior benchmark includes multiple sampling or stability evaluation. SELB demonstrates improved length adherence over LongWriter-8B but the evaluation has significant gaps that weaken the method contribution.

## Strengths
- **VOLTBench is the first benchmark to operationalize output volatility through repeated sampling.** The dedicated stability metrics (LSD, LVC, FAD) and N=5 repeated generations per prompt are a genuine innovation. Table 1 confirms no existing long-form generation benchmark includes "Multiple Sampling" or "Stability Eval," establishing this as a real gap that the paper fills.
- **Multi-dimensional benchmark design enables fine-grained behavioral analysis.** The 3×2×2 structure (language × format × complexity) plus chapter-based length scaling reveals nuanced findings — e.g., models produce longer, more stable outputs for structured tasks than unstructured ones, and English prompts yield lower volatility than Chinese (Figure 3).
- **Dual evaluation framework pairs complementary quality signals.** LLM-as-a-Judge (UCA) for unstructured tasks and Execution-based Verification (SCA) for structured tasks provide complementary quality assessment, avoiding sole reliance on subjective judge-based evaluation.
- **SELB demonstrates meaningful length-adherence improvements over LongWriter-8B.** On the 100-section task, SELB achieves MLA of 78.25% (vs. 31.6%), LVC of 14.02% (vs. 45.4%, a 69% relative reduction), and produces 15,651 words (vs. 6,320), while maintaining UCA at 86.7% — matching the base Qwen2.5-7B model's quality level (Section 6.3).

## Weaknesses

### Major
- **SCA=100% is mechanically guaranteed by SELB's design, not evidence of quality.** SELB forces section-title token generation at length thresholds (Eq. 2: "a strong positive bias β is applied to the logits of tokens corresponding to the next section title") and suppresses EOS until all sections are produced (Eq. 3: "−∞ if j = v_eos ∧ p < P_total"). The SCA metric (correct chapters / required chapters) is therefore guaranteed to be 100% by construction. Reporting this as an achievement ("our model scored a perfect 100%, dramatically better than LongWriter-8B's 32.6%") is misleading — it should be reported as a sanity check. The meaningful quality signal is UCA, where SELB scores 86.7%, identical to the base Qwen2.5-7B model's 86.7% in Table 2. Quality is maintained, not improved.

- **Missing comparison against decoding baselines.** Section 6.3 compares SELB exclusively against LongWriter-8B (a fine-tuned model), yet Section 4.1 introduces and evaluates four training-free decoding strategies — Repetition Penalty, Entropy-Based Stopping, Length Constraint, and Lookahead Decoding — implemented on the same Qwen2.5-7B base model. These are SELB's most natural competitors as they are also decoding-stage interventions requiring no training. No side-by-side comparison exists. The Length Constraint baseline from Table 2 achieves 4,470 words with 96% SCA; whether SELB's higher word count (15,651) and MLA (78.25%) represent genuine improvement or are explained by differences in implementation details is unexamined. This omission makes it impossible to assess SELB's marginal contribution over existing decoding interventions.

- **The 148% improvement claim in the abstract is not supported by the presented data.** The abstract states SELB "improves the mean output length of the base model by 148%." The base model (Qwen2.5-7B) produces 445 words on the 100-section task (Table 2). SELB produces 15,651 words (Section 6.3), which is a ~3,400% increase, not 148%. The 148% figure corresponds to the improvement over LongWriter-8B: (15,651 − 6,320) / 6,320 ≈ 148%. LongWriter-8B is a fine-tuned long-form specialist and the primary comparison target, not the "base model" SELB is applied to. This error in a headline abstract claim is a significant presentation problem that misleads readers about the method's actual effect.

### Minor
- **The attention probing does not inform the method design.** The paper's narrative arc (benchmarking → probing → mitigation) implies the attention findings motivate SELB. But SELB's two components — forcing section titles at thresholds and suppressing EOS/filler tokens — are heuristic rules that require zero knowledge of attention patterns. The probing identifies "Attention Collapse" and "Attention Instability," but SELB does nothing to detect, prevent, or respond to these patterns; it overrides model decisions with hard constraints. The paper would be equally coherent without Section 5. Additionally, the probing analysis is narrow: only two models (Qwen2.5-7B, Qwen2.5-3B), one task (diary, 40 sections), and entirely qualitative with two hand-picked traces (Figure 4), without quantitative linking of attention metrics to output volatility metrics.

- **N=5 is small for reliable variance estimation.** LSD and LVC are computed from only 5 generations per prompt. Standard deviation estimates from N=5 have wide confidence intervals, meaning the reported volatility numbers — particularly for high-variance models like LongWriter-8B (LSD=2,866, μ=6,320) — may be noisy. This affects the interpretability of the benchmark's primary contribution.

### Trivial
None.

## Nice-to-Haves
- The SELB-Hybrid extension for free-form generation (Section 6.4) is described only at a high level in the main text. Key details (how the Hybrid Keep-Alive mechanism detects stalls, what continuation tokens are boosted) are deferred to Appendix I. Including more substance in the main paper would strengthen the generalization claim.
- Benchmark construction details (total number of instances, whether prompts are human-authored or template-generated) are not specified in the main text, leaving readers uncertain about coverage and potential biases.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Harsh Critic: fine-grained constraint data relegated to Appendix D makes assessment impossible.** Removed — the parser strips appendix sections; the data exists in the original submission.
- **Harsh Critic: prior benchmarks "do evaluate length adherence" and the introduction should acknowledge this.** Removed per hard rule — this is about related work coverage, which cannot be externally verified.
- **Strength Finder: attention patterns are "causally linked" to failures.** Removed — the paper demonstrates only correlation through two qualitative trace examples, not causation.
- **Harsh Critic: benchmark description promises 100k-word coverage but experiments don't deliver at that scale.** Removed — Figure 1 does display results across that range, and the appendix may contain additional experiments.

## Novel Insights
None beyond the paper's own contributions. The observation that output length volatility can be systematically quantified and that simple decoding-time structural enforcement can substantially improve length adherence — while maintaining content quality — is the paper's own contribution, though the method's value relative to simpler baselines remains unestablished.

## Suggestions
- Treat SCA as a sanity check, not a quality result. Center the method evaluation on UCA and execution-based verification, and directly compare SELB against all decoding baselines from Table 2 on identical task configurations.
- Either deepen the attention analysis (quantitative metrics across more models and tasks, demonstrating predictive value for downstream volatility) and establish a genuine link to the method, or reposition it as purely diagnostic and shorten it substantially.
- Correct the 148% claim to reflect the actual reference point (LongWriter-8B, not "the base model") or recalculate against the true base model (Qwen2.5-7B, 445 words → 15,651 words = ~3,400% increase).

## Score and Decision

**Anchor comparison summary:**
| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| HelloBench (QM2WoPu1It) | 4.75 | R1/R2 | Most directly comparable — long-form generation benchmark. Our benchmark is more novel (volatility metrics), but our method evaluation gaps are more severe. Our paper is slightly weaker overall. |
| M4LE (IkIqzDI7ie) | 4.75 | R2 | Long-context benchmark with synthetic data construction issues. Our benchmark is more novel, but our method evaluation problems level the comparison. |
| AcademicEval (iRYExPKnxm) | 4.00 | R1/R2 | Narrow-scope benchmark with limited novelty. Our paper has broader contribution (benchmark + method) and more novel benchmark design. Our paper is stronger. |
| PRISM Decoding (A6juYCULJO) | 6.00 | R1/R2 | Comprehensive decoding-strategy evaluation. More thorough and polished than our paper. Our paper is clearly weaker. |
| Tool Decoding (5bUy4F59mk) | 6.00 | R2 | Training-free decoding method with thorough evaluation. More polished, fewer severe issues. Our paper is clearly weaker. |
| LongSafetyBench (dQzpP9ziaJ) | 3.50 | R1 | Safety-focused benchmark. Our paper has wider scope and more novelty. Our paper is stronger. |

**Round 1 bracket:** [3.5, 5.0]
**Round 2 narrowing:** The paper lands between AcademicEval (4.00) and HelloBench/M4LE (4.75). The benchmark contribution is more novel than AcademicEval's and comparable to HelloBench, but the method evaluation issues (tautological SCA, incorrect headline claim, missing baselines) are significant enough to place it closer to 4.0 than 4.75.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>