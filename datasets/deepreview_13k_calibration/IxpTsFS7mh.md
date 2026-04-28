# VQ-TR: Vector Quantized Attention for Time Series Forecasting

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Probabilistic time series forecasting is a challenging problem due to the long sequences involved, the large number of samples needed for accurate probabilistic inference, and the need for real-time inference in many applications. These challenges necessitate methods that are not only accurate but computationally efficient. Unfortunately, most current state-of-the-art methods for time series forecasting are based on Transformers, which scale poorly due to quadratic complexity in sequence length, and are therefore needlessly computationally inefficient. Moreover, with a few exceptions, these methods have only been evaluated for non-probabilistic point estimation. In this work, we address these two shortcomings.
For the first, we introduce VQ-TR, which maps large sequences to a discrete set of latent representations as part of the Attention module. This not only allows us to attend over larger context windows with linear complexity in sequence length but also allows for effective regularization to avoid overfitting.
For the second, we provide what is to the best of our knowledge the first systematic comparison of modern Transformer-based time series forecasting methods for probabilistic forecasting. In this comparison, we find that VQ-TR performs better or comparably to all other methods while being computationally efficient.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces VQ-TR, combining vector quantization and the transformer architecture for time series forecasting. Specifically, vector quantization limits query vectors to be one of a fixed size codebook, which implies that any subsequent cross/self-attention computation scales with the codebook size instead of the context length. A masked attention decoder is used to 'unroll' the forecast. Apart from favorable computational properties, the method appears to clearly outperform the SoTA in transformer-based point and probabilistic forecasting.

### Strengths
The paper proposes a simple and highly practical tool for forecasting, and helps resolve an ongoing discussion in the forecasting community about the use of transformers by positing that a 'quantized' small-scale transformer already outperforms many of the current architectures in use.

The extensive experimental results posted are themselves of interest to the community and the work can potentially benefit other areas where transformers are often applied.

### Weaknesses
Motivation, exposition and the key idea follow closely from VQ-AR. This is however justified since the computational benefits to the transformer architecture are stronger. However, the contrast could be made clearer in the paper.

Also, key design decisions about experiments including number of layers, codebook size used to produce the tables are currently only available in the appendix. Please consider moving these important details forward.

Importantly, the experiment presentation is somewhat misleading. The main paper only compares against transformer baselines where the proposed method appears to categorically outperform the SoTA, however the non-transformer based baselines are moved to the appendix where results are mixed against non-transformer baselines; and less competitive than what the main paper Section 4.4 claims. The lack of a direct comparison against non-transformer methods in the main paper makes it difficult to assess the true practical value of the proposed method.

A last open point that should be addressed is the choice of the distribution output per dataset. How was this choice made for the baselines? The fact that -iqn and -t survive for VQ-TR in wiki and taxi respectively invites the question how these hyperparameters were selected.

### Questions
- Why does the model have higher runtime than TFT? Despite the comment that similar batch sizes were used, one would expect that the quantized architecture still outperforms TFT. 
- In the appendix the authors write: "Note that we can afford to use a longer context length of C = 20 × P for VQ-TR due to its memory efficiency, as noted in Figure 2." Was the context length fixed across models or did VQ-TR get a head start?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the challenges in probabilistic time series forecasting, which involve long sequences, and the need for a large number of samples for accurate inference. The paper highlights that current state-of-the-art methods based on Transformers are computationally inefficient due to their quadratic complexity in sequence length and primarily focus on non-probabilistic point estimation. To overcome these limitations, the paper introduces a novel transformer architecture called VQ-TR. VQ-TR utilizes a discrete set of latent representations in the Attention module, enabling linear scaling with the sequence length and providing effective regularization to prevent overfitting. The authors compare several Transformer-based time series forecasting methods for probabilistic forecasting, and VQ-TR demonstrates competitive performance in forecasting accuracy, computational efficiency, and memory usage.

### Strengths
The manuscript is well-written, with clear and easily understandable ideas. The paper offers a thorough evaluation, encompassing multiple baseline models across various benchmark datasets. It effectively illustrates the impact of the VQ module, not only in terms of performance enhancement but also in computational and memory efficiency.

### Weaknesses
The paper suffers from a significant lack of novelty, as its approach closely mirrors that of VQ-AR by Rasul et al. (2022). Essentially, the method merely replaces the RNN with a Transformer model. Given this redundant contribution, the paper falls short of meeting the standards expected for a conference like ICLR and might be better suited as a workshop paper.

Furthermore, in Figure 3, the analysis of how codebook size affects overall performance, fails to provide a clear conclusion or discernible trends regarding the impact of codebook size. It appears that determining the correct size is critical, and achieving the desired performance may require a careful HP tuning for a given dataset.

### Questions
How many attempts were done to find the right codebook size for the presented experiments? Adding the computing costs of tuning the codebook size, how well VQ-TR compares with methods that provides comparable performance, when trained using default settings?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript proposes a transformer architecture for time series forecasting, that uses vector quantization to scale the encoder sequence size, resulting in faster training time, less memory usage, and time series forecasting results from multiple metrics.

### Strengths
To adopt vector quantization in Transformer based models for time series forecasting is novel to the best of my knowledge. 
The manuscript is overall well and clearly written.
The proposed method has the potential to benefit the time series modelling community.

### Weaknesses
 - From Fig. 3, the influence of the codebook size J to the VQ-TR seems not stable. A more detailed discussion on this might help potential users to select this hyperparameter when using the model.

 - The manuscript claims that
>...methods based on Transformers (Vaswani et al., 2017) have dominated the state-of-the-art, outperforming both classical autoregressive approaches, as well as deep learning approaches using Convolutional Neural Networks (CNNs) or Recurrent Neural Networks (RNNs).

   However, in e.g. [1], which is not a Transformer based model, results of CRPS are better than the ones reported in the manuscript.
   A discussion (or comparison) on [1] might help to promote the contribution of the manuscript.

 - The manuscript assumes that the distribution of the predicted time point follows a (conditional) Gaussian distribution. Is there any theoretical or empirical evidence supporting this assumption? In e.g. [2], the paper also proposes a model for probabilistic time series forecasting, with a more solid assumption that the frequencies follow Gaussian distribution. A discussion on this might help to understand this Gaussian assumption.

 - In Sec. 4.2, the use of ```\citet{}``` and ```\citep{}``` needs to be carefully handled. 

 - It is unclear whether the current implementation of VQ-TR models each time series independently or jointly when applied to multivariate time series data. This distinction is crucial for understanding the scope and limitations of the model.

### Questions
- Is it true that the model as proposed in the manuscript, works for univariate time series only?

 - Can you elaborate the influence of different codebook sizes?

 - How is the context window length C selected?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
