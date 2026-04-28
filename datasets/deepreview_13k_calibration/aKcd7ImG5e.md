# Towards a General Time Series Anomaly Detector with Adaptive Bottlenecks and Dual Adversarial Decoders

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6

## Abstract
Time series anomaly detection plays a vital role in a wide range of applications. Existing methods require training one specific model for each dataset, which exhibits limited generalization capability across different target datasets, hindering anomaly detection performance in various scenarios with scarce training data. Aiming at this problem, we propose constructing a general time series anomaly detection model, which is pre-trained on extensive multi-domain datasets and can subsequently apply to a multitude of downstream scenarios. The significant divergence of time series data across different domains presents two primary challenges in building such a general model: (1) meeting the diverse requirements of appropriate information bottlenecks tailored to different datasets in one unified model, and (2) enabling distinguishment between multiple normal and abnormal patterns, both are crucial for effective anomaly detection in various target scenarios. To tackle these two challenges, we propose a General time series anomaly \textbf{D}etector with \textbf{A}daptive Bottlenecks and \textbf{D}ual \textbf{A}dversarial Decoders \textbf{(DADA)}, which enables flexible selection of bottlenecks based on different data and explicitly enhances clear differentiation between normal and abnormal series. We conduct extensive experiments on nine target datasets from different domains. After pre-training on multi-domain data, DADA, serving as a zero-shot anomaly detector for these datasets, still achieves competitive or even superior results compared to those models tailored to each specific dataset.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new general time series anomaly detector with adaptive bottleneck and dual adversarial decoder. By pre-training on multi-domain time series data, anomaly detection is performed efficiently in different target scenarios without domain-specific training.
The overall writing of this article is good and the logic is clear。
This paper first proposes an adaptive bottleneck module to compress features into the latent space, reflecting the different information densities of multi-domain data. It solves the challenge of different requirements for appropriate information bottlenecks for different datasets.
This paper uses dual adversarial decoders to expand the robustness distinction between normal and abnormal modes, improving the general anomaly detection ability in different scenarios.

### Strengths
The overall writing of this article is good and the logic is clear。
This paper first proposes an adaptive bottleneck module to compress features into the latent space, reflecting the different information densities of multi-domain data. It solves the challenge of different requirements for appropriate information bottlenecks for different datasets.
This paper uses dual adversarial decoders to expand the robustness distinction between normal and abnormal modes, improving the general anomaly detection ability in different scenarios.

### Weaknesses
The adaptive router formula of the adaptive bottleneck module proposed in this paper lacks certain innovation, and its formula is similar to the routing function proposed in “PATHFORMER: MULTI-SCALE TRANSFORMERS WITH ADAPTIVE PATHWAYS FOR TIME SERIES FORECASTING”.
Some formulas in this paper lack clear explanations, which may cause some confusion when reading. For example, the reconstruction process proposed in the article is denoted as Recon(·), but there is a lack of detailed description of this process.

### Questions
I hope the author can explain the difference between the routing function proposed in "PATHFORMER: MULTI-SCALE TRANSFORMERS WITH ADAPTIVE PATHWAYS FOR TIME SERIES FORECASTING". At the same time, give a detailed explanation of the reconstruction process Recon(·).

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
5

### Summary
Authors propose a General time series anomaly Detector with Adaptive Bottlenecks and Dual Adversarial Decoders (DADA), which enables flexible selection of bottlenecks based on different data and explicitly enhances clear differentiation between normal and abnormal series. The zero-shot capability is indeed impressive.

### Strengths
The writing is clear and easy to understand.
The pictures and tables in the paper are beautiful and clear.
The proposed method, DADA, can achieve zero-shot.

### Weaknesses
1. AdaBN has almost no difference from the previous moe, yet the author exaggerates their design. I think there is a question of contribution. Moreover, the author does not explain the difference from Moe in the main text nor add relevant references. I think this is somewhat deceptive.
2. The role of AdaBN is not as great as the author claims. See the analysis in question 1. There is excessive exaggeration of contribution.
[a] Shazeer, Noam, et al. "Outrageously large neural networks: The sparsely-gated mixture-of-experts layer." arXiv preprint arXiv:1701.06538 (2017).

### Questions
1. In the ablation experiment, the result of the fourth row is the second highest. In my opinion, AdaBN should be basically equivalent to moe, except for the different dimensions. However, at this time, the model effect is basically close to the final model, which means that the main source of performance is not the specially designed optimization method. This makes me doubt the component innovation of the paper. At the same time, Table 10 in the appendix also supports this conclusion. The result of moe 256 is completely better than the result of the fourth row. This seriously indicates that AdaBN is likely to have a much smaller actual effect than Moe 256. Further, the innovation of AdaBN should be greatly discounted.
2. The experimental analysis lacks the analysis of COMPLEMENTARY MASK MODELING. The author takes this item as the key point of the method but lacks further research.
3. The visualization analysis does not state what dataset is used, nor is there visualization of the original data. Furthermore, there is a lack of visualization comparison with other algorithms, lacking the credibility of the experiment.
4. I hope the author can open source the generation method and generation script of Monash+ and provide a directly usable data set. At present, the explanations in the paper are completely insufficient.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper develops a novel general time series anomaly detection by pre-training on multi-domain time series.  The proposed adaptive bottleneck enables the general model to be applied to various target scenarios without requiring domain-specific training. To improve the general anomaly detection capability, the dual adversarial decoder is further employed to amplify the decision boundary.

### Strengths
1. The general time series anomaly detection plays a key role in the real application.
2. DADA employs the adaptive bottlenecks for multi-domain time series data by dynamically selecting suitable bottleneck sizes. 
3. The effectiveness of both AdaBN and Dual Decoders has been demonstrated in the experiments.

### Weaknesses
1. If anomaly injection is used to establish a supervised setting, this implies that all original samples(some anomalies are included) are treated as normal samples. I suggest the author add an experiment to examine performance under varying levels of anomaly contamination in the training samples. The impact of this assumption on the model's robustness should be thoroughly investigated, especially considering real-world datasets often contain some level of anomalies.
2. During model training, two optimization losses are utilized, along with the optimization approach and any challenges encountered in the optimization process. The visualizations of loss curves for the two losses are essential for further demonstration. It is crucial to understand how these losses interact and whether they converge stably, or if there are oscillations or other problematic behaviors that could affect the model's performance. The specific optimization algorithm used (e.g., Adam, SGD) and its hyperparameters should also be detailed, as these can significantly impact training dynamics.

### Questions
1. Does "anomaly injection" refer to incorporating multiple types of anomaly patterns into each dataset? More details about the implementation of anomaly injection should be included in the paper since it is crucial for conducting the supervised setting.
2. How do you adapt various baseline methods pre-trained on multi-domain datasets for zero-shot evaluation if they are typically utilized in the standard form?
3. How can DADA be applied during the inference step to further fine-tune the target datasets for downstream tasks in the experiments?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes DADA method for general time series anomaly detection, which is pre-trained on extensive multi-domain datasets and perform anomaly detection on various target scenarios without domain-specific training. DADA proposes Adaptive Bottlenecks to addresses the flexible reconstruction requirements of multi-domain data. DADA also employs Dual Adversarial Decoders amplify the decision boundaries between normal time series and common anomalies in an adversarial training way, which improves the general anomaly detection capability across different scenarios. The paper conducts extensive experiments on nine target datasets from different domains, and demonstrate that DADA achieves superior results compared with state-of-the-art models trained specifically for each dataset.

### Strengths
The paper addresses the issue that each dataset in the field of time series anomaly detection requires a specifically trained model, which holds practical significance. The paper proposes a novel method DADA for zero-shot inference on the target domain after pre-training on multiple datasets from different domains. DADA proposes the Adaptive Bottlenecks to addresses the flexible reconstruction requirements of multi-domain data, along with dual adversarial decoders to enhance the clear differentiation between normal and abnormal patterns, showcasing a degree of originality. The paper has a clear structure and expression. In the experimental section of the paper, DADA demonstrates superiority over multiple state-of-the-art methods across nine datasets and provides extensive analysis to prove the necessity of each module, showcasing high quality.

### Weaknesses
1. The paper lacks an analysis of the complementary mask rate's effect on anomaly detection performance. For example, the author could add an experiment to demonstrate the changes in anomaly detection F1-score under various complementary mask rates and explain why this mask performs the best. It is unclear how the specific choice of a 30%/70% complementary mask split was determined, and whether this is optimal for all datasets. A more thorough investigation into the impact of different mask ratios on reconstruction quality and downstream anomaly detection is needed. For instance, does a higher mask rate lead to more robust feature representations, or does it hinder the model's ability to capture essential temporal dependencies?

2. In the experimental section, Figure 4 shows that after fine-tuning, the model's performance improved from 78.48% to 79.90% on MSL and from 84.57% to 85.50% on SMD, an increase of about 1%. The data shows that the improvement of the model after fine-tuning is small. This raises questions about the practical utility of fine-tuning, especially given the computational overhead. A more detailed analysis of the fine-tuning process is needed, including the number of epochs, learning rate, and other hyperparameters. It is also important to consider whether the small gains justify the additional complexity and resources required for fine-tuning.

3. In the ablation study, Table 3 shows that the model performs better when removing the AdaBN, Adversarial, and Dual Decoders modules compared to removing only the Adversarial module. The paper explains that directly maximizing the anomalous time series will increases confusion. Further explanation is needed to clarify why maximizing the anomalous time series leads to increased confusion. Specifically, the interaction between the encoder and the anomaly decoder during adversarial training needs more elaboration. It's not clear why simultaneously maximizing the reconstruction loss for abnormal series by both the encoder and anomaly decoder would lead to confusion, and what specific mechanism causes this effect. A more detailed analysis of the gradients and the learning dynamics during adversarial training is necessary to understand this phenomenon.

4. There are labeling mistakes in the experimental results. For example, in Table 8, the R_AUC_PR value of DADA on the PSM dataset is 47.40, which is less than ModernTCN's 47.48, but 47.40 is bolded. In Table 2, the F1 metric column for the CICIDS dataset is missing a underline marking.

### Questions
1. The paper does not compare the inference time of DADA with the baselines. Compared to the baselines, does DADA have a shorter inference time?  In particular, when compared to other pre-trained models, does DADA have an advantage?

2. In the DADA model, the original data first undergoes complementary masking operations, and then features are extracted by the encoder. In subsection 3.2, it states that the masked portions of the original data input to the encoder have a value of 0, but there may also be 0 values in the non-masked portions of the original data. How does the encoder differentiate between the masked and non-masked portions?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The author propose a solution for general time series anomaly detection, which is call time series anomaly Detector with Adaptive bottlenecks and Dual Adversarial decoders (DADA). This model is  pre-trained on multi-domain time series data. Two components called Adaptive Bottlenecks and Dual Adversarial Decoders is leveraged to enhance the model performance. The model achieves competitive performance on various datasets even compared with SOTA models trained specifically for each dataset.

### Strengths
+ The task on zero-shot time series anomaly detection is quite challenging, the author build a unified end-to-end solution and demonstrate great results. 

+ The paper is well-organized, and it introduces the background and motivation of the proposed methods clearly. The figures also explain their method pretty well.

+ The paper demonstrate its experiment results on enough datasets.  The ablation studies on Sec 4.3 also makes the paper convincible.

### Weaknesses
 - The difference between the pretrain dataset and the evaluation dataset is not listed. How you select those dataset?

- It will be great to specify some more experiment details. Are there any data preprocessing on the input data?

- What's the computation cost(overhead) of importing Adaptive Bottlenecks and Dual Adversarial Decoders? Please specify.

### Questions
- Can you list the data difference between the pretrain dataset and the evaluation dataset? How you select the pretrain dataset?

- Are there any data preprocessing on the input data?

- What's the computation cost(overhead) of importing Adaptive Bottlenecks and Dual Adversarial Decoders? Please specify.

### Soundness
3

### Presentation
4

### Contribution
3
