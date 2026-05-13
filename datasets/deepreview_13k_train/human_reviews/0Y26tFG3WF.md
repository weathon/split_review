# Inducing Precision in Lagrangian Neural Networks : Proof of concept application on Chaotic systems

- Decision: Reject
- Scores: 3, 3, 5

## Abstract
Solutions of dynamic systems that exhibit chaotic behavior are particularly sensitive to errors in initial/intermediate state estimates when long term dynamics is of interest. Lagrangian Neural Networks (LNN) are a class of physics induced learning methods that seamlessly integrate physical conservation laws into functional solutions, by forming a parametric Lagrangian for the system of interest. However it has been seen that the function approximation error associated with the parametric Lagrangian modelling could prove to be catastrophic for the prediction of long term dynamics of chaotic systems. This makes improving the precision of the parametric Lagrangian particularly crucial. Considering the same in this work a modified Lagrangian Neural Network approach is proposed, where a customized neural network architecture is designed to directly emphasize the relative importance of each significant bit in the Lagrangian estimates produced. We evaluate our method on two dynamic systems that are well known in the literature in exhibiting deterministic chaos, namely the double pendulum and Henon-Helies systems. Further, we compare the obtained solutions with those estimated by Finite Element solvers (under optimal conditions) to validate the relative accuracy. We observe that the trajectory deviations as a result of chaotic behavior can be significantly reduced by the process of explicitly enforcing the precision requirement for the parametric Lagrangian, as modelled using the proposed approach.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Lagrangian neural networks have emerged as a promising approach to learning the dynamical behavior of a system from data. However, its limited precision hurts the prediction of long-time sequences, in particular, if the system is chaotic. The paper introduces a modification of the LNN framework where precision is explicitly modeled and shows that it improves prediction error in two empirical settings.

### Strengths
The problem studied is well justified. The description of the neural architecture used, and of the task studied is clear.

### Weaknesses
I found the algorithm extremely convoluted, which is, in general, not a good sign for its robustness. It could be justified if simpler solutions, such as changing the default float32 in Jax to float64, do not work. However, the authors do not provide any data points suggesting that these simpler approaches do not work.

The experiments are too limited for me to be able to judge if the approach works.

Additionally, I found it a bit weird that only the original Lagrangian Neural Network paper is cited (and compared to), as papers improving the idea have been published since then (e.g., Finzi et al 2020).

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a variant of the Lagrangian Neural Network (LNN) model for inducing higher precision outputs. The authors are motivated by chaotic systems, where slightly-inaccurate predictions can diverge quickly from the ground truth. In particular, the authors propose to output each binary bit of a traditional LNN's output, and they introduce several new regularization terms to supplement the regular LNN objective towards the goal of higher binary precision. The authors test their proposed model on the double pendulum and Henon-Heiles chaotic systems, with improvements over the original LNN architecture in the amount of steps before the predictions of each chaotic system's state diverges from the truth.

### Strengths
The method is unorthodox in the sense that neural network predictions are typically not performed as classification over the significant bits of the output. However, the authors design a training policy that carefully considers possible issues during training (such as the increasing $\mu_{TC}$ scale term and the proposed regularization term), which is appreciated. 

For instance, $O_{reg}$ is used to supplement, not replace, the $O_{pred}$ MSE loss, and $O_{TC}$ is a good heuristic to deal with the situation in which the Lagrangian of a given system does not have a known analytical form. The increase weight of $\mu_{TC}$ is also a good solution to reduce instability from the initial transient stages of training.

The authors also compare between various choices of the precision parameter $k$, and they empirically show that the results of using low $k$ values are similar to the results of the original LNN model, which is an interesting result.

### Weaknesses
There is little to no explanation, intuition, or motivation about why this method should be superior to standard regression techniques optimizing with mean squared error. In general, there are several methodological concerns I have. For instance, computing the explicit Lagrangian using eq. 8 and comparing it with the ground truth MSE loss seems equivalent to the standard LNN formulation. Thus, the novelty of this method is in the regularization term $O_{reg}$ and in the regularization method to deal with unknown Lagrangians for the underlying system. Can the authors provide some intuition for why $O_{reg}$ is added and why it improves performance? Also, in what sense does $O_{reg}$ provide a regularization effect?

There is also no discussion and comparison to prior variants of LNNs. One such paper is Finzi et al., 2020, which also performs experiments on the double pendulum. I would strongly recommend the authors perform numerical experiments to compare against other prior LNN variants, not just the original LNN model. Furthermore, there is little to no discussion in the introduction about these LNN variants. At the very least, I would like to see some discussion about prior improvements to the LNN/Hamiltonian neural network (HNN) architectures.

Furthermore, the evaluation for this method seems a bit limited. Recent extensions of LNNs and HNNs target more difficult problems, such as 5-pendulums (Finzi et al., 2020) and pendulums with friction (Zhong et al., 2021). Given these prior works, I would also strongly recommend the authors add more challenging case studies (e.g., any of the ones mentioned earlier) and compare to prior methods.

In summary, if the authors wish to convince the readers of the novelty and contribution of their work, I would recommend adding a deeper explanation and intuition for this method, adding more difficult test cases, and adding comparisons with other LNN variants (not just the baseline paper).

### Questions
* In $O_{reg}$, the least significant bits in the output appear to be weighted the same as the most significant bits. Is there a particular reason for this? Did the authors try a relative weighting between the most and least significant bits?
* In computation of $L_{pred}$, the authors mention that they round the sigmoid output of the model for each bit. How is this implemented in a differentiable way to allow for backpropagation through $O_{pred}$?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to approximate chaotic systems using Lagrangian Neural Networks (LNN) with better precision. A new LNN architecture is proposed to emphasize the importance of significant bits. A new regularization term is added to ensure the accuracy of each significant bit. Experimental results demonstrate that the proposed LNN can achieve better precision.

### Strengths
1. It is important to pursue precision when approximating chaotic systems since a small error can cause long-term large errors.
2. The proposed method is succinct and easy to understand.
3. Experimental results verify the efficacy of the proposed method.

### Weaknesses
The motivation of the regularized term is not convincing. Adding a regularization term is a tradeoff between the original objective (Eq. (7)) and the regularization term (Eq. (9)). In common cases, minimizing the regularization term will make the original objective larger. In this paper, the original objective cares more about higher decimals, while the regularization treats all decimals equally. Thus, adding the regularization term will inevitably sacrifice the accuracy of higher decimals, which hurts the original objective. To my understanding, the original objective already reflects the precision requirement when approximating chaotic systems, and the regularization term only plays a negative role.

There are many minor problems in this paper. Part of them are listed below.
1. In the tile, the colon is closer to proof rather than networks.
2. In the abstract, the abbreviation LNN appears on the 3rd line but its full name still occurs on the 10th line. After the abbreviation appears for the first time, it would be better to use the abbreviation rather than the full name.
3. On the 2nd line in the introduction, the citation is of the form "Name (year)". But the name is not a part of the sentence, thus it would be better to use the form "(Name, year)".
4. Above Eq. (1), "it's" should be "its".
5. The first paragraph in the introduction is too long (more than 1 page), and readers may lose the central idea easily. It would be better to separate it into several paragraphs.
6. Below Eq. (2), "maybe" should be "may be".
7. Significant digits or significant bits are not defined.
8. The form of citation of equations is not unified. Both "Equation 6" and "Eqn. 6" occur.

### Questions
There are many minor problems in this paper. Part of them are listed below.
1. In the tile, the colon is closer to proof rather than networks.
2. In the abstract, the abbreviation LNN appears on the 3rd line but its full name still occurs on the 10th line. After the abbreviation appears for the first time, it would be better to use the abbreviation rather than the full name.
3. On the 2nd line in the introduction, the citation is of the form "Name (year)". But the name is not a part of the sentence, thus it would be better to use the form "(Name, year)".
4. Above Eq. (1), "it's" should be "its".
5. The first paragraph in the introduction is too long (more than 1 page), and readers may lose the central idea easily. It would be better to separate it into several paragraphs.
6. Below Eq. (2), "maybe" should be "may be".
7. Significant digits or significant bits are not defined.
8. The form of citation of equations is not unified. Both "Equation 6" and "Eqn. 6" occur.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
