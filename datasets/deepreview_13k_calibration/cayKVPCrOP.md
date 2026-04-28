# GOOD: Decoding-Time Black-Box LLM Alignment

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
Large Language Models (LLMs) have demonstrated immense potential across various applications. However, aligning these models with specific real-world tasks and human preferences typically requires resource-intensive fine-tuning processes such as Supervised Fine-Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF).
In this paper, we propose GOOD (Guided Online Optimal Decoding), a novel alignment method that enhances pre-trained models without the need for parameter fine-tuning. We observed that the alignment-related behavior of one model can be used to guide another model, and based on this insight, we proposed the GOOD method. Utilizing a pair of guiding models, GOOD identifies critical positions related to alignment and adjusts the model’s output dynamically during the response generation. Notably, the interaction between the guiding models and the guided model occurs at the string level, enabling GOOD to be applied to align even black-box models.
Experiments show that GOOD can achieve performance comparable to or even surpassing direct fine-tuning in terms of comprehensive capability and harmless generation, reaching relative scores of 108\% and 105\% respectively. Even in weak-to-strong alignment, it can recover up to 94\% of the performance of directly fine-tuned models. GOOD can also be applied to enhance already aligned models (improving pass@1 by 52\% in code enhancement), making it compatible with various existing alignment techniques.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an alignment method called Guided Alignment Online Optimal Decoding (GOOD) that can enhance the outputs of a pre-trained models during response generation. This method uses a pair of guiding models, namely an aligned one and a non-aligned one, to identify critical positions and adjusts the target model’s output dynamically during decoding. The main advantage is that no finetuning or additional training required for the target model. Experiments show that this method has competitive performance compared to finetuning in terms of general capability and harmless generation,  In addition, it can be used to enhance strong non-aligned models and already aligned models.

### Strengths
1. Proposes a method that is able to align any large language model by having access to a pair of smaller models, a non-aligned model and its aligned version, during response generation without requiring any finetuning. 
2. The key innovation that differentiates it from proxy tuning is the idea of re-encoding and using the generated tokens from the guiding model on particular locations instead of directly modifying the output distributions of the target model. This enables its application to any black-box model.
3. Extensive evaluations show that the proposed method can recover the alignment performance of finetuned models by using to weak models. Notably, this finding holds for particularly large models (improving Qwen-2-72B model using Qwen-2-7B) and it can also improve already aligned models.

### Weaknesses
1. Using two models in addition to the target one and performing forward passes in parallel can lead to additional computational cost and memory requirements, as well as increased complexity during deployment phase. These factors can hinder applicability and adoption in real-world scenarios. The paper could benefit from quantifying this impact, not just theoretically but also empirically, by comparing the actual inference time and memory usage against baseline methods. It's crucial to understand how the overhead scales with model size and sequence length, as this will determine the practical feasibility of the approach.
2. The evaluation focuses mainly on comparisons with full-finetuning and lacks broader coverage of alternative alignment methods that are applied during decoding time other than Proxy Tuning and GaC. For instance, using a reward model directly during the decoding process to guide generation or through interpolation of logits. The absence of comparisons with methods that also operate at decoding time makes it difficult to assess the relative advantages and disadvantages of the proposed approach. Furthermore, the paper should discuss how GOOD compares to constrained text generation methods, which also aim to control the output of language models, and related techniques that use grammars or other constraints to guide decoding.
3. The necessity of using both auxiliary models haven't been justified theoretically or empirically through ablation experiments (even if it requires relaxing the blackbox assumption). I'd suggest comparing with output ensembling or speculative decoding by using the aligned auxiliary model whose output distribution you aim to maintain, to demonstrate if the proposed method is better than directly combining the aligned model with the target one. The current justification for needing two models is not sufficiently strong, and more rigorous experimentation is needed to validate this design choice.
4. Discussion is missing to highlight the differences of the proposed approach to constrained text generation literature and related methods. Specifically, it would be beneficial to discuss how GOOD compares to methods that use grammars or other constraints to guide decoding, and how it handles situations where the constraints are complex or ambiguous. The lack of this discussion limits the understanding of the novelty and applicability of the proposed method.
5. There is little emphasis on the potential drawbacks and performance in the limit of the proposed method, for instance what is the minimum size of the pair of auxiliary models need to be for this approach to work? The paper should explore the limitations of the method, such as the minimum size and quality requirements for the auxiliary models, and how performance degrades when these requirements are not met. It is also important to understand the sensitivity of the method to the choice of auxiliary models and their alignment quality.

### Questions
1. The introduction omits to explain the significance and impact of using a pair of guiding models in terms of cost and quality. What are the assumptions about these models? Do they require training on the same alignment data as the target model? 
2. Can you elaborate on the relationship of GOOD with prior work? It would be useful to explain for the reader what are the common parts and differences compared to prior established methods for constraining the outputs of LMs. 
3. What are the key advantages of GOOD compared to alternative decoding-time alignment methods such as the ones mentioned in the weakness 2 above?
4. Using three models during inference is expected to increase the latency and memory requirements dramatically. Can the authors share a few numbers that quantify the computational cost? Inference is actually the part of the LLM stack that is the most costly as it requires committed resources to it, while finetuning happens only once. If you have any comparisons between these costs it would help with better understanding the pros and cons.  
5. In what kind of scenarios to the authors envision this approach to be used in practice?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposes GOOD, a decoding-time alignment method that aligns raw pre-trained LMs without tuning. Specifically, a pair of Base and Instruction guiding LMs are utilized to identify the timing where guidance is needed, if this is the case, then the predictions from the guiding Instruction model is appended rather than the token decoded from the original model. Experiments in varioius evaluation settings are conducted, where the results indicate the effectiveness of the proposed method.

### Strengths
- Decoding-time alignment is an interesting research direction, which alleviate the potential costly tuning of LMs.
- The proposed method can obtain reasonable results, and the analyses provide some interesting insights.

### Weaknesses
 - This method still requires an aligned guiding model, which is still the resulting model from tuning-based alignment.
- Some parts of the algorithm is not well explained, specifically, it seems to be an important decision of when alignment is needed. More details on this part should be provided.

### Questions
- The idea is in some way very similar to the one proposed by Mitchell et al. (2023), comparisons or at least discussions should be provided.

[1] An Emulator for Fine-Tuning Large Language Models using Small Language Models, Mitchell et al., 2023

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
3

### Summary
This paper proposes a decoding-time LLM alignment method called GOOD (Guided Online Optimal Decoding), which utilizes a pair of guiding models (one aligned, one unaligned) to guide another model. Performing the alignment at decoding time is presented as an alternative to (resource-intensive) alignment during training (e.g., via SFT or RLHF). GOOD differs from other decoding-time alignment algorithms in that it does not require access to the guided model's parameters or vocabulary, and thus can be applied even to black-box models. GOOD is a two-step method: 1) Alignment discrimination, to identify positions which need alignment by comparing the logits of the two guiding models, and 2) Output substitution, where the guiding model's output replaces that of the guided model at the positions identified for alignment. This paper evaluates GOOD on MTBench and on the Helpful and Harmless dataset, and shows that it can achieve performance comparable to direct finetuning. Even when using guiding models which are weaker than the guided model, most of the performance of direct finetuning can be recovered at decoding time. The paper also shows that GOOD can further improve performance of already-aligned models. Finally, the paper performs some analyses to understand the importance of alignment discrimination (step 1 in the GOOD process) and its sensitivity to hyperparameter settings, and to understand similarity of GOOD-decoded outputs to both those of the guiding model and to those of the same model aligned directly through finetuning.

### Strengths
- The motivation is clear, including the relationship of GOOD to other training-time and post-training alignment methods.
- The results are compelling, especially those showing that 1) GOOD can perform on par with alignment via direct finetuning, and 2) most of these gains can still be preserved even when using a guiding model which is weaker than the guided model.
- There are some insightful ablations, including the ablation using random guidance (for understanding where the performance improvement from GOOD comes from), and the sweep over different guided decoding ratios (to understand the sensitivity of performance to the amount of alignment guidance provided).

### Weaknesses
 - There is no mention of the inference-time cost of GOOD (Algorithm 1). The paper motivates decoding-time alignment methods by citing the resource-intensiveness of training-time approaches, but does not provide an analysis of the time complexity of GOOD or report results on how much it slows down inference (for different guiding models). The tradeoff between cost at training versus inference time is an important consideration.
- The description of the GOOD algorithm in Figure 1 and Algorithm 1 (and in the text) is underspecified and missing key details. See specific questions in "Questions" section.
- The claims in the paper regarding where the GOOD performance enhancement comes from are not fully substantiated. See specific questions in "Questions" section.



### Questions
- Questions regarding the GOOD algorithm (Algorithm 1):
  - At every iteration of the while loop, are you re-decoding from the start of the input sequence I_{B}? If a token(s) is replaced in I_{B}, are the remaining decoding steps using model B conditioned on these replaced tokens?
  - Given that I_{A}, I_{A_{it}}, and I_{B} are not (necessarily) equal, the decodes t_{A}, t_{A_{it}}, and t_{B} are conditioned on different prefixes, and it seems likely they'd often be misaligned (e.g. different word order, etc). So is there any guarantee that i) the comparison of logits t_{A} and t_{A_{it}} (step 6) make sense, and 2) the replacement token t_{A_{it}} (step 8) makes sense in the context of the output O_B? 
- The paper mentions the importance of the alignment discrimination step, but only Max Match and a variant of Top P Overlap were considered. Were any ablations performed to investigate the effect of the discrimination method? Were alternative alignment discrimination methods (e.g. measures of distance between probability distributions) considered?
- The paper states that the performance improvement from GOOD "mainly stems from accurately identifying positions that need alignment". Figure 5 shows that random guidance substantially underperforms guided decoding (with a variant of Top P Overlap), but does not take into account the quality of the guiding model. Table 1, on the other hand, shows the performance of GOOD for a few different guiding models, but does not report the performance of the guiding model itself. Is there any complete analysis showing the relative importance of step 1 (alignment discrimination) versus step 2 (output substitution)?
- There is no discussion of how the A_{it} guiding models used in the experiments are aligned. Is it via SFT and/or RLHF, and which datasets are used to perform the alignment?

Nits:
- Figure 2 and Figure 3 are small and hard to read.
- The fact that GOOD doesn't require access to the guided model's parameters is emphasized several times, but there is no mention that access to the logits of the *guiding* models is indeed required. For clarity, it would probably be worth mentioning this point.
- Also, it is emphasized that access to the guided model's vocabulary is not required, but access to the guiding model's tokenizer is in fact required. This could be misleading, and should probably be clarified.

### Soundness
2

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
This paper proposes Guided Online Optimal Decoding (GOOD), a training-free and flexible decoding framework for aligning large language models (LLMs). This approach is based on the assumption that different models develop similar alignment skills during fine-tuning.

During each inference step, (1) GOOD first generates a token using a guiding model pair, which consists of a base pre-trained model and a well-tuned instruct version. (2) It then decodes the token using the guiding model. (3) If alignment is necessary, it converts the token to a string, and re-encodes it using the guiding model's tokenizer. (4) Finally, it updates the output and input sequences.

Extensive experiments on MT-bench, harmless generation, coding and weak-to-strong scenarios and further analysis demonstrate that the effectiveness of GOOD.

### Strengths
The paper is well-written and easy to read. The proposed method achieves competitive performance under the experimental setup of this paper, demonstrating results comparable to the instruct version without requiring any training.

### Weaknesses
1. The main weakness of the proposed method in this paper is the significantly high inference overhead. In the process of generating each token, three models (the guiding model pair and the guided model) perform synchronous inference, and after each reasoning step, a determination is made to check if alignment is needed. If alignment is required, the results must be concatenated and updated. Therefore, I believe the method proposed in this paper is somewhat tricky, as it increases the number of models involved in inference for the sake of a training-free gimmick, leading to significantly higher inference costs that hinder practical application.

2. The paper lacks an analysis of the inference costs, particularly in comparison to single-model inference and similar methods (like Proxy-Tuning) regarding memory usage and inference time. Specifically, the paper should provide a detailed breakdown of the computational cost associated with each step of the GOOD method, including the forward passes for both the guiding model pair and the guided model, as well as the overhead of tokenization and concatenation. A comparison of the total inference time and memory footprint with a standard single model inference should be included, as well as a comparison with Proxy-Tuning, which also involves multiple models.

3. The paper lacks experimental comparisons. While the authors compare GOOD and Proxy-Tuning in code generation, it is unclear why no comparisons were made for the other two experimental categories (MT-bench and harmless generation). Although Proxy-Tuning has limited flexibility, I believe it is important to conduct a comprehensive comparison, as it serves as a strong baseline for the method proposed in this paper. The absence of these comparisons makes it difficult to assess the true effectiveness of GOOD across different tasks and to understand its advantages and disadvantages relative to existing methods.

4. The paper lacks additional validation, such as further testing of conversational and instruction-following abilities on AlpacaEval, as well as more extensive verification of complex reasoning in mathematics. These additional evaluations are crucial to demonstrate the robustness and generalizability of the proposed method. The current experiments are limited in scope and do not fully explore the capabilities of the model in diverse and challenging scenarios.

5. The font size of the legends and coordinates in the figures is too small, making it difficult for readers to clearly see the information.

6. I believe that the tables in the paper should primarily use a three-line format, as the current table style does not seem to align with academic conventions.

### Questions
I would be very happy to engage in further discussion with the authors. My main questions are as follows:

1. I hope to discuss the value of this paper with the authors. In the first point under Weaknesses, I mentioned that the simultaneous inference of three models in the GOOD method may lead to excessively high inference costs, making practical application difficult. Therefore, I would like to gain deeper insights into how this work can inspire future improvements.

2. Could you provide a detailed comparison of inference costs to give readers a comprehensive and intuitive understanding?

3. Could you include comparisons with existing baselines in the experiments of this paper?

4. Could you add more evaluations, such as AlpacaEval or mathematical reasoning?

I will review the paper from a critical perspective to help make it more solid and I look forward to further discussions with you.

### Soundness
2

### Presentation
3

### Contribution
2
