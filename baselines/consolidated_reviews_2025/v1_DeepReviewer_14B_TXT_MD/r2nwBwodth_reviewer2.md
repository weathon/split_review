### Summary

The paper proposes a self-supervised learning method for time series data. The method is based on predicting statistical functionals of masked regions of the time series. The authors show that this method outperforms a baseline method (MAE) and is competitive with a state-of-the-art method (data2vec).

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The proposed method is simple and easy to understand.
- The paper is well-written and easy to follow.
- The authors provide a clear motivation for their work and explain the limitations of existing methods.

### Weaknesses

#### Some Related Works


#### comment

 - The experimental results are not very convincing. The proposed method only outperforms MAE by a small margin, and it is not clear if this difference is statistically significant. Also, the proposed method is not consistently better than data2vec across all tasks.
- The paper does not provide a good explanation of why the proposed method should be better than existing methods. The authors only provide a high-level intuition, but they do not provide any theoretical analysis or empirical evidence to support their claims.
- The paper does not discuss the limitations of the proposed method. For example, the authors do not discuss how the choice of statistical functionals affects the performance of the method. It is unclear how sensitive the method is to this choice, and what principles should guide the selection of functionals for different types of time series data. Furthermore, the paper does not address the potential for information loss when using lower-order functionals to represent complex time series data, especially when compared to methods that operate on the raw signal or higher-order representations.

### Suggestions

The paper would benefit from a more rigorous analysis of the proposed method's performance. Specifically, the authors should conduct statistical significance tests to determine if the observed improvements over MAE are indeed meaningful. Furthermore, a more detailed comparison with data2vec is needed, analyzing the specific scenarios where the proposed method excels or falls short. It would be beneficial to explore the impact of different masking strategies and their interaction with the chosen functionals. The authors should also investigate the sensitivity of the method to the choice of statistical functionals, perhaps by conducting an ablation study where different sets of functionals are used. This would provide a better understanding of the method's robustness and generalizability.

To strengthen the theoretical grounding of the method, the authors should provide a more in-depth explanation of why predicting statistical functionals is a useful pre-training task for time series data. This could involve relating the proposed method to existing theoretical frameworks in representation learning or by providing a novel theoretical analysis. The authors should also discuss the potential limitations of using lower-order functionals to represent complex time series data. For example, they could analyze the information content of the chosen functionals and compare it to the information content of the raw signal. This would help to clarify the trade-offs between simplicity and expressiveness in the proposed method. It would also be beneficial to explore the use of more complex functionals or combinations of functionals to capture more nuanced aspects of the time series data.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method. This should include a discussion of the computational cost of the method, its sensitivity to hyperparameter choices, and its applicability to different types of time series data. The authors should also discuss the potential for the method to be biased towards certain types of time series data or certain types of downstream tasks. Addressing these limitations would provide a more balanced and realistic assessment of the proposed method's strengths and weaknesses. The authors should also consider comparing their method to other self-supervised learning approaches for time series data, beyond just MAE and data2vec, to provide a more comprehensive evaluation.

### Questions

- How does the proposed method compare to other self-supervised learning methods for time series data?
- How does the choice of statistical functionals affect the performance of the method?
- What are the limitations of the proposed method?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
