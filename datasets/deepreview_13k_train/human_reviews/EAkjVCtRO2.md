# Variational quantization for state space models

- Decision: Reject
- Scores: 6, 6, 6

## Abstract
Forecasting tasks using large datasets gathering thousands of heterogeneous time series is a crucial statistical problem in numerous sectors. The main challenge is to model a rich variety of time series, leverage any available external signals and provide sharp predictions with statistical guarantees. In this work, we propose a new forecasting model that combines discrete state space hidden Markov models with recent neural network architectures and training procedures inspired by vector quantized variational autoencoders. We introduce a variational discrete posterior distribution of the latent states given the observations and a two-stage training procedure to alternatively train the parameters of the latent states and of the emission distributions. By learning a collection of emission laws and temporarily activating them depending on the hidden process dynamics, the proposed method allows to explore large datasets and leverage available external signals. We assess the performance of the proposed method using several datasets and show that it outperforms other state-of-the-art solutions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present a new algorithm for time-series prediction based on VQ-VAEs and RNNs, with separate emission models for each quantized hidden state. The authors evaluate their algorithm on a number of datasets, showing comparable results with SOTA algorithms.

### Strengths
* The authors evaluated their algorithm against multiple other algorithms on multiple datasets, with multi-seed comparison + grid search.
* As far as I am aware, combining VQ-VAEs and RNNs in this specific way (latent-conditioned observation model) has not been explored before.

### Weaknesses
 * While the emprical results are nice, it would further strengthen the paper if the authors could perform ablation experiments to uncover/provide a better intuition about why their algorithm performs well against others.

 * The author's new algorithm performs almost similarly to previous SOTA Transformer-based model PatchTST/64. However, it's unclear from my first reading why one would prefer one over the other. Is it easier to train/better runtime etc.?
* It's nice that the authors performed a grid search over learning rates and batch size for the other algorithms. I think the paper would be further strengthened if the authors conducted a hyperparameter search also over network size where it make sense (similar to the grid search that the authors performed over hidden size for their network)?

### Questions
* The author's new algorithm performs almost similarly to previous SOTA Transformer-based model PatchTST/64. However, it's unclear from my first reading why one would prefer one over the other. Is it easier to train/better runtime etc.?
* It's nice that the authors performed a grid search over learning rates and batch size for the other algorithms. I think the paper would be further strengthened if the authors conducted a hyperparameter search also over network size where it make sense (similar to the grid search that the authors performed over hidden size for their network)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a forecasting model that combines discrete state space hidden Markov models with recurrent neural networks. The model is trained in a similar way as VQ-VAE. Experiments on several datasets show that the proposed method outperforms other SOTA methods.

### Strengths
(1) Introducing finite state HMM for forecasting is interesting. 

(2) The formulation of the model and the learning method is sound. 

(3) The experiment results are good.

### Weaknesses
 (1) The two-stage training appears unnecessary in the context of time series. It may lead to sub-optimal results. The alternating training of emission and prior models, while potentially simplifying the optimization, could prevent the model from converging to a globally optimal solution. Specifically, the emission model might overfit to the current state of the prior, and vice-versa, without a joint optimization that allows for a more holistic view of the latent space.

 (2) More details should be provided on training the model with discrete latents in the VAE framework, i.e., how the discreteness is handled. The paper lacks specifics on how the discrete latent variables are incorporated into the backpropagation process. It is unclear whether techniques like straight-through estimators or Gumbel-Softmax are used, and how these choices impact the training dynamics and the quality of the learned representations. The absence of these details makes it difficult to reproduce the results and assess the robustness of the method.

 (3) There is only one baseline model based on Transformer. I suspect there are many variants for forecasting. The comparison to only one Transformer-based baseline is insufficient to demonstrate the superiority of the proposed method. There are numerous Transformer architectures and training strategies tailored for time series forecasting, and the paper should include a more comprehensive comparison to establish the true effectiveness of the proposed method.

### Questions
(1) How well does your method work on long context forecasting problem? 

(2) Do you employ straight-through trick or Gumbel trick in training your model?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new forecasting method by combining hidden Markov models and recurrent neural networks. The training procedure is inspired by vector quantized variational autoencoders, including the latent space and the emission laws parts. This method is computationally efficient and outperforms the SOTA baseline methods.

### Strengths
- The presentation of this paper is good. The authors show the comprehensive details of training and network architectures.

- The experiments and evaluation are convincing. The authors test on multiple stationary and non-stationary datasets.

### Weaknesses
 The writing of this paper can be improved. On Page 2, there is a relatively large blank space, which can be optimized. Also, there are many typos and grammatical issues in this paper. Some of the issues are listed below.
- On page 6, Section 3.1.3, “...where T stand for…”, “stand” should be “stands”.
- On Page 8, in the caption of Table 1, “...their associated MASE…”, “MASE” should be “MASEs”. 
- On Page 8, Section 3.2.2, the second equation should be MAE.
- On Page 8, Section 3.2.3, “the accuracy of our model reaches state-of-the-art standards and provide uncertainty quantification.”, the subject of "provide" is not the accuracy.

### Questions
In Figure 1, for Hidden States Trajectory, e.g., $\hat{x}_{t+1}^i=2$, are those “2,2,1,1,3,...,3” fixed or flexible to adjust in your implementation?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
