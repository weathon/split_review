## Summary

This paper proposes AMADEUS, a training-free RAG-based framework for role-playing agents (RPAs) consisting of three components: Adaptive Context-aware Text Splitter (ACTS) that segments persona documents into optimally-sized, overlapping chunks with hierarchical context; Guided Selection (GS) that uses LLM calls to iteratively filter chunks for inferability of character attributes; and Attribute Extractor (AE) that identifies belief/value and psychological trait attributes from GS-selected chunks. The paper also introduces CharacterRAG, the first role-playing dataset designed explicitly for RAG-based RPA evaluation, containing 15 fictional characters, 976K written characters, and 450 QA pairs.

---

## Strengths

- **Clearly identified gap with targeted solution**: The paper articulates a precise failure mode of naive RAG in role-playing—over-reliance on low-relevance chunks when queries exceed explicit persona knowledge (Figure 1)—and directly addresses it through GS and AE. The "chunk duplication frequency" framing is an intuitive diagnostic.

- **CharacterRAG dataset**: This is a genuine contribution as there is no prior RAG-specific role-playing dataset. Human annotators manually cleaned wiki text to remove non-character-perspective artifacts, and the 450 QA pairs across six attribute categories are well-structured. Human evaluation of GS+AE outputs achieves Cronbach's alpha of 0.81–0.83, supporting internal consistency of the evaluation itself.

- **Strong MBTI/BFI results**: AMADEUS achieves 85% MBTI accuracy vs. 65–68.33% for all baselines, and 81.33% vs. 72–76% for BFI (Table 1, GPT-4.1 setting). The improvement on out-of-knowledge queries—the hardest part of the problem—is the most compelling demonstration of the method's value.

- **Multi-faceted experimental coverage**: Experiments span 3 LLMs, 3 embedding models, 4 RAG baselines, and 2 evaluation paradigms (in-knowledge QA and out-of-knowledge personality assessments), yielding a thorough empirical picture.

---

## Weaknesses

### Fatal
None.

### Major

1. **GS computational cost is unaddressed**: GS performs up to N=30 LLM (GPT-4.1) calls per query. Since GS and AE are both always implemented with GPT-4.1 regardless of the backbone RPA model, the reported Gemma3 and Qwen3 results still incur GPT-4.1 costs internally. This is a significant practical concern that the paper does not discuss: neither latency, nor cost per query, nor the viability of replacing GPT-4.1 with lighter models in GS/AE. A framework designed for deployment needs this analysis.

2. **Marginal improvement on the main CharacterRAG task**: In Table 4, the improvement of AMADEUS over Naive RAG in ACC is 1.34% for GPT-4.1 (91.33% → 92.67%), 1.56% for Gemma3 (86.44% → 88.00%), and 0.45% for Qwen3. While HS improves more meaningfully, the in-knowledge retrieval improvement—the primary purpose of RAG—is modest. The headline contributions are driven primarily by out-of-knowledge scenarios (MBTI/BFI), which are evaluated differently and against simpler ground truth.

3. **Methodological concerns with MBTI/BFI as ground truth**: MBTI type assignments sourced from crowdsourced personality votes on personality-database.com are used as the evaluation gold standard. MBTI has well-documented test-retest reliability limitations, and aggregating crowd votes for fictional characters adds a further layer of uncertainty. The paper does not discuss this limitation, nor does it assess sensitivity to ground-truth label noise.

4. **CharacterRAG's narrow scope**: All 15 characters are from Japanese-origin anime/manga, sourced from a Korean-language wiki (Namuwiki). This monocultural scope raises questions about whether the framework and dataset generalize to Western fictional characters, historical figures, or non-pop-culture personas—domains equally important for RPA deployment.

### Minor

1. **Hyperparameter motivation is thin**: N=30 and M=2 are stated but not ablated. The overlap coefficient ablation (Figure 4) is provided, but a similar analysis for N and M would strengthen the paper.

2. **Comparison against LightRAG and CRAG may be unreliable**: LightRAG achieves only 48% ACC on GPT-4.1, lower than the no-RAG baseline of 49.56%. CRAG achieves only 28.67% ACC for Qwen3. These baselines appear misconfigured or fundamentally ill-suited for the task, making AMADEUS's gains over them less informative. The paper acknowledges this but doesn't explore better-configured intermediate baselines.

3. **Potential evaluator bias**: LLM-based metrics (ACC, ACC_L, HS) are scored by GPT-4.1, while GS and AE also use GPT-4.1. This creates a structural tendency for the metric to favor GPT-4.1-mediated outputs. The paper does not control for or discuss this confound.

### Trivial
Figure 1's MBTI label list contains repeated types (ISTP appears three times) which appears to be a parser artifact.

---

## Nice-to-Haves

- A cost/latency analysis comparing AMADEUS to Naive RAG under practical deployment conditions, including a version using an open-weight model for GS/AE.
- Expanding CharacterRAG to include non-anime characters to test generalizability.
- Error analysis: qualitative breakdown of the ~15% of MBTI cases AMADEUS still gets wrong.
- Ablation over GS slot size M and iteration limit N.

---

## Novel Insights

The core insight—that RAG for role-playing requires not merely factual retrieval but *inferential* retrieval of contextual chunks from which personality traits and beliefs can be deduced—is genuinely useful. The observation that Naive RAG's chunk duplication frequency is higher and less uniform when queries fall outside explicit persona knowledge is a diagnostic contribution that connects retrieval quality to persona consistency in a principled way. The finding that graph-based RAG (LightRAG) and web-augmented RAG (CRAG) are ill-suited for persona-constrained role-playing due to entity ambiguity and external noise, respectively, provides useful negative guidance for practitioners.

---

## Suggestions

- Report and discuss per-query API cost for AMADEUS vs. Naive RAG to quantify the tradeoff.
- Add ablation of M (slot size) and N (maximum iterations) in GS.
- Explore replacing GPT-4.1 in GS/AE with a lighter open model to decouple the framework from proprietary systems.
- Report inter-rater statistics for the LLM-based metrics, or cross-validate with a different judge model.
- Expand dataset to at least one domain outside anime/manga to validate cross-domain generalization.

---

## Score and Decision

AMADEUS addresses a real and understudied problem—RAG for role-playing agents, especially for out-of-knowledge queries—and the personality-based evaluation paradigm (MBTI/BFI) is creative and largely compelling. CharacterRAG fills a genuine dataset gap. However, the practical cost of the GS procedure (30 GPT-4.1 calls per query) is unaddressed, the improvement over Naive RAG in the primary in-knowledge setting is small, the dataset scope is narrow, and the MBTI/BFI ground truth has validity concerns that go unacknowledged. The contributions are solid but bounded—more of an applied system paper than a research advance at the frontiers of the field—and several key questions about cost, generalizability, and evaluation methodology remain unresolved.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>