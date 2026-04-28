# Forward Learning of Graph Neural Networks

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
vspace{-0.8em}
Graph neural networks (GNNs) have achieved remarkable success across a wide range of applications, 
such as recommendation, drug discovery, and question answering.
Behind the success of GNNs lies the backpropagation (BP) algorithm,
which is the de facto standard for training deep neural networks (NNs).
However, despite its effectiveness, BP imposes several constraints, which are not only biologically implausible, 
but also limit the scalability, parallelism, and flexibility in learning NNs.
Examples of such constraints include 
storage of neural activities computed in the forward pass for use in the subsequent backward pass, and
the dependence of parameter updates on non-local signals.
To address these limitations, 
the forward-forward algorithm (FF) was recently proposed as an alternative to BP in the image classification domain,
which trains NNs by performing two forward passes over positive and negative data.
Inspired by this advance, we propose \method in this work, a new forward learning procedure for GNNs,
which avoids the constraints imposed by BP via an effective layer-wise local forward training.
\method extends the original FF to deal with graph data and GNNs, 
and makes it possible to operate without generating negative inputs (hence no longer forward-forward).
Further, \method enables each layer to learn from both the bottom-up and top-down signals without relying on the backpropagation of errors.
Extensive experiments on real-world datasets
show the effectiveness and generality of the proposed forward graph learning framework.
We release our code at \repoURL.
\vspace{-1.0em}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper is an application of forward forward learning on graph neural networks. Authors modify the forward forward learning algorithm to train GNNs with several novel designs including node labels, virtual nodes, single forward pass, and the top-down signals. In summary, this paper is a good practice by applying forward forward algorithm to GNN learning and provides sufficient technical contribution with sound experiments. I raise a marginally accept for the lack of important experiments.

### Strengths
1. Authors systematically investigate the forward learning algorithm on GNNs.
2. This paper provides several technical contributions to forward forward algorithm, which is inspiring and important.
3. Extensive experiments have been carried out to prove their effectiveness.

### Weaknesses
1. Motivation is not well illustrated
2. Time efficiency is not analyzed
3. In the node classification task, authors randomly selected 64% for training, which is not the common practice in graph learning. In most cases, we only select a small percentage for training, as in the GCN, GAT, and SAGE paper author mentioned. I think more experiments on limited training data are needed as their proposed algorithm seems sensitive to that.

### Questions
1. From my point of view, the motivation of this paper is to apply the forward forward algorithm to GNN training. They do not mention what the problem is with the current BP training method on GNN. The three points (scalability, parallelism, and flexibility) they mentioned do not seem to be graph-related. I suggest finding a stronger motivation in the introduction, such as what the problem FF wants to solve on graph learning.
2. By training layer by layer, FF can be seen as a time-for-space algorithm. In the experiment, authors only show the limited space utilization without mentioning the overhead training time. I think it is inappropriate.
3. In the node classification task, authors randomly selected 64% for training, which is not the common practice in graph learning. In most cases, we only select a small percentage for training, as in the GCN, GAT, and SAGE paper author mentioned. I think more experiments on limited training data are needed as their proposed algorithm seems sensitive to that.

### Soundness
3 good

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Traditional training of GNNs relies on the backpropagation (BP) algorithm, which imposes certain constraints that limit scalability, parallelism, and flexibility in learning. To overcome these limitations, the authors propose FORWARDGNN, inspired by the forward-forward (FF) algorithm used in image classification. FORWARDGNN extends FF to work with graph data, eliminating the need for generating negative inputs and allowing layer-wise local forward training. The new method enables each layer to learn from both bottom-up and top-down signals without relying on error backpropagation. The paper demonstrates the effectiveness and generality of FORWARDGNN through experiments on five real-world datasets and three GNNs, showing that it performs on par or better than BP on link prediction and node classification tasks while being more memory efficient.

### Strengths
Forward-Forward learning proposed by Hinton is a very new and interesting research topic. This paper adopts that in GNN setup, and propose an alternative ( Single forward ) which only runs a single forward pass.


Experiments are very comprehensive, including both effectiveness and training efficiency.

### Weaknesses
Overall I think this is an interesting paper. Given the Forward-Forward Learning is a very new concept, this work is an interesting trial on the direction.

One question is can the proposed forward-only method only work for graph learning? Or it can be generalized to other tasks? If yes, better to show such results to make this work more solid; if not, better to explain clearly the assumption and some unique properties of graph to make this method work.



### Questions
see weakness.

How is this paper different from: "Decoupled Greedy Learning of Graph Neural Networks"

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The de-facto standard algorithm for training Graph Neural Networks (GNNs) is *Backpropagation*. Despite several advantages, the need to backpropagate gradients through the neural architecture hinders its scalability whenever the architecture depth increases. The recent Forward-Forward (FF) approach by Hinton et al. has inspired several works that aim at local/forward-only learning procedures. In this work, the authors propose ForwardGNN, which investigates FF in the context of GNNs for node classification and link prediction tasks, as well as and proposing a novel approach that requires only a single forward pass to learn GNNs.

### Strengths
The paper is well written and structured. The proposed approach is original, given that it extends the **FF** approach to GNNs by proposing a forward-only mechanism that avoids multiple forward passes for the positive and negative samples,  that would be required by standard FF.
Moreover, the interesting incorporation of top-down signals from upper layers is a clever intuition.

### Weaknesses
There are some details of the approach that have not been clearly described. 
In the case of the approaches that leverage virtual nodes (Sections 3.1-bottom and 3.2): the authors specify that the graph topology is enriched by such virtual nodes. It is not clear to me wheter such virtual nodes are processed as standard nodes by the GNNs -- e.g. they need initial nodal features $h_i^{(0)}$ and both receive and send message towards neighbors -- or they are solely used as *receiver* nodes, e.g. they only have incoming edges-- in order to compute their representation $c_k^{(\ell)}$.  

The role of the virtual nodes in the graph topology raises another question: if I did get it correctly, there are as many virtual nodes as classes. Hence, many nodes (depending on the graph scale) will be connected to the same virtual node forming a bottleneck. This approach seem to be very prone to the issue of over-squashing [1,2]. What happens when the number of classes is very low with respect to the graph scale (with millions of nodes)? An analysis on this could improve the paper contribution. 

The experimental setup analyzes some competitors that were not devised for GNN in the tasks of node classification and link prediction. Given that the **GFF** model by Paliotta et al. [3] is explicitly devised for GNNs, why did the authors not compare with **GFF**? Is the proposed approach compatible with the Graph classification task?

Regarding related work, there are some works that proposed alternative local rules for learning in GNNs that depart from the BackProp approach [4, 5]. Describing differences and advantages could help the reader in understanding the paper contributions.  

*Minors*
The authors refer to Alg. 1, 2, 3 that are not in the main paper (it should be clarified).

### Questions
Please also refer to the **Weaknesses** section.

1) It is not clear to me wheter virtual nodes are processed as standard nodes by the GNNs -- e.g. they need initial nodal features $h_i^{(0)}$ and both receive and send message towards neighbors -- or they are solely used as *receiver* nodes, e.g. they only have incoming edges-- in order to compute their representation $c_k^{(\ell)}$.  

2) The virtual node approach seem to be very prone to the issue of over-squashing [1,2]. What happens when varying the number of classes with respect to the graph scale (with millions of nodes)? An analysis on this could improve the paper contribution. 

3) The experimental setup analyzes some competitor algorithms that were not devised for GNNs, in the tasks of node classification and link prediction. Given that the **GFF** model by Paliotta et al. [3] is explicitly devised for GNNs, why did the authors not compare with **GFF**? Is the proposed approach compatible with the Graph classification task?

4) The authors analyzed the memory impact of the proposed method. What about the time complexity/execution timings?  And what are the model ability to scale to bigger graphs?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes ForwardGNN, a novel forward learning framework for Graph Neural Networks (GNNs) that addresses the limitations of the backpropagation (BP) algorithm, such as memory overhead and biological implausibility. By building upon and improving the forward-forward algorithm (FF), ForwardGNN is designed to work with graph data and GNNs without generating negative inputs. This results in a more efficient training and inference process. The framework also enables each layer to learn from both bottom-up and top-down signals without relying on backpropagation. Experiments conducted on five real-world datasets and three representative GNNs demonstrate the effectiveness and generality of the forward graph learning framework, showing that it outperforms or performs on par with BP while using less memory for training.

### Strengths
1. This paper systematically explores the potential of forward graph learning, paving the way for biologically plausible optimization techniques in GNNs.

2. The performance is impressive; this marks the first instance where FF algorithms outperform BP-trained deep neural networks in real-world applications.

3. The study proposes numerous algorithms that are model-agnostic, potentially inspiring further research on forward-forward algorithms in various applications.

### Weaknesses
There are a few areas for improvement:

1.  The proposed methods share a close relationship with layer-wise training of neural networks, which could potentially diminish the significance of this paper. Specifically, the paper does not adequately differentiate itself from existing layer-wise training methods for GNNs, such as those that use auxiliary classifiers at each layer [1,2]. A more extensive literature review is necessary to clarify the novelty of the proposed approach compared to these methods, particularly in how the forward-forward algorithm is adapted and whether the proposed method truly avoids backpropagation in the optimization of each layer. Additionally, the paper's contribution could be strengthened by including experiments for comparison with [2], which also explores layer-wise training of GNNs.

2. The data splitting does not adhere to standard practices. The paper should clarify why the standard semi-supervised node classification splits were not used and provide a justification for the chosen splitting method. This deviation makes it difficult to compare the results with prior work.

3. In Figure 2, the upper-left corner is crowded with too many methods, making it difficult to read. The overlapping lines and markers make it challenging to discern the performance of each method. Presenting the results in a table might be a better approach (the table should be much simpler compared to Table 2 and Table 3), or using a clearer visualization technique.

4. In Algorithms 1-4, the authors state "optimize layer using the computed loss" but the details of the optimizer are not clear, e.g., what optimizer is used, what are the learning rates, and how are these parameters tuned. This lack of detail makes it difficult to reproduce the results and understand the practical implementation of the proposed method.

5. In addition to memory, training time is an important metric. The paper should include the training time of the proposed method and baselines to provide a complete picture of the computational efficiency. This is crucial for understanding the practical applicability of the proposed method.

6. In Table 2, why does SF-Top-To-Loss achieve state-of-the-art performance with one layer, but the performance degrades with more layers? An explanation is needed, particularly regarding the potential for overfitting or the propagation of noisy gradients in deeper networks.

7. In Table 2, the best-performing method varies significantly across datasets. Providing an intuition for this variation would be beneficial. The paper should discuss the characteristics of each dataset that might favor one method over another, such as graph density, node degree distribution, or label correlation.

8. In Table 3, the memory of some proposed methods is higher than BP (even 20 times higher in Table 3 (c) GAT). This significant increase in memory usage could be a major bottleneck, especially for large graphs. The paper needs to address this limitation and discuss the practical implications of such high memory requirements.

### Questions
1. The proposed method involves layer-by-layer training of GNNs. In the literature, layer-wise training of deep neural networks has been a long-standing topic [1,2]. A more extensive literature review is necessary to differentiate the present paper. Additionally, the paper's contribution could be strengthened by including experiments for comparison with [2].

2. The data splitting differs significantly from those in previous papers. I recommend that the authors conduct experiments using standard splitting for semi-supervised node classification tasks.

3. In Figure 2, the upper-left corner is crowded with too many methods, making it difficult to read. Presenting the results in a table might be a better approach (the table should be much simpler compared to Table 2 and Table 3).

4. In Algorithms 1-4, the authors state "optimize layer using the computed loss" but the details of the optimizer are not clear, e.g., what optimizer is used.

5. In addition to memory, training time is an important metric. Including the training time of the proposed method and baselines will complete the picture.

6. In Table 2, why does SF-Top-To-Loss achieve state-of-the-art performance with one layer, but the performance degrades with more layers? An explanation is needed.

7. In Table 2, the best-performing method varies significantly across datasets. Providing an intuition for this variation would be beneficial.

8. In Table 3, the memory of some proposed methods is higher than BP (even 20 times higher in Table 3 (c) GAT). Would this be a significant bottleneck?

[1] Belilovsky E, Eickenberg M, Oyallon E. Greedy layerwise learning can scale to imagenet, ICML 2019. 
[2] You Y, Chen T, Wang Z, et al. L2-gcn: Layer-wise and learned efficient training of graph convolutional networks, CVPR 2020.

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good
