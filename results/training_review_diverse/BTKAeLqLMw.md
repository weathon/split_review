## Summary

This paper investigates what makes good data for instruction tuning through controlled studies across three dimensions — complexity, quality, and diversity — and proposes a selection pipeline (DEITA) that scores samples by the product of learned complexity and quality scores, then applies an embedding-based diversity filter. The key finding is that only 6K–10K automatically selected samples suffice to match or exceed models trained on over 10× more data across multiple backbones (LLaMA-1/2, Mistral-7B) and benchmarks (MT-Bench, AlpacaEval, Open LLM Leaderboard).

---

## Strengths

1. **Comprehensive controlled study isolating three data dimensions with novel, effective metrics.** The paper systematically investigates complexity, quality, and diversity in separate controlled experiments (Sections 3.2–3.4). For complexity, the proposed Evol-Complexity achieves the best MT-Bench scores on both data pools (6.27 on X_sota, 5.57 on X_base, Table 1), outperforming all baselines including Instag Complexity and IFD. For quality, Evol-Quality similarly generalizes better than direct scoring (Table 2). This rigorous per-dimension comparison provides concrete evidence distinguishing what "good data" means. The evolution-based relative scoring method (presenting all variants of a single sample within one prompt) is a clever design that enables finer-grained differentiation than absolute scoring.

2. **Extreme data efficiency demonstrated across multiple backbones and benchmarks.** DEITA models trained with only 6K–10K selected SFT samples match or surpass models trained on 10–30× more data. For example, DEITA-Mistral-7B_6K achieves 7.22 MT-Bench and 80.78% AlpacaEval (Table 3), outperforming Zephyr-beta-sft (200K samples) at 5.32 and 75.12, and Vicuna-13B (125K samples). With DPO (6K SFT + 10K DPO), it reaches 7.55 MT-Bench and 90.06% AlpacaEval — comparable to Zephyr-beta (200K SFT + 60K DPO). The data scaling curve (Figure 4) further shows DEITA with only 3K samples matches the full 300K pool.

3. **Data scaling law insight: more selected data can hurt alignment even from a high-quality pool.** The analysis in Figure 4 reveals that performance peaks then declines as dataset size increases, even when selecting from X_sota. This supports the paper's central claim that instruction tuning data has a limited pool of truly effective examples, underscoring the importance of automated selection.

---

## Weaknesses

### Fatal
None.

### Major

1. **The diversity condition is stated in a way that logically contradicts the paper's goal of promoting diversity.** The paper defines the Repr Filter condition as `d < τ` where `d` is the cosine distance (1 − cosine similarity) between a candidate sample and its nearest neighbor in the selected set. When `d` is *small*, the sample is *close* to an existing example — i.e., it is *redundant*, not diverse. A small `d < τ` condition selects samples similar to what is already selected, which is the opposite of diversity promotion. The same condition appears in Algorithm 1 (`IF d(x, S) < τ THEN add`). Since the method empirically works well (Repr Filter outperforms random and Instag Diversity), this is almost certainly a typo — the implementation likely uses `d > τ` or an equivalent logic. But as presented, the paper's method section is logically incoherent on a point central to the contribution. The authors must correct this, specify the actual threshold value, and explain how it was chosen. *(Verified: lines 293–295 and Algorithm 1, line 331.)*

2. **Missing ablation isolating the diversity filter's contribution in the full pipeline.** The final DEITA method combines score-sorting (by `c * q`) with the Repr Filter for diversity. The controlled studies in §3 separately test each dimension, but the paper never compares: select top-6K by `c * q` score **without** the diversity filter vs. the full method **with** the filter. This comparison is essential because: (a) the data pool X_sota is already described as diverse, so top-scoring samples may themselves be reasonably diverse; (b) the diversity studies in §3.4 were conducted on randomly ordered pools, not on score-sorted pools — the interaction between score ordering and the filter is unknown. Without this ablation, the contribution of the diversity component to the reported results is unsubstantiated. *(Verified: no such ablation exists anywhere in the paper.)*

### Minor

3. **The threshold value for the Repr Filter is truncated and its sensitivity is unexamined.** The threshold τ is shown as "$0." — truncated, likely a parser artifact. More importantly, the paper does not discuss how τ was chosen (e.g., validated on a held-out set, set heuristically) or how sensitive the results are to its value. This information is needed for reproducibility and to understand whether the method is brittle.

4. **Single-run evaluations without variance estimates.** All MT-Bench scores are reported as single numbers with no confidence intervals, standard deviations, or multiple seeds. The reported gaps are sometimes small (e.g., Evol Complexity 6.27 vs. Instag Complexity 6.18 on X_sota — a 0.09 difference). Given known noise in GPT-4-as-judge evaluations, providing variance would strengthen confidence in the conclusions. This is not fatal — single-run reporting is common in this literature — but it limits the reader's ability to assess significance.

5. **Distribution shift in scorer training not analyzed.** The complexity and quality scorers (LLaMA-1-7B) are trained on 2K examples from Alpaca (evolved variants) but applied to data pools from very different distributions (ShareGPT, UltraChat, WizardLM). The paper does not analyze how well the scorers generalize out-of-distribution. While the downstream results suggest the scorers are reasonably robust, a basic validation (e.g., Spearman correlation between scorer predictions and ChatGPT judgments on a held-out set from the target pools) would strengthen this methodological component.

6. **Data scaling curve (Figure 4) shows only the proposed method, with no baseline comparison.** The observed performance decline beyond 6K examples is interesting, but without a corresponding curve for random selection (or another baseline) on the same pool, it is unclear whether this decline is inherent to the data pool or specific to the DEITA selection strategy. This is relatively minor — the main claim about 3K matching 300K does not depend on this comparison — but it would improve the interpretation.

### Trivial

7. **The encoding input for diversity is underspecified.** The paper says "encode the sentence" using LLaMA-1-13B but does not specify whether this is the instruction only, the response only, or a concatenation of both. This should be clarified for reproducibility.

---

## Nice-to-Haves

- A sensitivity analysis of the threshold τ (e.g., varying τ and reporting downstream MT-Bench at a fixed budget of 6K) would demonstrate the method is not brittle.
- Reporting results over 2–3 random seeds for the main comparisons would improve statistical grounding.
- Including random selection in the data scaling curve (Figure 4) would clarify whether the peaking behavior is pool-inherent or method-specific.

---

## Removed Points

- **Complaint about threshold "0." being cut off / incomplete:** This is a PDF parser truncation artifact, not an author error. The removal of the specific "broken characters" complaint is per the hard rules. The *substantive* concern about how τ was chosen and its sensitivity (kept in Minor above) remains valid.
- **"The improvement over Instag Complexity is modest (0.09 on X_sota)" framed as a core weakness:** This compares single-dimension controlled studies, not the full DEITA pipeline. The paper's strength is the combined method; a small gap in one dimension of a controlled study does not threaten the paper's main claims. Kept only in weakened form as part of point #4 (lack of variance estimates makes it hard to assess this gap).
- **Claim that the paper should compare against reviewer-preferred methods or add more baselines:** Not applicable; the paper has reasonable baselines for its class.

---

## Novel Insights

The intersection of the inverted-diversity notation issue and the missing ablation creates a genuine puzzle: if the diversity condition as written (`d < τ`) promotes similarity rather than diversity, why does Repr Filter empirically outperform random and Instag Diversity? The most likely resolution is a sign-flip typo (implementation uses `d > τ`). If so, the controlled studies in §3.4 and the main results are both valid but the paper's textual description is wrong. If, alternatively, the text reflects the actual implementation, then the method's success must come from the score-sorting alone — but this is testable with the suggested ablation. Either way, fixing this inconsistency is the single most important revision.

A secondary observation: the paper's data-scaling result (3K selected samples matching 300K full data) is remarkably strong and, if robust, constitutes one of the most dramatic demonstrations of data efficiency in instruction tuning to date. The community would benefit from additional analysis of *what these 3K samples contain* — qualitative analysis or topic distributions could further inform the "what makes good data" question the paper sets out to answer.

---

## Suggestions

1. **Fix the diversity condition**: change `d < τ` to `d > τ` (or clearly define distance such that smaller values indicate greater diversity), report the actual threshold value, and explain how it was chosen.
2. **Add the missing ablation**: compare (a) top-6K by `c * q` score only vs. (b) full method with Repr Filter, on at least one backbone (e.g., LLaMA-1-13B on X_sota).
3. **Provide variance estimates**: at minimum, report scores for 2–3 seeds or cite established variance ranges for MT-Bench to help readers assess the significance of observed gaps.
4. **Clarify the encoding input**: specify exactly what text is fed to LLaMA-1-13B to obtain embeddings for diversity filtering.

---

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>