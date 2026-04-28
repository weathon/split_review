# Can the Training Loss be Predictive for Out-of-Distribution Generalization?

- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 3, 3, 3

## Abstract
Traditional model selection in deep learning relies on carefully tuning several hyper-parameters (HPs) controlling regularization strength on held-out validation data, which can be challenging to obtain in scarce-data scenarios or may not accurately reflect real-world deployment conditions due to distribution shifts.
Motivated by such issues, this paper investigates the potential of using solely the training loss to predict the generalization performance of neural networks on out-of-distribution (OOD) test scenarios.
Our analysis reveals that preserving consistent prediction variance across training and testing distributions is essential for establishing a correlation between training loss and OOD generalization.
We propose architectural adjustments to ensure $\textit{variance preservation}$, enabling reliable model selection based on training loss alone, even in over-parameterized settings with a sample-to-parameter ratio exceeding four orders of magnitude.
We extensively assess the model-selection capabilities of $\textit{variance-preserving}$ architectures on several scarce data, domain-shift, and corruption benchmarks by optimizing HPs such as learning rate, weight decay, batch size, and data augmentation strength.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work investigates the use of training loss to predict the generalization performance of neural networks on out-of-distribution scenarios, instead of using the validation data. This work is particularly useful in distribution-shifted scenarios, where standard validation data may be unavailable. This work examines the conditions for establishing linear relationships between training and test losses. Comprehensive empirical analysis is provided to analyze the model-selection capabilities of the proposed framework through extensive experiments setup, including optimizing several hyper-parameters across popular OOD benchmarks.

### Strengths
1. This work proposes a novel approach for model selection by relying solely on training loss to predict out-of-distribution generalization. This is different from the traditional validation-based model selection and is particularly suitable for scenarios involving distribution shifts.

2. This paper analyzes the conditions for which training loss can correlate with OOD generalization, and develop a variance-preserving architecture based on these conditions.

3. Various hyper-parameters are thoroughly investigated across different types of OOD benchmarks, including corruption and domain shifts.

### Weaknesses
1. It would be valuable to analyze and investigate on different types of OOD shifts, including diversity shifts and correlation shifts [1], and discuss whether the proposed conditions hold across these two dimensions of OOD shifts.

2. Extending the evaluation to more complex real-world natural images, such as the WILDS benchmarks [2].

3. Providing additional theoretical justification for supporting and explain the proposed variance preserving architecture, would enhancing the reasoning and foundation of the proposed framework.

### Questions
Refer to the detailed suggestions provided in the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work investigates the conditions under which the training loss can predict OOD generalization. The authors find that maintaining consistent prediction variance across training and testing distributions is key to correlating training loss with OOD generalization. They propose architectural adjustments to preserve this variance and demonstrate that these variance-preserving architectures allow for reliable model selection based on training loss in various OOD scenarios.

### Strengths
1. The study of OoD generalization and model robustness has always been an important topic. Investigating model selection and generalization ability from the perspective of network architecture is a worthwhile endeavor.

2. The paper is well written and easy to follow.

### Weaknesses
1. The authors’ claim that the RQ in line 69 is an unexplored research question is inaccurate, as this topic has already been studied extensively in prior work, such as [1] and [2]. This study's approach, which examines the problem from the perspectives of variance preservation and network architecture, is also not new; similar analyses have been conducted in previous studies, such as [3] and [4]. This work does not sufficiently compare itself to these prior studies and build upon them for further exploration.

2. It is inappropriate to directly ignore the gradient term $\nabla_f \mathcal{L}$ in formulas (2) and (3). It is a function of $f$ and $\boldsymbol{w}$, and choosing different $f$ and $\boldsymbol{w}$ will yield different $\nabla_f \mathcal{L}$, thereby impacting $\text{Cov}(J(\boldsymbol{w}, \boldsymbol{h}), J'(\boldsymbol{w}, \boldsymbol{h}))$ and $\text{Var}(J(\boldsymbol{w}, \boldsymbol{h}))$. Considering only the Cov term in formulas (2) and (3) leads to an incomplete conclusion.

3. The architectural adjustments proposed in this work are already commonly used for training neural networks and do not provide any new insights.

### Questions
1. With a substantial amount of research already available, why is the RQ in line 69 considered an unexplored research question? Is there a key point I might have overlooked?

2. Why can the gradient term $\nabla_f \mathcal{L}$ in formulas (2) and (3) be ignored?

3. Which of the architectural adjustments proposed in this work are newly introduced?

Please see Weaknesses for details.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates whether training loss could be used to predict OOD performance. It claims that preserving consistent prediction variance across training and testing distributions is essential. This paper analyzes the factors that may affect prediction variance and further proposes variance-preserving architectures.

### Strengths
* The attempt to bridge the training loss with the model performance on the testing set, especially the OOD test set is interesting.

* Generally this paper is clear. The figures in this paper are pretty.

### Weaknesses
 * The relationship between the training testing loss correlation and the correlation between each predicted label seems fra-fetched. As claimed in Eq.4, it requires the correlation between the predicted label of each of the two training testing data samples to be close to 1, which seems impossible. The derivation relies on a Taylor expansion of the loss function around the mean prediction, which may not be accurate, especially when the loss function is highly non-linear and the predictions vary significantly. The assumption that prediction variance is consistent across training and testing distributions is also questionable, as distribution shifts often lead to changes in the model's confidence and prediction patterns. The paper does not provide sufficient justification for why this assumption should hold true in general OOD scenarios.

* The experimental setting that random samples a subset from the CIFAR10 training set and tests on the CIFAR10 testing set does not qualify as an OOD scenario. The distribution of the CIFAR10 training set is the same as that of the CIFAR10 testing set. Randomly sampling a subset does not change the distribution. While the reduced training set size might lead to overfitting, it does not create a genuine distribution shift that would be expected in a real-world OOD scenario. The paper should have used a more appropriate OOD benchmark dataset to validate its claims.

* According to the results shown in Fig. 2, 3, 4, 5, and 6, these models show **the typical over-fitting pattern**. It seems that the proposed adjustment increases the correlation because it prevents over-fitting. However, overfitting is caused by the training on a small subset of the original training set, which could be simply dealt with. The paper does not adequately explore other methods for preventing overfitting, such as regularization techniques or data augmentation, which are commonly used in practice. The performance drop observed in Table 2 further suggests that the proposed method might be limiting the model's capacity to learn complex patterns, rather than genuinely improving OOD generalization.

Considering the above-mentioned weaknesses, I have doubts about the analyses in this paper and the proposed variance-preserving architecture. In my understanding, the proposed method limits the ability of the network to prevent overfitting, which also explains the performance drop as shown in Table 2.

### Questions
As mentioned in the weakness part, I have doubts about the analysis, the experimental setting, and the proposed method in this paper. I would like to see a rebuttal regarding the mentioned weaknesses. Currently, I will recommend reject for this paper.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, the authors explore the research question: "whether the training loss can be used as a reliable predictor of OOD performance". The authors found that neural network architecture may be an important factor for the reliability of predictions. Then, the authors study the conditions and neural architectural designs to control the prediction-variance across distributions. Empirical results on example datasets demonstrate of the effectiveness of this methodology. There are several points the authors may address to further clarify this paper. See questions.

Overall, this is an interesting paper and some points can be addressed or even refocus on the HP optimization to further improve it. Current title seems to be too broad for this paper.

### Strengths
Good presentations and writtings.

### Weaknesses
See summary.

1) What are the potential practical implications for this paper? As this paper focus on the neural architectural design to improve the reliability for prediction. Then,

   1.1	does the proposed architecture brings additional benefits or drawbacks or equivalent performances compared with normal neural architectures.  The authors need to show the performance comparisons before and after architectural modifications.

   1.2	Have the authors explored any techniques to improve OOD performance prediction without modifying existing architectures? If not, what are the key challenges in doing so?"

2)	Comprehensive evaluations on different OOD distribution shifts. The authors are suggested to consider different kinds of OOD distribution shifts. As shown in [1] and [2], there are different types of distribution shifts in real-world datasets, it is suggested to consider two types of distribution shifts including diversity shifts and correlation shifts. In this paper, spurious correlations are not considered. Or alternatively, justifying why focusing on the diversity shift instead if this is the primary focus on this paper.

3) Experiments of this method for hyper-parameter optimization. As this method can potentially serve as a way to help improving HP optimization, the authors can consider introduce this to existing HP optimization pipelines to wider experiments, such as PACS, and ImageNet to see how it works. What advantages will this method demonstrate over other HP optimization baselines.  Besides, it could also (might) be beneficial if the focus of this paper be moved into the HP optimization as this shall have strong practical implications in various fields.

4) Experiments on standard OOD datasets. The authors could explain why choosing the datasets in this paper over standard OOD benchmark datasets. This paper can consider standard datasets in OOD generalization, such as PACS, ColoredMNIST,  VLCS, etc as well as what is done in most OOD generalization papers.

### Questions
1)	What are the potential practical implications for this paper? As this paper focus on the neural architectural design to improve the reliability for prediction. Then,

   1.1	does the proposed architecture brings additional benefits or drawbacks or equivalent performances compared with normal neural architectures.  The authors need to show the performance comparisons before and after architectural modifications.

   1.2	Have the authors explored any techniques to improve OOD performance prediction without modifying existing architectures? If not, what are the key challenges in doing so?"

2)	Comprehensive evaluations on different OOD distribution shifts. The authors are suggested to consider different kinds of OOD distribution shifts. As shown in [1] and [2], there are different types of distribution shifts in real-world datasets, it is suggested to consider two types of distribution shifts including diversity shifts and correlation shifts. In this paper, spurious correlations are not considered. Or alternatively, justifying why focusing on the diversity shift instead if this is the primary focus on this paper.
 
[1] A Critical Analysis of Out-of-Distribution Generalization
[2] Ood-bench: benchmarking and understanding out-of-distribution generalization datasets and algorithms

3) Experiments of this method for hyper-parameter optimization. As this method can potentially serve as a way to help improving HP optimization, the authors can consider introduce this to existing HP optimization pipelines to wider experiments, such as PACS, and ImageNet to see how it works. What advantages will this method demonstrate over other HP optimization baselines.  Besides, it could also (might) be beneficial if the focus of this paper be moved into the HP optimization as this shall have strong practical implications in various fields. 

4) Experiments on standard OOD datasets. The authors could explain why choosing the datasets in this paper over standard OOD benchmark datasets. This paper can consider standard datasets in OOD generalization, such as PACS, ColoredMNIST,  VLCS, etc as well as what is done in most OOD generalization papers.

### Soundness
2

### Presentation
3

### Contribution
2
