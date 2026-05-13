# Navigation with QPHIL: Offline Goal-Conditioned RL in a Learned Discretized Space

- Decision: Reject
- Scores: 5, 5, 6, 3, 5

## Abstract
Offline Reinforcement Learning (RL) has emerged as a powerful alternative to imitation learning for behavior modeling in various domains, particularly in complex navigation tasks. An existing challenge with Offline RL is the signal-to-noise ratio, i.e. how to mitigate incorrect policy updates due to errors in value estimates. Towards this, multiple works have demonstrated the advantage of hierarchical offline RL methods, which decouples high-level path planning from low-level path following. In this work, we present a novel hierarchical transformer-based approach leveraging a learned quantizer of space. This quantization enables the training of a zone-conditioned low-level policy and simplifies planning, which is reduced to discrete autoregressive prediction. Among other benefits, zone-level reasoning in planning enables explicit trajectory stitching rather than implicit stitching based on noisy value function estimates. By combining this transformer-based planner with recent advancements in offline RL, our approach achieves state-of-the-art results in complex long-distance navigation environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on hierarchical methods in offline goal-conditioned reinforcement learning (GCRL) and proposes an optimized hierarchical framework specifically for this domain. The paper makes contributions by introducing some structures like VQ-VAE to enhance the existing hierarchical structures used in offline GCRL.

### Strengths
1. The focus on offline GCRL is valuable, and introducing a hierarchical framework with further in-depth exploration is interesting.
2. The writing is clear, and the paper is well-structured.
3. The paper introduces multiple interesting large-scale maze environments, which require high-quality GCRL policies to solve.

### Weaknesses
1. The proposed method is tested exclusively on the AntMaze benchmark, which raises concerns about the method's generalizability and robustness across different offline GCRL scenarios. The lack of evaluation on diverse environments, such as those found in the D4RL benchmark suite (e.g., Kitchen, Adroit), makes it difficult to assess the method's applicability beyond maze-like navigation tasks. This narrow focus limits the conclusions that can be drawn about the method's overall effectiveness in offline goal-conditioned RL.
2. In many AntMaze settings, the proposed approach does not consistently outperform existing state-of-the-art methods, such as HIQL, thus limiting the evidence for its effectiveness over current approaches. Specifically, the performance gains appear marginal in smaller or less complex AntMaze configurations, indicating that the method's advantages may only be realized in very specific, large-scale environments. This raises questions about the practical relevance of the method in more common or less challenging GCRL scenarios.

### Questions
The authors are encouraged to discuss the potential of applying the proposed approach to other offline GCRL environments to validate its broader applicability. Achieving successful results on varied benchmarks would strengthen the method's impact and demonstrate its generalizability.

### Soundness
2

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
The paper identifies a key challenge in offline RL: the signal-to-noise ratio, noting that prior work has shown the benefits of hierarchical offline RL methods in addressing this issue. In response, the authors introduce a hierarchical, transformer-based approach for goal-conditioned offline RL. Their method learns landmarks through a VQ-VAE model and plans a sequence of subgoals using a transformer-based planner, with subgoal policies trained via IQL. To encourage meaningful temporal structure, the authors implement a contrastive loss that assigns the same tokens to temporally close states while differentiating distant states. Additionally, they propose a subgoal-level stitching mechanism as a form of data augmentation. The method is evaluated on long-horizon tasks such as AntMaze, benchmarking against HIQL and other baselines. The experiments also include an ablation study to analyze the contributions of each component to performance improvements.

### Strengths
1. The proposed methods demonstrated significant improvement in the AntMaze environment, particularly on the Ultra maze, while achieving comparable results on smaller mazes.
2. The authors introduce a contrastive loss function that encourages temporally close states to share the same tokens, while assigning different tokens to temporally distant states. This contrastive loss yields substantial performance gains, particularly in the AntMaze-Extreme setting.
3. Leveraging the tokenization of trajectories, the authors propose a subgoal-level stitching mechanism as a form of data augmentation, which enhances performance in most cases.

### Weaknesses
1. A primary concern with the results is that they are limited to the navigation domain, specifically the AntMaze environment. This raises questions about the generalizability of the method to other settings, such as the Kitchen or Calvin environments evaluated in the HIQL paper. Expanding the evaluation to include diverse tasks, particularly those with different action spaces and reward structures, would provide a clearer understanding of the method's broader applicability. The current evaluation does not sufficiently demonstrate the robustness of the proposed approach beyond the specific characteristics of the AntMaze environment.
2. The concept of discrete planning over learned landmarks, subgoals, or skills has been well-explored in both online RL (e.g., Choreographer [1], Dr. Strategy [2], CQM [3]) and offline RL (e.g., PTGM [4], SAQ [5], SkillDiffuser [6], TAP [7]). While I acknowledge that none of these prior works directly address the goal-conditioned offline RL setting and that they are slightly methodologically different, the novelty here appears limited and incremental. The core idea of using a discrete latent space for planning is not entirely new, and the specific contributions of this work need to be more clearly delineated from existing approaches.
3. The authors state, “For long-distance tasks, the signal-to-noise ratio still degrades during subgoal generation, which can result in a noisy high-level policy and, consequently, reduced performance. In this paper, we propose to shift the learning paradigm of the high-policy towards discrete space planning” (lines 56-61). However, their analysis lacks a direct comparison between discrete and continuous space planning within the same framework to validate its impact on mitigating this issue. I would suggest modifying their approach by training a VAE instead of a VQ-VAE to enable such a comparison as part of an ablation study. Alternatively, they could compare their method to a variant using a larger number of landmarks to assess how this affects performance in handling the signal-to-noise problem. The current analysis does not provide sufficient evidence to support the claim that discrete planning inherently addresses the signal-to-noise issue better than continuous methods.

### Questions
1. Could you provide more details on how you selected the number of landmarks? Additionally, how does varying the number of landmarks impact performance? It would be helpful to understand how different quantities affect the system’s effectiveness.
2. In the experiments, could you clarify the terms “w/ repr.” and “w/o repr.”? I couldn’t find an explanation in the text.
3. From Figure 3, it appears that planning occurs only once. How does the system handle situations where the agent deviates from the plan? Is there any mechanism for re-planning if the agent is unable to follow the initial trajectory?

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
3

### Summary
The paper proposes a hierarchical policy architecture to address challenges in learning long-horizon goal conditioned policy with an offline RL setup where value function estimation can be particularly noisy. To decouple long-horizon planning and low-level control, the authors propose training a high-level agent that leverages a learned discretization of the state space (landmarks) to propose plans which are then achieved by low-level policies that transfer the agent between landmarks and also within a landmark (for precise goal alignment).

### Strengths
* The paper is well motivated and presents the approach clearly. The experiments also support the key claim of improvements in longer-horizon tasks.
* The proposed method’s discretization scheme and explicit trajectory stitching for learning high-level planning from offline data is an interesting approach and can be applied to more settings.

### Weaknesses
 - The paper is missing some details on the impacts of codebook size and tuning of the contrastive loss weights on the performance of the approach, these parameters seem integral to the contribution of the paper and also for broader applicability. As identified by the paper the subgoal step parameter of k is important in balancing the signal-to-noise ratio in low-level and high-level updates, as a consequence of replacing the training of high level policy with BC by a transformer it might have been beneficial to have very granular codebooks?
- While the proposed explicit trajectory stitching by augmenting high-level plans with different achievable subsequences works for the settings considered in the task it might not be broadly applicable as different paths have different difficulties (achievable success rates). So in general one might still have to learn a value function to perform implicit stitching – to isolate the benefits of proposed discretization at high-level, and also serve as a more direct comparison with HIQL, a version where a high-level value function is learned for planning can be beneficial to strengthen the claims.

### Questions
- Are all the results of QPHIL presented operating on open loop high level plans synthesized by the transformer policy on seeing just the first state?
- The hyperparameter for VQ-VAE suggests a very high coefficient for contrastive loss over reconstruction loss – what are suitable scales to balancing these different losses? Did they have to be tuned for different scales of the maze?
- With the stitched trajectory augmentation, I am wondering if the high-level BC policy has a tendency to generate longer paths if sampled multiple times. How many more trajectories are generated by such augmentation? Another assumption for stitching is that the low-level policy is capable of achieving any path – does the coverage of the dataset support even learning such policies?
- How does the coverage of the dataset (in the state space) broadly impact both the learning of the VQ-VAE and the policy?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposed a hierarchical offline RL framework, QPHIL, for navigation tasks. It relies on discretizing the state space into landmarks by learning a latent state representation and quantization. The proposed QPHIL algorithm then trains a high-level landmark planning policy via behavior cloning and a low-level goal-conditioned policy via IQL. QPHIL achieved good performance on the D4RL Antmaze benchmark and outperformed existing flat and hierarchical offline RL and BC baselines.

### Strengths
The idea of quantifying the states into coarse landmarks for high-level planning in hierarchical RL is interesting and intuitive. The proposed algorithm outperformed existing approaches by a large margin on the AntMaze benchmark.

### Weaknesses
1. Although multiple variants of the AntMaze environment were considered, the algorithm was only tested in the AntMaze environment. It should be tested for additional and possibly more complex navigation tasks (e.g., visual navigation, autonomous driving). One crucial factor is to show that the proposed tokenization method can scale to high-dimensional observation space (e.g., images). 
2. I also wonder if learning a latent space and quantizing it in the tested AntMaze environment is necessary. According to the visualized examples, the learned landmarks are mostly uniformly distributed across the maze and similar in size. Can one simply discrete the maze into lattices without learning the latent space? It also links back to the first point. The experiments would be more convincing if additional navigation tasks with high-dimensional visual observations could be included.


### Questions
1. In some of the tasks in Table 1, introducing data augmentation hindered QPHIL's performance by a large margin. Could the authors explain why data augmentation was not effective in these cases? It makes sense to me that data augmentation does not necessarily improve performance. Still, it is counterintuitive that the data augmentation step could cause a significant drop in performance in this context. 
2. Figure 3 is a bit confusing. How is $\omega$ defined, and why is the subgoal generation terminated once $\omega$ is reached? 
3. The signal-to-noise ratio arguments in Sec. 3 are hard to follow. In particular, I would appreciate the authors elaborating on the points: "A high k would improve the high policy’s signal-to-noise ratio by querying more diverse subgoals but at the cost of decreasing the signal-to-noise ratio of the low policy. Conversely, a low k would improve the low policy’s signal-to-noise ratio by querying values for nearby goals but at the cost of the diversity of the high subgoals."

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
A key challenge in Offline RL is the signal-to-noise ratio, which can lead to ineffective policy updates due to inaccurate value estimates. The authors propose a hierarchical transformer-based approach that utilizes a learned quantizer to simplify the navigation process and breaks the environment states into tokens. This method decouples high-level path planning from low-level path execution, allowing for a more straightforward training of low-level policies conditioned on discrete zones (tokens). This zone-level reasoning enhances planning by facilitating explicit trajectory stitching, reducing reliance on noisy value function estimates. The authors claim that this method achieves SOTA performance in complex long-horizon navigation tasks.

### Strengths
S1. Provided access to a larger antmaze dataset (Antmaze-extreme) with higher complexity.

S2. Develops on HIQL (Park et al, 2024) and adds a tokenization methods and a planner policy which breaks the problem into k distinct navigation problems.

S3. Outperforms all other benchmarks in larger datasets like antmaze-extreme depicting the strength of tokenization of the state space.

S4. The code provided has good documentation.

### Weaknesses
W1. The paper lacks a methodology diagram describing the entire training and inference procedure, which makes the paper difficult to follow.  

W2. The experiments lack other navigation environments and results are only shown on Antmaze.

W3. For the low level policy, $\pi_{\text{landmark}}$ and $\pi_{\text{goal}}$ are distinct policies which are both generating low level actions to reach to $\omega$ and $g$ respectively. The need for having two different policies is unclear and sparsely mentioned in the text.

W4. In the tokenizer, the contrastive loss penalizes temporal closeness of the states in the latent space.
W4.1. The tokenization example in Figure 4, has tokens broken into very non temporally close spaces as token 47 and 46 reach areas near token 43, and token 12 reaches near 16 and 17. 
W4.2. It’s also unclear how this loss “aligns with the walls thanks to the contrastive loss.” as mentioned in the caption of Figure 4. 

W5. The reason for using a transformer for sequence generation is unclear and thorough reasoning for using it would be appreciated as compared to HIQL.

W6. Does not perform well on smaller antmaze examples compared to other methods like HIQL.


Minor Nitpicks

N1. Spelling mistakes, line 444-445: “Exemple”

N2. Equations that are referred are not in the nearby pages of the reference, like line 347-348, referring to eq 7,

N3. $g$ is used both as a state encoder function, and the goal.

### Questions
Q1. In Figure 4, please explain the tokenization in more detail wrt. the W4. Also could you please elaborate on both the parts of W4.

Q2. Could you elaborate on W3 and explain the reason behind having two distinct low level policies. Could you show some ablations which provide empirical reasons for having $\pi_\text{goal}$.

Q3. Elaborate on the reasons for using a transformer architecture in $\pi_\text{plan}$ and ablations for the same would be helpful.

Q4. Why does QPHIL not perform above SOTA in smaller Antmaze datasets? Could changing the way of tokenization help with this?

Q5. Which is the proposed method in the paper, “QPHIL w/ aug.” or “QPHIL w/o aug.”? Having both where-in “w/ aug.” performs better in some scenarios and “w/o aug.” otherwise is confusing and elaborating on that would be helpful.

Q6. Can the prescribed method QPHIL work on other navigation tasks like Autonomous driving, and how would tokenization work for such a task?

### Soundness
3

### Presentation
2

### Contribution
2
