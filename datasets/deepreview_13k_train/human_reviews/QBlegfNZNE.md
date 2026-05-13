# Language as Kernels

- Decision: Reject
- Scores: 3, 1, 5, 5

## Abstract
In the realm of natural language understanding, the synergy between large language models (LLMs) and prompt engineering has unfurled an impressive tapestry of performance. Nonetheless, this prowess has often been overshadowed by the formidable computational resource requirements, rendering LLMs inaccessible in resource-constrained milieus. In this study, we embark on a journey to reconcile this paradox by introducing a nimble and elegant solution --- the kernel machine paradigm. Within these hallowed pages, we present a compelling proof, demonstrating the mathematical equivalence of zero-shot learning and kernel machines. This novel approach, marked by its computational thriftiness, bestows upon us the ability to harness the latent potential of LLMs, even when confined to the humble CPUs. The marriage of this approach with neural nets, renowned for their boundless abstraction capabilities, culminates in remarkable accomplishments with in the realm of language understanding. Our paramount contribution lies in unveiling a path less traveled, where the integration of kernel machines and LLMs unveils a promising vista, enabling the realization of sophisticated language processing tasks in resource-constrained environments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In order to relieve the computational resource requirement of learning with LLMs, this paper proposes a support vector generation (SVG) method on the embeddings produced by LLMs. This approach can also solve some classification tasks in an zero-shot manner. For example, in this framework, the sentiment prediction task can be conducted by $\phi(x)^T [\phi("positive") - \phi("negative")]$, where $x$ is the input text, and $\phi(\cdot)$ is the embedding produced by the LLM. The authors claim this method is able to work on CPUs.

### Strengths
I don't see clear strengths on this paper.

### Weaknesses
The paper is not understandable. I had a very hard time to follow the main message and the claims. for instance:

1. what is the main message of the paper? how is this connected to zero-shot learning.
2. Theorem 3.1 makes no sense. I might be missing something, but are you trying to prove representer theorem? What is the optimization over? any possible f? or you mean f in the Hilbert space corresponding to K? even in the proof, I saw that you have shown K is positive definite but how is K even related to the optimization problem in equation (3)?!!
3. The main algorithm (SVG) is very vague. What is \theta? what is p_{\theta}? what is q_{\theta}? why non of them formally introduced? Why A is a good criteria for accepting?!

I cannot trust the experiment result or any part of this paper.

### Questions
From Table 2, on MNLI, your approach doesn't outperform the baseline significantly. Is this because your approach only work well on binary classification? How is your performance on tasks with more labels, e.g., SST-5, SNLI, TREC, etc.?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The study explores the application of kernel methods to transformer-based embeddings. The approach involves utilizing these embeddings to train a kernel machine for (potentially) a new task, employing an iterative process that retains only the "support vectors" instead of the entire dataset. However, they claimed they mathematically showed kernel methods are zero-shot learners. (quote: "mathematical equivalence of zero-shot learning and kernel machines"!!)

### Strengths
1. The iterative method for selecting support vectors using a probabilistic approach seems interesting. However, the current description lacks sufficient detail to fully understand the specifics of the algorithm.

### Weaknesses
The paper is not understandable. I had a very hard time to follow the main message and the claims. for instance:

1. what is the main message of the paper? how is this connected to zero-shot learning.
2. Theorem 3.1 makes no sense. I might be missing something, but are you trying to prove representer theorem? What is the optimization over? any possible f? or you mean f in the Hilbert space corresponding to K? even in the proof, I saw that you have shown K is positive definite but how is K even related to the optimization problem in equation (3)?!!
3. The main algorithm (SVG) is very vague. What is \theta? what is p_{\theta}? what is q_{\theta}? why non of them formally introduced? Why A is a good criteria for accepting?!

I cannot trust the experiment result or any part of this paper.

### Questions
See weaknesses.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper presented `Support Vector Generation` which leverages generative capability of LLMs to better utilize kernel machines for thrift computation. This paper also mathematically demonstrated equivalence of zero-shot learning and kernel machines so that this method can be used for zero-shot task data argumentation. Experiments on GLUE showed comparable or better performance on multiple downstream tasks compared to prompting methods, and runs pretty fast on CPU.

### Strengths
This paper introduces a novel method for zero-shot learning, referred to as Support Vector Generation. It harnesses the generative capabilities of Large Language Models (LLMs) to enhance kernel machines, achieving highly accurate results while maintaining low computational resource requirements. The experiments conducted across multiple tasks in the GLUE Benchmark show promising results, and the paper also provides insights into the computational complexity, highlighting the effectiveness of this approach. Overall, this innovation has the potential to significantly improve the computational efficiency of zero-shot learning.

### Weaknesses
There is still uncertainty regarding whether this method can be advantageous in scenarios beyond zero-shot learning or other specific tasks. While the authors assert the computational efficiency of their approach, no direct numerical comparisons are provided to substantiate this claim. Additionally, as a data augmentation method, it's not explicitly clarified whether the improved performance primarily stems from the data sampling process or the kernel machine technique itself. Further clarification on these aspects would enhance the paper's findings and their broader applicability.

### Questions
1. Can this method be extended outside zero-shot learning?
2. Can you please explain with a more concrete example how SVG improved performance based on LLM?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an efficient kernel function for large language models and prompt engineering, to speed up the generation process. The proposed methods are useful for resource-constrained environments.

### Strengths
- The paper is well-written and well-organized.
- Using kernel functions for Large Language models is a pretty interesting topic.

### Weaknesses
- Since it is a rapidly growing area, comparing it with just one "prompting" baseline in 2020 is pretty unfair. I hope the author could introduce more recent baselines for comparison.
- I do not see any discussion or experiment in terms of a resource-constrained environment, where the paper claims to be beneficial with the proposed method.
- The necessity for introducing Theorem 3.1 and 3.2. The two theorems are not that relevant to the main contribution of this work. The concepts introduced in the two theorems are also not well explained.

### Questions
Could you also list more recent baselines to enrich Table 2?
Could you consider adding an experiment on a resource-constrained environment, like a no-GPU laptop, or GPU with only 4GB graphic memory?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
