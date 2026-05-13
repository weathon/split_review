# Scaling Laws of RoPE-based Extrapolation

- Decision: Accept
- Scores: 1, 6, 8

## Abstract
The extrapolation capability of Large Language Models (LLMs) based on Rotary Position Embedding \citep{su2021roformer} is currently a topic of considerable interest. The mainstream approach to addressing extrapolation with LLMs involves modifying RoPE by replacing 10000, the rotary base of $\theta_n={10000}^{-2n/d}$ in the original RoPE, with a larger value and providing longer fine-tuning text. In this work, we first observe that fine-tuning a RoPE-based LLM with either a smaller or larger base in pre-training context length could significantly enhance its extrapolation performance. After that, we propose \textbf{\textit{Scaling Laws of RoPE-based Extrapolation}}, a unified framework from the periodic perspective, to describe the relationship between the extrapolation performance and base value as well as tuning context length. In this process, we also explain the origin of the RoPE-based extrapolation issue by \textbf{\textit{critical dimension for extrapolation}}. Besides these observations and analyses, we achieve extrapolation up to 1 million context length within only 16K training length on LLaMA2 7B and 13B \citep{touvron2023llama2}.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Rotary Position Embeddings have played a significant role in improving the scalability of LLMs. However, RoPE faces problems when trying to extrapolate beyond the length the model was trained on.

Various approaches have been taken to solve the issue with extrapolation, and this paper goes in depth describing why these issues exist and derives pretty good solutions as well. Apart from this, it presents a good understanding of why some of the existing methods work and why a base of 10,000 is not a good value for RoPE's base.

All the claims are very well substantiated with theoretical as well as empirical analysis.

### Strengths
- Pretty useful theorems that shows why and how RoPE's beta impacts extrapolation.
- Results on critical base, d_{extra}, and T_{extra} and their relationship is a very useful contribution in this area.
- Both experimental and theoretical analysis are strong.

### Weaknesses
A bit more clarification around the calculation of critical beta, and why extrapolation capabilities exist even when beta values are large could be added since we will see OOD embeddings as soon as T is larger than T_{train} during inference.

### Questions
None.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on the extrapolation capability of Rotary Position Embedding (RoPE) in large language models (LLMs). The authors first observe that pre-training RoPE with smaller or larger bases can significantly enhance its extrapolation performance. Then, they propose the Scaling Laws of RoPE-based Extrapolation, a unified framework that describes the relationship between extrapolation performance and base value as well as tuning context length from a periodic perspective. Furthermore, they explain the origin of the RoPE-based extrapolation issue by the critical dimension for extrapolation. Finally, they achieve extrapolation up to 1 million context length within only 16K training length on LLaMA2 7B and 13B.

### Strengths
- Observing that pre-training RoPE with smaller or larger bases can significantly enhance its extrapolation performance, providing a new perspective for extrapolation research.
- Proposing the Scaling Laws of RoPE-based Extrapolation, offering a unified theoretical framework for RoPE extrapolation.
- Explaining the origin of the RoPE-based extrapolation issue through the critical dimension for extrapolation.
- Achieving extrapolation up to 1 million context length within only 16K training length on LLaMA2 7B and 13B, demonstrating the potential of RoPE extrapolation.
- Providing guidance for other extrapolation methods, such as dynamic NTK and Code LLaMA.

### Weaknesses
 - In fact, the analysis results of this article are basically available in the YaRN[4] paper, which had pointed out that certain dimensions have high frequency and enough turns are made during training, therefore, the training of these dimensions is sufficient and should remain unchanged during extrapolation; for those dimensions that are less than one circle, only interpolation (PI) can be used to ensure numerical stability. This is obviously the equivalent expression of the proposed concept "critical dimension" in this work.
- Most experimental comparisons only report ppl, which does not represent real long context ability. The authors should conduct experiments on some practical benchmarks and tasks. Eg. PASSKEY RETRIEVAL[2], the Hugging Face Open LLM Leaderboard[3] (ARC, HellaSwag, TruthfulQA, etc).
- The RoPE extrapolation methods discussed in the paper may have certain limitations in practical applications, it is just verified over perplexity, but not enough practical application scene.
- Compared to baselines, it lacks some comparison results over computational resources and memory usage.
- Missing reference. The work should compare results with ReRoPE[1].

### Questions
- Only 7B and 13B models are verified. Have you experimented with the proposed methods on larger or smaller models? So that the "scaling law" saying can be more convincing.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies how shall we scale the transformer context length up via modifying RoPE. Different from popular approaches that increase the rotary base, authors found both increasing and decreasing the rotary base could significantly enhance its extrapolation performance.

### Strengths
1) This paper studies a very interesting problem: How shall we modify the 10^4 rotary base? 
2) Well-written. 
3) Some reasoning and insights are very cool. Such as the Q1 and Q2 in the introduction.
4) The theoretical analysis of the benefits of a smaller rotary base would be helpful to the long seq community.

### Weaknesses
1) I have one strong concern about the evaluation of this paper. This paper only evaluates the scaled model on the long-context perplexity and short-context well-established benchmarks. Low ppl on long context language modeling cannot really reflect the good results on long-range reasoning. The short-context results can only show the proposed approach is not that harmful on short tasks. If so, there is no evidence showing that the proposed framework can really improve the long-range real-world tasks, which is exactly what we espect in the long-range modeling research.

2) There is no related work section. It is "okay" for expert readers, but it would be very helpful to make a broader impact if authors can write one. I think authors should at least include:
- scaling seq len with position embedding. The authors discussed some of these approaches, but it would be better to summarize them in a thread.
- scaling seq len with efficient implementation, such as Flash attention 1&2 [1]
- scaling seq len with a distributed system, such as Sequence Parallelism [2][3]

3) It would also be very interesting to study the filling-in-the-middle pattern after applying the proposed trick. Is the filling-in-the-middle related to the position embedding? This is just a bonus question. It is an okay paper without this study, but I suggest authors to study this to deliver more insights.

### Questions
See weakness above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
