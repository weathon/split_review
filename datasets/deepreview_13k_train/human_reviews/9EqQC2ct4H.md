# An Efficient Framework for Crediting Data Contributors of Diffusion Models

- Decision: Accept
- Scores: 5, 8, 5

## Abstract
As diffusion models are deployed in real-world settings and their performance driven by training data, appraising the contribution of data contributors is crucial to creating incentives for sharing quality data and to implementing policies for data compensation. Depending on the use case, model performance corresponds to various global properties of the distribution learned by a diffusion model (e.g., overall aesthetic quality). Hence, here we address the problem of attributing global properties of diffusion models to data contributors. The Shapley value provides a principled approach to valuation by uniquely satisfying game-theoretic axioms of fairness. However, estimating Shapley values for diffusion models is computationally impractical because it requires retraining and rerunning inference on many subsets of data contributors. We introduce a method to efficiently retrain and rerun inference for Shapley value estimation, by leveraging model pruning and fine-tuning. We evaluate the utility of our method with three use cases: (i) image quality for a DDPM trained on a CIFAR dataset, (ii) demographic diversity for an LDM trained on CelebA-HQ, and (iii) aesthetic quality for a Stable Diffusion model LoRA-finetuned on Post-Impressionist artworks. Our results empirically demonstrate that our framework can identify important data contributors across global properties, outperforming existing attribution methods for diffusion models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a framework for attributing the contributions of data providers in diffusion models. The authors propose a framework that efficiently approximates retraining and rerunning inference for diffusion models, thus enabling the estimation of Shapley values for data contributors. This is achieved by investigating how global properties of diffusion models are influenced by data contributors. Empirically, it is demonstrated that the proposed framework outperforms existing data attribution
methods across three datasets, model architectures, and global properties.

### Strengths
Overall, I think this paper is organized and written clearly and I enjoyed reading most of the parts. In particular, the conceptual strengths of this paper include:
1. The proposed framework utilizes Shapley values, a game-theoretic approach, to assign fair credit to data contributors based on their influence on model performance. This methodology uniquely meets the fairness principles in valuation.
2. To address the high computational cost of Shapley value calculations, the paper introduces a model-pruning and fine-tuning method, which significantly accelerates retraining and inference processes. 
3. The approach has the potential to be applicable in various scenarios, such as incentivizing quality data sharing, creating compensation policies, and improving model diversity and fairness, making it a nice tool for real-world diffusion model deployments​.

### Weaknesses
1. despite the computational efficiency of the proposed speed up method with sparsified fine-tuning (section 3.2), it seems to me that there is no in-depth discussion about its accuracy. The core idea of the approximation is Eq. (6), but there is no discussion or empirical evidence to support how well the approximation (6) is. Given that the idea is straightforward, it would be much more convincing if the author can provide additional justifications for Eq. (6), besides its superior empirical performance compared to baseline methods. Otherwise, it is difficult to digest why the proposed approach outperforms other methods with such a dominant advantage (Table 1).  
2. I do not see any particular reason the approximation for computing Shapley value has to be restricted in the diffusion model applications. Whether this is true or not, it would be better to include additional discussions in this regard.
3. I feel the contributions summarized at the end of the introduction is a bit over-claimed. For example, the first claimed contribution is not surprising from my perspective, as it is well-acknowledged that the performance of any ML model relies heavily on the sources of its training data set. For the second claim, I'm not so sure what does "efficiently approximate" mean. From the paper I get that the proposed approximation framework indeed reduces the computational efficiency of solving the least square problem (5), however, there is no evidence of how well the approximation is. In my opinion, an "efficient" approximation should somehow provide a trade-off between computational cost and approximation accuracy. That said, an approximation method with only a computational cost guarantee makes it less convincing and lacks insight. I think this paper can benefit more from an in-depth discussion of the proposed approximation approach. 
4. the focus of technical writing is not well-balanced. In my opinion, the entire section 2 and section 3.1 are known results (which do not contribute to the novelty of this work) and should be shortened significantly. However, unfortunately, the core novel part of the proposed method (section 3.2) is not discussed in depth.

### Questions
1. in definition 1, you said the function $\tau(\mathcal{F}, \\{C_i\\}_{i=1}^n)$ is supposed to assign a score to each contributor $i$. I'm wondering how this notation reflects this idea. Maybe it's a typo and it should be $\tau(\mathcal{F}, C_i)$?
2. if I understand it correctly, in the experiment results (section 4.5), the LDS is computed with different baseline methods for computing $\tau$. Then how are $\{\mathcal{F}(\theta^*_{S_b})\}_{b=1}^B$ computed? Are they computed by Sparsified-FT Shapley? If this is the case, why it is a fair comparison if the proposed approach is served as the benchmark in the evaluation metric?
3. is the proposed approach applicable to any data-driven machine learning model? I don't see any reason why it must be restricted to the diffusion model. If this is the case, why this paper focus on the application of diffusion models?

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
4

### Summary
The paper entitled "An Efficient Framework for Crediting Data Contributors of Diffusion Models" has focused on diffusion models and presented a method to fairly attribute data contributions using Shapley values. To address computational inefficiencies, the authors employ model pruning and fine-tuning, enabling practical Shapley value estimation. Their method is validated across multiple datasets, demonstrating improved attribution accuracy and efficiency over existing techniques.

### Strengths
1- The Shapley theorem has been proven to be an effective solution for calculating the contribution and is widely used in data valuation. The author has properly utilised this theorem as part of the methodology. 
2- Regarding quality, the methodology is well-executed, with rigorous evaluations across multiple datasets that demonstrate the proposed framework’s superior performance.
3- About the clarity, the paper is well-written, with structured explanations and nice visualization,

### Weaknesses
1- It is not a weakness, but the author could also provide an evaluation against data poisoning, which could make it even stronger. 
2- The provided code is well-structured but it could be improved by providing further demo Jupyter notebooks that make it easier for others to test and run the model.

### Questions
How does the framework handle cases where data contributors have varying data quality, styles, etc. and could this affect the accuracy of attribution?

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
3

### Summary
This paper proposes to use a combination of kernel-based Shapley value and sparse fine-tuning as a new method to credit the data contributor in diffusion models. The authors evaluated their approach on CIFAR-20 CelebA-HQ and Art

### Strengths
If the comparison and contribution calculation methods are indeed correct and reasonable, the numerical results look good

### Weaknesses
I'm not very convinced about the overall proposed method for the following reasons.

For the sparsified FT part. some design choice can be elaborated and some comparisons with alternative methods can make the method more convincing.

1. Why is training on the full data and then finetuning on the subset comparable with training with subset from scratch?
2. Why pruning? Why not suing alternative solutions like full model with LoRA instead?
3. When applying sparsified FT, what are the contribution score formulas?

For the Shapley value part.

4. It will be better to elaborate on the similarity and differences between the conventional prediction tasks and the generation tasks, why the kernel based Shapley value can still work well in the current situation needs more explanation as well

For the numerical results, the ablation study is needed.

5. In table 1, the baselines used models trained with subset from scratch but the proposed method used sparsified FT. The results will be more straight forward when using retraining from scratch for all these scoring method or use sparsified FT for all these methods, that will show the ablation for each component in the new method 

Overall speaking, the novelty seems fair.

6. The proposed method is a combination of Shapley value and sparse FT, and I think the reasoning for using this method will be much stronger if the authors can provide evidence showing that each component is better (either efficiency or effectiveness) than their alternatives in this task, like for contribution measurements, Shapley values vs LIME, PFI, etc., and for speeding up model retraining sparse FT vs unlearning, etc.

### Questions
Listed in the weaknesses

### Soundness
2

### Presentation
2

### Contribution
2
