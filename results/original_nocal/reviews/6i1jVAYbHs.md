Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper presents AtlasKV, a parametric framework for augmenting LLMs with billion-scale knowledge graphs using under 20GB VRAM. The method has two key components: (1) KG2KV, which converts KG triples into Q-K-V training/inference data with higher diversity than synthetic construction, and (2) HiKVP, a hierarchical key-value pruning algorithm that achieves sub-linear time and memory complexity during inference. Experiments show strong knowledge grounding accuracy on OOD datasets and GPU memory remaining under 20GB even for 1B triples.

## Strengths

- **Sub-linear memory scaling demonstrated to 1B triples**: Figure 4 empirically shows AtlasKV uses ≤20GB VRAM even for 1B triples, while KBLaM exceeds 40GB at just 10⁵ triples. The asymptotic complexity is formally stated as 𝒪((Cₜ∛M + N)·N·D) vs KBLaM's linear 𝒪((M+N)·N·D). This directly supports the core scalability claim.

- **Large-margin OOD knowledge grounding improvement**: Table 3 shows AtlasKV (3k steps) achieves 92.7% ACC@1 on ATLAS-Pes2o-QKV (10² triples) vs KBLaM's 25.5% (20k steps) — a +67.2 point gain. The improvement is consistent across all three OOD datasets and KG sizes.

- **KG2KV yields dramatically higher training-data diversity**: Table 1 reports KG2KV achieves a diversity ratio of 7.864% vs 0.003% for the synthetic method used in KBLaM, with lower average token cost (165.7 vs 349.9). This is a measurable, concrete improvement over prior practice.

- **HiKVP preserves accuracy while pruning at small scales**: Table 3 shows AtlasKV with HiKVP (128-64-16) on ATLAS-CC-QKV (10² triples) achieves 89.1% ACC@1 vs 96.4% without pruning, a loss of only 7.3 points — demonstrating the pruning is effective at the scales tested.

- **Ablation validates the entity-type design choice**: Table 4 shows removing event entities drops ACC@1 on ATLAS-Pes2o-QKV (10² triples) from 92.7% to 80.0%, and removing named entities drops it further to 49.0%, empirically validating the design of combining both entity types.

## Weaknesses

### Fatal

None.

### Major

- **Missing RAG baseline in accuracy and generation evaluations**: The paper discusses RAG and CAG in the complexity analysis (Table 2) and claims superiority over "RAG methods" in the introduction, but RAG is never evaluated in the accuracy experiments (Tables 3, 4) or the GPTScore evaluation (Figure 5). The only non-parametric baseline is ICL with *all* triples concatenated into context — which is not a reasonable instantiation of RAG, since a real RAG system would retrieve only relevant triples. Without comparison against a proper RAG baseline (e.g., dense retriever on KG triples + top-k ICL), the claimed advantage over RAG is unsubstantiated empirically.

- **Accuracy not validated at large KG scales**: The paper's main claim involves billion-scale KGs. However, accuracy results (Tables 3, 4) span at most 10⁴ triples, while the memory scaling (Figure 4) goes to 10⁹. There is no empirical evidence that HiKVP's hierarchical pruning preserves knowledge grounding accuracy at 10⁵–10⁹ triples. The cascade of pruning (root → inter → leaf) could amplify errors at larger scales, and the paper provides no analysis of pruning recall at any scale to mitigate this concern.

- **No evaluation on standard QA or knowledge-grounded generation benchmarks**: The evaluation uses datasets constructed by applying the same KG2KV pipeline to KGs (ATLAS-CC-QKV, ATLAS-Pes2o-QKV, Enron). While these are OOD relative to training, they do not correspond to standard KBQA or factual generation benchmarks (e.g., WebQuestionsSP, TriviaQA, NQ). The generation evaluation uses GPT-4o relevance scoring on these same KG-derived datasets, not standard metrics (EM/F1) on established benchmarks. This makes it difficult to assess whether the observed knowledge grounding accuracy translates to improved performance on real knowledge-intensive tasks.

- **KBLaM comparison confounded by training data differences**: KBLaM is trained on low-diversity synthetic data (0.003% diversity ratio) while AtlasKV uses the much richer ATLAS-Wiki-QKV (7.864% diversity). The paper does not control for this by training KBLaM on the same KG2KV data or by training AtlasKV on synthetic data matched to KBLaM's setup. The large performance gap (e.g., 82.3% vs 25.5% ACC@1 on ATLAS-Pes2o-QKV at 10² triples) may substantially reflect data quality differences rather than architectural advantages of AtlasKV over KBLaM.

### Minor

- **No recall analysis of HiKVP pruning**: The hierarchical pruning selects top-k at each layer, but the paper never reports recall — i.e., what fraction of truly relevant leaf-layer keys survive the cascade. Without this, it is unclear whether pruning at larger scales introduces systematic misses. This is especially important because the pruning decisions are based on learned projections (W̃_Q, W̃_K) whose generalization to unseen queries at coarse granularities is unanalyzed.

- **Near-perfect ACC@1 on several settings warrants discussion**: AtlasKV achieves 100% ACC@1 on 10³ triples for many conditions (Table 3). The paper notes an interesting training dynamic (appendix reference, removed by parser) but does not provide evidence against the possibility that the model overfits to KG2KV's pattern rather than learning genuine semantic retrieval. The near-perfect scores on settings with up to 1000 distractors are striking and could benefit from analysis (e.g., are failures correlated with semantically ambiguous triples?).

- **KG2KV conversion heuristics are plausible but not systematically justified**: The choices of which entity to mask, how to rewrite relations, and which entity types to use for keys vs values are grounded in ablation (Table 4) but not compared against alternatives (e.g., using raw relation strings, alternative masking strategies). The paper also does not evaluate whether the specific LLM-based relation rewriting step is critical or whether simpler heuristics suffice.

### Trivial

- Table 4's column headers appear garbled (repeated "10³" entries), likely a parser artifact that should be corrected in the original.
- The ACC@1/5 tables could benefit from clearer indication of which values are statistically significantly different given the reported standard errors.

## Nice-to-Haves

- **Scaled accuracy experiments**: Reporting ACC@1/5 and pruning recall at 10⁵, 10⁶ triples would substantially strengthen the scalability claim.
- **Hierarchy construction cost**: While inference complexity is the focus, discussing the offline cost (time, memory) of building the UMAP+GMM hierarchy for billions of keys would aid practical deployment assessment.
- **Incremental hierarchy updates**: KGs change over time; discussing how the triangle hierarchy could be updated incrementally (or acknowledging this as a limitation) would be valuable.

## Removed Points

These points were raised by reviewers but removed during consolidation:

- *"They do not compare to a simple LM fine-tuning on the same data"* — Outside the paper's scope; AtlasKV targets the parametric attention-integration paradigm (KBLaM-style), not standard fine-tuning.
- *"The hierarchical clustering step may require O(M log M) to build"* — This is a one-time offline cost; the paper's complexity claims specifically target inference, which is standard.
- *"Missing related works"* — Cannot be verified without external sources; all cited references are assumed to exist.
- *"Missing appendix content / proofs"* — The parser strips appendices; these exist in the original submission.
- *"Cannot be independently verified"* type criticisms of cited models/data — Rule: if the paper cites it, it exists.
- *Formatting nitpicks* (typos, whitespace, broken characters) — These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The two reviews confirm the paper's central contributions (KG2KV's diversity advantage, HiKVP's memory scaling) and converge on the same set of evaluation gaps (missing RAG baseline, no accuracy at scale, no real QA benchmarks). The most interesting cross-cutting observation is that the paper's strongest quantitative result (memory ≤20GB at 1B triples) and its weakest link (accuracy only measured up to 10⁴ triples) concern the same core claim: whether HiKVP preserves grounding accuracy at scale remains an open empirical question.

## Suggestions

1. **Add a RAG baseline**: Implement a standard retrieval pipeline (e.g., sentence-transformer dense retriever over KG triples, top-k ICL) and compare ACC@1/5 and generation quality against AtlasKV across KG sizes. This is the most impactful missing experiment.
2. **Scale accuracy experiments**: Report ACC@1/5 and pruning recall for KG sizes of 10⁵ and 10⁶ triples. Even if full 1B-scale accuracy evaluation is computationally prohibitive, showing a trend beyond 10⁴ would significantly strengthen the scalability claims.
3. **Control for training data when comparing to KBLaM**: Either train KBLaM on the same KG2KV data, or train AtlasKV on synthetic data, to isolate the effect of the architectural innovations from the data quality difference.
4. **Report HiKVP recall@k at each pruning stage**: Show what fraction of the ground-truth leaf-layer keys survive root → inter → leaf pruning. This would directly address concerns about error accumulation in the hierarchy.
5. **Evaluate on at least one standard QA benchmark**: Even a small-scale evaluation (e.g., a subset of WebQuestionsSP with KG triples from Wikidata) using standard metrics (EM/F1) would anchor the results to a familiar reference point for the community.

## Score and Decision

**Originality (7/10)**: HiKVP is a genuinely novel approach to scaling parametric KG integration, and KG2KV is a practical improvement over synthetic data construction.  
**Importance (8/10)**: The problem of integrating billion-scale KGs into LLMs efficiently is timely and relevant.  
**Claims well-supported (5/10)**: Memory scaling is well-supported; accuracy and generalization claims are supported at small scales but lack validation at the claimed billion-scale or on standard benchmarks.  
**Soundness (6/10)**: The methodology is sound but the evaluation has significant gaps (missing RAG baseline, no accuracy at scale, confounded KBLaM comparison).  
**Clarity (7/10)**: Well-structured and clearly written; diagrams effectively communicate the approach.  
**Value to community (7/10)**: The method is likely to be useful and the KG2KV + HiKVP pipeline is reproducible from the description.

The paper presents a clever, practical method with a clear advance over the KBLaM paradigm. However, the evaluation gaps — particularly the missing RAG baseline, absence of accuracy results at the claimed billion-scale, and lack of standard benchmark evaluation — mean the paper's strongest claims are empirically underdetermined. These are addressable weaknesses, but they are significant enough that the paper in its current form does not fully substantiate its central selling point of "billion-scale KGs in 20GB VRAM" as an integrated claim (memory + accuracy).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>