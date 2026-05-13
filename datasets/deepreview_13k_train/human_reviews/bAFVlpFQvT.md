# Memory-efficient Training of Large Language Models with Larger Mini-batches

- Decision: Accept
- Scores: 8, 5, 8, 6

## Abstract
Training with larger mini-batches improves the convergence rate and can yield superior performance. However, training with large mini-batches becomes prohibitive for Large Language Models (LLMs), due to the large GPU memory requirement. To address this problem, an effective approach is finding small mini-batch coresets that closely match the gradient of larger mini-batches. However, this approach becomes infeasible and ineffective for LLMs, due to the highly imbalanced nature of the sources in language data, use of the Adam optimizer, and the very large gradient dimensionality of LLMs. In this work, we address the above challenges by proposing *Coresets for Training LLMs* (CoLM). First, we show that mini-batch coresets found by gradient matching do not contain representative examples of the small sources w.h.p., and thus including all examples of the small sources in the mini-batch coresets is crucial for optimal performance. Second, we normalize the gradients by their historical exponential to find mini-batch coresets for training with Adam. Finally, we leverage zeroth-order methods to find smooth gradient of the last *V*-projection matrix and sparsify it to keep the dimensions with the largest normalized gradient magnitude. We apply CoLM to fine-tuning Phi-2, Phi-3, and Zephyr with LoRA on MathInstruct and SuperGLUE benchmark. Remarkably, CoLM reduces the memory requirement of fine-tuning by 2x and even outperforms training with 4x larger mini-batches. Notably, CoLM easily stack with existing memory-efficient training methods, such as LoRA.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces CoLM (Coresets for Training LLMs), a method for memory-efficient training of large language models (LLMs) using mini-batch coresets that approximate the gradients of larger batches. CoLM addresses specific challenges in LLM training, such as data imbalance, high gradient dimensionality, and compatibility with the Adam optimizer. CoLM addresses them by including all examples from smaller data sources, normalizing gradients for Adam, and using zeroth-order gradient estimates. It reduces memory requirements by 2x while maintaining or surpassing performance compared to larger mini-batches.

### Strengths
1. The approach takes a unique and innovative perspective on memory-efficient training. Unlike typical methods in field, it focuses on data selection and reduces batch size to achieve memory-efficient training.
2. The paper is clear to understand and well motivated. 
2. The paper presents comprehensive experiments on diverse datasets and models, substantiating the benefits of CoLM over various baselines.

### Weaknesses
1. Computational overhead: Figure 2(b) suggests that the computational overhead for CoLM is notably high, doubling the training time in some cases, whereas typical memory-efficient methods usually incur 5-20% overhead. A comparison of "memory vs. computational overhead vs. performance" with other methods would be beneficial. The high computational cost, especially in scenarios with limited resources, could hinder the practical adoption of the proposed method. It is critical to understand the trade-offs between memory savings and computational expenses, especially when compared to other memory-efficient training techniques.
2. The paper mainly evaluates CoLM in a fine-tuning context, where model and optimizer state memory are the main bottlenecks. It would be valuable to see CoLM tested in pre-training or continual pre-training settings, where activation memory dominates due to large batch sizes. This could pose additional challenges given complex data structures and extensive amount of training data. The current evaluation does not fully explore the potential of the method in more memory-constrained scenarios, such as pre-training with very large batch sizes, where activation memory becomes a significant factor. The method's performance in such scenarios remains unclear.
3. Not enough details of algorithm and discussion on hyper-parameters. The lack of a detailed algorithm description and discussion on hyper-parameters makes it difficult to reproduce the results and understand the sensitivity of the method to different settings. Specifically, the selection of small and large data sources, and the impact of their relative sizes on the performance of CoLM, are not clearly addressed.

### Questions
1. Is zeroth-order necessarily needed? How about estimating using standard first-order methods?
2. What hypeperparametrs involved in CoLM? Like how many small sources and large sources needed? How much is the cost of tuning those hyper parameters? Are they sensitive to different data structures and types of data?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method called Coresets for Training Large Language Models (CoLM) to enable memory-efficient training of large language models (LLMs) by constructing mini-batch "coresets." These coresets are small, representative subsets of mini-batches that approximate the gradient of larger batches, allowing effective model training with reduced memory usage. CoLM addresses challenges such as the high memory demands of large mini-batches, the imbalanced distribution in language data, and the complexities of using the Adam optimizer in high-dimensional gradient spaces.

### Strengths
- The presentation is clear, and the paper is easy to follow, with only a few minor typos.
- The proposed method, CoLM, is straightforward and demonstrates strong empirical performance.

### Weaknesses
 - **Limited Base Models**: While the authors mention using Phi-2, Phi-3, and Zephyr, the main results in Tables 1 and 7 only report Phi-2. To more fully demonstrate CoLM’s performance across various models, I recommend including Phi-3 in these tables and consider adding state-of-the-art models, such as LLaMA-3 8B and LLaMA-3.1.

- **Insufficient Discussion of Related Work and Novelty**: One of CoLM’s contributions is gradient normalization for the Adam optimizer, which improves mini-batch approximation by using historical averages. However, previous studies, such as [1], have explored renormalization techniques with mini-batches. It would strengthen the paper if the authors could discuss distinctions between [1] and CoLM to clarify CoLM’s unique contributions.

- **Lack of Clarity on Gradient Estimation**: The paper introduces a method for obtaining low-dimensional gradient estimates in Section 4.2, which bears similarity to Espace and Galore. However, the paper does not clearly articulate the differences between the proposed method and these existing techniques, nor does it explain the advantages of the method in Section 4.2 compared to Espace and Galore. A more detailed discussion is needed to justify the novelty of the approach, especially given the existing literature on low-dimensional gradient approximations.

### Questions
- **Computational Complexity**: CoLM introduces additional computational costs to find mini-batches. Could the authors discuss the complexity and time requirements for this estimation algorithm and expand on it in the main paper?

- **Convergence Rate Comparison**: Figure 3 compares CoLM and fine-tuning (FT) by plotting accuracy against training iterations to highlight CoLM’s faster convergence. Could the authors include a comparison of CoLM with LoRA in Figure 3? It would also be valuable to add perplexity or training loss versus iterations to provide further insight into convergence rates.

- **Time vs. Accuracy Comparison**: Given that CoLM involves additional computation to determine mini-batches, comparing accuracy against time would offer a fairer evaluation alongside FT and LoRA in Figure 3(a).

- **Quantitative Memory Cost Analysis**: While the paper claims CoLM uses 4x less memory, it lacks a quantitative breakdown of memory usage. Could the authors add specific memory costs for LoRA, other low-rank adaptation methods, and CoLM in a table? This would provide stronger evidence of CoLM’s memory efficiency.

- **Clarification on Motivation**: 1) In the introduction, the authors state that fine-tuning a model like Phi-2 with 2.7B parameters and a batch size of 128 requires at least 44 GB of GPU memory. However, fine-tuning LLMs primarily incurs memory costs due to model weights and optimizer states, which together cost approximately three times the model weight. Since Phi-2’s model size is under 7 GB, the total memory cost should be around 22 GB rather than 44 GB. Furthermore, batch size typically only affects activation memory and does not significantly impact memory for optimizer states or model weights, and the activation memory cost is not an issue for PEFT methods such as LoRA. 2) **Comparison to LoRA**: LoRA also reduce optimization memory significantly. Besides, LoRA also achieve significantly speedup since it has less trainable parameters. CoLM achieve similar wall clock time with full fine-tuning, but when it applies to full fine-tuning, it will be much slower than LoRA. Could the authors clarify the motivation of the paper from these aspects? 



- **Title Consistency**: Please align the submission title, "Memory-efficient Training of Large Language Models with Larger Mini-batches," with the manuscript title, "MINI-BATCH CORESETS FOR MEMORY-EFFICIENT TRAINING OF LARGE LANGUAGE MODELS."

I would like to discuss the questions I raised regarding the weaknesses and concerns with the authors. If my concerns are adequately addressed, I would be willing to reconsider my rating.

### Soundness
3

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
4

### Summary
The paper identifies three key difficulties when applying previous coreset findings methods (methods for finding small mini-batches that have gradients whose mean closely approximates the full gradient) to fine-tuning LLMs: imbalanced data, Adam's update, and large gradient dimensionality. The authors systematically formalize the difficulties and design methods to address them: by treating small-source examples and large-source examples differently, by comparing gradients in the space of Adam updates, and by using zeroth order gradient estimations methods, sparsifying the gradient, and using an appropriate distance metric. The combination of these improvements makes up their method,  Coresets for Training LLMs (CoLM). In their empirical study, authors demonstrate that their method leads to stronger performance compared to a number of baselines (including strong ones) and uses less memory than comparable methods while adding a reasonable overhead in training time.

### Strengths
- The paper is very well written. It provides clear motivations of the problem and in thoughtfully structured around the three key difficulties of applying coreset finding methods to LLM fine-tuning. This structure makes the paper clear and very easy to follow. 
quality, 
- The authors provide extensive ablation analyses about the great majority (if not all) of the improvements they propose, which is greatly appreciated and helps show they are worthwhile.
- The authors empirically demonstrate the effectiveness of CoLM for different pre-trained language models and across many datasets (Math Instruct, SST-2, CB, MultiRC).
- The method often outperforms fine-tuning with twice the batch size.
- The authors demonstrate that the method achieves a smaller memory overhead than a number of representative baselines.

### Weaknesses
 - Using gradient accumulation + LoRA trivially reduces the memory overhead. The paper would benefit from experiments making an explicit comparison to this case. It seems from Fig 2 (a) that you should be able to claim CoLM is still faster in this case, but not showing it and claiming memory efficiency makes the paper seem weak.

- While the memory overhead is reduced due to the smaller batch size, there is no figure showing how much the total memory decreased by making the batch size smaller when fine-tuning with LoRAs using CoLM. Does the batch size reduction account for a substantial portion of the memory consumption or is the memory consumption dominated by the model parameters given the smaller optimizer states required for one LoRA? Providing a figure with the memory consumption of CoLM compared to fine-tuning at different batch sizes is warranted given the author's claims about memory efficiency.

- Do the methods to estimate gradient distances scale to larger vocabulary sizes? Recent SOTA models (Llama 3 has 128k vocab size whereas phi2,phi3,and zephyr have 50k at most) have been using much larger vocabulary sizes and recent work "Scaling Laws with Vocabulary: Larger Models Deserve Larger Vocabularies" shows this is an important axis along which to scale LLMs. Simply including one experiment with a larger tokenizer 100k vocab+ would strengthen this aspect.

- *I believe the above concerns are easily addressable with small additional experiments. I would be happy to raise my score if these concerns are addressed. *

*List of Typos*:
 "to iteratively selecting small mini-batches from larger random batches." selecting --> select

### Questions
(Q1) For Figure 3 (c), how large does the batch size need to be to match your method?

### Soundness
4

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
3

### Summary
The paper introduces a method in using smaller mini-batches to simulate the performance of training with larger mini-batches, in the context of Large Language Models (LLMs). In particular, the authors propose coresets for training LLMs (CoLM) which involves the following aspects:

1. Including all examples from small sources in the mini-batch coresets
2. Adapt the mini-batch coreset selection process with ADAM, selecting medoids of big sources.
3. Use zero-order optimization technique based on MeZO in combination with LoRA to estimate the gradients.

Experiments show that the proposed method achieves comparable performance to regular fine-tuning that uses a much larger batch size, while reducing the memory requirements.

### Strengths
S1: Well written paper with nice motivation to enable both memory efficiency and performance gains by looking at a data perspective.

S2: Strong experimental results that demonstrate the benefits of their approach compared to baselines. The increase in training time due to mini-batch selection also justified given significant improvement in accuracy.

S3: Ablation studies give insight to the relative importance to each of the three components proposed, with emphasis on gradient approximation, which helps to better understand the benefits of the method.

### Weaknesses
W1: There should be some further clarification on how "all" examples of small sources can be included in the mini-batch coreset. Based on experiments, figure 4 shows that the data count for even small data sources can be over 1000 examples. Including all the sources in a single mini-batch does not seem to be plausible, but implied from the methodology and Algorithm 1. The description of how small sources are handled within the mini-batch selection process is unclear, particularly when considering the practical limitations of mini-batch sizes. The algorithm seems to suggest that all examples from small sources are included in the coreset, but this is not feasible if the total number of examples from small sources exceeds the mini-batch size. This needs to be clarified with a more precise description of the selection process for small sources, especially when the number of examples from small sources is large relative to the mini-batch size.

W2: Dependency on having access to the true source data distribution may not always be possible. In these cases, it is difficult to distinguish between small and large sources. In addition, how to determine the boundary between "small" and "large" partitions could be discussed in more detail with experiments. The paper mentions clustering as a potential solution when source information is unavailable, but the practical implications of this approach are not fully explored. Specifically, the sensitivity of the method to the choice of clustering algorithm and the number of clusters needs to be investigated. Furthermore, the paper does not discuss how the performance of the method might be affected by the quality of the clustering, which is a critical factor in the absence of true source information. The criteria for determining the boundary between small and large sources, especially in skewed distributions, needs more rigorous justification and empirical validation.

### Questions
Q1: Related to W1 - Is there some sampling or representative subset selection method for the small sources going on behind the scenes?

Q2: Related to W2 - How to determine the boundary between "small" and "large" partitions, especially with skewed distributions where average count may not serve as a good cutoff?

### Soundness
3

### Presentation
3

### Contribution
3
