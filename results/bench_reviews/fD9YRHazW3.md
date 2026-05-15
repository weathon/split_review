Now I have a thorough understanding of the paper and all calibration anchors. Let me compose the final review.

---

## Summary

This paper introduces In-Context Watermarking (ICW), a novel paradigm that embeds detectable watermarks into LLM-generated text solely through prompt engineering — requiring no access to model weights, logits, or decoding processes. Four watermarking strategies are explored at different linguistic granularities (Unicode, Initials, Lexical, Acrostics), each with tailored detection procedures and a structured analysis of trade-offs. Experiments on GPT-o3-mini demonstrate near-perfect detection in both direct-prompt and indirect prompt injection settings, with competitive robustness under editing and paraphrasing, and text quality comparable to unwatermarked output.

## Strengths

- **Genuinely novel watermarking paradigm**: ICW is the first approach to embed watermarks through prompt engineering alone, leveraging LLMs' instruction-following and in-context learning rather than requiring decoding-level access. This opens watermarking to third parties who cannot modify model internals — a clearly motivated gap in the literature (Section 1, Section 3).

- **Systematic, well-structured design space**: The paper explores four ICW strategies (Unicode, Initials, Lexical, Acrostics) spanning character-level to sentence-level granularity, with each method accompanied by clear embedding and detection algorithms (Section 4). Table 1 provides an honest, qualitative trade-off analysis across LLM requirements, detectability, robustness, and text quality.

- **Compelling application scenario with empirical demonstration**: The Indirect Prompt Injection (IPI) case study — embedding watermark instructions into manuscripts to detect AI-generated peer reviews — is a timely, concrete, and high-impact use case. The paper shows that ICW works reliably in this long-context IPI setting with GPT-o3-mini (Table 2, IPI columns), with ROC-AUC ≥ 0.997 for all non-Unicode methods.

- **Robustness evaluation under realistic perturbations**: The paper tests against word deletion, word replacement, and LLM-based paraphrasing (Figure 3), showing that Initials, Lexical, and Acrostics ICWs maintain substantial detectability (AUC up to 0.924 for Lexical under paraphrasing), which is a meaningful stress test for prompt-based watermarks.

- **Finding that ICW scales with model capability is well-supported**: The contrast between GPT-4o-mini (near-chance performance for Initials/Acrostics) and GPT-o3-mini (near-perfect) cleanly demonstrates the core thesis that more capable models produce stronger watermarks — an observation with forward-looking implications (Table 2).

## Weaknesses

### Major

- **Negative class is exclusively human-written text**: All detection experiments (Table 2, Figure 3) use human-written text as the sole negative class. While human text is a valid instance of the stated null hypothesis ("generated without knowledge of k and τ"), the realistic deployment concern is distinguishing watermarked LLM outputs from *unwatermarked LLM outputs* (e.g., the same model answering the same query without the watermark instruction). LLM-generated text may have statistical properties (word frequencies, sentence-initial letter distributions) that differ from human text and partially overlap with the watermark signal, potentially inflating apparent detection performance. Including unwatermarked LLM outputs as an additional negative class would substantially strengthen the evaluation and is necessary to fully validate the method for practical use. This does not invalidate the core feasibility demonstration — the watermark signal is clearly present — but it limits confidence in the reported ROC-AUC and T@F values as predictors of real-world performance.

### Minor

- **IPI covert embedding feasibility not experimentally validated** (Section 3.2): The paper proposes embedding watermark instructions as white text, zero-font text, or similar invisible formatting within PDFs, but does not demonstrate that such covert instructions survive typical text-extraction workflows (copy-paste, PDF-to-text parsing, direct file upload). The IPI experiments appear to concatenate the instruction as plain visible text. The paper acknowledges this limitation ("a detailed investigation of attack and defense methods is left for future work"), and the core contribution (showing ICW works in long-context settings) does not depend on covert embedding. However, a minimal demonstration of survivability would meaningfully strengthen the case study.

- **Acrostics detection statistic estimates its null from the suspect text** (Section 4.2.4): The detector resamples sentence-initial letter sequences from the suspect text itself to estimate the null mean and variance. Under H₀ (natural, unwatermarked text), this should still provide reasonable Type I error control. However, under H₁ (watermarked text), the resampled null distribution is contaminated by the watermark bias, which may inflate empirical power estimates. Using an external reference corpus for null calibration would be more rigorous and is a straightforward fix.

- **LLM-as-a-Judge calibration concerns** (Section 5.2.3, Table 3): The unwatermarked GPT-o3-mini baseline receives near-perfect scores (Relevance 4.982, Quality 5.000, Clarity 4.994 on a 1–5 scale), suggesting the judge (gemini-2.0-flash) is poorly calibrated for discriminating quality at this level. While relative comparisons between methods remain informative, the raw scores are difficult to interpret and do not substitute for human evaluation.

### Trivial

- The "model-agnostic" description in the abstract should be qualified: performance depends strongly on model capability, as the paper itself demonstrates with the GPT-4o-mini vs. GPT-o3-mini comparison.

## Nice-to-Haves

- A human preference study with blinded raters comparing watermarked vs. unwatermarked outputs would ground the text quality claims more convincingly than LLM-as-a-Judge alone.
- Testing on a broader set of models (including open-source LLMs with varying instruction-following strength) would probe the practical boundaries of the "model-agnostic" claim.
- Providing side-by-side examples of watermarked vs. unwatermarked outputs for each ICW method would help readers assess perceptual quality beyond aggregate scores.

## Removed Points

These points were flagged for removal; treat them with caution.

1. **"The negative class used for detection evaluation is fundamentally inappropriate" (as a fatal/structural flaw)**: Softened to major. The paper's null hypothesis covers "text generated without knowledge of k and τ," which human text satisfies. Using human text as the negative class is a limitation but not a structural invalidation. The paper demonstrates that the watermark creates a detectable signal; adding unwatermarked LLM text would improve confidence in real-world performance estimates.

2. **"The IPI case study lacks basic feasibility evidence regarding covert instruction embedding" (as an evidential gap undermining the central contribution)**: Downgraded to minor. The paper explicitly scopes detailed attack/defense investigation as future work (Section 3.2). The core IPI contribution is demonstrating that ICW works when instructions are embedded in long documents, not proving a specific covert channel.

3. **"Unicode ICW omission from robustness figure while still reporting perfect scores" as deceptive**: Removed. The paper explains clearly that Unicode ICW has perfect copy-paste robustness but is fragile to LLM paraphrasing (Section 5.2.2). Reporting both the strengths (Table 2) and limitations (textual discussion) is honest, not deceptive.

4. **Formatting/style nitpicks, grammar, typos**: Removed per instructions — these are parser artifacts.

5. **Missing appendices/proofs**: Removed — appendices were stripped by the parser but exist in the original submission.

6. **Questions about model/tool/dataset existence or release status**: Removed — all cited models, tools, and datasets are assumed to exist.

## Novel Insights

The paper's most insightful contribution goes beyond the specific watermarking schemes: it establishes that LLM capabilities (instruction-following, in-context learning) that are typically viewed as safety or alignment properties can be repurposed as *watermarking substrate*. This inverts the conventional relationship between model providers and watermarking — rather than requiring providers to implement watermarking (which they may lack motivation to do), ICW empowers motivated third parties to watermark outputs of any sufficiently capable model. The experimental finding that ICW effectiveness sharply scales with model capability (GPT-4o-mini → GPT-o3-mini) suggests a future where more powerful models become simultaneously more watermarkable, creating a virtuous cycle for content provenance.

## Suggestions

- Add unwatermarked LLM-generated text (same model, same query distribution, without watermark instruction) as a negative class in at least one key experiment (e.g., Table 2 for GPT-o3-mini DTS). This is the single most impactful improvement and can be done without re-running all experiments.
- For the Acrostics detector, compute the null distribution from a reference corpus (e.g., the Canterbury Corpus used for Initials ICW calibration) rather than resampling from the suspect text, and report whether detection performance changes materially.
- Add a brief demonstration (even qualitative) that an invisibly-formatted watermark instruction in a PDF survives copy-paste or PDF-to-text extraction into an LLM prompt, or explicitly note this as an engineering requirement for deployment.

## Score and Decision

**Anchor comparisons:**

| Anchor | Avg Score | Decision | Comparison to ICW paper |
|--------|-----------|----------|------------------------|
| WindTalkers (US1UwMHHtS) | 3.00 | Reject | ICW is far stronger: clearer problem formulation, systematic method exploration, proper baselines, and a genuinely novel paradigm vs. WindTalkers' confusing framing and missing comparisons. |
| SPO (rU9ZA8mqxN) | 3.50 | Reject | ICW stronger: more novel idea, better evaluation scope, clearer contribution. SPO has limited novelty and thin experiments. |
| Bias Inversion (dZY5t9ZrUB) | 4.50 | Reject | Different focus (attack paper). ICW is more constructive and broadly applicable. |
| OpenStamp (DU5eTaQSHT) | 5.00 | Reject | ICW is more conceptually novel and explores a broader design space, though OpenStamp has more rigorous robustness evaluation. Comparable quality but ICW's paradigm-shift contribution edges ahead. |
| Benchmark Contamination (WFGxFzFDmQ) | 5.00 | Reject | Both are novel applications of watermarking. ICW has a broader scope (4 methods vs. 1) and more systematic exploration. Comparable overall quality. |
| WaterDrum (5GVfneFvhq) | 5.33 | Accept (Poster) | Both are novel and well-motivated. ICW has broader applicability and a more systematic design space exploration. |
| Catch-22 (pAeEzS4LwS) | 2.67 | Reject | ICW is far stronger across all dimensions. |

ICW makes a genuinely novel contribution (prompt-only watermarking) with systematic exploration across four methods, compelling experimental results, and a clear demonstration that the approach scales with model capability. The main limitation — using only human text as the negative class — is a real evaluation gap but does not invalidate the core feasibility demonstration and is straightforward to address. This paper sits above the 5.0 reject boundary and is comparable to or stronger than WaterDrum (5.33, Accept Poster). The broader applicability and systematic design space exploration merit a solid accept.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>