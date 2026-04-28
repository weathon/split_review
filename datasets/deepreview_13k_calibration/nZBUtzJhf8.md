# Guiding Skill Discovery with Foundation Models

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
Learning diverse skills without hand-crafted reward functions could potentially accelerate reinforcement learning in downstream tasks. However, existing skill discovery methods focus solely on maximizing the diversity of skills without considering human preferences, which leads to undesirable behaviors and possibly dangerous skills. For instance, a cheetah robot trained using previous methods learns to roll in all directions to maximize skill diversity, whereas we would prefer it to run without flipping or entering hazardous areas. In this work, we propose a **Fo**undation model **G**uided (FoG) skill discovery method, which incorporates human intentions into skill discovery through foundation models. Specifically, FoG extracts a score function from foundation models to evaluate states based on human intentions, assigning higher values to desirable states and lower to undesirable ones. These scores are then used to re-weight the rewards of skill discovery algorithms. By optimizing the re-weighted skill discovery rewards, FoG successfully learns to eliminate undesirable behaviors, such as flipping or rolling, and to avoid hazardous areas in both state-based and pixel-based tasks. Interestingly, we show that FoG can discover skills involving behaviors that are difficult to define. Interactive visualisations are available from: https://sites.google.com/view/iclr-fog

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a foundation model-based approach for guiding unsupervised skill discovery to discover desirable skills and avoid undesirable skills. The key idea of the method is to encode human intentions into skill discovery using foundation models, by extracting a representative score function from them. By using these scores to re-weight the rewards of skill discovery methods, the approach achieves skills aligned with human intentions, while avoiding those that are misaligned.

### Strengths
Generally, the paper is well-written and the underlying idea is fairly straightforward. The authors have adopted the METRA framework, and can thus handle image inputs

### Weaknesses
In terms of the claimed novelties, one of them is that FoG can learn behaviors that are challenging to define. I do not believe this is a new phenomenon – it is fairly well documented in preference based RL works [1]. In the same light, I believe the work has overlooked some very relevant works [2,3] which I believe could be used as baselines or at least discussed in detail.

Generally, the paper is well-written and the underlying idea is fairly straightforward. In terms of the claimed novelties, one of them is that FoG can learn behaviors that are challenging to define. I do not believe this is a new phenomenon – it is fairly well documented in preference based RL works [1]. In the same light, I believe the work have overlooked some very relevant works [2,3] which I believe could be used as baselines or at least discussed in detail. My detailed comments are as follows:

1.	How does the method related to papers [2] and [3]? Does FoG provide any specific advantages over these methods? If so, would it be fair to consider these are relevant baselines for comparison?
2.	In lines 251-252, how did the foundation models develop this insight about the angle of the cheetah’s front tip? On a related note, can we guarantee the score functions are always appropriate?
3.	Is it assumed that the score can be captured purely by virtue of observing s’ (Eq 6)? Do these scores not consider the manner in which a task is achieved? For example, if the task is to cut a fruit, this could be done with a kitchen knife or a hacksaw. Although the final outcome (the fruit cut into pieces) may be identical, the way it is done also involves some alignment signals – does the proposed score function capture such process-based alignment (which would be based on state trajectories, and not just a single state) as opposed to state/outcome based alignment?
4.	Regarding lines 160-161, is the score function always binary in nature? If so, I wonder whether setting $\alpha>0$ even matters as long as $\alpha<1$.
5.	The experiments are run over just 3 seeds, which is quite low. Is there any specific reason for this?
6.	In the experiment relating to Fig 6, is the task to move while being stretched/twisted? If it is just to be in stretched/twisted positions, why do videos need to be shown?
7.	It is possible that in the video, the agent is initially stretched and then towards the end, gets twisted. How would this be handled?
8.	It would be better to include the full context/descriptions used to generate the score function.
9.	Typos- line 244, 257-258, 395

### Questions
Generally, the paper is well-written and the underlying idea is fairly straightforward. In terms of the claimed novelties, one of them is that FoG can learn behaviors that are challenging to define. I do not believe this is a new phenomenon – it is fairly well documented in preference based RL works [1]. In the same light, I believe the work have overlooked some very relevant works [2,3] which I believe could be used as baselines or at least discussed in detail. My detailed comments are as follows:

1.	How does the method related to papers [2] and [3]? Does FoG provide any specific advantages over these methods? If so, would it be fair to consider these are relevant baselines for comparison?
2.	In lines 251-252, how did the foundation models develop this insight about the angle of the cheetah’s front tip? On a related note, can we guarantee the score functions are always appropriate?
3.	Is it assumed that the score can be captured purely by virtue of observing s’ (Eq 6)? Do these scores not consider the manner in which a task is achieved? For example, if the task is to cut a fruit, this could be done with a kitchen knife or a hacksaw. Although the final outcome (the fruit cut into pieces) may be identical, the way it is done also involves some alignment signals – does the proposed score function capture such process-based alignment (which would be based on state trajectories, and not just a single state) as opposed to state/outcome based alignment?
4.	Regarding lines 160-161, is the score function always binary in nature? If so, I wonder whether setting $\alpha>0$ even matters as long as $\alpha<1$.
5.	The experiments are run over just 3 seeds, which is quite low. Is there any specific reason for this?
6.	In the experiment relating to Fig 6, is the task to move while being stretched/twisted? If it is just to be in stretched/twisted positions, why do videos need to be shown? 
7.	It is possible that in the video, the agent is initially stretched and then towards the end, gets twisted. How would this be handled?
8.	It would be better to include the full context/descriptions used to generate the score function.
9.	Typos- line 244, 257-258, 395



[1] Christiano, Paul F., et al. "Deep reinforcement learning from human preferences." Advances in neural information processing systems 30 (2017).

[2] Kim, Sunin, et al. "Safety-aware unsupervised skill discovery." 2023 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2023.

[3] Hussonnois, Maxence, , et al. "Controlled Diversity with Preference: Towards Learning a Diverse Set of Desired Skills." Proceedings of the 2023 International Conference on Autonomous Agents and Multiagent Systems. 2023.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Existing skill discovery methods typically focus on learning to reach diverse states. However, they may learn undesirable behaviors and possibly dangerous skills. To this end, the author proposes to use LLM and CLIP to generate a score function that judge whether the current state is undesirable (according to given text description of desirable and undesirable behaviors).

### Strengths
The paper is well written and easy to follow. The experiments show that the proposed method successfully achieve the proposed goal -- learning diverse skills while avoiding undesirable behavior, on both object state and image space.

### Weaknesses
Though learning diverse skills while avoiding undesirable behaviors is a valid motivation, using foundation models simply as an undesirable behavior recoginizer seems to be a weird use case. In the case that we already use foundation models, it seem to me a more natural way is to let foundation models propose some tasks and safety reward (if applicable), examples include but are not limited to [1] and [2]. This allows skill discovery to directly target at learning more semantically-meaningful skills, compared to target at visiting diverse states.

Could authors providing the reasoning for this design choice? (though a bit off-topic, though the authors mentions that Eureka requires multiple iterations of reward designs, I am not fully conviced. Learning a skill for each reward during the iterations could also lead to diverse skills).

### Questions
none

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a method called Foundation model Guided (FoG) skill discovery, which uses foundation models to incorporate human intentions into the process of skill discovery in reinforcement learning. FoG aims to align skills with specified human intentions, assigning higher rewards to desirable states and lower ones to undesirable states. It applies a score function generated by an LLM for state-based RL or implemented by CLIP for pixel-based RL to re-weight intrinsic rewards, guiding agents to avoid hazardous areas or eliminate undesirable behaviors. FoG is evaluated against baselines like METRA and DoDont, with experiments showing improved avoidance of undesirable behaviors and hazardous areas in specific environments.

### Strengths
The paper is generally well-organized, and the description of the FoG approach and its score function is detailed.

### Weaknesses
## Review

### summary:
 This paper presents a method called Foundation model Guided (FoG) skill discovery, which uses foundation models to incorporate human intentions into the process of skill discovery in reinforcement learning. FoG aims to align skills with specified human intentions, assigning higher rewards to desirable states and lower ones to undesirable states. It applies a score function generated by an LLM for state-based RL or implemented by CLIP for pixel-based RL to re-weight intrinsic rewards, guiding agents to avoid hazardous areas or eliminate undesirable behaviors. FoG is evaluated against baselines like METRA and DoDont, with experiments showing improved avoidance of undesirable behaviors and hazardous areas in specific environments.

### soundness:
 2

### presentation:
 3

### contribution:
 1

### strengths:
 The paper is generally well-organized, and the description of the FoG approach and its score function is detailed.

### weaknesses:
 **The methodology is the same as DoDont.**

The core methodology of FoG closely resembles the DoDont approach, as both employ a score function derived from human-provided preferences, especially the form $\max\sum p(s,s') \|\phi(s') - \phi(s)\| z, \quad\text{s.t.} \|\phi(s')-\phi(s)\|\le1 $. Although FoG uses $f(s')$ in its objective, i.e., $\sum f(s') \|\phi(s') - \phi(s)\| z, \quad\text{s.t.} \|\phi(s')-\phi(s)\|\le1$, $f(s')$ is just a special case of $p(s,s')$. The similarity to DoDont weakens FoG's novelty. The main contribution of the paper is thus this special implementation of the score function proposed by DoDont. However, as stated below, even this special implementation is trivial.

**The score function is trivial, and using the vision language model as the score function to capture the human intention for MuJoCo robots has been proposed.**

For state-based RL, FoG utilizes ChatGPT to "write" a function to indicate if a certain dimension of the state is larger than a threshold; for instance, 
```python
f(s) = lambda s: s[1] > threshold
```
This function is a trivial implementation of the score function, i.e., $p(s,s') = $ I(s'[1] > threshold), i.e., "s'[1] > threshold" is classified as "desired" and "s'[1] <= threshold" labeled as "undesired".

For pixel-based RL, FoG also utilizes the CLIP similarity score to implement a trivial score function $p(s,s') =$ CLIP(s', "desired") > CLIP(s', "undesired"). For instance, FoG utilizes CLIP(s', "ground is blue") > CLIP(s', "ground is orange") to encourage the halfcheetah to appear in the blue ground. However, one can easily obtain the visual state of the halfcheetah in the blue ground and the visual state of the halfcheetah in the orange ground and label the former as the "desired" state and the latter as the "undesired" state to train an image classifier for DoDont. The training process of the image classifier in DoDont can be regarded as a distillation from the pre-trained CLIP or human knowledge to a lightweight neural classifier. Similarly, the descriptions of "flip over" vs. "stand" and "twist" vs. "stretch" can easily be distilled from CLIP, other foundation models, or even human annotators. What's more, when there is no color in the ground or the color distribution in the left plane is the same as the right plane, the CLIP image encoder would fail since it does not capture any feature related to the motion.

Additionally, utilizing the vision language model to capture the human intention has been proposed by Juan et al.^1.

1. Juan Rocamonde, Victoriano Montesinos, Elvis Nava, Ethan Perez, David Lindner, Vision-Language Models are Zero-Shot Reward Models for Reinforcement Learning, ICLR 2024.


**Baseline comparison is unfair.**

The comparison to METRA is unconvincing because METRA does not incorporate any human intentions or extrinsic reward functions. For a fair evaluation, FoG should be compared with baselines that also incorporate human intentions, for instance, at least METRA+ implemented in DoDont, and might also consider other baselines utilized in DoDont, for instance,  DGPO and SMERL. 

**The experiments lack thoroughness, especially regarding visualizing score functions.**

For Section 4.2, the paper could benefit from visual comparisons between the score functions utilized by FoG and DoDont in pixel-based Cheetah and pixel-based Quadruped. As stated in Line 332, in Cheetah, FoG uses only simple descriptions like "ground is blue" and "ground is orange" to signal whether the agent is on the left or right part. This is actually as simple as "x<0" and "x>0" as long as the image encoder, such as the pre-trained CLIP image encoder, can differentiate between blue and orange. Thus, the explanation for the "failure" of the DoDont method in Cheetah should at least include the comparison between the performance of the score function of the DoDont, which is an image classifier similar to the CLIP image encoder. In the implementation details mentioned in Appendix A.9.2, the authors only mention that the image classifier utilized in DoDont is trained by themselves. No further details are provided. The implementation details of the score function are critical since both DoDont and FoG are based on METRA.

For Section 4.3, I'm afraid I have to disagree with the authors that  "twisted" or "stretched" samples are hard to obtain. Since both "twist" and "stretch" are relatively stable gestures, one can easily obtain such gestures via the MuJoCo UI provided by the Deepmind Control Suite and take a screenshot. Even without UI and without human resources to label, one can instruct a VLM  to score each or every N-th visual state with the same intention, i.e., either the agent is stretched or the agent is twisted, and then use the labeled batch as the demonstration to train the score function.

### questions:
 The description in Figure 5 is somewhat confusing. From the top subfigure, it is evident that MATRA, DoDont, and FoG all occupy both sides of the plane, with trajectories distributed on both the left and right. However, the authors assert that FoG avoids the right side, which is inconsistent with the experimental results. Please clarify this.

### flag_for_ethics_review:
 ['No ethics review needed.']

### rating:
 3

### confidence:
 5

### code_of_conduct:
 Yes

### Questions
The description in Figure 5 is somewhat confusing. From the top subfigure, it is evident that MATRA, DoDont, and FoG all occupy both sides of the plane, with trajectories distributed on both the left and right. However, the authors assert that FoG avoids the right side, which is inconsistent with the experimental results. Please clarify this.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes FoG (Foundation model Guided), a skill discovery method in reinforcement learning that incorporates human intentions by leveraging foundation models. FoG uses a score function extracted from foundation models to re-weight skill discovery rewards. This enables learning not only diverse skills but also desirable behaviors. The authors demonstrate FoG's performance compared to existing methods by evaluating it on both state-based and pixel-based tasks. Notably, FoG shows the ability to learn complex behaviors that are difficult to define, such as 'twisted' postures.

### Strengths
Unlike existing skill discovery methods, FoG can incorporate human intentions. It demonstrates flexibility by being applicable to both state-based and pixel-based tasks. Furthermore, FoG shows the ability to learn complex behaviors that are difficult to define, such as 'twisted' postures. Through experiments, FoG has been validated to learn intended behaviors, including eliminating dangerous actions and avoiding specific areas. The results demonstrate that FoG successfully guides agents to discover diverse and desirable skills while aligning with specified human intentions.

### Weaknesses
 * Studies such as [1] have already researched generating reward functions using foundation models. While there is some differentiation in applying a similar idea to skill discovery, the novelty appears limited compared to previous research that generated entire rewards through foundation models. The proposed idea only utilizes foundation models in the restricted aspect of 'applying weights to rewards proposed in other studies'.
* It seems that skills that cannot be generated by METRA also cannot be generated through FoG, raising concerns about whether the performance of the proposed framework is dependent on METRA.
* Although the paper explains why [2] was not used as a baseline, the lack of comparison with other studies that utilize foundation models appears to be a weakness of the paper.

### Questions
* A comparison with other studies that utilize foundation models appears to be necessary.
* The paper mentioned in the Weakness section, [2], claims to be able to discover useful skills in environments utilizing robotic arms. In contrast, FoG appears to have failed to discover useful skills in the Franka Kitchen environment. I'm curious what differences between the two methods led to these contrasting results.
  
[2] Rho, Seungeun, et al. "Language Guided Skill Discovery." arXiv preprint arXiv:2406.06615 (2024).

### Soundness
3

### Presentation
3

### Contribution
2
