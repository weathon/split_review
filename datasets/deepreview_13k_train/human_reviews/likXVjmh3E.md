# The Expressive Power of Low-Rank Adaptation

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
\emph{Low-Rank Adaptation} (LoRA), a parameter-efficient fine-tuning method that leverages low-rank adaptation of weight matrices, has emerged as a prevalent technique for fine-tuning pre-trained models such as large language models and diffusion models.
Despite its huge success in practice, the theoretical underpinnings of LoRA have largely remained unexplored. 
This paper takes the first step to bridge this gap by theoretically analyzing the expressive power of LoRA. 
We prove that, for fully connected neural networks, LoRA can adapt any model $f$ to accurately represent any smaller target model $\tgf$ if LoRA-rank $\geq(\text{width of }f) \times \frac{\text{depth of }\tgf}{\text{depth of }f}$, under a mild assumption. 
We quantify the approximation error when the LoRA-rank is lower than the threshold. 
For Transformer networks, we show any model can be adapted to a target model of the same size with rank-$(\frac{\text{embedding size}}{2})$ LoRA adapters.
Our study reveals numerous theoretical insights on hyperparameter tuning and algorithm development for LoRA, all of which are empirically validated.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
While conventional fine-tuning updates all model parameters for specialized tasks, full weight updating would be prohibitive for large language models (LLMs). Many methods were proposed to selectively update smaller parameter subsets or introduce lightweight adapters, significantly reducing computational and storage costs. The dominant method in this context is Low-Rank Adaptation (LoRA), which employs low-rank adapters to pre-trained weight matrices. Empirical evidence shows that LoRA can match or surpass the performance of full fine-tuning. However, there is a lack of theoretical understanding regarding how LoRA works, including questions about the minimum rank of adapters required for effective adaptation and how model architecture influences this threshold. Addressing these theoretical questions will provide valuable insights into the effectiveness and principles behind LoRA's adaptation of LLMs.

### Strengths
1. This paper claims that they are the first to study the expressive power of Low-Rank Adaptation (LoRA) for different model architectures. So, if this is true (I do not have sufficient knowledge to check), the novel of this paper is significant. 

2.  Their theoretical results align well with the recent advances of LoRA on LLMs. 

3.  Not only FNN but TFN is explored with the both theoretical and emperical study.

### Weaknesses
(1) From Figure 1, I can see that LoRA of FNN performs on par with gradient update, whereas LoRA of TFNs significantly outperform gradient updates. Could the author explain this performance difference? It is unclear why the performance of LoRA on FNN is not as pronounced as on TFNs. The paper should delve deeper into the architectural differences between FNNs and TFNs that might cause this discrepancy. Specifically, are there inherent properties of TFNs that make them more amenable to low-rank adaptation compared to FNNs? A more detailed analysis of the interaction between LoRA and different network architectures is needed to fully understand the observed results.

(2) It is impressive that LoRA with rank=1 can match the performance of gradient update in Figure 3. Does this mean the gradient update does not actually learn well? The paper should explore the optimization landscape of gradient descent in this context. Is the gradient descent algorithm getting stuck in local minima, or is the optimization problem inherently ill-conditioned? A comparison of the learned parameters from the gradient update with the parameters obtained via LoRA would provide valuable insights. Furthermore, it would be beneficial to investigate the sensitivity of gradient descent to different initialization strategies and learning rates. This analysis would help to determine if the observed performance is due to limitations of the optimization algorithm or if it is an intrinsic property of the problem.

### Questions
Please see the above weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a theoretical analysis of Low-Rank Adaptation (LoRA), a technique for efficiently fine-tuning pre-trained models, including large language and diffusion models. It establishes that LoRA can effectively adapt a fully connected neural network to represent a smaller target model if the LoRA-rank is sufficiently high. Specifically, the required rank is at least the product of the model's width and depth. For Transformer networks, the study demonstrates that a model can be fine-tuned to match a target of the same size using LoRA adapters of a particular rank. These theoretical assertions are underpinned by practical numerical experiments.

The paper concludes by highlighting the importance of LoRA's rank and the pre-trained model's depth in achieving close approximation to the target model. Despite these advances, it points out that the construction method for LoRA adapters might not be fully optimized and that better parameter efficiency could be achieved with more refined techniques. The paper also calls for additional research to measure approximation errors when LoRA-rank is not ideal, especially in the context of Transformer networks, and to further explore the application of LoRA in more complex network architectures.

### Strengths
- The study conducts a thorough analysis of the expressive capabilities of LoRA, underpinned by a set of well-founded assumptions.

- The findings from this research offer a theoretical foundation for applying LoRA to a diverse range of models, including Transformers and Diffusion models, and furnish insights on how to select hyper-parameters for designing LoRA effectively.

- The insights provided by this work can streamline the design process for LoRA, especially when the depth and width of the model in question are specified.

### Weaknesses
The experimental approach raises significant concerns. Given the widespread application of LoRA to various large language models (LLMs), such as LLaMA, there's an opportunity for the authors to substantiate their findings using models tasked with different challenges. Considering the availability of various model sizes in LLaMA and the comprehensive range of results provided by the original LoRA study, a comparison between the proposed theoretical analysis and empirical observations of LoRA would be insightful.

The use of Mean Squared Error (MSE) as a metric in the authors' presentation is questionable. Performance scores for LLMs typically exhibit a weak correlation with perplexity (PPL) or loss values. Therefore, relying solely on MSE for validation, particularly in the context of generative AI, may not adequately address the nuances of expressive capability. A multifaceted evaluation, including different performance metrics, would offer a more robust validation of the claims made in this work.

Additionally, it is acknowledged within the community that even very low ranks (such as 4, 2, or even 1) can yield satisfactory fine-tuning results. Readers would benefit from an exploration into how low-rank adjustments are able to achieve effective fine-tuning. The experimental outcomes presented in the paper currently do not offer practical insights for practitioners working with LoRA-based tuning, who would be looking for such guidance.

The authors are urged to establish a clearer connection between their theoretical discoveries and the empirical results previously reported for LoRA. Doing so could significantly streamline the hyper-parameter selection process for LoRA, reducing the effort required to fine-tune models effectively.

### Questions
Please refer to Weakness comments

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper provides an initial theoretical exploration of the popular parameter-efficient finetuning method LoRA. It proves for fully connected models, LoRA should be sufficient to finetune any base model for a smaller target model with a certain LoRA rank (threshold). They further provide approximation errors for the case when the rank is smaller than the threshold.

### Strengths
This is a theoretically strong paper, studying a very timely topic. While empirically, LoRA has been shown to do surprisingly well, a theoretical explanation for why has been missing. This paper is a good starting point in understanding how/why/when LoRA works.

### Weaknesses
While it is okay to not have them in this paper, I think it would be interesting to study other effects of LoRA theoretically. For example, how does LoRA affect generalization? What can we say about how fast LoRA can converge even if the target model can eventually be found by LoRA exactly.

### Questions
See above.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors conduct theoretical analysis for LoRA, a popular PEFT method for LLMs. For linear models with LoRA,  the “effective rank” is the sum of these low ranks. For multi-layer ReLU FNN, the effective expressive power of LoRA is nearly optimal up to a constant factor of 2. For transformer networks, adding LoRA adapters primarily to the self-attention layers enables the adapted model to exactly represent the target model.

### Strengths
+ The first theoretical analysis to understand the expressive power of LoRA. The first known results on the expressive power of LoRA
+ Linear models, FFNs, and transforms with LoRA are analyzed, providing comprehensive theoretical results.
+ Empirical results matches the rank requirements in theoretical analysis.

### Weaknesses
 + A notation table would help understand all the notations, since the paper is mostly about theoretical proof.

 + A more detailed discussion on the practical implications of the theoretical results would be beneficial. For example, while the paper shows that LoRA can achieve near-optimal expressive power, it does not discuss the trade-offs in terms of training time, memory usage, or generalization performance compared to other PEFT methods or full fine-tuning. It would be helpful to see a discussion on how the theoretical findings translate to real-world scenarios.

 + The analysis of transformer networks focuses on adding LoRA adapters to self-attention layers. It would be interesting to see an analysis of adding LoRA adapters to other parts of the transformer architecture, such as feed-forward networks, and how this affects the expressive power. The paper should also discuss the potential limitations of the current analysis and suggest future directions.

### Questions
In section 2, why a L-layer (instead of one-layer) linear model is considered, which is still a linear model?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
