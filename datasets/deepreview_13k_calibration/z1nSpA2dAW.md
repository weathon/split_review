# FLOPS: Forward Learning with OPtimal Sampling

- Decision: Accept
- Avg Score: 5.75
- Scores: 3, 6, 6, 8

## Abstract
Given the limitations of backpropagation, perturbation-based gradient computation methods have recently gained focus for learning with only forward passes, also referred to as queries. Conventional forward learning consumes enormous queries on each data point for accurate gradient estimation through Monte Carlo sampling, which hinders the scalability of those algorithms. However, not all data points deserve equal queries for gradient estimation. In this paper, we study the problem of improving the forward learning efficiency from a novel perspective: how to reduce the gradient estimation variance with minimum cost? For this, we propose to allocate the optimal number of queries over each data in one batch during training to achieve a good balance between estimation accuracy and computational efficiency. Specifically, with a simplified proxy objective and a reparameterization technique, we derive a novel plug-and-play query allocator with minimal parameters. Theoretical results are carried out to verify its optimality. We conduct extensive experiments for fine-tuning Vision Transformers on various datasets and further deploy the allocator to two black-box applications: prompt tuning and multimodal alignment for foundation models. All findings demonstrate that our proposed allocator significantly enhances the scalability of forward-learning algorithms, paving the way for real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper examines perturbation-based gradient computation methods tailored for forward-only learning. The authors introduce an optimal sampling strategy based on a Gaussian Allocator designed to maximize performance improvements incrementally. They evaluate this approach using pretrained transformers and demonstrate that it outperforms selected baseline methods.

### Strengths
1. The empirical accuracy results for ViT and CLIP appear to surpass those of the baselines. The authors have also conducted essential ablation studies to further validate their findings.

2. While the text in Figures 2 and 3 is smaller than the standard text size, making it challenging to read, the color combinations used in these figures are visually appealing.

### Weaknesses
1. **Overall outline and structure**: The paper builds upon DeepZero and Mezo by devising an optimization allocation for forward learning. However, the idea of optimal allocation is not new in the ML context. Papers such as "Stochastic Optimization with Importance Sampling" or "A General Analysis of Example-Selection for Stochastic Gradient Descent" (and several derived works) have explored similar concepts. For me, the main difference here is the focus on forward learning (or zeroth-order optimization) rather than backpropagation. The authors are encouraged to: (1) Review and mention this existing research (strongly encouraged) and (2) Compare these methods with their proposed algorithm (encouraged). Addressing these points would strengthen the paper's contribution and contextualize it within the field.

2. **Introduction and framing**: 
The decision to begin with biologically plausible algorithms (BioPA) seems unexpected and may not effectively frame the paper's contributions. Nevertheless, the general scheme could be unfolded more clearly:
     1. The citation of Jacot et al. for "learning high-level representation" appears unrelated in the BioPA context.
     2. Consider including more relevant BioPA works such as "Direct Random Target Projection" [1], "SoftHebb" [2], and "Counter-Current Learning" [3]

3. **Writing and proofreading**: 
   - Correct typographical errors (e.g., "Current Literature" should be "Current literature")
   - Address factual inaccuracies (e.g., L48 states that the FF algorithm is only capable of training MLPs on MNIST, but results for CIFAR are also presented)
   - Provide explanations for abbreviations (e.g., SPSA, LR)

4. **Related Work section**: The first subsection could be restructured. When discussing backpropagation-free learning, it's typically in the context of multi-layered neural networks. Also, including evolution theory and particle swarm optimization seem tangential. I suggest reorganizing this section and incorporating the suggested papers for a more focused discussion.

### Questions
For enhanced clarity, please focus on the weaknesses section, which includes my raised questions.

Concerning reproducibility, I reviewed the supplementary material, presumably the code. However, the absence of a README file and the presence of numerous extraneous files make it challenging to determine which files are essential. Additionally, the provided code lacks meaningful comments and contains a lot of debug information, which further complicates understanding its logic. If the authors aim to demonstrate reproducibility through the attached code, I recommend including a clean version of the code with detailed instructions in a README file to at least guide reviewers through the main logic.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces FLOPS: Forward Learning with Optimal Sampling, which aims to improve the efficiency of gradient estimation in forward-only learning methods by optimally allocating computational resources (queries) across data points within each mini-batch. The approach is motivated by the limitations of backpropagation, particularly in settings where only forward passes are feasible or desirable, such as in black-box optimization scenarios.  With a simplified proxy objective and a reparameterization technique, the authors derive a novel plug-and-play query allocator with minimal parameters. Extensive experiments show the superior performance of this method. Theoretical analysis is also provided.

### Strengths
1. The idea of dynamically allocating different numbers of queries to each data point within a batch during training is novel, which is indeed a point that previous zeorth-order optimization (forward learning) methods have not considered.

2. The proposed method is intuitive. The approach of leveraging a Gaussian Allocator (GA) combined with a likelihood ratio method introduces a creative solution to minimize gradient estimation variance. Through appropriate approximations, the computational cost is effectively reduced. Theoretical analysis is also provided.

3. The experimental setup is extensive and reasonable, and the results are convincing. Both prompt tuning for large models and multimodal alignment for foundation models are promising application scenarios for zeroth-order (ZO) methods, and the proposed approach demonstrates good performance on these tasks.

### Weaknesses
1. Although the authors provide part of the source code, I believe the coding is not advisable. Specifically, the authors override nn.Linear to create a custom Linear class and similarly override nn.Conv2d to create a custom Conv2d class. This approach results in the proposed method being tied to a specific model architecture, making it difficult to adapt to other architectures. In fact, existing zeroth-order optimization methods, such as ZO-SGD [1], ZO-AdaMM [2], and DeepZero [3], all have core optimization logic that can be implemented by inheriting from torch.optim.Optimizer, thereby aligning with gradient-based methods like SGD. Alternatively, they can be integrated into a specific function for easier migration.

2. One important reason why zeroth-order optimization is suitable for large model prompt fine-tuning is that these methods do not require backpropagation, which significantly saves memory compared to gradient-based methods like SGD. However, in the experimental results presented in the main paper, only the fine-tuning results are provided, without comparing their memory usage with backpropagation and other zeroth-order optimization methods.

[1] Saeed Ghadimi and Guanghui Lan. Stochastic first-and zeroth-order methods for nonconvex stochastic programming. SIAM Journal on Optimization, 23(4):2341–2368, 2013.

[2] Xiangyi Chen, Sijia Liu, Kaidi Xu, Xingguo Li, Xue Lin, Mingyi Hong, and David Cox. ZO-AdaMM: Zeroth-order adaptive momentum method for black-box optimization. NeurIPS, 32, 2019.

[3] Chen A, Zhang Y, Jia J, et al. Deepzero: Scaling up zeroth-order optimization for deep model training[J]. arXiv preprint arXiv:2310.02025, 2023.

### Questions
1. Please refer to Weakness 1. Is it possible to integrate the proposed method into a callable class or function without rewriting model architectures like Linear and Conv2d to implement the specific add_noise operation?

2. Please refer to Weakness 2. Could you provide detailed memory usage for different methods during training for a more thorough comparison? I noticed that the code uses a repeat operation to expand the batch for varying numbers of queries on different data. Does this operation increase memory usage?

3. The authors mention in the main text that 'All the methods in the experiments use the same query budgets, except for Mezo, which uses only 2 queries per data point in accordance with its original memory-efficient setting.' However, could you provide a more detailed comparison of runtime (e.g., clock time) compared to other ZO methods and the BP baseline?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This paper proposes an efficient query allocation strategy for forward-learning algorithms in gradient computation, reducing query usage by focusing on data points that need it most. Using a simplified objective and reparameterization, the authors introduce a lightweight query allocator that minimizes gradient estimation variance with low computational cost. Both experiments and theoretical analysis are provided.

### Strengths
1) The motivation is clear: optimizing the allocation of queries to effectively reduce computational overhead.
2) The experimental results show strong performance relative to the baselines.
3) The study provides both experimental and theoretical results, offering a well-rounded evaluation.

### Weaknesses
1) I am curious about why other methods that utilize all queries would perform worse than this method, that utilizes limited quries for each data. 
2) The comparison of exact computational cost between equally using all queries for each data point and your allocation method is unknown. However, it is one of the main motivation.  

Minor:   
3) In the abstract, the phrase “propose to allocate the optimal number of queries over each data” isn’t entirely accurate, as a total query budget must be pre-defined rather than learning an optimal number. Perhaps rephrasing to “allocate the optimal number of queries within a set budget” would be clearer.   
4) Table 2 is not well-formatted and appears misaligned.

### Questions
1) I am curious about why other methods that utilize all queries would perform worse than this method, that utilizes limited quries for each data.  Since MEZO is tailored to another baseline, using the same hyperparameters might not be entirely fair. Have you considered tuning MEZO with more available queries per data point for comparison?
2) What is the exact computational cost when using all queries for each data point compared to your allocation method under different budget constraints?

If reasonable answers are provided, I will consider rasing scores accordingly.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents an approach for optimizing a differentiable sampler in forward learning in foundation models, supported by theoretical proofs and extensive empirical evaluations. The work lies at the intersection of zeroth-order optimization and sampling optimization.

### Strengths
1. The empirical evaluation is comprehensive, demonstrating significant performance improvements through query sampler optimization.

### Weaknesses
1. **Overall outline and structure**: The paper builds upon DeepZero and Mezo by devising an optimization allocation for forward learning. However, the idea of optimal allocation is not new in the ML context. Papers such as "Stochastic Optimization with Importance Sampling" or "A General Analysis of Example-Selection for Stochastic Gradient Descent" (and several derived works) have explored similar concepts. For me, the main difference here is the focus on forward learning (or zeroth-order optimization) rather than backpropagation. The authors are encouraged to: (1) Review and mention this existing research (strongly encouraged) and (2) Compare these methods with their proposed algorithm (encouraged). Addressing these points would strengthen the paper's contribution and contextualize it within the field.

2. **Introduction and framing**:
The decision to begin with biologically plausible algorithms (BioPA) seems unexpected and may not effectively frame the paper's contributions. Nevertheless, the general scheme could be unfolded more clearly:
     1. The citation of Jacot et al. for "learning high-level representation" appears unrelated in the BioPA context.
     2. Consider including more relevant BioPA works such as "Direct Random Target Projection" [1], "SoftHebb" [2], and "Counter-Current Learning" [3]

3. **Writing and proofreading**:
   - Correct typographical errors (e.g., "Current Literature" should be "Current literature")
   - Address factual inaccuracies (e.g., L48 states that the FF algorithm is only capable of training MLPs on MNIST, but results for CIFAR are also presented)
   - Provide explanations for abbreviations (e.g., SPSA, LR)

4. **Related Work section**: The first subsection could be restructured. When discussing backpropagation-free learning, it's typically in the context of multi-layered neural networks. Also, including evolution theory and particle swarm optimization seem tangential. I suggest reorganizing this section and incorporating the suggested papers for a more focused discussion.

References

[1] "Learning Without Feedback: Fixed Random Learning Signals Allow for Feedforward Training of Deep Neural Networks" (Frontiers in Neuroscience, 2021)

[2] "Hebbian Deep Learning Without Feedback" (ICLR 2023)

[3] "Counter-Current Learning: A Biologically Plausible Dual Network Approach for Deep Learning" (NeurIPS 2024)

### Questions
1. **Clarification on LR and OPS-LR**: The distinction between LR and OPS-LR is not clear. More explanation would be appreciated.

2. **Clarification on experiments**: Do the experiments include cross-validation with multiple random seeds? If not, please show the experiment results with multiple seeds with dataset cross-validation. If yes, please provide more details.

3. **Ablation studies**: The proposed algorithms update four parameters. What if only three or two of them are updated? Which parameters are dispensable for this process? Conducting these experiments would provide more insights into the paper's contributions.

### Soundness
2

### Presentation
1

### Contribution
3
