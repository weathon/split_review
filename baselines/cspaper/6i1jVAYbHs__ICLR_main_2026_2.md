---
job_id: 4189d0af-005a-429b-afdb-65b5737429c6
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 6i1jVAYbHs.pdf
paper: AtlasKV: Augmenting LLMs with Billion-Scale Knowledge Graphs in 20GB VRAM
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on LLM knowledge augmentation, attention-based memory integration, scalable inference, and learning with knowledge graphs.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion, and it presents a concrete method with empirical validation, despite several important weaknesses.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, instructions targeting automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes AtlasKV, a parametric approach for augmenting LLMs with very large knowledge graphs by converting KG triples into key-value style representations and injecting them into attention layers. The method combines a data construction pipeline, KG2KV, which rewrites KG triples into query-key-value training examples, with a hierarchical pruning mechanism, HiKVP, intended to reduce the memory and compute cost of attention over large external knowledge stores. The paper reports improved knowledge grounding and answer relevance over KBLaM and prompt-based baselines, while claiming sub-linear scaling in memory and time with respect to KG size.

## Strengths
The paper tackles an important problem. There is real value in exploring alternatives to retriever-heavy RAG and retraining-based parametric adaptation, especially for settings where the external knowledge source is structured and very large. The motivation in **Figure 1** is simple but effective, because it clearly positions AtlasKV relative to non-parametric retrieval and retraining-based parametric methods, and makes the intended practical niche of the method easy to understand.

The central design has a coherent systems angle. The combination of KG2KV and HiKVP is not just a random bundle of tricks; the former addresses how to represent KG triples in a form compatible with attention-based injection, and the latter addresses the obvious scaling bottleneck of attending over huge KV banks. The pipeline in **Figure 3** helps the reader understand the root/intermediate/leaf pruning flow and the CPU/GPU movement, which is central to the paper’s scalability claim.

The empirical gains over KBLaM on the reported OOD knowledge-grounding benchmarks are substantial. In **Table 3**, the differences on ATLAS-Pes2o-QKV and ATLAS-CC-QKV are not marginal, they are large. For example, on ATLAS-CC-QKV with \(10^3\) triples, AtlasKV (128-64-16) reports ACC@1 of 61.8 versus 12.7 for KBLaM at 3e3 steps; on ATLAS-Pes2o-QKV with \(10^2\) triples, AtlasKV reports 87.3 versus 25.5. Even allowing for some caution about dataset design, these are strong deltas and they support the claim that the KG-derived training data has better out-of-distribution generalization than the synthetic scheme used in KBLaM.

The ablation in **Table 4** is useful and supports one concrete design choice in KG2KV. The degradation when dropping either named entities or event entities suggests that the data construction strategy is not arbitrary. This is one of the better parts of the paper empirically, because it tries to explain why the training signal helps.

The paper also does a decent job of exposing trade-offs instead of hiding them entirely. The appendix discussion around latency versus scalability, together with **Table 11** and **Figure 7**, shows that the authors are at least aware that pruning and CPU-GPU shuttling are not free.

## Weaknesses
1. **The main scalability claim is only partially supported, because the paper focuses on VRAM complexity while sidestepping the full end-to-end cost of building and serving the KGKV memory.**  
   The headline claim in the title and abstract is “billion-scale knowledge graphs in 20GB VRAM,” and **Figure 4** indeed suggests low GPU memory usage at inference. But this framing is narrower than the problem the paper claims to solve. AtlasKV requires offline sentence embeddings for all keys and values, hierarchical clustering over the key bank, storage of multi-level indices, and in many cases relation rewriting through an external LLM, as described in **Section 4.1**, **Page 5**, and the reproducibility/appendix sections. These are not side details, they are part of the method.  
   Why this matters: if the practical message is “we can augment an LLM with a 1B-triple KG cheaply,” then the relevant quantity is not just peak VRAM during attention, but the total preprocessing, storage, indexing, CPU memory, and runtime I/O burden. The paper is honest in **Appendix F.2** that HiKVP introduces substantial latency due to CPU-GPU transfer, with **Table 11** showing AtlasKV is slower than AtlasKV without HiKVP. That makes the “efficient” framing somewhat slippery. A stronger paper would report end-to-end storage footprint, preprocessing time, CPU RAM usage, and actual inference throughput, not only a favorable GPU-memory slice.

2. **The mathematical presentation around complexity is sloppy and in places inconsistent, which undermines confidence in the formal claims.**  
   The paper claims on **Page 4** that AtlasKV has time and memory complexity scaling as \( \mathcal{O}((C_t \sqrt[3]{M}+N)\cdot N \cdot D) \) and \( \mathcal{O}((C_m \sqrt[3]{M}+N)\cdot (N+D)) \), but **Table 2** later lists AtlasKV as \( \mathcal{O}((C_t \sqrt{M}+N)\cdot N \cdot D) \) and \( \mathcal{O}((C_m \sqrt{M}+N)\cdot (N+D)) \), using \(\sqrt{M}\) rather than \(\sqrt[3]{M}\). This is not a typo one can just shrug off, because the whole paper leans heavily on the sub-linear scaling story.  
   There are other notation issues. In **Section 3.2**, \(\bm{k}^{(l)m}, \bm{v}^{(l)m}\in \mathbb{R}^{M\times D_E}\) is odd for the \(m\)-th key-value pair, which should presumably be vectors in \(\mathbb{R}^{D_E}\), not matrices indexed by the whole memory size \(M\). Likewise, the text around the hierarchical sizes on **Page 6** gives \(M_R=\left\lceil\left\lceil M^{2/3}\right\rceil M^{-1/3}\right\rceil\), which simplifies roughly to \(M^{1/3}\), but the indexing and derivation are not cleanly presented in the main paper.  
   Why this matters: the theoretical story is not decorative here, it is the main justification for the method’s scalability. When the exponents and tensor shapes wobble, the reader is left wondering which claim is the real one.

3. **Equation-level exposition is not sufficiently precise for a method whose core novelty is in attention manipulation.**  
   The reformulation from rectangular attention to the weighted two-part form in **Equations (3) to (6)** is intuitive, but the main paper delegates the equivalence proof to the appendix and does not fully specify implementation details that affect behavior. For example, in **Equation (3)** the KG and sequence parts are normalized separately and then mixed by \(\lambda_{kg}\) and \(\lambda_{seq}\). In principle this is equivalent to a joint softmax if the logits are exactly preserved, but the paper later prunes the KG side in **Equation (8)** and replaces \( \lambda_{kg} \) with \( \tilde{\lambda}_{kg} \). The exact normalization after pruning is only loosely described. Is \( \tilde{\lambda}_{kg} \) computed from the pruned logits only, and if so how is the mismatch with the original full-memory partition handled?  
   Similarly, **Equation (11)** is awkwardly defined:  
   \[
   \mathrm{logits}_{kg}=\mathrm{TopK\text{-}logits}(\mathrm{Softmax}(\mathrm{logits}_{kg_L}),k_L)
   \]
   which appears to select logits according to top-\(k\) softmax scores. But logits and probabilities are different objects, and selecting top-\(k\) by softmax score is equivalent to selecting top-\(k\) by logits only under monotonicity, while the subsequent use of these “logits” in attention and weighting is not carefully stated.  
   Why this matters: a paper centered on custom attention should not leave the normalization and pruning semantics fuzzy. These choices affect both correctness and reproducibility.

4. **The empirical evaluation is narrower than the paper’s claims, especially regarding baselines.**  
   The paper frames AtlasKV against “RAG methods” and against parametric adaptation more broadly, but the actual comparisons are mostly to ICL and KBLaM, with CAG appearing only in the complexity table and not in the empirical result tables or plots. This is visible in **Section 5.1**, **Table 2**, **Table 3**, and **Figure 5**. If the claim is that AtlasKV is a practical alternative to non-parametric knowledge augmentation, then stronger retrieval-based baselines should be included in the main results, ideally with realistic retrieval budgets and latency-quality trade-offs.  
   Why this matters: without stronger non-parametric baselines, the reader mainly learns that AtlasKV outperforms KBLaM on these datasets and avoids stuffing the entire KG into context. That is interesting, but it is not the same as demonstrating superiority over modern KG-aware retrieval pipelines.

5. **The evaluation metrics are too indirect for some of the headline claims, and parts of the setup risk overstating generalization.**  
   The “knowledge grounding” metric in **Section 5.2** is derived from averaged KG-part attention scores at the 15th layer, and then ACC@1 / ACC@5 are computed from those scores. This is not a standard end-task QA metric; it is a proxy for retrieving the intended fact according to internal attention. That can be informative, but it is not the same as showing that the model answers correctly. The generation evaluation in **Figure 5** then uses GPT-4o scoring of answer relevance, which is again indirect and potentially noisy.  
   Why this matters: when both core evaluations are proxies, the paper needs especially careful triangulation. I would have liked to see exact-match or factual accuracy on decoded answers in the main paper, or at least stronger evidence that attention-based retrieval accuracy at one layer tracks actual answer correctness. Right now the paper is a bit too eager to treat internal attention selection as if it were equivalent to successful knowledge use.

6. **The claimed advantage of “no retraining when adapting to new knowledge” is somewhat overstated.**  
   The paper repeatedly contrasts AtlasKV with traditional parametric methods that require retraining for new knowledge, for example in the abstract, **Figure 1(c)**, and **Section 1**. But AtlasKV still relies on a learned projection interface trained on KGKV data, and adaptation to new knowledge is “training-free” only after one has already committed to the KG2KV representation, encoder choice, clustering scheme, and learned attention heads. This is not a fatal issue, but the wording is stronger than the actual guarantee.  
   Why this matters: the distinction between “no retraining per new KB after the interface is learned” and “training-free knowledge integration” is important. The latter sounds more magical than what the method actually delivers.

7. **Flattening the KG into independent triples is a real limitation, and the paper underplays how much of the graph signal is discarded.**  
   The authors acknowledge this only in **Appendix J**, where they state that KG2KV “flattens” the KG and blocks multi-hop reasoning capability. That limitation is more central than the paper admits in the main body. The whole point of using a KG rather than a text corpus is not just storing isolated facts, but exploiting relational structure. Yet the main method turns \((h,r,t)\) into local templates and clusters key embeddings; explicit graph topology is gone.  
   Why this matters: this affects what kind of “KG augmentation” AtlasKV really offers. The current method is better described as triple-memory augmentation than graph-structured reasoning. That does not invalidate the paper, but it substantially narrows the conceptual contribution.

8. **Some claims about efficiency and training economy are not normalized fairly across methods.**  
   In **Table 3**, AtlasKV is highlighted for achieving strong results with only 3e3 steps, while KBLaM is shown at both 3e3 and 2e4 steps. But the training data are different by construction, and the comparison blends method and dataset changes together. The paper argues this is precisely the point of KG2KV, which is fair, but then the conclusion should be phrased as “the AtlasKV recipe is more effective,” not cleanly “the architecture is more efficient.”  
   Similarly, **Table 1** compares diversity ratio and token cost between “Synthetic” and “KG2KV,” but the diversity metric is highly tied to how enquiry attributes are defined, and the token-cost accounting ignores the broader offline preprocessing burden.  
   Why this matters: several of the paper’s strongest practical claims come from composite comparisons in which multiple knobs change at once.

## Questions
1. The complexity claim needs cleanup. Which is the correct dependence in the main method, \( \sqrt[3]{M} \) or \( \sqrt{M} \)? Please correct the discrepancy between **Page 4**, **Appendix D**, and **Table 2**, and provide one clear derivation in the main paper.

2. Please clarify the tensor shapes and indexing in **Section 3.2**. For example, for a single memory item \(m\), should \( \bm{k}^{(l)m}, \bm{v}^{(l)m} \in \mathbb{R}^{D_E} \) rather than \( \mathbb{R}^{M \times D_E} \)? Several expressions around memory representation are hard to parse as written.

3. In **Equations (8) and (11)**, how exactly is \( \tilde{\lambda}_{kg} \) computed after pruning? Is it normalized only over the retained leaf logits, or is there an approximation to the full KG mass? A precise formula would increase confidence that the pruned attention remains a principled approximation.

4. Can the authors provide end-to-end system statistics for a large KG setting, including offline embedding time, clustering time, CPU RAM usage, disk footprint, and tokens or API cost for relation rewriting? This would help validate the practical significance of the “1B triples in 20GB VRAM” claim.

5. A stronger empirical comparison to modern retrieval-based KG augmentation would improve the paper substantially. If such results exist, especially under matched latency or memory budgets, they could change my assessment positively.

6. Can the authors show a tighter connection between the attention-based grounding metric and actual QA correctness, ideally in the main paper? Even a correlation analysis between ACC@1/ACC@5 and answer exactness would help.

7. Since **Figure 5** uses GPT-based relevance scoring, can the authors clarify the prompt robustness and whether there was any calibration against human judgments or exact-match metrics for a subset?

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)

## Details Of Ethics Concerns
The concerns are limited, but worth flagging. The paper states in **Section 7** that it uses public datasets including Enron and ATLAS-family resources, and that it complies with model/API terms. However, when scaling a system that stores and injects large external knowledge into model attention, privacy and legal issues depend heavily on the provenance of the underlying KG and whether personal or copyrighted content is embedded into the external memory. This is particularly relevant for corpora like Enron and for web-scale KG extraction pipelines mentioned in **Section 3.1**. I do not see an immediate ethical violation in the paper, but a brief discussion of data provenance, retention, and whether KG memories can expose sensitive facts would make the paper more responsible.

## Soundness Rating
2: fair. The core idea is plausible and supported by experiments, but the mathematical presentation has notable inconsistencies and the empirical support for some broad claims is incomplete.

## Presentation Rating
2: fair. The paper is readable at a high level and some figures help, but the notation, equations, and several claims need tightening; the writing also contains many grammatical issues and overstatements.

## Contribution Rating
3: good. Despite the caveats, the paper asks an important question and presents a meaningful combination of ideas for scalable KG-to-attention integration that seems useful to the community.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a real idea and nontrivial empirical signal, especially against KBLaM, but the technical presentation and evaluation breadth are not where they should be for a fully convincing acceptance.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main technical claims and experimental evidence carefully, though some implementation details remain underspecified in the paper.