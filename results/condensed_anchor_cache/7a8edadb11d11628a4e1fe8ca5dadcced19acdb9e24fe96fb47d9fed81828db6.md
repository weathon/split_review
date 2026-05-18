- Decision: Reject
- Scores: 3, 3, 5, 3

## Merged Review

### Summary

The paper introduces PromptNER, a prompt-based algorithm for few-shot and cross-domain Named Entity Recognition (NER) that uses an LLM (GPT-4, GPT-3.5) together with entity type definitions, few-shot examples, and chain-of-thought (CoT) templates to generate entities with explanations. Experiments show gains of 4% absolute F1 on CoNLL, 9% on GENIA, and 4% on FewNERD, and state-of-the-art on 3/5 CrossNER target domains with an average F1 gain of 3% using less than 2% of available data. All four reviewers found the prompt design simple and the idea intuitive, with three of them rating the paper 3 and one reviewer (Reviewer 3) rating it 5, noting that the method is clearly written and easy to integrate. The central disagreement is whether the simplicity constitutes a valuable contribution (Reviewer 3) or a lack of technical novelty (Reviewers 1, 2, 4). All reviewers agree that the core innovation is limited and that the strong results largely stem from the powerful GPT-4 backbone.

### Strengths

- The paper explores the potential of LLMs for NER in cross‑domain and low‑resource scenarios (Reviewers 1, 2, 4).
- The method is simple, clearly described, and easy to follow; the prompting template is straightforward to integrate into applications (Reviewer 1, 3).
- Experiments include detailed ablation studies that show the contribution of each component, such as the critical role of LLM size and few‑shot examples (Reviewers 2, 3).
- One reviewer noted comprehensive comparisons with prior work (Reviewer 3), while another acknowledged the demonstration of cross‑domain NER ability with GPT‑4 (Reviewer 2).
- The work emphasizes the importance of prompt‑based heuristics and in‑context learning for flexible, low‑human‑involvement NER systems (Reviewer 4).

### Weaknesses

- **Lack of technical novelty.** All reviewers agree that the method is straightforward and lacks core innovation: adding entity definitions, few‑shot examples, and CoT to the prompt is an intuitive and already‑known technique. Reviewers found the approach “naive” (Reviewer 4) and “similar to a strong baseline” (Reviewer 1). One reviewer questioned whether any other similar template could achieve comparable performance (Reviewer 3).
- **Performance is driven by the GPT‑4 backbone, not by the prompt design.** Reviewers 2, 3, and 4 note that the largest performance gains come from the powerful backend (GPT‑4) rather than from the proposed prompting strategy. Using T5 as the LLM yields results far below the state of the art (Reviewer 3). Reviewers 2 and 4 argue that comparing GPT‑4‑based models against much weaker baselines (Tables 2‑4) is unfair and “heavily favors the presented model”, rendering conclusions questionably validated (Reviewer 4). A proper comparison would use the same open‑source LLM of comparable size and type (Reviewers 2, 4).
- **Missing analyses and experiments.**
  - No analysis of computational cost for using GPT‑4, which is a significant factor for real‑world applications (Reviewer 2).
  - No sensitivity analysis to different prompt formulations or to the number of few‑shot examples (Reviewer 2). For Cross‑Domain NER (Table 2), only 2 examples are used; a reviewer asks why not add more examples (e.g., up to 200) to improve performance, and whether fine‑tuning GPT was considered (Reviewer 3).
  - Related work section does not clearly differentiate PromptNER from existing methods or explain how it improves upon them (Reviewer 4).
  - Several standard few‑shot NER benchmarks are omitted: WNUT‑2017, MIT‑Movie, MIT‑Restaurant, JNLPBA, etc. (Reviewer 4). There is also a lack of comparison with many state‑of‑the‑art few‑shot NER models (Reviewer 4). (Note: one reviewer (R3) considered the comparisons comprehensive, creating disagreement; the omission is noted by R4.)
- **Reproducibility and fairness concerns.** The use of proprietary GPT‑3.5/GPT‑4 models hinders reproducibility (Reviewer 4). The skewed comparison with baselines does not allow one to assess the contribution of the prompt methodology separately from the LLM backbone (Reviewers 2, 4).