# A Simple and Effective Pruning Approach for Large Language Models

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
As their size increases, Large Languages Models (LLMs) are natural candidates for network pruning methods: approaches that drop a subset of network weights while striving to preserve performance. Existing methods, however, require either retraining, which is rarely affordable for billion-scale LLMs, or solving a weight reconstruction problem reliant on second-order information, which may also be computationally expensive. In this paper, we introduce a novel, straightforward yet effective pruning method, termed \methodlong, designed to induce sparsity in pretrained LLMs. Motivated by the recent observation of emergent large magnitude features in LLMs, our approach prunes weights with the smallest magnitudes multiplied by the corresponding input activations, on a \textit{per-output} basis. Notably, \method requires \emph{no} retraining or weight update, and the pruned LLM can be used \emph{as is}. We conduct a thorough evaluation of our method Wanda on LLaMA and LLaMA-2 across various language benchmarks. \method significantly outperforms the established baseline of magnitude pruning and performs competitively against recent method involving intensive weight update.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript shows structured and unstructured pruning of LLMs can be successful if the pruning score accounts for the magnitudes of the $\textbf{W}$eight $\textbf{and}$ the $\textbf{a}$ctivation that the weight multiplies ($\textbf{Wanda}$). This approach is motivated by the observation that outlier activations with large magnitudes exist in LLMs, so pruning based on weight magnitudes alone can destroy salient computations of LLMs.

The pruning approach requires one forward pass, does not necessitate retraining, and causes minor performance degradation when applied to pretrained networks (larger networks are more tolerant of Wanda and pruning generally).

The reasons for Wanda's strong performance (e.g., against competitors like SparseGPT) are explored in convincing mathematical analyses and ablation studies that overall support the design decisions of Wanda, despite their simplicity.

### Strengths
Broadly, the manuscript gives timely insight and intuition for the problem of LLM pruning. Its proposed approach solves several problems with LLM pruning, making it faster, more performant, and simpler.

The authors make a helpful connection of their approach (Wanda) to existing work (SparseGPT), showing the similarity of their pruning scores when an assumption is made on the Hessian structure. This helps justify the pruning score used by Wanda, which is surprisingly principled given its simplicity (the connection to LeCun et al., 1989, is also nice). 

The observation that Wanda's choice of granularity ("[comparing] and [removing] weights on a per-output basis") is important to LLM performance but not image classifier performance is very significant and (as far as I know) original.

### Weaknesses
The main weakness of the manuscript is that it leaves unclear the benefits of Wanda to inference speed. While Wanda can accelerate matrix multiplications (Table 6), readers will be left curious about how inference timings are affected by Wanda. As my question below clarifies, this can be easily addressed.

### Questions
Score-affecting:

1. Can you please show full-model inference speeds for Wanda-pruned and dense networks? If you contextualize the matrix multiplication speedups of Table 6 with inference timings, the efficiency community can better understand the most relevant ways to build on the submitted work.
   - For example, as a reader interested in speeding up inference, I am unsure if the most promising next step is to figure out how to prune more weights with Wanda, or if the best next step is finding a distinct inference-speedup technique that complements Wanda's speedup of matrix multiplication.

Minor:

1. I believe Wanda prunes the weights of a given layer before computing the activations that will be used to prune the next layer, and the manuscript supports this by saying "After pruning a preceding layer, the subsequent layer receives updated input activations, based on which its pruning metric will be computed". I would suggest rephrasing this statement slightly to make it clear that the the "updated input activations" are those created by the pruned weights of the prior layer.

2. Is this really an "element wise dot product" (page 3), and not a Hadamard product?

3. On page 4, $\mathrm{diag}$ is used twice, once on a matrix and once on a scalar. I think the usage on the scalar is conveying that we have a diagonal matrix with each entry being the squared $\ell_2$ norm of the $j$th feature. If that's right, please consider if you can improve this sentence's notation to avoid confusion (e.g., change use of $\mathrm{diag}$ or its argument).

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces a novel one-shot pruning approach for LLM, with its primary contribution being the introduction of a new weight importance score function. This function evaluates each weight by multiplying its magnitude with the norm of the corresponding input activations, which are estimated using a small set of calibration data. Extensive experiments on Llama and LLama2 demonstrate the effectiveness.

### Strengths
1. The work conducts extensive experiments and demonstrates that the pruned models outperform SparseGPT.
2. The method requires no retraining or weight update for LLMs, and the pruning speed is very fast (in seconds)

### Weaknesses
This work proposes a simple yet effective one-shot pruning method for LLMs, which has demonstrated superior performance over sparseGPT. However, I have concerns regarding its incremental contributions due to the following reasons:

1. The paper's introduction of a method to estimate weight importance based on both activation and weights does not appear to be novel. Similar concepts have been explored in previous works on LLM quantization, such as the AWQ work [1]
2. The pruning method proposed in the paper is simple and straightforward, which can be seen as an advantage. However, it operates under some strong assumptions, such as comparing and removing weights on a per-output basis, rather than adopting a more global pruning strategy. This could limit its applicability and effectiveness.
3. Given the limitation mentioned in point 2, although the method can be extended to semi-structured pruning, there are doubts about its ability to be extended to structured pruning. 




[1] https://arxiv.org/abs/2306.00978

### Questions
Please refer to the weaknesses section.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes the implementation of the norm dot product of weights and activations (Wanda) as a pruning metric for LLMs. The primary motive is to preserve outlier weights within the LLM. Experiments were conducted on typical large models, such as Llama-v1 and Llama-v2. The results indicate that the proposed Wanda approach substantially reduces the time consumed by established pruning methods and enhances performance to a certain degree.

### Strengths
1. Although Wanda is quite simple and there are similar pruning metrics in the traditional pruning field, it is indeed buillt upon the consideration of outlier weights in LLM, rendering the narrative of the article easy to comprehend and follow. Thus, I believe that this paper holds significant value for the community. 
2. The proposed Wanda method is highly efficient. Notably, it does not require backpropagation like SparseGPT, enhancing its applicability across various terminals to a considerable extent. Given that the performance of Wanda has essentially reached the optimal level, I deem it to have significant practical value.
3. The experiments are very thoroughness, making it very easy to understand the impact of various factors in LLM pruning, such as the pruning granularity and the effect of fine-tuning, among others. These elements also support my recommendation for the acceptance of this paper.

### Weaknesses
1. The authors primarily focus on experiments at a low sparsity rate of 50%, yet at a high sparsity rate (80%), Wanda's performance noticeably lags behind SparseGPT, which somewhat dampens my enthusiasm for this paper. 
2. While the authors emphasize efficiency, and Wanda indeed greatly surpasses SparseGPT in efficiency (for example, 0.54s for WANDA and 203.1s for SparseGPT when pruning Llama-7b), I would like to question whether this disparity in time consumption truly holds value. My point being, the time expense for SparseGPT also remains quite low. Even though the authors claim the presence of certain real-time scenarios, I believe their notion of training sparse models from scratch is impractical, hence a more thorough discussion is warranted in this aspect.

### Questions
After fine-tuning with LoRA, the weights of LoRA will be incorporated into the pruned weights. As a result, the weights from LoRA will substantially mitigate the model's sparsity. Should the LoRA weights not be merged, however, additional inference time costs would ensue. Despite this not being the primary aspect of the paper, I maintain some reservations regarding this issue.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study introduces Wanda, an unstructured pruning method for large language models (LLMs). Wanda utilizes both weights and activations as proxies to estimate the importance of parameters, selectively zeroing out those with low importance. This approach results in a sparse LLM, which can be accelerated with some special devices capable of 2:4 sparsity acceleration. Wanda not only outperforms traditional magnitude-based pruning methods for efficiency but also offers quicker processing compared to SparseGPT, which depends on second-order information.

### Strengths
- The method proposed is simple and impressively effective, particularly when compared to SparseGPT. Its lower computational complexity is a significant benefit, leading to reduced memory requirements during the pruning process.
- This paper is well-organized and easy to follow. The authors thoughtfully include extensive experimental results from LLMs such as LLaMA, LLaMA-2, OPT, and Bloom, providing a useful resource for future research in this field.

### Weaknesses
- My primary concern lies in the relative contribution of Wanda compared to SparseGPT and several existing methods. There are a lot of criteria in the literature of pruning, such as first-order Taylor expansion ($|w*\delta w|$) [1], and optimal brain damage [2]. It seems that these general methods, with a similar form to Wanda, can be easily adapted to LLM. So, is the proposed $|w| \cdot |x|$ the optimal criterion, especially in the context of LLMs?

- It would be helpful if the authors could detail the overall speed-up of the entire LLM. Table 6 indeed summarizes the speedup for a single layer. However, an LLM usually comprises various components, including QKV, attention, and linear layers. Since Wanda primarily targets the sparsification of linear layers, it may not significantly boost attention computation speeds. Therefore, the actual overall speedup could differ from the single-layer improvements indicated in Table 6.

- The effectiveness of Wanda on models like OPT and Pythia, particularly under high sparsity conditions (e.g., 50%), seems to be limited. In these scenarios, SparseGPT has even demonstrated superior performance.

[1] Molchanov, Pavlo, et al. "Importance estimation for neural network pruning." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2019.  
[2] LeCun, Yann, John Denker, and Sara Solla. "Optimal brain damage." Advances in neural information processing systems 2 (1989).

### Questions
My questions can be found in the weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
