# Learning Diverse Bimanual Dexterous Manipulation Skills from Human Demonstrations

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Bimanual dexterous manipulation is a critical yet underexplored area in robotics. Its high-dimensional action space and inherent task complexity present significant challenges for policy learning, and the limited task diversity in existing benchmarks hinders general-purpose skill development. 
Existing approaches largely depend on reinforcement learning, often constrained by intricately designed reward functions tailored to a narrow set of tasks. In this work, we present a novel approach for efficiently learning diverse bimanual dexterous skills from abundant human demonstrations. Specifically, we introduce \textbf{BiDexHD}, a framework that unifies task construction from existing bimanual datasets and employs teacher-student policy learning to address all tasks. The teacher learns state-based policies using a general two-stage reward function across tasks with shared behaviors, while the student distills the learned multi-task policies into a vision-based policy. With BiDexHD, scalable learning of numerous bimanual dexterous skills from auto-constructed tasks becomes feasible, offering promising advances toward universal bimanual dexterous manipulation. Our empirical evaluation on the TACO dataset, spanning 141 tasks across six categories, demonstrates a task fulfillment rate of \textbf{74.59\%} on trained tasks and \textbf{51.07\%} on unseen tasks, showcasing the effectiveness and competitive zero-shot generalization capabilities of BiDexHD. For videos and more information, visit our \href{https://sites.google.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces **BiDexHD**, a framework designed to automatically turn a human bimanual manipulation dataset into simulation tasks and learn diverse bimanual dexterous manipulation skills with teacher-student method (RL in sim with state-based observations + distill into a policy with point cloud observation via Dagger). It aims to address the complexity and lack of task diversity in existing approaches. The authors propose a novel frame that:

1. instead of manually designed or predefined tasks, it creates feasible tasks from given bimanual trajectories;
2. using a teacher-student learning framework leveraging unified two-staged reward functions and vision-based policy distillation
3. evaluated on the TACO dataset across 141 tasks with strong performance on both seen and unseen tasks

The central claim of this paper is centered around the notion of "a preliminary attempt towards universal bimanual skills", and a framework that is "unified and scalable".

As in its current form, I cannot argue for its acceptance, due to the questions and weaknesses enumerated below. There is not enough evidence to support the strong claims of this work.

### Strengths
Originality:
- The framework described in the paper is novel in these perspectives:
1. While it is built on the widely used teacher-student framework, the authors designed two-staged reward functions that are universal to tool-use bimanual manipulation tasks constructed in simulation.
2. The idea of constructing many tasks from given bimanual trajectories is also a creative way of addressing the scalability challenge in simulation.

Quality:
- The authors performed several ablation experiments to demonstrate the effectiveness of each design choice, ranging from IPPO vs PPO, thresholds used in reward, each stage of the reward/training, functional grasping center, future conditioning steps, and baseline methods (BC). These efforts improved the technical soundness of the proposed method.

Clarity:
- I appreciate the clarity of the writing in terms of explaining the stages in this framework, the visual illustrations of each stage in figure 1 and figure 2, and the explanations for reward functions.

Significance:
- The problem of bimanual manipulation is becoming increasingly important for general-purpose robot intelligence. As the author pointed out, human-level performance on challenging bimanual dexterous manipulation skills is crucial for tasks involving coordination and tool usage. This work attempts to provide a unified and scalable framework that addresses several constraints in prior works.

### Weaknesses
1. This work limits the training and testing to one dataset and one simulator for a method that aims to be universal and scalable. If it is feasible, a demonstration of the proposed framework's effectiveness in other bimanual manipulation benchmarks and simulation environments would provide more convincing signals.

2. While there are 141 tasks from 6 categories, they are limited to tool-usage-oriented tasks, and the reward functions are tailored for solving this flavor of tasks. However, bimanual manipulation tasks that do not fall into this genre would likely require separate reward function designs. For example, cloth folding, packing & unpacking, or assembling & disassembling tasks are harder to simulate and have well-defined reward functions. As is commonly known, designing and tuning a good reward function for RL requires human effort and knowledge, which are both demanding and challenging. Thus, further experimental designs and evaluations are needed to strengthen the scalable and universal claim.

2. It is confusing that the BC baseline trained using teleoperated data achieves 0 success even on trained tasks. Could authors include more details on BC data's quality + quantity, training, and evaluation setting? To the best of my knowledge, other works have shown non-zero success for BC methods (even as baselines) on bimanual dexterous manipulation tasks.[1]

### Questions
1. The dataset used in this paper to generate tasks and provide trajectories is TACO: Benchmarking Generalizable Bimanual
Tool-ACtion-Object Understanding. In this dataset, there are 2.5k sequences of precise hand-object meshes and annotations. However, high-quality datasets such as TACO are costly to collect and difficult to scale as they require motion-tracking equipment and facilities. My questions are: how would reward engineering, depending on privileged state information in simulation tasks, that are constructed from motion-tracked trajectories, scale to infinitely diverse bimanual dexterous manipulation tasks? What are the limitations and bottlenecks?

2. Although I understand this work pertains to the study of bimanual dexterous manipulation framework in simulation, what would be some practical bottlenecks preventing this framework from being deployed onto a real bimanual dexterous robot?

3. For automatically constructed tasks in simulation, what are some limitations to the current framework preventing it from being "easily" scalable or applicable to other tasks? Or what quantifies as "easily"? (as the word "easily" is used in the paper)

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
4

### Summary
The authors propose BiDexHD for learning bimanual manipulation policies starting from human demonstrations. From human demonstrations, BiDexHD extracts human and object poses and defines the task based on them. During the policy training phase, BiDexHD first learns state-based policies that first aligns the hands and objects to the desired poses from human demos using RL and carefully designed reward functions, and then distills them into vision-based policies using DAgger. Experiments are based on the TACO dataset including six task categories. Ablation studies show the importance of aligning phase, and the main results show improvement over BC-only baseline.

### Strengths
I appreciate the authors carefully detailing the approach including the different tricks applied for setting up simulation environments based on human demos, and also the carefully designed reward functions. I don’t find major issues with the notations.

The overall approach is intuitive. It is clever to use human demos as an implicit representation of the task (despite not novel, see below), and then design RL training around it.

The experiment results are generally positive. The authors show the benefits of using IPPO instead of PPO in such a decentralized setup. The improvement over BC is also clear (despite the concern about the experiment setup).

### Weaknesses
My main concern of the paper is the lack of technical contribution over existing work. There is a similar work from Dasari et al., ICRA 2023 [1], which is not cited but proposes very similar ideas. In [1], the authors also use human demos and train RL policies to track the human trajectories. There is also an alignment phase by planning the hand to the object (not learned). Diverse tasks and objects are also considered. I think BiDexHD differs by (1) learning the alignment and (2) distilling into vision-based policies; (1) is new but (2) is well-studied in previous work as the authors also agree. I see the existing ideas from [1] also address the motivation of designing unified and scalable framework for learning bimanual dexterous tasks.

There are no details about how the BC baseline is designed and trained. I imagine with an expressive enough policy parameterization, e.g., diffusion, the BC baseline can achieve nonzero success rates. I urge the authors to carefully provide the details of the BC experiments.

I also find the writing of the introduction section can be improved. The current form reads rather vague —"unified and scalable” is emphasized multiple times, which I understand by reading the approach section, but the introduction does not explain at all why the approach is unified and scalable. I think the statement of contributions can be greatly improved to provide more details about the overall approach.

### Questions
Can you comment on how you think of sim-to-real transfer of the setup? From the videos it seems the motion is quite unstable and jittery at times, do you think some kind of regularization or reward shaping can fix it? Or do you envision some fundamental challenge in sim-to-real?

Can you comment on why BiDexHD-IPPO underperforms in Test New (Table 1) compared to BiDexHD-PPO?

What is the batch size used in IPPO/PPO? I don’t see it listed in the appendix. I am curious about the effect of batch size on training stability.

It would be good to discuss how the success rates vary among tasks (Appendix C) also in the main text.

I suggest using a different notation, e.g., M_1 and M_2, instead of r_1 and r_2, for the two metrics in the experiment section since readers might mistake them as rewards.

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
4

### Summary
This paper proposes an approach that learns bimanual dexterous manipulation from human demonstration dataset. The approach constructs corresponding tasks from existing bimanual dataset and applies teacher-student learning on the constructed tasks. The task construction part includes data preprocessing which converts human hand poses to LEAP hand pose and simulation initialization which initializes corresponding objects in the simulation environment according to the demonstration. Their approach also decomposes the teacher policy learning into two stages: 1) training the policy to matching the objects and hand poses with the first time step of the demonstration trajectory from initial pose and 2) tracking the reference object trajectory. The authors compare performance of different RL algorithms in teacher policy learning and different IL algorithms in vision-based policy distillation. They also ablate several design choices in teacher-student policy learning and demonstrate improved performance over other baselines.

### Strengths
By utilizing human demonstration dataset, BiDexHD learns bimanual dexterous policy in a scalable way. Unlike some prior works that is only limited to learning a specific task, BiDexHD is capable of learning many bimanual dexterous skills, meanwhile avoiding the effort of complex reward shaping for individual tasks. The author compares BiDexHD against ablated baselines and demonstrates its high performance over the baselines and competitive generalization capabilities.

### Weaknesses
1). Although BiDexHD is able to learn many bimanual tasks, it is tailored to learning one category of tasks: one hand holding the tool and another hand holding the object. It seems the framework is not able to deal with tasks that require in hand manipulation of either hand, or bimanual manipulation of a single object. For example, hand over and open bottle cap.

2). Description of Fig. 2 mentioned the tool and object are initialized at a fixed pose, but in real world application, the manipulated objects are seldom initialized at a fixed pose. The policy are not trained on a randomized initial pose.

3). Learning bimanual dexterous skills is extremely challenging, hence it is still unclear if the learned policies are able to be deployed on real-world hardwares.

4). In Sec. 5.2, the metric $r_2$ might not be a complete metric for task completion, because the task might still be completed while the hands fail to track the demonstration. For instance, when the tool and object both move up the same distance, while their relative pose keeps constant, the task is still completed.

5). The use of object trajectory tracking in reinforcement learning for dexterous manipulation is not particularly novel, as evidenced by prior works such as [1][2][3][4]. It would add depth to the discussion if the authors could address why existing trajectory-tracking methods cannot be directly adapted for bimanual dexterous tasks. While I understand that bimanual tasks indeed expand the observation and action spaces significantly, it would be helpful to know if there are additional, perhaps more nuanced, challenges that prevent a straightforward adaptation of these methods.

### Questions
1). The learned policy in the video includes a lot of jerking motion, is it possible to add some action penalty term in RL to smooth the motion?

2). Sec 4.2 mentioned identifying and removing invalid tasks to build up a complete task set. I am wondering how to identify invalid tasks after initialization.

3). Could you provide analysis on why BiDexHD-PPO outperforms BiDexHD-IPPO on teacher learning?

4). There has also been some work that learns bimanual dexterous policy from demonstration data. What is the difference between BiDexHD and other bimanual dexterous manipulation papers, for instance, DexCap?

5). Some discussion if the authors could address why existing trajectory-tracking methods ([1-4]) cannot be directly adapted for bimanual dexterous tasks.

### Soundness
3

### Presentation
4

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
This paper introduces an approach to learn multi-task bimanual manipulation policies through teacher-student training from human demonstrations. Before training, it uses existing bimanual dataset of human videos to extract human poses and other relevant information  for task construction. During training, It first trains a RL policy to grab the tool and object by two hands separately with multi-stage reward. Then it uses reward of tracking object poses to train a state-based RL teacher policy. After getting two-stage policies, it distills the policy to a point-cloud based policy with DAgger.

### Strengths
1. This paper proposes very detailed description of the pipeline and outlines each component and different stages
2. The learned multi-task policy can work on six categories of different bimanual tasks and outperforms the baselines. 
3. The paper also ablates the different components in the whole pipeline to highlight the importance of each component.

### Weaknesses
1. The paper uses the metrics of difference between object pose  and the reference object pose along the trajectory as the success criteria.  The proposed method has better performance in this metrics than the baselines. However, from the video shown on the website. The policy looks very jerky and sometimes the hand is in touch of the table. Therefore, this reduces the plausibility of this learned policy to transfer to the real robot.  It might be helpful to use other metrics to evaluate the policy such as number of collisions, the smoothness of the policy, etc. to have a comprehensive review of the paper.
2. The paper uses the teacher-student policy distillation to learn the bimanual policy which is commonly used for single dexterous hand manipulation. Extracting human poses from human videos are also common in prior work. Therefore, it is unclear to me what is the key innovation and contribution of this paper.
3. The paper introduces the behavior cloning (BC) baseline but doesn’t mention which algorithm they are using. Currently there are several popular BC methods including Diffusion Policy, BC Transformer, ACT, etc. The paper should include more details of the BC policy including the algorithm, the hyperparameters and the demonstration dataset size.

### Questions
1. There is one recent bimanual manipulation policies from point-cloud, DexCap[1] with imitation learning. That shows good results on learning tool use with bimanual manipulation. It would be interesting to see how their point-cloud based policy works in these tasks. 
2. It is a little surprising to see the IPPO has better results than PPO because some of bimanual manipulation tasks may need coordination. Could the authors provide more explanations about why IPPO behaves better than PPO.
3. The paper only compares PPO, IPPO and some ablation of different components of the IPPO. However, in the previous bimanual dexterous manipulation paper[2], they compare a variety of RL, MARL methods. It would make the paper stronger if the proposed method is also compared against MARL methods. 
4. What are the common failure modes of the baselines? It would be interesting to see the comparison between the videos of the  proposed methods and the baselines. Currently, the website only has videos of the proposed methods.
5. The paper already extracts the human poses from the bimanual demonstration dataset and can retarget from human poses to robot hand joint. Why not also use this data to add tracking reward not only to object pose but also to robot hand joint?
6. Adding the future object positions into the observations seems not very practical in real world. I am wondering if the authors have any insight about how to get future object positions to feed into the policy when deployed in the real world.

[1]Wang, Chen, et al. "Dexcap: Scalable and portable mocap data collection system for dexterous manipulation." In proceedings of Robotics: Science and System, 2024.

[2]Y. Chen et al., "Bi-DexHands: Towards Human-Level Bimanual Dexterous Manipulation," in IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 46, no. 5, pp. 2804-2818, May 2024,

### Soundness
3

### Presentation
3

### Contribution
2
