### Summary

This paper proposes ReMasker, a method for missing value imputation in tabular data. ReMasker extends the masked autoencoding framework to impute missing values by randomly masking some values (both observed and missing) and training the model to reconstruct the re-masked values. The authors conduct experiments on 12 datasets under MAR, MCAR, and MNAR settings, showing that ReMasker outperforms 13 baselines in terms of imputation accuracy and utility.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The idea of extending masked autoencoding to missing value imputation is interesting and novel.
- The experiments are extensive, including 12 datasets, various missingness mechanisms, and 13 baselines. The ablation studies are also comprehensive, covering encoder/decoder depth/width, embedding width, and masking ratio.

### Weaknesses

#### Some Related Works

[1] MissForest—nonparametric missing value imputation for mixed-type data.

#### comment

 - The novelty of the proposed method is limited. The idea of extending masked autoencoding to missing value imputation is not new, and the proposed method is a straightforward application of MAE to tabular data. The paper does not adequately address why this straightforward application is novel, especially given the existing literature on MAE for tabular data imputation. The core idea of masking and reconstruction is already established, and the paper needs to articulate a more compelling justification for its novelty beyond simply applying it to a new domain.
- The paper lacks theoretical analysis and justification. The authors claim that ReMasker encourages learning missingness-invariant representations, but they do not provide any theoretical analysis or justification for this claim. The paper needs to provide a more rigorous explanation of why the proposed method should learn representations that are invariant to missingness patterns. Without this, the claim remains unsubstantiated.
- The paper does not compare with other state-of-the-art methods for mixed-type data imputation, such as MissForest [1]. The absence of a comparison with MissForest, a well-established method for handling mixed-type data, is a significant oversight. The paper should include a comparison with MissForest to provide a more comprehensive evaluation of the proposed method's performance.
- The paper does not compare with other state-of-the-art methods for missing value imputation under MNAR, such as [2]. The lack of comparison with methods specifically designed for MNAR settings is a major weakness. The paper should include a comparison with these methods to demonstrate the effectiveness of the proposed method in handling MNAR data.

### Suggestions

The paper should provide a more detailed explanation of the novelty of the proposed method. While the idea of extending masked autoencoding to tabular data is interesting, the paper needs to clearly articulate why this is a novel contribution beyond a straightforward application of existing techniques. The authors should discuss the specific challenges of applying MAE to tabular data and how their method addresses these challenges in a unique way. For example, they could discuss the specific masking strategy used and how it is tailored to the characteristics of tabular data. Furthermore, the paper should provide a more thorough discussion of the existing literature on MAE for tabular data imputation, highlighting the differences and advantages of their approach. This would help to establish the novelty of the proposed method and justify its contribution to the field.

The paper needs to provide a more rigorous theoretical analysis of why the proposed method learns missingness-invariant representations. The authors should provide a formal definition of missingness-invariant representations and explain how their method encourages the model to learn such representations. This could involve analyzing the loss function and the training process to show how the model is forced to focus on features that are not directly affected by missingness. The paper should also provide empirical evidence to support the claim that the learned representations are indeed invariant to missingness patterns. This could involve experiments that specifically test the model's ability to generalize to different missingness mechanisms. Without a strong theoretical foundation, the claim of missingness-invariant representations remains speculative.

The paper should include a more comprehensive experimental evaluation that includes comparisons with state-of-the-art methods for mixed-type data imputation, such as MissForest, and methods specifically designed for MNAR settings. The inclusion of MissForest is crucial to demonstrate the effectiveness of the proposed method for mixed-type data, as it is a widely used and well-established method in this area. The paper should also include a comparison with methods specifically designed for MNAR settings, such as those mentioned in the original review. This would provide a more complete picture of the proposed method's performance and its ability to handle different types of missingness. The experimental results should be analyzed in detail, and the paper should discuss the strengths and weaknesses of the proposed method compared to the baselines.

### Questions

- How does the proposed method compare to other state-of-the-art methods for mixed-type data imputation, such as MissForest?
- How does the proposed method compare to other state-of-the-art methods for missing value imputation under MNAR, such as [2]?

[2] Li, J., Chen, H., & Liu, T. (2021). Missgnn: Missing value imputation for mixed-type data with graph neural networks. In Proceedings of the ACM on Web Conference 2021 (pp. 699-708).

### Rating

3

### Confidence

4

**********
