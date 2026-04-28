# Promoting Exploration in Memory-Augmented Adam using Critical Momenta

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 5, 3

## Abstract
Adaptive gradient-based optimizers, notably Adam, have left their mark in training large-scale deep learning models, offering fast convergence and robustness to hyperparameter settings. However, they often struggle with generalization, attributed to their tendency to converge to sharp minima in the loss landscape. 
To address this, we propose a new memory-augmented version of Adam that encourages exploration towards flatter minima by incorporating a buffer of critical momentum terms during training. This buffer prompts the optimizer to overshoot beyond narrow minima, promoting exploration.
Through comprehensive analysis in simple settings, we illustrate the efficacy of our approach in increasing exploration and bias towards flatter minima. We empirically demonstrate that it can improve model performance for image classification on ImageNet and CIFAR10/100, language modelling on Penn Treebank, and online learning tasks on TinyImageNet and 5-dataset.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a memory-augmented variant of the Adam optimizer that maintains a memory of critical momenta. The proposed method aims to address the gradient cancellation problem of Adam with critical gradients, encouraging exploration toward flatter minima. It is shown to improve performance across various tasks, including language modeling and image classification, by allowing the optimizer to escape sharp basins and converge in flatter regions.

### Strengths
The paper is well-written and clear, and uses both toy examples and real-world problems to demonstrate the effectiveness of the proposed method.

### Weaknesses
1. Prioritizing momenta with large gradient norms is not well motivated. It is unclear if and how this choice affects the performance of the method.
2. The paper seems to associate flat minima with global minima or lower loss values in some of the toy examples, which is not always the case in practice. Indeed, the training loss of a flat minimum is usually higher than that of a sharp minimum on real-world datasets.
3. The proposed method is partly motivated by the performance gap between SGD and Adam, but is not compared to SGD in the experiments. Moreover, it would be interesting to see if critical momenta improve the performance of SGD as well.
4. The baselines are not particularly strong, and it is a bit strange that Adam+SAM performs almost the same or even worse than vanilla Adam on image classification tasks.
5. The results shown in Fig. 5 could be sensitive to hyperparameters such as learning rate, which is not discussed in the paper.

### Questions
See above.

### Soundness
2 fair

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
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper introduces a memory-augmented version of Adam named Adam+CM, which maintains a buffer of critical momenta to enhance exploration and avoid sharp minima during training. The authors have conducted theoretical convergence analysis for the proposed method. Furthermore, they provided empirical results to substantiate the claims regarding the properties of the method. By presenting results in online learning and supervised learning scenarios (NLP + CV), the authors demonstrate that the proposed method achieves superior generalization performance compared to baseline methods.

### Strengths
- The proposed method is well-motivated, and to the best of my knowledge, it presents a novel approach to optimization.
- The presentation is lucid and easy to follow.
- The paper offers comprehensive evidence to back the primary claims, including theoretical analysis, numerical simulation results with toy examples, and real-world practical experiments.

### Weaknesses
 - (minor) The paper would be more convincing if larger-scale empirical experiments on NLP were conducted.

### Questions
- As a proposed deep learning optimization method, it would be more convincing if comparisons were made on larger-scale language model optimization tasks as well.

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
Building upon the framework of critical gradients, which maintains a buffer containing a limited history of gradients from previous iterations, this paper takes a similar approach by maintaining a buffer of previous momenta, which they call critical momentum (CM). The proposed method is expected to effectively escape sharp basins and converge to flat loss regions. They also investigate the effectiveness of combining CM with sharpness aware minimization (SAM).

### Strengths
The preliminary experiments using artificial loss functions such as the Goldstein-Price loss function and Ackley loss function show a clear advantage of CM variants to explore and find the lower loss surface near the global solution.

### Weaknesses
Although the experiments using artificial loss functions are promising, the results on actual deep neural networks is not as good. The fact that both CM methods overfit after convergence for LSTM on PTB in Figure 6 raises a major concern, and contradicts the main claim of the paper that CM methods can find a flatter minima.

The scores that are reported in this paper seem to be quite lower than what is reported in "papers with code". For example, EfficientNet-B0 on ImageNet should achieve a top-1 validation accuracy of 76.3% [https://paperswithcode.com/paper/efficientnet-rethinking-model-scaling-for], but the results reported in the paper range between 65.4-71.7%. Also, Adam+SAM is performing very poorly for this specific case, and is significantly worse than the original Adam, but no explanation is given for this poor performance.

It would seem like the current experiments would be strongly affected by the batch size, but the batch size is not included in their hyperparameter search.

### Questions
The escape ratio in Figure 5 is monotonically increasing with the sharpness coefficient. What happens if it is increased further?

In Figure 6, the validation perplexity of Adam+CM shows a peculiar behavior where it initially drops very fast but gradually increases and eventually crosses over with Adam+SAM. Is there any explanation as to why Adam+CM behaves this way when it is supposed to explore flatter regions compared to other optimizers?

Why is Adam+SAM performing so poorly for EfficientNet-B0 on ImageNet in Table 2?

Comments
The correspondence between the two plots in Figure 4 would be more obvious if the color of the lines were matched.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the challenge of poor generalization performance in adaptive gradient methods like Adam, hypothesizing that adding an exploration strategy with additional memory of gradient information could improve performance. Building on previous work, which used a memory buffer for storing "critical gradients," the authors propose a new memory-augmented Adam optimizer that stores "critical momenta" (CM). This new approach aims to prevent gradient cancellation and allows the optimizer to escape sharp minima and converge to flat regions which are more likely to generalize. The authors validate their approach through convergence analysis and empirical benchmarks, showing improvements in model performance in both supervised and online learning settings.

### Strengths
- The paper introduces a new concept of storing "critical momenta" in a memory buffer, aiming to overcome the limitations of previous memory-augmented optimizers.
- Intuitions for why this approach is helpful are built by analyzing toy functions.
- The method has potential applications in both supervised and online learning showing empirical improvements over vanilla Adam with combinations of CG/SAM.
- The paper is written with a clear structure and logical flow.

### Weaknesses
My main concerns are regarding the memory cost of the approach and whether these costs are justified given the plethora of other alternatives to Adam. The paper does not sufficiently discuss the computational overhead introduced by the memory component, which is critical for practical deployments, especially in resource-constrained environments. 

The experimental results indicate some improvements, but these could potentially be attributed to the additional use of memory and hyperparameters. It would be beneficial for the paper to discuss whether Adam+CM offers any regret guarantees or optimality conditions given the added computational complexity i.e. could there be another algorithm that does better? 

One potential alternative baseline that comes to mind is to consider averaging the weights via approaches such as Polyak averaging or Stochastic Weight Averaging. These methods have been shown to improve generalization performance and only require one additional copy of the parameters if one employs the exponential moving average trick. The paper could be strengthened by comparing Adam+CM to these alternatives--perhaps the two approaches are orthogonal.

### Questions
- I would consider additional measures of sharpness as well. For instance, it seems common to consider $|\lambda_{max}/\lambda_5| $ (Jastrzebski et al. (2020)) or measures of how quickly loss changes in a local neighborhood. The interaction between sharpness, distance travelled, and generalization performance seems quite complicated generally as it is also a function of the learning rate and other hyperparameters. This should be made clear in Figure 7 and Figure 8.
- In general, as mentioned in weaknesses, I would be interested in a more thorough study on how additional memory can best be used. It seems like C is generally set to 5 in the grid search -- can we get away with smaller $C$? What if we used a different value for CG and CM?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
