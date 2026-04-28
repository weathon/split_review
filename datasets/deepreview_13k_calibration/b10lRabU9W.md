# DeepGate4: Efficient and Effective Representation Learning for Circuit Design at Scale

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 6, 5

## Abstract
Circuit representation learning has become pivotal in electronic design automation, enabling critical tasks such as testability analysis, logic reasoning, power estimation, and SAT solving. However, existing models face significant challenges in scaling to large circuits due to limitations like over-squashing in graph neural networks and the quadratic complexity of transformer-based models. To address these issues, we introduce \textbf{DeepGate4}, a scalable and efficient graph transformer specifically designed for large-scale circuits. DeepGate4 incorporates several key innovations: (1) an update strategy tailored for circuit graphs, which reduce memory complexity to sub-linear and is adaptable to any graph transformer; (2) a GAT-based sparse transformer with global and local structural encodings for AIGs; and (3) an inference acceleration CUDA kernel that fully exploit the unique sparsity patterns of AIGs. Our extensive experiments on the ITC99 and EPFL benchmarks show that DeepGate4 significantly surpasses state-of-the-art methods, achieving 15.5\% and 31.1\% performance improvements over the next-best models. Furthermore, the Fused-DeepGate4 variant reduces runtime by 35.1\% and memory usage by 46.8\%, making it highly efficient for large-scale circuit analysis. These results demonstrate the potential of DeepGate4 to handle complex EDA tasks while offering superior scalability and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work aims to address the challenges in scaling to large circuits due to limitations like over-squashing in graph neural networks and the quadratic complexity of transformer-based models by introducing DeepGate4, a scalable and efficient graph transformer specifically designed for large-scale circuits. DeepGate4 has following contributions: (1) design a partitioning method and update strategy tailored for circuit graphs, reducing memory complexity to sub-linear levels; (2) propose a GAT based sparse transformer optimized for inference by leveraging the sparse nature of circuits; (3) propose with a loss balancer that dynamically adjusts the weights of multitask losses to stabilize training.

### Strengths
1. The experimental evaluation is comprehensive and compelling, showing significant performance improvements over state-of-the-art baselines. The empirical results strongly validate the effectiveness of the proposed approach, with substantial gains across multiple metrics and circuit scales.
2. The technical contribution is substantial. The work demonstrates innovation in addressing fundamental scalability challenges in circuit analysis through:
  a. A novel graph partitioning strategy
  b. An efficient sparse transformer architecture
  c. An adaptive loss balancing mechanism
3. The paper presents a thorough and well-structured literature review. It effectively traces the evolution of GNN applications in EDA while critically analyzing the limitations of current transformer-based approaches in GNN architectures. This comprehensive background provides a clear motivation for the proposed methodologies and firmly establishes their theoretical foundations.

### Weaknesses
1. The results of the experiment can be represented more visually in graphs. It will be better if the authors could explain in detail the parameter settings in the ablation experiment. For example, why was the parameter k set to 8?
2. It is mentioned that the loss balancer is very effective in reducing the loss, can the authors expand more on this or give a theoretical analysis? And it will be better if the authors could analyze why the loss balancer must be introduced in the last layer.
3、The description in section 3.3 is not very clear. It will be better if the authors could elaborate on the role of receptive fields and the specific way and basis for defining them in inter-class and intra-class.
4、How does the setting of k and d have effects on computing the receptive fields and subsequent calculations for the cones?
5、The figures need to be further explained clearly. For example, what are the meanings of the red arrows and the black arrows in Figure 2?

### Questions
Please see weakness

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a scalable and efficient graph transformer specifically designed for large-scale circuits, namely DeepGate4. DeepGate4 consists of several key components: (1) a partition method and update strategy tailored for circuit graphs; (2) a GAT-based sparse transformer optimized for inference by leveraging the sparse nature of circuits; (3) global and local structural encodings for circuits, along with a loss balancer. Experimental results show that DeepGate4 significantly outperforms previous state-of-the-art (SOTA) method.

### Strengths
This paper addresses a fundamental problem in machine learning for electronic design automation. The proposed DeepGate4 consists of several interesting and effective modules to improve the scalability of the method. Experimental results demonstrate a significant improvement.

### Weaknesses
The novelty of the proposed graph partitioning method and the loss balancer is limited. The graph partition mechanism is a commonly-used technique for handling large-scale industrial circuits. Moreover, the dynamic loss balancer has been widely investigated in computer vision [1].

The OpenABC-D benchmark is widely-used in previous work. Can the authors evaluate their method on this benchmark as well. A recent SOTA method called HOGA [2] also addresses the challenge of scaling to large-scale circuits. Can the authors compare their method with HOGA.

### Questions
1. Can the authors explain the metrics used in Table 1?
2. Can the authors clarify whether they evaluate their method on unseen testing datasets or training datasets?
3. Can the proposed method be applied to sequential circuit representation learning?

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
This paper introduces DeepGate4, a graph transformer specifically designed for large-scale circuits. Specifically, DeepGate4 proposes a partitioning method and update strategy tailored for circuit graphs, a GATbased sparse transformer optimized for inference, and global and local structural encodings for circuits. Experiments demonstrate the effectiveness of DeepGate4.

### Strengths
1.	Circuit representation learning is an interesting and important research topic.
2.	Experiments demonstrate the proposed method significantly outperforms baselines.

### Weaknesses
1.	The writing could be improved. (1) It would be more readable if the authors could provide a summary of contributions. (2) The method description is unclear. For example, the graph partition module and the multi-task training objective is unclear.  
2.	The novelty of the proposed method is unclear. The authors incorporates many modules into previous circuit representation learning method. However, the novelty and contribution of these modules seems limited. 
3.	Experiments are insufficient. (1) The experiments do not compare their method with a recent SOTA method HOGA [1] that is able to scale to large-scale circuits. (2) The evaluation metrics are unclear. The experiments report many metrics, such as $L_{gate}^{prob}$ and $L_{gate}^{con}$. However, a description of these metrics is missing. (3) The experiments do not apply the representation method to downstream tasks, especially real-world industrial tasks. (4) The sensitivity analysis of hyperparameters is missing. Do the authors use the same hyperparameters across all experiments? It would be more convincing if the authors could conduct sensitivity analysis on the hyperparameters $k$ and $\delta$.

### Questions
Please see weaknesses for my questions.

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
The paper presents a novel graph transformer model, DeepGate4, to address the challenges of scalability and efficiency in circuit representation learning, particularly for large-scale circuits used in electronic design automation (EDA) tasks. Previous methods, such as graph neural networks (GNNs) based and transformer-based models, face over-squashing and large memory overhead challenges. DeepGate4 introduces several innovations, including a partitioning method, a GAT-based sparse transformer, and structural encodings, to handle these issues. Experimental results show that DeepGate4 significantly outperforms previous methods.

### Strengths
- The proposed method in this paper can reduce GPU memory usage while ensuring the convergence of the model.

### Weaknesses
 - This paper proposes a method for representation learning but does not provide any experimental validation on specific EDA downstream tasks. Metrics such as the depth of gates provided by the paper are merely custom metrics for representation learning. We hope these methods can be used in practical EDA applications; unfortunately, this paper does not elaborate on how much benefit such methods could bring to actual EDA tasks.
- The novelty of this paper is limited. Previously, Deepgate3$^{[1]}$ also proposed a partitioning strategy for large-scale circuits, which weakens the contribution of the partitioning method. 
- Data is very important for deep learning. This paper uses two old datasets, but the data are insufficient for such a large-scale model, and the results provided are not solid enough. 

### Questions
- What's the difference between the two partitioning strategies used in Deepgate3 and Deepgate4. It would be better to discuss more about this.
- Conducting the experiments on modern, larger-scale datasets/netlists(e.g., [1], [2]) would significantly enhance the value of the paper.

[1] Chai, Zhuomin, et al. "Circuitnet: An open-source dataset for machine learning in vlsi cad applications with improved domain-specific evaluation metric and learning strategies." IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems 42.12 (2023): 5034-5047.

[2] https://github.com/TILOS-AI-Institute/MacroPlacement

### Soundness
3

### Presentation
3

### Contribution
3
