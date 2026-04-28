# CABS: Conflict-Aware and Balanced Sparsification for Enhancing Model Merging

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 6, 5

## Abstract
Model merging based on task vectors, i.e., the parameter differences between fine-tuned models and a shared base model, provides an efficient way to integrate multiple models without retraining. This approach can be used to combine task-specific models into a multitask model, improve generalization, or address model deficiencies. One of the significant challenges faced by model merging is the conflicts between task vectors. Existing works aim to mitigate these conflicts through sparsification; however, two issues observed in our experiments significantly limit their performance: $\textit{high parameter overlap}$ and $\textit{unbalanced weight distribution}$. To address these issues, we propose a simple yet effective framework called CABS (Conflict-Aware and Balanced Sparsification), consisting of $\textbf{C}$onflict-$\textbf{A}$ware Sparsification (CA) and $\textbf{B}$alanced $\textbf{S}$parsification (BS). CA can reduce parameter overlap by applying masks during sequential pruning, ensuring that each task vector retains distinct, non-overlapping parameters. BS leverages $n$:$m$ pruning to preserve critical weights while maintaining an even distribution across layers. Our comprehensive experiments demonstrate that CABS outperforms state-of-the-art methods across a range of diverse tasks and model sizes. Notably, in experiments with 7B-parameter language models, CABS surpasses the average performance of an "ideal" model, a virtual model that selects the highest score from individual fine-tuned models for each task (CABS: 76.50 vs. Ideal Model: 76.30 vs. Baseline: 76.02 vs. Fine-tuned Model: 75.86). Our results highlight the importance of addressing both high parameter overlap and unbalanced weight distribution to achieve robust and high-performance model merging.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents CABS (Conflict-Aware and Balanced Sparsification), a framework designed to address two key challenges in model merging: parameter overlap and unbalanced weight distribution. The framework consists of two main components:

- CA: A sequential pruning approach that reduces parameter overlap between task vectors
- BS: An n:m pruning strategy that maintains balanced weight distribution

The authors evaluate CABS on both large-scale models (Mistral-7B) and smaller models (RoBERTa), demonstrating improvements over existing methods, particularly at high sparsity levels (0.75). The method achieves better performance than an "ideal" model baseline on some tasks, though improvements are modest.

### Strengths
- Novel perspective on handling conflicts in model merging
- Simple but effective solution
- Practical value demonstrated in experiments- Clear problem formulation with empirical validation
- Comprehensive ablation studies
- Results generally support main claims
- Reasonable experimental design and evaluation metrics
- Well-organized structure with clear flow
- Good visualization of key concepts (Fig. 1)
- Detailed experimental results

### Weaknesses
Theoretical Foundation:

- No mathematical derivation or proofs
- Lack of mechanism analysis
- Missing theoretical basis for n:m ratio selection

Experimental Design:

- Limited model coverage (only Mistral and RoBERTa)
- Missing statistical significance analysis for Small model like RoBERTa
- Insufficient variance analysis across seeds
- Incomplete baseline comparisons
- Small performance improvements


Technical Limitations:

- Only applicable to homogeneous models
- Multi-task vector case not addressed
- Insufficient analysis of computational overhead
- Unknown performance on larger models (>7B)
- Simple linear combination for merging

### Questions
Theoretical:


- Can you provide some theoretical proof or analysis for why reducing parameter overlap improves performance?

Technical:

- How would the method extend to merging multiple (>3) task vectors?
- What is the impact of different pruning orders on final performance?
- How do you determine optimal n:m ratios for different model sizes?
- Why choose simple linear combination when there are more sophisticated approaches available, such as Fisher Information-based merging, gradient-based adaptive weighting, or attention-based parameter fusion? Have you considered incorporating these methods to potentially improve the merging performance? 


Experimental:

- Why weren't other major architectures (LLaMA, GPT) tested?
- Can you provide complete computational and memory overhead analysis?
- How does the method perform on cross-architecture merging?


Scalability:

- How would the method perform on larger models (30B+)?
- How does computational complexity scale with number of task vectors?

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
5

### Summary
This paper presents a new model merging approach called CABS. CABS has two steps: 1) Conflict-Aware sparsification (CA), which essentially applies masks sequentially during weight pruning for different tasks to avoid parameter conflicts. 2) Balanced sparsification (BS), which leverages existing n:m pruning technique to maintain weight balancing. Experiment results on both encoder-only and decoder-only models demonstrate the effectiveness of the proposed approach.

### Strengths
Model merging is a promising field in terms of compositing LLM capabilities without retraining.

### Weaknesses
The proposed method is very ad-hoc, and the improvement seems not that convincing. In particular:
- CA is simple, but questionable. However, what if you exchange the pruning order to task B first and then task A? The resulting model will not be equivalent, right? Also, what if you have > 2 models to merge? The later tasks will almost aways has less effective weights to be pruned from.
- CA can be combine with any pruning technique, I do not see why BS here is a particularly good pruning option. n:m pruning is a paper from 2021, and there are multiple state-of-the-art pruning techniques recently. While the paper empirically proves BS is better than basic magnitude based pruning, what about other advanced pruning techniques (e.g., https://arxiv.org/pdf/2305.11627). If CA + any pruning technique better than n:m pruning results in better performance, then we should not over-sell the importance of BS.
- The improvements are small compared to competing methods, what are the confidence intervals of these results?
- Sparsification is only a necessary for pruning-based model merging techniques. That said, I would like to see how the method compares against other categories of model merging techniques such as evolutionary model merge (https://arxiv.org/abs/2403.13187) and pack of llms (https://arxiv.org/abs/2404.11531).

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work introduces model merging based on task vectors, aiming to address high parameter overlap and unbalanced weight distribution through n:m pruning and inverse masks.

### Strengths
* Adopting n:m pruning and inverse masks to sparsify task vectors is an interesting approach. 
* The method is simple and straightforward. 
* Analyzing the impact of different overlap rates on performance in Figure 4 is insightful.
* Overall, this paper is well-written and easy to follow.

### Weaknesses
 * Since sequential pruning is utilized, I believe the task order could impact performance. For instance, extracting the mask for task A and then using its inverse mask for task B might yield different results compared to extracting the mask for task B and using its inverse mask for task A. Could the authors analyze this aspect?

* Additionally, I am uncertain about the rationale behind the inverse mask strategy. When extracting the mask for task A and then using its inverse mask for task B, the inverse mask may remove important patterns for task B, as it is derived without consideration of task B. Could the authors provide a theoretical explanation and/or a more detailed analysis to justify this method?

* Magnitude and random pruning are commonly regarded as baselines in network compression literature. What might happen if alternative pruning criteria, such as the geometric median criterion (https://arxiv.org/abs/1811.00250), were used instead?

* The score improvements in Tables 2 and 3 appear quite marginal compared to the baselines, and the results are not particularly compelling. Additionally, I believe it would be helpful to include the score of the pretrained model before fine-tuning to better understand the influence of the base model (W_base​ in Algorithm 1).

* It would be helpful to present results from merging 3–5 models and compare them with the baselines to demonstrate the scalability and generalizability of the method.

* Could the authors provide guidelines on setting λ_A,B​ (the weighting constants of masked task vectors)? Are these values sensitive, and do they significantly impact performance?

* Would it be possible to extend the experiments to include a generation-based benchmark, such as IFEval (https://arxiv.org/abs/2311.07911)? I am curious about the model's generation capabilities and instruction-following ability after merging.

### Questions
Please refer to the above weakness section.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents CABS (Conflict-Aware and Balanced Sparsification), a framework for improving model merging through task vectors. The key contribution is identifying and addressing two critical issues in existing sparsification approaches: high parameter overlap and unbalanced weight distribution. The method introduces Conflict-Aware (CA) Sparsification to reduce parameter overlap and Balanced Sparsification (BS) using n:m pruning for better weight distribution. Experiments on Mistral-7B and RoBERTa-Base demonstrate consistent improvements over SOTA.

### Strengths
- Comprehensive empirical validation across both encoder-based (RoBERTa) and decoder-based (Mistral-7B) architectures

- Strong quantitative results, notably surpassing the "ideal" model baseline (76.50 vs 76.30)

- Thorough ablation studies demonstrating the individual and combined effects of CA and BS components

- Clear practical impact with minimal computational overhead and straightforward implementation

### Weaknesses
 - Limited exploration of sparsity levels below 0.25 and above 0.75

- No investigation of the method's applicability to cross-architecture model merging

- Lack of analysis on the impact of different task orderings in the sequential pruning process

- Experiments focused primarily on English language tasks, leaving questions about multilingual applicability

### Questions
- How sensitive is the sequential pruning order in CA to task difficulty or model performance? Would a different ordering strategy (e.g., based on task complexity) potentially yield better results?

- Could CABS be extended to merge models across different architectures or pre-training objectives?

- In cases where sparsity levels exceed 1 and overlap cannot be completely eliminated, how do you determine which overlapping parameters to prioritize?

- What is the computational overhead of CABS compared to simpler merging approaches when scaling to larger models (>13B parameters)?

### Soundness
3

### Presentation
4

### Contribution
2
