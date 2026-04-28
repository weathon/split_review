# Enhancing One-Shot Pruned Generative Pre-training Language Models through Sparse-Dense-Sparse Mechanism

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
Pre-trained language models (PLMs) are engineered to be robust in contextual understanding and exhibit outstanding performance in various natural language processing tasks. However, their considerable size incurs significant computational and storage costs.
Modern pruning strategies employ one-shot techniques to compress PLMs without the need for retraining on task-specific or otherwise general data; however, these approaches often lead to an indispensable reduction in performance.
In this paper, we propose \textbf{SDS}, a \textbf{S}parse-\textbf{D}ense-\textbf{S}parse pruning framework to enhance the performance of the pruned PLMs from a weight distribution optimization perspective. We outline the pruning process in three steps. Initially, we prune less critical connections in the model using conventional one-shot pruning methods. Next, we reconstruct a dense model featuring a pruning-friendly weight distribution by reactivating pruned connections with \textit{sparse regularization}. Finally, we perform a second pruning round, yielding a superior pruned model compared to the initial pruning.
Experimental results demonstrate that SDS outperforms the state-of-the-art pruning techniques SparseGPT and Wanda under an identical sparsity configuration. For instance, SDS reduces perplexity by 9.13 on Raw-Wikitext2 and improves accuracy by an average of 2.05\% across multiple zero-shot benchmarks for OPT-125M with 2:4 sparsity.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel pruning framework called SDS (Sparse-Dense-Sparse) to enhance the performance of pruned Pre-trained Language Models (PLMs) while reducing computational and storage costs. SDS consists of three steps: initial pruning of less critical connections, reconstruction of a dense model with sparse regularization, and a second pruning round. The approach outperforms conventional one-shot pruning methods, such as SparseGPT, with limited calibration samples, achieving a decrease in language comprehension perplexity by 2.4 and an average accuracy improvement of over 2% across seven downstream tasks on OPTs.

### Strengths
- **Better performance than  SparseGPT**: Its performance seems better than SparseGPT.

- **Limited Calibration Samples**: SDS achieves superior results with a limited number of calibration samples, making it a practical and efficient approach for real-world applications where acquiring extensive labeled data might be challenging.

- **Detailed Process Explanation**: The paper provides a clear and detailed explanation of the three-step pruning process, enabling readers to understand the methodology thoroughly.

### Weaknesses
 - It is unknown whether this could be valid for pruning large language models. For pruning small language models, there are already many solutions. I wonder the advantage of pruning.

### Questions
- why couldn't SDSDS or SDSD...SDS achieves better performance? In general, an  iterative SDS framework seems a good idea. Any ideas to make it work and find how many iteration to get the saturated performance.
- Can SDS also work for **large** language models? any insight?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper builds on the SparseGPT work by Frantar and Alistarh, and proposes a Sparse-Dense-Sparse pruning framework to enhance the performance of pre-trained language models that have been pruned by just using the one-shot SparseGPT algorithm. The first sparse framework directly uses existing one-shot pruning algorithms, and the authors use SparseGPT during this phase. Then, a layer-wise knowledge distillation is applied using unlabeled training samples to recover the pruned connections in the model. The paper claims that the recovered dense model has enhanced pruning awareness for the subsequent pruning step. Finally, SparseGPT is applied again with weight adjusting to obtain the SDS sparse model which performs better than SparseGPT on smaller OPT models and on-par with SparseGPT on the larger models. The empirical performance is measured on raw-wikitext2 using perplexity and on some zero-shot downstream tasks like COPA, RTE, StoryCloze, Winogrande, etc.

### Strengths
- The paper tackles an important problem of sparsity in large language models that can help in reducing the memory footprint and reducing latency during inference for these large models.
- The paper is well written and is fairly easy to follow.
- The empirical results show gains over SparseGPT for the OPT-125m and OPT-350m models and on-par with SparseGPT for the OPT-1.3b and OPT-2.7b models (Table 2).

### Weaknesses
 - Although the results on OPT models look okay on paper, I believe they are not enough to judge the practical relevance of the proposed method. First of all, how much additional flops are being incurred to prune the models in three stages? Secondly, the performance of OPT class of models on pre-training and various downstream tasks is itself not good. So, are the gains reported in the paper statistically significant, or they lie within the standard deviation of the performance of OPT models on these tasks.
- Sparsity and pruning research is more relevant for larger models to reduce their inference time and the GPU/TPU memory footprint. But the proposed method only matches SparseGPT's performance for the larger models. Is the further Dense-Sparse pruning even necessary?
- The paper should also report results on the speedup obtained compared to the dense and SparseGPT models with varying model size and sparsity category (50%, 2:4, 4:8).

### Questions
I have asked most of my questions in the weakness section, but here are a few more:

- Is there a typo in Algorithm 1 in section A.1? The main text of the paper mentions that it uses $W_{l}^{sparse-2nd}$ to collect $X_{l - 1}$ during forward propagation, but line 8 in the $\textbf{Second pruning: sparse weight adjustment}$ sub-algorithm mentions $W_{i}^{sparse}$ for forward propagation.
- I believe the authors use the same subset of unlabeled data during the second and third phases of SDS. Did the authors observe any difference in using a different sample during these two stages?
- Typo in Section 2.2, third last line: it should be unlabeled data and not labeled data, right? since only $X$ input is being used and intermediate outputs collected during forward propagation?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a three-step framework to improve one-shot pruning for large language models to potentially accelerate inference. In the first step, the method performs a standard one-shot pruning such as the SparseGPT method; in the second step, they perform a dense reconstruction of the sparse model to reactivate the pruned connections, aiming to identify a dense model with enhanced pruning awareness; and in the last step, they perform pruning again for the reconstructed model. Comparison to SparseGPT methods show that this three-step method performs better than one-shot pruning with a single pruning step.

### Strengths
The explanation provided for Figure 3 is compelling and effectively illustrates the effect of the method on model parameters. Nevertheless, it's worth noting that the visualization in Figure 3 visualizes a small model opt-125m, leaving some uncertainty regarding whether the observed effect would hold the same significance for larger models.

### Weaknesses
- **Comparing to stronger methods like wandb:** Wandb (Sun et al., 2023) is a method that performs better than SparseGPT on one-shot pruning, and the authors should introduce it as a baseline and add more discussions around it. I believe that the framework is independent from the base pruning method, thus doing experiments on top of a strong existing method is highly recommended.
- **Performing experiments on stronger base models:** A clear trend that is disclosed by comparing SparseGPT and Wanda in Sun et al., 2023 is that the stronger the base model is, the more the pruning process hurts the performance of the model. For example, in the SparseGPT paper, pruning retains the model performance on OPT models; however, when Sun et al., 2023 evaluates on LLaMA based models, the performance degradation is way more significant. Such observations make intuitive sense, as the more stronger the base model is, the more information each parameter carries, and the more the model performance gets hurt when the parameter gets pruned. Given this observation, I suggest the authors test on stronger base models like LLaMA to give a more accurate account of how practical one-shot pruning is for real applications.
- **The extra step leads to diminishing returns in performance as the model scales up:** From table 2, it’s clear that as the model scales up and becomes stronger, the performance of the the re-dense and r-=prune process leads to minimal improvement compared to simply using one step of pruning.

### Questions
Will performing the re-dense and re-prune process in multiple iterations further improve performance?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
