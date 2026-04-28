# GITAR: GENERALIZED IRREGULAR TIME SERIES REGRESSION VIA MASKING AND RECONSTRUCTION PRETRAINING

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
Multivariate time series regression, encompassing forecasting and interpolation, is crucial for numerous real-world applications, particularly in healthcare, climate science, ecology, and others. While recent work has focused on improving modeling for time series regression, two main limitations persist. First, the prevalence of irregularly sampled time series with missing values poses significant challenges.
For instance, healthcare applications often involve predicting future or missing observations from irregular data to enable continuous patient monitoring and timely intervention. As current approaches mainly rely on the assumptions of regular time series such as strong periodicity, when applied to irregular ones they exhibit performance degradation. Second, while some state-of-the-art methods (SOTA) do model irregularity and perform regression tasks on irregular data, they are often trained in a fully supervised manner. This limits their ability to generalize easily to different domains (e.g., training and testing datasets with different numbers of variables). To address these challenges, we propose GITaR, a Generalized Irregular Time Series Regression model via masking and Reconstruction pertaining mechanism, aiming to capture the inherent irregularity in time series and learn robust, generalizable representations without supervision for downstream regression tasks. Comprehensive experiments on common real-world regression tasks in healthcare, human activity recognition, and climate science underline the superior performance of GITaR compared to state-of-the-art methods. Our results highlight our model’s unique capability to generalize across different domains, demonstrating the potential for broad applicability in various fields requiring accurate temporal prediction and interpolation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In order to handle irregular multivariate time series data, the paper presents GITAR, a self-supervised learning (SSL) framework that combines irregular-temporal encoder, time-sensitive patching, and irregular-sensitive masking. The suggested model aims to address drawbacks of current approaches, including limited adaptability to new domains and domain-specific inter-channel dependencies. According to tests conducted on a number of real-world datasets, GITAR outperforms other state-of-the-art (SOTA) techniques in irregular time series regression tasks.

### Strengths
- The paper addresses a relevant and challenging issue in irregular time series analysis, which is applicable across a variety of fields. 

- The framework is technically well-executed with clear mathematical formulations. The irregular-time attention mechanism (ITA) and continuous time embeddings are rigorously defined, providing robustness for learning temporal dynamics.

- The experiments cover multiple datasets, which helps evaluate the framework across different irregular time series contexts.

### Weaknesses
 - The theoretical foundations of the proposed methods are weakly articulated. The notation and assumptions behind the continuous embeddings and ITA mechanism are not thoroughly explained. Key concepts, such as the initialization and constraints of embedding parameters, are underexplored. Specifically, the paper lacks a rigorous justification for the choice of sinusoidal embeddings over other potential basis functions, and it does not provide a clear explanation of how the learnable parameters within these embeddings (\(\omega\) and \(\alpha\)) are initialized or constrained during training. This raises concerns about the stability and convergence of these parameters, particularly given the non-stationary nature of time series data.

- The model’s generalization claim would be better supported by comparing it to a broader array of baselines that specifically address irregular time series and variable sampling rates. While the paper includes several baselines, a more comprehensive comparison should include methods that explicitly handle irregular sampling and varying observation rates. This would provide a stronger empirical basis for the claim that GITAR generalizes well across different irregular time series contexts. The current comparison does not fully address the nuances of irregular time series analysis, potentially overlooking relevant state-of-the-art approaches.

- The model’s main innovations appear to be modest adaptations of existing techniques (e.g., masked autoencoders). Without stronger theoretical or empirical evidence, GITAR’s contribution to the field of irregular time series analysis seems limited. The paper does not sufficiently demonstrate how the proposed adaptations of masked autoencoders and attention mechanisms provide a significant advancement over existing methods. The novelty of the approach is not clearly established, and the empirical results do not conclusively demonstrate a substantial improvement over other techniques.

### Questions
- In case of continuous time embeddings, why are specific sinusoidal terms chosen over other possible basis functions? What benefits do $\omega$ and $\alpha$ provide in capturing irregular periodicities? Is there theoretical support indicating they are optimal for this purpose? How do these embeddings behave under highly irregular sampling intervals?

- What theoretical or empirical basis supports the choice of attention as the primary mechanism for learning temporal dependencies in irregular time series? Would other mechanisms (e.g., kernel-based methods,  spectral embeddings, or Neural ODE/SDE) potentially provide similar or improved performance?

- Is there any analysis or empirical validation demonstrating that these attention weights maintain meaningful interpretations across different irregularity patterns?

- The choice of patch size and masking ratio is critical for the performance of GITAR. How does the model’s accuracy change as these hyperparameters vary? Additionally, how are these hyperparameters selected for datasets with different irregularity patterns?

- Given the high complexity of long time series sequences, how does GITAR address computational challenges associated with global attention mechanisms?

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
The paper proposes a new generalized regression framework for irregular time series data.  The model is trained in the self-supervised mode by relying on a patching and masking mechanism that permits to define and learn the model on a variety of regression tasks. The task sampling schema used for training the model is proposed. After the self-supervised training the model can be used to support a variety of downstream regression tasks.  The model is tested on prediction and interpolation tasks on four datasets showing promising prediction performance against baselines.

### Strengths
Originality: A novel attempt to train the models supporting regression inferences on irregularly sampled time series data. Also the idea of using mTAN approach for encoding irregular time series patches to regular representation is interesting and can be applicable to future time series neural network architectures

Significance: Irregularly sampled time series data are important for many practical applications, most prominently healthcare. The objective of developing models that are able to support many downstream regression tasks  is well justified.  

Experiments: •	Authors show a promise of the GITaR method against baseline methods in interpolation, forecasting and transfer learning tasks on multiple irregular time series datasets.

### Weaknesses
 **** Methodology ****

The novelty of the patch schema is unclear and very much resembles recent work on T-PatchGNN.

Weijia Zhang, Chenlong Yin, Hao Liu, Xiaofang Zhou, and Hui Xiong. Irregular multivariate time series forecasting: A transformable patching graph neural networks approach. ICML, 2024 I 

It appears that the Global Temporal Encoding $E^i$ is over individual time series and does not capture dependencies across different time series. It is unclear if/how these patterns and dependences are captured in the model. The lack of explicit modeling of cross-channel dependencies is a significant limitation, especially given that many real-world time series exhibit strong inter-variable relationships. This design choice may limit the model's ability to capture complex dynamics present in multivariate time series.

The description of the decoder architecture is missing in the paper. It is understandable that the model transforms the irregular observations to a regular latent representation. It is unclear how the model then makes the predictions of time series variables at irregular times from this regular latent representation. The absence of details regarding the decoder's structure and its mechanism for handling irregular time outputs makes it difficult to fully assess the model's architecture and its suitability for the task.


**** Experiments *****

Evaluating the performance of models designed for regular time series (Re) against those specifically tailored for irregular time series (IR) on irregular time series regression tasks  doesn’t add much value to the analysis. Perhaps authors intend to just highlight the importance of incorporating time explicitly in the model is important, which makes sense. However, including only 3 IR model baselines in the main results section is limiting. More IR baselines from the families: RNN-based (e.g., GRU-D [1]), Graph-based (e.g., Raindrop [2]), and ODE-based (e.g., ContiFormer [3]) should be considered in the experimental analysis for robust evaluation. The current selection of baselines does not provide a comprehensive comparison against the state-of-the-art methods designed for irregular time series data. The absence of these established baselines makes it difficult to ascertain the true performance gains of the proposed method.

[1] Zhengping Che, Sanjay Purushotham, Kyunghyun Cho, David Sontag, and Yan Liu. Recurrent neural networks for multivariate time series with missing values.

[2] Xiang Zhang, Marko Zeman, Theodoros Tsiligkaridis, and Marinka Zitnik. Graph-guided network for irregularly sampled multivariate time series.

[3] Yuqi Chen, Kan Ren, Yansen Wang, Yuchen Fang, Weiwei Sun, and Dongsheng Li. Contiformer: Continuous-time transformer for irregular time series modeling, 2024.

Interpolation experiments are performed only on Physionet dataset, and do not have MAE metric in the final comparison.

The results section on generalization capabilities is promising but limited to draw meaningful conclusions from. It is unclear why training is performed only on the Physionet dataset and tested on the rest. It would be worthwhile to see if the benefits of this generalization hold up for when the model is pretrained on other datasets or on a combination of them and tested on the remaining set. For example, train on MIMIC and test on the rest; train on MIMIC+Physionet and test on the rest would help to evaluate GITaR’s generalization capabilities.

**** Code *****

The code necessary for reproducing the reported results is not included in the submission.

### Questions
- Can you explain the difference of patching mechanism in T-PatchGNN and Time-sensitive Patching proposed in your work? 

- The text for section on generalization capabilities can be improved. Can you clarify how exactly the results are computed? Is there a transfer learning step (i.e., training) on the target domain? Is it the forecasting task? If so, what is the forecasting horizon? Is it comparable to the forecasting results (i.e., Table 2)?

 Are there any special or extreme cases where task sampling schema for supporting SSL proposed in the paper may fail? If the masking of observation has uniform timespans, a sparsely sampled time series will have a smaller number of samples masked than a densely sampled time series. Because of these unequal masked observations, the model is biased to learn densely sampled time series better than sparsely sampled one.

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
4

### Summary
In this paper, the authors propose an architecture and training scheme for
irregular time series. They propose to patch and mask not specific amounts of
data points, but times-spans that can include more points in denser and lesser
points in sparser regions. Furthermore, the authors propose an architecture
which first use attention inside the patches (Called Irregular Patch Encoding)
and then an attention mechanism between different patches (Global Temporal
Encoding).

The authors test their approach both on regular regression task and on
out-of-domain forecasting.

### Strengths
+ The Architecture and the design decisions seem useful and reasonable. 
+ The results are promising, as Gitar outperforms t-patchGNN which outperforms a lot of the ODE Models.
+ Ablation study shows that indeed all components are needed

### Weaknesses
 - My strongest critique point is the paper writing. The paper on the hand contains a lot of self-advertising sentences which distracts from the "real content". Example:
  - Page 4, Starting at 207: "The first module preserves the original irregular patterns
    while masking and segments the multivariate time series into synchronized, channel-independent
    patches. This approach ensures effective learning of local semantics (i.e., irregular patterns) within
    patches and enhances generalization capability via channel-independent design, reducing process-
    ing complexity, and mitigating long-range information loss"
    -> Why not simply say: "For each channel, we randomly mask a time-span of range q_d and we patch by the time-span lengths instead of    by the amount of points in the patch."
   - On the other hand, a lot of crucial information is missing in the paper:
     - The decoder: How does it look like? Is it an MLP? Just one layer?
     - What does the following mean:
        "This pre-trained reconstruction model R will then be fine-tuned for downstream tasks such as
        forecasting or interpolation on irregular multivariate time series data. To validate its generalization
        capability, we fine-tune R across various domains, encompassing different datasets with varying
        input channels and irregular patterns"
        How exactly does that look like? How does the fine-tuning look like? How do you do for example forecasting? With a forecasting MLP- head as in PatchTST? Or do you just assume that the full forecasting horizon is masked and you apply your normal reconstruction?
      - How do you mask? Randomly select a time-span? How long is the time-span? Does masking means zeroing out? I would formalize and explain such crucial points in detail as instead of just mentioning them shallowly.
    - I was also not able to have a look at the code to answer these questions by myself. I could unfortunately not find a link in the paper and also I could not see any supplementary material.

- In the ablation study, I could not find the answer to the following question: Do you need pre-training at all? How good is your model when being only trained on target forecasting tasks?
- Missing comparison method: Can you compare your method against (https://ojs.aaai.org/index.php/AAAI/article/view/29560)? This paper also outperforms all ODE-based models and may be competitive to your model.

### Questions
- How does your model perform without any pre-training at all? When being just trained on the forecasting tasks?
- How did you collect your baseline results? Do you re-implement all baselines? Because your results for t-PatchGNN, are different then the results reported in the t-PatchGNN paper itself, have a look the table: (https://github.com/usail-hkust/t-PatchGNN). Regarding the results here, t-Patch GNN would be more competitive to your method.
- How exactly does your fine-tuning approach work?
- How exactly does your decoder look like?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces a generalized model for irregular time series regression, leveraging a masking and reconstruction pretraining mechanism. Experimental evaluation is given to show its performance.

### Strengths
The proposed model utilizes a masking and reconstruction pretraining mechanism to capture irregular patterns without requiring labeled data, enabling robust and generalized representations.

### Weaknesses
1. Although some modules are integrated, the motivation is missing in the paper, such as why this specific masking approach is useful over others for handling irregular time series. The authors are suggested to give more theoretical discussions and an intuitionistic example to strongly motivate the work. Note that in terms of the results reported in Table 3,  the PrimeNet method is able to obtain comparable performance than that of the proposed model in most cases.

2. What is the distinction between the two critical research questions the authors propose? They appear to address the same issue, as a robust self-supervised learning framework inherently implies the ability to adapt to different domains. Could the authors clarify how these questions are fundamentally different?

3. The description for Fig1 lacks clarity, making it difficult to understand the intended meaning. It is unclear whether “v1-v3” represents different variables, tasks, or something else. Additionally, if the figure is meant to illustrate a different domains/transfer learning issue, a more detailed explanation would help readers grasp the specific context and purpose of the comparison.

4. From the method and the experimental part, I cannot find how the proposed model learns and captures the claimed local semantics (i.e., irregular patterns) and global temporal dependencies. Could the authors provide more detail on how these aspects are addressed?

5. In addition to self-supervised learning, there are numerous deep generative models for irregular time series, including GANs and diffusion models [1-3]. The authors have not discussed or compared with these types of methods. Besides, the metrics used in Table 3 are not clearly specified. Also, while the authors claim “across PhysioNet to MIMIC,” in the caption of Table 3, it does not seem to present results specifically for the PhysioNet dataset.

### Questions
As provided in weakness.

### Soundness
2

### Presentation
2

### Contribution
2
