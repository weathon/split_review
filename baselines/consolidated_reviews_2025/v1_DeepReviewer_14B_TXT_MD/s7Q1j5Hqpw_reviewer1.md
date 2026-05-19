### Summary

This paper proposes a Shift-Resilient Diffusive Imputation (SRDI) framework to address the challenge of Variable Subset Forecasting (VSF) in time series data. In VSF, models trained on complete datasets are tested on datasets with missing variables due to issues like sensor failures, leading to distribution shifts that degrade forecasting accuracy. The SRDI framework tackles these challenges by integrating a diffusion-based imputation model with a meta-learning strategy. It separates data patterns into invariant and variant components to handle inter-series shifts and uses meta-learning to adapt to intra-series shifts across different time windows. Extensive experiments on multiple datasets demonstrate that SRDI outperforms existing imputation methods, providing more robust and accurate forecasting in VSF scenarios.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. This paper addresses the critical and underexplored problem of Variable Subset Forecasting (VSF), which is highly relevant to real-world applications such as IoT and sensor networks where missing data is common.
2. The paper introduces a novel approach by framing VSF within a shift-resilient diffusive imputation framework, integrating both inter-series and intra-series shifts, and leveraging meta-learning for adaptation.

### Weaknesses

#### Some Related Works


#### comment

1. The paper presents a method for Variable Subset Forecasting (VSF) by focusing on imputation followed by forecasting, but it does not clearly establish the unique advantages of this approach compared to traditional time series forecasting. The motivation for addressing VSF through imputation is not well-justified, especially given that the ultimate goal is forecasting. A more detailed explanation of why imputation is a necessary step, rather than directly training a forecasting model on the available variables, would strengthen the paper's premise.
2. The paper proposes a denoising approach to decompose time series data into invariant and variant patterns but does not provide sufficient theoretical or experimental evidence to substantiate the effectiveness of this method. The core idea of separating stable and unstable components is not novel, but the specific implementation within a diffusion model lacks rigorous justification. The paper needs to demonstrate that the proposed denoising approach effectively captures meaningful invariant patterns and that these patterns contribute to improved imputation and forecasting performance.
3. The experiments compare the proposed method with models trained on complete data (Oracle) and partially available data (Partial), but they do not include comparisons with models specifically designed for incomplete data. This omission limits the ability to assess the true value of the proposed method. The comparison against 'Partial' and 'Oracle' settings is not sufficient to demonstrate the superiority of the proposed method over existing techniques designed for handling missing data in time series.
4. The paper’s division of inter-series and intra-series shifts lacks clear justification, and the treatment of intra-series shift with meta-learning seems misapplied. The categorization of shifts is not well-defined, and the application of meta-learning to handle intra-series shift, which is essentially a distribution shift within the same series, seems inappropriate. Meta-learning is typically used for learning across different tasks, not for adapting to distribution shifts within a single task.

### Suggestions

The paper should more clearly articulate the specific challenges of VSF that necessitate an imputation-based approach. It is not sufficient to state that imputation is a common technique; the authors need to explain why directly training a forecasting model on the available subset of variables is inadequate for this specific problem. For example, they could discuss the potential for increased error propagation or the difficulty in capturing complex inter-variable relationships when training directly on incomplete data. Furthermore, the authors should provide a more detailed analysis of the limitations of existing imputation methods when applied to VSF, highlighting why a diffusion-based approach is needed. This would involve a discussion of how traditional imputation methods fail to capture the underlying data generating process in the presence of variable subsets, and how the proposed method addresses these specific shortcomings. The motivation needs to be more precise and technically grounded, rather than relying on general statements about the prevalence of missing data.

The paper needs to provide more substantial evidence for the effectiveness of the proposed denoising approach. The authors should include experiments that directly evaluate the quality of the decomposed invariant and variant patterns. For example, they could visualize these patterns or use quantitative metrics to assess their stability and variability. Furthermore, the paper should include ablation studies to demonstrate the contribution of each component of the denoising process to the overall performance. This would involve comparing the full model with variants that exclude the invariant variant decomposition, or that use alternative decomposition methods. The authors should also provide a theoretical justification for why the proposed denoising approach is expected to work, rather than relying solely on empirical results. This could involve discussing the properties of the diffusion model that make it suitable for this task, and how the proposed denoising process aligns with these properties. The paper should also clarify how the model handles the temporal dependencies of the variant patterns, given that they are extracted at each time step.

The experimental evaluation needs to be significantly improved by including comparisons with state-of-the-art methods specifically designed for handling incomplete time series data. The current comparison against 'Partial' and 'Oracle' settings is not sufficient to demonstrate the superiority of the proposed method. The authors should include comparisons with methods that explicitly address missing data in time series forecasting, such as those based on recurrent neural networks with imputation layers, or other diffusion-based imputation methods that are designed for time series. Furthermore, the paper should provide a more detailed analysis of the performance of the proposed method under different missing data scenarios, such as varying missing rates and patterns. This would involve conducting experiments with different proportions of missing variables and different patterns of missingness (e.g., random, block-wise). The paper should also discuss the computational cost of the proposed method and compare it to existing approaches. Finally, the authors should reconsider the use of meta-learning for handling intra-series shift and explore alternative approaches that are more suitable for adapting to distribution shifts within a single task, such as domain adaptation techniques.

### Questions

1. Why is the approach of first imputing and then forecasting necessary in VSF? How does this differ from traditional time series forecasting?
2. How does the proposed denoising method for decomposing time series data into invariant and variant patterns differ from existing techniques? What evidence supports its effectiveness?
3. Has the paper considered comparing the proposed method with existing techniques specifically designed for incomplete time series data?
4. Why is meta-learning applied to address intra-series shift? Could this be a misapplication of the method, and would alternative approaches be more suitable?

### Rating

3

### Confidence

4

**********
