# Self-supervised Masked Graph Autoencoder via Structure-aware Curriculum

- Decision: Reject
- Scores: 6, 5, 5, 3

## Abstract
Self-supervised learning (SSL) on graph-structured data has attracted considerable attention recently. Masked graph autoencoder, as one promising generative graph SSL approach that aims to recover masked parts of the input graph data, has shown great success on various downstream graph tasks. However, existing masked graph autoencoders fail to consider the degrees of difficulties of recovering the masked edges that often have different impacts on the model performance, resulting in suboptimal node representations. To tackle this challenge, in this paper, we propose a novel curriculum based self-supervised masked graph autoencoder that is able to capture and leverage the underlying degree of difficulties of data dependencies hidden in edges, and design better mask-reconstruction pretext tasks for learning informative node representations. Specifically, we first design a difficulty measurer to identify the underlying structural degree of difficulties of edges during the masking step. Then, we adopt a self-paced scheduler to determine the order of masking edges, which encourages the graph encoder to learn from easy parts to difficult parts. Finally, the masked edges are gradually incorporated into the reconstruction pretext task, leading to high-quality node representations. Experiments on several real-world node classification and link prediction datasets demonstrate the superiority of our proposed method over state-of-the-art graph self-supervised learning baselines. This work is the first study of curriculum strategy for masked graph autoencoders, to the best of our knowledge.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents Cur-MGAE, a new self-supervised approach for graphs that brings curriculum learning into masked graph autoencoders. The method uses a structure-aware design to recover masked edges in an easy-to-hard order, guided by reconstruction errors and a self-paced scheduler. Theoretical analysis shows the optimization converges, and experiments on node classification and link prediction tasks demonstrate Cur-MGAE’s strong performance, showing how well this approach captures meaningful node representations.

### Strengths
1. The paper introduces complexity-guided curriculum masking and self-paced mask scheduling as thoughtful strategies to integrate curriculum learning into graph masked autoencoder. These methods aim to structure the learning process in a way that aligns task difficulty with model capacity, potentially improving performance by enabling the model to handle simpler patterns before moving on to more complex structures in the graph. This structured approach provides a clear framework for applying curriculum learning principles effectively within graph masked autoencoder.
2. The paper does a great job of providing a detailed theoretical analysis of the convergence properties for the alternating optimization algorithm used in Cur-MGAE.

### Weaknesses
1. There are some typos in this paper. In line 359 and 363, the reference for PubMed is missing. Also, I believe the dataset name is misspelling, the “citepseer” should be “CiteSeer”?
2. The selected baselines are bit too old. I suggest the authors select more updated methods as your baselines [1].
3. It would be helpful if the paper discussed Cur-MGAE's computational efficiency a bit more. With the self-paced mask scheduler and iterative edge selection, there might be extra computational overhead. When dealing large graphs, will these factors affect the efficiency of Cur-MGAE?

### Questions
See weakness.

### Soundness
3

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
This paper presents a novel approach to self-supervised learning (SSL) for graph-structured data, specifically through an enhanced masked graph autoencoder. While existing methods have achieved success in recovering masked parts of graph data, they overlook the varying difficulties associated with masking edges, which can lead to suboptimal representations of nodes.
To address this issue, the authors introduce a curriculum-based self-supervised masked graph autoencoder that effectively captures the inherent difficulty levels of edge recovery. The approach involves the following parts:
1. Difficulty Measurer: A mechanism is proposed to assess the structural difficulty of edges during the masking process.

2. Self-Paced Scheduler: This component determines the sequence in which edges are masked, allowing the graph encoder to gradually progress from easier to more difficult tasks.

3. Adaptive Reconstruction Tasks: The masked edges are incrementally included in the reconstruction tasks, which fosters the learning of more informative node representations.

Extensive experiments on various real-world datasets for node classification and link prediction demonstrate that the proposed method outperforms existing state-of-the-art baselines in graph self-supervised learning. This work is notable as it is the first to apply a curriculum learning strategy specifically to masked graph autoencoders.

### Strengths
1. The introduction of a curriculum-based strategy for masked graph autoencoders is a potential solution to the field of self-supervised learning on graph data. This approach is novel and interesting. This idea is innovative and may provide insights to other researchers.

2. By taking into account the different levels of difficulty in masking edges, the proposed method seeks to enhance how node representations are learned. This adds an important improvement to traditional approaches by recognizing that some masked parts are harder to reconstruct than others.

### Weaknesses
1. Scalability Concerns: Depending on how the difficulty measurer and self-paced scheduler are implemented, there may be questions regarding scalability to very large graphs, where edge masking and reconstruction could become computationally intensive.

2. Insufficient baselines: Although the paper experiments with multiple datasets, the chosen GNN baselines are relatively outdated and perform exceptionally well. For instance, the OGBN-Arxiv leaderboard features numerous models, such as GLEM, GIANT, and SimTeg, that have surpassed the baseline. Furthermore, well-established frameworks like GAT are not included in the comparison, which raises questions about the effectiveness of the proposed model and its competitive standing in the current landscape of graph neural networks.

3. Theoretical Foundation: Although the paper introduces a difficulty level for edge masking, there is a lack of robust theoretical justification for how these difficulty levels are defined. This ambiguity raises concerns about the validity of the proposed curriculum approach, as it is not clear why these defined levels are beneficial compared to traditional methods. A stronger theoretical foundation would enhance the contribution of the work and clarify the rationale behind the chosen difficulty metrics.

4. Complexity of Implementation: The introduction of a curriculum-based approach may complicate the model's architecture and the overall training process, which could pose challenges in terms of reproducibility and practical deployment.

### Questions
1. Why did you choose the specific GNN baselines included in your experiments? Were there considerations for including more recent or competitive models, such as GAT or models from the OGBN-Arxiv leaderboard?

2. What theoretical principles support the effectiveness of the curriculum-based approach for masked graph autoencoders?

3. How did you determine the criteria for evaluating the difficulty levels of masking edges? Can you provide more details on the methodology behind this assessment?

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
4

### Summary
To address the issue that existing generative graph self-supervised learning models fails to consider the degrees of difficulties of recovering the masked edges, this paper proposes a curriculum based masked graph autoencoder, Cur-MGAE. Technically, the proposed model equips a difficulty measurer and a self-paced scheduler to modulate the training process of masked graph autoencoders.

### Strengths
1. The paper is well-organized and easy to follow.
2. The motivation of considering the difficulties of pretext tasks is reasonable.
3. The paper provides visualization of curriculum learning process.

### Weaknesses
1. Technically, although the proposed difficulty measurer appears intuitive, there is a gap in using the residual errors of a graph autoencoder (GAE) to measure the confidence of a masked graph autoencoder (MaskGAE), due to the different self-supervised learning principles of GAE and MaskGAE.
2. The literature review in the paper lacks the latest related works, including but not limited to GraphMAE2 [1], AUG-MAE [2], and Bandana [3]. Notably, AUG-MAE also considers the difficulties of pretext tasks and introduces an easy-to-hard training scheduler. This paper needs to discuss these related works.
3. The resulting edge embeddings in Equation 2 appear to be relatively high-dimensional, so it would be better to provide a comparison of the complexity analysis and model size (number of parameters) between the proposed model and baseline models.

### Questions
Please refer to the Weaknesses.

### Soundness
2

### Presentation
3

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
This paper utilizes a masking strategy and an autoencoder structure to model the complexity of edges in order to learn high-quality node representations for downstream tasks.

### Strengths
Consider the complexity of edges to optimize graph structures and learn high-quality node representations.

### Weaknesses
1. Insufficient motivation. Is edge complexity important in practical problems? What issues exist with the current Mask-GAE structure? Why consider edge complexity in Mask-GAE? What specific problems do you aim to address in Mask-GAE?

2. The scientific definition of edge complexity. Edge complexity is the motivation and starting point of this paper, but the definition of edge complexity in the text is not very scientific. Subtracting the initial structure from the learned structure as a measure of edge complexity—what is the basis for this or its physical significance? Is this definition of complexity generalizable? Could a similar definition be applied to node complexity (initial features minus reconstructed features)? What would be the significance of that?

### Questions
Please see Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
