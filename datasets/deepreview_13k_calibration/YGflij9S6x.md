# Continual Learning: Less Forgetting, More OOD Generalization via Adaptive Contrastive Replay

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 5, 6

## Abstract
Machine learning models often suffer from catastrophic forgetting of previously learned knowledge when learning new classes. Various methods have been proposed to mitigate this issue. However, rehearsal-based learning, which retains samples from previous classes, typically achieves good performance but tends to memorize specific instances, struggling with Out-of-Distribution (OOD) generalization. This often leads to high forgetting rates and poor generalization. Surprisingly, the OOD generalization capabilities of these methods have been largely unexplored. In this paper, we highlight this issue and propose a simple yet effective strategy inspired by contrastive learning and data-centric principles to address it.
We introduce \textbf{Adaptive Contrastive Replay (ACR)}, a method that employs dual optimization to simultaneously train both the encoder and the classifier. ACR adaptively populates the replay buffer with misclassified samples while ensuring a balanced representation of classes and tasks. By refining the decision boundary in this way, ACR achieves a balance between stability and plasticity. Our method significantly outperforms previous approaches in terms of OOD generalization, achieving an improvement of 13.41\% on Split CIFAR-100, 9.91\% on Split Mini-ImageNet, and 5.98\% on Split Tiny-ImageNet

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes Adaptive Contrastive Replay (ACR) to address the Out-of-Distribution (OOD) generalization problem often overlooked by existing class-incremental learning algorithms. While previous research has achieved strong performance across various class-incremental learning scenarios, these algorithms tend to perform well only on in-domain tasks due to issues with bad memorization, resulting in poor generalization to OOD tasks. To overcome this, the paper introduces a Proxy-based Contrastive Loss and Adaptive Replay Buffer Management. The Proxy-based Contrastive Loss utilizes the class weights as proxies for contrastive learning. Additionally, exemplars are sampled based on the variance of confidence scores, allowing for balanced sampling across tasks and classes and prioritizing hard examples close to decision boundaries to improve stability and OOD generalization. Through extensive experiments and analysis, the proposed algorithm demonstrates superior performance across diverse scenarios.

### Strengths
1. This paper identifies the often-overlooked OOD generalization issue in class-incremental learning and proposes ACR to address it. I find the distinction between bad and good memorization for explaining this problem, along with the design of Proxy-based Contrastive Loss and Adaptive Replay Buffer Management, to be well-motivated and effectively structured to tackle the identified issue.

2. To validate the proposed algorithm, the authors conducted extensive experiments across various datasets, algorithms, and memory buffer sizes. Additionally, the thorough analysis and ablation studies to verify and examine the effectiveness of the algorithm are insightful and engaging to read.

### Weaknesses
1. The paper [1] proposes a sampling method that stores the most interfered samples in the replay memory. I believe this plays a similar role and function described in equation (3) of the author's paper. Therefore, I think it is necessary for the authors to explain the differences from [1] and consider it as an additional baseline.

2. The authors validated the superiority of their proposed algorithm through various experiments using CIFAR-100, Split Mini-ImageNet, and Split Tiny-ImageNet in online class-incremental learning. However, I have the following questions regarding these experimental results:

   2-1) According to the paper, the results for Split CIFAR-100 in Table 1 show the experimental results for 10 tasks using the ResNet-18 model. I understand that reporting results for these 10 tasks have generally been done with the ResNet-32 model, starting with [2], and results have been reported in papers such as [3], [4], and [5]. When comparing these results (especially Figure 1(a) of [4]) with those in Table 1, the results in this paper appear to be relatively low. For example, when using a replay memory size of 2000 in [4] and [5], the accuracy of the naive algorithm ER (or replay) is reported to be around 40%, while Table 1 shows only 24%. Furthermore, the highest performance reported in [4] is 60% (e.g., DER), whereas the proposed algorithm achieved only 42% in Table 4. Is this discrepancy solely due to the model used? I believe that comparing the performance of the proposed algorithm with existing baselines using ResNet-32 is essential to confirm its superiority.

   2-2) Since all experiments were conducted using images sized 32 x 32 for a specific scenario, it makes it very difficult to assess whether the proposed algorithm can achieve excellent results across diverse scenarios. Additionally, many class-incremental learning algorithms are known to exhibit different performance trends depending on the input image size and scenario (shown in [4] and [5]), so I believe the authors should conduct additional experiments using ImageNet (or not resized ImageNet-100) and other task scenarios (e.g., a scenario in which a large number of classes are learned in the first task, and the remaining classes are divided and learned in subsequent tasks.) to demonstrate the effectiveness of their proposed algorithm in various settings.

3. From the results in Table 4, it is evident that the simple 'Random' policy already performs very close to 'Challenging' (ACR). This experiment was conducted with a replay memory size of 500; what would happen if it were increased to 2000? Would 'Challenging' still outperform 'Random' in this case? I think it is crucial to demonstrate that 'Challenging' provides superior performance compared to 'Random' in this experiment.

4. Additionally, I believe that, for the ablation study on Adaptive Replay Buffer Management, it is necessary to include results from experiments using ER without proxy-based contrastive learning in Table 4. This will allow for a proper evaluation of the standalone effectiveness of Adaptive Replay Buffer Management.

### Questions
I have included all weaknesses and questions in the Weakness section, so please refer to it. I strongly resonate with the authors' concerns about the OOD generalization problem in class-incremental learning algorithms, and I believe the proposed algorithm is well-designed. However, the various questions raised by the experiments and the lack of sufficient ablation studies make it difficult to provide a more favorable evaluation.I look forward to the authors correcting any misunderstandings I may have and providing a response to my review in their author response.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addressed the out-of-distribution generalization performance of rehearsal-based CL methods, which is a topic that has been overlooked by the community. The authors proposed Adaptive Contrastive Replay (ACR) which consists of two components: proxy-based contrastive learning and adaptive replay buffer management. The former encourages the model to maintain a clear class boundary while the latter populates the buffer with task- and class-balanced challenging samples to improve the model's stability and plasticity. Experiments on popular CL benchmarks showed improved performance with the proposed method with both iid and ood data.

### Strengths
1. The paper is well-motivated

2. The paper is generally easy-to-follow

### Weaknesses
There are some critical concerns about the proposed components, some missing explanations, and some room for improvement in the representations of the paper. Please refer to the Questions section.

1. How does the proposed PCL loss differ from a standard cross entropy loss with temperature-scaled softmax?

The authors might elaborate more on this because I cannot see the difference between the proposed PCL loss (Eq. 4) and a stand softmax CE loss.

2. Is the confidence variance evolved to fixed after epoch E, and is this robust?

According to Algorithm 1, it seems that confidence is only recorded until epoch E (which is 5 in practice) whereas the total training lasts 50 epochs. Is that correct? If so, I am wondering how robust is this confidence variance. First, in the first 5 epochs, the model might not be able to converge to a stable state, which means that the predictions can be rather random. Is the confidence variance based on nearly random predictions reliable? I am not sure. Can the authors compare the confidence variance at the beginning of the task and at the end? Second, it seems reasonable that the model would refine by itself the decision boundary, which means that some challenging samples might become not challenging along training. If the confidence variance is fixed after epoch E, the the entire buffer seems to be static within a task, then the score cannot take this into account.

3. Are the challenging samples really helping?

The authors' claim to include challenging samples in the buffer is to maintain accurate decision boundaries for old tasks (lines 285-286), which should lead to less forgetting. However, in Table 4, the challenging column is not performing better than the random column in BWT, which suggests that the proposed selection mechanism might not be effective in maintaining the decision boundary of old tasks. It also raised the concern that the improvement of the proposed selection mechanism might just be a result of balanced sampling in the memory buffer, which is more or less well-known in the CL community.

4. Some explanations are missing

In lines 89-90, the implementation of the comparison is not explained, which makes Fig. 1 harder to understand

In lines 266-269, the claim that no task label needs to be stored is confusing. How are the samples arranged separately in the buffer (line 266) if no task label is known?

The concept of proxy is not clearly explained (lines 182-184)

### Questions
1. How does the proposed PCL loss differ from a standard cross entropy loss with temperature-scaled softmax?

The authors might elaborate more on this because I cannot see the difference between the proposed PCL loss (Eq. 4) and a stand softmax CE loss.

2. Is the confidence variance evolved to fixed after epoch E, and is this robust?

According to Algorithm 1, it seems that confidence is only recorded until epoch E (which is 5 in practice) whereas the total training lasts 50 epochs. Is that correct? If so, I am wondering how robust is this confidence variance. First, in the first 5 epochs, the model might not be able to converge to a stable state, which means that the predictions can be rather random. Is the confidence variance based on nearly random predictions reliable? I am not sure. Can the authors compare the confidence variance at the beginning of the task and at the end? Second, it seems reasonable that the model would refine by itself the decision boundary, which means that some challenging samples might become not challenging along training. If the confidence variance is fixed after epoch E, the the entire buffer seems to be static within a task, then the score cannot take this into account.

3. Are the challenging samples really helping?

The authors' claim to include challenging samples in the buffer is to maintain accurate decision boundaries for old tasks (lines 285-286), which should lead to less forgetting. However, in Table 4, the challenging column is not performing better than the random column in BWT, which suggests that the proposed selection mechanism might not be effective in maintaining the decision boundary of old tasks. It also raised the concern that the improvement of the proposed selection mechanism might just be a result of balanced sampling in the memory buffer, which is more or less well-known in the CL community. 

4. Some explanations are missing

In lines 89-90, the implementation of the comparison is not explained, which makes Fig. 1 harder to understand

In lines 266-269, the claim that no task label needs to be stored is confusing. How are the samples arranged separately in the buffer (line 266) if no task label is known? 

The concept of proxy is not clearly explained (lines 182-184)

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes a novel approach called Adaptive Contrastive Replay (ACR) to improve continual learning, specifically focusing on reducing forgetting and enhancing out-of-distribution (OOD) generalization. Existing methods for continual learning often rely on retaining past samples to prevent catastrophic forgetting but struggle with OOD generalization, leading to imbalances and high memory costs. ACR addresses this by using a dual optimization strategy that refines the decision boundary, focusing on informative boundary samples rather than simple memorization. By balancing class and task representation in the memory buffer and leveraging a proxy-based contrastive loss, ACR achieves significantly better stability-plasticity trade-offs and outperforms prior methods on various benchmarks like Split CIFAR-100 and Mini-ImageNet

### Strengths
1. OOD generalization: it combines the robust features of contrastive learning with adaptive memory buffer management to address poor OOD generalization in continual learning.
2. Enhanced Memory Management: The method’s strategy for memory buffer management, which focuses on maintaining a balanced distribution of classes and tasks, helps mitigate the long-tail effect often observed in other methods. This leads to more stable learning outcomes.

### Weaknesses
1. Lack of novelty: The proposed "Proxy-Based Contrastive Loss" is already widely used in Continual Learning, as shown in [1], [2]. Please clarify the unique aspects of your method in comparison to existing approaches.
2. Lack of ablation study: In your paper, you propose using the output of the last layer as an index to estimate image uncertainty, which then guides the management of your memory set. I believe this could help select images near the decision boundary. Based on my experience, combining data augmentation and contrastive learning generally results in significant accuracy improvements in continual learning. Could you specify the performance gain achieved by solely using your memory management method? Additionally, what are the results when other methods are combined with your contrastive learning loss?

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Adaptive Contrastive Replay (ACR), a novel rehearsal-based continual learning method aimed at improving Out-of-Distribution (OOD) generalization while mitigating catastrophic forgetting. ACR leverages proxy-based contrastive learning and confidence-guided sample selection to populate its buffer with boundary samples rather than outliers. This approach balances stability and plasticity, ensuring the retention of old knowledge while adapting to new information. ACR achieves superior performance across multiple benchmarks (Split CIFAR-100, Split Mini-ImageNet, and Split Tiny-ImageNet) in both i.i.d. and OOD settings, outperforming state-of-the-art rehearsal-based methods.

### Strengths
1. Relevant Contribution: Tackles the overlooked issue of OOD generalization in continual learning, which enhances the practical applicability of CL methods.
2. Balanced Stability and Plasticity: Focuses on boundary sample selection, which helps maintain a stable yet adaptive learning process.
3. Efficiency Gains: Reduces computational complexity, making ACR suitable for deployment in resource-constrained environments.
4. Comprehensive Evaluation: Provides comparisons across multiple datasets and with several rehearsal-based baselines, showcasing consistent improvements.

### Weaknesses
1. Narrow Scope of Baselines: The paper compares ACR only with other rehearsal-based approaches, omitting non-rehearsal continual learning methods that could offer additional insights. This limits the understanding of ACR's relative strengths and weaknesses compared to the broader CL landscape, such as regularization-based or architecture-based methods.
2. Over-reliance on Specific OOD Corruptions: The focus on synthetic corruptions (e.g., Gaussian noise, blur) may not fully represent real-world OOD scenarios such as domain shifts or adversarial inputs. The evaluation lacks the complexity of real-world distribution shifts, which can involve more intricate changes in data characteristics.
3. Limited Hyperparameter Analysis: The impact of key hyperparameters like the temperature \(\tau\) and buffer size is not thoroughly explored, leaving some questions about robustness unanswered. A more detailed sensitivity analysis is needed to understand how these parameters affect performance and generalization.
4.Scaling Limitations: There is insufficient discussion about how ACR performs on longer task sequences or more complex datasets beyond the three benchmarks used in the paper. The analysis should include an evaluation of the method's scalability and its performance on more challenging continual learning scenarios.
5. Clarity Issues: Figure 2 is unclear, and key elements (e.g., proxy-based contrastive loss) would benefit from more intuitive explanations. The visualization of the buffer update mechanism needs to be improved for better understanding.
6.Assumptions in Methodology: The paper assumes that high-variance boundary samples will always improve performance, without discussing scenarios where this assumption might fail (e.g., noisy labels or unbalanced datasets). The method's reliance on confidence variance as a proxy for informativeness should be validated under more diverse conditions.

### Questions
1. Figure 2 is unclear. Can the authors provide an improved version or additional explanations to clarify how the buffer update mechanism works?
How would ACR perform under more realistic OOD scenarios such as domain shifts, adversarial attacks, or real-world data variability?
2. What are the computational trade-offs when balancing between boundary and outlier samples? Can ACR scale effectively for larger datasets or continuous tasks?
3. How sensitive is the performance to the temperature parameter ($\tau$) in the proxy-based contrastive loss, and what is the impact of different buffer sizes on the results?
4. Are there any failure cases or situations where ACR struggles, particularly for longer task sequences or when facing noisy or imbalanced datasets?

### Soundness
3

### Presentation
3

### Contribution
3
