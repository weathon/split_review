# Will the Inclusion of Generated Data Amplify Bias Across Generations in Future Image Classification Models?

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
\nnfootnote{$\star$ indicates equal contribution with random order.}
As the demand for high-quality training data escalates, researchers have increasingly turned to generative models to create synthetic data, addressing data scarcity and enabling continuous model improvement. However, reliance on self-generated data introduces a critical question: \textit{Will this practice amplify bias in future models?} While most research has focused on overall performance, the impact on model bias, particularly subgroup bias, remains underexplored. In this work, we investigate the effects of the generated data on image classification tasks, with a specific focus on bias. We develop a practical simulation environment that integrates a self-consuming loop, where the generative model and classification model are trained synergistically. Hundreds of experiments are conducted on Colorized MNIST, CIFAR-20/100, and Hard ImageNet datasets to reveal changes in fairness metrics across generations. In addition, we provide a conjecture to explain the bias dynamics when training models on continuously augmented datasets across generations. Our findings contribute to the ongoing debate on the implications of synthetic data for fairness in real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the bias implications of incorporating generated data from generative models into training downstream tasks. The authors propose an iterative pipeline that repeatedly uses new generators to create additional images that enhance training. Their analysis spans three image datasets of varying complexity, exploring both performance improvements and bias impacts on downstream classification tasks. Bias is examined across different subgroups, covering both single and multiple bias interactions. Through this setup, they observe mixed trends in performance and bias effects across datasets of different complexities and model capacities. The paper concludes with a high-level discussion on potential root causes behind these varied results.

### Strengths
- This paper addresses a highly relevant topic by examining the implications of generated data on bias, which is essential for advancing our understanding of the gaps between generated and real data.
- The iterative pipeline for incorporating generated data closely resembles real-world applications. By using datasets of varying complexity and models with different capacities, the study effectively explores different aspects of the problem, enhancing the generalizability of the findings.
- The study provides noteworthy observations with good experimentation support, such as the low correlation between dataset bias and resulting bias effects, the higher susceptibility of pre-trained models to integration bias, and insights into how different factors affect bias across datasets and models.

### Weaknesses
 - The paper presents mixed findings across datasets and models but does not provide in-depth explanations for these variations. While section 5 includes some discussion on the root causes of observed behaviors, this analysis remains at a high-level and is not well-supported or directly connected to the experiments in earlier sections. The analysis would be more convincing with clearer connections to the results, reinforcing the paper’s claims with evidence from the experiments. For instance, the discussion does not delve into why pre-trained models are more susceptible to integration bias, or why certain datasets show more consistent bias trends than others. A more granular analysis, perhaps by examining the feature space learned by different models or by analyzing the specific types of errors made on different subgroups, would strengthen the conclusions.
- In table 1, FID fluctuates for Color-MNIST and CIFAR10 after several rounds of data generation, while it increases substantially for HARD-ImageNet starting from the second iteration. This trend suggests a marked difference in data quality for HARD-ImageNet compared to the other datasets. However, the subsequent experiments focus primarily on how generated data impacts downstream performance and bias without addressing how this observed FID trend might influence these results. A discussion on how the data quality (assessed by FID) could affect interpretations across the three datasets would enhance the clarity of the findings. For example, it is unclear whether the increasing FID for HARD-ImageNet is due to the generative model drifting away from the original data distribution, or if it is simply generating more diverse (but not necessarily lower quality) images. This distinction is crucial for interpreting the downstream task results.
- Some methodology details are lacking, making it challenging to fully understand and replicate the study. For example, in section 3.2, there is limited information on the design of the human study, the impact of expert-guided filtering on image quality, and the specific r% used. The paper would benefit from some recommendation on the usage of generated data in generative models or downstream tasks with the insights from the experiments. Specifically, the criteria used by human experts for filtering images are not defined, and it is unclear how this subjective process might introduce additional biases. Furthermore, the paper does not specify how the r% was determined for each dataset, making it difficult to assess the sensitivity of the results to this parameter.

### Questions
1. Can you provide more detail on the human study in section 3.2, and the r% used?
1. What is the impact of image quality from the expert-guided filtering in section 3.2? 
1. How well does the findings generalize to other dataset? For example, section 4.2 showed dataset bias does not amplify model bias. Do authors expect that to hold for other datasets, too?

### Soundness
3

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
3

### Summary
With the growing prevalence of generative models, the authors raised the concern regarding model bias, particularly in the context of generation and retraining cycles. Then the authors developed a simulation environment and conducted extensive experiments on image classification datasets to reveal how fairness metrics evolve across successive generations.

### Strengths
S1. The scenario proposed by the authors is highly relevant, as synthetic data is increasingly shared online and integrated into various domains. More studies on how the synthetic data will affect model training in generations will be beneficial for the research community.

S2. The experiments on the proposed dataset are extensive, e.g., w/ or w/o biased initialization, different base models.

### Weaknesses
W1. Lack of experiments on the choice of generative models. Various generative models can differ in behavior, the choice of model likely impacts sample quality and influences the outcomes of subsequent studies.

W2. The motivation of the paper is on future image classification synthetic data plays in it. With foundational models playing a dominant role, integrating settings like synthetic data for transfer learning in classification will enhance the paper better, going beyond the current base case that may lack scalability.

W3. The experiments are mainly targeting the model bias within a self-consuming loop in image classification domain. However, the conclusions/observations are not significant.

### Questions
Q1. How many synthetic data are added or ratio p? Is there a rationale behind the choice of p.

Q2. Are there any experiments or preliminary results on tasks with a larger number of classes?

Q3. How is CLIP used in filtering? Specifically, is it based on the similarity score between label texts and images?

Q4. Would different losses lead to varying results?

Q5. Any insights on how could the conclusion generalize to other tasks, or other modality?

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
4

### Summary
The paper attempts to analyze whether the inclusion of generated data alleviates the model bias. In the paper, the authors repeatedly train generative models on the generated augmented data and study its impact on multiple fairness metrics.

### Strengths
The paper is studying a new problem. In the era of generative AI, more generated content is available on the Internet. Training on the generated data may influence model performance. In this sense, the paper is studying a valid and important problem.

### Weaknesses
The paper mostly conducts experiments on three datasets. Among the three datasets, Colourized-MNIST and CIFAR20/100 are very small datasets in terms of the resolutions and the number of data and classes compared to the existing image data. Moreover, the largest model used in the paper is ResNet50, which is a relatively small network when compared to SOTA models like ViT. This raises the concern of whether the observations from the experiments are still valid in realistic scenarios with large datasets and models.

Some experimental results are hard to understand.
- baseline performance. To my understanding, CIFAR20/100 has a smaller number of classes and should be an easier dataset to classify when compared to CIFAR100. However, the baseline performance of ResNet50 on CIFAR100 is around 80%; on CIFAR20/100 is around 50%.
- The trends are inconsistent between models. For example, in Fig. 6(a), ResNet50 and LeNet show an opposite trend in Equal Opportunity and Disparate Impact but the same trend in average accuracy and Maximal Disparity; VGG-19 remains unchanged for the tested metrics.
- The trends are inconsistent between datasets. For example, comparing the ResNet50 baseline between Fig 5(a) on CIFAR-20/100 and 6(a) on CIFAR-100. Even though the datasets are similar, the ResNet50 baseline shows a totally different trend for the Equal Opportunity, Disparate Impact, and Maximal Disparity metrics. 
- Similar discrepancies are noted in other sections of the paper. The experimental findings do not appear to explain how the generated data affects model bias in general.

The conclusion is weak. Based on the observations, the authors conjectured that the model bias is affected by multiple factors, including the datasets, models, and data quality across generations. However, the authors did not provide clear experiment evidence or solid theory explaining how these factors influence the model bias.

### Questions
The authors reported the FID score for the augmented data from multiple generations in Table 1. It seems that the FID scores for unbiased colorized MNIST show a decreasing trend; biased colorized MNIST is more or less the same; CIFAR-20/100 decreases first and then increases; Hard ImageNet shows a sudden increase from 50.9 to 186.4. Can the author explain the inconsistent changes here? Are there any implications from the observations? Also, it would be better if the author could visualize the generated images from different generations to visually see the changes across generations.

The authors mentioned, “We manually partition the original dataset into multiple subgroups, where subgroups within the same class share similar semantics.” Can the authors explain more clearly how they defined and constructed the subgroups for each dataset?

### Soundness
2

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
3

### Summary
Great:
The authors investigated an important question on a selected dataset. The future work can be extended to other hierarchical sub-groups and more datasets.
Limited benchmark results are apparent and convincing.

Missing:
It will be helpful to accept the claim with more extensive experiments and analysis.
According to me, citations to the original work/s are missing.
The final section can be elaborated to cover the important findings that support the main problem.

Without additions:
It's a strong acceptance for a poster.
Weak acceptance for the main track.

Explanation:
1. The experiments: If possible, I would like to see the results from other standard datasets or more subgroups for the dataset used.
2. Citations: Some original works in the introduction section and later are missing citations. If the authors think they have cited all the necessary work, please put that in a rebuttal.
3. Conclusion and future work: I think it can be improved or extended to connect with the problem and story.

### Strengths
The authors investigated an important question on a selected dataset. The future work can be extended to other hierarchical sub-groups and more datasets.
Limited benchmark results are apparent and convincing

### Weaknesses
It will be helpful to accept the claim with more extensive experiments and analysis. 
According to me, citations to the original work/s are missing.
The final section can be elaborated to cover the important findings that support the main problem.

### Questions
Look at weakness section to know what to improve.

### Soundness
3

### Presentation
2

### Contribution
2
