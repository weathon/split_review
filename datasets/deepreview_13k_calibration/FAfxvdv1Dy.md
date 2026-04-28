# STAFF: Speculative Coreset Selection for Task-Specific Fine-tuning

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Task-specific fine-tuning is essential for the deployment of large language models (LLMs), but it requires significant computational resources and time.
Existing solutions have proposed coreset selection methods to improve data efficiency and reduce model training overhead, but they still have limitations:
\ding{182} Overlooking valuable samples at high pruning rates, which degrades the coreset's performance.
\ding{183} Requiring high time overhead during coreset selection to fine-tune and evaluate the target LLM.
In this paper, we introduce \sys, a speculative coreset selection method.
\sys leverages a small model from the same family as the target LLM to efficiently estimate data scores and then verifies the scores on the target LLM to accurately identify and allocate more selection budget to important regions while maintaining coverage of easy regions.
We evaluate \sys on three LLMs and three downstream tasks and show that \sys improves the performance of SOTA methods by up to 54.3\% and reduces selection overhead by up to 70.5\% at different pruning rates.
Furthermore, we observe that the coreset selected by \sys at low pruning rates (\ie, 20\%) can even obtain better fine-tuning performance than the full dataset.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes an improved coreset selection method for task-specific fine-tuning of LLMs which consists of two stages: speculative score calculation by leveraging a small LLM of same structure, and LLM verification and selection which dynamically allocate selection budgets for easy and difficult regions of data samples. The authors demonstrate the effectiveness and efficiency of their proposed method by comparing to five SOTA selection methods, including random, GraNd, EL2N, CCS, and D2 Pruning, on three different tasks, including BioInstruct (QA), DialogSum (summarization), and WMT-19 (translation), for three different LLMs, including Gemma-7b, Llama-2-13b, and Mistral-Nemo-Instruct-2407. The results show the proposed method outperforms other baselines by a significant margin.

### Strengths
1. In general this paper is well-written and the authors demonstrate their methodology in a clear way. The experimental part of this paper is also persuasive with broad ranges of tasks, models, and comparison with different baselines. 

2. Although speculative decoding is well-defined and applied for optimizing LLM decoding, incorporating this approach for coreset selection can not only broaden the scope of application, but also fosters creativity and novel insights.

3. An effective and efficient coreset selection method is indeed important for real-world LLM applications. If the proposed approach can be generalized for a broad range of tasks and models, it could be of great significant for building new applications based on LLMs.

### Weaknesses
1. Although the authors show extensive experimental results, it will be of great significant to show if the proposed method can be scalable for different model sizes, especially for bigger models.

2. Some parts of this work should be clarified. Please refer to my questions.



### Questions
1. I'm a bit concerned on maintaining the diversity of the coreset data. Basically the authors utilize the scores estimated from a smaller model to split the dataset into different regions which represent the diverse distribution of the data. The authors only update their estimation of importance during the verification stage without any modification of the regions. Could the authors quantify the difference of diversity estimated by the small and the target models?

2. It seems their is no ablation study estimation better combination of small and target models, e.g. how small the small model could be to make it more efficient?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel method for improving the efficiency of large language model (LLM) fine-tuning by reducing the computational resources and time required. The authors propose STAFF, a speculative coreset selection method that leverages a small model from the same family as the target LLM to estimate the importance of data samples. This approach allows for the identification of important data regions while maintaining diversity, leading to a more efficient selection process with lower overhead. The paper evaluates STAFF on three different LLMs and three downstream tasks, demonstrating that it can improve the performance of state-of-the-art methods by up to 54.3% and reduce selection overhead by up to 70.5% at various pruning rates.

### Strengths
The paper presents a creative solution to the problem of resource-intensive fine-tuning of LLMs by introducin a speculative coreset selection method coreset.

The paper demonstrates that STAFF can reduce the selection overhead by up to 70.5% compared to other methods, which is a substantial improvement for practical applications where time and computational resources are critical.

The proposed method can selected the important samples (and also the important sample for the target LLM) while keeping the diversity.

### Weaknesses
The effectiveness of STAFF relies heavily on the small model's capability to estimate the importance of data samples accurately. If the small model is not sufficiently capable, the coreset selection may not be effective.

For the gradient used in paper, the gradient of small LLM is from a LLM that has been finetuned. However, the gradient of target LLM is from a LLM that is not finetuned. Those two gradient might not be comparable for the calculation of Verification score. Maybe a sample that is hard for a small LLM is easy for a larger LLM?

### Questions
Is there result for more tasks?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents an efficient coreset selection algorithm for LLMs which is performant at high pruning rates. The key ideas are to 1) use a smaller LLM from the same model family as the larger LLM to compute an example score and verify that score using the larger LLM, and 2) allocate selection budget to regions which are more important for the target LLM.  Results on Gemma-7b, Llama-2-13b and Mistral-Nemo show that the method can outperform other baselines at both high and low pruning rates (up to 54.3%) with a lower time overhead (up to 70%).

### Strengths
* Presents an approach for core set selection which is both performant and efficient compared to existing baselines
* Demonstrates improvements in performance and time-overhead for three LLMs across a range of pruning rates
* Presents ablations showing the role of each component (verification step, smaller model, smaller model from a different family)

### Weaknesses
 * Some parts of the paper are hard to follow. See questions below.
Note: The authors have addressed the clarity issues in their updated version.

### questions:
 Questions
* It is hard to decipher whether the target LLM (\theta_t) used in verification (Step 10 in Algorithm 1) is a fine-tuned model. Algorithm 1 suggests that it is not fine-tuned but it would be good if this can be clarified.
* L184 says: "without extensive fine-tuning of the target LLM." Does this imply that some fine-tuning was done? Please clarify.
* L247 says: "After selecting and fine-tuning θs, we introduce the effort score ". It looks like the effort score was computed after fine-tuning the smaller LLM and prior to data selection. Please clarify. 
* Table 1: It would be useful to report the performance of the fine-tuned small LLM used in coreset selection.

Typos:
* L045: are difficult -> have difficulty
* L297: 'use' -> 'uses'
* L731: 'baslines' -> 'baselines'

### Questions
Questions
* It is hard to decipher whether the target LLM (\theta_t) used in verification (Step 10 in Algorithm 1) is a fine-tuned model. Algorithm 1 suggests that it is not fine-tuned but it would be good if this can be clarified.
* L184 says: "without extensive fine-tuning of the target LLM." Does this imply that some fine-tuning was done? Please clarify.
* L247 says: "After selecting and fine-tuning θs, we introduce the effort score ". It looks like the effort score was computed after fine-tuning the smaller LLM and prior to data selection. Please clarify. 
* Table 1: It would be useful to report the performance of the fine-tuned small LLM used in coreset selection.

Typos:
* L045: are difficult -> have difficulty
* L297: 'use' -> 'uses'
* L731: 'baslines' -> 'baselines'

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents a novel method called STAFF for efficient and effective coreset selection in task-specific fine-tuning of large language models (LLMs). The paper claims to address two challenges from existing coreset selection methods: (1) Balancing data importance and diversity across pruning rates. (2) High overhead from the need to train the target LLM for several epochs to evaluate data scores and regions during selection.

The proposed STAFF method leverages similar ideas from speculative decoding to do speculative score calculation using small models and verification score from big models. A selection budget is calculated for each region based on the verification result, allocating more budget to regions deemed important to the target LLM while ensuring coverage of diverse data regions. 

Experiment Results demonstrate that STAFF outperforms state-of-the-art coreset selection methods in both performance and efficiency across various pruning rates, LLMs, and downstream tasks

### Strengths
1. The experiment results look strong. The paper also includes detailed ablation studies.
2. The paper emphasizes reproducibility by providing access to the code and data used in the experiments.

### Weaknesses
1. The paper has limited incremental innovation on top of the work [Zhengetal.(2023)]"COVERAGE-CENTRIC CORESET SELECTION FOR HIGH PRUNING RATES". The [Zhengetal.(2023)] already did the research into the data importance and data diversity issue. This paper basically follows the similar way as [Zhengetal.(2023)] but with focus on the speculative implementation.
2. The paper doesn't have comprehensive related work study. For example, "Mods: Model-oriented data selection for instruction tuning" and 
"Maybe only 0.5% data is needed: A preliminary exploration of low training data instruction tuning" also explored the small model for coreset selection. Given these two work already using small models for data selection. It might be helpful to discuss the difference of this paper with the above two papers. 
3. The paper misses some theoretical analysis and proof for the equation (2)? For example, is that possible to define some theorem to get the connection of the equation (2) with loss?

### Questions
How does the equation (2) come from? 
Why not apply some normalization method for each weight change? For example, each weight difference normalized by the average of weight difference in each matrix or each layer.
Did you observe weight difference distribution across different layers?

### Soundness
3

### Presentation
3

### Contribution
3
