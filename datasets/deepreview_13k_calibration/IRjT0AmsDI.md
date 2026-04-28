# Understanding Grokking: Insights from Neural Network Robustness

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
Recently, an interesting phenomenon called grokking has gained much attention, where generalization occurs long after the models have initially overfitted the training data. We try to understand this seemingly strange phenomenon through the robustness of the neural network. From a robustness perspective, we show that the usually observed decreasing of $l_2$ weight norm of the neural network is theoretically connected to the occurrence of grokking. Therefore, we propose to use perturbation-based methods to enhance robustness and speed up the generalization process. Furthermore, we show that the speed-up of generalization when using our proposed method can be explained by learning the commutative law, a necessary condition when the model groks on the test dataset. In addition, we empirically observe that 
$l_2$ norm correlates with grokking on the test data not in a timely way and then propose new metrics based on robustness that correlate better with the grokking phenomenon.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper aims to understand the grokking phenomenon deeper and proposes a method to mitigate grokking to achieve faster generalization. Authors provide both theoretical and experimental evidences for the grokking phenomenon and shows their perturbation method accelerates the generalization speed. Authors also provide 2 metrics PMI and PE that aim to better monitor when grokking happens.

### Strengths
The novelty and contribution of this paper is good, focusing on grokking problem, authors provide better metrics and algorithm to accelerate model generalization.
The paper has both theoretical and empirical results.

### Weaknesses
1. Figures' x-axis switch between logarithmic and linear, make it very hard to do a comparison among figures. Especially in Figure 3, curves are compressed by logarithmic x-axis on larger step numbers make it very difficult to understand the difference. The use of a logarithmic scale for the x-axis in Figure 3, particularly, obscures the details of the accuracy increase between steps 100 and 1000. The majority of the figure (3/4) is dedicated to the 1-100 step range where accuracy is near zero, while the crucial 100-1000 step range, where accuracy increases, is compressed into the remaining 1/4 of the figure. This makes it difficult to discern the actual differences in accuracy during this critical phase, as small differences in the compressed region may represent larger differences in a linear scale.
2. It is vague that how authors choose the transition point in all figures, for example, in Fig 1(a), the transition point for weight norm is selected at the beginning of weight norm start decrease, but in Fig 9(b), where PE has a similar curve, the transition point is selected much later to convey the point that PE is more aligned with Test Acc. The vague selection also happens in 8(b) 9(a) 10(b) 14(a) and etc. I suggest authors provide a consistent principle in choosing those points to reduce bias in result presenting. The selection of the small square markers on the curves appears inconsistent across figures. For instance, in Figure 1(a), the marker for weight norm is placed much earlier compared to the marker on the PE curve in Figure 9(b), despite both curves exhibiting similar shapes. The rationale for choosing a later marker for the PE curve in Figure 9(b) is unclear, especially when both curves show a similar trend. This inconsistency in marker selection raises concerns about potential reporting bias. Similar issues are present in Figures 8(b), 9(a), 13(b), and 15(a)(b).
3. I didn't really get the definition of PMI, in ln 394, $W_1$ is the first layer so the $W_2$ is the second layer? Is the PMI defined as the layer-wise mutual information on feature embedding gram matrix? also, in ln 399, It is not clear to my that $z^{(2)}_i$ is defined on whether entire $W$ or $W_2$?
4. Results and experiments are mostly based on shallow network and no deep network results.
5. Combine 3 and 4, if I understand correctly PMI and PE will be extremely costly when network being larger and deeper, what will be the complexity of PMI and PE regarding the number of layers and representation dimensions?
6. Ln 429 states that in Fig. 9, the PE changes sharply but 9(a) doesn't, and 9(b) also changes earlier than test acc (see weakness 2).

### Questions
1. What is meaning of X-axis in figure 1 and 2? There are several more figures don't have x-axis labels.
2. What is Algo refer to in Fig 2?
3. In Fig. 7, the logit distance has a significant scale difference(0-15000 vs. 0-150), does standard training also has the "chaotic behavior" if we zoom-in?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work explains grokking, a large accuracy gap between training and test errors in the early stage of the training, with a sharp catch-up of test errors in the late stage. The authors show the importance of weight decay (or small L2 norm of parameters) from the nearest-neighbor perspective (Theorem 4.2). Further, several interesting observations are made empirically in terms of the commutativity and information-theoretic metrics that correlate better with the timing of the grokking.

### Strengths
- Grokking is explained from their lower bounds of test accuracy. 
- Several interesting observations are made in terms of the commutativity and information-theoretic metrics.

### Weaknesses
I raise the following as the major weaknesses of this work. 
1. Limited technical contributions
2. Limited justifications and interpretations for the observations
3. Poor paper writing

I elaborate on the weaknesses below. 

1. Limited technical contributions
This paper has only one technical claim (Theorem 4.2) with the associated corollary. Theorem 4.1 should be a direct adaptation from a related work. The proof of Theorem 4.2 is also straightforward. Further, it is not very clear to me whether the conditions in Theorem 4.2 to guarantee the lower bound of test accuracy are likely to be satisfied in the realistic datasets and whether it really explains the grokking that occurs in various types of datasets. To me, Theorem 4.2 certainly gives an intuitive but still weak argument. 

Corollary 4.3 gives a more concrete lower bound, but it was not very understandable as several definitions are missing. What are $L$, $a$, and $b$? The programming-like variable "train-acc" is also not professional. The condition $\|\mathbf{x}\|_2 = 1$ seems to assume one-hot encoding of a number or a concatenation of two encoding vectors, but no details are given. 

Figure 3 seems amazingly fits to the empirical test accuracy. However, the choice of the values of $(L, \mu, a, b)$ is not justified. To me, these values appear to be carefully selected for the fitting. 

2. Limited justifications and interpretations for the observations
The observations on the commutativity and the better correlating metrics are interesting. It would be better if the authors could justify them theoretically or at least give reasonable interpretation. As for the metrics, I don't see why these better correlate with the timing of grokking - is it trivial or not - and their utility. 

2. Poor paper writing
As partially given in Weakness 1, this paper does not provide sufficient details of the symbols and setup. To list a few, 
- [Sec. 3] The encoding of numbers is not given. The theoretical model of the neural network is not given (ReLU network?). Numerical experiments are done with transformer models, but the theory is for MLPs. What is the one-layer ReLU transformer? (one encoder layer or decoder layer)?
- [Sec. 4.1, line 158] $\mathrm{onehot}(\,\cdot\,)$ is not defined.
- [Corollaly 4.3] See Weakness 1.

**Minor comments**
- [Sec 5.2, line 322] "(a) shows that ... but (b) [Perturb learning?] has a chaotic."

### Questions
Please answer the two weaknesses raised above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper shows that the L2 weight norm decay is connected to generalization and designs an adaptive data augmentation method to speed up generalization

### Strengths
- The paper studies how to speed up generation in grokking, that is an important problem.
- The theory seems to match the experiments well.

### Weaknesses
In Figure 4, how are the hyperparameters (learning rate, weight decay) selected? In the standard training of Figure 4b, the generalization speed may be much faster with proper tuning. It would make the generalization speed-up method more convincing by carefully tuning the hyperparams.

Where did you define $a$ and $b$ shown in Corollary 4.3? The only place a,b are defined is Sec 3, where (a,b) represents the input pair. 

Why do you set L=1/2, a=1925, b=500? Does Corollary 4.3's predicted accuracy change with learning rate and weight decay?

[1] mentioned that there is almost no grokking phenomenon for the MNIST experiments under standard training, and they induce clear grokking by setting large initialization scale. But Figure 2a and 2c show clear grokking for MNIST. What initialization scale is used in those experiments?

### Questions
- Where did you define $a$ and $b$ shown in Corollary 4.3? The only place a,b are defined is Sec 3, where (a,b) represents the input pair. 
- Why do you set L=1/2, a=1925, b=500? Does Corollary 4.3's predicted accuracy change with learning rate and weight decay?
- [1] mentioned that there is almost no grokking phenomenon for the MNIST experiments under standard training, and they induce clear grokking by setting large initialization scale. But Figure 2a and 2c show clear grokking for MNIST. What initialization scale is used in those experiments?

[1] OMNIGROK: GROKKING BEYOND ALGORITHMIC DATA

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper investigates the phenomenon of "grokking" in neural network training, where models fully fit the training data but experience a prolonged period of low test accuracy before suddenly achieving high generalization performance. Through theoretical analysis and experiments, the authors reveal a relationship between grokking and the decay of the l2 weight norm, proposing a robustness-based "degrokking" strategy to accelerate grokking. Specifically, they demonstrate that the reduction in the l2 weight norm enhances model robustness, thus improving generalization to test data. The authors also introduce novel information-theory-based metrics that aim to better capture the grokking phenomenon, with empirical evidence supporting the effectiveness of these metrics.

### Strengths
1. The paper provides a new theoretical framework to explain the underlying mechanisms of grokking and proposes a robustness-based degrokking method, offering a fresh perspective on the study of grokking.
2. The authors design new metrics based on information theory that show potential in capturing grokking effectively.
3. The experiments on MNIST and the Modulo Addition dataset support the theoretical findings, demonstrating the relationship between l2 weight decay and grokking.

### Weaknesses
1. The study and experiments are based primarily on small-scale tasks and datasets, such as MNIST and a Modulo Addition task, making it difficult to assess the generality of the theory in larger, more complex datasets or deeper networks. The observed grokking phenomenon and its relation to l2 weight decay might not directly translate to scenarios with higher dimensionality, more intricate data distributions, or deeper architectures commonly used in modern deep learning. This limitation restricts the scope of the conclusions and raises questions about the practical relevance of the findings in real-world applications.
2. Although the authors propose a perturbation strategy for degrokking, they do not clearly differentiate this approach from traditional data augmentation methods or discuss its unique advantages in accelerating generalization. The paper lacks a detailed analysis of how the proposed perturbation method compares to standard data augmentation techniques like adding random noise, rotations, or scaling. It is unclear whether the specific type of perturbation used offers any benefits over these common approaches in the context of accelerating generalization, and the paper does not provide a clear justification for the choice of perturbation strategy.

### Questions
1. While the authors demonstrate a relationship between l2 weight decay and grokking, the applicability of this theory to more complex datasets or large-scale models (e.g., modern deep neural networks) is not discussed. For instance, does this phenomenon persist when the dataset and task complexity increase? Could similar l2 weight decay behavior be observed on more complex tasks?
2. The proposed degrokking strategy introduces perturbations to enhance robustness, thereby accelerating generalization. How does this method fundamentally differ from traditional data augmentation techniques? If the goal is to accelerate generalization, could conventional data augmentation methods (e.g., random noise) achieve similar effects? Additionally, the authors’ theory appears to support the idea that data augmentation enhances generalization—would it be helpful to further clarify the relationship between the two?
3. Although the decay in the l2 weight norm is related to grokking, how does this phenomenon relate to the model’s learning dynamics and generalization ability? This relationship could be more complex in larger models. Can the authors’ theoretical explanation be extended to more diverse model architectures and tasks?

### Soundness
3

### Presentation
2

### Contribution
2
