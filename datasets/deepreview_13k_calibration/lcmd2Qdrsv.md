# Mixture-of-Diffusers: Dual-Stage Diffusion Model for Improved Time Series Generation

- Decision: Reject
- Avg Score: 5.60
- Scores: 8, 3, 3, 6, 8

## Abstract
Synthetic Time Series Generation (TSG) is a crucial task for data augmentation and various downstream applications. While TSG has advanced, its effectiveness often relies on the availability of extensive training datasets, posing challenges in data-scarce scenarios. Generative Adversarial Networks (GANs) and Variational Autoencoders (VAEs) have shown promise, but they frequently struggle to capture the complex temporal dynamics and interdependencies inherent in time series data. To address these limitations, we propose a novel generative framework, Mixture-of-Diffusers (MoD). This approach decomposes the diffusion process into a collection of specialized diffusers, each designed to model specific patterns at distinct noise levels. Early-stage diffusers focus on capturing overarching global and coarse patterns, while late-stage diffusers specialize in capturing fine-grained details as the noise level diminishes. This hierarchical decomposition empowers MoD to learn robust representations and generate realistic time series samples. The model is trained using a combination of multi-objective loss functions, ensuring both temporal consistency and alignment with the true data distribution. Extensive experiments on a diverse range of real-world and simulated time series datasets demonstrate the superior performance of MoD compared to state-of-the-art TSG generative models. Furthermore, rigorous evaluations incorporating both qualitative and quantitative metrics, coupled with assessments of downstream task performance on long-term generation and scarce time series data (see Figure 1), collectively validate the efficacy of our proposed approach.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a novel framework, mixture-of-diffusers (MoD), for time series generation. This framework employs dual-stage diffusion models, integrating the Transformer architecture, to explicitly model the global and local features at different noise levels within time series. Experimental results show the superiority of MoD over existing approaches.

### Strengths
1. The hierarchical modeling of time series features at different noise levels is innovative to the best of my knowledge.
2. This paper is well-structured and easy to follow. The authors provide sufficient preliminaries for the readers unfamiliar with the key concepts.
3. I appreciate Figure 2. It provides a clear overview of MoD, making the general process easier to understand.
4. The experiments are thorough, conducting a range of datasets and evaluation metrics that underscore the effectiveness of the proposed model.

### Weaknesses
1. The paper lacks a detailed discussion on the time-dependent weighting scheme used to integrate the early and late-stage diffusers. A more thorough analysis, supported by theoretical or empirical evidence, is required to clarify how this scheme effectively distinguishes the granularity of features for the dual-stage diffusers, e.g., how each stage of the diffusion model contributes to processing different levels of noise. Specifically, the paper does not provide sufficient insight into how the weighting function is designed, what parameters govern its behavior, and how these parameters are tuned to ensure the desired separation of coarse and fine-grained feature learning. It is unclear if the weighting is a simple linear interpolation or a more complex function, and how this choice impacts the overall performance.
2. The methodology section would benefit from a stronger focus on the novel designs introduced by the MoD framework. In particular, sections 2.2 and 3.1 could be streamlined to avoid redundancy and discuss more on the novel aspects of MoD. The current presentation spends too much time on standard diffusion concepts and Transformer architecture, which are not the core contributions of this work. The paper should instead emphasize the unique aspects of the MoD framework, such as the dual-stage diffusion process and the specific mechanisms that allow it to model hierarchical temporal features.
3. The bullet points outlining the evaluation metrics lack a clear hierarchical structure, leading to potential confusion. A more organized presentation would enhance the readability. The current list of metrics is presented as a flat list, making it difficult to understand the relationships between different metrics and their relevance to the evaluation of time series generation. A better approach would be to categorize the metrics based on their purpose, such as metrics for assessing the quality of generated samples, metrics for evaluating the diversity of the generated data, and metrics for assessing the temporal coherence of the generated time series.

### Questions
1. How can we guarantee the early-stage and late-stage diffusers, despite having the same network design, learn to represent coarse-grained and fine-grained temporal dynamics, respectively? Would it be possible for them to learn entangled representations, like VAE-based models,  of the target time series but not the hierarchically global and local features as designed?
2. Given that the training data are sampled as L-length sequences from a target time series, is there a risk that this sampling method might miss critical patterns, especially at the ends of the windows, hindering the model’s ability to capture vital fine-grained features?
3. In Figure 3, the KDEs for real data appear different when comparing MoD and TimeGAN, particularly for the Energy dataset. Is it possible to compare the MoD and TimeGAN data distribution with the same real samples?
4. Is the MoD framework suitable for direct use in forecasting applications?
5. Can you discuss the limitations of MoD?
I'd like to raise my score once my concerns are addressed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a mixture of two diffusion models to generate time series in an unconditional setting. The models are trained using the MSE and KL divergence of the posteriors. Experiments show improvements over different baselines on various metrics.

### Strengths
- The model explores unconditional time series generation via a mixture of two diffusion models with a modified loss function
- Results outperform the corresponding baselines on various metrics

### Weaknesses
 - The novelty is limited. The proposed diffusion model consists of a linear interpolation of two neural networks and uses a slightly modified loss function. 
- A "hierarchical decomposition" should consist of more than two models.
- The loss function in equation 12 needs to be further explained. How is the KL divergence computed? I assume there is a typo as $q(x_{t-1}\mid x_t)$ is, to the best of my knowledge, not tractable. It is unclear how this helps the training process, as the KL divergence should simplify to a weighted l2 loss.
- There are several wrong equations; for example, equation 8 is incorrect. No noise should be added to the mean.
- Related works should be discussed more thoroughly. Multiple works are ignored, including irregular and unconditional models [1,2,3,4]. 
- There are various typos in the manuscript, including in the pseudo-codes, e.g., $T$ should be $t$ in algorithm 1.
- Labels in Figure 1 are missing. It is unclear which color represents the GT and which represents the synthetic samples.
- Experimental details are missing: how many random seeds were used to compute standard deviations?

**Code issues:**
- command in readme wrong
- conflict of PyYaml: two times a different version
- config file is only available for ETTh1
- details should be included in the paper. E.g., dropout and EMA are applied in the code but not mentioned in the paper

### Questions
- Can you elaborate on the claim "we employ a joint training regimen that integrates different loss functions, concurrently enforcing temporal consistency and data distribution similarity"? How does the loss enforce temporal consistency?
- The paper states that the early-stage diffuser concentrates on global structure while the late-stage diffuser specializes on local fine-grained structures. Have any experiments investigated these properties?
- In section 3.2, it is stated, "Each Diffuser is designed to model specific underlying patterns within its specialized domain of expertise". Can you elaborate on the different designs? 
- In the introduction, irregular data is mentioned as a limitation of previous models. How does MoD address this limitation?
- The ablation in Table 4 shows that certain configurations, e.g., using the MSE loss, improve the metrics by >10x. Is there a qualitative comparison between these or an intuition as to why the difference is so substantial?

### Soundness
1

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
This paper proposes the mixture-of-diffusers (MoD) method, which introduces two-stage diffusion models to handle the data with different noise levels. With the design of the MoD architecture and integrating the MSE and KL loss functions, this work can achieve learning robust representations and generating realistic time series samples.

### Strengths
1.	The experimental design is rich, and a variety of indicators are introduced to evaluate the quality of the generated time series, which is quite convincing.
2.	The design of using the MoE approach to combine the two-stage diffusion model is original.

### Weaknesses
1.	The selection of downstream tasks is limited. The conditional generation may be a task that better reflects the multi-scale modeling of time series.
2.	The innovation of this paper seems insufficient. Can the weight of MoE be changed dynamically based on the granularity level of the sample itself? Are the number of stages (two) enough? Can more diffusers further improve performance? The paper lacks further exploration, making the innovation of the method quite limited.
3.	The descriptions of some figures in the paper lack information, e.g., what data the blue and red points in Figure 1 represent, which can easily confuse the readers.
4.	The experimental results of the baselines seem to be directly copied from Diffusion-TS, I suggest the authors try reproducing the results of the baselines for more fair comparison.

### Questions
1.	The paper lacks some analysis about the roles of the diffusers in the two stages. I am curious whether the diffuser in the first stage is really modeling coarse-grained information, and whether the diffuser in the second stage is really modeling fine-grained information. 
2.	In the ablation study, the lead of the MoD method over the “no Time Adaption” and “w/o KL methods” is not significant, even basically within the standard deviation range. Can I conclude that the MoD method does not significantly improve the performance?
3.	Can adding more experts further improve the performance? Are two experts enough?
4.	I noticed that the coordinates of the t-SNE visualizations of different proportions in Figure 1 are not the same. Is the data of each figure reduced in dimension by t-SNE alone? If the visualizations of different proportions use the same dimensionality reduction as 100%, we can observe the distribution of the sampled data and the corresponding generated data in the overall data, which help to establishing an intuitive understanding.
5.	As mentioned above, could you please ensure that all comparative experiments are conducted under the same environment and settings with repeated trials?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes using a combination of exporters for time series generation with diffusion models. It suggests that one model specializes in the initial noise reduction stages where high-level details are more dominant in time series in general, while another focuses on the final steps that involve producing fine-grained details. Additionally, the paper introduces new tasks for generating longer time series (up to 256 time steps) and for creating new data in situations with limited data availability.

### Strengths
- The concept of using a Mixture of Experts for different attribute generation steps is sensible in the context of time series and is straightforward to implement.  
- In my opinion, the benchmark focused on scarce training data is important and relevant.  
- The paper is well-written.

### Weaknesses
 - The benchmarks lack state-of-the-art methods like [1], which show significantly better results than the other methods presented. Consequently, the claim of being state-of-the-art remains invalidated.
- In the scarce data experiment a SOTA method is not being compared to (Diffusion-TS)
- The method is a simple adaption of a mixture of experts, although incremental changes may be important, in this case, where the results are not substantially stronger, or nor is a specific problem is being solved where other models completely fail on it, I think its a weakness of the paper.

### Questions
- Could the author clarify the motivation for adding the KL loss in addition to what has already been stated and the improved experimental results? In diffusion models, it’s uncommon to include such a term, and it somewhat resembles the use of noise prediction loss alone.  
- The generation of long sequences is interesting but has been addressed in other setups [2]. Additionally, a recent paper [4] has proposed it as well.  
- While it’s not necessary to compare or include these in the benchmarks of this paper, I recommend incorporating references to cutting-edge papers [3, 4, 5] to enhance the quality of the related work section and keep it up to date.

[1] Generative Modeling of Regular and Irregular Time Series Data via Koopman VAEs  
[2] Deep Latent State Space Models for Time-Series Generation  
[3] IDE: Frequency-Inflated Conditional Diffusion Model for Extreme-Aware Time Series Generation  
[4] Utilizing Image Transforms and Diffusion Models for Generative Modeling of Short and Long Time Series  
[5] SDformer: Similarity-driven Discrete Transformer For Time Series Generation

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
5

### Summary
This paper presents a method for time-series generation using two diffusion models. The two models are specialized for different aspects of the generation process:

1. Capturing coarse-grained patterns in high-noise regimes
2. Capturing fine-grained patterns as the noise level decreases

To train these models, the authors employed two loss functions:

1. MSE (Mean Squared Error) loss
2. KL (Kullback-Leibler) divergence loss

 These loss functions were used to align noise prediction with the data distribution. The results demonstrate strong performance across various datasets, including impressive results on longer sequences.

The proposed approach effectively generates time series data by leveraging the strengths of diffusion models at different noise levels. By separating the tasks of capturing coarse-grained patterns, the method appears to achieve better overall performance in time series generation tasks.

### Strengths
This paper is well-written and easy to understand. The authors have conducted a fair comparison with other baseline models using a variety of datasets and evaluation metrics. Additionally, the model demonstrates good performance on datasets with long-term sequences, addressing existing generative models' limitations.

In terms of contributions, the following points stand out:

1. Dual Loss Function: The use of both MSE loss and KL divergence loss is a significant contribution. This approach likely enhances the 2. model's ability to align noise prediction with the data distribution more effectively.
2. Two-Stage Diffusion Model: The implementation of two separate diffusion models is intuitive and innovative. This design allows for:
- Capturing coarse-grained patterns in high-noise regimes
- Focusing on fine-grained patterns as the noise level decreases
3. Comprehensive Evaluation: The authors have demonstrated the model's effectiveness across various datasets, including those with long sequences. This thorough evaluation strengthens the credibility of their approach.
4, Addressing Long-Term Dependencies: By showing good performance on long-term sequences, the paper tackles a known challenge in generative models for time-series data.

The combination of these strengths suggests that the paper makes a valuable contribution to the field of time-series generation, offering both theoretical insights and practical improvements over existing methods.

### Weaknesses
Despite being well-written overall, this paper has a significant issue. The method proposed in the paper is described as a "mixture-of-diffusers" in the title, but the content related to this concept is lacking in the main text. 

The paper doesn't adequately explain at which point the model switches from one diffusion model to the other. This lack of clarity makes it difficult to fully understand the proposed method's mechanics.

Also, the experiments on data scarcity seem unnecessary in the context of this paper. The results show that the performance of existing models remains unchanged as the amount of data decreases from the original dataset size. This doesn't appear to contribute meaningfully to the paper's main arguments or proposed method.

These weaknesses, particularly the lack of detailed explanation about the mixture-of-diffusers approach and the inclusion of seemingly irrelevant experiments, detract from the overall impact and clarity of the paper. More in-depth analysis and better alignment with the proposed method would significantly strengthen the paper's contributions.

### Questions
Transition Point Between Diffusers

The exact transition point (t) between the early-stage and late-stage diffusers is not explicitly stated in the paper, which is a significant oversight. This lack of clarity leads to several important questions:

1. **Determination of t**: How is the transition point t determined? Is it:
   - Fixed for all datasets?
   - Learned during training?
   - Dynamically adjusted during the generation process?

2. **Factors Influencing t**: What factors influence the choice of t? Possible considerations might include:
   - The nature of the dataset
   - The complexity of the patterns being generated
   - The total number of diffusion steps

3. **Consistency Across Datasets**: Does the transition point remain consistent across different datasets, or does it vary? If it varies, what causes these variations?

4. **Impact on Performance**: How sensitive is the model's performance to the choice of t? Is there an optimal range for this transition point?

In addition, computational complexity and efficiency of transformer-based architectures, especially in the context of using two diffusion Additionally, I believe the complexity has increased due to the use of a transformer-based architecture, especially because two diffusion models are being used. Therefore, I'm curious about the sampling speed and the number of parameters for each model.

### Soundness
3

### Presentation
3

### Contribution
3
