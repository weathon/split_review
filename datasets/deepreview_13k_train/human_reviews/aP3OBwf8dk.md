# Need a Small Specialized Language Model? Plan Early!

- Decision: Reject
- Scores: 5, 5, 8

## Abstract
Large language models are versatile tools but are not suitable for small inference budgets. Small models have more efficient inference, but their lower capacity means that their performance can be good only if one limits their scope to a specialized domain.  This paper explores how to get good specialized small language models using a large, generic, pretraining set and a limited amount of specialized data. We consider two scenarios, depending on whether (i) one can afford pretraining a model for each specialization task, or (ii) one wants to cheaply adapt a single pretrained model for each task. In the first scenario, we propose an effective solution based on importance sampling: we resample the pretraining set to imitate the specialization data and train a small model on it. In the second scenario, we propose a novel architecture, projected networks (PN). PN is a large network whose parameters can be linearly projected into a small network for specialization. For both scenarios, we demonstrate the empirical effectiveness of our solutions across various domains, training set sizes, and training budgets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
* The authors propose ways of obtaining SLMs from LLMs, depending on different situational constraints.
  * To create one domain-specific SLM, the authors propose importance sampling, i.e., resampling from the larger general dataset to mimic the distribution of scarce task-specific data
  * To create multiple SLMs for each sub-task, the authors propose projected networks (PNs), i.e., projecting the weights of the LLM to generate weights for the SLM
* PNs can be seen as hypernetworks in that their output parameterizes the SLM.

### Strengths
* The work addresses a relevant and applicable question around the effective deployment of LLMs, possibly via their pruned or distilled variants.
* Thorough record of the setup, e.g., number of GPU hours, training steps, parameter count, makes the case for SLM methods convincing and highlights the gains that can be reaped from the proposed methods.

### Weaknesses
 * There is lack of theoretical or heuristic justification behind why linear projections are a suitable operator for deriving SLMs from LLMs. Some exploratory work on, e.g., the activation patterns of the LLMs across different domains that justify the linear projections, would have been nice.
* A more direct comparison to other baselines such as LoRA would have made evaluations more informative. Appendix F does include a comparison, but a direct reference in the main text would make it even more helpful for further contextualization and comparison.
* It would have been nice to see actual applications of these methods to existing LLMs (e.g., Llama, Gemini) instead of an in-house LLM trained on C4.

### Questions
* Why do you use linear projections instead of more common hypernetwork formulations? What is gained or lost by doing this?
* Do the linear projections learn anything meaningful, e.g., the singular values of the FFN layers?
* How does this work relate to LoRA? It seems that there is an explicit connection to be made between LoRA and PNs as they both encourage low-rank behavior in the learned weights. Appendix F seems to address this to an extent, but I would appreciate a more direct account on this.

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
2

### Summary
The paper studies the task of training a group of domain-specialized SLMs. It proposes two different methods for achieving the task: 1) important sampling based specialized pretraining, and 2) projection networks based model architecture. Experiment results show a trade-off between performance and compute cost, where method 1 achieves better overall performance but requires more compute budget, and method 2 could still achieve acceptable performance while requiring less compute budget.

### Strengths
The proposed projected network method is novel and the experiment section is comprehensive.

### Weaknesses
The paper is not well-written, and some details are difficult to understand. For example:
1) Section 2.4 has many equations, but the symbols used in these equations are not defined. This makes it difficult to understand how to get the weight for importance sampling. Specifically, the roles of \(D_{spec}\) and \(D_{generic}\) are unclear within the equations, and the relationship between the loss function \(\ell\) and the overall objective is not explicitly stated. The lack of clear definitions for these terms makes it challenging to reproduce the importance sampling weights.
2) Figure 4 is a bit misleading. The perplexity for SLM-is is a flat line, but it doesn't reflect the fact that SLM-is requires significantly more compute during specialization compared to other methods. The figure should more clearly represent the total computational cost, not just the perplexity at different training data sizes. The current presentation obscures the practical trade-offs between methods.
3) The training budget is defined as GPUh throughout the paper. Is it measured in a single GPU, multi-GPU, or multi-node setting? Because these different settings will have impacts on the training cost and actual throughput. Perhaps the standard FLOPs notation is clearer and less ambiguous. Furthermore, the paper does not specify the GPU model used, which is crucial for interpreting the GPUh metric. Different GPU models have vastly different computational capabilities, making the GPUh metric difficult to compare across different hardware setups.

### Questions
Please refer to the weaknesses section.

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
3

### Summary
The paper studies two scenarios about training specialized small models on specific domains. In the first scenario, people can do pretraining on every specific domain; in the second scenario, people have to distribute computational resources among specific domains. Targeting the first scenario, the paper proposes SLM-is, which uses importance sampling w/ a clustering-based technique giving the importance weight. Targeting the second scenario, the paper proposes SLM-pn, where a PN projects a large model to a small model for each domain.

(After rebuttal, I decided to increase my score from 6 to 8.)

### Strengths
+ The studied problem is very meaningful.
+ I personally like the method of SLM-is. The idea is novel and reasonable. The performance is also good.

### Weaknesses
+ It is unclear how important the design choice of using PN is for SLM-pn. Naturally, one could consider using an Adapter/LoRA/any possible PEFT module to adapt a large model to a specific domain. It would be better to show why taking PN is better, in terms of either performance or efficiency. Specifically, the paper does not clearly articulate the advantages of using a hypernetwork-based projection (PN) over other parameter-efficient fine-tuning (PEFT) methods. For instance, while PEFT methods like LoRA also introduce a small number of trainable parameters, the paper does not provide a clear comparison or justification for why a projection-based approach is superior. The paper should include experiments that directly compare PN with other PEFT methods, such as LoRA or adapters, to demonstrate the benefits of the proposed approach.


### Questions
In Section 6.1 of [Scaling Expert Language Models with Unsupervised Domain Discovery](https://arxiv.org/pdf/2303.14177), the author tried a method that is IMO similar to SLM-pn. Basically, there is a shared base model for all domains and each domain has a specific module. It is also relevant to the weakness mentioned above. What do you think?

### Soundness
3

### Presentation
2

### Contribution
3
