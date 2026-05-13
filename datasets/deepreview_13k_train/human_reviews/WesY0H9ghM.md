# Uni-RLHF: Universal Platform and Benchmark Suite for Reinforcement Learning with Diverse Human Feedback

- Decision: Accept
- Scores: 8, 6, 5

## Abstract
Reinforcement Learning with Human Feedback~(RLHF) has received significant attention for performing tasks without the need for costly manual reward design by aligning human preferences. It is crucial to consider diverse human feedback types and various learning methods in different environments. However, quantifying progress in RLHF with diverse feedback is challenging due to the lack of standardized annotation platforms and widely used unified benchmarks. To bridge this gap, we introduce \textbf{\alg}, a comprehensive system implementation tailored for RLHF. It aims to provide a complete workflow from \textit{real human feedback}, fostering progress in the development of practical problems. \alg contains three packages: 1) a universal multi-feedback annotation platform, 2) large-scale crowdsourced feedback datasets, and 3) modular offline RLHF baseline implementations. \alg develops a user-friendly annotation interface tailored to various feedback types, compatible with a wide range of mainstream RL environments. We then establish a systematic pipeline of crowdsourced annotations, resulting in large-scale annotated datasets comprising more than 15 million steps across 30 popular tasks. Through extensive experiments, the results in the collected datasets demonstrate competitive performance compared to those from well-designed manual rewards. We evaluate various design choices and offer insights into their strengths and potential areas of improvement. We wish to build valuable open-source platforms, datasets, and baselines to facilitate the development of more robust and reliable RLHF solutions based on realistic human feedback. The website is available at \url{https://uni-rlhf.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a new framework to collect human feedback for RLHF. The framework allows for five different types of feedback to be collected with a convenient user interface, depending on the task at hand. A dataset of feedback of three of these types is collected using crowdsourced human workers. This dataset is then used to evaluate multiple existing offline RLHF approaches, where a trained reward model is used to label trajectories from a dataset, and then an offline RL algorithm is used to produce a policy. The evaluation shows that the collected data for comparative and attribute feedback is of good quality, and allows for the learned policy to perform at a quality comparable to a policy trained from hand-crafted reward models. In some cases the policies trained from human feedback outperform those trained from hand-crafted reward models.

### Strengths
In my view, the main strength of the paper is the open-sourced dataset and the tool for feedback collection. These will bring great value to the community and allow for easy benchmarking of offline RLHF methods. The extensive evaluation on D4RL is another strong point of the paper. It will provide a reasonable baseline for future offline RLHF approaches. Finally, the dataset with collected attribute feedback can be used for multi-objective learning, an area where fewer datasets in general are available.

### Weaknesses
- The claim for a "standardized feedback encoding format along with corresponding training methodologies" in Section 3.2 might be overly ambitious. Most importantly, the training methodologies are only provided in the appendix for two out of the five feedback types. Comparative feedback interface also does not allow the user to indicate the strength of preference, as done e.g. in the Anthropic's dataset for language model alignment [1]. The extension of the methodology in Appendix E.1 to this type seems straightforward (introduce y=(0.75,0.25), for example), and it could be beneficial to mention this.
- Related to the previous point, the paper provides too few details on the way Atari experiments were performed. Appendix G and Section 4.1.1 imply that comparative feedback was collected, but Figure 5 (d) in the appendix -- that visual feedback was used instead. The highlighting in Table 8 should be explained. My guess is that the best of the ST and CS labels is highlighted.
- There is no dataset or benchmarking for evaluative feedback, hence it is hard to assess the usefulness of this part of the system. It is unclear whether data for keypoint and visual feedback on the Atari environments was collected. I believe that the datasets for comparative and attributive feedback are already a good enough contribution, and an interface for other feedback types is a nice-to-have extra, so this point does not make me give this paper a negative rating.
- Star annotations in Table 2 are incomplete. As I understand it, higher is better in the entire table. If that is the case, stars that should mark that the method performs better than the oracle are missing in several places: (hopper-m, CQL, CS-TFM), or (antmaze-u-d, IQL, CS-MLP). There are more missing stars in the table.
- Blue annotations in Table 2 are also significantly wrong, if I understand them correctly. Blue should mark the methods where crowdsourced labels (CS) show better results than the synthetic labels (ST) for the corresponding method. Then, for example, (walker2d-m-r, IQL, CS-MLP) should not be colored in blue, since (walker2d-m-l, IQL, ST-MLP) shows a better score (109.8 > 109.4). I counted 10 instances of such mislabeling in the IQL group alone. This is especially important since the paper claims that "the performance of models trained using crowd-sourced labels (CS) tends to slightly outperform those trained with synthetic labels (ST) in most environments, with significant improvements observed in some cases." Once the blue labels are revised, it is questionable whether this claim still holds. Other offline RL approaches (CQL and TD3BC) show that CS labels are better more consistently, but these approaches perform worse than IQL, so the results for them are correspondingly less important.
- Some CS-TFM results are missing from Table 2. I did not find the explanation for this, maybe I missed it? It would be helpful to see these results in the final version, to better assess the claim of the paper that "CS-TFM exhibits superior stability and average performance compared to CS-MLP".
- For the SMARTS experiment in Section 4.1.2, the paper claims that "the best experimental performance can be obtained simply by crowdsourcing annotations, compared to carefully designed reward functions or scripted teachers." I would say that from the three tasks used one cannot conclude that carefully designed rewards perform worse than crowdsourced annotations. In table 3, the former outperforms the latter on two out of three methods. The claim seems to be made based on average success rate, which only differs by 0.01, less than one standard deviation.
- In Figure 4, speed and torso height are plotted against time. Every 200 steps, the speed attribute value changes (1 to 0.1 and back), so we see the respective changes in speed on the first plot. The relative strength of the "torso height" attribute, however, does not change (stays at 0.1), and the torso height parameters do not change much between the changes. It would be more interesting to see the results where the strength of torso height also changes, so that we can see that it influences the plot.
- Generally speaking, RLHF is most useful in domains where only the humans understand the true reward. This is the case, for example, with "helpfulness" of an LLM, or with "humanness" of the gait of a walking robot. An important evaluation, then, is to see whether the human evaluators prefer the policies trained with an RLHF approach in terms of these hard-to-define measures. This paper, however, does not present such an evaluation. "Humanness" comparisons are collected as shown in Section 4.2, but it is never compared to a policy that is trained without taking humanness into account.

### Questions
- In table 2, the results are normalized against an "expert", as the formula in the beginning of Section 4.1.1 shows. How is the expert trained? It is interesting that some of the methods in the table outperform the expert.
- I found the attribute training model in Appendix E.2 confusing. The learned log-preferences $\hat{\zeta}^\alpha$ in eq. (7) probably also need the subscript $\theta$.  The relative strengths of attributes $v^\alpha_{opt}$ are provided as hyperparameters. These strengths are in $[0,1]$. Why, then, in eq. (7) the attributes are checked for being close to $\hat{\zeta}^\alpha$, which is supposed to become the probability of preference according to the respective attribute only after the softmax operation (5)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Uni-RLHF is a comprehensive system for reinforcement learning with diverse human feedback. It includes an Enhanced-RLHF platform that supports multiple feedback types, environments, and parallel user annotations, along with a feedback standard encoding format. The system also provides large-scale datasets, offline RLHF baselines, and human feedback datasets for relabeling and human-aligned reward models.

### Strengths
1. Uni-RLHF provides a universal platform for RLHF that supports multiple feedback types, environments, and parallel user annotations. The system includes a feedback standard encoding format that facilitates the integration of diverse feedback types.
2. Uni-RLHF provides large-scale datasets and offline RLHF baselines for evaluating the performance of RL algorithms with human feedback. The system also includes human feedback datasets for relabeling and human-aligned reward models, which can improve the efficiency and effectiveness of RLHF.
3. Uni-RLHF can foster progress in the development of practical problems in RLHF by providing a complete workflow from real human feedback.

### Weaknesses
1. Uni-RLHF's large-scale crowdsourced feedback datasets may contain noise and bias, which can affect the performance of RL algorithms trained on these datasets. The potential for annotator bias, where certain preferences or interpretations skew the feedback, is a significant concern. Additionally, the inherent variability in human judgment can introduce inconsistencies in the data, making it difficult for RL algorithms to learn robust policies. The lack of a standardized quality control mechanism for the crowdsourced data raises questions about the reliability of the feedback.
2.  The system's offline RLHF baselines may not be optimized for specific applications, which can limit their usefulness in practical settings. The provided baselines may not adequately address the nuances of different RL tasks, potentially leading to suboptimal performance when applied to real-world scenarios. The absence of task-specific tuning or adaptation of the baselines could hinder their effectiveness in diverse application domains. Furthermore, the baselines may not account for the unique characteristics of different environments, limiting their generalizability.
3. The system's reliance on human feedback may introduce additional costs and delays in the RL development process, compared to purely synthetic feedback. The process of collecting and processing human feedback is inherently time-consuming and resource-intensive, which can slow down the development cycle. The need for human annotators also introduces financial costs, which may be prohibitive for some research groups or applications. The reliance on human feedback also makes the system less scalable compared to methods that rely on synthetic feedback.

### Questions
Please refer to weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work introduces Uni-RLHF, an eco-system for Reinforcement Learning with Human Feedback to facilitate the data collection with human annotators, the sharing of datasets and the RL alignment.
In particular, the annotation platform named Enhanced-RLHF supports various feedback types.
Then, the paper investigates different offline RL strategies, and show that the reward models trained on their crowdsourcing labels lead to better performances than when using synthetic labels, and can approximate the Oracle rewards. This is done on motion control/manipulation tasks such as D4RL or Atari or Smarts. They aim for fair evaluation of RLHF strategies.

### Strengths
- The work effectively succesfully presents a comprehensive system to deal with the data collection process with diverse human feedback types.
- The motivation is clear and interesting: indeed, RLHF appears nowadays as a go-to strategy to ensure the reliability of AI systems. Therefore the proposed eco-system can be of interest to some researchers.
- Crowdsourced labels are sufficient to approximate Oracle-based reward, showing the flexibility of RLHF even in those D4RL datasets.

### Weaknesses
 - The main weakness is the limitation to control/locomotion tasks. More real world tasks/other modalities (such as text), and also larger architectures are required to make this eco-system more attractive.
- The benchmark only compares offline RL, thus for example the de facto online strategy for RLHF (PPO) is not ablated.
- The different query samplers are not ablated.
- Only the comparative feedback is ablated. It would have been interested to compare the quality of the reward models.
- While the authors do acknowledge this, providing a data cleaning procedure (or data filters) in the eco-system would be very positive to foster its applicability.

### Questions
- could you please clarify the differences with RLHF-Blender ? in which case we should use one or the other ?
- How did you select the hyperparameters?
- Have you applied any strategy to refine the dataset quality?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
