# A Quadratic Synchronization Rule for Distributed Deep Learning

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 5, 8

## Abstract
In distributed deep learning with data parallelism, synchronizing gradients at each training step can cause a huge communication overhead, especially when many nodes work together to train large models.
  Local gradient methods, such as Local SGD, address this issue by allowing workers to compute locally for $H$ steps without synchronizing with others, hence reducing communication frequency.
  While $H$ has been viewed as a hyperparameter to trade optimization efficiency for communication cost, recent research indicates that setting a proper  $H$ value can lead to generalization improvement. Yet, selecting a proper $H$ is elusive. This work proposes a theory-grounded method for determining $H$, named the Quadratic Synchronization Rule (QSR), which recommends dynamically setting $H$ in proportion to $\frac{1}{\eta^2}$ as the learning rate $\eta$ decays over time.
  Extensive ImageNet experiments on ResNet and ViT show that local gradient methods with QSR consistently improve the test accuracy over other synchronization strategies. Compared with the standard data parallel training, QSR enables Local AdamW on ViT-B to cut the training time on 16 or 64 GPUs down from 26.7 to 20.2 hours or from 8.6 to 5.5 hours and, at the same time, achieves $1.12\%$ or $0.84\%$ higher top-1 validation accuracy.%\jz{Maybe report a greater reduction in computation time with matched test accuracy (just look at the figure and roughly calculate). 0.9 percent improvement can be very vague without specifying the model /  task, and we wouldn't want to do that in the abstract.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a scheduler for the synchronization interval of local SGD/ADAM, a.k.a. the Quadratic Synchronization Rule (QSR), which recommends dynamically setting such intervals in proportion to the inverse of the square of learning rate. The proposed algorithm is supported by theoretical analysis based on SDE. The empirical results show that QSR can achieve better validation accuracy with less communication overhead.

### Strengths
1. This paper proposes a scheduler for the synchronization interval of local SGD/ADAM, a.k.a. the Quadratic Synchronization Rule (QSR), which recommends dynamically setting such intervals in proportion to the inverse of the square of learning rate. 

2. The proposed algorithm is supported by theoretical analysis based on SDE. 

3. The empirical results show that QSR can achieve better validation accuracy with less communication overhead.

### Weaknesses
1. The experiments focuses on vision tasks and models. Although ViT model uses the transformer-like architecture, I'm still very interested in how QSR performs in NLP tasks with transformer architectures.

2. The theoretical analysis only applies to local SGD. I wonder whether it could be extended to local Adam.

### Questions
1. Although QSR is supported by theoretical analysis, I still wonder how the other options work, such as setting $H$ proportion to $\frac{1}{\eta}$ or $\frac{1}{\sqrt{\eta}}$. Is there any corresponding ablation experiments?

2. Many theoretical analysis suggests a learning rate scheduler $\eta \propto \frac{1}{\sqrt{T}}$, where $T$ is the number of steps. What if we detach the choice of $H$ from the learning rate, and simply use $H \propto T$ (with some rounding of course)?

3. Is it possible to extend the theoretical analysis to local Adam?

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
This paper builds upon the theoretical insights from [[1]](https://openreview.net/pdf?id=svCcui6Drl) to introduce the "Quadratic Synchronization Rule" (QSR), a theoretically grounded method to set the parameter $H$ in Local-SGD. By analyzing a "Slow SDE for Local SGD with QSR", it is shown that scaling $H \propto \frac 1 {\eta^2}$ (with $\eta$ the Local-SGD decaying learning rate) allows to regularize the objective function towards flatter minima, increasing generalization compared to other schemes (constant values of $H$, or $H \propto \frac 1 {\eta}$). Extensive experiments using ResNet-152 and ViT-B on ImageNet are made to confirm the advantages of QSR compared to previous methods both in terms of test accuracy and wall-clock time for the training.

[1] Xinran Gu and Kaifeng Lyu and Longbo Huang and Sanjeev Arora. *Why (and When) does Local {SGD} Generalize Better than {SGD}?*, In The Eleventh International Conference on Learning Representations, 2023.

### Strengths
* **Promising experimental results**: In the presented settings, the introduction of QSR seems to lead to noticable gains in terms of validation accuracy compared to all the chosen baselines, as well as some mild savings in wall-clock time compared to methods using a constant $H$.
* **Theoretical analysis of Slow SDE for Local SGD with QSR**: Efforts are made to make the reader intuitively understand the changes the introduction of QSR makes to the Slow SDE and how the $K$ times larger drift term favors generalization.

### Weaknesses
* **No confidence intervals in experiments**: given the extensive hyper-parameter search Appendix C claims, I would have expected that the  experimental results in the main paper would come with confidence intervals, and were presented as average over several runs to confirm the reproducibility of the results. The lack of confidence intervals makes it difficult to assess the statistical significance of the claimed improvements, especially considering the inherent stochasticity of deep learning training.

* **No visualization of the effective $H$ scheduler**: Tab. 4 hints that using constant $H$ and QSR actually leads to very similar training times, suggesting that using the QSR scheduler for the values of $\alpha$ retained does not lead to major deviations compared to using constant $H$. In effect, what does the evolution of $H$ look like throughout training, and how different is it from using a constant $H$ ? A direct visualization comparing the $H$ values over time for both QSR and a constant $H$ baseline would clarify the practical impact of the proposed scheduler.

* **Theoretical reasons for the focus on large model and long horizon unclear**: While the main paper focuses on fairly large models (ResNet-152 and ViT-B) and long horizon (200-300 epochs on ImageNet), Appendix D shows that for training a ResNet-50 on 90 epochs, QSR has no effect. Are there any theoretical reasons why QSR should only work for large model and training procedures ? The paper should elaborate on the theoretical underpinnings that suggest a connection between model size, training duration, and the effectiveness of QSR.

* **Unclear why $\gamma =2$ is optimal:** Section 2 claims that *"$H^{(s)}$ could have been set to $H^{(s)}:= \max \left \{ H_\text{base},  \left \lfloor \left ( \frac{\alpha}{\eta_t}  \right )^{\gamma} \right \rfloor \right \}$ for any $\gamma$"*. However, it still remains unclear to me why setting $\gamma = 2$ is optimal. The paper should provide a more thorough justification, either theoretical or empirical, for the choice of $\gamma = 2$ and discuss the implications of using other values.

* **Comparison with related work lacking:** Appendix A cites the *"Stochastic Weight Averaging in Parallel (SWAP) algorithm"* [2] as another method that varies the value of $H$ during training, leading to a decrease in training time and better generalization. Yet, no comparison with the method is performed in the paper. A direct comparison with SWAP, particularly in terms of generalization performance and wall-clock time, would strengthen the paper's contributions.

* **Additional hyper-parameter to tune**: *"choosing the right value of $H$"* has been traded for *"choosing the right value of $\alpha$"*, thus QSR does not "automatically" set $H$ and no hyper-parameter tuning has been saved. This introduces another hyperparameter, $\alpha$, that requires careful tuning, potentially offsetting the benefits of the method.

### Questions
* A network speed of 25Gbps is used for the experiments. Would your algorithm still help in HPC settings where fast communications can happen over 100 Gbps Infiniband ?
* Are both the model size **and** number of epochs important factors for QSR to work ? For example, using a smaller model (such as ResNet18) but with a decent amount of epochs (e.g., 300 epochs on CIFAR10), would QSR have an impact ?

### Soundness
3 good

### Presentation
2 fair

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
The paper examines the optimal approach for dynamically determining H, a hyperparameter in Local SGD, allowing workers to compute locally for H steps without synchronizing with others.

The goal is to strike a balance between communication costs and the final test accuracy. While a large 'H' might degrade accuracy, a small 'H' could intensify communication overhead. Drawing inspiration from the stochastic differential equation introduced by [Gu et al.](https://arxiv.org/pdf/2303.01215.pdf), this paper introduces a new Quadratic Synchronization Rule for setting the H dynamically given a predetermined learning rate schedule. Furthermore, the research provides proof delineating the approximate convergence bounds concerning the distance between the iteration and the manifold. The paper also presents experimental results in various settings.

### Strengths
S1. The concept presented is intuitive—convergence can be improved by dynamically tuning H the number of steps of local updates before syncing with others. The introduced Quadratic Synchronization Rule holds potential for application in distributed machine learning.

S2. The paper provides a theoretical analysis of their idea and conducts experiments to support their theoretical results.

### Weaknesses
W1. The motivation of finding 'H’  given a learning rate schedule is questionable. Both learning rate and H should be tunable hyperparameters in distributed learning.
"Specifically, we introduce a simple yet effective strategy, called Quadratic Synchronization Rule (QSR), for dynamically adjusting the synchronization period according to the learning rate: given a learning rate schedule, we set H proportional to η^−2 as the learning rate η decays. This rule is largely inspired by a previous theoretical work (Gu et al., 2023), which shows that the generalization benefits arise only if H = Ω( 1/η ) when η → 0, but did not make any recommendation on how to set H."

Solely determining H given the learning rate schedule, yet without asking about what the optimal learning rate is is a less valuable question. While prior work [1] already shows that the generalization benefits arise only if H = Ω( 1/η ) when η → 0, this work specifically sets H to 1/η^2, which is incremental, reinforcing the same results. In fact, the learning rate is of greater significance in deep learning and distributed learning; for many problems, one can boost generalization and convergence performance solely by carefully tuning the learning rate. A more valid question that I believe should be asked is what is the optimal dynamic learning rate schedule under a given schedule of H, e.g. H=1 or 2 or Post-local SGD with variable H. There is no comparison to this learning rate question under a fixed H schedule, which further saves communication and is easier to implement in reality. Therefore, I think the problem studied here to recommend how to set H is kind of artificial.

W2. The baseline for comparison is not clear. For instance, what is the Parallel AdamW? How does the Parallel AdamW work? I can’t find the rigorous definition of it given by the paper. Because of the second momentum terms, Parallel AdamW that assumably aggregates the model parameters every H=1 step is not equivalent to Centralized AdamW when only setting H = 1. The second momentum can not be simply averaged. Even the definition of Parallel SGD is not provided. The paper simply says that refers to Local SGD when H=1. At least a reference or a definition should be provided.

W3. Some experimental settings are questionable. What has motivated the adoption of only SGD for ResNet experiments and AdamW only for VIT experiments? Furthermore, while all experiments employ momentum-based optimizers and underscore the effectiveness of QSR with such optimizers, the paper doesn't deeply explore the role of momentum in this methodology.

W4. The theoretical analysis and proof overlap too much with previous work [1]. Both rely on the same SDE technique (which is the novelty of the prior work) for analyzing analogous issues, with the current work lacking additional theoretical insights and development. Additionally, some proof steps are missing. See questions for details.

W5. There is no comparison with other practical distributed learning systems and methods, given the vast literature on distributed learning. The comparison is more of a simple self-comparison between different hyperparameter scalings of H, e.g., constant H vs. the QSR of H,  assuming the same learning rate schedule is used. This comparison is not convincing because 1) for different H setups, the optimal learning rate schedule will vary; 2) it didn’t compare to other possibilities of H = Ω( 1/η ) making it hard to understand the limitations of the problem domain. This makes the work more of hyperparameter tuning heuristics and lacks insights. The experimental results are more of validating the theorems and lack practical value.

W6. The exploration of the choice for $H_{base}$ seems insufficient. Providing a graph that illustrates the relationship between final test accuracy, communication volume, training time reduction, and the selection of $H_{base}$ would be more persuasive.

### Questions
(1) Have you considered comparing the performance of $H\sim \eta^{-3}$, $H\sim \eta^{-4}$? While prior work [Gu et al.](https://arxiv.org/pdf/2303.01215.pdf) already shows that the generalization benefits arise only if H = Ω( 1/η ) when η → 0, this work specifically sets H to $η^{-2}$. This results seem to be quite heuristic and not a thorough investigation of the problem domain. What understanding about the limitations or insights of the method has been derived?

(2) The proof provided for Lemma E.2 appears to be too succinct. Furthermore, in Lemma E.2, it is stated that 'we can apply the Itô-Taylor expansion from Lemma B.7 of Malladi et al. (2022) to derive (16), (17), and (18).' Is there a typo in this reference to equations? I suspect you meant to refer to equations (11), (12), and (13). Also, could you please elucidate how you derived equations 11, 12, and 13?

(3) Proof for Theorem 3.1 is overly concise. What is Lemma I.43? What is the definition of r? How do you get 
$$E[u(\hat{\zeta}_{s, s+1},(s+1) \alpha^2, n \alpha^2)]$$

from
 
$$E[g(\hat{\zeta}_{s,n})]$$

(4) How do you calculate the communication time in Table 4, why don't you opt for using communication volume instead?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a new synchronization rule for local gradient methods, where synchronization among processors is performed after multiple rounds of local updates. In the synchronization rule, the number of local updates is proportional to the inverse of the learning rate square. Theoretical analysis is provided to motivate the proposed synchronization rule. Experimental results on ResNet and ViT show that local gradient methods with the proposed synchronization rule yield better test accuracy and less training time.

### Strengths
1. The proposed quadratic synchronization rule is simple but effective, backed up by strong theoretical analysis.
2. Experimental results show both efficiency gain and better generalizations.
3. The experiments are comprehensive, including various architectures, learning rate decay strategies, and batch sizes.

Overall, I think this is a good paper.

### Weaknesses
n/a

### Questions
n/a

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
