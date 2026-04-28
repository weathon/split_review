# UnCLe: An Unlearning Framework for Continual Learning

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 8, 5

## Abstract
Recent advances in deep learning require models to exhibit continual learning capability, allowing them to learn new tasks and progressively accumulate knowledge without forgetting old tasks. Concurrently, there are growing concerns and regulatory requirements to meet privacy and safety by discarding some knowledge through machine unlearning. With the rapidly rising relevance of continual learning and machine unlearning, we consider them together under a unified framework in this paper. However, the conflicting nature of past data unavailability arising from continual learning makes it challenging to perform unlearning with existing methods which assume data availability. Moreover, in the proposed setup, where tasks are repeatedly learned and unlearned in a sequence, it is another challenge to maintain the stability of the tasks that need to be retained. To address these challenges, we propose UnCLe, an Unlearning Framework for Continual Learning designed to learn tasks incrementally and unlearn tasks without access to past data. To perform data-free unlearning, UnCLe leverages hypernetworks in conjunction with an unlearning objective that seeks to selectively align task-specific parameters with noise. Our experiments on popular benchmarks demonstrate UnCLe's consistent unlearning completeness and ability to preserve task stability over long sequences.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes UnCLe, an unlearning framework for continual learning designed for a sequence of learning and unlearning tasks without access to past data. UnCLe is formulated as an approximate unlearning framework. 

The CL solution employs a hypernetwork that takes a task specific embedding (together with network chunk embeddings, Fig. B.7) as input to generate weights for the main network to solve a task. Furthermore, a regularization loss is used to reduce catastrophic forgetting. Sharing of hypernetwork weights between tasks leads to inter-task knowledge transfer. 

The same hypernetwork is used for unlearning, where the forget task identifier is used as input (no forget data is used). The optimization objective is to reduce the MSE between the hypernetwork output and noise, averaged over n samples. Using Theorem 3 (Appendix A), the authors demonstrate that the objective effectively reduces the generated parameter values to zero, while simultaneously retaining the performance on other tasks. 

The efficacy of UnCLe is demonstrated by comparing with multiple unlearning techniques, using a set of five metrics, over different datasets.

### Strengths
* Considering unlearning jointly within the continual learning setting is an important problem. Given that many of the unlearning techniques rely on availability of forget and retain datasets, their unavailability in this setting introduces unique challenges. 

* The hypernetwork based solution is interesting. 

* The authors adopt the existing unlearning methods to the CL setting for performing comparison.

### Weaknesses
 * One major weakness in the paper is lack of insights behind empirical observations. This lack of systematic experimentation or presentation makes it difficult to assess the impact of the different solution pieces. For example, the paper does not provide ablation studies to understand the contribution of the regularization term or the hypernetwork architecture itself. It is unclear how much each component contributes to the overall performance.

* Figure 3 (right) shows that one can recover the task embedding of the forgetting task. What impact does this have on the recovery of the forgetting task performance. The results of the Membership Inference attack need to be discussed more to understand the unlearning performance. Specifically, the paper needs to clarify if the membership inference attack is performed on the task embedding or the model weights and how this relates to the unlearning objective. The implications of successful membership inference attacks on the unlearned task need to be discussed in the context of the proposed unlearning method.

* Figure 4 (left) shows that task 0 does not suffer from catastrophic forgetting when a sequence of learning and unlearning operations are performed (x-axis). I could not find information about the dataset used for task 0, and if subsequent overlap in task data distribution is helping reduce catastrophic forgetting. How are the unlearning tasks related to the learning tasks and so on. The paper should clarify the nature of the tasks, their data distributions, and how the unlearning tasks are selected with respect to the learning tasks. It's crucial to understand if the unlearning tasks are related to the learning tasks and if the data distribution of the unlearning tasks overlaps with the learning tasks.

* The authors claim that UnCLe is agnostic to the operation sequence used. Other than the results over the three sequences in Figure F.8 is there something more concrete that can be discussed in support of this general claim. The paper should provide a more rigorous analysis of the sequence agnosticism, perhaps by testing on a wider range of task sequences or by providing a theoretical argument for why the method is sequence agnostic.

* Other than permuted dataset, the RA scores for all the other datasets are dominated by the baseline methods. Does it show that UnCLe sacrifices learning in favor of reducing catastrophic forgetting. The paper needs to discuss the trade-offs between learning performance and unlearning effectiveness. It should be clarified whether the lower RA scores are a result of the unlearning process or a limitation of the learning method itself.

* In Algorithm 2, besides the regularization term (which basically prevents the model from moving too far away from the starting values) there is nothing to prevent the unlearning from causing catastrophic forgetting. Can the authors please bring more clarity into why they observe so little impact on the existing tasks. Specifically, it is unclear how the regularization term prevents catastrophic forgetting, and the paper should provide a more detailed explanation of the mechanism.

### Questions
* As per Algorithm 1, the task specific embedding is randomly initialized and then learnt as part of the optimization steps. Is this the same embedding that is then used for a forgetting task? 

* The 32-dimensional task-specific embedding seem to be extremely critical for the functioning of Algorithm 1 and 2. Are there any results on the characteristics of these vectors, their alignment based on the similarity of tasks and so on.

* Thoughts on how will this hypernetwork-based solution scale to larger networks?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a unified framework to consider both continuous learning and machine unlearning. Since past data is often inaccessible in some scenarios, this makes existing machine unlearning methods challenging. To address these challenges, the authors propose UnCLe, a framework for incremental task learning and unlearning in the absence of past data. UnCLe uses a hypernetwork and unlearning goals to selectively tune task-specific parameters to achieve data-free unlearning.

### Strengths
1 The unified continuous learning and machine unlearning framework provided by the authors is interesting and meets the challenge of not being able to access past data.

2 The proposed framework is experimented in some popular benchmarks.

3 The authors make an attempt to prevent catastrophic forgetting in the machine learning process.

### Weaknesses
1 Some sentences are more complex in structure and less readable, such as 'To prevent catastrophic forgetting, the hypernetwork is regularised in such a way that ...' in Chapter 5. This sentence is too long and can be broken down into two short sentences.

2  Section 5: Conversely, for an unlearning request, R t = (U, T_f , ϕ), task …’ The ϕ in ϕ and the ϕ in hypernetwork parameters ϕ are prone to ambiguity. Using different notation or adding subscripts to distinguish between the different meanings of ϕ.

3  The ResNet-50 used by the authors was too large for these tasks. The method proposed in [1] can achieve good performance in continuous learning tasks on CIFAR-10, CIFAR-100 and Tiny-ImageNet datasets (which are also used in this paper) using ResNet-18. You can justify why you did not use ResNet-18 for testing or add experiments using ResNet-18 to show the superiority of the methodology.

### Questions
1 Why must the model's prediction be similar to a random guess and close to a uniform distribution in the unlearning task? In my opinion, it probably doesn't need to be a uniform distribution to achieve unlearning capability. Could you explain why the model’s prediction must have some distributions in unlearning process.

2 In Fig.2, how to use hypernetwork to generate ResNet parameters?

### Soundness
2

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
4

### Summary
The authors address the challenge of stability when unlearning in a continual learning environment. To address this challenge, the authors propose UnCLe, an Unlearning Framework for Continual Learning designed to learn tasks incrementally and unlearn tasks without access to past data. The method uses hypernetworks together with an unlearning objective that aligns task-specific parameters with noise. Experimentally they show the method’s unlearning completeness and preservation of task stability over sequences of tasks.

### Strengths
The research will be of interest to the ICLR community.

Originality: There is currently a lot of interest in unlearning in the continual learning setting. The authors have summarised and categorised the main approaches. They have highlighted the advantages of their approach over other approaches.

Quality: The description of the proposed method is clear and there is extensive experimentation.

Clarity: The presentation of the work is generally of high quality, and easy to read.

Experimentation: The experimentation supports the claims.

### Weaknesses
Significance: The significance of the work is questionable. It is incremental rather than opening a new direction of unlearning in the continual learning domain.

Motivation: The motivation given for unlearning is for privacy and the regulatory environment. The example which follows straight after this is unlearning for other reasons. I suggest that you either move the other reason for unlearning that is described in Section 6.5.1 to the motivation, or chose a motivating example that aligns with the motivation.

Claim: On page 1 there is a claim that retaining data goes against regulatory interests. In fact the opposite is true. Regulators often require data to be kept for a number of years, in case it is required as evidence.

Future work: This is missing. What are the next logical steps?

Figure 1 is a special case of unlearning where it is always unlearning the oldest task. I suggest that this is updated to the more general case where any task can be unlearnt at any time.

The grammar needs to be checked. There are prepositions missing. There are also some words that are unusual in the context in which they are used, such as "biome" on page 1, "prowess" on page 2 and "befit" on page 4.

The caption for Figure 6 has a typo: "with and with" should read "with and without"

### Questions
I have offered suggestions under Weaknesses above.

I am impressed with the thoroughness of the evaluation, but the paper is missing a discussion of the limitations of the approach and potential ways to address them.

What are the open problems or future directions related to your work. Adding this to the paper would improve the paper's discussion of broader impact and potential future work.

### Soundness
3

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
This paper studies a novel setup of continual unlearning, where tasks are repeatedly learned and unlearned in a sequence. Considering the data regulations in continual learning, the unlearning is performed without access to data. The authors propose a novel method based on hypernetwork. Specifically, the hypernetwork is trained to produce main network parameters to minimize task-specific loss for learning request, together with regularization term that retains its performance on former tasks. For unlearning request, the hypernetwork is trained to produce main network parameters that is close to Gaussian noise for unlearning target task. The proposed method outperforms existing unlearning methods in the proposed setting.

### Strengths
1. The paper is well-written, the methodology is clearly presented, and the readability is strong.
2. The paper considers an interesting setting where tasks can be iteratively learned and unlearned. The unlearning is conducted by data-free method, requiring no data from forget set or retain set.
3. It is demonstrated that existing method can not be directly applied for the problem setup and proposed a novel framework designed for the specific setup.

### Weaknesses
1. The motivation for continual unlearning requires further elaboration since this is relatively new area. In paragraph 1, machine unlearning is firstly introduced as a technique aiming to comply with privacy and regulatory requirements. However, later in this paragraph, two application examples of continual unlearning are discussed where the motivation of unlearning shifts towards utility considerations: “Unlearning obsolete skills would enable the robot to learn newer skills within the same parameter constraints”. My concerns are as follows: First, the claim that unlearning can enhance model performance on newer tasks is bold yet underexplored. Given that deep learning models exhibit sparsity, the retention of old knowledge may not significantly impede the learning of new tasks. I suggest you provide empirical evidence or citations to support the claim that unlearning can enhance performance on newer tasks. Second, the authors should clarify whether the unlearning part in continual learning aims at privacy protection or performance boost. There exists conflict mentioned above in current demonstration which may cause confusion.

2. The proposed method should align with the motivation. The unclear motivation weakens the persuasiveness of the proposed approach.. As illustrated in the paper, there is “a trivial way to unlearn” that is to discard the embedding $e_f$. But this may serve as a strong baseline. Let’s consider two circumstances: (1) Unlearning is conducted for protecting privacy. Then discarding the embedding $e_f$ or setting $	heta_f$ to be zero could suffice. To argue that the proposed method is stronger than the trivial baseline, authors should conduct experiments to demonstrate the proposed method achieves better privacy protection than these “trivial way” For example, results from MIA attacks should be reported to evaluate privacy protection, if that is indeed a key motivation. (2) Unlearning is performed for boosting performance for newer tasks. Then after unlearning the performance of later learned tasks should improve. In other words, if a task $T_f$ is unlearned at time step t, tasks learned at subsequent time steps should achieve better performance than if task $T_f$ had not been unlearned at time step t. This should be supported by empirical experiments if the motivation is indeed boosting performance. Furthermore, the aforementioned two baselines (discarding the embedding $e_f$ or setting $	heta_f$ to be zero) should be included in the experiments and compared with the proposed method.

### Questions
see Weaknesses

### Soundness
3

### Presentation
4

### Contribution
2
