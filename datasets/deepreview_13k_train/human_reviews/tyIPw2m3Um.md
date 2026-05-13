# Probability-dependent gradient decay in large margin softmax

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
In this paper, a gradient decay hyperparameter is introduced in Softmax to control the probability-dependent gradient decay rate. By following the theoretical analysis and empirical results, we find that the generalization and calibration depend significantly on the gradient decay rate as the confidence probability rises, i.e., the gradient decreases convexly or concavely as the sample probability increases. Moreover, optimization with the small gradient decay shows a curriculum learning sequence where hard samples are in the spotlight only after easy samples are convinced sufficiently, and well-separated samples gain a higher gradient to reduce intra-class distance. Unfortunately, the small gradient decay exacerbates model overconfidence, shedding light on the causes of the poor calibration observed in modern neural networks. Conversely, a large gradient decay significantly mitigates these issues,  outperforming even the model employing post-calibration methods.
Based on the analysis results, we can provide evidence that the large margin Softmax will affect the local Lipschitz constraint by regulating the probability-dependent gradient decay rate.
This paper provides a new perspective and understanding of the relationship among large margin Softmax,  curriculum learning and model calibration by analyzing the gradient decay rate. Besides, we propose a warm-up strategy to dynamically adjust gradient decay.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a modification to softmax when using softmax in conjunction with cross-entropy for classification tasks to combat the following problem: when the magnitude of the partial derivative of the softmax with respect to the class outputs decays rapidly, model tends to overfit (but converges faster). On the other hand, if the magnitude of the partials decays too slowly, the model takes a longer time to converge (but tends to generalize better). The modification introduces a hyperparameter $\beta$ where small $\beta$ encourages rapid decay of the partials while large $\beta$ encourages slow decay of the partials. To combine the best of both worlds, the paper proposes a warm-up scheme by starting with a small $\beta$ so that the model will converge quickly and then increase $\beta$ to discourage overfitting and overconfidence.

### Strengths
Paper proposes a simple modification to softmax in conjunction with a warm up scheme with respect to the margin parameter $\beta$ to get faster convergence and better generalization.

### Weaknesses
The warm-up scheme does not seem to provide a significant advantage over prior proposed modifications to softmax (e.g A-softmax) or does worse according to table 2 in the paper. The paper's core idea of modulating gradient decay via a hyperparameter $\beta$ is interesting, but the experimental results do not strongly support the effectiveness of the proposed warm-up schedule. Specifically, while the method aims to combine the benefits of fast convergence (small $\beta$) and better generalization (large $\beta$), the results presented in Table 2 indicate that the warm-up schedule does not consistently outperform a fixed, large $\beta$ value. This raises concerns about the practical utility of the proposed dynamic adjustment of $\beta$. Furthermore, the paper lacks a detailed analysis of how the choice of the warm-up schedule (e.g., the rate of increase of $\beta$) affects the final performance, making it difficult to understand the sensitivity of the method to this hyperparameter.

### Questions
What does the training loss look like across epochs for the warm-up schedule (more specifically could you plot another curve in figure 5 displaying the loss over epochs for the warm-up schedule)?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the influence of introducing a margin parameter $\beta$ in the softmax operator for classification problems. The idea is to relate the margin parameter $\beta$ to the decay rate of the gradients so that the classification confidence can be manipulated. The margin parameter also gives rise to some improved performance in image data. I would view the margin parameter $\beta$ as the major contribution of the paper, as existing study often focuses on the temperature parameter.

### Strengths
The paper provides a very detailed guide to understand the influence of the margin parameter $\beta$ on the decay rate of the gradient. The study looks comprehensive and correct, which leads to the successful empirical verification.

Most of the paper is well organized, although some part needs additional care.

### Weaknesses
Section 2 needs a revision. See more in questions section.

As far as I can tell, the classification error improvement is a bit marginal. The baseline accuracy should correspond to $\beta = 1$ and the highlighted best obtained errors may not have significant improvement. Although this evaluation might be objective, but this concern can be partially addressed by providing a standard deviation computed in multiple runs, so that the statistical significance can be verified.

Given the concerns above, I am giving a negative rating. However, I am willing to discuss with the authors on the significance of the proposed method and potentially raise the score.

### Questions
The grammar around Equations (1) -- (6) should be polished.

In Equation (4), (5) and (6), is there a bracket around $z_i - z_c$?

What is hidden in the approximate equality in Equation (5)?

Figure 3 has a vague description: "confidence of some samples during training". The font in the figures is small.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the impact of adding a $\beta$ term in the softmax equation. Let $m$ be the number of classes, they propose:
$$p = \frac{e^x}{\sum_i e^{x_i} + \beta e^x}, \quad \text{with } x \in R^{m}, \text{and } p \in R^{m}$$
When used alongside the cross-entropy loss, the formulation of the loss on a training sample $(x,y)$ becomes:
$$\ell(x,y) = -\log(p_y) = - \log(\frac{e^{x_y}}{\sum_i e^{x_i} + \beta e^{x_y}}) $$
They show how $\beta$ enforces a soft margin and modulates the gradient magnitude depending on the probability $p_y$. More precisely, they show how small $\beta$s increase the gradient magnitude for larger probabilities---promoting a soft margin---, while larger $\beta$s reduce the gradient magnitude for larger probabilities. They theoretically derive this observation and validate it empirically on $4$ vision datasets. Moreover, they draw a parallel with curriculum learning and calibration.

### Strengths
I find this work well motivated: the softmax function is ubiquitous in modern machine learning and studying its various caveats is important. 
The connection with calibration is interesting, and the results in figure 6 are very promising. Especially, the calibration improves as $\beta$ increases, which allows the model to be less influenced by current samples having a $p_y$ close to $1$.

### Weaknesses
I found two main weaknesses in this work. The first one consists of the overall lack of clarity. I find the paper hard to read. Here are some parts I found confusing:
- "MSE takes into account more complex optimization scenarios": What do you mean by that?
- "Hard mining strategy": you could briefly introduce what this is. 
- in section 2, you talk about $J_j$ before introducing it
- In figure 3: there are no legends for the top row, and the caption does not help to clarify the different curves being shown, the main text is also unclear about those i.e. what are "post-training samples", are those test samples? 
- In figure 3 still, it should be mentioned in the legend or in the caption that the different groups correspond to samples of varying difficulty
- "If we make excessive demands on the margin, some post-training samples cannot get any chance and will be "sacrificed" according to the soft curriculum learning strategy [...]", what do you mean? 
- "So it is convinced that the general softmax [...]"
- "The beta smaller is, the gradient smoother is"
- "Warm-up strategy achieves even better results."
- "Curriculum design that divides samples is crucial to curriculum learning idea."
- "Besides, based the previous analysis [...]"
- In figure 6: the y axis mentions accuracy and but also shows confidence, this is confusing and could be clarified in the caption. 

The second weakness is the lack of rigor in the experiments: 
- In figure 4: which model is being used? How many parameters? How were the hyperparameters tuned? Are those averaged over multiple seeds, if yes can we see the standard deviation? 
- In table 2: The different values are quite close, and it is difficult to evaluate the robustness of the improvement without standard deviation. It should be possible to run the same experiment with different seeds for some of the smaller datasets. 
- In table 3: same as above, I would love to see standard deviations 
- For all the experiments, which experimental protocol was followed: which architecture, tuning, seeds, optimizer, ... I couldn't find those in the appendix either

### Questions
See above.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
