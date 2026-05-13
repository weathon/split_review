# 3D Diffuser Actor: Multi-task 3D Robot Manipulation with Iterative Error Feedback

- Decision: Reject
- Scores: 3, 6, 1, 5

## Abstract
We present 3D Diffuser Actor, a framework that marries diffusion policies and 3D scene representations for robot manipulation. Diffusion policies capture the action distribution conditioned on the robot and environment state using conditional diffusion models. They have recently shown to outperform both deterministic and alternative generative policy formulations in learning from demonstrations. 3D robot policies use 3D scene feature representations aggregated from single or multiple 2D image views using sensed depth. They typically generalize better than their 2D counterparts in novel viewpoints. We unify these two lines of work and present a neural policy architecture that uses 3D scene representations to iteratively denoise robot 3D rotations and translations for a given language task description. At each denoising iteration, our model “grounds" the current end-effector estimate in the 3D scene workspace, featurizes it using 3D relative position attentions and predicts its 3D translation and rotation error. We test 3D Diffuser Actor on learning from demonstrations in simulation and in the real world. We show our model outperforms both 3D policies and 2D diffusion policies and sets a new state of the art on RLBench, an established learning from demonstrations benchmark, where it outperforms the previous SOTA with a 12% absolute gain. We ablate our architectural design choices, such as translation invariance through 3D grounding and relative 3D transformers, and show they help model generalization. Our results suggest that 3D scene representations and powerful generative modeling are key to efficient learning of multi-task robot policies.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a framework called "3D Diffuser Actor," combining diffusion policies and 3D scene representations to enhance robot manipulation. Along with 3D scene features aggregated from single or multiple 2D image views using sensed depth, these policies enable improved generalization over 2D counterparts. The new model’s architecture uses 3D scene representations to iteratively rectify robot 3D rotations and translations given a language description of a task. The experiments demonstrate the efficacy of the proposed framework by outperforming previous benchmarks in learning from demonstrations, both in simulated environment and real world.

### Strengths
The authors conduct a thorough evaluation of their method as they evaluate their method in both simulated environment and real world, and comparing them with existing strong baselines. A thorough evaluation have us better understand the proposed model and their actual performance.

### Weaknesses
1. The scientific contribution of this paper is unclear. Diffusion model could not be the contribution of this paper, and adopting diffusion mode for trajectory generation is not a new idea (see [a]). 
2. The figures in this paper lack sufficient illustrative value and information. For instance, Figure 1 appears to show the model taking a multi-view image as input, yet the caption indicates it uses a 3D scene feature cloud. A clear connection between these two elements would greatly improve understanding.

### Questions
Your diffusion model appears to produce only the target pose of the action, after which a trajectory is generated using the MoveIt planner given the initial joint state and target joint state. Does the robot execute the entire trajectory directly until the end, or does it update the target pose using the diffusion model and regenerate the trajectory after each forward step?

### Soundness
2 fair

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
This paper proposes 3D Diffuser Actor, a transformer-based behavior-cloning method that combines the power of diffusion policies and 3D scene representations. The model tokenizes multi-view camera observations, language instructions, and the history proprioception information. A 3D relative transformer models the diffusion process, processing these tokens to predict the next gripper pose over several diffusion steps. The experimental results showcase the remarkable performance of the proposed method, outperforming several strong baselines in the RLBench environments.

### Strengths
The experimental results are exceptionally strong, demonstrating a substantial improvement over various recently proposed baselines (from late 2022 to mid-2023).

### Weaknesses
1. The method's description lacks clarity, particularly concerning crucial components of the architecture. The appendix does not sufficiently clarify these ambiguities either.
2. The backbone of the proposed network is extremely similar to Act3D, including using multi-view image input, using the pyramid network for feature exaction, the generation of the 3D feature cloud, and the 3D relative transformer. I understand that Act3D is a very recent work, however, as the authors are already aware of Act3D, proper discussion regarding the relationship between this work and Act3D should be addressed.

### Questions
1. When building the 3D scene feature cloud, the authors claim, `We associate every 2D feature grid location in the 2D feature maps with a depth value, by averaging the depth values of the image pixels that correspond to it.` What is a `grid` here? Is each 2D feature map from the feature pyramid network separated into an NxN grid akin to ViT?
2. When generating the 3D feature cloud, how does the method handle cases where multiple points (pixels) from different views correspond to the same 3D location? Are the features averaged in such instances?
3. What constitutes a visual token in this context? Are individual 3D points considered tokens?
4. The performance of the proposed method is notably poor in close jar and sort shape. Could the authors provide a detailed failure analysis to shed light on these issues?
5. Given that diffusion policies suggest the utility of diffusing multiple action steps into the future, has the method been evaluated with multiple keypoint steps in the diffusion process?

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a framework that marries 3D scene representations and diffusion policies for imitation learning of robot manipulation tasks. The proposed scene representation is a 3D feature cloud fused from multi-view, multi-scale CLIP features using depth maps, which encodes semantics and spatial information. The diffusion policy captures the multimodality of action distribution. In the experiments, the proposed method is compared against multiple baselines on the simulated RLBench dataset, and tested on 5 real-world tasks. Ablation studies further verify the necessity of the 3D representation and the use of relational attention.

Note that many of the design choices and setups in this work are largely based on Act3D [1].

[1] Theophile Gervet, Zhou Xian, Nikolaos Gkanatsios, and Katerina Fragkiadaki. Act3d: Infinite
resolution action detection transformer for robotic manipulation. CORL 2023.

### Strengths
This paper is probably the first work to combine 3D scene representations with diffusion policy for learning robot manipulation tasks. The proposed framework demonstrates good performance in both simulation and real-world experiments, and establishes a new SOTA on RLBench tasks.

### Weaknesses
My initial impression of this paper is that some aspects of the method lack clarity, and certain paragraphs appear somewhat inconsistent. I found myself confused about specific technical details until I reviewed Act3D [1], a previous paper that this work heavily draws upon. 

**My primary concern about this work is that a portion of the technical method and writting appears to be directly borrowed from [1]. However, this relationship is not transparently acknowledged.**

1. The proposed framework adopts the 3D scene representation (in a simplified form), 3D relational transformer, and training/evaluation setups from [1], which is never explicitly mentioned in the paper.
2. The main contribution of this work lies in the use of a diffusion policy to capture multimodal action distributions. However, this aspect is not extensively discussed or thoroughly evaluated.
3. Not only the writing style of this paper closely resemble Act3D [1], but some paragraphs have similar or even same counterparts in [1]. Detailed in ethics review.

### Questions
N/A

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes 3D Diffuser Actor, a new behavior cloning algorithm combining diffusion policy and 3D representations for multi-task robotic manipulation. Utilizing the 3D representation and the attention mechanism, the proposed method achieves new SOTA on RLBench tasks. The authors also conduct real robot experiments with the newly proposed method, showing the applicability of the diffusion-based actor.

### Strengths
- **Motivation is good and natural**. Diffusion policies have achieved success in fitting distributions, and introducing them into 3D is a necessary step.
- **Good results and extensive experiments.** The results (12\% improvements) seem to be significant, which are gained on a multi-task benchmark across diverse tasks, and showing some real robot experiments are also very necessary for such robotic manipulation agents.

### Weaknesses
- **No deeper analysis about why diffusion models could help**. The ablation results only show two factors matter, but all these factors seem to be not novel and not surprising, thus deeper analysis might be necessary. I have also checked the supplementary files and the presented Figure 7 looks interesting, but why `scaled linear` is worse than `square cosine` when the former one seems to cover the original distribution better?
- **The inference time and the denoising steps are both not clear.** The proposed method achieves 12% absolute gain, but considering the inference time of diffusion models, this gain might be not obvious in the real world, due to huge latency. Could the authors also report the wall time between different algorithms?
- **The evaluation process is not clear**. Is the result in Table 1 the best success rate over a lot of checkpoints? And how many training 
epochs are used? How many episodes are tested during the evaluation? How many seeds are used for the main results (Table 1)?
- **Lack of baselines in real robot experiments**. 
- **Lack of discussion and experiment comparison with recent related works such as GNFactor [2].** I think this very recent method [1] could possibly serve as a baseline and it would be good to see some direct experiment results.
- **Lack of multi-task manipulation results in real robot experiments**. Both PerAct [1] and GNFactor [2] have shown ability to execute real-world multi-task manipulation, and it could be good to compare the multi-task performance in real robot also, considering this work is closely related to PerAct [1] and GNFactor [2].
- **Typo** in Figure 2 (a): Acter -> Actor

Overall, I tend to reject this paper with a score slightly lower than borderline,  considering the above issues for the initial review.  I would carefully consider raising my score if my questions are well addressed. 

[1] Shridhar, Mohit, et al. "Perceiver-actor: A multi-task transformer for robotic manipulation." CoRL, 2022.

[2] Ze, Yanjie, et al. "Gnfactor: Multi-task real robot learning with generalizable neural feature fields." CoRL, 2023.

### Questions
See `weakness` above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
