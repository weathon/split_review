# Navigation-Guided Sparse Scene Representation for End-to-End Autonomous Driving

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 8, 6, 6, 6

## Abstract
End-to-End Autonomous Driving (E2EAD) methods typically rely on supervised perception tasks to extract explicit scene information (e.g., objects, maps). This reliance necessitates expensive annotations and constrains deployment and data scalability in real-time applications. In this paper, we introduce SSR, a novel framework that utilizes only 16 navigation-guided tokens as Sparse Scene Representation, efficiently extracting crucial scene information for E2EAD. Our method eliminates the need for human-designed supervised sub-tasks, allowing computational resources to concentrate on essential elements directly related to navigation intent. We further introduce a temporal enhancement module, aligning predicted future scenes with actual future scenes through self-supervision. SSR achieves a 27.2\% relative reduction in L2 error and a 51.6\% decrease in collision rate to UniAD in nuScenes, with a 10.9× faster inference speed and 13× faster training time. Moreover, SSR outperforms VAD-Base with a 48.6-point improvement on driving score in CARLA’s Town05 Long benchmark. This framework represents a significant leap in real-time autonomous driving systems and paves the way for future scalable deployment. Code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel method for end-to-end trajectory prediction for autonomous driving, with a model that takes as input surround view camera images, and outputs a predicted trajectory for the vehicle. The main novelties are:
- the use of a sparse tokenizer to reduce the typical dense BEV representation into a sparse (in experiments 16) set of feature vectors.
- the introduction of the driving command into the BEV representation via cross attention.
- the application of a future prediction module for the BEV features as an auxiliary loss.
The proposed method aims to reduce the dimensionality of the BEV space without using pre-defined intermediate signals such as detections, mapping etc. This allows the model to be end-to-end differentiable, with the tokenization learned as a part of the driving task. 

Experiments and ablations are performed on the nuScenes dataset, where the proposed method produces a new SOTA in terms of both quality and latency.

### Strengths
The main novel contribution of this work lies in the use of the TokenLearner for BEV feature compression. From the experiments, the authors demonstrate that they are able to achieve new SOTA trajectory prediction results without any intermediate perception signals used by previous works. Ablations are also performed demonstrating the improvements provided by both the future prediction auxiliary task as well as the navigation command cross attention into the BEV feature space. Visualizations are also provided demonstrating the the model's attention mechanism does seem to focus on reasonable parts of the scene given a navigation command (i.e. it's possible that the model is not directly overfitting in some way).

Overall the paper is well written and easy to understand, and the overall method seems reasonable and based on sound prior works.

### Weaknesses
The number of optimal scene queries selected by the authors seems surprisingly small, and may be skewed by the difficulty of the average scene encountered in nuScenes. From the provided visualizations, it looks like the model focuses directly on relevant agents and objects in the scene. However, it's unclear whether the model would be able to extend to extremely dense scenes, where a fixed number of scene queries may limit the models ability to handle many other agents / objects.

In Table 4, the authors ablate the addition of a perception module. However, no results for the perception tasks themselves are provided, and so it cannot be determined whether these tasks were actually trained appropriately (i.e. they may have simply diverged altogether).

One additional factor to call out is the inherent risk of the nuScenes dataset being skewed in some way (i.e. Rethinking the Open-Loop Evaluation of End-to-End Autonomous Driving in nuScenes), but this is not the fault of the authors.

In Figures 7 and 8, it would be helpful to explain the colormap.

### Questions
What is the channel dimension of the scene queries?

How would the model respond in a very dense scene? Is there an inherent limitation in the number of objects / components that the model can focus on given a fixed number of scene queries?

What is the quality of the perception outputs in Table 4?

### Soundness
3

### Presentation
4

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
This paper proposed a novel approach for trajectory prediction in autonomous driving called SSR. A very straight intuition is that the more comprehensive and precise the information one can extract, the better the downstream tasks will perform. Many recent models try to extract dense BEV features with rich scene information and route the information to multiple auxiliary tasks. On the contrary, the authors argue that for end-to-end autonomous driving, auxiliary supervision from perception tasks might be unnecessary, instead computational resources can be focused on crucial parts of the scene.
To achieve this, the paper introduced a scene token learner that learns sparse scene queries from BEV features extracted by a BEV encoder (BEVFormer in particular) and current navigation command. The trajectory is then predicted based on the scene queries. To train the model, two loss terms are used. The first term directly minimizes the L1 loss between the predicted and ground truth trajectory. The second term aims to enhance scene representation by introducing a BEV world model. This term replaces the perception sub-tasks in other models, with more focus on temporal context. The BEV world model takes the BEV features, scene queries and predicted trajectory as input and it tries to predict the BEV features at the next frame. We minimize the L2 distance between the output of the world model and the BEV features directly extracted by the BEV encoder at the next frame. The overall loss is the sum of these two terms.
The authors show that a small set of tokens is sufficient to outperform sota models in trajectory prediction on NuScenes dataset.

### Strengths
The paper is well written, with clear and insightful motivation. The proposed model architecture is novel, and the experimental results show significant improvement over existing methods. The experiment section is comprehensive, with insightful analysis.
In autonomous driving, multi-head models are very popular, for a number of reasons. Not only because different tasks can serve as auxiliary supervision for each other and contribute to the overall performance improvement, the output of the individual tasks can also be utilized by downstream tasks in a modular autonomous driving system (e.g. occupancy map can be the input of a traditional pathfinding algorithm for parking). However in a fully end-to-end autonomous driving system all those intermediate outputs are unnecessary. It’s interesting to see papers questioning the design choices of existing models and exploring alternative designs.

### Weaknesses
1. The proposed architecture borrows the idea of a world model by predicting future bev features. However it seems that the BEV features are only regularized by the trajectory prediction task. There’s no reconstruction loss and other downstream tasks. In this case it’s questionable to still call it a world model. The absence of a direct reconstruction loss on the BEV features, or the inclusion of other auxiliary tasks, raises concerns about the richness of the learned representation. The model might be learning a representation that is highly specialized for trajectory prediction, potentially lacking the generalizability expected from a true world model. This could limit its applicability to other tasks or scenarios.
2. The paper lacks theoretical analysis of why the proposed SSR method is better. While the empirical results are promising, a theoretical underpinning would strengthen the claims. For example, an analysis of the convergence properties of the training process, or a study of the information bottleneck imposed by the sparse scene queries, could provide valuable insights. Without such analysis, it is difficult to fully understand the mechanisms that contribute to the observed performance gains.

### Questions
1. There’s a paper “Rethinking the Open-Loop Evaluation of End-to-End Autonomous Driving in nuScenes” (https://arxiv.org/abs/2305.10430) claims that a simple MLP model that takes simple ego state (velocity, acceleration, historical trajectory) can also outperform VAD and UniAD. While their claim is that the metrics may not adequately capture the superiority of different methods, in combination with table 2.(b) in this paper being reviewed, where a larger number of scene queries leads to worse performance, is this an indication of overfitting of the larger models (or generally speaking, a case where a larger model is being overperformed by a smaller model due to various reasons)? Considering the trajectories in NuScenes are relatively simple, will this weaken the conclusion of this paper, especially when the navigation tasks become more complex?
2. Why the visualization in Figure. 5 in a hexagon format instead of square grids?

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
In this paper, the authors propose a navigation-guided sparse scene representation for end-to-end autonomous driving. The proposed solution eliminates the need for supervised sub-tasks, allowing computational resources to concentrate on essential elements directly related to navigation intent. Specifically, the proposed solution utilizes learned sparse query representations guided by navigation commands, and introduces a BEV world model for self-supervision on dynamic scene changes to highlight the critical role of temporal context in autonomous driving. The experimental results show that the proposed solution achieves great performance on nuSccenes dataset with minimal training and inference cost.

### Strengths
1. The proposed solution sounds solid in theory. Specifically, eliminating the need for supervised sub-tasks, e.g., detection, mapping, motion, occupancy, etc., indeed speed up the training and inference time. The proposed navigation-guided concept and BEV world model should extract useful features for the autonomous driving. 
2. The proposed navigation-guided concept is inspring. As mentioned in the paper, it is a human-inspried solution whose intuition is to mimic the behavior of human beings. It is a good research direction. The authors propose a way to combine the information with the special features.
3. The ablation study is helpful. Readers can get more information from the ablation study results.
4. The analysis and discussion guide readers think more deeper about the model design and the performance.

### Weaknesses
1. There are some important information is missing. For example, detailed model structure, navigation commands pre-processing operation, etc. Specifically, the paper lacks a clear description of the network architecture, including the specific layers, activation functions, and number of parameters used in the image backbone, BEV encoder, TokenLearner adaptation, planning decoder, and BWM module. The absence of these details makes it difficult to reproduce the results or compare the proposed method with other approaches. Furthermore, the paper does not specify how the high-level navigation commands are encoded and fed into the model, which is crucial for understanding the navigation-guided aspect of the method. The lack of detail regarding the transformation of ground truth ego trajectories into driving commands also hinders the reproducibility of the results.
2. It will be better if the authors could report some failure cases. Especially for those cases which the predictions are totally opposite toward the navigation command. Without such analysis, it is hard to understand the limitations of the proposed method and the scenarios where it might fail. For example, it would be beneficial to see cases where the model misinterprets the navigation command or fails to handle complex driving scenarios, such as intersections or lane changes.

### Questions
1. Are the navigation commands open-set or close-set, how many commands were used in this paper, how to pre-processing the high-level navigation commands so that the model can take them as inputs, etc. 
2. What is the performance of the model if the navigation command never appears in the training set (or confusing command, e.g., turn left and right, or turn left or right, etc.)?

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
The paper introduces a novel SSR framework that requires no auxiliary task outputs or labels, relying instead on just 16 sparse navigation tokens for guidance. This approach achieves SOTA performance on the nuScenes dataset, with both inference and training processes being fast.

### Strengths
The model proposed in this paper yields excellent results, achieving SOTA performance on the nuScenes dataset. Additionally, both the inference and training speeds are fast on 3090 GPUs.

### Weaknesses
1. From the ablation studies (Table 2), it can be seen that the core contribution of this paper is the introduction of navigation information as guidance. The addition of the STL and BWM modules does not significantly affect L2, which suggests that navigation information provides significant assistance for lane following, especially when driving straight. It is understandable that the introduction of the BWM module, which incorporates temporal modeling, improves collision rates. In other words, the key contribution of this paper lies in utilizing navigation information, which is not employed by other methods. This kind of approach is relatively common in the industry but is rarely mentioned in academia. Whether merely introducing navigation information as input is worthy of an ICLR paper is something I am somewhat conflicted about.
2. The STL and BWM modules lack novelty. Furthermore, I'm not particularly fond of naming the BWM module a "world model." Given that it primarily involves predicting the next frame in BEV, the term "world model" might be considered too broad. I'd like to reiterate that I think the core contribution of this paper is the introduction of navigation information.
3. The color scheme used in the figures could be slightly unappealing, with most modules and features using white as the primary color. It would be nicer if the visuals were more aesthetically pleasing.

### Questions
Refer to the weakness

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
5

### Summary
This work proposes to extract sparse scene queries to represent the scene and use the scene queries to generate planning results.  Further, they propose an auxiliary task head and loss - predict future BEV feature.

### Strengths
1. The elimination of middle task could indeed reduce the latency and annotation requirements.
2. The writing is clear

### Weaknesses
1. Lack of closed-loop evaluation:  as pointed in AD-MLP and BEVPlanner, it is rather simple to fit nuScenes, as most of its data is going straight.  BEVPlanner only uses BEV feature, even without the need of the proposed scene queries.  (**Strangely, the authors cite BEVPlanner but do not compare with it in Table 1. I hope the authors could give an explanation**). Not to mention that AD-MLP even does not need any sensor inputs.  Thus,  **it is not convincing to claim that there is no need for middle supervision under nuScenes open-loop evaluation**. It is important to have closed-loop results and ablation studies on it.

Due to the missing of closed-loop results, the argument in the paper is not convincing and thus I give a reject rating. I will increase my rating if closed-loop results and ablations are provided.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
3
