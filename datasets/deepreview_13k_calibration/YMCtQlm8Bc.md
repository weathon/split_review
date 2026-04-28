# Critical Influence of Overparameterization on Sharpness-aware Minimization

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
\vspace{-0.5em}
Training an overparameterized neural network can yield minimizers of different generalization capabilities despite the same level of training loss.
Meanwhile, with evidence that suggests a strong correlation between the sharpness of minima and their generalization errors, increasing efforts have been made to develop optimization methods to explicitly find flat minima as more generalizable solutions.
Despite its contemporary relevance to overparameterization, however, this sharpness-aware minimization (SAM) strategy has not been studied much yet as to exactly how it is affected by overparameterization.
Hence, in this work, we analyze SAM under overparameterization of varying degrees and present both empirical and theoretical results that indicate a critical influence of overparameterization on SAM.
At first, we conduct extensive numerical experiments across vision, language, graph, and reinforcement learning domains and show that SAM consistently improves with overparameterization.
Next, we attribute this phenomenon to the interplay between the enlarged solution space and increased implicit bias from overparameterization.
Further, we prove multiple theoretical benefits of overparameterization for SAM to attain (i) minima with more uniform Hessian moments compared to SGD, (ii) much faster convergence at a linear rate, and (iii) lower test error for two-layer networks.
Last but not least, we discover that the effect of overparameterization is more significantly pronounced in practical settings of label noise and sparsity, and yet, sufficient regularization is necessary.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors perform experiments to 
measure the effect of overparameterization in SAM for a diverse set of tasks (Section 3). The goal is to observe how overparameterization
affects SAM under various conditions, e.g.,  label noise, sparsity, and regularization. 
Furthermore, they prove that stable minima of SAM are flatter and have more uniform Hessian moments (if compared with SGD), and stochastic SAM can also converge at a linear. The overall contribution is that they empirically and theoretically proved that overparameterization critically affects SAM.

### Strengths
- interesting and well-motivated problem
 - very well written

### Weaknesses
 - discussion on higher moments of Hessian is missing

### Questions
This is an interesting paper. I have a question: how does the convergence of higher-order moments of Hessian in your result compare with the other approaches in the literature, e.g., [1]? Can you provide a literature review on the previous works considering higher-order moments of Hessian to define flatness?

[1] Tahmasebi, Behrooz, et al. "A Universal Class of Sharpness-Aware Minimization Algorithms." Forty-first International Conference on Machine Learning.

### Soundness
3

### Presentation
4

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
This paper studies the critical influence of overparameterization on SAM.

### Strengths
The experiments in this paper are insightful, showing that overparameterization can increase the performance gap between SAM and SGD, while also highlighting the role of factors such as label noise, sparsity, weight decay, and early stopping in this phenomenon.

### Weaknesses
- It is widely recognized that overparameterization improves the generalization performance of SGD (e.g., ResNet-152 outperforms ResNet-18 on Cifar10 using SGD). And it is unsurprising that overparameterization can also improve the generalization performance of SAM. However, the non-trivial aspect is that overparameterization increases *the gap between SAM and SGD*, as shown in Figure 1. To avoid trivialization, reconsidering the title and abstract might be beneficial.

- My primary concern is that the theoretical analysis can not support the main claim/findings (e.g., Figure 1).
  - The linear stability analysis in Section 6.1 can not demonstrate how overparameterization affects SAM (i.e., that “greater overparameterization leads SAM to find flatter minima”). Specifically, the analysis does not show how the bound on the maximum Hessian eigenvalue changes with increasing model size, given fixed values of \(\eta\) and \(\rho\). The current analysis only shows that a larger \(\rho\) leads to a tighter bound, but does not explain why overparameterization would permit or necessitate a larger \(\rho\).
  - In the convergence analysis in Section 6.2: (i) it lacks relevance to generalization, the core focus of the paper; (ii) it does not clarify how the degree of overparameterization influences the convergence speed within the interpolation regime; (iii) in the interpolation regime, the exponential convergence result also holds for SGD (Bassily et al., 2018). The proof for SAM appears to be a minor extension from SGD, which treats SAM as SGD + small permutation. The analysis does not address whether the convergence rate of SAM is accelerated by overparameterization, which is a critical question given the empirical findings.
  - The theoretical analysis in Section 6.1/6.2 focus on a variant of SAM (SAM without normalization) for simplification, rather than the original SAM. While not a major issue, the formulation should be clearly presented in Section 6 to prevent potential reader confusion.

### Questions
Could the authors provide adequate theoretical support for the main findings? e.g., an analysis on diagonal linear networks.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper claimed that SAM benefits from the over-parameterization. They find that SAM could find different (e.g. simpler) solutions than SGD in the over-parameterization regime. In addition, they find that SAM is robust to label noise and sparse parameterization. They also include some theoretical analyses, thought these analyses are irrelevant to their main findings.

### Strengths
1. The authors picked up an interesting perspective to investigate the mechanism of SAM. This research topic is significant.
2. The experiments are extensive, across various datasets and architectures.
3. The writing structure is clear, and the paper is easy to follow.

### Weaknesses
Firstly, for the empirical findings,

1. It is unclear that whether over-parameterization consistently helps SAM find more generalizable solutions as the model parameters scale up. As shown in Fig.1 and Fig. 7 (I think the Fig. 7 is clearer), for MLP on MNIST, ResNet-18 on CIFAR-10, LSTM on SST2 and CNN on Atari, when model get more over-parameterized, the generalization improvement does not always increase; sometimes, a noticeable decline is observed. Moreover, as noted by the authors, when there is no sufficient regularization, SAM might not benefit from the over-parameterization (as shown in Fig. 5). In addition, I notice that the authors conducted experiments for ViT on CIFAR-10 in Fig.5 but not in Fig. 1. I wish the authors could include the results for ViT on CIFAR-10 in Fig.1.
2. Increasing depth of models yields different conclusions than increasing width. In Fig. 1, authors increase the number of neurons in each layer, leading to a seemingly consistent conclusion that over-parameterization helps SAM find generalizable solutions. However, in Fig. 17, when increasing the number of layers, SAM might not benefit from the over-parameterization (ResNet on CIFAR-10). Clearly, the increase of both depth and width demonstrates the over-parameterization, however, the conclusion differs. 
3. It is not surprising that the marginal improvement of SAM over SGD increases with higher label noise. In Fig. 12, in the over-parameterization regime, the performance of SGD drops significantly with higher label noise rate; however, SAM remains good generalization ability. Indeed, it is well known that SAM is robust to label noise, while SGD not. Thus, it is not surprising for us to observe such phenomenon. Also, it seems that the authors over-claimed that over-parameterization secures the robustness of SAM to label noise. Indeed, the observed increase of margin improvement of SAM over SGD with larger model parameters is primarily due to the pronounced decline in SGD's performance as the model parameters scale up under high label noise conditions.
4. The conclusion on the effect of sparsity contradicts with the main argument that SAM benefits from the over-parameterization. In Fig. 5, it is observed that the generalization improvement tends to increase as the model becomes sparser. However, increased sparsity indicates that the model is becoming more under-parameterized. The authors are suggested to explain such contradiction.
5. In Fig. 2 and 3, the authors compare GD and SAM, however, a comparison between SGD and SAM is more preferred.
6. In section 4.2, “implicit bias of SAM increase with over-parameterization” is over-stated. In this section, the authors demonstrated that we could use larger perturbation radius when scaling up the model parameters, however, this doesn’t indicate that a larger scale of model parameters induces stronger implicit bias towards flatter minima. 

In short, SAM doesn’t always benefit from the over-parameterization in practice. A more thorough justification is needed to clarify whether over-parameterization is advantageous for SAM and under what specific conditions it may provide benefits. Indeed, it is quite expectable that SAM would benefit from over-parameterization sometimes. Because in the under-parameterization regime, the model capacity is low (say only one solution in the solution space), thus both SGD and SAM achieve similar solutions. Once scaling up the parameters, the solution space is getting larger, thereby SAM could differ from SGD and find more generalizable solutions. However, SAM might not always from the over-parameterization. 

Second, for the theoretical analysis,

1. As noted by the authors, the theoretical analysis cannot support the findings in Section 3 and 4, and thus the significance of the theoretical analysis is limited. The section 6 is more like a collection of possible theoretical analyses that could be done for SAM. 
2. Indeed, there is no clear theoretical support for the main discovery of this paper, as noted by the authors in the limitations part in Section 7. This is another critical issue of this paper.

Overall, the major issue of this paper is the novelty. The empirical findings are largely anticipated, and the theoretical analysis closely follows prior works without introducing any new proof techniques.  Also, some statements are clearly over-claimed. The contribution of this paper is marginal, and thus I lean to rejection.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work attempts to disclose the critical influence of overparamatrisation on  Sharpness-Aware Minimization  (SAM) from experimental and theoretical perspectives. It starts with an extensive evaluation to display a  highly consistent view showing the generalization benefit of SAM increases with overparametrisation. Without such overparametrisation  SAM may not work. This leads authors to consider the benefit in terms of more solutions and implicit bias. Finally, they developed theoretical advantages and advantages of overparametrization for SAM on linear stability, convergence and generalization.

### Strengths
Nice empirical and theoretical work on overparametrisation on sharpness-aware minimization. It is interesting and useful for ICLR communauty

### Weaknesses
See questions below.

(1) Please clarify the large curve surrounding the "real" curve in Fig . 1 (and possibly in other Figs). Specify if the shaded regions represent confidence intervals, standard deviations or soe other measures of uncertainty. 
(2) How can SAM improvements be compared to SGD improvements via overparametrisation? Hoa SAM and SGD performance changes with increasing model size (may be you can add provide (in Annex) plots showing relative improvement over a baseline for both optimizers across different nodel sizes)
(3) Min Max optimization has some limitations (High complexity; Oscillatory behavior, sensitivity to initialization, etc.), how these problems are addressed here ? Can equation (3) (or some of its properties) help mitigate these issues ? Did you observed these specific issues in your experiments and if so, how have you addressed them ?
(4) Can we use Elliptic Loss Regularisation for SAM instead of Min Max? Please comment on whether Elliptic Loss Regularization could be a viable alternative to the min-max formulation in SAM, and what potential advantages or disadvantages it might have in this context.
(5) Is there a sort of "optimal" number of parameters for which the computation price is acceptable ?Did you  observed any diminishing returns in performance improvement as model size increased. Please provide guidance on balancing computational cost with performance gains when using SAM in practice

### Questions
(1) Please clarify the large curve surrounding the "real" curve in Fig . 1 (and possibly in other Figs). Specify if the shaded regions represent confidence intervals, standard deviations or soe other measures of uncertainty. 
(2) How can SAM improvements be compared to SGD improvements via overparametrisation? Hoa SAM and SGD performance changes with increasing model size (may be you can add provide (in Annex) plots showing relative improvement over a baseline for both optimizers across different nodel sizes)
(3) Min Max optimization has some limitations (High complexity; Oscillatory behavior, sensitivity to initialization, etc.), how these problems are addressed here ? Can equation (3) (or some of its properties) help mitigate these issues ? Did you observed these specific issues in your experiments and if so, how have you addressed them ?
(4) Can we use Elliptic Loss Regularisation for SAM instead of Min Max? Please comment on whether Elliptic Loss Regularization could be a viable alternative to the min-max formulation in SAM, and what potential advantages or disadvantages it might have in this context.
(5) Is there a sort of "optimal" number of parameters for which the computation price is acceptable ?Did you  observed any diminishing returns in performance improvement as model size increased. Please provide guidance on balancing computational cost with performance gains when using SAM in practice

### Soundness
3

### Presentation
3

### Contribution
3
