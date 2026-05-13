# GFSE: A Foundational Model For Graph Structural Encoding

- Decision: Reject
- Scores: 6, 6, 5, 3, 5

## Abstract
Foundation models have recently shown remarkable promise by leveraging extensive pre-training on diverse datasets to acquire generalizable representations, which enable effective transfer to a wide range of downstream tasks. In the graph domain, however, most existing pre-training models are tailored to specific domains, primarily due to the inherent differences in semantic meanings of graph features across various contexts. Additionally, most existing models struggle to capture the rich topological complexity of graph structures, leading to inadequate exploration of the embedding space. To address these challenges, we propose a novel Graph Foundational Structural Encoder (GFSE) that identifies universal structural patterns, facilitating a unified feature embedding space suitable for diverse domains, including molecular structures, social networks, and citation networks. GFSE is the first cross-domain graph structural encoder pre-trained with multiple self-supervised learning objectives. Built on a Graph Transformer, GFSE incorporates attention mechanisms biased by graph structural information, allowing it to encode intricate multi-level and fine-grained topological features within complex graph structures. The pre-trained GFSE produces generic and theoretically expressive positional and structural encoding for graphs, which can be seamlessly integrated with various downstream graph feature encoders, including graph neural networks for graphs with vectorized features and Large Language Models for text-attributed graphs. Comprehensive experiments on synthetic and real-world datasets demonstrate GFSE's capability to significantly enhance the model's performance while requiring substantially less task-specific fine-tuning. 
Notably, GFSE boosts the performance by an average margin of 20.48% across eight real-world datasets, highlighting its potential as a powerful and adaptable foundational encoder for graph-structured data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces GFSE, a Graph Foundational Structural Encoder, designed to capture universal structural patterns in graph data, thus enabling effective cross-domain transfer. GFSE employs a Graph Transformer architecture with a focus on multiple structural pre-training objectives. By leveraging relative positional encoding and attention mechanisms, GFSE encodes complex topological information into a foundational model applicable to diverse domains, such as molecular and social networks. Experimental results reveal that GFSE significantly improves performance on various downstream tasks, including molecular property prediction and community detection.

### Strengths
1. The problem this paper aims to solve—Graph Foundation Model—is a highly relevant and challenging direction that has garnered significant attention.
2. The comparative experiments on SE and PE are extensive, thoroughly demonstrating the powerful capabilities of this work as a pre-trainable Structural Encoder.
3. The validation at the pre-training stage is highly meaningful. Compared to some studies that only evaluate downstream task performance, this pre-training stage validation provides deeper insights.

### Weaknesses
1. Although the title proposes to be ‘foundation model for graph structure encoding,’ the authors seem to aim to establish a connection with graph foundation models. However, the definition of ‘foundation model for graph structure encoding’ in the title remains unclear. GFM is expected to be pre-trainable on a wide range of graph data and applicable across various downstream tasks in different domains. In contrast, the GFSE in this paper is merely a pre-trainable positional encoding (PE) module. The subsequent integration with the downstream feature encoder is directly trained on downstream data, without pre-training on large-scale data or extracting transferable knowledge. Therefore, I find it difficult to consider this approach a GFM. Moreover, the experiments in the paper primarily compare various PE and SE methods. It seems more appropriate to position the scope of the paper as a pre-trained structural encoding model.
2. There are several aspects missing in the experimental validation. First, an important experiment is lacking: namely, an evaluation without pre-training the GFSE, where the full pipeline is applied directly to the downstream task (GFSE trained from scratch). This would allow for comparison with the pre-trained GFSE. The most similar experiment to this setup is in Table 4, but here the backbone models used in the ‘train from scratch’ and ‘fine-tuned’ modes are different, making a direct comparison infeasible. Second, in Table 5, the experiments combining GFSE with LLMs should be compared against existing models that integrate LLMs with graphs, as many of these models employ various methods for this integration (OFA [1] etc.).  Third, the dataset used for pre-training includes multiple collections, but the impact of the number of pre-training datasets on downstream performance is not shown. Additionally, is there a trend that shows better downstream performance as the number of pre-training datasets increases?
3. Many design choices lack motivation. For instance, regarding the selection of pre-training tasks, why were these four tasks chosen? In terms of task categories, the paper includes node-level and edge-level reconstruction tasks, as well as edge-level and graph-level contrastive learning tasks. Why not include graph-level reconstruction tasks or node-level contrastive learning tasks? Furthermore, why was motif counting chosen specifically for the node-level task instead of other reconstruction tasks? For the pre-training backbone, why were $P_M$ and $P_T$ input to the MLP separately rather than concatenated? Additionally, if only graph structure is being input, why rely solely on existing real-world graph data for pre-training rather than using some generated graph structures?
4. There are some details that need polishing. For example, in Figure 1, how should the textual features of B.2 be input to the Graph Foundational Structural Encoder? During the pre-training stage, the Graph Foundational Structural Encoder only receives $P$ and $R$ as inputs, without any text input. So, how are these textual features utilized in downstream tasks? Additionally, in Equation (1), $P$ and $R$ should have dimensions of $N \times (d + 1)$ and $N \times N \times (d + 1)$.

### Questions
See the weaknesses.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces GFSE, a novel model designed to enhance the performance of graph-based machine learning by addressing the limitations of existing graph pre-training models. GFSE leverages a Graph Transformer architecture with biased attention mechanisms, incorporating multiple self-supervised learning objectives to capture complex, multi-level structural patterns universally across domains. This allows it to produce generic, expressive PSE that enhance downstream tasks in various graph domains, including molecular structures, social networks, and citation networks. Importantly, the results discussed in section 4.5 of the paper is particularly promising.

### Strengths
1. GFSE successfully addresses the challenge of domain-specificity in graph pre-training by identifying and encoding universal structural patterns.
2. By focusing on universal graph characteristics, GFSE potentially reduces the need for extensive domain-specific fine-tuning, facilitating easier deployment and adaptation in various applications.
3. The paper presents comprehensive experimental results.

### Weaknesses
1. While the paper introduces GFSE as an innovative architecture, it primarily appears to be a composite of existing methods such as GraphGPS, GRIT’s RRWP, and Attention Bias. The real novelty claimed, addressing domain-specificity in graph pre-training, is not compellingly validated by the experiments.

2. The downstream evaluation in section 4.4 does not include comparisons with SOTA models. The results presented do not meet the results of current SOTA models. 

3. The experiments in section 4.3 lack detailed descriptions of hyperparameter tuning, which undermines the credibility of the results. 

4. There is a noticeable lack of ablation studies comparing GFSE with GRIT’s RRWP, which could provide critical insights into the unique contributions and improvements made by GFSE’s specific features.

5. Missing related work such as [1] on shortest-path distance PSE and [2,3] on graph contrastive learning.

### Questions
Does the dataset used in the experiments of section 4.6 overlap with those appearing in InstructGLM? It is recommended that the authors include the original datasets from InstructGLM.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
To facilitate pre-trained graph models across diverse domains, this paper proposes a cross-domain graph structural encoder, GFSE. This encoder is built on a graph transformer architecture and is pre-trained on multiple domains with multiple self-supervised learning objectives. After pre-training, the encoder is evaluated on two types of downstream graphs, i.e., vectorized-feature graphs and text-attributed graphs.


Thank you for providing a detailed rebuttal. After reviewing your responses and the revised manuscript, my concerns regarding the technical novelty remain unresolved. Additionally, the revised paper still does not include comparisons with state-of-the-art baseline models.
As such, I have decided to maintain my original score.

### Strengths
1. The paper is well-organized and easy to follow.
2. The proposed method is technically sound, which introduces multiple self-supervised learning objectives to pre-train a generalizable structural encoder.
3. The paper provides a complexity analysis and compares the runtime with some existing structural encodings.

### Weaknesses
1. The proposed model is not very novel, as most components have been introduced in prior graph transformer models.
2. There is a lack of detailed descriptions of the method. For example, when encoding graphs from different domains using the same encoder, how are the graphs featurized to ensure they can be encoded by the same encoder? Specifically, what preprocessing steps are taken to ensure that the structural information from different graph types (e.g., molecular graphs, social networks, citation networks) is compatible as input to the graph transformer? The paper only mentions random walk encoding, but it is unclear how this is applied across diverse graph structures with varying node and edge attributes.
3. The baselines used for comparison are not up-to-date. Since GPS, newer graph transformer models have been proposed, and these should also be included in the comparison. For example, models like Nodeformer and GRIT, which have demonstrated superior performance on various graph benchmarks, should be included to provide a more comprehensive evaluation of the proposed method's effectiveness.
4. The paper only conducts ablation study on different pre-training sub-objectives. It is recommended to also perform ablation study on different pre-training domains or datasets, as this could reveal which domains contribute to learning cross-domain general patterns. It is important to understand how the choice of pre-training datasets affects the model's ability to generalize to unseen graph structures, and which domains might be more crucial for learning universal structural representations.

### Questions
Please refer to the Weaknesses.

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
This paper proposes GFSE (Graph Foundational Structural Encoder), a graph transformer model pre-trained on diverse graph datasets using multiple self-supervised tasks to generate positional and structural encodings (PSE). This model aims to serve as a universal structural encoder that can enhance various downstream graph learning tasks and models. The key contributions include: (1) a multi-task pre-training framework with four structural tasks, (2) some theoretical analysis of the model's expressiveness, and (3) some empirical validations across different graph domains and model architectures.

### Strengths
1. This paper is generally easy to follow and well-structured.
2. The multi-task pre-training approach combining different structural aspects is interesting.
3. The empirical performance shows some gain.

### Weaknesses
1. **Overclaiming and Overstated Results**:
   - The claim of being "the first cross-domain graph structural encoder" ignores relevant prior work:
     * GCC [1] already proposed cross-domain pre-training
     * GraphMAE [2] and other self-supervised approaches [3,4] have demonstrated cross-domain capabilities
   - The "20.48% average improvement" appears selectively calculated:
     * Tables 2-3 show many improvements <1% (e.g., MNIST: 0.31%, PubMed: 0.38%)
     * Best results seem cherry-picked from different model combinations

2. **Limited Technical Novelty**:
   - The core architecture is largely borrowed from GPS [5] with minimal modifications:
     * The biased attention mechanism is a straightforward extension of existing work [6]
     * The pre-training tasks are mostly adapted from prior graph learning literature [7,8]
   - The multi-task learning setup uses standard techniques:
     * Uncertainty-based loss weighting is directly from [9]
     * Community detection approach follows [10]
     * Motif counting implementation is based on [11]

3. **Methodological Limitations**:
   - Pre-training effectiveness:
     * No comparison with recent advances in cross-domain graph pre-training [12,13]
     * Missing analysis of task interactions shown to be crucial in [14]
   - Theoretical guarantees:
     * The expressiveness analysis follows similar arguments to [15]
     * The proofs rely on assumptions challenged in recent work [16]

### Questions
See weakness

### Soundness
2

### Presentation
3

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
The authors propose a universal graph position encoding method, GFSE, designed for graphs from different domains. The method utilizes a graph transformer as its backbone and is pretrained with four self-supervised learning tasks—such as shortest path prediction, motif counting, and contrastive learning—to capture structural knowledge. Experimental results demonstrate the method’s effectiveness across diverse tasks and domains.

### Strengths
1. The paper is well-written and easy to follow.

2. The proposed method is supported by a solid theoretical foundation, demonstrating its effectiveness.

3. The method is versatile and can be applied to various tasks, including basic graph reasoning, classification-related tasks, and LLM-based inference.

### Weaknesses
1. The contribution of the proposed approach is unclear, as it does not appear to be a graph foundation model applicable for inference across various graphs. Instead, it may be more accurately described as a universal graph positional encoding method.

2. The motivation for adopting a universal positional embedding is unclear. Couldn’t we simply train a positional encoder for each dataset individually? Additionally, the paper lacks evidence that the model pretrained on one dataset (e.g., Dataset A) can be successfully transferred to another dataset (e.g., Dataset B) with strong performance.

3. While the authors present experimental results on graph and node classification, it would be interesting to see if this method significantly improves performance on link prediction tasks and on heterophilic graphs, where capturing structural insights is especially important.

### Questions
1. The motivation behind GFSE appears somewhat similar to UniAug [1], both aiming to identify universal structural patterns. Could the authors elaborate on the differences between these approaches?

2. The authors have not provided an official codebase, which may limit the practical usability of the method. Do the authors plan to release the code?

3. Can the proposed method be applied effectively in scenarios with limited label availability?

Reference: 

[1] Cross-Domain Graph Data Scaling: A Showcase with Diffusion Models, 2024.

### Soundness
2

### Presentation
3

### Contribution
2
