# Semi-Supervised Vision-Centric 3D Occupancy World Model for Autonomous Driving

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Understanding world dynamics is crucial for planning in autonomous driving. Recent methods attempt to achieve this by learning a 3D occupancy world model that forecasts future surrounding scenes based on current observation. However, 3D occupancy labels are still required to produce promising results. Considering the high annotation cost for 3D outdoor scenes, we propose a semi-supervised vision-centric 3D occupancy world model, **PreWorld**, to leverage the potential of 2D labels through a novel two-stage training paradigm: the self-supervised pre-training stage and the fully-supervised fine-tuning stage. Specifically, during the pre-training stage, we utilize an attribute projection head to generate different attribute fields of a scene (e.g., RGB, density, semantic), thus enabling temporal supervision from 2D labels via volume rendering techniques. Furthermore, we introduce a simple yet effective state-conditioned forecasting module to recursively forecast future occupancy and ego trajectory in a direct manner. Extensive experiments on the nuScenes dataset validate the effectiveness and scalability of our method, and demonstrate that PreWorld achieves competitive performance across 3D occupancy prediction, 4D occupancy forecasting and motion planning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a semi-supervised vision-centric 3D occupancy world mdoel, PreWorld. It leverages 2D labels through two-stage training, self-supervised pretraining and supervised finetuning. In the pre-training stage, the method utilizes an attribute projection head to enable temporal supervision from 2D labels. The method also includes a state-conditioned forecasting module.

### Strengths
1. The self-supervised pre-training is simple and intuitive. The method projects predicted volume using attribute projection head, then use future 2D frames as supervision signal. It is effective by upgrading training strategy without introducting extra modules for inference.
2. The experiments are extensive to show superior performance in occupancy prediction and forecasting tasks.
3. The paper writing is clear, it is easy to read and follow.

### Weaknesses
1. The improvement with and with-out pre-training seems not very significant. The module sometimes hurt performance (In tab.1). 
2. The ego state-conditioned module lacks of sufficient analysis and comparison.


### Questions
1. "Our Copy&Paste"  in Tab.6 is confusing for me. What is the setting of row 2 in Tab. 6 and what is difference between row 2 and copy & paste?
2. How to correctly interrept the result in Tab.3? The method can achieve a comparable result even without ego-state information? Can you elaborate more about the result for ours with ego-state information.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents "PreWorld," a semi-supervised model aimed at improving 3D occupancy prediction and 4D forecasting for autonomous driving. It leverages both 2D and 3D data in a two-stage training approach, including a self-supervised pre-training phase using 2D labels and a fully-supervised fine-tuning phase with 3D labels. The authors introduce a state-conditioned forecasting module that directly predicts future occupancy and vehicle trajectory. Tests on the Occ3D-nuScenes dataset show PreWorld achieves competitive results.

### Strengths
The paper provides a thorough evaluation of different methods on the Occ3D-nuScenes dataset. The experiments shows that the proposed model and training method can achieve competitive results across 3D occupancy prediction, 4D forecasting, and motion planning tasks.

### Weaknesses
1. The contributions are largely incremental. While the state-conditioned forecasting module (Section 3.2) enables volume feature preservation for rendering, this approach aligns closely with existing practices in similar tasks​ [1][2]. The self-supervision in Section 3.3 extends volume rendering to 4D but follows typical methodologies in related work​ [3].
2. The figures are difficult to interpret due to insufficient captions. For instance, Figures 2 and 3 lack details, making it unclear how the components operate or interact. The difference between solid and dashed arrows in Figures 1, 2, and 3 is not explained. Figure 2 leaves confusion about whether the two stages are jointly or sequentially trained.
3. The authors claim 2D rendering as self-supervision, but the best result comes from utilizing depth and semantic labels, which is not self-supervision, and invalidates "semi-supervision" in the title.
4. The performance improvement is minimal. For example, the mIoU improvment for 3d occupancy prediction is only about 2% compared to OccFlowNet. And there is no significant improvement in other experiments and metrics

### Questions
The proposed two stages can be trained jointly, why train them in two stages? Can the authors provide any motivation on this?

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
The paper propose a semi-supervised method called Pre-World for occupancy forecasting problem. Pre-world first train the occupancy network in a self-supervised manner with the pre-training goal to render future image observation. Then Pre-world train the occupancy network with temporal occupancy labels to further improve the performance. Experiment results on NuScenes dataset show that the proposed method to some extend improve the performance compared to training from scratch.

### Strengths
The paper is easy to follow. The proposed Preworld is able to utilize unlabeled data for pre-training and improve the performance of the downstream tasks. The experiments are extensive.

### Weaknesses
1) The performance improvement seems not that significant. Generally, there are two kinds of improvement that pre-training can bring. The first one is to accelerate convergence in the downstream task. The second one is to improve sample efficiency in the downstream task, that is to improve the performance at convergence. The reviewer are concerned about whether the improvement presented in the experiment part is related to the acceleration of convergence.

2) It can be found in Table 1 that after pre-training, ious of some categories like driving surface and manmade drop. Also, compared to previous method, performance on some categories including manmade and vegetation are lower. But there is no analysis about these.

### Questions
1)  Is it possible for the authors to provide experiments on training longer for both randomly initialization and pre-trained ones until they both converge in the downstream task?

2) Could the authors provide analysis on the detailed category performance?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes PreWorld, a semi-supervised, vision-centric 3D occupancy model that leverages 2D labels through a novel two-stage training approach. In the self-supervised pre-training stage, an attribute projection head is used to enable temporal supervision from 2D labels, while the fully-supervised fine-tuning stage introduces a state-conditioned forecasting module to directly predict future occupancy and ego trajectory.

### Strengths
The paper presents a comprehensive approach, from the overall architectural design to thorough experimental validation:

a). The paper is well-written and easy to follow, presenting a method that is both well-motivated and clearly explained.

b). The proposed state-conditioned forecasting module is interesting.

### Weaknesses
a). Although PreWorld leverages 2D labels to reduce the cost of 3D annotations, the paper only utilizes the nuScenes dataset for training, which does not fully demonstrate the method’s advantages. The semi-supervised approach should be highlighted by showcasing its benefits in terms of data efficiency. Specifically, the paper lacks a clear comparison of performance gains against a baseline model trained solely on limited 3D data, without the proposed 2D pre-training. This comparison is crucial to validate the effectiveness of the semi-supervised approach and quantify the benefits of leveraging 2D labels.

b). Different tasks in occupancy predictions (4D occupancy forecasting, motion planning...) may have interdependent effects, where optimizing one module could potentially negatively impact others. The paper should provide a clear discussion on how to achieve a balance among these tasks and address potential interactions between the modules. For example, the paper should analyze how the loss functions for different tasks are weighted and how these weights affect the overall performance. Furthermore, the paper should discuss potential trade-offs between the accuracy of occupancy prediction and the precision of motion planning, and how these trade-offs are managed within the proposed framework.

c). PreWorld’s two-stage training process may increase model complexity. This could lead to higher computational demands, potentially affecting the feasibility of real-time application in autonomous driving. The paper should further validate the feasibility of this method in terms of real-time inference performance. The paper should provide a detailed analysis of the computational cost of each stage of the training process, including the number of parameters, FLOPs, and memory requirements. Additionally, the paper should report the inference time of the model on a standard hardware platform to assess its real-time capabilities.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
