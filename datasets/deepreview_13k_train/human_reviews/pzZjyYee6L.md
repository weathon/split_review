# Don't Reinvent the Steering Wheel

- Decision: Reject
- Scores: 1, 3, 3, 3

## Abstract
To make safe and informed decisions, autonomous driving systems can benefit from the capability of predicting the intentions and trajectories of other agents on the road in real-time. 
Trajectory forecasting for traffic scenarios has seen great strides in recent years in parallel with advancements in attention-based network architectures and robust, large-scale benchmarks. 
However, such models are becoming larger, resource-hungry, and less portable as state-of-the-art pushes for larger-scale of road networks and real-world complexity. 
Previous works that achieve state-of-the-art results predict future trajectories as a series of waypoints in Euclidean space, yet do not frame learning through the lenses of classical kinematic models that describe the motion of moving vehicles. 
Instead of leaving the network to learn the inherent dynamics of traffic agents, we can instead leverage kinematic models of vehicle dynamics as priors to guide neural networks toward physics-informed solutions earlier in learning.
By combining existing knowledge of how agents move with powerful deep learning techniques, agents learn trajectories that are not only more interpretable but also more plausible in terms of vehicle kinematic constraints. 
In this work, we investigate the use of different kinematic formulations as learning priors for trajectory forecasting tasks and evaluate how each affects learning both empirically and analytically. 
In addition, we take advantage of time integration in order to derive the original output format of future trajectory coordinates, enabling the use of existing architectures and complementing previous work. 
This approach is easy to implement for trajectory forecasting and achieves a considerable performance gain on large-scale benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors present a method to improve trajectory forecasting using kinematic models. In particular, they propose to slightly change the output of the existing models where they implement kinematic equations to ensure that feasible trajectories are inferred. They discuss several different kinematic approaches and showcase how this idea can be applied to a recent state-of-the-art model.

### Strengths
- A very relevant problem being investigated.
- Intuitive idea being proposed.
- Promising experimental results shown.

### Weaknesses
 - Novelty is very limited, as the authors present a method of an existing work that is not referenced.
- Writing and explanations can be improved.
- Experiments are quite dry and could be expanded with more visualizations.

- "but also scales well in size", unclear if this is a good or a bad thing. The authors should clarify this better.
- The authors need to cite the earlier work listed above, and put their work into context. This is the biggest issue with the current manuscript and makes the work not ready for publication until this is done (since the level of contributions of the work is questionable).
- Figures 1 and 2 are not referenced in the text.
- Notation can be improved. E.g., in the equation for L  in Section 4.1 the notation p_h is not introduced before being used. The authors should make sure that all notation is properly defined.
- "we downscale the model", how exactly? Unclear.
- The authors do not properly explain the experiments, such as the number of mixture components used and other information relevant to understanding the approach and the experiments.
- For the experiments with noisy trajectories, do you add noise during training as well? Unclear, would be good to clarify.
- The experiments are somewhat dry, would be good to add some visual results as well.

### Questions
The work presents quite an intuitive idea that is showing good results. However, the problem is that the same idea is already presented in an earlier work: "Deep Kinematic Models for Kinematically Feasible Vehicle Trajectory Predictions", ICRA 2020. The authors do not cite this paper and do not put their work in the correct context when it comes to the existing literature. As such, the main contribution of the work, as stated by the authors, lacks novelty.
Please find detailed comments below:
- "but also scales well in size", unclear if this is a good or a bad thing. The authors should clarify this better.
- The authors need to cite the earlier work listed above, and put their work into context. This is the biggest issue with the current manuscript and makes the work not ready for publication until this is done (since the level of contributions of the work is questionable).
- Figures 1 and 2 are not referenced in the text.
- Notation can be improved. E.g., in the equation for L  in Section 4.1 the notation p_h is not introduced before being used. The authors should make sure that all notation is properly defined.
- "we downscale the model", how exactly? Unclear.
- The authors do not properly explain the experiments, such as the number of mixture components used and other information relevant to understanding the approach and the experiments.
- For the experiments with noisy trajectories, do you add noise during training as well? Unclear, would be good to clarify.
- The experiments are somewhat dry, would be good to add some visual results as well.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method for using kinematic models for trajectory forecasting in the context of self-driving. Three different kinematic formulations (velocity, acceleration, speed+heading) are ablated in three settings (full dataset, small dataset, noise) on the Waymo open motion forecasting dataset. Analytical error bounds some of the kinematic formulations given.

### Strengths
* The method proposed makes sense and is simple.
* The analysis on dataset size and noise was nice to see, and not common in existing literature to my knowledge. 
* The derivations for the linear approximations for the distribution of positions is also useful.

### Weaknesses
 **1) Related work**

This paper claims the novelty for "simple and effective method for incorporating kinematic priors into probabilistic models
for trajectory forecasting", but is missing many related works that have explored this in the past. For some examples of works which use some variant of bicycle, unicycle or other kinematic model for trajectory forecasting in the context of self driving:

* Imagining The Road Ahead: Multi-Agent Trajectory Prediction via Differentiable Simulation
* Deep Kinematic Models for Kinematically Feasible Vehicle Trajectory Predictions
* A Kinematic Model for Trajectory Prediction in General Highway Scenarios
* MixSim: A Hierarchical Framework for Mixed Reality Traffic Simulation
* Guided Conditional Diffusion for Controllable Traffic Simulation

As these are papers that simply come top of mind / found after a brief literature review, I may have missed more and thus I encourage the authors to add this list after performing a more thorough literature review. For the rebuttal I'd like to see the authors more clearly position their work in the context of existing literature.


**2) Experiments**
The paper was unclear about the baseline performance. Specifically, did the authors compare to the original MTR, or a re-implemented and retrained version of MTR? I found the following statements in the paper:
> We implement kinematic priors on state-of-the-art method Motion Transformer (MTR) Shi et al. (2022), which serves as our baseline method.

> ... we downscale the model from its original size of 65 million
parameters to 2 million parameters and reproduce baseline results in our experiments

> We compare our model against the state-of-the-art architecture...

In all tables in both the main paper and the appendix, the results are written as relative to the baseline, and I could not find absolute numbers for the baseline anywhere. Thus I am lead to believe that the results are for the smaller model, which likely performs worse than the original MTR? If this is true, I believe the authors need to release the absolute performance of their baseline.
The reason that the absolute performance is important to me is that its unclear whether the gains of the kinematic model hold when absolute performance increases as you scale the model, etc.

### Questions
Could the authors address my questions in the Weaknesses section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors develop a trajectory forecasting model that makes use of a simple kinematics model for vehicle dynamics to induce a bias and facilitate learning. In particular, instead of predicting a GMM over x/y, they predict 1) the velocity, 2) acceleration, or 3) speed and heading. For 3) they also derive analytical error bounds for a linear approximation around sin / cos. They show that formulation 1) improves a baseline on WOMD.

### Strengths
* The proposed model beats the baseline model
* Results for different kinematics models

### Weaknesses
 * The authors claim that previous SotA results were only obtained by directly predicting Euclidean coordinates. However, for example “MULTIPATH++: EFFICIENT INFORMATION FUSION AND TRAJECTORY AGGREGATION FOR BEHAVIOR PREDICTION” (https://arxiv.org/pdf/2111.14973.pdf), which the authors cite as a SotA model, also uses an underlying kinematics model as described in Section 3.6.
* Lack of novelty / contributions. Trajectory forecasting with kinematics models exists in literature. The given kinematic model derivations are quite straightforward.

### Questions
As mentioned above, kinematics models have been applied for ML trajectory forecasting and hence, the contributions of this paper seem minor.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper explores several alternative output representations of the trajectory prediction model. Instead of directly predicting the position coordinates (x, y), the authors proposed three alternative output representations:
* Predicting (vx, vy)
* Predicting (ax, ay)
* Predicting (speed, heading)

The authors implemented the three approaches on the Motion Transformer (MTR) model. The evaluation result on the WOD dataset shows that by predicting (vx, vy), they improve the prediction mAP by 2.376%.

### Strengths
* This paper shows some performance improvement over the MTR model on the WOD dataset.

### Weaknesses
 * The contribution of this paper is very weak. The related work section claims that none of the existing trajectory works uses the bicycle kinematic model, which is not true. There are many existing trajectory prediction models (such as MultiPath++ [1] and DKM [2]) that explicitly predict future accelerations and steering angles and roll out future trajectories using the bicycle kinematic model.

[1] Varadarajan et al. 2022. Multipath++: Efficient information fusion and trajectory aggregation for behavior prediction.

[2] Cui et al. 2019. Deep Kinematic Models for Kinematically Feasible Vehicle Trajectory Predictions.

 * This paper talks about the advantages of using the bicycle kinematic model as the prior for trajectory prediction. However, none of the three proposed formulations used the actual bicycle kinematic model. From the result in Table 1, Formulation 1 has the best performance, and Formulation 1 is simply to predict deltas between waypoints.

 * The evaluation result lacks some important information. The tables only show the relative improvement from the MTR baseline. However, it is not clear whether the MTR numbers are from the MTR paper, the WOD leaderboard, or from the authors' own implementation. I highly recommend the authors submit their solution to the WOD leaderboard and report the numbers from the leaderboard.


--- Other minor comments

 * Please add equation numbers.

 * I am not sure sigma_{x + vx * dt} = sigma_x + sigma_{vx} * dt is correct. The summation of two Gaussian variables x + y should be sigma_{x + y} = \sqrt{sigma_x ^ 2 + sigma_y ^ 2}.

 * Reference Chai et al., 2020a and Chai et al., 2020b are the same paper.

### Questions
N/A

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor
