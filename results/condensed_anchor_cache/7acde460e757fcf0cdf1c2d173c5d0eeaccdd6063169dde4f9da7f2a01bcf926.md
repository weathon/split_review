- Decision: Accept
- Scores: 6, 1, 6, 6

## Merged Review

### Summary
This paper studies the safety risks of fine-tuning aligned large language models (Llama, GPT-3.5 Turbo) under three scenarios: explicitly harmful training data, identity-shifting data, and completely benign datasets. It finds that safety alignment can be compromised with as few as 10 adversarial examples (costing <$0.20 via OpenAI’s API) or even by fine-tuning on benign, commonly used datasets. The paper also demonstrates that backdoor triggers during fine-tuning can bypass safety evaluation benchmarks. While one reviewer (Reviewer 2) considers this a very important paper with major societal significance, other reviewers note that the findings are not surprising given known catastrophic forgetting and the strength of LLMs in following instructions, and they raise concerns about novelty, evaluation completeness, and missing comparisons.

### Strengths
- The paper is well-written, well-organized, and easy to follow (Reviewers 1, 3).
- It considers multiple scenarios: harmful training data, identity-shifting data, and benign data, showing three levels of fine-tuning effects (Reviewers 1, 3).
- The studied problem is interesting and the evaluation is detailed, including results on AdvBench (Appendix F) and MT-bench (Reviewers 1, 4).
- Reviewer 2 highlights the paper’s **societal significance**, urgency for stronger AI safety research, and the need for regulatory guardrails; they believe it should be nominated for a best paper award.
- The demonstration that backdoor triggers can bypass safety tuning with a mixed dataset is considered a more surprising point (Reviewer 4).

### Weaknesses
- **Novelty and surprise:** The finding that fine-tuning degrades safety is not surprising, as LLMs are known to follow instructions strongly and are subject to catastrophic forgetting under distribution shift (Reviewers 1, 4). The technique (standard fine-tuning) is simple, limiting technical novelty (Reviewer 1). One reviewer questions whether the main hazard only affects users/attackers (Reviewer 4).
- **Missing comparisons:** No comparison with existing jailbreak attacks (handcrafted or automatically optimized). If such attacks achieve higher harmfulness, the paper’s findings may be less meaningful (Reviewer 3).
- **Incomplete evaluation:**
  - Only harmfulness is measured; helpfulness is neglected. A model that always generates toxic words would score high on harmfulness but may not represent a meaningful risk (Reviewer 3). Quantitative results on other domains (generative capabilities, helpfulness scores on MT-bench) are needed (Reviewers 1, 4).
  - Evaluation is primarily on a dataset created by the paper; it is unclear if it is representative. The authors show some results on AdvBench in Appendix F but do not rely on this public dataset for most experiments; Table 10 is missing metrics and reliability is unclear (Reviewer 1).
  - Model scale is not explored beyond Llama-2; the authors should evaluate Llama-7b or 13b and show generated samples (Reviewer 4).
- **Lack of mechanistic explanation:** It is unclear how only 5 gradient steps (possibly due to a large learning rate) can significantly affect model behavior; deeper explanation is requested (Reviewer 3). The paper lacks exploration of underlying principles relating fine-tuning and safety alignment (Reviewer 4).
- **Mitigation concerns:** No clear mitigation strategy for open-source models; the proposed “mix in safety data” approach is not explained in terms of how it could prevent malicious behavior (Reviewers 1, 3). The adopted defense (mix training) appears satisfactory only when using the same amount of safe data, but its robustness is not fully explored (Reviewer 4).
- **Missing hypothesis discussion:** Reviewer 2 suggests the paper would benefit from including a brief discussion of hypothesized causes of the observed fragility, even if speculative.
- **Minor reviewer contrast:** Reviewer 2 (who rated the paper 1 but praised its importance) had only one additional suggestion (hypothesis discussion) and no other major weaknesses; all other reviewers listed multiple substantive weaknesses.