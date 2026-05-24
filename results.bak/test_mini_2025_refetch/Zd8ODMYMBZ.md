Now I have sufficient calibration data. Let me write the consolidated review.

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Reward-RAG | oqRe1KvD17 | 3.00 | 1 | Much weaker — withdrawn paper with poor evaluation |
| TimeRAG | GvzL4LuycW | 3.00 | 1 | Much weaker — different domain, withdrawn |
| LongLLMLingua | 8dkp41et6U | 5.80 | 2 | Weaker — seen as incremental, FAVICOMP is more novel and has cleaner experiments |
| Compressed Context Memory | 64kSvC4iPg | 5.75 | 2 | Weaker — task-specific method, FAVICOMP more broadly applicable |
| ICAE | uREj4ZuGJE | 6.75 | 2 | Comparable — similar quality, both accepted-quality methods with some evaluation gaps |
| Retrieval is Accurate Gen | oXYZJXDdo7 | 7.00 | 2 | Comparable — different approach, similar strength |
| **RECOMP** | **mlJLVigNHp** | **7.00** | **1, 2** | **Stronger — more thorough evaluation, but FAVICOMP has more novel training-free approach** |

**Round 1 bracket:** 3.5–7.5
**Round 2 narrowing:** FAVICOMP sits between LongLLMLingua (5.8) and RECOMP (7.0), closest to ICAE (6.75). Score = 6.5.

---

## Summary

This paper proposes FAVICOMP, a training-free evidence compression method for RAG that uses multiplicative ensemble decoding between the compression model and the target model during compression. At each decoding step, tokens are selected by weighting log-probabilities from both models, which lowers the target model's perplexity on the compressed evidence while enabling the integration of parametric knowledge. Experiments across five open-domain QA datasets with two target model families (Llama3-8B, Mixtral-8x7B) show consistent improvements over recent compression baselines including CompAct, RECOMP, and LongLLMLingua. Ablation studies on the ensemble coefficient α and a Hits-based analysis of parametric vs. non-parametric knowledge integration provide mechanistic insight into how the method works.

## Strengths

- **Novel and clean approach to evidence compression**: FAVICOMP's ensemble decoding (§2.3, Eq. 5) is a conceptually simple but effective departure from prior compression methods. Rather than training a compressor or relying on a single model's output, it proactively shapes the compressed evidence to be more familiar to the target model by constraining the token search space. This is training-free and model-agnostic, making it easy to plug into existing RAG pipelines.

- **Consistent outperformance over supervised and unsupervised baselines**: In Table 1, FAVICOMP achieves the highest accuracy among all compression methods across five datasets with both Llama3-8B-Instruct and Mixtral-8x7B-Instruct. It surpasses supervised methods like CompAct (e.g., HotpotQA with Llama3: 33.0 vs. 29.8) despite using a smaller 3B compression model and requiring no training. On MuSiQue, FAVICOMP even exceeds the Gold Compression oracle, demonstrating that parametric knowledge integration can compensate for imperfect evidence.

- **Demonstrated integration of parametric knowledge on evidence-irrelevant subsets**: The Hits analysis (§4.3, Figure 3) provides the strongest evidence for FAVICOMP's claimed capability. On the Hits=0 subset (where retrieved evidence lacks the answer), FAVICOMP substantially outperforms both Zero-shot Summarization and CompAct (e.g., MuSiQue Hits=0: 11.4 vs. 2.9 and 9.2). This is directly attributable to the ensemble mechanism drawing on the target model's parametric knowledge — a capability not shown by prior compressors.

- **Informative ablation on the ensemble coefficient α**: Figure 2 traces a clear U-shaped accuracy curve peaking at α=0.5, alongside monotonically decreasing perplexity. This reveals the trade-off between evidence grounding and parametric knowledge, showing that the optimal point balances both sources. The analysis goes beyond a simple "lower perplexity is better" story and provides genuine mechanistic insight.

## Weaknesses

### Fatal
None.

### Major

- **No variance or statistical significance reporting**: All main results (Table 1, Figure 2, Figure 3) are reported as single point estimates without standard deviations, confidence intervals, or significance tests. This is a significant evidential gap because several of the claimed improvements over the strongest baseline (CompAct) are modest: on NQ with Llama3-8B-Instruct, FAVICOMP (3B) achieves 42.8% vs. CompAct's 42.3% (0.5% gap); on TQA, 68.0% vs. 67.0% (1.0% gap). Without error bars, readers cannot determine whether these advantages reflect systematic improvement or random variation. While many comparisons show larger margins (HotpotQA: +3.2, 2WikiMQA: +4.1), the paper's central claim of "consistently outperforming" baselines requires stronger evidential support. The paper should provide at minimum multiple runs with means and standard deviations for the key comparisons.

### Minor

- **Computational cost of ensemble decoding is uncharacterized**: FAVICOMP runs two LMs (compression model and target model) at each decoding step during compression. This introduces non-trivial inference overhead compared to single-model compression. The paper does not report wall-clock time, latency, or FLOPs for any method. While the method is training-free, practitioners need to understand the inference cost trade-off. Even a single table reporting average compression latency per query would substantially improve the paper's practical value.

- **Decoding strategy for downstream generation is unspecified**: The paper does not state whether the target model uses greedy decoding, sampling, or beam search for the downstream QA generation task. This affects reproducibility. The prompts are referenced to the (stripped) appendix, but the decoding strategy should be stated in the main body.

- **Subset sizes not reported for Hits analysis**: In Figure 3, the accuracy on the Hits=1 (evidence-relevant) subset is suspiciously flat across all α values (e.g., HotpotQA: 9.5 for all α; 2WikiMQA: 11.4 for all α; MuSiQue: 5.9 for all α). This flatness likely reflects either a very small sample size or a floor effect. The paper should report the number of samples in each Hits subset to let readers properly contextualize these percentages.

### Trivial
None.

## Nice-to-Haves

- A controlled experiment to more directly test the familiarity hypothesis (e.g., generating two compressed contexts with the same perplexity but different origins and comparing downstream performance) would strengthen the paper's conceptual framing, though it is not required to validate the method's empirical effectiveness.
- Reporting baseline hyperparameters in the main text (e.g., compression length, ensemble coefficients for other methods) rather than deferring entirely to the appendix would make the paper more self-contained.

## Removed Points

These points were raised by the harsh critic or strength finder but are removed with justification:

- *"Familiarity mechanism conflates correlation with causation"* — Removed. The paper uses perplexity as a proxy for familiarity, which is standard in prior work (Liu et al., 2024; Gonen et al., 2023). Figure 2 shows a nuanced U-shaped curve that actually argues against a simple "lower PPL = better" story; the paper explicitly discusses the trade-off. The method's effectiveness does not depend on proving a causal theory of familiarity.
- *"Compression model is from the same family as target"* — Removed. This is transparently disclosed in §3.2, and the paper includes a same-model setting (Mistral-7B as both compression and target) in Appx. §B.1, demonstrating the approach works even without cross-family benefit.
- *"Missing self-RAG comparison"* — Removed. Self-RAG is an architecturally different paradigm (learned retrieval decisions, special tokens) rather than a compression method. Not an appropriate baseline for this paper's framing.
- *"Perplexity rise at α=0.9/1.0 unexplained"* — Removed. The paper provides a reasonable explanation: "increased uncertainty with limited evidential knowledge."
- *"Comparison with RECOMP uses different base models"* — Removed. The paper acknowledges this and includes a head-to-head experiment in Appx. §B.2 (stripped by the parser but present in the original submission).
- *"The 'up to 23.91%' claim is ambiguous"* — Removed. Verified correct: Zero-shot Summarization (8B) on 2WikiMQA = 22.3 → FAVICOMP (8B) = 27.6, which is a 23.8% relative improvement.
- *"Hits=1 flatness not contextualized"* — Downgraded to Minor and kept (subset sizes should be reported), but the observation itself is correct and worth noting.

## Novel Insights

The most interesting insight from synthesizing the reviews is that the ensemble coefficient α serves dual roles simultaneously: it controls both (1) the target model's perplexity on the compressed evidence and (2) the degree of parametric knowledge injection. These two effects are entangled in FAVICOMP — a higher α both lowers perplexity AND increases parametric token selection. The Hits analysis partially disentangles them by showing that α=0.5-0.7 works best on evidence-irrelevant subsets (where parametric knowledge is needed), while α=0.1-0.5 all perform similarly on evidence-relevant subsets. This suggests that the main risk of high α is not over-reliance on parametric knowledge per se, but rather the loss of evidence-grounded tokens even when evidence is useful — a more nuanced trade-off than the paper explicitly draws out.

## Suggestions

1. **Add error bars**: Run all key experiments (at least Table 1's main results with the 3B compression model) with 3-5 random seeds and report means with standard deviations. This directly addresses the most serious weakness and would likely take fewer than 100 GPU-hours given the 3B compression model size.

2. **Report wall-clock time for compression**: Add a simple table comparing average compression latency (seconds per query) for FAVICOMP vs. Zero-shot Summarization and CompAct. This would help practitioners assess the practical overhead of running two models.

3. **State the downstream decoding strategy explicitly** (greedy/sampling/beam search) in §3.2 or §3.3.

4. **Report Hits subset sizes** to contextualize Figure 3's percentages.

## Score and Decision

Based on calibration against human-reviewed anchors — the paper is clearly stronger than LongLLMLingua (5.8, Reject) and Compressed Context Memory (5.75, Accept poster), comparable to ICAE (6.75, Accept poster), and slightly below RECOMP (7.0, Accept poster) due to the missing error bars. The core idea is novel and clean, the experiments are broad and largely convincing, and the main weakness (no variance reporting) is addressable. However, this weakness is significant enough that the paper does not reach the RECOMP tier.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>