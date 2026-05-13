# A ROBUST DIFFERENTIAL NEURAL ODE OPTIMIZER

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Neural networks and neural ODEs tend to be vulnerable to adversarial attacks, rendering robust optimizers critical to curb the success of such attacks. In this regard, the key insight of this work is to interpret Neural ODE optimization as a min-max optimal control problem. More particularly, we present Game Theoretic Second-Order Neural Optimizer (GTSONO), a robust game theoretic optimizer based on the principles of min-max Differential Dynamic Programming.
The proposed method exhibits significant computational benefits due to efficient matrix decompositions and provides convergence guarantees to local saddle points.
Empirically, the robustness of the proposed optimizer is demonstrated through greater robust accuracy  compared to benchmark optimizers when trained on clean images. Additionally, its ability to provide a performance increase when adapted to an already existing adversarial defense technique is also illustrated.
Finally, the superiority of the proposed update law over its gradient based counterpart highlights the potential benefits of incorporating robust optimal control paradigms into adversarial training methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies robust optimisation method for neural ODEs. The authors interpret Neural ODE optimization as a min-max optimal control problem, and then design a Game Theoretic Second-Order Neural Optimizer (GTSONO), based on min-max Differential Dynamic Programming, with convergence guarantees to local saddle points. The authors also conduct experiments to verify the performance of GTSONO.

### Strengths
This paper is well motivated - addressing the vulnerability to adversarial attacks in neural network related methods, including neural ODE.

The authors design a Game Theoretic Second-Order Neural Optimizer as a robust optimiser for neural ODEs. 

They also provide rigorous, theoretical analysis for the proposed method. The proofs are given in detail. 

The paper is well written.

### Weaknesses
I am worried about the novelty, after reading the calculations. Leveraging min-max methods for adversarial learning is a usual approach.  convergence. The calculations of gradients and backpropagation are simple calculus and linear algebra. The proof of convergence is a direct application of existing results in optimisation. I suggest the authors clarify the novelty of their algorithms and proofs, and discuss the differences and advantages of their method.

The experiments are only conducted on CIFAR-10 and SVHN. Experiments on CIFAR-100, and ImageNet (or at least TinyImageNet) are needed for comparison.

From Tables 1 and 2, GTSONO has fairly bad performance in CIFAR-10 in term of natural accuracy. Please discuss why this happens.

The authors only compare with SGD, Adam, and a second order baseline SNOpt. It is not enough. Please compare your method with most existing methods. I list some below:

https://proceedings.mlr.press/v162/rodriguez22a/rodriguez22a.pdf

https://arxiv.org/pdf/2210.16940.pdf

### Questions
Please address the above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper interprets neural ODE optimization as a min-max optimal control problem, and proposed a second order optimizer. The proposed optimizer is computationally feasible by matrix decomposition. Empirically, the authors compare with other optimizers (Adam, SGD and another not min-max second order optimizer), and show it has improved adversarial robustness.

### Strengths
This paper proposes an interesting perspective of robust neural ODE optimization via min-max optimal control. 

The authors make the proposed second order optimizer to be computational feasible: instead of back propagate coupled matrices, one can back propane a set of vectors. 

The authors provide convergence guarantee of the proposed optimizer. 

Experiments show improved adversarial robustness comparing with other non-robust neural ODE optimizers.

### Weaknesses
1. Although I think it is interesting to formulate robust neural ODE optimization as min-max OC, I feel there is gap why the formulation in (3) can be beneficial to the robustness problem in (1): in (3), the adversary is on neural network weights, and in (1), the adversary is on the inputs to the neural network. It is not clear how optimizing against adversarial weights directly translates to robustness against input perturbations. The connection between these two adversarial scenarios needs further clarification. Specifically, the formulation in (3) seems more relevant to adversarial attacks on the network's parameters rather than its inputs.

2. Despite the effort of reducing computational cost, the proposed method is still very expensive. It would be good to include a complexity comparison between other neural ODE optimizers: first-order adjoint and SNOpt. A detailed analysis, perhaps in the form of a table, would be beneficial, outlining the computational cost (time and memory) of the proposed method compared to these alternatives. This should include a breakdown of the operations involved and their respective complexities.

3. It is known that neural ODE tends to suffer from gradient obfuscation issue when being evaluated for empirical adversarial robustness. It would be beneficial to have some adaptive attacks or non-gradient based attacks to make sure the improved robustness is valid. For instance, the attacks used in [1]. Since the optimizer on its own has lower robustness accuracy than adversarial training methods, it is crucial to have solid experiments to show its benefits when combining with other robust training techniques. In general, I like the min-max OC perspective, but it may still lack evidence for its usefulness. Maybe the authors could also consider evaluating against adversary on neural network weights, which I think is more close to the formulation.

### Questions
1. My main question is as in weakness 1: the proposed optimizer seems to be beneficial to attacks on neural network weights rather than on the inputs. I hope the authors can clarify why they choose to demonstrate the effectiveness of their optimizer on input-robustness, and will the method be useful for attacks on system weights?

2. In the experiments, it seems that only having adversarial control on convolution layers is much better than having them on all of the layers. From the theory parts it is not clear why this is the case. The authors should provide more analysis on this.

3. When combing with adversarial training (table 4), why CW accuracy drops? This may indicate some gradient obfuscation issue, it will be good to include some stronger attacks in the evaluation (like AutoAttack, Square) as suggested in weakness 3.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a robust optimization algorithm called GTSONO, designed to train Neural Ordinary Differential Equations (Neural ODEs) that are more resilient to adversarial attacks. Based on min-max Differential Dynamic Programming, the algorithm is not only computationally efficient but also guarantees convergence to local saddle points. Experimental results demonstrate its significant advantage in improving model robustness compared to benchmark optimizers. Overall, the paper offers a new and effective tool for enhancing the robustness of deep learning models.

### Strengths
Originality:
The paper introduces a novel perspective by interpreting Neural ODE optimization as a min-max optimal control problem. GTSONO's approach, rooted in min-max Differential Dynamic Programming, showcases a creative amalgamation of existing concepts.
Quality:
Offering convergence guarantees to local saddle points signifies the robustness of GTSONO. Efficient matrix decompositions and strong empirical results further attest to the research's high quality.
Clarity:
The document articulately bridges intricate theoretical concepts with empirical findings. Despite some formatting issues, the presentation remains clear and coherent.
Significance:
This work addresses a pivotal challenge in neural ODEs, enhancing their robustness against adversarial attacks. The exploration of optimal control paradigms in adversarial training methods underscores its contributions in the domain.

### Weaknesses
1. Although the GTSONO optimizer proposed in this paper can improve the robustness of the model to some extent, it adds too much extra computational overhead, which is unacceptable in the training of larger models. Specifically, the introduction of a second set of weights, even if updated through a single backpropagation, significantly increases the memory footprint and computational cost per iteration. This overhead could become a bottleneck when scaling to more complex architectures or higher-resolution data, making it less practical for real-world applications where computational resources are often limited.
2. The paper's limited comparison with just one other optimizer that improves robustness diminishes the persuasiveness of the results, as a more comprehensive comparison would have strengthened the findings. The lack of comparison against a wider range of state-of-the-art robust optimization techniques makes it difficult to assess the true relative performance of GTSONO. A more thorough benchmark would include methods that employ different adversarial training strategies, such as those based on projected gradient descent or other min-max optimization approaches.
3. One limitation of this paper is that the experiments are confined to the CIFAR10 and SVHN datasets, with no validation on more extensive datasets such as CIFAR100 and ImageNet. This restricts the applicability of the research to a certain extent. The absence of results on more complex datasets makes it unclear how well GTSONO would generalize to more diverse and challenging scenarios. The performance on CIFAR10 and SVHN may not be indicative of its behavior on datasets with higher dimensionality or more complex data distributions.

### Questions
1. Could the authors provide insights into the feasibility of applying GTSONO to larger and more complex datasets such as CIFAR100 and ImageNet?
2. Given the focus on robustness improvement, could the authors consider including a more extensive comparison with various state-of-the-art optimizers that enhance robustness? 
3. Are there any further insights into the stability and convergence properties of GTSONO, especially under varying hyperparameters and different neural network architectures?
4. In general, deep learning optimizers have used mini-batch size to obtain a partial batch of datasets, which means that random noise will be introduced, so the optimizer's parameter update rule should correspond to a stochastic differential equation instead of an ordinary differential equation. Therefore, why do the authors use an ODE rather than an SDE for their theoretical analysis?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
