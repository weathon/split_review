# SSNet: Skip and Split MLP Network for Long-Term  Series Forecasting

- Decision: Reject
- Scores: 8, 1, 1, 10

## Abstract
Time series forecasting is critical across various domains, 
   including energy, transportation, weather prediction, and healthcare. 
   Although recent advances using CNNs, RNNs, and Transformer-based models have shown promise, 
   these approaches often suffer from architectural complexity and low computational efficiency. 
   MLP-based networks offer better computational efficiency, 
   and some frequency-domain MLP models have demonstrated the ability to handle periodic time series data. 
   However, standard MLP-based methods still struggle to directly model periodic and temporal dependencies in the time domain, 
   which are essential for accurate time series forecasting. 
   To address these challenges, we propose the Skip and Split MLP Network (SSNet), 
   featuring innovative Skip-MLP and Split-MLP components that enable MLP models to directly capture periodicity and temporal dependencies in the time domain. 
   SSNet requires fewer parameters than traditional MLP-based architectures, 
   improving computational efficiency. 
   Empirical results on multiple real-world long-term forecasting datasets demonstrate that SSNet significantly outperforms state-of-the-art models, 
   delivering better performance with fewer parameters. Notably, even a single Skip-MLP unit matches the performance of high-performing models like PatchTST.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces the Skip and Split MLP Network (SSNet) for time series forecasting, which offers superior computational efficiency compared to existing models. SSNet’s Skip-MLP and Split-MLP components effectively capture both temporal and periodic patterns using much fewer parameters, outperforming SOTA transformer-based models on benchmark datasets. The paper highlights the efficiency and effectiveness of MLP-based methods over transformer-based approaches once again.

### Strengths
1. SSNet achieves SOTA forecasting performance with significantly fewer parameters, providing a promising direction for time series forecasting research.
2. The proposed Split-MLP and Skip-MLP components are well-suited to the characteristics of time series data.
3. The paper is easy to follow, and the experiments are extensively conducted.
4. The supplementary materials are well-prepared.

### Weaknesses
1. Although the authors provide the number of parameters to show efficiency, FLOPs are also an important factor. Please include FLOP measurements.
2. The results in Figures 6 and 7 are blurry and overlap, please revise them.
3. In the README, it is stated that "A NVIDIA graphics card with 80GB of VRAM is required," but as shown in Figure 6, GPU usage is less than 10GB. Please explain it and provide more explanation in the README.

### Questions
1. K is an important hyper parameter in the model design and feature extraction, how does it affect the model performance?
2. Please address the concerns raised by W1 and W3.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper focuses on long-range time series forecasting, and introduces a novel MLP-based network, comprising Skip-MLP and Split-MLP, combined into SSNet. The author conducted experiments on 7 datasets to compare the performance of SSNet with past methods.

### Strengths
1. The innovativeness of the model is good. 

2. The overall presentation of the article is very clear.

### Weaknesses
1. The experimental setup has some issues. The article used different look-back lengths for the models being compared, which is evidently unreasonable as the input length variable was not controlled. Although it must be acknowledged that different models may exhibit varying performance at different look-back lengths, a reasonable approach would be to evaluate all models using both long and short look-back lengths to compare their performance. Therefore, the results under the current setup are difficult to be convincing.

2. The author seems to have a bias towards the models being compared. I noticed that the author focused on TimeMixer and PDF but did not pay attention to contemporaneous models like iTransformer[1], FITS[2], ModernTCN[3], or even earlier methods such as Koopa[4], CrossGNN[5], FourierGNN[6], WITRAN[7], and Basisformer[8]. The author should comprehensively compare all of them, as I believe this would enhance the quality of the article.

[1] Liu, Y., Hu, T., Zhang, H., Wu, H., Wang, S., Ma, L., & Long, M. (2024). iTransformer: Inverted Transformers Are Effective for Time Series Forecasting. In The Twelfth International Conference on Learning Representations.

[2] Xu, Z., Zeng, A., & Xu, Q. (2024). FITS: Modeling Time Series with $10 k $ Parameters. In The Twelfth International Conference on Learning Representations.

[3] Luo, D., & Wang, X. (2024). Moderntcn: A modern pure convolution structure for general time series analysis. In The Twelfth International Conference on Learning Representations.

[4] Liu, Y., Li, C., Wang, J., & Long, M. (2024). Koopa: Learning non-stationary time series dynamics with koopman predictors. In Thirty-seventh Conference on Neural Information Processing Systems.

[5] Huang, Q., Shen, L., Zhang, R., Ding, S., Wang, B., Zhou, Z., & Wang, Y. CrossGNN: Confronting Noisy Multivariate Time Series Via Cross Interaction Refinement. In Thirty-seventh Conference on Neural Information Processing Systems.

[6] Yi, K., Zhang, Q., Fan, W., He, H., Hu, L., Wang, P., ... & Niu, Z. FourierGNN: Rethinking Multivariate Time Series Forecasting from a Pure Graph Perspective. In Thirty-seventh Conference on Neural Information Processing Systems.

[7] Jia, Y., Lin, Y., Hao, X., Lin, Y., Guo, S., & Wan, H. (2023). WITRAN: Water-wave Information Transmission and Recurrent Acceleration Network for Long-range Time Series Forecasting. In Thirty-seventh Conference on Neural Information Processing Systems.

[8] Ni, Z., Yu, H., Liu, S., Li, J., & Lin, W. (2023). BasisFormer: Attention-based Time Series Forecasting with Learnable and Interpretable Basis. In Thirty-seventh Conference on Neural Information Processing Systems.

3. It seems that the author has not described the details of the parameter search space for the compared baselines. Has the author validated the baseline methods by searching for the best parameters on the validation set? If this has been done, please disclose the results of the parameter search. If this work has not been carried out, it would not provide strong evidence that SSNet outperforms the compared methods. Because the experimental platform can also affect the accuracy of model training, in other words, the optimal parameters on different platforms should be different. To make a fair comparison of their performance, a sufficiently comprehensive parameter search would be conducted on the same platform for all methods within the same search space to ensure they all achieve the best performance. Otherwise, it is difficult to eliminate the significant impact of the experimental platform and parameter selection on the experimental conclusions. Therefore, the experimental conclusions presented in this paper are difficult to be convincing.

### Questions
1. Can the author provide details about the search space and make them public?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes a novel architecture with Skip-MLP and Split-MLP components that effectively captures periodic and temporal relationships while maintaining computational efficiency. Through extensive evaluation of real-world datasets, this paper demonstrates that SSNet outperforms several models with fewer parameters, with even a single Skip-MLP unit achieving comparable performance to complex models like PatchTST.

### Strengths
1. this paper studies a popular problem, i.e., time series forecasting.

2. this paper revised MLP architectures and applied them for forecasting, which seems interesting.

### Weaknesses
1. This paper is not well-motivated. This paper mentioned that "MLP-based networks offer better computational efficiency but struggle
to effectively model periodic and temporal relationships, which are essential for accurate time series forecasting". However, several models that utilized frequency-domain MLPs can effectively capture the frequency components, such as [1-2]. These methods can better capture the periodic and temporal patterns.

2. The experimental results are less convincing. The experiments are lack of comparisons with other MLP time series forecasting models and SOTA transformer models [1-3]. Thus, the experimental results are not enough.


[1] FITS: Modeling Time Series with 10k Parameters.

[2] Frequency-domain MLPs are More Effective Learners in Time Series Forecasting.

[3] iTransformer: Inverted Transformers Are Effective for Time Series Forecasting.

### Questions
Can the author revise or improve the motivations or better explain it?

Can more experiments be added?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
In this paper, the authors propose a novel network structure, the Skip and Split MLP Network (SSNet), which integrates Skip-MLP and Split-MLP components. The SSNet model outperforms general MLP-based, CNN-based, and Transformer-based models in terms of parameter efficiency, computation time, and accuracy. The authors clearly explain the decomposition and prediction challenges in time series forecasting, providing detailed mathematical explanations for Skip-MLP and Split-MLP calculations.

The paper introduces the SS-MLP block, consisting of two Skip-MLP layers and two Split-MLP layers. In the SSNet section, they describe the structure of the Auto-correlation Block, which is based on periodicity and strength, and then present the overall SSNet architecture, including the Auto-correlation Block, Skip-MLPs, and SS-MLPs.

The SSNet model is tested on seven datasets and compared with other MLP-based methods (TimeMixer, DLinear), Transformer-based methods (PatchTST, PDF, FEDformer), and CNN-based methods (FiLM, TimesNet, MICN). SSNet consistently ranks as the best or second-best in terms of MSE and MAE. Additionally, the model demonstrates significantly lower running times and GPU/memory usage compared to other methods.

### Strengths
1. The inclusion of clear visuals such as Figures 1, 3, 4, and 5 significantly aids in understanding the components of the model, including Skip-MLP, Split-MLP, and the overall structure of SSNet, SS-MLP Block, and the Auto-correlation Block.

2. The concise mathematical derivation of Skip-MLP and Split-MLP helps readers grasp the underlying mathematical framework of the proposed model.

3. The model was tested on multiple large-scale datasets and compared to several well-known deep learning models, offering substantial evidence of the model's strengths and performance.

4. Sufficient data on computational time and GPU usage is provided, demonstrating that the model achieves improved accuracy without requiring additional time or resources, making it highly efficient.

### Weaknesses
1. Please explain the reasoning behind this specific number of layers and whether they experimented with different configurations

2. Offer further explanations regarding the structure of Figure 5, provide a step-by-step explanation of the data flow through the SSNet architecture, including how the residual connections are incorporated.

3. Describe the specific type of linear projection used (e.g., fully connected layer) and explain why this particular approach was chosen for the output layer.

4. Provide a brief description of each dataset's domain and characteristics, and suggest including a sample visualization of the time series data from one or two representative datasets.

### Questions
I have just one question: Would changing the order of the Skip-MLP and Split-MLP in the SS-MLP block, or adding additional hidden layers, have any impact on the MSE or MAE?

### Soundness
4

### Presentation
4

### Contribution
4
