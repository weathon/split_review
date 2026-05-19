### Summary

This paper proposes two methods to improve the performance of DP Transformers. The first method, Phantom Clipping, efficiently computes the per-sample gradient norm for parameter sharing embeddings in Transformers. The second method, Re-Attention, mitigates attention distraction within the DP training by correcting the attention scores based on the variance of the noise introduced by DP-SGD. The authors provide theoretical analysis and empirical results to support their claims.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper addresses an important problem in the field of differentially private deep learning, specifically for Transformers.
2. The proposed methods are well-motivated and theoretically grounded.
3. The empirical results demonstrate the effectiveness of the proposed methods in improving the performance of DP Transformers.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is not well-written and is difficult to follow. The authors should improve the clarity and organization of the paper.
2. The paper lacks a thorough comparison with existing DP Transformer methods. The authors should provide a more comprehensive comparison to highlight the advantages and disadvantages of their proposed methods.
3. The paper does not discuss the computational cost of the proposed methods. The authors should provide a detailed analysis of the time and space complexity of their methods and compare them with existing methods.
4. The paper does not discuss the limitations of the proposed methods. The authors should acknowledge the potential drawbacks and challenges of their methods.

### Suggestions

The paper needs significant improvements in clarity and organization. The introduction should clearly define the problem of applying differential privacy to Transformers, highlighting the specific challenges that the proposed methods aim to address. The motivation for Phantom Clipping and Re-Attention should be presented in a more structured manner, explaining the limitations of existing approaches and how the proposed methods overcome these limitations. The paper should also provide a more detailed explanation of the mathematical formulations and algorithms, making it easier for readers to understand the technical details. Furthermore, the experimental section should be reorganized to clearly present the setup, results, and analysis for each experiment. The authors should also consider adding more visualizations to help readers understand the behavior of the proposed methods. The paper should also include a more detailed discussion of the hyperparameter settings and their impact on the performance of the proposed methods.

The paper should include a more comprehensive comparison with existing DP Transformer methods. The authors should not only compare the performance of their methods with existing methods but also discuss the differences in the training procedures, privacy guarantees, and computational costs. The comparison should be done on a variety of datasets and tasks to demonstrate the generalizability of the proposed methods. The authors should also discuss the advantages and disadvantages of their methods compared to existing methods, highlighting the specific scenarios where their methods are most effective. The paper should also include a more detailed discussion of the limitations of the proposed methods. The authors should acknowledge the potential drawbacks and challenges of their methods, such as the potential for increased computational cost or the sensitivity to hyperparameter settings. The paper should also discuss the potential for future research to address these limitations.

The paper needs a more detailed analysis of the computational cost of the proposed methods. The authors should provide a theoretical analysis of the time and space complexity of their methods, and compare them with existing methods. The analysis should consider the impact of different parameters, such as the sequence length, embedding dimension, and batch size. The authors should also provide empirical results on the training time and memory usage of their methods, comparing them with existing methods. The paper should also discuss the potential for optimizing the implementation of the proposed methods to reduce their computational cost. The authors should also consider the impact of the proposed methods on the convergence rate of the training process. The paper should also discuss the potential for using techniques such as gradient accumulation or mixed-precision training to further improve the efficiency of the proposed methods.

### Questions

1. How does the proposed method handle the case where the attention scores are negative?
2. How does the proposed method handle the case where the noise added by DP-SGD is large?
3. How does the proposed method handle the case where the embedding dimension is large?

### Rating

5

### Confidence

3

**********
