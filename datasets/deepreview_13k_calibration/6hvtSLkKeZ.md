# Learning to solve Class-Constrained Bin Packing Problems via Encoder-Decoder Model

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 8, 6, 6

## Abstract
Neural methods have shown significant merit in solving combinatorial optimization (CO) problems, including the Bin Packing Problem (BPP). However, most existing ML-based approaches focus on geometric BPP like 3DBPP, neglecting complex vector BPP. In this study, we introduce a vector BPP variant called Class-Constrained Bin Packing Problem (CCBPP), dealing with items of both classes and sizes, and the objective is to pack the items in the least amount of bins respecting the bin capacity and the number of different classes that it can hold. To enhance the efficiency and practicality of solving CCBPP, we propose a learning-based Encoder-Decoder Model. The Encoder employs a Graph Convolution Network (GCN) to generate a heat-map, representing probabilities of different items packing together. The  Decoder decodes and fine-tunes the solution through Cluster Decode and Active Search methods, thereby producing high-quality solutions for CCBPP instances. Extensive experiments demonstrate that our proposed method consistently yields high-quality solutions for various kinds of CCBPP with a very small gap from the optimal. Moreover, our Encoder-Decoder Model also shows promising performance on one practical application of CCBPP, the *Manufacturing Order Consolidation Problem* (OCP).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Authors propose a new learning-based solver for Class-Contrained Bin Packing Problem (CCBPP). CCBPP is commonly applied to planning optimization problems. As a good solution requires clustering of items in the same class, existing sequential learning-based algorithms struggle. Authors propose a GNN-based model, which is pre-trained on synthetic data with ground truths. The model is further fine-tuned with policy gradient. In order to account for the fact that good solutions should cluster items in the same class, a decoding algorithm that prioritizes items clustered to existing open bin is proposed. Experimental results demonstrate that the proposed algorithm outperforms reasonable heuristics, typical population-based algorithms, and standard Pointer Networks.

### Strengths
Originality, Significance: While many of the learning-based combinatorial optimization methods employ sequential models, CCBPP is a problem sequential models may not be best suited. Authors demonstrate that indeed the proposed method, which accounts for the clustering of items in the heatmap, outperforms previous sequential methods. This is an original contribution that will help the research community to think differently. As the use of GNNs & heatmaps are common in other methods, innovations in this paper, such as cluster decoding would also easily transfer to other problems in the future work. 

Quality: Authors follow best practices in the literature. First, they use GNN to model the interaction between variables, which has become standard in neural combinatorial optimization algorithms. Then, they use heatmap for decoding, which is becoming standard for TSP and related problems. The choice of supervised pre-training is also very well-suited, because difficult problems with known ground-truth shall be easily generated. The proposed method also makes a good improvement over Pointer Network baseline. Experiments cover both synthetic and real-world data.

Clarity: The main ideas of the paper is mostly straightforward to follow, although I had some questions.

### Weaknesses
While the paper makes some methodological contributions such as GNN modeling of the problem and cluster-aware decoding algorithms, the significance of these proposed methods are contingent on the significance of CCBPP problem. As I am not an expert on bin packing and related problems, it is difficult for me to evaluate the significance of CCBPP. Also, other attendees of this conference may feel similarly. When authors present the paper, attendees wouldn't be interested in the talk unless they are convinced of the usefulness of CCBPP. While authors discuss CCBPP applications in Section 3, I would encourage authors to elaborate more on their significance in order to convince this conference's audience.

In equation (8), wouldn't it numerically more tractable to optimize the log probability $\sum_{i,j} \hat{p}_{i,j}  \cdot \log p_{i,j}$, rather than sum of probabilities as in (8)? I understand this has nice interpretation as modularity, but often, probabilities are harder to optimize with gradient descent than log-probabilities, because sigmoid has near zero gradient for most of its domain.

I was also not sure how Policy Gradient shall be applied on ClusterDecode. Authors say $p_\theta$ in Policy Gradient equation (Section 4.3.2) correspond to Cluster Decode, but according to Appendix C, Cluster Decode is mostly deterministic algorithm (other than the choice of the first item). Hence, conditioned on the choice of the first item, the probability will be 1 for chosen item at the state, and 0 for not chosen items.

### Questions
In equation (8), wouldn't it numerically more tractable to optimize the log probability $\sum_{i,j} \hat{p}_{i,j}  \cdot \log p_{i,j}$, rather than sum of probabilities as in (8)? I understand this has nice interpretation as modularity, but often, probabilities are harder to optimize with gradient descent than log-probabilities, because sigmoid has near zero gradient for most of its domain.

I was also not sure how Policy Gradient shall be applied on ClusterDecode. Authors say $p_\theta$ in Policy Gradient equation (Section 4.3.2) correspond to Cluster Decode, but according to Appendix C, Cluster Decode is mostly deterministic algorithm (other than the choice of the first item). Hence, conditioned on the choice of the first item, the probability will be 1 for chosen item at the state, and 0 for not chosen items.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the Class Constrained Bin Packing Problem (CCBPP), which is a typical example of the vector Bin Packing Problem. The authors propose an encoder to predict the connectivity probabilities of different items and a fine-tuned decoder to output the solution. Experiments demonstrate that the proposed method outperforms baselines on several benchmarks.

### Strengths
1.	To the best of my knowledge, this paper is the first learning-based method to address Class-Constrained Bin Packing Problems.
2.	Experiments demonstrate that the proposed method outperforms baselines on several benchmarks.

### Weaknesses
1. This paper studies a typical example of the vector Bin Packing Problem. The authors may want to explain the significance and generality of the studied problem in detail. Specifically, it is unclear how the class-constrained variant of bin packing relates to real-world applications or theoretical challenges in the broader field of combinatorial optimization. The paper should elaborate on the practical relevance and the unique difficulties posed by the class constraints, beyond a standard bin packing problem.
2. This paper proposes an encoder-decoder model to solve Class-Constrained Bin Packing Problems. However, many existing learning-based methods for solving combinatorial optimization problems are based on Encoder-Decoder Models as well [1, 2, 3]. The authors may want to explain the novelty of their proposed method over existing works in detail. The current description lacks a clear articulation of how the proposed encoder-decoder architecture differs from existing approaches, particularly in terms of the encoding and decoding mechanisms and how these differences lead to improved performance for the specific problem.
3. The authors propose to use a graph neural network to generate a connection heatmap for classifying items into different packs. However, the motivation of using a heatmap to classify items rather than directly learning a node classification model is unclear. The paper does not sufficiently justify why a heatmap representation is superior to a direct node classification approach for assigning items to bins. The advantages of using a heatmap, such as capturing pairwise relationships, are not clearly explained in the context of the bin packing problem.
4. Discussion on related work of other learning-based approaches for bin packing problems is missing. The paper lacks a comprehensive overview of existing learning-based methods for bin packing problems, which makes it difficult to assess the novelty and contribution of the proposed approach. A thorough discussion of related work is needed to properly contextualize the paper's contribution.
5. The baselines are insufficient. Although the authors compare their method against the pointer network, recent work has proposed several improved models of the pointer network [4, 5]. The authors may want to compare their method with these baselines. The comparison to a basic pointer network is not sufficient to demonstrate the effectiveness of the proposed method. The paper should include comparisons to more advanced pointer network architectures and other state-of-the-art learning-based approaches for combinatorial optimization.
6.  It would be more convincing if the authors could evaluate their method on large-scale benchmarks, such as bin packing problems with over 1,000 items. The current experimental evaluation is limited to relatively small problem instances. The paper should include results on larger-scale benchmarks to demonstrate the scalability and practical applicability of the proposed method.

### Questions
1. What is the technical novelty of the proposed method?
2. What is the motivation of using the heatmap to classify items?
3. Can the authors evaluate the proposed method on large-scale benchmarks?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
1.In this paper author proposed a vector BPP variant called Class-Constrained Bin Packing Problem (CCBPP), dealing with items of both
classes and sizes, and the objective is to pack the items in the least amount of bins respecting the bin capacity and the number of different classes that it can hold.

### Strengths
1.The pipeline encoder and decoder is quite unique work.
2. Presented results are compared with recent state of art techniques in detail.
3.More scope for the future researchers.

### Weaknesses
No

### Questions
1.Justify the need of encoder architecture proposed by Fraughnaugh, 1997 used here what advantages it has in the proposed work implementation.
2.Math mentioned in the decoder archticture in figure 2 should be mentioned in detail.

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
This paper presents a neural network solver for the bin packing problem. The neural network model is built under the encode-decoder framework, where the encoder network is a graph neural network to modulate the problem, and the decoder module contains heuristics, neighborhood search, and RL-like active search. Experiments are conducted on

### Strengths
* The problem of bin packing problem and its variants are important and worth studying.
* The methodology presented in this paper seems technically sound.
* The authors conduct extensive experiments on different variants of the bin packing problem. The design of data generation with ground-truth labels in the order consolidation problem is interesting. 
* This paper is well-written and easy to follow.

### Weaknesses
 * The encoder-decoder pipeline is quite common in machine learning solvers for combinatorial optimization problems. The authors make some specific adaptations for the bin packing problem, while in general, the results are not too surprising under such a framework. 
* It will be better to have more insights into the bin packing problem and what machine learning can help to inspire future researchers.

### Questions
* Can you plot the gap vs time for different methods?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors aim to solve a special 1D-BPP with class constraints. First, train a heatmap to represent the probability. Second, use a decode strategy to generate a solution from the heatmap while satisfying the constraints. In addition, it could be finetuned with RL.

I admit it is a new problem, but the action space is much smaller than traditional 3D-BPP.

### Strengths
The problem is new and the authors proposed a framework (which might be already used in TSP and VRP)  to solve the problem well.

The authors conduct comprehensive experiments. 

The ablations study is provided.

### Weaknesses
The used heatmap method is not new and a similar method has been used in TSP and VRP.

The studied topic CCBPP and problem is less-studied and uncommon to see.

The method is not explained well and clearly in the main body such as cluster decode and active search.

The active search seems to be fine-tuning with RL. I do not see anything novel.

The paper is not easy to follow.

The constraints seem not as complex as the constraints in 3D-BPP. In the seq2seq problem, it could be easily handled by the mask function.

### Questions
"we use class cosine similarities as edge feature" How to calculate the edge feature? 

What's the size number N set in the experiments?

What's the dataset used for finetuning in experiments? 

Is it a fair comparison with the baseline method without the finetuning dataset?

Why did the active search improve so significantly? 

Could you clearly explain how to select items? how do choose the current bin to place the selected items while satisfying constraints?

Could other constraints be considered rather than just class numbers?

The constraints seem not as complex as the constraints in 3D-BPP. In the seq2seq problem, it could be easily handled by the mask function.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
