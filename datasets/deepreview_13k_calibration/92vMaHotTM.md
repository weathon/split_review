# Edge Prompt Tuning for Graph Neural Networks

- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
In recent years, prompt tuning has sparked a research surge in adapting pre-trained models.
Unlike the unified pre-training strategy employed in the language field, the graph field exhibits diverse pre-training strategies, posing challenges in designing appropriate prompt-based tuning methods for graph neural networks. 
While some pioneering work has devised specialized prompting functions for models that employ edge prediction as their pre-training tasks, these methods are limited to specific pre-trained GNN models and lack broader applicability.
In this paper, we introduce a universal prompt-based tuning method called \textit{Graph Prompt Feature (GPF)} for pre-trained GNN models under any pre-training strategy.
GPF operates on the input graph's feature space and can theoretically achieve an equivalent effect to any form of prompting function.
Consequently, we no longer need to illustrate the prompting function corresponding to each pre-training strategy explicitly.  
Instead, we employ GPF to obtain the prompted graph for the downstream task in an adaptive manner. 
We provide rigorous derivations to demonstrate the universality of GPF and make guarantee of its effectiveness.
The experimental results under various pre-training strategies indicate that our method performs better than fine-tuning, with an average improvement of about $1.4\%$ in full-shot scenarios and about $3.2\%$ in few-shot scenarios.
Moreover, our method significantly outperforms existing specialized prompt-based tuning methods when applied to models utilizing the pre-training strategy they specialize in.
These numerous advantages position our method as a compelling alternative to fine-tuning for downstream adaptations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Recent graph prompt tuning methods have proven effective in adapting pre-trained GNNs to downstream tasks. However, they often overlook the crucial role of edges in graph prompt design. To address this research gap, this submission introduces a new graph prompt tuning method focused on edges, called EdgePrompt. Nevertheless, despite emphasizing the importance of edges in graphs, the authors make an overly strong assumption by considering only a single type of edge. Additionally, the paper does not address edge-related tasks, which significantly undermines the overall contribution and impact of the work.

### Strengths
S1. Clear motivation and presentation.

S2. The proposed method can be integrated with existing pre-trained GNNs.

### Weaknesses
W1. The unclear statements regarding the edge-level aspect weaken the paper’s contributions.

W2. The authors need to further elaborate on the technical contributions.

W3. More experiments are needed to better support the superiority of the proposed method.

**Concerns**

C1. As a study focused on edge-level prompt tuning, the assumption that there is only one type of edge could significantly undermine the contributions and claims of this paper. In line 154, the modeling of the adjacency matrix, $\mathbf{A} \in \{0,1\}^{N \times N}$, implies that the paper does not target multi-relational graphs. However, compared to other node-level graph prompting systems, the proposed edge-level graph prompting method could be more suitable for graphs with multiple edge types. The authors may need to clarify this in the submission.

C2. Since this work emphasizes edge-level prompt tuning, it would be beneficial for the authors to explore edge-related tasks, such as edge classification and link prediction, to further expand the scope of the paper.

C2-1. In many real-world scenarios, studying edge-level tasks is highly relevant because the space of edge types can evolve over time. For example, in a social network, a newly introduced user interaction feature might require predicting new edge types using a trained GNN.

C2-2. If the research on edge-level tasks is beyond the scope of current pre-trained GNNs (i.e., no existing pre-trained GNNs focus on edge-level tasks), the authors should clarify this limitation in the submission.

C3. The core Equation (4) in EdgePrompt+ appears overly similar to existing work, which may diminish the paper’s technical contribution. In CompGCN [1], the operation of weighting relation embeddings based on relation base embeddings has already been shown to be simple and parameter-efficient. Therefore, the authors should elaborate on the unique technical contributions of their method.

Minor Concerns:

C4. More classic and promising pre-trained GNNs, such as Infomax, EdgePred, AttrMasking, MGSSL, GraphMAE, and Mole-BERT, could be included in the experimental section. At the very least, the authors should discuss these models and explain why they are excluded from comparison.

C5. Figure 2 presents convergence speeds in terms of the number of epochs. The authors should also analyze the efficiency of the proposed method using learning curves or running time comparisons.

### Questions
Please focus on answering concerns C1-C3.

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
This paper introduces EdgePrompt, a new graph prompt tuning method that improves graph representation for downstream tasks by learning edge-specific prompts, enhancing the performance of pre-trained GNNs. Extensive experiments show EdgePrompt’s effectiveness across various datasets and pre-training strategies, outperforming several baseline methods.

### Strengths
1. EdgePrompt improves the adaptation of pre-trained GNN models for downstream tasks by introducing edge-level prompts, which helps bridge the objective gap between pre-training and downstream tasks..
2. Extensive experiments on multiple datasets and pre-training strategies demonstrate the method’s effectiveness, showing better performance compared to existing graph prompt tuning approaches.

### Weaknesses
1. EdgePrompt uses shared prompt vectors, which may not capture the different relationships between edges well. This can limit the model’s ability to use all the information in the graph.
2. EdgePrompt+ adds multiple anchor prompts and score calculations, which can make the model more complex. This can lead to higher computational costs, making it harder to use in larger graphs.
3. The method struggles with few-shot learning because most edges lack supervision. This can reduce the model’s performance in real-world tasks where labeled data is limited.

### Questions
How can the performance of EdgePrompt be improved in scenarios with limited labeled data to enhance its effectiveness in node classification tasks?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes EdgePrompt, a graph prompt tuning method that enhances GNNs by learning prompt vectors for edges, improving graph representations. EdgePrompt integrates these edge prompts through message passing, outperforming existing methods across ten datasets under four pre-training strategies.

### Strengths
1. The paper is well-motivated. It's important to integrate structural knowledge in prompt learning.
2. The authors conducted extensive experiments, demonstrating the effectiveness of the proposed methods.
3. The authors provide theoretical analysis, further proving the effectiveness of the proposed methods.
4. The paper is well written and easy to follow.

### Weaknesses
1. **Inaccurate statement**: GraphPrompt [1] is not based on a specific pre-training strategy. As shown in GraphPrompt+ [2], all contrastive learning pre-training methods can be unified as subgraph similarity calculations. The link prediction used in [1] can be replaced by other methods.
2. **Missing related work**: GraphPrompt+ [2] also adds prompt vectors to each layer of the pre-trained graph encoder, which should be discussed and compared. The current discussion lacks a detailed comparison of how EdgePrompt's approach to prompt integration differs from the layer-wise prompt addition in GraphPrompt+.
3. **Unclear explanation of anchor prompts in EdgePrompt+**: It is unclear what the anchor prompts in EdgePrompt+ represent. In my opinion, anchor prompts are introduced to address the overfitting problem caused by directly learning edge-specific prompts for different edges, but there lacks a clear explanation for the meaning of the anchor prompts and how they are initialized. A more reasonable and effective solution could be conditional prompting [3,4], which I highly recommend the authors explore in future work. Specifically, the paper should clarify how the anchor prompts are distinct from learnable parameters within the GNN itself and how their initialization affects the final performance.

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents EdgePrompt, a method that enhances pre-trained GNNs for downstream tasks by using learnable prompt vectors on edges. EdgePrompt+ further customizes these vectors for individual edges. This approach improves graph structural representation and is compatible with various GNN architectures. Experiments on multiple datasets show its effectiveness over existing methods for node and graph classification tasks.

### Strengths
1. The paper is well-organized, with clear points, and is easy to follow.
2. The effectiveness of EdgePrompt is theoretically guaranteed, and it performs excellently in downstream tasks.

### Weaknesses
1. The motivation for constructing EdgePrompt is insufficient. Why is it necessary to design EdgePrompt under graph prompt tuning? What core problem does EdgePrompt address compared to existing graph prompt tuning methods? What are its advantages?
2. Compared to ALL-in-one and GPF, EdgePrompt and EdgePrompt+ set different prompt vectors $p^{(l)}$ for each layer. What are the benefits of this design? Both All-in-one and GPF only add prompt vectors in the first layer to reduce dependency on the specific structure of the model. EdgePrompt lacks such advantages, and the paper does not explore the reasoning behind this design. Furthermore, the experimental section does not include relevant comparisons to demonstrate the necessity of setting different prompt vectors for each layer.
3. The datasets included in the experimental section do not contain initial edge features, which raises doubts about the effectiveness of EdgePrompt on graphs that inherently have edge features. If the original graph already contains edge features, how should EdgePrompt be integrated with these edge features? What would its performance be like in that case?
4. The downstream tasks involved in the experiments are limited to node classification and graph classification, with other graph tasks such as link prediction and node regression not being included.

### Questions
Please refer to the points I mentioned in the weakness part.

### Soundness
2

### Presentation
3

### Contribution
2
