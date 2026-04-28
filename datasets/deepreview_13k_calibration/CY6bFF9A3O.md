# RACCOON: Regret-based Adaptive Curricula for Cooperation

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 8, 6

## Abstract
Overfitting to training partners is a common problem in fully-cooperative multi-agent settings, leading to poor zero-shot transfer to novel partners. A popular solution is to train an agent with a diverse population of training partners. However, previous work lacks a principled approach for selecting partners from this population during training, usually sampling at random. We argue that partner sampling is an important and overlooked problem, and motivated by the success of regret-based Unsupervised Environment Design, we propose Regret-based Adaptive Curricula for Cooperation (RACCOON), a novel a method which prioritises high-regret partners and tasks. We test RACCOON in the Overcooked environment, and demonstrate that it leads to sample efficiency gains and increased robustness across diverse partners and tasks, compared with strong baselines. We further analyse the nature of the induced curricula, and conclude with discussions on the limitations of cooperative regret and directions for future work.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present RACCOON, a method for designing the curriculum for training generalist ad-hoc teamplay agents. The authors propose to sample training partners and tasks at each training iteration by ranking the partners based on relative regret. The authors apply RACCOON on a multi-layout Overcooked setting where a single student agent has to learn to generalize to new partners across multiple Overcooked layouts.

### Strengths
- The paper tackles a novel area in ZSC/Ad-hoc teamplay, autocurricula design.
- The proposed method is relatively straightforward and should be able to be easily plugged into most existing ZSC/Ad-hoc teamplay methods.
- The paper is generally well written and the authors present their motivation, methodology and results in a succinct manner.

### Weaknesses
 - I am not convinced by the multi-task experimental set up where a single student agent is evaluated on all 5 Overcooked layout simultaneously. The papers results show that all baselines includeing RACCOON can barely deliver more than more than 2 dishes on the 3 more challenging layouts, suggesting that the agents did not learn any meaningful cooperative policies. Perhaps a more more interesting multi-task setup would be to move the locations of counters/pots around similar to what was proposed in [1].
- The authors use a very simple method of generating training partners (random initialization + adding poast checkpoints) without any explicit methods to encourage partner diversity when many such methods exist (TrajeDi, LIPO, CoMeDi etc.)

### Questions
- I would like to know authors' rationale for proposing to sample the tasks  _after_ sampling the partner. The authors mention that all partners are "specialist agents" and sampled partner might be used to generate an episode that they are not trained on. Wouldn't it more effective to first sample the task and then sample the partners that are trained on said task?
- As the student's policies improve, wouldn't it result in a negative score based on the equation presented in Section 3.3?

### Soundness
4

### Presentation
4

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
This paper proposes a new method for configuring curriculum tasks in multi-agent reinforcement learning (MARL) based on regrets. The primary aim of this approach is to address overfitting issues in MARL algorithms, which typically lack zero-shot generalization. In scenarios where partner behaviors change even slightly, existing algorithms perform significantly worse. The regret-based curriculum learning framework dynamically selects agents, encouraging the MARL algorithm to avoid memorizing environment-specific information solely for performance gains. Instead, it promotes adaptive strategies that utilize cooperative partners more effectively.

To evaluate their method, the authors conducted experiments in a collaborative MARL environment called OverCooked, focusing on its generalization capabilities. The results demonstrate that this curriculum-based approach facilitates a more generalizable and efficient method for leveraging partner information across diverse environments, yielding strong performance on the Forced Coord and Counter Circ tasks. Analysis of the training dynamics reveals that the proposed method initially prioritizes high skilled partners early in training, gradually shifting to lower-level partners toward the end, optimizing the agents’ adaptability.

### Strengths
- This paper addresses the overfitting challenges inherent in existing MARL approaches. Typically, standard MARL environments guide algorithms to train agents to perform specific actions in particular scenarios, often tailored to the environment itself, rather than utilizing cooperative behavior among agents. In contrast, this study focuses on improving inter-agent cooperation, proposing a method that promotes zero-shot generalization in MARL. This contribution is especially significant as it introduces a pathway for MARL algorithms to achieve more adaptable and generalized learning that extends beyond environment-specific contexts.

### Weaknesses
 - The experimental design of this paper does not align well with the principles of MARL. Although the proposed method is at an early research stage, it is difficult to claim effectiveness in a multi-agent context based solely on a two-agent environment. To demonstrate robust, generalized performance, results should ideally involve three or more agents, which would provide a more comprehensive test of the method’s effectiveness. Limiting experiments on only two agents places significant constraints on the study’s findings.

- In a fully observable environment with two agents, the necessity of agent-based learning itself is questionable. In this setting, the benefits of using MARL over conventional reinforcement learning are unclear, as there is no substantial increase in state or observation complexity. This raises concerns about the rationale for applying an agent-based approach in these circumstances.

- The experimental explanation is also insufficient. While the OverCooked environment is used, the paper should clearly explain why this environment is particularly suitable for examining generalization, overfitting, and zero-shot evaluation. Providing this context would better support the experimental design and underscore its relevance to the paper.

### Questions
- The concept of calculating regret in RL raises questions about its alignment with the field’s core principles. RL traditionally focuses on learning directly from the environment via online learning techniques, so introducing a regret variable and selecting the best task based on this metric may diverge from standard RL practices. Although this paper addresses this issue by using pre-trained agent policies and concentrating solely on selecting effective tasks, this approach still appears somewhat misaligned with the philosophy of RL, which emphasizes learning through environmental interactions rather than pre-determined information.

- I would like to ask the proposed method could improve generalization performance if incorporating partially observable or noisy environments, rather than a fully observable setting. I believe that such stochasticity might actually help mitigate overfitting. Furthermore, insights into how performance might vary under these settings would add valuable perspective on the robustness and adaptability in diverse environments.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Prior work on UED has used the idea of "regret-minimization" as a promising way to generate a curriculum of tasks for agents to train on. For building agents capable of zero-shot coordination, there is a lot of MARL research on generating diverse partners to train with. However, there is not much work on which partners to train with. This paper introduces a regret-based curriculum for deciding which partners in a population are most useful for training with, and compares its approach to common objectives from the UED literature.

### Strengths
This is a pretty original idea which has promising applications. The idea to create a curriculum for training against population based agents is very interesting and the authors did a good job showing the sample efficiency and learning trends of agents using their RACCOON approach. I particularly thought the analysis of sample probability as a function of updates was compelling, both for partner skill level and problems sampled, was compelling and revealed some of the limitations of naively choosing which partner from a population to train with. Moreover, the algorithm was very cleanly written and easy to follow, and the tensions between relative vs absolute regret, and other methods for formalizing regret in the appendix, was well motivated and ablated well.

### Weaknesses
It was a little unclear at first that the evaluations for the main section of the paper in section 5 were done on a multi-task setting, particularly when prior overcooked work has looked at just single-task performance. While the single task problems were still introduced, to someone quickly looking at results like Figure 2, it may be confusing that traditional PBT methods (essentially Domain Randomization for just partners from my understanding) did not replicate in grids like Forced coordination. These methods do replicate in the results shown in the appendix, so maybe reference this earlier. I would emphasize in the "Tasks" section of Section 4 that you will primarily be addressing the multi-task setting, and for the caption of Figure 2 add a brief line saying that by "all tasks" agents are trained on you mean they could sample any of the 5 grids in addition to partners. If you have space, I would briefly describe how your method stacks up to DR and Minimax on the single task section right at the beginning of section 5 so that someone reading it quickly can understand how your approach can still replicate results from the canonical study of Overcooked.

Moreover, for analysis as to why the multi-task section is failing for harder grids, the plots of grids sampled is nice, but even more interesting would be a look at the state the agents are failing at. Is it just because agents trained with DR are learning a different set of norms compared to RACCOON that don't support generalization, or is it something much simpler like they just don't know how to pass an item at the top of a grid compared to the bottom? If it's the latter, an explanation as to how RACCOON helps address this issue would be nice. If you could include some examples of states or sequences of states to compare the different failure modes of RACCOON and DR on harder grids like Forced Coordination that would make for a really strong qualitative analysis.

### Questions
Why are agents struggling in the multi-task setting but doing well in the single-task setting on the same grids, especially since your results show the harder grids are being sampled more for RACCOON?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper argues that partner sampling is an important yet overlooked issue when training agents to cooperate with novel partners. To address this, the authors propose Regret-based Adaptive Curricula for Cooperation (RACCOON), which prioritizes high-regret partners and tasks. This approach allows adaptation to the student (the learning agent)'s changing abilities throughout training and reflects the relative learning potential of each (partner, task) pair for the student. RACCOON demonstrates improvements on challenging tasks within the Overcooked environment. The paper analyzes the method through experiments involving varying skill levels, task difficulties, and scalability.

### Strengths
1. The issue of partner sampling is crucial for the generalizability of MARL and broader multi-agent collaboration algorithms.
2. The paper compares the proposed method with other mainstream sampling approaches and extends the experiments with deeper analysis.
3. While the concept of regret is not novel in reinforcement learning, its application to partner sampling is a new contribution.

### Weaknesses
1. The paper adopts "the difference between the maximum return ever achieved with $\pi'$ (on that task) and the current return" as the regret estimation. I believe this approach is relatively simplistic, and the performance of this method may depend on an effective exploration strategy, which is not adequately addressed in the paper. The authors might consider exploring better estimation methods and comparing their effectiveness. Specifically, the current regret calculation does not account for the variance in returns, which could lead to unstable partner selection, especially early in training when returns are highly variable. Furthermore, the maximum return achieved so far might not be a good proxy for the true maximum achievable return, especially if the exploration strategy is not sufficiently diverse. A more robust regret estimation method, such as using a moving average of past returns or incorporating uncertainty estimates, could potentially improve the stability and effectiveness of the proposed approach.
2. The readability of the paper could be improved, as some figures are of low quality and the text is difficult to follow. The descriptions of the experimental setup and the results are not always clear, making it difficult to fully understand the contributions of the paper. For example, the specific details of the Overcooked environment configurations and how the different skill levels of partners are generated should be more clearly explained. Additionally, the paper could benefit from more detailed explanations of the different baseline methods and their specific implementations.
3. The experiments involve only two agents; cooperation with multiple novel partners would present greater challenges, and the proposed method may not be directly applicable in such scenarios. The paper does not seem to address this or discuss the limitation of this aspect. The current approach assumes that all partners are interchangeable, which may not be the case in more complex multi-agent systems. The paper should discuss the potential limitations of the proposed method when dealing with heterogeneous partners and how the method might be extended to handle such scenarios.

### Questions
1. Why does the return of Asymm Adv in Figure 3 suddenly increase?
2. Why are the returns for Forced Coordination and Counter Circuit in Figure 3 measured in different ways?
3. How are the skill levels defined?
4. Why choose the very challenging task Counter Circuit to conduct scalable sample efficiency experiments in Figure 6?
5. How can the proposed methods be scaled to tasks involving cooperation with two or more partners?

### Soundness
3

### Presentation
2

### Contribution
2
