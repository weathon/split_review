# Learning Physical Simulation with Message Passing Transformer

- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 6, 5, 5, 6

## Abstract
Machine learning methods for physical simulation have achieved significant success in recent years. We propose a new universal architecture based on Graph Neural Network, the Message Passing Transformer, which incorporates a Message Passing framework, employs an Encoder-Processor-Decoder structure, and applies Graph Fourier Loss as loss function for model optimization. To take advantage of the past message passing state information, we propose Hadamard-Product Attention to update the node attribute in the Processor, Hadamard-Product Attention is a variant of Dot-Product Attention that focuses on more fine-grained semantics and emphasizes on assigning attention weights over each feature dimension rather than each position in the sequence relative to others. We further introduce Graph Fourier Loss (GFL) to balance high-energy and low-energy components. To improve time performance, we precompute the graph's Laplacian eigenvectors before the training process. Our architecture achieves significant accuracy improvements in long-term rollouts for both Lagrangian and Eulerian dynamical systems over current methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes a new hybrid Graph Neural Network based autoregressive Transformer architecture. The authors use an Encoder-Processor-Decoder (EPD) architecture to model physical simulations.
The major contributions of the work include the scaled Hadamard Product Attention (along feature dimensions) and a novel loss function which utilises Graph Fourier Transform.
The authors have shown the effectiveness of the proposed model on both eulerian and lagrangian dynamical systems by achieving superior performance over previous GNN and Transformer based methods.

### Strengths
S1) Novel Graph Fourier Loss which helps learn complex physical phenomena effectively across the energy spectrum of the system. This helps avoid using the Graph Fourier Transform in both training and inference

S2) Modified Attention mechanism focusing on obtaining importance of features as scores by using softmax along the dimension and not along the sequence. This is one of the major contributors to the results as the graph structure helps with message passing/interaction and hence softmax can be applied along the dimension instead of sequence.

S3) Detailed experiments and theoretical/mathematical justification alongwith ablations of all the design choices considered. The combination of HPA and GFL seems to achieve superior performance by learning in both spatial and spectral domains.

### Weaknesses
W1) Comparison between the current method and previous methods in terms of the wall clock time and memory footprint have not been included (The authors have mentioned this as a limitation and also in section F of the appendix). A thorough quantitative analysis of time and memory for each component would be useful for the current and future research as well.

W2) Although the GFL seems very effective, how one arrives at the formulation is not very clear. How does one arrive at the expression of $\alpha$ and and the concept of segment rate as well  in section 4.3 is not straightforward. This makes it unclear of how to build further on this work.

**Presentation/Typos/Corrections**

Section 1 line 47-48
*we replace the commonly used Multi-Layer Perceptron (MLP) with Hadamard-Product Attention.* 
From what I understand in Figure 1, we are still having MLP (FFN) layers right. Should this not be *we replace the commonly used Scaled Dot Product Attention with Hadamard-Product Attention.* instead? 

In Figure 1, I believe it should be *xM* times instead of *xMP* times as MP is not a quantity and refers to Message Passing

Section 2 line 63 *methods have achieved* or *methods achieve* instead of *methods have achieve*

Section 3 line 116-117 For the clarity of notation, can we have a superscript $t$ to denote time along with the currently defined iteration $k$ as a subscript. I feel this will greatly enhance readability (Also make the changes elsewhere)

Section 4.2.1 line 257-259 Is the expression for the gradient computation correct? I believe either a parenthesis is missing or the $\sigma$ should be moved after the first term.

### Questions
Q1) What does MHHA refer to in the figure 1, I believe it is the Scaled Hadamard Product Attention (HPA)?

Q2) Can this model be used effectively with the pretrain and then finetune paradigm (especially on completely different equations/regimes) ? How generalizable is the model across equations, regimes, meshes etc?

Q3) How would this GNN-Transformer modelling of the system behave if we wanted to incorporate physics-informed loss components (Especially as the loss is GFL and not standard MSE)?

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
5

### Summary
The authors introduce the message passing transformer, a graph neural network transformer hybrid introducing two novel components, the Hadamard product attention, and a novel graph Fourier loss, to improve the algorithm's training speed the Laplacian eigenvectors are precomputed. Rollouts of the spatiotemporal dynamics are tested on the datasets of the Meshgraphnet paper, with long-term rollouts being found to be more stable across Eulerian, as well as Lagrangian dynamics.

### Strengths
Where the paper shines is the theoretical background of its approach, the entire model architecture, as well as formulation intricacies are described in detail, and allow for an in-depth look at the architecture, the notable differences to preceding work like the Hadamard-Product attention, and the graph Fourier loss. As far as the reviewer can tell, the architecture should be fully reproducible from this exhibition.

### Weaknesses
Where this paper falls short in its current form is the evaluation, and its embedding into present literature.

Maybe slightly too focussed on PINN literature, it misses two landmark works of the past year:

* The Universal Physics Transformers of Alkin et al., which also have a GNN-core and hence fall squarely into the category of a GNN-Transformer hybrid like the presented architecture
* Poseidon: Efficient Foundation Models for PDEs by Herde et al., which is also built to spatio-temporally evolve physical systems These two works, as well as the datasets they were introduced with are presently not represented in the paper.

It would improve the related work greatly to contrast these approaches to highlight the architectural differences, and if on purpose to make sure that it is clear to the reader why the proposed architecture is not compared to the previous two. Both models are freely available, and could be fine-tuned to the datasets used in this paper. Leading into the evaluation, the reviewer would furthermore question whether the models evaluated against are representative of the current state-of-the-art.

There have been a number of new datasets since MGN, not only the two previously mentioned works, but furthermore other datasets for PDEs/Physical systems which are more challenging than MGN's datasets. I would urge the authors to consider extending their evaluation to these more recent datasets. Concretely, the following datasets could provide a good starting point:
* _PDEBENCH: An Extensive Benchmark for Scientific Machine Learning_ by Takomoto et al.
* _LagrangeBench: A Lagrangian Fluid Mechanics Benchmarking Suite_ by Toshev et al.
* _PINNacle: A Comprehensive Benchmark of Physics-Informed Neural Networks for Solving PDEs_ by Hao et al. includes benchmarks simulated with spectral methods, which should lend itself to the style of the message-passing Transformer.
* _Toward multi-spatiotemporal-scale generalized PDE modeling_ by Gupta et al.

More directly with the two previously mentioned models, I would urge the reviewers to consider extending their evaluations to more related models to allow for a better comparison against contemporary work. Specifically for the problem of long rollouts in the context of machine learning models for particle dynamics, _Neural SPH: Improved Neural Modeling of Lagrangian Fluid Dynamics_ was introduced at ICML'24 by Toshev et al., alongside its datasets, and would lend itself to comparison. It is unclear to the reviewer why the proposed architecture was not compared to this state-of-the-art architecture for longterm rollouts of particle dynamics. Either comparing to this architecture, or

### Questions
Seeing that the entire model is trained, as well as inferred on a single RTX 4090, do you see a way to compare the performance against the other evaluated models across training compute, as well as the cost of inference? As is, it feels like this computational efficiency is not captured properly by the evaluation design. Specific comparisons I think would help to emphasize this point would be 

* Rollout performance on a fixed training budget on aforementioned RTX 4090. If you were to e.g. take only the training budget of the introduced model, and retrain the compared to models with only this budget, how would rollout performance compare?
* At inference time, one could for example evaluate the time to first sample as a comparative metric on the chosen hardware, my intuition woulds be that the optimizations done by you with the precomputation & caching should aid your proposed approach considerably.

### Soundness
3

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
The paper introduces the Message Passing Transformer for physical simulations. MPT employs an Encoder-Processor-Decoder framework and integrates two innovative components: Hadamard-Product Attention and Graph Fourier Loss. Hadamard-Product Attention assigns attention weights at the feature level rather than by sequence position. Graph Fourier Loss is introduced as a spectral loss function that balances high- and low-energy graph components. By precomputing the graph’s Laplacian eigenvectors, GFL maintains computational efficiency, as this precomputation does not impact inference time.

### Strengths
- The proposed Hadamard-Product Attention offers a fine-grained approach to attention by assigning weights to each feature dimension. The experiments show that it brings an improvement over traditional Dot-Product Attention. 
- The application of Graph Fourier Loss to balance spectral components is novel, leveraging graph signal processing to enhance model accuracy over extended rollouts in physical simulations.

### Weaknesses
 - The computational requirements of the proposed method are significantly greater than all the baselines. Moreover, the computational cost for precomputing Laplacian eigenvectors is not discussed, particularly how this scales with graph size and feature dimensionality. The paper should include a detailed analysis of the time and memory complexity of this precomputation step, as it could become a bottleneck for larger graphs.
- From my understanding, the precomputation of Laplacian eigenvectors is not feasible for dynamic graphs that undergo frequent topological changes, such as some of the datasets regarding dynamic flags proposed in the MGN paper. The paper needs to clarify how the proposed method handles dynamic graphs, including the computational overhead of recomputing the Laplacian eigenvectors at each time step or whether it is even applicable in such scenarios.
- The ablation study in Table 2 is only conducted on the CylinderFlow dataset, limiting the generalizability of the conclusions. The ablation study should be extended to other datasets, especially those with different characteristics, to demonstrate the robustness of the proposed method.
- In Figure 3(a), is there something wrong with the label on the graph? It's quite confusing that the figure aims to show the effectiveness of Hadamard-Product Attention while it compares the results of different segment rate. The figure needs to be clarified to accurately reflect the effect of Hadamard-Product Attention.
- In Figure 8, it would be better if the authors could also present the ground truth results for better comparsion. This would allow for a more direct and quantitative assessment of the model's performance.
- Typo: Line 481, "wwe"

### Questions
- What does "weight of the edge" mean in Line 131?
- How is the weighted value matrix $w$ reshaped back to a dimension of d in detail? Is the process implemented with a learned MLP?
- During each step of message passing, are the networks $f_1, f_2, f_3, f_4, f_5$ shared or independent, respectively?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces the Message Passing Transformer for physical simulation. It employs Hadamard-Product Attention for fine-grained feature processing and Graph Fourier Loss for optimization. The model achieves  accuracy gains in long-term simulations of both Lagrangian and Eulerian dynamical systems compared to existing methods.

### Strengths
The use of Hadamard-Product Attention (HPA) and Graph Fourier Loss (GFL) enhance the accuracy and robustness of physical simulations. The results show that MPT has superior performance on four datasets.

### Weaknesses
1. The paper suggests using Graph Fourier Transform for preprocessing by calculating the eigenvectors of the graph Laplacian matrix, assuming a fixed graph topology. However, for Lagrangian systems like deforming plates or flags, the graph topology changes over time based on world positions and relationships. This inconsistency raises questions about the validity of the methods and experiments presented, as the assumption of a constant structure contradicts the dynamic nature of Lagrangian systems.
2. The introduction of HPA significantly increases computational overhead in training and inference. The computation overhead largely depends on the sequence length, there is a lack of comprehensive computation analysis for Sec 4.2.
3. The proposed method should compare more attention-based baselines, such as [1], [2].
4. There are missing annotations in Figure 3a, making it unclear which one is HPA.

### Questions
1. In line 113, it is said the graph topology does not vary over sequence. However, for lagrangian systems like deforming plate and flag simple that construct lagrangian edges based on world positions under certain radius, how do you compute eigenvectors of the graph laplacian matrix. 
2. In more complex scenarios that require mesh refinement, such as the sphere and flag dynamics datasets, the graph topology will also change over time. How can Graph Fourier Loss be applied in these situations?
3. In Sec 4.3, why is the loss calculated on the results after the adjust function rather than directly on the results from the Graph Fourier Transform?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper applies Hadamard-Product Attention and a Graph Fourier Loss within a ‘Message Passing Transformer’ framework to address feature importance in both the spatial and spectral domains. The authors show that this leads to accuracy improvements for modelling dynamical systems.

### Strengths
- The Graph Fourier Loss is a novel loss term for learning dynamic systems (to the best of my knowledge). It is well motivated and discussed in detail throughout the paper and in the appendix. Additionally, it is shown to improve performance on a range of datasets over some baselines. 

- The ablation studies clearly show the performance improvements of incorporating the attention mechanism and GFL, highlighting the benefits of the outlined contributions.

### Weaknesses
 - The main weakness in the paper is the impractical computation runtime of the approach which is substantially slower than the baselines (Table 6). Given that methods such as MGN [2] also focus on achieving substantial computational speed ups, it is not clear from the paper what the practical benefit is in improving the accuracy over such a method whilst being much slower and having larger memory requirements. Additionally, the paper hides some of the training time in a pre-processing step calculating the eigenvalues and eigenvectors. In order to have a fair comparison, the paper should quote this pre-processing time as its a required step for training. 

- Using the Hadamard-Product Attention has already been shown to be beneficial in graph representation learning over dot-product attention (Appendix F of [5]). Additionally, the use of message-passing and a transformer itself is not new. For example, GraphGPS [3] uses both local message-passing and global transformer updates. Graph Attention Networks [4] uses attention to weight local updates. Graph MLP-MIXER [5] uses Hadamard-Product Attention between local patch encodings. The paper needs to be more clear what are its contributions in relation to other Graph Neural Networks (such as those which I have listed and others). It seems the only difference and contribution is the Graph Fourier Loss which can lead to a computational burden in the pre-processing step and suffers from instabilties (see Question 1).

### Questions
-  Small perturbations to the Laplacian could result in completely different eigenspaces [1]. Do you think the introduction then of a Graph Fourier loss (GFL) would lead to difficulties for remeshing or to generalise when the underlying connectivity/mesh differs? 

- There is quite substantial differences between the results of MGN in your work and that quoted in the original paper [2] on the same datasets. Why is this the case? 

- When you do ablations and state your results "without" GFL it is not clear what you mean. Do you mean replacing this loss with an MSE on the velocities?

- You state in the introduction that a common solution to over-smoothing and over-squashing in similar works is to map to a latent space before preprocessing. However, if you map node features to a latent representation and then use a standard GNN which only incorporates local updates then this would not solve over-squashing. How does your method solve this issue? 

- The words "new" and "universal" to describe your architecture are not clear to me. Is your model universal? Additionally, the use of message-passing and a transformer itself is not new (see second point of weaknesses). What is novel about the architecture which you use outside of the loss function?

- Given the above point and the many other methods which use attention and message-passing, the term 'message passing transformer' to describe the method is not clear and confuses other terms and methods used in the Graph Machine Learning literature. Why would you say the term 'message passing transformer' describes your architecture better than what is done with these other approaches? 

- You mention in the paper that HPA and GFL "synergistically" optimize the model’s performance. Why is it the case the the methods in combination are more effective than the sum of their parts? 

- Some recent work [6] has also shown improvements over these baselines on these datasets. Can you say that your model is 'State-of-the-art' without also having newer methods such as this as a baseline? 

[1] Huang et al. ON THE STABILITY OF EXPRESSIVE POSITIONAL ENCODINGS FOR GRAPHS. ICLR 2024.

[2] Pfaff et al. LEARNING MESH-BASED SIMULATION WITH GRAPH NETWORKS. ICLR 2021. 

[3] Rampášek et al. Recipe for a General, Powerful, Scalable Graph Transformer. NeurIPS 2022. 

[4] Veličković et al. Graph Attention Networks. ICLR 2018.

[5] He et al. A GENERALIZATION OF VIT/MLP-MIXER TO GRAPHS. ICML 2023. 

[6] Luo et al. CARE: Modeling Interacting Dynamics Under Temporal Environmental Variation. NeurIPS 2023.

### Soundness
3

### Presentation
2

### Contribution
2
