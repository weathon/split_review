# Small features matter: Robust representation for world models

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
In Model-Based Reinforcement Learning (MBRL), an agent learns to make decisions by building a world model that predicts the environment's dynamics. The accuracy of this world model is crucial for generalizability and sample efficiency. Many works rely on pixel-level reconstruction, which may focus on irrelevant, exogenous features over minor, but key information. In this work, to encourage the world model to focus on important task related information, we propose an augmentation to the world model training using a temporal prediction loss in the embedding space as an auxiliary loss. Building our method on the DreamerV3 architecture, we improve sample efficiency and stability by learning better representation for world model and policy training. We evaluate our method on the Atari100k and Distracting Control Suite benchmarks, demonstrating significant improvements in world model quality and overall MBRL performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a model-based reinforcement learning method designed to guide the world model towards crucial task-related information. It extends the DreamerV3 framework and integrates an augmented temporal contrast (ATC) loss as an auxiliary loss. The effectiveness of this approach is evaluated on the Atari and DeepMind Control Suite with distractions, demonstrating comparable performance to baseline methods.

### Strengths
1. This paper is relatively straightforward and easy to comprehend.
2. It learns a robust world model to focus on the task-relevant information.

### Weaknesses
1. This paper primarily focuses on endogenous information that directly influences the success of the agent's strategy. However, when using reconstruction losses, the model will inevitably consider exogenous information, and it may be better to replace the reconstruction loss with other loss functions, such as DreamerPro [1]. Additionally, the process by which the augmented temporal contrast loss guides the model to focus on relevant information remains unclear. Specifically, it is not clear how the contrastive loss inherently filters out irrelevant information, as the loss itself only encourages similar representations for temporally close states, regardless of their relevance to the task.
2. In Lines 205-206, the predictor model is employed to forecast the positive embeddings $(x_{t+K}, x_{t+1+K}, \ldots, x_{t+T+K})$ based on the anchor embeddings $(x_t, x_{t+1}, \ldots, x_{t+T})$. Does this suggest that $x_t$ is leveraged to predict $x_{t+K}$, and what actions can be taken to implement the transition from the time step $t$ to time step $t+K$? The paper does not explicitly address how the model handles the stochasticity of the environment when predicting K steps into the future, especially when the action space is discrete. The lack of clarity on how the model accounts for the multiple possible trajectories given a sequence of actions is a significant concern.
3. Several previous works have tackled visual distractions to enhance robustness in representation learning, including DreamerPro [1], Iso-Dream [2], DBC [3], and Denoised-MDP [4]. It is better to compare these method with the proposed method. The absence of a comparative analysis with these existing methods makes it difficult to assess the novelty and effectiveness of the proposed approach in the context of the current state-of-the-art.
4. The current experimental environment may be somewhat limited and simplistic for effectively showcasing the proposed method's effectiveness. Considering a more realistic environment like CARLA, which incorporates a range of distractions both related and unrelated to the agent's actions, could provide valuable insights. The Atari and DeepMind Control Suite with distractions, while useful for initial testing, may not fully capture the complexities of real-world scenarios where distractions are more varied and dynamic.
5. In this paper, the authors did not analyze whether the data augmentation or the augmented temporal contrast loss had a greater impact on the model performance. It would be beneficial to conduct ablation studies to explore this further. Without such an analysis, it is difficult to determine the individual contribution of each component to the overall performance gain.
6. In Fig.1, the arrow between $h_t$ and $z_{t+1}$ is incorrect.

### Questions
Please see the weaknesses section.

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
This paper introduces a new world model for deep reinforcement learning by integrating DreamerV3 with augmented temporal contrast (ATC) as an auxiliary loss. This added component enhances the world model's robustness to exogenous, irrelevant features. The authors evaluate their approach on the Atari 100k benchmark and conduct several ablation studies.

### Strengths
- [S1] The paper proposes a novel and meaningful combination of established methods, leveraging ATC to strengthen DreamerV3's auxiliary loss, which is a promising direction.
- [S2] The paper demonstrates a good selection of experiments, yielding promising—albeit preliminary—results on the Atari 100k benchmark.

### Weaknesses
 - [W1] Figure 2, in its current form, is not particularly convincing. Firstly, it's unclear whether it shows reconstructions from a real trajectory or a rollout generated by the world model. This distinction should be clarified both in the figure caption and in Section 5.1. I assume it represents a rollout, as the trajectories appear noticeably different. For instance, the second row might depict the initial situation in Breakout, where the paddle moves before the 'FIRE' command, making it reasonable to model the absence of the ball. To strengthen this experiment, the authors should consider using consistent starting states for rollouts, especially since the evaluation relies exclusively on qualitative assessment without quantitative metrics. The lack of a quantitative metric makes it difficult to assess the quality of the rollouts, and the use of inconsistent starting states further complicates any qualitative analysis.
- [W2] The "Implementation" section in 4.2 is confusing. The variable $\overline{x}$ (presumably the latent features from the target encoder) is used without prior introduction. The terms "forward propagation $p_t$" (line 248) need clarification—do the authors mean "forward prediction"? Additionally, the notation $p_t = x_t + h_\phi(x_t)$ suggests a residual connection, which requires further explanation. Lastly, it's unclear how the matrix $W$ is updated; if it's part of $\phi$, this should be made explicit. The description of the contrastive loss lacks sufficient detail, particularly regarding the update mechanism for the transformation matrix $W$ and the precise nature of the residual connection. The relationship between the target encoder and the online encoder also needs to be clarified, especially how the EMA is applied.
- [W3] The paper does not sufficiently differentiate which components are inherited from ATC and which are original contributions. For example, Section 4.2 introduces anchors and positives from ATC, but it is unclear whether elements like the InfoNCE loss, target encoder with EMA, and data augmentation are standard in ATC or were newly introduced. Additionally, it would be beneficial to reference Stooke et al. (2021) in lines 170-176. The paper needs to clearly delineate which aspects of the method are directly adopted from the ATC framework and which are novel contributions. The specific implementation details of the InfoNCE loss, target encoder with EMA, and data augmentation should be explicitly stated, as these are critical to the method's success.
- [W4] All experiments use only three random seeds, and ablation studies are limited to three games, reducing the generalizability of the findings. Although the authors acknowledge this limitation, and I understand that expanding these experiments may be challenging, doing so would significantly strengthen the paper's significance. The limited number of random seeds and games in the ablation studies raises concerns about the robustness and generalizability of the results. The findings might be specific to the chosen games and random initializations.
- [W5] More presentation issues:
  - Equations should be numbered for ease of reference.
  - The encoder notation $g_\phi$ appears in Section 4.2 without prior introduction. Including it in the overview on lines 189-197 would improve clarity.
  - Section 7 could be merged with Section 6 for a more cohesive structure.
  - Moving Section 5.4 to the beginning of Section 5 would clarify the experimental setup. Additionally, including a description of the Atari 100k benchmark in this section (noting it comprises a subset of 26 games) would be helpful.
  - Lines 207-209: Consider rephrasing for clarity: "For regularization, we use a target encoder updated via exponential moving averages (EMA) and apply data augmentation to the sensory observations."
  - Figure 2 could be improved by reducing font size, labeling rows, and adding whitespace between them.
  - Line 125: "scricter" should be "stricter"
  - Line 186: Correct symbols to $\hat{r}_t$ and $\hat{o}_t$.

### Questions
- [Q1] Why is an additional recurrent predictor used? Could the RSSM not serve this purpose?
- [Q2] I assume a frame skip of 4 is applied, meaning the prediction horizon of $K = 4$ would cover 16 frames. Could the authors confirm?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work focuses on improving the world models of reconstruction-based MBRL approaches. It tries to address the issue of learning task-irrelevant features arising from pixel-level reconstructions by modifying DreamerV3 with an additional Augmented Temporal Contrasted (ATC) loss term. Empirically, the authors show that this results in superior sample efficiency on the Atari 100k benchmark and also give a few examples of improved representation learning.

### Strengths
1. The fundamental limitation of reconstruction-based MBRL is nicely outlined and the idea behind the proposed approach is explained intuitively.
2. Subsections 5.3 and 5.4 show promising results (but would still like to see more extensive results).
3. Subsection 5.5 discovers an important limitation of ATC which might inspire new research directions.

### Weaknesses
1. The greatest weakness of this work is the lack of novelty. It is a direct application of ATC by [Stooke et al. 2021](https://arxiv.org/pdf/2009.08319) to DreamerV3 [Hafner et al. 2024](https://arxiv.org/pdf/2301.04104v2). While this is a clear weakness, it can still be executed in such a way that it is more fruitful for the research community. One option would be to explore the idea of ATC to the larger scope of MBRL, not just Dreamer. Another option that would compensate for this weakness would be extensive empirical experiments and novel findings.
    * Note that the lack of algorithmic or theoretical contributions means that I am evaluating your work mostly on the empirical results presented.
2. I generally found Section 4 to be poorly written and I struggled to understand this relatively simple method.
    * I found the introduction of the encoders and variables produced (as outputs of models) highly confusing. Section 4.1 introduces $x_t$ which is not part of Dreamer but never explains what produces this variable. Then seemingly all the model components are presented in the equations of Section 4.1, yet it still unclear where this is coming from. Section 4.2 then adds an additional deterministic decoder component which produces $x_t$ forcing readers to circle back and re-read the whole section to understand the flow of variables. While I am not sure what is the best idea, I can suggest (1) re-writing the whole section as if you are explaining Dreamer from scratch or (2) assuming dreamer formulation and tightly focusing on how you modify the training of the encoder.
    * It is not clear from the text along what the transformation matrix W is. Given that this is your core algorithmic contribution, I strongly suggest expanding on this.
3. Mathematical formulations are sloppy.
    * Equations are not numbered.
    * Variables are used liberally. Main loss equation (right above subsection 4.3), you use T very liberally. Following your problem definition, T should be episode length. If so, I doubt you are computing this loss over the whole episode. Furthermore, the expectation doesn’t seem right as there is a replay buffer here.
4. Results are a combination of limited and unconvincing.
    * In my opinion, when you add complexity to an already very complicated algorithm such as Dreamer, the benefits of this have to be very clearly visible. This is the lens from which I am approaching this.
    * Subsection 5.1 attempts to answer “Does our method learn useful endogenous representation for the world model?” by using one subjective demonstration on a single task with a single seed. I find this insufficiently rigorous do draw any conclusions from. I suggest attempting to answer this question by focusing on specific tasks that have these types of environment dynamics and presenting numerical results from that.
    * Subsection 5.2 shows promising results but I find it very limited as it only shows 3 environments. I believe we are far beyond this point as a research community. Furthermore, if you want to showcase sample efficiency, I suggest showing return vs samples in Figure 3.
    * Table 1 is difficult to read and draw conclusions from as noted by [Agarwal et al., 2022](https://arxiv.org/abs/2108.13264). As you already have this, I would strongly suggest replacing Table 1 with Figure 6.
5. The proposed approach also includes an image augmentation technique in the form of a shift operation. It is unclear how much this helps to achieve the final results. You should include an ablation of removing this but keeping the ATC loss.

### Questions
1. What are the evaluation metrics used in Figure 3? They are not described in the text up to that point.
2. One of the interesting things about your method is that it allows for training MBRL algorithms without reconstruction. Why didn't you explore other world model frameworks such as TDMPC [(Hensen et al, 2022)](https://arxiv.org/abs/2203.04955)?
3. Do you have any intuition as to why your proposed method doesn't work as well on the Distracting Control Suite?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper aims to improve the robustness of the world model training in MBRL, which is important to its generalizability and sample efficiency. Going beyond relying on pixel-level reconstruction, this paper enables the world model focusing on task-related information by augmenting world model training with a temporal prediction loss in embedding space. The experiments demonstrate its improvements in representation quality and overall performance.

### Strengths
1.This paper is well written, easy to follow, and the  motivation is clear.  For instance, the notion of endogenous and exogenous information is well explained with a specific example in the introduction.

2.The proposed method, though simple, makes sense, as it adds a sensible auxiliary loss function in DreamerV3 to learn a more robust representation for embedding forward prediction. The experiments demonstrate its performance.

### Weaknesses
1. The proposed idea is straightforward.

2. Loss clarification. The paper does not clarify  how the forward-predictive scheme with ATC loss helps to learn sufficiently endogenous features. In section 4.2 where the design of ATC loss is presented,  the relationship between these loss functions and endogenous information is not clear.  In particular, the paper should try best to explain why this loss function “prefers” endogenous information. I suggest the authors provide a theoretical justification or empirical analysis showing how the loss function encourages focus on task-relevant information.

3.  Augmentation. More details on augmentation are needed to understand the key steps in the proposed method. How does the augmentation by random shifts on observation produce the time sequences of anchor and positive from t to t+T+K? Does this augmentation involve random actions in  the environment or just random shifts that change the observation frames while the environment stays the same? It will help to provide a step-by-step description of the augmentation process.

4.  Figures. Some figures in the paper should be improved to make them more readable. For example, the ball in Figure.2 is too small to read.  Also, there is no label in the figure (only in the caption) to indicate the model of each line, which makes the figures hard to understand.  I recommend enlarging the ball in Figure 2 and providing a legend for clarity.

### Questions
Figure 2 shows the reconstruction in 40k and 60k steps, while the experiments are in 100k steps. How is the reconstruction of DreamerV3 in 100k steps or more? The ball is still invisible sometimes?

Can the authors compare the proposed methods against other methods, such as image augmentation, in terms of robustness? More experiments along this line will strengthen the contributions.

### Soundness
2

### Presentation
3

### Contribution
2
