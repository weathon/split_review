# Surprising Effectiveness of pretraining Ternary  Language Model at Scale

- Decision: Accept
- Scores: 8, 10, 10, 5, 5

## Abstract
Rapid advancements in GPU computational power has outpaced memory capacity and bandwidth growth, creating bottlenecks in Large Language Model (LLM) inference. Post-training quantization is the leading method for addressing memory-related bottlenecks in LLM inference, but it suffers from significant performance degradation below 4-bit precision. This paper addresses these challenges by investigating the pretraining of low-bitwidth models specifically {\em Ternary Language Models (TriLMs)} as an alternative to traditional floating-point models (FloatLMs) and their post-training quantized versions (QuantLMs). We present {\em Spectra LLM suite}, the first open suite of LLMs spanning multiple bit-widths, including FloatLMs, QuantLMs, and TriLMs, ranging from 99M to 3.9B parameters trained on 300B tokens. Our comprehensive evaluation demonstrates that TriLMs offer superior scaling behavior in terms of model size (in bits). Surprisingly, at scales exceeding one billion parameters, TriLMs consistently outperform their QuantLM and FloatLM counterparts for a given bit size across various benchmarks. Notably, the 3.9B parameter TriLM matches the performance of the FloatLM 3.9B across all benchmarks, despite having fewer bits than FloatLM 830M. Overall, this research provides valuable insights into the feasibility and scalability of low-bitwidth language models, paving the way for the development of more efficient LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addressed the limitation of post-training quantization by investigating the pretraining of low-bitwidth models specifically Ternary Language Models as an alternative to traditional floating-point models and their post-training quantized versions (QuantLMs). The authors conducted extensive experiments to evaluate the model's performance in different aspects. The experiment results and analysis revealed valuable insights into the feasibility and scalability of low-bandwidth language models.

### Strengths
1. Authors comprehensively evaluate the model's commonsense reasoning performance, knowledge capacity, and toxicity. The experiment part is sufficient and convincing.
2. This work is well presented and it offers valuable insights into the pertaining of low-bitwidth models.

### Weaknesses
1. The pretraining cost of QuantLMs is not revealed (e.g., hardware, GPU hours). Specifically, the paper lacks details on the computational resources required for pre-training, making it difficult to assess the practical feasibility of the proposed approach. The absence of information regarding the number of GPUs, the type of GPUs (e.g., A100, V100), and the total training time in GPU hours hinders a comprehensive understanding of the resource demands.
2. The paper does not discuss how the hyperparameters are selected and tuned. The methodology for choosing hyperparameters such as learning rate, batch size, and optimizer settings is not clearly outlined. This lack of transparency makes it challenging to reproduce the results and understand the sensitivity of the model's performance to different hyperparameter configurations. It is unclear whether a systematic approach like a grid search or Bayesian optimization was employed, or if the hyperparameters were chosen based on heuristics or prior experience.

### Questions
1. Could the authors clarify what the "validation loss" in Figure.7 means? Is it "Log Perplexity" just as in the y-axis in Figure.19 in Appendix D.4? I am curious about the model's generation performance on commonly used datasets such as WikiText-2, C4, PTB.
2. Some fonts in the line chart are difficult to recognize, such as legends in Figure 6(a). In addition, many figures seem incorrectly scaled, making the label of the x/y-axis twisted. Authors should check all figures to improve the clarity.
3. This paper only provides the maximal speed-up compared with FP16. Authors are recommended to benchmark the end-to-end inference performance, such as throughput, first token time, and average latency.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
In this paper, the authors present the Spectra LLM suite, i.e a suite of ternary (1.5-bit) language models (TriLLMs), ranging from 99M to 3.9B parameters. 

Specifically, the authors first extensively pretrain TriLLMs in various size and the corresponding LLM in FP16 (FloatLLM) with exactly the same recipe, and study their differences. The findings are quite fruitful:
1. **Convergence behavior**: TriLLM in various scales can converge normally. With some techniques, like decreasing peak learning rate and removing weight decay at some points, they can converge faster.
2. **Scaling law**: Overall, TriLLM demonstrate a similar scaling law as FloatLLM. With a similar model size in GB, TriLLM achives lower perplexity than FloatLLM. With a similar parameter count, TriLLM is worse than FloatLLM.
3. **Benchmark accuracy**: The authors compare TriLLM to FloatLLM and the quantized version of FloatLLM with GPTQ (QuantLLM), the experimental results show: (1) With a similar model size, TriLLM outperforms FloatLLM and QuantLLM <= 4-bit; (2) With a similar parameter count, TriLLM is worse than FloatLLM and QuantLLM-4bit, but outperforms QuantLLM-3bit.

### Strengths
1. The paper is well-written, and the structure of the paper is clear.
2. The experiments are extensive and the settings are fair, with all claims being well supported. 
3. The findings are interesting. And I believe that the release of all models (including TriLLM and FloatLLM) will further advance the study of TriLLM.

### Weaknesses
1. The only weakness is the applied quantization method in this paper, i.e. GPTQ. GPTQ performs well for bit-level >= 4-bit. However, with lower bit-level, its performance degrades significantly. It would be interesting to see the comparison with more advanced post-training quantization methods, like OmniQuant [1], BiLLM [2], AffineQaunt [3] and so on.

### Questions
1. In Table 5, why isn't the number of skipped tokens proportional to the number of skipped batch?
2. In Figure 6b, what's the motivation for the comparison between TriLLM 2.4B and FloatLLM 1.1B and 1.5B, instead of FloatLLM 2.4B? I think it's better to compare with a similar number of paramters or with a similar model size.
3. Could you also offer some few-shot results on some benchmarks, like MMLU and Lambda? It would be interesting to see the in-context learning ability of TriLLM.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
This paper presents an extensive study on the scaling law of low-bit models, specifically 4-bit, 3-bit, and ternary models. Ternary models (TriLMs) demonstrate impressive effectiveness when scaling model size, with the authors concluding that TriLMs achieve higher performance gains more rapidly during scaling compared to FloatLMs and QuantLMs. A 3.9B TriLM model exhibits performance similar to a 3.9B FloatLM but has a size smaller than that of an 830M FloatLM. The paper first introduces the theoretical advantages of scaling low-bit LMs using information theory. Following this, the authors propose the Spectra LLM suite, which facilitates training experiments on models of varying sizes and bit widths. Finally, scaling experiments conducted on the Spectra LLM platform reveal that scaling a TriLM is more efficient than scaling QuantLMs or FloatLMs. Detailed experimental results are provided, covering the training dynamics of low-bit LMs, pretraining outcomes, and evaluations on downstream tasks. The experiments show that, when scaled to 3.9B, the TriLM achieves comparable performance to the original FloatLM on most aspects, except in areas like toxicity and stereotyping. Further studies on BiLMs are also included in the appendix, where BiLMs show scaling effectiveness, although the performance gap reduction between BiLMs and FloatLMs is slower than with TriLMs.

### Strengths
This paper provides an exceptional perspective on the scaling law of low-bit models, with a particular focus on Ternary Models (TriLMs). The strengths of this study are summarized below:

1. Extensive and thorough workload. This paper comprehensively addresses major concerns regarding the scaling law of low-bit models, including training dynamics, loss curves during pretraining, and evaluation results on downstream tasks. The authors conducted numerous model training sessions and extensive evaluations to support their conclusions. Additionally, the paper provides well-articulated theoretical explanations for why low-bit models scale more effectively and examines how these models align with modern GPU architectures. The paper is inclusive and well-scaled in its coverage of relevant aspects.

2. High novelty and significant contribution. To the best of my knowledge, research on the scaling law of low-bit models is limited, making this work a valuable contribution with well-supported, insightful conclusions. By demonstrating the efficiency of scaling low-bit models, this paper encourages more effective model designs for scaling.

3. Valuable software contribution. As described in the paper, the Spectra LLM Suite serves as a platform for studying the scaling law of low-bit models. This platform is beneficial for the research community, facilitating future work on quantization and low-bit model training.

### Weaknesses
Although this paper provides valuable contributions, there are some areas for improvement. The overall score could be raised if the following issues are fixed and good discussion is made during the rebuttal phase.

1. Presentation needs refinement. While the figures in this paper offer essential information, some are poorly displayed. For instance, Figures 6 and 13 appear compressed, with text that is has low readability. Figure 5 is also confusing due to the similar colors used for arrows. A detailed explanation should guide readers through each part of Figure 5. Additionally, presenting Table 1 alongside Figure 5 could clarify the calculation details.

2. Content organization for conciseness. To fit within the constraints of a 10-page conference paper, the paper could better prioritize content. Since the main contribution is the scaling law of TriLMs versus FloatLMs, related content should be given more prominence. Sections 2.1 and 2.3 are to some extent redundant and could be moved to the Appendix. Section 4.3 could be split into separate sections on scaling law and training dynamics, with each elaborated more thoroughly. Moving parts of Appendix C and findings in Appendix A.5 to the main text would improve the discussion of the corresponding aspect. Moving some BiLM discussions to the main text would also help clarify the outline.

3. Deeper analysis of training dynamics. The paper notes a loss reduction halfway through training but could benefit from further examination of this phenomenon, as it may relate to efficient convergence and scaling. A detailed discussion of changes in the model at this stage would be valuable. Incorporating experiments similar to Appendix D "Analysis of the decay stage" of the MiniCPM paper [1] (COLM 2024 official version) might be helpful to explain this effect. Additionally, a deeper exploration of why low-bit models scale more efficiently than FloatLMs in terms of training dynamics would be insightful.

### Questions
1. Section 2.2 suggests that low-bit models should theoretically provide a better approach for capturing weight variance. In the experiments, TriLMs—where each parameter is restricted to {-1, 0, 1}—demonstrate better scalability than 4-bit models, which in turn scale better than floating-point models. However, in Section 5, the results show that 3-bit models exhibit lower scalability compared to 4-bit models and TriLMs. What might be the underlying reason for this? Additionally, why could TriLMs be more scalable than BiLMs?

2. Based on the discussion in Section 2.2, there may be a relationship between the number of states in each numeric representation and scaling efficiency. What might this relationship look like? Could there be an optimal number representation? This is intended as a discussion question, and a concrete answer is not required during the rebuttal phase. Personally, I believe this could be an interesting direction for future research.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The author developed a series of LLMs with parameters ranging from 99M to 3.9B. These models include a 16-bit floating-point model and a ternary model, both trained from scratch using 300B tokens. Additionally, the author created 3, 4, 6, and 8-bit PTQ variants by applying GPTQ to quantize the floating-point model. Detailed evaluations and comparisons were conducted for each model. The results indicate that the ternary variant outperforms others at the same bit size, and the 3.9B parameter ternary model performs comparably to the 3.9B floating-point model on several evaluation datasets.

### Strengths
The author released a family of a fp and quantized model variant, as well as all the train details/loss and training techniques. Further more, the paper offers detailed evaluations results. Together, it provide good reference for the commnity for lower bit models.

### Weaknesses
The paper extensively discusses the theoretical or maximum possible speedup of the Ternary model, but it lacks results on actual inference speed. It would be beneficial to test the model in a real kernel environment, as many factors could influence speedup, such as activation quantization, KV cache, and kernel implementations.

*FP vs Ternary*: Both models were trained with 300B tokens, and the training loss does not appear to have fully converged yet. It remains to be seen how the models compare once both have converged, and the FP model may require more tokens due to its larger model capacity. The claim that training with 300B tokens is sufficient is not convincing, especially for the 3.9B parameter model. Given the scale of modern LLM training, such as Llama3 which was trained on 15T tokens, it is likely that the 3.9B model is significantly under-trained, and further training could reveal different performance trends between the FP and ternary models.

*Ternary vs Quant 3/4-bit Variant*: The comparison seems unfair, as the Ternary model is trained from scratch with QAT, while the Quant models are derived from GPTQ. The conclusion in the paper may not hold when using QAT for 3/4 bit variant. Furthermore, the choice of GPTQ as the sole PTQ method is limiting. More recent PTQ methods, such as OmniQuant, SpinQuant, or QuaRot, could provide a more accurate comparison point, particularly given that GPTQ is not state-of-the-art for low-bit quantization. The paper's claim that the Ternary model outperforms floating-point or 3/4-bit quantized models under size constraints is unconvincing without a more thorough comparison using state-of-the-art PTQ methods or QAT for the 3/4-bit models.

The novelty is also limited. All components, such as the Ternary network, QAT with STE training, GPTQ, and model architecture, are well-known. The released pretrained models do not have much practical use, as there is a significant performance gap compared to state-of-the-art models of the same size.

### Questions
1. Can the author provide the actual inference speedup numbers for the quantized model compared to the FP model?

2. Train the FP models with more tokens and compare them with the Ternary models.

3. For the PTQ quantized model comparison versus QAT, can the author compare with QAT variant or use more recent PTQ methods such as SpinQuant/QuaRot?

4. What is the training cost of full QAT training compared to the FP baseline? The paper mentions model parallelism at scale. Why is it even necessary, given that the largest model is just 3.9B parameters?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper investigates the scaling law of low bit-width models, specifically ternary language models (TriLMs). The authors present Spectra LLM, an open suite for the quantization-aware training of LLMs. They conduct detailed analysis about TriLM and FloatLM in terms of reasoning, knowledge and toxicity. 3.9B parameter TriLM matches the performance of the FloatLM 3.9B across various benchmarks.

### Strengths
1) The authors provide detailed results of LLMs in various sizes and bits.
2) The authors conduct extensive evaluations in terms of reasoning, knowledge and toxicity.

### Weaknesses
The novelty of the proposed work is unclear. The architecture and training approach of TriLM appear quite similar to BitNet b1.58 [1], including methods such as two-stage weight decay and learning rate scheduling. Previous work [1] has already shown that a 3B ternary LLM can match half-precision LLMs with similar parameter counts and training costs. What additional contributions does this paper offer beyond BitNet b1.58?

The claim that “Spectra is the first to demonstrate the feasibility of pretraining ternary language models compared to their floating-point counterparts” is clearly over-estimated.  BitNet b1.58 already shows this. Furthermore, the training method of Spectra is quite like BitNet b1.58, especially two-stage weight decay scheduling. As for architecture, Spectra only replaces normalization per projection with normalization per layer, which is a very minor difference, and the authors do not explain clear motivations.

The scalability of training data is also very important for pre-trained models. However, the paper does not conduct studies on this problem.

Lack of details about comparison with BitNet b1.58. The authors do not provide experimental details in Appendix A.7, e.g., training data, hyper-parameters. Furthermore, the authors do not report on the validation perplexity of the two models on public dataset, e.g., wikitext or C4.

### Questions
See Weaknesses

### Soundness
3

### Presentation
2

### Contribution
2
