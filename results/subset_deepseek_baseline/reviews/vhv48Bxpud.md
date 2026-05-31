## Summary

The paper proposes StructZip, a framework that compresses large structured prompts (tables, tool descriptions, classification taxonomies) into parametric memory accessible via a single learned token. The approach first “unzips” structured data into a comprehensive set of natural language question-answer pairs, then fine-tunes the LLM on these pairs mixed with general SFT data. At inference, only the special token is needed, allowing the model to reason over the entire structured information with zero additional token overhead. Experiments on three tasks show that StructZip achieves high compression ratios while maintaining performance close to uncompressed prompts, significantly outperforming existing prompt-compression methods.

## Strengths

- **Important problem, underexplored setting**: The compression of structured prompts (dense, formatted, long) is a practical bottleneck for LLM-based agents, and existing methods focus on unstructured text. The paper rightly identifies this gap.
- **Simple and intuitive method**: Converting structured data into natural language QA pairs and fine-tuning with a special token is conceptually clean and easy to implement. The pipeline is clearly described and the idea of a compressed token as a memory key is elegant.
- **Strong empirical results on structured tasks**: StructZip consistently and substantially outperforms all compression baselines (LongLLMLingua, AutoCompressors, Gist, 500xCompressor) across text classification, table QA, and tool-use. On several datasets it matches or even exceeds the zero-shot performance of GPT-4o with the full prompt.
- **Informative ablation studies**: The paper investigates the effect of prompt length, the number of compressed tokens, coverage of QA pairs, and the use of parallel corpora — providing valuable insight into the method’s behavior.

## Weaknesses

### Major

- **The method requires per-prompt fine-tuning, severely limiting practical applicability**: StructZip is not “compression” in the usual sense of producing a shorter prompt that works with a frozen model. Instead, it fine-tunes the model on the specific structured data at hand. For any new structured prompt (different tools, different tables, different classification schemes) a new fine-tuning run is needed. This cost is not discussed, and the paper frames the approach as a general solution without addressing this critical limitation.
- **Unfair comparison against baselines, especially for tool-use**: In the xLAM task, the uncompressed baselines (including GPT-4o) are restricted to a retrieved subset of 20 tools because the full set of ~30 k tools exceeds context length. StructZip, by contrast, is fine-tuned on all tools and can “remember” them all. The claim of compressing “millions of tokens into one” is thus misleading: the 3 M‑token prompt does not appear in any baseline experiment. The actual compression ratio reported (13×) is much more modest and does not reflect the extreme claim in the abstract.
- **Lack of critical discussion of limitations**: The paper does not address the overhead of constructing QA pairs, the risk of catastrophic forgetting (mitigated only by mixing SFT data, but no evaluation), or the scalability to truly arbitrary structured data (e.g., very long schemas that cannot be exhaustively covered by QA pairs within the model’s context).

### Minor

- **Missing ablation: direct fine-tuning on raw structured data**: The paper does not compare against simply fine-tuning the model on the original structured prompt (without QA pairs). Such an experiment would isolate whether the QA decomposition is necessary or whether memorization of the raw schema suffices.
- **Incomplete experimental details**: The number of QA pairs generated per dataset, the mixing ratio with SFT data, training hyperparameters, and the exact initialization/training procedure for the special token are not provided. This makes reproducibility harder.
- **The unstructured‑prompt experiment (Section 5.3) is superficial**: The paper briefly tests on LongBench, claiming competitive results. However, the motivation is unclear (the method is designed for structured data) and the performance gains are marginal. This section feels tacked on and does not strengthen the main thesis.
- **Certain claims are overstated**: For example, “our compressed version trailing by only 0.6%” on TableBench is compared against GPT-4o, which is zero‑shot and not fine‑tuned; a fairer baseline would be a fine‑tuned Qwen2.5-7B without compression.

### Trivial

- Table 1 is difficult to read: several baseline entries have missing latency or compression ratio fields, and the layout (e.g., “Lat.(ms)”) is cramped.
- Some in‑text examples (e.g., “{{output the entire system}}”) use pseudo‑code that is not explained, making the concrete format of QA pairs unclear.

## Nice-to-Haves

- Discuss or evaluate an automated pipeline for QA pair generation (e.g., using the LLM itself to write diverse questions).
- Provide a head‑to‑head comparison with a version of the model fine‑tuned on the raw structured data (without QA decomposition).
- Include a clear statement of the method’s intended use case (repeated use of the same structured data) and acknowledge scenarios where it is not suitable.
- Measure the training overhead and inference latency on a more realistic scale to help practitioners assess the trade‑off.

## Novel Insights

The key insight that a single learned token can act as a memory key to retrieve entire structured representations from the model parameters is interesting, though the underlying technique (fine-tuning on derived QA pairs) is a straightforward application of existing machinery. The observation that one token is often sufficient, and that increasing the number of tokens beyond 10 yields diminishing returns, provides a useful design guideline for similar approaches.

## Suggestions

1. **Reframe the paper**: Clearly distinguish between “compression” (which typically implies a universal method applicable to new prompts without retraining) and “memory injection” (fine-tuning on the specific data). Adjust claims accordingly.
2. **Provide a more honest baseline comparison**: When the full structured prompt is too large for any baseline, state this limitation explicitly and explain why StructZip’s advantage is inherent to its design. Report the actual compression ratio used in experiments (e.g., the 13 × on xLAM) rather than “millions of tokens”.
3. **Add an ablation: fine-tuning on raw structured data**: This will demonstrate whether the QA decomposition is the crucial ingredient or whether the model could simply memorize the schema.
4. **Discuss scalability**: How does the method handle structured data with tens of thousands of items when the generated QA pairs themselves may exceed the training context length? What strategies can be used (e.g., packed training, curriculum)?

## Score and Decision

**MY FINAL SCORE:** <score>4.0</score>  
**MY FINAL DECISION:** <decision>Reject</decision>