# Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
Representation learning on text-attributed graphs (TAGs) has become a critical research problem in recent years. A typical example of a TAG is a paper citation graph, where the text of each paper serves as node attributes. Initial graph neural network (GNN) pipelines handled these text attributes by transforming them into shallow or hand-crafted features, such as skip-gram or bag-of-words features. Recent efforts have focused on enhancing these pipelines with language models (LMs), which typically demand intricate designs and substantial computational resources. With the advent of powerful large language models (LLMs) such as GPT or Llama2, which demonstrate an ability to reason and to utilize general knowledge, there is a growing need for techniques which combine the textual modelling abilities of LLMs with the structural learning capabilities of GNNs. Hence, in this work, we focus on leveraging LLMs to capture textual information as features, which can be used to boost GNN performance on downstream tasks. A key innovation is our use of \emph{explanations as features}: we prompt an LLM to perform zero-shot classification, request textual explanations for its decision-making process, and design an \emph{LLM-to-LM interpreter} to translate these explanations into informative features for downstream GNNs. Our experiments demonstrate that our method achieves state-of-the-art results on well-established TAG datasets, including \texttt{Cora}, \texttt{PubMed}, \texttt{ogbn-arxiv}, as well as our newly introduced dataset, \texttt{tape-arxiv23}. Furthermore, our method significantly speeds up training, achieving a 2.88 times improvement over the closest baseline on \texttt{ogbn-arxiv}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a method to solve TAG problems. The method uses an LLM to generate category prediction and explanation of the target node, then the explanation is used as an enhancing part of the node feature. An LM is used to encode the raw text feature and the additional explanation into hidden space. A GNN predictor receives the hidden features, the prediction of LLM, and the shallow embeddings to give the final classification results. Experiments on several TAGs show the effectiveness of the method.

### Strengths
1. The paper is clearly written and easy to follow.
2. Bagging LLM prediction, LM features and shallow features is reasonable for the node classification task.
3. The experiments show the method can achieve SOTA performance on several benchmark datasets.

### Weaknesses
1. The main concern is that the method has little to do with graph. It seems like an application attempt of LLMs on natural language tasks, and TAG is just a scenario. Thus the contribution of the method is limited.
2. Since the Debera need fully fine-tuning, training the method cost much more memory than pure GNN methods.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a framework for representation learning on text-attributed networks. The authors first prompt the LLM to obtain explanations and predictions for each node based on its textual information. Then they finetune language models on different textual attributes and obtain feature embeddings. Finally, the graph neural network adopts the learned embeddings from the second step to conduct the final prediction.

### Strengths
1. The author proposes a method to augment LM with LLM-generated features.
2. The paper is easy to follow.

### Weaknesses
1. Lack of baselines. Many important baselines that conduct learning with language models on TAGs including GraphFormers [1] and Patton [2] are missing in the experimental section. The absence of these baselines makes it difficult to assess the true performance of the proposed method in comparison to state-of-the-art techniques that leverage language models for text-attributed graphs. Specifically, GraphFormers [1] which uses a GNN-nested transformer architecture and Patton [2] which focuses on language model pretraining on text-rich networks, represent key approaches that should be included for a comprehensive evaluation.
2. The theorem is not specific to this problem. The theorem in 4.4 is not particular for LLM and LM for TAGs, and needs strong assumptions. The theorem, as stated, lacks specificity to the unique challenges and characteristics of text-attributed graphs and the interplay between LLMs and LMs within this context. The assumptions required for the theorem to hold true are not clearly justified within the specific application of the proposed framework.
3. Lack of evaluation tasks. The paper claims to do representation learning on TAGs but only evaluates the node classification task. It would be better to add experiments on other tasks such as link prediction to evaluate the quality of the representations. Evaluating only on node classification limits the understanding of the quality of the learned representations. The paper should demonstrate the versatility of the learned embeddings by including experiments on other tasks such as link prediction or graph classification.
4. Lack of ablation studies. 1) If we need to finetune the LM in step 2 or not?; 2) Why do we need to have different LM for original text encoding and explanation encoding? The paper lacks a thorough ablation study to justify key design choices. Specifically, it is unclear whether fine-tuning the language model in step 2 is necessary for optimal performance. Furthermore, the rationale behind using separate language models for original text and explanation encoding is not sufficiently explored.
5. Limit novelty. While I appreciate the introduction of the new arxiv-2023 dataset, the technique contribution of this work is very limited, which basically introduces LLM to conduct data augmentation for node classification on TAGs. The core contribution of the paper appears to be the use of LLMs for data augmentation, which is not a novel concept. The overall approach lacks significant technical novelty beyond the application of LLMs for generating node explanations.

### Questions
Please refer to the comments raised in the weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the challenge of leveraging Large Language Models (LLMs) such as GPT to enhance the performance of Graph Neural Networks (GNNs) on Text-Attributed Graphs (TAGs). The authors propose an innovative approach called GRAPHTEXT, which combines LLMs' textual modeling abilities with GNNs' structural learning capabilities. The key innovation lies in using explanations generated by LLMs as features to boost GNN performance on downstream tasks.

### Strengths
1. The proposed method presents a novel and effective way to integrate the power of LLMs, like GPT, with GNNs to handle text-attributed graphs. By using LLMs to generate explanations and converting them into informative features for GNNs, it bridges the gap between textual information and graph structure, enabling more sophisticated graph reasoning.

2. The experimental results demonstrate that the proposed method achieves state-of-the-art performance on well-established TAG datasets, including Cora, PubMed, ogbn-arxiv, and a newly introduced dataset, arXiv-2023. This underscores the effectiveness of the proposed approach in improving the accuracy of downstream tasks on TAGs.

3.The proposed method not only enhances performance but also significantly speeds up training. It achieves a 2.88 times improvement over the closest baseline on the ogbn-arxiv dataset. This computational efficiency is crucial for practical applications and scalability.

### Weaknesses
1. The time analysis and money estimation are lacking. The paper utilizes the chatgpt API, nonetheless, there is a large restraint on the word limitation per day, and the cost of one dataset should also be taken into consideration. Specifically, the paper should detail the number of API calls required for each dataset, the average token length of both input and output sequences, and the associated monetary cost based on current API pricing. A breakdown of the time required for processing each dataset, considering API rate limits, is also necessary.

2. The robustness of the prompt is lacking. The paper proposed a single prompt for the node classification. Nonetheless, is another similar prompt can achieve a similar performance. The paper should explore the sensitivity of the method to variations in prompt design. This should include testing different prompt phrasings, instructions, and levels of detail to determine the consistency of performance. A more systematic analysis of prompt engineering is needed to ensure the reliability of the results.

3. There may lack of ablation study on the LM. Current LM focuses on BERT, while other LM are ignored. Recent paper demonstrates that they can achieve satisfying performance with only SentenceBert Embedding. The paper should provide a more comprehensive ablation study on the choice of language model. This should include experiments with other popular models, such as Sentence-BERT, RoBERTa, or other embedding models, to assess the impact of different text representations on the final performance. The study should also compare the computational cost and performance trade-offs of these models.

4. There lack some experimental results in table 1, especially Giant.

### Questions
See the weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
