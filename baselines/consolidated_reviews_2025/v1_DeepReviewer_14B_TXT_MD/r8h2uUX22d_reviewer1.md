### Summary

The paper studies the MLP-Mixer architecture, and shows that it is equivalent to a wider MLP with Kronecker product weights. This interpretation is used to shed light on the implicit bias of the architecture. The authors also propose a new family of MLP-Mixer-like architectures based on their interpretation.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The paper is well-written, and the authors seem to be knowledgeable in the field. The topic is interesting and relevant as the field moves forward and tries to understand the impact of architecture choices on learning. The results could potentially be very impactful given the recent interest in MLP-Mixer architectures, although I am not an expert in that field and my evaluation might be off.

### Weaknesses

#### Some Related Works


#### comment

I do not find any major issues in the paper, but I am not an expert in the field and I will update my review after the discussion period. I believe that the results could be presented in a more clear way, and that the implications of the theoretical results could be made more explicit. I leave this to the authors' expertise.

### Suggestions

The paper would benefit from a more detailed explanation of the practical implications of the Kronecker product weight structure. While the authors establish a theoretical link between MLP-Mixer and wider MLPs with Kronecker product weights, the paper does not fully explore how this connection can be leveraged in practice. For example, it would be beneficial to discuss specific parameterization strategies that could be used to exploit the Kronecker product structure, and how these strategies could lead to more efficient models or improved generalization. The authors could also provide more concrete examples of how the proposed interpretation can guide the design of new architectures, beyond the simple modification of patch sizes. A more thorough discussion of these aspects would significantly enhance the impact of the paper.

Furthermore, the paper could benefit from a more detailed discussion of the implicit biases induced by the Kronecker product structure. The authors mention that this structure leads to sparse weight matrices, but they do not fully explore the consequences of this sparsity. For instance, how does this sparsity affect the optimization landscape? Does it lead to better generalization performance compared to dense MLPs? A more in-depth analysis of these questions would provide a deeper understanding of the advantages and disadvantages of the proposed architecture. The authors could also explore the connection between the Kronecker product structure and other forms of regularization, such as low-rank approximations or structured sparsity. This would help to contextualize their findings within the broader literature on neural network regularization.

Finally, the paper should provide more clarity on the relationship between the proposed interpretation and existing techniques for analyzing neural network architectures. For example, how does the Kronecker product perspective relate to other methods for understanding the behavior of MLP-Mixers, such as spectral analysis or information-theoretic approaches? A more detailed comparison with these existing techniques would help to position the paper within the broader research landscape and highlight its unique contributions. The authors could also discuss the limitations of their approach and identify potential directions for future research. This would help to make the paper more accessible to a wider audience and stimulate further investigation into this area.

### Questions

1. Is the Kronecker product structure something that can be exploited in practice? For example, by using specific parameterizations, could we benefit from the structure to get more efficient models?
2. Is it possible to modify the architecture to remove the ineffectively large intermediate dimension, while maintaining the benefits of the implicit bias?

### Rating

6: marginally above the acceptance threshold

### Confidence

1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

**********
