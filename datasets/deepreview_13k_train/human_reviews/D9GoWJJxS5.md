# Bypass Back-propagation: Optimization-based Structural Pruning for Large Language Models via Policy Gradient

- Decision: Reject
- Scores: 5, 6, 5, 6, 3

## Abstract
In contrast to moderate-size neural network pruning, structural weight pruning on the Large-Language Models (LLMs) imposes a novel challenge on the efficiency of the pruning algorithms, due to the heavy computation/memory demands of the LLMs. Recent efficient LLM pruning methods typically operate at the post-training phase without the expensive weight finetuning, however, their pruning criteria often rely on heuristically hand-crafted metrics, potentially leading to suboptimal performance. We instead propose a novel optimization-based structural pruning that learns the pruning masks in a probabilistic space directly by optimizing the loss of the pruned model. To preserve the efficiency, our method eliminates the back-propagation through the LLM per se during the optimization, requiring only the forward pass of the LLM. We achieve this by learning an underlying Bernoulli distribution to sample binary pruning masks, where we decouple the Bernoulli parameters from the LLM loss, thus facilitating an efficient optimization via a policy gradient estimator without back-propagation. As a result, our method is able to 1) operate at structural granularities of channels, heads, and layers, 2) support global and heterogeneous pruning (i.e., our method automatically determines different redundancy for different layers), and 3) optionally initialize with a metric-based method (for our Bernoulli distributions). Extensive experiments on LLaMA, LLaMA-2, LLaMA-3, Vicuna, and Mistral using the C4 and WikiText2 datasets demonstrate that our method operates for 2.7 hours with around 35GB memory for the 13B models on a single A100 GPU, and our pruned models outperform the state-of-the-arts w.r.t. both perplexity and the majority of various zero-shot tasks. Codes will be released.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this work, the authors leverage policy gradient estimation to optimize pruning masks without relying on backpropagation. They validate the efficacy of their approach on various pre-trained models and compare it with several heuristic-based baselines.

### Strengths
- The performance gain is significant.
- The idea of leveraging policy gradient for pruning is novel and insightful.

### Weaknesses
1.  **Lack of Comparison with Recent Baselines**:  
   The paper does not compare the proposed method with recent pruning techniques such as Shortened LLaMA ([arXiv:2402.02834](https://arxiv.org/abs/2402.02834)) and SLEB ([arXiv:2402.09025](https://arxiv.org/abs/2402.09025)), which were published prior to ShortGPT ([arXiv:2403.03853](https://arxiv.org/abs/2403.03853)) and Gromov et al.'s work ([arXiv:2403.17887](https://arxiv.org/abs/2403.17887)). Additionally, MKA ([arXiv:2406.16330](https://arxiv.org/abs/2406.16330)) is also not included. Including comparisons with these methods on benchmarks like MMLU and GSM8K, using metrics like accuracy and perplexity, would provide a more comprehensive evaluation of the method's performance relative to the latest advancements in the field.

### Questions
N/A

### Soundness
4

### Presentation
2

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
This paper proposes an optimization-based structural pruning method for Large Language Models (LLMs) which notably does not require any gradient back-propogation. The method works by casting the binary pruning mask over structural components as a bernoulli variable. This reparametrization allows us to solve the pruning problem via policy gradient. The authors conduct thorough experimental evaluation on open-sourced LLMs and demonstrate the effectiveness of the proposed pruning method.

### Strengths
- This paper proposes a novel method, which casts the optimization problem of selecting optimal pruning mask as a reinforcement learning problem. This allows us to avoid the inefficiency for performing computationally intensive back-propogation.  
- The authors have conducted extensive experimental evaluation and compare with many existing baseline methods for structural pruning. The results show that the proposed method is a promising approach for structural pruning.

### Weaknesses
- It might be good to evaluate a larger LLM model, e.g., LLaMA-3-70B.  
- The authors stress the memory efficiency of optimizating without back-propogation. It would be good to dedicate one section comparing the resource consumptions of different pruning approaches, especially to those with gradient computation.

### Questions
- Could the proposed approach be used for width pruning [1]?  
- In principle, could we solve problem 4 via back-propogation? For this setting, is it expected that the solver with gradient information be better?  
- Could iterative pruning be beneficial for this approach? By iterative pruning, I mean doing the pruning procedure multiple times until the target prune ratio is reached. 

[1] LLM Pruning and Distillation in Practice: The Minitron Approach. NVIDIA 2024.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces an optimization-based structural pruning method for LLMs that eliminates the need for back-propagation. By employing Bernoulli distributions to learn pruning masks, the authors optimize these masks using a policy gradient estimator, enabling gradient estimation solely through the forward pass. This approach enhances efficiency in memory and computation compared with methods requiring back-propagation, and it achieves performance superior to heuristic-based pruning metric methods.

### Strengths
1. The paper presents a novel pruning method that leverages policy gradient estimators instead of back-propagation, addressing key computational challenges in gradient-based LLM pruning methods.
2. The method supports multiple structural granularities (channels, heads, layers), providing flexibility in how the model is pruned. It also allows for global and heterogeneous pruning, which is more aligned with the varying redundancy across layers in LLMs.

### Weaknesses
1. While the paper suggests using a policy gradient estimator to bypass back-propagation, policy gradient methods can suffer from high variance, which may lead to unstable training. The paper does propose a variance-reduction technique, but the effectiveness of this could be further elaborated or validated with more ablation studies. For example, how is the performance of the proposed methods compared with the results of using back-propagation? 
2. Following up on Weakness 1, could you clarify the exact speedup over direct back-propagation? A runtime comparison on a specific model and hardware or a theoretical analysis of computational complexity would be helpful.
3. The proposed method requires 120K samples with a sequence length of 128, whereas baseline methods like LLM-Pruner, SliceGPT, and Wanda-SP use significantly smaller calibration data, such as 128 samples with a sequence length of 2048. Are the results for the baseline methods obtained with the same calibration data as yours? If not, this may lead to unfair comparisons. Please clarify if all methods used the same calibration data in the reported results. If not, provide results with all methods using the same calibration data, or explain why this is not feasible
4. The sparsity ratios used in the experiments exceed 30%, which may be excessive for structured pruning, as the high PPL results may not be meaningful in practice and could significantly degrade real inference performance, such as in question answering tasks. Therefore, it is important to report performance under lower sparsity levels, such as 10% and 20%.
5. The experiments primarily compare the proposed method with other non-weight-updating pruning techniques. While this makes sense in terms of efficiency, it would be interesting to see how the method stacks up against pruning methods that do involve weight updates, such as [1], especially in terms of final model performance.

[1] Xuan Shen, Pu Zhao, Yifan Gong, Zhenglun Kong, Zheng Zhan, Yushu Wu, Ming Lin, Chao Wu, Xue Lin, and Yanzhi Wang. Search for efficient large language models. arXiv preprint arXiv:2409.17372, 2024.

### Questions
In addition to the questions regarding weaknesses, I recommend including the results of dense models in your tables to highlight the performance degradation resulting from pruning.

### Soundness
2

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
3

### Summary
This paper presents a novel approach to structural pruning of LLMs that bridges the gap between optimization-based and metric-based pruning methods. The key innovation lies in the use of Bernoulli distributions to sample binary pruning masks, coupled with a policy gradient estimator that eliminates the need for back-propagation through the LLM. This is a clever solution that maintains the benefits of optimization-based approaches while achieving the efficiency typically associated with metric-based methods.

### Strengths
- The proposed method is both theoretically sound and practically implementable, requiring only forward passes through the LLM during optimization.
(1) The efficiency claims are impressive (2.7 hours, 35GB memory for 13B models on a single A100)
(2) The approach is flexible, supporting multiple structural granularities (channels, heads, and layers)
(3) The method automatically handles heterogeneous pruning across layers, addressing a key limitation of existing approaches
(4) Extensive experimental validation across multiple LLM architectures and datasets

### Weaknesses
The paper could benefit from more detailed ablation studies on the impact of different structural granularities.

The main weaknesses of this LLM pruning work include: 
(1) limited evaluation beyond perplexity and basic zero-shot tasks, particularly lacking analysis of inference speed improvements and downstream task performance, 
(2) methodological constraints of using basic REINFORCE rather than more advanced policy gradient methods, 
(3) heavy reliance on the C4 dataset with some cross-dataset performance issues on specific zero-shot tasks like WinoGrande and Hellaswag. 
(4) While the method is more efficient than traditional back-propagation approaches, it still requires longer training time compared to metric-based methods (2.7 hours for LLaMA-2-13B) and significant memory usage (35GB).

### Questions
- While the method avoids back-propagation through the LLM, how does the efficiency-accuracy trade-off compare when scaling to much larger models beyond 13B parameters? This is crucial for understanding the method's practical applicability.

- Is there any patterns among the structures pruned through using this method ?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a novel optimization-based structural pruning method for Large Language Models (LLMs) that avoids expensive back-propagation through the LLM. The key idea is to formulate pruning as learning binary masks sampled from underlying Bernoulli distributions. By decoupling the Bernoulli parameters from the LLM loss, the method enables efficient optimization using policy gradient estimation that only requires forward passes. The approach supports different structural granularities (channels, heads, layers) and enables global/heterogeneous pruning across the model. Extensive experiments on various LLMs demonstrate strong performance while maintaining efficiency.

### Strengths
- Clear writing and good organization of the paper
- The paper presents a novel methods for structural pruning that leverages policy gradient estimation, bypassing the need for back-propagation through large models.
- The method supports multiple pruning granularities (channels, heads, layers) and can be initialized using metric-based methods, showcasing its adaptability and potential for widespread application.

### Weaknesses
1. **Lack of Comparison with Recent Baselines**:  
   The paper does not compare the proposed method with recent pruning techniques such as Shortened LLaMA ([arXiv:2402.02834](https://arxiv.org/abs/2402.02834)) and SLEB ([arXiv:2402.09025](https://arxiv.org/abs/2402.09025)), which were published prior to ShortGPT ([arXiv:2403.03853](https://arxiv.org/abs/2403.03853)) and Gromov et al.'s work ([arXiv:2403.17887](https://arxiv.org/abs/2403.17887)). Additionally, MKA ([arXiv:2406.16330](https://arxiv.org/abs/2406.16330)) is also not included. Including comparisons with these methods on benchmarks like MMLU and GSM8K, using metrics like accuracy and perplexity, would provide a more comprehensive evaluation of the method's performance relative to the latest advancements in the field.

### Questions
1. Does the paper include accuracy (ACC) results on more advanced benchmarks like MMLU or GSM8K? If not, could the authors provide such evaluations to demonstrate the method's effectiveness on tasks that require higher reasoning capabilities?

2. The proposed method exhibits longer training times compared to metric-based pruning methods. Are there potential optimizations or strategies that the authors are considering to reduce the training duration without compromising performance?

### Soundness
2

### Presentation
2

### Contribution
2
