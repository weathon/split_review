# Towards Robust Alignment of Language Models: Distributionally Robustifying Direct Preference Optimization

- Decision: Accept
- Avg Score: 6.20
- Scores: 8, 6, 5, 6, 6

## Abstract
This study addresses the challenge of noise in training datasets for Direct Preference Optimization (DPO), a method for aligning Large Language Models (LLMs) with human preferences. We categorize noise into pointwise noise, which includes low-quality data points, and pairwise noise, which encompasses erroneous data pair associations that affect preference rankings. Utilizing Distributionally Robust Optimization (DRO), we enhance DPO's resilience to these types of noise. Our theoretical insights reveal that DPO inherently embeds DRO principles, conferring robustness to pointwise noise, with the regularization coefficient $\beta$ playing a critical role in its noise resistance. Extending this framework, we introduce Distributionally Robustifying DPO (Dr. DPO), which integrates pairwise robustness by optimizing against worst-case pairwise scenarios. The novel hyperparameter $\beta'$ in Dr. DPO allows for fine-tuned control over data pair reliability, providing a strategic balance between exploration and exploitation in noisy training environments. Empirical evaluations demonstrate that Dr. DPO substantially improves the quality of generated text and response accuracy in preference datasets, showcasing enhanced performance in both noisy and noise-free settings.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper addresses the noisy data problem in DPO alignment. Specifically, the authors start with pointwise noise data and show that the SFTed model on these data harms DPO performance. Then, the authors build a connection between DPO and DRO and point out that the smaller $\beta$ in DPO implicitly enlarges the search space of DRO, therefore suitable for larger noise.

Authors then argue that DPO cannot handle the pairwise noise and show pairwise noise harm the DPO performance. To tackle the problem, authors derive DrDPO from DRO. DRO can be understood as a dynamic-reweighting DPO that assigns more weight to less likely noisy data.

During experiments, authors show how small $\beta$ can mitigate pointwise noisy data and DrDPO achieve higher rewards than DPO with faster convergence and similar KL.

### Strengths
* Clear problem formulation and motivation. Each motivation has introductory supporting experiments.

* Concise writing is easy for readers to understand even though readers do not know DRO much in advance. The running example is very helpful to understand the algorithm.

* Extensive experiments and ablation study to support motivation, main claim (DrDPO), and method's characteristics (convergence, KL, etc).

### Weaknesses
 * DrDPO requires the estimation of E_O.  In practice, this is often achieved within a batch or pre-computed on the whole dataset. Which implementation is used in the paper? How does the batch size affect the optimization results if using the former one?

* Experiments on more models and sizes will make the results more convincing.

* There are several papers discussing reweighting DPO, such as WPO (https://arxiv.org/pdf/2406.11827v1), which could be discussed in related work.

### Questions
Typo: line 194: \pi_\theta

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the challenge of noisy training data in Direct Preference Optimization (DPO) for aligning Large Language Models (LLMs) with human preferences. The authors identify two types of noise: pointwise noise (low-quality data points) and pairwise noise (incorrect preference rankings). They enhance DPO's robustness using Distributionally Robust Optimization (DRO). They reveal that DPO inherently provides robustness to pointwise noise. To tackle pairwise noise, they introduce Distributionally Robustifying DPO (Dr. DPO), which optimizes against worst-case pairwise scenarios and introduces a new hyperparameter to control data pair reliability. Empirical results show that Dr. DPO significantly improves text quality and response accuracy in both noisy and clean datasets, offering a more robust method for LLM alignment in the presence of data noise.

### Strengths
1. The paper is well written and easy to follow.
2. Addressing the issue of noisy data in preference learning for LLMs is both important and interesting.
3. The paper has extensive experiments and theoretical analysis to prove the effectiveness of their proposed method.

### Weaknesses
1. The authors include IMDB and Anthrophic HH for experiments. It’s better to provide more datasets like TruthfulQA, GSM8k and other datasets.
2. It’s better for authors to conduct experiments on more open-source LLMs to further verify the effectiveness of their algorithms.
3. The authors can provide some more case studies to better understand the performance of their method.

### Questions
I have included my questions in the weaknesses part.

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
4

### Summary
In this paper, the authors explore the noisy data challenges when using Direct preference optimization (DPO) methods in large language models (LLMs). In this paper, noise is divided into pointwise noise and pairwise noise, and a method called Dr. DPO based on DRO is proposed to enhance DPO's resistance to these two kinds of noise. By introducing a new hyperparameter $\beta'$, Dr. DPO is able to achieve a better balance between exploration and utilization in noisy environments. The experimental results show that Dr. DPO not only performs well on noisy data sets, but also shows stronger performance on noiseless data sets.

### Strengths
1. The Dr. DPO framework proposed in this paper is an important improvement over the existing DPO methods, which effectively solves the noise problem in training data and improves the robustness and accuracy of the model.

2. The authors provide a solid theoretical basis to explain why DPO essentially incorporates the principles of DRO and how to improve the model's resistance to point noise by adjusting the regularization coefficient $\beta$.

3. This paper verifies the effectiveness of Dr. DPO through a large number of experiments, and the experimental results show that the method can significantly improve the quality of generated text and the accuracy of response under different types of noise environments.

4.  The authors provide links to the code, which helps other researchers reproduce the experimental results and further promote the research progress in related fields.
defect.

5. The authors provide a Toy Example of How Dr. DPO Works, which is helpful to understand the proposed method.

### Weaknesses
1. The evaluation could be compared with more baselines, please refers to https://arxiv.org/pdf/2409.02795.

2. These evaluation tasks are too simple; some methods may be effective on benchmarks like IMDB but may not generalize well to more complex tasks.

3. Although the authors provide beautiful theory proof, the objective of Eq (12) seems to be in contradiction with IPO.

### Questions
1. Despite how funny this question might sound, can I understand Dr. DPO as simply adding an exponential function ($e^{(\cdot)}$)to the objective function of DPO?

2. Could you explain the weakness-3?  IPO learns the $h(x,y_w,y_l)$ to a specific value, but Dr. DPO maximize the $h(x,y_w, y_l)$, are you be in contradiction ?

### Soundness
3

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
3

### Summary
This paper addresses the problem of noise in training datasets for Direct Preference Optimization (DPO). It first classifies noise into pointwise (low-quality data points) and pairwise (erroneous data pair labeling). Then, it analyzes DPO from the perspective of Distributionally Robust Optimization (DRO) to evaluate its resistance to both types of noise. Finally, it presents the Distributionally Robustifying Direct Preference Optimization (Dr. DPO) framework, which incorporates pairwise robustness by optimizing for worst-case pairwise situations and features a new hyperparameter β' to manage data pair reliability. Experiments reveal that Dr. DPO enhances the quality of the generated text within preference datasets.

### Strengths
- DPO is inherently a form of Distributionally Robust Optimization (DRO) that confers pointwise robustness, with the regularization coefficient $\beta$ inversely related to the robustness radius $\eta$.
- The authors introduce Distributionally Robustifying DPO (Dr. DPO), which incorporates pairwise robustness by optimizing against the worst-case pairwise scenarios, without the need for explicit noise estimation.
- Dr. DPO demonstrates enhanced performance compared to DPO and other baselines in both noisy and noise-free environments, showcasing its effectiveness in aligning language models with human preferences.

### Weaknesses
 - The assumptions about pointwise and pairwise noise in Subsection 3.1 and Subsection 4.1 are not quite comparable, which may affect the conclusion in the paper that DPO is robust to pointwise noise but not robust to pairwise noise. Details in Question 2.
- There is a lack of ablation experiments regarding the batch size in the paper. Details in Question 4.
- Some declarations in the paper is not so clear, which make it a little hard to follow. For example, 1) It is declared a topic "DPO is Implicitly a Pointwise DRO" in subsection A on line 192. But apart from a standalone Theorem 3.1 and some "insights" statements, there are lacking of a formal proof to connect DPO and Pointwise RPO. 2) When discussing "Why DPO is Robust to Pointwise Noise" on line 212, it is directly stated that "the implicit robust framework of DPO counters data perturbations effectively" on line 215, rising the question again "why is DPO robust to pointwise perturbations?". As a comparison, Section 4.3 is presented much better.


### Questions
1. In Figure 4 (Left), there seem to be similar trends of trading off between Reward and KL, and if a small KL value is required under the scenario of RLHF (e.g. less than 2), are similar rewards gained from different rates of flipped pairs?

2. The noise added to the pointwise dataset and the pairwise dataset in the paper cannot be regarded as the same type of noise. The noise added to the pointwise dataset by generating samples from the un-tuned GPT-2 only weakens the extent of a sample being good, similar to reducing $P(y\ \text{is\ positive})$ rather than setting $P(y\ \text{is\ positive})=0$. So a more corresponding method of adding noise to the pairwise dataset would be reducing $P(y_w > y_l)$, rather than reversing the order to make $P(y_w > y_l)=0$. Therefore, it seems that the different impacts on DPO caused by adding noise to the pointwise and pairwise datasets in Sections 3.1 and 4.1 are not really comparable.

3. The toy example in Section 4.3 is a little hard to follow. The function $h$ that has been clearly defined in the previous text is used, but an inconsistent combination of parameters is passed in, which is confusing.

4. During the training process, the estimations of both $L_{Dr.DPO}$ and $\omega$ rely on a batch of data. Will the batch size become a crucial factor affecting the effectiveness of the policy? There is a lack of ablation experiments regarding the batch size in the paper.

PS. There is a typo "DRDPO" in Section 5.3.

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper examines the robustness of Direct Preference Optimization (DPO) in aligning large language models (LLMs) with human preferences and introduces "Distributionally Robustifying DPO" (Dr. DPO) as a framework to enhance this robustness. The authors identify two types of noise in training data: pointwise noise (low-quality data in supervised fine-tuning) and pairwise noise (incorrect preference rankings in preference training). For pointwise noise, they show that the original DPO framework inherently applies DRO principles, where the parameter $\beta$ correlates with the robustness radius $\eta$ in the DRO framework, reflecting tolerance to pointwise errors in the data. To address pairwise noise, they extend DPO with Dr. DPO by introducing a new hyperparameter that adjusts the impact of noisy pairs, resulting in improved performance in challenging, noisy environments. Empirical results validate Dr. DPO’s effectiveness in producing high-quality responses and sustaining accuracy across various noise levels.

### Strengths
Originality:
- The idea of applying Distributionally Robust Optimization to LLM alignment is novel and interesting.

Clarity:
- The paper is well writen and easy to follow.

Significance:
- The proposed Dr. DPO method has natual interpretation and easy to compute. 
- Experimental results are promising. Auther compres the performance of Dr.DPO with various alignment methods and provide detailed ablation studies and parameter $\beta'$.

### Weaknesses
Major concerns:
- The discussion on pointwise noise and DRO lacks clarity. Equation 7 appears to be a dual form of the PPO objective (Equation 3). Typically, DRO aims to optimize a target function over distributions close to the empirical sample distribution. In reward modeling, the "sample" refers to the input prompt and the answer generated by the target model, $\pi_{\theta}$. Following this logic, the DRO objective would optimize over distributions $Q$ close to $(x, \pi_{\theta}(y|x))$. However, in Equation 7, the authors approach the problem as optimizing objectives over distributions $\pi_{\theta}(\cdot|x)$ near $\pi_{ref}(\cdot|x)$. I don't see a clear connection between equaiton 7 and DRO. Providing an interpretation of Equation 7 and discussing its relation to Equation 6 would help clarify this connection.


Minor concerns:
- The model used in pairwise experiments is not explicitly stated in the main text. The Pythia 2.8B model is mentioned only in the appendix, which reduces confidence in the experimental results.
- The authors have omitted relevant literature on applying Distributionally Robust Optimization to LLMs, specifically, Oren, Yonatan, et al.'s "Distributionally Robust Language Modeling."
- Setting $\beta' = 1$ results in $L_{Dr.DPO} = -\log E[\exp(h_{DPO})]$, which differs slightly from the original DPO formula. A more detailed interpretation of this form would be insightful.
- In Figure 5 (left), Dr. DPO shows higher win and loss rates at 0 flips. Does this imply that incorporating Dr. DPO leads to a trade-off between performance and robustness?

### Questions
I look forward to discussing these questions further in the weaknesses section, as they have the potential to either increase or decrease the score.

### Soundness
3

### Presentation
3

### Contribution
3
