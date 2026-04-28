# Large Language Models based Graph Convolution for Text-Attributed Networks

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 3, 5

## Abstract
Text-attributed graph (TAG) tasks involve analyzing both structural information and textual attributes. Existing methods employ text embeddings as node features, and leverage structural information by employing Graph Neural Networks (GNNs) to aggregate features from neighbors. These approaches demand substantial computational resources and rely on two cascaded stages, limiting scalability in large-scale scenarios and making them vulnerable to the influence of irrelevant neighboring nodes. The advancement of language models (LMs) presents new avenues for tackling this task without GNNs, leveraging their ability to process text attributes of both the target node and its important neighbors. Instead of using graph convolution modules, LMs can assign weights to these tokens based on relevance, enabling token-level weighted summarization. However, it is nontrivial to directly employ LMs for TAG tasks because assessing the importance of neighbor nodes involves both semantic and structural considerations. Additionally, the large search space presents efficiency issues for computing importance scores in a scalable manner.
To this end, we propose a novel semantic knowledge and Structural Enrichment framework, namely SKETCH, to adapt LMs for TAG tasks by retrieving both structural and text-related content. Specifically, we propose a retrieval model that identifies neighboring nodes exhibiting similarity to the target node across two dimensions: structural similarity and text similarity. To enable efficient retrieval, we introduce a hash-based common neighbor estimation algorithm for structural similarity and a nearest-neighbor recalling algorithm for embedding similarity. These two similarity measures are then aggregated using a weighted rank aggregation mechanism. The text attributes of both the retrieved nodes and the target node provide effective descriptions of the target node and are used as input for the LM predictor. Extensive experiments demonstrate that SKETCH can outperform other baselines on three datasets with fewer resources.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates an interesting problem of leveraging LLM for learning on text-attributed graphs. The authors propose a method called SKETCH which adapts LLM for graphs by retrieving both structural and semantic information. To be specific, the semantic-based retrieval is built upon some off-the-shelf pretrained retrievers, and the similarity score is calculated by the embedding similarity search. On the other hand, the structure-based retrieval is designed to fetch related neighbors from the graph with a novel hash-based Jaccard similarity estimation. The semantic similarity score and structural similarity score are merged to select the final neighbors, which are put into the LLM together with the center node for problem-solving. The authors then conduct experiments on three real-world datasets to demonstrate the effectiveness of their proposed method.

### Strengths
- This paper is very well-written and easy to follow.
- The proposed method of conducting LLM-based learning on graphs without a GNN component is novel and makes sense.
- The proposed hash-based structural similarity calculation is novel to me.

### Weaknesses
 - Some model designs are not well-illustrated. For example, how the sampled neighbors and center text is finally fed into the LLM? What kind of instruction or prompt are you using? Do you train the model or just use do direct prompting?

- Some experiments on larger datasets or other tasks other than node classification can be helpful. The experiments are mainly focused on 10k-size graphs. Can the method be scaled to a large graph with millions of nodes? Node classification might not be enough to demonstrate the strength of the proposed method. It would be interesting to try on some more advanced LLM-based graph reasoning benchmarks [1].

- How many neighbors are finally selected? Is the model performance sensitive to the number of selected neighbors? Is there any scalability issue?

- Typos: (1) “where |S| is the size of the text-attributed nodes” should it be |V|? (2) The equation in line 224 needs one further “=” to be complete.

### Questions
See the weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The author has introduced a new method that combines a pre-trained language model (PLM) with a graph heuristic (Common Neighbor) for semi-supervised node classification. In this approach, the PLM generates semantic proximity by incorporating a weighted sum of token-level embeddings. This semantic information is then fused with local graph structure, such as the common neighbor heuristic, by weighting the local connections according to their semantic proximity.

### Strengths
1. Due to the missing semantic information during the message-passing process, the author has proposed a fused framework based on LM and graph heuristics, which is easily scalable.
2. The author has conducted extensive experiments to demonstrate the performance improvement and computational efficiency.

### Weaknesses
1. When introducing the background of GCN and RAG, some crucial papers are not cited. For instance, the structure of text-attributed graphs encompasses textual information from various nodes. Inspired by concepts from Retrieval-Augmented Generation (RAG) {one in NLP}{one in graph}{one in tag}, we propose integrating an additional corpus during the training process.
   
2. The paper requires additional revision for better and more fluent logical flow. For example, GNNs primarily depend on node-level aggregation via graph convolutions to compute weighted sums of neighboring features. While effective, this method may overlook the rich semantic nuances in textual data. Incorporating such nuances enables a more granular understanding of the relationships between tokens, leading to improved flexibility and adaptability.

3. The method is not well presented. In the section on aggregated learning of retrieved content, a weighted sum of semantic and structural proximity is introduced, but the difference from graph convolution is not carefully studied or justified.

4. Empirical Demonstration: The results are reported without running on 5-10 random seeds or multiple data splits.

5. It is not clear how to calculate semantic proximity and structural proximity for a node classification task.

### Questions
1. Is the method reproducible? Please provide your repository if possible. 
2. Is the GCN-generated embedding also leveraged in the method? Has the author carefully considered the differences between the proposed method and GCN, or should these differences be discussed further?
3. The title is **LARGE LANGUAGE MODELS BASED GRAPH CONVOLUTION FOR TEXT-ATTRIBUTED NETWORKS**. Does this imply that feature aggregation based on a weighting mechanism quantified by semantic and structural proximity is a better way to present it?
4. "While effective, this method may miss the rich semantic nuances in textual data." This is probably a crucial starting point. Are there any references or experiments to support this claim?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces SKETCH, a novel framework for handling text-attributed graphs (TAGs) based on retrieval-augmented generation, enhancing large language models (LLMs) for TAG-related tasks.

### Strengths
1. The retrieval-based approach offers a fresh perspective on handling TAGs.

2. The model leverages hash-based similarity estimation to reduce computational costs in multi-hop similarity estimation.

### Weaknesses
1. Work on graph retrieval-augmented generation, which is closely related to the topic of this paper, is not discussed.

2. Lack of implementation details such as hyparameter searching space, prompts used, etc.

3. Only texts in documents (nodes) are used, and connections (graph structure) between texts are not considered in the generation phase. The authors presents several drawbacks in TAG modeling, such as "the text representations and graph structure are trained independently from their respective aspects, potentially resulting in sub-optimal integration between the two modalities" and "the separate processing stages do not take into account the simultaneous optimization of the two data types, resulting in information loss and reduced robustness". Could the authors clarify how SKETCH addresses these challenges?

4. It is fair to use frozen / fine-tuned LLMs as baseline. However, comparing the proposed model with tailored TAG models that do not utilize external knowledge bases may be unfair. Why not include RAG-based approaches for TAGs?

5. Why SKTECH with Nomic (127M parameters) perform better than SKTECH with Llama3 (8B parameters) on Wikipedia when Nomic has much fewer parameters?

### Questions
1. The foundational work of Retrieval-Augmented Generation (RAG) [1] is not cited. Given that the primary contribution of this paper lies in graph retrieval-augmented generation, it is crucial for the authors to provide a comprehensive discussion of significant prior works [2-4] in related fields.

2. Only texts in documents (nodes) are used, and connections (graph structure) between texts are not considered in the generation phase. The authors presents several drawbacks in TAG modeling, such as "the text representations and graph structure are trained independently from their respective aspects, potentially resulting in sub-optimal integration between the two modalities" and "the separate processing stages do not take into account the simultaneous optimization of the two data types, resulting in information loss and reduced robustness". Could the authors clarify how SKETCH addresses these challenges?

3. The paper lacks implementation details and accessible code. How do authors fine-tune LLMs? What is train / val / test split? What is the searching space for each hyperparameter, e.g., $k$-hop? The reproducibility claims in the article are not convincing. The claim that "the results and related analysis reported in the paper are only a summary of those available in the code" is ambiguous.

4. What is $G$ in $G = R_{sum} + R_{struct}$?

5. It is fair to use frozen / fine-tuned LLMs as baseline. However, comparing the proposed model with tailored TAG models that do not utilize external knowledge bases may be unfair. Why not include RAG-based approaches for TAGs?

6. What is external knowledge data used for each dataset?

7. What are promps used for proposed model (SKTECH)? Are the prompts employed for the LLM baseline the same as those used for SKETCH?

8. Why SKTECH with Nomic (127M parameters) perform better than SKTECH with Llama3 (8B parameters) on Wikipedia when Nomic has much fewer parameters?

---
[1] Lewis, Patrick, et al. "Retrieval-augmented generation for knowledge-intensive nlp tasks." Advances in Neural Information Processing Systems 33 (2020): 9459-9474.

[2] He, Xiaoxin, et al. "G-retriever: Retrieval-augmented generation for textual graph understanding and question answering." arXiv preprint arXiv:2402.07630 (2024).

[3] Hu, Yuntong, et al. "GRAG: Graph Retrieval-Augmented Generation." arXiv preprint arXiv:2405.16506 (2024).

[4] Edge, Darren, et al. "From local to global: A graph rag approach to query-focused summarization." arXiv preprint arXiv:2404.16130 (2024).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed Semantic Knowledge and Structural Enrichment framework (SKETCH) to extract the semantic and structural related information from the graph to help graph understanding and reasoning. The conducted experiments show that SKETCH could enhance the model's performance on three graph datasets.

### Strengths
- The proposed method is well motivated and easy to follow
- SKETCH givens a new perspective to integrate LLMs and the graph task
- The writing and presentation of this paper is clear

### Weaknesses
 - The evaluation is only limited to 3 datasets with less than 10 classes. InstcurtGLM [1] was evaluated on Ogn-arxiv, while GraphFormers [2] was evaluated on Product, DBLP and Wiki.
- The improvement from Llama3-8b+GraphSAGE scenario is marginal.
- SKETCH requires extensive hyper-parameters tuning compared to existing graph based methods (such as Llama3-8b+GraphSAGE).

### Questions
- Could you release the train/test/val splits of the three datasets? I haven't found it in Appendix A.1 and main text.
- Could you provide more explanation on the claim that SKETCH requires fewer computational resources than other baselines?

### Soundness
2

### Presentation
3

### Contribution
2
