# FLDmamba:  Integrating Fourier and Laplace Transform Decomposition with Mamba for Enhanced Time Series Prediction

- Decision: Reject
- Scores: 6, 5, 6, 5, 8, 6

## Abstract
Time series prediction, a crucial task across various domains, faces significant challenges due to the inherent complexities of time series data, including non-stationarity, multi-scale periodicity, and transient dynamics, particularly when tackling long-term predictions. While Transformer-based architectures have shown promise, their quadratic complexity with sequence length hinders their efficiency for long-term predictions. Recent advancements in State-Space Models, such as Mamba, offer a more efficient alternative for long-term modeling, but they lack the capability to capture multi-scale periodicity and transient dynamics effectively. Meanwhile, they are susceptible to the data noise issue in time series. This paper proposes a novel framework, FLDmamba (Fourier and Laplace Transform Decomposition Mamba), addressing these limitations. FLDmamba leverages the strengths of both Fourier and Laplace transforms to effectively capture both multi-scale periodicity, transient dynamics within time series data, and improve the robustness of the model to the data noise issue. By integrating Fourier analysis into Mamba, FLDmamba enhances its ability to capture global-scale properties, such as multi-scale periodicity patterns, in the frequency domain. Meanwhile, the Fourier Transform aids in isolating underlying patterns or trends from noise in time series data by emphasizing key frequency components, thereby enabling the model to mitigate noise effects. Additionally, incorporating Laplace analysis into Mamba improves its capacity to capture local correlations between neighboring data points, leading to a more accurate representation of transient dynamics. Our extensive experiments demonstrate that FLDmamba achieves superior performance on time series prediction benchmarks, outperforming both Transformer-based and other Mamba-based architectures. This work offers a computationally efficient and effective solution for long-term time series prediction, paving the way for its application in real-world scenarios. To promote the reproducibility of our method, we have made both the code and data accessible via the following URL: \href{https://anonymous.4open.science/r/FLambas-AD7E/README.md}{https://anonymous.4open.science/r/FLDmamba}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes Fourier and Laplace Transform Decomposition Mamba for time series forecasting. There are three major innovations over the basic Mamba. First is using RBF kernel to  smooth the data. Second is selectively filtering \Delta with a Kernel using fourier transform. Third  is applying inverse Laplace transformation to obtain the final output. The proposed FLDmamba achieves SOTA result on a wide range of the datasets for long term time series forecasting.

### Strengths
The proposed model has outsanding emprical performance.

### Weaknesses
The improvement proposed in the paper are largely orthogonal to Mamba algorithm, which makes the story less coherent. For example, I think RBF kernel and inverse Laplace transformation are mostly agnostic of the model struce, and can be applied to other forecasting model such as MLP or transformer.

Page 6 line 270 says $\tilde{W}$ denotes the Fourier transform of the kernel $\tilde{K}$, but I don't see where the kernel $\tilde{K}$ is defined in the paper. Then in Algorithm 2, there is $\Delta'=FFT(\Delta)$, $\Delta_F=IFFT(\Delta')$. Doesn't this implies $\Delta=\Delta_F$, and therefore nothing is done?

### Questions
Page 6 line 270 says $\tilde{W}$ denotes the Fourier transform of the kernel $\tilde{K}$, but I don't see where the kernel $\tilde{K}$ is defined in the paper. Then in Algorithm 2, there is $\Delta' = FFT(\Delta)$, $\Delta_F = IFFT(\Delta')$. Doesn't this implies $\Delta=\Delta_F$, and therefore nothing is done?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces FLDmamba by incorporating Fourier and Laplace Transform Decomposition, effectively addressing three key challenges in time series tasks: **multi-scale periodicity**, **transient dynamics**, and **data noise**.

### Strengths
+ The writing is clear and effectively outlines three challenges while presenting corresponding strategies for their resolution. 
+ The authors enhance Mamba's performance on time series tasks by incorporating RBF, Fourier, and Laplace Transform Decomposition. 
+ Additionally, they conduct extensive experiments using popular benchmark datasets and compare their proposed model with state-of-the-art approaches to demonstrate its effectiveness.

### Weaknesses
 - The authors' characterization of **multi-scale periodicity**, **transient dynamics**, and **data noise** as challenges specific to the Mamba-based model is inappropriate. These three challenges are faced by all models, not just those based on Mamba. Furthermore, among the proposed improvements to address these challenges, only the FLDMAMBA module appears to be model-specific; the others seem to be model-agnostic. The paper lacks experiments demonstrating the integration of these strategies into other methods. Additionally, it is unclear whether the authors are making improvements to the Mamba architecture or proposing a collection of strategies to address these three challenges.
- The authors need to provide details on computational overhead. One motivation for introducing Mamba is its lower time complexity compared to Transformer models. However, on one hand, the authors employ parallel FMamba and Mamba modules, which significantly increase the model's parameters and computational overhead. On the other hand, it is uncertain whether FFT and IFFT will become computational bottlenecks, especially for datasets with a high number of channels, such as "electricity," which has 321 channels.
- RBF is a model-agnostic data preprocessing method. It is unclear whether its application would also be effective in other methods.
- In the FMamba module, the authors adopt the Fourier transform on the $\Delta$ to identify important frequency information and further capture multi-scale periodic patterns in time series data. Can the authors provide a more detailed explanation and analysis, including a visual representation of $\Delta A$ and $\Delta_F A$?
- This paper focuses on Mamba; therefore, the baselines in experimental section should include more Mamba-based methods. Currently, only S-Mamba is considered.
- There is a lack of discussion regarding related work on the application of Mamba in time series forecasting. The authors should address how their work differs from these existing methods.

### Questions
Please refer to my weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel framework for time series prediction, leveraging the backbone of Mamba and integrating the Fourier and Laplace Transform. The major contributions are summarized as follows: (i) the Mamba-based framework provides a more efficient inference compared to Transformer-based models; (ii) the integrated Fourier transform enables the framework to capture multi-scale periodicity and extract useful signals from noise, while the Laplace Transform allows the model to capture transient dynamics within time series. The experimental results demonstrate the superiority of the proposed approach over existing baselines.

### Strengths
1. The combination of Mamba with the Fourier and Laplace Transforms is innovative. The experimental results suggests the approach indeed captures more precise time series features than the existing methods.
2. The proposed FLDmamba effectively captures the multi-scale periodicity and transient dynamics within time series data. Somehow, it also shows a certain level of robustness in handling distribution shifts.
3. This paper is well-written. The experiments are well-designed and thoroughly discussed.

### Weaknesses
1. This paper claims that FLDmamba theoretically achieves faster inference than Transformer-based models, which could be partially demonstrated by the experiments on training time. However, there is no experiment to directly validate this claim. The paper should include a direct comparison of inference times, perhaps by measuring the time taken to predict a fixed number of time steps across different models. This would provide a more concrete validation of the claim regarding inference efficiency.
2. The discussions in ablation study are thorough, but the conclusion is a little confusing and inconsistent with the experimental results. Specifically, the paper should clarify the specific conditions under which each component of FLDmamba is most effective, rather than making a general claim about the overall effectiveness of the inverse Laplace Transform. The discussion should also address the observed inconsistencies, such as the performance of the variant without ILT on the PeMS08 dataset.

### Questions
1. Does other transforms in frequency domain provide similar benefits as the Fourier and Laplace Transform? Could you provide some insights into this?
2. How do the variants of FLDmamba in ablation study perform in capturing the multi-scale periodicity and transient dynamics in the experiments of the case study section?
3. Figure 1 suggests that FLDmamba is able to predict accurately when temporal dynamics change. Is it able to handle the problem of distribution shifts in time series? If so, please analyze which specific component(s) in FLDmamba contribute to this capability.
4. In Figure 3, distinct components of FLDmamba impact model performance  differently across datasets. Can you provide insights from data perspective into which features in time series may correlate with this impact? Are there limitations or scenarios that the components in FLDmamba may not generalize well to specific time series?
5. Lines 439-441 indicates the inverse Laplace Transform impact the most significantly on the overall effectiveness. Is this finding consistent across all datasets, particularly noticing that for PeMS08, the variant without ILT is not the least effective one among all the variants of FLDmamba?
6. Why do the MSE and MAE values in Figure 3 differ from those in Table 1 for the same length setting on the same dataset?
7. Figure 12 compares the training time between different models. Can you also provide the comparison of inference time as well?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces FLDMamba, a multi-variate time series prediction model.
The model focuses on (1) multi-resolution on the periodicity of input sequence, (2) Transient dynamics of the time series and (3) noise filtering in time series data.
The authors construct the FMamba-Mamba (FMM) layer as the foundational unit to build the FLDMamba model.
The authors conduct extensive experiments to show the effectiveness of the proposed model, model's capability on long-range prediction, and noise robustness.

### Strengths
- 1. I think the motivation of the paper is reasonable. Using the RBF kernel does seem to be a fair approach.
- 2. I also think the use of the FFT makes sense especially when dealing with the lead-lag relationships between variates. The convolution operation is able to reveal such information in the discrete data points.
- 3. The experiments contain most of the state-of-the-art time series prediction models I can think of.

### Weaknesses
 - 1. My biggest concern about this paper is their evaluation metric. I believe using R2 score or Pearson correlation is more suitable for the task. However, this paper only considers the MSE and MAE error, while the MSE and MAE seems to be lower than all other baselines, I still have some doubts on the models ability to capture informative time series patterns.
- 2. The long-term prediction part doesn't seem to be very informative. Beside the problem on MSE and MAE, the max look-back length is only set to 720, which most baselines are capable of handling. And the improvement is small in my opinion.

- I do consider the technical details of this paper is sound and informative, I would love to increase my ratings as long as the R2 score and Pearson correlation also reflects the effectiveness of their model.

### Questions
- 1. Are you able to report the R2 score or the Pearson correlation? I strongly believe this is an essential metric the author should provide when evaluating their model on time series prediction tasks.
- 2. What is the computational efficiency in terms of computational time? I know Mamba-based models are easy to compute, but do they also take shorter time to generate predictions?
- 3. What is the main point of the case study? I feel like the sample size of this case study is extremely small and is not enough to reflect the real situation.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents FLDmamba, a novel time series prediction framework combining Fourier and Laplace transformations with the Mamba architecture to improve accuracy and robustness for long-term predictions. The Fourier transform aims to capture multi-scale periodicity and reduce noise, while the Laplace transform enhances the model’s ability to capture transient dynamics. Through ablation studies and benchmark comparisons, FLDmamba demonstrates state-of-the-art performance on several time series prediction datasets. The authors also evaluate the model's robustness, efficiency, and sensitivity to hyperparameters, contributing to a well-rounded evaluation.

### Strengths
1. Innovative Framework: Integrating Fourier and Laplace transformations into the Mamba model is novel in the context of time series forecasting. This combination allows FLDmamba to address core challenges in time series data—multi-scale periodicity, noise reduction, and transient dynamics.

2. Solid Performance Gains: FLDmamba consistently outperforms other models on key benchmarks, particularly in scenarios involving noisy data or long lookback lengths, demonstrating that the model effectively generalizes across diverse datasets.

### Weaknesses
While this paper is generally strong, there are a few minor weaknesses that could be addressed to further strengthen the contribution:

1. Incomplete Justification for RBF Kernel: Although the RBF kernel is presented as an effective data-smoothing technique, its choice is not empirically validated. A comparison with other kernel functions or a focused ablation study would help verify this choice and ensure that RBF is the optimal choice.

2. Unclear Necessity of FFT-IFFT Sequence: The FMamba block employs an FFT followed by an IFFT without a clear explanation of any specific frequency-domain manipulations before reconstructing the signal in the time domain. If this process is meant to filter specific frequencies or reduce noise, the details of such operations should be specified. Otherwise, the sequence could appear redundant, as it may be feasible for the neural network to approximate frequency characteristics without explicitly embedding FFT.

3. Limited Explanation of Explicit Transformations: While the inclusion of Fourier and Laplace transforms is well-motivated theoretically, it remains unclear why these explicit transformations are necessary. Neural networks, particularly those with linear layers, can approximate operations like FFT. A clearer discussion on the unique advantages of explicitly integrating these transforms would strengthen the architectural justification.

4. Incomplete Complexity Analysis: The complexity analysis, which estimates FLDmamba’s time complexity as $𝑂(𝐵𝐿𝑉𝑁)$, does not fully account for the computational costs of FFT, IFFT, and inverse Laplace transforms. Each of these operations introduces additional costs (e.g., $O(BLNlogL)$ for FFT)) that may not scale efficiently for large datasets. This makes the current complexity analysis potentially optimistic, particularly given that working in the complex domain could introduce additional memory and processing overhead. Wall-clock inference times compared to baseline models would better validate FLDmamba's practical efficiency and help justify the complexity of the FFT and Laplace operations.

5. Incomplete Citation of S-Mamba: While S-Mamba is frequently referenced as a baseline, it lacks a formal citation in the main text. Adding this citation would improve the academic rigor and proper attribution within the paper.

6. Clarity of Figures: Some figures could benefit from clearer axis labels to improve interpretability. For example, in Figure 1, the y-axis label is ambiguous, and the x-axis label as “Time of Day” is potentially misleading since it exceeds 24 hours. Clarifying these points would improve the readability of the time series prediction results.

### Questions
1. Since both FFT and Discrete Cosine Transform (DCT) are effective for frequency-domain analysis, could the authors clarify why they selected FFT over DCT? DCT, for instance, has shown advantages in signal compression and noise reduction and might benefit time series forecasting by emphasizing low-frequency components. Further insight on this choice would help clarify the design decision.

3. Deep learning models with linear layers can often approximate linear transformations, including FFT. Could the authors elaborate on the specific necessity of explicitly embedding Fourier and Laplace transforms rather than relying on the model's intrinsic capacity to learn these linear relationships? This would clarify whether these transformations improve interpretability, robustness, or training efficiency in ways that the network alone might not achieve.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes FLDmamba, a novel framework that integrates Fourier and Laplace Transform Decomposition with the Mamba State-Space Model (SSM) to enhance long-term time series prediction. The authors identify key challenges in existing models, particularly in capturing multi-scale periodicity, transient dynamics, and handling data noise. Extensive experiments on nine real-world datasets demonstrate that FLDmamba outperforms state-of-the-art Transformer-based and Mamba-based architectures

### Strengths
1. The paper introduces a novel integration of Fourier and Laplace transforms into the Mamba framework, addressing the limitations of previous SSMs in capturing multi-scale periodicity and transient dynamics.
2. The paper includes thorough experiments on nine diverse real-world datasets, covering various domains. The results consistently show that FLDmamba achieves superior performance compared to strong baselines.
3. The model's robustness to data noise is evaluated, showing that FLDmamba maintains high performance even under increased noise levels, outperforming other methods like S-Mamba and iTransformer. Detailed ablation studies are conducted to isolate and demonstrate the contribution of each component in the FLDmamba framework.

### Weaknesses
1. While the paper explains the intuition behind using the Laplace transform to capture transient dynamics, it lacks a deeper theoretical exploration of how exactly the inverse Laplace transform contributes to performance improvements in the context of the model. Specifically, the paper does not provide a rigorous mathematical justification for why the chosen parameterization of the inverse Laplace transform is optimal or even appropriate for capturing the transient dynamics in time series data. The connection between the mathematical properties of the inverse Laplace transform and the specific implementation within the model is not clearly established, leaving a gap in the theoretical understanding of the proposed method.
2. The experimental comparison focuses primarily on Transformer-based models and Mamba-based methods. Inclusion of more diverse SSM-based baselines, such as those based on S4 or other recent advances, would strengthen the evaluation. The current set of baselines does not fully explore the landscape of state-space models, potentially overlooking relevant comparisons that could highlight the specific advantages and disadvantages of the proposed FLDmamba framework. A more comprehensive comparison with other SSM architectures would provide a more robust assessment of the model's performance.

### Questions
1. Can you provide more details on how the inverse Laplace transform is computed in practice within your framework? Given that inverse Laplace transforms can be numerically challenging, how do you ensure stability and efficiency in this component?
2. Have you explored using alternative kernel functions beyond the RBF kernel for data smoothing? If so, how do they compare in terms of performance and computational cost?

### Soundness
3

### Presentation
3

### Contribution
3
