# Privacy-Aware Lifelong Learning

- Decision: Accept
- Scores: 5, 6, 6, 8

## Abstract
Lifelong learning algorithms enable models to incrementally acquire new knowledge without forgetting previously learned information. Contrarily, the field of machine unlearning focuses on explicitly forgetting certain previous knowledge from pretrained models when requested, in order to comply with data privacy regulations on the right-to-be-forgotten. Enabling efficient lifelong learning with the capability to selectively unlearn sensitive information from models presents a critical and largely unaddressed challenge with contradicting objectives. We address this problem from the perspective of simultaneously preventing catastrophic forgetting and allowing forward knowledge transfer during task-incremental learning, while ensuring exact task unlearning and minimizing memory requirements, based on a single neural network model to be adapted. Our proposed solution, privacy-aware lifelong learning (PALL), involves optimization of task-specific sparse subnetworks with parameter sharing within a single architecture. We additionally utilize an episodic memory rehearsal mechanism to facilitate exact unlearning without performance degradations. We empirically demonstrate the scalability of PALL across various architectures in image classification, and provide a state-of-the-art solution that uniquely integrates lifelong learning and privacy-aware unlearning mechanisms for responsible AI applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper formulates a task-incremental learning and unlearning problem with strong privacy considerations, by extending the traditional task-incremental learning setup to allow exact task unlearning instructions. The authors present privacy-aware lifelong learning (PALL) as a memory-efficient algorithmic solution to this new problem.

### Strengths
1. A novel experimental setup is proposed to combine lifelong learning and machine unlearning, addressing key challenges in both domains, which have not been addressed to date.
2. This paper presents privacy-aware lifelong learning (PALL) as a memory-efficient algorithmic solution to this setup, which enables learning without catastrophic forgetting, allows learnable forward knowledge transfer, and ensures exact unlearning guarantees by design.
3. The algorithmic empirically demonstrates the scalability of PALL on both convolutional benchmark architectures and attention-based vision transformers, yielding a stable performance in highly dynamic lifelong learning scenarios with randomly arriving unlearning requests.

### Weaknesses
1. This paper presents a new problem setting, but this problem lack significant innovation compared with existing problems. What is the most different points that distinguish this problem from others? It seems the objective of this problem in section 3.2 also holds for existing problem such as domain incremental learning and unlearning. Is there any challenges specific to this problem so that we must formulate it as a new problem?
2. The methods presented for the problem setting proposed in this paper appear to be well-established and lack significant innovation. The authors should either highlight any novel contributions or improvements to existing methods or explore more advanced techniques that could offer better solutions to the unique aspects of the problem.
3. This paper introduces an interesting approach, but it is unclear how the proposed method has been specifically tailored to address the new problem setting. The authors should provide a more detailed explanation of how their approach was designed to handle the new settings.
4. The paper should clarify why the task-incremental setting was chosen instead of class- or domain-incremental learning. Providing a rationale for this choice would help to better understand the appropriateness of the selected setting for the problem at hand.
5. The cited references of Regularization-based methods are mostly foundational works, but some are relatively dated, potentially overlooking recent improvements or newer approaches in the field.
6. The details of the Baseline you compared are not clearly described, e.g., how you tailor these baseline methods to fit the proposed problem setting?
7. In the experimental section, the results should be compared with the latest state-of-the-art (SOTA) models in Continual Learning. A more detailed comparison with existing SOTA methods would provide a clearer context for evaluating the proposed approach and strengthen the overall analysis.
8. In the section on Comparisons to Independent Subnetworks without Knowledge Transfer, the descriptions of the two configurations—static sparsity and dynamic sparsity—are not sufficiently clear. Although static sparsity is introduced as a random initialization of T independent sparse subnetworks, and dynamic sparsity as an optimization of sparse connectivity via score optimization, the explanation lacks details on how each configuration functions within the broader experimental setup.

### Questions
1. The cited references for Regularization-based methods mainly cover foundational works, but the discussion could benefit from including more recent studies that reflect the latest advancements in this area. 
2. The experience settings of other baselines are different from those in this paper. The Baseline Methods section should describe more detailed setups. 
3. Including SOTA models would strengthen the study’s impact by showcasing its performance relative to the best-performing approaches in the field.
4. It would be helpful to clarify the initialization and optimization processes more explicitly and outline each configuration's practical implications. Adding these clarifications would aid in understanding the differences and rationale behind these two configurations, improving the overall readability and transparency of this section."

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the important problem of “privacy-aware life-long learning” where a model must learn from a sequence of tasks, while supporting unlearning of a task previously-encountered in the sequence, when requested. Task unlearning is defined as a modification to the model to make it indistinguishable from one that was trained on the remainder of the sequence, excluding the task to be unlearned. Overall, this problem formulation inherits several desiderata from standard life long learning, e.g. enabling forward knowledge transfer, preventing backwards interference (reduced accuracy on old tasks due to learning new tasks), while being as memory efficient as possible. In addition, the desire to support task unlearning requests brings additional considerations, like being able to do unlearning in an “exact manner” (guaranteeing that influence from the unlearned task is indeed fully removed), with minimal impact to performance of other tasks. 

The authors propose a new method to address this problem based on an architecture that can be seen as comprising multiple sub-networks. Each task is assigned a mask (based on learnable parameters determining the importance of each parameter in the model for that particular task), and only modifies the parameters indexed by that mask during learning. Each new learning task in the sequence can only choose to modify previously-unused parameters. To unlearn a task, the parameters that had been affected by that task get reset and a light-weight retraining is performed on only the reset parameters, in order to restore performance for other tasks that might have come after the unlearned task in the sequence. This light-weight retraining is done using a buffer of some randomly-chosen data stored from each task seen so far.

The authors conduct experiments against several baselines from life-long learning and on various datasets. They also conduct thorough ablations to understand the effect of the frequency of unlearning tasks, the effect of the number of finetuning steps, as well as comparisons to an ablation of their system that maintains independent subnetworks within the model but does not facilitate forward transfer.

### Strengths
- The paper studies an important problem and presents a novel solution. To the best of my knowledge, this work is the first to provide an exact unlearning solution in a lifelong setting of interleaved learned and unlearned tasks.

- The paper is for the most part well-written and easy to follow.

- The experimental evaluation covers various relevant baselines and ablations.

- The proposed method performs well simultaneously in terms of several metrics and desiderata compared to the baselines considered.

### Weaknesses
 - It seems that the “independent subnetworks without knowledge transfer” ablation actually performs very similarly to the proposed approach (in Table 3), making it harder to motivate the significantly-more-complex variant for the additional 1% accuracy? Especially given that no confidence intervals are reported there, it’s hard to tell if these differences are significant and whether they justify the additional complexity. Are there perhaps other sequences of tasks / datasets where the “knowledge transfer” would be more “needed”, perhaps making this not the best “benchmark” to showcase the added benefits of knowledge transfer?

- Some clarity issues when describing the method, metrics and setup. Specifically, A) I don’t understand the difference between m_t and \bar m_t. The authors say the latter are the parameters specifically trained using data from D_t, but I don’t understand this statement. What does “specifically trained” mean? B) When describing the metric A_t, it’s unclear whether the final model checkpoint (after addressing the whole sequence) is used to compute accuracy on all tasks, or is a separate checkpoint (right after training on the particular task) used to evaluate the accuracy on each task? The text made me think the former but the notation a_{i,t} and explanation below made me think the latter. C) ““Regularization-based methods [...] were indifferent to task unlearning instructions, since the original methods are not adapted to unlearning” – how were these applied to unlearning tasks, then?

- Insufficient description (in the main paper) for how various other methods were adapted from the standard lifelong setting to the privacy-aware lifelong setting. It is difficult to fully grok how this adaptation was done and why in that particular way (rather than applying other types of approximate unlearning from the literature, for example).

- It is unclear how one should interpret the A_u metric. Having a network perform at chance level in terms of accuracy does not imply an unlearning guarantee, as the authors also acknowledged. It is not obvious that lower A_u is better (an accuracy that is “too low” can compromise privacy and cause vulnerability to attacks). Further, even when taking the right reference point (for how low accuracy should be) into consideration, accuracy-based metrics correlate poorly with more rigorous metrics for unlearning (see e.g. [1]). The authors seem to acknowledge this but still use this metric in the results and in discussions. It would be great to clarify in what way this information should be used and taken into consideration, given this caveat.

- Missing an important baseline: training sequentially with Differential Privacy (DP). This would yield approximate (but theoretically sufficient) unlearning without the need for resetting and retraining any weights. Various DP baselines can be considered: a DP variant of “Sequential”, where all parameters are updated for all tasks, as well as a DP variant of a sub-networks architecture, like in the proposed approach, where each task gets to choose which parameters to update, but in this case addressing unlearning requests can be done trivially (via a “no op”). Depending on the desired level of privacy, I expect such methods to have lower accuracy, but this feels like an important and relevant baseline to include and capture these trade-offs.

- Missing baselines from the unlearning literature. A plethora of approximate unlearning methods have been proposed (see e.g. [2-4]), that try to post-hoc modify a model to remove the influence of a subset of its training data. It feels like these would be readily combinable with the “Sequential” approach, for instance. 

- Building further on the above remarks, it would be very useful to build a comparison between the proposed method (and other exact solutions) with inexact unlearning. While the authors have considered some inexact methods, there aren’t proper metrics considered to empirically estimate the privacy of such methods. The only metric considered for this is the accuracy on unlearned tasks, which is a weak notion of privacy, as discussed above. I fully understand that adding empirical privacy auditing is a substantial amount of additional work and potentially difficult to do all of this within a single paper, but I do view this as a clear piece that is missing, or area for future work. 

- Another baseline can be training a model sequentially (without subnetworks), and when unlearning is needed, simply retrain the entire model from scratch (using the data in the buffers). I don’t expect this to perform well in terms of accuracy (and would also be less efficient at handling unlearning requests), but would be a useful data point for comparison; this is more akin to the “retrain from scratch” reference point in the unlearning literature. One may additionally consider an “oracle” version of this, that assumes access to all past data as another reference point (I understand that past data is assumed not to be available in life-long learning, hence referring to this as an “oracle”).

- A limitation of this framework is that “user privacy” can only be addressed (via exact unlearning) if a user’s data is cleanly separated in terms of “tasks”. Other scenarios, where all users participated in all “tasks”, would make this framework unable to support users to request their data to be deleted. It would be great to discuss this.

### Questions
- For the “independent subnetworks without knowledge transfer” ablation, could you explain specifically in what way(s) “Dynamic Sparse Ind.” differs from PALL? It seems both have the learned mask for which parameters to update per task. The authors claim that PALL additionally supports knowledge transfer but it’s not obvious to me what the mechanism is for that, given that each new task only modifies (a chosen subset of) previously-unused weights? I previously assumed that the way that knowledge transfer is realized is that the other weights, even if not directly optimized by the specific task, are still used in the forward pass and therefore still influence the model applied to this task too. Is this correct? And how is this done differently in the “Dynamic Sparse Ind.” variation? Or is there some other difference between the two?

- What is the worst-case sequence of interleaved learning and unlearning requests, w.r.t each metric considered here? Are there cases where the proposed method is no better than naive baselines? It would be great to discuss this in the paper.

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
This paper proposes privacy-aware lifelong learning (PALL). It is lifelong learning because it learns (explicit) tasks sequentially, and it is privacy-aware because it can unlearn any previously learned task. Tasks are learned on a sparse subset of the parameters only, i.e., the rest are masked out. These sparse active-subset masks are stored for each task, where the sparsity ratio is a hyperparameter. This makes it possible to unlearn a specific task by "removing" the subset determined by its associated mask, where "removing" here means a memory buffer rehearsal on the subsequent tasks of the unlearned task. Specifically speaking, for each subsequent task of the unlearned task (that has not been unlearned so far), we retrain the loss on a memory buffer and additionally regularize the logits to be close to the stored logits in the buffer. This lifelong learning algorith is thus memory-efficient and can preserve privacy by unlearning tasks. Experiments show that this algorithm is sound and performs well in practice.

### Strengths
- The paper is well-written
- The proposed method is sound and does well on the experiments.
- Modeling data in terms of tasks is a sound approach.
- Memory-efficiency is a good plus. Learning a subset of parameters per task is practical and performs well on experiments.
- Unlearning is possible and done by memory buffer replay with logits regularization. The performance of unlearning is shown empirically to be exact, which is one of the benefits of PALL.
- A better metric is proposed for measuring the performance of algorithms in sequential task learning-and-unlearning setting. Methods from the literature were adjusted to adapt to this setting, and the authors explained this adaptation well.
- The experiments are extensive and demonstrates the benefits of PALL over other the methods.
- The authors discuss a future direction for PALL to be applicable in class-incremental learning.

### Weaknesses
 **Main**:
- The algorithm is not necessarily always memory-efficient since the memory complexity still grows linearly in the number of tasks. In other words, the improvement is a constant, albeit a very small one given that it's stored in 1-bit format. However, some models nowadays are trained with less bits (e.g., 8-bits), so storing masks becomes non-trivially expensive when the number of tasks is very large (say, 50). Furthermore, the memory cost of storing the masks is directly proportional to the total number of parameters in the model, which can be substantial for large models, thus diminishing the memory efficiency gains.
- The tasks are given explicitly. While this might be the case sometimes in practice (e.g., tasks are user data), it still a disadvantage in terms of privacy (e.g., the data of some task are known to belong to some user). This explicit task identification could be a vulnerability, as it creates a direct link between data and task, potentially revealing sensitive information about the data source, which is a privacy concern.
- Eq. 6. is not novel. It is introduced as a generalized case of DER++ (Buzzega et al., 2020) because the authors say "$\beta=0.5$ yields DER++". Looking at the DER++ paper, it seems to me that their equation is more or less the same with $\beta$ intact ($\beta=0.5$ is the default value). I suggest the author rephrase this section to make this clear since it was written in a way that gives the reader the impression that this is an original contribution that generalizes prior work. The use of $\beta$ as a weighting factor is not a novel contribution, and the authors should clarify that they are simply using a standard approach.
- I would further argue that Eq. 6 is not an elegant remedy for such a privacy-aware algorithm since it requires access to some data from previous tasks. The need for a memory buffer, even if small, to perform the replay with logits regularization, undermines the privacy claims, as it necessitates storing and accessing data from previous tasks, which is not ideal for a privacy-focused method.
- The authors mentions "strong privacy considerations, where exact unlearning is possible." The authors should mention that the unlearning is is found to be exact *empirically* because it could be the case that the proposed algorithm would not be able to *unlearn exactly* on real-world data (e.g., foundational models might not be able to unlearn *exactly* even when using PALL). The claim of exact unlearning should be tempered with the understanding that it is demonstrated empirically, and might not hold under all conditions, especially with more complex real-world datasets and models.
- There are no investigations done on language data. This is especially important since the right to be forgotten is very applicable in this case. The lack of experiments on language data limits the generalizability of the findings, as the dynamics of language data and models can be quite different from those in vision, and the right to be forgotten is a critical aspect in language applications.
- Dynamic sparsity does not seem to be very important. Perhaps using static sparsity *and* increasing model size can match the same performance with the same memory cost. The benefits of dynamic sparsity are not clearly demonstrated, and it is possible that a simpler approach with static sparsity and a larger model could achieve similar results with comparable memory usage, which would be a more straightforward solution.
- Some experiments are not directly related to PALL. For example, Table 2. It is quite obvious that having more data in the memory buffer helps (the authors mention a counter case in the text, but I think the difference here is insignificant and the dataset CIFAR-10 is less real-world-like to make conclusions from).

**Minor**:
- Eq. 1., uses inconsistent notation for $\mathcal{L}$ in terms of arguments. Shouldn't contain $\theta_0$ on the left hand side? I also think it would be less convoluted without the $\theta_t \sim$ since it unnecessarily assumes that $\mathcal{L}$ is stochastic.
- Eq. 2., $\mathbf{U}$ and $\mathbf{L}$ not introduced. I believe they are just flag variable?
- Eq. 3., the first constraint is an expression without equality/inequality (min ERM). Perhaps "s.t." should be replaced with an inequality and "min" should be replaced with "argmin".
- I believe experiments and experimental results should traditionally be in the same section.
- $\alpha$ is not clearly introduced, only briefly after Eq. 4. I suggest to reintroduce $\alpha$ somewhere in the experimental results section  for clarity as it is used extensively there.
- The choice $\alpha = 1/T$ provides a fixed memory budget, but this might make comparisons between CIFAR-10 and CIFAR-100 trickier since they have a different number of tasks. The fixed memory budget allocation might not be optimal for all datasets and could lead to unfair comparisons between datasets with varying numbers of tasks.
- The experiments are being compared with methods that are not designed for the problem in this work. While this is not necessarily bad, it makes PALL more likely to outperform them since PALL is designed for this problem, so its better peformance, particularly in unlearning, is expected and not surprising.

### Questions
- How do you guarantee that a random sparse subset would not have significant overlap with a previous subset?
- Seems like memory buffers are an integral part of this lifelong learning algorithm. Do the authors have an idea how it could be done without them?

### Soundness
3

### Presentation
3

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
This manuscript focused on a novel setting for task-incremental lifelong learning with selectively forgetting (i.e., exact task unlearning) regarding the data privacy concern. This setting aims to simultaneously realize some challenging objectives, including learning tasks without forgetting, facilitating forward knowledge transfer, selective forgetting of specific tasks, and guaranteeing memory efficiency. To address this challenging task, the authors proposed Privacy-Aware Lifelong Learning (PALL) framework. Specifically, inspired by previous work WSN, this method adopted an architecture-based strategy through knowledge isolation and sharing with subnetwork masks. Furthermore, the experience replay strategy was applied to mitigate potential performance degradation caused by the parameter reinitialization after knowledge unlearning. Empirical experiments on three standard benchmarks were conducted to support the effectiveness in different aspects compared to other baseline methods.

### Strengths
1. This manuscript considered a novel setting. The data privacy concern is practical in lifelong learning but the exact task unlearning is less explored in this context. The proposed setting is well-defined.

2. The adoption of subnetwork masks provided a unified perspective for controlling catastrophic forgetting and exact task unlearning.

3. The experiments indicated that the proposed method is memory-efficient compared to baseline methods.

### Weaknesses
1. Most parts of this manuscript came from a previous study WSN [1]. Although the experience replay (in section 3.3) was tailored for knowledge recovery after an unlearning step, the new message conveyed from this manuscript is limited. The core mechanism of using subnetwork masks for knowledge isolation and sharing is directly adopted from WSN, and the modifications, such as reinitializing scores and unused weights, appear to be incremental rather than fundamentally novel. The experience replay, while adapted for unlearning, doesn't introduce a significant departure from standard replay techniques, thus limiting the overall contribution.

2. The scalability of the proposed method needs to be further demonstrated with more experiments on other datasets. While the experiments show memory efficiency, the performance on larger datasets with more tasks and unlearning requests is not thoroughly explored. The current experiments are limited to relatively small datasets and a limited number of tasks, which raises concerns about the method's applicability to more complex real-world scenarios. For instance, the performance on datasets with a larger number of classes or more complex data distributions needs to be evaluated.

3. The current version only considered the task-incremental setting where the task id is known during the inference. I wonder the applicability on other settings, such as class-incremental setting or domain incremental setting. The assumption that task IDs are always available during inference is a significant limitation. In many real-world scenarios, the task identity is not known, and the model must be able to generalize to new tasks without explicit task labels. The lack of discussion on how the method would perform in class-incremental or domain-incremental settings, where the task boundaries are not clearly defined, limits the practical applicability of the proposed approach.

### Questions
1. I noticed that the maximum number of tasks in this manuscript is 40 in S-TinyImage and the maximum unlearning requests $N_u$ is 9 for the S-TinyImageNet 20-split setting. I wonder if the proposed method is scalable for larger numbers of tasks and more unlearning requests, e.g., on the Omniglot-Rotation dataset which has 100 tasks in total.

2. Can the proposed PALL be adapted to the class-incremental setting? If so, what changes should be introduced to make it compatible with the scenario if we don't know the task identity?

3. About the training efficiency. In section 5, the authors only discussed the memory that needs to store the additional parameters along the learning dynamic. The comparisons of the training time among different methods were missed. The proposed method is mainly based on WSN [1]. However, according to my experience in training WSN, I found that WSN could be a little slow since it requires the parameter-level gradient masking within each backpropagation step and I believe this operation also exists in your proposed PALL. Thus, could the authors provide a comparison w.r.t. the training efficiency among different methods?

References:

[1] Forget-free Continual Learning with Winning Subnetworks. ICML 2023.

### Soundness
3

### Presentation
3

### Contribution
3
