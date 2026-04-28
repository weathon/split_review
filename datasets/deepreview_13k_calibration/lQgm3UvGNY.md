# Synergistic Information Retrieval: Interplay between Search and Large Language Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 6, 3

## Abstract
Information retrieval (IR) plays a crucial role in locating relevant resources from vast amounts of data, and its applications have evolved from traditional knowledge bases to modern retrieval models (RMs). The emergence of large language models (LLMs) has further revolutionized the IR field by enabling users to interact with search systems in natural languages. In this paper, we explore the advantages and disadvantages of LLMs and RMs, highlighting their respective strengths in understanding user-issued queries and retrieving up-to-date information. To leverage the benefits of both paradigms while circumventing their limitations, we propose $\textbf{InteR}$, a novel framework that facilitates information refinement through synergy between RMs and LLMs. InteR allows RMs to expand knowledge in queries using LLM-generated knowledge collections and enables LLMs to enhance prompt formulation using retrieved documents. This iterative refinement process augments the inputs of RMs and LLMs, leading to more accurate retrieval. Experiments on large-scale retrieval benchmarks involving web search and low-resource retrieval tasks demonstrate that InteR achieves overall superior zero-shot retrieval performance compared to state-of-the-art methods, even those using relevance judgment.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a Bayesian tool for retrieval-augmented generation in natural language processing. The aim of the proposed method is to improve the capability of large language models by incorporating user specific characteristics. To achieve this aim the authors a Bayesian learning method consisted of three main steps. First, they rely on counting processes to draw a finite sample of diverge documents and thus obtain characteristics from the user. In the next stage they use a Bayesian procedure to update their beliefs about the user's preference preference metric and finally they accordingly prioritize their responses to the user's query. After carefully presenting their proposed techniques the authors rely on simulated datasets and show empirical evidence for outperformance of their approach compared to existing methods in the literature.

### Strengths
The paper is well-written and address a significant problem for the improvement of applications that are used by a large amount of people nowadays. The paper does not lack of originality since proposes a Bayesian learning approach for a problem where Bayesian methods are not well-developed. I think that after a major revision the quality of the paper will be enough for getting published in ICLR.

### Weaknesses
The paper is not linked carefully with the related literature. Moreover, although the authors propose a Bayesian approach to deal with information retrieval for large language models they do not clearly explain the advantages of Bayesian methods in these type of problems. Finally, I think that the paper lacks of a comprehensive comparison with existing methods. The authors perform comparisons only on simulated data, they do not explain why the choose specific alternatives to compare whereas they do not explain if the differences in efficiency that they show are significant in a statistical manner.

### Questions
The authors should include a Section of related work after their introduction. Since the paper proposes a Bayesian learning technique the authors should clearly explain the advantages of Bayesian methods in these type of problems. The paper presents results only on simulated data although they exist several widely-used real datasets that could be also employed for the comparison with existing methods. The authors should also justify their particular choices for the methods with which the compared their developed technique, are these methods the most relevant to the problem they study? The authors should also comment on the computational cost of the methods under comparison. Finally, the authors should explain if the outperformance of their proposed technique is statistically significant.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Information retrieval (IR) is a critical technique to locate relevant data in vast collections. Modern search engines (SEs) are based on neural representation learning and large language models (LLMs), which provide contextual understanding and the potential to save time by directly answering queries. However, LLMs have limitations, such as generating outdated or incorrect information, whereas search engines can swiftly sift through vast updated data.  This paper intends to bridge the capabilities of retrieval models (RMs) and LLMs, enhances IR by expanding queries using LLM-generated knowledge and enriching LLM prompts using RM-retrieved documents.

### Strengths
1. Introduction of InteR, a framework that combines the strengths of both RMs and LLMs, addressing their individual limitations.

2.  LLMs can understand user-issued queries' context, generating specific answers rather than just presenting a list of relevant documents, RMs can provide fresh information.

3. The experimental results showcasing that InteR can perform zero-shot retrieval more effectively than other state-of-the-art methods.

### Weaknesses
1. The idea is not new, as You.com and Bing.com are doing this, and Google Bard undoubtedly has developed InTeR-like capabilities.

2. RMs require well-crafted keywords to deliver accurate results, which might not be user-friendly.  Query formulation is a problem
to be addressed.

3. The extensive reliance on vast training datasets like NQ and MS-MARCO for dense retrieval models, which can be time-consuming and may have commercial use limitations.

### Questions
1. How scalable is the InteR framework when applied to different types of data beyond the current experimental setup?

2. Can there be further optimizations in the synergy between RMs and LLMs to address real-time search requirements?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents InterR, an information retrieval method that refines the query iteratively using an LLM and a retriever model. Both modules update the query by adding new relevant information to it. When using Vicuna/gpt-3.5 in combination with BM25, the method exhibits competence against zero-shot models as well as those based on relevance judgements on web search and low-resource scenarios. Ablation and case studies are included to analyze the method.

### Strengths
- The method is simple yet very effective. The results are strong.
- The idea is not super novel but original to the best of my knowledge.
- Reproducibility: The authors promise to release the code.
- Clarity: The paper is overall well-written.

### Weaknesses
 - The method achieves strong accuracy, but its latency must have been severely compromised as it involves multiple rounds of LLM and RM querying. This makes this method unideal for most retrieval applications where latency is prioritized. Would be great to include the latency results so that readers can better understand the tradeoff.
- One part that is missing is an analysis of the side- or negative- impacts of the method. The iterative expansion will likely sometimes introduce information with negative effects. e.g. irrelevant info, contradictory logics, hallucinated content, lexically similar but semantically irrelevant texts, etc. How often does this happen? How does this hurt performance? Any potential mitigation strategy?

### Questions
- Are the authors from Microsoft? If so, there is a potential **RISK OF IDENTITY LEAK** as they use the Bing logo in Figure 1 but the experiment setting is totally irrelevant to Bing. I am just pointing out the risk here and will let the meta-reviewer decide whether this is an issue or not.
- On what dataset do you tune the hyperparameters on? If it is the test set, then it largely weakens the reliability of the conclusions.
- Another area of related work to cite and discuss is query rewriting in conversational QA (e.g. QReCC), where a NLG model is used to refine the query to augment retrieval.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper leverages LLMs (templates) to iteratively generate passages more relevant to a given user query (sections 4.2 and 4.3). The INTER model then scores passages comparing the output of the LLM and documents using a dense model. Experiments on MS MARCO, and a set of 6 BEIR datasets, show that the model performs better than ANCE or Contriever-FT.

### Strengths
- A new method for query expansion relying on LLMs
- The method is zero-shot

### Weaknesses
First, the process depending on an LLM might not offer the same guarantees as trained retrieval models - as the LLM is a black box in this case. 

Second, and more importantly, there is no comparison with sparse approaches (which have a good ZSL generalization capacity) or dense models (e.g. ColBERT-v2 or SPLADE-v2), for which the performance is much better than the proposed approach while being much lighter in terms of computation. The authors should also compare to BM25+monoT5/monoBERT since they generalize quite well on other datasets.

The argument of having a lightweight zero-shot system does not hold since these models perform at least on par with the proposed approach while being much lighter in terms of computation.

- ColBERTv2 http://arxiv.org/abs/2112.01488
- SPLADE https://doi.org/10.1145/3477495.3531857
- monoT5 https://aclanthology.org/2020.findings-emnlp.63/

### Questions
- How does the performance vary with different LLMs?
- What is the overall cost (computational) compared to other approaches?
- More experimental details on the effect of hyperparameters is needed given the very empirical nature of the approach

Other:

- DeepCT is not an unsupervised model

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor
