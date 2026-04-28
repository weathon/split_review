# Improving Uncertainty Quantification in Large Language Models via Semantic Embeddings

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
Accurately quantifying uncertainty in large language models (LLMs) is crucial for their reliable deployment, especially in high-stakes applications. Current state-of-the-art methods for measuring semantic uncertainty in LLMs rely on strict bidirectional entailment criteria between multiple generated responses and also depend on sequence likelihoods. While effective, these approaches often overestimate uncertainty due to their sensitivity to minor wording differences, additional correct information, and non-important words in the sequence. We propose a novel approach that leverages semantic embeddings to achieve smoother and more robust estimation of semantic uncertainty in LLMs. By capturing semantic similarities without depending on sequence likelihoods, our method inherently reduces any biases introduced by irrelevant words in the answers. Furthermore, we introduce an amortised version of our approach by explicitly modelling semantics as latent variables in a joint probabilistic model. This allows for uncertainty estimation in the embedding space with a single forward pass, significantly reducing computational overhead compared to existing multi-pass methods. Experiments across multiple question-answering datasets and frontier LLMs demonstrate that our embedding-based methods provide more accurate and nuanced uncertainty quantification than traditional approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the problem of quantifying uncertainty in large language models. Specifically, previous methods, such as Semantic Entropy (SE), use bidirectional entailment criteria to assess whether two responses share the same meaning. However, the authors argue that bidirectional entailment criteria are sensitive to linguistic variations. To address this, they propose SEU, which quantifies uncertainty using cosine similarities between the semantic embeddings of different responses. Additionally, since both SE and SEU require multiple forward passes, the authors introduce an amortized version of SEU that models the underlying semantics as latent variables, requiring only a single forward pass while still achieving strong results.

### Strengths
1. **Important problem**: The paper focuses on an important and valuable problem: quantifying the uncertainty of large language models.

2. **Efficient method**: The authors propose an amortized version of SEU that models the underlying semantics as latent variables. This approach requires only a single forward pass but still demonstrates very strong performance.

3. **Experimental validation**: The authors conduct experiments on three QA datasets across three LLMs, demonstrating the effectiveness of the proposed SEU and ASEU methods.

### Weaknesses
1. **Reliability of cosine similarity of embeddings as an absolute measure of semantic relatedness**: I have some concerns about using cosine similarity as an absolute measure to describe the similarity between two responses. As shown in [1], the embedding space is isotropic, meaning that some texts are very close together within a narrow cone, while others are far apart. Thus, cosine similarity may not function well as an absolute measure. Furthermore, while cosine similarity can indicate relative similarity (i.e., A is more similar to B than C), there is no guarantee that a high cosine similarity score (e.g., >0.9) directly translates to a high degree of semantic similarity. The Sentence-BERT model, while effective for ranking similarity, does not provide a well-calibrated absolute measure of semantic equivalence. This is because the training objective focuses on relative similarity, not absolute semantic correspondence. 

2. **Advantages of SEU compared to SE**: The authors claim that SE models are sensitive to linguistic variability and minor wording differences, whereas SEU models are more robust and focus on the underlying semantic content. However, the SE method uses NLI classifiers that take the combined input of both responses, allowing for more fine-grained interaction between them. In contrast, SEU encodes responses independently, lacking such fine-grained interaction. As such, I find the argument for SEU being superior to SE unconvincing. Additionally, the experiments are conducted on a single model for both SE and SEU, which may not reveal whether the observed advantages are due to model choice or differences in methodology. The comparison should include multiple NLI classifiers to ensure the observed benefits are not specific to a particular model.

3. **Bidirectional entailment criterion can only act as a binary measure**: The authors claim that bidirectional entailment criteria can only yield binary outcomes. However, since the criterion relies on an entailment classification, the output probability of the entailment class has the potential to express the degree of relatedness between different responses.

### Questions
Please see my comments on the Weakness section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduce, the technical challenges include addressing "hallucinations" in LLMs, where models generate coherent but incorrect responses, and the difficulty of applying traditional uncertainty quantification methods to the open-ended nature of natural language generation. Our innovations introduce Semantic Embedding Uncertainty (SEU) to estimate semantic uncertainty more accurately by leveraging semantic embeddings, and an amortized version (ASEU) that reduces computational costs by estimating uncertainty in a single forward pass.

### Strengths
1 The paper presents a novel approach to uncertainty quantification in large language models (LLMs) by introducing Semantic Embedding Uncertainty (SEU) and its amortized version (ASEU). These methods innovatively leverage semantic embeddings to address the limitations of traditional uncertainty estimation techniques, offering a more nuanced understanding of semantic uncertainty without relying on strict bidirectional entailment criteria.
2 The research demonstrates high quality through  empirical evaluation across multiple question-answering datasets and state-of-the-art LLMs. The paper provides a good comparison against existing methods, showcasing SEU's superior performance in accurately quantifying uncertainty. 
3 The paper is well-structured and clearly articulates the problem, the proposed solutions, and their significance.

### Weaknesses
 1. Generalization Limitations: The SEU method proposed in this paper has mainly been experimentally validated for question-answering tasks, and its effectiveness and generalization ability in other types of natural language processing tasks, such as text summarization or machine translation, have not been fully tested. The method's reliance on comparing semantic embeddings of generated text may not directly translate to tasks where the evaluation criteria are less about semantic similarity and more about other factors like coherence or fluency.
2. Computational Resource Consumption: Although the amortized SEU (ASEU) reduces computational overhead, during the model training phase, especially when it involves inference and optimization of latent variables, it may still require relatively high computational resources. The paper lacks a detailed analysis of the computational cost associated with training the ASEU model, making it difficult to assess its practical applicability in resource-constrained environments.
3. Dependence on Pre-trained Models: The SEU method relies on high-quality pre-trained language models to generate semantic embeddings. If the pre-trained models themselves have biases or inaccuracies, it could affect the accuracy and reliability of the SEU method. The paper does not sufficiently address the potential impact of the choice of embedding model on the overall performance of SEU and how to mitigate the propagation of biases from these models.
4. Figure 1,2,3,  model size diversity analyses needed.  While the paper provides a comparison of uncertainty estimation methods across different models, it would be beneficial to include models of varying sizes to get a more comprehensive understanding of how the proposed methods scale. The current selection of models does not fully represent the spectrum of LLMs, particularly the very large models (e.g., 70 billion parameters) or smaller models (e.g., 3 billion parameters). Including a broader range of model sizes could provide insights into the scalability and generalizability of the SEU and ASEU methods.
5 . Close Model Variations analysing needed.  It would be insightful to see comparisons that include close variations of the same model architecture but with different sizes. This could help elucidate whether the performance of the uncertainty estimation methods is more dependent on the model architecture or its size. Such an analysis could reveal trends that are crucial for understanding the behavior of SEU and ASEU in different practical scenarios.

### Questions
1. Generalization to Other NLP Tasks?  The SEU method has been validated primarily for question-answering tasks. Could the authors discuss the potential effectiveness and generalization of the SEU method to other natural language processing tasks such as text summarization or machine translation, where the context and requirements might differ significantly?

2. Computational Resources in Model Training? While ASEU is praised for reducing computational overhead during inference, what are the computational resource requirements during the model training phase, particularly when dealing with the inference and optimization of latent variables? How does this compare to traditional methods in terms of efficiency?

3. Reliability on Pre-trained Models? The SEU method's performance seems to heavily rely on the quality of the pre-trained language models for generating semantic embeddings. How sensitive is the SEU method to potential biases or inaccuracies in these pre-trained models, and what measures can be taken to mitigate such issues?

4. Diversity in Model Size Analysis? Figure 1, along with other figures, compares uncertainty estimation methods across a limited range of model sizes. Could the authors expand on the analysis to include a more diverse set of model sizes, especially very large models (e.g., 70 billion parameters) and smaller models (e.g., 3 billion parameters), to provide a comprehensive understanding of how the proposed methods scale and perform across different model sizes?

5. Analysis of Close Model Variations? It would be insightful to see an analysis that includes close variations of the same model architecture but with different sizes. How does the performance of the uncertainty estimation methods vary with model size while keeping the architecture constant? What trends can be observed that would help us understand the behavior of SEU and ASEU in practical applications with different model sizes?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper identifies that bidirectional entailment used for semantic uncertainty is sensitive to minor variations in responses. 
To address this issue, the authors propose a refined method, semantic embedding uncertainty (SEU), which is based on the average pairwise cosine similarity of the generated responses’ embeddings. The SEU consistently outperforms other baselines on three short-answer datasets. However, SEU still requires multiple runs of LLMs to collect a set of responses. To estimate uncertainty within a single forward pass, Amortised SEU is presented, which introduces a latent variable model to impute latent semantic embeddings with regard to the embeddings of an input.  Experimental results show ASEU achieves better performance than another single forward-pass baseline, length normalized predictive entropy.

### Strengths
1. the paper is well-written with a clear storyline
2. the Amortised SEU is able to estimate uncertainty within a single forward pass,  which is efficient and interesting

### Weaknesses
1. Apart from the Amortised SEU, I find that the scientific contribution of SEU (average pairwise cosine similarity) is not sufficient. 
First, the proposed SEU is a simple adapted version of the original semantic uncertainty. Second,   The authors claim that bidirectional entailment cannot provide continuous scores, but it is doable to use the probability of the NLI model for this purpose. I would suggest adding another baseline that replaces cosine similarity in SEU with the NLI scores. 
2. The experimental setting should be improved. First, it is necessary to compare SEU to other embedding-based methods, e.g., INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection (ICLR 2024). Second, it is useful to report multiple metrics for evaluating uncertainty methods, e.g., Brier and ECE. Last, even though the authors mention the problem of the ROUGE-L metric and only short-answer datasets, I would believe that it is easy to mitigate these issues, e.g., Bert score and evaluation of long-form questions like TruthfulQA
3. Amortised SEU required further fine-tuning while other baselines are unsupervised. The generality of ASEU is not clear

### Questions
1. in line 185, "cosine similarity provides a continuous metric". In fact, the bidirectional entailment can also offer continuous scores by using the output probability (or logit). 
2. ROUGE-L cannot capture the semantic equivalence well and is insensitive to word orders. The evaluation step needs further improvement by using better metrics such as BERTScore and LLM-as-Judge (though stated in the conclusion)
3. It is important to report multiple metrics for uncertainty estimation, e.g., Brier and ECE.
4. a key baseline is missing: INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection (ICLR 2024), which develops an EigenScore metric to measure the semantic consistency in the embedding space.  
5. In Table 2, it is hard to see the benefit of SEU since it leads to a worse FPR

### Soundness
2

### Presentation
3

### Contribution
3
