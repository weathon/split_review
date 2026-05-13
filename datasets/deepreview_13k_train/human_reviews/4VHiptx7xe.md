# STRAP: Robot Sub-Trajectory Retrieval for Augmented Policy Learning

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
Robot learning is witnessing a significant increase in the size, diversity, and complexity of pre-collected datasets, mirroring trends in domains such as natural language processing and computer vision. Many robot learning methods treat such datasets as multi-task expert data and learn a multi-task, generalist policy by training broadly across them. Notably, while these generalist policies can improve the average performance across many tasks, the performance of generalist policies on any one task is often suboptimal due to negative transfer between partitions of the data, compared to task-specific specialist policies. In this work, we argue for the paradigm of training policies during deployment given the scenarios they encounter: rather than deploying pre-trained policies to unseen problems in a zero-shot manner, we non-parametrically retrieve and train models directly on relevant data at test time.  Furthermore, we show that many robotics tasks share considerable amounts of low-level behaviors and that retrieval at the "sub"-trajectory granularity enables significantly improved data utilization, generalization, and robustness in adapting policies to novel problems. In contrast, existing full-trajectory retrieval methods tend to underutilize the data and miss out on shared cross-task content. This work proposes STRAP, a technique for leveraging pre-trained vision foundation models and dynamic time warping to retrieve sub-sequences of trajectories from large training corpora in a robust fashion. STRAP outperforms both prior retrieval algorithms and multi-task learning methods in simulated and real experiments, showing the ability to scale to much larger offline datasets in the real world as well as the ability to learn robust control policies with just a handful of real-world demonstrations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces STRAP, a novel method for trajectory retrieval to find similar sub-trajectory segments in large-scale datasets for efficient policy learning in few-shot settings. The method's key contribution lies in combining pretrained visual encoders with Dynamic Time Warping to encode sub-trajectories of variable lengths for improved retrieval. The proposed method is tested against several retrieval baselines and BC ones on LIBERO-10 simulation and real world pick and place tasks and achieves good performance.

### Strengths
- The proposed method is well motivated and achieves strong results across multiple experiments, both in simulation and real-world settings

- The use of Dynamic Time Warping for sub-trajectory matching is novel and well-suited for the problem domain

- Comprehensive evaluation against recent retrieval baselines demonstrates the method's effectiveness

- Thorough ablation studies on different pretrained encoders provide valuable insights into architecture choices

- The paper is well written and includes several illustrative figures that enhance the text

### Weaknesses
 - The baseline comparison against multi-task policy appears weak, as it only uses pretrained weights without fine-tuning. This seems like an artificially weak baseline since fine-tuning is standard practice for all MT-policies.

- The paper's argument that retrieval is more efficient than expensive pretraining needs stronger empirical support, especially given that the robotics community regularly fine-tunes general policies for downstream tasks

- The computational cost of STRAP's retrieval process on large-scale datasets like Droid is not adequately addressed, raising questions about real-world scalability. Some more clarity is necessary here

- The choice of K for constructing D-retrieval lacks sufficient explanation and ablations. The paper should explore how different K values affect both retrieval quality and computational overhead and policy performance, as this parameter likely presents a trade-off between performance and efficiency. A discussion about the retrieved data quantity would provide valuable insights and strengthen then paper.

- Small number of tested tasks in real world setting and missing baselines of MT policy and finetuned MT policy

- Real world retrieveal is conducted with the same robot embodiment and gripper. How does STRAP Perform when retrieving similar data from other robot datasets like BridgeV2 that does not share the same robot and scenes?

### Questions
- Could STRAP be combined with fine-tuning of MT policies on the retrieved dataset to potentially achieve even better performance than domain-specific fine-tuning alone?

- How does STRAP's performance compare against standard fine-tuning approaches when controlling for the total amount of data used?

- What are the memory and computational requirements for deploying STRAP on very large trajectory datasets like Droid?

- Can you add the average performance for LIBERO-10 results to the main table?

- Can you provide a few more real world tasks with required baselines?

- Real world retrieveal is conducted with the same robot embodiment and gripper. How does STRAP Perform when retrieving similar data from other robot datasets like BridgeV2 that does not share the same robot and scenes?

STRAP presents an novel and well designed approach to few-shot learning, that tackles several drawbacks of prior methods through sub-trajectory retrieval with dynamic time-warping. However, more comprehensive comparisons against fine-tuned baselines and clearer analysis of computational requirements would strengthen the paper's contributions. Thus, I recommend weak reject pending addressing the following concerns: (1) comparisons against fine-tuned baselines, (2) clearer analysis of computational requirements, and (3) better justification of parameter choices.

### Soundness
2

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
4

### Summary
This paper focuses on the setting of generalizing a policy to an unseen task with few-shot demonstrations. Instead of deploying zero-shot, the paper proposes STRAP, training a model on task-relevant data augmented by retrieval. STRAP first retrieves sub-trajectories from a large pretraining dataset that are similar to the new task demonstrations, then combines them with the few-shot demos to train a policy. Results on sim and real environments show that STRAP outperforms other retrieval methods and pure behavioral cloning. Ablations show that STRAP is compatible with various vision encoders and justify each of its component.

### Strengths
- Sub-trajectory retrieval for the few-shot demo behavioral cloning setting is a well-motivated and novel idea.
- The method is clear and straightforward to implement.
- Results show that matching with DTW on vision foundation model features are robust to variations and capture task semantics.
- Real and simulated environments show that STRAP outperforms other retrieval methods and pure behavioral cloning.

### Weaknesses
 - STRAP requires few-shot demos and model training at test time for a new task.
- It would be good to see more sim and real environments for evaluations.
- It would be more convincing to see a behavioral cloning baseline that uses all available data.

### Questions
- Baseline: how does STRAP compare to the pretrain-then-finetune setup? (Pretrain on the prior dataset, then fine-tune on the few-shot target demonstrations?)
- Baseline: how does STRAP compare to a multitask policy trained on all available data?
- Generalization: to what extent does STRAP generalize across environments or embodiments?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose a task-specific robot learning framework using pre-collected datasets. Unlike the many robot learning methods that train the generalist policy model with multi-task expert data, the proposed method (STRAP) train a task-specific policies, which can yields better performance on single task. When the few-shot target demo, in addition to prior dataset is given, STRAP filters the task-relevant data from prior data and use it with target demo to train the model. One of the key features of STRAP is that it retrieves the data measuring the similarity between sub-trajectories, rather than the whole trajectories. Also, it utilize subsequence dynamic time warping (S-DTW) to match between the data. As a result, the proposed method shows improved performance compared to the previous methods, generalist policy models, and specialist models that only use the target data.

### Strengths
- To deal with potentially variable length during retrieval, STRAP use dynamic time warping (DTW) to match the sub-sequences
- STRAP shows improved performance compared to the prior framework (Behavior Retrieval, Du et al., 2023) which retrieves single state-action pairs using VAE.

### Weaknesses
 - The idea of using only data relevant to the target task, rather than learning a generalist policy through multi-task data, is interesting. However, retrieving new data from prior dataset and training a policy each time a new scene is encountered is highly computationally costly.
- Comparing the entire prior data with the target data one-to-one to measure similarity is not scalable with the dataset size. Moreover, since this retrieval process requires computationally intensive neural network operations, such as DINO, it raises questions about whether this process can be performed at test time. In particular, there is no mention of how to handle an increase in offline dataset size, nor are there any discussions about limitations in this regard. The computational cost of calculating the S-DTW distance matrix between all sub-trajectories in the prior and target datasets is also a significant concern, especially as the dataset size grows. The paper lacks a detailed analysis of how this cost scales, and whether the proposed method can be applied to larger datasets without becoming prohibitively expensive.
- There is no discussion about computational cost.
- STRAP uses a top-k retrieval dataset. Increasing this k could bring in more data but might reduce relevance, whereas a smaller k would provide more refined data but with a smaller amount. However, there is a lack of analysis on how changing this k value affects performance.

### Questions
- Compared to the prior framework (Behavior Retrieval, Du et al., 2023), STRAP seems to have three main differences in retrieval system. (a) use non-parametric retrieve vs. VAE (b) use sub-trajectory wise retrieve vs. single state-action pairs and (c) use DTW. Among these, what gives the most / least performance gains?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
## Paper Review Summary

This work advocates for training policies dynamically during deployment, utilizing the encountered scenarios to improve model performance. Instead of relying on pre-trained policies to tackle new problems in a zero-shot fashion, the authors propose a non-parametric approach that retrieves relevant data and trains models directly at test time. The paper introduces SRTAP, a method built on pre-trained Vision-Language Models (VLM) and dynamic time wrapping, which combines sub-trajectories into a policy. The approach involves some training on a set similar in language to the test set, and has been demonstrated in both real-world and simulated environments.

### Strengths:
1. **Innovative Approach**: The authors present a compelling intuition, demonstrating robustness in solving multitask generalization challenges.
2. **Efficient Data Usage**: The method shows improvement in the way data is leveraged for robotics tasks, particularly in sub-trajectory retrieval.
3. **Thorough Experiments**: The experiments are detailed and show promising results for sub-trajectory retrieval and policy creation.

### Weaknesses:
1. **Project Incompleteness**: There is no accessible website or supplementary information, suggesting the project might still be unfinished.
2. **Visual Readability**: The images in the paper are difficult to interpret, potentially detracting from the clarity of the results.
3. **Writing Quality**: The paper's writing needs improvement, especially in terms of clarity and readability.
4. **Generalization**: Some imitation learning methods, such as [Sparse Diffusion Policy](https://forrest-110.github.io/sparse_diffusion_policy/), [HPT](https://liruiw.github.io/hpt/), [RDT-Robotics](https://rdt-robotics.github.io/rdt-robotics), and [Humanoid Manipulation](https://humanoid-manipulation.github.io/), appear to show more generalization in similar settings.
5. **Formatting**: The paper's formatting is problematic, with certain sections being hard to read, affecting the overall readability of the work.

In conclusion, while the proposed method shows strong intuition and detailed experimentation, there are concerns about project completeness, readability, and potential improvements in both writing and generalization when compared to existing work. 

I would like to change the rate after discussion, but at least you should finish the site you provide.

### Strengths
1. **Innovative Approach**: The authors present a compelling intuition, demonstrating robustness in solving multitask generalization challenges.
2. **Efficient Data Usage**: The method shows improvement in the way data is leveraged for robotics tasks, particularly in sub-trajectory retrieval.
3. **Thorough Experiments**: The experiments are detailed and show promising results for sub-trajectory retrieval and policy creation.

### Weaknesses
1. **Project Incompleteness**: There is no accessible website or supplementary information, suggesting the project might still be unfinished.
2. **Visual Readability**: The images in the paper are difficult to interpret, potentially detracting from the clarity of the results.
3. **Writing Quality**: The paper's writing needs improvement, especially in terms of clarity and readability.
4. **Generalization**: Some imitation learning methods, such as [Sparse Diffusion Policy](https://forrest-110.github.io/sparse_diffusion_policy/), [HPT](https://liruiw.github.io/hpt/), [RDT-Robotics](https://rdt-robotics.github.io/rdt-robotics), and [Humanoid Manipulation](https://humanoid-manipulation.github.io/), appear to show more generalization in similar settings.
5. **Formatting**: The paper's formatting is problematic, with certain sections being hard to read, affecting the overall readability of the work.

### Questions
1. Would you please update the sites in the paper?
2. Could you please add some experiments with other imitation learning methods?

### Soundness
2

### Presentation
1

### Contribution
3
