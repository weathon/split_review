# A Self-Supervised PINN for Inertial Pose and Dynamics Estimations

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Accurate real-time monitoring of not only movements, but also internal joint moments or muscle forces that cause movement in unrestricted environments is key for many clinical and sports applications. A minimally obstrusive way to monitor movements is with wearable sensors, such as inertial measurement units, using the fewest sensors possible. 
Current real-time methods rely on supervised learning, where a ground truth dataset needs to be measured with laboratory measurement systems, such as optical motion capture, which then needs to be processed with methods that are known to introduce errors. There is a discrepancy between laboratory and real-world movements, and for analysing new motions, new ground truth data would need to be recorded, which is impractical.
Therefore, we introduce SSPINNpose, a self-supervised physics-informed neural network that estimates movement dynamics, including joint angles and joint moments, from inertial sensors without the need for ground truth data for training.
We run the network output through a physics model of the human body to optimize physical plausibility and generate virtual measurement data. Using this virtual sensor data, the network is trained directly on the measured sensor data instead of a ground truth. Experiments show that SSPINNpose is able to accurately estimate joint angles and joint moments at 8.7 degrees and 4.9 BWBH%, respectively, for walking and running at up to speeds of 4.9 m/s at a latency of 3.5 ms. We further show the versatility of our method by estimating movement dynamics for a variety of sparse sensor configurations and inferring the positions where the sensors are placed on the body.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
This paper presents a method to estimate the human pose and dynamics from wearable IMU sensors. Specifically, a self-supervised method is used to reconstruct the input IMU signals and to estimate joint angles and dynamics. Kane’s equations are used to calculate the motion equations. Experiments show promising performances on dynamics and pose estimations.

### Strengths
1. Estimating human dynamics from IMU sensors is an important and meaningful research direction.

2. Using a self-supervised learning method to capture information from IMU sensors sounds very interesting.

3. Combining a neural network with a physics model is also reasonable.

### Weaknesses
1. In line 199 it is mentioned that "the IMU data consists of 2D acceleration and 1D gyroscope data per sensor". Why is the acceleration 2D and gyroscope data 1D, instead of 3D? Besides, what does the "gyroscope measurement" refer to? Is it angular velocity or estimated orientation?

2. I am also a little bit confused by the proposed method. It is mentioned that this is a self-supervised method, however, in Section 3.1, the output contains root rotation and translations, joint angles and joint torques. I don't quite understand how each of these outputs is predicted (e.g., what is estimated by neural networks, what is calculated from Kane’s equations)

3. Besides, are the motion capture data used for this method? or purely based on IMU data (since it is self-supervised)? If ground truth joint angles are provided to supervise training, it will not be self-supervised learning.

4. I can not find much information about the adopted dataset Dorschky et al., 2024. I am curious about the choice of dataset and suggest using some well established dataset like [1,2].

[1] Zhang et al.: MMVP: A Multimodal MoCap Dataset with Vision and Pressure Sensors, CVPR 2024

[2] Werling et al.: AddBiomechanics Dataset: Capturing the Physics of Human Motion at Scale, ECCV 2024

5. I think it would be very important and beneficial to show the proposed method can benefit the existing 3D pose estimation methods from IMU sensors. However, such a comparison is only provided in the appendix using different datasets, and compared to SMPL models, the joint angle ranges are manually set. There are also recent works that try to make SMPL models or AMASS datasets align with biomechanical models with a meaningful degree of freedom, like [3]. Perhaps similar methods can be applied to enable a fair comparison.

[3] MANIKIN: Biomechanically Accurate Neural Inverse Kinematics for Human Motion Estimation, ECCV 2024

### Questions
See above

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
5

### Summary
The paper introduces SSPINNpose, a self-supervised approach for estimating gait kinematics only from IMU data. The authors proposed a self-supervised approach to train a recurrent model based on LSTMs. The model is trained in an IMU signal reconstruction task without any labels while regularized by a multitude of physical constraints. Their approach demonstrates promising results in estimating joint angles, torques, and GRFs from IMU data, and the source code for testing/training is provided.

### Strengths
- The paper is well-written and easy to follow. 
- The paper shows the potential of combining physics-informed objectives during self-supervision for gait kinematic estimation.

### Weaknesses
 - **Lack of Comparisons**: One of the main weaknesses of the paper is its lack of direct comparisons with prior approaches on the same datasets and under the same conditions and evaluation criteria. I find the comparisons in the supplementary materials insufficient for judging the contribution and effectiveness of their work, especially given that the proposed method is not evaluated under the same conditions as prior works. Specifically, the paper should provide a more detailed comparison of its performance against state-of-the-art methods using identical evaluation metrics and datasets. This would involve not only reporting the overall error but also analyzing the error distribution across different gait phases and joint angles. Please see my suggestions below to address this limitation.
- **Contributions**: The paper proposes several physics constraints to guide the model's training. However, it is unclear what their contributions are in this combination. I have found several other optimization-based studies using the same physical constraints during pose/motion/gait kinematic estimation. Despite this, the paper's approach of combining physics-informed objectives during model training is somewhat unique. However, there are no experiments that support or highlight the impact of this novelty. For instance, an ablation study that systematically removes each physical constraint and evaluates the impact on the final performance would be necessary to highlight the contribution of each constraint. The paper should also clarify how the specific combination of these constraints contributes to the overall performance, as opposed to using them individually.
- **Evaluations**: The authors evaluate their approach only on one dataset, which contains only walking and running sequences. Therefore, the impact of this paper is only on some applications and its influence on others is not fully studied. The paper should include evaluations on a more diverse range of activities, such as stair climbing, jumping, or other complex movements, to demonstrate the robustness and generalizability of the proposed method. This would also help to identify the limitations of the method and the types of movements where it performs well and where it struggles.

### Questions
The paper tackles an important problem in the pose and gait estimation fields and shows promising results in the same range as prior works on other datasets. However, I have some concerns regarding the evaluations and the lack of comparisons. Therefore, I suggest rejecting this paper in its current form. To improve the paper, I have several questions and suggestions:
1. Can you please provide direct comparisons with state-of-the-art methods on the same dataset and under the same evaluation conditions? In the first paragraph of page 8, the paper mentions that the dataset owners have used another evaluation scheme, and therefore the results are not directly comparable with the authors. To address this issue, my suggestion is to evaluate your approach with both schemes to back up your claims.
2. Can you please elaborate on the paper's contributions, beyond combining and tuning existing losses during self-supervised training? I suggest authors add a recap of their contributions to the last paragraph of the introduction to clarify and highlight their contributions. 
3. Can you please evaluate the computational cost of adding all objective functions during training? Does it increase the training time?
4. Can you please elaborate on the difference between your approach and two-stage solutions, similar to Physical Inertial Poser (PIP)? I would be interested in knowing if there are any merits in a second-stage optimization after you have the initial results. In this case, some physics constraints like GRF may be necessary during the first stage (self-supervised learning) based on Table 8. But how necessary would the other losses be? One advantage of the second stage is that it can generalize well to unseen actions, which I believe your approach lacks. It would be valuable if the authors could provide more details on the advantages and disadvantages of their design vs optimization-based and hybrid (2-stage) solutions.


Some things could be improved, but did not impact the score:
- On some places, like L236 and L268, the authors say "see supplementary A/B/C", but on others, like L377, L382, and L359, they just say "See B/C/D". Please use a more constant formatting.
- On L240, "This loss is applied generalized coordinates q" seems like an incomplete sentence.
- The authors have used a simple LSTM network that is likely to have been fully tuned in prior works. It would be interesting to see a comparison with more modern signal processing architectures or a comparison with CNN approaches from prior works. What is the intuition behind choosing this network? Tables 5,6 and 8 are more informative for belonging to the main paper, while Table 1 is just a network comparison that should be supplementary.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces SSPINNpose, a self-supervised physics-informed neural network designed to estimate human movement dynamics from inertial measurement unit (IMU) data without requiring ground truth labels. By integrating a physics model of the human body and leveraging virtual sensor data, the method enforces physical plausibility using Kane's equations and a temporal consistency loss. SSPINNpose is capable of accurately estimating joint angles and joint moments in real-time, even with sparse sensor configurations, and can infer the positions of the sensors on the body. Experiments demonstrate that SSPINNpose achieves comparable performance to supervised methods in estimating lower-body dynamics during walking and running at various speeds.

### Strengths
Innovation: Proposes a novel self-supervised approach to estimate human movement dynamics from IMU data without the need for ground truth labels, addressing a significant limitation in current methods.
Real-time Capability: Demonstrates that SSPINNpose can estimate dynamics in real-time with low latency, which is crucial for practical applications in clinical and sports settings.
Physical Plausibility: Incorporates physics-based constraints using Kane's equations and temporal consistency to ensure physically plausible motion estimations.
Sparse Sensor Configurations: Shows the method's versatility by effectively handling sparse IMU setups and inferring sensor placements, enhancing its practicality.

### Weaknesses
Limited to 2D Movements: The method focuses on lower-body dynamics in the sagittal plane and does not address full 3D motion estimation, limiting its applicability to more complex movements. This is a significant limitation as many real-world human movements involve substantial out-of-plane motion, such as during turning, twisting, or even subtle shifts in balance. The current approach, therefore, cannot be directly applied to a wide range of activities.

Simplifying Assumptions: Assumes flat ground and non-sliding feet, which may not hold in real-world scenarios and could affect the accuracy of estimations in such conditions. These assumptions are quite restrictive. For example, walking on uneven terrain or performing any activity involving foot slippage would introduce significant errors in the model's estimations. The lack of robustness to these common real-world variations is a concern.

Model Personalization: Uses a generic multibody dynamics model without personalization, potentially affecting the accuracy due to individual anatomical differences. The use of a generic model neglects the significant variability in human body segment lengths, mass distributions, and joint ranges of motion. These individual differences can substantially impact the accuracy of the estimated dynamics, especially when considering the sensitivity of inverse dynamics calculations to these parameters.

Replication of Noise: The model may replicate noise in IMU signals, which could reduce the physical plausibility of the estimated motions. IMU data is inherently noisy, and if the model does not adequately filter or account for this noise, it could lead to physically implausible jerky or erratic motion estimations. This is a critical concern for the reliability of the method.

### Questions
How does SSPINNpose perform when applied to movements involving significant out-of-plane dynamics or complex 3D motions?
Can the method be adapted or extended to handle 3D movement estimation, and what challenges would that entail?
How sensitive is SSPINNpose to variations in IMU placement, and how robust is the sensor placement inference in practice?
What impact do the simplifying assumptions (e.g., flat ground, non-sliding feet) have on the method's performance in more variable real-world environments?
How does the model handle or mitigate the replication of noise in IMU signals to maintain physical plausibility?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes SSPINNpose, a self-supervised physics-informed neural network for estimating human movement dynamics using inertial measurement units (IMUs) for real-time applications in uncontrolled environments. SSPINNpose leverages a combination of physics-informed losses and recurrent neural network (RNN) architecture to infer both kinematic and kinetic properties of human motion.

### Strengths
- The paper estimates dynamics as a byproduct of kinematic alignment of actual IMU and estimations from a virtual model. I find this as the most interesting aspect of the paper.

- The authors use auxiliary physics-inspired losses for attempting realistic estimations.

### Weaknesses
 The authors highlight that most state-of-the-art methods rely on supervised approaches, while their method does not require labeled data, and that, this is one of the highlight of their work.

- However, as such, in this case of joint kinematics and kinetics regression, there is nothing as labeled or unlabeled data because the authors are anyway using full lower-body motion. The question of labeled or unlabeled data may appear in cases of classifying the intent such as walk level ground, climb stairs etc., but in the case where the goal is to regress body kinematics or kinetics, anyway, the recording full body motion is done, thus, there is no question of explicitly labeling the data.

- Thus, both supervised and self-supervised approaches appear to aim at the same objective: minimizing the deviation between experimental and estimated kinematics. So here, the self-supervised goal seems to be only a wording and framing problem. 
It is also evidenced by the main self-supervised objective that the authors use, minimizing the deviation between actual IMU motion and the virtual model’s motion, which closely resembles a supervised objective. Could the authors clarify how their approach differs fundamentally from traditional supervised methods? Further, the fact that dynamics is estimated as a byproduct of minimizing kinematic deviations could be done by posing this as a supervised method also, since the authors are estimating GRF using a ground contact model anyway.  

 I found the objectives, contributions, and methodology of this work weakly positioned and unclear, as the authors highlight multiple objectives to establish the novelty of their method over existing approaches. Could the authors to clarify the primary advantages of their approach and how it complements or differs from existing state-of-the-art tools. Here are some specific points of feedback:

- One stated objective appears to be the estimation of kinematics and kinetics using IMUs rather than optical motion capture systems. Then why go for a self-supervised method, which may be less accurate? Musculoskeletal models, e.g., OpenSim can do this too. AFAIK, OpenSim 4.1 has begun supporting IMU data analysis. Could the authors elaborate on the specific advantages of their self-supervised approach compared to these methods? It appears that the real-time estimation is the only advantage. Then why this highlight of IMUs vs. OMC?

- Another goal mentioned is to facilitate analyses outside laboratory settings. This could theoretically be achieved by collecting data in real-world environments and applying OpenSim or similar tools to calculate inverse kinematics and dynamics. Could the authors clarify the added value of SSPINNpose for these applications, particularly if it avoids preprocessing requirements that are still necessary for lab-based systems?

- The authors also emphasize real-time computation of kinematics and kinetics. This seems particularly relevant to their approach, as OpenSim and related tools typically do not offer real-time capabilities. However, did the authors test this model in real-time by actually doing lower-limb gait analysis in the wild? Could the authors describe the setting in detail and elaborate on the real-time metrics like what was the real-time prediction frequency, lost packets, how the sensor synchronization and failure were handled, read rate etc? Sorry if I missed the information.

 The authors miss many common regression-based works that estimate joint kinematics regression of one joint from other inputs such as [1], [2], [3], [4], etc.
 - Many such works are missing in the related works.
 - Comparison with many such common existing methods also seem to be missing.

 When posed as a self-supervised problem, how do the authors handle collapse, especially, when the virtual model estimation is so perfect that the difference between the actual and virtual model estimations are almost trivial?

 Do the authors evaluate other similar self-supervised methods like [5] on their data?

### Questions
Please see the weaknesses section

### Soundness
2

### Presentation
2

### Contribution
2
