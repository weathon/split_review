# On the Surprising Efficacy of Online Self-Improvement for Embodied Multimodal Foundation Models

- Decision: Reject
- Avg Score: 6.25
- Scores: 5, 10, 5, 5

## Abstract
Foundation models trained on web-scale data have revolutionized robotics, but their application to low-level control remains largely limited to behavioral cloning. Drawing inspiration from the sample efficiency and success of reinforcement learning (RL) fine-tuning in large language models (LLMs), we propose a two-stage approach suited to robotics. The first stage, Supervised Fine-Tuning (SFT), fine-tunes pre-trained foundation models using goal-conditioned behavioral cloning and “steps-to-go” prediction objectives. In the second stage, this foundation enables the extraction of a well-shaped reward function and a success detector, eliminating the need for manual reward engineering and real-world instrumentation, and allowing robots to practice autonomously with minimal human supervision. Our experiments on both real-world and simulated robots demonstrate that the combination of SFT and online Self-Improvement is significantly more sample-efficient than supervised learning alone. Furthermore, the combination of our proposed approach with web-scale pre-trained foundation models enables rapid acquisition of new skills, allowing robots to generalize far beyond the behaviors observed in the imitation learning datasets used during training. These findings highlight the transformative potential of combining pre-trained foundation models with online fine-tuning to unlock new levels of autonomy and skill acquisition in robotics.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The author's propose a novel pipeline to adapt foundation models to robotic low-level control tasks. Their pipeline is a two-stage process. The first is supervised fine-tuning which takes a previously trained foundation model and adapts it to robotic control. Their approach learns to predict the actions and steps to completion during training. Using this pretrained model, they define a reinforcement learning problem using the pre-trained models steps-to-go signal as reward. Including the steps-to-go signal enables their approach not to require a previously defined reward signal, and relies on this prediction as a reward signal. Experimentally,  the author demonstrated that combining a multi-modal pretrained model, their reward function and supervised learning step are necessary to maximize performance.

### Strengths
The author’s proposed system doesn’t require a hand-crafted reward signal to do the second fine-tuning stage. It is impressive to see how well this works in their experimental results. The pipeline also seems straightforward to deploy in practice with the understanding that it’s necessary to have large compute available for the foundation models. The authors also conduct several simulation experiments to validate their system and analyze different components in ablation.

### Weaknesses
Overall, the paper requires some further work to improve the quality of the manuscript. We leave several suggested edits below. If the authors can address these meaningfully, we believe the paper adequately addresses the target problem (adapting foundation models for low-level control).

Most of our worries with the system are otherwise on the practicality of the approach. The primary issue is that the system requires a second frozen foundation model in the second phase. Storing a second foundation model seems immensely expensive. Consider that some foundation models are at the scales of billions of parameter cases. Perhaps in the current version of the author's framework, this is not an issue. Still, if not in this work, we believe that future work should address compressing this second reward foundation model to make the approach more practical. Furthermore, real-world robotic experiments need more rigorous evaluation. In the appendix, the authors mention only using a single random seed. Granted, having a single person watch a robot for 20 hours for multiple runs is time-consuming, but this should not be an excuse to properly evaluate the framework's robustness. If this is not feasible, we encourage the authors to discuss this decision, or clearly state better it's a limitation of their evaluation process.

Writing comments: 
- Figure 5 is clearly ouside the margins. not adhering to proper margins can be sufficient justification for a desk rejection in some conferences, so please fix it. You can probably cut half the frames for this and keep the intent of the picture 
- Should probably use “et al.” in the references for Open X-embodiment [way too many authors] 
- Figure 9 in the Appendix is blurry. Either put in clearer pictures or remove them. 
- line 042: “Throughout this work…” - sentence feels clunky in the paragraph; rewrite to make a smoother introduction of the term. 
- line 087 “our results demonstrate that State 2…” hard to read sentence
- 2 Background -  The author's could move this to the appendix. A better use of background would be to explain the structure of the foundation control “framework” and note that these two models are used (or else push this discussion in methodology as these models are presumably part of the author’s method, whether or not it is unique to these specific models). For example, presumably, you’re using a transformer architecture, which is unclear here. Also, given that you are assuming access to text, formalizing mathematically the structure of your inputs would be more helpful to readers. 
- Your algorithm 1 should be referred to as “Algorithm 1” in the main paper (see “Algorithm Box” in line 213)
- Figure 2 - The figure is too big and goes outside the margins of the paper. Reduce the size and improve the quality of the second plot. It could be more vibrant and visually appealing (the y-axis label is too long, the ticks could be bigger, etc.) 
- line 249 Mathematical Intuition. Having skimmed Appendix E, it's short enough that you might as well just put it in the main paper or shorten the sentence to “See the appendix for more details”. The current sentence is too long as is. 
- Experiments section - I do not like the [Q1, Q2, …, QN] format in the subsections. You could have a preamble in the section saying this section investigates the following Questions instead. It does not look visually appealing as a reader. 
- Q1 - Q3, The author's could merge these three questions into a single question
- line 309 “Figure 8 left” the authors should refer to the fact this is in the appendix 
- Figure 3 “Values above are averaged across seeds.” How many seeds? 
- Figure 3: Author's should add a legend to clarify diagrams
- Figure 3 Why is there a floating orange block in the “Aloha Single-insertion” task? 
- Use a more informative name than “Frankenstein.” Some shorthand for what is not included would be more meaningful. 
- it would be interesting to see some more meaningful investigation of the claim in Appendix E as it would seemingly give more meaningful results for the second phase of the proposed system.

### Questions
- Given the benefits that online training has had in other fields (as discussed in the introduction), what makes the application to robotic control surprising exactly? 
- Do you even need these sentence goals in section 3.1? If the prefix is always the same, you could put arbitrary strings for both and achieve the same result, or otherwise not even bother with text. 
- line 180 - Why did the authors not add these auxiliary tasks? 
- In Equation  1: Is this the actual expectation or a direct prediction of the model? If it’s not clear: \sum p(steps_to_go_i) * steps_to_go_i [ where each option is predicted separately by the foundation model ] vs E(x) = f(o, question) so “expectation” is directly predicted 
- Line 214 / Algorithm 1 - Is the small positive constant less than 1? What makes this different from just simply reducing the learning rate? 
- Shouldn’t Frankenstein just be called “Pali-ViT without vision-language co-training?”
- What do the authors mean by their results when the Scratch & Frankenstein “underperform” relative to PaLI in Stage 1? Doesn’t including this result by itself support their claim in section 5.2?
-  Figure 7, why do the runs for e.g. 20% State 1, 3 robots end prematurely compared to the other runs?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
This paper employs a method proven effective in training language models to train embodied intelligence models, using reinforcement learning to further refine the model. Following Supervised Fine-Tuning (SFT), the model undergoes an online self-improvement process. In the first phase, the model is trained to clone actions and predict the remaining steps to action success. In the second phase, the predicted remaining steps to task completion serve as a reward for training, enabling reinforcement learning-based optimization. The step count to task completion is also predicted by the model, achieving self-improvement. Validation on the PaLI model showed that the self-improvement procedure increased action success rates by over 1.5 times.

### Strengths
This paper introduces reinforcement learning methods into the training of embodied intelligence models, offering a training approach that is more sample-efficient than supervised learning alone. The two-stage training method improves training efficiency, and the second phase enables the model to learn a broader range of actions, enhancing its generalizability. The reinforcement learning section provides detailed explanations of parameter settings. Experiments with the PaLI model validate the practical effectiveness of this training method, supported by real-world robot testing.

### Weaknesses
The paper lacks a concluding section, which might impact the overall readability and leave readers without a clear summary of the findings and contributions. Additionally, the arguments supporting the model's generalizability are somewhat limited. The reinforcement learning section would also be strengthened by including more theoretical derivations to better explain the underlying principles. Furthermore, the paper does not sufficiently address the potential limitations of the action discretization method, particularly how the granularity of discretization impacts the model's ability to perform complex or fine-grained manipulations. The discussion around the choice of the 3B parameter model is also weak, lacking a clear justification for why this specific size was chosen over other options, and how this choice might affect the scalability of the method.

### Questions
1) In the paper, which specific actions are included in the action steps mentioned? Is there a fixed set of actions? When training the model to perform new types of tasks, is it possible to add new actions, or is it limited to the predefined action range?
2) In the middle subfigure of Figure 3, it seems that these exists a more orange box.
3) The authors mentions that the main work is to design an effective and sample-efficient procedure for fine-tuning pretrained multimodal foundation models. Are there any requirements or limitations for multimodal foundation models？What is the impact of the parameter size of the multimodal foundation models on the results, and will the types of multimodal data involved affect the results？
4）In the stage 2, the authors use an online RL to train. Has the online training process considered the safety and coherence of the generated action set?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores a novel approach to enhance the performance of multimodal foundation models (MFAs) in robotics. The authors propose a two-stage fine-tuning framework:

Stage 1: Supervised Fine-Tuning (SFT), which uses goal-conditioned behavioral cloning and "steps-to-go" prediction objectives.

Stage 2: Online Self-Improvement, where robots practice autonomously using a data-driven reward function based on the "steps-to-go" prediction from the pre-trained model. This eliminates manual reward engineering and enables autonomous practice in simulated and real environments.

### Strengths
1. The combination of multimodal foundation agent, supervised fine-tuning, and online self-improvement is a powerful concept that enhances sample efficiency and policy generalization.

2. The method to generate reward functions using expected value of “steps to go” is novel and effective for RL finetuning.

3.  The proposed approach outperforms supervised learning alone and demonstrates generalization capability to new tasks beyond those observed during training.

### Weaknesses
1. The method which combines imitation learning with RL finetuning has been used in various areas of robot learning, such as efficient learning [1, 2], bridging human and robot embodiment gap [3], and bridging sim2real gap [4]. This paper just combines this method with Multimodal foundation model, which limits the novelty. Also, adding a paragraph to discuss those related work is helpful.

2. This paper demonstrates that using RL finetuning enhances sample efficiency and policy generalization compare with using only supervised fine-tuning. However, how about only uses pure RL finetuning without supervised fine-tuning? Include an ablation study comparing their two-stage approach to pure RL finetuning without the supervised stage should be helpful.

3. The idea to generate reward functions using expected value of “steps to go” is novel. However, what's the main difference between this idea and using reference trajectory from dataset/ offline policy [2]? The logic might be similar, and it also didn't require human-designed reward. Can you compare the performance of these two methods? Also, there are a lot of related work for generating rewards automatically, such as using human/LLM feedback [5, 6] and metrics functions library [7]. Adding a paragraph to discuss how this paper differs from or improves upon existing methods for automatic reward generation can highlight the contribution.

4. Out of sample efficiency, the another challenge for doing online RL in the real world is that those unreasonable behavior during the exploration process will lead to problems, especially for those  fine-grained tasks and contact-rich manipulation tasks (like the aloha task in this paper). How to avoid these problems? Discuss any safety measures or constraints in the online RL phase in the real world should be helpful.

5. I found the experiment section of this paper paper very difficult to read.

   i. Many of those paragraphs are too long, and a lot of content and images are in the appendix. It is difficult to understand what are the 
       tasks at once. 

   ii. All the data are placed in paragraphs. This makes the article difficult to read. Perhaps using a table would be a better choice.

### Questions
1. How to define the success indicator?

2. The aloha task seems that no semantic information is needed？Why MFA can be benefit?

3. The aloha task requires a large amount of data with additional RL finetuning, but diffusion policy only requires 800 demonstrations. What's the success rate of diffusion policy? Compare with diffusion policy, what are the benefits of using this method?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work explores the application of Large Language Model (LLM) training strategies to the web-scale training of a Multimodal Foundation Agent (MFA) for robotics. Specifically, the approach adapts the Supervised Fine-Tuning (SFT) process from LLMs into goal-conditioned behavioral cloning and "steps-to-go" prediction (The model predicts the remaining time steps needed to achieve a given goal) to fine-tune the foundation model. The second phase, analogous to the self-improvement process in LLMs, involves the creation of a reward function. Instead of relying on manual reward design, this method leverages data-driven reward function formation for improved generalization. The reward function is derived from the MFA’s own predictions of the remaining steps-to-go before achieving the goal.

The experiments examine various aspects of implementing the proposed training strategy, including the benefits of the pretraining phase and the improvements gained through the self-improvement stage. Key metrics such as generalization and robustness are analyzed to evaluate the method’s effectiveness.

### Strengths
This work focuses on a well-defined setting, utilizing a selected foundation model (PaLI-3B) and a policy architecture similar to RT-2.

The methodology is clearly formalized, with key implementation details explicitly provided. Theoretical insights are also included, offering valuable intuition to aid understanding. Additionally, the use of figures make an attempt to enhance interpretability.

The author conducts extensive experiments across diverse settings (e.g., LanguageTable, ALOHA, BananaTable) to evaluate the model's capabilities. Ablation studies on various components (such as the initialization of the foundation model) are performed to demonstrate the necessity and effectiveness of the design choices.

### Weaknesses
A key limitation lies in the use of the time-step variable for the step-to-goal loss, which is central to the pretraining process. However, the time-step is constrained to the range $[0,T]$, which, in my view, limits its generalizability to tasks with arbitrary or longer durations. That said, if the work provides experiments addressing this concern, I am willing to reconsider this point.

Another potential bottleneck arises from the reward function, which remains static due to reliance on frozen pretrained parameters, possibly hindering further performance improvement.

The experiment in Section 5.1 seems insufficient, as it only explores fine-tuning on a narrow subset of tasks. Expanding the study to a broader variety of tasks would enhance its persuasiveness.

Some figures are not clearly presented, particularly Figure 5. I’d appreciate further clarification on its meaning, as I understand it aims to demonstrate the superiority of the BananaTable task, but its message remains unclear.

Certain experiments modify numerous settings without adequately investigating the effect of these changes through ablation studies. For instance, in Section 5.1.3 (the ALOHA experiment), several settings—such as checkpoint selection—are altered, seemingly to push performance boundaries rather than to analyze the impact of individual components. While the system appears promising, a more structured investigation of the contributions of each component would strengthen its case.

The related work section could benefit from deeper analysis of how this work differs from prior studies, rather than merely listing them and leaving readers to infer the differences.

Finally, although this might be a challenging request, the study relies solely on the PaLI-3B model. Evaluating the method on additional Vision-Language Foundation Models would provide more comprehensive insights. Different models adopt varying strategies for input processing and output generation, and these subtle differences could significantly impact fine-tuning results.

### Questions
Is there stronger (non-empirical is better) evidence or insight to support why step-to-go prediction is a reasonable approach? My concern is that not all robotic datasets operate under the same speed settings. Even with the same robot, speed may vary across tasks, resulting in significantly different completion times for identical scenarios. This variability could make step-to-go predictions almost random. However, I would consider additional design or ablation studies to address this issue, showing that such speed variations do not have the negative impact I am assuming.

I am concerned that a large improvement in fine-tuning performance might indicate an undesirable outcome. Ideally, the pretrained model should already offer reasonably good performance, and substantial improvement might suggest that the pretraining phase was not as effective as intended. To address this, the reported improvements should be demonstrated through empirical experiments across various tasks, ensuring they reflect multitask generalization or efficient adaption rather than just performance gains on isolated downstream tasks. Could you provide further experiments and insights to validate the observed improvements and confirm that they result from efficient adaptation or general improvements?

### Soundness
3

### Presentation
2

### Contribution
2
