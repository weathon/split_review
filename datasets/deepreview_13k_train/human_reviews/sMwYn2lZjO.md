# Examining Post-Training Quantization for Mixture-of-Experts: A Benchmark

- Decision: Reject
- Scores: 6, 3, 6, 3, 5

## Abstract
Large Language Models~(LLMs) have become foundational in the realm of natural language processing, demonstrating performance improvements as model sizes increase. 
The Mixture-of-Experts~(MoE) approach offers a promising way to scale LLMs more efficiently by using fewer computational FLOPs through sparse activation.
However, it suffers from significant memory overheads, necessitating model compression techniques. 
Post-training quantization, a popular method for model compression, proves less effective when directly applied to MoE models due to MoE's overlooked inherent sparsity.
This paper explores several MoE structure-aware quantization heuristics, ranging from coarse to fine granularity, from MoE block to individual linear weight. 
Our investigations reveal critical principles: different MoE structures (\textit{i.e.}, blocks, experts, linear layers) require varying numbers of weight bits for effective and efficient quantization. Conclusions are supported by extensive benchmarking across two representative MoE models and six tasks. We further introduce novel enhancements to more accurately identify the most critical weights in MoE quantization that necessitate higher bit allocations, including the linear weight outlier scorer and MoE block scorer. Additionally, subsequent experiments validate our findings in the context of both weight and activation quantization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper empirically examines the quantization of MoE models across multiple dimensions, including granularity, significance, and bit allocation of various MoE structures, such as MoE blocks, experts, and linear layers. Extensive experiments are conducted on two representative MoE models to cover these aspects comprehensively.

### Strengths
1. The paper is well-structured and easy to follow.
2. The use of expert utilization and large weight outliers in linear layers as guidance for quantization is well-justified and effectively validated through extensive experiments.
3. This empirical study addresses many critical aspects of MoE structure importance, offering solutions to improve the accuracy-efficiency trade-off through targeted quantization.

### Weaknesses
While the paper explores various heuristic approaches to assess the importance of different MoE model structures, the reasons behind certain representational behaviors remain unclear. For example, in Figure 1, the visualization of expert usage across two MoE models is presented. A discussion on the underlying causes of these representation patterns and their potential generalizability to other models would enhance understanding. Specifically, the paper lacks a detailed analysis of why some experts are consistently more utilized than others, and whether this is due to inherent properties of the data, the routing mechanism, or the expert initialization. Furthermore, the paper does not investigate the potential for load imbalance among experts during inference, which could lead to performance bottlenecks and impact the effectiveness of quantization strategies. The analysis of large weight outliers, while useful, could be strengthened by exploring the relationship between these outliers and the specific tasks or data distributions that the model is trained on. This would provide a more nuanced understanding of how quantization affects different parts of the model.

### Questions
In Table 1, the gain of "frequent" over "random" expert selection is less pronounced when choosing 10 and 15 experts compared to 20 and 25 experts. Could you provide insights into why this difference is observed?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper argues that difference structures in MoE LLMs require tailored quantization strategy through extensive experiments with diverse settings. Further, several enhancements aiming at the discovered phenomenon are introduced to increase the quantization performance.

### Strengths
Firstly, this article fills the gap in research on benchmark research for Mixture of Experts MoE LLMs. Additionally, unlike other benchmarks that merely present experimental findings, the authors further proposes performance enhancement strategies based on the discovered quantization patterns.

### Weaknesses
1. For Q1 in Section 4.2, this discovery and conclusion are not novel, as numerous previous studies have already confirmed that expert usage frequency can serve as a good basis for compression, i.e., [1][2].

2. For Q2 in Section 4.2, in my opinion, there are significant issues with this viewpoint. In the experiments, the experts in the FFNN layers are randomly selected, which means that it is highly possible that in multiple tests, the activated experts are consistently quantized to 2 bits, while the experts remained at 4 bits are not actually utilized. Therefore, this cannot be used to conclude that quantization in the FFNN layers has a smaller impact on final performance compared to the attention layers.

3. For Q3 in Section 4.2, this is a critical issue because your own experimental data (Figure 5) reveal that you have drawn incorrect and contradictory conclusions. Specifically, in Q3, you assert the first blocks are more important than the last blocks and therefore need to be quantized to higher bits. However, in Figure 5 of Section 5.3, it can be seen that the importance scores of the last blocks are the lowest, indicating their highest importance and the need for higher bit quantization. This means that if comparative experiments between the first two blocks and the last two blocks are included in Table 2, the conclusion would no longer hold. Your own experimental results contradict your previous conclusions.

4. For Section 5.1, Although the authors claim that this work primarily focuses on weight-only quantization for MoE LLMs and their conclusions can be generalized to weight-activation quantization, the results in Table 3 actually demonstrate that weight-activation quantization needs to be thoroughly discussed. Normally, the performance of A4, A8, and A16 would gradually improve and the gaps would be significant. However, Table 3 presents a completely different conclusion: FP16 is not optimal in most cases. Therefore, I believe that it cannot be proven that the conclusions drawn from weight-only quantization for MoE LLMs can be fully applied to weight-activation quantization.

### Questions
1. For weakness2, the experiment would be more convincing if the experts selected are not random but are currently activated and quantized to 2/4/8 bits.

2. For weakness3, the content and conclusion in Section4.2-Q3 requires to be reformulated to correspond to Section 5.3 to avoid conflicts.

3. For weakness4, it is necessary to conduct an in-depth analysis of the causes of this phenomenon or to prove from other perspectives that the conclusions drawn from weight-only quantization can be generalized to the weight-activation scenario.

4. For Section 5.3, why only the results on DeepSeek-MoE model is provided? Mixtral family is also needed to be stay consistent with Table 2. 

5. In addition, in Section 5.3, as well known that MSE loss is generally considered as the formulation of quantization error, so what about incorporate MSE into the importance score predictor?

In summary, I consider there are several flaws in this paper that cannot withstand scrutiny. The authors need to carefully revise and improve it to enhance its persuasiveness.

------

[1] Li P, Zhang Z, Yadav P, et al. Merge, then compress: Demystify efficient SMoe with hints from its routing policy[J]. arXiv preprint arXiv:2310.01334, 2023.
[2] Huang W, Liao Y, Liu J, et al. MC-MoE: Mixture Compressor for Mixture-of-Experts LLMs Gains More[J]. arXiv preprint arXiv:2410.06270, 2024.

### Soundness
2

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
3

### Summary
This submission provides a comprehensive benchmark to explore post-training quantization (PTQ) in Mixture of Experts (MoE) models. The authors examine several heuristics for designing effective quantization methods, such as using coarse-to-fine granularity and allocating bits across different sub-structures. To validate these design choices, experiments were conducted on Mixtral-8x7B and DeepSeed-MoE-16B-base using GPTQ and SmoothQuant. The study evaluates the sensitivity of various layers and blocks to quantization, observing that some components, such as shared experts and the first expert blocks, require higher bit allocation, while attention layers tend to be more bit-efficient. Results across benchmarks like MMLU indicate that careful bit allocation can significantly enhance MoE performance. Additionally, the paper introduces an importance predictor to identify sensitive layers, which is practical in real-world applications.

### Strengths
1. This paper presents a thorough and comprehensive benchmark for addressing the bit allocation challenge in post-training quantization (PTQ), offering valuable insights into effective strategies for adaptively assigning bits to layers that are particularly sensitive to quantization. Furthermore, the authors propose an importance predictor aimed at identifying key layers, thereby reducing the need for repetitive quantization experiments. The empirical findings presented are expected to serve as a solid foundation for future research in this area.

2. The proposed methodology has been rigorously evaluated across several benchmarks and large language models (LLMs), which robustly support the main claims of the study. The paper is well-organized and clearly presented, making it accessible and easy to follow. This clarity of presentation is a notable strength, enhancing the impact and readability of the work.

3. The concept of allocating more bits to frequently activated experts and other sensitive layers is both innovative and practical. This paper offers a holistic approach to implementing this idea, from empirical experimentation to the development of carefully designed predictors. Such a comprehensive perspective makes this work particularly insightful for practitioners and researchers alike.

### Weaknesses
1. The primary weakness appears to be the somewhat marginal and inconsistent improvements provided by the proposed predictor. As shown in Table 5, results with the predictor are mixed when compared to simple baselines like FIRST and RANDOM. On the MMLU benchmark, in particular, the predictor does not demonstrate substantial improvement over these baselines.

2. The title may be somewhat overstated. This paper primarily addresses the sensitivity, or bit requirements, of various components within MOE models. However, the title may give an initial impression of a comprehensive evaluation of multiple MOE architectures or algorithms. A more precise title would improve clarity.

3. The observations from the benchmark lack a strong connection to the proposed method. The predictor currently relies on a magnitude-based approach, but there may be potential to develop a more tailored predictor based on the empirical findings. For instance, could an allocator be learned through reinforcement learning to better capture these insights?

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes post-training quantization for MoE LLMs. In particular, the authors propose a benchmark for evaluating the effectiveness for MoEs. These benchmarks test different facets of compression, including mixed compression setups. Using this benchmark, the authors find different mixed compression strategies.

### Strengths
1. The paper directly tackles the most salient pain point of LLM inference latency -- namely, their memory bound. This work also explores the intersection of two commonly-used methods: post-training quantization, and mixtures-of-experts LLMs.
2. The core insight is interesting to consider: Experts are each used with different frequencies, and it seems intuitive that more frequently-used experts should be given more model representation. One way to achieve this is to allocate different numbers of bits in their quantized representation.
3. The structure in the methods is slightly unorthodox, but I like that the core question is highlighted, then immediately answered. Unconventional as it may be, I find this clearer than the usual generic 'Quantization', 'Quantization with X' titles that aren't very descriptive. The conclusion to Q1 is fairly expected (the more uneven the router distribution, the more than frequency-based allocation helps), but that's a good thing. Clear question and intuitive results.

### Weaknesses
1. Strength #2 is poorly communicated and should be emphasized much earlier on. To the author's credit, this idea was probably already obvious by the time they sat down to write the abstract. To me as a new reader though, this just seemed like a haphazard combination of two frequently-seen ideas in LLM papers. It didn't occur to me, until the methods section, that MoEs were natural benefactors of mixed compression. This should've been emphasized, especially on L71 next to "(Q)". Rather than touting the different ablations you ran, focus on this core insight. The same goes for the abstract. Different granularities of quantization are not the most interesting; that again just sounds like extensive ablations -- but, mixed compression + MoEs are interesting. I would also suggest revising the title to better reflect this. I appreciate that PTQ is very clearly stated upfront, to set expectations, but "mixed compression for mixtures-of-experts" would more clearly convey the idea.
2. The methods section should be reorganized. Instead of presenting a series of experiments -- what looks like 'ablations' -- as your main results, instead present your main result first. A clearly defined Table 1 with your best, highest quality numbers that I (or other researchers) can easily reference when comparing against other methods. *Then, present the remainder of the studies as ablations on top of your method.
3. Quality for the method is very poor. The core results in Table 3 are all guessing accuracy. This doesn't mean that the proposed activation quantization strategy is 'good' -- all it means is that the 'original' weight-quantized model was so bad, it couldn't do any worse. Winogrande is a binary classification task, so the ~50% accuracies are all the same, effectively. Likewise, hellaswag is 4-way classification, so 25% is also guessing. PIQA is binary as well, so ~50% is guessing. I don't think those differences, so close to guessing, are meaningful.
4. There seems to be a few baselines missing, which make it hard to assess the quality of this method. For example, in Table 1, it'd be worth including the original FP16 accuracy. The random baseline is good. What if we uniformly applied NF3, 3-bit GPTQ, or SqueezeLLM to all experts, for example? I have no vested interest in these particular methods, but any sort of baseline along these lines -- where we eliminate the mixed compression part. I trust this baseline would be worse than your method.
5. The extended study section is confusing. It looks like each section is a mini-paper of its own, with insights, methods, experiments, and visualizations. Instead of introducing a potpourri of techniques, either (a) reorganize so that this method is presented in the Methods section or (b) drop this, and simply truncate the paper to 8 pages.

### Questions
In short, I'm giving a reject because the paper needs a major rewrite. The core insight is there and is interesting, but there are pretty big problems with organization throughout. I believe the rebuttal paper allows you reupload a copy of the paper; if you can refactor the paper in that compact period of time to organize sec 5 and present a 'main' table 1, remove observations that are based on guessing accuracies (or improve SmoothQuant results to be better than guessing), then I would bump up my score. I think a week is way too short a time to do this, but I'm open-minded about being wrong.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a benchmark of post-training quantization techniques specifically tailored for Mixture-of-Experts models, with the objective of reducing memory overhead without necessitating retraining. The authors propose MoE-aware quantization heuristics, revealing that varying bit allocations across different MoE components—such as blocks, experts, and layers—enhances quantization efficiency. Extensive experiments on two representative MoE models, Mixtral-8x7B and DeepSeek-MoE-16B-base, across six tasks substantiate the efficacy of these techniques. The study further introduces strategies, , including novel enhancements such as expert usage frequency, linear weight outlier scoring, and block importance prediction to optimize quantization efficacy.

### Strengths
● This paper presents the first benchmark specifically for post-training quantization tailored to the MoE architecture, addressing a relevant and timely topic given the computational demands of large language models. 

 ● The proposed quantization techniques are impactful for enhancing the memory efficiency of MoE models, potentially enabling more resource-effective deployments. 

● The authors validate the effectiveness of their proposed heuristics through thorough comparisons with existing quantization methods, offering detailed empirical insights into optimal bit allocation across different MoE components

### Weaknesses
● The paper focuses primarily on FFNN-based MoE structures and does not extend the evaluation to other variants, such as Attention MoE. Since MoE techniques are versatile and implemented in diverse configurations, it would be beneficial to investigate whether the proposed quantization heuristics, like expert usage frequency and block importance prediction, generalize well to other MoE types. Specifically, the absence of experiments on Attention-based MoE architectures leaves a significant gap in understanding the robustness of the proposed techniques. The behavior of attention mechanisms can differ substantially from FFNNs, particularly in terms of activation patterns and sensitivity to quantization, which could render the current heuristics ineffective or require substantial modifications. Without empirical validation, the general applicability of the proposed methods remains uncertain.

● The use of WikiText as calibration data and as input for training the block importance predictor might limit the generalizability of the predictor across tasks or data types. WikiText, while useful, may not capture the diverse behaviors and importance of various MoE blocks, particularly for complex or varied NLP tasks that MoE models often encounter. Relying solely on WikiText may constrain the predictor's ability to generalize accurately for determining block quantization importance across broader applications of MoE models. The predictor's performance might degrade when applied to tasks involving different linguistic styles or data distributions, such as code generation or specialized domain texts, where the block importance patterns could significantly differ from those observed in WikiText.

● Certain methodological aspects, such as the normalization step in Equation (3) for calculating expert usage frequency, are not clearly explained. While normalization presumably aims to ensure that routing scores sum to 1 across experts in an MoE block for clearer usage distribution interpretation, the authors do not specify the type of normalization applied (e.g., min-max scaling, softmax). This lack of clarity makes it difficult to reproduce the results and understand the precise impact of the normalization on the expert usage frequency calculation. The choice of normalization method can significantly affect the resulting usage scores and, consequently, the effectiveness of the quantization strategy.

●  The quantization methods  for MoE are primarily pseudo-quantization techniques and lack guidance on how they would translate to practical hardware implementations. Specific hardware constraints, including compatibility with fixed-point formats (e.g., INT8, INT4), efficient memory access patterns, and sparse routing support, are not addressed in detail. Additionally, the heterogeneous bit allocation across different layers, experts, and blocks may lead to unstructured patterns that complicate real-world hardware deployment, making it difficult to efficiently map these techniques onto current hardware platforms. The paper does not discuss the potential overhead of managing mixed-precision data formats and the associated memory access challenges, which are critical for practical implementation.

●  Finally, training a predictor to determine block importance may introduce computational overhead, potentially impacting inference time and contradicting the goal of efficient deployment. The paper does not discuss this aspect, leaving open questions about the predictor's scalability and its impact on real-time performance. The computational cost of training and deploying the predictor, especially for larger models, needs to be quantified to assess the overall efficiency gains of the proposed quantization method. The paper should also discuss the memory footprint of the predictor and its impact on resource-constrained environments.

### Questions
● Q1: Could the authors clarify if they expect the proposed quantization heuristics, such as expert usage frequency and block importance prediction, to be effective for other MoE configurations, such as Attention MoE?

● Q2: The block importance predictor was trained on WikiText data, which may not encompass the full diversity of tasks for MoE models. Could the authors clarify whether they believe WikiText fully represents the characteristics necessary for predictor generalizability? If not, would the authors consider testing the predictor on broader datasets or providing an analysis of the limitations that may arise from using WikiText as the sole source of calibration data?

● Q3: In Equation (3), the normalization procedure for calculating expert usage frequency is not fully defined. Could the authors specify the exact type of normalization applied (e.g., softmax, min-max scaling) and its purpose?

● Q4: The paper outlines methods that seem primarily focused on pseudo-quantization rather than real-world hardware deployment. Could the authors discuss the feasibility of implementing these techniques on practical hardware platforms, particularly with regard to compatibility with fixed-point formats (e.g., INT8, INT4), efficient memory access, and sparse routing support? Additionally, how might the heterogeneity in quantization across different layers, experts, and blocks impact structured deployment on hardware?

● Q5: Training a predictor for block importance may introduce computational overhead, potentially affecting inference time and efficiency. Could the authors address whether this training impacts real-time performance and if there are any strategies to mitigate this overhead, especially for larger models?

### Soundness
2

### Presentation
3

### Contribution
2
