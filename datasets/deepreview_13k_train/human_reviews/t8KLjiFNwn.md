# Sparse Learning for State Space Models on Mobile

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Transformer models have been widely investigated in different domains by providing long-range dependency handling and global contextual awareness, driving the development of popular AI applications such as ChatGPT, Gemini, and Alexa.
State Space Models (SSMs) have emerged as strong contenders in the field of sequential modeling, challenging the dominance of Transformers. SSMs incorporate a selective mechanism that allows for dynamic parameter adjustment based on input data, enhancing their performance.
However, this mechanism also comes with increasing computational complexity and bandwidth demands, posing challenges for deployment on resource-constraint mobile devices.
To address these challenges without sacrificing the accuracy of the selective mechanism, we propose a sparse learning framework that integrates architecture-aware compiler optimizations. We introduce an end-to-end solution--$\mathbf{C}_4^n$ kernel sparsity, which prunes $n$ elements from every four contiguous weights, and develop a compiler-based acceleration solution to ensure execution efficiency for this sparsity on mobile devices.
Based on the kernel sparsity, our framework generates optimized sparse models targeting specific sparsity or latency requirements for various model sizes. We further leverage pruned weights to compensate for the remaining weights,  enhancing downstream task performance.
For practical hardware acceleration, we propose $\mathbf{C}_4^n$-specific optimizations combined with a layout transformation elimination strategy. 
This approach mitigates inefficiencies arising from fine-grained pruning in linear layers and improves performance across other operations. 
Experimental results demonstrate that our method achieves superior task performance compared to other semi-structured pruning methods and achieves up-to 7$\times$  speedup compared to llama.cpp framework on mobile devices.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a mobile-friendly solution for SSMs, targeted for on-device inference. Specifically, the authors propose a sparsification & pruning method of contiguous weights along with a reordering operator for efficient on-device execution. Last, they introduce a sample-efficient compensation algorithm that recovers any lost accuracy. Results showcase gains of from 3.2x to 7x without gradual accuracy degradation as a function of sparsity.

### Strengths
* The paper contributes both an algorithmic/architectural change and a system hardware component implementation for efficient on-device execution, across CPU and GPU backends, which is evaluated on device.
* There has been great effort put in the evaluation and comparing against various baseline methods and models.
* The proposed method, albeit involved, is straightforward and through the ablation we witness the importance of each component in the resulting accuracy.

### Weaknesses
 * The proposed technique has only been applied to one SSM architecture (Mamba) and evaluated on a single high-tier device. The lack of diversity in both model architecture and hardware platform limits the generalizability of the findings. It is unclear if the observed performance gains would translate to other SSM architectures, which may have different computational characteristics or memory access patterns. Furthermore, the reliance on a single high-tier device does not provide insights into the method's performance on resource-constrained devices, which are often the target for on-device ML.
* The on-device ML literature is quite old and there have been various contributions from 2018 onwards, also focusing on LLMs (see [a,b]). The paper does not adequately contextualize its contributions within the broader landscape of on-device machine learning, particularly concerning recent advancements in efficient inference techniques for large language models. The cited works [a,b] highlight the need for a more thorough comparison with existing methods.
* The advertised gains are not quoted over the same accuracy threshold. The 7x speedup claim is misleading, as it is achieved at the cost of significant accuracy degradation. The paper lacks a clear presentation of the trade-off between speed and accuracy, making it difficult to assess the practical utility of the proposed method. The absence of speedup numbers for a sub-1% accuracy degradation further obscures the true performance benefits.

### Questions
### Evaluation

* In the introduction, the authors quote that "llama.cpp takes over 5.8s to generate a single token with Mamba-2.8B", However, in table 3 of the evaluation, a similar setup is quoted at 0.4 tokens/sec = 2.5s per token. Could the authors clarify the source of this discrepancy?
* Although the performance benefits seem impressive at first sight, the 7x gains quote is quite misleading, as it comes with significant accuracy degradation. For a sub-1% degradation, the speedup gain is not quoted on Table 3.
* Why does Table 3 miss GPU execution for llama.cpp?
* In Section 6.2, the average column seems to represent an non-weighted average across the datasets, thus not taking into consideration the size of each task. Is this correct?

### Omissions / Extensions

* Results have only been benchmarked on a single high-tier device with 16GB of memory. I am wondering how the proposed solutions work on lower-end devices that do not have these level of resources. At the same time, it would be very interesting to quantify the energy requirements of running such workloads on device.
* A comparison with a similarly-sized Transformer-based LM would greatly enhance the evaluation and put the gains into perspective. Table A3 partly accomplished this, but there is no quantification of on-device performance.
* Furthermore, it would be valuable to see how these gains compare with different compression methods, such as quantization for example.
* Would there be any limitations of the method being applied to other modalities, such as vision (see Vision Mamba [c])
* Since SSMs come with memory benefits, as quoted in §3, it would be important to highlight the peak memory consumption of the pruned models during inference.
* It would be very insightful to visualise the sparsity per block in the resulting model to see if there is some kind or pattern in the pruning dynamics.

### Questions

* How does the compiler select the best layout per operator for different target devices?
* What is the overhead during training of the models with the proposed method? Are there gains from pruning during training?

[a] Xu, J., Li, Z., Chen, W., Wang, Q., Gao, X., Cai, Q., & Ling, Z. (2024). On-device language models: A comprehensive review. arXiv preprint arXiv:2409.00088.  
[b] Liu, Z., Zhao, C., Iandola, F., Lai, C., Tian, Y., Fedorov, I., ... & Chandra, V. (2024). Mobilellm: Optimizing sub-billion parameter language models for on-device use cases. arXiv preprint arXiv:2402.14905.  
[c] Zhu, L., Liao, B., Zhang, Q., Wang, X., Liu, W., & Wang, X. (2024). Vision mamba: Efficient visual representation learning with bidirectional state space model. Forty-First International Conference on Machine Learning (ICML).

### Nitpicking

* Table 1: sparsity typo
* Numbering issue on remarks (i.e. missing remark 5.1)
* Section 6.4: LAMBDA -> LAMBADA

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Recently, State Space Models (SSMs) are gaining attention in sequential modeling problems. However it comes with increasing computational complexity and bandwidth demands. This paper proposes a sparse learning framework with architecture-aware compiler optimizations. This proposal includes 1. optimized kernels, 2. sparsity or latency oriented learning framework that uses 1.

The paper is too abstract to provide sufficient insight to readers. It seems that the framework and the algorithm provided seems to be a reasonable contribution. hence the score of 5: marginally below the acceptance threshold.

### Strengths
As the on-device AI is an important topic w.r.t privacy issues, it is an important direction to explore.

The paper seems to build a framework that reduces the computational intensity of the SSMs (which already is lower computational complexity than currently dominant Attention) seems to be a good direction.

It seems that the paper is claiming to have combined a number of compiler optimizations making it an end-to-end solution over simply exploring an algorithm-only or compiler-only or HW-only solution.

### Weaknesses
The paper is very difficult to understand. It seems that there are a lot of abstract explanations without concreteness that makes it difficult. Maybe adding some figures of what is really happening might help. For example, the paper states "our kernel is designed as Cn4 , which removes n elements from every group with four adjacent weights." There may be multiple ways by which this could happen and the paper does not dive into details.

It is unclear how the proposed sparse learning framework practically addresses the computational complexity of SSMs. The paper mentions optimized kernels and compiler optimizations but lacks specific details on how these are implemented and how they interact with the underlying SSM computations. The description of the kernel design, specifically the Cn4 notation, is insufficient to understand the actual pruning strategy. For instance, it's not clear whether the 'n' elements are chosen randomly, based on magnitude, or using some other criteria, and how this choice impacts the model's performance. Furthermore, the paper does not clearly explain how the weight compensation method works and how it helps in maintaining the accuracy after pruning. The lack of concrete examples and visualizations makes it difficult to assess the practical effectiveness of the proposed approach.

The paper also lacks details on the compiler optimizations. It is not clear what kind of compiler is used, what kind of optimizations are performed, and how these optimizations are integrated with the proposed sparse learning framework. The paper mentions that the compiler optimizations are architecture-aware, but it does not specify which architectures are targeted and how the optimizations are tailored to those architectures. Without these details, it is difficult to evaluate the generality and effectiveness of the proposed approach. The paper also does not provide any details on the memory access patterns and cache hit rates, which are crucial for evaluating the performance of the proposed approach.

### Questions
* Is there any performance impact associated with Remark 5.2.

* How long does this "sparse learning take" it seems like the computation seems to be quite complicated and may prolong the "learning" by a big factor. Can you provide some data?

* It seems that the work includes some compiler optimization that itself could be large enough to account for a separate paper. Can you provide more details to the infrastructure used? Is this some open-source work? Is this published anywhere?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a novel learning framework for state space models (SSMs) that emphasizes kernel sparsity to enhance performance on mobile devices. The approach optimizes for an ideal balance between sparsity, latency, and accuracy, enabling an efficient pruning strategy suited for mobile hardware. With a robust theoretical foundation, the framework accounts for sparsity levels and latency impact on accuracy. Further, the authors incorporate hardware efficiency through architecture-aware compiler optimizations, including weight reordering, sparse weight storage, and eliminating layout transformations, achieving state-of-the-art (SOTA) results in accuracy at comparable or higher sparsity levels.

### Strengths
* Focus on Mobile Efficiency: The paper addresses a critical need for efficient execution of SSMs on mobile devices by optimizing for kernel sparsity without sacrificing accuracy, a valuable contribution to resource-constrained deep learning.
* Strong Theoretical Foundation: The proposed framework’s theoretical backing adds credibility, ensuring that the optimizations in sparsity and latency are rigorously derived, rather than heuristically implemented.
* Effective Hardware-Aware Optimization: Integrating architecture-aware compiler optimizations to handle sparse weight storage and reordering is a practical enhancement, boosting hardware efficiency while maintaining performance. This integration yields improved results over SOTA methods, showcasing either better accuracy for the same sparsity or higher sparsity for the same accuracy.* * Performance Presentation: The authors provide strong quantitative support,

### Weaknesses
 * More discussion of latency trade-offs relative to different levels of accuracy and sparsity on the same model would be valuable for considering real-world deployment.
* A minor improvement could be made by bolding or highlighting the best results in each column of Table 2 for easy reference.

### Questions
* Could additional metrics be included for deployment feasibility? Metrics like power consumption and memory consumption could provide more insights for real-world deployment on mobile devices.

### Soundness
3

### Presentation
3

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
The paper introduces a solution for accelerating inference using the Mamba SSM on mobile devices. The solution includes a framework for pruning the model’s weights and an assortment of optimizations to improve inference execution, such as weight reordering, operator fusion, and layout transformation elimination. Experiments using different sizes of the Mamba model show that the presented sparsification method achieves better accuracy than other semi-structure pruning methods, namely SparseGPT and Wanda. The authors’ solution outperforms llama.cpp when running inference with Mamba on the CPU of a Snapdragon 8 Gen2 SoC, and exhibits further speedup on the GPU.

### Strengths
Overall, the sparse-learning framework for exploring pruning strategies for Mamba’s weights is promising. Furthermore, experimental results show an improvement in accuracy compared to other semi-structure pruning methods, SparseGPT and Wanda.

### Weaknesses
The paper presents an end-to-end solution, starting from a specific model, Mamba, pruning its weights, applying optimizations, and executing inference on a mobile SoC. Although such work must involve considerable engineering to implement the different stacks comprising the solution and gluing them together, it does not automatically produce any interesting results for the research-oriented community. Were there any particular challenges that had to be overcome, driving the development of specific innovations in the process? I do not see any such discussion in this submission. Although there can be innovations in the individual components, the full-stack presentation fails to sufficiently highlight them as, inevitably, we only get a rather shallow look into each one, both qualitatively and quantitatively. I am elaborating on that for every main component below.

The sparse-learning framework is very interesting, and the authors present improvements compared to other state-of-the-art pruning methods. However, the presentation is lacking. Are there other similar approaches to the Cn4 kernels? What is the related work here? SparseGPT and Wanda were initially developed for transformer-based models. Can the presented kernels tackle such models? If yes, how do they compare against the state of the art? If we are only looking at SSMs, why only Mamba? What about, e.g., S4 and H3?

The optimization workflow presented supposedly targets mobile devices. However, there is no explanation for why these optimizations are particularly good just for mobile devices and not all computational devices. The cited lack of “high throughput memory” (HBM?) on mobile devices is weak. All modern CPU and GPU architectures, both mobile and desktop/server, suffer from expensive data movement. Therefore, optimizations that reduce it are of general benefit. They may not offer equal benefit to all devices, but we cannot tell because there are no such comparisons in the paper. Maybe the optimizations take advantage of specific aspects of mobile architectures? There is no clear indication. There is a short discussion on SIMD units, but these are not fundamentally different between mobile and desktop/server devices.

There is a high-level description of the optimization workflow, but it is difficult to tell if any interesting innovations exist. Much prior work exists on optimizing sparse operations by reordering the non-zeros and introducing custom hierarchical sparse formats, such as the ParTI! Library (https://github.com/hpcgarage/ParTI). Other examples of prior work are DNNFusion (https://dl.acm.org/doi/10.1145/3453483.3454083) for operator fusion and SmartMem (https://dl.acm.org/doi/10.1145/3620666.3651384), which specifically addresses layout transformation elimination for mobile DNN execution. I am not saying that any of the above works are necessarily super relevant to the authors’ submission or that they need to be addressed, but if you are going to claim “a set of comprehensive compiler optimizations, including Cn4-specific optimizations and layout transformation elimination strategy on mobile devices” as a significant contribution, it will help to put your work into a better context.

The paper compares performance against llama.cpp. The authors provide an insight into why their solution is faster. Paraphrasing from their supplemental material, llama.cpp relies on a fixed pattern matching strategy to identify and fuse operation combinations, an approach that fails to recognize new combinations. Although llama.cpp is popular for executing transformer-based models, is it decent with SSMs? Aren’t there any better ways to execute Mamba and compare against them? If we are currently limited to llama.cpp because it is the only inference engine out there that currently supports Mamba and mobile, I would question if it is a “bad” baseline and how interesting the results are in the first place.

### Questions
- Is your sparse kernel design and sparse learning approach unique, or is there prior related work?
- Can your approach work for transformer-based models? If yes, have you done any accuracy comparisons?
- Have you tested your approach with other SSMs? If yes, do you have any accuracy comparisons?
- Why are your optimizations particularly good for mobile devices? Do you have any comparisons of the effects of your optimizations on mobile and desktop/server devices?
- Can you comment on the novelty of your optimizations compared to related work?
- Can you run your solution on non-mobile devices? If yes, do you have any results?
- How can your approach be extended to NPUs?
- You state in the paper that Mamba-370M achieves in your tests an average accuracy of 50.0%, while your 30%-sparse version achieves 50.6%. However, if one looks at the individual tests, there is no test where your version achieves higher accuracy than the original. Is there a typo?

### Soundness
3

### Presentation
1

### Contribution
2
