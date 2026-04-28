# Predictive Uncertainty Quantification for Bird's Eye View Segmentation: A Benchmark and Novel Loss Function

- Decision: Accept
- Avg Score: 5.40
- Scores: 6, 6, 3, 6, 6

## Abstract
The fusion of raw sensor data to create a Bird's Eye View (BEV) representation is critical for autonomous vehicle planning and control. Despite the growing interest in using deep learning models for BEV semantic segmentation, anticipating segmentation errors and enhancing the explainability of these models remain under-explored. This paper introduces a comprehensive benchmark for predictive uncertainty quantification in BEV segmentation, evaluating multiple approaches across three popular datasets and two representative backbones. Our study focuses on the effectiveness of the quantified uncertainty in detecting misclassified and out-of-distribution (OOD) pixels, while also improving model calibration. Through empirical analysis, we uncover challenges in existing uncertainty quantification methods and demonstrate the potential of evidential deep learning techniques, which capture both aleatoric and epistemic uncertainty. To address these challenges, we propose a novel loss function, Uncertainty-Focal-Cross-Entropy (UFCE), specifically designed for highly imbalanced data, along with a simple uncertainty-scaling regularization term that improve both uncertainty quantification and model calibration for BEV segmentation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a thorough study on predictive uncertainty quantification of BEVSS and introduces the Uncertainty-Focal-Cross-Entropy (UFCE) loss function to enhance model calibration.  Experiments demonstrate that the uncertainty quantification framework can outperforms baseline methods  in aleatoric uncertainty and calibration in various situations.

### Strengths
+ The paper proposes a novel loss function, Uncertainty-Focal-Cross-Entropy (UFCE), specifically designed for highly imbalanced data, which significantly enhances model calibration and segmentation accuracy.
+ The introduction of an uncertainty-scaling regularization term improves both uncertainty quantification and model calibration for BEV segmentation.
+ The comprehensive  experiments are conducted across three popular datasets, two representative backbones and five uncertainty quantification methods.
+ The theoretical proof is solid.

### Weaknesses
 - Without pseudo OOD, the model performs not well. It is crucial to elucidate the criteria for selecting pseudo OOD data and to discuss its impact on the model's generalization capabilities. Furthermore, an explanation of how varying choices of pseudo OOD data might influence model training would be beneficial. What criteria were used to select the pseudo-OOD data? How sensitive is the model performance to different choices of pseudo-OOD data? Did the authors conduct any ablation studies with different types of pseudo-OOD data?
- As indicated in A.3.1, the selection of parameters like λ and γ varies across different datasets and backbone networks. The experiments should include a comprehensive hyperparameter analysis to illustrate the optimal setting of these parameters for diverse datasets and models. Please discuss any patterns observed in optimal hyperparameter settings across datasets and backbones. If possible, propose guidelines for selecting these hyperparameters on new datasets or architectures.
- While the proposed framework demonstrates notable enhancements over the baseline models, it would be strengthened by a comparison with the latest methods in uncertainty quantification. Is there any specific reason of not choosing more recent baselines instead of LSS and CVT?

### Questions
- It would be better to clarify the meaning and difference between OOD and pseudo-OOD.
- It is also better to provide the clear definition on the evaluation metrics. 
- Is there anything missing in Appendix A.5? There are two empty subsections.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Summary:

This paper is motivated to explored the uncertainty estimation in bird’s-eye-view segmentation task, as uncertainty estimation can be utilized to handle out-of-distribution scenarios and adapt to unexpected conditions, especially in dynamic driving environments.. The contribution is two-folds: 

1. Testing of Uncertainty Quantification: The paper evaluates predictive uncertainty quantification methods in Bird's Eye View (BEV) semantic segmentation with existing datasets, highlighting the model’s ability to detect misclassified and out-of-distribution (OOD) pixels. This incorporates five existing approaches across multiple backbones.
2. New Loss Function – UFCE: The authors claim a novel Uncertainty-Focal-Cross-Entropy (UFCE) loss function. This loss function is designed to handle the challenges of highly imbalanced data, improving both model calibration and the reliability of uncertainty predictions for BEV segmentation tasks. The UFCE loss, inspired by Focal Loss, enhances the model’s focus on uncertain predictions, leading to better aleatoric (data-related) and epistemic (model-related) uncertainty estimation.
3. Improvement in Model Calibration and OOD Detection: The proposed UFCE loss function, coupled with an uncertainty-scaling regularization term, shows superior results over traditional methods, especially in improving the AUPR (Area Under Precision-Recall curve) for OOD detection by approximately 4.758%. The framework achieves high accuracy in segmentation while also performing well in detecting misclassifications and OOD pixels, thus bolstering both model reliability and safety for autonomous vehicle applications.

### Strengths
Strength

1. Effectiveness Across Datasets and Models: Through extensive experiments, the paper demonstrates that the proposed uncertainty quantification framework performs robustly across various datasets (CARLA, nuScenes, Lyft) and model architectures (Lift-Splat-Shoot, Cross-View Transformer), outperforming existing methods on key metrics like AUROC (Area Under ROC Curve) and Expected Calibration Error (ECE).
2. Computational Efficiency: The proposed Evidential Neural Networks (ENN) with UFCE loss achieves comparable or improved results with lower computational complexity compared to methods requiring multiple forward passes, making it practical for real-time applications.
3. Methodical Analysis: The study rigorously evaluates aleatoric and epistemic uncertainties, using metrics like Area Under the ROC Curve (AUROC) and Area Under Precision-Recall Curve (AUPR). Also a runtime efficiency comparison is included as well. This multi-faceted approach allows for a clearer understanding of each method's effectiveness. 
4. Real-world Relevance: By focusing on predictive uncertainty in the context of autonomous vehicles, the research addresses a critical area of real-world application where model reliability and safety are paramount.

### Weaknesses
Weakness:

1. This paper looks more than a study than a question-motivated paper. The benchmark part utilizes existing dataset as well as existing methods and no clear conclusion is drawn from the study. The proposed new loss and the regularization terms are not quite related to the study in terms of motivation. The author is encouraged to explain more on the logical motivation of the proposed new loss function part. 
2. Missing details in experiments part. For different datasets, they have different sensor setting (camera position on the vehicle, FOV, number of camera, number of beams for LiDAR) as well as the scale of bird’s-eye-view grid (0.25m or 0.5m or 1m?). It would be great if the authors could provide a table summarizing the sensor configurations and BEV grid scales for each dataset used in the experiments.
3. Some typos. For example, L49: Aleatoric uncertainty, which arises from inherent randomnesses, such as noisy data and labels. **not sure if it's missing Subject–verb–object or Subject-Link verb-Predicative Structure** L075: We propose the UFCE loss, which we theoretically **demonstrate can** implicitly regularize sample weights, mitigating both under-fitting and over-fitting.

### Questions
Question

1. What is the reason of choosing such pseudo-OOD classes in those dataset? Any statistical supporting evidence here? Or any quantitative justification for the choice of pseudo-OOD classes, such as similarity metrics between the chosen classes and true OOD examples?
2. Also the reason of choosing LSS and CVT as baselines. These two methods are back in 2022 and there are many more advanced BEV segmentation models such as BEVSegFormer[1], PETR-V2[2], and so on. It is suggested that authors either include more recent baselines in their comparison or provide a clear justification for why LSS and CVT were chosen despite the availability of newer methods.

[1] Peng, Lang, Zhirong Chen, Zhangjie Fu, Pengpeng Liang, and Erkang Cheng. "Bevsegformer: Bird's eye view semantic segmentation from arbitrary camera rigs." In Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision, pp. 5935-5943. 2023.

[2] Liu, Yingfei, Junjie Yan, Fan Jia, Shuailin Li, Aqi Gao, Tiancai Wang, and Xiangyu Zhang. "Petrv2: A unified framework for 3d perception from multi-camera images." In Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 3262-3272. 2023.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper addresses the challenge of uncertainty quantification in BEV segmentation, a critical component of autonomous vehicle perception. The authors propose a loss function, called uncertainty-focal-cross-entropy (UFCE), in order to improve uncertainty estimation and calibration of BEV segmentation. The authors conduct a comprehensive benchmark, evaluating various uncertainty quantification methods on popular datasets and backbones.

### Strengths
The paper presents an evaluation benchmark for uncertainty quantification in BEV semantic segmentation, which consists of three datasets like CARLA, nuScenes, and Lyft. 


The benchmark includes two backbones that are proposed for general BEV semantic segmentation. The benchmark provides insights into potential improvements of previous BEV semantic segmentation models.

The paper introduces a novel loss function, UFCE, which is specifically designed for imbalanced data in BEV segmentation.

### Weaknesses
While the paper focuses on uncertainty quantification of the BEV segmentation task, it would be beneficial to explore the impact of uncertainty on other downstream tasks such as motion planning and decision-making of the advanced driver-assistance systems (ADAS). This is a critical aspect for real-world deployment and should be considered for a more complete evaluation of the proposed method.

A more detailed comparison with other state-of-the-art uncertainty quantification methods would strengthen the finding and prove the effectiveness of the proposed loss function. For example, there is only a comparison between UCE and UCFE. The paper should include a more comprehensive analysis of how the proposed method compares to other established techniques.

While the paper focuses on evidential deep learning, a more comprehensive comparison with other uncertainty quantification methods, such as Bayesian neural networks, Monte Carlo dropout, and deep ensembles, would be valuable. The current evaluation lacks a thorough comparison to these established methods, limiting the understanding of the proposed method's relative strengths and weaknesses.

The organization of the results is not easy to follow. For example, Sec. 4.2 presents results from ten tables, but the tables are not well structured. Therefore, the presentation and organization of the experimental results could be improved. The current structure makes it difficult to compare different methods and draw clear conclusions.

The comparison with other robust BEV methods is missing. The paper should include a comparison with existing methods that focus on improving the robustness of BEV segmentation, to better contextualize the contribution of the proposed method.

### Questions
Why is the evidential neural network selected to conduct uncertainty quantification for BEV semantic segmentation? Is only the last softmax function replaced by using the relu function so as to have the Dirichelt distribution of the pixel-wise classification prediction? How about this method compared to other uncertainty estimation methods? 

Is there any comparison between the ENN and other uncertainty measure methods? Or the combination of these methods? For example, the methods mentioned in Sec.2, like Bayesian Neural Networks, Monte Carlo Dropout, and Deep Ensembles? 

How do the authors prove that the UCE loss has also the issue that the optimization reduces the NLL value by increasing the probability of the predicted class? Is there any case study about the limitation of UCE loss?

In Sec. 3.2, the authors claim that the UFCE loss improves the calibration over UCE loss. Is there any detail or training results for comparison? 

For the comparison of calibration between UCE and UFCE, the authors claim that models with focal-based loss exhibit lower ECE scores, indicating better calibration than cross-entropy based models. But in Table 1, the performance of UFCE is not consistently better than UCE. 


The presentation and organization of the experimental results/tables make it difficult to follow. For example, Sec. 4.2 presents the results from Table 1 to 10.  Not all tables need to show comparison with all methods. For instance, some tables can focus on comparing UCE and UFCE.

Are there any visualisation results to show the calibration between UCE and UFCE? 

How about the comparison with the most recent BEV methods? Also the comparison with other robust BEV segmentation models?

### Soundness
2

### Presentation
1

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
The task tackled in this paper is Bird’s Eye View (BEV) semantic segmentation. The authors present  a comprehensive benchmark for predictive uncertainty quantification and introduce a novel loss function, i.e., Uncertainty-Focal-Cross-Entropy
(UFCE). The studies focus on model calibration, uncertainty quantification (detecting misclassified pixels) and out-of-distribution (OOD) detection. The methods are evaluated across three popular datasets and two representative backbones.

### Strengths
- The problems addressed in the paper are very important in the area of safety in neural networks.
- The new loss function presented is well thought out and mathematically motivated.
- The very well-known uncertainty methods are compared with each other. Different datasets are used, both synthetic and real-world.
- The methods are briefly explained in the main part, and details are provided in the appendix. It is a good balance between information and details in the method section.
- The implementation details are very well documented, also the dataset details in terms of creation and splitting etc.
- The complexity analysis and the ablation studies show a good comparison.

### Weaknesses
 - A figure for BEVSS and uncertainty estimation at the beginning of the paper would have an explanatory effect.
- The experiments section is very confusing, constantly going back and forth between results in the main section and in the appendix. Differences between the datasets are not emphasized enough. For example, you could focus on one dataset and one network in the main part and have all the other experiments in the appendix. If the results for the datasets/networks differ, a paragraph with the most important findings could be written.
- The appendix on page 24 is also a bit mixed up with the headings printed, but the tables are in different places.
- I am missing a related work section on the papers that have already dealt with uncertainty estimation and OOD detection for the BEVSS task. This makes it difficult for me to assess the added value of this paper.

### Questions
- The two selected networks seem to be representative, but not SOTA, which would be expected for benchmark paper. What were the reasons for selecting these two networks and how does this choice affect the generalizability of the benchmark results?
- The in-distribution results between the uncertainty methods are very similar and provide little information. What is this supposed to show?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This manuscript introduces a new benchmark and a new approach for predictive uncertainty quantification in Bird’s Eye View Semantic Segmentation (BEVSS) tasks. 

BEV segmentation plays a key role in understanding the vehicle’s surrounding environment by creating a top-down representation using sensor data (e.g., cameras, LiDAR, radar). However, neural networks used for these tasks often produce overconfident predictions on unseen data and underconfident predictions in noisy data. The paper focuses on the two types of uncertainty—aleatoric (caused by noise in data) and epistemic (caused by model uncertainty due to lack of knowledge)—and their impact on safety-critical tasks like autonomous driving.

The authors propose a new loss function called Uncertainty-Focal-Cross-Entropy (UFCE), which mitigates under- and overfitting in BEV segmentation models by integrating regularization on uncertainty. 

Additionally, the paper introduces a benchmark for evaluating five uncertainty quantification methods across three large autonomous driving datasets (CARLA, nuScenes, and Lyft) using two popular BEV segmentation backbones: Lift-Splat-Shoot and Cross-View Transformer. The primary goal is to quantify how well these methods detect misclassified pixels, improve model calibration, and identify out-of-distribution (OOD) data.

Experiments demonstrate that the UFCE loss improves both aleatoric and epistemic uncertainty prediction compared to the existing softmax and ensemble-based approaches. The paper reports a 4.758% improvement in OOD detection performance and gains in misclassification detection. The benchmark serves as a good resource for future work in predictive uncertainty quantification for BEVSS.

### Strengths
(+) The focus on uncertainty quantification for BEV segmentation is highly relevant to real-world applications in autonomous vehicles, where handling uncertain and dynamic environments is crucial for decision-making.

(+) The manuscript provides some good evaluations of uncertainty quantification techniques, analyzing their performance across various autonomous driving datasets and network backbones.

(+) The introduction of the UFCE loss function is a good contribution, effectively enhancing the calibration and uncertainty prediction of BEVSS models. It mitigates the shortcomings of traditional loss functions in handling aleatoric and epistemic uncertainties.

### Weaknesses
(-) While the manuscript provides a thorough benchmark for predictive uncertainty quantification, the individual uncertainty quantification techniques themselves are not particularly novel. Many of these approaches, such as deep ensembles and MC-Dropout, are well-established in the literature, and the work lacks an in-depth exploration of more recent or advanced uncertainty quantification methods. Specifically, the paper does not consider more recent techniques such as those based on normalizing flows or Bayesian neural networks with more sophisticated posterior approximations, which could offer improved uncertainty estimates.

(-) Although the paper addresses both types of uncertainty (aleatoric and epistemic), the explanations regarding how the proposed method specifically handles these uncertainties are not well developed. More technical insights on how the UFCE loss function balances both types of uncertainty and why it is better than existing methods are needed. For instance, the paper does not clearly articulate how the loss function's components interact to disentangle these uncertainties, nor does it provide a theoretical justification for its effectiveness in this regard. A more rigorous analysis of the loss function's properties would be beneficial.

(-) The benchmark, while extensive, is focused primarily on the CARLA, nuScenes, and Lyft datasets. These datasets are useful but do not encompass the full range of scenarios an autonomous vehicle might encounter, particularly when it comes to highly dynamic environments like dense urban settings or environments with poor weather conditions. Evaluating on a wider variety of datasets, including those that feature more diverse sensor modalities or environments, would strengthen the paper’s claims. It would also be interesting to see how the benchmarked models perform on out-of-distribution data, such as those corruption sets from RoboBEV [R1], MapBench [R2], and Robo3D [R3]. Furthermore, the benchmark lacks an analysis of the computational cost associated with each uncertainty quantification method, which is crucial for real-time applications.

(-) The manuscript lacks clarity in some sections, particularly in the technical description of the UFCE loss function and the details of the ablation studies. Some important concepts, such as the handling of noise and sparsity in the LiDAR point clouds, are not adequately explained, which might make it difficult for readers to fully grasp the method’s contributions. For example, the paper does not provide a clear mathematical formulation of how the uncertainty is derived from the network outputs, nor does it detail the specific hyperparameters used in the ablation studies and their impact on the results.

### Questions
- **Q1:** Could the authors provide more detailed insights into how the UFCE loss function handles both aleatoric and epistemic uncertainty in BEVSS? Specifically, what mechanisms within the loss function enable it to balance both types of uncertainty effectively?

---

- **Q2:** How does the proposed UFCE loss function compare to other more recent uncertainty quantification techniques? Are there any specific examples where the UFCE loss provides a distinct advantage over methods such as deep ensembles or MC-Dropout?

---

- **Q3:** The paper discusses its benchmark evaluation on the CARLA, nuScenes, and Lyft datasets. Could the authors provide more information on how well the model performs in more complex or dynamic environments, such as dense urban settings or environments with adverse weather conditions?

---

- **Q4:** Could the authors explain the potential computational overhead of the UFCE loss function and other uncertainty quantification techniques? Specifically, how feasible is the proposed method for real-time applications in autonomous driving, considering resource-constrained environments?

---

- **Q5:** The manuscript lacks comparisons with recent benchmarks such as RoboBEV, MapBench, and Robo3D for out-of-distribution detection. Could the authors conduct additional experiments on these datasets to strengthen the claims about the robustness of their model?

### Soundness
2

### Presentation
2

### Contribution
3
