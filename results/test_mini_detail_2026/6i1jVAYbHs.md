Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes AtlasKV, a parametric framework for augmenting LLMs with billion-scale knowledge graphs using under 20GB VRAM. Two innovations drive the approach: (1) KG2KV, which converts KG triples into diverse query-key-value (QKV) training data with 2600× higher diversity than synthetic alternatives, and (2) HiKVP, a hierarchical key-value pruning algorithm that achieves sub-linear time and memory complexity O(∛M) in the number of triples compared to KBLaM's linear O(M). Experiments on three OOD datasets (Enron, ATLAS-CC-QKV, ATLAS-Pes2o-QKV) show AtlasKV substantially outperforms KBLaM on knowledge grounding accuracy and GPT-evaluated generation relevance while using orders of magnitude less GPU memory.

## Strengths

- **Genuine algorithmic contribution: HiKVP achieves sub-linear complexity.** Table 2 formally states AtlasKV's O((C_t ∛M + N)·N·D) time and O((C_m ∛M + N)·(N+D)) memory, translating the ∛M from the cluster size S = ⌈∛M⌉ into a concrete complexity reduction over KBLaM's linear O(M+N). This is a non-trivial engineering insight—organizing knowledge keys into a 3-level hierarchy where each level prunes to top-k before moving to finer granularity.

- **KG2KV data pipeline yields large and measurable diversity gains.** Table 1 reports a diversity ratio of 7.864% vs 0.003% for the synthetic method used by KBLaM—a 2600× improvement—while simultaneously cutting average token cost by more than half (165.7 vs 349.9). This quantifies why AtlasKV generalizes better: the KG's natural relational structure provides far more query patterns than fixed human-defined schemas.

- **Large and consistent accuracy gains across OOD datasets.** Table 3 shows AtlasKV (even with HiKVP pruning) consistently outperforms KBLaM by wide margins: e.g., on ATLAS-Pes2o-QKV with 10² triples, AtlasKV achieves 82.3% ACC@1 vs KBLaM's 25.5% (AtlasKV w/o HiKVP reaches 92.7%). The advantage holds across Enron, ATLAS-CC-QKV, and ATLAS-Pes2o-QKV, spanning KG sizes from 10⁰ to 10³.

- **Training efficiency advantage validated.** AtlasKV achieves superior results with 3K training steps while KBLaM uses 20K steps, and both use similarly sized training sets (20K samples). This suggests KG2KV data is not only more diverse but also more learnable.

## Weaknesses

### Major

- **Missing RAG accuracy comparison undermines the paper's central framing.** The paper repeatedly positions AtlasKV as an alternative to RAG (Abstract: "RAG methods... introduce substantial inference latency"; Introduction: "limitations of RAG"), but the accuracy experiments include ICL, KBLaM, and zero-shot only—no RAG baseline. ICL is described as "the basic knowledge augmentation paradigm used in RAG methods," but this conflates the retrieval and in-context steps. A simple dense retriever (e.g., Contriever or DPR) retrieving top-k triples and feeding them as context would be the most natural competitor. Without it, the claim that AtlasKV achieves "superior... effectiveness... compared to RAG methods" (line 60) is unsupported.

- **Figure 4 contains an internal inconsistency that undermines the scalability presentation.** The paper states (line 258): "when there are more than 100 triples in a KG, over 48GB VRAM is required [for ICL] and can not be run on the limited GPU memory." Yet Figure 4 shows ICL memory usage staying below 20GB even at 10⁹ triples. The complexity table (Table 2) lists ICL memory as O((MT+N)·(MT+N+D)), which would explode at 1B triples. If Figure 4 instead models ICL as retrieving a small fixed number of triples (the standard RAG pattern), this needs to be explicitly stated and the labeling corrected. As presented, the figure contradicts both the paper's own text and its complexity model. The core AtlasKV scalability claim (sub-linear < 20GB) does not depend on ICL's exact memory, but the inconsistency damages credibility.

- **Accuracy evaluation does not extend beyond 10³ triples.** Table 3 tests KG sizes from 10⁰ to 10³ triples. The billion-scale claim rests entirely on the memory plot (Figure 4); there is no accuracy or generation quality evaluation at 10⁴, 10⁵, or beyond. Showing that accuracy does not catastrophically degrade as KG size increases would substantially strengthen the paper.

### Minor

- **Primary metric is a proxy for downstream task performance.** The main knowledge grounding accuracy metric extracts post-softmax attention scores at layer 15 to measure which triple the model attends to most. This directly tests whether the model retrieves the correct triple from its parametric memory, but it is not standard QA accuracy. The GPTScore evaluation (Figure 5) partially addresses this by measuring generation relevance, but it is only reported for AtlasKV w/o HiKVP—the variant without the pruning that makes AtlasKV scalable.

- **Potential format confound for two of three OOD evaluation datasets.** ATLAS-CC-QKV and ATLAS-Pes2o-QKV are constructed from their respective KGs using the same KG2KV pipeline as the training data. While the KG domains differ from ATLAS-Wiki, the shared format means AtlasKV has been trained on data structurally identical to the evaluation data, whereas KBLaM trains on synthetic data with different formatting. The Enron dataset (where AtlasKV also outperforms KBLaM) partially mitigates this concern, but the format familiarity could inflate the reported margins.

- **No wall-clock latency measurements.** The paper claims sub-linear inference time but provides no runtime numbers. The HiKVP pipeline involves multiple CPU-GPU transfers (offloading and uploading keys at each hierarchy level), which could dominate actual wall-clock time even if the asymptotic complexity is favorable.

### Trivial

- Table 4 caption has a typo: "ATLAS-Pen2o-QKV" should instead refer consistently to "ATLAS-Pes2o-QKV."

## Nice-to-Haves

- Run accuracy evaluation at 10⁴–10⁵ triples to connect the billion-scale memory claim to actual performance at scale.
- Report wall-clock inference time for HiKVP to complement the complexity analysis.
- Evaluate on a standard knowledge-intensive QA benchmark (e.g., WebQuestions or a subset) with natural-language queries not pre-structured into the KG2KV format.

## Removed Points

- **"ICL memory usage in Figure 4 is physically impossible" (harsh critic's point #1 framed as fatal):** The harsh critic asserts this is a "fatal flaw" and "structurally flawed." I treat this as a Major inconsistency requiring clarification, not a fatal error—the core AtlasKV scalability claims (sub-linear complexity, <20GB for 1B triples vs KBLaM's >40GB at 100K) remain supported by the complexity analysis and the KBLaM comparison, independent of the ICL line.
- **"Evaluation does not measure LLM performance on knowledge-intensive tasks" (harsh critic's point #2, framed as evidential issue):** Overstated. The paper includes both attention-based accuracy and GPTScore generation evaluation, and the Enron dataset is an established benchmark from KBLaM. Moved to Minor as the GPTScore covers only the w/o HiKVP variant, which is a genuine limitation.
- **"KG2KV format shared between train and eval creates in-distribution advantage" (harsh critic's point #3):** Demoted to Minor. The Enron results (different format) show AtlasKV still outperforms KBLaM, so this is a partial confound, not a fatal flaw.
- **"Training and evaluation dataset same KG2KV transformation" (strength finder overclaims on generalization):** The strength finder calls the 72.8-point gap "direct evidence of superior generalization"—this is partially confounded by format sharing. Acknowledged and qualified.
- **Strength finder's praise of Figure 4 as primary evidence:** Kept as a qualified strength, but the inconsistency is now noted as a Major weakness.
- **Strength finder's "3K steps vs 20K" efficiency claim:** Kept as a valid strength with evidence from Table 3.
- **"Relation rewriting by unspecified LLM, cost not reported" (harsh critic):** This is a minor implementation detail; the paper references its analysis in the (stripped) appendix. Removed as a nitpick.
- **"HiKVP parameters seem chosen for desired complexity bound" (harsh critic):** Speculative. The setting S = ⌈∛M⌉ for 3 layers is mathematically natural for equal burden-sharing. Removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Clarify Figure 4 immediately.** State explicitly what "ICL" means in the figure: is it the memory of putting all M triples in context, or is it the memory of putting a small fixed number of retrieved triples (top-k) in context? The current presentation contradicts the paper's own text.
- **Add a RAG baseline to Table 3.** A simple dense retriever retrieving the top-5/10 most relevant triples and feeding them as ICL context would directly address the paper's positioning.
- **Report GPTScore for AtlasKV with HiKVP.** The current GPTScore evaluation only covers the w/o HiKVP variant; including the pruned version would show whether pruning preserves generation quality.
- **Run accuracy at 10⁴ triples** to bridge the gap between the small-scale accuracy evaluation and the billion-scale memory claim.
- **Add a brief limitations paragraph** acknowledging the KG2KV format overlap and the proxy nature of the attention-based metric.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak band (<3.5): SynthKGQA (3.33, Reject) — proposed a framework already used in prior work; low novelty. AtlasKV is clearly stronger.
- Middle band (3.5–7.5): KRLM (5.0, Accept) — complex KG reasoning architecture with unclear novelty over known ingredients; MLP Memory (5.0, Accept) — parametric memory replacement for RAG with limited contribution; LMLM (6.5, Accept) — novel pre-training paradigm with thorough evaluation.
- Strong band (>7.5): No directly comparable papers retrieved.

**Round 2 (Narrowing, bracket 4.5–7.0):**
- MLP Memory (5.0, Poster): Proposes parametric memory module to replace RAG. Similar framing to AtlasKV but contribution is more incremental (MLP as kNN-LM approximator vs AtlasKV's KG2KV+HiKVP). AtlasKV has more structural novelty but weaker evaluation breadth. AtlasKV is slightly stronger.
- Knowledgeable-R1 (5.5, Poster): RL framework for RAG robustness. Thorough evaluation across 5 datasets and 4 model sizes. AtlasKV has clearer algorithmic contribution but narrower evaluation. Comparable quality.
- LinearRAG (6.0, Poster): Scalable GraphRAG with linear complexity. Very clean evaluation on 4 standard benchmarks. AtlasKV has more novel approach (parametric memory via attention) but less rigorous benchmark coverage. AtlasKV is slightly weaker.
- LMLM (6.5, Poster): Novel pre-training paradigm. Broader and more thorough evaluation than AtlasKV across perplexity, FactScore, NLU, and forgetting. AtlasKV is notably weaker than this anchor.

**Round-1 bracket:** 4.0–6.5  
**Narrowing:** The paper is clearly above the 3.33 band, comparable to the 5.0–5.5 band, and below the 6.0–6.5 band. Positioned between MLP Memory (5.0) and Knowledgeable-R1 (5.5), with the Figure 4 inconsistency and missing RAG baseline preventing it from reaching the LinearRAG/LMLM tier.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>