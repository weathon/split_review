# Activation Decay by Loss Smoothing to Enhance Generalization

- Decision: Reject
- Avg Score: 2.50
- Scores: 3, 3, 1, 3

## Abstract
Generalization in deep learning  is often associated  with the sharpness of the minima encountered during training. We introduce a novel, deterministic, and computationally efficient method called \emph{activation decay}, designed to flatten sharp minima and improve generalization across a wide range of tasks. Derived from Gaussian smoothing, activation decay operates by regularizing the activations of critical network layers, effectively reducing sharpness and improving robustness. Unlike stochastic techniques such as dropout or the more computationally expensive Sharpness-Aware Minimization (SAM), our approach requires no additional computational overhead, making it particularly suited for large-scale models.
We further demonstrate that activation decay can be seamlessly combined with other regularization techniques, offering enhanced regularization without increasing training complexity. Extensive experiments on CIFAR-10, ImageNet, and natural language processing (NLP) tasks validate our approach, showing consistent improvements in generalization and robustness to label noise.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an "activation decay" method to flatten sharp minima and thereby enhance generalization.

### Strengths
The authors conducted extensive experiments across CV and NLP tasks to demonstrate the effectiveness of activation decay (AD).

### Weaknesses
 **Main Concern: Activation Decay (AD) Method**

- **Novelty**: AD appears to randomly permute parameters only in the last layer, which is akin to using average-direction SAM, i.e., $\min_{\theta}:\mathbb{E}_{g\sim N(0,I)}L(\theta+\rho g)$ [1][2], but applied solely to the last layer.

Additionally, related work [3] also suggests that SAM is not required for all parameters; applying it only to layer normalization layers suffices.

- **Theoretical supports:**
  - Theorem 1 applies to parameter permutation across all layers, unlike AD, which permutes parameters only in the last layer.
  - Theorem 2 could not illustrate why you only permunate the parameters in the last layer, as similar results should hold for other layers ($l\leq L-1$).
  - Theorem 3 provides only an upper bound for AD loss, insufficient to substantiate AD's effect similar to weight decay. A two-sided bound is needed for this claim.

**Secondary Concern: Practical Applicability**
- AD introduces an additional hyperparameter $\sigma$, requiring tuning for different tasks, which limits its flexibility. Results in Tables 1, 2, and 3 indicate that $\sigma$ values must be adjusted across tasks.

### Questions
- Why do the authors refer to this method as "activation decay"? Note that it does not alter the activation function or activations directly, but only the parameters in the output layer.

- What would the experimental results be if parameters in layers other than the last layer were perturbed?

- In Table 1, why do the authors use an unconventional $\rho=2$ for SAM? The standard $\rho$ for SAM on CIFAR-10 is 0.05 or 0.1. Additionally, have the authors tuned SAM across all experiments to ensure fair comparison?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a deterministic regularizer to ensure that training converges to a wider minima known to lead to improved generalization. Some experiments are conducted on computer vision and NLP tasks to validate the claim. The regularizer is also justified theoretically.

### Strengths
The paper clarity is good and the motivation to move away from stochastic regularization is important.

### Weaknesses
 
**Missing references**:
- Large Margin Deep Networks for Classification
- Minimizing Layerwise Activation Norm Improves Generalization in Federated Learning (closest)

**Missing experiments**:
- SAM with much finer set of p needs to be provided for **all** the experiments
- additional datasets and architectures need to be explored at least for the computer vision domain (as per the SAM paper)
- additional comparisons with dropout, stochastic depth needs to be provided


### Questions
In addition to the above concerns that need to be addressed. A lot of claims from the paper feel subjective, e.g., the batch size argument (in contrast to that paper finding (Stochastic Training is Not Necessary for Generalization). Also, the authors need to provide much more experimental details and configurations used for training as the work is currently not reproducible e.g. there is no mention of data augmentation in the entire paper.

Because of the above + all my concerns and the fact that this work provides a method that was already explored before and fails to expand on their empirical validation (and the derivations in the paper are well known and were already used in previous papers), I do not think there is novelty or insights to meet the acceptance level.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
Thank authors for submitting their work to ICLR 25'. The paper proposes so called $\textit{activation decay}$ (AD) regularizer ($\ell_2$ norm penatly of activations of the last layer) derived from Gaussian smoothing (convolution with Gaussian noise) designed to flatten sharp minima and improve generalization. It is argued that AD promotes the flatter minima and it is positioned as a less computational expensive alternative to stochastic regularizers such as dropout or SAM. The method is corroborated by experiments on CIFAR-10, InageNet and NLP tasks (BERT architecture).

### Strengths
S1: Timely, well suited topic for applications and ICLR community

### Weaknesses
While paper addresses the timely topic of generalization ability of deep learning it seems it does it by taking too many shortcuts as if it was written in a hurry. It proliferates into rather significant weaknesses in almost all sections, including errors in proof of the main results, as follows

W1 (Introduction, Related Work): The paper claims a theoretical contributions ($1^{st}$ bullet point in Introduction) as well. It stands on flattness = goog generalization premise (abstract, l:11 or l:28: "One of the key factors influencing generalization is the nature of the minima in the loss landscape.") or dedicated section 2.1. While this phenomenon has been reported under several settings experimentaly, flatness/curvature/Hessian is in general is parameter dependent and deep overparameterized networks are widely weight invariant, e.g., ReLU networks, pre-/post- non-lineartity rescaling, allowing for counter examples showing that sharp minima can generalize well and vice-versa, see for instance (Zhang et al., Understanding deep learning requires rethinking generalization, 2017).

More over that is dedicated section 2.1 that reviews the related work dedicated to flat minima, yet it does not mention any opposing works whatsoever, which seems to me a bit biased, given that this is to the best of my knowledge still an open problem (at theory at least). The paper should mention (Introduction, Related Work) these works and challenges and take necessary assumptions under which flatness implies good generalization to make theoretical part solid. In its current version the flatness is presented as the sufficient condition to generalization, which does not hold in general.

Section 3.
W2: The theory is presented for "near optimum" l171 "In the regime near a minimum, ...", Theorem 1, or even for "$\nabla \mathcal{L} = 0$" Theorem 2. Letting alone works as "Chaudhuri et al., Neural Network Weights Do Not Converge to Stationary Points: An Invariant Measure Perspective, PLMR 2022" questioning whether finding well generalizing solution requires convergence at all, presented Theorem 1 argues that flattening of landscape happens after converging to neighborhood of a particular optimum. 

However, Theorem 1 gives an upper bound for smoothed (training) loss $\nabla_{\theta}^2 \mathcal{L}(\theta + \Delta)$, yet for generalization the $test$ loss, i.e., $without$ noise convolution (Gaussian smoothing), is relevant. Could authors present the argument leading to test loss improved bounds? Recall, under "near optimum" assumption the neighborhood of a local optimum $\theta_0$ is fixed ...
 
W3: Overall theoretical contribution:
W3a: Theorem 1. This is just a Theorem 2 taken from Dellattre as also mentioned (or its special case follows from a convolution with Gaussian noise). Proof in SM is also just 2 lines reference to Dellattre paper. I suggest not to present it as a standalone Theorem, but rather apply it on your settings. 

W3b: Proof of Theorem 2 does not hold. Line 807: "At a local minimum, the gradient term involving the first derivatives vanishes." - unfortunately this does not imply that $\nabla_z \mathcal{L}=0$ because this is gradient w.r.t. outputs of the networks, not weights in general. In fact for convex loss $\nabla_z \mathcal{L}=0$ only vanishes in GLOBAL optimum. Thus the Eq. on line 809, does not hold and hence Theorem 2 conclusion is fault. (Btw. It also is mentioned not to yield any improvements in Discussion & COnclusion, line 497-499.) 

Experiments
W4a. SAM. Exclusion of SAM from experiments, l 324, and it suboptimal results in Table 1 and 2. This is confusing to me as SAM is by definition method that explicitly finds flatter (and thus better generalizing optima according to paper) and weight decay or AD are just rougher (yet faster) "flat optima searching" methods. Thus while providing efficiency merits, they should not significantly overperform SAM. However this is not what is reported and to me it looks as a wrong hyperparameter choice for SAM. But then, are the experiments conclusive?
W4b. The difference in Table 1 between (AD + SAM) and SAM rows are not significant, given the standard deviation presented ...
W4c. Qute importantly, weight decay (WD) experiments with hyper parameter optimization are missing to be compared with AD. WD has all the computational and efficiency merits as AD and thus AD should outperform WD in accuracy to makes practical sense to replace it...

### Questions
See Weaknesses

### Soundness
1

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
4

### Summary
The authors introduce a method called as "Activation Decay", which regularizes the activation in the penultimate layer to flatten sharp minima and improve generalization across a range of tasks. This approach is grounded in a theoretical framework that connects noise variance to the spectral norm of the Hessian, demonstrating that the activation in the penultimate layer serves as an upper bound for Gaussian smoothing on Hessian curvature. There are experiments on CIFAR-10, ImageNet, and NLP benchmarks.

### Strengths
- The paper is easy to follow.
- The idea of regularizing only the activation in the penultimate layer is quite interesting, and it can replace dropout at this layer.

### Weaknesses
 - The idea of regularizing later layers has been explored in Baek et al. [2024]. This effectively reduces SAM's effectiveness to that of SGD with an L2 norm penalty on the intermediate activations and the weights of the last layer in a two-layer, deep linear network. Could you compare your method with theirs?
- Activation decay can only be applied to the penultimate layer, whereas dropout can be applied in multiple locations within the backbone architecture. Therefore, the use of activation decay might be limited. The restriction to the penultimate layer, while theoretically motivated, may not fully leverage the potential benefits of regularization across the entire network architecture. This is a significant limitation, as it prevents the method from being applied to earlier layers, which could potentially offer further improvements in generalization.
- Figure 1a lacks annotations for better clarity. The absence of a legend or clear labels makes it difficult to interpret the results and understand the specific components being visualized. This lack of clarity hinders the reader's ability to fully grasp the experimental setup and the implications of the findings.
- In Figure 1a, why is the estimated Hessian calculated only with respect to the final layer? Does this mismatch the theoretical results in Theorems 1 and 2? The theoretical framework seems to suggest that the Hessian should be calculated with respect to all parameters, not just the final layer. This discrepancy between the theory and the experimental setup raises concerns about the validity of the empirical results.
- In Table 1, this paper compares its methods with ASAM [Kwon et al., 2021]  but is missing a citation for it. Why don’t the authors compare their methods with the original SAM?

### Questions
- In Table 2, could you explain why the optimal perturbation for your experiments with SAM is lower ($\rho = 0.01$) compared to the optimal $\rho = 0.15$ recommended for NLP tasks in Bahri et al. [2022]?
- The improvement of proposed methods in Section 4.2 is not significant. Could you extend your experiments to more complex datasets, such as CIFAR-100 and Tiny ImageNet, so that the differences and improvements are clearer? 
- See the Weaknesses part.

References:
- Dara Bahri, Hossein Mobahi, and Yi Tay. Sharpness-aware minimization improves language model generalization, 2022. URL https://arxiv.org/abs/2110.08529.

### Soundness
2

### Presentation
2

### Contribution
2
