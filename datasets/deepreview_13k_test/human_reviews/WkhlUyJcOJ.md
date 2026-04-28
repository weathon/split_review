# Less is More: Extreme Gradient Boost Rank-1 Adaption for Efficient Finetuning of LLMs

- Decision: Reject
- Scores: 5, 6, 5, 8, 6

## Abstract
Fine-tuning Large Language Models (LLMs) has become a crucial technique for adapting pre-trained models to downstream tasks. However, the enormous size of LLMs poses significant challenges in terms of computational complexity and resource requirements. Low-Rank Adaptation (LoRA) has emerged as a promising solution. However, there exists a gap between the practical performance of low-rank adaptations and its theoretical optimum. In this work, we propose eXtreme Gradient Boosting LoRA (XGBLoRA), a novel framework that bridges this gap by leveraging the power of ensemble learning. Inspired by gradient boosting, XGBLoRA iteratively learns and merges a sequence of LoRA adaptations to refine model predictions. It achieves better performance than the standard LoRA, while enjoying the computational efficiency of rank-1 adaptations. We provide theoretical analysis to show the convergence and optimality of our approach, and conduct extensive experiments on a range of natural language processing tasks. The results demonstrate that XGBLoRA consistently outperforms standard LoRA and achieves performance comparable to full fine-tuning with significantly fewer trainable parameters. This work advances parameter-efficient fine-tuning for LLMs, and offers a promising solution for adapting LLMs to downstream tasks while optimizing performance and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper gives a novel framework that enhances LoRA through ensemble learning, bringing it closer to theoretical optimality. The proposed method’s convergence is demonstrated through detailed theoretical analysis. Comprehensive experiments reveal the relationship between the number of weak learners and model performance. Additionally, XGBLoRA outperforms traditional LoRA and many baseline methods across multiple tasks while significantly reducing the number of trainable parameters and memory usage.

### Strengths
1. It is a good idea to use gradient boosting in LoRA finetuning, and the results showed that the idea is valid.

2. The concepts in the paper are clear and understandable. This paper has a well-organized structure that effectively conveys the authors’ ideas.

3. This paper provides detailed theoretical analysis and proofs.

### Weaknesses
1. In Lines 251-256, could frequent merging introduce additional overhead? This part lacks quantitative analysis.

2. Line 413 mentioned that the hyperparameters refer to LoRA[1], but to my knowledge, multiple sets of hyperparameters were provided, which seems ambiguous. Moreover, I am uncertain if the hyperparameters for RoBERTa and GPT-3 are suitable for the current models.

3. In Table 5, the performance improves as the rank decreases. Could this be due to the simplicity of the data, which fails to allow for sufficient fitting?

4. Alpaca is an excellent project; however, the dataset is relatively simple (despite being regenerated with GPT-4). Meanwhile, base models such as LLaMA3-8B and Mistral exhibit strong performance. Based on my experience, fine-tuning a highly capable base model with a lower-quality dataset can lead to model degradation.

	(a) From the existing leaderboards[2], LLaMA3-8B has achieved 66.49% accuracy on MMLU, it is even higher than the best value in Table 4. To avoid discrepancies due to evaluation methods and code versions, could you provide the performance of base models like LLaMA3-8B and Mistral on 8 tasks?

	(b) The Alpaca GPT-4(en) dataset differs significantly from the currently popular instruction fine-tuning datasets. Could you share results from other datasets like WizardLM[3], Infinity-Instruct [4] ?

[1] https://arxiv.org/pdf/2106.09685

[2] https://huggingface.co/spaces/open-llm-leaderboard-old/open_llm_leaderboard

[3] https://huggingface.co/datasets/WizardLMTeam/WizardLM_evol_instruct_70k

[4] https://huggingface.co/datasets/BAAI/Infinity-Instruct

### Questions
Please refer to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel, efficient fine-tuning method for LLMs, XGBLoRA, inspired by gradient boosting. XGBLoRA randomly samples a subset of layers for rank-1 adaptation at each training step, significantly reducing the parameters required per step. XGBLoRA outperforms standard LoRA while using less GPU memory.

### Strengths
- The paper is clear and easy to understand, effectively explaining the ideas.
- The paper also presents a straightforward, efficient fine-tuning method that achieves state-of-the-art results with fewer parameters across various benchmarks.
- The theoretical analysis provided by the authors supports the method's expressiveness power.

### Weaknesses
- A significant limitation of the paper is that the reduction in trainable parameters does not significantly decrease GPU memory usage and training time. Furthermore, the frequent merging operations compromise LoRA's plug-and-play nature (efficient model storage), making the "Params" axis in Figure 1 misleadingly optimistic. Specific limitations include:
  - In Table 1, the computational cost for the base model $\beta$ appears higher than $\alpha$, suggesting that XGBLoRA does not significantly reduce the total cost. As shown in Figure 5, the difference in wall-clock time between 0.64s and 0.62s is minimal.
  - The optimization of an unstable subset of parameters in XGBLoRA adds complexity to the training pipeline, potentially slowing convergence. It would be beneficial to compare different total training steps $K$.

- There are minor errors in the Figures and Tables:
  - In Figure 4, the x-axis should be labeled $\kappa$ instead of $K$.
  - In Figure 5, the x-axis should be labeled as XGBLoRA, not GBLoRA.
  - In Table 5, bolded entries under Other, SIQA, and ARC-e columns are not optimal.
  - In Table 6, bolded entries under Social and Other columns are not optimal.

### Questions
- **Related work**: The paper omits a significant related work, COLA [r1], which also employs residual learning. Please provide a brief comparison of the key methodological differences between XGBLoRA and COLA, as well as to include COLA in their experimental comparisons if feasible.

    [r1] Xia, Wenhan, Chengwei Qin, and Elad Hazan. "Chain of lora: Efficient fine-tuning of language models via residual learning."

- **Theoretical justification**: The paper mentions that for LoRA, "To fit any target matrix, the rank of the adaptation must satisfy (r ≥ embedding_size/2)." For XGBLoRA, the paper presents Theorem 2. Please provide a more detailed explanation of how Theorem 2 demonstrates the expressiveness advantages of XGBLoRA over LoRA, particularly in relation to the trade-off between rank r and iterations T. And how to ensure consistent total training times between XGBLoRA and LoRA in the theoretical analysis.


Post-Rebuttal:

After reviewing author responses, all concerns are addressed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes XGBLoRA, a low-rank adaptation method based on ensemble learning. It trains LoRA Adapters iteratively.

### Strengths
1. Interesting idea.
2. Comprehensive experiment.

### Weaknesses
I will raise my score if the authors could address my concerns, especially weakness 3.
1. Figure 1 is not mentioned in the manuscript.
2. The motivation is poor and insufficient. In other words, any method could be considered a product of this motivation. Moreover, the motivations in the introduction (Line 66-69) and the abstract (15-16) are not consistent.
3. I believe the parameter comparison of XGBLoRA with other methods is unfair. While it’s true that XGBLoRA requires fewer GPU resources, this does not mean the number of parameters it trains is significantly smaller than other methods. In some cases, the number of parameters required by XGBLoRA should actually exceed that of LoRA. Compared to a method, XGBLoRA is more like a training approach. In other words, one could also train LoRA’s parameters in stages, which would also allow it to “use a minimal number of parameters”.
Note that this weakness is related to Question 3.

### Questions
1. Line 58, what are rank_r and embedding_size? What does “much smaller ranks” in Line 59 refer to?
2. Actually, I don’t quite understand what is meant by “theoretical optimum” (Line 61). Does this refer to better performance corresponding to a higher rank? And what is the “performance gap” (Line 68)? Does it refer to the difference in performance between low-rank and high-rank?
3. How to store the trained weights of XGBLoRA?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a method to improve LoRA, by posing the fine-tuning as a gradient boosting where randomly selected rank-1 LoRA matrices are used as weak learners. This method achieves better results than LoRA, with fewer parameters, less memory footprint and better speed per batch.

### Strengths
* The authors tackle an important and meaningful topic that would be of interest to the community. PEFT is gaining more and more attention as the size of language models continues to grow.

* The results are impressive.

* Memory footprint is better, less trainable parameters, and better speed.

### Weaknesses
* Equation (7): In the first part of the equation, all components are fixed: the label y_i and the previous iteration of the model. Where is the current iteration prediction? Where is the residual part?

* In line 252, double ‘the’.

* Line 383, is it ‘1000%’ or ‘100%’? Same for line 447.

* Line 497, is it ‘GBLoRA’ or ‘XGBLoRA’?

### Questions
* Line 324, it is called here ‘Lemma 1’, while later on in the appendices it is called ‘Lemma 4’?

* In line 327, I assume the definition of L() is the loss of the model, given the weights? Furthermore, matrices A,B are defined earlier on with superscript and subscript. Here they are with two superscripts. Can you add a definition explanation?

* Line 347, where is L* defined?*

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes XGBLoRA to bridge the gap between LoRA and FT by leveraging gradient boosting. This approach achieves high performance and low complexity, as shown in Figure 1. The authors demonstrate the empirical performance through extensive experiments, including various benchmarks and comparison baselines. The convergence guarantees and approximation error bounds are also justified.

### Strengths
1. The presentation is clear and easy to follow.
2. The approach refines the pre-trained weight matrix progressively, with the original LoRA as a special case, which makes sense and is novel to me.
3. The proposed approach is justified both empirically and theoretically.
4. The influence of each hyperparameter, such as $k$ and rank, is illustrated in the experiments.

### Weaknesses
1.  The idea of ensemble learning has been used for LoRA before, like MELoRA, which the authors have already included in the experiments. I encourage the authors to include a discussion about ensemble learning for LoRA in the Related Work section and highlight the differences.
2. Is the hyperparameter setting robust across different base models and datasets? For example, Table 6 shows that $L_s = 11$ gives the best performance for LLaMA3-8B on the MMLU benchmark; does it hold for other setups? The same question applies to $k$. If the performance significantly depends on the hyperparameters, extra effort would be required for hyperparameter search, which could be a weakness of XGBLoRA.
3. The authors state, "...leading to better generalization performance without explicitly adding regularization terms to the loss function..." on page 6, line 300. However, in equation (7), regularization terms on the norms of $A$ and $B$ are explicitly used. Whether these regularization terms have an influence is not verified in the experiments.

**Minor comments**

1. Page 5, Line 252: "set the the number of" -> "set the number of"
2. Page 5, Line 269: "the the expressiveness" -> "the expressiveness"

### Questions
1. Does the learning rate $\alpha_t$ used in equation (8) have a big influence? It seems to me that a constant $\alpha_t = 1$ may not be the best choice.

### Soundness
3

### Presentation
3

### Contribution
3
