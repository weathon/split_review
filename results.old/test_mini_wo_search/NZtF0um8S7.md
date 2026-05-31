Here is the consolidated review.

---

## Summary

This paper investigates in-context few-shot learning for seq2seq (encoder-decoder) models, a capability that has mostly been studied in decoder-only architectures. The authors propose two adaptations: (1) objective-aligned prompting — placing the target input on the encoder side and using sentinel tokens or mode tags consistent with pretraining — and (2) fusion-based methods (early-fusion and late-fusion) that independently encode each demonstration to sidestep length limits and permutation bias. On an 11-task NLU benchmark, T5-11B with early-fusion achieves 58.1–58.7 average accuracy, surpassing OPT-66B (54.5–55.1) despite being six times smaller. The fusion methods also eliminate permutation bias entirely on the tested tasks. The paper is the first to report systematic few-shot (>1-shot) results for seq2seq models on generation tasks (XSum, WebNLG).

## Strengths

- **First broad head-to-head comparison of seq2seq vs. decoder-only in-context few-shot learning across NLU.** Table 3 evaluates T5, T5-LM, T0, and UL2 (with the proposed methods) against OPT-7B–66B and BLOOM-7B on 11 diverse tasks under controlled prompting and scoring, going substantially beyond prior work that focused on zero-shot or generation-only settings.

- **Demonstrates a concrete parameter-efficiency advantage.** T5-11B with early-fusion (58.11 five-shot, 58.72 ten-shot) outperforms OPT-66B (54.52, 55.11) on the same 11-task benchmark — a model six times larger — with the advantage holding across multiple shot configurations (Table 3). This is a striking empirical result backed by per-task scores.

- **Objective-aligned prompting yields large, measured gains.** The paper quantifies gains of up to +20.5 %p from placing the target input on the encoder side (Table 1) and up to +13 %p from adding sentinel tokens (Table 2), with results shown across four different seq2seq models. The ablations are well-controlled and convincing.

- **Complete elimination of permutation bias.** Early- and late-fusion both achieve a standard deviation of 0.00 across all 120 permutations of 5-shot examples in a 4-task evaluation, while the original seq2seq method has std 4.51 and OPT-13B has std 2.02 (Table 5). This is a clean, quantitative demonstration of an important property.

- **Robust improvement across diverse seq2seq base models.** Figure 2 shows that early- and late-fusion consistently improve performance for T5, T5-LM, T0, and UL2 — models with different pretraining objectives and training histories — reinforcing the generality of the approach.

## Weaknesses

### Fatal

None.

### Major

- **No variance reporting for the core comparison in Table 3.** The paper runs five random seeds and reports averages (line 300), but neither standard deviations nor confidence intervals are shown for any model in Table 3 — not for the decoder-only baselines, and not for the seq2seq variants that constitute the headline result. Figure 2 provides standard deviations for seq2seq models but omits the decoder comparisons from the same table. Since the claimed advantage (T5-early vs. OPT-66B) is 2–4 percentage points on an 11-task average, and the paper itself notes that some tasks (Winogrande, HellaSwag) favor decoder models, the reader cannot assess the reliability or stability of the average margin. This is the paper's central evidential claim and it lacks basic variance quantification.

- **No decoder-only baseline for generation tasks.** Tables 4a and 4b (XSum, WebNLG) compare only T5 variants (T5*, T5, T5-early, T5-late). The abstract frames seq2seq models as "robust few-shot learners for a wide spectrum of applications," and the title is broader still, but the generation results include no decoder-only comparison. While the paper's stated contribution is the first *few*-shot (>1-shot) results for seq2seq on generation tasks, the absence of any decoder baseline in these tables limits how broadly the "outperforming decoder-only models" claim can be extended.

### Minor

- **Prompt engineering asymmetry between seq2seq and decoder-only models is not acknowledged as a limitation.** The decoder-only baselines use "minimal templates" from eval-harness (Table 3 caption), while the seq2seq models additionally use objective-aligned prompts (sentinel tokens, mode tags) that Tables 1–2 show are critical for performance (gains up to +20 %p). The paper states the evaluation uses "identical prompt structures" (line 191), which is strictly inaccurate — the prompt format differs because seq2seq models receive model-specific tokens. This does not invalidate the result (the paper's point is that these adaptations are what enable seq2seq few-shot learning), but the limitation should be explicitly discussed rather than presented as a controlled architecture comparison.

- **Computational cost of fusion methods is not discussed.** The paper notes that "inference time can be reduced… through batch processing" (line 182) but does not quantify the tradeoff: early-fusion encodes each demonstration independently, incurring k× the encoder cost plus longer cross-attention. A brief FLOPs or wall-time comparison between original, early-fusion, and late-fusion would help readers gauge practical deployment cost.

### Trivial

None.

## Nice-to-Haves

- Including standard deviations or confidence intervals for all baselines in Table 3 would substantially strengthen the paper.
- Adding a decoder-only baseline (e.g., OPT-13B) to the XSum and WebNLG tables would extend the scope of the comparison to generation.
- A dedicated plot or table comparing T5-early against multiple OPT scales (7B–66B) would more clearly show the crossover point and strengthen the "six times larger" result.
- A brief FLOPs or latency analysis of the fusion methods would aid practical assessment.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The claim that 'this is the first work that explores few-shot learning for seq2seq models on generation tasks' should be softened."** — The paper explicitly acknowledges that UL2 and AlexaTM only reported *1-shot* results (lines 342–343), so the claim about *few*-shot (>1-shot) being first is defensible. Not a genuine weakness.

2. **"Excluding T0 and UL2 from Table 3 because they underwent further training narrows the evidence."** — The paper's reasoning (line 314: T0 was multitask fine-tuned, making comparison to raw pretrained models unfair) is methodologically sound. Results for these models are shown separately in Figure 2. Not a genuine weakness.

3. **"GPT-4 speculation in conclusion feels out of place."** — A single sentence in the discussion section; not material to evaluation.

4. **"Permutation bias analysis is only on 4 tasks; careful not to imply universality."** — The paper explicitly scopes this to 4 tasks covering diverse taxonomies (lines 411–412) and uses appropriately cautious language. Not overclaimed.

5. **"Ablation on intermediate fusion points (not just early vs. late) would be useful."** — This demands exploration beyond the paper's stated scope; the two extremes are well-motivated by the RAG/FiD literature.

## Novel Insights

The two reviews converged on the same set of substantive issues (missing error bars, prompt asymmetry, missing decoder baselines on generation) while disagreeing on several weaker points (scope of UL2/T0 exclusion, the "first work" claim, which the paper explicitly qualifies). A key observation that neither reviewer fully articulated: the paper's strongest individual-task results (e.g., CB: +24 %p over OPT-66B, WSC: +26 %p, RTE: +7–10 %p) are so large that even without formal significance testing, they strongly suggest the claimed advantage is real for specific task types. The weaker tasks (Winogrande, HellaSwag) are where the decoder models excel, which is an informative finding in itself — seq2seq and decoder-only models have complementary strengths that fusion amplifies rather than introduces. The paper would benefit from leaning into this pattern rather than focusing solely on the aggregate average.

## Suggestions

1. Add standard deviations (from the 5 seeds already run) to Table 3 for all models, or alternatively provide a supplementary table with per-seed results.
2. Add a decoder-only baseline (OPT-13B or BLOOM-7B) to the XSum and WebNLG tables.
3. Explicitly acknowledge the prompt asymmetry in the limitations section — state that decoder-only baselines use minimal templates and that objective-aligned prompting for decoder models is left to future work.
4. Add a brief paragraph or small table analyzing the computational cost (relative FLOPs or wall time) of original, early-fusion, and late-fusion as the number of shots increases.
5. Consider reframing the headline result around task-specific advantages (e.g., "seq2seq models with fusion dramatically outperform decoder-only models on reasoning and coreference tasks") rather than relying solely on the aggregate average.

## Score and Decision

This paper makes a meaningful contribution: it demonstrates that with appropriate prompt alignment and fusion-based encoding, seq2seq models can be effective few-shot learners, outperforming a six-times-larger decoder model on NLU tasks and eliminating permutation bias. The ablations are careful, the experimental scope is broad, and the core results are likely reliable. The weaknesses are real (missing variance reporting, incomplete generation-task comparison, unacknowledged prompt asymmetry) but addressable — they do not undermine the paper's central contribution. With the suggested revisions, this would be a strong paper.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>