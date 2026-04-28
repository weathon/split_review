# SIEVE: General Purpose Data Filtering System Matching GPT-4o Accuracy at 1% the Cost

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Creating specialized large language models requires vast amounts of clean, special purpose data for training and fine-tuning. With only a handful of existing large-scale, domain-specific datasets, creation of new datasets is required in most applications. This requires the development of new application-specific filtering of web-scale data. Filtering with a high-performance, general-purpose LLM such as GPT-4o can be highly effective, but this is extremely expensive at web-scale. This paper proposes \name, a lightweight alternative that matches GPT-4o accuracy at a fraction of the cost. \name can perform up to 500 filtering operations for the cost of one GPT-4o filtering call. The key to \name is a seamless integration of GPT-4o and lightweight T5 models, using active learning to fine-tune T5 in the background with a small number of calls to GPT-4o. Once trained, it performs as well as GPT-4o at a tiny fraction of the cost. We experimentally validate \name on the OpenWebText dataset, using five highly customized filter tasks targeting high quality and domain-specific content. Our results demonstrate the effectiveness and efficiency of our method in curating large, high-quality datasets for language model training at a substantially lower cost (1\%) than existing techniques. To further validate \name, experiments show that \name and GPT-4o achieve similar accuracy, with human evaluators preferring \name's filtering results to those of GPT-4o.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces SIEVE, a cost-effective system for high-quality data filtering that achieves results comparable to GPT-4o while operating at just 1% of its cost. SIEVE employs a T5-based binary classification model to replicate GPT-4o’s filtering decisions, classifying text snippets as relevant (pass) or irrelevant (fail). To minimize expenses, SIEVE integrates an active learning approach that selectively queries only the most informative snippets for labeling by GPT-4o. This targeted approach reduces the need to label every snippet, gathering only the most valuable samples. Each batch of GPT-4o-labeled data is used to periodically fine-tune the T5 model, progressively improving its accuracy in replicating GPT-4o’s filtering.

To address class imbalance—where the majority of snippets may not meet filtering criteria—the active learning algorithm incorporates a True Risk Minimizer (TRM) threshold. Unlike traditional uncertainty sampling, which uses a fixed 0.5 threshold and can over-represent the majority class, the TRM threshold dynamically adjusts to balance samples from both majority and minority classes around the decision boundary. This design ensures a more balanced labeled dataset, reducing the risk of model bias. The TRM threshold is approximated using a high-confidence interval, updated iteratively as new snippets enter in a streaming format, allowing the model to query only the most promising samples.

This efficient and adaptive approach enables SIEVE to create a balanced and accurate training set for the T5 model with minimal reliance on costly GPT-4o queries. The result is a scalable, high-accuracy filtering system that optimizes computational resources and cost, making SIEVE well-suited for large-scale data filtering applications in training language models.

### Strengths
1. The methodology is sound. Incremental fine-tuning and the TRM threshold enhance efficiency, though testing on more diverse datasets would better demonstrate generalizability.

2. SIEVE’s cost-efficient filtering method is impactful for large-scale data filtering, achieving GPT-4o-level quality at minimal cost.

### Weaknesses
 **1. Limited exploration of diverse datasets.**

An area where SIEVE could improve is in testing across a broader range of datasets. While the OpenWebText dataset provides a good baseline for evaluating filtering performance, testing SIEVE on datasets with varied writing styles, content types, or noise levels would offer a clearer picture of its versatility. For instance, it would be helpful to see how SIEVE performs on datasets with different imbalance ratios or topics to understand whether the TRM threshold effectively adapts to various content structures and domain-specific challenges.

**2. Baseline limitations.**

Although SIEVE is compared to GPT-4o, adding baselines with more straightforward methods (e.g., T5-based filtering or basic binary classifiers without active learning) would give a clearer insight into SIEVE's improvements. This would help show how much each part—like the active learning framework and TRM threshold—contributes to its performance. If a basic T5 model alone performs comparably, it could suggest that the added complexity of SIEVE may not be necessary. Including T5 as a baseline would help clarify whether SIEVE’s specific design choices are essential for its performance improvements or if similar results could be achieved with a more straightforward approach.

**3. Unclear writing.**

The paper does not provide details on how the sigmoid score is calculated for determining snippet relevance. Since the TRM threshold relies on the sigmoid score to identify the informative samples, it’s necessary to provide a clear explanation of how the model and approach are used for calculating this score.

### Questions
1. Would it be possible to include comparisons with simpler filtering methods, like T5-based classifiers?

2. Has SIEVE been tested on domain-specific datasets (e.g., medical or scientific)? If not, could you discuss any anticipated adjustments needed to maintain performance in these areas?

3. Could you clarify the model or method used to calculate the sigmoid score necessary for determining the TRM threshold?

### Soundness
3

### Presentation
2

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
The authors present SIEVE, a cost-efficient data filtering approach that uses stream-based active learning and reduces the number of filtering calls to costly models( in this case, gpt4) in favor of a lighter, finetuned model (T5). This approach reduces the cost to 1% while maintaining a similar accuracy to gpt4 on the OpenWebText dataset using five filter tasks.

### Strengths
This paper studies the high cost of using large models such as gpt4. This is a fascinating topic and should be studied more. That being said, these are some of the strengths of this paper:
1. Theoretical Analysis: This paper's strength is its addition of a theoretical section that provides a rigorous analysis of the balancedness bound for the TRM threshold.
2. Human Evaluation: The paper doesn't only consider gpt4 as the golden truth but also uses human evaluation to validate the results, which  strengthens the author's point.
3. Clear layout of the approach: The active learning approach is clearly presented and easy to understand.

### Weaknesses
Here are some places for improvement:
1. A detailed discussion on how $B$  from algorithm A was chosen and how it affects the performance. It is unclear how the batch size $B$ impacts the trade-off between the frequency of lightweight model retraining and the accuracy gains from active learning. A more thorough analysis should explore how different values of $B$ affect the convergence rate and the final performance of the filtering tasks. For instance, how does a smaller $B$ (e.g., 500) compare to a larger $B$ (e.g., 5000) in terms of the number of GPT-4 calls and the final accuracy achieved? This analysis should also consider the computational cost of retraining the lightweight model for different batch sizes.
2. The impact of model size on performance is not studied. Given that only T5 was used for experiments, I wonder how choosing a different model architecture or size would affect the performance both in terms of accuracy and cost (in terms of gpt 4 calls). It is important to investigate how the performance of SIEVE scales with different lightweight model architectures and sizes. For example, how would a smaller model like DistilBERT or a larger model like a T5-XXL impact the overall cost and accuracy? This analysis should include a comparison of the training time, inference speed, and the number of GPT-4 calls required for different lightweight models. Furthermore, it should explore whether the optimal lightweight model size is task-dependent.
3. Are the legends for Figure 4 flipped? It looks like Active learning requires more queries. 
4. How are you selecting the upper and lower bounds? Are there examples of values for those upper bounds for a specific filter? The paper should provide more clarity on how the upper and lower bounds for the TRM threshold are determined. While the paper mentions the empirical Bernstein bound, it lacks specific examples of how these bounds are calculated and how they vary across different filters and iterations. Providing concrete examples of the upper and lower bound values for a specific filter at different stages of active learning would greatly enhance the reader's understanding.

### Questions
1. Why did you choose T5 specifically? 
2. Have you considered any tasks beyond filtering that could benefit from your approach? Generalizing this to involve more tasks would be highly beneficial.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes SIEVE for filtering web-scale data for the creation of clean datasets.
SIEVE utilized GPT-4o and proposed an active learning and knowledge distillation pipeline to distillate knowledge to lightweight T-5 Model for more cost-efficient filtering. SIEVE achieved comparable performance as GPT-4o on filtering OpenWebText dataset and with approximately 1% of the cost.

### Strengths
- The paper provides formal proofs and theoretical guarantees for their active learning algorithm's performance, particularly regarding class balancedness.
- The approach to filtering data for dataset creation is crucial for many LLM and DL tasks.
-  Achieves comparable performance to GPT-4o at with much less cost

### Weaknesses
 - The system's performance is bounded by GPT-4o's capabilities and inherent inconsistencies
- The evaluation is a little bit limited and only conducted on OpenWebText 
- The filtering is distillate from another LLM, so it's hard to guarantee the filtering robustness and fairness. 
- While the paper demonstrates effectiveness on OpenWebText, but sounds like lacks novelty and it's combining of active learning with knowledge distillation.

### Questions
- The 1% cost compared to GPT-4o, my understanding is that you considering only inference cost, how about the whole training and active learning cost of the T-5 model?
- The human evaluation was conducted only on cases where GPT-4o and the lightweight model disagreed. But there still have possibility that both models make mistakes. Wouldn't it be more comprehensive to also evaluate a random sample of cases where they agreed?
- Why choose the T-5 model, and how was this architectural choice made? Shouldn't decoder-only architecture be more efficient in dealing with such filtering tasks, which has much higher throughputs?
- Given that your approach relies on GPT-4o's chain-of-thought reasoning, I am concerning about the reliability and of the LLM output. Probably authors may considering multi-agent (multi prompts) ensemble as the base teacher model.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The SIEVE system is designed to make large-scale data filtering more cost-effective by leveraging GPT-4o’s high-quality filtering capabilities as a guide for fine-tuning a more efficient, lower-cost T5 model. SIEVE's goal is to minimize reliance on GPT-4o by enabling T5 to approximate GPT-4o's filtering decisions, thus reducing computational costs.

### Strengths
+The paper addresses an important and practical challenge in the community: domain-specific data filtering.

+It introduces a TRM threshold approximation method to ensure balanced and informative data selection, effectively mitigating potential bias induced by class imbalance in datasets.

+The proposed approach is comprehensively validated across five datasets, comparing the performance and cost-effectiveness of GPT-4o and a lightweight T5 model.

+Theoretical support is provided to demonstrate the balance of labeled snippets, strengthening the method’s foundation.

More specifically: 

SIEVE uses an active learning approach to select the most informative samples for GPT-4o annotation. Rather than using all available data, SIEVE prioritizes examples based on T5’s uncertainty in predictions. This uncertainty is measured with a True Risk Minimizer (TRM) threshold, which targets samples near the model’s decision boundary (i.e., where T5’s confidence is low). Selecting samples around this threshold ensures balanced, informative data that challenges the model, improving generalization without overwhelming it with redundant or obvious examples.

Recognizing that datasets can be imbalanced. Specifically, in filtering tasks, “fail” samples often outnumber “pass” samples. To address this issue, SIEVE implements a class-balanced sampling strategy. This approach uses the TRM threshold to select samples from both classes near the decision boundary, and ensures that training data has sufficient representation from both “pass” and “fail” classes, preventing T5 from becoming biased towards majority-class predictions.

### Weaknesses
-Fine-tuning is conducted incrementally with new batches of informative data labeled by GPT-4o, rather than retraining on a combined dataset that includes original T5 training data. In other words, SIEVE does not use the original T5 dataset during fine-tuning; instead, it focuses exclusively on samples curated through GPT-4o labeling. Will this approach cause potential catastrophic forgetting?

-The paper has several errors or unclear statements that could be misleading. For instance, in the last paragraph of Section 2.1, the authors mention training the T5-decoder, but in other sections, the T5-encoder is referenced. Additionally, in Figure 4, the legends for 'Random' and 'Active (SIEVE)' appear to be swapped. The meaning of the two 'SIEVE (Ours)' results for the Politics Filter in Table 2 is also ambiguous.

-There may be a disconnect between the goal of approximating the TRM threshold (and the interval of the confidence set) and the actual training methodology. While the approximation aims to balance the probabilities of majority and minority classes within the interval, the real training data may still be imbalanced due to sample distribution. If focal loss is employed to address this imbalance, it raises questions about the necessity of estimating the confidence set interval. Furthermore, the method of determining the alpha parameter in focal loss remains unclear. Using the imbalance ratio from randomly sampled snippets as alpha may not be appropriate or feasible in practical applications.

### Questions
1. What impact would training the model using a fixed sigmoid threshold of 0.5 have on the performance of the lightweight model? Could it degrade the model's effectiveness?
2. How does the upper and lower bound of the confidence set interval change throughout the training process? Could it lead to a situation where data samples selected as informative at the start of training fall outside the updated confidence interval, resulting in the model including less informative samples over time?
3. How is the initial labeled set in Algorithm 1 obtained? Is it initialized as an empty set, or is there a specific strategy for selecting the initial samples?
4. Do you only use (snippet, annotation) pairs to train the model or include the prompt as part of the input?

### Soundness
3

### Presentation
3

### Contribution
3
