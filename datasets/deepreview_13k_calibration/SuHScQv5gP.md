# Data Unlearning in Diffusion Models

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 8, 3

## Abstract
Recent work has shown that diffusion models memorize and reproduce training data examples. At the same time, large copyright lawsuits and legislation such as GDPR have highlighted the need for erasing datapoints from diffusion models. However, retraining from scratch is often too expensive. This motivates the setting of data unlearning, i.e., the study of efficient techniques for unlearning specific datapoints from the training set. Existing concept unlearning techniques require an anchor prompt/class/distribution to guide unlearning, which is not available in the data unlearning setting. General-purpose machine unlearning techniques were found to be either unstable or failed to unlearn data. We therefore propose a family of new loss functions called Subtracted Importance Sampled Scores (SISS) that utilize importance sampling and are the first method to unlearn data with theoretical guarantees. SISS is constructed as a weighted combination between simpler objectives that are responsible for preserving model quality and unlearning the targeted datapoints. When evaluated on CelebA-HQ and MNIST, SISS achieved Pareto optimality along the quality and unlearning strength dimensions. On Stable Diffusion, SISS successfully mitigated memorization on nearly 90% of the prompts we tested. We release our code online.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes Subtracted Importance Sampled Scores (SISS), a family of loss functions that integrate importance sampling to facilitate data unlearning while preserving model quality. The method provides theoretical guarantees for data unlearning and is experimentally evaluated on CelebA-HQ and MNIST.

### Strengths
1) The paper introduces an approach to data unlearning by applying importance sampling within the loss function framework, which has not been explored in the literature so far.
2) The paper is well written and structured.

### Weaknesses
1)  While SISS is shown to be more efficient than retraining, the paper could provide more details for the computational cost of the proposal. Specifically, a breakdown of the operations involved in the forward and backward passes, including the number of gradient calculations and memory requirements, would be beneficial. The current discussion lacks a detailed analysis, making it difficult to assess the practical efficiency gains over other unlearning methods. For instance, the cost of computing the importance weights and the impact of this on overall runtime should be quantified.
2) Some important details regarding the experimental resutls are not mentioned clearly. Specifically, the discrepancy in the number of fine-tuning steps between Table 1 (60 steps) and Table 2 (various steps) raises concerns about the comparability of results. This inconsistency makes it difficult to draw meaningful conclusions about the relative performance of different methods. The lack of a consistent evaluation protocol across datasets and methods undermines the validity of the experimental findings.
3) The paper does not sufficiently explore the behavior of the method for different values of lambda. A more detailed analysis of how the method behaves for lambda values between 0 and 0.5, and between 0.5 and 1 is needed. The conceptual implications of these different ranges are not fully explained, leaving the reader with an incomplete understanding of the method's sensitivity to this hyperparameter.

### Questions
1) What is the computational cost of the proposed method? It would be helpful to have a table that summarizes the computationa cost compared to other works. For example, it is mentioned for SISS (no IS) that "Note, however, that it requires two forward passes through the denoising network ϵθ and is thus doubly more expensive in compute and memory." but it is also mentioned that the proposal is more computationally efficient than retraining.
2) Table 2 presetns results for various steps but table 1 contains results for 60 fine-tuning steps. Could you please explain the rational behind this choice? What would be the results in talbe 2 if the same number of steps were used across all the methods?
3) how does the method behave for lambda between 0 and 0.5 and between 0.5 and 1, and what does this means conceptually? 

Minor comment:on page 8, there is a lot of white space that could be used or eliminated

### Soundness
3

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
This paper proposes a new family of loss objectives to perform data unlearning in diffusion models. Based on former work of defensive mixture distributions and by employing importance sampling, these loss objectives can be tuned to unlearn sub-datasets with less degraded quality in retained images.

### Strengths
1. The paper is well-written and easy to follow. 
2. The proposed method is simple, and only based on light mathematical derivations. 
3. The numerical performance is promising, showing significant improvements over reported baselines.

### Weaknesses
1. Although the experiments in this work are promising, there are insufficient theoretical justifications in some sense. I understand that this may be beyond the current scope, but this work can be strengthened if discussing more about working principles. For example, is it possible to introduce (mathematical) tools of traditional machine unlearning (for classical supervised machine learning) for more rigorous demonstrations? What are the main potential difficulties and differences when it comes to the generative setting?

2. The ablation studies can be more comprehensive (see details in the "Questions" section).

### Questions
1. Please kindly provide more details to the questions raised in the "Weaknesses" section. 

2. Ablations: 
- It seems that only $\lambda=0, 1$ are tested. What about other values of $\lambda$? 
- In addition, how does the "superfactor" $s$ in Eq. (8) effect the unlearning performance numerically? 

3. Experimental illustrations: 
- It is shown that the method "SISS (No IS)" appears similar (even mostly better) performance with SISS ($\lambda=0.5$) across all experiments. Does this imply that it is unnecessary to introduce defensive mixture distributions? 
- Also, there are missing 0/1 values of $\lambda$ to be tested (see Fig. 3 (no $\lambda=1$) and Fig. 6(a) (no $\lambda=0$)). 

4. Can authors explain in more details on how to avoid training from scratch using the proposed loss objectives (since Eq. (4) also involves the expectation w.r.t. $p_X$)?

### Soundness
2

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
2

### Summary
The authors propose a new method to address data unlearning in diffusion models. If a diffusion model is trained on a set X, and the goal is to remove a set A, then the resulting diffusion model should not produce any element of A, unless it can be created from the set X \ A. The authors state that the data unlearning process should maintain model quality and be efficient (more efficient that retraining the model from scratch with X \ A).

For data unlearning, the authors introduce a new family of loss functions, Subtracted Importance Sampled Scores (SISS), which balances fine-tuning with the data remaining after subtracting A from X (naive deletion) and gradient ascent on the set A (NegGrad).

The authors show that two variations of their method lead to the best results: 1) SISS (lambda = 0.5), where naive deletion and NegGrad are balanced by a hyperparameter lambda and importance sampling is used to improve efficiency, and 2) SISS (no IS), where lambda is not needed and importance sampling is not used.

### Strengths
The authors introduce a new method for data unlearning in diffusion models, SSIS. The paper is well written, clearly defining the problem and motivating the need for this approach. Furthermore, the results with their approach are very promising. The authors use standard benchmarks and evaluation metrics, which support that their method is effective and efficient. Their experiments are well designed. Overall, this is a strong paper that makes a valuable contribution to the field.

### Weaknesses
1. A brief discussion on the limitations of generating synthetic data and using k-means clustering for Stable Diffusion would strengthen the analysis. Additionally, including a qualitative analysis of similarity, rather than relying solely on quantitative measures (k-means clustering) would provide additional support your method.
2. A discussion on why your method's performance, for the given metrics, surpasses the gold standard (retraining) with MNIST T-Shirt (Figure 4b) would be helpful.

### Questions
Please address the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper present a new data unlearning objective, Subtracted Importance Sampled Score (SISS). To efficiently compute SISS, the paper devices a new objective using importance sampling and defensive mixture distribution. Then the authors provide some empirical results to prove the effectiveness of the proposed objective.

### Strengths
- The paper is mostly well written. 
- The paper conducts various experiments, including some ablations, to prove the effectiveness of the proposed method.

### Weaknesses
 - The authors did not justify why *"involving sampling from the unlearning set A"* is beneficial, which seems to be the most important motivation of the proposed work.
- The choice of defensive mixture distribution $q_\lambda(m_t | x, a)$ seems not suited for diffusion training objective. According to the definition, it is a mixture of two normal distributions, and I believe sampling $m_t$ from such distribution will generate some sort of interpolated version of two noisy images. I'm not sure if this is a good noisy sample for the denoising objective of diffusion model. The actual sampling example from Figure 2 hints an overlay of two different images, which might be the innate problem caused by the objective.
- The need for IS is not clear. SISS (no IS) shows superior quality over SISS (with IS), and since the computational overhead only occurs during training, this, in my opinion, might not be a big problem. Also if involving samples from A is the core motive, one might consider objectives like $(1 - \delta_{x\in A})L(\theta, x) - \lambda (\delta_{x\in A})L(\theta, x)$, where $\lambda$ is the magnitude hyperparameters. This requires only one forward pass, and seems to resemble the spirit of Equation (4).

### Questions
- Why is involving samples from A important for unlearning?
- How do you calculate IS ratio?
- For CelebA example, why was **6** chosen as the number of samples to remove?
- Is the objective suggested in **Weaknesses** inferior to proposed SISS (empirically)?
- (Not so related to this work) Most samples in Figure 5 seems cartoonish. In fact, the only realistic hippo images are memorized ones. According to [1],  memorization can happen at concept-level, and [2] conjectures that memorization can be induced by lack of samples from specific concepts. Perhaps only realistic hippo related to the prompt in training set is the memorized one, and rather than unlearning, adding more realistic images for given prompt might solve the memorization problem. 


[1] Somepalli et al. "Diffusion Art or Digital Forgery? Investigating Data Replication in Diffusion Models", CVPR 2023

[2] Yoon et al. "Diffusion Probabilistic Models Generalize when They Fail to Memorize", ICML 2023 Workshop on Structured Probabilistic Inference & Generative Modeling, 2023

### Soundness
3

### Presentation
3

### Contribution
2
