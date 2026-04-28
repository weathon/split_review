# Addax: Utilizing Zeroth-Order Gradients to Improve Memory Efficiency and Performance of SGD for Fine-Tuning Language Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Fine-tuning language models (LMs) with the standard Adam optimizer often demands excessive memory, limiting accessibility. The ``in-place'' version of Stochastic Gradient Descent (IP-SGD) and Memory-Efficient Zeroth-order Optimizer (MeZO) have been proposed as solutions to improve memory efficiency. However, IP-SGD still requires a substantial amount of memory, and MeZO suffers from slow convergence and degraded final performance due to its zeroth-order nature. This paper introduces {\em Addax}, a novel method that improves both memory efficiency and algorithm performance of IP-SGD by integrating it with MeZO. Specifically, Addax computes the zeroth- or first-order gradient of the data points in the minibatch based on their memory consumption and combines zeroth- and first-order gradient estimates to obtain the updated direction in each step.
By computing the zeroth-order gradient of data points that require more memory and the first-order gradient of the ones that require less memory, Addax overcomes the slow convergence of MeZO and the excessive memory requirement of IP-SGD. Additionally, the zeroth-order gradient acts as a regularizer for the first-order gradient, further enhancing the model's final performance.
Theoretically, we establish the convergence of Addax under mild assumptions, demonstrating faster convergence and less restrictive hyper-parameter choices than MeZO. Our extensive experiments with diverse LMs and tasks show that Addax consistently outperforms MeZO in terms of accuracy and convergence speed while having a comparable memory footprint. 
In particular, our experiments using one A100 GPU on the OPT-13B model reveal that, on average, Addax outperforms MeZO in terms of accuracy/F1 score by $14\%$ and runs $15\times$ faster while having a comparable memory footprint to MeZO. In our experiments on the larger OPT-30B model, on average, Addax outperforms MeZO in terms of accuracy/F1 score by $>16\%$ and runs $30\times$ faster on a single H100 GPU. Moreover, Addax surpasses the performance of standard fine-tuning approaches, such as IP-SGD and Adam, in most tasks in terms of accuracy/F1 score with significantly less memory requirement.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents Addax, a novel approach to fine-tuning large language models (LMs) with reduced memory usage and improved convergence speed. Addax aims to bridge the gap between two existing methods—IP-SGD, which is memory-intensive, and MeZO, which suffers from slow convergence due to its zeroth-order gradient estimation. By combining zeroth-order and first-order gradient estimates based on the memory consumption of different data points, Addax attempts to balance the benefits of each approach, reducing memory requirements without sacrificing performance.

### Strengths
The concept behind Addax is promising. By selectively applying zeroth-order and first-order updates depending on memory requirements, Addax cleverly attempts to sidestep some of the limitations of both IP-SGD and MeZO. The added benefit of using zeroth-order gradients as a regularizer for first-order gradients is an interesting approach that theoretically could lead to better model generalization.

- it assigns data points with higher memory demands to a zeroth-order gradient estimation, while data points with lower memory demands use a more standard first-order gradient approach.

- the wallclock time details provided are very helpful.

### Weaknesses
 - Addax introduces an additional layer of complexity by dynamically selecting gradient types based on memory consumption, which may require extra engineering effort to implement effectively in various environments. 
-  The algorithm involves splitting data into two subsets, resetting random seeds, and clearing gradients for each update step. This is quite complicated. The need to track memory usage for each data point and dynamically switch between gradient estimation methods introduces significant overhead. This complexity could hinder adoption, especially in production settings where simplicity and stability are paramount. Furthermore, the process of splitting data into subsets based on memory consumption, resetting random seeds, and clearing gradients adds considerable computational overhead, potentially negating some of the gains in memory efficiency.
- While the hybrid gradient approach is novel, it’s unclear from the presented results to what extent this technique actually enhances performance, or to be specific, in results shown in figure 1 e.g. some of the tasks's improvement seem very marginal compared to MEZO. The performance gains over MeZO, particularly in Figure 1, appear marginal for some tasks, raising questions about the practical significance of the improvement given the added complexity. A more rigorous analysis of the performance gains, including statistical significance tests, would be beneficial to determine if the observed improvements are truly meaningful.

### Questions
- the experiments done here are all done with high-end h100 gpus, I am curious who are actually the targeted users for Addax? does this work on lower-end GPUs? say 3090s?
- with the empirical improvement presented, and the complexity of the methods. I am curious if the authors could further list your No.1 selling point vs. well-established first-order finetuning methods, what would be your pitch to convince the community to adopt Addax in practise?

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
This paper proposes a novel LLM fine-tuning methods, which try to combine the first-order (sgd) and zeroth-order (mezo) to efficiently fine-tune LLM. The experiments on OPT and LLaMA Illustrate that the proposed method can achieve a better performance than SGD and faster convergence than MeZO.

### Strengths
1. The intuition and motivation are very easy to understand and the paper is also easy to follow. 

2. The paper provides the results on different models with different sizes to verify the performance of the proposed method, which also makes the paper more convincing.

### Weaknesses
1. The opinion that "SGD can match the performance of Adam in fine-tuning tasks." is not very reasonable to me. I think the main reason why the authors reached this conclusion is because the tasks in this paper are too easy (mainly focusing on classification tasks). If the authors conduct some experiments on math and code generation tasks, Adam could be better than vanilla SGD. 

2. Ablation Study. We can notice that the paper provides the results of ip-sgd and addax in Table 1, 2, 3. And the main difference of these two methods is some long sequences use different optimizers. Specially, for addax, the long sequences use zero-order optimization. What is the result if we set the learning rate of these zeroth order optimization to 0 (That means we can skip these long sequences and no update with these data). I just want to see whether the zeroth-order optimization really works. I guess update too much times with sgd may cause overfitting and just skip some training steps (long sequences in addax) can improve the performance (even if don't use zeroth-order on this data). So I would like to see the results if we just skip these long sequence data in addax. 

3. The paper mainly focuses on the tasks on SuperGulu. These tasks are too easy to LLM fine-tuning with first-order methods. It would be better if the authors could provide the results of complex tasks. This is just a suggestion and should not be a weakness.

### Questions
1. From my experience about MeZO, it usually begin to work after a large number of epochs. So I would like to ask whether Addax and SGD use a same epoch value?

### Soundness
3

### Presentation
3

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
This paper proposes Addax, which assigns different mini-batch of data to compute zeroth-order and first-order gradients respectively based on the sequence length of the data, and combines the two kinds of gradients to update the model parameter. Addax outperforms existing zeroth-order method MeZO in accuracy/F1 score and achieves comparable memory footprint with MeZO. Furthermore, it surpasses IP-SGD and Adam with significantly less memory requirement.

### Strengths
-	The motivation of the proposed method is well supported by the preliminary experiments.
-	This paper provides theoretical guarantee that the propose method enjoys faster convergence and less restrictive hyper-parameter choices than MeZO.
-	This paper conducts extensive experiments to demonstrate its effectiveness on models with various sizes ranging from 350M to 70B, achieving superior performance both in test accuracy, memory and time efficiency.

### Weaknesses
 - In Algorithm 1 step 7, the mini-batch $\beta^1$ is sampled from $D^1$, while in Line 298, it is claimed that $\beta^1$ is sampled from $\beta^0$, which is inconsistent. 
- The performance of the proposed method is sensitive to the mixing constant $\alpha$ for combining the zeroth-order and first-order gradients. Also, it may be sensitive to the length threshold $L_T$ and the random seed. 
- It would be better to further demonstrate the effectiveness of the proposed method on more challenged tasks such as commonsense reasoning tasks and mathematics tasks.

### Questions
Please refer to the Weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Authors propose Addax, algorithm which adaptively combined zero-order (MeZO) and in place first-order (IP-SGD) optimization methods, to achieve LLM fine-tuning with low memory requirement.

### Strengths
An excellent description of problems with MeZO and IP-SGD. 
Better results than MeZO while keeping memory consumtion low.

### Weaknesses
Authors do memory profiling without gradient checkpointing, a very common technique to lower memory requirements for storing activations for backward computation. I believe this overestimates the memory requirements of IP-SGD. 
The main selling point is that Addax has lower memory requirements than IP-SGD. However, this selling point vanishes the moment we turn gradient checkpointing on.

A minor selling point of Addax is that it sometimes produces better results even when zero-order gradients are computed concurrently with first-order ones (Addax-WA). However, it is hard to find which results actually belong to Addax-WA in the paper. E.g. section 4 says "we plot the convergence curves of Addax-WA and MeZO using the same batch size in Figure 11", but figure 11 label says "Addax with 4×
less first-order samples achieves a convergence speed similar to SGD", which suggest we are not running Addax-WA here.

Nitpick: Figure 4 just feels wrong, because SGD should always have higher memory requirements than IP-SGD).

### Questions
How would results look like when we run IP-SGD with gradient checkpointing?

### Soundness
3

### Presentation
3

### Contribution
2
