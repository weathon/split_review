# Soup to go: mitigating forgetting during continual learning with model averaging

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
In continual learning with pretrained large language models (LLMs), where data from instruction fine-tuning (IFT) tasks arrives in a sequence, fine-tuning on later tasks will often lead to performance degradation on earlier tasks. 
This is especially pronounced when the IFT tasks come from diverse domains.
In this setting, how can we mitigate catastrophic forgetting of earlier tasks and retain what the LLM has learned?
Inspired by a classical continual learning method, L2 penalty to previous weights, we propose Sequential Fine-tuning with Averaging (SFA), a method that merges models with earlier checkpoints trained on previous tasks during the course of training. 
SOTA approaches typically maintain a data buffer of past tasks or impose a penalty at each gradient step. However, our method achieves comparable results without the need to store past data, or multiple copies of parameters for each gradient step. 
Furthermore, our method outperforms penalty methods like L2 regression and EWC, as well as other common merging techniques such as Task Arithmetic, and TIES Merging.
Finally, we show that using our method, a single model can simultaneously perform well on a range of fine-tuning tasks in diverse domains, including Math, Law and Code.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes Sequential Fine-tuning with Averaging for continual learning in LLMs pre-training. The proposed method mitigates forgetting by periodically merging the fine-tuning model with earlier checkpoints trained on previous tasks.

### Strengths
1. The motivation for the proposed methodology is clear: the proposed method reduces forgetting without intensive memory costs for storing past data or multiple copies of previous checkpoints.
2. This paper presents empirical comparisons of the proposed method with regularization-based CL and model merging in LLMs pre-training CL. These results verify the effectiveness of the proposed method.

### Weaknesses
1. The proposed is validated in limited settings: it only tests on 3 or 4 tasks. Moreover, the order of arrival of these 3 or 4 tasks is fixed. This is not practical in continuous learning, where there may be an infinite number of tasks and we have no control over the incoming tasks. The evaluation should include more task sequences with varying orders to demonstrate robustness to different task distributions. Furthermore, the limited number of tasks makes it difficult to assess the long-term performance of the proposed method, especially in terms of catastrophic forgetting.
2. The proposed method can be applied to CV tasks. Thus, it can be tested in CV tasks under more settings and compared with more existing works. However, this paper fails to do so. The paper should include experiments on standard CV benchmarks with established continual learning protocols, such as CIFAR-100 or ImageNet, to better position the method within the broader CL literature. This would also allow for a more direct comparison with existing methods.
3. The performance of the proposed method is inferior to the data replay-based method in most cases. The paper should provide a more in-depth analysis of the trade-offs between the proposed method and data replay, especially in terms of memory usage and computational cost. It is important to understand the scenarios where the proposed method is more suitable than data replay, and vice versa. The current analysis lacks a detailed discussion of these trade-offs.
4. [Minor] In "Model Merging" of related works, the paragraphs have no space between them, making it uncomfortable to read.

### Questions
Can the proposed method be generalized to longer task sequences? If so, I would suggest that the authors use the CIFAR100 or ImageNet datasets to construct task sequences, as is done in existing CL works, and compare the proposed method to more CL baselines.

### Soundness
3

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
This paper introduces the SFA method, designed to address the issue of catastrophic forgetting in the continuous learning process of models. The method does not rely on historical data but instead continuously merging checkpoints from the training process with the original model. SFA is equivalent to L2 regularization to some extent. In the settings proposed in the paper, this method outperforms existing penalty update methods. The paper further analyzes the performance of the SFA method under different merging frequencies.

### Strengths
- The method is simple and easy to understand, which could facilitate practical usage if proven effective.
- The paper compares the method with several existing approaches, validating its effectiveness.

### Weaknesses
 - The overall writing and organization of the paper are unclear in many places. For example:
  1. The reviewer believes that the formula in Algorithm 1 should be $\theta_t = \beta \theta_0 + (1-\beta) \theta_{t-pT}$. The key point of the algorithm, as understood by the reviewer, is to mix the merged and updated model with the original model to maintain performance.
  2. The explanation from lines 154 to 156 is confusing.
  3. The experimental results are introduced starting on page 5, but the related figures are placed on page 7, making the paper difficult to read.
  4. In Figure 1, the legends for L2 and EWC should be dashed lines.
  5. In the series of figures starting from Figure 2, the author attempts to include too much comparative information in a single figure, making them hard to understand.
- The models used in the paper are all the relatively poorly performing Pythia 2.8B, leading to a direct drop in GSM8K accuracy to 0% in some cases. This limits the reliability of the results in these scenarios. The authors are encouraged to conduct experiments on more recent and higher-performing small language models.

### Questions
- Besides linking SFA with L2 penalty, could the reviewer further discuss why SFA significantly outperforms L2 penalty? Are there specific scenarios where one method is more suitable than the other?

### Soundness
2

### Presentation
1

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
This paper concentrates on catastrophic forgetting of pretrained large language model where data from instruction fine-tuning (IFT) tasks arrives in a sequence. To mitigate the forgetting, this paper proposes Sequential Fine-tuning with Averaging (SFA), a method that merges models with earlier checkpoints trained on previous tasks during the course of training. This paper also tries to bridge L2 penalty with model merging technique, which aims to explain why the proposed method works. Finally, experiments are provided to empirically evaluate the proposed method.

### Strengths
1. This paper is well-written and easy to follow.

2. I appreciate the extensive experiments.

### Weaknesses
My main concern is about the proposed method.

1. I think the entire work (including the proposed method) is based on eq.3 which is not correct. Section 4 of this paper try to explain why the proposed method is reasonable by eq.3. According to eq.1, we can obtain the update rule of parameters, i.e. $\theta_{t+1}=\theta _t-\eta(\Delta _{\theta _t}L _{\mathrm{task}} + \theta _t- \theta _o)$. Splitting this update into 2 steps, we obtain eq.2 and $\theta _{t+1}=\theta _{t+1}^*-\eta(\theta _t- \theta _o)$. It is noteworthy that $\theta _{t+1}=\theta _{t+1}^*-\eta(\theta _t- \theta _o)$ is not equal to eq.3, because $\theta _{t+1}^*=\theta _t-\eta \Delta _{\theta _t}L _{\mathrm{task}} \neq \theta _t$. Therefore, eq.3 is not correct.

2. The issue in 1 can not be ignored, because it means that the proposed method in Algorithm 1 is not reasonable. It is a significant mistake.

3. The explanation of SFA as an approximation of L2-regularization is not convincing. L2-regularization applies the penalty term at every gradient step, while SFA only applies the merging step every pT steps. This difference is substantial, as T is typically large, and p is often a small fraction, meaning the frequency of the merging step in SFA is much lower than the regularization term in L2-regularization. The paper lacks a rigorous analysis to justify this approximation, particularly given the significant difference in the frequency of the penalty application. This makes the connection between SFA and L2-regularization weak and not well-supported.


### Questions
1. What is $p$ and $T$ in Algorithm 1? Please provide a more detailed description on the steps of algorithm.

### Soundness
1

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
This paper introduces Sequential Fine-tuning with Averaging (SFA), a method designed to mitigate catastrophic forgetting in pretrained large language models during continual learning by merging earlier checkpoints without requiring data buffers or parameter copies. SFA outperforms traditional penalty methods and merging techniques, enabling effective performance across diverse fine-tuning tasks in areas such as Math, Law, and Code.

### Strengths
This paper investigates an important problem on alliviating the forgetting of LLM during contiually fine-tuning. It shows that an simple technique that averages the model averages can effectively perserve the abilities of different domains.

### Weaknesses
While the paper presents valuable insights, I would like to point out several limitations based on my evaluation:

*   **On the Novelty of Findings**: The use of model averaging (WiSE-FT [1]) to alleviate forgetting has been extensively investigated in prior work [1]. Although this paper claims to extend WiSE-FT to multiple domains, it appears to still average the model checkpoints before and after fine-tuning a new domain, which closely resembles the approach in [1, 2]. Furthermore, many of the results are consistent or overlapped with those found in [2]. Specifically, the core mechanism of averaging pre- and post-fine-tuning weights is not a novel contribution, as this has been explored in the context of continual learning and domain adaptation. The paper does not adequately differentiate its approach from these existing methods, particularly in terms of the specific averaging strategy and its impact on the learned representations.

*   **On the Effectiveness of Model Averaging**: The paper posits that model averaging mitigates forgetting by mimicking L2 regularization towards θ0. However, numerous studies [1, 2] indicate that model averaging is generally more effective than L2 regularization. Therefore, this explanation might not sufficiently account for the observed effectiveness of model averaging. The paper lacks a detailed analysis of why model averaging surpasses L2 regularization in this context, and it does not explore the potential benefits of averaging different layers or parameters. The justification for the observed performance gains is not sufficiently rigorous, and a more in-depth investigation into the underlying mechanisms is needed.

In conclusion, neither the results nor the explanations presented seem particularly novel. Additionally, I would recommend that the paper include a more thorough discussion of existing work, particularly [2], due to the significant overlap in findings.

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
2
