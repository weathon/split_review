# AlignDiff: Aligning Diverse Human Preferences via Behavior-Customisable Diffusion Model

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
Aligning agent behaviors with diverse human preferences remains a challenging problem in reinforcement learning~(RL), owing to the inherent \attrabs~and \attrdyn~of human preferences. To address these issues, we propose \textbf{AlignDiff}, a novel framework that leverages RLHF to quantify human preferences, covering \attrabs, and utilizes them to guide diffusion planning for zero-shot behavior customizing, covering \attrdyn. AlignDiff can accurately match user-customized behaviors and efficiently switch from one to another. To build the framework, we first establish the multi-perspective human feedback datasets, which contain comparisons for the attributes of diverse behaviors, and then train an attribute strength model to predict quantified relative strengths. After relabeling behavioral datasets with relative strengths, we proceed to train an attribute-conditioned diffusion model, which serves as a planner with the attribute strength model as a director for preference aligning at the inference phase. We evaluate AlignDiff on various locomotion tasks and demonstrate its superior performance on preference matching, switching, and covering compared to other baselines. Its capability of completing unseen downstream tasks under human instructions also showcases the promising potential for human-AI collaboration. More visualization videos are released on \href{https://aligndiff.io/}{https://aligndiff.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper utilizes the diffusion model conditioned on attributes for planning. Inspired by RLHF, this paper first fits a reward model trained to predict preference over trajectories given human preference, followed by using it to predict the attribute strengths given the episode. This is then used to label the unlabelled episodes with the corresponding attributes, which are then used to condition the diffusion model, trained in a classifier-free guidance sense.  

The paper shows the advantages of the proposed technique over existing baselines for learning the policy including on human preferences, and tests its robustness when the strengths are suddenly changed in between. Lastly, an ablation of label pool size is done to understand its impact on learning the reward model.

### Strengths
The paper is easy to follow in most places, and I like the experiments on the robustness and label efficiency of the reward function.

### Weaknesses
As someone who is not well versed in the empirical reinforcement community, my weak comments would be high level and mostly some of my confusion throughout the paper.

- Can authors provide the inter-annotator correlation when they're labeling the reward model? Annotator alignment is a problem in the RLHF community when it comes to LLMs and even RLHF for diffusion models in image generation (See [1]) therefore it would be good to see some numbers on annotator agreement.

- Can authors provide the accuracy of the reward model after training it based on human preference? Does the Area metric in Table 5 correspond to that? Moreover, what is the accuracy of random guessing? I am assuming it would be 50%?

- Are there any ablations done in case one does not apply masking in the way current AlignDiff is applying? What if one just used 0s in the strength where it is not needed? I think having that result would further showcase the utility of masking in the current way.

- How exactly is BERT used in the pipeline? How is the mapping from BERT representations to strength and mask learned?

- How is the performance affected by the precision of discretization?

- $\mathcal{B}(k, p)$ is not defined.

- How is the performance of the reward function (that predicts strengths) affected by the length of episodes, when varied during training and inference time (zero-shot say)?

### Questions
Refer to the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a method for aligning agent behaviors with human preferences. Firstly, it introduces multi-perspective human feedback datasets. Secondly, it trains an attribute-conditioned diffusion model, referred to as AlignDiff, to act as a director for preference alignment during the inference phase. AlignDiff utilizes Reinforcement Learning from Human Feedback (RLHF) to quantify human preferences, allowing it to match user behaviors and seamlessly transition between different preferences.

### Strengths
1. The proposed diffusion-based framework demonstrates exceptional performance in decision-making scenarios involving complex dynamics.
2. The method presented in this paper is capable of effectively matching user-customized behaviors and seamlessly transitioning between different preferences.
3. Additionally, this paper introduces a valuable contribution in the form of a multi-perspective human feedback dataset. This dataset has the potential to facilitate the wider adoption of human preference aligning techniques.
4. The proposed method leverages a multi-stage diffusion process, which effectively simulates the reinforcement learning (RL) process.

### Weaknesses
1. Both the proposed method and RBA utilize RLHF for aligning agent behaviors with human preferences. The novelty is unclear.
2. The diffusion model usually achieves the best result in the final step. How does the diffusion model guarantee the best human preference at each step? Does the proposed method obtain a plan with T diffusion steps? If so, how about the inference time?
3. The proposed method only did some ablation studies and has not compared with the state-of-the-art methods, such as RBA.

### Questions
1. What is the inference time?
2. How about the comparison with the state-of-the-art methods, such as RBA.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on the issue of consistency between agent behavior and human preferences in RLHF, and proposes an alignment method based on the diffusion model. The authors construct a multi-perspective human feedback dataset and train an attribute model, which is then used to relabel the dataset. A diffusion model is utilized as a planner and it's trained on the preference-aligned dataset. In this way, the authors achieve preference aligning between different human. Both quantitative and qualitative experimental results demonstrate the effectiveness of this method.

### Strengths
1. The authors revisit the impact of inherent human annotator preferences on reinforcement learning training, which is illuminating.

2. The proposed method is innovative and achieves relatively good results, which is demonstrated by the experiments.

3. The visualizations and supplementary material provided in the website support the paper and make it easier for readers to understand.

4. The paper is clearly written and well organized.

### Weaknesses
1. The paper does not include ablation experiments on attribute model training, so the actual effect of attribute alignment is not easy to measure.

2. The explanation of some details of the method is not clear enough. For example, the meaning of equation (5) and "inpainting manner" needs further clarification.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a diffusion model with RLHF to train an RL agent that follows human preferences and instructions. A attribute strength model is trained on a newly built human feedback datasets, which is leveraged to annotate the behavior dataset. Extensive experiments are conducted on the proposed method in terms of the preference matching, switching, and covering. All achieves superior performance compared to baselines.

### Strengths
1. The idea of using RLHF to align human preference is reasonable and insightful.  
2. The experiments are extensive and verify the effectiveness of the proposed method. 
3. The design of the attribute strength and the corresponding datasets could be helpful to many relative future works.

### Weaknesses
Could the authors offer more clarifications and analysis to demonstrate the extent to which the proposed attribute strength can encompass a broad spectrum of human preferences and instructions? 
How accurate is the language model to find the correct attribute strength that match user's intent?

### Questions
Please refer to the weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
