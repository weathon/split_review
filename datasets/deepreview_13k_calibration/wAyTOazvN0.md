# Learning Multiplex Embeddings on Text-rich Networks with One Text Encoder

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
In real-world scenarios, texts in a network are often linked by multiple semantic relations (e.g., papers in an academic network are referenced by other publications, written by the same author, or published in the same venue), where text documents and their relations form a multiplex text-rich network. Mainstream text representation learning methods use pretrained language models (PLMs) to generate one embedding for each text unit, expecting that all types of relations between texts can be captured by these single-view embeddings. However, this presumption does not hold particularly in multiplex text-rich networks. Along another line of work, multiplex graph neural networks (GNNs) directly initialize node attributes as a feature vector for node representation learning, but they cannot fully capture the semantics of the nodes’ associated texts. To bridge these gaps, we propose METERN, a new framework for learning Multiplex Embeddings on TExt-Rich Networks. In contrast to existing methods, METERN uses one text encoder to model the shared knowledge across relations and leverages a small number of parameters per relation to derive relation-specific representations. This allows the encoder to effectively capture the multiplex structures in the network while also preserving parameter efficiency. We conduct experiments on nine downstream tasks in five networks from both academic and e-commerce domains, where METERN outperforms baselines significantly and consistently. Code is available at https://anonymous.4open.science/r/METERN-ICLR24-C6CD.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces an approach to learn embeddings for nodes in multi-relational knowledge graphs where the node embedding is conditioned on the target relation of interest. The relation-informed embedding is to be used for knowledge graph inference. 

The approach to learn the embedding is to include prefix embeddings to the language model encoder  that are relation-specific similar to prefix tuning. The relation embeddings are learned from the training data by maximizing similarity of observed node pairs as is typical for knowledge graph embedding. At inference time, when it is not apparent what relevant relation embedding to use , the authors propose an attention over the trained relation embeddings that is learned from some limited samples from the target task.

The authors perform evaluation of their approach, comparing with some existing approaches (some of which like GNN do not use language model encoders) and some single node embedding baselines. The approach seems somewhat better than the baselines.

### Strengths
- The paper seems easy to follow and the problems is clearly described.
- Results show good improvements over baselines.

### Weaknesses
 - The approach is very much prefix tuning applied to this problem of knowledge graph inference, so as such there is little novelty in the approach.
- Baselines: 
   - some of the baselines like multiplex GNN use weaker bag of word encoder so they are not directly comparable.
   - other baselines it's hard to see which baselines actually use a comparable encoder to the proposed model, ideally all baselines should have the same underlying encoder 
- The approach is missing comparison with the simpler, no training required, baseline of adding a natural language description of the relation before encoding (instead of learned prefix embeddings). This approach is also directly applicable at inference time without requiring any additional training for unseen relations. This should potentially be applied with larger LM embeddings as well since there is no additional training needed.

### Questions
See "weakness" section for concerns with baselines.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work focuses on generating multiplex embeddings i.e. relation-conditioned node/text embedding for each relation type. The paper address the challenges of prior art in terms of time and memory, as the the prior art employed one encoder for each relation types in learning multiplex embeddings. 
In doing so, they encode multiplex embeddings by introducing prior relation tokens and computing relation-conditioned embeddings with one encoder using the node/text information and the target relation as input such that relation-specific signals are encoded in each relation embeddings and on top, shared knowledge across relations is captured by a single encoder.  The paper also contributes in inference schemes: direct and "learn-to-select-source-relations" inference to map/select source relation and corresponding embeddings for downstream tasks.

Experimental setup is comprehensive, employing several datasets and  baselines approaches. The approach has shown improved performance for downstream tasks and gained efficiency in term of time and memory compared to the baseline approaches.

### Strengths
+ the paper is well written and easy to follow 
+ motivation, problem statement and methodology is well formulated 
+ the paper is incremental however simple in extending the baseline research, like using one encoder for generating relation-conditioned multiplex embeddings instead of employing one encoder for one relation type
+ the paper also contributes in inference strategies for selecting source relations for downstream tasks 
+ the proposed approach is incremental, however proposes benefits in terms of compute cost and performance boost on downstream tasks
+ the proposed approach has been evaluated across different data sets, sound exprimental setup and qualitative evaluation 
+ sound abalation studies and efficiancy analysis  e.g. time and memory optimization 
+ the paper also presents a good study and insights on relation weights and multiplex embedding visualization 
+ experimental setup is comprehensive

### Weaknesses
 - the paper is incremental and advances the baseline approaches in multiplex embedding representation, like introducing a single encoder to generate relation-conditioned multiplex embeddings for each relation type instead of using several encoders
- still there are few questions about claims on scalability (please see question section) 
- the scalability of "learning-to-select-source-relations" for downstream tasks for novel relation types is unclear?

### Questions
- how does text encoder handle the concept drift induced due to different relation or data distribution or domains?
- how to predetermine the number of relation types and corresponding relation prior tokens? 
- In multiplex text-rich network, what is the span (context) of associated texts to compute node representation?

- Transformers in essence are a special case of GNN - they semantically compute a different contextualized representation for each token (or multiple text tokens) in the text sequence and encode different relationship in different contexts. How does it differ with the proposed method of computing multiplex representation for texts for nodes? 

- Here, the example are contrary to proposed method - multiplex representation for a token or text sequence for example for the word "llama", however, in the proposed method, node is representing a document, which is longer text and may consists of several thematic structures like topics. Please clarify.

- how does the multiplex representation learning approach scale as the number of relation scales between entities? Similarly, if many relations exists among entities, there are many representations of the same texts due to different relations. How does the approach scale in terms of handling multiplex embedding representations for the sake of leveraging overlapping semantics across relations ?

- On one hand, the method proposes to use only one text encoder to learn different relation embeddings however on other side, generating as many embeddings of the same text in different relations. Scalability is still challenging with this approach in real-world application? 

- How does the "learn-to-select-source-relations" inference work for novel relations on the downstream task? the approach seems to works with relations of known type or the downstream task has to select a relation from one of the source relations?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a framework for learning multiplex embeddings in text-rich networks. The authors address the challenges of modeling diverse semantic relations among texts in real-world scenarios, where traditional methods based on pre-trained language models (PLMs) fall short due to their single-view embeddings. Additionally, multiplex GNNs cannot capture the semantics of associated texts effectively. METERN overcomes these limitations by using one shared PLM encoder with relation prior tokens to capture both shared knowledge and relation-specific signals. The paper demonstrates the effectiveness of METERN on various downstream tasks across academic and e-commerce networks.

### Strengths
- The paper addresses an important and challenging problem in multiplex text-rich networks and proposes an innovative approach, METERN, to tackle it. This approach leverages relation prior tokens and a shared PLM encoder to capture both shared and relation-specific information, providing a unique solution to the problem.

- The authors provide extensive experimental results across a range of downstream tasks and domains, demonstrating the effectiveness of METERN in outperforming competitive baseline methods. This empirical validation adds credibility to the proposed approach and its practical utility.

- The paper discusses the application of METERN in different scenarios, including direct inference and "learn-to-select source-relation" inference, which enhances the versatility of the proposed framework.

### Weaknesses
 - The paper could benefit from a more detailed and structured discussion of related works. Currently the line spacing is too small and more detailed discussions can provide more context for readers.

- The paper introduces "relation prior tokens" as a novel concept, but lacks thorough discussions of the computational complexity and scalability implications of this approach.

- While the paper emphasizes the problem of multiplex representation learning in text-rich networks, it could benefit from real-world use cases or examples to illustrate the practical applications and impact of the proposed method.

### Questions
Can you elaborate on real-world use cases or examples where METERN's multiplex representation learning could have a significant impact, such as in academic networks or e-commerce domains? How might this framework be adopted and adapted in practical scenarios?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work notices that a real-word text graph usually has multiple types of edges connecting text documents, which is called multiplex network. To account for such multi-type edges, authors propose to assign embeddings for different relations or edge types. The embeddings in turn are concatenated with text tokens for encoding. Furthermore, since some downstream tasks may not have a direct alignment with any observed relation or edge type, authors propose an inference method to learn text embeddings with an attention mechanism for different edge types. Experiments show the effectiveness of the proposed model.

### Strengths
1. Clear motivation. This paper clearly introduces the drawback of existing works and explains why a multiplex network is important and why a text should possess multiple embeddings to capture different relations.

2. This paper is self-contained and comprehensive with the evidence that authors present a figure for visual illustration of the model, text description of the modeling component, complexity analysis, as well as a contrast against existing works.

3. Experiments are comprehensive with different tasks and baselines from different categories.

### Weaknesses
1. When conducting experiments, we usually encourage authors to repeat the same experiments multiple times and report both mean and standard deviation. However, I see mean results only, but not standard deviation, which is hard for readers to judge the significance of the outperformance over baselines.

2. Insufficient baselines. There are models that work on text-rich networks with pretrained language models, such as GraphFormer [1] and LinkBERT [2]. Though they are designed not for multiplex networks, it is worth comparing against them to highlight the advantage of the multiplex network proposed by this submitted work.

[1] Yang, J., Liu, Z., Xiao, S., Li, C., Lian, D., Agrawal, S., ... & Xie, X. (2021). GraphFormers: GNN-nested transformers for representation learning on textual graph. Advances in Neural Information Processing Systems, 34, 28798-28810.

[2] Yasunaga, M., Leskovec, J., & Liang, P. (2022, May). LinkBERT: Pretraining Language Models with Document Links. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) (pp. 8003-8016).

3. Some math notations are not well defined, such as superscript $m$ at second line in page 4 and superscript $s$ at second last line in page 4. Authors are suggested to provide a table to summarize main mathematical notations used.

### Questions
1. How to handle a previously unseen relation during testing phase?
2. what does superscript $m$ mean and how to set a value for it? Same question for superscript $s$.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
