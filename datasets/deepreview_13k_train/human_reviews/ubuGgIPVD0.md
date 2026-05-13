# TSTTC: A Large-Scale Dataset for Time-to-Contact Estimation in Driving Scenarios

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Time-to-Contact (TTC) estimation is a critical task for assessing collision risk and is widely used in various driver assistance and autonomous driving systems. The past few decades have witnessed development of related theories and algorithms. The prevalent learning-based methods call for a large-scale TTC dataset in real-world scenarios. In this work, we present a large-scale object oriented TTC dataset in the driving scene for promoting the TTC estimation by a monocular camera. To collect valuable samples and make data with different TTC values relatively balanced, we go through thousands of hours of driving data and select over 200K sequences with a preset data distribution. To augment the quantity of small TTC cases, we also generate clips using the latest Neural rendering methods. Additionally, we provide several simple yet effective TTC estimation baselines and evaluate them extensively on the proposed dataset to demonstrate their effectiveness. The proposed dataset is publicly available at \url{https://open-dataset.tusen.ai/TSTTC}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a time-to-contact dataset for the safety requirements of the redundancy system in ADAS. In addition to being collected from real-world scenarios, the dataset also introduces NeRF scenes to further extend the number of safety critic scenarios. Other than the dataset, this paper also models the TTC estimation problem as estimating the scale ratio of 2D bounding boxes, thus making the TTC problem solvable using image pairs solely, and introduces Pixel MSE and Deep Scale accordingly. Experiments demonstrate the effectiveness,

### Strengths
1. The time-to-contact estimation task makes sense to me. Though some existing tasks like depth estimation and velocity estimation, or motion prediction can be used to solve this task as well, using TTC system as a redundancy system makes sense to me.

### Weaknesses
1. It is unclear about the quality of the ground-truth labels. The authors should conduct experiments to show the quality of labels. Specifically, the authors should investigate the noise level in the ground truth TTC values, perhaps by analyzing the distribution of errors or comparing against a small subset of manually verified labels. This is crucial for establishing the reliability of the dataset.

2. Albeit the dataset is large, what does the dataset bring? Can other methods benefit from using the dataset? In other words, a cross-dataset experiment is needed. The authors should demonstrate the generalizability of the dataset by evaluating existing TTC estimation methods on it and showing how performance compares to their original datasets. This would highlight the value of the new dataset.

3. The introduction of the Nerf dataset is somewhat unclear. Why should it be used? How realistic is the dataset? The authors need to provide a clear justification for using the NeRF dataset, explaining how it complements the real-world data and what specific advantages it offers for training or evaluation. A discussion on the limitations of the NeRF dataset in terms of realism is also necessary.

4. The authors use the MiD metric as the main metric rather than the RTE metric by stating that "Due to the instability of TTC at larger value". This makes the reviewer wonder about the validity of the TTC metric and the correctness of the proposed approaches. The authors should provide a more thorough analysis of why RTE is unstable and justify the use of MiD. A comparison of the performance of both metrics would be beneficial.

### Questions
See weakness.

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
4

### Summary
This work proposes a Time-to-Contact dataset and two baselines to estimate time-to-contact. Time-to-Contact (TTC), the time for an object to collide with the observer's plane, is an important metric in autonomous driving. Vision-based, especially RGB-based TTC estimation method is needed for cost-efficiency.

### Strengths
1. A Large dataset.

2. Promising performance.

### Weaknesses
1. The layout caption of Figure 2 on page 5 requires refinement. 
2. It is recommended that the author provide a flowchart to illustrate further details on the continuous monocular image generation of NeRF images.
3. Lighting conditions (such as nighttime or low-light environments) or weather (such as rain or snow) affect the quality of NeRF rendering? The author could include some statistics regarding these factors in the dataset, as these issues are highly relevant in autonomous driving scenarios. Specifically, the impact of these conditions on depth estimation and subsequent TTC calculation should be analyzed. For example, how does the accuracy of depth maps from NeRF degrade under heavy rain, and what is the corresponding impact on TTC estimation? 
4. In real driving scenarios, the motion trajectories of objects can be highly complex, which may lead to cumulative errors in speed and depth estimation, ultimately affecting the accuracy of TTC estimation. It is recommended that the author, after the derivation of the formulas, further discuss how to reduce the impact of these errors on the final results, for example, by using filtering or other smoothing techniques. The discussion should include specific methods, such as Kalman filtering or moving average techniques, and how these methods can be integrated into the TTC estimation pipeline to mitigate the effects of noisy or inaccurate trajectory data. 
5. In the future, it is necessary to increase the diversity of scene types in the dataset.

### Questions
1. It is unclear why object-level TTC is used rather than pixel-level TTC. It seems that pixel-level TTC is more informative than object-level TTC.

2. The objective of the proposed baseline is to estimate the ratio of objects. Can we use an object detection algorithm to perform such a task? Why should we use the proposed baselines? I have found that there is an object detection method (SOT) in the experiment. Is the SOT method retrained or finetuned on the proposed dataset?

3. What is the LIDAR model used in Table 2?

**Minors**
1. Line 064, what does "class 8" mean?

2. The authors state that "due to page limitation", the overall RTE metic is reported. The page limitation of ICLR is 10 pages, so please present more results.

3. Line 238: How do you obtain the velocity of the vehicle? Through using which data by what means? Please be specific. Is the velocity data provided by radar accurate?

4. Line 238, How exactly do you fit the velocity by the depth?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a large-scale monocular Time-to-Collision (TTC) dataset for driving scenarios, including both 2D and 3D NeRF (Neural Radiance Field) image data. Additionally, it introduces two simple yet effective TTC estimation algorithms to validate the effectiveness of the proposed approach. Future work will focus on expanding the types of scenarios in the dataset or incorporating more safety-critical situations. Overall, this paper offers new insights into TTC estimation methods in the field of autonomous driving.

### Strengths
1.	The author provides a very detailed explanation of the dataset processing.
2.	This work builds a large-scale TTC dataset and provides a simple yet effective TTC estimation algorithm as baselines for the community.

### Weaknesses
(-) The addition of NeRF-generated sequences is an interesting idea, but the exact impact of these synthetic data on the model’s generalization capabilities is not sufficiently explored. More detailed analysis of how much NeRF data improves performance, especially on smaller TTC values, would be helpful. Specifically, it's unclear if the NeRF data is truly bridging the gap in the distribution of real-world small TTC values, or if it's introducing a bias due to the synthetic nature of the data. A comparison of model performance on real-world small TTC data with and without the NeRF augmentation would be crucial to validate this approach.

(-) The manuscript lacks thorough ablation studies for the proposed Pixel MSE and Deep Scale methods. It would be beneficial to break down the impact of different components (e.g., center shift, different scale bins) and analyze their contributions to the final performance. For instance, how does the choice of scale bins affect the accuracy of TTC estimation, and is there an optimal configuration? Similarly, the center shift parameter needs more justification; is it a fixed value, or is it learned? If it is fixed, what is the rationale behind the chosen value? A detailed analysis of these parameters is essential for understanding the method's sensitivity and robustness.

(-) The manuscript does not address the computational complexity or real-time performance of the proposed TTC estimation methods. In real-world applications like autonomous driving, it is crucial to assess the trade-off between accuracy and computational cost, especially for resource-constrained systems. The authors should provide a detailed analysis of the inference time for both Pixel MSE and Deep Scale methods, including the hardware used for testing. This analysis should also consider the impact of different input resolutions on the computational cost. It is also important to discuss the memory footprint of the models, which is a crucial factor for deployment on embedded systems.

(-) The dataset is primarily focused on highway and urban driving scenes, which limits its applicability in more complex scenarios like pedestrian-rich environments or non-vehicle objects. Including data for other road users, such as pedestrians and cyclists, would broaden the scope of the dataset. Furthermore, the current dataset seems to focus on scenarios with clear visibility. It would be beneficial to include more challenging scenarios with occlusions, varying weather conditions, and different lighting conditions to improve the robustness of TTC estimation methods.

### Questions
1. Please provide more details for the NeRF rendering concerning different weather and light conditions.
2. The trajectory feature is hard to maintain in complex driving scenes, and the solutions are preferred for reducing the impact of the cumulative errors in trajectories for final results.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The manuscript introduces TSTTC, a large-scale dataset for Time-to-Contact (TTC) estimation in driving scenarios. 

TTC is a key metric in ADAS for assessing collision risks, which is essential for subsystems like Adaptive Cruise Control (ACC) and Automated Emergency Braking (AEB). The authors argue that there is a scarcity of real-world, large-scale TTC datasets, which has historically limited the effectiveness of deep learning-based TTC estimation methods.

To address this gap, the authors have constructed a dataset comprising 206K sequences from real-world driving scenes (highway and urban), supplemented by 1K sequences generated using NeRF for scenarios with small TTC values. Each sequence contains six consecutive frames captured at 10 Hz, annotated with 2D and 3D bounding boxes and ground-truth TTC values for vehicles.

Additionally, the manuscript proposes two baseline TTC estimation methods: Pixel MSE and Deep Scale. Both methods rely on calculating the scale ratio between consecutive frames to estimate TTC, with the latter using deep learning to enhance accuracy. 

The authors evaluate these methods on the TSTTC dataset, reporting some good improvements in terms of Motion-in-Depth (MiD) and Relative TTC Error (RTE). The results demonstrate that Deep Scale outperforms traditional depth estimation and other baselines.

The work highlights the benefits of their dataset for future TTC estimation research and emphasizes the importance of real-world datasets in improving the robustness of TTC predictions in autonomous driving systems.

### Strengths
(+) The TSTTC dataset is a valuable contribution to the community, filling a notable gap by providing a large-scale, real-world dataset specifically tailored for TTC estimation. The dataset’s focus on both urban and highway driving scenarios, combined with a wide depth range (up to 400 meters), makes it highly relevant for autonomous driving applications.

(+) The paper presents a solution to the problem of data scarcity in small TTC cases by augmenting the dataset with NeRF-generated sequences. This approach is proposed to address the imbalance in real-world data.

(+) The proposed TTC estimation methods (Pixel MSE and Deep Scale) are well-executed. The results on various metrics such as MiD and RTE demonstrate the efficacy of the methods in practical driving scenarios, providing useful baselines for future research.

### Weaknesses
(-) The addition of NeRF-generated sequences is an interesting idea, but the exact impact of these synthetic data on the model’s generalization capabilities is not sufficiently explored. More detailed analysis of how much NeRF data improves performance, especially on smaller TTC values, would be helpful.

(-) The manuscript lacks thorough ablation studies for the proposed Pixel MSE and Deep Scale methods. It would be beneficial to break down the impact of different components (e.g., center shift, different scale bins) and analyze their contributions to the final performance.

(-) The manuscript does not address the computational complexity or real-time performance of the proposed TTC estimation methods. In real-world applications like autonomous driving, it is crucial to assess the trade-off between accuracy and computational cost, especially for resource-constrained systems.

(-) The dataset is primarily focused on highway and urban driving scenes, which limits its applicability in more complex scenarios like pedestrian-rich environments or non-vehicle objects. Including data for other road users, such as pedestrians and cyclists, would broaden the scope of the dataset.

---

### Justification of Rating

While I do not have extensive experience in evaluating dataset papers, I can appreciate the significance of introducing the TSTTC dataset for TTC estimation in autonomous driving scenarios. 

The dataset fills a notable gap by providing large-scale, real-world data for both urban and highway driving, which will undoubtedly be useful for researchers working on Time-to-Contact estimation tasks. The inclusion of NeRF-generated sequences for small TTC cases is an innovative approach to addressing the imbalance in real-world data, although a more detailed analysis of the impact of this synthetic data is needed.

The proposed TTC estimation methods, Pixel MSE, and Deep Scale, provide useful baselines for further research, but the manuscript could be improved by discussing their computational complexity and real-time performance, which are crucial factors for practical deployment in ADAS systems. 

Additionally, the paper lacks thorough ablation studies and analysis of the individual contributions of different components in the methods. 

Given these factors, I would leave more room for other reviewers to determine the overall contribution and novelty of this work.

### Questions
- **Q1:** Could the authors provide a more detailed analysis of the impact of NeRF-generated data on the model’s generalization capabilities, especially for smaller TTC values? How much do these synthetic sequences contribute to performance improvements?

---

- **Q2:** The manuscript lacks ablation studies. Could the authors provide more details on the individual contributions of the components in the proposed methods, such as the center shift or scale bins? This would help clarify the relative importance of each element in the final performance.

---

- **Q3:** The paper does not discuss the computational complexity or real-time performance of the proposed methods. How do Pixel MSE and Deep Scale perform in terms of runtime, and are they suitable for real-time applications in ADAS?

---

- **Q4:** The dataset primarily focuses on vehicles in highway and urban scenarios. Do the authors have plans to extend the dataset to more complex environments, such as pedestrian-rich or mixed-traffic scenarios? If so, how would the proposed methods perform in these cases?

### Soundness
3

### Presentation
3

### Contribution
3
