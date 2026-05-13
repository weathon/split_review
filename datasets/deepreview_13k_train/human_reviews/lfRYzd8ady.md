# Discrete Codebook World Models for Continuous Control

- Decision: Accept
- Scores: 5, 8, 8, 5, 8, 6

## Abstract
In reinforcement learning (RL), world models serve as internal simulators, enabling agents to predict environment dynamics and future outcomes in order to make informed decisions. While previous approaches leveraging discrete latent spaces, such as DreamerV3, have achieved strong performance in discrete action environments, they are typically outperformed in continuous control tasks by models with continuous latent spaces, like TD-MPC2. This paper explores the use of discrete latent spaces for continuous control with world models. Specifically, we demonstrate that quantized discrete codebook encodings are more effective representations for continuous control, compared to alternative encodings, such as one-hot and label-based encodings. Based on these insights, we introduce DCWM: Discrete Codebook World Model, a model-based RL method which surpasses recent state-of-the-art algorithms, including TD-MPC2 and DreamerV3, on continuous control benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper explores the use of discrete latent spaces for continuous control with world models. The authors introduce DCWM: Discrete Codebook World Model, a model-based RL method which surpasses recent state-of-the-art algorithms. it’s a well written paper in general.

### Strengths
1. The authors demonstrate that quantized discrete codebook encodings are more effective representations for continuous control, compared to alternative encodings, such as one-hot and label-based encodings. 

2. The authors  introduce DCWM: Discrete Codebook World Model, a model-based RL method which surpasses recent state-of-the-art algorithms, including TD-MPC2 and DreamerV3, on continuous control benchmarks.

### Weaknesses
What it misses I think  is  a comparison of the method with other approaches that are not based on the same embeddings ideas. For example I think MAMBA and Hungry hungry hippos (H3) apply to similar scenarios.

### Questions
I think a comparison of the method with other approaches that are not based on the same embeddings ideas can be added.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a new architecture for world modeling for continuous control that utilizes discrete representations. Rather than use a learned codebook or one-hot encodings, they utilize finite scalar quantization (FSQ) which simplifies the loss function and stabilizes the learning according to their claims. They build upon the TD-MPC2 algorithm which utilizes model predictive path integral (MPPI) to search the world model for high value actions.

They test their algorithm in a number of high dimensional continuous control tasks including Meta-World manipulation and DeepMind Dog and Humanoid tasks, showing that their algorithm achieves higher success and learns with fewer samples compared to baselines. In addition to comparison against baselines, they also provide experiments supporting their choice of discrete encodings, showing that they can achieve similar performance to one-hot encodings while increasing training efficiency.

### Strengths
The paper is well-written and explains all necessary background material in sufficient detail to understand the algorithm. While none of the individual components are novel, the experimental evaluation provides evidence that the proposed algorithmic details are critical for the success of model-based learning.

### Weaknesses
The one question that I have relates to the use of REDQ to reduce bias in the TD learning. Since the baseline does not seem to use this method, it begs the question of how much of the demonstrated performance is due to this component. It would be nice to see how DCWM compares to a version that uses the standard one or two Q functions to make sure the performance gap is in fact due to the choice of latent spaces. Furthermore, it is unclear what the computational costs of this method are. While the paper claims that FSQ simplifies the loss function, it is not clear if this translates to a reduction in training time or computational resources. A more detailed comparison of the computational costs, such as training time and memory usage, would be beneficial to understand the practical implications of the proposed method.

### Questions
What does the algorithm performance look like without using REDQ?

What are the computational costs or benefits to this method over TD-MPC in terms of runtime?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors contribute a novel method, called DCWM, for model-based RL on continuous control tasks. Specifically, building on the works of Dreamer V3 and TD-MPC2 (prior model-based continuous control methods), the paper sheds light on the impact of how these methods encode latent state (different ways of discrete encoding vs. continuous), how that state is trained (a categorical loss or a regressive loss), and the impact of stochasticity in modeling dynamics. The paper conducts experiments and ablations on Deepmind Control Suite and Meta World to identify which components are most impactful on performance, and combines them to present the aforementioned method, while comparing to baselines from literature. The authors conclude that learning a discrete latent state (specifically one encoded by codebook quantization over other methods), and training with a cross entropy objective results in improved performance.

### Strengths
The authors present a strong paper, with excellent methodology and solid experimental results. They compare with two SOTA baselines, Dreamer V3 and TD-MPC2, and demonstrate that their method indeed outperforms or matches the baseline performance. They conduct additional experiments (sections 4.3, 4.4 and 4.5) to understand how different variables affect performance, which enhances the paper's contributions to bettering understanding latent spaces in world model learning. The paper's clarity is also very good, with a great presentation of background and method. The authors provide sufficient detail, such as the discussion around the fixed FSQ codebook illustration in Figure 2 or the extensive documentation of various tricks used to improve performance (lines 309, 352, 355, etc.). Additionally, the supplementary material is strong, with detailed extra information on method, environment, architecture, etc, and addition ablation experiments. The results contributed are significant, not only advancing the state of the art for model-based continuous control (to my knowledge), but also contributing to the field's understanding of the impacts of latent space encodings, losses, and stochasticity in modeling transition dynamics. I would argue that the method merits originality as well, since it cleverly combines prior work (the consistency approach from TD-MPC2 and discrete encodings/cross entropy objective from Dreamer V3) and introduces novel elements as well (codebook quantization). 

Overall, this is a strong contribution to the field, and I recommend acceptance.

### Weaknesses
The paper is free of major flaws: it has thoroughly conducted experiments and is clear and well-written. However, I have identified some nits and clarifying questions listed in the section below that would be minor improvements.



### Questions
Question:
- I imagine that taking the expected code might sometimes result in an invalid state, as discussed here:

>  Whilst the expected value of
a discrete variable does not necessarily take a valid discrete value, we find it effective in our setting.

Is that simply then fed into the dynamics model (after normalization etc.) and the reward model MLPs?
- Relatedly, when you normalize the code to [-1, 1], you claim it improves performance. Is there a reference for this or was this empirically observed? Would you be able to speak to why this is required? (One thought I had was it normalizes the different quantization levels $L_i$, i.e. the two channels would otherwise have values ranging from [-5, 5] and [-3, 3]).

Nits (not affecting score):
- line 217, formatting for `i-th` and `d-th` is inconsistent, and should use latex
- line 352 typo in 'warms starts'
- line 465, missing 'and' before models in 'entropy), **and** models'

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes a model-based RL method for continuous control tasks. Compared with TD-MPC2, the latent space is represented as a discrete codebook. The proposed modifications lead to some improvements over TD-MPC2.

### Strengths
1. The paper is well organized and easy to follow. 
2. The description of the contribution to the article is simple and concise. 
3. The ablation experiment is sufficient and persuasive.

### Weaknesses
1. The test for multi-tasking learning is missing. It would be great if the authors could consider extend their studies to multi-task learning and study the differences in codebooks between different control tasks.
2. In some Meta-World tasks, the performance of the proposed method is comparable to TD-MPC2, and the variance is larger. Specifically, the performance on tasks like 'assembly' and 'peg-insert-side' appears quite similar, and the higher variance suggests a lack of robustness in these scenarios. A more detailed analysis of why the proposed method does not consistently outperform TD-MPC2 across all tasks is needed.
3. The stochastic transition dynamics in the latent space could be better described and explained. The current description lacks detail on how the categorical distribution is parameterized and how the logits are generated from the previous latent state and action. It is unclear how the model ensures that the predicted probabilities are well-calibrated and lead to stable training.

### Questions
1. The authors kept most hyperparameters fixed across all tasks, what parameters will affect the performance of some special tasks?
2. Is the codebook a direct application of quantization-aware training (QAT)?
3. How to determine the weights of the expected code? Is this a hyperparameter of the algorithm?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a discrete latent space approach for world models in continuous control, utilizing FSQ within a MBRL algorithm, DCWM, following TD-MPC2. The experiments, conducted on DMC and Metaworld, demonstrate improvements over state-of-the-art methods, including TD-MPC2 and DreamerV3. Additionally, the authors analyze the effectiveness of discrete vs. continuous latents, classification vs. regression objectives, and deterministic vs. stochastic transitions.

### Strengths
1. The investigation into latent space design is valuable for the model-based RL community.
2. The experiments are informative, offering insights across multiple dimensions of the design.

### Weaknesses
1. A significant concern is the need for clarification; some claims may be overstated. See questions below.
2. For an impactful empirical study on algorithmic design, the scale of experiments—particularly in terms of the number of environments and tasks—seems insufficient. The experimental design is also somewhat confusing; see questions below.

On clarifcation (major):

1. The claim in the abstract that discrete latent spaces typically underperform in continuous control tasks needs specification. First of all, to my knowledge, TD-MPC2 only conducts experiments on state-based tasks, lacking results on pixel-based continuous control, while DreamerV3 does include these. Second, it is unfair to compare methods with (TD-MPC) and without inference-time planning (Dreamer), as in the MuZero paper we can see that this makes a great performance boost. I think this work can naturally motivate itself from TD-MPC2 alone instead of comparing DreamerV3 and TD-MPC2 without head-to-head experiments.
2. A preliminary section clarifying different discrete encodings is necessary; I find the distinction between label encoding and one-hot encoding unclear for the first-time reading. The methods section extensively describes FSQ, which is not originally proposed here.
3. Also, the methods section contains many elements that directly follow TD-MPC2, which may confuse non-expert readers regarding what is novel. Clear differentiation is needed. For example, TD-MPC2 exactly uses an ensemble of five critics with randomly sampled two for bootstrap, but this is not explicitly mentioned by the authors in Line 277.
4. Algorithm 1 appears to be a standard procedure in model-based RL and could be moved to the appendix.

On clarifcation (minor):

1. Can you elaborate on what you mean by "codebook encoding captures similarity between observations" and how this contrasts with one-hot encodings in Line 248?
2. I did not understand why "we did not conﬁgure the transition model to accept the label and one-hot encodings as this resulted in the agent being unable to learn." Can you explain more?
3. I did not understand the sentence "our codebook is conﬁgured with b = 2 channels and the label encoding incorrectly assumes an ordinal structure through both." How does the hyperparameter $b$ in your proposed codebook encoding affect label encoding?
4. In Line 514, why is $|C|=2^4$ for $L=[5,3]$, when it is claimed $|C|=\prod L_i$ in Line 224.

On experiments:

1. Could you provide additional experiments on more tasks, such as ManiSkill2/Myosuite, which TD-MPC2 used? It would also be beneficial to include experiments on more base algorithms, such as DreamerV3 (see question 2).
2. The most direct evidence that the proposed discrete latents outperform one-hot and continuous latents would be to replace the latent space in DreamerV3 and TD-MPC2 with your proposed approach. Why wasn't this head-to-head comparison conducted?
3. Have you compared FSQ and VQ (referred to as dictionary learning in Line 206)?
4. Codebook encoding only outperforms one-hot encoding in one task in Figure 6, yet it is claimed to be more computationally efficient in Line 485. Is there any numerical analysis to support this claim?

### Questions
On clarifcation (major):

1. The claim in the abstract that discrete latent spaces typically underperform in continuous control tasks needs specification. First of all, to my knowledge, TD-MPC2 only conducts experiments on state-based tasks, lacking results on pixel-based continuous control, while DreamerV3 does include these. Second, it is unfair to compare methods with (TD-MPC) and without inference-time planning (Dreamer), as in the MuZero paper we can see that this makes a great performance boost. I think this work can naturally motivate itself from TD-MPC2 alone instead of comparing DreamerV3 and TD-MPC2 without head-to-head experiments.
2. A preliminary section clarifying different discrete encodings is necessary; I find the distinction between label encoding and one-hot encoding unclear for the first-time reading. The methods section extensively describes FSQ, which is not originally proposed here.
3. Also, the methods section contains many elements that directly follow TD-MPC2, which may confuse non-expert readers regarding what is novel. Clear differentiation is needed. For example, TD-MPC2 exactly uses an ensemble of five critics with randomly sampled two for bootstrap, but this is not explicitly mentioned by the authors in Line 277.
4. Algorithm 1 appears to be a standard procedure in model-based RL and could be moved to the appendix.

On clarifcation (minor):

1. Can you elaborate on what you mean by "codebook encoding captures similarity between observations" and how this contrasts with one-hot encodings in Line 248?
2. I did not understand why "we did not conﬁgure the transition model to accept the label and one-hot encodings as this resulted in the agent being unable to learn." Can you explain more?
3. I did not understand the sentence "our codebook is conﬁgured with b = 2 channels and the label encoding incorrectly assumes an ordinal structure through both." How does the hyperparameter $b$ in your proposed codebook encoding affect label encoding?
4. In Line 514, why is $|C|=2^4$ for $L=[5,3]$, when it is claimed $|C|=\prod L_i$ in Line 224.

On experiments: 

1. Could you provide additional experiments on more tasks, such as ManiSkill2/Myosuite, which TD-MPC2 used? It would also be beneficial to include experiments on more base algorithms, such as DreamerV3 (see question 2).
2. The most direct evidence that the proposed discrete latents outperform one-hot and continuous latents would be to replace the latent space in DreamerV3 and TD-MPC2 with your proposed approach. Why wasn't this head-to-head comparison conducted?
3. Have you compared FSQ and VQ (referred to as dictionary learning in Line 206)?
4. Codebook encoding only outperforms one-hot encoding in one task in Figure 6, yet it is claimed to be more computationally efficient in Line 485. Is there any numerical analysis to support this claim?

Overall, I find this paper interesting. If the authors adequately address my concerns, I would be willing to significantly improve my rating.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper explores the application of discrete latent spaces for continuous control in reinforcement learning (RL), an innovative perspective other than the typical use of continuous latent spaces. The authors introduce the Discrete Codebook World Model (DCWM), which utilizes quantized discrete codebook encodings to represent latent states. The DCWM is demonstrated to surpass recent state-of-the-art RL algorithms, including TD-MPC2 and DreamerV3, especially in those tasks with high-dimensional action spaces.

### Strengths
1. Although similar ideas like the token-based world model were recently published, the proposed method seems computationally efficient, benefiting from the 'Finite Scalar Quantization' paper.
2. The paper first made the discrete latent space method work in continuous control tasks.
3. The paper writing is clear and easy to understand.

### Weaknesses
1. This paper lacks comparisons with the more advanced baselines like EfficientZero-V2.
2. The authors didn't test the proposed method with visual inputs, which made this paper not that strong.

### Questions
1. What's your idea about if FSQ-based discretization could be used for action space discretization? (like action sampling) If yes, how will you do that?
2. Although it could be more computationally challenging, could you please provide several visual input results? You can ignore the most difficult tasks like humanoid walk/run.

### Soundness
4

### Presentation
3

### Contribution
3
