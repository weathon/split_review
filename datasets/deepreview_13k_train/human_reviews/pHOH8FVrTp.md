# No Need to Talk: Asynchronous Mixture of Language Models

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
We introduce \smalltalk{}, an innovative method for training a mixture of language models in an almost asynchronous manner. Each model of the mixture specializes in distinct parts of the data distribution, without the need of high-bandwidth communication between the nodes training each model. At inference, a lightweight router directs a given sequence to a single expert, according to a short prefix. This inference scheme naturally uses a fraction of the parameters from the overall mixture model. Our experiments on language modeling demonstrate that \smalltalk{} achieves significantly lower perplexity than dense model baselines for the same total training FLOPs and an almost identical inference cost. Finally, in our downstream evaluations we outperform the dense baseline on $75\%$ of the tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Large language models at modern scale are typically trained by means of distributed, synchronous model-parallel algorithms that rely on bespoke compute clusters with expensive fast interconnect hardware. To make progress towards eliminating this requirement, the authors tap into recent literature in parameter-sparse language models. So-called "mixture of experts" (MoE) language models replace a monolithic language model with a number of smaller "expert" models that are allocated inputs according to some (typically co-trained) routing mechanism and therefore require many fewer active parameters per input at inference time. The authors propose efficient new routers that can be trained completely independently of the mixture of experts, permitting asynchronous training for each expert. They show that mixture-of-expert models trained with these routers are competitive with dense language models of the same size and also outperform MoE models trained with even more trivial routers previously explored in the literature.

### Strengths
The method is simple (to its credit), intuitive, and effective, and it attacks an important problem. While information about the largest and most significant language models is, of course, sparse, they do not appear to be growing at the same rate as they have in previous years, and significant attention is now being devoted to the problem of improving the performance of comparatively small models (e.g. 2B models like Gemma). Good algorithms for asynchronous training could potentially unlock previously unattainable advantages of scale.

The paper is thorough and explicitly addresses most of the potential shortcomings of the proposed method that came to my mind as I read it (e.g. efficient allocation of inputs, the question of how each of the experts perform relative to each other). The authors ran a lot of very expensive experiments. It's also quite clearly written.

I was also surprised by the effectiveness of small routing models. I wouldn't have guessed that the data partitions would have been so similar across model scales.

### Weaknesses
I'm not in love with the choice to benchmark the asynchronous MoE against a dense model with the same number of parameters as each expert but trained for as many tokens as all experts combined (see the para. starting "Comparison to the Dense Model..."). Depending on how the number of training tokens was chosen, it might unfairly bias the results towards the expert setup---training one really saturated model up to 32x longer than each expert might just be a waste of compute and not a realistic counterfactual. At inference time, it's also a little generous to the MoE approach. It implicitly assumes that all of the experts are loaded in GPU memory at inference time. While this is not completely unrealistic, especially if we're modeling the very plausible scenario where we're running some kind of chat service and the number of incoming requests is high enough that we can pre-load all experts and still keep them saturated, it ignores the very real strength of the dense model that it can more efficiently be run in situations where these assumptions do not hold. I generally prefer Gururangan et al., 2023's approach to evaluation, which pitches the MoE against a single larger but train-compute-matched dense model. Inference-time compute is matched by ensembling the predictions of the top k experts. I like it for the additional reason that it gestures toward the scenario where the dense model is so large that it does not fit on a single compute node and requires model-parallel training (whereas individual experts don't). If this isn't the case, we can always still train the dense model without fast interconnect hardware if we're just willing to train it for a longer time, which, relatively speaking, diminishes the argument for a sparse model. There are lines in this paper that hint at something similar by comparing 335M experts to the 1.3B dense model, so I assume it wouldn't require too much work/compute to add more evaluations with that flavor.

Throughout, the paper also needs to do a better job positioning itself relative to Gururangan et al., 2023. The abstract is pretty representative; with the exception of the phrase "according to a short prefix" and the name of the method, the abstract of this paper could have been that for the prior paper, which differs from this one only in the choice of routing function. It needs to be clearer that this isn't the first paper to attempt asynchronous training using MoEs and that all the novelty lies in the routing.

### Questions
How were the number of tokens chosen for each configuration (see Weaknesses section above)?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The study introduces a method for asynchronously training a mixture of language models (LLMs), called experts, which significantly reduces communication overhead by eliminating the need for high-volume interactions between experts during training. Each expert is specialized to process a distinct segment of data, directed by a small, specialized router—a lightweight language model with as few as 4 million parameters. These routers evaluate text sequences using a scoring system that determines the most suitable expert for each sequence based on a short prefix of 256 tokens. A novel balanced assignment approach is proposed to ensure that each expert receives a roughly equal volume of data, minimizing training imbalances. The only communication overhead is needed for the data partitioning phase and the conventional high-volume communication between experts is completely removed by the proposed method.

### Strengths
- The authors show that the same perplexity can be achieved with three times less compute cost compared to the dense baseline

- The final performance (test PPL) is not sensitive to the router size hence, making the approach succeed with even tiny routers (4M parameters)

- The authors have conducted experiments that are highly expensive in nature. The community will benefit from such a study. Especially, the test PPL benefits (line 349) with three times less compute is a remarkable result, it can potentially open avenues for more research on large-scale LLM development with limited resources.

### Weaknesses
Performance (test PPL) is sensitive to the prefix length (256 tokens used to train routers) and the sensitivity increases with the number of experts. This sensitivity to prefix length is a critical concern, as the routing task becomes more complex with an increasing number of experts, potentially leading to less accurate assignments. The probability of randomly assigning a sequence to the correct expert increases linearly with the number of experts, making the model more vulnerable to errors when the prefix is not sufficiently representative of the entire sequence. This is particularly concerning because the model's performance relies heavily on the router's ability to make accurate decisions based on a limited context, and this limitation becomes more pronounced as the number of experts grows.

### Questions
Minor edits:
- Line 300: glitch in the reference for Adam Optimizer
- Figure 3 is difficult to read, especially the legends


Questions:
- Line 309: a different schedule (warmup + stable) for the routers, it’d be great if authors could add a line of reasoning behind this decision
- Line 388: Figure 4 (b): If the performance is sensitive to the prefix length, how would it affect the tasks where only a few tokens are provided as the prompt e.g., essay writing?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces SmalltalkLM, where instead of having a single large dense connected network, we have multiple individual dense models (the experts) and a router, which predicts which expert a given input should be routed to. During training, the data is partitioned into separate groups using the router, and each expert is then trained with language modelling on the allocated subset of data. During inference, the router can assign a new sample to the relevant expert. This enables the model to be trained with more limited RAM requirements (as each expert can be trained independently on the partitioned data) and yields better performance while only having a marginal increase in cost at inference (with the increase only as the router is first used to route the current input).

### Strengths
- Unlike approaches like MoE, the experts here are independent, and therefore, the routing can be done before each training epoch. Since each system can be trained independently, this reduces the simultaneous RAM requirements, which, unlike MoE approaches, enables SmalltalkLM systems to be trained using the same computational hardware. Inference also has lower RAM requirements. 

- They demonstrate that this approach results in better performance across different model sizes and can yield improved downstream performance on different tasks beyond language modelling. 

- The paper is quite easy to follow, and the overall idea is quite simple and seems reasonable.

### Weaknesses
 - As far as I understand, this work takes ideas of existing deep learning MoE but simplifies the process, and instead of using the top-k experts, operating at the token-level, or having experts per layer, have a single router to a single expert, which may be of limited novelty.

- The savings in RAM might not be too substantial, as when deployed in live systems, you’ll need to load up all experts simultaneously anyway (to avoid the massive latency of continually reloading the next expert). Since the running inference costs are already more expensive than training, it seems to be quite a contrived advantage.

- this point is a bit pedantic, but the base system was presented as a vanilla LLM (i.e. not actually helpful for any particular task), although it was demonstrated it yielded marginally better performance of MCQA tasks in an ‘emergent’ setting. If these systems are further tuned (which I assume is the purpose of having these base LLMs), the routing aspect may limit the practicality. The router balancing may no longer be applicable, and possibly, specialized systems may not generalize as well as a single network trained on all the data when adapted to particular tasks. It might be interesting to see how this model might operate in more practical settings, i.e. with instruction-tuning or fine-tuning to particular tasks.

### Questions
- Just to clarify, the performance shown in Figure 3 is the performance of the model, which was only trained using language modelling, when it is further prompted for the downstream tasks?

- I want to raise the weaknesses above in case the authors have any further comments.

### Soundness
3

### Presentation
3

### Contribution
2
