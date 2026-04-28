# CPDD: Generalized Compressed Representation for Multivariate Long-term Time Series Generation

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 3, 5

## Abstract
The generation of time series has increasingly wide applications in many fields, such as electricity and energy. Generating realistic multivariate long time series is a crucial step towards making time series generative models practical, with the challenge being the balance between long-term dependencies and short-term feature learning. Towards this end, we propose a novel time series generative model named Compressed Patch Denoising Diffusion-model (CPDD). Concretely, CPDD first employs the Time-series Patch Compressed (TPC) module based on the patch mode decomposition method to obtain the latent encoding of multi-scale feature fusion. Subsequently, it utilizes a diffusion-based model to learn the latent distribution and decode the resulting samples, thereby achieving high-quality multivariate long-time series generation. Through extensive experiments, results show that CPDD achieves state-of-the-art performance in the generation task of multivariate long-time series. Furthermore, TPC also exhibits remarkable efficiency in terms of robustness and generalization in time series reconstruction.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to address the challenge of balancing the long-term dependencies and short-term features in time series generation and proposes a novel model named Compressed Patch Denoising Diffusion-model (CPDD). The proposed approach first employs a Time-series Patch Compression (TPC) module to decompose time series patches into mode functions, effectively capturing latent representations of both long-term and short-term features. Afterward, a diffusion-based model with a CNN backbone is designed to learn the latent distributions and generate multivariate long-term time series. Experimental results demonstrate that CPDD achieves the SOTA performance in time series generation. Furthermore,  the robustness and generalization capabilities of the TPC module are rigorously verified.

### Strengths
- The generative modeling approach of decomposing time series patches into mode functions presented in this paper is novel and well-positioned in the literature on time series generation, to the best of my knowledge.
- The introduction of the Time-series Patch Compression (TPC) module marks a notable innovation in time series modeling. This module provides a robust alternative to the commonly used autoencoder-based compression methods and trend-seasonality decomposition techniques. The exploration of its robustness and generalization is particularly noteworthy
- Figures 1 and 2 provide a clear illustration of the proposed approach, making the core designs easier to understand.

### Weaknesses
 - This paper identifies high computational demands as a limitation of existing methods, but the proposed approach also employs a computationally intensive Transformer-based architecture. Therefore, a detailed analysis of the computational complexity of the proposed CPDD is essential. The paper should include a breakdown of the computational cost associated with each module, such as the TPC and the diffusion model, and compare these costs to those of baseline models. This analysis should consider both training and inference phases, offering a clear picture of the practical trade-offs.
- The visualizations in this paper are generally of high quality. Unifying the font size in Figure 4, especially on the left-side module, to match that of other figures would improve visual consistency and readability.
- CPDD divides the entire time series into N patches, which might pose a risk of disrupting critical temporal patterns at the boundaries of these patches. The paper should include a discussion on how the model handles potential discontinuities or artifacts introduced by patch boundaries, and how this might affect the model's ability to accurately capture and reproduce these dynamics. The use of overlapping patches should be explicitly mentioned and its impact on performance should be analyzed.


### Questions
1. CPDD divides the entire time series into N patches, which might pose a risk of disrupting critical temporal patterns at the boundaries of these patches. Could this potentially affect the model's ability to accurately capture and reproduce these dynamics?
2. How does the patch length N impact the model performance? Is there an optimal range of N?
3. Can you provide a detailed comparison of the computational complexity between CPDD and baselines? For example, a table comparing their training and inference time.

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
This paper presents a diffusion-based method for time series generation that integrates a patch compression module with trend-seasonal decomposition to enhance generation performance.

### Strengths
1. This paper effectively leverages a patch compression method to capture complex long-term and short-term dependencies in time series data.

2. The authors employ trend-seasonal decomposition to facilitate the diffusion model's ability to learn complex distribution shifts.

### Weaknesses
1. The evaluation experiments presented in the paper are insufficient to convincingly demonstrate the effectiveness of the proposed method. Specifically, more common used evaluation metrics need to be added (like MSE, MAE, .etc), and the selection of baseline methods (both the diffusion-based methods and the transformer-based methods should be compared) and datasets is not comprehensive enough to provide a robust comparison.

2. The formulation of the paper needs significant improvement; the organization and clarity of the text make it difficult to identify the key ideas and contributions. 

3. The integration of the proposed patch compression method with seasonal-trend decomposition seems to offer limited novelty, as this combination may be viewed as a relatively minor contribution to the existing body of work in this area.

4. While the paper employs a transformer as the encoder within the diffusion model, it is essential to consider the associated computational costs when making comparisons with baseline methods.

### Questions
1. How are the short-term and long-term modes decomposed from the patches?

2. What is the rationale for employing the transformer as the encoder of the diffusion model instead of using the transformer directly?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces CPDD, a method for time series generation, which addresses challenges in balance between long-term dependencies and short-term feature learning. It utilizes a patch Compressed module based on the patch mode decomposition method to obtain the latent encoding of multi-scale feature of time series. It utilizes a diffusion-based model to learn the latent distribution and decode the resulting samples, which achieves state-of-the-art performance in the generation task of multivariate long-time series with efficiency and robustness.

### Strengths
1. Methodology: CPDD is a patch compression method to capture complex long-term and short-term dependencies more effectively with the diffusion model for high-quality samples generation.
2. Empirical Results: The numerical results presented in the paper are compelling, showing significant improvements over competing 
approaches in terms of generated time series quality. This empirical evidence supports the effectiveness of the proposed method.
3. Proofs: The author gives a detailed formal proof of the effectiveness of DSConv blocks' structural regularization.

### Weaknesses
1.  The problem that the article aims to address is confusing; what does "balance between long-term dependencies and short-term feature learning" mean?
2. In line 25 of the article, the author mentions "efficiency." How is this demonstrated in the article? Please compare the model's memory usage and inference time.
3. In the embedding space shown in Figure 1, what do "distant" and "nearby" mean? This is quite confusing.
4. The entire CPDD process is quite confusing. please provide a specific implementation process or corresponding pseudocode?
5. In lines 340-341 of the article, the author mentions "Z: latent representation obtained from the TPC Encoder during training." Then why is there no loss term for the TPC Encoder/Decoder in Equation 16? Is CPDD an end-to-end or a two-stage process? Please provide a detailed explanation.
6. What is “L_{AFC}" in Equation 16? Is there any difference between "L_{AFC}" and "L_{ACF}"?
7. The writing issues in the article are evident, with many sentences being difficult to understand, and the challenge that article aims to address is not clearly defined.

### Questions
Please refer to the Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper analyses the challenges faced in the time series generation task, including the limited ability of the proposed approach to model long-term dependencies due to cumulative errors, the high computational complexity and time overhead due to the attention mechanism, and the inability to capture both long-term global dependencies and short-term local features. Inspired by the spatial distribution of latent variables modelled by LDM, in order to achieve a balance between long-term dependencies and short-run feature learning in time-series generation tasks, it proposes the Compressed Patch Denoising Diffusion-model (CPDD), where Time-series Patch Compressed (TPC) is designed based on the block pattern decomposition method to obtain multi-scale latent representations. And the diffusion model achieves high quality multivariate long time series generation after decoding by modelling the probability distribution of potential representations.

### Strengths
The main contribution of this paper is to propose a technique that can efficiently compress and represent multivariate long-term time series data by decomposing the patches into pattern functions through which long-term dependencies and short-term features are consistently represented. Specifically, the TPC module learns generic combinations of pattern functions from patches to accommodate various patterns and enables a generic compressed representation of time series data.

### Weaknesses
This paper is dedicated to present a technique that can efficiently compress and model multivariate long-term time series data, which has important real-world implications. The main concerns are as follows:

1.	As a model ‘designed for multivariate long-term time series’, the main innovative structures proposed by CPDD, DSConv and TPC, do not have a structure or design aimed at establishing explicit cross-channel connectivity. While the DSConv module uses point-wise convolutions, it's unclear if this is sufficient to capture complex inter-dependencies across a large number of channels, such as those found in the ECL dataset (321 channels) or the Traffic dataset (862 channels). The paper does not provide a clear explanation of how the single-channel convolutions and point-wise operations within DSConv effectively model these intricate cross-channel relationships. Advances in multivariate prediction methods (iTransformer[1], SAMformer[2]) have shown that proper integration of channel management strategies in time series backbones is crucial for discovering univariate dynamics and cross-variate correlations.

2.	The lack of advanced baselines leads to the inability to validate the competitiveness of the proposed CPDD. Specifically, only three baselines based on Diffusion are shown in Table 1, and among them, TimeGAN and TimeVAE are published in 2021 and 2019, respectively. The introduction of a wider range of Baselines to compare the performance of the proposed models is expected to be complemented to fully validate the effectiveness of the proposed methods. The referenced baselines can be divided into 4 parts: 1) Models based on pre-trained LLM alignment to TS, e.g. TimeLLM[3]; 2) Pre-trained foundation models on unified time series datasets from multiple domains, e.g. Timer[4], UniTime[5]; 3) Proprietary models trained and tested on specific datasets, e.g. PatchTST[6]; 4) Recent Diffusion-based temporal probabilistic prediction models, e.g. Diffuison-TS[7], mr-Diff[8]. CCPD is expected to be compared with at least one competitive model in each prediction paradigm to demonstrate the soundness of the model design. In addition, we would like to introduce more benchmarks, such as ECL and Traffic datasets with a large number of channel counts, which we believe will help to validate the promising real-world applications of the proposed models. The current baselines do not adequately cover the spectrum of available methods, particularly those designed for long-term time series forecasting, which is a critical omission given the paper's focus.

3.	The design of the ablation experiments in this paper is deficient. In addition to DSConv and TPC, CPDD uses other strategies such as Patch Embed and Trend-seasonal Decomposition, yet the ablation experiments presented in Table 2 do not include these structural designs. This raises our concern about the validity of DSConv and TPC. The absence of ablation studies for patch embedding and trend-seasonal decomposition makes it difficult to ascertain the individual contribution of each component to the overall performance of the model. Without these experiments, it is unclear whether the reported results are genuinely due to the proposed DSConv and TPC modules or other architectural choices.

### Questions
1.	The results of Baseline presented in Table 1 are inconsistent with the results presented in the original paper, e.g., the Discriminative Score of the Diffusion-TS model under the Sines dataset in Table 1 is 0.326, whereas it is reported as 0.006 in the original paper.In fact, the results of all Baselines in Table 1 are in significant differences. In addition, Table 1 only shows some of the metrics on the performance of time series generation, and the results of the proposed method on both Context-FID Score and Correlational Score are missing. In addition, traditional metrics for time series forecasting, such as MSE, MAE, CRPS, etc., are missing from Table 1, which results in the reader not getting a full picture of the potential limitations of CPDD.

2.	In Table 2, in the Predictive Score metric, the model with DSConv removed achieves better performance in the Sines dataset, and the model with TPC removed exhibits the best performance in the Energy dataset. The results of the ablation experiments are puzzling, which may shake the rationality of the structural design of DSConv and TPC.

### Soundness
2

### Presentation
3

### Contribution
2
