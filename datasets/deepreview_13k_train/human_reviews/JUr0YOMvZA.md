# DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
Large Vision-Language Models (VLMs) exhibit significant potential in multimodal tasks but often struggle with hallucinations—responses that are plausible yet visually ungrounded. In this work, we investigate the layer-wise prediction tendencies of VLMs and conduct an in-depth analysis of their decoding mechanism. We observe that VLMs tend to ``overthink'' during the final stages of decoding, making significant prediction shifts in the last few layers often favoring incorrect results, which leads to a surge in hallucinative outputs. Leveraging this localized pattern, we propose a novel decoding strategy inspired by the momentum analogy used in gradient descent-based optimizers. Our method enforces decoding consistency across layers in an adaptive manner during forward passes—an under-explored approach in existing works. This strategy significantly improves the reliability and performance of VLMs in various multimodal tasks, while introducing only negligible efficiency overhead.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper observes that VLMs tend to make prediction shifts in the last few layers, which leads to a surge in hallucinative outputs. The authors propose a decoding strategy inspired by the momentum analogy used in gradient descent-based optimizers, which enforces decoding consistency adaptively across layers during forward passes. The proposed method outperforms existing approaches on several public datasets.

### Strengths
1. The motivation of hallucinations frequently emerge in the later layers seems interesting.
2. The main technical pipeline is clear.

### Weaknesses
1. Writing and diagrams require improvement.
1). Large Vision-Language Models (VLMs) mentioned in the abstract abbreviated as LVLMs would be better.
2). A single-paragraph abstract would improve conciseness.
2). Figure 1(c) requires a more detailed description.
3). In Section 2, lines 151–152, the statement “However, these methods do not correct hallucinations during the inference process” could be reconsidered. In my view, methods like VCD, which contrast output distributions, are indeed part of the inference process.
4). It would improve readability if the introduction were revised to emphasize the primary contributions of this work more clearly.

2. Could you increase the number of instances shown in Figure 1(b) to provide a more comprehensive view?

3. Section 3.2, line 198-200, "VLMs are already proficient in capturing detailed visual information, so further intensifying image-text fusion is unnecessary." how to validate "VLMs are already proficient in capturing detailed visual information" from your results?

4. Section 3.4, line 261-261, "Varying the starting layer for refinement can enhance different model capabilities (e.g., layer 16 excels in OCR tasks, while layer 24 improves positional perception)." (e.g., position scores do not consistently increase, nor do OCR scores consistently decrease). This makes it challenging to conclude that varying the starting layer directly enhances distinct capabilities. Could you provide additional evidence to support this claim?

5. The performance improvement appears modest. For instance, on the MME benchmark, the score of 1515.89 is slightly lower than OPERA’s 1518.36 on the LLaVA baseline. Additionally, it would strengthen the evaluation if more hallucination benchmarks, such as CHAIR, were included.

6. I am concerned about the quality of text generated at preceding layers. Further evaluation metrics for text quality, such as BLEU or other relevant scores, would provide a clearer understanding.

### Questions
My primary concern lies in the performance and  the quality of text generated at preceding layers. I will be happy to raise my score if my current questions and concerns can be addressed.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes DAMO (Decoding by Accumulating Activations Momentum), a novel decoding strategy designed to reduce hallucinations in Vision-Language Models (VLMs) by maintaining consistency across layers during inference. DAMO introduces a momentum-based mechanism in transformer forward computation to smooth activation updates layer-by-layer, mitigating hallucinations by preserving visual grounding in predictions. DAMO shows good results on various benchmarks (MME, POPE) and models (LLaVA1.5, INF-MLLM1, mPLUG-Owl2) with minimal memory overhead. Its adaptability is demonstrated through successful application to LLM benchmarks such as TruthfulQA and FACTOR, highlighting DAMO’s transferability across various tasks.

### Strengths
- The paper presents an interesting observation that VLMs are often able to generate accurate predictions in the initial layers, with hallucinations surfacing in later layers. This suggests that hallucinations could stem from disruptions in the decoding sequence rather than an absence of underlying knowledge, providing a novel diagnostic angle on VLM hallucinations.
- The paper’s approach to using "momentum" within the forward computation of transformers is intuitive and impactful. By building consistency across activations, DAMO effectively mitigates hallucination emergence in later layers, reinforcing layer-wise stability and preserving visual grounding.
- The authors extend their method beyond VLMs to yield strong performance in LLM benchmarks like TruthfulQA, FACTOR, StrQA and GSM8K, showcasing its versatility across various language tasks.

### Weaknesses
 - The performance improvement on HallusionBench appears minor and lacks a substantial breakthrough. 
- The model seems overly sensitive to hyperparameters, raising concerns that its performance may heavily depend on hyperparameter tuning. Specifically, the reported results for the Random setting on the POPE dataset show that when \(\tau = 0.30\), the F1 score (88.83) is lower than at other tested values, which contradicts the claim of insensitivity to this parameter. Furthermore, the evaluation of \(\tau\)'s sensitivity is limited to the POPE dataset; extending this analysis to other datasets would provide a more robust foundation for the claim. Similarly, the MME benchmark results in Appendix Table 10 show that when \(\beta_1 = 0.20\), the Total Score (1462) is lower than other decoding methods, which also contradicts the claim that \(\beta_1\) is not sensitive. The lack of a clear trend in the relationship between \(\beta_2\) and performance, despite the new ablation study, further suggests that the model's performance may be highly dependent on specific hyperparameter settings, and the role of \(\beta_2\) is not well understood.
- While the novelty is acknowledged, there is lingering uncertainty about whether the improvements are genuinely impactful or effective.

### Questions
- The results on the MME dataset show only modest improvements in hallucination reduction, with much of the gains appearing in tasks that may be more knowledge-based (e.g., Celebrity, Posters, Landmark, Artwork) rather than directly related to hallucination robustness. Would you consider testing DAMO on additional hallucination-focused benchmarks? Alternatively, could you clarify how the MME dataset captures DAMO's effectiveness in mitigating hallucinations?
- Given that the threshold τ\tauτ is central to controlling the switch between coefficients \beta_1​ and \beta_2​, could you provide more information on how its value was determined? Additionally, could you discuss any observed sensitivity of DAMO’s performance to variations in \tau?
- Could you provide further insights on the actual layers where the adaptive coefficient adjustment activates? For instance, does the transition of \beta from \beta_1​ to \beta_2​ tend to occur around specific layers, such as the after 24th, as observed in your analysis? Clarifying whether these transitions align with the predefined analysis layers would help in understanding DAMO’s consistency and effectiveness.

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the layer-wise prediction tendencies of VLMs and proposes a novel decoding strategy called DAMO to mitigate hallucinations. DAMO enforces decoding consistency across layers in an adaptive manner during forward passes, amplifying visual semantics consistently extracted throughout the inference while reducing hallucination biases. Experiments on various VLM benchmarks demonstrate that DAMO significantly mitigates hallucinations, resulting in more visually grounded and accurate predictions.

### Strengths
1. Novel insights consider the layer-wise outputs, especially regarding to language bias in LVLMs.

2. Simple but effective solutions named DAMO based on the proposed findings.

3. Extensive experiments and pleasant results are achieved.

4. Source codes and partial experimental results are provided.

### Weaknesses
1. Although this method is proposed for LVLMs, this paper does not mention the DoLa [r1] in the main body. DoLa's claims are somewhat opposite to DAMO's. More analysis is needed to clarify the insights and differences.
[r1] Dola:  Decodingbycontrastinglayers improves factualityinlarge languagemodels. arXivpreprint
 arXiv:2309.03883,2023.
2. Applying DAMO to LVLMs and LLMs seems to be contradictory, especially considering the DoLa's findings.
3. I check the appendix and think some critical experimental details of DAMO are missing, like temperature, max token, decoding strategies.
4. GPT4-V experiments should be better conducted rather than GPT4, following VCD.
5. typo: INF-MLLM1 $\rightarrow$ INF-MLLM.

### Questions
1. How about some complex reasoning VQA performances in terms of Figure 1(b) (c). As indicated in DoLa [r1], deep layers facilitate the complex reasoning. Also, the reasoning steps is more complex as in [r1], please add more explanations.
[r1] Dola:  Decodingbycontrastinglayers improves factualityinlarge languagemodels. arXivpreprint
 arXiv:2309.03883,2023.
2. In 'Figure 1(c) Proportion of samples in a small dataset....',  Detailed descriptions in the Figure 1 caption are better illustrated.
3. Better re-organize Figure 1 to save more space.

I consider adjusting my score based on the clarification of DAMO and DoLa.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the issue of hallucinations in Large Vision-Language Models (VLMs) by analyzing their layer-wise prediction tendencies and decoding mechanisms.  The authors propose a decoding strategy inspired by the momentum concept in gradient descent optimizers, which ensures adaptive decoding consistency across layers.

### Strengths
1. The authors conduct a detailed layer-wise analysis of VLMs' prediction tendencies, identifying that hallucinations often emerge in the final layers due to significant shifts in decoding. This insight may provide a deeper understanding of the underlying mechanisms causing hallucinations.

2. The proposed Decoding by Accumulating Activations MOmentum (DAMO) method is somewhat effective. By accumulating momentum across layers, DAMO ensures consistent decoding and reduces the impact of late-stage hallucinations.

### Weaknesses
1. The paper draws inspiration from the momentum concept and contrast decoding, but it lacks a detailed analysis and comparison with recent related work, such as [1, 2]. Additionally, the paper does not adequately explain why the proposed method theoretically offers advantages over previous approaches.

2. Poor presentation: The paper lacks comprehensive framework diagrams that clearly illustrate the specific content and workflow of the proposed method, making it difficult to understand the method's details.

3. The paper does not provide a detailed analysis of how sensitive DAMO is to hyperparameters, such as the momentum coefficient. Understanding the optimal settings for different models and tasks could help in practical implementation.

### Questions
Please refer to Weakness

### Soundness
3

### Presentation
2

### Contribution
2
