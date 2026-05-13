# Enhancing Unsupervised Sentence Embeddings via Knowledge-Driven Data Augmentation and Gaussian-Decayed Contrastive Learning

- Decision: Reject
- Scores: 5, 6, 3, 3, 5

## Abstract
Recently, using large language models (LLMs) for data augmentation has led to considerable improvements in unsupervised sentence embedding models. 
However, existing methods encounter two primary challenges: limited data diversity and high data noise. 
Current approaches often neglect fine-grained knowledge, such as entities and quantities, leading to insufficient diversity.  Additionally, unsupervised data frequently lacks discriminative information, and the generated synthetic samples may introduce noise.
In this paper, we propose a pipeline-based data augmentation method via LLMs and introduce the Gaussian-decayed gradient-assisted Contrastive Sentence Embedding (GCSE) model to enhance unsupervised sentence embeddings.
To tackle the issue of low data diversity, our pipeline utilizes knowledge graphs (KGs) to extract entities and quantities, enabling LLMs to generate more diverse, knowledge-enriched samples. 
To address high data noise, the GCSE model uses a Gaussian-decayed function to limit the impact of false hard negative samples, enhancing the model's discriminative capability.
Experimental results show that our approach achieves state-of-the-art performance in semantic textual similarity (STS) tasks, using fewer data samples and smaller LLMs, demonstrating its efficiency and robustness across various models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the use of large language models for data augmentation to generate unsupervised sentence embeddings. To overcome two limitations of existing methods: limited data diversity and high data noise, the authors propose using knowledge graphs to extract entities and quantities to address low data diversity. Additionally, they suggest using a Gaussian-decayed function to limit the impact of false hard negative samples in the Contrastive Sentence Embedding model to tackle the issue of high data noise. Experimental results on semantic textual similarity (STS) and reranking tasks indicate that the proposed method offers certain improvements over existing large language model-based approaches.

### Strengths
The authors have provided a thorough analysis and summary of the shortcomings of existing methods.

This paper is easy to follow, and the technical approach is sound.

### Weaknesses
Although introducing the Gaussian-decayed function into SimCSE is straightforward, its contribution does not seem very significant.

From the results in Tables 2 and 3, the improvement of GCSE over SynCSE appears to be relatively minor in many cases. I suggest conducting multiple experiments and reporting the results of statistical significance tests.

### Questions
If SynCSE and GCSE use the same LLM, would the improvement be greater? Could you provide these results?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To address the challenges of unsupervised sentence embedding models in terms of data diversity and noise, this paper first proposes a pipeline-based data augmentation method using large language models. This method utilizes knowledge graphs to extract entity and quantity information, generating more diverse samples. Next, the paper introduces a Gaussian Contrastive Sentence Embedding (GCSE) model assisted by a Gaussian decay function to reduce the impact of false negative samples and enhance the model's discriminative ability. Finally, the paper demonstrates that this approach achieves SOTA performance on semantic textual similarity  tasks, while exhibiting efficiency and robustness with fewer data samples and smaller LLMs.

### Strengths
1. By integrating knowledge graphs and LLMs, the paper proposes a novel data augmentation approach that effectively enhances sample diversity and embedding quality.
2. The introduction of the Gaussian decay function significantly mitigates the impact of false negative samples, bolstering the model's robustness.
3. While reducing data requirements and model size, the method presented in this paper achieves state-of-the-art performance across multiple benchmarks, demonstrating its efficiency and generalization capability.

### Weaknesses
1. The core motivation of this paper's approach is data diversity and data noise. Although higher benchmark performance has been achieved, there is a lack of significant quantitative analysis on how the proposed methods or modules enhance data diversity and reduce data noise. For example, could some quantitative metrics be used to intuitively demonstrate the improvements in data diversity and reductions in data noise brought about by the proposed method or individual modules?

### Questions
1. Is it possible to visually demonstrate the improvement in data diversity and reduction in data noise brought about by the proposed method through some quantitative metrics (same as Weakness) ?

2. Ablation analysis of the hyperparameters α and β in equations 10 and 11.

3. The impact of different LLMs on performance, and whether replacing with a more powerful LLM could raise the method's upper limit.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a STS task-related data augmentation method, prompting LLM for entity extraction, KG construction and data generation. It also introduces a Gaussian-decayed function to align hard negatives between a training encoder and a frozen encoder.

### Strengths
1. The paper is well-written. The figures are neat and clear to read.
2. The pipeline of utilizing prompt engineering, entity extraction and KG construction serves as a new paradigm of data augmentation for STS tasks.

### Weaknesses
1. Analysis of false positive (FP) and negative (FN) in Figure 1 is unconvincing. See Question 1 for details.
2. The improvements (0.28 with BERT-base, 0.23 with BERT-large, and 0.46 with RoBERTa-large) seem very marginal.
3. The motivation of choosing Gaussian-decayed function is unclear. No theoretical proves on the modification with Gaussian-decayed function.

### Questions
1. In figure 1, why choosing 0.5 as a hard limit to distinguish Positives & Negatives? Can we choose other limits, like >0.8 is Positives, < 0 is Negatives, and 0~0.8 is ambiguous? Theoretically,  most embedding models like SimCSE are trained with a list-wise temperature-scaled contrastive loss, which is basically optimized via Cross-Entropy. The distribution of query-positive cosine similarity scores will be pushed greatly towards 1.0, and query-negative scores towards -1.0. If SimCSE is trained with some optimization object like a point-wise MSE loss, choosing 0.5 will be more rational. Thus, I suggest you to set a hard limit Top-k window for the prediction of Positives & Negatives. For example, the prediction with largest similarity is positive, and lowest is negative.
2. Can you do statistic significant tests on your results?
3. Where is the evaluation model E′ in Figure 4?
4. Why choosing Gaussian-decayed function? Does it have some special mathematical traits? Can we just choose a MSE loss / Cross-Entropy loss / KL loss to align hard negatives between the training encoder and frozen encoder?
5. Why do you want to align the hard negatives between the training encoder and frozen encoder?
6. Why do you train a frozen encoder first, then train a new encoder with the LLM-generated data? Can we just merge these steps to one stage? 
7. Line 311: How would the “spatial distribution of negatives” change? How will the gradients update?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a data augmentation method related to the STS task, aiming to prompt LLMs for entity extraction, knowledge graph construction, and data generation. Additionally, it introduces a Gaussian-decayed function to align hard negatives between a training encoder and a frozen encoder.

### Strengths
The proposed pipeline, which leverages prompt engineering, entity extraction, and knowledge graph construction, introduces a novel paradigm for data augmentation in STS tasks. The paper is well written and easy to follow.

### Weaknesses
1、The motivation is not clearly clarified. why was a Gaussian-decayed function chosen?
2、The experimental improvement is marginal.  

missing references;
[1]  Zhou K, Zhang B, Zhao W X, et al. Debiased contrastive learning of unsupervised sentence representations[J]. arXiv preprint arXiv:2205.00656, 2022.
[2] Wu X, Gao C, Su Y, et al. Smoothed contrastive learning for unsupervised sentence embedding[J]. arXiv preprint arXiv:2109.04321, 2021.

### Questions
1、Why was a Gaussian-decayed function chosen? 
2、Why train a frozen encoder first, followed by training a new encoder with LLM-generated data? What's the benefit?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a pipeline-based data augmentation method via LLMs and introduces the Gaussian-decayed gradient-assisted Contrastive Sentence Embedding (GCSE) model to enhance unsupervised sentence embeddings. The data augmentation first constructs a knowledge graph (KG) with the extracted data, guides LLM to generate more diverse positive samples, and filter noisy data. Experimental results show its effectiveness.

### Strengths
1. The paper is well-written.
2. The data augmentation is interesting.

### Weaknesses
1. The main results are based on BERT and Roberta. However, LLMs are effective in sentence embedding [1,2]. Please use LLMs for evaluation. Using only ChatGLM-3 for evaluation is not convincing. Therefore, the experimental evaluation in this paper should be redone.

2. Analysis of \alpha and \beta.

3. Two missing references. [3] is about data noise and [4] is about data augmentation.

4. The motivation of Gaussian-decayed function needs to be demonstrated more clearly.

5. It is not clear that the methods in this paper are superior to recent methods [1,2]. Furthermore, it is unclear whether the data augmentation method in this paper has an advantage compared to [3]. Conducting a thorough comparison and evaluation with recent related works would improve the soundness of this paper.

### Questions
Why the Gaussian-decayed function G() in the denominator? It seems that the Gaussian-decayed function has no connection with the denominator. Can we just add the Gaussian-decayed function to the contrastive learning loss?

### Soundness
1

### Presentation
3

### Contribution
1
