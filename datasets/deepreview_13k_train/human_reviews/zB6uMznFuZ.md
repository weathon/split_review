# TimeAutoDiff: Generation of Heterogeneous Time Series Data via Latent Diffusion Model

- Decision: Reject
- Scores: 5, 1, 3, 3

## Abstract
In this paper, we leverage the power of latent diffusion models to generate synthetic time series tabular data.
Along with the temporal and feature correlations, the heterogeneous nature of the feature in the table has been one of the main obstacles in time series tabular data modeling. 
We tackle this problem by combining the ideas of the variational auto-encoder (VAE) and the denoising diffusion probabilistic model (DDPM).
Our model named as \texttt{TimeAutoDiff} has several key advantages including 
(1) \textit{\textbf{Generality}}: the ability to handle the broad spectrum of time series tabular data with heterogeneous, continuous only, or categorical only features; 
(2) \textit{\textbf{Fast sampling speed}}: entire time series data generation as opposed to the sequential data sampling schemes implemented in the existing diffusion-based models, eventually leading to significant improvements in sampling speed, 
(3) \textit{\textbf{Time varying metadata conditional generation}}: the implementation of time series tabular data generation of heterogeneous outputs conditioned on heterogenous, time varying features, enabling scenario exploration across multiple scientific and engineering domains.
(4) \textit{\textbf{Good fidelity and utility guarantees}}: numerical experiments on eight publicly available datasets demonstrating significant improvements over state-of-the-art models in generating time series tabular data, across four metrics measuring fidelity and utility; 
Codes for model implementations are available at the supplementary materials.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a novel method, TimeAutoDiff, to generate time series. It combines a variation autoencoder and DDPM. The method empirically outperforms prior methods on several datasets and allows for conditional time series generation.

### Strengths
- **Writing** The paper is well-written and well-structured.
- **Methodological contribution** The paper presents a clear method similar to diffusion methods in other domains. The technical details are discussed in detail. It seems straightforward to reproduce the results.
- **Research problem** The presented problem is essential and timely. In particular, synthetic time series generation is critical for foundation model development, as the authors mention in the discussion.

### Weaknesses
See Questions for detailed comments and suggestions.

- **Comparison to prior methods** It is worth discussing more the key differences to other diffusion-based models such as Diffusion-ts (https://github.com/Y-debug-sys/Diffusion-TS), and TimeDiff (https://openreview.net/pdf?id=ESSqkWnApz). Additionally, it is worth expanding metrics, such as consistency and diversity, as discussed in the TSGM framework (https://github.com/AlexanderVNikitin/tsgm).

- **Limitations and fairness**. Limitations and fairness are not discussed enough. In particular, can generated data be biased with respect to conditional metadata?

- **Design choices**. It would be great to have more details on the design choices of the decoder and $\epsilon_\theta$. Do other architectures significantly affect the performance of the method?

### Questions
>The sampling time column ranks models by their speed, with lower numbers indicating
faster sampling

Please add details.


> We set the dimensions of output features in this way as we used
the mean-squared (MSE), binary cross entropy (BCE), and cross-entropy (CE) in the Pytorch package.

It looks disconnected from the main text. Could you clarify?

>L: 249 More details are deferred in the Appendix J.

Appendix J does not provide additional details on the selection of a decoder architecture.

> LL: 171-173

Does the current model generate data for textual metadata? If so, it would be great to provide more experiments/demonstrations. If not – it may be worth removing this example.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
1

### Summary
This paper proposes to use latent diffusion models to generate synthetic time series tabular data.
They propose to combine VAE with DDPM and term the proposed method TimeAutoDiff.
They claim many advantages of this proposal and provide some experiments.

### Strengths
NA

### Weaknesses
Originality. DDPM or VAE for time series generation is not new. Most techniques used are also from prior works.
**Soundness.** It’s well-known that VAE is considered 1-step DDPM. I find the motivation and reasoning in `line 144-154` very unconvincing. It’s still unclear why DDPM is good at handling time series data, why VAE, as a special case is DDPM, can bring more to the table. Also, I don’t think citing unpublished and prior venue’s rejections as SOTA method is convincing, e.g., TSGM in `line 156`. 
**Clarity.** The captions of Fig 2,3 provide zero information. Many notations are introduced without definition, e.g., x_cont in `line 192`. Overall clarity can be further improved.
**Significance.**  The significance is hard to parse due to limited clarity. At best, I find it lacking due to its assembly nature. Additionally, I question the correctness of the experimental evaluation.

### Questions
Why are most experiments on regression datasets? How can these validate heterogeneous properties of “tabular” time series data?

The experiments lack convincing evidence. Please include additional summary statistics of the generated data and compare with baselines. For instance, stock data (nasdaq100) are known for key summary statistics like volatility and moving averages. Demonstrating that the proposed method closely matches these statistics would provide stronger support for its efficacy. Can you provide a generated example of your trained nasdaq100 model?

Why is Section 4.2 titled “Utility Guarantees” when there is no theoretical analysis provided?

These weaknesses are not meant to be exhaustive. I believe they are sufficient to show that this paper is not ready for publication.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The proposed work presents a framework of latent diffusion models for heterogeneous time series data. The framework utilizes an encoder within a variational autoencoder (VAE) to project both discrete and continuous features of time series data into a continuous latent space. Subsequently, a diffusion model is employed to model the distribution of the latent codes of the time series data. The encoder employed in the VAE is an RNN, while the diffusion model is DDPM[1]. Notably, the denoising network within DDPM employs cyclic encoding to incorporate time-stamp information into the time series and adopts a bi-directional RNN architecture. The proposed latent diffusion model can also be conditioned on meta-data for incorporating conditional information. Evaluation results on unconditional generation demonstrate that the proposed approach generates high-quality synthetic data and outperforms existing approaches.

References

[1] Ho, Jonathan, Ajay Jain, and Pieter Abbeel. “Denoising diffusion probabilistic models.” Advances in neural information processing systems 33 (2020): 6840-6851.

### Strengths
The work has the following notable strengths:
1. The works did comprehensive evaluation on unconditional and conditional generation tasks, taking both lower-order and higher-order statistics into account. The proposed approach shows superior performance over existing approaches on both tasks across the datasets considered in the work. In addition the work also did comprehensive over different hyper-parameters variations and ablations to reveal the impact of different components to the model.
2. The presentation quality of the work is good and the proposed method of the work is easy to follow.

### Weaknesses
The work exhibits several significant weaknesses:
1. The work lacks innovative methodology. Similar ideas for tabular data, which arguably encompass time-series data, have been explored in existing works [1]. Despite some crucial technical differences between the two works, including the design of the denoising network $\epsilon_\theta$ and the approach to the latent space, the high-level framework of both works is both a latent diffusion model that projects structured data to a latent space and uses a diffusion model to model the distribution of latent codes.
2. The majority of the experiments are limited to unconditional generation of time-series data, and it is unclear how the proposed model can be readily adapted to tasks with more practical applications, such as forecasting and imputation.

### Questions
1. I would like to inquire about the rationale behind employing RNN as the encoder for time-series data and capturing temporal dependencies between features across various timestamps. The temporal dependencies between features can also be captured by the denoising network of the diffusion model. Therefore, is it necessary to utilize an RNN to capture temporal dependencies when encoding the data?

2. I would encourage the author to provide a more comprehensive discussion and emphasize the values or practical significance of the tasks the model is evaluated on, specifically unconditional generation and time-variant meta-data conditioned generation.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces TimeAutoDiff, a time series tabular data synthesizer that combines the Variational Auto-Encoder (VAE) and Denoising Diffusion Probabilistic Model (DDPM). It effectively manages heterogeneous features and enhances data generation fidelity and temporal dependencies. The model integrates a latent diffusion framework with a specialized VAE, improving performance in high-dimensional settings. It supports applications such as missing data imputation, privacy, and interpretability, and demonstrates superior results compared to existing models in generating synthetic time series data.

### Strengths
The paper is easy to read and the experiments are comprehensive.

### Weaknesses
One concern is its current inability to generate interpretable results. In many practical applications, especially in high-stakes fields like finance and healthcare, stakeholders must clearly understand how models make decisions. The lack of interpretability can lead to skepticism and reluctance to adopt the model, as users may hesitate to trust a system whose inner workings are opaque. This limitation could hinder the model's applicability in scenarios where understanding the rationale behind generated data is crucial for decision-making; Another point is the pure focus on continuous data: While the method demonstrates good performance with continuous data, its methods are primarily tailored for this data type. This focus raises concerns about the model's effectiveness when dealing with heterogeneous datasets that include categorical features. The inability to seamlessly integrate and process diverse data types could restrict the model's usability in real-world applications where such heterogeneity is common; another point is the dependence on latent space reduction: The paper notes a performance drop when the feature sizes increase, which necessitated a reduction in the latent space dimension. This reliance on dimensionality reduction to maintain performance raises concerns about the model's scalability and robustness. If the model's effectiveness is sensitive to the dimensionality of the latent space, it may struggle to perform well in high-dimensional settings without careful tuning.

### Questions
1, How can the model be made more robust to high-dimensional feature spaces without relying heavily on latent space reduction?

2, What modifications or extensions to the framework would be necessary to effectively handle heterogeneous datasets that include both continuous and categorical features?

### Soundness
3

### Presentation
4

### Contribution
3
