# Sketch-to-Skill: Bootstrapping Robot Learning with Human Drawn Trajectory Sketches

- Decision: Reject
- Scores: 5, 3, 8, 8, 5

## Abstract
Training robotic manipulation policies traditionally requires numerous demonstrations and/or environmental rollouts. While recent Imitation Learning (IL) and Reinforcement Learning (RL) methods have reduced the number of required demonstrations, they still rely on expert knowledge to collect high-quality data, limiting scalability and accessibility. We propose Sketch-to-Skill, a novel framework that leverages human-drawn 2D sketch trajectories to bootstrap and guide RL for robotic manipulation. Our approach extends beyond previous sketch-based methods, which were primarily focused on imitation learning or policy conditioning, limited to specific trained tasks. Sketch-to-Skill employs a Sketch-to-3D Trajectory Generator that translates 2D sketches into 3D trajectories, which are then used to autonomously collect initial demonstrations. We utilize these sketch-generated demonstrations in two ways: to pre-train an initial policy through behavior cloning and to refine this policy through RL with guided exploration. Experimental results demonstrate that Sketch-to-Skill achieves $\sim$96\% of the performance of the baseline model that leverages teleoperated demonstration data, while exceeding the performance of a pure reinforcement learning policy by $\sim$170\%, only from sketch inputs. This makes robotic manipulation learning more accessible and potentially broadens its applications across various domains.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
SKETCH-TO-SKILL leverages 2D human-drawn sketches to bootstrap and guide RL for robotic manipulation, making the approach accessible and potentially impactful. However, based on the presented experiments, the practical potential remains unclear. The real-world demonstrations focus on relatively simple tasks, making it challenging to fully gauge the framework's effectiveness or scalability in more complex, nuanced environments. More diverse and demanding experiments, along with detailed explanations, would help reveal whether this approach can truly generalize and perform under varied real-world conditions.

### Strengths
- The paper introduces an innovative approach by leveraging human-drawn 2D sketches to initialize and guide reinforcement learning in robotic manipulation.

- SKETCH-TO-SKILL provides an alternative in robot learning by enabling task training from simple sketches, which reduces the reliance on teleoperation data, specialized hardware, and advanced expertise. This approach potentially broadens access to robotic training methods.

### Weaknesses
1. The examples shown focus on short, simple trajectories, so it’s difficult to gauge how well the framework would handle longer, more complex paths. This leaves open the question of how trajectory complexity and length impact the learning cost.

2. For human users, sketching complex trajectories might require a lot more effort than the straightforward examples presented. 

3. There’s also limited information on how the framework would deal with cases where paths overlap or are partially obscured. This could present practical challenges, both in terms of creating the sketches and the model’s ability to interpret them accurately.

4. The paper doesn’t clarify if there are specific guidelines for choosing sketch perspectives. It seems each task might need its own camera setup, which could complicate consistency and generalization in real applications.

5. The discriminator doesn’t appear to contribute significantly to the results, which makes it unclear how essential it is or if it’s been optimized effectively for generalization.

6. The experiments are carried out in simplified environments without much complexity or occlusion, so it’s hard to assess how well the model would perform in more realistic, cluttered settings.

7. The real-world tasks demonstrated are quite basic, which doesn’t fully showcase the framework’s potential across a broader range of applications. More varied real-world tests could provide deeper insights into its versatility.

8. There’s little information on the types of sketches and common sketching errors anticipated. Understanding how the model handles imperfections and what types of errors might impact learning outcomes would add clarity.

### Questions
1. How does trajectory complexity affect the learning cost, both for the model and for users creating these sketches?

2. How feasible is it for users to sketch accurately for more complex, multi-step tasks, and is this approach realistic for those scenarios?

3. How does the model manage paths that overlap or are partially obscured? Are there any specific recommendations for users to handle these situations in sketches?

4. Are there guidelines for choosing the best perspective for sketching, and does each task require a different camera setup? If so, how might this impact the model’s ability to generalize?

5. Has the discriminator been optimized for generalization, and what tangible impact does it have on the model’s overall performance?

6. How sensitive is the model to changes in the scene, such as additional objects or occlusions?

7. Would testing on a wider variety of real-world tasks help to bring out a clearer picture of the model’s strengths and limitations?

8. What are the most common sketching errors expected in real-world use? How does the model handle these, and which types of errors are most likely to affect performance?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores the use of a sketch-based method as the means to provide robots with expert demonstrations that show how various manipulation tasks should be completed. These demonstrations can then be used to bootstrap the process of training control policies via behaviour cloning and reinforcement learning. The proposed system consequently consists of 1) a module that transforms a pair of 2d sketches (which correspond to two different viewpoints of a scene) into 3d trajectories, 2) a behaviour cloning step to generate an initial control policy, and 3) an RL module that refines this policy. Comparisons to teleoperation-based demonstrations and pure RL show how well this method works for six manipulation tasks that are relatively simple.

### Strengths
I like the way the paper is written, and the clear research questions that are articulated / studied in Chapter 4. Within the context of the relatively simple manipulation tasks which are chosen, I think the paper is very thorough with its analysis, and the evaluation does indeed shine a positive light on sketch-based methods as the means to provide expert demonstrations. Nevertheless, as I explain below, I am afraid that this approach will not scale to manipulation tasks which are more complex.

### Weaknesses
The methodology is overall sound, but nothing stands out as particularly novel. In addition, and more importantly, the manipulation tasks which are chosen for experiments are too basic. They do not showcase adaptive behaviours (e.g. what happens if an object that needs to be picked up is accidentally dropped, or if it otherwise does not behave/move as originally intended) or multi-stage, longer-horizon motions (e.g. opening a cardboard box before picking objects up from it, or folding a t-shirt). Teleoperation has been shown to be effective in such settings due to its real-time feedback and high-throughput high-DOF nature. I fear that the sketch-based approach presented here is simply too limited and will quickly become overly cumbersome as the task difficulty increases. For example, even providing a time-dependent orientation for the robot's end effector would likely be non-trivial through the pair of 2d sketches used as input for the system that is proposed in this paper. I would be happy to reconsider this standpoint if further experiments are presented for manipulation tasks that are considerably more complex.

### Questions
As mentioned above, I have significant concerns over the scalability of the proposed sketch-based method for complex, real-world manipulation tasks. As robotics manipulation problems go, the tasks which are chosen in this work fall well within the toy-model domain, and as such, the findings do not apply to the real-world problems which we expect robots to be able to learn how to undertake through expert demonstrations.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work aims to use human-drawn sketches to learn RL policies for robotic manipulation tasks. They use a trajectory generator to generate demonstrations from sketches, then use IBRL to train a policy from the generated demonstrations. The paper additionally tests whether there are benefits in (1) generating more demonstrations per sketch and (2) performs guided exploration using a discriminator.

### Strengths
Good results on a novel method, which is able to generally preserve performance while removing the need for high-quality teleoperated demonstration data. Each piece of the method is explained clearly, and the method is designed logically (e.g. exploit the demonstrated smoothness of the latent space to generate more demos per sketch with controlled noise). The results are presented clearly and effectively, and the Appendix provides useful information. Tests in the real-world show practical applicability of the method.

### Weaknesses
Firstly, some additions to improve performance seem to have ambiguous results:

(a) Discriminator to guide exploration: In Fig. 6, the performance with and without the discriminator seem fairly close. The policy trained with discriminator only seems to perform better in ButtonPressTopdownWall, while the policy without discriminator seems to perform the same if not marginally better in the rest of the tasks. It's unclear if the discriminator is consistently beneficial, especially given the added complexity and computational cost.

(b) Additional demos per sketch: In Fig. 8, 10 demos per sketch + discriminator has similar average performance in ButtonPress (though lower lows), similar performance to others in CoffeePush, and has better average but lower max performance in BoxClose. It is mentioned that there is diminishing performance with more demos, but it does not seem clear that more demos per sketch is necessarily better? In fact, in Fig. 14, 10 demos + discriminator seems worse than others. The inconsistency in performance gains with additional demonstrations raises questions about the robustness of this approach and whether the added complexity is justified.

Secondly, it seems one benefit of sketching vs teleoperating is that sketched demonstrations can be made much faster and without expensive hardware. So, the usage of only 3 demos, and the absence of demo ablations (specifically on the number of sketches/teleoperated demonstrations provided) is somewhat odd. Perhaps MetaWorld tasks are too easy when using more demonstrations, but there exist harder standard LfD benchmarks which the authors did not test on. The lack of exploration on the number of sketches is a significant oversight, given the potential for sketches to provide a large amount of data with minimal effort, and the absence of testing on more complex benchmarks limits the generalizability of the findings.

### Questions
Are there additional clarifications which would explain why the authors chose to keep the discriminator and 10 demos per sketch? Perhaps a different way to present the data (e.g. raw success rate on more eval episodes)?

Does the method scale to more sketches (and how does it compare to IBRL when providing more teleoperated data)?

Have you tried this method with other backbone RL algorithms (e.g. ensemble SAC, REDQ) to improve sample efficiency or final performance?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work presents an interesting approach to extending IBRL by incorporating a trajectory generation method reminiscent of RT-Sketch. The core idea of generating 3D trajectories from pairs of 2D sketches, augmented by noise injection for data diversity, is novel.  The addition of a discriminator to guide the IBRL policy towards these generated trajectories further strengthens the link between user-provided sketches and learned robot behavior. However, the paper leaves some questions unanswered.

Firstly, the authors show a pair of sketches in Fig. 2, but it's not quantitatively clear how robust the trajectory generator is to variations in the spatial correlation between these sketches. Some of the analysis is present in appendix B, but adding information like the benefits of each augmentation strategy, sample variations in sketches, etc. would be beneficial. For example, how much spatial variation do you add?

In line 369, how many hand-drawn sketches do you collect?. Is it also three (i.e. number of expert tele-operated policies used)? The ablation study on Discriminator reward weighting in Fig. 9 is good, but the choice of reward weights seems arbitrary. A more logical progression (e.g., 0.1, 0.01, 0.001) would make the analysis clearer, or explain your rationale for choosing the current set of weights. While the appendix includes a no-discriminator condition (Fig 14), this crucial ablation should be in the main paper.

Looking ahead, the authors briefly mention "time parameterization of the trajectory" in future work (line 529).  This raises the question of how they envision solving the increased difficulty in achieving correlation between two sketches when time is factored in.

Finally, the paper would benefit from a discussion situating this method within the broader context of recently popular Vision-Language Agents (VLAs) for robotic manipulation, such as OpenVLA. This is particularly relevant given the increasing use of real-world robot-collected data in VLAs, whereas Sketch-to-Skill is trying to reduce tele-operated data collection. How do the authors see sketches complementing this data? Moreover, given the prevalence of LFD and imitation learning in VLA pre-training and fine-tuning, how do the authors position the advantages of RL in this setting? Including this in a related work or discussion section would be helpful.

Some minor points:
*   There is a typo on line 071: "we present a more approach."
*   For improved accessibility, the figures could be made more color-blind friendly, potentially by incorporating textures. For example, add textures to the bar plots in Fig 7.
*   In Fig. 3, why is there an asterisk after "Replay Buffer"?

### Strengths
provided in summary

### Weaknesses
This work presents an interesting approach to extending IBRL by incorporating a trajectory generation method reminiscent of RT-Sketch. The core idea of generating 3D trajectories from pairs of 2D sketches, augmented by noise injection for data diversity, is novel.  The addition of a discriminator to guide the IBRL policy towards these generated trajectories further strengthens the link between user-provided sketches and learned robot behavior. However, the paper leaves some questions unanswered.

Firstly, the authors show a pair of sketches in Fig. 2, but it's not quantitatively clear how robust the trajectory generator is to variations in the spatial correlation between these sketches. Some of the analysis is present in appendix B, but adding information like the benefits of each augmentation strategy, sample variations in sketches, etc. would be beneficial. For example, how much spatial variation do you add? Specifically, what are the ranges of the random rotations, translations, and scaling variations applied to the sketches? Furthermore, what is the magnitude of the elastic deformations applied to the sketches and trajectories, and how were these parameters chosen? It's unclear if these augmentations are sufficient to cover the space of possible hand-drawn variations.

In line 369, how many hand-drawn sketches do you collect?. Is it also three (i.e. number of expert tele-operated policies used)? The ablation study on Discriminator reward weighting in Fig. 9 is good, but the choice of reward weights seems arbitrary. A more logical progression (e.g., 0.1, 0.01, 0.001) would make the analysis clearer, or explain your rationale for choosing the current set of weights. While the appendix includes a no-discriminator condition (Fig 14), this crucial ablation should be in the main paper.

Looking ahead, the authors briefly mention "time parameterization of the trajectory" in future work (line 529).  This raises the question of how they envision solving the increased difficulty in achieving correlation between two sketches when time is factored in. How will the temporal alignment of the two sketches be handled, and how will the model ensure that the generated trajectory respects the temporal constraints implied by the sketches?

Finally, the paper would benefit from a discussion situating this method within the broader context of recently popular Vision-Language Agents (VLAs) for robotic manipulation, such as OpenVLA. This is particularly relevant given the increasing use of real-world robot-collected data in VLAs, whereas Sketch-to-Skill is trying to reduce tele-operated data collection. How do the authors see sketches complementing this data? Moreover, given the prevalence of LFD and imitation learning in VLA pre-training and fine-tuning, how do the authors position the advantages of RL in this setting? Including this in a related work or discussion section would be helpful.

Some minor points:
*   There is a typo on line 071: "we present a more approach."
*   For improved accessibility, the figures could be made more color-blind friendly, potentially by incorporating textures. For example, add textures to the bar plots in Fig 7.
*   In Fig. 3, why is there an asterisk after "Replay Buffer"?

### Questions
provided in summary

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a method for training robotic manipulation policies through the use of 2D human trajectory sketches. The pipeline depends on a generator that takes a pair of 2D human trajectory sketches, drawn on the same scene captured from two different view points, and generates 3D trajectories (sequences of 3D points). This generator must be pre-trained using a dataset of sketches and corresponding 3D trajectories. Next, the 3D trajectories are used to train an agent with imitation learning, and then the agent is finetuned via reinforcement learning, using a discriminator-based reward to ensure consistency between the agent behavior and the 3D trajectories that came from the sketches. The method is shown to perform well on 6 tasks in MetaWorld and on a button pressing task in the real world.

### Strengths
The paper is well-written and easy to follow. The idea is interesting at a high-level and demonstrated on MetaWorld, a common benchmark, which could help others reproduce the work.

### Weaknesses
 **Practicality of Approach.** The approach depends on a trained sketch-to-3D trajectory generator, which itself must be trained on a sufficient set of data. It seems that the burden of collecting this dataset would outweigh the benefits of using this generator as an alternative to providing human demonstrations. Furthermore, teleoperating a handful of demonstrations seems like a more general approach. Demonstrations can be collected for any task that the human can demonstrate, while the performance of the proposed approach is constrained to the capabilities of the trained generator. For example, it seems that the current method can only be using for position-controlled tasks, and not tasks where the robot must control both position and orientation. Furthermore, the trained generator might not generalize well beyond the training data, which likely needs to be collected on the same set (or very similar set) of tasks, or at the very least in the same domain (e.g. same robot, same workspace). 

**Method Novelty.** The method itself seems limited in novelty -- the core component is the learned sketch-to-3D trajectory generator. Apart from that, it seems like an existing RL-finetuning algorithm is used (IBRL), with the only critical changes being (1) the choice of initial dataset and (2) the use of a discriminator. However, the discriminator itself seems to be unneeded, having little to no performance gain over not using it (Figure 8), while needed careful tuning for the discriminator reward weight (Figure 9). Even in the real robot experiments, it seems as though no discriminator is used.

**Experiment Issues.** The tasks presented in the paper appear to be limited in complexity. For example, the TD3 (RL baseline) can solve several of the tasks with just a sparse reward (Figure 5). I would suggest using some more challenging tasks for evaluation, perhaps from some other common benchmarks such as [robomimic](https://robomimic.github.io/), [RLBench](https://sites.google.com/view/rlbench), or [ManiSkill](https://www.maniskill.ai/home). There is also insufficient evaluation on some of the components of the method. In particular, how well does the sketch-to-3D generator generalize to new settings? Can it be applied to new tasks or new domains outside of the training data? How important is the architecture choice of the generator? Is the VAE crucial, or would other architectures work just as well? Is the choice of RL-finetuning method also critical, or would another method such as GAIL (as used in this work: https://arxiv.org/abs/1802.09564) work as well? Finally, in the real-world experiment, if BC already achieves 80%, what is the point of RL finetuning, if it achieves the same performance? Furthermore, training the sketch generator seemed to require 85 teleoperated trajectories itself (from Appendix). Training the 3D generator and then running RL seems much more painful than just training an agent directly on the teleoperated trajectories.

**Minor Issues.**

- line 71: "a more approach" - missing a word?

### Questions
- Sec 4.1 - is there any quantitative evaluation as well, or is it all qualitative?
- What if the two human sketches are inconsistent? It might be tricky to ensure that they are consistent.

### Soundness
1

### Presentation
3

### Contribution
1
