# TrajGPT: Irregular Time-Series Representation Learning for Health Trajectory Analysis

- Decision: Reject
- Scores: 6, 6, 5, 8

## Abstract
In many domains, such as healthcare, time-series data is often irregularly sampled with varying intervals between observations. This poses challenges for classical time-series models that require equally spaced data. To address this, we propose a novel time-series Transformer called \textbf{Trajectory Generative Pre-trained Transformer (TrajGPT)}. TrajGPT employs a novel Selective Recurrent Attention (SRA) mechanism, which utilizes a data-dependent decay to adaptively filter out irrelevant past information based on contexts. By interpreting TrajGPT as discretized ordinary differential equations (ODEs), it effectively captures the underlying continuous dynamics and enables time-specific inference for forecasting arbitrary target timesteps. Experimental results demonstrate that TrajGPT excels in trajectory forecasting, drug usage prediction, and phenotype classification without requiring task-specific fine-tuning. By evolving the learned continuous dynamics,  TrajGPT can interpolate and extrapolate disease risk trajectories from partially-observed time series. The visualization of predicted health trajectories shows that TrajGPT forecasts unseen diseases based on the history of clinically relevant phenotypes (i.e., contexts).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes an approach for representation learning of irregularly sampled time-series data called Trajectory Generative Pre-trained Transformer (TrajGPT). The TrajGPT architecture employs a Selective Recurrent Attention (SRA) mechanism that allows it to selectively focus on relevant past information and ignore irrelevant data. The proposed approach is able to capture continuous dynamics and perform interpolation and extrapolation. The proposed approach achieves strong performance on several tasks, including forecasting disease trajectories, predicting drug usage, and classifying patient phenotypes. It also show good zero-shot performance on several tasks and provides interpretable results.

### Strengths
- The paper focuses on an important problem of learning from irregularly sampled time series which is important for several practical use cases.
- The paper introduces a novel architecture for modeling irregularly sampled time series- selective recurrent attention (SRA). SRA enables time-specific inference that leads to better imputation and forecasting. 
- Experiments show that the framework achieves strong zero-shot performance across multiple tasks and achieves comparable results with SOTA in the finetuning setup.
- The paper is well written and easy to follow.

### Weaknesses
- The evaluation of TrajGPT is limited, as it does not include benchmark irregularly sampled time series datasets such as PhysioNet and MIMIC-III. This makes it difficult to compare the performance of TrajGPT with other state-of-the-art models in this space despite the authors doing a good job of comparing on PopHR dataset.
- The paper overlooks important relevant work [1] and fails to provide a comparison with [1] which is the state-of-the-art for imputation in irregularly sampled time series.
- The paper lacks insight into why time-specific inference leads to better results than auto-regressive inference, which is the method used to train the model.


### References
[1] Heteroscedastic Temporal Variational Autoencoder For Irregularly Sampled Time Series, International Conference on Learning Representations, 2022.

### Questions
Listed them out in the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper propose a novel transformer-based model tailored for irregularly-sampled time-series data, especially in healthcare domain. 
TrajGPT features the Selective Recurrent Attention (SRA) mechanism, which incorporates a data-dependent decay to filter out irrelevant historical data, thus improving its adaptability to variable intervals in time-series data. The model is interpreted as discretized ODEs, enabling both interpolation and extrapolation, which is essential for accurate, time-specific predictions.

### Strengths
The authors provide clear motivations for their methods design. Especially,  the SRA mechanism design acts like a discretization of continuous-time ODE not only helping the model to learn the hidden continuous dynamics but also can achieve linear training complexity and constant inference complexity. 
The visualizations in the result part looks really insightful and back up authors' assumption.

### Weaknesses
1. As the paper targeted representation-learning,  current representation-learning, like self-supervised learning for irregular time series lacks of discussion[1].
2. The paper only conducts experiments on PopHR dataset. Benchmark datasets such as MIMIC-III and physionet2012 are not included. 

[1].Ranak Roy Chowdhury, Jiacheng Li, Xiyuan Zhang, Dezhi Hong, Rajesh K. Gupta, and Jingbo Shang. 2023. PrimeNet: pre-training for irregular multivariate time series. In Proceedings of the Thirty-Seventh AAAI Conference on Artificial Intelligence and Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence and Thirteenth Symposium on Educational Advances in Artificial Intelligence (AAAI'23/IAAI'23/EAAI'23), Vol. 37. AAAI Press, Article 807, 7184–7192. https://doi.org/10.1609/aaai.v37i6.25876

### Questions
/

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces TrajGPT, a generative pre-trained Transformer designed for irregular time-series in healthcare applications. TrajGPT incorporates a novel linear Selective Recurrent Attention (SRA) mechanism that uses data-dependent decay to filter past information contextually. By interpreting the architecture as discretized ordinary differential equations (ODEs), the model effectively handles continuous dynamics, enabling it to interpolate and extrapolate for irregularly sampled data, thus enabling making direct predictions into desired future time step. TrajGPT is evaluated across trajectory forecasting, drug usage prediction, and phenotype classification, achieving strong zero-shot performance without task-specific tuning. Additionally, its design supports interpretability in health trajectory analysis, allowing clinicians to link disease trajectories with patient histories.

### Strengths
- Efficiency: TrajGPT achieves linear training and constant inference complexities, making it more scalable compared to traditional Transformers for long sequences.
- Performance and Generalizability: TrajGPT demonstrates impressive zero-shot capability across diverse tasks, highlighting its potential as a general-purpose tool for healthcare applications.
- Interpretability: The model’s architecture allows for meaningful health trajectory predictions and risk analysis, supporting clinical applications by enabling interpretative insights into disease progression.

### Weaknesses
- Ambiguity in the definition of ODEs: The proposed TrajGPT model has a form that the gradient of the trajectory at certain time is not only dependent on the state at that time, but also the input at that time. This data-dependent gradient no longer satisfies the definition of ODEs, but more towards the definition of PDEs. The authors should clarify this discrepancy and provide a more accurate interpretation of the model.
- Poorly justified visualization: In Fig 3a, the authors visualize the learned embeddings along with head specific decay vectors using UMAP. However, these decay vectors do not have same meaning as the embeddings, as one is intended to be a weight matrix of the input data while the other serves as a representation of the input data. Therefore, although these vectors share the same dimensionality, they should not be embedded in the same manifold space by using UMAP.
- Improvements in paper structure: The paper would benefit from a more structured presentation of the proposed model, for example, in section 3.1, the authors could avoid presenting the parallel formulation of the proposed model as it is not directly related to the main contributions of the paper. On the other hand, the experiment section could be expanded to provide more insights on the model's performance across different tasks, including more detailed explanation of the results and comparison with established medical findings.
- Absence of robustness analysis: As the paper proposes a novel model for healthcare applications, it is important to evaluate the robustness and potential biases of the model. For instance, as the model draws similarities to ODEs, it is crucial to investigate intrinsic biases in the model such as the limit cycle bahavior, which could lead to biased predictions in certain scenarios. The authors should provide a more comprehensive analysis on the robustness of the model to ensure its reliability in real-world applications.

### Questions
- Can you provide more insights on the discrepancy between the proposed model and the definition of ODEs? Since the model relies on the PDE form to make predictions in the future, the lack of future observation, i.e., inputs, will almost surely lead to biased or at least inaccurate predictions. Can you explain how the model handles this issue and how it can be improved?
- Can you justify for the visualization of the learned embeddings and decay vectors? Or seperate the visualization of the learned embeddings and decay vectors to avoid confusion. This will help readers to better understand the model's inner workings and the role of each component in the model and avoid misinterpretation of the results.
- Can you explain more on the results of the experiments and find more support from the literature to validate the model's performance? This will help to better understand the model's effectiveness and accuracy in real-world applications.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents the Trajectory Generative Pre-trained Transformer (TrajGPT), a Transformer model designed to handle irregularly sampled time series, particularly within the healthcare domain. TrajGPT introduces a novel attention mechanism, Selective Recurrent Attention (SRA). Inspired by discretized ordinary differential equations (ODEs), the model achieves interpolation and extrapolation in irregular time series, excelling in trajectory prediction tasks. Experimental results show outstanding performance in zero-shot learning scenarios, underscoring TrajGPT’s capability to capture complex health dynamics from incomplete data.

### Strengths
- Comprehensive literature review.

- Thorough evaluation across different scenarios, with comparisons to multiple models and diverse datasets. The inclusion of interpretability through added figures is beneficial, and the ablation study is particularly valuable for assessing the contribution of each model component.

- The method is highly compelling, supported by a robust and thorough mathematical explanation.

- Novelty of the Attention Mechanism: The introduction of the Selective Recurrent Attention (SRA) module, which uses data-dependent decay, is an innovative contribution.

- Interpretation of TrajGPT as a Discretized ODE: Modeling TrajGPT as a discretized ODE is a valuable approach, allowing the model to capture continuous dynamics in irregular time series and perform time-specific inference, facilitating both interpolation and extrapolation in temporal data.

- Throughout the paper, I noted the similarities to State Space Models, which led me to find Appendix C particularly valuable.

### Weaknesses
There are few weaknesses in this paper:

- Since the relationship with State Space Models (SSMs) is discussed, it might have been interesting to include a method using Mamba to compare results with this type of model.

- Including a comparison with methods such as Multi-Gaussian Processes, which have been previously used for this type of approach, could strengthen the evaluation [1].

- Ultimately, as I understand it, this method has only been applied to univariate time series; it would be beneficial to explore its extension to multivariate time series in future work.

[1] Moor, M., Horn, M., Rieck, B., Roqueiro, D., & Borgwardt, K. (2019, October). Early recognition of sepsis with Gaussian process temporal convolutional networks and dynamic time warping. In Machine learning for healthcare conference (pp. 2-26). PMLR.

### Questions
- Do you believe this method could be easily extended to the context of multivariate time series?

- If expanded to multivariate time series, could it be combined with methods like GNNs to extract improved spatio-temporal representations?

- Despite the relationship, it remains unclear what the main advantages or potential inductive bias would be in using this method over Mamba blocks. Could you clarify this further? I would be happy to increase my score if the authors could expand on this information to clarify this important issue.

### Soundness
4

### Presentation
4

### Contribution
4
