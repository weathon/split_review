# Learning Time-shared Hidden Heterogeneity for Counterfactual Outcome Forecast

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
Forecasting counterfactual outcome in the longitudinal setting can be critical for many time-related applications. To solve this problem, the previous works propose to apply different sequence models including long short-term memory (LSTM) networks and transformers to model the relationship between the observed histories, treatments and outcomes, and apply various approaches to remove treatment selection bias. However, these methods neglect the hidden heterogeneity of outcome generation among samples induced by hidden factors which can bring hurdles to counterfactual outcome forecast. To alleviate this problem, we capture the hidden heterogeneity by recovering the hidden factors and incorporate it into the outcome prediction process. Specifically, we propose a Time-shared Heterogeneity Learning from Time Series (THLTS) method which infers the shared part of hidden factors characterizing the heterogeneity across time steps with the architecture of variational encoders (VAE). This method can be a flexible component and combined with arbitrary counterfactual outcome forecast method. Experimental results on (semi-)synthetic datasets demonstrate that combined with our method, the mainstream models can improve their performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a Time-Shared Heterogeneity Learning from Time Series (THLTS) approach for Counterfactual Outcome Forecasting, addressing the limitation in previous sequential models caused by insufficient consideration of hidden heterogeneity in sample outcomes caused by hidden factors. Extensive experiments demonstrate the effectiveness of THLTS, as well as its robustness in scenarios with unstable hidden factors or long sequence data.

### Strengths
1.This paper addresses the high relevance between decision-making tasks and temporal sequences, thoroughly analyzing the limitations of previous methods in modeling hidden factors beyond historical records. Leveraging a Variational Autoencoder (VAE), it creatively proposes a Time-Shared hidden factor learning approach to effectively bridge these gaps, demonstrating both originality and significance in the field.

2.This paper begins by presenting intuitive examples to illustrate how hidden factors can lead to different counterfactual outcomes for individuals with identical historical information. It then introduces the proposed THLTS method in a progressively detailed manner, followed by a rigorous theoretical derivation to analyze the validity of this hidden factor learning approach. Subsequently, the paper provides a detailed description of the three key components that enable THLTS, as well as its training and inference processes. The logic is coherent.

3.This paper conducts comprehensive experiment, validating the effectiveness of THLTS and its flexibility as a plugin of pioneering models, particularly under conditions of unstable hidden factors and long sequence data.

### Weaknesses
1.Clarity issues in some details. This is evident, on one hand, in the mismatch between figure legends and definitions in the text. For example, in the problem description, sample indices are indicated as superscripts, yet in Figure 1, sample indices for each latent factor are shown as subscripts, which potentially confuses them with time indices. On the other hand, some symbols lack explicit explanations; for instance, m in Equation (5), while seemingly representing the number of repetitions for sampling Time-Shared Hidden Factors and outcome prediction, would benefit from explicit clarification to enhance understanding.

2. Lacking sufficient background information. It particularly in explaining of VAE. For readers unfamiliar with variational inference, it may be challenging to understand how to model and sample the Time-Shared Hidden Factors.

3. The experiments are not sufficiently extensive. On one hand, the experimental data heavily relies on synthetic datasets, which significantly reduces the persuasiveness of the results and raises concerns about the practical applicability of the model. The synthetic data generation process is not clearly described, making it difficult to assess the realism of the data. On the other hand, the choice of comparison baselines appears to lack novelty, as the most recent baseline, G-net, was proposed in 2020. Exploring and discussing more recent methods that incorporate, for example, attention mechanisms or more advanced causal inference techniques, to highlight the contribution of this study would be beneficial.

### Questions
Q1: One argument in the paper posits that the modeling approach using Time-Shared Hidden Factors across all time steps for each sample is superior to previous methods that model hidden factors differently at each time step. This claim may appear somewhat counterintuitive and perplexing. Beyond the empirical conclusions drawn from experiments and the potential rationale of limited supervisory signals, is there a more comprehensive explanation or theoretical justification to alleviate this concern?

Q2: In the experiments, synthetic datasets were used. Firstly, does the synthetic method employed in the paper generate data that aligns with real-world distributions? Is this synthetic approach a standard in the field or a heuristic design by the authors? Furthermore, do the experimental results based on these datasets have practical significance? How is this demonstrated or substantiated?

Q3: There are some clarity-related concerns. Firstly, the learning of Time-Shared Hidden Factors is based on VAE, which is not reflected in the overall illustration in Figure 2. While appropriate simplification is essential, would incorporating the VAE structure into the diagram help readers better understand the model architecture? Additionally, in Section 4.3, could the mathematical description of L_t^((i)) be streamlined to aid readers in comprehending the model implementation? For instance, specifying that the KL divergence term involves the normal distributions corresponding to two contiguous time steps if correct.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper tackles the challenge of forecasting counterfactual outcomes in longitudinal settings. Previous methods using LSTM networks and transformers often neglect hidden heterogeneity caused by unobserved factors, which complicates predictions. The authors propose the Time-shared Heterogeneity Learning from Time Series method, which captures shared hidden factors using variational encoders. This approach enhances any counterfactual forecasting method and demonstrates improved performance in experiments with synthetic datasets.

### Strengths
1. Forecasing counterfactual prediction is highly applicable in real-world scenarios.
2. The time-shared heterogeneity based learning method is easy to implement with VAE.
3. This paper first utilizes longitudinal method to find the latent factor of each sample, which is intuitive.

### Weaknesses
1. In Proposition 4.1, it would be helpful for the authors to explain more about when the prediction model $g$ is Lipschitz with respect to $e$, as this is critical for ensuring the model's effectiveness in identifying the latent factor. Specifically, the paper should discuss the implications of the Lipschitz constant's magnitude on the stability and generalization of the learned latent representations. A large Lipschitz constant could lead to unstable gradients and poor generalization, while a small constant might overly constrain the model's expressiveness. The paper should also clarify whether the Lipschitz condition is assumed for the entire input space or only a specific region, and how this choice affects the theoretical guarantees.
2. Since the latent factor is not directly observed, how can you guarantee that the latent factor identified by your method is the one you intend to find? It would be beneficial to provide some analysis regarding the identifiability of your method. The paper should explore the uniqueness of the learned latent factors and discuss potential issues arising from multiple possible latent representations that could explain the observed data. Furthermore, the paper should consider providing a theoretical analysis or empirical validation to demonstrate that the learned latent factors are indeed capturing the intended underlying heterogeneity, rather than simply fitting noise or spurious correlations in the data.
3. Why did you choose VAE to implement your method? Could other structures, such as deterministic models, serve as the backbone? If so, is it possible to test different models as backbones in the experimental section? The paper should justify the choice of VAE over alternative generative models, such as normalizing flows or GANs, by discussing the specific advantages of VAEs in this context. The paper should also explore the impact of different encoder and decoder architectures within the VAE framework on the quality of the learned latent factors and the overall performance of the counterfactual forecasting task. A comparison with deterministic models, even if not as a primary focus, would provide valuable insights into the robustness of the proposed method.
4. The compared baselines are not state-of-the-art methods. It would be better to select more recent methods as baselines to demonstrate the effectiveness of your approach, such as [1]. The paper should include a more comprehensive comparison with recent state-of-the-art methods in counterfactual inference for time series data. The current baselines do not fully represent the advancements in the field, and a comparison with methods that explicitly address time-varying confounders or use more advanced representation learning techniques would provide a more rigorous evaluation of the proposed method's performance.

### Questions
See weakness

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Time-shared Heterogeneity Learning from Time Series (THLTS), a novel method for capturing hidden heterogeneity in longitudinal counterfactual outcome prediction. THLTS, designed as a flexible component that can be integrated with existing models, learns time-shared latent factors using VAE architecture.

### Strengths
1.The motivation is well-presented, which helps contextualize the problem being addressed.

2.The proof in Section 4.2 logically explains the motivation for employing a VAE architecture, making the rationale clear and reasonable.

3.Comprehensive experimental evaluation demonstrates performance improvements

### Weaknesses
1.The paper lacks novelty. The idea of recovering hidden factors has been widely explored in previous research. While learning the "TIME-SHARED" components is not as commonly discussed, but it is not significantly different from previous work, like Causal Effect Inference with Deep Latent-Variable Models" (Louizos et al., 2017),Causal Dynamic Variational Autoencoder for Counterfactual Regression in Longitudinal Data" (Bouchattaoui et al., 2023) and Factual Observation based Heterogeneity Learning for Counterfactual Prediction" (Zou et al., 2023).

2.While the paper mentions that "decision-making problems can span long periods of time," it does not introduce any specialized structures to capture unique features of long time series, such as periodicity or seasonality. For example, incorporating techniques like Fourier transforms for periodicity detection or wavelet transforms for handling multi-scale temporal structures could offer substantial improvements.

3.Despite claiming to address long-term time series forecasting, the paper only validates its method on notably short sequences (maximum 30 time steps).

### Questions
What are the unique challenges of addressing hidden heterogeneity across time?

### Soundness
4

### Presentation
3

### Contribution
2
