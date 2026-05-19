### Summary

This paper proposes Swin4TS algorithm for long-term time series forecasting (LTSF). The algorithm incorporates the window-based attention and hierarchical representation techniques from the Swin Transformer, a well-known ViT algorithm, and applies them to the LTSF. The authors show that Swin4TS outperforms the latest baselines and achieves state-of-the-art performance on 8 benchmark datasets.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The idea of applying Swin Transformer to LTSF is intuitive and convincing.
2. The authors provide a detailed explanation of the proposed method, including both channel-dependence and channel-independence strategies. The use of window-based attention and hierarchical representation is well-motivated and clearly described.
3. The authors conduct extensive experiments on 8 benchmark datasets and achieve impressive results. The ablation study further demonstrates the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that the proposed method has linear computational complexity, but do not provide a formal proof or analysis to support this claim. The lack of a detailed complexity analysis, particularly concerning the window-based attention mechanism, makes it difficult to assess the scalability of the proposed method. It is unclear how the linear complexity is derived, especially when considering the hierarchical representation and shift-window attention operations. A rigorous analysis, including the dependence on input sequence length and number of channels, is needed.
2. The authors only provide the inference time and memory usage for one baseline model (PatchTST). A more comprehensive comparison with other baselines would be helpful for a thorough evaluation. The absence of a broader comparison makes it difficult to contextualize the computational efficiency of the proposed method relative to other state-of-the-art approaches. It is important to compare against a diverse set of models to understand the trade-offs between accuracy and computational cost.
3. The authors do not discuss the limitations of the proposed method in detail. For example, the effectiveness of Swin4TS/CD may depend on the quality and quantity of the training data, as well as the complexity of the underlying time series patterns. The paper lacks a discussion on potential failure cases or scenarios where the proposed method might underperform. For instance, it is unclear how the method would handle time series with abrupt changes or non-stationary behavior.

### Suggestions

To address the lack of a formal complexity analysis, the authors should provide a detailed derivation of the computational complexity of the proposed Swin4TS algorithm. This analysis should include a breakdown of the complexity of each component, such as the window-based attention, shift-window attention, and hierarchical representation. The analysis should explicitly show how the complexity scales with respect to the input sequence length (L), the number of channels (M), and the number of patches (N). Furthermore, the authors should provide a comparison of the computational complexity of Swin4TS with other state-of-the-art methods, such as Transformer, Informer, Autoformer, FEDformer, PatchTST, Crossformer, and TimesNet. This comparison should be presented in a table format, clearly showing the order of complexity for each method. This will allow readers to better understand the computational advantages and disadvantages of the proposed method.

To provide a more comprehensive evaluation of the computational efficiency of the proposed method, the authors should include inference time and memory usage comparisons with a wider range of baseline models. Specifically, the authors should compare the inference time and memory usage of Swin4TS with PatchTST, Crossformer, and TimesNet, in addition to the comparisons already provided with PatchTST. These comparisons should be conducted on the same hardware and software configurations to ensure a fair evaluation. The authors should also provide a discussion of the factors that contribute to the differences in inference time and memory usage among the different models. This will help readers to better understand the trade-offs between accuracy and computational cost when choosing between different methods. The authors should also consider providing a more detailed analysis of the memory usage, including the memory usage for different components of the model, such as the attention layers and the feed-forward networks.

Finally, the authors should provide a more detailed discussion of the limitations of the proposed method. This discussion should include a consideration of the factors that may affect the performance of Swin4TS, such as the quality and quantity of the training data, the complexity of the underlying time series patterns, and the presence of noise or outliers in the data. The authors should also discuss the potential failure cases of the proposed method, such as when the time series data is highly non-stationary or contains abrupt changes. The authors should also consider providing some guidelines on how to choose between Swin4TS/CD and Swin4TS/CI, based on the characteristics of the dataset. For example, the authors could discuss the trade-offs between the two methods in terms of computational cost and accuracy, and provide some recommendations on when to use each method.

### Questions

1. Can you provide a formal proof or analysis to support the claim of linear computational complexity?
2. Can you provide a more comprehensive comparison of inference time and memory usage with other baselines?
3. What are the limitations of the proposed method? How does the effectiveness of Swin4TS/CD depend on the quality and quantity of the training data and the complexity of the underlying time series patterns?
4. How does the proposed method handle the uncertainty in the forecasting process?
5. How does the proposed method compare to other state-of-the-art methods in terms of interpretability? Can you provide some insights into the learned representations and attention patterns?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
