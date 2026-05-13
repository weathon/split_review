# You Only Prune Once: Designing Calibration-Free Model Compression With Policy Learning

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
The ever-increasing size of large language models (LLMs) presents significant challenges for deployment due to their heavy computational and memory requirements. Current model pruning techniques attempt to alleviate these issues by relying heavily on external calibration datasets to determine which parameters to prune or compress, thus limiting their flexibility and scalability across different compression ratios. Moreover, these methods often cause severe performance degradation, particularly in downstream tasks, when subjected to higher compression rates. In this paper, we propose *PruneNet*, a novel model compression method that addresses these limitations by reformulating model pruning as a policy learning process. PruneNet decouples the pruning process from the model architecture, eliminating the need for calibration datasets. It learns a stochastic pruning policy to assess parameter importance solely based on intrinsic model properties while preserving the spectral structure to minimize information loss. PruneNet can compress the LLaMA-2-7B model in just 15 minutes, achieving over 80\% retention of its zero-shot performance with a 30\% compression ratio, outperforming existing methods that retain only 75\% performance. Furthermore, on complex multitask language understanding tasks, PruneNet demonstrates its robustness by preserving up to 80\% performance of the original model, proving itself a superior alternative to conventional structured compression techniques.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces PruneNet, a policy-based pruning method designed to learn the removal of redundant parameters without the need for calibration data. PruneNet’s policy is trained based on intrinsic model properties to minimize information loss, quantified using the KS distance between the singular value distributions of the uncompressed and compressed matrices. To make policy learning differentiable, the paper employs the reparameterization trick, introducing a random variable into the sampling process and training the policy module by evaluating various pruning outcomes. The proposed method is primarily evaluated on Llama-2 7B and Phi-2, with comparisons to SliceGPT, a technique that directly compresses parameter matrices by training on datasets. Results indicate that PruneNet achieves superior performance on several popular benchmarks.

### Strengths
* One of the key strengths of this paper is a data-independent importance scorer, derived through a policy-learning process. The policy focuses mainly on individual linear layers, making the method theoretically efficient. This efficiency is demonstrated by its successful application to Llama-7B, where pruning requires only 15 minutes, illustrating its practicality for large-scale models.
* The authors conducted extensive experiments, exploring factors such as compression ratio, RFT dataset, and computational costs. 
* The policy learner can be applied across different compression ratios, which offers practical value for determining optimal pruning ratios in large language models (LLMs). This flexibility could be particularly advantageous for users looking to fine-tune pruning ratios without retraining the policy for each setting.

### Weaknesses
 * The pruning approach is focused on single layers, potentially overlooking structured interdependencies with subsequent layers. In structured pruning, parameters in one layer impact those in the next; by not accounting for this, the proposed method risks removing essential parameters from interconnected layers. This oversight could inadvertently affect model performance, as it might miss opportunities for more coordinated pruning across layers.
* Although the method is designed to optimize the KS distance before and after pruning, it lacks a detailed analysis of its policy-learning approach. A simple random sampling approach might also work: sampling multiple randomly pruned matrices and selecting the one with the lowest KS distance might be able to provide good results. Including more ablation studies to compare these methods would enrich the analysis. Additionally, further discussion on the design and benefits of the policy approach would add valuable insights.
* While the method shows promise on Llama-7B, its efficacy on larger models, such as Llama 13B, remains untested. An evaluation on larger LLMs would help establish its robustness and scalability, further highlighting its applicability to a broader range of large models.

### Questions
Please see weaknesses

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
3

### Summary
This paper proposes a FFN-layer pruning algorithm for large language models that does not require a calibration dataset. The idea is to prune the weight matrices so that the spectrum of the matrices before and after pruning remains similar in the Kolmogorov-Smirnoff distance. To hasten the pruning procedure, one trains a policy that predicts the importance scores of the first layer of FFN. The empirical results show that the proposed method outperforms SliceGPT, in terms of prediction quality and the actual speedup.

### Strengths
- The central research question of training a policy to prune LLMs is quite intriguing, with some practical importance. Although the paper mainly claims the benefit on the data side, I personally find that the method might have more future uses on low-memory or compute scenarios where it is very difficult to run usual pruning algorithms that require much gradient-based computations.

- The empirical performance seems to be reasonably good.

- The paper asks many interesting questions in section 5.2, including the transferability and the layerwise compression ratio.

### Weaknesses
 - One nitpick is that the comparison against SliceGPT, reported on Table 2, can be quite misleading. The figures seems to be the one for SliceGPT with WikiText2 calibration data, which is much worse than the SliceGPT with Alpaca calibration data. In fact, with Alpaca, I believe that the SliceGPT works much better than the proposed PruneNet. Of course, this is somewhat expected because it utilizes more data than PruneNet; making a comparison with both WikiText and Alpaca case does not diminish the usefulness of the proposed method, as they assume different amount of usable resources. Thus I recommend including both SliceGPTs, for a more comprehensive comparison.

- Another weakness is that the proposed method may not work better than the methods that use calibration data, as assuming no access to the calibration data also makes it impossible to use RFT. It seems like Table 3, ironically, can also be interpreted as a limitation of the proposed method, in a sense that the model pruned with PruneNet cannot recover much with RFT, while LLMs pruned with other methods can recover much with fine-tuning.

- Also, the motivation is quite unclear to me. At least for the text data, I am not sure why it is practical to assume no access to the calibration data. We already have quite abundant text data (crawled from web), even as our benchmark. Why should we suddenly assume that those data are not available? Can you give any further justifications?

- The idea of spectrum matching is also not justified well. First, I do not see how corollary 3.3 can be used to predict that the singular values of the matrix become more right-skewed. Doesn't the corollary simply states that the spectrum will be about subsampling, rather than predicting anything about the skewness? Also, the fact that there can be some spectrum shift does not fully mean that it will be an effective criterion for deciding how to prune. Perhaps more comparison with other criterion (e.g., minimizing Frobenius norm distortion) may help us understand whether the spectrum matching part is indeed an essential and nontrivial component.

### Questions
Discussed in 'weaknesses'

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
This paper introduces PruneNet, a structured pruning technique that deploys a policy learning process to identify important parameters. The proposed method is calibration-free, and once completed, can be applied to different pruning ratios without repeated assmentments of weights and data. The proposed method can be applied to popular Llama-2-7B in just 15 minutes, which is efficient enough for LLM pruning. The author conducted experiments on Llama-2 7B and Phi-2, with the compression ratio from 20% to 30%. Compared to SliceGPT, the method archives better accuracy on 5 zero-shot tasks, keeping >80% performance of the original LLMs. Besides, even without fine-tuning, the method is still able to preserve a good average accuracy.

### Strengths
The idea of calibration-free pruning is interesting.  The policy learned on one compression ratio is scalable and can be directly transferred to higher or lower ratios. This is a useful feature if one would like to evaluate the performance of pruned models for a good trade-off between performance and efficiency. In addition, Extensive experiments were conducted to evaluate the effectiveness of the policy learning, with different finetuning settings and compression ratios, The proposed method is able to achieve better average accuracy (+3%~+4%) on zero-shot tasks.

### Weaknesses
1. It appears that most of the experiments in this paper were conducted without fine-tuning. It would be insightful to examine how the proposed method compares to other baselines when fine-tuning is enabled, as this could provide a more complete picture of its performance under optimal conditions.
2. The efficiency of policy learning has not been studied. Providing more analysis on the efficiency of policy learning would enhance the understanding of its practical impact.
3. Based on point 3, if we allocate the same computational budget across all baselines, such as assigning the training cost of policy learning to LoRA fine-tuning in other baselines, does the proposed method still achieve superior performance?
4. Including pseudocode for the entire pipeline would improve clarity and reproducibility.
5. On of my main concerns is the lack of clarity behind the motivation for each design choice. For example, Equation 3 is introduced without sufficient context or explanation. The KS Distance introduced in Equation 6 also reveals weak insights about its motivation. Why KS distance instead of other distribution distance? In addition, other paragraphs could also benefit from refinement. In particular, the background section, especially sections 3.2 and 3.2, is densely packed with technical details and formulas about SliceGPT and eigenvalues. However, the relevance to the proposed method remains unclear until the final paragraph, creating a disconnect that might hinder reader understanding.

### Questions
May I ask about the motivation behind Equation 3 (the importance score)? It appears that the equation is designed to project the parameter $W$ into a score $d$-dim vector. Could you clarify why this approach was chosen over other designs, such as directly optimizing a d-dimensional vector as the importance score? Additionally, will the learned matrix be shared across all linear weight layers?

### Soundness
3

### Presentation
1

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
This paper describes a technique -- PruneNet that avoids the usage of calibration data for structured pruning. They instead reformulate it as a policy learning process via (prun)ing-object(e)d (net)work. They does this by first making a corollary that the range of eigenvalues of the compressed model weights is a subset of the original model weights (corollary 3.3). Following that, the key idea is to identify (using an MLP/policy learner) and remove rows/columns in such a way that the distribution (and distance using Kolmogorov Smirnoff (KS) Distance) of the eigenvalues for original and compressed weights remain the same. 

The method seems to achieve robust results across various models/datasets and compression ratios without a calibration dataset.

### Strengths
1. The removal of dependence on calibration dataset while pruning. As noted by authors in L115, calibration dataset has an impact on performance of models, so it has important effects for applications. 
2. The intrinsic model compression is an interesting observation. This helps practitioners understand the dependency of compression methods (whether method X is adding parameters or not) with respect to the compression ratios
3. The reusability of policy learner i.e train a learner (MLP) for one compression ratio and use it for another ratio as the authors have noted down is a huge strength (L412)
4. Very well written with clear presentation.

I believe the paper would be a great addition with some clarifications needed in design space and experiments.

### Weaknesses
I don't have a list of "weakness" i.e substantial missing components. Please refer the questions section for potential ideas and clarifications needed.







### Questions
***Model design***

1. The sampling is done on FFN1 and complementary columns are chosen in FFN2 to match the dimensions. This makes sense logically/intuitively but did the authors experiment with sampling FFN2 separately and/or any other design choices. Does the indices match the intuitive selection. Or does the authors have an explanation on why this choice is better compared to other intuitive selections? 
2. Did the authors perform experiments on usage of other penalty functions (KS)? That can be a good ablation study to have. 
3. L292: The assumption of discounted penalty works if the LLM has higher singular values at later layers. Has there been any (previous) analysis on existing LLMs whether that’s the scenario? A reference would be great if it exists. If not, having plots similar to Figure 1 for other LLMs at appendix would be great. 

***Experiments***

4. L361: Are the results for the one-sided test and additional details available? A reference would be great.
5. L375 (RFT): Can the authors add more insights on why RFT on model X might reduce the performance?
6. L375 (RFT): Can the RFT be done on SliceGPT as well (i.e Table 3 looking similar to Table 2). That will help to understand whether RFT helps SliceGPT more (>1.5%) and PruneNet less (marginal 1.5%) or less for both methods (in either case, it will be a useful finding to understand the effects of RFT)

***Suggestion for additional experiment on design choice***

1. Can this policy be extended to attention matrices as well? From my understanding, the key idea seems to be applicable on any matrix, so this experiment will be super helpful to understand the design space more clearly? There has been some studies [1] done to understand the effects of compression on different modules in a transformer, so the authors might take some inspiration to understand the effects on compressing on different modules.
2. Can the authors perform an experiment with >40% compression ratio? The performance drops most likely with higher compression ratios [1, 2, 3] but it would be great to know how much the PruneNet can achieve for reasonable compression. 

***Possible relevant citation***
1. The Cost of Compression: Investigating the Impact of Compression on Parametric Knowledge in Language Models - https://arxiv.org/abs/2312.00960
2. Are sixteen heads really better than one? - https://arxiv.org/abs/1905.10650
3. Compressing bert: Studying the effects of weight pruning on transfer learning - https://arxiv.org/abs/2002.08307

***Format***

1. Line 37 - Can be more descriptive about the model sizes rather than a simple statement (eg: Llama 2 can be of different sizes)
2. Can the authors give clear explanations on different between Effective Sparsity and Sparsity (maybe in Appendix if possible)

### Soundness
4

### Presentation
4

### Contribution
3
