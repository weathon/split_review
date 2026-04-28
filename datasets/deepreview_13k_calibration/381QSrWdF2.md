# Law of Balance and Stationary Distribution of Stochastic Gradient Descent

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 8, 3

## Abstract
The stochastic gradient descent (SGD) algorithm is the algorithm we use to train neural networks. However, it remains poorly understood how the SGD navigates the highly nonlinear and degenerate loss landscape of a neural network. In this work, we prove that the minibatch noise of SGD regularizes the solution towards a balanced solution whenever the loss function contains a rescaling symmetry. Because the difference between a simple diffusion process and SGD dynamics is the most significant when symmetries are present, our theory implies that the loss function symmetries constitute an essential probe of how SGD works. We then apply this result to derive the stationary distribution of stochastic gradient flow for a diagonal linear network with arbitrary depth and width. The stationary distribution exhibits complicated nonlinear phenomena such as phase transitions, broken ergodicity, and fluctuation inversion. These phenomena are shown to exist uniquely in deep networks, implying a fundamental difference between deep and shallow models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
From the view of symmetry, this manuscript shows that SGD systematically moves towards a balanced solution when rescaling symmetry of loss function exists. The stationary distribution of model parameters of is also derived for simple diagonal linear networks. Many connections with other works also shown.

### Strengths
1. A novel view, symmery of loss, is provided for analyzing the solution of SGD and its stationary distribution. 
2. The derived stationary distribution under different factors, including learning rate, batch size, data noise, model width and depth, is analytically derived. This result explains many interesting observed phenomenon in practice or colloborates with exsiting findings in other works.

### Weaknesses
1. The diagram of phase transition is a special case or general, which should have been clarified. Specifically, the manuscript should explicitly state the conditions under which the observed phase transition occurs, and whether this is a general phenomenon or specific to the chosen data distribution. The current description lacks the necessary detail to assess the broader applicability of the results.
2. Given the symmetry view,  whether the diagonal linear network is a representative architecture for investigating SGD? Could the authors comment more regarding this? The analysis relies on a diagonal linear network, which is a highly simplified model. It is unclear how the insights gained from this model translate to more complex, non-linear architectures commonly used in deep learning. The authors should discuss the limitations of this model and the potential impact on the generalizability of their findings.
3. Another concern is that when conducting the analysis, a L2-norm regularization term is added. How does this affect all the derived results and further interpretation? The manuscript does not adequately address how the inclusion of L2 regularization affects the derived stationary distribution and the observed phase transitions. It's crucial to understand whether the regularization term is merely a technical convenience or if it fundamentally alters the behavior of SGD and the interpretation of the results. The interplay between the regularization strength and other parameters such as learning rate and batch size needs further clarification.

### Questions
See the above

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a law of balance phenomenon to better understand the SGD dynamics. Based on the proposed method, the authors have theoretically shown the unique properties separating the deep and shallow networks.

### Strengths
The theory is centered around the law of balance equation, which is clean and interpretable in some sense.

### Weaknesses
The theory is centered around the law of balance equation, which is clean and interpretable in some sense.

The boundness of the law of balance seems determined largely by the covariance matrices in equation 4. However, is there any guarantee on the condition of the matrices? what happens if the matrices are degenerate, and can you justify the matrices' degeneracy matter in practice?

### Questions
I would like to know more details about the case when the matrices are degenerate or justifications that they are non-degenerate.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors show that the noise of SGD from minibatching regularizes the solution towards a "balanced" solution whenever rescaling symmetries are present in the loss function. They then apply these results to derive the stationary distribution of SGD for a diagonal linear network. Then the authors characterize this stationary distribution, showing such phenomena as: phase transitions, loss of ergodicity, and fluctuation inversion. They show that these properties exist uniquely in deep networks, thus delineating a difference between deep and shallow networks.

### Strengths
- The paper provides new insights into the behavior of stochastic gradient descent (SGD), such as: how the Langevin model is flawed in studying SGD, that the noise in SGD creates a qualitative difference between it and gradient descent (GD), analysis between networks with and without depth, loss of ergodicity, among many others. 
- Characterizing the stationary distribution of SGD analytically.
- Provided insights into why the Gibbs measure is bad for SGD.
- The paper is original, and very clearly written.

### Weaknesses
 - The most complicated model they analyzed was a linear deep diagonal network, but I can imagine the general case being extremely difficult.

### Questions
- Can the properties found for SGD, such as "the qualitative difference between networks with different depths, the fluctuation inversion effect, the loss of ergodicity, and the incapability of learning a wrong sign for a deep model" be extended to loss functions without rescaling symmetries?

- How well do you believe the results in the paper transfer to nonlinear neural networks (i.e. with a nonlinear activation function)?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work considers (mini-batch) SGD on loss functions with re-scaling symmetry. This work shows that SGD tends to find a solution with balanced weights. Furthermore, this work also analyzes the stationary distribution induced by a continuously approximated SGD for a diagonal linear network, where several complicated behaviors of SGD are discussed, such as phase transition, loss of ergodicity, and fluctuation inversion.

### Strengths
+ The focus of this work, that is, the behavior of SGD, is an important and relevant topic to the community. 
+ Some of the findings on the differences between SGD and (noisy) GD might be interesting.
+ The calculation of the stationary distribution of SGD for diagonal linear networks should be new to my knowledge.

### Weaknesses
 - Some statements/writing are not precise and might be misleading. See more in the Question section. 
- Some messages are already known from prior papers. For example, it is known (references are actually mentioned in this work) that SGD should not be approximated by gradient flow or gradient Langevin dynamic and that the SGD noise is parameter dependent. This paper should have been more careful in terms of clarifying the contributions. 
- Not sure how relevant is the theory in this paper to practice. See more in the Question section.



### Questions
1. Discussions before Theorem 1. "....For example, it appears in any neural network with the ReLU activation". This might not be true. For example, $(u \\max \\{ w x, 0 \\} -y)\^2$ is rescaling symmetric only for non-negative $\\lambda$. 

2. Theorem 1 and the follow-up discussions. Note that $C\_1 $ and $C\_2$ are functions of $u$ and $v$. Therefore, $\\lambda\_{1m}, \\lambda\_{1M}, \\lambda\_{2m}, \\lambda\_{2M}$ are not constants but functions of $u$ and $v$. Hence, eqs (5) or (6) do not directly imply that $u$ and $v$ are approximately balanced. Could the authors make some clarifications? 

3. Discussions after eq (8). There seems to be a typo in the display after "....can be upper-bounded by an exponentially
decreasing function in time:...". Please clarify. 

In addition, in eq(7), the coefficient $\\alpha\_1 v\^2 - 2\\alpha\_2 v  + \\alpha\_3$ is not a constant but a function of $v$ (hence a function of $u$ and $w$). So the statement that "....can be upper-bounded by an exponentially decreasing function in time" might not be accurate. 

4. Discussions after eq (9). There might be a typo in the definition of $C(v)$. It should be the variance of the gradient of the loss. 

5. "These relations imply that $C$ can be quite independent of $L$, contrary to popular beliefs in the literature...". Here, should the word "independent" be revised to "dependent"? 

6. The diagonal linear network studied in this paper takes a 1-dimnensional input. However, prior works consider diagonal linear network with a multivariate input. So the setting in this work might be limited compared to prior works. 

Overall, I feel the theory in this work is not entirely precise. Plus, the model setup is limited, and the results might not be general and might be strongly rely on this particular setup.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
