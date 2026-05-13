# MERIT: Maximum-normalized Element-wise Ratio for Language Model Large-batch Training

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Large-batch training has become a cornerstone in accelerating the training of deep neural networks, yet it poses challenges in optimization and generalization. Existing optimizers like AdamW present performance degradation during language models' large-batch training, due to the information bottleneck of attention layers caused by the sharp increase of max attention logit. While the LAMB optimizer partially addresses this issue, some attention layers still experience sharply increased maximum attention logits. The reason is that $l_2$-norm-based trust ratios in LAMB are less effective in directly influencing extreme weight values. Furthermore, the weight-wise trust ratio in LAMB is error-prone due to overlooking relationships of weight values within rows or columns. Building on these observations, we propose a novel optimizer, MERIT, which leverages the max norm to calculate the trust ratio to directly constrain the max attention logit. Moreover, we further construct element-wise trust ratios to provide more robust update scaling by focusing on local weight structures. Extensive experiments of large-batch training across various sizes of GPT-2 models demonstrate the superior performance of MERIT. Notably, during the training of GPT-2 Medium, MERIT enables the use of a 6k batch size without any performance degradation compared to the standard batch size (480). This work highlights the importance of considering the max attention logit and finer granularity trust ratio calculation in large-batch training. It successfully improves the training stability and paves the way for larger batch usage, enabling faster development and iteration on large language models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper discusses the optimization problem caused by too large maximum attention logits during large-batch training. The authors analyzed that the issue with LAMB arises from the use of L2-norm and proposed a new optimizer, MERIT, which utilizes the max norm to adjust extreme values and introduces element-wise trust ratios to enable more robust updates. In experiments based on GPT-2, MERIT is stable in large-batch settings and outperforms optimization methods such as AdamW and LAMB.

### Strengths
-	The problem of too large logist in attention is a problem that needs to be studied, and the motivation for this study is good.
-	A new optimization method is proposed, which is technically sound
-	In experiments with large batch sizes, MERIT outperformed several popular optimizers including AdamW and LAMB.

### Weaknesses
The writing of this paper needs considerable improvement.

- The layout of figures and tables is confusing. For example, Figure 1 is shown on page 2 but is first mentioned on page 8.
- Table 2 is shown on page 9 but is never mentioned in the content.
- The caption description of the figure is confusing. It would be clearer to use \subfigure[]{}{} to display each subfigure separately and provide individual descriptions for each, rather than combining everything into one single caption for the entire figure.
-  Some text descriptions are also unclear. For example, the caption in Figure 5 says "AdamW:3.470, LAMB:3.355..." The meaning of the numbers is confusing.
- It is recommended to write the definition of Maximum normalized ratio in Section 4.1

There are also some experimental concerns.

- What is the batch size of AdamW in the experiment? From Figure 7 and Table 2, we can see that the batch size of AdamW is 480 and that of MERIT is 4k/8k/12k. Why are they not set the same?
- The ablation experiment in Figure 9 is a key part of verifying the contributions of this paper, but it only lists several absolute values under different learning rates without comparing the effects before and after ablation. I recommend that the authors redraw Figure 9 to include such comparisons.
- The paper needs to compare the performance of MERIT under different batch sizes.

### Questions
-	In lines 46-50, the authors mention two challenges brought about by too large batch size. Can the method proposed in this paper handle these two challenges?
-	What is the connection between the issue of attention generating large logits and the large batch size? Why are these two problems not independent of each other? Could the authors elaborate on this further?

### Soundness
2

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
This paper addresses the challenge of accelerating the pre-training of large language models (LLMs). Specifically, it focuses on a large-batch training approach that can speed up deep neural network training but often encounters degradation if the batch size exceeds certain limits. Current optimizers, such as AdamW, often suffer from performance degradation in very large-batch settings, particularly due to issues in the attention layers. While alternative new methods, like the LAMB optimizer, offer some improvements, they are less effective at managing extreme weight values and fail to account for relationships within weight matrices, resulting in instability.

To address these issues, this paper proposes the MERIT optimizer, which introduces a max-norm-based trust ratio to directly limit the maximum attention logit and applies element-wise trust ratios to better adjust updates. Experiments with various GPT-2 models demonstrate MERIT’s superior stability and performance, even allowing larger batch sizes (up to 6k in GPT-2 Medium) without degradation. This approach highlights the importance of managing maximum attention logits and refining trust ratio calculations for stable large-batch training, supporting faster LLM development.

### Strengths
* This paper addresses an important issue: reducing the high cost of LLM pre-training by using large batches.

* The motivation and approach are clear and reasonable, making them easy to understand.

* The proposed method is simple and appears easy to implement.

* The experimental results are promising.

### Weaknesses
 * The proposed method has only been tested on a single model architecture, GPT-2, so its generalization to other model architectures remains unclear. It would be preferable to evaluate it across multiple model architectures, including newer ones such as Llama-3 and Mixtral for MoE. The lack of evaluation on diverse architectures limits the conclusions about the optimizer's robustness and broad applicability. Specifically, the attention mechanisms and layer structures in models like Llama-3 and Mixtral differ significantly from GPT-2, potentially affecting the optimizer's performance.

* Similarly, the experiments were limited to 125M (small), 355M (medium), and 770M (large) models, which are relatively small compared to recent advancements in model scaling. Models with over 100 billion parameters benefit significantly more from large batch settings. Demonstrating the effectiveness of the proposed method on these larger models would substantially enhance the impact of this paper. For example, showing the comparisons of the initial pre-training stages of larger models may be sufficient. The current scale of experiments does not fully capture the challenges and benefits of large-batch training in the context of modern, massive language models.

* The explanations in this paper are somewhat insufficient in certain parts, making it difficult to interpret what the authors intend to convey. (See the following questions)

### Questions
* I would like to clarify MERIT's memory efficiency. From my understanding, MERIT requires additional temporary memory to compute $b_t$, $r_t$, and $c_t$, but does not need to store these values for subsequent steps. Is this correct? If so, does the additional temporary memory impact the overall GPU memory limits to store the large batch?

* If I am not mistaken, line 10 in Algorithm 1 seems wrong. In my understanding, $x_{t+1} =x_{t} − η_t ...$ should be $w_{t+1} =w_{t} − \eta_t ...$. 

* Moreover, for line 10 in Algorithm 1, there is no clear definition of the clip function, specifically $clip(s_t ·(u_t +\lambda w_t),1)$. Additionally, it is unclear how to compute $clip(st ·(u_t +λw_t),1)$. Does the dot operator represent element-wise multiplication or an inner product? Also, how should the function $clip(A, B)$ be computed, and is argument $A$ a scalar or a vector, given that $B$ appears to be scalar?

* Intuitively, Clipping 1 has a detrimental impact on the optimization process in general, as it may cause the gradient vector to point in an incorrect direction. Therefore, I would like to know the ratio of Clipping 1 throughout the entire optimization process. Could you create a graph that plots the Clipping 1 ratio on the y-axis against the optimization steps on the x-axis?

* I would like to clarify the discussion in the "Curvature of Convergence Point" paragraph. From my understanding, this section claims that large batch sizes tend to converge at sharper minima with higher curvature, but MERIT does not exhibit this trend, unlike AdamW. However, there doesn’t seem to be a clear analysis explaining why this happens. Could you provide an intuitive explanation of why MERIT converges at better points? Also, is this trend observable in medium and large settings?

* The description of Figure 9 is insufficient, making it difficult to interpret. Could you provide more details about each value in the figure?



I am open to increasing my overall rating if the above questions are answered satisfactorily.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces MERIT, a novel optimizer designed for large-batch training of language models. MERIT addresses the issue of max attention logit growth in large-batch training, which can lead to performance degradation. MERIT uses max norm instead of l2 norm to calculate trust ratios, directly constraining max attention logits.  Ant it implements element-wise trust ratios to capture local weight structures more accurately. The authors demonstrate MERIT's effectiveness through the experiments on GPT-2 models of various sizes, showing improved performance and stability in large-batch training compared to existing optimizers like AdamW and LAMB.

### Strengths
1. The authors provide a thorough analysis of the limitations of existing optimizers like LAMB and AdamW in large-batch training, supported by empirical evidence, and then introduce an solution to large-batch optimization for language models by focusing on controlling max attention logits and using finer-grained trust ratios.

2. The proposed method enables stable training with significantly larger batch sizes (up to 6k for GPT-2 Medium) without performance degradation, which could accelerate the development of large language models.

3. The paper is well-structured, with clear explanations of the problem, proposed solution, and experimental results.

### Weaknesses
1. The experiments focus solely on GPT-2 models. It would be beneficial to see results on other architecture types or tasks to demonstrate broader applicability.

2. The paper does not discuss the sensitivity of MERIT to hyperparameter choices, which could be crucial for practical adoption.

### Questions
1. How does MERIT perform on other types of language models beyond GPT-2, such as decoder-only, decoder-encoder models?

2. Can you provide a theoretical analysis or proof for why max-norm-based trust ratios are more effective than l2-norm-based ones in controlling max attention logits?

3. What is the computational overhead of MERIT compared to AdamW and LAMB? How does this impact overall training time when considering the ability to use larger batch sizes?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces MERIT, an optimizer inspired from LAMB that computes trust ratios at several levels (rows, columns, weights) to control the max norm of self-attention logits when training Transformers-based language models. Introducing these ratios allows to avoid the explosion of this value during large-batch training. The authors conduct experiments where language models are trained using large batch sizes and show that their optimizer achieves a better performance than its counterparts for larger batch sizes.

The authors additionally provide a proof of convergence for MERIT. They conduct experiments with language models of varying sizes, and analyze the geometry of the parameter space at convergence. They provide an ablation study to validate the relevance of some parts of their methods.

### Strengths
This paper addresses an important problem and proposes a promising and simple variation to existing optimization techniques to obtain good performance on large batch training. The authors conduct experiments at various model sizes, and provide a theoretical proof of convergence for their optimizer. They identify the max norm of the self-attention logits as an optimization issue for large batch training, which paves the way for more theoretical and empirical work on the subject.
The results of the paper could facilitate distributed model training by allowing larger batch size without performance drop.

### Weaknesses
This paper has major weaknesses, both from the formal and technical viewpoints.
First, this paper has formal issues:
- Some details are missing / poorly explained: in Figure 2, a "medium" self-attention layer is mentioned, but the authors never specifically provide the specific index of this layer. In the Ablation study (Figure 9a), the reported metric is not named, and it is thus impossible to tell if it should be maximized or minimized. Even if one can hypothesize that this metric is final cross-entropy loss, no comparison point is shown with baselines.
- Some notations could be improved: the l2 norm uses the general norm notation, and the max-norm uses an index $m$. A more usual choice would be $2$ and $\infty$ as the norm index.
- The choice of zooming on the last steps of the training in training loss plots is unusual, and discards potentially relevant information.
- Some parts of the presentation could be improved. For instance, in Figure 5, the presentation of the results in the caption is not very readable.

Second, this paper has important limitations, especially when it comes to analyzing Transformers and conducting experiments on language models:
- The authors entirely neglect the fact that self-attention in Transformers is multi-headed, and that although the $W_Q$ and $W_K$ projections are usually implemented using a single matrix for all heads for efficiency purposes, it makes more sense mathematically to discuss head-wise $W_Q$ and $W_K$. They also forget to mention any literature about the outlier dimension phenomenon, which has been extensively studied in the field (https://arxiv.org/abs/2105.06990 is the oldest mention of it I can think of). As such, the observation in Figure 4 can be largely explained by two facts: 1) rows corresponding to the same heads have weights of similar magnitudes, which is why we clearly distinguish 12 stripes in the figure; 2) columns corresponding to outlier dimensions are particularly activated. Moreover, the claim that large max norm for attention logits can be expected when $W_Q$ and $W_K$ have high max-norm as well (L191-197) is not supported by any theoretical evidence and could be false, as $||W_Q||$ and $||W_K||$ do not have any trivial lower-bound implication on $||a||$, especially one that is verified for all possible $X$.
- The authors summarize that the Chinchilla scaling laws predict when "model performance is maximized", without mentioning the fact that this maximization relies on a compute budget constraint. The Chinchilla scaling laws indeed predict that **for a fixed amount of compute**, a model with $N$ parameters should be trained on $D$ tokens to maximize the final performance. Hence, it can be relevant to train small models for a longer time, especially to show the longer-term convergence properties of an optimizer under a fixed training compute budget. Training a model (regardless of its size) on 16B tokens is not in line with current training practice, and we encourage the authors to conduct experiments for larger token counts to validate the relevance of their method.
- The benchmark evaluation results (Figure 6) seem partly not conclusive or relevant. The results for WiC, RACE and Hellaswag are close to those of a random baseline.

The article also presents other flaws:
- The *Curvature of Convergence Point* section: although it seems intuitive that training on large batch sizes leads to smoother curvatures, it would be relevant to compare the method to other large batch methods instead of the small-batch AdamW model. This would make a stronger point to explain the contribution of this paper and single out MERIT on that specific point.
- The claim that *MERIT enables batch sizes over 10 times larger than AdamW*, done in the conclusion, is poorly justified by experiments: based on Figure 1, the negative returns of increasing batch size appear when using a batch size more than 2x as large as with AdamW; Figure 5 shows that AdamW is still an acceptable (although suboptimal) solution in large-batch setups; Table 2 shows that a similar performance can be reached for AdamW used with a batch size of 480 and for MERIT with a batch size of 6k, but it does not mean that AdamW could not have reached a similar performance using a larger batch size. All in all, I do not identify results that can support this claim in the paper.

### Questions
- The choice of the learning rate can be crucial for optimizers. How did you conduct the grid search mentioned in the paper? What were the results of this grid search?
- Scaling training to large setups (i.e. setups that benefit from large-batch training) requires the use of optimizers that can easily be adapted to work in distributed setups. Can your method be easily adapted to work for cases where model weights and optimizer states are sharded and with data parallelism? What was the hardware setup used for your training experiments?
- Why did you not conduct ablations for row-wise / column-wise ratios?
- Did you check the effect of MERIT on the weights as displayed in Figure 4? Does MERIT also change the structure of attention maps (e.g. attention sinks) or the structure of other weights (MLPs, layer norm) ?

### Soundness
2

### Presentation
3

### Contribution
3
