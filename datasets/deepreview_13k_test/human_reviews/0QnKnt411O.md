# Unsupervised Zero-Shot Reinforcement Learning via Dual-Value Forward-Backward Representation

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Online unsupervised reinforcement learning (URL) can discover diverse skills via reward-free pre-training and exhibits impressive downstream task adaptation abilities through further fine-tuning.
However, online URL methods face challenges in achieving zero-shot generalization, i.e., directly applying pre-trained policies to downstream tasks without additional planning or learning.
In this paper, we propose a novel Dual-Value Forward-Backward representation (DVFB) framework with a contrastive entropy intrinsic reward to achieve both zero-shot generalization and fine-tuning adaptation in online URL.
On the one hand, we demonstrate that poor exploration in forward-backward representations can lead to limited data diversity in online URL, impairing successor measures, and ultimately constraining generalization ability.
To address this issue, the DVFB framework learns successor measures through a skill value function while promoting data diversity through an exploration value function, thus enabling zero-shot generalization.
On the other hand, and somewhat surprisingly, by employing a straightforward dual-value fine-tuning scheme combined with a reward mapping technique, the pre-trained policy further enhances its performance through fine-tuning on downstream tasks, building on its zero-shot performance.
Through extensive multi-task generalization experiments, DVFB demonstrates both superior zero-shot generalization (outperforming on all 12 tasks) and fine-tuning adaptation (leading on 10 out of 12 tasks) abilities, surpassing state-of-the-art URL methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work presented a pre-training framework for zero-shot reinforcement learning by leveraging forward-backward (FB) representation. Unlike some previous study on zero-shot RL, this work analysed the performance gap of FB in the online learning setting compared with a specific exploration strategy. The authors then proposed a new exploration reward based on contrastive learning and incorporated this into FB traning by end-to-end online learning. The proposed method is evaluated in zero-shot online URL and fine tuning settings. Experimental results suggest that it achieved improved performance than some baseline methods given limited interactions.

### Strengths
This work is well motivated and the promotion of exploratory behaviour during the pre-training phase to increase the data coverage is reasonable.

The paper is well written and easy to follow.

### Weaknesses
The major contribution in this work is the combination of an exploration reward with FB learning, where the technical novelty is limited.

Although the performance gain shown in Table 1 looks strong, I have concern on the baselines used in comparison for this setting. It is unclear why these are suitable baselines here for the problem of zero-shot online URL. Many baselines here are either not designed for online learning with self-generated trajectory (for example, LRA-SR used in (Touati et al., 2023)) or not zero-shot testing (if I’m not mistaken some baseline finetunes longer steps, for example, CeSD with 100k interactions rather than 1e^4 used in this work). So it does not look so exciting when explicit exploration techniques are used in combination with a zero-shot technique. A naive approach for this problem would be using a method of pure exploration (e.g. r_{ce} proposed in this work as the proposed intrinsic reward itself has the capability to collect an offline dataset.) or a method of skill discovery to collect an offline dataset with better data coverage than FB, then training FB on top of this dataset and testing its ability in zero-shot generalisation. This could probably better demonstrate the advantage of combining exploration reward with FB in online URL.

Following the previous comment, for Table 1, it would be better to group the baselines into several categories so that it is clear from the table which property (zero-shot, online, offline,  exploration or skill discovery) each method has or does not have.

There is no theoretical analysis to support the proposed objective function and reward function either in the FB pre-training stage or fine-tuning stage. It is unclear what guarantee of zero-shot generalisation of the proposed method can have.

Questions and suggestions:

For Fig. 2 and Fig. 3, Please add more descriptions to the caption so that the reader can understand the main discovery and meaning of the figure.

### Questions
Please see the weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work introduces the Dual-Value Forward-Backward (DVFB) representation framework for unsupervised reinforcement learning (URL). It tackles the challenge of enabling agents to generalise to new tasks without further training (zero-shot generalisation) in addition to fine-tuning adaptation in online settings.

It builds on successor representation (SR)-based approaches which aim to learn a representation of expected future states and have been shown to aid zero-shot generalisation in RL. In particular, the work extends forward-backward (FB) representations by learning both forward and backward dynamics. The authors explore failures in FB-based approaches in online URL settings and find that it is due to inadequate exploration. They address this by introducing an intrinsic reward based on contrastive learning to encourage exploration, combining this “exploration value” function to the usual “skill value” function to arrive at their DVFB. The authors also introduce a fine-tuning scheme using a reward mapping technique to add further online adaptation capabilities to their method. 

The authors validate DVFB across twelve robot control tasks in the DeepMind Control Suite and demonstrate the approach gives both superior zero-shot and fine-tuning performance.

### Strengths
- Zero-shot generalisation in online settings is an important problem in RL, where progress is going to be essential for successfully deploying RL in real-world applications. DVFB advances the field's understanding of how to create agents that can solve and adapt to new tasks immediately, without requiring extensive retraining. 
 - The authors build on foundational concepts in the field such as SR and FB representations. The paper does a good job identifying the limitations of FB in online settings, pinpointing insufficient exploration as a core issue, and using their insights to justify the extensions of FB into DVFB. The introduction of a novel exploration value function alongside the skill value function is an original approach that enhances exploration and, as shown in their motivation and results, improves generalisation. Furthermore, the addition of a reward mapping is a valuable addition that enables them to demonstrate both zero-shot generalisation and fine-tuning in an online setting.
 - Impressive results: the paper presents rigorous experiments across 12 diverse control tasks in a widely used benchmark for tasks requiring fine-grained motor control. In terms of zero-shot performance, their method outperforms baseline methods across the 12 tasks, particularly in tasks where others struggle with exploration (further supporting their motivation). It also outperforms on fine-tuning performance, showing faster adaptation and greater stability compared to the state-of-the art in URL.
 - The paper is well written, guiding the reader through the problem being addressed, relevant related work, the motivations for their extensions, implementation, results and conclusions. The methodology section is nicely laid out, with clear explanations and schematics detailing components of the model. Their experimental results are clearly presented and easy to understand.

### Weaknesses
- Potential for broader applicability: the paper focuses on tasks in the DeepMind Control Suite. This demonstrates DVFB’s capability in robotic control tasks, but leaves one wondering about the framework's versatility which otherwise seems very general. Could the authors discuss the potential for adapting DVFB to other domains, such as navigation? If possible, preliminary results or  discussion on expected performance in different contexts would broaden the scope of the work.
 - Other intrinsic rewards: the paper attributes improvements to enhanced exploration, but it doesn’t delve into specific advantages that contrastive entropy is providing over other intrinsic rewards. Going beyond the DVFV w/o CE ablation experiment and trying out other intrinsic rewards (beyond just RND rewards) could add further insight into their particular choice of contrastive entropy.
 - Sparse presentation of reward mapping technique: there’s limited detail and justification for the reward mapping technique. It’s unclear whether this particular mapping method is optimal or if other strategies might perform equally well or even better in different tasks.  Further exploration would clarify its effectiveness and limitations. Could the authors discuss more justification for this approach, as well as analysing some alternatives? 
 - Reproducibility: lack of code to reproduce the results: providing code would significantly enhance the paper’s accessibility. While the inclusion of pseudocode and hyperparameters is appreciated and provides important details for the method, the absence of actual code makes it challenging for others to fully replicate the experiments or apply the DVFB framework to other settings.

### Questions
Reflecting the weaknesses discussed above, my key questions are:
 - How broadly applicable is the method, particularly beyond robotic control tasks? Are there any preliminary results in other domains that the authors could include?
 - How important is their particular choice of reward to encourage exploration -- the contrastive entropy reward? How well would other rewards stand-in for this, or is it particularly well suited?
 - Similar questions for the reward mapping technique. Could we see more justification for their approach and other alternatives explored?
 - Can the authors provide code so that others can directly reproduce the results?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The study presents the Dual-Value Forward-Backward (DVFB) framework for zero-shot generalization in online unsupervised reinforcement learning (URL). DVFB integrates a skill value function with an exploration value function to enhance data diversity and generalization in the absence of task-specific rewards. It utilizes a contrastive entropy intrinsic reward to improve exploration and a dual-value fine-tuning method to optimize downstream task performance, claiming good results in continuous control tasks.

### Strengths
1. The research presents a novel Dual-Value Forward-Backward (DVFB) paradigm that integrates skill and exploratory value functions to improve data variety and zero-shot generalization in online URL, providing an innovative method for reward-free learning.

2. Should the suggested DVFB approach demonstrate efficacy, it may rectify a basic constraint in reinforcement learning by facilitating zero-shot generalization absent task-specific incentives, hence potentially enabling RL agents to adapt more readily to varied real-world contexts.

### Weaknesses
1. The experimental configuration and illustrations are challenging to interpret, with scant explanation offered for particular measures and comparisons. Enhanced labeling, elucidation of axes and benchmarks, and uniform layout throughout figures would facilitate comprehension of the data and augment the paper's readability. Figure 6 has mixed x-axis labels, which needs an improvement. Legends can be bigger w/o affecting the size of total figure for example Figure 7. 

2. The method depends on several essential network hyperparameters given in Table-3 yet the research fails to analyze the sensitivity of the results to these selections. An investigation of network hyperparameter sensitivity would enhance confidence in the robustness and generalizability of the findings.

3.The implementation and/or utilization of the reward mapping technique for fine-tuning can be clarified. Integrating pseudocode would improve the accessibility and reproducibility of this component.

4. The report omits a discussion of potential limitations, including computing cost, scalability, and difficulty in real-world implementation. Recognizing these factors might yield a more equitable viewpoint and inform subsequent research.

### Questions
1. Could you furnish more detailed explanations regarding the metrics employed in the studies, especially for figures where the axes and comparisons lack clarity? Supplementary labeling and contextual information would assist readers in appropriately interpreting your findings.

2. What is the performance of DVFB in relation to other contemporary zero-shot generalization methods, and what are the reasons for the selection or exclusion of specific baselines? Incorporating a broader array of comparisons or elaborating on these selections would bolster the assertion of enhanced performance.

3. Could you provide a detailed explanation of the practical execution of the reward mapping technique, possibly including pseudocode? Additional detail would elucidate this component's impact during fine-tuning.

4. In what manner does the contrastive entropy reward facilitate skill differentiation, and can you present empirical data that substantiates its efficacy? An elucidation or ablation of the role of this reward would improve comprehension.

5. Have you performed any analysis to assess the sensitivity of DVFB to essential hyperparameters? This would be beneficial to evaluate the resilience of the framework across diverse contexts and circumstances.

6. Could you elaborate on the possible limits of DVFB, including computational complexity and scalability in practical applications? Considering these criteria would yield a more equitable perspective on the approach's practical viability.

### Soundness
3

### Presentation
3

### Contribution
3
