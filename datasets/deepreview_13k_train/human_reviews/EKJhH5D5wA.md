# SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration

- Decision: Accept
- Scores: 8, 6, 5, 6

## Abstract
Speculative decoding (SD) has emerged as a widely used paradigm to accelerate the inference of large language models (LLMs) without compromising generation quality. It works by first employing a compact model to draft multiple tokens efficiently and then using the target LLM to verify them in parallel. While this technique has achieved notable speedups, most existing approaches necessitate either additional parameters or extensive training to construct effective draft models, thereby restricting their applicability across different LLMs and tasks. To address this limitation, we explore a novel \textit{plug-and-play} SD solution with layer-skipping, which skips intermediate layers of the target LLM as the compact draft model. Our analysis reveals that LLMs exhibit great potential for self-acceleration through layer sparsity and the task-specific nature of this sparsity. Building on these insights, we introduce \method, an on-the-fly self-speculative decoding algorithm that adaptively selects intermediate layers of LLMs to skip during inference. \method does not require auxiliary models or additional training, making it a \textit{plug-and-play} solution for accelerating LLM inference across diverse input data streams. Our extensive experiments across a wide range of models and downstream tasks demonstrate that \method can achieve over a $1.3\times$$\sim$$1.6\times$ speedup while preserving the original distribution of the generated text.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
By adaptively skipping intermediate layers during inference, SWIFT improves speedups of LLMs without compromising the quality of generation. The method integrates a Bayesian optimization-based layer selection mechanism to adapt to task-specific requirements dynamically.

### Strengths
While the concept of layer-skipping is not really novel, its use of bayesian optimization can be a good idea for self-SD.

### Weaknesses
1. The reward design and its stability under distributional changes need more explanation. Open discussion with concurrent work, such as "A Unified Framework for Speculative Decoding with Multiple Drafters as a Bandit (Submitted at ICLR'25; https://openreview.net/forum?id=5haYLrlyGj)", could enhance understanding of these challenges. While the primary focus is different, the insight of using bandit approach is quite similar to this paper. And I recommend the authors to put the discussions for the assumption and extensions of Bayesian optimization for layer skipping inspired by this work.


2. More discussions on related work, such as Kim et al. (2024), Stern et al. (2018), and Gloeckle et al. (2024) on pretrained blockwise parallel language models, would position the contribution better within the existing literature. Because both papers are also a parallel line of work for self-speculative decoding, while they use the non-autoregressive heads instead.

- Gloeckle et al. (2024),  Better & Faster Large Language Models via Multi-token Prediction.
- Stern et al. (2024), Blockwise Parallel Decoding for Deep Autoregressive Models
- Kim et al. (2024), Accelerating Blockwise Parallel Language Models with Draft Refinement. (https://openreview.net/forum?id=KT6F5Sw0eg)

### Questions
1. How does SWIFT handle non-stationary input distributions during Bayesian optimization?

2. Could the authors provide insights into how SWIFT performs under extreme token count variations or highly domain-specific tasks?

### Soundness
3

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
3

### Summary
This paper aims to improve speculative decoding (SD) with a focus on eliminating the need for additional model parameters or extensive training to enable effective drafting in SD. In particular, the paper utilizes the same (target) model as the draft model by skipping a subset of model layers while generating draft tokens. Towards this, the paper proposes an SD method, namely SWIFT, that performs on-the-fly adaptive layer selection via an optimization phase to identify task-specific layers to skip. The optimization phase is followed by an inference acceleration phase that leverages the identified layers to perform skipping during drafting. During the inference acceleration phase, SWIFT additionally relies on 1) early stopping of the drafting process if (draft) model's confidence is not high enough; and 2) utilizing top-k predictions for each draft token position during parallel verification. The authors empirically validate the utility of SWIFT by showcasing 1.3-1.6x speed-up on CNN/DM, GSM8K, and TinyStories datasets.

### Strengths
1) The paper successfully demonstrates that the speculative decoding (SD) framework has the potential to speed up LLM inference even when one does not employ additional model parameters and task-specific training to support the drafting phase.

2) The paper makes two key observations about layer skipping during the drafting phase that highlights the need for adaptive (task-specific) selection of layers to skip during the drafting phase to maximize the benefit of layer skipping-based drafting approach. Subsequently, the paper proposes SWIFT - an effective SD approach that can identify a reasonable set of layers to skip for the underlying task with minimal training.

3) The paper further showcases the utility of leveraging the (draft) model's prediction confidence and top-k per-token predictions to improve the realized speed-up via SWIFT.

4) The paper is mostly well-written and conveys the key ideas in sufficient detail. The proposed ideas exhibit sufficient novelty over existing SD methods. The empirical results and in-depth empirical analysis highlight the gains realized by SWIFT over vanilla LLM inference.

### Weaknesses
1) There is room for improvement in the discussion of related prior work. Given that Elhoushi et al. 2024 also leverage layer skipping during the drafting phase, a detailed discussion of this work is warranted. Furthermore, the authors may also want to cite https://openreview.net/pdf?id=yUmJ483OB0. 

2) The authors may want to make their empirical evaluation more comprehensive. Currently, the authors don't compare with existing approaches that rely on layer skipping during the drafting phase. Even though these existing methods might rely on extensive training, the authors should compare SWIFT with these methods. Such a comparison can highlight if there is any performance gap between these methods and their proposed plug-and-play approach.

3) The paper aims to eliminate the extensive training of existing layer skipping-based approaches via an efficient on-the-fly optimization phase. However, it's not clear if the existing methods can also perform well even when one limits the amount of offline training for these methods.

4) The authors repeatedly emphasize that their proposed method is a plug-and-play method. However, they don't seem to be evaluating their method in a dynamic setting where the underlying task (distribution) changes over time. In such a dynamic setting, would SWIFT have to interleave the optimization and acceleration phases? Would one still observe a good amount of speed up in such settings?

### Questions
Please see the weaknesses section above. In addition, please consider the following questions:

1) Looking at the ablation studies in Appendix D (Table 7), it appears that *dynamic verification* does not bring much value as the loss in overall speed-up is minimal when one excluded dynamic verification (1.560x to 1.541x). Could authors comment on this?

2) Do the speedup numbers in Table 2 take into account the optimization phase? If yes, how many LLM generations are performed to obtain the results in Table 2?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a plug-and-play self-speculative decoding method. The authors employ a layer-skipping approach to construct a draft model. Experimental results indicate that this method achieves a 1.3-1.6 times inference speedup on Llama-2 and Code-Llama models.

### Strengths
The method does not require training an additional model or module for drafting, making it applicable to most large language models.

### Weaknesses
1. The speedup is not as promising compared to other training-free methods like Lookahead. The authors should also present results for methods such as Mudusa and Eagle, which require minimal training overhead.
2. It is recommended that the authors test well-trained LLMs, such as Llama-3, as models with less effective performance might yield higher speedup ratios.
3. The method requires different settings for different tasks. However, in real-world LLM chat applications, it is often difficult to predict the corresponding tasks of user instructions. It is suggested that the authors evaluate the method's speedup performance on benchmarks like MT-Bench, which test the general capabilities of models.

### Questions
1. Table 2 presents results for Llama-2-13B, Llama-2-13B-Chat, and Llama-2-70B. Why are the results for Llama-2-70B-Chat and Llama-2-7B(-Chat) not included?
2. How does the overhead of the proposed layer searching algorithm compare to the overhead of training additional modules like Eagle?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to accelerate the inference of LLMs. They introduce SWIFT, a self-speculative decoding algorithm that adaptively selects intermediate layer to skip without extra cost. They performed an empirical analysis of layer-skipping SD paradigm and show the potential of self-accelerate of LLMs through layer sparsity. They used some techniques like early-stop drafting to further speed up reasoning.

### Strengths
1.The paper is well-written and flows very smoothly. 
2.The authors make effort to demonstrate the feasibility of their theory through experiments.
3.The method incorporates many of the latest techniques.

### Weaknesses
1.The author should compare their method with self-SD [1] in table 2, since their method is an improvement of the latter. 
2. The author only compared to the baseline on the Llama and CodeLlama models. I believe experiments should be conducted on larger models with different architectures to demonstrate the generalization of the method.
3.Moreover, compared with self-SD, the innovation is still insufficient, for example , the confidence-aware inference strategies are similar to some mechanism in [1],[2]
4.Despite SWIFIT does not require additional training, comparing with other method ,like EAGLE [2] ,Medusa [3], which can achieve over a 3.05-4.26x speedup, SWIFIT does’t show much value.As reported in [2], the draft models is trainable within 1-2 days for 70B models.

### Questions
1.The author should compare their method with self-SD [1] in table 2, since their method is an improvement of the latter. 
2. The author only compared to the baseline on the Llama and CodeLlama models. I believe experiments should be conducted on larger models with different architectures to demonstrate the generalization of the method.
3.Moreover, compared with self-SD, the innovation is still insufficient, for example , the confidence-aware inference strategies are similar to some mechanism in [1],[2]
4.Despite SWIFIT does not require additional training, comparing with other method ,like EAGLE [2] ,Medusa [3], which can achieve over a 3.05-4.26x speedup, SWIFIT does’t show much value.As reported in [2], the draft models is trainable within 1-2 days for 70B models.

[1] Draft & Verify: Lossless Large Language Model Acceleration via Self-Speculative Decoding. ACL 2024
[2] EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees, EMNLP 2024
[3] Medusa: Simple Framework for Accelerating LLM Generation with Multiple Decoding Heads, ICML 2024

### Soundness
2

### Presentation
3

### Contribution
2
