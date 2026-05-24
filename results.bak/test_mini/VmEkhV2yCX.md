Now I have all the evidence I need. Let me write the final review.

## Summary

This paper presents a large-scale empirical study (1T token pretraining, 8B parameters, from scratch) investigating how reasoning data should be allocated across pretraining, supervised fine-tuning (SFT), and reinforcement learning (RL) phases of LLM training. The authors vary reasoning data along dimensions of scale, diversity, and quality, and find an asymmetric principle: pretraining benefits most from diverse, large-scale reasoning data, while SFT is dominated by data quality. They show that front-loading reasoning data into pretraining creates a durable advantage (≈19 percentage point lead after RL) that cannot be closed by more intensive SFT, and that high-quality pretraining data has a latent effect only unlocked after SFT. These findings are practically significant and supported by multiple controlled comparisons.

## Strengths

1. **Large-scale, controlled pretraining from scratch with phase-wise analysis.** The paper pretrains 8B models from scratch for 1T tokens with a fixed 80B reasoning token budget within pretraining, then systematically varies SFT data and evaluates through RL. This is the first study to span all three phases (PT→SFT→RL) with controlled reasoning data injection. The scale (512 H100 GPUs, 8B parameter models) far exceeds typical academic experiments and lends credibility to the findings.

2. **Clear, actionable asymmetric principle supported by converging evidence.** Table 1 shows that diverse reasoning data in pretraining (M_LDQ) outperforms high-quality narrow data (M_SHQ) by 9 absolute points, with the biggest gains in math (+23 points). Table 5 shows the reverse for SFT: high-quality data (D_SHQ) yields 44.99 vs 31.54 for diverse data — a 13.5 point advantage. The fact that the optimal data type flips between phases is the paper's strongest and most novel finding.

3. **RL phase demonstrates that pretraining gains compound, not wash out.** Table 3 is a striking result: M_LMQ+SFT_SHQ+RL achieves 56.66% vs 37.92% for M_base+SFT_SHQ+RL — an 18.74 point gap that widens to 33 points on AIME24 (45.21 vs 12.29). This directly refutes the hypothesis that post-training can fully compensate for a weak pretraining foundation.

4. **Latent effect of high-quality pretraining data.** Table 4 shows M_LMQ and M_LDQ are nearly identical at the base stage (64.07 vs 64.09), but after SFT the gap opens to 4.25 points (50.95 vs 46.70). This non-obvious finding — that high-quality data in pretraining can lie dormant and only activate after fine-tuning — is a genuine empirical contribution.

5. **Demonstration that naive SFT scaling is harmful.** Table 8 shows that doubling mixed-quality SFT data (2×LDQ) actually *decreases* math accuracy by 4.92 points, while a targeted 0.4% addition of high-quality data (D_ALF*) raises average accuracy by 10 points. This provides practical guidance for practitioners.

6. **Comprehensive evaluation suite.** The paper evaluates across 14+ benchmarks spanning math (GSM8K, MATH-500, AIME24/25), science (MMLU, MMLU-Pro, GPQA), code (LiveCodeBench), and instruction following (IFEval), with multiple evaluation runs for variance reduction.

## Weaknesses

### Major

1. **Framing mismatch: the budget-constrained optimization (Eq. 2) is not tested.** The paper sets up the problem as maximizing accuracy subject to `B = |D_res^PT| + |D_res^SFT|` (Eq. 2), suggesting it will compare allocations of the *same* total reasoning budget across phases. The experiments do not enforce this. In the main contrast (Table 3), M_base receives 0 reasoning tokens during pretraining while M_LMQ receives 80B — their total reasoning budgets differ by ~80B tokens. The catch-up experiment (Table 4) doubles SFT epochs, adding only ~2.4B tokens, still two orders of magnitude less than 80B. This does *not* test whether front-loading is optimal under a fixed total budget; it tests whether adding reasoning data to pretraining helps when post-training is held constant. That is a legitimate question with interesting results, but the headline claim overreaches. **This is a narrative issue that requires major revision of the framing.** The paper's core empirical findings remain valid — the asymmetric principle, the latent effect, the catch-up failure — but they should be presented as a study of *when* to inject reasoning data, not as a solution to a constrained allocation problem.

2. **The "diversity" attribution in pretraining is confounded with unique sample count.** D_LDQ (268M unique samples) and D_SHQ (1.2M unique samples) are both scaled to 80B reasoning tokens, so D_SHQ is repeated ~67× more. The paper attributes M_LDQ's 9-point advantage over M_SHQ to "diversity," but the comparison also differs on total unique examples, repetition frequency, reasoning-type composition, answer formatting, and other factors. The conclusion that "diversity" drives the gain is plausible but not uniquely supported — for example, the repeated exposure to a narrow set in D_SHQ could cause memorization without generalization, rather than diversity *per se* being beneficial. The paper acknowledges the datasets vary in "scale, diversity, and quality" but should soften the claim that diversity *per se* is the causal factor, or add a control (e.g., subsampling D_LDQ to match D_SHQ's unique example count while preserving diversity).

### Minor

3. **Scale asymmetry in the "catch-up" experiment.** Doubling M_base's SFT epochs adds only ~2.4B tokens (at ~500 tokens/sample, 4.8M samples) compared to the 80B reasoning tokens used in pretraining. The claim that "SFT cannot catch up" is well-supported for *this level of SFT scaling* but not as a general conclusion about any amount of SFT. The paper should explicitly acknowledge this orders-of-magnitude asymmetry rather than presenting it as a definitive refutation.

4. **RL evaluation limited to a single comparison path.** Table 3 only compares two models (M_base vs M_LMQ, both SFT_SHQ → RL). Other SFT combinations and RL recipes could yield different gaps. While single-path RL is understandable given computational cost, the paper should explicitly note this limitation.

### Trivial

5. **Unclear "19% average gain" phrasing.** The abstract and intro report "19% average gain" without specifying absolute vs. relative percentage. From Table 3, the gain is 18.74 *absolute percentage points* (37.92 → 56.66). The paper should say "19 percentage points" to avoid ambiguity. Similarly, "11% average gain" (M_base 52.70 → M_LDQ 64.09 = 11.39pp) and "15% average gain" (Table 5: 29.92 → 44.99 = 15.07pp) are also absolute point differences, which should be stated clearly.

## Nice-to-Haves

- A dedicated table showing total reasoning tokens across both phases for each model configuration would help readers understand the budget differences. Currently this must be manually inferred.
- An ablation using D_LDQ subsampled to match D_SHQ's unique example count (1.2M) while preserving diversity would substantially strengthen the diversity attribution.
- Additional analysis of the repetition effects in D_SHQ (e.g., training loss curves or memorization metrics) would improve the diversity argument.

## Removed Points

- **Missing appendix/proofs/related work** — These sections are stripped by the parser; the original submission contains them. Not a valid criticism.
- **D_ALF answer-length filtering validity** — The paper explicitly states this as an assumption ("based on the principle that longer responses often correspond to more complex CoT reasoning"), which is a reasonable heuristic used in prior work. The criticism is speculative, not a specific identified error.
- **Table 2 averaging obscures interactions** — The full breakdown is in Table 13 (appendix), which is standard practice for space-constrained papers.
- **"19% gain not explicitly referenced to a table"** — The gain is clearly traceable to Table 3 (37.92→56.66), and Table 1 and Table 5 for the 11% and 15% claims. The paper's attribution is clear enough.
- **Generalization to other architectures** — A 1.2B Transformer experiment is reported in the appendix (Table 14), partially addressing this concern. The hybrid Mamba2+Attention architecture is a reasonable modern choice.
- **Missing variance/error bars** — The paper reports multiple evaluation runs for key benchmarks (16 runs for AIME, 4 runs for others), which is standard practice for this scale of experiments.
- **Formatting nitpicks** — Parser artifacts, not author errors.
- **Generic or superficial strengths from the Strength Finder** (e.g., "the paper addressed an important problem") — Removed because they lack specific evidence or are generic praise.

## Novel Insights

Beyond the paper's own contributions, a noteworthy synthesis from the reviews is that the paper's most robust finding — the asymmetric principle — emerges even without perfectly controlled budgets. The fact that diversity in pretraining and quality in SFT is *so* dominant that it shows through despite multiple confounds (different unique sample counts, different total PT+SFT budgets, different repetition patterns) suggests the effect is genuine and practically meaningful. This robustness-through-replication across conditions is itself a strength that is not explicitly discussed in the paper.

## Suggestions

1. **Reframe the contribution.** Drop or significantly soften the budget-constrained optimization framing (Eq. 2). Instead, present the work as a systematic study of *when* reasoning data should be introduced: "We study the effect of injecting reasoning data at different phases and find that (a) front-loading yields a durable advantage that post-training cannot close, and (b) the optimal data type differs by phase — diversity in pretraining, quality in SFT." This honest framing is still a strong contribution.

2. **Add a deconfounding ablation for the diversity claim.** Either (a) subsample D_LDQ to 1.2M unique examples while preserving its diversity mixture and show it still outperforms D_SHQ, or (b) explicitly acknowledge the confound and soften the causal language about "diversity" to "scale and diversity" throughout.

3. **Clarify the scale asymmetry in the catch-up experiment.** State explicitly that doubling SFT adds ~2.4B tokens vs. 80B pretraining reasoning tokens, so the test shows "SFT at this scale cannot compensate" rather than implying any SFT scale would fail.

4. **Use "percentage points" throughout.** Replace ambiguous "X% gain" with "X percentage point gain" wherever the numbers refer to absolute differences in accuracy scores.

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| /home/wg25r/review_agent/human_reviews_2026/sHn5rq6L0O.md | 3.33 | R1 | Synthetic reasoning tasks, smaller scale; weaker contribution |
| /home/wg25r/review_agent/human_reviews_2026/Ia6kJSCqGO.md | 4.50 | R1 | Distillation-only study of reasoning, rejected; less ambitious |
| /home/wg25r/review_agent/human_reviews_2026/9Gp45bnDrJ.md | 5.60 | R1/R2 | New pretraining objective (RLP), accepted Poster; mixed reviews, smaller models |
| /home/wg25r/review_agent/human_reviews_2026/uLM3BfKo19.md | 5.67 | R1 | SFT-RL post-training study, accepted Poster; narrower scope |
| /home/wg25r/review_agent/human_reviews_2026/ou2GyHZ7HI.md | 5.00 | R1 | Reasoning evolution in decision-making domains, Rejected |
| /home/wg25r/review_agent/human_reviews_2026/IaEqjWXd1d.md | 6.50 | R1/R2 | AceReason SFT+RL synergy, accepted Poster; similar scale, fewer framing issues |
| /home/wg25r/review_agent/human_reviews_2026/9ZcB6tMcVP.md | 4.00 | R1 | RAFT fine-tuning, Withdrawn; limited scope |
| /home/wg25r/review_agent/human_reviews_2026/yKUbw7q1IA.md | 6.80 | R2 | Data-efficient LLM training, accepted Poster; T5-scale, more controlled variations |
| /home/wg25r/review_agent/human_reviews_2026/ZC5QBfdOw7.md | 6.50 | R2 | Text quality interventions, accepted Poster; similar large-scale pretraining study |
| /home/wg25r/review_agent/human_reviews_2026/7xjoTuaNmN.md | 6.50 | R2 | OpenThoughts data recipes, accepted Oral; SFT-focused, 1000+ exps |
| /home/wg25r/review_agent/human_reviews_2026/EoBmdFujak.md | 5.50 | R2 | Multi-experiment pretraining, accepted Poster |
| /home/wg25r/review_agent/human_reviews_2026/IKJyRyHpHV.md | 5.50 | R2 | Multilingual data mixtures, Rejected |
| /home/wg25r/review_agent/human_reviews_2026/B5Jl2srJXC.md | 6.00 | R2 | Procedural pretraining, Rejected despite score |

**Round 1 bracket:** 4.5 – 7.5 (clearly above the ~3 reject band, clearly below the ~8 top papers in different areas)

**Round 2 narrowing:** Comparing to accepted papers in the 5.5–6.8 range, this paper is stronger than the 5.5–5.7 anchors (Quagmires, RLP) due to the sheer scale of pretraining from scratch and the broader coverage of all three training phases. It is weaker than the 6.5–6.8 anchors (AceReason, How to train data-efficient LLMs, OpenThoughts) due to the framing mismatch and the diversity confound. It is most comparable to the 6.0–6.5 range (Procedural Pretraining, which scored 6.0 despite being rejected on other grounds), but the framing issues prevent it from reaching the same tier as the strongest accepted papers. The paper's genuine contributions (asymmetric principle, latent effect, catch-up refutation) are important, but the narrative overreach requires a major revision.

**Final score:** 6.0

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>