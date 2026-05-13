# Refine Knowledge of Large Language Models via Adaptive Contrastive Learning

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
How to alleviate the hallucinations of Large Language Models (LLMs) has always been the fundamental goal pursued by the LLMs research community. Looking through numerous hallucination-related studies, a mainstream category of methods is to reduce hallucinations by optimizing the knowledge representation of LLMs to change their output. Considering that the core focus of these works is the knowledge acquired by models, and knowledge has long been a central theme in human societal progress, we believe that the process of models refining knowledge can greatly benefit from the way humans learn. In our work, by imitating the human learning process, we design an Adaptive Contrastive Learning strategy. Our method flexibly constructs different positive and negative samples for contrastive learning based on LLMs' actual mastery of knowledge. This strategy helps LLMs consolidate the correct knowledge they already possess, deepen their understanding of the correct knowledge they have encountered but not fully grasped, forget the incorrect knowledge they previously learned, and honestly acknowledge the knowledge they lack. Extensive experiments and detailed analyses on widely used datasets demonstrate the effectiveness and competitiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors tackle the issue of hallucination, specifically factual errors, in Large Language Models (LLMs) by introducing a novel knowledge boundary delineation method and an Adaptive Contrastive Learning strategy. This approach aims to enhance the model's ability to accurately represent and refine its knowledge, maintain known facts, consolidate uncertain knowledge, and forget incorrect information. Through experiments on both in-distribution and out-of-distribution datasets, the authors demonstrate a significant improvement in the models' Truthful rate, bolstering the validity of their proposed methods and offering valuable insights for future research in enhancing the reliability and honesty of LLMs.

### Strengths
The authors propose a new knowledge representation method for LLMs, which assists the model in better refining its own knowledge scope, enhances the model’s honesty and alleviates the model’s hallucination problem through a new knowledge boundary division.

The  authors design an Adaptive Contrastive Learning strategy, through which the model can maintain its known knowledge, consolidate the known but uncertain knowledge, and forget the unknown knowledge, which improves the validity and honesty of the model’s responses.

### Weaknesses
The experiments in the paper are not solid enough, only on LLAMA2-7B, and more different models such as Qwen2.5 series should be considered to enhance the said reliability of the experimental results. And the effect on different size models should also be considered and analyzed, such as 13B and above.  

The baseline in the paper is too simple and lacks comparison with other up-to-date approaches to knowledge boundary identification.

### Questions
Since the use of the proposed method enables the model to distinguish knowledge boundaries effectively, it would be interesting to study the performance of the model after using the RAG technique. For example, comparison experiments with paper [Enhancing Noise Robustness of Retrieval-Augmented Language Models with Adaptive Adversarial Training](https://aclanthology.org/2024.acl-long.540) (Fang et al., ACL 2024) could be added.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper tries to mitigate the hallucination problem of large language models by proposing an Adaptive Contrastive Learning strategy. The method curates data that represent the zones of "model knows it knows", "model doesn't know it knows", "model doesn't know it doesn't know", and designs contrastive learning loss to strengthen the model's desired behavior to be more trustworthy when answering questions. Experimental results show that the proposed method outperforms "I don't know" prompting and "I don't know" SFT.

### Strengths
1. The results of the paper are solid, as the proposed method outperforms IDK-Prompting and IDK-SFT by a large margin. Contrastive learning is not a new method, but the paper provides a good example of how to use it to improve large language models with careful contrastive pairs and loss design.
2. The paper is well-motivated with well-made figures illustrating the data construction idea. The hallucination issue is a major block of using LLMs in high-stake scenarios, and many papers have thought of tuning the models to output "I don't know"[1]. However, the existing papers usually only consider the dichotomy of answerable and unanswerable questions without having a 2-D division of the space. It's interesting to see this paper brings out this concept as it's not only useful for helping model learning but could also help human learning [2].

[1] R-Tuning: Instructing Large Language Models to Say "I Don't Know", Zhang et al., NAACL 2024.

[2] Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations, Jiang et al., EMNLP 2024.

### Weaknesses
1. Even though the results look strong by looking at the Truthful Rate, I am not sure whether the proposed Truthful Rate is well-defined. Given the denominators of IK-IK Rate and IK-IDK Rate are different, I don't think it's rigorous to add them together as the final score. An alternative could be treating answering "I don't know" to those answerable questions as correct and computing the overall accuracy on the full dataset. Also, why the IK-IK rate for Mistral-7B-Instruct-v0.1 drops drastically compared to IDK-prompting? This is a bit concerning as it indicates after Adaptive Contrastive Learning, the model may not be useful anymore.
2. i am unsure what's the major takeaway of Section 5.3. Does the accuracy under repeated samplings represent the concept of "confidence"? Actually, the paper mentions the term of "confidence" when introducing the motivation of the proposed method. It would be interesting to see whether the proposed method can draw a more rigorous connection of model's confidence in its generation.
3. The presentation for the paper can be further improved. See my detailed comments below.

### Questions
I think the paper can benefit from a careful round of proofreading. Here are some nits I discovered when reviewing the paper:
1. In Table 1, it's better to use "IDK" instead of "idk" to be accord with the main paper.
2. I suggest rewriting Section 5.2 as the current writing is a bit confusing, even though I can get the meaning by reading Table 3. For example, for the first bullet point, "With" should be "Without" based on my understanding.
3. I am wondering if the notations of the paper can be improved. For example, using $IDKIK$ as subscript in equations looks weird.

### Soundness
3

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
3

### Summary
This paper primarily addresses the issue of hallucination in large language models (LLMs), particularly when models provide incorrect or fabricated answers to questions they cannot answer, severely impacting model trustworthiness.

### Strengths
The paper is well-structured, especially in its quadrant-based classification of knowledge and its innovative use of an adaptive contrastive learning strategy, demonstrating a rigorous design approach. By combining knowledge classification with an adaptive loss function, it presents a novel solution to effectively address the hallucination problem in LLMs.

### Weaknesses
First, the experiment coverage is relatively narrow, with results demonstrated on only two datasets. Although the method shows promising results, its broad applicability across more tasks and domains is uncertain. Expanding the evaluation to more diverse datasets, such as dialogue or fact-checking datasets, would help validate the robustness and applicability of the method. 
Second, although the paper proposes using a combination of three loss functions for different types of knowledge, it does not delve into the interactions and balance between these loss functions. In different scenarios, each loss may contribute differently; exploring the interactions and balance of these loss functions across various tasks would further strengthen the theoretical foundation of this method.

### Questions
I don't have questions.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors emulate the human learning process by proposing an **Adaptive Contrastive Learning** strategy. This approach dynamically constructs positive and negative samples based on the actual mastery of knowledge in Large Language Models (LLMs). It enhances LLM's understanding of the correct knowledge they have encountered but not fully grasped, allows them to discard incorrect knowledge they previously learned, and candidly recognizes the knowledge they lack. Extensive experiments and detailed analyses demonstrate the effectiveness of this method.

### Strengths
- **Innovative Knowledge Representation Method:** This is a well-written paper. The knowledge quadrant refines the boundaries of an LLM’s knowledge representation, aligning it more closely with real-world human knowledge needs.

- **Well-Motivated Adaptive Contrastive Learning Strategy:** By maximizing the distance between negative samples and minimizing the distance between positive samples, the model learns to preserve its existing knowledge, consolidate known but uncertain information, and forget unknown knowledge. This approach enhances the validity and honesty of the model’s responses.

- **Effective Approach:** Experimental results demonstrate that the strategy achieves the highest truthful rate across various advanced LLMs with both in-distribution and out-of-distribution data, thereby confirming the effectiveness of the proposed strategy.

### Weaknesses
 - In this work, the discussion surrounding the concept of "I know that I don't know" (Quadrant 2) is lacking. Could you provide an explanation of how to differentiate between the knowledge categories of "I know that I know" and "I know that I don't know"? Specifically, would you categorize information as "I know that I don't know" if the model consistently responds with "I don't know" across all sampling responses?

### Questions
- How does varying the inference temperature affect the model confidence in your setting?

### Soundness
3

### Presentation
4

### Contribution
3
