# Hindsight Preference Learning for Offline Preference-based Reinforcement Learning

- Decision: Reject
- Scores: 5, 3, 5, 8, 5

## Abstract
Offline preference-based reinforcement learning (RL), which focuses on optimizing policies using human preferences between pairs of trajectory segments selected from an offline dataset, has emerged as a practical avenue for RL applications. Existing works rely on extracting \emph{step-wise} reward signals from \emph{trajectory-wise} preference annotations, assuming that preferences correlate with the cumulative Markovian rewards. However, such methods fail to capture the holistic perspective of data annotation: Humans often assess the desirability of a sequence of actions by considering the overall outcome rather than the immediate rewards. To address this challenge, we propose to model human preferences using rewards conditioned on future outcomes of the trajectory segments, i.e. the \textit{hindsight information}. For downstream RL optimization, the reward of each step is calculated by marginalizing over possible future outcomes, the distribution of which is approximated by a variational auto-encoder trained using the offline dataset. Our proposed method, \emph{Hindsight Preference Learning (HPL)}, can facilitate credit assignment by taking full advantage of vast trajectory data available in massive unlabeled datasets. Comprehensive empirical studies demonstrate the benefits of HPL in delivering robust and advantageous rewards across various domains.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a new preference learning method that utilizes hindsight information. By incorporating future states into the reward through a VAE structure, HPL can generate more robust rewards and overcome the limitations of Markovian rewards.

### Strengths
- The paper introduces a framework for hindsight preference learning, with a practical implementation using a VAE architecture.
- I think using the example of a gambling MDP greatly helps in understanding the motivation for using hindsight preference learning.
- Experimental results support the effectiveness of HPL.

### Weaknesses
 - Although I understand the benefits of hindsight preference learning over Markovian rewards, the authors do not clearly position their paper within the broader research on non-Markovian rewards. As mentioned in the related work, both the Preference Transformer and Hindsight PRIOR  assume non-Markovian rewards and consider the full trajectory when calculating rewards. Given this, why does the paper primarily motivate its approach as an improvement over Markovian rewards, despite the existence of several approaches that do not rely on this assumption?
- For example, what is the fundamental difference between this paper and the Hindsight PRIOR paper, as Hindsight PRIOR considers “the importance of a state in a trajectory given that a future state was reached” [1]? Please clarify the novelty of this work in comparison to other hindsight-based PbRL papers.
- The gambling example is very helpful in illustrating the motivation. However, I am concerned that in more stochastic settings, hindsight modeling may introduce noise and add excessive complexity. The ablation study on k, while focusing on a different message, seems to somewhat support this concern.

### Questions
- Why do the segment encoder q, decoder p, and prior f all use the same notation, θ, for their parameters?
- How does the distribution mismatch between Dp and Du cause problems, and how does HPL address this issue (through improved credit assignment) in the main benchmark experiments? Is there any analysis on these tasks other than the example of gambling MDP?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies preference-based reinforcement learning (PbRL). Notably, it proposes to consider human annotations from a holistic perspective; that is the annotations would include the considerations of future outcome instead of in-trajectory information only. Inspired by this mismatch, authors propose to model human preference with hindsight information via a VAE structure, which is further marginalized for rewarding labeling and following RL downstream tasks. Experiments are conducted on annotations from human and scripted teacher and advantageous performance is demonstrated.

### Strengths
**Originality**: The paper studies a very important problem in PbRL: the nature of human annotations, which is inherently more complex than scripted annotations. By proposing a VAE structure with marginalization techniques, this paper a novel and interesting method.


**Quality**: Experiments are conducted on existing human-annotated dataset where the proposed method shows greater performance.


**Clarity**: The paper is well written with illustrative examples, clear text and figures.


**Significance**: The studied problem: the mismatch between annotations and chosen reward models is of very importance and shall be beneficial for the community.

### Weaknesses
The primary concern lies in the **mismatch** between motivation and downstream methods.

The paper aims to incorporate additional future information when learning the $r_{\psi}$. However, actually, the $r_{\psi}$ that takes future information into account should be the Q-function rather than the reward function. Or more rigorously, the $r_{\psi}$ actually encompasses far more information than reward function, but it is not necessarily a Q-function. When downstream algorithms utilize the $r_{\psi}$, the $r_{\psi}$ is considered as reward function, employing a method that does not consider future information.

### Questions
The preference signals on the MetaWorld platform do not actually take into account future information. Why is the algorithm proposed in this paper considered superior?

### Soundness
2

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
3

### Summary
The authors study the problem of offline preference-based RL. One major problem with existing SOTA approaches, as cited by the authors, is the evaluation of trajectory segments from a global perspective, making the obtained reward implicitly dependent on the future part of the segment. The contributions of the paper can be summarized as follows:
- The authors propose HPL, which models human preferences using a reward function conditioned on the state, action, and future trajectory, referred to as hindsight information.
- HPL leverages the trajectory distribution of the unlabeled dataset to learn a prior over future outcomes, providing robust and advantageous rewards during labeling.

### Strengths
- The problem to be solved is clearly specified, and although the approach is simple, it effectively addresses aspects that previous papers have overlooked.
- In the experiments, HPL outperforms the existing SOTA algorithms on most datasets.

### Weaknesses
 - I understand that the use of a gambling MDP in Section 3.1 highlights the importance of this study. However, given the very short trajectory length (two steps) in the example, it remains unclear whether hindsight information was effectively applied to achieve accurate credit assignment using future trajectory information.
- Figure 10 shows that HPL is already 2 to 10 times slower than other models. There seem to be several reasons for this slower speed. 
     - Equation 8 requires summing all steps of each trajectory, which likely takes considerable time.
     - A significant amount of time is spent on sampling in Equation 9.
     - If the running time includes VAE modeling time, it is expected to take even longer.
- The core idea of HPL seems to lie not in using future trajectory to train the model, but rather in the learned VAE that represents the future trajectory. As the authors mentioned, when the future length exceeds a certain threshold, it becomes difficult to accurately represent longer future segments, which lowers HPL's performance. If future information is available, the performance should ideally be more accurate. How might this limitation be addressed?

Minor comments:

- typo on line 403: ''$\hat{P}(s_{good}|s_{1},a_{1})$ and $\hat{P}(s_{good}|s_{1},a_{1})$" -> "$\hat{P}(s_{good}|s_{1},a_{1})$ and $\hat{P}(s_{bad}|s_{1},a_{1})$"

### Questions
In addition to questions about potential weaknesses, I would like to raise a few more questions:
- When computing the reward using the prior distribution, how does the effect depend on the number of samples? (N=20 in appendix)
- What about using both preference data and unlabeled data when training the VAE? Wouldn't this improve the representation across multiple points?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Hindsight Preference Learning (HPL), a novel reward model learning method for offline preference-based reinforcement learning. The authors address the issue of distribution shift between preference-labeled and unlabeled datasets, which can bias the Markovian reward assumption. To tackle this problem, they propose a reward function that is conditioned not only on states and actions but also on future segments. To handle the high-dimensional nature of future segments, the authors employ a conditional VAE to transform them into embedding vectors that better integrate with the reward function. The effectiveness of the method is demonstrated through experiments on Gym-MuJoCo, Adroit, and Meta-World benchmarks, comparing against existing preference-based reinforcement learning algorithms. The results show significant improvements under preference distribution shift, while ablation studies validate the effectiveness of both the VAE and hindsight reward function.

### Strengths
1. The paper addresses a critical challenge in offline preference-based reinforcement learning, presenting well-motivated arguments and clearly illustrating the reward modeling issue through compelling examples.
2. The authors make the insightful observation that human preferences often stem from final outcomes. Their proposed hindsight preference learning leverages future segments to better model these preferences, resulting in a more robust reward function, particularly for datasets with outcome shifts due to multiple modalities or approaches. The integration of conditional VAE makes the algorithm practical for complex tasks like visuomotor policy learning.
3. The experimental evaluation strongly supports the core ideas, encompassing multiple popular benchmarks and competitive baselines. The comprehensive ablation studies examining future segment length, dataset sizes, and reward ensemble provide valuable insights into HPL's advantages.

### Weaknesses
1. The VAE implementation is limited to encoding future segments, whereas it could potentially be extended to data augmentation, prior distribution modeling, and other applications. While the current use of the VAE is effective for its intended purpose, the paper does not explore its potential for generating synthetic future segments. Such an approach could enhance the robustness of the reward model by exposing it to a wider range of possible future outcomes, potentially mitigating overfitting to the training data. Furthermore, the VAE's latent space could be leveraged to model a prior distribution over future segments, which could be useful for tasks with sparse rewards or where exploration is challenging.
2. While the authors focus on "preference distribution shift" between labeled and unlabeled datasets, they assume stability in other distributions. The paper does not adequately address potential shifts in visual appearance, dynamics, and sensor noise - common challenges in real-world datasets. This is a significant limitation, as real-world datasets often exhibit these types of shifts, which can severely impact the performance of reinforcement learning algorithms. For example, changes in lighting conditions or camera angles can alter visual appearances, while variations in the environment or robot hardware can lead to shifts in dynamics and sensor noise. The proposed method does not offer any mechanisms to handle these shifts, which could limit its applicability in practical scenarios.

### Questions
1. The experiments utilize a customized split of the original dataset, using medium-expert quality for the preference dataset and medium quality for the unlabeled dataset. Has there been any evaluation of preference shift on real-world, large-scale datasets?
2. Equation 9 includes the number of samples N in the reward function. How does N influence performance, and what is the practical range for this parameter?
3. The concept of utilizing future segments appears similar to graph search and retrieval-based offline RL methods [1,2]. Could HPL achieve comparable results?
[1] Deyao Zhu, Li Erran Li, and Mohamed Elhoseiny. Value memory graph: A graph-structured world model for offline reinforcement learning. arXiv preprint arXiv:2206.04384, 2022. 
[2] Yin Z H, Abbeel P. Offline Imitation Learning Through Graph Search and Retrieval. arXiv preprint arXiv:2407.15403, 2024.

### Soundness
4

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
This paper introduces Hindsight Preference Learning (HPL), a novel method for offline PbRL. It addresses the shortcomings of existing methods that rely on Markovian reward assumptions, by incorporating future trajectory outcomes in reward learning. HPL uses a variational auto-encoder (VAE) to encode future information and improves credit assignment by considering the future consequences of actions. The authors provide extensive empirical results across a variety of tasks (locomotion and manipulation) and demonstrate that HPL outperforms several state-of-the-art PbRL methods.

### Strengths
1. The paper is clearly written, easy to understand, and provides detailed, well-functioning code.
2. The proposed VAE method incorporates hindsight future information from trajectories into the reward model, which effectively mitigates the reward learning issue caused by the distributional shift between preference data $D_p$ and offline data $D_u$.
3. The experimental performance is impressive, and the ablation studies are thorough.

### Weaknesses
1. The motivation example might be unreasonable: As far as I know, in the same task, $D_u$ is often sampled from $D_p$, so they follow the same marginal distribution. When such an extreme example occurs, it indicates a significant distribution difference between $D_u$ and $D_p$. Although Section 5.3 demonstrates the effectiveness of HPL under distributional shift, this example may lack generality. Specifically, the paper does not clearly define the sampling process for $D_u$ and $D_p$, making it difficult to assess the practical relevance of the distributional shift. It would be beneficial to clarify whether $D_u$ is intended to represent a broader dataset of potentially suboptimal trajectories, or if it is assumed to be a dataset with a similar distribution to $D_p$ but with a much larger size, and how this impacts the interpretation of the results.
2. In fact, this method can be viewed as leveraging the unlabeled dataset to improve the robustness of the reward model. The idea is somewhat similar to previous work [1], which learns the reward model from labeled data and then labels the unlabeled data to enhance offline RL performance. A further theoretical analysis, such as exploring the theoretical performance bounds of learning the hidden dynamics from the unlabeled data in the reward model, would enrich the paper (though this could be very challenging, so it's just a suggestion). The paper lacks a discussion on the potential limitations of relying on the VAE to capture the full complexity of the future trajectory. The VAE's latent space might not fully represent all relevant aspects of the future, which could limit the effectiveness of the proposed method. A discussion of this limitation and potential mitigation strategies would be valuable.
3. In Table 7, the performance of OPPO and CPL is quite poor. Is this mainly because the preference data $D_p$ is too small? The paper does not provide sufficient analysis on why these baselines perform poorly, especially given that CPL is designed for preference-based learning. A more detailed analysis of the failure modes of these baselines would be helpful.
4. In Figure 6c, reducing the size of $D_p$ leads to worse performance. Why is that? The paper should provide a more in-depth analysis of the relationship between the size of $D_p$ and the performance of HPL. It is unclear why a smaller $D_p$ would lead to better results, and this counterintuitive finding needs further investigation.
5. The baselines and ablations lack verification of the core idea of the paper: If the authors aim to verify that the performance improvement comes from the richer environment dynamics provided by the unlabeled data, they should compare with an ablation version where the VAE learns future representations from $D_p$ itself rather than from $D_u$, to further clarify the source of the performance gain. Additionally, in Table 1, a bi-directional transformer version of PT could be used to model future information as another baseline for comparison.

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3
