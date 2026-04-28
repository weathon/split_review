# Network Memory Footprint Compression Through Jointly Learnable Codebooks and Mappings

- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 8, 6

## Abstract
The massive interest in deep neural networks (DNNs) for both computer vision and natural language processing has been sparked by the growth in computational power. However, this led to an increase in the memory footprint, to a point where it can be challenging to simply load a model on commodity devices such as mobile phones. To address this limitation, quantization is a favored solution as it maps high precision tensors to a low precision, memory efficient format. In terms of memory footprint reduction, its most effective variants are based on codebooks. These methods, however, suffer from two limitations. First, they either define a single codebook for each tensor, or use a memory-expensive mapping to multiple codebooks. Second, gradient descent optimization of the mapping favors jumps toward extreme values, hence not defining a proximal search. In this work, we propose to address these two limitations. First, we initially group similarly distributed neurons and leverage the re-ordered structure to either apply different scale factors to the different groups, or map weights that fall in these groups to several codebooks, without any mapping overhead. Second, stemming from this initialization, we propose a joint learning of the codebook and weight mappings that bears similarities with recent gradient-based post-training quantization techniques. Third, drawing estimation from straight-through estimation techniques, we introduce a novel gradient update definition to enable a proximal search of the codebooks and their mappings. The proposed jointly learnable codebooks and mappings (JLCM) method allows a very efficient approximation of any DNN: as such, a Llama 7B can be compressed down to 2Go and loaded on 5-year-old smartphones.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper compresses memory footprint in deep neural networks inference by a codebook-based approach, mainly solving the granularity problem and the training problem suffered by the previous works. This paper tried two methods to solve the granularity problem, setting per-channel scaling factors with one codebook or using multiple codebooks with weight matrix reordering. To enable proximal search thus solving the training problem, this method uses custom gradient updates inspired by STE.

### Strengths
1. In the experiment section, this method shows advantages over baselines.

2. This paper provides a detailed analysis of memory usage in different settings.

### Weaknesses
The paper has some unclear statements that require more explanation:

1.  The settings for the number of codebooks and the number of scaling factors should be further explained. Although the authors mention in the paper that these values are determined by compression goal, the process needs more details and therelationship with the weight distribution needs to be explained as well. Specifically, it is unclear how the target compression ratio directly translates into the number of codebooks or scaling factors. The paper lacks a clear explanation of the optimization process for these parameters given a target compression rate. It would be beneficial to understand if there is a search space and how the authors navigate it, and if there are any heuristics used to determine these values based on the characteristics of the weight distribution.

2. This paper does not explain how to cluster the neurons. There is also no data to prove that “two neurons far from each other in the weight matrix can be similarly distributed”. The clustering method is not specified, and it's unclear whether it's a standard algorithm like k-means or a custom approach. Furthermore, the claim about neurons far apart having similar distributions needs empirical validation. The paper should provide some visualization or statistical analysis to support this claim, as it is not immediately obvious that spatial distance in the weight matrix correlates with distributional similarity.

3. The meaning of the X-axis in Figure 1 is confusing. For different curves, the X-axis seems to have different meanings. These should be marked on the figure. The lack of clarity in the x-axis labels makes it difficult to interpret the results presented in the figure. The paper should clearly specify what each x-axis represents for each curve, and if different curves have different x-axis meanings, this should be explicitly stated and explained in the caption.

4. For the LLM experiments in Table 6, how are the results compared with more recent works, e.g., SqueezeLLM, AWQ, etc.

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a series of improvements to codebook-based weight compression schemes for deep neural networks with the aim of enabling larger models to fit in the limited on device storage for accelerators like GPUs. Their method is based on three core changes relative to existing methods. First, they apply a neuron re-ordering to group weights with similar distributions. This allows for finer-grained application of codebooks to weights without increasing the storage overhead of the compressed representation. Second, they propose to jointly learn the codebook and codebook mappings, similar to gradient-based post-training quantization schemes. Lastly, they modify the gradient update for the codebook mappings to enable more effective optimization.

### Strengths
Despite my lack of experience with the topic of this paper I found the text reasonably easy to follow. I think the paper is well written and the methods appear to be sound to me. In particular, the impact of part 3 of the proposed method (improved gradient estimator) seems to be considerable based on the ablation results presented in Table 4.

### Weaknesses
I am not an expert on compression of neural network weights for storage optimization but I did not identify any particular weaknesses in the methodology. The technique appears to be reasonable and the results appear to be sound based on my review of the paper.

### Questions
The neuron permutations you use in your method remind me of the channel permutations that are used by N:M sparsification methods [1]. Drawing this connection could be interesting in your related work section.

In a number of places you use “Go” as a unit - is this intentional? Was “Go” supposed to be “GB”?

In Table 2, I’m curious to understand how you implemented offloading of parameters to disk. Are transfers from disk to GPU pipelined with computation to hide as much transfer latency as possible? What batch sizes were used for each model?

[1] https://proceedings.neurips.cc/paper_files/paper/2021/hash/6e8404c3b93a9527c8db241a1846599a-Abstract.html

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The novel ALAM framework introduced in this paper leverages average quantization and a simple sensitivity calculation method to reduce memory usage in LLMs without affecting their training efficacy. This approach minimizes gradient variance by compressing activations to their group average values, allowing for effective compression to less than 1 bit. Additionally, ALAM employs a novel sensitivity calculation that uses the L2 norm of parameter gradients, greatly reducing memory overhead. In testing, ALAM achieves up to a 12.5× compression rate for activation memory in LLMs without sacrificing accuracy.

### Strengths
1.The paper applied a re-order method on neurons to reduce the memory overhead, which is quite novel.

2.This paper jointly optimized the mapping and codebooks, and the proximal search method can be used to the modified gradient update method.

3.The evaluation demonstrates the effectiveness.

### Weaknesses
1.It is hard to understanding the background part, especially the challenges of conventional approach. It would be better to provide a straightforward illustration with a figure or algorithm.
2.Some typos. In the beginning of sec3.2, “the” should be “The“; “ram” in sec 3.1 should be “RAM”; Something is missing in Equation 3.
3.The metric in evaluation part is accuracy and compression ratio. Can the proposed idea bring more benefits like accelerating the inference/training/finetuning?

### Questions
1.It would be better to explain why the second term $log(\Omega(C))\Omega(W)$dominates. It seems a common sense but I cannot see it in the context.

2.Can you provide some evaluation results in inference or training or finetuning performance in efficiency (throughput or energy efficiency)?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
