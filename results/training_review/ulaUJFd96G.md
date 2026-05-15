Now I have a thorough understanding of the paper. Let me write the final consolidated review.

---

## Summary

HOMER proposes a training-free, hierarchical divide-and-conquer scheme for extending the context limit of pre-trained decoder-only LLMs (specifically Llama-2). Long inputs are divided into chunks, processed with shared affixes, progressively merged with token reduction at each step, and refined via upper-to-lower-layer propagation (propagative refinement). An optimized DFS computation order is claimed to achieve logarithmic memory scaling. Experiments on passkey retrieval, QA (QuALITY), language modeling perplexity, and memory efficiency are reported, comparing against RoPE-scaling baselines (PI, NTK, YaRN).

## Strengths

1. **Massive improvement on passkey retrieval at extended lengths**: HOMER achieves 80.4% retrieval accuracy at 32k tokens, while the best RoPE-scaling baseline (YaRN) reaches only 22.4% (Table 1, Section 4.1). This is a large, clean signal that the method is doing something fundamentally different from simple positional encoding extrapolation.

2. **Logarithmic memory scaling with >70% reduction**: The optimized computation order (Section 3.3) reduces peak GPU memory for 64k inputs by over 70% compared to all baselines (Table 4, Section 4.5). The memory efficiency is concretely demonstrated with numbers, and the DFS tree-traversal argument for logarithmic scaling is clearly motivated.

3. **Training-free and plug-in compatible with RoPE scaling methods**: HOMER requires no finetuning and can be stacked on top of PI, NTK, or YaRN. Combined with NTK, it improves QuALITY accuracy from 32.7% to 38.8% (Table 2), showing practical additive benefit.

4. **Ablation studies validate key design choices**: The paper ablates (a) calibrated attention-based pruning vs. random and uncalibrated pruning, and (b) propagative refinement vs. alternatives (Section 4.4, Tables 5–6). These experiments give empirical grounding for the claimed mechanisms, even if tested only on passkey retrieval.

5. **Novel application of token reduction to LLM context extension**: Adapting token pruning/merging (from vision transformers) to progressive chunk merging in LLMs is a genuine methodological contribution that opens a new direction distinct from prior independent-chunk-encoding approaches.

## Weaknesses

### Fatal
None.

### Major

- **Incomplete baseline comparisons weaken the headline claims.** The paper compares HOMER only to RoPE-scaling methods (PI, NTK, YaRN), which address a different subproblem (positional extrapolation). The Related Work section (lines 61–63) correctly identifies Unlimiformer as a *training-free* divide-and-conquer method, yet provides no comparison to it or any other training-free context extension approach (e.g., simple chunking + voting/routing). The passkey retrieval result (80.4% vs. 22.4%) is dramatic, but it is unclear how HOMER would fare against an alternative training-free method that also processes long inputs by chunking. The paper does not rule out the possibility that a simpler chunking scheme could achieve competitive results on these tasks. This is the most significant gap in the evaluation.

- **QA evaluation confounds method effectiveness with document access.** For QuALITY, baselines have their input clipped to fit their context limits, while HOMER receives the full document (Section 4.2). The 3% improvement (32.7% → 35.7%) may partly or entirely reflect that HOMER simply *sees more text*, not that its compression is superior. A controlled comparison (e.g., giving baselines the same information via chunking + voting or giving HOMER only the same clipped context) is needed to isolate the compression's contribution. Without this, the QA results provide weak evidence for the method's effectiveness at complex reasoning.

### Minor

- **Perplexity evaluation uses a nonstandard protocol that limits interpretability.** The paper measures perplexity by condensing prior context with HOMER and evaluating on subsequent 2k segments (Section 4.3). This is transparently described and is a natural adaptation for a compression method, but it is not standard language model perplexity (which evaluates each token against the full, uncorrupted preceding context). Lower perplexity under compression could reflect preserved information, but could also arise from the compression retaining only high-probability patterns. The comparison against baselines (which process unmodified but truncated context) is not apples-to-apples. The claim that "HOMER is the only method that maintains reasonable fluency" (line 180) is undersupported by this protocol.

- **Key hyperparameters are not specified in the main text.** The paper does not state chunk size, the number or ratio of tokens pruned per layer, the number of layers over which merging occurs, or how the "fixed number" of pruned tokens (line 91) is determined. While some of these details likely appear in the appendix (stripped by parsing), they are important for immediate reproducibility and for assessing the method's generalizability beyond the reported setup.

- **Efficiency analysis omits runtime/wall-clock costs.** The paper reports peak GPU memory (Table 4) and references speed analysis in the appendix (line 209), but the main text claims logarithmic memory scaling without discussing any time trade-off introduced by the DFS computation order. The method serializes computation that would otherwise be parallel, potentially trading memory for time. Presenting runtime numbers alongside memory in the main text would give a more complete picture of the method's practical efficiency.

- **Ablation studies are limited to passkey retrieval only.** The ablations for pruning criteria and propagative refinement (Section 4.4) are tested solely on the passkey retrieval task, which is simple and well-suited to the attention-from-last-token pruning signal. It is unclear whether the same design choices generalize to more complex tasks (QA, language modeling) or to tasks where important information is not near the end of a chunk.

### Trivial
None.

## Nice-to-Haves

- A controlled QA experiment where baselines receive the full document via a simple chunking + voting baseline, to isolate HOMER's compression benefit from simply seeing more text.
- Reporting variance or statistical significance measures for the QA results, given the modest improvement magnitude (3%).
- A brief discussion of why Unlimiformer (which the paper acknowledges as training-free) was not included as a baseline, and under what conditions comparisons to encoder-decoder methods would be fair.
- Per-task ablations (e.g., on QA and perplexity) to test whether the design choices validated on passkey retrieval generalize.

## Removed Points

These points were flagged by the reviewer but are removed for the following reasons:

- **"Training-free is misleading because HOMER requires self-attention computation on each chunk"** — The term "training-free" is standard in the literature, meaning no additional *training/finetuning* is required, not that the method has zero computational overhead. The paper consistently uses the terminology correctly (lines 7, 28, 59). This is a misunderstanding.
- **"45.8GB for Flash Attention 2 baseline seems high"** — This is speculation about baseline behavior, not a weakness of the paper. The paper reports empirically measured numbers.
- **"Proof is relegated to an appendix we cannot see"** — The appendix exists in the original submission; parsing strips it. Per review guidelines, missing appendix content is not a valid weakness.
- **"No confidence intervals or variance reported"** — Single-run evaluation on large-scale benchmarks is the norm in this setting. Requesting confidence intervals is a nice-to-have, not a valid weakness.
- **"The method uses attention-based pruning that requires running self-attention on each chunk" as a criticism of "training-free" framing** — Same as above; misunderstanding of the term.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a new interpretation or observation that the paper itself does not make.

## Suggestions

1. **Add at least one training-free chunking baseline.** The most impactful improvement would be to compare against Unlimiformer (adapted to decoder-only if needed) or a simple chunking + voting scheme on passkey retrieval and QA. Even a brief discussion of why such comparison is methodologically challenging would strengthen the narrative.
2. **Include a controlled QA experiment** where baselines receive the full document via sliding window or chunking + voting, to disentangle HOMER's compression effectiveness from the advantage of seeing more text.
3. **Report runtime alongside peak memory** in the main efficiency analysis (Table 4 or a companion table), to clarify any time-memory trade-off from the DFS ordering.
4. **Specify chunk size and pruning ratio in the main text** for reproducibility.
5. **Extend ablations to at least one additional task** (e.g., QA) to show that the pruning and refinement design choices generalize beyond passkey retrieval.

## Score and Decision

**Originality**: The hierarchical merging idea is novel and distinct from both RoPE scaling and independent-chunk-encoding approaches.  
**Importance of research question**: Addressing the context limit of pre-trained LLMs without training is practically important.  
**Claims support**: The passkey retrieval and memory efficiency claims are well-supported. The QA and perplexity claims are partially supported but have evaluative confounds.  
**Soundness of experiments**: Passkey retrieval experiments are sound. QA experiments are confounded by unequal document access. Perplexity uses a nonstandard but transparent protocol.  
**Clarity of writing**: The method description is clear and well-structured, though some hyperparameters are deferred.  
**Value to community**: The method is practical, training-free, and compatible with existing approaches, giving it immediate utility.

The paper makes a genuine methodological contribution with a strong result on passkey retrieval and clear memory efficiency. However, the evaluation is narrower than it should be given the claims — the omission of comparisons to other training-free chunking methods and the confounding in the QA setup are the principal concerns. The contribution is promising and the weaknesses are addressable, but in its current form the evaluation does not fully establish that HOMER is generally superior for long-context understanding.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>