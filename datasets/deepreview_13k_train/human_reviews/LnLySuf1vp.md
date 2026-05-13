# A Graph is Worth 1-bit Spikes: When Graph Contrastive Learning Meets Spiking Neural Networks

- Decision: Accept
- Scores: 3, 6, 6, 6

## Abstract
While contrastive self-supervised learning has become the de-facto learning paradigm for graph neural networks, the pursuit of higher task accuracy requires a larger hidden dimensionality to learn informative and discriminative \underline{full-precision} representations, raising concerns about computation, memory footprint, and energy consumption burden (largely overlooked) for real-world applications. This work explores a promising direction for graph contrastive learning (GCL) with spiking neural networks (SNNs), which leverage sparse and binary characteristics to learn more biologically plausible and compact representations. We propose \ours, a novel GCL framework to learn binarized \underline{1-bit} representations for graphs, making balanced trade-offs between efficiency and performance. We provide theoretical guarantees to demonstrate that \ours has comparable expressiveness with its full-precision counterparts. Experimental results demonstrate that, with nearly 32x representation storage compression, \ours is either comparable to or outperforms many fancy state-of-the-art supervised and self-supervised methods across several graph benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a novel graph contrastive learning (GCL) framework called SPIKEGCL, which leverages sparse and binary characteristics to learn more biologically plausible and compact representations. The proposed framework outperforms many state-of-the-art supervised and self-supervised methods across several graph benchmarks, achieving nearly 32x representation storage compression. The paper also provides experimental evaluations and theoretical guarantees to demonstrate the effectiveness and expressiveness of SPIKEGCL.

### Strengths
1.	This paper propose a novel GCL framework called SPIKEGCL that leverages sparse and binary characteristics to learn more biologically plausible and compact representations. 
2.	This paper provides theoretical guarantees to demonstrate the expressiveness of SPIKEGCL.
3.	SpikeGCL nearly 32x representation storage compression and outperforming many state-of-the-art supervised and self-supervised methods across several graph benchmarks. 
4.	Extensive experimental evaluations to demonstrate the effectiveness of the proposed framework.

### Weaknesses
1.	In Section 4.1, to reduce the complexity of SNNs by sampling from each node, the authors uniformly partition the node features into T groups, which is unreasonable. Features of different dimensions may represent different meanings, and operations after grouping these features may lead to inconsistencies in the feature space between different groups. For instance, if a node has features representing both 'age' (in years) and 'income' (in dollars), grouping these into the same feature subset for the SNN input would mix fundamentally different scales and potentially corrupt the learned representation. On the contrary, the traditional mask method retains most features by randomly masking some features, ensuring the consistency of feature distribution. Therefore, in this section, the author can consider using random masks to reduce computational complexity while ensuring the consistency of data distribution.
2.	In table 2, the authors compare the parameter size and energy consumption between proposed method with traditional unsupervised/self-supervised mehtods. Howvere, from table 1, the performance of spikeGCL is worse than the spike-based mehtods in most cases, there’s no evidence that SpikeGCL is better than other mehtods. The authors should add the comparision between SpikeGCL with spike-based mehtods in Table 2.
3.	An intuitive question: Contrastive learning usually generates rich features from multiple perspectives to represent the target. However, spike-based methods usually lose a large amount of data, that is, a large number of learnable features are lost. Why can SpikeGCL still achieve similar results compared with traditional contrastive learning methods?
4.	Generally speaking, combining Spiking and GCL is a good idea, but the novelty is not enougt. Compared with traditional methods, SpikeGCL only groups features and then uses the traditional GCL method for learning, which does not present the special nature of contrastive learning in the scenario where spike and graph are combined.

### Questions
check the comments above

### Soundness
3 good

### Presentation
3 good

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
The paper addresses the challenge of learning full-precision representations in graph neural networks,
which can be computationally and resource-intensive. The authors propose a new approach that
combines graph contrastive learning with spiking neural networks to improve efficiency and accuracy.
The proposed framework, SPIKEGCL, learns binarized 1-bit representations for graphs and provides
theoretical guarantees to demonstrate its comparable expressiveness with full-precision counterparts.

### Strengths
1. The motivation is clear. The paper combines graph contrastive learning with spiking neural
networks to improve efficiency and accuracy.
2. The proposed method is tested on several benchmarks.
3. The paper is well-written and provides a promising direction for graph contrastive learning with
spiking neural networks.

### Weaknesses
1. The author divided the original graph in time in the feature dimension and obtained T graph
structures with the same structure and reduced the node feature dimension to N/T. Compared with
copying T copies, it saves storage resources. However, the author did not explain the reason for
this approach. For example, from my personal understanding, the author's approach can be
understood as for a 1xd feature vector, there is a temporal relationship between the 0th value and
the N/T-th value, which we can’t understand.
2. The author used the SNN method to compress the original representation. One problem is that
SNN considers the accumulation in time and does not take into account the distribution
characteristics in time. What I mean is, if the characteristics of time T-1 and time T-2 are
exchanged. It seems that the value of time T will not be affected, but they will become two
completely different vectors. In this way, will there be a many-to-one situation during the
compression process?
3. I think the article lacks some quantitative analysis, such as what is the connection between the
compressed binary vector and the original vector, what is the distribution of the conventional

### Questions
Please see the weakness section for detailed questions.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents SpikeGCL, a GCL framework built upon SNNs to learn 1-bit binarized graph representations and enable fast inference. The authors shows that Spike GCL achieves high efficiency and reduces memory consumption, and is also theoretically guaranteed with powerful capabilities to learn representations. Extensive experimental results verified that spikeGCL achieves comparable or superior performance to full-precision competitors.

### Strengths
The paper presents a new framework for learning on graph data, the spikeGCL. The paper is well written with clear introduction of the model and the learning algorithm to prevent the vanishing gradient problem, and presents both theoretical guarantees and extensive numerical results to demonstrate the capabilities of the model.

### Weaknesses
The paper focuses on the learning algorithm and performance of SpikeGCL, I think it would be interesting to further explore the properties of the 1-bit node representations themselves and compare them with other baseline models, to better understand why the learned graph representations are superior to other binary GNNs.

### Questions
How much does the result rely on detailed implementation of the SNN (such as reset to 0/reset by subtraction/IF or LIF)?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents SpikeGCL which targets on optimizing GCL with SNN. They provide detail experiments to demonstrate the efficiency of the proposed method.

### Strengths
1.	Connect SNN and GNN is a very important topic, since GNN is closer to the neuron system and SNN is closer to the neuron dynamic.
2.	It is interesting to combine feature dimension and temporal axis.

### Weaknesses
1. The detailed background does not provide in background section, and there are too many existing work descriptions in the method sections.
2. Some design choices do not present.
3. In Sec3, it is not clearly stated whether the problem formulation is specific to this work or general for all GCL applications. The distinction needs to be made explicit.
4. The motivation for using T encoders is not fully justified. While the authors claim a reduction in computational complexity, the explanation is not clear, especially regarding how the feature dimension is partitioned and how this relates to the time step size. The claim that computation complexity does not change when modifying T seems inconsistent with Fig4.
5. Fig3(b) ‘y1->y2’ is unclear. Also, it is not clear how the entire backpropagation works. It's unclear whether all y1…yn can directly receive gradient from the loss. Sec 4.4 introduces too much previous studies, it is better to clarify the gradient diagram in revision, i.e. for different blocks, where the gradient come from.
6. It is not clear how SPIKEGCL reduces parameter size. The authors claim SNNs usually reduce activation size but not parameter size. A diagram explaining parameter size computation is needed.

### Questions
1.	In Sec3, does the problem formulation special for this work, or it is general for all GCL application? Please make it clearly. 
2.	I think author should formulate the GCL problem in background (instead of giving a brief introduction). Also, it is better to highlight which part is optimized by the proposed methods.
3.	Why T encoders? Usually, neurons adopt the same weight among T time-steps, this design may increase the model size. Also, it is not clear how computation complex relates to time step size, since the author claim that they partition the feature dimension into T blocks. In my opinion, the computation complexity would not change when modifying T, which is not consist to Fig4.
4.	Fig3(b) ‘y1->y2’. Also, it is not clear how the entire backpropagation work. whether all y1…yn can directly receive gradient from the loss? Sec 4.4 introduces too much previous studies, it is better to clarify the gradient diagram in revision, i.e. for different blocks, where the gradient come from
5.	How SPIKEGCL can reduce parameter size? Usually, SNN can reduce the activation size but keep parameter size unchanged. Author should provide a diagram of how to compute the parameter size.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
