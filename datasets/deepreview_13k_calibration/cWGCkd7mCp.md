# Efficient Learning with Sine-Activated Low-Rank Matrices

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
Low-rank decomposition has emerged as a vital tool for enhancing parameter efficiency in neural network architectures, gaining traction across diverse applications in machine learning. These techniques significantly lower the number of parameters, striking a balance between compactness and performance. However, a common challenge has been the compromise between parameter efficiency and the accuracy of the model, where reduced parameters often lead to diminished accuracy compared to their full-rank counterparts. In this work, we propose a novel theoretical framework that integrates a sinusoidal function within the low-rank decomposition process. This approach not only preserves the benefits of the parameter efficiency characteristic of low-rank methods but also increases the decomposition's rank, thereby enhancing model performance. Our method proves to be a plug in enhancement for existing low-rank models, as evidenced by its successful application in Vision Transformers (ViT), Large Language Models (LLMs), Neural Radiance Fields (NeRF) and 3D shape modelling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a theoretical framework that integrates a sinusoidal function within the low rank decomposition process to achieve efficient learning. The proposed method was evaluated on several applications such as LLMs parameter efficient fine-tuning, NeRF and 3D shape modeling.

### Strengths
+ The paper provides theoretical justification on benefit of the proposed sine-activated low rank matrices without adding additional parameters.
+ The experimental results show the proposed sine-activated low-rank decomposition works better than the original LoRA.

### Weaknesses
 - The paper talks about the benefits of using a sine function for increasing rank, but it could explain more about why this function was chosen over others and why it works. A discussion of its advantages would strengthen this work.

- While the proposed method is applied across various domains, the paper lacks a comprehensive comparison with existing low-rank approximation techniques. There are many existing LoRA variants and improved versions, e.g. [a] [b].

[a] LoLDU: Low-Rank Adaptation via Lower-Diag-Upper Decomposition for Parameter-Efficient Fine-Tuning
[b] MELoRA: Mini-Ensemble Low-Rank Adapters for Parameter-Efficient Fine-Tuning

- It would be good to provide space and time complexity analysis of the proposed method. 

- There is a lack of quantitative results on a standard dataset for the 3D shape modeling task. It would be good to evaluate the method on other popular tasks such as text to image generation. 

- How do we choose the frequency parameter (ω) in practice? Is there an easy way to adjust it? As per the paper, (ω) higher increases the rank. But do we always pick highest (ω) ? How do we effectively use different frequencies within an interval ?

- For each application, the implementation details of the proposed method should be provided.

- Are there any implementation challenges, like increased computation time during training? Does this technique slow down the model
during inference, especially in environments with limited resources?

### Questions
Please refer to the weakness section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes the introduction of sinusoidal functions within LORAs to improve model performance across a range of tasks. The claim is to be able to balance parameter efficiency and model performance by increasing the rank with sinusoidal functions without adding parameters. The contributions are a theoretical framework, demonstrations of the performance and evaluation on several tasks such as computer vision, 3D shape modeling and NLP. A large part of the paper is the mathematical analysis of low-rank decomposition and the derivation of a non-linear low-rank decomposition as well as showing mathematically why its rank is larger. The supplementary material holds detailed proofs for the propositions and theorems.

### Strengths
- The idea is simple and fascinating. If there are no flaws in the proof, which I didn't find, this has a potential large impact in the domain.
- The mathematical background is well explained, motivated and proven.
- Figures like Figure 2 help in understanding the impact of the method's parameter.
- The method is shown on a variety of very different tasks from classification to Nerf.
- Extreme scenarios are studied like Nerf reconstruction using Lora with rank k=1

### Weaknesses
 - The method is only compared on self-implemented baselines and seems to underperform compared to other improvements in the domain. E.g. One of the citations even mentions DoRA but as an example of application of Lora techniques. They do have results of LLaMA3-8B LoRA which are similar to the results achieved in this paper but with DoRA they improve the performance on commonsense reasoning beyond this paper. When presenting an improved LoRA training technique the authors should compare their performance not only to the vanilla LoRA case but to other techniques like DoRA and ideally implement and evaluate an improved DoRA although I do not see with this specific work how that would be applied. Nevertheless, it seems important state-of-the-art here is missing, which is needed to position the paper in the research landscape.

There are a lot of minor syntax errors or errors in the equations which need to be corrected and do not give a polished impression (See questions)

 Figure 4 in the text is referenced as table 4.

Why is DoRA cited only once as Lora technique but then there is no reference to it's improved performance?

In line 182, and 765 is the A_{ij} \neq 0 maybe a A_{ij \neq 0} ? It looks as if the indexes should not be 0 and not as if the assumption of A \neq 0 is formalized. 

The operator norm in equation 5 has one | too much.

Why is the observation in line 786 important for 11? This should be true in any case.

Line 799 Says Equation equation 13. Probably an issue with cref

The sentence starting in 855 is somehow messed up.

Using parameter counts instead of compression rate in Figure 1 for ViT Classification would improve comparison with other state-of-the-art approaches.

Why does an increased rank improve performance? This point may have been demonstrated by experiments but an intuition could be given. Adding certain noises to the matrix may also increase it's rank without increasing it's parameter count but will probably not lead to improved performance. The link between an increased rank and improved performance could be made clear or hypothesized. Seeing that low-rank adaptation decreases performance may be not sufficient to claim an inverse relationship.

In line 480 I am not sure it is good to speak of overfitting regarding to NeRFs because this sounds as if it's negative when it is the desired behavior.

Figure 10 seems to indicate the frequency parameter has an optimum. How hard is it to choose it? Are the best results retrieved from a grid search or is there any intuition about it's value beforehand?

### Questions
Figure 4 in the text is referenced as table 4.

Why is DoRA cited only once as Lora technique but then there is no reference to it's improved performance?

In line 182, and 765 is the A_{ij} \neq 0 maybe a A_{ij \neq 0} ? It looks as if the indexes should not be 0 and not as if the assumption of A \neq 0 is formalized. 

The operator norm in equation 5 has one | too much.

Why is the observation in line 786 important for 11? This should be true in any case.

Line 799 Says Equation equation 13. Probably an issue with cref

The sentence starting in 855 is somehow messed up.

Using parameter counts instead of compression rate in Figure 1 for ViT Classification would improve comparison with other state-of-the-art approaches.

Why does an increased rank improve performance? This point may have been demonstrated by experiments but an intuition could be given. Adding certain noises to the matrix may also increase it's rank without increasing it's parameter count but will probably not lead to improved performance. The link between an increased rank and improved performance could be made clear or hypothesized. Seeing that low-rank adaptation decreases performance may be not sufficient to claim an inverse relationship.

In line 480 I am not sure it is good to speak of overfitting regarding to NeRFs because this sounds as if it's negative when it is the desired behavior.

Figure 10 seems to indicate the frequency parameter has an optimum. How hard is it to choose it? Are the best results retrieved from a grid search or is there any intuition about it's value beforehand?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the critical need for compact and parameter-efficient architectures in machine learning. While low-rank techniques are a popular solution for reducing model complexity, the authors introduce high-frequency sinusoidal non-linearity functions to enhance the capabilities of low-rank matrices. The paper provides a theoretical framework demonstrating how this modulation increases the rank of matrices without adding extra parameters. This sine-based non-linearity is incorporated into low-rank decompositions, effectively balancing efficiency and performance improvements across various benchmarks, including Vision Transformers (ViT), Large Language Models (LLMs), Neural Radiance Fields (NeRF), and 3D shape modeling.

### Strengths
Task Motivation:
The paper tackles a highly relevant problem—parameter-efficient learning. While overparameterization is effective for generalization, practical deployment in industry necessitates efficient architectures for cost-effectiveness.

Simple Yet Effective Approach:
The introduction of a sine function to augment low-rank decompositions is straightforward but impactful. As shown in Figure 3, the Sine LR method maintains representational power comparable to other activation functions while improving efficiency. The effectiveness of this method is demonstrated across multiple tasks and backbones, including LoRA in LLMs (ROBERTaV3 and LLaMA 3-8B), ViT (ViT-base and ViT-small), NeRF (vanilla NeRF on LLFF), and 3D shape modeling (Thai Statue example).

Technical Soundness:
The theoretical analysis highlights how controlling the frequency coefficient "w" in the sine function affects the linear independence of the original matrix "W". Figure 2 illustrates this effect, showing that the sine-activated low-rank decomposition facilitates efficient training without increasing the number of model parameters.

### Weaknesses
Lack of Rationale Behind the Sine Function's Effectiveness: While the theoretical and experimental validations in Sections 3.2 and 4 establish the efficacy of the sine activation, the paper doesn't delve into why the sine function specifically enhances parameter-efficient training. I'm left wondering what inherent properties of the sine function drive these results. A clearer explanation of how the sine function contributes to increasing matrix rank or improving performance without adding parameters would significantly strengthen the argument. Specifically, the paper lacks a discussion on why the periodic nature of the sine function is beneficial in this context, and how this periodicity interacts with the low-rank structure to achieve the observed performance gains. It would be beneficial to see a more detailed analysis of how the frequency parameter influences the effective rank of the modulated matrix, and how this relates to the optimization landscape.

Hyperparameter "w" Tuning:
The role of the frequency hyperparameter "w" isn't thoroughly addressed. Is there a need to fine-tune "w" for each task, or does it generally benefit from being larger? More importantly, how do we determine the optimal "w"? A systematic exploration or guidelines for selecting "w" across different tasks would be helpful, as the current approach seems to leave this critical aspect underexplored. The paper should provide more insight into the sensitivity of the method to the choice of "w", and whether there are any heuristics or rules of thumb that can be used to guide the selection of this parameter. For example, does the optimal "w" depend on the scale of the input data or the specific architecture being used?


Applicability to CNN Architectures:
Although the paper demonstrates strong results on various architectures like ViT, LLMs, NeRF, and 3D shape modeling, it leaves a gap concerning CNNs. Given that CNNs are still widely used in practice, it would be valuable to explore whether the sine-activated low-rank method can be effectively applied to CNN architectures. A discussion or preliminary results in this area would broaden the paper’s applicability and relevance. Specifically, it is unclear if the proposed method can be easily integrated into the convolutional layers of CNNs, and whether the same performance gains can be achieved as with other architectures. The paper should at least discuss the potential challenges and opportunities in applying this method to CNNs.

### Questions
Please refer the weakness section above.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces concise and elegant improvement method for Low Rank Adaption (LoRA) and reveals its underlying principle by rigorous formula derivation. In addition to fine-tuning large language model, this method can even also achieving competitive results when directly replacing original full-rank weight, which provides some inspiration for model compression. Although there are some parts that I think are slightly lacking in depth, I would suggest accepting it after the following issues are addressed.

### Strengths
This paper introduces concise and elegant improvement method for Low Rank Adaption (LoRA) and reveals its underlying principle by rigorous formula derivation. In addition to fine-tuning large language model, this method can even also achieving competitive results when directly replacing original full-rank weight, which provides some inspiration for model compression. Although there are some parts that I think are slightly lacking in depth, I would suggest accepting it after the following issues are addressed.

### Weaknesses
Advice & Question:
1. In formula 3, why the coefficient w and g are non-learnable ? If learnable, will it cause gradient problem? For the same model, has it been considered to provide different w and g for different linear layers? Can the recommended values for these two be provided?
2. Since other nonlinear functions are almost useless, why not directly give the sine function in Equation 3?
3. Regarding the right diagram in Figure 3, I don't think we can see a trend of the matrix rank increasing with the increase of frequency w. Because the rank of a matrix is only related to the number of nonzero singular values. So when w is 200 and 400, it seems that the ranks of the two are almost equal.
4. In the setting of section 4.1, why do not implement low-rank adaptations on all linear modules of LLM?
5. Does the rank of the decomposed matrix necessarily be less than that of the original matrix regardless of how the frequency is adjusted?

### Questions
Advice & Question:
1. In formula 3, why the coefficient w and g are non-learnable ? If learnable, will it cause gradient problem? For the same model, has it been considered to provide different w and g for different linear layers? Can the recommended values for these two be provided?
2. Since other nonlinear functions are almost useless, why not directly give the sine function in Equation 3?
3. Regarding the right diagram in Figure 3, I don't think we can see a trend of the matrix rank increasing with the increase of frequency w. Because the rank of a matrix is only related to the number of nonzero singular values. So when w is 200 and 400, it seems that the ranks of the two are almost equal.
4. In the setting of section 4.1, why do not implement low-rank adaptations on all linear modules of LLM?
5. Does the rank of the decomposed matrix necessarily be less than that of the original matrix regardless of how the frequency is adjusted?

### Soundness
3

### Presentation
2

### Contribution
2
