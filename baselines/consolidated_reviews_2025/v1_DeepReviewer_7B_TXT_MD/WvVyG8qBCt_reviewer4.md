### Summary

This paper proposes two methods to train differentially private Transformers. The first method is called "phantom clipping", which is an efficient per-sample gradient norm computation method for Transformers with parameter sharing. The second method is called "re-attention", which is a method to mitigate attention distraction by correcting the attention scores. Experiments on two real-world datasets demonstrate the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The authors provide theoretical analysis to support their claims.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that the proposed method can reduce computational costs during gradient clipping. However, they do not provide a detailed comparison of the computational costs with other methods. Specifically, the paper lacks a breakdown of the computational overhead of Phantom Clipping compared to standard per-sample gradient clipping, including FLOPs or wall-clock time. It is unclear how the proposed method scales with increasing sequence lengths and model sizes, which are critical factors in Transformer training.
2. The authors claim that the proposed method can reduce attention distraction. However, they do not provide sufficient experimental evidence to support this claim. The experiments only show the performance of the proposed method on two datasets, and it is unclear how the method performs on other datasets with different characteristics. Furthermore, the paper does not provide a detailed analysis of the attention scores or the attention distraction phenomenon, making it difficult to assess the effectiveness of the proposed method in mitigating this issue.

### Suggestions

The paper would benefit from a more thorough analysis of the computational costs associated with the proposed Phantom Clipping method. The authors should provide a detailed comparison of the computational overhead of Phantom Clipping against standard per-sample gradient clipping, breaking down the costs by different components of the Transformer model. This analysis should include a breakdown of the FLOPs or wall-clock time required for each step, such as the computation of the gradient norm and the parameter sharing. Furthermore, the authors should investigate how the computational cost of Phantom Clipping scales with increasing sequence lengths and model sizes. This could be done by providing a table showing the computational cost of Phantom Clipping for different sequence lengths and model sizes, and comparing it to the cost of standard per-sample gradient clipping. This would provide a clearer understanding of the practical benefits of the proposed method, especially in resource-constrained environments.

To strengthen the claim that the proposed method reduces attention distraction, the authors should provide more comprehensive experimental evidence. The experiments should be conducted on a wider range of datasets, including datasets with different characteristics, such as varying sequence lengths, vocabulary sizes, and data distributions. This would demonstrate the generalizability of the proposed method. Additionally, the authors should provide a more detailed analysis of the attention scores, such as visualizations of the attention maps before and after applying the Re-Attention mechanism. This would help to understand how the Re-Attention mechanism mitigates attention distraction. Furthermore, the authors should provide a quantitative analysis of the attention distraction phenomenon, such as measuring the variance of the attention scores before and after applying the Re-Attention mechanism. This would provide a more objective assessment of the effectiveness of the proposed method in reducing attention distraction.

Finally, the authors should clarify the relationship between the theoretical analysis and the experimental results. The theoretical analysis should be more closely aligned with the experimental setup and results. For example, the authors could provide a theoretical analysis of the computational cost of Phantom Clipping and compare it to the empirical results. Similarly, the authors could provide a theoretical analysis of the effectiveness of Re-Attention in reducing attention distraction and compare it to the empirical results. This would provide a more rigorous and convincing evaluation of the proposed method. The authors should also discuss the limitations of their theoretical analysis and the potential for future work in this area.

### Questions

1. How does the proposed method perform on other datasets?
2. How does the proposed method compare to other methods in terms of computational costs?

### Rating

6

### Confidence

3

**********
