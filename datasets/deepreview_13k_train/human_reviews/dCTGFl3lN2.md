# Improving Influence-based Instruction Tuning Data Selection for Balanced Learning of Diverse Capabilities

- Decision: Reject
- Scores: 8, 3, 3, 3

## Abstract
Selecting appropriate training data is crucial for successful instruction fine-tuning, which aims to (1) elicit strong capabilities from pretrained large language models (LLMs), and (2) achieve balanced performance across a diverse range of tasks. Algorithms based on influence estimation have shown promise in achieving (1) through estimating the contribution of each training example to model's prediction on a downstream task, but they often struggle with (2). Through systematic experiments, we attribute their underperformance to an inherent bias---certain tasks intrinsically have greater influence than others. Directly comparing influence scores across different tasks would thus bias the selected data towards these tasks, hurting the LM's performance not only on other capabilities, but also, surprisingly, on the tasks for which the selected data has high influence.

To address this issue, we propose BIDS, a Balanced and Influential Data Selection algorithm.  BIDS first normalizes influence scores of the training data with respect to each downstream task at an instance level. It then applies an iterative process to further balance the selection of influential training data. At each step, BIDS selects the training example that bears the highest influence on the most underrepresented capability by the currently selected data. We perform comprehensive experiments using both Llama-3 and Mistral-v0.3 on seven evaluation benchmarks spanning five diverse capabilities. Results demonstrate that BIDS consistently outperforms both state-of-the-art influence-based data selection algorithms and other non-influence-based selection frameworks under various budgets. Surprisingly, training on a 15% subset selected by BIDS can even outperform full-dataset training with a much more balanced performance across different tasks. Our analysis further highlights the importance of both instance-level normalization and iterative optimization of selected data for balanced learning of diverse capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces BIDS (Balanced Influence-based Data Selection), an algorithm for improving the balance and performance of LLMs across diverse tasks during supervised instruction tuning. Traditional influence-based methods often skew data selection toward tasks with inherently higher influence scores, leading to unbalanced model capabilities. BIDS addresses this by normalizing influence values at the instance level and applying an iterative selection process that prioritizes data for underrepresented tasks. Experimental results show that BIDS achieves more balanced performance across tasks like coding, logic, math, and instruction-following.

### Strengths
1. strong results with only 15% of the dataset, keeping up with full-dataset training, demonstrating its potential for resource-efficient tuning of LLMs.
2. Comprehensive across diverse tasks (coding, logic, math, and instruction-following), showing consistent improvements over baseline methods, which strengthens the validity of its balanced selection approach.

### Weaknesses
The paper primarily focuses on specific tasks and one model (Llama-3-8B). Testing BIDS on a broader range of models (different families and sizes) and larger task sets would help assess its scalability and generalization. The evaluation also lacks a detailed analysis of the computational overhead introduced by the influence estimation process, which could be a significant factor in practical applications. Furthermore, the paper does not explore the sensitivity of BIDS to the choice of hyperparameters, such as the number of iterations or the normalization method, which could affect the final performance and balance achieved.

### Questions
How robust is BIDS to noise or inaccuracies in influence score estimation? Could variations in influence scoring across tasks impact the balance achieved, and have any measures been taken to address potential score biases?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies selecting suitable training data for supervised instruction fine-tuning (SFT) of pretrained LLMs. Specifically, this paper focuses on the strategy of iterative balanced selection based on the influence score between training and validation samples, named BIDS. BIDS first normalizes influence scores per task and iteratively selects training data that maximally enhances underrepresented capabilities. They provide several analyses and ablations to validate the effectiveness of core components and motivations of their approach.

### Strengths
Pointing out the necessity of balanced sampling for recent instruction tuning datasets, which usually consist of multiple distinctive tasks.

### Weaknesses
The reviewer agrees that the balanced selection should be meaningful for the multitask instruction tuning dataset.

However, the observations and discussions provided in the paper seem to be limited and less rigorous than the reviewer expected.

1. limited contribution: I understand this work as a LESS method, but I draw each sample iteratively for balance, which sounds more like an ad-hoc engineering technique for LESS. Evaluation with a single LLM backbone and single 'meaningful' baseline doesn't give me meaningful insights throughout the paper.

2. limited analysis: The most straightforward setting for balanced sampling should be to select the same number of influential samples of each training dataset (i.e., task) from the corresponding validation set (i.e., task-specific LESS selection). However, there is no comparison or discussion. Also, the impact of influence score from validation sets from a task to training samples from other tasks is not discussed, which may provide further insights on balanced sampling for underrepresented tasks.

3. marginal performance improvement: performance improvement is limited. For example, in Table 2, under a 5% budget, there is a 0.4% improvement from simple *sum*. Under 15% sample budget, it also shows 0.4% improvement against *random*. Considering the randomness of selecting validation samples and stochastic training, it looks almost like random fluctuation within the variance.  In addition, in Table 1, I wonder why the gap between the random selection and LESS has a marginal performance difference, which is quite hard to understand considering the report of the original LESS paper showing significant performance gain from random selection. This paper uses LLAMA3 (LESS uses llama2-7B, llama2-13B, and mistral-7B), but not sure this is the only reason for this. 

4. limited experiments: this paper uses only one LLM backbone (llama3-7B) and uses only one meaningful baseline - LESS. More extensive comparison under the various LLM backbones following LESS paper and including various types of data pruning/selection papers, including a balanced or density-based selection approach, should be needed.

### Questions
Please see the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new data selection method for instruction tuning of LLMs to achieve better performance while using less data. The method proposed is BIDS, which normalizes influence scores per task and iteratively selects the most influential data for underrepresented capabilities, ensuring a balanced selection across different tasks. Experiments on LLama3 show that BIDS achieves better performance on UltraInteract benchmark over several baselines.

### Strengths
1. The writing is clear and easy to follow.
2. After using the proposed data selection algorithm, the performance is better than using all data on some benchmark.

### Weaknesses
1. The algorithm design lacks enough novelty. It simply modifies the original LESS algorithm by adding a instance-level normalization to the attribution matrix. The modification, while effective, appears to be a relatively straightforward application of normalization techniques rather than a fundamentally new approach to data selection. The core idea of using influence scores remains the same, and the added normalization does not introduce a significant conceptual leap.
2. The paper does not well explain why using a balanced data selection can leads to better performance. And why using less data can leads to better performance than using all data for training. (Why excluding less "Influence" data can leads to better performance.) The paper lacks a rigorous analysis of the underlying mechanisms that cause the observed performance gains. Specifically, it does not explore the potential for negative transfer from less influential data points, nor does it investigate the role of data redundancy in the full dataset. A more detailed discussion of these factors is needed to justify the effectiveness of the proposed method.
3. The algorithm needs to maintain a |d| &times; |V| matrix, which is not efficiency when the dataset is large. The computation cost of the proposed algorithm needs to be discussed in the paper. The paper should include a more thorough analysis of the computational complexity, including both time and memory requirements, especially when scaling to larger datasets. The current discussion is insufficient, and concrete benchmarks are needed to demonstrate the practical feasibility of the method.
4. Authors should compare their results with other SOTA data selection algorithms to prove their effectiveness, instead of just comparing different variant of Influence-based instruction tuning data selection. The paper's evaluation is limited by its focus on comparing only different variants of influence-based data selection. To establish the true value of the proposed method, it is essential to compare it against other state-of-the-art data selection techniques, including those not based on influence scores.

### Questions
What is the ratio for dividing the data into training, validation, and test sets?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes BIDS, a data-selection algorithm designed to address the inherent bias in existing influence-based data selection methods for instruction tuning of large language models. Build upon the previous work LESS, they first apply instance-level normalization on the influence scores, then utilize an iterative selection algorithm to identify influential samples while maintaining a balance between tasks.

### Strengths
- Overall, the writing is clear and easy to follow, and the problem setup is well-defined.
- The paper provides a detailed analysis of the limitations of previous work.
- Experimental results demonstrates the propose method's effectiveness across the selected baselines (however, see weaknesses).

### Weaknesses
 - This proposed is somewhat incremental, with limited technical contributions. It heavily relies on the previous work LESS, with the primary contributions being instance-level normalization and an “iterative” selection algorithm. However, normalization is already well-explored in ML, and the iterative selection is very similar to “maximal marginal relevance"[1]. The paper does not sufficiently articulate the novelty of their approach beyond these known techniques. The core idea of balancing relevance and diversity through iterative selection is not new, and the specific implementation lacks a strong justification for its unique contribution.

  - Experiments are insufficient. There is no direct comparison between the proposed method and its previous work, LESS, or other data selection methods. The selected baselines are naive. Additionally, experiments are limited to LLaMA-3-8B, leaving the generalization capacity of the proposed method unproven. The absence of comparisons with other state-of-the-art data selection techniques makes it difficult to assess the true value of the proposed method.

- The experimental results are not very convincing. The performance of the proposed method is worse than the random baseline on some benchmarks, and there is no clear clarification or explanation in the paper. Besides, there are some presentation issues in table 2. It is misleading to "bold" the results if it outperforms two baselines (even if it is specified in the caption). In addition, results for the 5% budget and 15% budget on MMLU should not be bolded.

### Questions
- Why do you call it "instance-level" normalization? Can you provide some more comparisons between different normalization methods?
- Can you provide additional results on different LLMs (e.g. Mistral-7B, LLama-2-7B/13B as used in LESS)? It might better demonstrates the generalization of the proposed method.
- Can you provide some examples (LLM response) to show that the proposed method is better for balancing across tasks?

### Soundness
2

### Presentation
2

### Contribution
1
