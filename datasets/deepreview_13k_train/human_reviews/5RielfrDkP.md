# Learning Adaptive Multiresolution Transforms via Meta-Framelet-based Graph Convolutional Network

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Graph Neural Networks are popular tools in graph representation learning that capture the graph structural properties. However, most GNNs employ single-resolution graph feature extraction, thereby failing to capture micro-level local patterns (high resolution) and macro-level graph cluster and community patterns (low resolution) simultaneously. Many multiresolution methods have been developed to capture graph patterns at multiple scales, but most of them depend on predefined and handcrafted multiresolution transforms that remain fixed throughout the training process once formulated. Due to variations in graph instances and distributions, fixed handcrafted transforms can not effectively tailor multiresolution representations to each graph instance. To acquire multiresolution representation suited to different graph instances and distributions, we introduce the Multiresolution Meta-Framelet-based Graph Convolutional Network (MM-FGCN), facilitating comprehensive and adaptive multiresolution analysis across diverse graphs. Extensive experiments demonstrate that our MM-FGCN achieves SOTA performance on various graph learning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper use meta-learning to build for adaptive framelet for GNN.

They evaluate the model's performance on various graph learning tasks.

### Strengths
1. MM-FGCN is can learn adaptive multiresolution representation.

2. Achieve STOA performance on graph learning tasks.

3. parameterization of the meta-framelet generator uses use fewer parameters than previous method.

### Weaknesses
1. Require additional meta training.
2. The framelet is defined using a meta-band-pass filter based on polynomial splines, the model use Chebyshev approximation to circumventing the need for eigen-decomposition, but compared with graph-structure-based approach, Chebyshev approximation seems a more expensive.
3. Following the previous point, it seems it's hard to use the model on large graphs. (ogbn tasks)
4. The performance is not close to STOA, recent studies show better performance, e.g. [1],[2]

### Questions
1. Could you provide details on the time cost for meta-learning as well as the inference time for the model?
2. Would it be possible to evaluate the model on larger datasets like ogbn? I did observe ogbg-molhiv, but I'm referring to graphs with a larger number of nodes rather than the total number of graphs.
3. An detailed introduction to meta-learning would help readers in gaining a clearer understanding of the experimental setup.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The Multiresolution Meta-Framelet-based Graph Convolutional Network (MM-FGCN) is a novel approach to graph representation learning that allows for adaptive multiresolution analysis across diverse graphs. It achieves state-of-the-art performance on various graph learning tasks. 

In my opinion, adaptive multi-resolution is a promising yet difficult approach for the representation of graphs, lying in the intersection of graph signal processing and graph machine learning. In particular, I appreciate the construction of the framelet filters to satisfy the three properties (where denseness is different from the sparse and redundant representation in wavelet and framelet). The paper extends the framelet theory and presents the solution with relatively few parameters (only $\Theta, \omega$) to avoid a large number of parameters for the framelet system, yet achieves significant improvement in the experiments. The theories and proofs are solid in general, and though some of the writing could be improved, I think it is an excellent piece of work.

### Strengths
1. The paper proposes a novel approach to design an adaptive learnable set of multi-resolution representations on graphs, with solid theoretical motivation and proof.    
2. The proposed method significantly improves node classification (especially on disassortative tasks) and graph classification tasks.

### Weaknesses
1.The paper lacks some necessary model  and data descriptions for the implementation, like the specification of neural network $M_\xi$.    
2. minor issues:  missing "translation" before property near "Mallat, 2006".

### Questions
1. How is the neural network $M_\xi$ formulated? What does the output $\omega$ look like?     
2. How is the graph data split to obtain $S_{meta}, S_{main}$?    
3. Why is the meta training needed for the training procedure?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a Multiresolution Meta-Framelet-based Graph Convolutional Networks (MM-FGCN), which employs a diverse set of framelets for constructing graph convolution and learns meta-framelet generator networks via the meta-learning scheme. Since most GNNs depend on single-resolution graph feature extraction, they often fail to capture local patterns and community patterns simultaneously. To resolve it, some papers have proposed multi-resolution graph feature extraction-based GNNs. But, they use predefined and hand-crafted multiresolution transforms. To address these issues, this paper designs meta-learning based adaptive multiresolution graph convolution and they have shown the effectiveness with their experiments.

### Strengths
- The proposed paper deals with really important research problem. Simultaneously capturing high and low resolution with graph convolution is interesting and important.
- The proposed method seems novel to me.
- From their experiments, the proposed meta-framelet-based graph convolutional networks show good performance on various tasks. 
- The paper is well-written and easy to follow. In particular, the preliminary section provides the necessary and detailed information to understand the proposed method.

### Weaknesses
 - One of the important details about how to split the meta dataset from the main dataset is missing. It should have been provided to fairly compare the proposed method with other graph neural networks.
- In the same context, it would be better if you explain why meta learning framelet transforms is better than directly training them. From Table 3, it is easy to know that framelet transforms with meta-learning is more effective compared to the direct training scheme. But, why meta-learning scheme is better than the direct training scheme is mysterious. I think this is related to how to construct the meta dataset.
- It would be better if the author provided the change of filters according to the training step since the author claimed that the limitation of existing multiresolution transforms works is that they remain fixed throughout the training process. So, I'd like to see the variations of filters during the training and the analysis about it.

### Questions
- I think MM-FGCN can also be applied to the graph classification tasks. Could you provide the performance of MM-FGCN with MM-FGPool and MMFGCN with the standard graph pooling?

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
The paper proposes a new method for graph representation learning leverage spectral graph representation learning and meta learning. Experiments show the proposed method shows superior performance on a variety of graph datasets.

### Strengths
1. The method is relatively novel, combining several ideas from graph spectral filtering and meta learning.
2. Adequate ablation studies are performed to show the importance of proposed components.

### Weaknesses
1. The datasets used in the paper are relatively small, given the fact that there are a numerous large-scale graph benchmark datasets nowadays. It may not be a large concern in the early days, e.g. 2016-2017 when GNN was originally proposed, but in today’s standard more larger graphs are expected to evaluate the proposed approach rigorously and reliably. Specifically, the datasets used, such as Cora, Citeseer, and Pubmed, are often considered toy datasets in the current landscape of graph representation learning. The lack of evaluation on larger, more complex graphs limits the generalizability of the findings.
2. Lack of some well-known baseline methods such as GIN (Xu, Keyulu, et al. "How powerful are graph neural networks?." arXiv preprint arXiv:1810.00826 (2018).) and graph transformers (e.g. Rampášek, Ladislav, et al. "Recipe for a general, powerful, scalable graph transformer." Advances in Neural Information Processing Systems 35 (2022): 14501-14515.) Given the abundance of such existing methods, I encourage the authors to admit this fact and discuss about the pros and cons of using the proposed MM-FGCN approach in practice. The absence of comparisons with these models makes it difficult to assess the relative strengths and weaknesses of the proposed method. For example, GIN is known for its strong performance on node classification tasks, and graph transformers have shown impressive results on various graph benchmarks. A thorough comparison with these models is necessary to position the proposed method within the current state-of-the-art.
3. There is no mentioning on the releasement of the code making reproducibility hard. The lack of publicly available code hinders the ability of other researchers to verify the results and build upon this work. This is a significant concern for the reproducibility of the research.
4. Typo, e.g. “denseness, dilation property, and property (Mallat, 2006)” in Section 3.

### Questions
1. Why Geom-GCN in Table 6 lacks std?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
