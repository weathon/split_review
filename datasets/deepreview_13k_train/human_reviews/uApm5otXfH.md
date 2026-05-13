# Interleaving Optimizers for DNN Training

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
Optimizers are crucial in deep neural network (DNN) training, affecting model quality and convergence. Researchers have found that different optimizers often suit different problems or different stages of a problem. Hence, some studies have tried to combine different optimizers to better train DNNs. However, existing methods are limited to simple optimizer switch strategies, which leads to unstable model quality and slow convergence. In this paper, we propose a fine-grain optimizer switch method called Iterleaving Optimizer for Model Training (IOMT), which automatically switches to the appropriate optimizer and hyperparameters based on the training stage information, achieving faster convergence and better model quality. IOMT employs surrogate models to estimate the performance of different optimizers during training and is supported by a transferability assessment to predict the training cost. By combining the transferability assessment, performance estimation, and training process information with an acquisition function, IOMT calculates the optimization gain of each optimizer and switches the optimizer with the largest gain for the next training stage. The experimental results on full training and fine-tuning demonstrate that IOMT achieves faster convergence (e.g., 10\% on the *stl10* dataset) and better performance (e.g., 3\% accuracy improvement on the *cifar10* dataset) compared to existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes an optimizer switching method, the interleaving optimizer for model training (IOMT), for DNN training. The proposed IOMT automatically switches the optimizer and hyperparameters during the model training based on the optimization status information, resulting in faster convergence and better model quality. The experimental result demonstrates that IOMT outperforms existing SGD optimizers on several tasks and models.

### Strengths
- The motivation for switching the optimizer during the model training is good.
- The switching strategy based on the Gaussian process surrogate seems novel, and some modified acquisition function is introduced.
- The effectiveness of the proposed method is demonstrated by several datasets and DNN models.

### Weaknesses
 - The reason for the improvement of model quality is not sufficiently elaborated. It is not clear why switching optimizers during training would lead to better generalization performance. While faster convergence is a plausible outcome of optimizer switching, it does not necessarily imply improved generalization. The paper needs to provide a more detailed analysis of how the proposed method avoids overfitting or finds a better local minima compared to using a single optimizer throughout training.
- It is unclear how sensitive IOMT is against its hyperparameter setting. Therefore, it would be great if the sensitivity analysis of the hyperparameter setting in IOMT was conducted. Specifically, the impact of the initial step size, the switch step size $\tau$, and the number of PCA components on the final model performance should be analyzed. Without such analysis, it is difficult to assess the robustness and practical applicability of the proposed method.
- The reviewer feels that there are several unclear points of the detailed procedure of IOMT. Please see questions.

### Questions
- The reviewer does not understand why IOMT improves the model quality, although the faster convergence by IOMT is somewhat convincing. Could you explain why IOMT can improve the generalization performance of the trained model?
- The reviewer is not sure what weights parameter sets are used for computing principle axes and when the PCA calculation is performed. To compute the principle axes (eigen decomposition), data points $\{ {\bf \theta} \}$ should be prepared.
- IOMT introduces additional hyperparameters, such as the number of PCA components and the switch step size $\tau$. What is the impact of such hyperparameter settings on performance?
- Most optimizers have internal states, such as momentum information. How are such internal states inherited and maintained when switching the optimizer?
- There are some typos: "Iterleaving" should be "Interleaving."



----- After authors' response -----

Thank you for your response. I am satisfied with the authors' response. I would keep my score positive side.

I would like to comment a little bit more about the PCA calculation.
Let us assume the dimensionality of $\theta$ parameters as $D$; then, ideally, we need more than $D$ data points of $\theta$ parameters to calculate the principal axes. At least, I suppose that we need $D'$ data points for PCA calculation, i.e., {$\theta^{(1)}, \dots, \theta^{(D')}$ }, $\theta^{(k)} \in \mathbb{R}^D$, where $D'$ is the number of PCA components for dimensionally reduction.
I am still not sure how the authors collect such $\theta$ parameter sets.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Deep neural networks often face the issue of how to select optimizers. This paper addresses this problem by proposing IOMT, a fine optimizer switch based on a surrogate method (i.e., Gaussian process). The authors provide relevant experiments to support their method. However, the experimental section has several issues, such as limited improvement in performance and a lack of ablation studies.

### Strengths
1.	The paper is easy to read.
2.	The problem of optimizers is clear.

### Weaknesses
1.	There exist some typos/grammatical errors in the paper and should be revised.
2.	The authors mention in the abstract that the main issue with DNNs is uncertain impact of optimizers. However, they have not rigorously validated or proven this issue on larger datasets (ImageNet, COCO2017, VOC) and tasks (i.e., object detection, VQA, NLP-based tasks). Clearly, this statement needs further verification to establish its existence.
3.	In page one, what is the definition of better model quality?
4.	In page 1, the author claims that surrogate models, namely Gaussian process will predict the performance of different optimizers during training, the presentation of performance is unclear: is it accuracy or something else?
5.	Why transferability assessment is used to predict training cost? I don’t see any definition and discussion in your paper.
6.	The presentation of Figure 1 is not clear.
7.	Please provide more experiments on training cost.
8.	Please provide a comparison with more competitors.
9.	This topic is not novel. Please read the paper about AutoML.
10.	It would be interesting to use NAS to search for the best configuration for optimizers.
11.	Provide a more thorough discussion of the generalization ability, robustness, and potential applications of the proposed approach.
12.	The format of references is not correct.
13.	The main limitation of this paper is that proposed method lacks theriacal analysis, ablation study, larger datasets (ImageNet, COCO2017, VOC), more tasks (i.e., object detection, VQA, NLP-based tasks), and larger networks (i.e., stable diffusion, LLMs), and visualization.
14.	Exploring the reasons behind the success of these techniques and providing intuitive explanations would contribute to the overall scientific contribution of the work.

### Questions
see Weaknesses

### Soundness
3

### Presentation
2

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
The paper introduces the IOMT framework, which combines multiple optimization algorithms in a novel way to enhance the training of deep learning models. This approach aims to leverage the strengths of different optimizers at various stages of training. The proposed approach builds a surrogate model that takes the hyper-parameters and the preprocessed model parameters as input and returns the here-defined score. An optimizer, hyper-parameter values, and the training time are then selected based on the acquisition function defined using the trained surrogate model. The authors conduct extensive experiments to validate the effectiveness of the IOMT approach, demonstrating its advantages over baseline (single) optimization methods and other hybrid methods. The results show improved performance in various scenarios with different models and different datasets.

### Strengths
A novel method for optimizing deep learning training by interleaving multiple optimizers. This innovative strategy allows for leveraging the unique strengths of different optimizers at various stages of training, which can lead to improved model performance.

Empirical validation. The paper provides extensive experimental results that demonstrate the effectiveness of the IOMT approach.

### Weaknesses
The problem is formulated as a general problem in (1). However, in the experiments of this paper, only a single hyper-parameter (i.e., learning rate) is considered and the training time is fixed. It is not clear whether it is effective when more hyper-parameters are to be optimized and the training time is to be optimized. In particular, it is not clear if the proposed approach can really select the best approach when baseline approaches have different number of hyper-parameters, leading to different difficulties in building surrogate models for different approaches.

Related to the above point, the search space is small. Only 5 methods with 3 possible learning rate values, resulting in 15 choices in total. It is not clear how much it scales.

Some details are not clear. How are w_p and w_d defined? It is recommended that their definitions be added to the Appendix.

### Questions
How could the proposed approach avoid overfitting? Doesn't it overfit if you run it longer? I couldn't find any mechanism that could prevent it.

### Soundness
2

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
The paper introduces the Interleaving Optimizer for Model Training (IOMT), a method for dynamically switching optimizers during a DNN's training to enhance model quality and convergence speed.  IOMT leverages surrogate models to estimate the performance of various optimizers based on parameter states and combines this with a transferability assessment to predict optimization gains. Furthermore, an acquisition function selects the optimizer with the highest expected benefit for each training stage. Experimental results suggest 3% accuracy increase on the CIFAR10 dataset and a 10% reduction in convergence time on STL10, positioning IOMT as a more efficient alternative to traditional or hybrid approaches.

### Strengths
The paper demonstrates a degree of coherence throughout, effectively guiding the reader through its arguments and findings. The choice of topic—optimizer selection—addresses a compelling area in machine learning research, and the approach presented brings a refreshing level of novelty to the field. Additionally, the paper’s examination of transferability represents a valuable addition, hinting at potential applications across various domains and suggesting broader implications for adaptability in optimization.
The comparative analysis presented in the paper appears thorough and fair, particularly with regard to benchmarking against both static optimizers and hybrid methods. However, as indicated in the weaknesses and questions section, some aspects of the methodology and analysis could benefit from further clarification or refinement to strengthen the overall impact of the work.

### Weaknesses
The paper presents two central claims that form the foundation of its proposed approach: first, that optimizers lead to distinct final weights by making divergent choices at key saddle points, and thus, selecting the most suitable optimizer at each of these saddle points could lead to more effective optimization of deep neural networks (DNNs). Secondly, the authors claim that the performance of each optimizer can be anticipated through a surrogate model. If this surrogate model is accurate, an acquisition function can be employed to switch between optimizers based on their predicted performance. 

The design decisions surrounding the accuracy of the surrogate model, the effectiveness of the acquisition function, and the tuning of implementation hyperparameters are crucial elements in this framework. Each of these components directly influences the method's success, and so examining them carefully through the lens of methodological implementation, presentation, and results is warranted.

I will separate my critiques into the following themes:

### Method implementation:

First, the authors have not provided sufficient details on how they chose the hyperparameters for their method. For example, the initial phase, which relies on weighted random selection, is likely essential for achieving a high-quality surrogate model. This initial phase could be particularly sensitive to various hyperparameter configurations, impacting the model's effectiveness. Therefore, presenting the surrogate model's fit across different training points would help validate these design choices and clarify their impact. 

Second, the switch step size is another significant hyperparameter that merits careful explanation, as it could substantially influence the optimization process. A more detailed rationale on how these hyperparameters were chosen, possibly accompanied by an ablation study or sensitivity analysis, would strengthen the methodological transparency and robustness of the proposed approach. 

Finally, variance halving is presented as a core component of the method, yet no ablation study is included to demonstrate its necessity. Including this analysis would substantiate the importance of variance halving and justify its role within the overall framework.

### Presentation:

The presentation of the approach, while promising, could benefit from some improvements in clarity. 

First, Figure 1 does not effectively communicate the paper’s key insight, as it displays only a single function evaluation and simply illustrates how different optimizers follow distinct paths from a saddle point. Replacing this with an aggregated figure that visualizes multiple runs would provide a clearer, more comprehensive view of how optimizers differ in their decision-making at saddle points. 

Second, the explanation in the introduction could be clarified; specifically, the authors should more explicitly state that different optimizers result in varied weight configurations due to their unique decision-making characteristics. Establishing the significance of matching optimizers to saddle points would benefit the reader's understanding of the approach’s core motivation (Lines 40–48). 

Third, Figure 7 is somewhat unclear. While it illustrates that different optimizers reach different final parameter states, it remains ambiguous whether these states yield comparable performance levels or achieve similar final accuracies. More detailed labeling or annotations could clarify these distinctions. 

Finally, there is some ambiguity in Lines 14–19, where it is unclear whether the authors are jointly optimizing for both optimizers and other hyperparameters, or if their focus is solely on optimizer selection. Clarifying this would prevent potential confusion and ensure a clearer presentation of the research focus.

### Results:

The comparison with static and hybrid baselines is indeed informative; however, the observed incremental improvements on CIFAR may reflect the plateaued progress often seen on this dataset with current optimization methods. Given that the approach’s strength lies in its dynamic adaptability at critical saddle points, it would be beneficial to consider adversarial benchmarks like Imagenet-A to illustrate this advantage. Imagenet-A presents a challenging environment where subtle variations in optimization strategies could have a more pronounced impact, thereby highlighting the adaptability of the dynamic optimizer selection process.

Furthermore, the sensitivity of switching behavior to the surrogate model’s accuracy is an essential aspect. Since hyperparameters influence the surrogate model’s quality directly, understanding how these hyperparameters affect switching decisions would reinforce the robustness of the approach. One way to evaluate this would be to compare switching profiles under different surrogate strategies, including a scenario where the model operates suboptimally by relying purely on exploitation. Such an analysis would provide valuable insights into the flexibility of the proposed method, showing whether it can maintain performance even when the surrogate model is imperfect.

While optimizer selection is certainly an interesting approach and previous work, particularly Im et al., motivates the need for this, it still needs justification in terms of usability. Generally, tuning just the hyperparameters is simple and easy, which is why it is the go-to strategy for optimizing neural networks. A technique such as an optimizer selection, if necessary for the considered problems, should be able to beat a simple and common HPO baseline, such as tuning Learning rates with cosine annealing. Therefore, having this as a baseline can help empirically justify the need for optimizer selection.

### Questions
* How is this work related to learned optimization?
* How is the proposed SMBO technique related to previous work on Dynamic Algorithm Configuration (see Adriansen et al. JAIR’22)? As I see it, the aim here is to dynamically switch between optimization methods and that is understandable. 
* How did the authors decide hyperparameters $n_{\text{ini}}$ and $\tau$? 
* How did the authors decide on PCA as a feature engineering method? Is there a particular benefit that PCA has over other methods, say UMAP, Random projection or shallow autoencoders?
* How do the authors select which layers to use as inputs to the surrogate model?

### Soundness
2

### Presentation
2

### Contribution
2
