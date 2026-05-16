Now I have all the information needed to write a thorough, evidence-based review.

---

## Summary

This paper proposes SensZOQ, a zeroth-order (ZO) fine-tuning method for LLMs that combines extreme static sparsity (updating only 0.1% of parameters) with 4-bit quantization. The key idea is that the sparse set of "sensitive" parameters can be derived from pre-training data gradients (C4) and transferred across downstream tasks without modification. The method enables fine-tuning of 7B-scale LLMs under 8 GiB of CUDA memory while outperforming full-model ZO fine-tuning, in-context learning, and ZO-based PEFT baselines across three LLM families and nine tasks.

## Strengths

- **Demonstration of extreme static sparsity (0.1%) for ZO fine-tuning with task transferability.** Figure 5a shows that sensitive parameters selected via C4 gradients maintain near-optimal accuracy down to 0.1% sparsity, while weight-magnitude baselines degrade sharply. Figure 5b confirms C4-derived masks achieve accuracy close to task-specific masks (within ~1–2 points). This is the paper's central empirical discovery and is well-supported.

- **Concrete memory achievement under 8 GiB for 7B models without system-level tricks.** Figure 1 directly benchmarks CUDA memory usage for Llama2-7B, showing SensZOQ stays under 8 GiB while full ZO FT and LoRA (with ZO) exceed it. This addresses a practical deployment barrier for on-device personalization.

- **Consistent empirical results across three LLM families and nine diverse tasks.** Table 1 reports results for Llama2-7B, Mistral-7B, and OPT-6.7B on SST-2, RTE, CB, BoolQ, WSC, WiC, COPA, WinoGrande, and WikiText-2 with 3 random seeds. SensZOQ consistently matches or outperforms ZO Full FT, ICL, and ZO-based PEFT baselines.

- **Practical comparison against smaller-model first-order fine-tuning.** Table 2 shows SensZOQ on OPT-6.7B (5.2 GiB) outperforms FO-Adam on OPT-1.3B (11.6 GiB) on several tasks, demonstrating the practical value of the memory-performance trade-off.

## Weaknesses

### Fatal
None.

### Major

- **Section 2.3 promises theoretical guarantees but the theorem statement is absent from the main text.** The paper outlines on line 34 that it will cover "theoretical guarantees" in Section 2.3, and line 76 begins "The theoretical support of sensitive parameters can be derived from the lens of SPSA gradient estimator and Fisher information matrix as follows:" — then the content cuts off with no theorem statement, equation, or interpretation. "Theorem 1" is referenced in Section 3.1 (line 87) but never stated in the main body. While some content may have been lost to the appendix (which the parser strips), the main text must be self-contained enough for a reader to evaluate the claim of theoretical grounding. This is a structural issue that undermines the paper's claim of "theoretical guarantees" — the authors must either state Theorem 1 and its intuition in the main paper or remove the claim.

### Minor

- **Missing wall-clock time measurements to support the static-vs-dynamic sparsity motivation.** The introduction argues that dynamic sparsity "reduces training iterations but not necessarily wall-clock time" and that static sparsity is preferable (lines 17–18). Yet no training latency or throughput data is reported for SensZOQ versus any dynamic sparsity baseline or ZO full fine-tuning. This leaves a key motivating claim untested. The paper would be stronger with even a simple timing comparison.

- **Memory profiling (Figure 1) only measures SensZOQ without comparing competing methods under matched conditions.** Showing, for example, that LoRA+4bit+ZO or Q+Prefix+ZO also do or do not fit under 8 GiB would strengthen the memory-efficiency argument.

- **The number of C4 examples used to derive the transferable mask is unspecified.** The paper (line 129) says "a small batch of C4 texts" but gives no batch size, leaving the procedure under-specified for reproduction.

- **No ablation isolating the effect of quantization.** The paper never compares SensZOQ (sparse ZO + 4-bit) against SensZO without quantization (sparse ZO in 16-bit). This would isolate the accuracy impact of 4-bit quantization from the sparsity benefit.

### Trivial

- **Figure 3 description is sparse.** The y-axis label ("Cumulative normalized gradient square values") appears only in the figure caption (line 104) and the text (line 89) could more clearly explain what is being plotted and why. The claim ">20× higher" on line 91 would benefit from a brief numerical illustration.

- **Accuracy values from Figures 5a/5b are not reported numerically in the text.** The text (line 270) says "the performance curve ... is near a flat curve" and "the gap ... is small" without providing the actual numbers, making the claim harder to assess precisely.

## Nice-to-Haves

- A brief "Limitations" paragraph discussing scenarios where C4-derived masks might fail (e.g., tasks requiring very different knowledge from pre-training data).
- Sensitivity analysis of the derived mask to the random seed or size of the C4 batch.
- Wall-clock training time comparisons against ZO full fine-tuning and a dynamic sparsity baseline.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. *Criticism that LoRA and Prefix baselines are unfairly evaluated with ZO-SGD* — The paper's Table 1 clearly labels the optimizer as ZO-SGD in column headers, and the comparison is appropriately situated within the ZO paradigm. The paper is about ZO methods; asking for FO baselines for these specific approaches would change the paper's scope from a ZO comparison to a ZO-vs-FO comparison. (Scope creep per instructions.)

2. *Hyperparameters not listed explicitly* — The paper cites prior work (Malladi et al., 2023a) for the standard ZO fine-tuning settings and uses the same codebase. This is standard practice.

3. *Criticism about Section 2.2 needing more empirical analysis* — The paper provides the relevant empirical analysis in Section 4.2, which is the appropriate place for experimental validation of the mask choice.

## Novel Insights

The reviews converge on a central tension: the paper's empirical contribution is solid and well-supported (the 0.1% static sparsity transfer finding is genuinely novel), but the claimed theoretical contribution is invisible in the main text. This suggests the paper should lean into its empirical strengths and either substantially restore the theoretical exposition in the main body or reframe its contributions as purely empirical. Additionally, the reviewers collectively identify that the paper's motivational claims about wall-clock time advantages of static over dynamic sparsity remain unverified, which is a gap that would take relatively little effort to fill but would meaningfully strengthen the practical narrative.

## Suggestions

1. Restore Theorem 1 and its interpretation to the main text (Section 2.3). At minimum provide the theorem statement and a paragraph of intuition. If the full proof belongs in the appendix, the main text should still convey the key insight.
2. Add wall-clock timing comparisons (SensZOQ vs. ZO full FT vs. a dynamic sparsity baseline) to support the static-sparsity motivation.
3. Include a SensZO-without-quantization (16-bit sparse ZO) ablation to isolate quantization's impact.
4. Specify the number/configuration of C4 examples used for mask derivation.
5. Report numerical accuracy values alongside the figures in Section 4.2.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>