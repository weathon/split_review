# Drama: Mamba-Enabled Model-Based Reinforcement Learning Is Sample and Parameter Efficient

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Model-based reinforcement learning (RL) offers a solution to the data inefficiency that plagues most model-free RL algorithms. However, learning a robust world model often demands complex and deep architectures, which are expensive to compute and train. Within the world model, dynamics models are particularly crucial for accurate predictions, and various dynamics-model architectures have been explored, each with its own set of challenges. Currently, recurrent neural network (RNN) based world models face issues such as vanishing gradients and difficulty in capturing long-term dependencies effectively. In contrast, use of transformers suffers from the well-known issues of self-attention mechanisms, where both memory and computational complexity scale as $O(n^2)$, with $n$ representing the sequence length.

To address these challenges we propose a state space model (SSM) based world model, specifically based on Mamba, that achieves $O(n)$ memory and computational complexity while effectively capturing long-term dependencies and facilitating the use of longer training sequences efficiently. We also introduce a novel sampling method to mitigate the suboptimality caused by an incorrect world model in the early stages of training, combining it with the aforementioned technique to achieve a normalised score comparable to other state-of-the-art model-based RL algorithms using only a 7 million trainable parameter world model. This model is accessible and can be trained on an off-the-shelf laptop.git}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces DRAMA, a model-based reinforcement learning (MB-RL) agent that leverages the Mamba-2 architecture, a state space model (SSM), as its core dynamics architecture. Traditional MB-RL approaches often rely on recurrent neural networks (RNNs) or transformers for world modelling, which suffer from issues like vanishing gradients, difficulty in capturing long-term dependencies, and quadratic scaling of computational complexity with sequence length. DRAMA addresses these challenges by utilizing Mamba-2, which achieves linear computational and memory complexity while effectively capturing long-term dependencies.

Additionally, the authors propose a novel dynamic frequency-based sampling (DFS) method to mitigate the suboptimality arising from imperfect world models during early training stages. They evaluate DRAMA on the Atari100k benchmark, demonstrating that it achieves performance comparable to state-of-the-art algorithms using a significantly smaller world model (7 million parameters) that can be trained on standard hardware. The paper also includes ablation studies comparing Mamba-1 and Mamba-2, highlighting the superior performance of Mamba-2 despite its constrained expressive power.

### Strengths
- **Originality:** The paper introduces the novel application of Mamba-2 SSMs within MB-RL, specifically as the dynamics model in the world model. This is a new approach that addresses the limitations of existing architectures like typical RNNs and transformers and it makes a lot of sense in my opinion.
- **Quality:** The authors provide thorough experimental evaluations on the Atari100k benchmark, demonstrating that DRAMA achieves competitive performance with significantly fewer parameters (at least in the tasks and model sizes tested). The inclusion of ablation studies comparing Mamba-1 and Mamba-2, as well as the impact of DFS, strengthens the empirical results.
- **Clarity:** The paper is well-written and structured, providing clear explanations of the methodology, including detailed descriptions of Mamba-2 and how it is integrated into the world model. The figures and tables effectively support the textual content although I would make some further stylistic improvements in Figure 1 to maximise clarity.
- **Practical impact:** By achieving comparable performance to state-of-the-art methods with a smaller and more computationally efficient model, the DRAMA method contributes to making MB-RL more accessible and practical, particularly in resource-constrained environments.

### Weaknesses
 - **Unsupported claims about capturing long-term dependencies:** While the authors claim repeatedly that Mamba-2 effectively handling long-term dependencies, the paper provides limited direct evidence or analysis to demonstrate this capability. Including experiments or analyses that specifically test and showcase the ability to capture long-term dependencies would strengthen the paper. For instance, a task designed to require long-term memory or metrics that quantify the model's ability to capture dependencies over long sequences could be included. In the current form of the paper, it is not clear to me what "long" really means.
- **Limited Comparison with Scaled Models:** The comparison with DreamerV3 is somewhat limited. While the authors emphasize parameter efficiency, it would be valuable to see how DRAMA performs when scaled up to match the model size of DreamerV3, even on a subset of games. This would help understand the limits and potential of their approach and whether the advantages of Mamba-2 persist at larger scales. If hardware limitations prevented this, a discussion of these constraints would be very helpful.
- **Marginal Performance Gains:** While DRAMA achieves comparable performance to existing methods, the improvements are not substantial across all games. Demonstrating scenarios where DRAMA significantly outperforms other approaches would strengthen the claims about its effectiveness.
- **DFS Method Clarity:** The explanation of the dynamic frequency-based sampling method could be more detailed. Providing more comprehensive comparisons with other sampling strategies would help in understanding its effectiveness. Additionally, including ablation studies that isolate the impact of DFS would clarify its contribution.
- **Hyperparameter Sensitivity:** The paper mentions that increasing the model size leads to better performance but does not deeply explore this aspect. Though I understand that extensive hyperparameter search might be too difficult given computational constraints, some analysis of how sensitive DRAMA is to hyperparameter choices, including model size, sequence length, and learning rates, would be very valuable for understanding its practical applicability, otherwise the paper looks relatively incomplete.

### Questions
- **Evidence of Long-Term Dependency Capture:** You mention the ability of DRAMA to capture long-term dependencies. Could you provide more direct evidence or experiments that demonstrate this capability? For example, have you considered tasks that specifically require long-term memory or conducted analyses that quantify the effective memory length of the model?
- **Scaling DRAMA for Direct Comparison:** Have you considered scaling up DRAMA to match the model size of DreamerV3 for a direct comparison? If not, could you explain the limitations (e.g., hardware constraints) that prevented this? Testing DRAMA with larger models on a few games could provide insights into its scalability and performance limits.  
- **Effectiveness of DFS:** Could you elaborate on how the dynamic frequency-based sampling (DFS) method compares to other sampling strategies in terms of its impact on learning efficiency and final performance? Including quantitative comparisons or ablation studies would be helpful.
 - **Hyperparameter Sensitivity and Trade-offs:** Can you provide insights into the trade-offs between model size and performance in DRAMA? Specifically, how does increasing the size of the Mamba-2 model or the autoencoder affect results across different games?
- **Code and Reproducibility:** Is there a plan to release the code and pretrained models for DRAMA to facilitate reproducibility and further research in this area?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes using State-Space Models (SSMs) for learning World Models. Specifically, the architecture comprises an encoder to get discrete latents, a SSM module (Mamba-2) to estimate the dynamics which is used to predict the latent embedding of observation, reward value and termination flag. This world model is used to train a policy by imagination. The paper also uses a method to sample transitions from the replay buffer based on the number of times the transition is used to update WM and policy. Experiments conducted on Atari100K show that the proposed method Drama attains similar performance to IRIS and TWM with a much smaller model in terms of parameters.

### Strengths
- The proposed idea of using SSM for WMs is interesting as they provide crucial benefits over training with Transformers and RNNs. 
- The proposed method achieves good performance with significantly fewer parameters (7M) when compared with baselines.

### Weaknesses
 - It is hard to articulate where the performance gains are coming from. Section 3.2.1 discusses that DFS provides an advantage over uniform sampling. Since DFS is agnostic to most baselines, it is important to see a comparison of either Drama with Uniform Sampling or baselines with DFS sampling to understand if the architecture is helping or the sampling.
- The paper is not well written and it is hard to understand the details and motivation behind the design choices. Questions 1-5 below expand on this. The paper can use a pseudocode to describe the behavior learning part.

- At line 222, it is not clear what targets mean.
- Section 2.3 is not described well. At line 240, when the ‘b’ starting points are sampled of length $l_{img}$, is it just picking random samples along $b_{img}$ sequences? Since the batch sampled from replay buffer is of length $l_{img}$, I am unsure what this additional sampling is doing? Why not just sample $b$ trajectories from the buffer?
- What is $h_t$ in behavior policy learning? The deterministic variable is defined as $d_t$ in Eq 5.
- While training Dreamer, the method uses the whole sequence of ($b_{img}, l_{img}$) to compute a good hidden state and uses all sampled to generate trajectories in the future. I am curious to know why only the last hidden state $l_{img}$ is used for learning the policy and not the whole sequence like Dreamer? (describe around line 243).
- The terminal flag is defined as $e_t$ at line 93, whereas it is $t_i$ in description of Figure 1. Also, the description of Fig 1 uses $i$ for indexing the time and the Section 2 starts with $t$ as time index. The description of Fig 1 should match the notation in the main text.
- Was any experiment conducted to see if the behavior model underestimates rewards especially with limited data?
- For the ablation presented in Sec 3.2.2, were both variants Mamba-1 and Mamba-2 based WM trained with DFS?
- How does the proposed method compare with R2I [1]. Since they propose using SSMs, should it be included as another baseline?
- [Typo] Employs is written twice at line 132.

### Questions
1. At line 222, it is not clear what targets mean.
2. Section 2.3 is not described well. At line 240, when the ‘b’ starting points are sampled of length $l_{img}$, is it just picking random samples along $b_{img}$ sequences? Since the batch sampled from replay buffer is of length $l_{img}$, I am unsure what this additional sampling is doing? Why not just sample $b$ trajectories from the buffer?
3. What is $h_t$ in behavior policy learning? The deterministic variable is defined as $d_t$ in Eq 5.
4. While training Dreamer, the method uses the whole sequence of ($b_{img}, l_{img}$) to compute a good hidden state and uses all sampled to generate trajectories in the future. I am curious to know why only the last hidden state $l_{img}$ is used for learning the policy and not the whole sequence like Dreamer? (describe around line 243).
5. The terminal flag is defined as $e_t$ at line 93, whereas it is $t_i$ in description of Figure 1. Also, the description of Fig 1 uses $i$ for indexing the time and the Section 2 starts with $t$ as time index. The description of Fig 1 should match the notation in the main text.
6. Was any experiment conducted to see if the behavior model underestimates rewards especially with limited data? 
7. For the ablation presented in Sec 3.2.2, were both variants Mamba-1 and Mamba-2 based WM trained with DFS?
8. How does the proposed method compare with R2I [1]. Since they propose using SSMs, should it be included as another baseline?
9. [Typo] Employs is written twice at line 132.

#### References
[1] Samsami et al., Mastering Memory Tasks with World Models, ICLR’24.

### Soundness
3

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
3

### Summary
This paper presents a new world model for deep reinforcement learning that is based on the Mamba-2 architecture. In addition, the authors introduce dynamic frequency-based sampling, which leads to more accurate imaginations of the world model. The approach achieves competitive performance on the Atari 100k benchmark while maintaining a lightweight architecture with only 7 million trainable parameters.

### Strengths
- [S1] The paper combines established methods in a novel way, effectively addressing an existing gap in world model research.
- [S2] The proposed model is computationally efficient, requiring only 7 million trainable parameters, making it accessible.

### Weaknesses
 - [W1] The extent to which the Mamba architecture contributes to the model's performance remains unclear. Specifically, it is unclear how DFS impacts scores across all games. Extending ablation study 3.2.1 to cover more games, or conducting a new study that replaces Mamba with an RNN or transformer, would clarify these contributions.
- [W2] While the paper emphasizes Mamba's computational efficiency, there is a lack of exact wall-clock training and inference times. The abstract claims the model can be trained on a standard laptop, so providing specific runtime metrics would substantiate this claim.
- [W3] Several presentation aspects should be improved:
  - The paragraph in lines 99–105 shifts from general statements about model-based RL to specific details about the paper's world model. This transition could lead readers to infer that every world model relies on a variational autoencoder or linear heads, which isn't necessarily the case. Additionally, other model-based RL methods exist that don't utilize world models, such as those using lookahead search.
  - Many figures contain small text that is difficult to read without zooming.
  - Minor suggestions:
    - Highlight the highest scores in Table 1 for easy reference.
    - Correct notations for all \hat{} terms (e.g., \hat{r}_t instead of \hat{r_t}).
    - Address minor notation errors: e.g., incorrect $A$ on lines 148, 154, 169 and incorrect $T$ on line 177
    - Variables on line 218 should be in math mode.
    - Consider changing "auto-generative" to "autoregressive" on line 238?
    - Revise line 264 to read "tracks the number of *times* the transition has been used."
- [W4] To strengthen the soundness of findings, additional evaluations on alternative benchmarks, such as the DeepMind Control Suite, would be valuable. That said, I understand this may be challenging to realize.

### Questions
- [Q1] Could the decoder operate based on the output of Mamba-2, such that $d$ rather than $z$ serves as the input?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a MAMBA-based world model architecture, as opposed to previous transformer and RSSM based ones. They also compare between MAMBA-1 and MAMBA-2 for world models. Finally, they evaluate and ablate their technique on the Atari100k benchmark.

### Strengths
- The combination of MAMBA and Sequence-based world models is novel
- The authors demonstrate comparable results with a smaller model size

### Weaknesses
 - Some results are unclear. For example, could you go into details on why the model is not doing well on the Breakout game? What is it producing? Some figures from the game can be also useful--not just this one, but the ones in which model does well too.
- It is not clear why imagination context length is kept to 8. I would suggest providing experiments, both involving time-complexity and performance, for different imagination context length. Also, explaining why this is done would be useful.

### Questions
- What is the value of h?
- "A key difference between Mamba-based and transformer-based world models in the ‘imagination’ process is that Mamba updates inference parameters independent of sequence length."--can you explain it more?

### Soundness
3

### Presentation
3

### Contribution
3
