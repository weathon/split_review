# Composing Recurrent Spiking Neural Networks using Locally-Recurrent Motifs and Risk-Mitigating Architectural Optimization

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
In neural circuits, recurrent connectivity plays a crucial role in network function and stability. However, existing recurrent spiking neural networks (RSNNs) are often constructed by random connections without optimization. While RSNNs can produce rich dynamics that are critical for memory formation and learning, systemic architectural optimization of RSNNs is still an open challenge. We aim to enable systematic design of large RSNNs via a new scalable RSNN architecture and automated architectural optimization.  We compose RSNNs based on a layer architecture called Sparsely-Connected Recurrent Motif Layer (SC-ML) that consists of multiple small recurrent motifs wired together by sparse lateral connections. The small size of the motifs and sparse inter-motif connectivity leads to an RSNN architecture scalable to large network sizes. We further propose a method called Hybrid Risk-Mitigating Architectural Search (HRMAS) to systematically optimize the topology of the proposed recurrent motifs and SC-ML layer architecture. HRMAS is an alternating two-step optimization process by which we mitigate the risk of network instability and performance degradation caused by architectural change by introducing a novel biologically-inspired ``self-repairing" mechanism through intrinsic plasticity.  The intrinsic plasticity is introduced to the second step of each HRMAS iteration and acts as unsupervised fast self-adaptation to structural and synaptic weight modifications introduced by the first step during the RSNN architectural ``evolution".  To the best of the authors' knowledge, this is the first work that performs systematic architectural optimization of RSNNs. Using one speech and three neuromorphic datasets, we demonstrate the significant performance improvement brought by the proposed automated architecture optimization over existing manually-designed RSNNs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper developed a new neural architecture search algorithm in the recurrent spiking neural networks search space. Analogous to a cell in the NASNet search space, they defined a sparse connected motif layer (SC-ML). A recurrent spiking neural network is formed by stacking several of these SC-ML layers. The SC-ML layer has N motifs where each motif is comprised of recurrent spiking neurons of a fixed size. The neurons within a motif and between two motifs are connected using excitatory, inhibitory and non-existent connections. Further, in order to reduce the number of recurrent connections, a motif is restricted to be connected to only its neighboring motif rather than any N-1 motifs in the layer. 
    In the search step, the algorithm finds the optimal motif size, the intra-motif and the inter-motif connection types. They designed a supernet which has all possible motif sizes and the intra-motif/inter-motif connection types. For intra-motif connections, a connection matrix similar to an adjacency matrix determines the kind of connection between neuron i and j.  Similar to DARTS, the motif sizes and the connection types are relaxed to form continuous probability predictions. A gradient optimization based bi-level optimization algorithm is used to perform the search, where the architecture parameters and the neural network weights are optimized alternately. In addition to that at every step, SPiKL-IP based intrinsic plasticity is used to adapt the spiking neurons to the changing network weights and the architecture weights. Upon convergence, the discretization step is performed  to obtain the best RSNN architecture. 
     They evaluated the search algorithm on 3 datasets.

### Strengths
1. It is the first paper to perform neural architecture search for recurrent spiking neural networks. Using motifs and having intra-motif and inter-motif connections, the model's connections are no longer unwieldy and is easier to train. 
2. In their ablation studies, they further bolstered their claims by showing that using motifs, intra-motifs connections and IP contribute towards the performance of the model.

### Weaknesses
1. While the architecture found by the model outperforms the other baselines, it comes at a significant a computational cost. Please report the time taken to run the search and the number of parameters of each model.

### Questions
1. Generally in DARTS, the best architecture found in the supernet is retrained from scratch. The accuracy of the retrained architecture is reported. Can the architecture found in your supernet be deployed as is? 
2.  While the intra-motif connections are detailed, the search space of inter-motif connection is not elaborated in 3.2.1. Have I missed it?If not, can you please describe that too? Given that there are no explicit constrains in the search space formulation of the layer connection matrix, how can we enforce sparse inter-motif connections? In DARTS search space, a node i can only be connected with a node j if i < j. One can enforce a similar constraint in this case too.
3. Like you pointed out, the validation loss of the continuous representation is lower than the discretized version. So several works such as RobustDarts (that was cited in your papaer) suggested various regularization techniques to alleviate it. Similar to Robust Darts, can you also empirically show what the validation loss before and after descretization is? How does using SpiKL-IP influence it?
4. Can you also perform random search in your search space? In NAS, generally random search is also used as a baseline to understand the effectiveness of the proposed search algorithm.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper is well-composed and delves into the design and optimization of recurrent spiking neural networks (RSNNs). The authors introduce a scalable architecture called Sparsely Connected Recurrent Motif Layer (SC-ML) that uses small recurrent motifs connected sparsely. To optimize this architecture, they present the Hybrid Risk-Mitigating Architectural Search (HRMAS) method, which incorporates a biologically inspired "self-repairing" mechanism through intrinsic plasticity.

### Strengths
The paper is interesting as the proposed method addresses the design and optimization for the RSNN. Results from the experiments suggest that the RSNN, when integrated with SCML and Spike-IP, not only matches the performance of other SNN models but also upholds a high degree of biological accuracy. The composition of the paper is clear, making it reader-friendly and engaging.

### Weaknesses
- The paper lacks a comparative analysis with contemporary NAS methods for SNNs, such as “Autosnn: Towards energy-efficient spiking neural networks” and “Neural architecture search for spiking neural networks.

- The choice of baselines across different datasets lacks uniformity. The rationale behind using different baselines for each dataset remains unclear.

- The paper omits crucial metrics such as training cost, energy efficiency, latency, and hardware compatibility. While accuracy is discussed, potential strengths of the algorithm in these areas remain unexplored.

- The authors highlight the compactness of motifs and sparse connectivity between motifs as factors that make the RSNN architecture scalable via “The small size of the motifs and sparse inter-motif connectivity leads to an RSNN architecture scalable to large network sizes”. However, the significance of this claim, especially in contrast to existing state-of-the-art methods, is neither elaborated upon nor supported with empirical evidence.

- Weight evolution and architecture evolution for the algorithms are not shown. These are critical as these give crucial insight into the working of the algorithm.

### Questions
- Can the authors provide insights into the evolution of motif topologies during training? Such an evolution could offer valuable insights into the algorithm's adaptability and optimization process.

- There is inconsistency in the choice of baselines across datasets. The comparison of unsupervised learning rules with supervised ones seems inappropriate. As anticipated, unsupervised methods would underperform compared to their supervised counterparts.

-  The authors make claims about the Sparsely-Connected Recurrent Motif Layer (SC-ML) being able to identify sparsely connected motifs. Are there any empirical results that support this assertion?

- The algorithm hasn’t been compared to un-optimized motif networks. Such a comparison seems like a more pertinent baseline than what has been chosen for the paper.

- A comparative evaluation of the proposed method with leading NAS methods for SNNs would enhance the paper's credibility and relevance. Are there plans to include such a comparison in the future?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
To solve the systemic architectural optimization of RSNNs, this paper proposed RSNN models with scalable architecture and automated architectural optimization. The proposed RSNN is composed based on a layer architecture called Sparsely-Connected Recurrent Motif Layer (SC-ML) that consists of multiple small recurrent motifs wired together by sparse lateral connections. They claim that the small size of the motifs and sparse inter-motif connectivity leads to an RSNN architecture scalable to large network sizes. The Hybrid Risk-Mitigating Architectural Search (HRMAS) is designed to systematically
optimize the topology of the proposed recurrent motifs and SC-ML layer architecture. The experiments are conducted on one speech and three neuromorphic datasets, and the results demonstrate the performance improvement brought by the proposed automated architecture optimization over existing manually-designed RSNNs.

### Strengths
The architecture optimization in RSNNs is important. The problem that this paper tries to solved is interesting.

### Weaknesses
* About the presentation

The figure 4 is not clear to show the mechanism of the HRMAS. More explanation can be added.
Also the figure 2 is not clear enough to show the architecture optimization in HRMAS.

* About the performance

Although there is little accuracy improvements brought by the proposed method. But the accuracy increasing is quite limited in these datasets, especially on the N_TIDIGITS and DVS-GESTURE and N_MNIST.

* About the experimental results except the accuracy

Since the architecture optimization proposed in this paper is complex, how about the training speed and computation resources consumption? Only accuracy comparison seems not sufficient for ICLR publication.

### Questions
1. Please refer to the above weakness.
2. If the proposed RSNN model is applied to larger datasets such as DVS-CIFAR10, how about the training speed and computation resources consumption?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a novel bi-level optimization method for architecture search in recurrent spiking neural network models. The authors compose RSNNs using a sparsely connected recurrent Motif Layer (SC-ML), which consists of multiple small recurrent motifs wired together by sparse lateral connections. They also propose a method called Hybrid Risk-Mitigating Architectural Search (HRMAS) to systematically optimize the topology of the proposed recurrent motifs and SC-ML layer architecture.

### Strengths
The notion of a systematic architecture search process for RSNNs is a very interesting research question. 
The authors showed the performance of their method on some standard tasks is comparable or better than current methods, which is good.
The notion of using intrinsic plasticity for an unsupervised self-repairing model was very interesting

### Weaknesses
Though the paper showed promising results, some major issues need to be addressed in the paper:

The major contributions of this paper seem to be just taking the current DARTS-based architecture search method used in DNNs and using it for RSNNs.  I would recommend the authors to highlight their key contributions ( see Questions for details)

The paper introduces two different things, and as such, the experimental section is extremely weak and does not give sufficient evidence of the model performance and how the introduced concepts help in designing a better RSNN model. The absence of more complete ablation studies and specific case scenarios limits the understanding of the necessity and impact of certain methodological choices.

The paper does not delve into the computational complexity and practicality of the proposed methods, especially in terms of time and resources required for simulations and optimizations.

The robustness and stability of the proposed methods, especially in the context of different initializations and model sizes, are not thoroughly validated.

### Questions
A. SPARSELY-CONNECTED RECURRENT MOTIF LAYER (SC-ML)

1. Since the authors use the same topology for all the motifs, it would be good if the authors could elucidate how they chose this topology and what effect it has on the final architecture. I feel this notion of motifs is inspired by the blocks building the cells in the DARTS paper - if so, the DARTS method used a variety of different convolution layers for these blocks. It would be interesting if the authors could highlight why no such heterogeneity would be required in designing RSNNs.

2. The SC-ML architecture seems very similar to the concept of clustered ESNs. Can you give some explanation of how this is similar/different?

B. HYBRID RISK-MITIGATING ARCHITECTURAL SEARCH (HRMAS)

1. The authors introduce the HRMAS as a bi-level optimization where, in the first step, they optimize $\alpha$ and $w$ hierarchically, based on gradient-based optimization. In the second step, they use IP to adapt the parameters of each neuron over a time window. However, that does not match with the problem formulation in Eqs 1-3, where it seems the first-level optimization searches for the architecture, the second-level searches for the optimal  parameters, and the third level optimizes the weights

2. The authors repeatedly mention the “risks” caused by the change in the first level of the bi-level optimization. It would be good if the authors were more specific and showed a more complete ablation study of what happens if they do not use this IP optimization.

3. It seems the gradient-based optimization is simply the DARTS method - it would be good if the authors could highlight the novelty of the architecture search method and how they are optimized for spiking neural networks and the neuronal timescales (as they mentioned in the abstract and introduction) Right now, it seems the architecture search is an off the shelf implementation of the DARTS bi-level optimization problem.

4. Since this is an architecture search process, it would be recommended that the authors also add the following results:
       a. performance comparison with random weights/architecture (this should be the baseline)
       b. the complexity of the algorithm - like how long it took to run these simulations and how the performance changes over the iterations of the optimization problem

5. The authors propose this method can be used to design very large RSNN models. The results in Table 1 show the size is comparable to current RSNN models. It would be interesting if the authors could give more results on what happens if the number of neurons increases.

6. From Figure 6, it seems the final model is a densely connected model compared to many of the current methods. As mentioned before, an important ablation study would be to compare with a randomly generated model (normally these models are much sparsely connected). If there is a significant difference, it would be interesting to know why such dense connections are important for better performance

7. From my personal experiences, such architecture search models are extremely unstable and highly dependent on the initializations. Can you add some details on the initialization you used for your experiments and whether two different initialization models converge to similar or very different models?  It is also important that the authors rerun the experiments a few times (with same/different initializations) and report the mean and variance of the performance in Table 1.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
