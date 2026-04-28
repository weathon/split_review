# DiffImp: Efficient Diffusion Model for Probabilistic Time Series Imputation with Bidirectional Mamba Backbone

- Decision: Reject
- Avg Score: 5.40
- Scores: 5, 3, 3, 8, 8

## Abstract
Probabilistic time series imputation has been widely applied in real-world scenarios due to its ability to estimate uncertainty of imputation results. Meanwhile, denoising diffusion probabilistic models (DDPMs) have achieved great success in probabilistic time series imputation tasks with its power to model complex distributions. However, current DDPM-based probabilistic time series imputation methodologies are confronted with two types of challenges: 1)~\textit{~The backbone modules of the denoising parts are not capable of achieving sequence modeling with low time complexity.} 2)~\textit{The architecture of denoising modules can not handle the inter-variable and bidirectional dependencies in the time series imputation problem effectively.} To address the first challenge, we integrate the computational efficient state space model, namely Mamba, as the backbone denosing module for DDPMs. To tackle the second challenge, we carefully devise several SSM-based blocks for bidirectional modeling and inter-variable relation understanding. Experimental results demonstrate that our approach can achieve state-of-the-art time series imputation results on multiple datasets, different missing scenarios and missing ratios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors investigate the problem of time series imputation. Since the authors find that the DDPM-based models are usually not capable of achieving sequence modeling with low time complexity and cannot handle the inter-variables and temporal dependence. The authors integrate Mamba and develop the bidirectional model for time series imputation and forecasting. The authors evaluate the proposed method on several datasets and achieve good performance.

### Strengths
N.A.

### Weaknesses
1.	The contribution is limited. This paper looks like a combination of the diffusion model and Mamba. Specifically, the advantage of low time complexity comes from Mamba, and the technique of changing the SSM-based block to a bidirectional one is not very new. A similar idea has been used in bi-LSTM. The core innovation seems to stem from the application of Mamba to this specific problem, but the underlying methodology lacks significant novelty. The bidirectional approach, while potentially beneficial, is not a groundbreaking contribution in the context of sequence modeling.
2.	In addition, this article mainly solves the imputation problem, but the author considers time series forecasting, which makes the whole work seem to be pieced together. The paper does not adequately address the distinct challenges of forecasting, such as handling non-stationarity and periodicity, which require specialized techniques beyond basic imputation. The inclusion of forecasting feels like an afterthought, diluting the focus on the core imputation task.
3.	For fair comparison, authors should consider common imputation benchmarks such as the healthcare dataset in PhysioNet Challenge 2012 and air quality dataset. The current evaluation lacks breadth and does not establish the method's performance on standard datasets used in the time series imputation community. This makes it difficult to assess the true impact and generalizability of the proposed approach.
4.	Although the author mainly emphasizes that this method is better than other methods based on the diffusion model, this is not enough. The author should consider more time series imputation methods such as [1,2,3,4]. The comparison is too narrowly focused on diffusion-based models, neglecting other established imputation techniques. A more comprehensive comparison is needed to demonstrate the method's superiority over a wider range of alternatives.

### Questions
N.A.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a time series imputation method using Mamba state space model as the backbone of diffusion model. The SSM-based blocks aim to improve inter-variable and bidirectional dependency modeling. Experimental results show this approach achieves state-of-the-art performance across multiple datasets and varying missing scenarios and ratios.

### Strengths
1) The proposed method focuses on modeling channel dependencies in time series and the the backbone selection in diffusion models. This is a novel and interesting idea.
2) The conditional diffusion model should allow exploitation of useful information in the data for accurate reconstruction. This is a strength.
3) There are good experimental evaluations and comparisons presented in the paper.

### Weaknesses
1) The main motivation of model compatibility in diffusion-based imputation is not well-stated. Seems like authors would investigate which backbone is more suitable for diffusion model. It does not clear what certain limitation in using other models as the backbone, since CNN, Transformer, and SSM are channel independent and unidirectional. 
2) Authors claim the proposed method is channel-dependent and has low complexity. But it seems like using SSM in a different way, i.e., modeling across channel correlation. I do not agree this point can be stated as a drawback. If capturing inter-channel relationships is one of the key motivations for this paper, I would like to know why these relationships are essential for the imputation task and what issues might arise from ignoring them. But, this discussion is missing from the paper.
3) In the original SSSD paper, ECG data was also used for experiments, and the model was evaluated based on imputation accuracy and visualization. The ECG experiments were significant in the SSSD paper, yet it appears the authors did not include this experiment in their current paper. Given that the authors replicated other experiments from the SSSD paper, omitting this key experiment seems unusual. Without it, the authors only tested their method on two datasets for the imputation task. Including additional datasets could enhance the reliability of the results.
4) Have the authors tried other approaches for modeling channel-wise dependencies? As noted in the paper, there is no clear order among channels in multivariate time series, so using an order-agnostic attention mechanism for inter-channel relationships is intuitive. However, the motivation for using the Mamba model to capture inter-channel relationships is unclear, as state space models typically assume a temporal order in the data. Could the authors provide further explanation to clarify the rationale behind the channel Mamba block? Additionally, an ablation study on channel modeling would be beneficial.

### Questions
Please refer to the weakness. Here my main concern is with the motivation of this paper. It appears to be an exploratory study investigating a good model combination without clearly defining a technical, theoretical, or practical research question. Vanilla CNN, Transformer, and SSM are just model architectures; using them in an appropriate way does not, in itself, demonstrate significance. Overall, the contribution of this paper is limited, and a more comprehensive literature review and clearer positioning within the research field are needed.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Probabilistic time series imputation, capable of estimating imputation uncertainty, is widely used in real-world applications. Denoising diffusion probabilistic models excel in this task due to their ability to model complex distributions. However, current DDPM-based methods face challenges in achieving low time complexity for sequence modeling and effectively handling inter-variable and bidirectional dependencies. To overcome these, the authors integrate the efficient state space model Mamba as the backbone denoising module and design SSM-based blocks for bidirectional modeling and inter-variable relation understanding. Experimental results show that the approach achieves state-of-the-art time series imputation results across multiple datasets, missing scenarios, and missing ratios.

### Strengths
S1. Time series imputation is an important and widely studied problem.

S2. Diffusion model and Mamba are popular models recently.

S3. Complexity analysis is provided for the model.

### Weaknesses
W1. As discussed in Section 1, the main contribution is proposing a diffusion-based framework for time series imputation, by integrating Mamba-based blocks into diffusion models. However, diffusion models have been proved to be effective in time series imputation, and Mamba is also an existing technique. Modeling bidirectional dependencies and channel dependencies are common techniques to capture characteristics of time series data. Therefore, the novelty and contributions are limited.

W2. There is no theoretical result to support the proposed techniques.

W3. It is unbelievable that the time cost is totally ignored in experiment results, since the main contribution claimed by authors is that the linear complexity of proposed models.

W4. Only synthetic missing values are considered in experiments. It is suggested to use real-world incomplete datasets to demonstrate the effectiveness and efficiency of proposed methods.

W5. 70%, 80%, 90% missing values are injected into the MuJoCo dataset, and 10%, 30%, 50% missing values are considered into the Electricity dataset. It is wondered why different missing rates are considered in different datasets, why not consider 10%, 30%, 50%, 70%, 80%, 90% for them consistently.

W6. Since all the imputation baselines can impute incomplete time series, it is suggested to consider the comparison with them in all datasets, instead of using a subset of them in different datasets.

W7. Scalability experiments are necessary to demonstrate the linear complexity of this paper. Therefore, it is suggested to conduct this on additional large real-world datasets.

W8. There is no parameter sensitivity analysis in experiments, which is also suggested to show the stability of models and illustrate how to determine parameters.

W9. Although the source code has been released, there is not guideline for how to use the codes and how to get the experimental results for each table and figure, leading to the doubts of reproducibility.

### Questions
See W1-W9.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper provides a diffusion-based imputation method for time series data with missing values. The proposed method integrates Mamba-based models and diffusion-based models to achieve linear complexity for sequence data. The method is evaluated on two real-world datasets, Electricity and MuJoco, and the results show that it outperforms other state-of-the-art methods in terms of accuracy and efficiency.

### Strengths
1. This paper proposes an effective method for the time series data. The authors explores the availabity of using Mamba models as the diffusion backbones. The intergration of Mamba-based models and diffusion-based models provides linear complexity for sequence data and works fine on time series imputation tasks.
2. The improvements of deterministic results on high missing ratios are significant and the CRPS-sum improvement is also very significant compared with the other baselines, which means the proprosed method is effective in .
3. The running time of the proposed method is significantly lower than the other baselines and demonstrates the efficiency of the proposed method.
4. The bidirectional modeling, temporal attention module and channel modeling module are well designed and can effectively capture the temporal and channel dependencies of the time series data.
5. The authors provide detailed code for reproducible experiments.

### Weaknesses
1. In your paper, the experiments are conducted on the Electricity and MuJoco dataset. And as in [1], the experiments are conducted on AQI and healthcare dataset. The reason of choosing these datasets seems not clear.

2. for efficiency, the authors only compare the time complexity of the proposed method with the state-of-the-art methods.

3. The training manner of building missing values may need further expalaination

### Questions
For contents:

1. the authors state the mask strategy is utilized for training and in all there are three kinds of mask strategies. It is not clear that how you applied the mask. e.g. if there are no missing values in the original dataset, how to construct the mask for training? and if there are missing values in the original dataset, how to construct the mask for training? Now it seems that the mask is applied similarly to all kinds of datasets.

2. It seems that you designed two kinds of blocks for modeling channel dependency and sequential dependency, why you choose unidirectional channel modelling as shown in Fig 3c.

3. As shown in Fig 3d, it seems not clear how the temporal attention is utilized for the bidirectional modelling, besides, as in Fig 3c, the CMB module has the same sigmoid module as Fig 3d, is it also the temporal attention module and why you applied temporal attention module for channel modeling?

For experiments

1. Can the authors explain the choice of datasets and provide further experiments results and comparsions on AQI and healthcare dataset?

2. As it is an efficient time series diffusion model, can the authors provide more details, including training memory details or model parameters?

For details

4. as in table 1, the authors state that the SSM models is partial global dependency, why?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper provides an efficient method for time series imputation problems with a self-supervised training manner. The authors implemented the state-space model based Mamba architecture as the backbone for diffusion models. The authors validate their model on different real-world datasets.

### Strengths
1. This paper proposes an effective method for the time series data and the architecture details (bidirectional modeling and channel dependency) is well-suited for the time series data.
2. For probablistic time series imputation, the proposed method has a significant improvement in the CRPS-sum metric.

### Weaknesses
1. The implementation details of probabilistic time series imputation is not clearly explained in the paper.

2. The diffimp seems like a condition diffusion model but the conditions are not clearly explained in the paper.

3. While modeling inter-channel dependencies, it is clear that the dependency is related to the distance of the timestep, is diffimp capable of addressing the distance issue?

### Questions
1. You have mentioned your model is a probabilistic model but the analysis of probabilistic imputation is not clear. Can the authors provide more details about why your model is capable of achieving probabilistic impuation and the implementation of the probabilistic time series imputation?

2. Can the author provide more details about the choice of mask ratios among the datasets and how the inference time is calculated among different methods?

3. The model is a conditional dpm. Can the authors provide more details about the conditions and how the conditions are used in the model?

4. A straightforward conclusion is that different distance has different impacts on one timestamp. Can the authors provide more details about the inter-channel dependencies and how the model addresses the distance issue?

### Soundness
3

### Presentation
3

### Contribution
3
