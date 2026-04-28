# Joint Representations for Reinforcement Learning with Multiple Sensors

- Decision: Reject
- Avg Score: 5.25
- Scores: 3, 5, 8, 5

## Abstract
Combining inputs from multiple sensor modalities effectively in reinforcement learning (RL) is an open problem. While many self-supervised representation learning approaches exist to improve performance and sample complexity for image-based RL, they usually neglect other available information, such as robot proprioception. In this work, we show how using this proprioception for representation learning can help algorithms to focus on relevant aspects and guide them toward finding better representations. Building on Recurrent State Space Models, we systematically analyze representation learning approaches for RL from multiple sensors. We propose a novel combination of reconstruction-based and contrastive losses, which allows us to choose the most appropriate method for each sensor modality, and demonstrate its benefits in a wide range of settings. This evaluation includes model-free and model-based RL on complex tasks where the images contain distractions or occlusions, a new locomotion suite, and a visually realistic mobile manipulation task. We show that learning a joint representation by combining contrastive and reconstruction-based losses significantly improves performance compared to the common practice of combining image representations and proprioception and allows solving more complex tasks that are beyond the reach of current SOTA representation learning methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a framework to jointly learn representations from vision and proprioception sensors based on the recurrent state space model (RSSM). It systematically studies the ways to combine contrastive and reconstruction losses on different sensor inputs through comprehensive experiments.

### Strengths
1. In general, the writing is clear and easy to follow
2. The experiments are solid and comprehensive. The experiment section and appendix present the results of various joint representation learning designs (CV, CPC, reconstruction) as well as different ablations (concat, image-only, state-only) and baselines (model-free, model-based) under different environment settings. 
3. Code is provided with good reproducibility.

### Weaknesses
1. While the overall logic is clear and smooth, some specific notations and figures are confusing. 

    (a) From the figure plotted in the main paper or appendix, it's very hard to draw any conclusions about which representation learning method is the best. Instead of presenting the curves, drawing some bar charts about the final performance average over different settings and environments can be more straightforward.

    (b) The figures in the main paper (Figure 2, 3, 4) are interleaving with model-free/model-based and occlusion/locomotion, which makes it hard to understand what's been delivered

    (c) There is no explanation of e.g, Joint(CV+R), Joint(CPC+R) which make the confusion that the "+R" is for reward reconstruction.

2. The results are not clear or convincing enough to draw a strong conclusion as in the discussion section

    (a) The environmental and experimental design is not delivered clearly. Please address Questions 1. a for clarification.
    
    (b) "In the more difficult settings, i.e., Occlusions, Locomotion (Fig. 4), and OpenCabinetDrawer (Fig. 5), using a joint representation gives the largest benefits", "In the Locomotion experiments, the CPC approaches (Fig. 4) have a significant edge over reconstruction", which is only true for model-based occlusion (Fig. 4), and for Fig. 5 the gain is unclear (see question 1. b).

    (c)  "In the Locomotion experiments, the CPC approaches (Fig. 4) have a significant edge over reconstruction". First, the gain is not significant. Second, Locomotion's model-based results are missing.

    Understandably, there may not exist a unified framework that works best for model-based and model-free RL. Given that many details are missing, the conclusion seems too strong and not rigorous enough. Some possible improvements e.g. separately discuss (i) model-free and model-based, (2) locomotion and manipulation, and (3) standard image and background changes, to make a less strong but more rigorous conclusion. Also DMC's results are very saturated, it might be more convincing to include more diverse domains (e.g. more Maniskill/RLBench/FrankaKitchen results).

3. The formulation in equation (4) is not mathematically rigorous. If CPC is applied to estimate the MI between the current representation and the next observation, the KL part should be factorized differently but not naively apply equation (1). 

4. Typo in caption: Figure 9 should be model-based results.

### Questions
1. Task and experimental details

    (a) Is the "standard image" /"video background" / "occlusion" suite all modified from environments in Table 1? Are the curves averaged in each suite? How many seeds do you run for each task? The curves in each figure have low variance, which doesn't look like an average as different tasks require very different sample complexities in each suite. If you normalized that, how the normalization was done?

    (b) Are the Maniskill results model-free or model-based? Why only a SAC baseline is included?

    (c) Why the locomotion's model-free results are missing?

2. Model details

    (a) For the model-free results, are you also reconstructing reward based on latent representation z?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of reinforcement learning from observations collected across different sensors, and in this work, specifically, image observations and robot proprioception. The representation learning method aggregates historical observations through the Recurrent State Space Model (RSSM). The main difference from prior work is that the latent representation is now trained to be predictive of observations from multiple sensors. The experiments are conducted in various simulated vision-based environments, including an ego-centric cheetah-run task with obstacles.

### Strengths
- The experiments study a range of and introduce some new environments, from locomotion to manipulation with moving backgrounds and with occlusions. These settings are particularly challenging because they rely (1) on robust representation learning and (2) on both vision and proprioception.
- The proposed approach tackles both of these challenges by learning a representation that is task-relevant and represents both modes of observation.
- The observation that the joint representation leads to more efficient RL over concatenation is useful for practitioners.

### Weaknesses
 - The experiments only look at image observations and proprioception as the two modalities. It would be interesting to see this approach applied to other sensor modalities.
- The extension of RSSMs to model both image observations and proprioception is a straightforward one, which is the primary contribution of this work.
- It seems like the correct loss for each modality varies quite a bit across domains.
- I'm still unclear on details for some of the comparisons and results (see Questions).
- The paper lacks a thorough analysis of the computational overhead introduced by the joint representation, especially concerning the increased dimensionality and processing requirements compared to simply concatenating the sensor data. This is important for practical applications.
- The choice of using a fixed variance for the proprioception decoder in the OpenCabinetDrawer task, while simplifying the implementation, could potentially limit the model's ability to adapt to the varying uncertainty levels in different proprioceptive signals. A more adaptive approach to modeling proprioceptive uncertainty may lead to better performance.

### Questions
- Why do you think there is such a gap between Joint and Concat, where Concat performs the same as ProprioSAC on the cabinet tasks? It seems like Concat should be able to produce any representation that Joint can. Does Concat eventually converge to the same performance as Joint in Fig. 5 if we let it train for longer?
- Do the DenoisedMDP and DreamerPro comparisons utilize observations from both modalities?
- In Fig. 6 (right), are the images reconstructed from a separately trained decoder as a way to probe the representations? 
- How are the losses for different observation modalities weighted against each other?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studies RL problems with multiple modalities of different nature, i.e., images and proprioception. The authors argue that reconstruction and contrastive objectives for representation learning, studied separately in prior work, are better tailored to each modality and combined in a joint fashion. This proposal is realized in the recurrent state-space model (RSSM) framework, where the authors extend the formulation to multiple modalities. To further highlight the strengths of each combination, the authors propose new datasets and tasks, and perform an extensive comparison against a variety of baseline models.

### Strengths
- Extends the RSSM model to multiple observation models to account for multi-modalities
- Introduces two datasets with specific additional challenges: VideoBackgrounds and Occlusions
- Introduces a new Locomotion benchmark with a focus on egocentric vision for obstacle avoidance (6 tasks)
- Performs additional experiments in the OpenCabinetDrawer task with variations in lighting and surroundings
- Extensive comparison over a large collection of model families

### Weaknesses
Nothing stands out, beyond the remaining questions pointed out in the limitations section, also raised in the questions below.

**Missing technical discussion:**
- Is it possible to combine both contrastive learning paradigms? Or, to alternate between the two objectives at each epochs based on a given metric? Looking again at the discussion leading up to Eq.2 and Eq.3, there's no clear reason to favor one over the other. Moreover, as the two equations are pretty similar, perhaps it hints at a more general form. (Could the CV term be an alternative to the reward-based regularizer?). It's a useful ablation study to study CV or CPC in isolation, but since the experiments show distinct advantages to each formulation, it's likely the agent can learn to combine the two flavors. (Now I also see no reason why there's no Joint(CV + CPC) or Joint(CPC + CV) in the experiments. Makes me wonder why the authors completely overlook this option.)

**Presentation:**
- Abstract, last sentence: please clarify at this point what is meant by "common practice", as explained in the 3rd paragraph of the introduction.
- Section 3:
    - Suggest to break up the paragraph before Eq.2, possibly using a bold header corresponding to the block for CPC.
    - The inputs to the score functions seems to be flipped at the end of S3.1
- Section 4:
    - It would help to e.g. move the "Representation Learning Methods" paragraph to the beginning of the section before any of the figures to help read the legend.
    - ProrioSAC -> ProprioSAC

### Questions
**Missing technical discussion:**
- Is it possible to combine both contrastive learning paradigms? Or, to alternate between the two objectives at each epochs based on a given metric? Looking again at the discussion leading up to Eq.2 and Eq.3, there's no clear reason to favor one over the other. Moreover, as the two equations are pretty similar, perhaps it hints at a more general form. (Could the CV term be an alternative to the reward-based regularizer?). It's a useful ablation study to study CV or CPC in isolation, but since the experiments show distinct advantages to each formulation, it's likely the agent can learn to combine the two flavors. (Now I also see no reason why there's no Joint(CV + CPC) or Joint(CPC + CV) in the experiments. Makes me wonder why the authors completely overlook this option.)

**Presentation:**
- Abstract, last sentence: please clarify at this point what is meant by "common practice", as explained in the 3rd paragraph of the introduction.
- Section 3:
    - Suggest to break up the paragraph before Eq.2, possibly using a bold header corresponding to the block for CPC.
    - The inputs to the score functions seems to be flipped at the end of S3.1
- Section 4:
    - It would help to e.g. move the "Representation Learning Methods" paragraph to the beginning of the section before any of the figures to help read the legend.
    - ProrioSAC -> ProprioSAC

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes representation learning in reinforcement learning using multi-modal data sources. It aims to enhance representation learning by constructing Recurrent State Space Models tailored with specific objectives for each modality. This work's contribution lies in optimizing the integration of low-dimensional modalities (like proprioception) with high-dimensional, noisy modalities (such as images) to enhance representation learning for RL. The paper suggests employing a reconstruction loss for proprioception data and a contrastive loss for image observations. This work performs experiments on a modified version of the DeepMind Control Suite (DMC) and Mujoco tasks such as Cheetah Run and OpenCabinetDrawer task from ManiSkill2. The results underscore that utilizing a combined representation with appropriate loss functions can improve the performance of RL-based methods.

### Strengths
- This framework introduces a clear joint training framework for multi-modal reinforcement learning. It employs reconstruction loss proprioception data and contrastive losses for noisy high-dimensional inputs, such as images. The method is straightforward in both comprehension and implementation.
- Extensive testing on various benchmarks as tasks and baseliens including model-free and model-based RL baselines.

### Weaknesses
 - Firstly, if the joint representations (adding proprio and images) improves performance over learning an image-only or proprio-only representation, I do not find this surprising. It makes sense that adding more informations improves the performance.
- Secondly, adding different losses for each modality, contrastive for images and reconstruction for proprioception, as the central contribution of this work is weak. What can however make this paper a stronger contribution is pursuing other sensor modalities (depth images, surface normals, segmentations, etc) and then exploring various appropriate losses there. As it stands, the paper is only applying a typical reconstruction-based loss to the proprio and contrastive to the image, which are the current norms in the field - no exciting surprise!
- Thirdly, even though this work provides extensive experiment results, in many figures, the methods showing the effect of each loss, for instance `Joint(R+R)` and `Joint(CV+R)`, the performance of these seem to be on-par with each other e.g. `Figure 8, Figure 2, Figure 3` etc. 
- Even though its nice the huge amount of analysis performed in this work, the concluding story is very hard to digest, specially since there are many different acronyms to their proposed method such as `Joint(R+R), Joint(CPC+R), Joint(CV+R)`. In addition, some baselines are missing for some tasks (e.g. `Figure 5`) and it makes drawing a final conclusion hard.
- I also disagree with the following statement made in the paper ` While many self-supervised representation ...  neglect other available information, such as robot proprioception`.  Adding proprioceptive state observations along with images is not novel in the field (especially in robotics).

### Questions
- Except for combining multi-modal inputs with appropriate losses per each, are there any other interesting take-away observations from this work?
- Is there a reason many of the model-based baselines are missing for the `OpenCabinetDrawer` task?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
