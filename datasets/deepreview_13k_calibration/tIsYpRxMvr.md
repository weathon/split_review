# Good Better Best: Self-Motivated Imitation Learning For Noisy Demonstrations

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 6, 5

## Abstract
Imitation Learning (IL) aims to discover a policy by minimizing the discrepancy between the agent's behavior and expert demonstrations. However, IL is susceptible to limitations imposed by noisy demonstrations from non-expert behaviors, presenting a significant challenge due to the lack of supplementary information to assess their expertise. In this paper, we introduce Self-Motivated Imitation LEarning (SMILE), a method capable of progressively filtering out demonstrations collected by policies deemed inferior to the current policy, eliminating the need for additional information. We utilize the forward and reverse processes of Diffusion Models to emulate the shift in demonstration expertise from low to high and vice versa, thereby extracting the noise information that diffuses expertise. Then, the noise information is leveraged to predict the diffusion steps between the current policy and demonstrators, which we theoretically demonstrate its equivalence to their expertise gap. We further explain in detail how the predicted diffusion steps are applied to filter out noisy demonstrations in a self-motivated manner and provide its theoretical grounds. Through empirical evaluations on MuJoCo tasks, we demonstrate that our method is proficient in learning the expert policy amidst noisy demonstrations, and effectively filters out demonstrations with expertise inferior to the current policy.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors address the challenge of noisy demonstrations in Imitation Learning (IL), which hinders the discovery of effective policies. They propose Self-Motivated Imitation Learning (SMILE), a method that progressively filters out demonstrations from policies considered inferior to the current policy, eliminating the need for additional information about the demonstrators' expertise. SMILE leverages Diffusion Models to simulate the shift in demonstration expertise, extracting noise information that diffuses expertise from low to high and vice versa. The predicted diffusion steps are used to filter out noisy demonstrations in a self-motivated manner, as empirically demonstrated on MuJoCo tasks, showing proficiency in learning expert policies amidst noisy demonstrations.

### Strengths
* This paper employs a diffusion model, which has shown promising performance in generative model training. The idea of this paper seems to be novel. 

* The authors provide theoretical derivations and empirical results demonstrate good results.

### Weaknesses
1. The paper's clarity can be significantly enhanced. For instance, the caption of Figure 1 lacks sufficient information for readers to fully comprehend its content. Furthermore, there is a need for a detailed explanation how does SMILE algorithm actually perform and how the noisy demonstrations filter is incorporated into existing IL methods. The methodology section lacks an overall algorithmic explanation, causing confusion. While the appendix provides pseudocode to elucidate the algorithm, the authors should emphasize these details in the main methodology section. Additionally, the authors introduce Definition 2.1 in the preliminary part, but its application in the subsequent content remains unclear.

2. The authors should provide more details about the dataset used for training since they collect the dataset themselves. For example, the quality of each inferior demonstrator related to varying levels, the number of demonstrations used for training should be provided. Moreover, does the corrupted action being used to transit to the new state when collection demonstration?

3. My critical concern is about the way the suboptimal data is generated. The method is to add Gaussian noise to the actions of an optimal policy. This noise maps exactly the one used in the diffusion process. Is this a relevant factor to explain the performance of the method? It would be great to investigate other forms of noise.

4. The evaluations are only conducted on MuJoCo tasks. Is it able to evaluate the proposed method using one of the many existing datasets of human demos, such as RoboMimic? RoboMimic includes a classification of the level of dexterity of human demonstrations in multiple robotic tasks (in simulation), akin to the levels of noise used in the paper's experiments. Are there additional issues or limitations when applying this method to human-generated data?

### Questions
1. From the pseudecode provided in the appendix, it seems that SMILE can be incorporated with both GAIL and BC. However, it's unclear which IL method is used to incorporate with SMILE in Figure 2. If BC is employed, it might introduce a potential fairness issue when comparing it with GAIL. Additionally, is it possible to integrate the SMILE method with online methods, and if so, what could be the expected performance?

2. I believe VILD [1] in online setting or modified VILD in offline setting (using pre-collected demonstrations and using IQL or CQL instead of SAC or TRPO) can serve as a powerful baseline, both theoretically and experimentally.

3. I am wondering if it is suitable to connect the proposed method to the idea of self-paced learning. Self-paced learning starts from easier sample (which is judged by the sample loss) and gradually include more samples into training to ensure the generalization. In SMILE, the authors seem to start from the whole dataset and gradually filter out noisy demonstrations.

4. According to Algorithm 2, while both diffusion model and policy network are initialised, how could the algorithm achieve good performance at filtering out noisy demonstrations? Additionally, is there any theoretical guarantee for the convergence of the diffused policy and the agent policy?

[1] Variational Imitation Learning with Diverse-quality Demonstrations, ICML 2020.

[2] DemoDICE: Offline Imitation Learning with Supplementary Imperfect Demonstrations, ICLR 2022.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a novel method called Self-Motivated Imitation Learning (SMILE) for imitation learning in situations where there are varying levels of expertise in the demonstrations provided. The main contribution is the ability of SMILE to predict the number of diffusion steps (akin to the level of noise) between the current policy and the demonstrations, which correlates to the expertise gap. The authors theoretically justify their approach and provide a detailed explanation of how this prediction mechanism works for filtering purposes. They then validate their method through experiments on MuJoCo tasks. The results show that SMILE can effectively learn from the best available demonstrations and ignore those that are less skilled, leading to more efficient learning of expert policies.

### Strengths
- provide the proof of predicting how many steps to denoise
- the results is better when the non-expert is just expert plus noise generated by Gaussian distribution

### Weaknesses
 - The paper claims that they want to handle non-expert demonstrations. However, the non-expert demonstrations they handle are only demonstrations generated by the same expert but some gaussian noise. There are many other ways to generate non-expert trajectories.For example, one can perturb the input observation and get a perturbed action. In addition, dataset D4RL provides non-expert demonstrations directly.  Many other methods have shown the ability to handle those non-expert demonstrations.
- There can be multiple kinds of experts in Mujoco. The proposed method might learn only one of them and be unable to handle the states of other experts.
- Since the method filters out many demonstrations, it might lose the chance to learn the dynamic of the environment and ends up being bad at OOD states.
- The many parts of the design are different from DDPM. The author needs to provide explanations. For example, in eq.6, q(a_t|a_{t-1}, s) is different from ddpm (eq.3). Another example is that it uses a one-step generator. I wonder about the performance of it compared to multisteps. Especially if it uses DDIM.

### Questions
- It is hard to understand the one-step generator. What is \mu_t in equation 10? Why not just train an additional policy with algorithms like BC and the data that have been filtered.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper uses diffusion model in place of GAN in generative adversarial imitation learning problem. At the first stage, this paper uses diffusion model to learn the noise information for forward and reverse process on the expert demo. Then, the noise information is leveraged to predict the diffusion steps between the current policy and demonstrators. Experiments show that this work have some performance gain s upon noisy expert demonstrations.

### Strengths
This work is novel and easy to follow. I think diffusion model is applied here do have some advantages. For example, imitation learning could be more robust to the noisy expert demos.

### Weaknesses
1. The performance gains reported in the paper appear to be marginal. While the authors demonstrate some improvement when handling noisy expert demonstrations, the quantitative results do not suggest a substantial advantage over existing methods across all tested scenarios. A more detailed analysis of the specific conditions under which the proposed method outperforms others would be beneficial.

2. The paper lacks a comprehensive comparison with other methods specifically designed for handling noisy expert demonstrations in imitation learning. A thorough survey and experimental evaluation against these specialized techniques would strengthen the paper's claims and provide a clearer understanding of the proposed method's relative performance in this niche.

3. The absence of experimental results based on clean expert data limits the understanding of the diffusion model's general advantages in imitation learning. Including such results would help determine whether the proposed approach offers benefits beyond the specific case of noisy demonstrations and provide a more complete picture of its capabilities compared to other generative models like GAIL.

### Questions
Could the authors report the training time of this newly proposed method. I think diffusion model is too slow for training in imitation learning setting. I am concerned about this. However, I would like to see more results with clean and noisy expert demos in experiments. I am wondering why diffusion model could be better than generative model such as GAIL, except for noisy expert setting. Could the author illustrate this?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considers the problem of imitation learning from noisy demonstrations. To address the problem, the paper introduces Self-Motivated Imitation Learning (SMILE), which filters out noisy demonstrations using a diffusion model. Theoretical results are introduced to show the efficacy of the proposed algorithm, and experiments are done to show that SMILE researches higher rewards compared with other baselines.

### Strengths
The paper considers an important problem. The proposed algorithm that uses diffusion model to judge the optimality of the demonstrations is novel and interesting. The experimental results show that the algorithm is promising.

### Weaknesses
1. The technical writing of the paper can be improved. There are several places that are not fully clear to me:

- Definition 2.1, I think comparing the expertise of two demonstrations by only comparing their rewards are not sufficient. What if the two demonstrations start from different initial conditions? Also, the environment considered is a stochastic environment, where the reward of two trajectories can be different even if we use the same policy. How does the definition deal with this problem? It seems more appropriate to define expertise based on the expected return of a policy rather than a single trajectory's reward, as the latter is highly dependent on initial states and stochastic transitions. A policy could be considered more expert if its expected return is higher, which is a more robust comparison.

- Proposition 3.1, in what sense does the author mean by "non-expert"? Can the authors define "non-expert" mathematically first? In addition, in the proof of Proposition 3.1, only action-wise proof is provided. However, is "non-expert" a property that might be defined over trajectories? The term "non-expert" lacks a precise definition. It would be beneficial to define it mathematically, perhaps in relation to the optimal policy or a threshold of performance. Furthermore, the proof should consider whether "non-expert" is a property of individual actions or entire trajectories, as this distinction is crucial for the validity of the proof.

- The notation $t$ is a bit confusing. Sometimes the subscript $t$ represents for simulation time step, while sometimes it represents for the diffusion step. The inconsistent use of the notation $t$ makes the paper difficult to follow. It is important to clearly distinguish between simulation time steps and diffusion steps using different notations to avoid confusion.

- I encourage the authors to add more explanations to Figure 1, which currently is confusing to me. The current explanation of Figure 1 is insufficient. A more detailed description of each step in the process, including the inputs, outputs, and the purpose of each module, would greatly enhance the reader's understanding.

2. There are some places for improvement in the experiments:

- It is claimed in the paragraph before "Contributions" that "SMILE achieves results comparable to method that rely on human annotations for several tasks". Which baseline does the authors mean here? The claim about comparable performance to methods using human annotations is vague. The authors should specify which baseline they are referring to, and provide a more detailed comparison.

- As introduced in paragraph "Dataset", the experts' original actions are corrupted by adding Gaussian noise, which is consistent to the diffusion model. I wonder what if we corrupt the dataset using other methods? For example, with probability $p$, the agent choose random action. The use of Gaussian noise for corrupting demonstrations is a specific choice. It would be interesting to see how the method performs with other types of noise, such as random actions with a certain probability, which might better simulate real-world imperfect demonstrations.

3. There is some incorrectness and insufficiency of the related work. For example, in the last paragraph of page 1, [1] is introduced as "introduced human annotations to indicate the expertise of the demonstrations" However, I think there is no human annotation in this work, but the algorithm automatically generates labels by injecting noise in the demonstrations itself. Similar works including [2-4] are not included in the related work.

### Questions
Please refer to each point raised in "Weaknesses".

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
