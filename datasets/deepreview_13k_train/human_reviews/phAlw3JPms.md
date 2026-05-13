# Tackling Data Corruption in Offline Reinforcement Learning via Sequence Modeling

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Learning policy from offline datasets through offline reinforcement learning (RL) holds promise for scaling data-driven decision-making while avoiding unsafe and costly online interactions. However, real-world data collected from sensors or humans often contains noise and errors, posing a significant challenge for existing offline RL methods, particularly when the real-world data is limited. Our study reveals that prior research focusing on adapting predominant offline RL methods based on temporal difference learning still falls short under data corruption when the dataset is limited. In contrast, we discover that vanilla sequence modeling methods, such as Decision Transformer, exhibit robustness against data corruption, even without specialized modifications. To unlock the full potential of sequence modeling, we propose **R**obust **D**ecision **T**ransformer (**RDT**) by incorporating three simple yet effective robust techniques: embedding dropout to improve the model's robustness against erroneous inputs, Gaussian weighted learning to mitigate the effects of corrupted labels, and iterative data correction to eliminate corrupted data from the source. 
Extensive experiments on MoJoCo, Kitchen, and Adroit tasks demonstrate RDT's superior performance under various data corruption scenarios compared to prior methods. Furthermore, RDT exhibits remarkable robustness in a more challenging setting that combines training-time data corruption with test-time observation perturbations. These results highlight the potential of sequence modeling for learning from noisy or corrupted offline datasets, thereby promoting the reliable application of offline RL in real-world scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The work deals with the challenges posed by data corruption in offline RL and proposes a novel approach RDT. The primary contribution is the application of sequence modeling, specifically through a decision transformer, which has shown greater robustness against corrupted data compared to conventional RL methods that rely on temporal difference learning. The RDT model incorporates three key techniques—embedding dropout, Gaussian weighted learning, and iterative data correction—to enhance robustness. Empirical results indicate that RDT achieves superior performance under various corruption scenarios and provides resilience to both training-time data corruption and testing-time observation perturbations.

### Strengths
- Novel Method: The use of sequence modeling as a robust alternative to traditional temporal-difference-based methods for offline RL under corrupted data conditions is a significant and novel contribution.
- The paper introduces a robust architecture combining embedding dropout, Gaussian weighted learning, and iterative data correction, addressing different aspects of the corruption challenge.
- The experiments are extensive, covering several benchmarks and a variety of corruption scenarios, demonstrating consistent outperformance of RDT over baselines.
- The study highlights the potential of sequence modeling to handle real-world data corruption in offline RL, an area with increasing practical relevance.

### Weaknesses
 -The datasets used are predominantly standard RL benchmarks. Incorporating more complex, real-world datasets could provide stronger support for the robustness claims in real-world applications.

- While the paper corrects actions and rewards through iterative data correction, it leaves out the correction of states, which might impact robustness in tasks with high state complexity.

- The study lacks a detailed comparison with other robust sequence modeling approaches outside of decision transformers, such as those incorporating value functions or other regularization techniques.

### Questions
Could the authors provide more clarity on the choice of dropout probabilities for different embeddings (states, actions, rewards) and its sensitivity to these values? How were these values chosen in the experiments?

The paper states that actions and rewards are corrected iteratively but leaves out state correction. What challenges or limitations prevented state correction? Would the authors consider incorporating state correction as future work, and how would it theoretically affect robustness?

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
This paper focus on invesgating the robustness of offline RL to various data corruption, including states, actions, rewards.  The problem getting more challengable as the dataset is limited. To tackle this problem, the paper proposed Robust Decision Transformer (RDT) by incorporating three effective components, embedding dropout, gaussian weighted learning and iterative data correction. The experiment results demonstrates RDT consistently outperforms the baselines on most tasks under limited corrupt dataset settings.

### Strengths
1. This paper is well-written, and the main idea is easy to follow.
2. The problem setting is interesting, and the proposed method is straightforward, effectively demonstrating its efficiency in handling corrupted, limited datasets.

### Weaknesses
 1. There is no discussion regarding corrupted data at different scales. An analysis of how dataset scale affects the challenges of data corruption would be beneficial.
2. The proposed method is only evaluated on the medium-replay dataset for MuJoCo tasks and the expert dataset for Adroit. A discussion on the impact of corrupted data with varying quality levels is needed.
3. No discussion of the limitations of RDT, which would help in fairly assessing the proposed approach
4. There is a typographical error on line 452: "relocate-exper" should be corrected to "relocate-expert."

### Questions
1. In the gaussian weight learning section, the paper proposes using the exponential form of the prediction loss as a weight for the optimization terms in RDT. This design seems questionable, as early in training, the model is likely to be inaccurate, resulting in high loss values. However, this approach down-weights these losses, potentially reducing gradient information and slowing the learning process. Could the authors provide more intuition behind the design of these weighted terms?
2. Based on the experimental results, RDT appears to provide greater benefits for Adroit tasks compared to the other two task settings. Could you explain the reason for this difference?
3. I reviewed the full dataset results in RIQL, and they seem to conflict with the scores listed in the paper’s appendix. Could you clarify why this discrepancy occurs?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper attacks the problem of learning a policy in an offline RL setting, in the specific case of having access to a lossy dataset, where data can be perturbed. While the literature has focused on algorithms leveraging the Q function to handle this problem, this paper shows that sequence-based models such as the Decision Transformer (DT) perform competitively, and are surprisingly robust compared to baselines when the size of the dataset is significantly reduced. The authors then propose 3 modifications to the DT algorithm that lead to algorithm even more robust than DT. They evaluate the performance of their proposed algorithm in the D4RL benchmark, and perform several ablations to get a better understanding of their method.

### Strengths
This paper has several strengths.
- I found the introduction did a good job of introducing the problem and motivating the research direction. This is particularly true for the introduction, where the overarching research question was clearly stated. Overall, the paper was well written and pleasant to read. The structure of the document is logical and progressively builds the proposed method. The different contributions were mostly clearly presented, using equations when necessary to support the text. Finally, Fig. 2 was a welcome addition to summarize the modifications brought by the algorithm to the DT architecture.
- Offline RL is an important problem, with many applications in the real-world; I think the community benefits of works improving the performance of policies in that setting, and even more since it includes using a new policy architecture. I find it very sensible to wonder how sequence models fare in that setting, especially since their influence and importance in the literature has grown steadily over the past years. The modules to add to the DT are well motivated and sensible (especially the first 2). In addition, the modules seem rather easy to implement, which makes the paper easily applicable.
- I found the paper did a good job at studying comprehensively the use of DT-like methods in the offline RL literature. Several ablations are done to isolate the contribution of the different elements of RDT (Fig. 3 and Fig. 6). Moreover, there is a large variety of additional experiments in the appendix that naturally answered some of my questions as I read the main text, such as the influence of the value of $\zeta$ and $\beta$ (Fig. 10) or the variation of performance for different corruption scale values (Fig. 11).
- The proposed method delivers, as it gets robust performance in the small scale version of the D4RL dataset, improving over the baselines considered (Table 1), sometimes significantly.
- Ultimately, I think the paper asks an interesting question in the use sequence-based methods for robust offline learning. I believe this can generate interesting discussions at the conference around the usage of sequence-based models.

### Weaknesses
There are a couple of axes where I found weaknesses in this work, which I present below.
- Several of the methodological details are pushed to the appendix without being explicitly referred to in the main text. For instance, it is hinted in the main text that the choice of the $\zeta$ parameter (L301) or when the data iterative process starts (L292, “after sufficient training”) is important, but you have to go to the appendix to discover that this information is indeed provided. Adversarial corruption is mentioned quickly (L132) but without giving an intuition about how it would be used in this setting; the action diff perturbation (L426-428) could also have used some intuition (generic is OK) about it before being pushed to the appendix. Overall, I find the authors could make the main text more self-contained by giving the conclusions (maybe broadly) of their different experiments in the main text and referring to the appendix only for the in-depth analysis of the results. Methodological details can be pushed to the appendix, but as the reader goes through the paper, they should know that these details do, in fact, exist.
- While the three proposed additions to DT presented in Sec. 3 make sense, I found their concrete impact on performance difficult to evaluate. For instance, in the ablation of Fig. 6, the addition of the different modules to DT do not drastically change the performance — in fact, in several settings the confidence interval of RDT intersects with the DT(RP). I would be also curious to know how these ablated methods compare with unmodified DT in Fig. 6. Moreover, it seems that different modules contribute more in different settings (ED on action attack, GWL on reward attack …); I think some analysis about which environment should benefit from which module the most, if possible, would have helped framing the modules. The fact that the different ablations of Fig. 6 and 3 are evaluated on different environments also makes it difficult to get a clear sense of the general behavior of each module.
- I find the setting in which this method is expected to perform well to be relatively narrow, as it is mostly valid for datasets that are simultaneously small and corrupted. I do not think this makes this submission less valuable, but it raises questions that I would have liked to see addressed — for instance, what aspect exactly of the low data regime favors sequence models over Q-function based models? Is there any hope for sequence models to overcome Q-function models, even with bigger datasets (especially since transformer models have been shown to work so great in large data regimes)? On this point, while the problem is well-motivated, I found the conclusion that DT worked better than Q-function based models could have used more insights. It is explained at the end of Sec 3.1 (L187-189) but I found these two sentences did not bring much besides repeating the definition of a sequence model. 
- Only RDT has an uncertainty measure in Table 1, and there is no uncertainty measure in Table 2. Moreover, I did not find a description of the nature of the uncertainty measure in the main text.

In addition, I list below other minor weaknesses which did not impact my rating, but that I think could be addressed to improve the document:
- The text of the figures is small and makes reading the paper difficult on paper. (Especially true for Fig. 3 that was very hard to read). It would be useful to increase the size of the captions to make the figure more readable.
- L. 98: “Different from the MDP framework, DT [..]”. I would argue that DT still operates within the MDP framework, it is just a different algorithm to learn a policy.
- L246, Eq 4: you did not define the circle-cross operator. If this is supposed to be an elementwise product, I would argue that this is not the most appropriate symbol ($\odot$ would, I think, be more appropriate). 
- L535: I found the term “exceptional” to be rather out of place.
- Typo: MoJoCo, while it should be MuJoCo (several places).
- Table 1: Lacking information about the meaning of +- in the RDT column. What exact uncertainty measure did you use? 
- In the experiments section, I would refer to the papers that introduced the experiments parameters setting (for example, you set the corruption scale to 1., but unless I am mistaken, we see in the appendix only that this value is set the same as previous works).

### Questions
- In Section 3.2.2, you add a reward prediction term that predicts the immediate reward. Unless I am mistaken, you tested your model on dense reward environments, where such a prediction makes sense and might be more aligned with the environment goal. Do you expect your method to work well in non-dense reward environment? If not, do you think “dense reward signal” should be added as a constraint of your method? 
- In Section 3.2.2 still, what happens at the beginning of training, when all examples are unknown? How do you differentiate corrupted examples from natural ones, when we expect the model’s prediction to be poor for all inputs?
- Section 3.2.3 : Have you tested how frequently your assumption was true? I am curious to know the proportion of times the z score actually detects the perturbed transitions. 
- In Table 1, only RDT gets an uncertainty measure. Why is that? 
- In Figure 3, different environments are chosen to showcase the effects of the elements forming the robust DT method (which are also different from the ones of the ablation in Fig. 6). How were these environments chosen? Why not use the same environment? If there is a difference in behavior of the RDT additions across environments, is there a pattern? 
- In Figure 6, could you add DT without any modification as a baseline?

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
This paper introduces a novel method, the Robust Decision Transformer (RDT), designed to address data corruption in offline reinforcement learning. The study finds that traditional offline reinforcement learning methods based on temporal difference learning perform poorly under data corruption, while the DT, a sequence modeling approach, demonstrates greater robustness in such scenarios. RDT enhances DT’s robustness by incorporating three simple yet effective techniques: embedding dropout, Gaussian-weighted learning, and iterative data correction. Experimental results show that RDT significantly outperforms traditional methods across various tasks in the presence of data corruption, especially in complex scenarios where both training and testing phases are affected by attacks.

### Strengths
1. Innovation: This approach introduces sequence modeling to address data corruption, moving beyond traditional frameworks based on temporal difference learning.
2. Enhanced Robustness: Embedding dropout, Gaussian-weighted learning, and iterative data correction significantly improve the algorithm’s performance under data corruption.
3. Extensive Validation: The method has been validated across various data corruption scenarios and with limited datasets, demonstrating its robustness.
4. High Adaptability: RDT performs exceptionally well in limited data settings, showcasing the potential of sequence modeling across diverse tasks and data conditions.

### Weaknesses
No obvious weaknesses.

### Questions
1. Figure 1 is not as intuitive as it could be; it might be more effective to directly display the performance decline under various attacks.
2. In the ablation study, the current approach is to compare RDT with DT(RP) that incorporates three different improvements. A more rational method would be to compare the performance of RDT with RDT w/o (ED, GWL and IDC).

### Soundness
2

### Presentation
3

### Contribution
2
