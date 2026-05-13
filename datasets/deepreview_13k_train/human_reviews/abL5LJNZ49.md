# SCHEMA: State CHangEs MAtter for Procedure Planning in Instructional Videos

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
We study the problem of procedure planning in instructional videos, which aims to make a goal-oriented sequence of action steps given partial visual state observations. The motivation of this problem is to learn a \textit{structured and plannable state and action space}. Recent works succeeded in sequence modeling of \textit{steps} with only sequence-level annotations accessible during training, which overlooked the roles of \textit{states} in the procedures. In this work, we point out that State CHangEs MAtter (SCHEMA) for procedure planning in instructional videos. We aim to establish a more structured state space by investigating the causal relations between steps and states in procedures. Specifically, we explicitly represent each step as state changes and track the state changes in procedures. For step representation, we leveraged the commonsense knowledge in large language models (LLMs) to describe the state changes of steps via our designed chain-of-thought prompting. For state change tracking, we align visual state observations with language state descriptions via cross-modal contrastive learning, and explicitly model the intermediate states of the procedure using LLM-generated state descriptions. Experiments on CrossTask, COIN, and NIV benchmark datasets demonstrate that our proposed SCHEMA model achieves state-of-the-art performance and obtains explainable visualizations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper focuses on the task of procedure planning in instructional videos. Given an initial visual state and a goal visual state as input, the model is tasked with generating a sequence of action steps to form a procedure plan, guiding the progression from the initial visual state to the goal state. The authors highlight the significance of states in these procedures and introduce State CHangEs MAtter (SCHEMA) to model state changes. Specifically, they prompt pre-trained large language models to describe the state changes at each step, enhancing learning the intermediate state and step representations. Then, they use cross-modal contrastive learning to align the visual state observations with language state descriptions. Experiments validate that the proposed method achieves  state-of-the-art performance.

### Strengths
The paper introduces a novel approach to address the task of procedure planning in instructional videos, placing a strong emphasis on state changes and utilizing pre-trained large language models. The motivations and ideas presented in this paper are reasonable.

The proposed method has achieved noticeable performance gains.

### Weaknesses
1. The clarity and composition of the paper could be enhanced. Please refer to the questions below.

2. There has been a notable surge in research exploring the use of pre-trained large language models (LLMs) for video-related tasks, e.g., [1]. This submission aligns with this emerging trend, and its overarching idea is conceptually sound. However, the fairness of the comparisons drawn in the paper could become questionable due to the employment of LLMs. Further in-depth discussion and analysis may be necessary to fully understand the extent of the LLM’s impact on the final results.

### Questions
1. How does aligning visual state observations with language state descriptions *track* state changes? This process involves cross-modal contrastive learning; it is unclear how it could facilitate *tracking* over state changes.

2. Why are step descriptions not utilized as external memory for the step decoder, while *state* descriptions are used instead? The same $D_s$ is employed in Sections 3.3.2 and 3.3.3.

3. In Sec. 3.4, there are $a_i$ and $A_i$. Could you clarify how these two differ and specifically define $A_i$?

4. In State Space Learning via vision-language alignment, is it necessary for the training data to include temporally localized states or actions corresponding to the intermediate states of procedure plans? While I presume the answer is no, Fig. 4(a) and Sec 3.4 leave some room for ambiguity.

5. Why is Eq. (5) called “Masked State Modeling”? The method described does not involve any mask-based modeling or random masking; instead, it is just predicting intermediate locations in a given sequence. The use of the phrase “Masked State/Step Modeling” seems to be an overstatement.

6. What does “DCLIP” refer to in Table 5?

7. Could you also present the results on procedure planning metrics in Table 7?

Missing related literature:

- Li, Zhiheng, Wenjia Geng, Muheng Li, Lei Chen, Yansong Tang, Jiwen Lu, and Jie Zhou. "Skip-Plan: Procedure Planning in Instructional Videos via Condensed Action Space Learning." In Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 10297-10306. 2023.


- Fang, Fen, Yun Liu, Ali Koksal, Qianli Xu, and Joo-Hwee Lim. "Masked Diffusion with Task-awareness for Procedure Planning in Instructional Videos." arXiv preprint arXiv:2309.07409 (2023).

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new framework for procedure planning in instructional videos called SCHEMA, which leverages LLM and cross-modal contrastive learning to track state changes and establish a more structured state space. The authors introduce a chain-of-thought prompting approach to describe state changes and use a mid-state prediction module to improve performance. The SCHEMA model is evaluated on three benchmark instruction video datasets, CrossTask, COIN, and NIV, and achieves state-of-the-art performance in terms of SR, mAcc, and mIoU.

### Strengths
**Originality**: The authors propose a new framework for procedure planning in instructional videos that emphasizes the importance of state changes, which is a novel approach to the problem formation. The use of chain-of-thought prompting to describe state changes is a creative and effective way to leverage language models for this task. The idea of mid-state prediction module is interesting and seems to improve the performance of the model. 

**Quality**: The paper is well-written and well-organized, making it easy to follow and understand. The experiments are thorough and well-designed, with results presented in a clear and concise manner.

**Clarity**: The paper is written in clear language and is easy to understand. The figures and tables are easy to read, providing a clear summary of the results.

**Significance**: The results demonstrate the effectiveness of the proposed approach and suggest that it could be a valuable tool for procedure planning in instructional videos.

### Weaknesses
 * Novelty: While the paper proposes a new framework for procedure planning in instructional videos, some of the individual components of the framework (such as LLM and cross-modal contrastive learning) are not novel in themselves. I personally loathe the trend that LLM+everything -> novelty. Thus I feel that the contribution of this proposed framework is incremental. That being said, I recognize that the authors have done non-trivial work in incorporating these components and perform thorough experiments. 

* Failure cases: The paper does not provide a detailed analysis of the limitations of the proposed approach or potential failure cases. I would be interested in seeing more examples of failures cases and with detailed explanations on why those cases have failed. 

* Scaling up: While the proposed approach shows promising results, the paper does not provide a clear explanation of how it could be applied in real-world scenarios or how it could be scaled up to handle larger datasets. Please note that I do not suggest that the model has to be able to handle larger datasets as long term prediction is hard by nature, but an analysis on the model's potential would be useful. 

* The paper could benefit from more detailed explanations of the experimental setup and methodology, particularly for readers who wish to replicate the experiments. I find it difficult to replicate the model and experiment based on information provided in appendix A/B.

### Questions
* Can you provide more details on the mid-state prediction module? How does it work, and how does it differ from existing mid-state prediction methods?

* Can you provide more examples of failures cases and with detailed explanations on why those cases have failed?

* Can you provide how the model could be scaled up to handle larger datasets?

* Can you provide more detailed explanations of the experimental setup and methodology?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel procedural planning method that models the task elegantly as a joint probability of time-series states and actions conditioned by start and end states. The method fills the gap of ungiven states before and after each action by LLM with a Chain-of-though prompt. Ground truth of actions and the estimated states are used to train the model with reasonable loss functions. Experiments show the clear superiority of the proposed method.

### Strengths
- The motivation is clear.
- The presentation is clear.
- The query design for the state decoder is elegant (a sequence of state vectors, where a known step is the sum of encoded state feature and positional embedding and an unknown step is only positional embedding).
- Augmenting state description with LLM from action labels is novel.
- The reported results are thorough and look promising.

### Weaknesses
1. Overlooked related work

The authors overlook two studies focusing on state transition in instructional videos.

First, in the paragraph "Instructional video analysis," a dense video captioning method [a] is missing. The method tracks material state change with a MemNet-like architecture [a]. It trains state-modifying actions with distant supervision. It also analyzes the state change obtained as a shift in the latent space. Thus, it definitely relates to this work but is missing.

[a] T. Nishimura et al., "State-aware Procedural Video Captioning," ACMMM, 2021.

Similarly, in the same paragraph, the authors claimed, "there are few discussions on state changes in complex videos with several actions, especially instructional videos." However, [b] models such complexity of the instructional video as an action graph to retrieve the goal state image with an instructional text (that directs actions) and an image before the action. The authors adequately refer to this study since the work also tries to model state-action relations in complex instructional videos.

[b] K. Shirai et al., "Visual Recipe Flow: A Dataset for Learning Visual State Changes of Objects with Recipe Flows," COLING2022.

2. Minor flaws in presentation.

The first sentence in 3.3.1 explains about 3.4 but mentions nothing about the content in 3.3.1. This part was confusing for this reviewer.

The paragraph "Masked Step Modeling" in 3.4 claims that "ground-truth answers $a_t$"; however, for the readers, it is not known whether ground-truth actions are given at training or not. Please fix this problem.
 
FYI
In Figure 2, there is a type "oancake." However, it is not clear whether the typo is by GPT-3.5 or the authors.

### Questions
Please point out any factual errors in this review if the authors find them.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new model called SCHEMA for procedure planning in instructional videos. The model leverages language models and cross-modal contrastive learning to track state changes and establish a more structured state space. The authors conduct experiments on three benchmark datasets and show that SCHEMA outperforms existing methods in terms of state recognition accuracy and task success rate. The paper's contributions include a new approach to procedure planning that accounts for state changes, a novel cross-modal contrastive learning framework, and a new benchmark dataset for evaluating procedure planning models.

### Strengths
This paper has several strengths that make it a valuable contribution to the field of procedure planning in instructional videos:  

1. Originality:  

1.1  The paper proposes a new approach to procedure planning that accounts for state changes, which is a novel idea that has not been explored in previous works.  

1.2 The authors leverage language models and cross-modal contrastive learning to track state changes and establish a more structured state space, which is a creative combination of existing ideas.  

2. Quality:  

2.1 The authors conduct experiments on three benchmark datasets and show that SCHEMA outperforms existing methods in terms of state recognition accuracy and task success rate, which demonstrates the quality of their proposed approach.  

2.2 The paper is well-written and well-organized, making it easy to follow and understand.  

3. Clarity:  

3.1 The authors provide clear explanations of their proposed approach and the experiments they conducted, making it easy for readers to understand their contributions.  

3.2 The paper includes helpful visualizations and tables to illustrate their results and comparisons with existing methods.

### Weaknesses
While this paper has several strengths, there are also some weaknesses that could be addressed to improve the work:  

- The paper could benefit from a more detailed discussion of the limitations of the proposed approach. For example, the authors could discuss cases where the model may struggle to recognize state changes or situations where the model may not be applicable.  Specifically, the paper should address the reliance on explicit visual cues for state changes. In many real-world scenarios, state transitions are subtle or implied, not always directly visible. For instance, a change in temperature or the internal state of a mixture might not be visually apparent, yet they are crucial for understanding the procedure. The model's performance under such conditions needs to be thoroughly analyzed and discussed.

- The paper could provide more information on the computational requirements of the proposed approach. It is important to understand the practical feasibility of the model, including the training time, memory usage, and inference speed. This is crucial for assessing the scalability and applicability of the model in real-world applications. The paper should specify the hardware used for training and inference, and provide a detailed analysis of the computational cost associated with each component of the model.

### Questions
1. Could you provide more information on the computational requirements of the proposed approach? Specifically, what hardware and software were used to train and run the model, and how long did it take to train the model? 

2. How does the proposed approach handle cases where the state changes are not explicitly shown in the video? For example, if a video shows a person making a sandwich, but does not show the person adding mayonnaise, how would the model recognize this state change? 

3. Can you provide more information on the limitations of the proposed approach? Specifically, are there any cases where the model may struggle to recognize state changes or situations where the model may not be applicable?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
