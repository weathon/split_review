# Hyperbolic Fine-tuning for Large Language Models

- Decision: Reject
- Scores: 6, 6, 6

## Abstract
Large language models (LLMs) have demonstrated remarkable performance on various tasks. However, it remains an open question whether the default Euclidean space is the most suitable choice for embedding tokens in LLMs.
   In this study, we first investigate the non-Euclidean characteristics of LLMs. 
   Our findings reveal that token frequency follows a power-law distribution, with high-frequency tokens clustering near the origin and low-frequency tokens positioned farther away. Additionally, token embeddings exhibit a high degree of hyperbolicity, indicating a latent tree-like structure in the embedding space. 
   Building on the observation, we propose to efficiently fine-tune LLMs in hyperbolic space to better exploit the underlying complex structures. 
   However, we found that this fine-tuning in hyperbolic space cannot be achieved with naive application of exponential and logarithmic maps, when the embedding and weight matrices both reside in Euclidean space.
   To address this technique issue, we introduce a new method called hyperbolic low-rank efficient fine-tuning, \method, that performs low-rank adaptation directly on the hyperbolic manifold, avoiding the cancellation effect caused by the exponential and logarithmic maps, thus preserving the hyperbolic modeling capabilities.
   Through extensive experiments, we demonstrate that \method significantly enhances the performance of LLMs on reasoning tasks, particularly for complex reasoning problems. In particular, \method improves the performance in the complex AQuA dataset by up to 13.0\%, showcasing its effectiveness in handling complex reasoning challenges

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel approach for fine-tuning large language models (LLMs) within a hyperbolic space using their proposed method, HypLoRA. The authors build on observations in Section 4.1 that token embeddings exhibit a latent tree-like structure and token frequency correlates with outlier dimensions. HypLoRA adapts the low-rank transformation directly on the hyperbolic manifold, avoiding the cancellation effect typically observed when applying exponential and logarithmic maps in Euclidean space. Experimental results conducted in Section 5.1 indicate that HypLoRA significantly enhances LLM performance, particularly on reasoning tasks with complex structures, with a noted improvement of up to 13.0% on the AQuA dataset.

### Strengths
HypLoRA provides competitive fine-tuning results with various state-of-the-art PEFT methods. Furthermore, Figure 3 demonstrates that HypLoRA requires fewer GPU hours than the recent state-of-the-art method, DoRA. Further, HypLoRA appears to be easy to use and does not require additional hyperparameter tuning since Table 5 shows that setting K=1 results in the best performance regardless of the dataset. 

The results presented in 4.2 provide an interesting, novel analysis of token embeddings by measuring their $\delta$-hyperbolicity. Table 2 demonstrates that the $\delta$-hyperbolicity is extremely low regardless of the model or dataset.  These findings could help motivate future works studying the geometry of LLM embeddings. I think an excellent follow-up study would examine the relationship between the hyperbolicity of LLM embeddings and cases where HypLoRA performs better than other Euclidean-based PEFT methods. 

The analysis presented in Section 5 clearly demonstrates the challenges of fine-tuning models in hyperbolic space. The author’s proposed solution to combat these challenges is simple, effective, and theoretically motivated.

### Weaknesses
The authors fail to acknowledge a large body of works investigating the structure of token embeddings in LLMs that have presented findings similar to the first section. Namely, previous works have shown LLM embeddings have an implicit tree-like structure (Andy Coenen et al. 2019: https://arxiv.org/pdf/1906.02715) and that token frequency is highly correlated with `outlier dimensions’ and causes distributions to utilize the embedding space uniformly (Gao et al. 2019: https://arxiv.org/pdf/1907.12009, Rudman et al. 2022 https://arxiv.org/pdf/2108.07344 and Puccetti et al 2022: https://aclanthology.org/2022.findings-emnlp.93.pdf). Given this, the experiments conducted in Section 4.1 do not provide any novel insights into the structure of LLM token embeddings. 

The overall effectiveness of  HypLoRA is inconsistent. While Table 3 demonstrates that HypLoRA tends to perform very well with Gemma-7B and LLAMA3-8B, the results are mixed with Llama. Further, Table 3 does not provide any information about the number of random seeds used to generate results. If performance is evaluate using only a single random seeds, results claimed about the effectiveness of HypLoRA are weakened.

Table 6 can be removed. Adding a cherry-picked example do not provide any additional insights.

### Questions
1. The claim in lines 489-493 is not well supported. The improvement of HypLoRA over traditional PEFT methods for some models and tasks does not demonstrate that this enhances the model’s ability to comprehend hierarchical relationships between tokens. How is the concept of hierarchical relationships explicitly tested? 

2. In Figure 2, you specify that you use LLaMA3; however, in Table 1, you do not specify the LLM used to get these results. What LLM is used? How do these results vary across different LLMs?  

3. How many random seeds were used to create Table 3?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors observe that token embeddings in LLMs exhibit a high degree of hyperbolicity, suggesting an underlying tree-like structure in the embedding space. Motivated by this, they introduce HypLoRA, which performs low-rank adaptation directly on the hyperbolic manifold, thus avoiding the cancellation effect introduced by the exponential and logarithmic maps. The effectiveness of HypLoRA is demonstrated through extensive experiments across multiple reasoning tasks.

### Strengths
1. **Interesting angle**: Fine-tuning LLMs in hyperbolic space introduces an interesting angle on LLM fine-tuning research. The observation that token embeddings exhibit a high degree of hyperbolicity further supports the motivation to explore fine-tuning in hyperbolic space.

2. **Reasonable approach**: HypLoRA is proposed to perform low-rank adaptation directly on the hyperbolic space, thus avoiding the cancellation effect introduced by the exponential and logarithmic maps. The approach is reasonable and intuitive.

3. **Experimental effectiveness**: The effectiveness of HypLoRA is demonstrated through experiments conducted across multiple reasoning tasks.

### Weaknesses
1. **Lack of Detailed Representation of Hierarchical Structures**: Although the introduction provides an intuitive example of hierarchical relationships like "fruit-banana," the paper does not describe how hierarchical structures within text are specifically represented. In line 212, the authors mention, "This power-law behavior aligns with the hierarchical nature of language," but power-law distribution is only one of many characteristics of hierarchical structures and does not inherently imply or sufficiently indicate hierarchy. This claim lacks theoretical and experimental support, and there is no clear causative or correlational relationship between power-law distribution and hierarchy.

2. **Unquantified Computational Complexity**: Equation 9 is a key contribution of the paper; however, it involves logarithmic and exponential mappings, which add substantial computational complexity. Since the paper does not quantify or analyze this computational load in detail, it’s challenging to assess the actual efficiency of HypLoRA in large-scale language models. While HypLoRA shows theoretical advantages, its efficiency relative to traditional methods in practical applications remains unclear.

3. **Learning in Hyperbolic Space vs. Embedding in Euclidean Space**: HypLoRA conducts learning in hyperbolic space, whereas embedding occurs in Euclidean space, which differs significantly from the traditional LoRA approach. This design shift is not sufficiently explained, especially regarding the choice of rank for the low-rank decomposition submatrices. An analysis of rank selection could provide insights into optimizing HypLoRA’s performance in hyperbolic space, which remains unexplored.

4. **Unclear Significance of Lorentz Rotation and Boost**: The HypLoRA (I) and HypLoRA (II) methods involve Lorentz rotation and boost operations, but their definitions and roles in this context are ambiguous, making it difficult to understand their actual significance in LLM fine-tuning. Further clarification on how these operations function within the model and their intended effects would improve understanding of hyperbolic transformations' contributions to semantic reasoning tasks.

### Questions
Please see my comments in the Weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the non-Euclidean properties of LLMs, demonstrating that token frequency adheres to a power-law distribution and that token embeddings reveal a significant hyperbolic structure, suggesting an underlying tree-like arrangement in the embedding space. It introduces a novel approach, Hyperbolic Low-Rank Efficient Fine-Tuning (HypLoRA), designed to fine-tune LLMs effectively in hyperbolic space while circumventing the cancellation effects associated with exponential and logarithmic maps. HypLoRA markedly improves LLM performance on reasoning tasks, especially for complex problems.

### Strengths
1. This paper claims to be the first study on fine-tuning LLMs in hyperbolic space. It investigates the token embedding properties of LLMs and proposes the HypLoRA method based on the analysis. Overall, the work makes a significant contribution.
2. This paper is well-organized and well-written, encompassing analysis, methodology, experiments, and conclusions, with a clear overall presentation and fluent language.
3. The content of this paper is rich and comprehensive, with thorough comparative experiments and analyses.

### Weaknesses
1. In Introduction and Related Work, the authors claimed existing works have not attempted to study LLM embeddings in the context of non-Euclidean geometry. However, there are studies on hyperbolic space learning of language models like Chen W, et al, 2024 (https://ieeexplore.ieee.org/document/10542420). It may not directly relate to LLMs, but I still believe that these methods should be considered as relevant work and comparative approaches, as the main idea of your study is on hyperbolic learning. An actionable suggestion is trying to discuss how your approach differs from or builds upon these existing methods for smaller language models, and explain why their technique is specifically suited for LLMs.
2. In Introduction part (Line 95-97), a brief explanation would be better about how the proposed HypLoRA is designed and what features of HypLoRA leads to its consideration of token hierarchies and minimizing computational costs.
3. In Section 4.1, how you obtain the distribution of token frequencies? Though the computation may be simple, a brief illustration would still be better to provide a clearer presentation.
4. In Section 4.2 (Line 282-283), can the power-law frequency distribution and significant hyperbolicity completely indicate a tree-like hierarchical structure of token embeddings? Are there any previous studies on the properties of tree-like hierarchical structures can prove this conclusion? A more rigorous analysis would be better to give the conclusion of the investigation. I think the authors could either provide references to studies that support this connection between power-law distributions, hyperbolicity, and tree-like structures, or to clarify that this is a hypothesis that requires further investigation.
5. Table 3 should provide more direct comparison between HypLoRA and other PEFT methods, expecially LoRA, by using highlighting marks for easier understanding. 
6. In the inference efficiency part of Section 5.3, it would be better to record both inference and fine-tuning efficiency for a more comprehensive analysis.

### Questions
1. In Section 5, why directly applying low-rank adaptation on hyperbolic manifold works? What is the main purpose of using tangent space from previous work? Is LLR already an existing and universal strategy of reducing costs of learning hyperbolic representation?
2. In Table 3, from my view, HypLoRA seems not have obvious performance advantages than other methods on all datasets? Maybe the performance of hyperbolic fine-tuning is task-dependent? So I would like to see more performance comparison on other tasks rather than just arithmetic reasoning.
3. In case study part of Section 5.3, as you mentioned the hyperbolic learning is good at capturing tree-like nature of language, would it be better to provide a specific example that demonstrates how HypLoRA better captures hierarchical relationships in language compared to baseline methods? Such as showing a case where HypLoRA correctly handles a complex hierarchical concept that other methods struggle with.

### Soundness
3

### Presentation
4

### Contribution
3
