- Decision: Reject
- Scores: 3, 6, 8, 3

## Merged Review

### Summary
This paper proposes Inference-time Dynamic Prompting (IDP) to improve the performance of compressed LLMs (3-bit GPTQ, SparseGPT applied to OPT-6.7B and LLaMA-7B). IDP learns a set of soft prompts and during inference selects the prompt with the highest attention score. The authors argue that prior work using naïve prompts suffers from over-reliance on a single prompt, and that compression displaces rather than erases knowledge. Experiments on nine downstream tasks show IDP achieves an average 1.24% improvement over baselines (single prompt, prompt tuning, prefix-tuning, LoRA). The paper also discusses the distinction between knowledge attrition and knowledge rechanneling.

### Strengths
- The paper addresses an important problem: improving compressed LLMs without re-training or extra parameters.
- IDP is a simple, effective, and inference-time lightweight approach.
- IDP consistently outperforms baseline methods (prompt tuning, prefix-tuning, LoRA) across nine varied tasks spanning multiple knowledge domains.
- The theoretical analysis of why compression leads to performance loss (knowledge displacement vs. erasure) is interesting and contributes to understanding.
- The exploration of how IDP “re-channels” inherent knowledge rather than adding new data is a valuable insight.
- Experiments include careful visualizations of layer-wise attention and activation matrices (reviewer 2).
- Some reviewers found the paper clear and well-structured (reviewers 2, 3), though others noted clarity issues (see Weaknesses).

### Weaknesses
- **Motivation and theoretical explanation are insufficient.**  
  It is unclear how IDP’s dynamic selection directly addresses the discrepancy between perplexity and downstream accuracy identified in Section 3.1 (reviewer 1). The mechanism of why selecting by maximal mean attention works is not justified—why does higher mean attention correspond to a better prompt? (reviewers 1, 3, 4). The distinction between “data attrition” and “knowledge rechanneling” is subtle; the evidence (attention shifts) does not convincingly rule out other explanations, and the hypothesis testing does not follow standard practice (reviewer 4). A deeper theoretical foundation is needed (reviewer 2).

- **Performance gains are modest and lack statistical significance.**  
  The reported improvements are often around 1% (e.g., Tables 1–4). No significance tests are conducted, making it unclear whether the differences are meaningful or due to random variation (reviewers 1, 4). The practical significance of such marginal gains in real-world applications is not justified (reviewer 1).

- **Clarity, organization, and reproducibility are lacking.**  
  Several experimental details are missing:
  - The values of hyperparameters *n* (prompt length), *m* (number of prompts), and *e* (embedding size) for IDP are not specified (reviewers 1, 4).
  - The meanings of suffixes `/short` and `/large` in Tables 1 and 2 are not explained in the main text (reviewer 4).
  - In Figure 5, prompt sizes for small and large prompts are not given (reviewer 1).
  - Settings for LoRA, ptuning, and soft prompts are not provided (reviewer 4).
  - The organization of the experiment section is confusing: Table 1 and 2 are discussed after Table 3, and the distinction between Sections 3.3.1 and 3.3.2 is unclear (reviewer 4). 
  - A typo is noted: “triviqa” should be “TriviaQA” (reviewer 4).  
  These omissions hinder reproducibility (reviewers 1, 4).

- **Novelty is contested.**  
  While some reviewers found IDP original (reviewer 2), others consider the contribution limited: IDP is essentially a prompt ensemble with hard selection, and similar ideas have been explored in prior work (reviewers 3, 4). The main novelty is the selection mechanism, which alone does not constitute a significant technical advance (reviewer 3).

- **Missing baselines and comparisons.**  
  The paper compares only to LoRA, prefix-tuning, and single/static prompting. A broader set of methods would give a more holistic perspective (reviewer 2). For example, comparisons to other compression recovery techniques or to the original uncompressed models are absent—showing uncompressed model performance would clarify how much compression degrades accuracy (reviewer 4).

- **Task diversity is limited.**  
  The experiments focus predominantly on world-knowledge tasks; incorporating a wider variety of downstream tasks (e.g., reasoning, generation) would better demonstrate versatility (reviewer 2).

- **Hypothesis test is not rigorous.**  
  The claimed hypothesis test (H0 vs. H1) does not follow conventional statistical hypothesis testing (e.g., rejecting the null). The evidence provided (attention pattern shifts) is not strong enough to definitively support the “knowledge rechanneling” hypothesis over “data attrition” (reviewer 4).