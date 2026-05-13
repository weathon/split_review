# Mitigating Shortcut Learning with Diffusion Counterfactuals and Diverse Ensembles

- Decision: Reject
- Scores: 5, 3, 5, 6

## Abstract
Spurious correlations in the data, where multiple cues are predictive of the target labels, often lead to a phenomenon known as shortcut learning, where a model relies on erroneous, easy-to-learn cues while ignoring reliable ones. In this work, we propose \emph{DiffDiv} an ensemble diversification framework exploiting Diffusion Probabilistic Models (DPMs) to mitigate this form of bias. We show that at particular training intervals, DPMs can generate images with novel feature combinations, even when trained on samples displaying correlated input features. We leverage this crucial property to generate synthetic counterfactuals to increase model diversity via ensemble disagreement. We show that DPM-guided diversification is sufficient to remove dependence on shortcut cues, without a need for additional supervised signals. We further empirically quantify its efficacy on several diversification objectives, and finally show improved generalization and diversification on par with prior work that relies on auxiliary data collection.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper addresses the shortcut learning problem. It proposes to use diffusion model to generate new samples which contain new feature combinations. The generated samples will be used to train the ensemble classifiers.

### Strengths
The idea of using diffusion models to generate samples with novel feature combination to mitigate short-cut learning makes sense. The paper shows some very interesting findings, such as the relations between the generated sample fidelity vs the diversity. I feel the idea can be useful in mitigating spurious correlations as well.

### Weaknesses
1. The paper claims that the proposed method can mitigate short-cut learning. However, the only evidence it provided is the disagreement between ensemble classifier. It’s not very clear how disagreement in ensemble training can lead to mitigating short-cut learning. Similar works (say Lee et al., 2022) leverages worst class acc (or validation accuracy over majority and minor categories) in datasets like Waterbirds and CelebA. These are direct evidence to show how the proposed method can mitigate short-cut learning. Showing experiments like these can greatly strengthen the paper.

2. Similar to above comments, although Table 1 shows that ensemble classifiers trained with DiffDiv generated samples, rely less on the short-cut feature, it also takes a significantly hit on the majority class accuracy. For example, in ColorDSprites dataset, the Acc drops from 100% to 70% - 90% from baseline to the proposed method. It’s hard to justify that the model learns from a more robust feature set. It would be super helpful if the rebuttal can justify why getting a hit on majority class accuracy is not a big concern. 

3. The paper is using diffusion model training epochs to evaluate the Fidelity. However, it seems to be a very unstable cue, since 3 different datasets the maximum diversity achieved at very different number of epochs, 20 for ColorDSprites, 800 for UTKFace and 1000 for celebA. In Supp 2.2, the paper mentions that using validation loss can be a good early stopping cue. If it’s the case, why not using validation loss to be a measure? I tried to get some insights from Fig. 6. However, it’s quite hard to understand Fig. 6. Especially 3 datasets showed quite different behavior. 

4. From line 242-243, the paper mentions that “L1 and L2 baseline objectives, designed to induce diversity by maximizing the pairwise distance between any two model outputs and the moving average of the ensemble prediction”, however in the loss function, only the average of the prediction is measured. Did I miss anything? 

5. It’s not very clear how the diffusion model is trained, especially some important details such at the size of the model and the structure of the model are missing from the paper. It’s also not clear if the conclusion is sensitive to the structure of the diffusion models or not. It would be helpful to clarify the structure of the diffusion model.

### Questions
It's not clear to me how disagreement in ensemble training can lead to mitigating short-cut learning. It would be really helpful if the authors can help clarify this in the rebuttal. 

I also want to understand the trade-off between the val acc and the disagreement in ensemble training.

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
This paper tackles the challenge of mitigating shortcut learning by introducing an ensemble framework named DiffDiv, which leverages Diffusion Probabilistic Models (DPMs). DiffDiv generates synthetic counterfactual data through DPMs to weaken shortcut dependencies, enhancing prediction diversity within the ensemble. Experimental results demonstrate that DiffDiv successfully guides the model to perform as intended.

### Strengths
- This paper presents a straightforward approach addressing shortcut learning by synthesizing counterfactuals, leveraging the strengths of modern DPMs.

- An in-depth analysis of the impact of sample fidelity on the OODness is nice.

### Weaknesses
 - While DPMs are central to the proposed method, additional details—such as the training scheme specific to this framework, the model's architecture, and the integration of synthetic data during training—would enhance readability. The current visualization results alone feel insufficient. At least, please provide clear and concise explanations of the overall process for integrating synthetic data into training, ensuring ease of understanding. Specifically, the denoising architecture, the precise diffusion training parameters (e.g., the noise schedule, number of steps), and the exact mechanism for how the generated counterfactuals are incorporated into the ensemble training process are missing. This lack of detail makes it difficult to assess the reproducibility and validity of the approach.

- The presentation of the manuscript could be significantly improved. An overview figure of the proposed framework seems essential. Despite the complex components like DPMs in this framework and strategies such as early stopping sampling, the lack of additional explanations makes it challenging for readers to grasp the framework as a whole. Furthermore, the content in Table 1 is difficult to follow. Why are the fractions in Table 1 selected as they are? Also, the reviewer suggests splitting the main quantitative table to highlight the superiority of the proposed method and clearly presenting the ablation study on different diversification objectives for improved readability. The rationale behind the specific fractions used in Table 1 for the synthetic data is unclear, and the lack of a clear explanation makes it difficult to understand the experimental setup and the impact of different synthetic data ratios on the results. The table should also be restructured to better highlight the performance gains of the proposed method compared to baseline approaches and to clearly separate the results of the ablation study on different diversification objectives.

- The paper presents a straightforward solution, but a lack of novelty remains a key concern. While insights like the influence of sample fidelity on OODness and the early-stopping sampling strategy are good, the manuscript would benefit from theoretical analysis if possible, or novel regularizers for DPMs to generate enhanced counterfactuals against spurious correlationsfrom a generative perspective. The current approach relies on an observed phenomenon of DPMs, but lacks a theoretical grounding or a novel mechanism to enhance the counterfactual generation process. A theoretical analysis of why early-stopped DPMs produce OOD samples or the development of specific regularizers to guide DPMs towards generating more effective counterfactuals would significantly improve the novelty and impact of the work.

- Lastly, the proposed framework requires manual tuning for each specific domain or dataset, making it impractical for real-world application and reproducibility. The manuscript would benefit from introducing a universal cheat sheet or automated tuning strategies that perform effectively across diverse scenarios. Specifically, the selection of the diversification hyperparameter (gamma) and the DPM fidelity level requires manual tuning for each dataset. This lack of a systematic approach makes it difficult to apply the method to new datasets without significant effort. The paper should provide clear guidelines or automated strategies for selecting these hyperparameters to enhance the practical applicability and reproducibility of the proposed framework.

### Questions
- The authors consider many objectives for diversificiation such as div, cross, and kl. Is there any reason for this design? If there is an analysis on the selection of diversification objective, it would be better.

- I wonder if the authors have considered the options of using GANs or optimal transport distance to generate synthetic counterfactuals.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a framework, DiffDiv, to mitigate spurious correlations in the data. The framework makes use of DPMs and the authors show that at certain training intervals, even if the model was trained on data with correlated data, it can generate novel feature combinations. Thus, counterfactual data can be generated and used to encourage ensemble diversification.

### Strengths
- The paper was well written and easy to follow.
- Analysis of diversity from DiffDiv was thorough and insightful.
- The idea of using diffusion models for diversification seems promising.

### Weaknesses
 - The framework involves training a DPM which can be expensive for larger datasets. There may be cheaper ways to generate diverse data. E.g., ALIA [1] captions the training images and uses a language model to generate diverse prompts for a text to image. It involves several stages but does not require training a DPM. Furthermore, one of their experiments involves generating data to mitigate spurious correlations. It would also be interesting to compare against generating data from standard augmentations.
- Finding the best DPM epoch for generation in practice seems tricky. Furthermore, the originative interval sometimes leads to generations where the class is ambiguous (e.g., fig 3). 
- Most of the analysis seems to be focused on showing the diversity of the data from DiffDiv. It would be useful to compare the downstream performance from using different types of additional data e.g., from augmentations or using pre-trained diffusion models to edit the training data.

### Questions
- How should the generation epoch be chosen in practice during training time?
- The generalization to different feature combinations of DPMs is not well understood, as mentioned in the limitations section. Thus, given the option of a framework like [1], that is less likely to fail silently, i.e., where we can check from the LLM summary if all features are extracted, what is the advantage of using DiffDiv?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a method using Diffusion models for diversifying sets of ensemble models. The authors use Diffusion models to generate synthetic training data that presents novel feature combinations, even when the original training data has highly correlated features, providing a representation of the original data that covers a broader set of features and hides potentially dangerous short cut cues. The authors demonstrate that using their synthetic data for ensemble training helps improve model generalization to out-of-distribution samples, diversity, and mitigation of shortcut bias.

### Strengths
The paper shows originality by proposing a novel approach to address shortcut learning with DPMs to generate synthetic counterfactuals for ensemble diversification. 

The application of DPMs for mitigating bias without relying on labeled out-of-distribution data is particularly innovative. Through the use of DPMs to generate feature combinations unseen in the training data, the research extends beyond conventional methods that depend on auxiliary datasets or explicit feature labels. 

The authors use a few challenging datasets to demonstrate the efficacy of their method. 

Writing is clear with ample citations provided should it be difficult to follow. 

The paper content has significant practical applications for ML practitioners dealing with entangled factors in their training data.

### Weaknesses
The paper could benefit from more comparisons to competing methods, even if those methods require out-of-distribution data as an assumption without any mechanism in place for data/counterfactual generation. 

More discussion on the advantages of using DPMs for counterfactual generation could be beneficial, particularly some discussion on the generation flexibility of DPMs and how they handle feature disentanglement. 

Despite providing a reasonable method, some of the “work” being done is obfuscated behind the use of DPMs and lack of direct comparisons to other methods.

### Questions
1. Are there more competing methods? Please compare with the state-of-the-art methods. Otherwise, there is no way to assess the proposed method accurately.

2. Have you considered applying the DiffDiv framework beyond computer vision, such as in text or structured data? If so, what challenges or modifications do you anticipate for adapting it to non-visual data? 

3. How do you determine the optimal training stage (e.g., burn-in, originative, exact) for DPMs to generate counterfactuals effectively across different datasets? Could this be automated for practical use? Is there a way to systematically balance sample fidelity and the diversity required for effective training?

### Soundness
3

### Presentation
3

### Contribution
3
