# Learning View-invariant World Models for Visual Robotic Manipulation

- Decision: Accept
- Scores: 6, 6, 6, 6, 3

## Abstract
Robotic manipulation tasks often rely on visual inputs from cameras to perceive the environment. However, previous approaches still suffer from performance degradation when the camera’s viewpoint changes during manipulation. In this paper, we propose ReViWo (Representation learning for View-invariant World model), leveraging multi-view data to learn robust representations for control under viewpoint disturbance. ReViWo utilizes an autoencoder framework to reconstruct target images by an architecture that combines view-invariant representation (VIR) and view-dependent representation. To train ReViWo, we collect multi-view data in simulators with known view labels, meanwhile, ReViWo is simutaneously trained on Open X-Embodiment datasets without view labels. The VIR is then used to train a world model on pre-collected manipulation data and a policy through interaction with the world model. We evaluate the effectiveness of ReViWo in various viewpoint disturbance scenarios, including control under novel camera positions and frequent camera shaking, using the Meta-world & PandaGym environments. Besides, we also conduct experiments on real world ALOHA robot. The results demonstrate that ReViWo maintains robust performance under viewpoint disturbance, while baseline methods suffer from significant performance degradation. Furthermore, we show that the VIR captures task-relevant state information and remains stable for observations from novel viewpoints, validating the efficacy of the ReViWo approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The goal of this paper is to train world models for robot manipulation
that are robust to changes in the position of the camera observing the
manipulator and the environment. This is a very relevant problem,
since cameras frequently move between training sessions and
deployment. To achieve this, the authors introduce a training setup in
which a combination of two VQ-VAE encoders is trained on a multi-view
dataset; one of the encoders, the VIE, learns to encode the
view-independent setting and arrangement of the scene, while the other
encoder, VDE, learns to encode the view-dependent aspects of the
scene. Taking the two encodings together, a decoder can reconstruct
the input scene as if it was observed from the viewpoint represented
in the other scene.

The VIE is then used to train a world model that can be applied for
policy learning or behavior cloning. The results indicate that the
approach is able to disentangle the different aspects of the view
inputs, leading to improved generalization to viewing changes between
training and testing.

### Strengths
- The training setup to enforce a separation of view-independent and view-dependent encoders is clever and seems novel.

- The view generation results indicate that the encoders and the decoder learn the kind of representation intended by the authors. 

- The evaluation of the learned policies indicates strong improvements over prior approaches to world model learning with respect to
generalization to novel viewpoints.

### Weaknesses
The main weakness of the paper lies in the experimental evaluation. As I understand, the model needs to learn (at least) two key aspects for a scenario: Where is the camera relative to the manipulator base (VDE) and what is the task-relevant layout of the scene (VIR). The decoder then needs to use that information to generate a novel viewpoint of the input scene. While this seems to work for the test cases, it is not clear whether the success is due to overfitting to a rather small number of settings and tasks, or whether the approach would scale to more complex scenarios, including real world data and camera pose changes beyond azimuth. The current evaluation does not provide sufficient evidence regarding real world significance.

In light of changing camera poses, the action space of the controller is very important. There are at least three I could imagine: (delta) joint space, (delta) end effector pose in camera frame of reference, (delta) end effector pose in manipulator frame of reference. The specific choice is extremely important for how a policy might transfer to different camera viewpoints. Which specific one was used in the experiments? Could the approach work for all of these? What if the camera calibration of a test scene is known?

### Questions
Additional questions beyond those already mentioned in the weakness sections. 

I like the idea of training the encoder / decoder using multiple viewpoints. Using a different scene along with a different camera pose to training view dependent aspects seems elegant. However, I'm not sure that this is really necessary. What is there to be encoded beyond the pose of the camera relative to the manipulator? If there's nothing else, is training the VDE overkill to extract that information from the scene? It'd be interesting to validate what specifically is learned by the VDE (e.g. could you train a readout network to extract relative camera pose?). Also, does this work equally well for more translation and rotation of the camera?

Why does the model performance drop so significantly in the BC results shown in E.2? I can imagine that this might be due to the reference framework used for the robot actions.

A discussion in the context of 3D representations for keyframe-based manipulation would be helpful. Several works, such as [1,2], train a model that is independent of the camera viewpoint by generating actions in the camera frame of reference and then translating these into robot actions using a calibrated camera pose. Could the same idea be applied here?

[1] Perceiver Actor: https://peract.github.io/
[2] 3D Diffusor Actor: https://3d-diffuser-actor.github.io/

### Soundness
2

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
3

### Summary
This study investigates robust robotic manipulation in the presence of camera viewpoints disturbances. It develops viewpoint-invariant representations learning methods with a VAE-like objective. The learned viewpoint-invariant representations are subsequently utilized for robotic control. The experimental results on two simulation environments demonstrate the enhanced robustness across two types of viewpoint disturbances.

### Strengths
1. The approach for learning viewpoint-invariant representations is quite novel. This paper employs a view-invariant encoder and a view-dependent encoder, which take two images from different viewpoints as input. The features encoded by these two branches are then processed through a decoder, utilizing a VAE-like learning objective to decompose view-invariant and view-dependent information.
2. Both the comparative experiments and the ablation studies are thorough.

### Weaknesses
1. The experiments are conducted on two simulation environments only, and the effectiveness of ReViWo on real-world robots remains unvalidated.
2. From Figure 4, even when applying the proposed algorithm ReViWo in this paper, the success rate still significantly declines under disturbances caused by Camera Installation Position (CIP) and Camera Shaking (CSH). This indicates that the enhancement in robustness to viewpoint variations achieved by this method is limited.
3. The representation of Figure 4 is quite misleading. It is recommended to revise it.

### Questions
1. Is the proposed algorithm's performance under viewpoint disturbances stable across different tasks, and does it remain consistent outside the simulation tasks involved in this paper?
2. Why does the integration of Open X-Embodiment data into ReViWo lead to a decline in model performance under Camera Shaking (CSH) for the Door Open task? Additionally, why does the integration of the world model into ReViWo result in reduced performance under Camera Shaking (CSH) for the Drawer Open task?

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
3

### Summary
The draft proposes and evaluates a new approach for learning a view-invariant encoding and world model, in the context of learning vision-based robotic manipulation.

### Strengths
The problem addressed by the draft, view-invariance or at least viewpoint-robustness of learnt robotic manipulation policies, and more generally learning of view-invariant world models, is extremely important and challenging.
The solution proposed by authors for learning a view-invariant representation, which consists in learning a distangling of view-invariant encoding and view-dependant encoding, is appealingly elegant and seems rather original. It also has the interest as a by-product of enabling generation of an arbitrary (?) new view-viewpoint for a given system state, and conversely.
The experiments conducted on Meta-world and Panda-gym reported in the paper are rather convincing regarding the ability of the proposed approach to bring significant viewpoint-robustness (figures 4 and 5), and to learn a relatively view-invariant embedding (figure 6).

### Weaknesses
The main weaknesses of the paper are the following:
 - while the "baselines for comparison" include MVWM, no comparison is conducted with other important very-related works mentioned: RT-X series works and RoboUniView
- the experiments are conducted on a quite small number of tasks (3 out of 50 on Meta-World), and only one (!) in Panda-Gym ; this raises some doubt on possible "cherry-picking" approach for choosing these tasks

 The values of the \lambda_1 and \lambda_2 coefficients for respectively the VQ-term and contrastive-term in the training objective (equation 3) are listed in Table 3 of the annex, but authors provide absolutely no clue on how these values were chosen, and do not analyze how critical these values might be for the result (my intuition is that they should have a significant impact). Could authors clarify that, and ideally provide at least a minimal quantitative analysis/assesment of how important it could be ?

In second paragraph of §4.2, authors write that their proposed method "consistently surpasses the baselines", but on figure 4 it can be seen that for task Window-Close, MVWM has much higher success rate (~85%) than ReWiVo on the CIP case, and slighltly higher succes rate on the CSH case. Authors should NOT "over-claim" in their text compared to figure, and should comment on this lesser performance of their method on this task.
Furthermore, the presentation of figure 4 with "skipping" the 40%-80% part of the y axis is somewhat misleading: this must be corrected, possibly by using higher plots that do NOT skip the 40%-80% range.

Regarding the use of Open X-embodiment data, ablation study reported table 1 shows it has a quite significant impact ; however, authors mention on line 227 that they "introduce a weigthing factor in the loss calculation for these unlabeled data", but it seems they provide no information whatsoever about what value is this weighting and how critical this value could be for the outcome. 
Also, it appears in table 1 that inclusion of this extra data actually *degrade* result in the CSH case for Door-Open task ; author should comment on that.

Examples of the decoder output shown in figure 7 are impressively similar to the ground truth, but are those examples on *test* data or on some of the training data ??
Furthermode, since the success rate falls from over 90% on training data down to below 40% on test data of the 3 first tasks (a) (b) and (c) on figure 4, there must be a significant number of cases for which the view-invariance does not work so well --> authors should show and comment some of these failure cases, to allow readers to qualitatively evaluate what happens when results are not as good as in current figure 7...

In last part of §4.4, authors write that inclusion of their World Model (WM) "present a consistent performance enhancement", while actually in table 2 providing some ablation on the impact of their world model component, WM appears to slightly *degrade* result for CSH case of Drawer-Open task ; author should comment on that.

### Questions
The values of the \lambda_1 and \lambda_2 coefficients for respectively the VQ-term and contrastive-term in the training objective (equation 3) are listed in Table 3 of the annex, but authors provide absolutely no clue on how these values were chosen, and do not analyze how critical these values might be for the result (my intuition is that they should have a significant impact). Could authors clarify that, and ideally provide at least a minimal quantitative analysis/assesment of how important it could be ?

In second paragraph of §4.2, authors write that their proposed method "consistently surpasses the baselines", but on figure 4 it can be seen that for task Window-Close, MVWM has much higher success rate (~85%) than ReWiVo on the CIP case, and slighltly higher succes rate on the CSH case. Authors should NOT "over-claim" in their text compared to figure, and should comment on this lesser performance of their method on this task.
Furthermore, the presentation of figure 4 with "skipping" the 40%-80% part of the y axis is somewhat misleading: this must be corrected, possibly by using higher plots that do NOT skip the 40%-80% range.

Regarding the use of Open X-embodiment data, ablation study reported table 1 shows it has a quite significant impact ; however, authors mention on line 227 that they "introduce a weigthing factor in the loss calculation for these unlabeled data", but it seems they provide no information whatsoever about what value is this weighting and how critical this value could be for the outcome. 
Also, it appears in table 1 that inclusion of this extra data actually *degrade* result in the CSH case for Door-Open task ; author should comment on that.

Examples of the decoder output shown in figure 7 are impressively similar to the ground truth, but are those examples on *test* data or on some of the training data ??
Furthermode, since the success rate falls from over 90% on training data down to below 40% on test data of the 3 first tasks (a) (b) and (c) on figure 4, there must be a significant number of cases for which the view-invariance does not work so well --> authors should show and comment some of these failure cases, to allow readers to qualitatively evaluate what happens when results are not as good as in current figure 7...

In last part of §4.4, authors write that inclusion of their World Model (WM) "present a consistent performance enhancement", while actually in table 2 providing some ablation on the impact of their world model component, WM appears to slightly *degrade* result for CSH case of Drawer-Open task ; author should comment on that.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents ReViWo (Representation learning for View-invariant World model), a novel approach addressing the challenge of viewpoint changes in robotic manipulation tasks. Traditional methods struggle with performance degradation under varying camera angles; ReViWo overcomes this by leveraging multi-view data to learn robust representations for control under viewpoint disturbances. Using an autoencoder framework, ReViWo combines view-invariant and view-dependent representations, trained on both labeled multi-view simulator data and the Open X-Embodiment dataset (without view labels). Tested in Meta-world and PandaGym environments, ReViWo outperforms baseline methods, maintaining stable performance in scenarios with novel camera angles and frequent camera shaking. These results validate ReViWo’s effectiveness in providing robust, task-relevant representations across diverse viewpoints.

### Strengths
View variation is a very practical problem in robotic manipulation. This paper provides good experiments, and leverages Open X-Embodiedment, leveraging this dataset is a promising direction is robotics. Also, the manipulation video in the link is cool.

### Weaknesses
1. The paper shows application in simulation. However, in other specific real world scenarios, there is not enough multi-view data for training. So, I recommend authors to demonstrate how the study can work in the real world, and show real-world evaluation results.

2. This paper only shows results in some simple tasks. Will this method work in more diverse tasks? For example, manipulating deformable objects like folding cloth. These experiments will improve the significance of this paper in robotics field.

### Questions
1. To my knowledge, the output of VAE is blurred. The multi-step world model will enlarge the blurring problem. Could you please how this problem affects this performance? Also, I will appreciate if the author could release the structure of VAE for reproductibilty.

2. Also, will the vae have some errors? For example, will the generated object have different geometries?

2. See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a framework named as ReViWo to learn view-invariant representation (VIR), then uses the VIR as the low-dimensional state representation to train a policy with model-based offline RL (COMBO). 


1. ReViWo includes a view-invariant encoder and view-dependent encoder to reconstruct images at different viewpoints by combining VIR with view-dependent information. 
2. ReViWo was trained from multi-view simulation data and open-x datasets, and then evaluated on selected tasks on MetaWorld and PandaGym environments.
3. The authors show that ReViWo is robust to viewpoint changes in evaluation.

### Strengths
1. It is beneficial to improve the robustness of a robotic policy to camera shaking or viewpoint changes. 
2. Finding low-dimensional state representation for high-dimensional visual signals (such as images), and applying existing offline RL methods on that state representation, is an interesting policy structure.   
3. The writing is easy to follow.

### Weaknesses
 **1. (Fundamental Limitation)**

Robotic tasks heavily depends on the understanding of multi-view camera data. For example, it is very common to have a static top camera and a moving on-gripper camera. The focus is on how to leverage information from different views in order to get better performance instead of only using the very limited invariant information. Therefore, by latching on view-invariant information, the proposed ReViWo is limited to only single-view RGB observation without depth, a highly constrained and often impractical setting in robotics  (Note that if we have RGBD, we could reproject the point cloud to multiple views, so RGBD can be considered as multi-view).

Moreover, suppose there is a desk in a single RGBD image, the camera movement can be viewed as the relative movement of the desk as well. This means that a view-invariant representation will lose some ability to sense object layout changes. This is really undesirable.

**2. (Lack of Technical Contribution)**

The method section looks hand-wavy. The authors propose a view-invariant encoder and view-dependent encoder to reconstruct images and learn view-invariant representation. However, the authors did not provide any mathematical guarantee or at least intuition on why the representation can be disentangled that way. It is very likely that the two encoders just work in parallel without having the expected property. 

Moreover, the authors mentioned the training of a world model and training a reward model, but in fact, they used the COMBO method to do all these [1]. I am not sure whether COMBO, an offline model-based RL method, can be called a world model because it only predicts the next low-dimensional state. The COMBO framework includes the training of a reward model, so it is not the contribution of this method. 

**3. (Lack of Proper Evaluation)**

The authors only evaluate on MetaWorld and PandaGym, two very simple task suites in terms of manipulation diversity, precision, horizon length. Even on these simple task suites, the authors only select 3 tasks from MetaWorld and 1 task from PandaGym, while the MetaWorld has roughly 50 tasks. This evaluation is very insufficient.

### Questions
(see weakness)

### Soundness
2

### Presentation
3

### Contribution
2
