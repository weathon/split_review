# Enhancing End-to-End Autonomous Driving with Latent World Model

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
End-to-end autonomous driving has garnered widespread attention. 
Current end-to-end approaches largely rely on the supervision from perception tasks such as detection, tracking, and map segmentation to aid in learning scene representations. 
However, these methods require extensive annotations, hindering the data scalability.
To address this challenge, we propose a novel self-supervised method to enhance end-to-end driving without the need for costly labels. 
Specifically, our framework \textbf{LAW} uses a LAtent World model to predict future latent features based on the predicted ego actions and the latent feature of the current frame.
The predicted latent features are supervised by the actually observed features in the future.
This supervision jointly optimizes the latent feature learning and action prediction, which greatly enhances the driving performance.
As a result, our approach achieves state-of-the-art performance in both open-loop and closed-loop benchmarks without costly annotations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces LAW (LAtent World model), a self-supervised learning approach for end-to-end autonomous driving. The key innovation is using a latent world model to predict future scene features based on current features and ego trajectories. The method can be integrated into both perception-free and perception-based frameworks, predicting either perspective-view features or BEV (Bird's Eye View) features respectively. The authors demonstrate state-of-the-art performance across multiple benchmarks including nuScenes, NAVSIM, and CARLA simulator.

### Strengths
1. Novel integration of world model concepts into end-to-end driving
2. Comprehensive experimental validation across multiple benchmarks. Demonstrates practical improvements in both closed and open-loop settings

### Weaknesses
1. Limited discussion of computational overhead - no analysis of inference time or model size. Autonomous driving systems must make decisions in real-time, typically requiring processing speeds of at least 10-20 Hz (decisions every 50-100ms). Without inference time analysis, it's unclear if LAW is applicable for real deployment on edge computing devices. Specifically, the paper lacks a breakdown of the latency introduced by the latent world model component itself, making it difficult to assess its practical impact. Furthermore, the paper does not discuss memory footprint of the model, which is a critical factor for deployment on resource-constrained edge devices.
2. No discussion of robustness to adverse weather/lighting conditions. As in Appendix A.1, the augmentation is claimed to enhance the robustness, but there is no experiments to validate such ability of the model. The paper should include experiments that specifically evaluate performance under conditions such as heavy rain, fog, or nighttime driving. Without such analysis, the practical applicability of the method in real-world scenarios is questionable.
3. Missing references:
- [1] DriveVLM: The convergence of autonomous driving and large vision-language models
- [2] EMMA: End-to-End Multimodal Model for Autonomous Driving
- [3] VLP: Vision Language Planning for Autonomous Driving
- [4] OmniDrive: A Holistic LLM-Agent Framework for Autonomous Driving with 3D Perception, Reasoning and Planning

### Questions
1. What is the computational overhead of adding the latent world model? How does this impact real-time performance?
2. How does the method perform under challenging weather conditions or poor lighting? Are there specific failure modes?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces LAW, a self-supervised method that enhances end-to-end autonomous driving without the need for expensive annotations. It employs a latent world model to predict future latent features based on current data and actions, along with a view selection strategy to improve model efficiency. LAW outperforms state-of-the-art methods on both open-loop and closed-loop benchmarks.

### Strengths
The proposed LAW framework utilized a self-supervised method to significantly reduce the need for heavy annotation tasks, addressing the data scalability challenge of many existing methods. The detailed breakdowns of ablation studies, latency analyses, and visualizations provide readers with clear and comprehensive information to understand and reproduce the work.

### Weaknesses
The view selection strategy is a valuable insight to improve the efficiency of the method, but it adds complexity to the overall framework. Although there is only a minimal performance drop, it seems the view selection strategy hasn’t fully captured the informative scenes in driving scenarios. If there could be more discussion or analysis on what caused the performance drop, or how this issue could be mitigated with the Latent World Model, it would make the work more complete.

### Questions
Current View Selection Strategy Adaptability: Currently, the view selection strategy is designed for six cameras. If the number of cameras changes, how much effort is required to adjust the strategy? Is it possible to design the strategy to be adaptive to: 1) the total number of cameras, and 2) the selected number of cameras used at each time step—for example, using two cameras at  t=0  and three cameras at  t=1 ? In that case, how would you modify the selection reward?

Typographical Error in ‘Implementation Details’: On page 7 in the “Implementation Details” section, the last sentence starting with “For the closed-loop benchmark. And we use…” seems to contain a typographical error or is missing information.

Enhancing System with Additional Supervision: In Table 1, the ablation study shows the effectiveness of latent prediction. Additionally, what other forms of supervision could be added to further improve the system?

Performance with View Selection Strategy: In Tables 1 and 2, the open-loop and closed-loop tests are based on the default LAW, which does not use the View Selection strategy. If that’s the case, could you clarify the performance when the View Selection strategy is included?

Performance Discrepancy in Table 7: In Table 7, why is the performance using six views worse than using the Front + GT Views—for example, why is six-view performance worse than two-view performance? Could you explain the possible reasons?

Metrics at Other Time Horizons: In Table 4, the time horizons for latent prediction are only 0.5, 1.5, and 3.0 seconds. How does the metric change at other time horizons, such as 1 or 2 seconds?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes the Latent World Model (LAW) to predict future features based on current features and ego trajectories, presenting a novel approach for end-to-end autonomous driving.

### Strengths
1. Introduction of the Latent World Model (LAW) to predict future scene latents from current scene latents and ego trajectories.

2. Demonstrated universality across various common autonomous driving paradigms, i.e.,  perception-free and perception-based frameworks.

3. Extensive experiments conducted on multiple benchmarks, achieving state-of-the-art performance on real-world open-loop datasets like nuScenes and simulator-based closed-loop CARLA benchmark.

### Weaknesses
See the Questions section.

### Questions
1. What is the shape of the Visual Latents, and can provide ablation studies?

2. Will LAW's use of the unique trajectory of the next frame as ground truth supervision limits the model's capabilities, given that trajectories are often not unique? Since the paper uses a simulation platform, could experiments with multi-trajectory supervision be provided?

3. LAW currently only uses the current frame latent to predict the next frame latent, while the introduction mentions that "using temporal data is crucial."

   3.1. Can experiments be conducted to predict multiple future frame latents?

   3.2. Can the model be trained to predict multiple future frame latents while taking in multiple input frame latents, leveraging temporal information more effectively?

4. Given that LAW currently predicts only the next frame latent based on the current frame latent, how does it handle tasks like predicting multiple future frames in nuScenes? Is this achieved through progressive prediction of the next frame latent?

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
This paper proposes a self-supervised learning approach, LAW, using the latent world model for end-to-end planning. The latent world model predicts future scene features based on the current scene features and predicted waypoints to learn better scene feature representation. This module is compatible with both perception-free and perception-based frameworks. The authors demonstrate that the proposed algorithm can beat existing baselines on three different benchmarks.

### Strengths
1. The proposed latent world model is a flexible plug-in module, which should be compatible with various end-to-end planning framework. 
2. This paper conducts extensive experiments, showing the great performance on multiple benchmarks. The ablation study is comprehensive to cover different aspects of the latent world model.
3. The paper is well-written, very easy to understand and follow.

### Weaknesses
1. I think the idea of using self-supervised world model for autonomous driving is not novel, discussed in multiple prior works like GAIA-1, ADriver-I, and Drive-WM. The main difference of this work is the world model in latent space. However, it is not well-motivated why latent world model is better than world model in image space. For example, people can easily evaluate the image space world model by visualizing the prediction but it is hard to do the same thing for latent world model. The authors should provide a more thorough justification for their choice of a latent space model, perhaps by analyzing the computational costs and memory requirements of both approaches, and also by discussing the trade-offs in terms of interpretability and performance.

2. Following 1, the authors do not show any direct evaluation of world model future prediction itself. I notice that the performance gap of different time horizons are very small (Tab. 6) compared with the gain brought by world model (Tab. 4). Does the future prediction performance similar for different time horizons? If not, why their performances are similar? In my opinion, I do not think it is easy to predict the future if the time horizon is as long as 3s. Maybe the authors can at least provide the L2 error of the latent features on the validation set for different time horizons. It would be beneficial to see a more detailed analysis of how the prediction error changes with the prediction horizon, and how this affects the overall driving performance. Specifically, it is unclear if the model is actually learning to predict the future, or if it is simply learning to extrapolate from the current state.

3. I think the settings in the experiment part are not fair. LAW uses Swin-T as the image backbone for nuScenes dataset. However, the baseline VAD and BEV-Planner are using ResNet-50, which is much weaker. This makes it difficult to isolate the contribution of the proposed method from the effect of using a stronger backbone. The authors should provide results using the same backbone for all methods, or at least provide a clear justification for using different backbones.

### Questions
Please consider replying to the points in the Weaknesses part.

### Soundness
2

### Presentation
3

### Contribution
2
