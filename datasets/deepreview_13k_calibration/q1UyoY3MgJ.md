# Rethinking Invariance in In-context Learning

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
In-Context Learning (ICL) has emerged as a pivotal capability of auto-regressive large language models, yet it is hindered by a notable sensitivity to the ordering of context examples regardless of their mutual independence. To address this issue, recent studies have introduced several variant algorithms of ICL that achieve permutation invariance. However, many of these do not exhibit comparable performance with the standard auto-regressive ICL algorithm. In this work, we identify two crucial elements in the design of an invariant ICL algorithm: information non-leakage and context interdependence, which are not simultaneously achieved by any of the existing methods. These investigations lead us to the proposed \emph{Invariant ICL (InvICL)}, a methodology designed to achieve invariance in ICL while ensuring the two properties. Empirically, our findings reveal that InvICL surpasses previous models, both invariant and non-invariant, in most benchmark datasets, showcasing superior generalization capabilities across varying input lengths.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new permutation-invariant attention mechanism InvICL, which is adapted from Bag-of-Example (BoE) but admits full context-interdependnce. The authors enable the context interdependence by duplicating the context examples and allowing leave-one-out (LOO) attention from the duplicated tokens to original tokens. By doing so, IncICL enjoys the properties of (i) permutation-invariant, (ii) information non-leakage, (iii) context interdependence. Evaluations show that InvICL outperform baselines (Prefix, AR, BoE, NoPE) on tasks that adimit a permutation-invariant nature.

### Strengths
The idea is novel and interesting. The motivation is clear as InvICL is proposed by the desired three properties.

### Weaknesses
1. Experiment results need more analysis and interpretations. The authors find InvICL shows better length-generalization capabilities, whose mechanism is unclear to me. Specifically, while the paper claims improved length generalization, it lacks a mechanistic explanation of why the proposed architecture achieves this. The observed performance gains could be due to various factors, and the paper does not sufficiently isolate the contribution of the permutation-invariant attention mechanism. A more detailed analysis, perhaps through ablation studies or visualizations of attention patterns, would be beneficial to understand the underlying reasons for the improved generalization.

2. More experiment results needed. Most results do not have a  reported std. Besides, it would be benificial if there is a figure of squared error curves where the x-axis is the training epochs. Currently there are only results from 50k and 200k epochs. The absence of standard deviations makes it difficult to assess the statistical significance of the results. Furthermore, the limited number of training epochs reported prevents a thorough understanding of the learning dynamics. It is crucial to observe the training curves to determine if the model is converging and to compare the learning rates of different methods. The lack of these details makes it difficult to draw firm conclusions about the effectiveness of the proposed approach.

3. The results of Prefix ICL for linear regression are a bit weird to me. The reported squared error seems to fairly high (around 0.5) even when the number of examples is 40. In another paper [1], the reported squared errors are much lower than 0.1 for 5-layer transformers with number of context examples 10 and data dimension 10. The discrepancy in performance compared to [1] raises questions about the experimental setup and the implementation of Prefix ICL. It is important to clarify the differences in experimental settings that might lead to such different results. It would be helpful to investigate whether the high error is due to specific choices in the model architecture, training procedure, or data generation process.

### Questions
1. Is the loss taken over only the test token or all tokens (autoregressive loss) in the input for Prefix ICL in the training stage? If it is the latter, then it does not make too much sense since for Prefix ICL the context example can attend to its label directly.

2. Can the test token attend to itself in authors' implementation in Prefix ICL for linear regressions? From figure 2 it seems to be attending to itself, but I am not sure if that is the case in the experiments. Other papers [1, 2] using Prefix attention avoid such attention since it could provide incorrect signals to multilayer transformers (the corresponding $\hat y$ is inaccurate within the forward passes).

3. Does the positive encoding in the footnote of page 1 refer to positional encoding?


[1] Johannes von Oswald, Eyvind Niklasson, Ettore Randazzo, João Sacramento, Alexander Mordvintsev, Andrey Zhmoginov, Max Vladymyrov. Transformers Learn In-Context by Gradient Descent. ICML 2023.

[2] Kwangjun Ahn, Xiang Cheng, Hadi Daneshmand, Suvrit Sra. Transformers learn to implement preconditioned gradient descent for in-context learning. NeurIPS 2023.

### Soundness
2

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
This paper presents InvICL, a new approach to in-context learning that achieves three key properties: permutation invariance, information non-leakage, and context interdependence. The authors propose a parallel implementation using a duplicated input sequence and modified attention patterns. They provide a theoretical analysis showing that InvICL approximates standard gradient descent and demonstrates improved performance over baseline methods (GPT-2 Large 762M, GPT-Neo 2.7B, Pythia-2.8B). The work tries to understand and improve in-context learning, though there are some practical concerns.

### Strengths
- The paper identifies and formalizes three important properties for ICL that weren't previously unified. The authors demonstrate why these properties matter. 
- The theoretical analysis is simple but straightforward. The authors prove that InvICL approximates standard gradient descent (Theorem 4.1) and show how this leads to better convergence properties compared to other ICL variants.
- The experimental results look interesting. The method shows strong performance across multiple settings - synthetic tasks (Figure 3), out-of-distribution scenarios (Figure 7), and real-world datasets (Table 2).

### Weaknesses
 - The practical applicability of the method raises some concerns. The paper relies on MetaICL finetuning, which is computationally expensive for modern large language models. I wonder if there are any training-free methods. 
- The efficiency implications are concerning. Doubling the input sequence length (as shown in Figure 2d) increases memory usage. In Section 5.2, “We find that when the inputs size of the GPT-2 Large model increases from 512 to 1024, the GPU memory overhead increases by 14% (from 4.2 GB to 4.8GB)”. However, when the context is long, e.g., 64k, the overhead will be super large. Moreover, the attention pattern used likely makes it incompatible with FlashAttention optimizations, which could further impact practical deployment. The specific attention mask used by InvICL, which enforces permutation invariance, likely prevents the use of standard optimizations such as block-sparse attention, which could mitigate the memory overhead. This makes the method less practical for long sequences.
- The experimental setup feels somewhat dated by using GPT-2 Large as the primary model. While the authors include some results with GPT-Neo 2.7B and Pythia-2.8B in the appendix, evaluating more recent models like Phi-3.5 or Llama 3.2 would better demonstrate the method's relevance to current architectures. The choice of GPT-2 Large as the primary model, given its age and relatively small size, makes it difficult to assess the scalability and relevance of the proposed approach to modern large language models.
- There are some inconsistencies in the presentation. Figure 1 shows results for PCW while Table 1 uses different terminology (Inv ICL), making it difficult to track the method comparisons. It confuses me to understand the relative performance of different approaches.

### Questions
How would InvICL perform in few-shot settings without MetaICL finetuning? This would be particularly relevant for scenarios where finetuning isn't practical.

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
4

### Summary
The paper presents a new method to achieve higher performance out of In-Context Learning with no additional model training. It presents conditions under which a well defined notion of invariant In-context learning should perform well highlighting the gap in prior works that this paper fills with its proposed method. The paper gives theoretical and empirical justification for the superiority of its method.

### Strengths
- The paper presents a clear step up in terms of theoretical ideas as well as empirical evidence of improvement compared to prior works attempting to optimize ICL.
- Paper is very well written, clearly presents and distinguishes its contribution.
- Although the method requires more computation in theory, the authors achieve parallelism and same order of computation as standard ICL with a smart trick. The authors also talk about the additional memory requirements. [Point being that the paper addresses a plethora of relevant points surrounding its method].

### Weaknesses
 **The significance of section 4 and section 5.1 are unclear.** Please see this [ICML 2024 paper](https://arxiv.org/abs/2310.08540) that talks about how training transformers with ICL objective may be incompatible with real ICL in LLMs that do not train explicitly for ICL with fixed ICL prompt format.
- Theorem 4.1 shows that if we put weight matrices in a particular format, we can simulate InvICL with transformers. But, is there reason to believe that trained transformers end up with similar weights? The theorem seems to be an existence proof, but the paper does not discuss the practical implications of this theoretical result, especially for pre-trained models that are not trained with an ICL objective.
- Similarly, results from section 5.1 assume that transformers are trained with ICL objective, which is not true for LLMs. The experiments in this section, therefore, do not reflect the behavior of real-world LLMs and their ICL capabilities. The paper should clarify the limitations of these experiments and their relevance to practical applications.

I believe these points merit a discussion in the paper.

### Questions
- **Definition 3.3**: if j > i, and this condition still holds, then isn’t it sort of contradicting information non-leakage (not technically with your definition as it only requires non-leakage to the corresponding label; but in my opinion, if an x_i can influence another x_i or y_i later in the sequence, it should count as information leakage)? Should the condition be j < i instead of j \neq i? This is intuitively the case for AR LLMs because they only depend on previous context and you have mentioned it in point 3 (“These examples provide the context for better encoding of x_i, which in turn improves the prediction of future examples when x_i serves as their context.”) Why is context interdependence important, or why should I believe that context interdependence should be useful/necessary for AR LLMs, when they can not attend to future demonstrations?
- External modification of attention masks (through aggregation via BoE) is a deviation from how these models are trained to read those activations. How do you think this impacts the model’s internal representations? What could be the effects on predictions apart from pure performance numbers (like does it increase hallucination)? Would like to see some discussion or simple experiment along this line.

PS: I hope to increase my rating if the authors make an effort to discuss my concerns.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes InvICL, a new invariant ICL algorithm that satisfies not only invariance, but also information non-leakage and context interdependence. Then the authors provide both theoretical and empirical evidence to prove the effectiveness of the proposed algorithm on ICL.

### Strengths
- The paper is overall well written and well presented. 
- The paper present reasonable desiderata for ICL algorithms, and the proposed method complements prior works on those criteria.
- The paper present some theoretical intuition on why the proposed method should work better than its counter parts.
- Authors conduct various experiments to prove the effectiveness of the proposed algorithm.

### Weaknesses
 - One might view the proposed method as concatenation of the prior works (PrefixICL and (variant of) PCW)
- As with the previous works, it lacks connection with *actual* ICL performed by LLMs.
- Although the inference time of InvICL does not differ much from AR ICL, is it also true for training? To my understanding, in InvICL (and other invariant ICL algorithms), $\hat{g}(x_i)$ and $\hat{g}(x_{i+1})$ cannot be computed on one forward pass. 
- For real-world dataset experiments, is AR ICL also fine-tuned on ICL tasks? If not, comparing ICL specific fine-tuned model and general LLM on ICL tasks seems unfair.

### Questions
- Even with InvICL, is there a *learning plateau* during training?
- If we actually train with InvICL, does the weight matrices aligns with Theorem 4.1?
- Why is adding only symmetric positional embedding not beneficial?

### Soundness
4

### Presentation
4

### Contribution
3
