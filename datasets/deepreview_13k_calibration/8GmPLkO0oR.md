# NeRFuser: Diffusion Guided Multi-Task 3D Policy Learning

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 3, 8

## Abstract
This paper presents \ours, a language-conditioned multi-task policy framework that integrates neural rendering pre-training and diffusion training to enforce multi-modality learning in action sequence spaces. To learn a generalizable multi-task policy with few demonstrations, the pre-training phase of \ours leverages neural rendering to distill 2D semantic features from foundation models such as Stable Diffusion to a 3D space, which provides a comprehensive semantic understanding regarding the scene. Consequently, it allows various applications to challenging robotic tasks requiring rich 3D semantics and accurate geometry.
Furthermore, we introduce a novel approach utilizing diffusion training to learn a vision and language feature that encapsulates the inherent multi-modality in the multi-task demonstrations. By reconstructing the action sequences from different tasks via the diffusion process, the model is capable of distinguishing different modalities and thus improving the robustness and the generalizability of the learned representation.
\ours significantly surpasses SOTA NeRF-based multi-task manipulation approaches with over 30\% improvement in success rate. Project website: \ourwebsite.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes NeRFuser that utilizes volume rendering pre-training and diffusion processes to learn the inherent multi-modality in the multi-task demonstrations. NeRFuser developes a 3D encoder capable of providing 3D semantic information in pre-training phases. In order to integrates multi-modal features, NeRFuser formulate the representation learning as an action sequence reconstruction with DDPM. It outperforms baseline approaches with an improvement of over 30% in 10 RLBench tasks and 5 real robot tasks.

### Strengths
1.The proposed idea is reasonable and its framework is well designed.
2.The authors provide adequate experiments and visualization results.

### Weaknesses
1.The author did not clearly articulate the motivation and contributions of the paper.
2.In my opinion, the writing of the paper is confusing. For example, in the first paragraph of introduction, why are the issues raised considered important and in need of resolution? As a researcher in another field, I cannot determine if this is a consensus within the field or the personal opinion of the author. 
3.Based on the author's statements in the second paragraph of the introduction and the proposed methodology, it gives me the impression that the two methods have been cleverly combined together, lacking novelty to some extent.

### Questions
1.In Table 1, there seems to be a significant discrepancy between the performance of PerAct and the results reported in the original paper. Is this difference due to variations in the calculation of metrics or because the PerAct used for comparison in the experiments did not fully converge?
2.In the original paper, the author argues that the extensive inference time of diffusion models is a significant drawback. However, why is this issue resolved by adding a policy network? Additionally, I did not find any results related to speed or inference time in the experimental section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This method integrates neural rendering pre-training (with diffusion-based foundation model) and diffusion training to learn a unified 3D representation for multi-task robotic manipulation in complex environments. The 3D encoder is pre-trained using NeRF to synthesise novel views, predicting corresponding semantic features from Stable Diffusion, language-2D foundation model. This pre-training representation equips the policy with out-of-distribution generalisation ability. The paper shows clear performance improvements compared with previous methods and baselines.

### Strengths
1. Overall architectural choices are reasonable and intuitive with clear reasoning.
 - Denoising objective the authors adopted is well-known to have a good performance in terms of representation learning
 - The authors utilize distillation of Stable Diffusion to improve generalization, which can be clear motivation.
- The above things are well combined in two-phase framework.
2. The authors provide abundant analysis (generalization, ablation on components of the framework) in simulation and real world.

### Weaknesses
 - One major concern is a lack of explanation about how the foundation model (Stable Diffusion) is integrated in Sec 2.2. I couldn't find what F(r) exactly is. Are per-pixel features from Stable Diffusion? Then, how exactly was the feature derived? What is the language condition? What was the timestep set to? Which layer of the Stable Diffusion U-Net's features did the authors utilize? Are these settings sensitive to changes in hyper parameters? Utilizing features from the Text-to-Image diffusion model or distilling the information contained in the diffusion model into 3D representations like NeRF is in itself a significant area where active research is being conducted.  I think a detailed explanation, reasoning, and related experiments on this are needed. If I've misunderstood something, I'd appreciate it if the authors could explain further.

- It is just a minor thing, but Table 4 is ambiguous. I think it would be good to supplement it a little more so that it's easy to understand.

### Questions
1. Please see weaknesses.
2. I'm quite interested in the results shown in Figure 5. Could you explain the results? I couldn't find a paragraph mentioning Figure 5. Could you show more visualization results in other settings (unseen, out-of-distribution, without distillation of vision foundation models)?

I'm willing to raise my rating if my concerns are addressed well.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a method for language-conditioned multi-task policy learning. NeRFuser pretrains a visual representation using novel view synthesis as an objective with volume rendering. The method uses stable diffusion to distill semantic features into a 3D voxel encoder. Then the method uses Denoising Diffusion Probabilistic Models to reconstruct action sequences to train the decoder which fuses the encoded text from CLIP, the NeRF encoder, and PointNext encoded point clouds. Finally the method learns a policy on top of the learned representation. The paper performs experiments on RLBench and a real-world tabletop environment. NeRFuser shows significantly improved success rate over two recent methods, GNFactor [1] and PerAct [2]. 

1. GNFactor: Multi-Task Real Robot Learning with Generalizable Neural Feature Fields.
2. Perceiver-actor: A multi-task transformer for robotic manipulation.

### Strengths
- The performance gains over GNFactor and PerAct are statistically significant (over 16% higher success rate across 10 tasks).
- The benchmarking experiments are extensive with 5 real-world tasks, 10 in-distribution simulated tasks, and 5 unseen simulated tasks. 
- The method figure is clear and helps to understand all of the components of NeRFuser.

### Weaknesses
 - The stated technical contributions have been proposed by previous works.
    - In the abstract the work claims as a contribution: “NeRFuser leverages neural rendering to distill 2D semantic features from foundation models.” However, this exact setup was proposed by GNFactor [1]. 
    - The other contribution is stated to be:  "We introduce a novel approach utilizing diffusion training to learn a
vision and language feature". This approach seems very similar to previous works Janner et al. [2] and Huang et al. [3]


1.  GNFactor: Multi-Task Real Robot Learning with Generalizable Neural Feature Fields.
2. Planning with diffusion for flexible behavior synthesis
3. Diffusion-based generation, optimization, and planning in 3d scenes

- Given the close similarity to GNFactor, it would be useful to have experiments to analyze which component of NeRFuser is providing the improved performance. The ablation study which changes out stable diffusion for other pretrained models is interesting, but doesn't show the merits of NeRFuser over GNFactor. 
- A potential weakness of the method, albeit minor is that it requires a specialized setup during training with multiple calibrated cameras. 

- Details are unclear, particularly in the methods section (see questions).

### Questions
- The quantitative numbers for GNFactor from their paper differ significantly (sometimes as much as 20% success rate) than the ones reported in NeRFuser, could you explain why the performance differs so much in your setup?
- It’s unclear in Table 3 what the commands drawer, meat, and safe mean. Slide and place make sense as natural language commands for the encoder, but the other words don’t seem like commands.
- Frames are passed to the system as pointclouds, but there is no mention of how the point clouds are obtained.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a method for robot instruction following. In the first phase, it trains a 3D encoder that converts a voxelized representation of a 3D scene to its 64-dimensional latent representation. the encoder is trained such that the latent representation can reconstruct the scene's radiance field as well as features distilled from 2D vision models such as Stable Diffusion, DINO or CLIP. In the second phase, the 3D encoder is frozen, and PointNext + a policy model is trained. the 3D latent representation is used in combination with PointNext features and a pre-trained language encoder to produce fused features, which are then the input to the policy model. The policy model is an MLP trained to predict Q values, alongside a diffusion model that seeks to generate action sequences. The authors demonstrate this method on a number of robotic manipulation tasks.

### Strengths
The work is very clearly presented with a nice project page and good figures. The authors will release code.
They perform solid experiments with thorough baseline comparisons and ablations. They make a number of interesting insights, including the superiority of Stable Diffusion as a 2D teacher to CLIP or DINO features, and the ability to pretrain the 3D encoder on out of distribution data and still achieve good performance. The experimental results and model capabilities are not groundbreaking, but are still a meaningful improvement of the state of the art on a challenging task.

### Weaknesses
This method has several limitations, although most of these limitations are shared by many other works in this area:
- the reliance on point cloud voxelization means that the entire scene must be completely observed up front and small enough to be voxelized. this makes it unusable for e.g. autonomous driving / robot navigation in large scenes. The voxelization process also introduces a discretization of the input space which could limit the precision of the learned representations, especially for fine-grained manipulation tasks.
- I am skeptical that the neural rendering objective can achieve stronger forms of generalization. "New position", "larger object" and "distractors" are all fairly weak forms of generalization, and I suspect the method would not be able to generalize to new environments or objects that have the same semantics but significantly different appearance from the training set. Ideally Stable Diffusion can help bridge this gap, but I assume the authors tried tougher OOD tasks and the method didn't work. The reliance on Stable Diffusion features also introduces a potential bottleneck, as the quality of these features is dependent on the pre-training data and architecture of the Stable Diffusion model itself. It is unclear how the method would perform if the visual appearance of the objects significantly deviates from the distribution used to train Stable Diffusion.
- the gap between the final checkpoint and the best checkpoint suggests to me that the training for these models is still quite unstable and requires a lot of tuning. I do see that this is a weakness of all the baselines too. This instability could be due to the multi-task nature of the training, where the objectives for the 3D encoder, policy model, and diffusion model might be conflicting or require careful balancing of their respective loss functions.
- going from a voxel grid to its radiance field is a little strange. the voxel grid already stores RGB and occupancy, so the 3D encoder basically has to learn the identity function and only recover view dependence to turn it into a radiance field. so I suspect the NeRF (RGB) objective barely contributes to learning at all. maybe the authors can verify / refute this. It is not clear why a radiance field representation is necessary when the voxel grid already encodes the necessary geometric and color information. The added complexity of learning a radiance field might introduce unnecessary computational overhead without significant benefits.
- the method seems quite general but the types of environments/tasks explored in this paper are fairly constrained. it would have been nice to see some more diverse environments / agents

### Questions
- I don't particularly like the name NeRFuser because it sounds like a method for improving/fusing NeRFs. I also feel like the neural rendering component here is not the most important part of the pipeline, and the 2D teacher is at least equally as important. See if you can come up with a better name.
- I am not entirely sure what is the pre-training / training / test set for the real robot experiment. I think it would be interesting if you trained only on RLBench and tested on real robot tasks, but my understanding is that this combination was not tried. it would also be nice to repeat the real robot results several times to report stdev in the table
- can you describe exactly how the stable diffusion features are extracted? you feed in the input image, encode it, add noise (to which timestep?), then denoise (in 1 step)?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
