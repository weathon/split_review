# A Large-scale Training Paradigm for Graph Generative Models

- Decision: Accept
- Scores: 5, 5, 5, 6

## Abstract
Large Generative Models (LGMs) such as GPT, Stable Diffusion, Sora, and Suno are trained on a huge amount of language corpus, images, videos, and audio that are extremely diverse from numerous domains. This large-scale training paradigm on diverse well-curated data enhances the creativity and diversity of the generated content. However, all previous graph-generative models (e.g., GraphRNN, MDVAE, MoFlow, GDSS, and DiGress) have been trained only on one dataset each time, which cannot replicate the revolutionary success achieved by LGMs in other fields. To remedy this crucial gap, we propose a large-scale training paradigm that uses a large corpus of graphs (over 5000 graphs) from 13 domains, leading to the development of large graph generative models (LGGMs). We empirically demonstrate that the pre-trained LGGMs have superior zero-shot generative capability to existing graph generative models. Furthermore, our pre-trained LGGMs can be easily fine-tuned with graphs from target domains and demonstrate even better performance than those directly trained from scratch, behaving as a solid starting point for real-world customization. The generated graphs can boost the training data and lead to better graph classification performance. Inspired by Stable Diffusion, we further equip LGGMs with the Text-to-Graph generation capability, such as describing the network name and domain (i.e., "The power-1138-bus graph represents a network of buses in a power distribution system.") and network statistics (i.e., "The graph has a low average degree, suitable for modeling social media interactions."). This Text-to-Graph capability integrates the extensive world knowledge in the underlying language model, offering users fine-grained control of the generated graphs. We release the code, the model checkpoint, and the datasets at https://github.com/GraphGG/LGGM.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
To mitigate the gap between graph generative models and general generative models (especially for texts / images), the paper propose a new generative training paradigm (LGGMs) for graphs from 13 domains. The pretrained LGGMs achieves better performance than existing graph generative models on the zero-shot tasks. With proper finetuning, the LGGMs can be applied to targeted domains with good performance. Furthermore, the LGGMs can be also used for text-to-graph scenarios by combining a text encoder.

### Strengths
- The proposed LGGM framework can be trained on graphs from 13 different domains, which covers most of the graph scenarios. 
- The framework can be used both on zero-shot generation setting and fine-tuning setting. 
- The paper proposes to utilize the text encoder to enable LGGMs to use the text-to-graph capability.

### Weaknesses
 - The performance of zero-shot scenarios differs in different domains. On some domains such as FB, the LGGM does not work well. 
- The paper emphasizes that the LGGM is trained on over 5000 graphs. The number is not such large for a generative pre-trained model. 
- In the experiment of augmenting graph classification, the performance of LGGM is not promising (especially on the ENZYMES dataset).

### Questions
1. The time and space complexity is quadratic to the number of nodes. How can the method be applied to graphs with large numbers of nodes?
2. The number of used training graphs is over 5000. What if the model (pre-)trains on millions of graphs?
3. In line 866 (Appendix C), the equation number is missing.

### Soundness
3

### Presentation
2

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
This paper proposes a large-scale graph generative model (LGGM). The proposed LGGM is pretrained over 5000 graphs from 13 domains and thereby demonstrates better zero-shot generation on graphs from unseen domains. Extensive experiments showcase the superior performance of the proposed LGGMs compared to baselines (e.g., DiGress) trained on specific domains. The proposed LGGM is equipped with the Text-to-Graph generation capability, which integrates extensive world knowledge in the underlying language model and offers users fine-grained control of the generated graphs. This is the very first one exploring the potential of the large-scale training paradigm on graph-structured data.

### Strengths
- The paper is well-written. Concepts and proposed techniques are clearly explained and clarified.
- The proposed method is the very first one exploring the potential of the large-scale training paradigm on graph-structured data.
- The proposed LGGM shows exceptional zero-shot capability and novel text-to-graph generative ability.
- The experimental results show significant improvement and potential.

### Weaknesses
 - The proposed LGGM builds upon the DiGress architecture, with the primary differences being cross-domain pretraining and text-to-graph features. These aspects are not particularly novel in this field. Additionally, the expectation of enhanced zero-shot generative ability and fine-tuned performance from cross-domain pretraining is not surprising.
- The computational complexity and scalability of the discrete denoising diffusion process raise concerns, particularly when applied to large-scale real-world networks with high-dimensional node and edge categories. A discussion on how these challenges might be addressed would be beneficial. Specifically, the quadratic scaling of the adjacency matrix reconstruction with respect to the number of nodes is a significant concern that needs to be addressed. The paper should also discuss the memory requirements for storing intermediate diffusion steps, especially when dealing with large graphs and high-dimensional node/edge attributes.
- See questions below.

### Questions
- What specific architecture is utilized for the reverse process mentioned in Line 193? More detailed information regarding this architecture should be provided to enhance understanding.
- It remains unclear whether the performance improvements observed over DiGress are primarily due to the cross-domain pretraining or any enhancements in the pretraining architecture. The authors should clarify how each component contributes to the overall performance, ideally through ablation studies or additional experiments.
- The authors mention that the default hyperparameter settings from DiGress are used for implementing LGGM during cross-domain pretraining. How do the authors ensure that these hyperparameters (best for certain domain training) are also optimal for cross-domain pretraining? Is there any empirical evidence or rationale behind their choice?
- As the model scales to accommodate larger graph corpora, is there a scaling law that governs the architecture’s performance? A discussion on how the model's behavior and hyperparameter effectiveness change with the size of the graph data would provide valuable insights.
- The textual descriptions are limited to graph structure and domain type. As the architecture has diffusion modeling on node/edge categories, is it possible to extend to text-to-graph generation conditioned on certain categories, which will be more useful and applicable in real-world scenarios?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a large-scale training paradigm for graph generative models (LGGMs), pre-trained on over 5000 graphs from 13 domains. The work aims to mirror the success of large generative models like GPT and Stable Diffusion in the graph domain, offering both zero-shot generation capabilities and domain-specific fine-tuning. The authors propose a diffusion-based architecture that incorporates text-to-graph generation through language model integration and demonstrates empirical improvements across multiple domains. While the approach shows promise in expanding graph generation to multiple domains, the paper suffers from overclaiming and limited technical innovation in its core methodology.

### Strengths
1. The paper is generally easy to follow and the motivations are clear.
2. The integration of text-to-graph generation capabilities represents a new direction for controlled graph generation.
3. The paper provides an interesting roadmap for scaling up graph generation models with practical applications.

### Weaknesses
1. **Fundamentally Weak Theoretical Foundation**:
   * The theoretical analysis is superficial and merely combines existing results without meaningful insights. While Section 3.3 claims novel expressiveness results, the proofs follow directly from prior work [1,2] and ignore fundamental limitations established in recent literature [3]. Specifically, the expressiveness analysis in Section 3.3 reuses the framework from [1,2] without addressing the known limitations of message-passing GNNs, such as their inability to distinguish certain non-isomorphic graphs, as highlighted in [3]. The paper fails to provide any theoretical justification for why cross-domain pre-training should help, or how the sampling strategy preserves important graph properties. Most importantly, there's no analysis of how the multi-domain training affects model capacity and expressiveness, such as potential negative transfer or interference between different graph domains. There is no discussion of how the model's capacity scales with the number of domains or the diversity of graph structures, which is a crucial consideration for a large-scale pre-training approach.

2. **Limited Technical Innovation and Poor Design Choices**:
   * The core methodology is essentially DiGress [1] with small modifications. The sampling strategy for handling large graphs is ad-hoc and lacks theoretical guarantees, while all four pre-training tasks are directly borrowed from existing work without significant adaptation to graph-specific challenges. For example, the node masking strategy is a direct application of BERT-style pre-training, which may not be optimal for capturing graph-specific structural information. The architecture choices appear arbitrary rather than fundamental, and the text-to-graph component is a straightforward application similar to existing approaches TAPE[4] and GraphGPT[5] without addressing the unique challenges of graph generation. The text-to-graph mechanism is particularly concerning - it simply concatenates LLM embeddings with graph features without addressing the fundamental challenges of aligning textual and structural representations. This naive approach ignores significant prior work on text-attributed graphs, such as [4,5], which have developed sophisticated techniques for text-graph alignment, including methods that explicitly model the relationships between text and graph nodes, or use attention mechanisms to align textual features with relevant graph substructures.

3. **Empirical and Evaluation Limitations**:
   * The experimental evaluation has several critical flaws. The paper primarily compares against a single baseline (DiGress) while ignoring crucial comparisons with recent graph generative model works like GCC [6] and GraphMAE [7]. The evaluation metrics don't adequately capture global structural properties, and there's no analysis of computational efficiency or scaling behavior. Specifically, the evaluation relies on simple graph statistics (degree, clustering coefficient, etc.) which are insufficient to capture complex graph structures. There is no evaluation of the generated graphs' spectral properties, such as eigenvalue distributions, which are important for understanding graph connectivity and robustness. The ablation studies are insufficient to justify architectural choices, and more importantly, I would not really call 5000 graphs a large graph dataset.

### Questions
See weakness

### Soundness
2

### Presentation
3

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
The paper presents a novel approach to large-scale graph generation with the introduction of a Large Graph Generative Model (LGGM). The authors design an innovative training paradigm for graph generative models, training over 5,000 graphs sourced from 13 distinct domains. Remarkably, this work is the first to explore a large-scale training paradigm specifically tailored to graph-structured data generation, marking an exciting achievement for the graph modality. By addressing the complexities of large-scale graph generation, this research expands the capabilities of generative modeling for graph-based data, offering substantial contributions to the field.

### Strengths
1.  The paper addresses a novel problem by extending the scope of large-scale generative models to the graph domain. This exploration into graph generative modeling at scale is a significant contribution, introducing fresh perspectives and potential for advancements in the field.
2. The implementation is both innovative and thorough, covering several essential aspects, including Pre-training Evaluation, Fine-tuning Evaluation, Graph Classification, and Text-to-Graph Generation. These multiple dimensions demonstrate a robust approach.
3. The comprehensive dataset scale strengthens the results, making the findings more generalizable across graph-structured data.

### Weaknesses
1.  The approach relies primarily on existing discrete denoising diffusion techniques, which, while effective, lacks methodological innovation specific to large-scale graph generation. This reliance on existing methods may limit the theoretical foundation and originality of the model within the context of large-scale graph generation. Specifically, the paper does not introduce novel mechanisms for handling the unique challenges of large graph structures, such as computational bottlenecks in diffusion steps or memory limitations when processing very large adjacency matrices. The method essentially applies existing diffusion techniques without addressing the specific scaling issues inherent in graph data.
2. The paper includes a comparison with only a single baseline, which is insufficient to thoroughly evaluate the model’s performance. The lack of comparison with other state-of-the-art graph generation models makes it difficult to ascertain the true efficacy and relative advantages of the proposed approach. A more comprehensive evaluation should include comparisons with a diverse set of baselines, including both traditional and more recent graph generation techniques, to provide a more robust assessment of the model's capabilities.

### Questions
1. Are there any experiments or analyses conducted to evaluate the model's performance in relation to scaling law expectations?

### Soundness
2

### Presentation
3

### Contribution
3
