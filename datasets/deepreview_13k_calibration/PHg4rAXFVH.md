# RTop-K: Ultra-Fast Row-Wise Top-K Selection for Neural Network Acceleration on GPUs

- Decision: Accept
- Avg Score: 6.50
- Scores: 5, 10, 6, 5

## Abstract
Top-k selection algorithms are fundamental in a wide range of applications, from high-performance computing and information retrieval to big data processing and neural network model training. In this paper, we present RTop-K, a highly efficient parallel row-wise top-k selection algorithm specifically designed for GPUs. RTop-K leverages a binary search-based approach to optimize row-wise top-k selection, providing a scalable and accelerated solution. We conduct a detailed analysis of early stopping in our algorithm, showing that it effectively maintains the testing accuracy of neural network models while substantially improving performance. Our GPU implementation of RTop-K demonstrates superior performance over state-of-the-art row-wise top-k GPU implementations, achieving speed-ups ranging from 4.25× to 9.51× with early stopping, and 3.94× without early stopping. Moreover, RTop-K is capable of accelerating the overall training workflow of MaxK-GNNs, delivering an average speed-up of 9.76% to 31.53% across different models and datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper presents RTop-K, a GPU acceleration of row-wise TopK selection. The proposed algorithm is based on binary search. Also, it introduces the early stopping strategy to improve the performance further. The experimental results show that it outperforms the state of the art row-wise TopK implementation.

### Strengths
1. The paper is well organized and easy to follow.
2. This work addresses one of the key component in the GNN training.

### Weaknesses
1. Regarding the kernel performance comparison, the authors compares the solution with the PyTorch. The proposed solution should be compared with other topK solutions, like Shanbhag et al. [1], or radix select-based etc--assessment that "not suitable for GNN is not sufficient", in my opinion. Besides, I am not sure the recent PyTorch is the best baseline to compare, as I see some complaints that it is slower than torch.sort (I am not sure whether this is already resolved or not).

2. Limited applicability: the experiment shows the speedup for Max K-GNN (includes GraphSAGE, GIN, GCN) in the only. Not sure if there's a broader impact on other DL networks.
3. Theoretical analysis on early stopping.
4. It'd be great if you can mark speedup on Fig. 4
5. How the implementation is close from the roofline? Can you please share the Nsight profiling results?
6. Is TopK bottleneck in the GNN? Can you please share the breakdown results, not just showing the portion of the TopK part?

### Questions
Please refer to Weakness above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper looks at performing top-k row-wise selection in matrices that are, broadly, tall and skinny – with fewer than 1000 elements per row but perhaps millions of rows. Most existing algorithms focus on the opposite regime – relatively few rows that are much longer – and this distinction is important for designing performant GPU implementations. The authors introduce an algorithm that seeks to outperform alternative approaches, including the default RadixSelect algorithm in PyTorch, and is designed for the hardware, using warp-level parallelism within a row and careful use of the cache hierarchy. They also introduce an early stopping version of the algorithm that uses a fixed number of iterations, as load imbalance across warps/rows could significantly decrease the potential speedup. Results are shown in two settings. First, they consider the performance of the algorithm with and without early stopping on synthetic data, evaluating the number of iterations required and finding acceptable error rates when using early stopping. When compared with PyTorch’s implementation, they find substantial speedups (2-6x). Second, the implement their top-k in a few max-k GNN algorithms, like SAGE, where top-k calculations account for a non-trivial amount of runtime, and test on a few benchmark graph datasets. They report speedups of 10-30% and, with early stopping, find that model test accuracy fluctuates around that expect from using the optimal top-k values.

### Strengths
This is a good study. Despite the field being well-studied, their approach is fairly original. It really sets aside what has typically been done and asks, for this context, precisely what does the algorithm need to do and on what hardware would it run. The consideration of the appropriate level of parallelism based on both GPU hardware constraints and problem size considerations is thoughtful, and they get to a nice answer. The paper is quite well written and was pleasantly easy to read.

The GNN test doesn’t have a ton of detail, but is well conducted and does a nice job of rounding out a clear ML story from an otherwise pure HPC-focused study.

### Weaknesses
I debate whether this is a better baseline comparison that PyTorch’s RadixSelect. As the authors suggest, it solves a somewhat more difficult problem – sorting. I don’t disagree with the comparison for the GNNs, as it is the operational default, but it was more difficult for me to interpret the value of the speedups is in the synthetic data top-k test. 

I would have liked the authors to push the bounds on the algorithm a little more. I understand the regime they tested is representative of a standard family of networks, but I would have liked to see another version of at least Figure 4 which looked at increasing M to ~10^4 or even 10^5 . This would indicate potential places where GPU cache/warp size limitations cause behavior to deteriorate, or suggest where the line between better performance with this algorithm vs more traditional approaches like RadiK is crossed.

### Questions
The authors did a nice job of taking an HPC paper and providing a compelling presentation for an ML setting. But, as suggested above, I feel it would be a better paper in itself (if admittedly not necessarily for this venue) if the authors considered how it would perform for large M and more general guidance could be given to researchers on where to switch between algorithms.

### Soundness
3

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
2

### Summary
RTop-K is an efficient parallel row-wise top-k selection algorithm for GPUs, leveraging a binary search-based approach to significantly enhance performance in neural network training and inference. This algorithm achieves speedups ranging from 4.25 to 9.51 times compared to existing GPU top-k implementations, and it also improves the overall training workflow of MaxK-GNN by 9.76% to 31.53%. Furthermore, RTop-K, when combined with the Early Stopping technique, maintains model accuracy while enhancing efficiency through reduced resource requirements.

### Strengths
1. RTop-K shows a 4.25- to 9.51-fold speedup over existing state-of-the-art GPU-based row-wise top-k implementations, demonstrating in particular performance improvements in GNN training and inference.  It is meaningful that RTop-K is designed based on efficient parallel processing and resource optimization.
2. RTop-K adopts an approximation method to select the top k elements from each row without sorting, reducing computational time complexity and accelerating neural network training.

### Weaknesses
1. What is the method to overcome the limitations of approximation methods used by algorithms?
2. Is resource optimization a general methodology? In the paper, the performance of RTop-K is likely to depend on a particular GPU architecture (A6000). Therefore, it is necessary to review whether usabilty is secured in other GPU environments or structures.
3. RTop-K is optimized for limited-sized vectors, but there seems to be a lack of discussion on how resource consumption and memory management are performed on very large datasets.

### Questions
See weakness.

### Soundness
3

### Presentation
3

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
This paper presents RTop-K, a GPU-based algorithm that enhances the efficiency of row-wise top-K selection, specifically targeting Graph Neural Network (GNN) applications. The authors use a binary search strategy with optional early stopping to streamline top-K selection, offering a significant reduction in computational demands while preserving accuracy. Experiments show RTop-K provides speedups of 4.25× to 9.51× relative to PyTorch’s top-K implementation and achieves up to 31.53% faster training when integrated into GNN workflows.

### Strengths
1,Relevance and Novelty: The paper addresses an important computational bottleneck in GNN acceleration, offering an innovative approach with practical speed improvements for real-world applications.

2,Comprehensive Experimental Validation: The experimental analysis is thorough, showing RTop-K’s efficacy both as a standalone kernel and within the GNN training workflow across various architectures and datasets.

3,Effective Use of Early Stopping: The early stopping mechanism is a valuable addition, providing computational savings without significantly impacting model accuracy.

4,Reproducibility: The paper provides detailed descriptions of the algorithm and implementation, along with pseudocode, which improves replicability and clarity for the audience.

### Weaknesses
1,Ablation Study on Implementation Optimization: The paper describes a GPU implementation with several stages (loading, searching, and selecting) but could benefit from a breakdown of how each stage contributes to the overall speedup. A detailed analysis of performance gains per stage would shed light on optimization details. Additionally, an ablation study examining how binary search and early stopping impact efficiency would highlight their specific contributions and help readers better understand the trade-offs involved.

2,Scalability Results on Hidden Dimensions: While the paper provides scalability results for different values of K, it lacks scalability analysis on various hidden dimensions, which is equally important for understanding the algorithm’s performance on high-dimensional data, as seen in some GNN and non-GNN applications.

3,Guidance on Hyper-Parameter Tuning: The RTop-K algorithm involves critical hyper-parameters, specifically the precision value (ϵ') in Algorithm 1 and max_iter in Algorithm 2. Some discussion on how to set these parameters effectively across different tasks would enhance usability. A sensitivity analysis for these parameters could guide users in balancing performance with computational efficiency.

4,Lack of Comprehensive Baselines: The paper compares RTop-K primarily with PyTorch’s row-wise top-K implementation. Including comparisons with other top-K selection algorithms, such as Avg-TopK and TopK-SGD, which are popular in neural network training, would provide a more complete evaluation of RTop-K’s performance and position it within the broader field.

5,Discussion on Broader Applicability: While the paper focuses on GNN applications, top-K selection is widely used in various domains, such as expert selection in Mixture of Experts and vector search in large models like GPTs. A discussion on potential extensions of RTop-K to other contexts would strengthen the paper, showcasing its broader utility across different neural network architectures and tasks.

6.Contribution. summary of something, in this case, GPU top-K selection alrorithms, should not be the contribution of one research paper.

### Questions
Except for the weaknesses above, I have several questions about this work.

1, Just integrating the binary search into the top-K selection sounds not innovative, so can the authors dig more novelty from this work? Besides, I am curious that what searching performance improvement will using binary search bring, compared with not using binary searching. 

2, The authors claim the parallel top-K selection algorithm, but what are the specific 'parallel' mechanism is NOT clear. It seems that, just many single top-K selection are executed on GPU platform. Can the authors explain this? If my understanding is correct, then this paper should not emphasize the "parallel"?

### Soundness
2

### Presentation
2

### Contribution
1
