# OccProphet: Pushing the Efficiency Frontier of Camera-Only 4D Occupancy Forecasting with an Observer-Forecaster-Refiner Framework

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
Predicting variations in complex traffic environments is crucial for the safety of autonomous driving. Recent advancements in occupancy forecasting have enabled forecasting future 3D occupied status in driving environments by observing historical 2D images. However, high computational demands make occupancy forecasting less efficient during training and inference stages, hindering its feasibility for deployment on edge agents. In this paper, we propose a novel framework, *i.e.*, OccProphet, to efficiently and effectively learn occupancy forecasting with significantly lower computational requirements while maintaining forecasting accuracy. OccProphet comprises three lightweight components: Observer, Forecaster, and Refiner. The Observer extracts spatio-temporal features from 3D using the proposed Efficient 4D Aggregation with Tripling-Attention Fusion, while the Forecaster and Refiner conditionally predict and refine future occupancy inferences. Experimental results on nuScenes, Lyft-Level5, and nuScenes-Occupancy datasets demonstrate that OccProphet is both training- and inference-friendly. OccProphet reduces 58\%$\sim$78\% of the computational cost with a $2.6 \times$ speedup compared with the state-of-the-art Cam4DOcc. Moreover, it achieves 4\%$\sim$18\% relatively higher forecasting accuracy. The code will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces OccProphet, a novel camera-only framework for occupancy forecasting. It features an Observer-Forecaster-Refiner pipeline optimized for efficient training and inference, utilizing 4D aggregation and tripling-attention fusion on reduced-resolution features. Experimental results show that OccProphet outperforms existing methods in both accuracy and efficiency.

### Strengths
1. The article is well-written and easy-to-follow.
2. Figure 2 is helpful to understand the effect of OccProphet.
3. The ablation study is helpful in demonstrating the benefits of each module in OccProphet.
4. Extensive experimental results on several benchmarks back up the effectiveness of OccProphet.

### Weaknesses
1. Some symbols and design details of the model are unclear.
2. The analysis of failure scenarios is lacking, but this is not a major concern.
3. See Questions.

### Questions
1. What part of the Cam4DOcc model contributes to its high computational cost? How much memory does Cam4DOcc use during training and testing? Approximately how many GPU days are needed for full training?

2. In multi-frame 3D occupancy results, how can environmental dynamics be effectively captured? The proposed Observer-Forecaster-Refiner pipeline seems to learn the dynamics of objects in the latent space without strict physical constraints. If the real world presents scenarios that are rare or unseen in the dataset, could 4D predictions fail? Are there any examples of such failures?

3. 4D prediction is challenging, especially when occlusions are frequent, leading to potential voxel loss. Have the labels in the 4D dataset been completed to account for these occlusions? If they have, can the authors' method handle situations where any frame from the historical RGB images loses an object?


4. Are the 6-DoF camera parameters in the Observer used to align historical 3D features with the current frame? In lines 188-191, why does F change to F_{motion}, resulting in an extra matrix dimension of 6×X×Y×Z? Is this converting the 6-DoF pose into a matrix?

5. In lines 206-207, how does C+6 become C? Is this done through a 1×1×1 3D convolution?

6. What is the difference between the E4A module shown in Figure 4 and the UNet structure? It looks like a 4D version of UNet. Why does the FLOPs increase significantly while the number of parameters in E4A decreases? Is this due to the upsampling process?

7. In TAF, after applying 3D, 2D, and 1D global average pooling, the same scale features perform temporal attention. Would cross-attention between different scales yield better results?

8. In the Forecaster, is the condition for prediction learned from past voxels?

9. What does the colon symbol in line 313 mean?

10. The comparisons could be more thorough. For example, it would be helpful to follow the output of the 4D BEV method, like [1], with a 2D to 3D detection head for comparison.
[1] Bevdet4d: Exploit temporal cues in multi-camera 3D object detection

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
OccProphet is an efficient occupancy forecasting framework for autonomous driving, reducing computational costs by 58%–78% and achieving a 2.6× speedup over existing methods while maintaining high accuracy. Through its Observer, Forecaster, and Refiner modules, OccProphet predicts future 3D occupancy from 2D images, making it suitable for real-time edge deployment.

### Strengths
a). OccProphet addresses the computational limitations of previous methods, a crucial improvement for deploying autonomous vehicles on edge devices.

b). The authors’ writing style is clear and concise, effectively conveying the ideas and concepts of 4D occupancy prediction.

### Weaknesses
a) Although the authors have distinctively named the three components as Observer, Forecaster, and Refiner to differentiate them from previous methods, the paper should more clearly highlight the distinctions from the traditional encoder-decoder architecture to better emphasize its contribution.

b) The tripling-attention and reduced-resolution feature aggregation may sacrifice some granularity or detail in the forecasts, possibly affecting the precision of the model in dense scenarios.

c) The paper lacks details on how well the model performs over varying forecasting time horizons, especially under extended timeframes, which are critical in autonomous driving scenarios.

### Questions
The current baselines lack sufficient comparison methods and evaluation metrics, which are inadequate to demonstrate the superiority of the proposed approach.

### Soundness
3

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
This paper propose a method called OCCPROPHET for efficient occupancy forecasting with camera-only inputs. The proposed framework is consisted of Observer, Forecaster, and Refiner. OCCPROPHET first embeds the sequence of camera images into 3D voxel features. Then Observer applies 4D feature aggregation to gradually reduce the spatial resolution of the 3D features and a tripling-attention fusion strategy on the lower-resolution 3D features to reduce information loss. The Forecaster component forecast the state of the environment based on the feature output from Observer. Finally, Refiner utilize temporal relationship to enhance the quality of the 3D voxel features to generate the final prediction of future occupancy. The key idea is reducing spatial resolution at the very beginning of the network to reduce computational cost during embedding and forecasting. The tripling-attention part take spatiotemporal interactions into account to reduce the information loss and the Refiner part makes use of temporal correspondence to increase the granularity of the prediction. The proposed method makes a good trade-off between efficiency and effectiveness. The extensive experiment results show that OCCPROPHET largely reduce computational cost while achieving slightly better performance.

### Strengths
This paper propose OCCPROPHET to improve the efficiency of occupancy forecasting algorithm while maintaining and even improving the performance. The key idea is to embed a coarse-level 3D voxel features at the very beginning of the network to reduce computational cost and meanwhile utilize the temporal-spatial relationship to reduce information loss during embedding and forecasting. Finally, in order to guarantee prediction quality, the Refiner part enhance the feature quality with temporal-spatial correspondence and increase the granularity of the prediction. OCCPROPHET provides a better balance between efficiency and effectiveness in occupancy forecasting problem. The experiments are extensive and the results demonstrate both the efficiency and effectiveness of OCCPROPHET.

### Weaknesses
The reviewer is concerned about the effectiveness part of OCCPROPHET. Since OCCPROPHET reduce spatial resolution at the beginning of the network, there should be information loss no matter what strategy OCCPROPHET uses to compensate that. At the same time, temporal-spatial interaction should also be utilized in OCFNet (Cam4DOcc). The reviewer is a bit confused about the better performance OCCPROPHET shows than that of OCFNet (Cam4DOcc). The reviewer is concerned about whether the performance improvement stems from the fact that OCFNet (Cam4DOcc) is underfit and OCCPROPHET converges faster.

### Questions
1) Could the authors show experiment results on training for longer with both OCFNet (Cam4DOcc) and OCCPROPHET to see whether the performance improvement stems from early convergence.

2) If not, is there any analysis or explanation about the performance improvement with respect to the information loss?

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
3

### Summary
The paper introduces a novel framework named OccProphet, designed to predict the 3D occupied status of driving environments based on historical 2D images, with a focus on improving efficiency and reducing computational demands during training and inference stages. This is particularly aimed at enhancing the feasibility of deploying such technology on edge agents like autonomous vehicles.The OccProphet framework consists of three lightweight components: the Observer, Forecaster, and Refiner. The Observer extracts spatio-temporal features from 3D data using an Efficient 4D Aggregation with Tripling-Attention Fusion method. The Forecaster and Refiner work together to conditionally predict and refine future occupancy inferences. The paper claims that OccProphet is both training- and inference-friendly, reducing computational costs by 58% to 78% with a 2.6x speedup compared to the state-of-the-art Cam4DOcc method, while achieving 4% to 18% higher forecasting accuracy. The experimental results are demonstrated using the nuScenes, Lyft-Level5, and nuScenes-Occupancy datasets.

### Strengths
1. The paper introduces a new framework, OccProphet, which is designed to be efficient and effective for camera-only 4D occupancy forecasting, a critical capability for autonomous driving.
2. The framework significantly lowers computational requirements by 58% to 78% compared to the state-of-the-art Cam4DOcc, making it more feasible for deployment on edge agents like autonomous vehicles.
3. OccProphet achieves a relative increase in forecasting accuracy of 4% to 18% over existing methods, which is a substantial improvement in the field of autonomous driving perception.

### Weaknesses
The paper does not give detailed explanations for the design of the three proposed modules.

### Questions
What is the actual frames-per-second of the model. And is it good enough for deployment?

### Soundness
3

### Presentation
3

### Contribution
3
