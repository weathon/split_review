# Efficient Fine-Tuning of Quantized LLMs via Three-Stage Optimization

- Decision: Reject
- Avg Score: 5.40
- Scores: 5, 3, 6, 5, 8

## Abstract
To address the memory consumption and computational efficiency issues in fine-tuning large language models (LLMs), Parameter-Efficient Fine-Tuning (PEFT) and quantization have emerged. Recent studies have combined the two and have proposed adjusting parameters before fine-tuning to reduce quantization errors, aiming to improve fine-tuning performance. We find that the performance of fine-tuning on the adjusted quantized models is even worse than using the original quantized models directly, as the adjusted model is essentially a completely different model from the original quantized model. Additionally, we have discovered that due to the poor robustness of quantized models, increasing the training difficulty may result in even worse outcomes. To address this, we propose two constraints for fine-tuning quantized models, and based on these, we introduce a general fine-tuning framework called QR-Adaptor. This framework bypasses the network errors introduced by quantization and directly uses actual performance and memory as optimization targets. Through initialization, extrapolation, and interpolation, it quickly solves this gradient-free optimization problem. Experimental results demonstrate that our method yields fine-tuned low-bit quantized models that outperform fine-tuned 16-bit models while maintaining the same memory usage as fine-tuning 4-bit models. For example, in the zero-shot test on MMLU, it improves accuracy by 3.3\% over both LoftQ and LQ-LoRA.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Based on the motivation that the performance of fine-tuning on the adjusted quantized models is even worse than using the original quantized models directly, the paper introduced QR-Adaptor that bypasses the network errors introduced by quantization and directly uses actual performance and memory as optimization targets. The experimental results are based on Llama 2 7B and 13B.

### Strengths
- The paper presents the clear motivation that the performance of fine-tuning on the adjusted quantized models is even worse than using the original quantized models directly.

- Low-precision models fine-tuned with QR-Adaptor can surpass the 16-bit fine-tuned models, while maintaining memory usage comparable to that of 4-bit quantized models.

### Weaknesses
 - It would be necessary to conduct experiments for Llama-3 family (e.g., Llama 3 8B), which are known to be harder to quantize.

- The comparison of training time between QR-Adaptor and existing methods would be required because QR-Adaptor seems to take longer than previous methods due to the presence of bayesian optimization.

- It would be more beneficial if prior methods are also done with 6.125-bit for Llama 2 13B and 5.875-bit for Llama 2 7B in Table 1.

### Questions
NA

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Summary
The authors propose a novel method for fine-tuning quantization LLM. The core of this approach is a three-stage optimization process that selects quantization bit-widths and corresponding LoRA ranks for each layer of the model. Initially, the method computes layer-wise importance on a small dataset, which serves as the initial values for bit-widths and ranks. Subsequently, the authors employ their proposed Pareto Ranking Genetic Algorithm (PRGA) optimization method, followed by Bayesian optimization, to identify more optimal solutions. The efficacy of this method is demonstrated through experimental validation on datasets such as MMLU, showcasing its superiority in terms of both memory efficiency and performance metrics.

### Strengths
Strengths:
1. Overall, the paper is well-organized and easily comprehensible. The motivation is effectively introduced, and the methodology is clearly described.
2. The method's introduction of gradient-free optimization to the fine-tuning of quantized LLMs is noteworthy and provides valuable insights for future research in this area.
3. The proposed approach demonstrates superior performance in terms of both memory efficiency and model performance compared to state-of-the-art works in the same domain.

### Weaknesses
Weaknesses:
1. The author claims that"inspired us to develop the Pareto Ranking Genetic Algorithm (PRGA), a novel multi-objective optimization method."The proposed Pareto Ranking Genetic Algorithm (PRGA) bears a striking resemblance to the existing Non-dominated Sorting Genetic Algorithm II (NSGA-II), to the extent that they are virtually indistinguishable. However, the authors have failed to acknowledge or cite NSGA-II, instead claiming PRGA as a "novel multi-objective optimization method".PRGA and NSGA-II are almost identical, including key elements such as non-dominated sorting, crowding distance calculation, and elitist strategy. 
2. The novelty of this paper appears limited, as it primarily applies existing algorithms, namely NSGA-II and Bayesian Optimization, to the fine-tuning of quantized LLMs. 
3. The authors claim that previous methods relying on gradient norms to quantify layer importance fail to accurately represent a layer's contribution during inference. However, they do not substantiate this claim with ablation studies. 
4. The current ablation experiments are insufficient. Additional studies should be conducted to demonstrate the impact of iterations and population size on the results. 
[1]Deb K, Pratap A, Agarwal S, Meyarivan TAM. A fast and elitist multi-objective genetic algorithm: NSGA-II[J]. IEEE Transactions on Evolutionary Computation,2002, 6(2):182-197.

### Questions
Question
1. What are the differences between NSGA-II and PRGA?
2. Is the proposed method sensitive to the selection of iterations and population size?

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
The paper introduces a framework called QR-Adaptor that combines parameter-efficient fine-tuning and quantization techniques to improve the performance of LLMs with reduced memory usage. The QR-Adaptor framework includes three stages: initialization based on task information, global exploration using Pareto Ranking Genetic Algorithm (PRGA), and local refinement with Bayesian optimization. Experimental results show that the method outperforms fine-tuned 16-bit models while maintaining the same memory usage as fine-tuning 4-bit models.

### Strengths
1.This article proposes the use of gradient-free optimization methods to optimize the rank selection of layer-wise LoRA and the bit selection of layer-wise Quantization, which is quite novel.
2.This method could be combined with other quantization methods to potentially achieve better performance.
3.The results on datasets such as MMLU show that QR-Adaptor has achieved excellent performance in both memory and accuracy.
4.Ablation studies indicate that the proposed three-stage optimization framework effectively yields superior solutions.

### Weaknesses
1.The introduced multi-stage optimization process increases the time cost.
2.The experiments in this article are limited, conducted only on Llama2, and the datasets used are not diverse enough. If considering expanding the experiments, one could refer to the experiments in the LoFTQ paper.
3.There is a lack of experiments on the impact of PRGA hyperparameters on model performance.
4.There is a lack of comparative experiments between the PRGA method and other multi-objective optimization methods.
5.Figure 1 is somewhat difficult to understand and should not be placed on the first page.

### Questions
In addition to the weaknesses, I have the following questions:
1.I am curious about the effectiveness of directly applying the approach of this article to LLMs quantization, that is, using gradient-free optimization methods to select the quantization bit numbers for each layer's parameters.
2.AdaLoRA is not specifically designed for quantized LLMs, and its direct performance may be poor. Therefore, concluding that dynamically adjusting rank is not suitable for fine-tuning quantized LLMs may not be sufficiently justified. Can we test AdaLoRA's performance on fine-tuning quantized LLMs again under the condition of Preserving quantized model parameters before fine-tuning?

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
This paper addresses quantized parameter-efficient fine-tuning. It proposes two constraints: initializing LoRA parameters either as zero or using MSE initialization like LoftQ and LQ-LoRA, while fixing all trainable parameters. Additionally, it introduces mixed-precision quantization and mixed-rank LoRA, achieving higher performance with the same training memory footprint as 4-bit models.

### Strengths
1. The framework is practically useful, allowing for higher-performance fine-tuned models with a 4-bit memory footprint.
2. The paper is well-written and easy to follow.

### Weaknesses
1. The constraints are derived from limited experiments in Figures 2 and 3. For instance, Figure 2 suggests careful LoRA initialization does not improve performance, yet LoftQ and LQ-LoRA demonstrate its effectiveness. LoRA initialization can mitigate quantization loss, crucial for models with significant quantiztaion loss, such as lower-bit quantizations or more challenging models like llama-3-8B. A deeper analysis with stronger experiments and detailed discussion on LoRA initialization is needed.

2. The paper heavily focuses on the two constraints, which seem more like ablation studies and do not offer new insights or motivation for the final methods. The main contribution is achieving higher performance with the same memory footprint as 4-bit models. The paper should be reorganized to highlight its original contributions.

3. The performance improvements could be attributed to higher-bit models and reduced memory footprint through adaptive LoRA rank reduction. Since small LoRA ranks may not perform well on large datasets, it's important to verify the method's effectiveness on larger datasets.

### Questions
Why does QR-Adaptor consistently outperform LoRA fine-tuning with 16-bit models? Is the advantage due to adaptive LoRA ranks, considering FP16 models are typically more powerful than quantized models?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
They bypasses the network errors introduced by quantization and directly uses actual performance and memory as optimization targets. Through initialization, extrapolation, and interpolation, they quickly solves the gradient-free bit-width and lora rank optimization problem of fine-tuned low-bit quantized models.

### Strengths
The framework outlined in Figure 1 is resonates. Figures 2 and 3 effectively illustrate the key observations and the rationale behind our approach.

### Weaknesses
This paper is credible in its approach, but lacks a good logical structure in presenting the corresponding challenges. In the abstract "We find that the performance of finetuning on the adjusted quantized models is even worse than using the original quantized models directly,  as the adjusted model is essentially a completely different model from the original quantized model. ", the adjusted quantized models is a vague statement, and these unclear statements affect my understanding. Therefore, I expect the authors to reformulate the three challenges of the necessity of init/search r and q layer-wise and adopting a gradient-independent strategy in Introduction.

### Questions
1. My main concern was the extra time cost, could you provide comparisons with existing methods in terms of time cost? Can the computational cost of each stage be disclosed?
2. The caption of the subfigure in Figure 7 needs to be supplemented.
3. Will the bad performance affected by unfixed parameters mentioned in Figure 3 improve with longer fine-tuning epochs? This does not seem to be a very intuitive phenomenon, can the author provide more explanation?

### Soundness
4

### Presentation
3

### Contribution
3
