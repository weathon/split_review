# Efficient local linearity regularization to overcome catastrophic overfitting

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
Catastrophic overfitting (CO) in single-step adversarial training (AT) results in abrupt drops in the adversarial test accuracy (even down to $0\%$). For models trained with multi-step AT, it has been observed that the loss function behaves locally linearly with respect to the input, this is however lost in single-step AT. To address CO in single-step AT, several methods have been proposed to enforce local linearity of the loss via regularization. However, these regularization terms considerably slow down training due to \emph{Double Backpropagation}. %
Instead, in this work, we introduce a regularization term, called \methodname, %
to mitigate CO \emph{effectively} and \emph{efficiently} in classical AT evaluations, as well as some more difficult regimes, e.g., large adversarial perturbations and long training schedules. Our regularization term can be theoretically linked to curvature of the loss function and is computationally cheaper than previous methods by avoiding \emph{Double Backpropagation}. Our thorough experimental validation %
demonstrates that our work does not suffer from CO, even in challenging settings where previous works suffer from it. We also notice that adapting our regularization parameter during training (\adaptivemethodname{}) greatly improves the performance, specially in large $\epsilon$ setups.%

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors investigate the issue of catastrophic overfitting and propose an efficient and effective solution in the form of a local linear regularizer. The introduced algorithm not only mitigates catastrophic overfitting but also circumvents the double backpropagation problem. It performs well in challenging scenarios, such as dealing with large adversarial perturbations and long training schedules, especially when pursuing Fast-AT. Experimental results demonstrate that the proposed method achieves good results while effectively addressing catastrophic overfitting.

### Strengths
1. The proposed regularization scheme as well as the analysis are reasonable, and the introduced local linear approximation scheme is very simple.
2. The experiments show that the proposed ELLE can work well under large adversarial perturbations and long training schedules.

### Weaknesses
1. The definition of Equation 1 is excessively simplistic, lacking any explanation or validation. It's important to note that the majority of deep models and training losses do not conform to linear mappings, which leads me to question this particular configuration. Also, the authors claim that ''CO appears when the loss suddenly becomes non-linear, ...'' (on page 4) I find this description somewhat confusing. Since the loss function usually remains constant throughout the training process, how does this transition from linear to non-linear occur in the loss?

2. The proposed local linear approximation error is similar to the mixup, which has been studied in adversrial training [a]. But, the comparison and analysis are missing.

3. According to the results shown in Figure 4, I found that ELLE-A is not better than ELLE, but I cannot find any clear explanation.

4. The proposed method does not work well under short training schedule and small adversarial perturbation. The authors have not provided a satisfactory explanation or analysis for this issue. Since the defensive performance obtained from long training schedule and short training schedule is comparable, why should we necessarily opt for the longer training schedule? Moreover, large perturbations imply that the noise becomes more pronounced, which contradicts real-world scenarios.

5. In the review process, I attempted to use mathematical tools to show that the regularization introduced in this paper can be used for the approximate estimation of LLR. That is, 

   $L(f_\theta(x+\delta),y)-L(f_\theta(x),y)-\delta^T\nabla_xL(f_\theta(x),y)\approx L(f_\theta(x_c),y)-(1-\alpha)L(f_\theta(x_a),y)-\alpha L(f_\theta(x_b),y)$.

   So, I think ELLE is an effective approximation for LLR. And it's better to compare LLR and ELLE in the all experiments. BTW, the authors only report some results in Figure 1, when considering methods enforcing local linearity. But, I cannot find any comparison in the experiments. I think this lack of comparison to be unfair.

### Questions
Please check the problems mentioned in the Weaknesses part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new regularization techinque which address the catasterophic overfitting of AT approaches.
The new requalrization term is combined with FGSM AT method to improve the robustness of the model during training.

### Strengths
The method addresses a significant challenge in the field of adversarial training with a fairly simple yet effective approach. 
I appreciate the theoretical analysis provided in the paper and the level of details shared by the authors.

### Weaknesses
I understand the paper mainly focuses on the theoretical aspect of the proposed algorithm. 
However, there are some aspects missing which make it difficult to understand how practical the proposed method is.

1- There are several SOTA AT methods currently being used which have demonstrated significant improvement in this area. It would be benficial to have other SOTA adversarial attacks evaluation in the paper as well to show how this approach helps against other SOTA  attacks as well.

### Questions
The main question is that how the proposed method is compared with SOTA adversarial attack algorithms and how this method can be combined with other AT algorithm than FGSM and whether it would be effective in the sence or not.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to mitigate the catastrophic overfitting (CO) phenomenon in adversarial training by enforcing local linearity in the underlying model. Their proposed solution (ELLE) is a computationally efficient approach to enforce local linearity without using double backpropagation, which is time-intensive. Instead, this approach enforces local linearity using multiple forward passes, which is memory-intensive, and hence trading off time for space. Experiments show that their proposed approach is faster than the alternatives, and is successful at mitigating CO.

### Strengths
- This paper proposes a simple but effective strategy to enforce local linearity that does not incur double backpropagation costs. Their theoretical results also show that their method implicitly reduces a quantity related to the Hessian, which is expected.

- The paper has a nice study on the CO problem in the experiments section, especially where it defines “perturbation-wise” and “duration-wise” CO, and has nice figures demonstrating CO and its avoidance with the provided method.

### Weaknesses
 **Not conceptually novel, fails to discuss simpler solutions**

The main idea presented is not conceptually novel. Local linearity has been presented as a solution to catastrophic overfitting several times in the literature (which the paper also discusses). The only novelty is regularizing for linearity using an objective that does not involve gradients. I am unsure how novel or interesting this part itself is – for instance, one can just as well use any other local linearity regularizer (for example, LLR or GradAlign), and replace the gradient terms therein using finite differences. This would eliminate the need for the “double backpropagation” as well and meet their desiderata. The paper needs to discuss why these simple solutions are undesirable if at all they are. 

**Misses key references**

The paper misses a couple of key references (see [1,2]), which aim to achieve the same objective as this given paper. It would be great if the authors could comment on how their method compares with the approaches presented in these works.

[1] Singla et al., Low Curvature Activations Reduce Overfitting in Adversarial Training, 2021  
[2] Srinivas et al., Efficient Training of Low-Curvature Neural Networks, 2022

**Experiments ignore a canonical adversarial defense: PGD**

While the experimental section nicely demonstrates CO and the effect of its method, it **fails to present comparisons** with the canonical method of PGD [Madry et al., 2018]. While speed comparisons are made with PGD in Figure 1, there do not appear to be accuracy comparisons (AA, Clean accuracy) or comparisons with regard to the ability of PGD to locally linearize the model or usage of the proposed method (ELLE) with PGD. This notable omission of PGD significantly weakens the paper. Rather, the paper focuses primarily on improving FGSM-based defenses (although it also discusses improving GAT and N-FGSM in the experiments), which is a significantly weaker defense than PGD

### Questions
- The authors claim in Section 3.3 that the GAT and NuAT methods are not relevant since they attempt to make models locally constant as opposed to locally linear. But surely, local constancy is a special case of local linearity, and thus it is not inconceivable to compare the two methods on equal grounds, like you do for LLR and GradAlign?


- The authors are encouraged to comment on the highlighted weaknesses of the paper.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
