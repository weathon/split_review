Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper introduces HOMER (Hierarchical cOntext MERging), a training-free method for extending the context length of pre-trained LLMs. HOMER divides long inputs into chunks, attaches shared prefixes/suffixes to each chunk, progressively merges adjacent chunks with token reduction, reuses position IDs, and employs propagative refinement. An optimized computation order achieves logarithmic memory scaling. Experiments on passkey retrieval (80.4% accuracy at 32k tokens vs. 22.4% best baseline), question answering (3% improvement over plain Llama, 38.8% with NTK), and perplexity (stable up to 64k) demonstrate the method's effectiveness, along with >70% peak GPU memory reduction.

## Strengths

- **Passkey retrieval success at 8× context length with a large margin.** Section 4.1 reports 80.4% accuracy at 32k tokens vs. the best RoPE-scaling baseline (YaRN) at 22.4%. This is a direct, clean demonstration that HOMER enables pre-trained LLMs to use long contexts effectively without finetuning. The gap is far too large to be explained by noise.

- **Peak GPU memory reduced by >70% for 64k inputs compared to all baselines.** Section 4.5 documents this reduction while baselines (Plain Llama, PI, NTK, YaRN) all consume the same high memory. The optimized computation order provides logarithmic memory scaling, a concrete algorithmic advantage over quadratic-attention methods.

- **Orthogonal and complementary to RoPE-scaling methods.** Multiple experiments show HOMER+YaRN outperforms HOMER alone (passkey retrieval), HOMER+NTK improves over HOMER alone (QA accuracy: 38.8% vs. 35.7%), and HOMER+YaRN yields lower perplexity. This demonstrates the method is not merely an alternative but a compatible add-on.

- **Ablation studies validate the key internal design choices.** Section 4.4 shows that calibrated attention-based pruning outperforms random pruning, and propagative refinement outperforms alternative refinement strategies (per-layer significance, random). These ablations provide empirical grounding for the method's components.

- **Clear and motivated method design.** The paper explains the motivation for each design decision: why affixes are attached (ensuring all chunks see instruction/ending tokens), why position IDs are reused (avoiding underperformance of scaled RoPE at large factors), and why hierarchical merging is preferred over independent chunk processing (richer cross-chunk representations).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No comparison to any training-free chunking baseline.** The paper cites Unlimiformer (line 63) as a training-free divide-and-conquer method but compares only against RoPE-scaling baselines (PI, NTK, YaRN), which are not chunking-based. Without a comparison to at least one chunking-based approach (even a simple independent-encoding baseline), it is difficult to isolate whether HOMER's gains come from hierarchical merging specifically or from the general benefits of chunking + token reduction. The paper acknowledges Unlimiformer as related work and explains its baseline choice based on Flash Attention 2 compatibility (line 59), which is reasonable but does not fully address this gap.

- **Position ID reuse is asserted but not analyzed.** Section 3.1 states that position IDs are "reused across different chunks" and that "for affixes, we ensure that corresponding tokens in different chunks are assigned the same ids." This is a significant departure from standard practice (where position IDs are globally sequential or scaled). The paper provides no analysis or targeted experiment to validate that the model can correctly distinguish tokens with identical position IDs but different semantic content. While the overall empirical results support that the approach works, a dedicated probe or controlled experiment would strengthen this design choice.

- **Propagative refinement ablation is limited to passkey retrieval.** The ablation (Section 4.4) validates propagative refinement only on the passkey retrieval task. Showing its effect on QA accuracy or perplexity would strengthen the claim that upper-layer pruning decisions reliably identify important tokens for lower layers across diverse tasks.

- **Some important experimental hyperparameters are not reported in the main text.** Chunk size, number of tokens pruned per layer, number of layers before merging, and exact affix lengths are absent from the main paper (likely deferred to the appendix). These should be summarized at least briefly for readers to gauge implementation feasibility.

### Trivial
- None.

## Nice-to-Haves

- A controlled experiment validating position ID reuse (e.g., a test where the model receives a sentence with duplicated position IDs and must demonstrate correct semantic understanding).
- Comparison to a simple chunk-encode-merge baseline (e.g., independent chunk encoding with average-pooled representations) to isolate the benefit of hierarchical merging.
- An analysis of what types of tokens are disproportionately dropped during pruning (e.g., rare or semantically critical tokens) to ensure the compression is not overly lossy.
- Wall-clock time comparison alongside the memory comparison (the paper mentions speed in an appendix reference).

## Removed Points

These points were flagged during review but are not valid criticisms of the paper; they are listed here for transparency.

- **"Affix duplication confounds passkey retrieval"** — REMOVED. This reflects a misunderstanding of the affix attachment mechanism. The paper states (line 86) that the prefix is the *initial* part of the entire prompt and the suffix is the *concluding* part — these are shared across chunks but are fixed instruction/conclusion tokens, NOT overlapping boundary content between adjacent chunks. The passkey (a random number) is embedded in the text body and appears in exactly one chunk's body. The critic's scenario ("the suffix of chunk A and the prefix of chunk B") does not match the paper's description. The affix duplication only affects shared instruction/conclusion tokens, and the paper explicitly averages these duplicates at merge time (line 98).

- **"QA improvement could be due to full document access"** — REMOVED. This IS the purpose of context extension. Baselines are truncated (line 165) because they cannot handle longer contexts. Comparing a method that processes the full document against methods that truncate is the correct evaluation of whether context extension helps.

- **"Perplexity protocol makes it unclear whether full past is compressed"** — REMOVED. The paper clearly states (line 176): "preceding contexts are condensed with HOMER, and the perplexity of the subsequent segment is deduced based on these compressed contexts." This unambiguously describes compression of the full preceding context, not a sliding window.

- **"3% QA improvement could be within noise"** — REMOVED. The paper reports 32.7% → 35.7% (3.0 absolute points, ~9% relative improvement). For a task like QuALITY, this is a meaningful difference. Combined with HOMER+NTK reaching 38.8% (6.1 point gain), the improvement is consistent and non-trivial.

- **"Claim that token reduction is 'first work to apply to extend context limit' is narrow"** — REMOVED. The paper (line 66) qualifies this claim with "To the best of our knowledge," which is standard academic phrasing for novelty claims. The sentence correctly identifies the domain (extending context limit of LLMs) and acknowledges vision transformer precedents.

- **Various formatting/style nitpicks and speculative concerns** — REMOVED per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's primary concern (affix confound) is factually incorrect upon close reading of the method description. The remaining valid criticisms are well-understood minor gaps (missing chunking baseline, unanalyzed position ID reuse) rather than novel observations.

## Suggestions

1. **Add a chunking-based baseline.** The most actionable improvement: compare against a simple independent-encoding baseline (encode each chunk separately, then concatenate or average representations at the end) to isolate the benefits of hierarchical merging and token reduction.
2. **Include a targeted experiment validating position ID reuse.** For example, test whether the model can correctly answer a question that requires distinguishing two tokens with the same position ID but different content.
3. **Briefly summarize key hyperparameters in the main text** (chunk size, pruning rate per layer, affix length) for quick reference.
4. **Extend the propagative refinement ablation** to at least one additional task (e.g., QA) to confirm the pattern observed in passkey retrieval generalizes.

## Score and Decision

Based on my assessment:

- **Originality**: The hierarchical merging + token reduction combination for extending LLM context without training is novel. The optimized computation order (logarithmic memory) is also a genuine contribution.
- **Importance of research question**: Extending LLM context limits without expensive finetuning is practically significant.
- **Claims supported**: The core claims (effective context extension, memory efficiency, compatibility with RoPE methods) are well-supported by the evidence. The headline passkey result is clean — the affix confound concern does not hold up under scrutiny.
- **Soundness of experiments**: The experimental design is sound. Passkey retrieval, QA, perplexity, and memory measurements cover the relevant dimensions. Ablations validate key design choices.
- **Clarity of writing**: The paper is well-structured and clearly written, with good motivation for each design decision.
- **Value to community**: A training-free context extension method with significant memory savings is practically valuable. The method's compatibility with RoPE-scaling methods makes it deployable on top of existing techniques.

There are no fatal or major weaknesses. The remaining concerns (missing chunking baseline, position ID analysis) are minor points that can be addressed without changing the paper's core contribution.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>