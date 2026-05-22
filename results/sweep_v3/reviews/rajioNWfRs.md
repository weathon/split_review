Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes TNT, a two-stage training paradigm for deep memory modules (RNNs with test-time memorization, specifically instantiated with Titans). Stage 1 uses a hierarchical memory architecture — a global memory for long-range context over large chunks, and multiple parallel local memories with periodic state resets that break sequential dependency and enable massive context parallelism. Stage 2 is a lightweight fine-tuning phase that adapts local modules to smaller chunk sizes for improved inference quality. On 150M-parameter models, TNT achieves up to 17× training speedup to a target loss while simultaneously improving perplexity over baseline Titans and matching vanilla Transformer quality.

## Strengths

1. **Up to 17× training speedup with simultaneous quality improvement (Table 1 & 2):** TNT (C_L={64}) reaches loss 3.20 in 1.12 hours versus 19.48 hours for the best Titans baseline (C=8) — a 17.37× speedup. Critically, this acceleration does not come at the cost of quality: the best TNT Stage 1 model achieves 23.13 average perplexity vs. 25.07 for Titans and 23.58 for vanilla Transformer. This directly validates the paper's central claim of decoupling training efficiency from inference performance.

2. **Linear runtime scaling that outperforms FlashAttention at long sequences (Figure 4):** TNT's runtime grows linearly with sequence length due to its periodic-reset parallelism, while Titans and attention-based models scale super-linearly. At 32K sequence length, TNT (C_L=128) runs in ~550ms vs. ~1000ms for FlashAttention and ~4000ms for Titans (C=16). This is concrete evidence that the hierarchical memory with resets enables effective context parallelism — a non-trivial achievement for non-linear recurrences.

3. **Clean ablation validates each component (Table 3):** Removing global memory increases perplexity by >4 points (21.04→25.60); removing Q-K projection costs ~1 point (21.04→22.01); Stage 2 fine-tuning adds further improvement (21.04→20.86). These controlled experiments provide direct causal evidence for the contributions of Sections 4.1.1, 4.1.2, and 4.2.

4. **Well-motivated problem diagnosis (Figure 2 / Challenge 3):** The paper identifies and cleanly demonstrates chunk-size sensitivity — inference perplexity is optimal only when inference chunk size matches the training chunk size, with a sharp U-shaped degradation on either side. This empirical finding (on a 550M model) is a clear insight that motivates the Stage 2 fine-tuning solution.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison: Stage 2 fine-tuning vs. simply fine-tuning the baseline Titans model.** Stage 2 is applied only to TNT Stage 1 models, never to the baseline Titans architecture. The paper does not compare against the obvious control: take a pre-trained Titans model (trained with C=8), fine-tune it with a smaller chunk size for the same number of steps, and measure the result. Without this, the claimed benefit of the two-stage TNT design over simpler alternatives (e.g., "train with C=8 then fine-tune with C=1") is unsubstantiated. This is directly fixable with one additional experiment.

2. **No evaluation on tasks requiring long-range dependencies.** The quality evaluation (Table 2) uses a fixed 16K context on standard language modeling (C4, FineWeb, PG19) and short-context reasoning benchmarks. Despite the paper's framing around "remov[ing] a critical scalability barrier" for "truly long sequences," there is no evaluation on any long-context benchmark (e.g., needle-in-a-haystack, LongBench, RULER, multi-document QA). The speed experiments (Figure 4) measure runtime but not quality at longer contexts. For a paper whose core thesis is about enabling efficient long-context training, the absence of evidence that TNT models *actually perform well* on long contexts is a significant gap.

3. **Weak support for the "model-agnostic" claim.** The paper asserts TNT is a general paradigm for any deep memory module, but only instantiates it on Titans. The abstract claims evaluation on "Titans and TTT models," yet TTT appears only as a baseline (PPL 27.62), not as a TNT instantiation. While the appendix (stripped by the parser) may contain additional results, the main paper provides no evidence of TNT's generality beyond a single architecture.

### Minor

4. **No compute-matched (FLOPs or wall-clock) comparison for quality.** Table 1 measures time-to-loss; Table 2 measures quality at a fixed token budget (10B tokens). These are not aligned. The paper does not provide FLOPs-per-step analysis, so it is unclear whether TNT's speedup comes from better architecture or more per-step computation. A comparison at equal wall-clock time or equal FLOPs would clarify this. The speedup claim in Table 1 is still meaningful as a practical metric, but the evidential support for "faster training while improving accuracy" would be stronger with a compute-matched anchor.

5. **Q-K Projection lacks cost–benefit analysis.** The projection requires maintaining a running d×d matrix per chunk, which represents non-trivial compute and memory overhead. The paper describes it as "efficient" and "constant-size" but provides no FLOPs, memory footprint, or wall-clock overhead numbers. Given the speedup claims, understanding the overhead of this component is essential.

6. **The "ideal inference scenario: chunk size of one" claim is contradicted by the data.** The paper asserts that Stage 2 fine-tuning adapts models for "the ideal inference scenario: a local chunk size of one." However, in Table 2, the Stage 2 model with C_L={1} achieves 23.99 PPL — worse than every Stage 1 model (best: 23.13). The best Stage 2 result uses {2,4,8,16} (23.09 PPL). The claim about chunk size 1 is overstated; the evidence shows multi-resolution local memories are what matter.

7. **Missing hyperparameter reporting in Table 1.** Table 1 lists C_L for TNT configurations but omits C_G and S_L. The paper states S_L=2048 for efficiency benchmarks (Sec. 5.1) and S_L=4096 for performance benchmarks, but it is unclear which applies to Table 1. This harms reproducibility.

### Trivial

8. **Minor presentation issues:** The notation C is used inconsistently between baseline Titans and TNT configurations in Tables 1-2. The abstract's phrasing "Evaluated on Titans and TTT models" is ambiguous and could be read as claiming TNT-TTT results that are not presented.

## Nice-to-Haves

- Evaluation at larger model scales (350M or 1B) to demonstrate scalability beyond 150M.
- Analysis of the periodic reset period S_L: the paper uses S_L=2048 or 4096 without ablation or justification for the choice.
- A brief analysis of the key-query domain mismatch (Challenge 2) beyond the ablation — e.g., cosine similarity between q_t and in-chunk keys to empirically validate the motivating claim.
- Discussion of training stability: hierarchical memory with resets could produce optimization challenges (e.g., loss spikes at reset boundaries), which are not addressed.

## Removed Points

The following points raised by the harsh critic were removed for the reasons stated:

- **"Uncontrolled compute budgets in the time-to-quality comparison"** (weakened to Minor #4 above): The harsh critic framed this as fatal, but Table 1's time-to-loss and Table 2's fixed-token-budget are both standard, complementary measurements. The gap between them is a real limitation but does not invalidate either measurement independently.
- **"Challenge 2 lacks empirical evidence beyond ablation"** (removed): The ablation in Table 3 (w/o Q-K projection → PPL 22.01 vs. 21.04) *is* the empirical evidence the critic asks for. The critic's request for cosine similarity analysis is a nice-to-have, not a missing requirement.
- **Criticism about W_init training stability** (removed): This is speculative; the paper does not report training instability, so the criticism lacks a concrete anchor in the text.
- **Criticism about missing comparison with concurrent work (Zhang et al., Guo et al.)**: These are discussed in Section 1 (line 39), and the paper clearly states the distinctions. The critic's request for empirical comparison against them is scope creep.
- **Criticism about larger model sizes**: Acknowledged as a nice-to-have but not a core weakness. The 150M scale is standard for this line of work.
- **Reproducibility nitpicks about missing hyperparameters**: Partially addressed in Minor #7; the remainder (learning rate, optimizer settings) are reported in Sec. 5.1.

## Novel Insights

The two reviews together surface an interesting tension: the harsh critic's strongest objection (no long-context evaluation) is about what the paper *didn't* test, while the strengths are all about what it *did* test (speed, PPL, ablation). This is characteristic of a paper that convincingly solves a sub-problem (training efficiency for deep memory modules) while making forward-looking claims about a larger goal (enabling long-context modeling). The insightful synthesis is that TNT's contribution — context parallelism for non-linear recurrences via periodic resets — is independently useful even without long-context quality evaluations, because the speedup and quality improvements at 16K already advance the practicality of deep memory modules. The long-context evaluation gap is real but does not undermine the core efficiency result; rather, it sets a natural agenda for follow-up work.

## Suggestions

1. **Add the missing Stage 2 control experiment:** Fine-tune a pre-trained Titans model (C=8) with a smaller chunk size for the same number of steps as TNT Stage 2. Compare the result to TNT Stage 2. This single experiment would substantially strengthen the paper's central claim about the two-stage design.

2. **Include at least one long-context quality benchmark** (e.g., RULER or LongBench at 32K). This does not require retraining — just evaluate the already-trained 16K models on long-context tasks and report whether quality degrades gracefully.

3. **Report FLOPs and memory overhead for the Q-K Projection** to calibrate the speedup claims.

4. **Tone down the "ideal chunk size of one" claim** given the experimental evidence, or clarify that the multi-resolution {2,4,8,16} configuration is the intended operating point.

5. **Clarify the abstract** to accurately reflect that TNT is instantiated on Titans (with TTT as a baseline, not a TNT variant).

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TvGPP8i18S.md` (MELODI) | 6.25 (Accept) | Similar hierarchical memory architecture; MELODI has stronger long-context evaluation but weaker speed claims. TNT has better-validated ablations but the same gap in long-context testing. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/E34AlVLN0v.md` (DEER) | 6.00 (Accept) | Both parallelize non-linear sequential models. DEER has broader architectural generality; TNT has more comprehensive quality evaluation. Comparable experimental depth. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/l0ZzTvPfTw.md` (FlashRNN) | 6.50 (Accept) | Hardware optimization for RNNs. Both show strong speedups. FlashRNN's engineering contribution is different in nature; comparable overall quality. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/IiagjrJNwF.md` (Memory Mosaics) | 6.25 (Accept) | Associative memory architecture. TNT has stronger experimental validation and clearer ablations. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/GrmFFxGnOR.md` (minLSTM/minGRU) | 5.00 (Reject) | Both simplify/parallelize RNN training. TNT has substantially stronger empirical evaluation on standard benchmarks vs. primarily synthetic data. TNT is the stronger paper. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/8qYuxV4lRu.md` (Recycled Attention) | 5.40 (Reject) | Long-context efficiency method. TNT has more architectural novelty and better ablation but similar experimental gaps. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/4ymHtDAlBv.md` (FSFC RNN) | 2.33 (Reject) | Weak paper with minimal experimentation. TNT is far stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/N581Nje6fH.md` (Long Horizon Episodic) | 1.50 (Reject) | Poorly executed early-stage work. TNT is incomparably more rigorous. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/HEcbGXzIHK.md` (Episodic Memory Theory) | 4.25 (Reject) | Theoretical RNN analysis. Different contribution type; TNT has clearer empirical contributions. |

The paper presents a well-motivated and technically sound approach with strong speedup results and clean ablations. However, the experimental evaluation has two significant gaps — no long-context quality evaluation and a missing control for the Stage 2 fine-tuning — that prevent the paper from reaching the level of the stronger accepted anchors (6.0–6.5). The contribution is clearly above the level of papers scoring ≤5.0, and the weaknesses are addressable. Relative to the anchors, TNT sits between the top of the reject band (minLSTM at 5.00) and the bottom of the accept band (DEER at 6.00).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>