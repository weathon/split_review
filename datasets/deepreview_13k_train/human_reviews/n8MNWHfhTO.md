# GaLore$+$: Boosting Low-Rank Adaptation for LLMs with Cross-Head Projection

- Decision: Reject
- Scores: 6, 3, 3, 6

## Abstract
Recent low-rank training methods, such as GaLore, have significantly reduced the memory required to optimize large language models (LLMs). However, these methods often suffer from time-consuming low-rank projection estimations. In particular, the singular value decomposition (SVD) in GaLore can consume more than 80\% of the total training time. To address this issue, we propose GaLore$+$, which uses cross-head low-rank projection to reduce the substantial time consumption in estimating low-rank projections for multi-head attention. In addition, we employ randomized subspace iteration to achieve fast SVD. To further enhance performance, we propose sparsely coded residuals to reduce the errors caused by low-rank approximation on the first- and second-order moments of the optimizers and weight updates. We evaluate GaLore$+$ on arithmetic reasoning and natural language generation datasets. Our experiments demonstrate that GaLore$+$ delivers superior performance while achieving approximately $4\times$ fine-tuning speed compared to vanilla GaLore.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces GaLore+, an improved version of the GaLore method for memory-efficient fine-tuning of large language models. GaLore+ tackles the time bottleneck in GaLore by utilizing cross-head low-rank projections and randomized subspace iteration for faster singular value decomposition. Additionally, it introduces sparsely coded residuals to minimize errors from low-rank approximation. Experiments on arithmetic reasoning (GSM8k, d MAWPS datasets) and natural language generation (E2E) tasks show that GaLore+ achieves significantly faster fine-tuning (around 4x) while maintaining superior performance compared to the original GaLore.

### Strengths
1) the analysis (Figure 2) nicely identifies the issue and motivates the paper
2) the proposed method is sound and the results seems convincing.

### Weaknesses
1) the evaluation datasets in experiment study are limited. Eval metrics for NLG(E2E) are not suitable for generative task evaluation. 
2) The sensitivity of Hparams (rank, low data regime) is not well studied.

### Questions
1) Given LoRA's established effectiveness in low-data fine-tuning scenarios, how does the proposed method perform under similar low-rank, data-constrained conditions?
2) Do the reported performance gains, measured using LLM-based evaluation metrics on NLG datasets, translate to demonstrable improvements in generated output quality?
3) To further assess the method's capabilities, consider expanding the evaluation to include a wider range of generative tasks and datasets.

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
4

### Summary
GaLore+ is proposed as an enhancement to GaLore, addressing the computational bottleneck of SVD which consumes over 80% of training time in the original method. The improved method combines cross-head low-rank projection and randomized subspace iteration for faster SVD computation, while introducing sparsely coded residuals to minimize approximation errors in optimizer moments. Experimental results show that GaLore+ achieves 4x faster fine-tuning speed compared to vanilla GaLore while maintaining or improving performance on arithmetic reasoning and natural language generation tasks.

### Strengths
This paper presents an upgraded version of GaLore that employs randomized SVD for acceleration and uses Residual of Moments to compensate for potential accuracy loss from the randomized approach.

### Weaknesses
While the core idea is straightforward and easy to understand, the paper's primary weakness lies in insufficient experiment, making it difficult for reviewers to properly evaluate the effectiveness of these enhancements. 

- Counter-intuitive results require explanation. While the method aims to accelerate training through randomized SVD and use the sparsely coded residuals to reduce the approximation errors, it's fundamentally still an SVD computation. Theoretically, the performance upper bound should be the exact SVD computation. Although speed improvements are understandable, the significant performance gains over exact SVD computation (GaLore) are unexpected and need explanation

- The experimental methodology raises several concerns. The authors only examine cases with large rank values, despite evidence showing that LoRA typically performs best with r=8~32 during Supervised Fine-Tuning (SFT). Additionally, the single-epoch training approach may result in underfitting, potentially skewing the results. The effectiveness of the Sparsely Coded Residual method also remains uncertain, as there's insufficient evidence to show whether the improvements come from this specific component or could be achieved simply through the combination of random SVD and GaLore.

- Another  limitation of this work is the insufficient comparison with relevant baselines. Given that the paper's main contribution centers on accelerating PEFT training, it should include comparisons with other efficient methods like DoRA and FFT LoRA that achieve similar goals with reduced parameter counts and faster training speeds.

### Questions
To strengthen the paper, the authors should expand their experimental evaluation to include various rank settings, extended training epochs, comprehensive ablation studies, and detailed comparisons with modern PEFT methods. This would provide a more complete and convincing demonstration of their method's advantages.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents GaLore+, a new parameter-efficient finetuning (PEFT) technique that extends previous work on GaLore to enhance its time-efficiency as well as downstream performance. To reduce the cost of GaLore taken to compute SVD factors on weight gradients, GaLore+ proposes cross-head low-rank projection which uses a single attention head to compute its low-rank projection, and apply the same projection across all heads. Instead of deterministic SVD, GaLore+ also uses randomized SVD via subspace iterations. Lastly, inspired by previous work on low-rank plus sparse approximators, GaLore+ adds a sparsely coded residual to the low-rank factors, approximating the true gradients better than with only low-rank factors. Experiments using the Llama2-7B model on arithmetic reasoning and natural language generation datasets show that GaLore+ significantly reduces the cost of finetuning in both time and memory.

### Strengths
- [S1] **Clear motivation and interesting problem setup.** Parameter-efficient finetuning is a widely used technique for adapting pretrained LLMs, and the techniques introduced in this paper would be a good addition to the LLM finetuning toolkit. The motivation is also crystal clear with preliminary experimental results presented early in the paper: to reduce the time-consumption and enhance performance of GaLore.

### Weaknesses
 - [W1] **Weak novelty and contribution.** The techniques newly incorporated into GaLore+, which include cross-head low-rank projection, randomized SVD, and sparse residuals, are all essentially from existing work, which significantly weakens the overall novelty of this work. The techniques are also discussed and demonstrated solely under the scope of applying gradient projections (i.e. vanilla GaLore) and thus the contributions are too shallow, and does not seem sufficient to constitute a conference paper at ICLR.
- [W2] **Lacking experimentation.** Even though the paper is mostly empirical, the experimental setup is narrow, covering two arithmetic reasoning datasets and one natural language generation dataset. Considering that GaLore+ can be used essentially anywhere when finetuning pretrained Transformers, it would be great to add (1) more datasets and pretrained models as well as (2) more PEFT baselines (other than LoRA and GaLore) to fully argue that the gain in time-efficiency as well as downstream performance leads to competitive results.
- [W3] **Weak intuition behind cross-head low-rank projection.** The discussion on the cross-head similarity for simplified SVD (Section 4.1.1) is a bit hard to follow. Specifically, how can it be the case that "the gradient of different heads within the same layer are similar" (Lines 236-237), but treating all attention heads as a whole "fails to capture the structure of each individual attention head accurately" (Lines 250-251)?  Shouldn't the hypothesis essentially allow us to treat all attention heads as a whole?

### Questions
- [Q1] For Figure 2b, is GaLore+ (in blue) using each $i$-th head to approximate the gradient of the $i$-th head? How can it be that GaLore+ is achieving lower RMSE on all heads, when the rank-$r$ SVD used by vanilla GaLore is known to provide an optimal rank-$r$ approximation in Frobenius norm?
- [Q2] How many random seeds were used for main results in Tables 1 and 2? What were the standard deviations on different performance metrics?
- [Q3] When using randomized subspace iteration to perform fast SVD, how many subspace iterations does GaLore+ use? 
- [Q4] Based on Figure 3, it seems the sparsely coded residual does not have a significant impact on downstream performance. Could we compare LoRA and GaLore vs. GaLore+ without sparsely coded residuals to better assess the performance gains?
- Typo in Line 401: Teble 1 $\rightarrow$ Table 1

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces an improved version of GaLore, significantly reducing training time and memory usage. The authors first proposed the cross-head low-rank projection, which obtained the low-ranking gradient projection via the SVD of a randomly selected head rather than that of all heads. They further proposed a mechanism to rectify the first, second moments and the weight updates to reduce the error induced by the low-rank approximation.

### Strengths
- GaLore+ showcases its superiority in the arithmetic reasoning task.
- The authors successfully propose a training-accelerating version of Galore, which will reduce both the training resources and improve performance.

### Weaknesses
 - The empirical results on the natural language generation tasks show insignificant improvements of GaLore+ over LoRa. 
- In Line 50, the authors mentioned that the errors in Equation 6 are lower than those in Equation 4, as depicted in Figure 2b. This is because Equation 6 treats all attention heads collectively, thereby not accurately capturing the structure of each individual attention head. Does a lower error indicate a better scenario? Is the error calculated for each head individually or across all heads?
- How does GaLore+ determine the head used for computing low-ranking gradient projection? Based on my understanding, it is selected randomly. Is there any theoretical or empirical rationale behind this choice? If not, at the very least, conducting an ablation study on various head selection strategies is essential.

**Minor errors**: 

- Tebble in Line 401.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3
