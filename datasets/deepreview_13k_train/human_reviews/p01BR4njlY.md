# Solving New Tasks by Adapting Internet Video Knowledge

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
Video generative models, beyond enabling the production of astounding visual creations, offer a promising pathway for unlocking novel, text-conditioned robotic behaviors, whether utilized as a video planner or as a policy supervisor.  When pretrained on internet-scale datasets, such video models intimately understand alignment with natural language, and can thus facilitate novel text-conditioned behavior generalization.  At the same time, however, they may not be sensitive to the specificities of the particular environment in which a policy of interest is to be learned.  On the other hand, video modeling over in-domain examples of robotic behavior naturally encodes environment-specific intricacies, but the scale of available demonstrations may not be sufficient to support generalization to unseen tasks via natural language specification.  In this work, we investigate different adaptation techniques that integrate in-domain information into large-scale pretrained video models, and explore the extent to which they enable novel text-conditioned generalization for robotic tasks.  Furthermore, we highlight the individual data and training requirements of each approach, which range from utilizing only a few still frames illustrating the subject of interest, to direct finetuning over videos labelled with text descriptions.  We successfully demonstrate across robotic environments that adapting powerful video models with small scales of example data can successfully facilitate generalization to novel behaviors, both when utilized as policy supervisors, and as visual planners.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work investigates how to adapt large-scale, pre-trained video models to solve novel, text-conditioned robotic tasks in specific environments. The authors explore three adaptation techniques: direct ft, subject customization, and probabilistic adaptation. It further introduces inverse probabilistic adaptation. The model is evaluated on metaworld and deepmind control suite.

### Strengths
1) The motivation is straightforward. 
2) The paper is well written, it does lots of controlled experiments to discuss which adaption techniques are better.

### Weaknesses
The scope of this paper is limited. While visual planning and goal-conditioned imitation/reinforcement learning (IL/RL) are indeed significant topics in robotics, the approach to generating visual targets appears straightforward. 

The experimental results lack novelty, as it is unsurprising that a web-scale, pre-trained text-to-image (T2I) or video generator would produce superior images or videos. Specifically, the paper does not sufficiently explore the nuances of how these models are adapted for robotic control. The adaptation techniques, while presented as distinct, do not delve into the underlying mechanisms that would make them suitable for the specific challenges of robotic manipulation and control. The paper does not provide a detailed analysis of how the pre-trained models' latent space is being manipulated and whether this manipulation is truly beneficial for the downstream tasks. 

Furthermore, this work does not directly address whether improvements in image quality contribute to enhanced performance or generalization in control tasks. For example, while Table 2 shows that inverse probability achieves the highest success rate, its FVD score in Table 3 is higher than others, raising questions about the relationship between quality and control success. Additionally, the study does not include generalization tests for control tasks. Although the paper aims to address new tasks, no genuinely novel tasks are explored. The evaluation on MetaWorld, while a standard benchmark, does not push the boundaries of what is considered challenging in robotic manipulation. The tasks are relatively simple and do not require complex reasoning or planning, which limits the impact of the proposed approach.

### Questions
My suggestion is to conduct more experiments, such as testing model generalization ability.

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
3

### Summary
The paper presents a study on how to incorporate pre-trained, language conditioned video generation models into robot learning. The paper considers three adaptation strategies for using video generation towards policy learning: finetuning the majority of the video generation model on expert demonstrations (most expensive for data and compute), subject customization using a few static images from the target domain, and probabilistic adaptation which trains a small in-domain model supervised by the large-scale video generation model. The paper further considers two options for downstream robotic task evaluation: video planning by predicted a plan to follow into the future and policy supervision by using the adapted video model to synthesize rewards for the policy. The different adaptation and evaluation techniques are benchmarked on the MetaWorld-v2 and DeepMind Control Suite simulations. Probabilistic adaptation and subject customization show promise in this domain when combined with the AnimatedDiff video generation model.

### Strengths
* The general problem of incorporating large-scale video generation into robot policy learning is of high interest to the robotics community. Particularly, with the rise in popularity of World Models in robotics, this paper's study is quite timely.
* The paper is well written and fairly easy to follow.
* I found the discussion of positives and negatives of the policy supervision evaluation approach to be insightful in Sec. 3.2.2.
* The experiments are fairly extensive in the simulated environments and transparent regarding underperformance in certain domains.
* The limitation section is thoughtfully constructed.

### Weaknesses
 * The majority of the assumption in the paper seems to be that video models provide strong motion priors and just require adaptation to the downstream domain visually (please correct me if I'm wrong) e.g., through static images in subject customization. However, from my experience large-scale video generation models still really struggle with the dynamics of the environment. This even seems to come across in the MetaWorld-v2 benchmark where a lot of the tasks achieve 0% or very low success rate. The paper does not adequately address the limitations of video generation models in capturing complex, physically plausible dynamics, particularly when extrapolating to novel scenarios.
* All the results are based on a single video generation model: AnimateDiff. It would have been more compelling to show results on a few models, in case the findings are particular to the specific chosen model. This raises concerns about the generalizability of the conclusions. The paper should explore models with different architectures and training procedures to ensure the findings are robust.
* Some of the language is quite repetitive throughout the paper (e.g., last sentence of 3.1.1 and first sentence of 3.1.2).
* I am not sure I entirely agree with the premise that it is impossible/highly challenging to obtain in-domain video demonstrations for a task. ~100 demonstrations are often assumed for imitation learning papers like Diffusion Policy [1], particularly if high success rates are desired on dexterous tasks. This relates to the low success numbers seen in the MetaWorld-v2 tables, particularly for tasks unseen during adaptation. Optimization compute cost seems like potentially a bigger concern. The paper should more clearly justify the low data regime and discuss the trade-offs with imitation learning approaches that use more data.
* Since a large focus of the paper is evaluating video generation adaptation in robotics tasks, it feels like real-world robot experiments should be included in the analysis. In simulation, adaptation may be more focused on the appearence of the simulated environment than the physics modeling of the language-specified task. In the real-world, modeling the physics of the interactions between the robot and the environment in real-time is the challenge. The lack of real-world validation limits the practical relevance of the findings.
* The data budgets for the expert demonstrations is quite low and appears rather arbitrary (25 for MetaWorld-v2 and 6 and 17 for the DeepMind Control Suite). It would be helpful to ground these design choices in recent literature. The paper should provide a more rigorous justification for the chosen number of demonstrations and discuss the impact of varying this parameter.
* Standard error is only present for the first column of Table 1. It should be included across the considered methods. The lack of standard error across all results makes it difficult to assess the statistical significance of the findings.
* The very poor performance of probabilistic adaptation in Table 1 is attributed to the small capacity of the in-domain model used. However, this should have been explored to understand the potential of this method in the DeepMind domain. The paper should provide a more thorough investigation of the limitations of probabilistic adaptation and explore potential solutions, such as increasing the capacity of the in-domain model or using different architectures.
* The results in Figure 3 were not particularly convincing to me for the dog jumping case. It seems the video generation model was able to generate a partially reasonable but not entirely accurate jumping dog sequence. The resulting simulated behavior appears to be a degenerated version of that suboptimal supervision. Although I do see that there is potential there for simulating unseen behaviors zero-shot. The paper should acknowledge the limitations of the video generation model and discuss how these limitations impact the downstream robotic task performance.
* Showcasing results where all methods get 0% (or close to 0^%) success rate for about half the tasks is not very meaningful as a takeaway. It seems like these experiments should have been iterated on futher. Likely including additional expert demonstrations would help the success rate. The paper should address the limitations of the proposed methods in these challenging tasks and discuss potential avenues for improvement.

Some typos and points of confusion are listed below:
1. Line 018 - video modeling ... [encodes].
2. The score in Sec. 3.1.3 should be formally defined.
3. The FVD acronym should be defined once in line 239.

### Questions
1. Is there a reason batch-balanced co-training was not studied as an alternative adaptation technique? Co-training has seen decent success in robot learning in recent years [2]? 
2. Why is inverse probabilistic adaptation good fro MetaWorld-v2 but so much worse for the DeepMind Control Suite?

[2] Khazatsky, Alexander, et al. "DROID: A large-scale in-the-wild robot manipulation dataset." RSS, 2024.

### Soundness
2

### Presentation
3

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
This paper investigates three adaptation techniques for generative video models, and proposes two evaluation metrics that go beyond traditional visual similarity scores in an attempt to more precisely test the effect of different adaptation techniques of video models on downstream performance for robotic tasks. The proposed adaptation techniques require small amounts of training data, and in some cases (subject customization) only static paired data. The proposed evaluation methods are by using the adapted video model as either a visual planner or policy supervisor, each with its own strengths as noted at the end of the methods section. Experiments are performed on a dog/humanoid and robot arm dataset 2 tasks and 16 tasks respectively. The authors finally observe that domain specific fine-tuning (for the dog/humanoid) and inverse probabilistic adaptation (for the robot arm) achieve the best performance. 

Overall this paper explores an important topic that will have many implications when using generative video models for robotic tasks.

### Strengths
1. Several robot arm tasks in MetaWorld environment and an additional environment are proposed as an evaluation scheme
2. The work is well motivated and tackles a nuanced but important question that is often glossed over in other policy-focused works.
3. Implementation details are very clearly stated and discussed so readers have a full picture
4. The subject customization technique is unique and novel, and I think the inverse probabilistic adaptation method is original (but please clarify this too (ask mentioned in Question #1 below) 
5. Very interesting observations regarding visual appearance vs task success rate are made, motivating the need to perform real world experiments such as those done in this paper to really understand what the right way to train/fine-tune/adapt video models for robotic tasks.

### Weaknesses
1. Quantitative results are not presented for the out-of-domain Humanoid and Dog environments. Table 1 seems to be for in-domain dataset, and Figure 3 shows qualitative results, but quantitative results for the jump task would be good to include in Table 1. Specifically, it's unclear how the success of the jump is measured, and what metric is used to evaluate the performance of the different adaptation techniques. Without these metrics, it's difficult to objectively assess the effectiveness of the proposed methods in these environments.

2. Two different adaptation techniques are concluded to work the best for the two different environments. (fine tuning for the dog/human environment, and inverse probabilistic adaptation for the robotic manipulation environment). This raises 2 questions: first, why do the ‘best methods’ differ in these two environments? And second, what are readers supposed to take away when working with a new different environment? A discussion, about knowing what technique to use based on the environment and why, would be good to include. The paper should delve deeper into the characteristics of each environment that make one adaptation technique more suitable than the other. For example, is it the complexity of the dynamics, the nature of the visual input, or some other factor?

3. Why do many adaptation methods completely fail for several tasks when using Video Planning (Table 4)? Especially the Soccer task? Is this due to poor inverse dynamics model or the inability to perform good video adaptation? There should be an explanation of why this is happening, otherwise it's hard to be convinced this is a valid experiment since the point of failure is unclear. It would be beneficial to analyze the failure cases and provide insights into the limitations of the video planning approach in these specific scenarios. For instance, are the generated plans simply not aligned with the task requirements, or is there a problem with the execution of these plans by the robot?

4. Subject customization is interesting, but it is unclear if motion dynamics in a new environment can be learned. The training data only includes static images paired with text, so when the dynamics vary greatly, will this method fail in comparison to direct fine-tuning/probabilistic adaptation? A good test of this would be to change the dynamics in an out-of-domain environment (something like the gravity constant if you can control that in the dog/humanoid world) and compare the 3 adaptation methods. I expect that static transfer cannot capture dynamics differences. If this is a tough experiment to run but there is a different way to prove the soundness of this adaptation method given different dynamics, please go ahead and present that, this was just one possible idea.

### Questions
Questions that should be addressed:
1. I am unsure if (inverse) probabilistic adaptation has been explored before at all in the robotics tasks context. Maybe make this more explicit in the ‘adaptation techniques for diffusion models’ related works section. 
2. Eq 1 & 2 introduces notation but many of the variables (theta, t, tao) are not defined. Please state what each variable means.
3. Also, please clarify what e_theta is in Eq 1&2. Is this indicating the denoising unet for the AnimatedDiff model?  
4. It would be good to clarify what ‘out of domain’ means in these adaptation experiments. It seems the robot arm and its dynamics must stay fixed for subject customization since the visual token is encoding this specific robot arm right? What about for (inverse) probabilistic adaptation, are there any such constraints on the domain you are adapting to? 
5. Sec 3.2 does not have details about how the reward is calculated using the adapted video model, all details are in Appendix B. Maybe it is because VideoTADPoLe is unknown to me, but I expect this to be the case for many readers. So please give atleast a brief description in the main paper and then you can point the readers to Appendix B.  
6. Please include the exact details of the ‘small dataset’ mentioned in line 312. I believe is important and should not just be kept in supplemental because the paper focuses on how to adapt with small # of examples. 
7. Please show a qualitative example from the Subject Customization for Figure 3 so that the readers  can see the qualitative comparisons as described in the paragraphs in Sec 4.2. 
8. What is ‘high variance’ referring to in L285? Variance in the output of a video model planner?
9. AnimateDiff produces very short horizon videos (in terms of time into the future). Therefore, completing a task seems to require lots of closed-loop rollouts. A mention of the number of steps to complete the task might be good to include in each type of experiment.

Minor Comments:
1. It is unclear whether AnimateDiff is the right model for this work. Why did the authors not choose to just use a video-model itself such as StableDiffusionVideo which has stronger priors about long-term motions? Some mention of this would be good to include.
2. The ‘Studying Data Quality’ section is interesting, but very few details are mentioned in the main paper, with most left to the supplementary section. If you would like to keep this section in the main paper, I would suggest at least including what a ‘suboptimal dataset’ means. Otherwise there is very little a reader can take away from this section.

### Soundness
3

### Presentation
4

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
This paper explores a range of domain adaptation techniques and incorporates them into large-scale, pre-trained video models for domain-specific robotic tasks. Notably, the authors extend the motion module, originally introduced in AnimateDiff, to enhance the animation capabilities of the video model for these specific tasks. Building on a vanilla video model, the authors examine various domain adaptation strategies, including direct fine-tuning, subject-specific customization, and probabilistic adaptation. A key innovation in this work is the redesign of the probabilistic adaptation approach to an inverse version, which demonstrates superior performance across both visual planning and policy learning tasks. The inverse approach yields significant improvements, achieving a success rate of 52.6% in policy learning and 28.4% in video planning, along with enhanced visual quality in the MetaWorld environment.

### Strengths
1. This work explores an efficient strategy for adapting internet video knowledge to in-domain simulation environments.
2. The experimental design is thorough, encompassing evaluations of policy learning and video planning across both seen and unseen tasks. 
3. Part of the experimental results look convincing, effectively demonstrating the performance of the proposed adaptation strategies.

### Weaknesses
1. The results in Table 1 show that subject customization achieves significant improvement over both the direct fine-tuning approach and vanilla AnimateDiff. However, probabilistic adaptation underperforms compared to the other three settings, exhibiting a notable discrepancy in return values. Although the authors assert that probabilistic adaptation focuses on in-domain estimation and struggles to learn effective policies in the Humanoid and Dog environments, I am concerned that the evaluation protocol may not be optimal when using policy discrimination for this setting. To my knowledge, probabilistic adaptation adopts score composition from both the pre-trained model and the domain-specific model, introducing a distribution shift during sampling. I recommend that the authors tune hyper-parameters for probabilistic adaptation methods by re-evaluating policy discrimination to minimize model prediction biases. Additionally, it would be helpful to see a case study that further examines the return values for probabilistic adaptation/inverse probabilistic adaptation, similar to the results presented in the Policy Discrimination section of the project website.


2. The results in Table 2 show that the inverse probabilistic adaptation model outperforms other adaptation methods in policy learning success rate on MetaWorld. Could the authors also provide the average returns for each baseline method?

3. Evaluation of Video Quality: The quantitative results in Table 3 are not entirely convincing, as only two evaluation tasks (coffee push and button press) are considered, which may lead to evaluation bias. Please provide additional video quality analysis across all tasks to present a more comprehensive assessment of the overall results.  

4. Based on the qualitative results from both the project website and the paper, it does not appear that the in-domain-only model performs worse than probabilistic adaptation or inverse probabilistic adaptation in task-level motion; the primary differences seem to be at the pixel-level generation. Another concern is that the reproduced results of the in-domain-only model exhibit lower video quality compared to the qualitative results presented in the AVDC paper (synthesized videos in MetaWorld). This discrepancy could lead to an unfair comparison. Could the authors explain their implementation process in detail, noting any deviations from the AVDC paper that might account for this discrepancy in video quality? A thorough review of the reproduction process would help ensure an accurate assessment of the model's performance.

### Questions
While the authors provide a comparative analysis with baseline methods, the paper still lacks some thorough examination of adaptation techniques to demonstrate the significant improvement of video adaption to in-domain video generation and robot manipulation tasks. Additionally, some baseline methods were not accurately reproduced during the evaluation, raising concerns about the validity of the results.

Given these issues, I am inclined to give the rating below the acceptance threshold. However, I will reassess my rating after reviewing feedback from other reviewers and the authors' responses. I am willing to raise my score if the authors address these concerns.

### Soundness
3

### Presentation
2

### Contribution
2
