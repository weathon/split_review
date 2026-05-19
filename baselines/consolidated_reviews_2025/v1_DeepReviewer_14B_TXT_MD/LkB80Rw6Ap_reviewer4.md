### Summary

This paper proposes a new message-passing neural network (MPNN) model, called Curvature-Constrained Message Passing (CCMP), that leverages the curvature of the edges to guide learning by dissociating edges with positive and negative curvature. The authors propose different variants of this model, each one based on a different way of propagating the information: only on edges with negative curvature, positive curvature, or a combination of both. They also propose two- or one-hop propagation strategies that are bound to the curvature. The authors empirically demonstrate a performance gain on heterophilic datasets and show that using a curvature message passing attenuates over-squashing.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a new measure of homophily based on edge curvature that allows us to better model the community behavior of a neighborhood. This is a novel and interesting idea that has not been explored before in the context of MPNNs.

2. The paper proposes a new MPNN model (curvature-constrained message passing) that leverages the curvature of the edges to guide learning by dissociating edges with positive and negative curvature. This is a novel and interesting idea that has not been explored before in the context of MPNNs.

3. The paper empirically demonstrates a performance gain on heterophilic datasets and shows that using a curvature message passing attenuates over-squashing. This is a significant result that shows the effectiveness of the proposed method.

### Weaknesses

#### comment

1. The paper does not provide a theoretical analysis of the proposed method. It is not clear how the curvature-constrained message passing affects the convergence of the model or the generalization error. A theoretical analysis would provide a deeper understanding of the method and its limitations.

2. The paper does not compare the proposed method to other state-of-the-art methods for mitigating over-squashing, such as graph transformers or other graph neural networks with long-range interactions. A comparison to these methods would provide a better understanding of the strengths and weaknesses of the proposed method.

3. The paper does not provide a detailed analysis of the computational cost of the proposed method. It is not clear how the curvature computation affects the training time and memory usage of the model. A detailed analysis of the computational cost would be useful for practitioners who want to use the proposed method.

### Questions

1. How does the curvature-constrained message passing affect the convergence of the model? Is there any theoretical guarantee on the convergence of the model?

2. How does the proposed method compare to other state-of-the-art methods for mitigating over-squashing, such as graph transformers or other graph neural networks with long-range interactions?

3. What is the computational cost of the proposed method? How does the curvature computation affect the training time and memory usage of the model?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
