# DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agent

- Decision: Accept
- Scores: 6, 5, 8, 8

## Abstract
On-device control agents, especially on mobile devices, are responsible for operating mobile devices to fulfill users' requests, enabling seamless and intuitive interactions. Integrating Multimodal Large Language Models (MLLMs) into these agents enhances their ability to understand and execute complex commands, thereby improving user experience. However, fine-tuning MLLMs for on-device control presents significant challenges due to limited data availability and inefficient online training processes. This paper introduces \textsc{DistRL}, a novel framework designed to enhance the efficiency of online RL fine-tuning for mobile device control agents. \textsc{DistRL} employs centralized training and decentralized data acquisition to ensure efficient fine-tuning in the context of dynamic online interactions. Additionally, the framework is backed by our tailor-made RL algorithm, which effectively balances exploration with the prioritized utilization of collected data to ensure stable and robust training. Our experiments show that, on average, \textsc{DistRL} delivers a \textbf{3$\times$} improvement in training efficiency and enables training data collection \textbf{2.4$\times$} faster than the leading synchronous multi-machine methods. Notably, after training, \textsc{DistRL} achieves a \textbf{20\%} relative improvement in success rate compared to state-of-the-art methods on general Android tasks from an open benchmark, significantly outperforming existing approaches while maintaining the same training time. These results validate \textsc{DistRL} as a scalable and efficient solution, offering substantial improvements in both training efficiency and agent performance for real-world, in-the-wild device control tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents DistRL, an asynchronous distributed reinforcement learning framework designed explicitly for on-device control agents in mobile environments. DistRL aims to optimize training efficiency and agent performance for complex tasks, leveraging centralized training with decentralized data acquisition. By introducing a unique off-policy algorithm, A-RIDE, DistRL effectively manages asynchronous data collection and prioritizes valuable interactions, addressing challenges like delayed updates and non-stationary data. Experiments demonstrate its significant performance and efficiency improvements over existing frameworks, especially for real-world mobile tasks, positioning DistRL as a scalable solution in distributed reinforcement learning for mobile devices.

### Strengths
- DistRL employs a decoupled architecture that enhances scalability and robustness by distributing data acquisition across heterogeneous mobile devices, making it efficient for large-scale deployment. Moreover, they propose an A-RIDE algorithm adapted for asynchronous environments, balancing exploration and stability, which improves sample efficiency and task success rates.
- The paper provides comprehensive experiment results that significantly outperform baselines, showcasing superior success rates in complex tasks. Ablation studies highlight the importance of its components, like DPER and retrace correction.
- The paper is well-written and easy to follow.

### Weaknesses
 - Lots of hyperparameters are required. (e.g., Equation 1, 2, DPER). Do you have any tips or evidence for determining them, and are the values sensitive to different types of environments?
- Although the experiments cover general tasks, expanding the testing to a broader range of mobile applications would offer more substantial evidence of DistRL’s adaptability. (from additional tasks from AITW and AndroidWorld)
- Is VLM Evaluator (Gemini)'s performance in providing reward signals credible? Did you encounter any failure cases where VLM misleadingly provides success/failure signals? AndroidWorld provides manually defined dense rewards. Have you tried training DistRL with such a reward?
- While the asynchronous design improves adaptability, more detail on DistRL's response to drastic changes in mobile environments or new, unseen tasks would strengthen the discussion of its robustness in dynamic settings.

### Questions
- Any results from INSTALL and GOOGLEAPPS of AITW? / Why not compare results in AndroidWorld tasks?
- In real-world cases, many users (workers) have different types of devices and different OS versions. How does DistRL handle scenarios where the mobile device encounters significant UI changes or unexpected app updates during training?
- What are the trade-offs between computational overhead and empirical performance (success rate) when using more environments (workers) and Distributed Prioritized Experience Replay (DPER)?
- Could the framework be adapted for other operating systems, such as iOS, and if so, what modifications would be necessary?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces DistRL, an asynchronous distributed reinforcement learning (RL) framework designed to fine-tune on-device control agents, particularly for mobile environments. The key contributions include a scalable architecture that decouples data acquisition from policy learning, improving training efficiency and robustness in dynamic environments. The paper claims significant improvements in training speed and success rates compared to state-of-the-art methods, validated through experiments on Android tasks.

### Strengths
1. The decoupling of data acquisition from policy learning allows the framework to handle heterogeneous devices efficiently, which is crucial for real-world applications.
2. The asynchronous nature of DistRL enables faster data collection and policy updates compared to synchronous methods, which is demonstrated by a claimed 3x improvement in training speed.
3. The focus on mobile device control agents addresses a practical problem with significant industry relevance, particularly in automating complex user interactions on smartphones.

### Weaknesses
1.  There is a significant discrepancy between the model descriptions in different sections (T5-based multimodal model mentioned in Sec 1 vs GPT-2/ROBERTA in A.5.1). This inconsistency undermines the paper’s credibility and makes it difficult to understand what model was actually used. If different models were used for different tasks or components (e.g., policy learning vs critic evaluation), the authors should explain why and provide a rationale for these choices. If there were intentional changes in model usage (e.g., using GPT-2 for policy learning and ROBERTA for critic evaluation), the authors should explain why these variations were necessary and how they impacted performance. The lack of clarity regarding the specific model architecture and its components makes it challenging to assess the validity of the experimental results. For example, it is unclear if the encoder and decoder components of the T5 model were initialized with pre-trained weights, and if so, from which models. This lack of detail makes it difficult to reproduce the results and understand the contribution of the proposed method.

2. It is unclear how the proposed method differs from IMPALA from the methodology perspective. I understand that applying them to a new on-device setting is trivial, but it is confusing to me what are the major differences from the algorithm side. It seems that A-RIDE builds upon existing methods like Retrace and GAE but does not introduce substantial innovations beyond adapting these techniques to a distributed setting. Additionally, the author mentioned in Sec. 2.3 that:
> Furthermore, we develop a novel reinforcement learning algorithm specifically designed to handle the stochasticity and scalability inherent in mobile device environments.
However, I did not see any specific techniques and algorithm improvements that address the stochasticity and scalability issues. If there are indeed major algorithm changes, it would be beneficial to add a baseline of IMPALA and IMPACT. The paper needs to clearly articulate the algorithmic differences from existing methods, especially in how it addresses the unique challenges of mobile environments, such as stochasticity and limited resources. The lack of a direct comparison with IMPALA and IMPACT makes it difficult to assess the novelty and effectiveness of the proposed approach.

3.  Additionally, the training and testing set used are not clearly described. I am a bit confused about the difference between the training and testing sets -- are there overlaps of tasks between them? How is the expert-curated and AndroidWorld training set selected? This questions the generalization issues of the experiments. The paper should provide a detailed description of the training and testing datasets, including the number of tasks, the complexity of the tasks, and how they were selected. The lack of clarity regarding the dataset construction makes it difficult to assess the generalizability of the results. It is important to understand if the training and testing sets are sufficiently diverse to evaluate the performance of the proposed method in real-world scenarios.

4. The evaluation metrics and result plots are a bit confusing. It is unclear whether the plots in Fig. 6 are for the training task success rate or the testing task's. Additionally, adding the testing task success rate plots instead of just training one in Fig. 5 would be beneficial as well. The paper should clearly specify the evaluation metrics used and provide separate plots for training and testing performance. The lack of clarity in the evaluation metrics and plots makes it difficult to understand the actual performance of the proposed method.

5. The x-axis in Fig. 5 (a) is the time. From Fig. 5 (c) we can see there are significantly more trajectories collected than baselines. I acknowledge that the implementations of the proposed method is much more efficient than baselines, but I am also curious about what the plot looks like if the x-axis is the trajectory-num or the step-num, which is commonly reported in the RL literature. It would be super helpful to understand the upper bounds of the baseline algorithms given the same number of collected data. It is also interesting to know the synchronized algorithm performance trend.

### Questions
See weakness

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper provides a way to train device control agents using reinforcement learning. Specifically, it proposes a setup of asynchronous data collection using parallelized data collection on emulators (or real devices), combined with a centralized learning algorithm. The algorithm for training is V-trace, combined with prioritized replay buffer and an additional component encouraging exploration. The system runs on multiple workers and uses a single host learner.

The paper evaluates results on AitW using model-based evaluation. Compared to existing literature/SoTA the DistRL approach achieves a high success rate in less wall time by applying a distributed, asynchronous training approach, which results in faster emulation speed (traj/min). In the General test set, DistRL achieves a success rate a relative improvement of over 19% vs previous work (DigiRL) in the Web Shopping test set, DistRL attains a success rate  outperforming DigiRL by over 14%. The work conducts ablation analysis.

### Strengths
The work achieves impressive results on a challenging task. It provides a path to scale up data collection and enable future work to tackle even more complex problems. Implementing this distributed setup and making it work is a valuable contribution. This work is particularly relevant to future researchers where researchers can easily spin up many workers on cloud platforms. 

The paper is well-written, with technical depth and there are enough details describing the methodology and approach. The paper does a good job of comparing their results to existing works and agents.

It is good the authors run multiple experiments per and average the results to provide more stable results. It is also good that the work includes an ablation study.

### Weaknesses
In order for this work to be a major contribution, I feel it should be open-sourced since a core contribution is the engineering work around centralized training and decentralized data acquisition, which requires complex communication between different systems. Open-sourcing will greatly help the community to take advantage of the contributions here and with reproducibility.

The core RL techniques used are relatively standard. There's no fundamental advance in machine learning theory or methodology. However combining IMPALA with prioritized experience replay seems to be novel, and it’s implementation is highly non-trivial.

If both DigiRL (single) and DigiRL (multi) have the same amount of emulators, why are the performance numbers between them different? Ultimately, both consist of 32 emulators, if I understand correctly, operating with synchronous training. Please clarify how they are different and why it's relevant to include both. I also think the number of emulators should be displayed more prominently as a key experimental parameter (rather than only in Figure 5)

Spelling/Writing: "ensuring that only contextually appropriate actions are penalized". I believe this should be “inappropriate actions are penalized”?

### Questions
“The evaluator receives the current observation, composed of the task description and a screenshot of the device, and outputs a reward signal.” – Have the authors validated that this does a good enough job of success validation, versus, say using the entire trajectory?

To me, “On-device End-to-End Agent Performance Evaluation” implies that the inference is done on the device, but this appears not to be the case. I understand it could be done in theory because the model is small enough, but it’s not actually on device as far as I can tell. Is there another way to describe it?

## Comments
(You don’t have to address these; they are intended to be helpful only.)

For future work, you may consider SeedRL to further scale the approach. https://arxiv.org/pdf/1910.06591#page=5.27

Future work could evaluate on online benchmarks such as AndroidWorld to ensure that results are easily comparable for future researchers, since model-based evaluation is harder to reproduce due to costs and because of differences in model outputs, even for the same base model.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper focuses on the domain of on-device control agents and presents DistRL, an asynchronous distributed reinforcement learning framework for device control agents. This paper designs a centralized training and decentralized data acquisition system design to ensure the efficiency of online RL fine-tuning given potentially heterogenous hardware specifications. It also proposes a tailor-made RL algorithm in the context of distributed device control training. Both the system design and new RL algorithm shows improvements over the prior state-of-the-art DigiRL in a popular device-control benchmark AitW.

### Strengths
The paper addresses a realistic concern of asynchronomous data collection in applying RL fine-tuning for device-control agents, so it is highly relevant. 

The proposed system-level optimizations can be valuable to the open-source community. I hope the authors can clean up and release the infrastructure for their experiments.

The proposed RL algorithm and system design seems to make a difference on popular AitW benchmark.

### Weaknesses
The writing of the paper, in particular the introduction and methodology, can be improved. In fact, the current state of writing has caused me trouble for understanding the contributions of the paper. A significant amount of re-writing is required before the paper can be published in a top-tier venue like ICLR. Please see my questions for more details.

The organization of the section 5 methodology makes it hard to understand what parts are novel in the paper and what parts are adapted from existing literature. From the current writing, it seems to be a combination of existing components from the prior literature. Additional motivations are needed to explain what is novel in the tailor-made RL algorithm.

Line 53-70 seems repetitive.

Line 71 fine-tuning(type of light training) -> fine-tuning

Paragrapho one and two of intro seem to be a bit verbose in introducing the background.

Line 78-85, it seems unnecessary to introduce the notion of RLHF here cuz this paper does not have human preferences.

Line 86-90 is confusing, it seems to describe challenges of exisiting offline datasets such as AitW and Android-Control, but why is it relevant for online RL fine-tuning?

Line 98-104 can be best put in the related works.

There are too many bolded text in the introduction that can tire the readers. I would suggest removing the bold font for related methods. Same applies to the experiment section.

Line 121-122, te claim of "DistRL is the first work to scale autonomous, online RL fine-tuning for mobile device control in a distributed environment." may be incorrect, DigiRL also supports distributed data collection. I understand that DistRL supports more distributed RL optimizations, but it might be good to update this sentence.

Line 247-257, would be great to defer algorithm-related designs to the next section as this section mainly talks about system design.

There can be more details for the method. In particular, do you maintain a separate model for $Q$ and $\rho$? If so, how are those models trained? How is $\Pcal_{invalid}$ calculated? How is $A(s_t, a_t)$ calculated? More motivations can also be included. For example, why does DPER improve sample efficiency? 5.3 includes a training loss for the trajectory value function $V_{traj}$, where is it used?

Figure 5 (b) needs more explanations, what does "Proportion Above 60%" mean?

### Questions
Line 53-70 seems repetitive.

Line 71 fine-tuning(type of light training) -> fine-tuning

Paragrapho one and two of intro seem to be a bit verbose in introducing the background.

Line 78-85, it seems unnecessary to introduce the notion of RLHF here cuz this paper does not have human preferences.

Line 86-90 is confusing, it seems to describe challenges of exisiting offline datasets such as AitW and Android-Control, but why is it relevant for online RL fine-tuning?

Line 98-104 can be best put in the related works.

There are too many bolded text in the introduction that can tire the readers. I would suggest removing the bold font for related methods. Same applies to the experiment section.

Line 121-122, te claim of "DistRL is the first work to scale autonomous, online RL fine-tuning for mobile device control in a distributed environment." may be incorrect, DigiRL also supports distributed data collection. I understand that DistRL supports more distributed RL optimizations, but it might be good to update this sentence.

Line 247-257, would be great to defer algorithm-related designs to the next section as this section mainly talks about system design.

There can be more details for the method. In particular, do you maintain a separate model for $Q$ and $\rho$? If so, how are those models trained? How is $\Pcal_{invalid}$ calculated? How is $A(s_t, a_t)$ calculated? More motivations can also be included. For example, why does DPER improve sample efficiency? 5.3 includes a training loss for the trajectory value function $V_{traj}$, where is it used?

Figure 5 (b) needs more explanations, what does "Proportion Above 60%" mean?

### Soundness
2

### Presentation
1

### Contribution
3
