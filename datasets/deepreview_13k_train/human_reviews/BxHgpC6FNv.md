# Benign Overfitting and Grokking in ReLU Networks for XOR Cluster Data

- Decision: Accept
- Scores: 6, 6, 5

## Abstract
Neural networks trained by gradient descent (GD) have exhibited a number of surprising generalization behaviors. First, they can achieve a perfect fit to noisy training data and still generalize near-optimally, showing that overfitting can sometimes be benign. Second, they can undergo a period of classical, harmful overfitting---achieving a perfect fit to training data with near-random performance on test data---before transitioning (``grokking'') to near-optimal generalization later in training. In this work, we show that both of these phenomena provably occur in two-layer ReLU networks trained by GD on XOR cluster data where a constant fraction of the training labels are flipped. In this setting, we show that after the first step of GD, the network achieves 100\% training accuracy, perfectly fitting the noisy labels in the training data, but achieves near-random test accuracy. At a later training step, the network achieves near-optimal test accuracy while still fitting the random labels in the training data, exhibiting a ``grokking'' phenomenon. This provides the first theoretical result of benign overfitting in neural network classification when the data distribution is not linearly separable. Our proofs rely on analyzing the feature learning process under GD, which reveals that the network implements a non-generalizable linear classifier after one step and gradually learns generalizable features in later steps.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper analyzes two-layer ReLU network trained by gradient descent on XOR cluster data with a high-dimensional input space, and rigorously proves grokking and benign overfitting occurs.

Specifically, with one sufficiently large gradient step, the network is almost a linear classifier and achieves perfect overfitting to the training data, which contains label-flipping noise. If training is continued, the model almost perfectly predicts the clean label, while keeping perfect overfit to the training data.

### Strengths
### Notable results on benign overfitting of neural networks beyond linearly separable data

As far as I understand, proving benign overfitting for neural network involves several difficulties due to its nonlinearity, and especially I agree that showing the superiority of neural network to linear methods by learning nonlinear target function has been largely open in this context. I think XOR cluster data is a good starting point to this problem and this paper proves benign overfitting under moderate assumptions.

### Providing useful theoretical understandings on grokking

As well as benign overfitting result, this paper also proves that after one large (compared to the initialization scale) gradient step, the neural network approximately behaves as the linear model and perfectly overfit to the training data. The phenomena that the early stage of training only produces the linear model but there is a transition to the nonlinear neural network with richer features is particularly interesting, providing one of the first rigorous theoretical demonstrations of grokking.

### The paper is well written and clearly explaining its theoretical key points.

The proof sketch section is well-written and provides a sufficient understanding of the overall theoretical contributions. It is expected that the techniques presented in this paper will also be valuable in demonstrating the potential for more enriching feature learning in the future.

### Weaknesses
### Justification of the small initialization

In my understanding, it is crucial to take a small initialization scale compared to the step size $\alpha$ to obtain the perfect overfitting at the first gradient step. I think this is acceptable as theory, but it should be better to justify such a small initialization, especially in the context of practical applications where larger initializations might be preferred. I also want to know what happens if the initialization scale is much larger than used in Figure 3. Specifically, how does the behavior of the model change, and does grokking still occur? An empirical investigation into the effects of varying initialization scales on the model's performance would be highly beneficial.

### Large signal-to-noise ratio

Compared to [1,2,3,4,5], where $x$ is a $d$-dimensional (essentially) rotationally invariant input and $y=\rm{sgn}(x_1x_2)$, this paper considers large signal $\|\mu\|$ as an input. This choice, while theoretically interesting, raises questions about the practical applicability of the findings. In real-world scenarios, data is often characterized by lower signal-to-noise ratios. It would be valuable to understand how the model's behavior changes as $\|\mu\|$ decreases, and whether the observed grokking phenomena persist under such conditions. A theoretical analysis or empirical study exploring the impact of varying $\|\mu\|$ on the model's performance would significantly enhance the paper's contribution.

### Questions
- Is it possible to see an additional experiment when the initialization scale is not so small?

- When $\|\mu\|$ gets small, is this grokking phenomena still observed?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper delves into the exploration of benign overfitting and "grokking" in two-layer ReLU neural networks when trained on XOR cluster data with noisy labels. The authors demonstrate that networks can perfectly fit noisy training data (benign overfitting) and, after a period, transition from harmful overfitting to a stage where they generalize near-optimally ("grokking"). Through rigorous theoretical analysis and proofs, the study reveals that these surprising phenomena are evident in the networks' training trajectories, providing a nuanced understanding of overfitting and generalization in neural network models.

The paper's contributions lie in providing the first theoretical insights into benign overfitting in non-linearly separable data distributions, unraveling the feature learning dynamics under gradient descent. These findings illuminate the pathways through which neural networks navigate the complexities of noisy data, offering a fresh perspective on their capacity to generalize despite apparent overfitting.

### Strengths
* The paper offers a new theoretical examination of benign overfitting and "grokking" in two-layer ReLU neural networks. It focuses on XOR cluster data with noisy labels, giving a detailed exploration and proofs related to these phenomena. The authors use existing concepts and new theories to better explain the behavior of neural networks with noisy training data.

* The paper is structured and clear, effectively communicating the authors’ work and results. It has a logical organization that makes it easy for readers to follow the ideas and analyses. The presentation of definitions, explanations, and proofs is mostly straightforward, helping readers understand the complex concepts and findings.

* The paper is important because it helps understand overfitting and generalization in neural networks better. It explains the concepts of benign overfitting and "grokking" in one framework.

### Weaknesses
 * The assumption made in A1 seems to contradict common understanding. Generally, increasing the number of samples, even with limited noisy labels, tends to enhance the generalization capability of neural networks. However, in Assumption A1, having a larger number of training samples seems to adversely affect the model, as indicated by its presence on the right-hand side of the inequality. This aspect might require further clarification or justification within the context of the study. Specifically, the inequality in A1, which involves $n$, appears to suggest a negative correlation between sample size and model performance, which is counterintuitive and needs more detailed explanation of why this specific bound is necessary for their theoretical analysis, and what specific aspect of the model or data necessitates this bound.

* The mechanism of overfitting, once the neural network learns the directions of $u_1$ and $u_2$. is not explicitly clear. The paper mentions that post the initial gradient step, positive neurons learn $u_1$ while negative neurons learn $u_2$. However, the explanation seems lacking in how the network overfits to samples with noisy (flipped) labels in this condition. A more detailed discussion or clarification on how the network's weights evolve to memorize the noisy labels, given the initial learning of $u_1$ and $u_2$, would be beneficial. It is unclear how the network distinguishes between correctly labeled and incorrectly labeled data points after the initial feature learning phase.

* The role of Lemma 4.6 in the paper is unclear. A clearer explanation of how it relates to other parts of the paper and how it contributes to the overall arguments and conclusions is needed for better understanding. The paper does not explicitly explain how this lemma is crucial for the subsequent analysis, and it would be helpful to have a more detailed explanation of how it connects to the main results, and why it is necessary for the approximation in Equation (4.3).

* The paper seems to lack a comparative discussion with some relevant works, specifically references [1,2].

### Questions
* Could you provide more insights or justification regarding Assumption A1? Specifically, could you clarify why an increase in the number of training samples seems to negatively influence the model, contrary to the common understanding that more samples generally improve a model's generalization capability?

* Could you elaborate on the mechanism of overfitting after the neural network learns the directions of $u_1$ and $u_2$.

* Could you clarify the role and significance of Lemma 4.6 in the context of the paper's objectives and findings?

* Could you make a comparsion your results and techniques with [1] and [2]?

* Have you considered variations in the network architecture, such as not fixing the second layer, and if so, how do these variations influence the results?

* In the model settings used in the paper, there doesn’t appear to be an upper bound on the network width. If an extremely wide network setting were used, would the findings align with the "lazy training" regime? Could you discuss how the results might be influenced by varying the width of the network to such extremes?

I would increase my score if the authors could clarify my concerns demonstrated in the above questions.

--------------------------------------
I increase my score to 6 after rebuttal.

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
This paper theoretically combines the phenomena of benign overfitting and Grokking by training a two-layer ReLU neural network using gradient descent on XOR cluster data. The authors demonstrate that after the first step of gradient descent, the network achieves 100% training accuracy, perfectly fitting the noisy labels in the training data, but exhibits nearly random performance on the test data. However, after some time in training, the Grokking phenomenon occurs, and the network achieves near-optimal test accuracy while still adapting to the random labels in the training data, demonstrating benign overfitting.

### Strengths
This paper is the first to study the combination of benign overfitting and the Grokking phenomenon in neural networks.

### Weaknesses
My main concern about this paper lies in its assumptions. Combining assumptions A1 and A2, we can obtain $p\geq C^4 n^{5.02}$. This is an extremely high-dimensional setting. The authors provide a theoretical analysis of the Grokking phenomenon in the context of benign overfitting, but the practical relevance of the result is limited by the extremely high dimensionality required. The condition $p \geq C^4 n^{5.02}$ is significantly more restrictive than what is typically seen in practical applications of neural networks, and it is not clear if the same phenomena would occur in more realistic settings with lower dimensionality. This raises concerns about the generalizability of the theoretical findings to real-world scenarios. Furthermore, the paper does not adequately address the limitations imposed by this high-dimensional assumption, nor does it explore the potential for achieving similar results under less restrictive conditions.

### Questions
1: Do the authors have any ideas for improvements in the high-dimensional setting?

2: What behavior does the test error exhibit when the training time is between 1 and $n^{0.01}$?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
