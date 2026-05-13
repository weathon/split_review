# A Reparameterized Discrete Diffusion Model for Text Generation

- Decision: Reject
- Scores: 6, 3, 5, 8

## Abstract
This work studies discrete diffusion probabilistic models with applications to natural language generation. We derive an alternative yet equivalent formulation of the sampling from discrete diffusion processes and leverage this insight to develop a family of \textit{reparameterized discrete diffusion models}. The derived generic framework is highly flexible, offers a fresh perspective of the generation process in discrete diffusion models, and features more effective training and decoding techniques. We conduct extensive experiments to evaluate the text generation capability of our model, demonstrating significant improvements over existing diffusion models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper addresses the challenge of applying discrete diffusion probabilistic models to natural language generation. The authors propose a novel reparameterized discrete diffusion model (RDM) by re-examining the sampling process from discrete diffusion models. They introduce a route-and-denoise process that includes a stochastic routing mechanism, which makes the training more efficient by simplifying the training objective to a reweighted standard cross-entropy loss. This new family of models, RDMs, demonstrates significant improvements in terms of effectiveness and flexibility over existing diffusion models in text generation tasks.

The RDMs achieve high-quality text generation by offering a more effective training and decoding process, which can be highly flexible and adaptive. The model's performance is evaluated across various text generation benchmarks, showing superior results over both existing discrete and continuous diffusion models while operating several orders of magnitude faster. This work pushes the boundaries of non-autoregressive text generation, providing a fresh perspective on the discrete diffusion approach and opening pathways for further research and application in more complex language tasks.

### Strengths
Advantages:
 - Improved Training and Decoding Techniques Allows Efficient and Effective Non-autoregressive Generation: The RDM incorporates improved training and decoding strategies that significantly enhance performance over vanilla baselines. The derived loss objective, formulated as a reweighting cross-entropy function, and the discriminative routing mechanism for decoding are highlighted as key contributors to this performance boost.
 - Solid Performance on Machine Translation Experiments: RDM achieves a milestone-level performance as a diffusion-based Machine Translation model with either competititive or superior performance compared to previous Non-autoregressive translation models.

### Weaknesses
Disadvantages:
 - Limited Comparison: I always think the comparison between text diffusion models and other important non-autoregressive models is important. This is not only because of the concerns for a fair and thorough comparison. This is more because of the fact that such non-autoregressive models **are** text diffusion models that has a diffusion process defined as operating the discrete tokens. Levenshtein Transformer, for example, is cited yet not quite compared in many of the experiments, which limits the soundness of the experiments. I encourage the authors to add them in (many of the results can actually be directly borrowed from their original paper I think).

- Limited Choice of Tasks that Raises Concerns of Overclaiming: This method is now mostly tested on semantically deterministic tasks like Machine Translation. There's still a very huge gap between getting the model to function on MT tasks and getting it to produce diverse, informative outputs on open-domain text generation tasks. With this concern, I would tend to suggest the authors to claim smaller, to restrict the claim to be a diffusion-based machine translation model instead of claiming it as a diffusion-based text generation model.

### Questions
Is it possible to also conduct a running time study to compare RDM with other non-autoregressive models? Currently only previous diffusion sequence models and CausalLM baselines are compared. This comparison can sometimes be tricky because many irrelevant factors like the quality of implementation also impacts the running time. But I would be more convinced about the practical value if I see such results in the experiment section (since the model itself is already falling short in terms of #refinements compared to LevT, but if each refinement with RDM is computationally cheaper, there's still a chance for RDM to be faster)

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This research delves into discrete diffusion probabilistic models, specifically focusing on their applications in conditional natural language generation. The study introduces an innovative and equivalent approach for sampling anf training from discrete diffusion processes. This novel framework provides a fresh perspective on the generation process within these models and incorporates more effective training and decoding techniques. Extensive experiments are conducted to assess the text generation capabilities of this model.

### Strengths
This paper introduces a novel framework for discrete diffusion probabilistic models. It presents a comprehensive array of experiments conducted on conditional NLP datasets, showcasing significant enhancements compared to existing diffusion models.

### Weaknesses
The main critique of this paper centers on its narrow experimental scope, concentrating solely on conditional text generation tasks such as machine translation, question generation, and paraphrasing. This focus is somewhat limiting, particularly given the absence of experiments on unconditional text data. This omission is notable, especially considering the extensive body of prior work in this area, including significant contributions by Austin et al. (2021) and Hoogeboom et al. (2022b), who have extensively explored these scenarios.

This paper, although introducing a new formulation and reparameterization of discrete diffusion models, primarily builds upon existing frameworks. The use of discrete diffusion processes for text generation is not entirely novel, and the proposed modifications could be considered incremental improvements to established methods.

### Questions
1. How does your proposed method perform on established conditional NLP datasets, such as enwik8 and text8, as previously tested in well-regarded papers (Hoogeboom et al., 2021 and Austin et al., 2021)?

2. To what degree does the quality of your text generation process rely on the choice of your training objective during the training phase? If you were to employ the loss functions utilized in Hoogeboom et al., 2021 and Austin et al., 2021 to train your diffusion model, how would this impact the quality of the generated text?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a reparameterization approach for discrete diffusion models applied to text generation tasks. By introducing two additional variables to process noisy and original inputs separately, the proposed method aims to improve the performance of discrete diffusion models. The experiments are conducted on machine translation, question generation, and paraphrasing tasks, demonstrating improvements over baseline discrete diffusion models.

### Strengths
- The paper attempts to provide a new perspective on discrete diffusion models by introducing a reparameterization approach, which could potentially lead to better results in text generation tasks.

- The experiments conducted cover a variety of text generation tasks and show improvements over the baseline discrete diffusion models.

### Weaknesses
 - The motivation behind the proposed method is not clearly explained, and the paper lacks a solid theoretical foundation to support the reparameterization approach. The reasoning behind dividing the diffusion of tokens into two conditions by comparing with the original input is not well-justified. Specifically, the paper does not provide a clear mathematical derivation or proof demonstrating that the proposed reparameterization is equivalent to the original diffusion process, nor does it rigorously explain why separating the routing and denoising steps should lead to improved performance. The lack of a formal analysis makes it difficult to assess the theoretical validity of the approach.

- The proposed method appears to borrow heavily from masked language modeling techniques that have already been utilized in non-autoregressive text generation works, such as CMLM, DisCo, and others. Furthermore, existing discrete diffusion models like improved VQ-Diffusion have proposed advanced models that consider each token separately, making the contribution of the proposed method less novel and impactful. The paper does not adequately differentiate its approach from these existing methods, particularly in terms of the specific mechanisms that lead to performance gains. The reparameterization, while presented as a novel contribution, seems to be a variation of existing techniques, and the paper does not provide a clear explanation of its unique advantages.

- The performance improvements demonstrated by the proposed method over the discrete diffusion baseline are not consistent across different tasks and metrics. This raises concerns about the generalizability and robustness of the proposed method for various text generation tasks. The paper should include a more detailed analysis of the performance variations, including a discussion of the factors that might contribute to these inconsistencies. For example, it is unclear why the proposed method performs better on some tasks but not others, and the paper lacks a thorough investigation of these differences.

- The choice of baselines and metrics for comparison in the experiments could be more appropriate. For example, in Figure 2 (b), the comparison with Diffuseq, a continuous baseline, is not suitable, and the performance of Diffuseq is not well-explained. Moreover, the paper does not follow the experimental settings of CMLM, which achieves higher performance in their original paper. The comparison with a continuous model is not a direct comparison and does not provide a clear understanding of the proposed method's performance relative to other discrete diffusion models. The lack of consistent experimental settings with CMLM makes it difficult to assess the true performance of the proposed method.

- The paper does not provide an in-depth analysis of the discrepancy between training and inference introduced by the proposed method. The decoding method presented is similar to existing mask-predict and easy-first policies applied in non-autoregressive or diffusion models, raising questions about the novelty and effectiveness of the proposed approach. The paper does not address the potential issues that may arise from the difference between the training and inference procedures, nor does it provide a detailed analysis of the decoding method's impact on the overall performance.

- The paper does not include a comprehensive ablation study to demonstrate the effectiveness of the proposed method and its individual components. A detailed ablation study could provide insights into the contribution of each component to the overall performance improvements. The paper should include a more thorough investigation of the individual components of the proposed method to understand their specific contributions to the overall performance.

- The experiments in the paper focus mainly on conditional text generation tasks, where a source input is provided. It remains unclear whether the proposed reparameterization approach can also enhance performance in other text generation tasks, such as unconditional language modeling, limiting the potential impact and generalizability of the method. The paper should include experiments on unconditional text generation tasks to demonstrate the general applicability of the proposed method.

### Questions
Please refer to weaknesses for the questions.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper develops a novel framework for discrete diffusion models. In particular, they develop an adaptive routing strategy that routes tokens to the denoised state only if the router outputs high scores instead of uniformly processing all the tokens.  And extensive experiments have been conducted to evaluate the text generation capability of their model, demonstrating significant improvements over existing diffusion models

In my opinion, this is a novel work that divides the generative process into two processes, consisting of a noise token and an unnoise token. Generally, if the state is a noise token, the generative process selects to denoise with a neural network. If the state is an unnoise token, the generative process selects to add noise. Compared with the base diffusion model, this method reduces the generative difficulty of the generative network, which only needs to take denoise tasks.   From another principle, the method can be seen as a decoupling method that makes the nework not need to learn two tasks (add noise and denoise) at the same time.

### Strengths
1) This paper proposes a novel framework for the discrete diffusion model, and it is well written and easy to understand, although it has many mathematical

2) This paper provides us with new insight into the diffusion model.

3) This work gets effective performance with extensive experiments.

### Weaknesses
Can you take more experiments on different length language datasets that is aimed at exploring  model performance boundaries? In my opinion, the diffusion model hard to generates a longer sequence than the auto-agressive language model

why the recursive computation for b_t is effective; I'm confused on it.

### Questions
Is it simple to adapt this method to other diffusion models, such as the Gaussian diffusion model? If not, why?


why the recursive computation for b_t is effective; I'm confused on it.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
