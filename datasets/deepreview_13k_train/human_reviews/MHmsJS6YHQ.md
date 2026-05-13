# Interpolate: How Resetting Active Neurons can also improve Generalizability in Online Learning

- Decision: Reject
- Scores: 5, 5, 3, 5

## Abstract
While neural networks have shown a significant gain in performance across a wide range of applications, they still struggle in non-stationary settings as they tend to lose their ability to adapt to new tasks — a phenomenon known as the loss of plasticity. The conventional approach to addressing this problem often involves resetting the most under-utilized or dormant parts of the network, suggesting that recycling such parameters is crucial for maintaining a model's plasticity. In this study, we explore whether this approach is the only way to address plasticity loss. We introduce a resetting approach based on model merging called Interpolate and show that contrary to previous findings, resetting even the most active parameters using our approach can also lead to better generalization. We further show that Interpolate can perform similarly or better compared to traditional resetting methods, offering a new perspective on training dynamics in non-stationary settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a resetting-based method to address the plasticity loss issue in non-stationary learning settings, such as online learning. The authors empirically demonstrate that resetting the most active parameters can yield performance improvements, contrasting with previous findings. The method, called Interpolate, combines this reset-based approach and model merging. Empirical experiments on the CIFAR-10 dataset show that this method achieves competitive performance when compared to other approaches.

### Strengths
- This paper provides a clear background, making it accessible to readers unfamiliar with the problem.
- The approach of resetting active/inactive parameters is intriguing.
- The authors compare the proposed method with other approaches such as ReDo and CBP across different types of distribution shifts on a benchmark dataset (CIFAR-10).

### Weaknesses
 - The authors need to conduct additional experiments to thoroughly test their hypothesis and validate the proposed method. The current results are limited to a few experiments on the CIFAR-10 dataset with relatively simple neural network architectures, which raises concerns about the robustness of these findings. Testing on a broader range of datasets (e.g., CIFAR-100 or noisy datasets), more complex network architectures (e.g., ResNet or other high-capacity networks), alternative utility functions, and different problem domains (e.g., deep reinforcement learning) would provide stronger empirical support for the claims made in the paper

 - While the improvements via resetting the most active parameters are intriguing, the paper does not explain why these effects occur, particularly in contrast with the original ReDo paper. I am curious whether the dormant neuron phenomenon observed in ReDo is also present here. Additionally, while this paper uses the dormancy score as a utility function, I am uncertain whether the authors’ claims hold when alternative metrics (e.g., Zhou et al. [1]) are used to assess neuron importance

 - The ratio between $\theta$ and $\theta_{perm}$ in Eq. (2) likely has a substantial impact on neural network learning dynamics. The authors used a midpoint merge between $\theta$ and $\theta_{perm}$, but it would be informative to understand how different ratios might affect outcomes

 - I am unclear why the authors did not use the optimal hyper-parameters from Sec. 4.4 in the experiments shown in Fig. 2. Using consistent hyper-parameters could improve result interpretability.

 - The phenomenological findings on the impact of resetting active parameters appear loosely connected to the proposed Interpolate method. While this relationship might align with the question raised in lines 50-51, it is known that ReDo is not the only way to reactivate a model. A clearer explanation of how these findings connect would strengthen the paper


 - In line 172, it is unclear why parameters $\phi_k$ are in $\mathbb{R}^k$.
 - The experimental details provided are insufficient for full comprehension. While references are given, this paper should contain specific details on the datasets used (lines 221-222), task composition, definitions for terms like ‘reset with random noise’ in Sec. 4.1, ‘Dormancy’ in Fig. 2, etc.
 - In Sec. 4.1, how many runs were averaged to obtain the results? Also, the term ‘jump in training loss’ in Fig. 1 is not clearly defined.
 - Please provide the hyper-parameters used for each method in Figs. 2 and 3.
 - Why does the number of tasks (x-axis) differ in Fig. 3?
 - In line 188, there exists a typo: $pi_k$ should be $\pi_k$.

### Questions
### Major
- While the improvements via resetting the most active parameters are intriguing, the paper does not explain why these effects occur, particularly in contrast with the original ReDo paper. I am curious whether the dormant neuron phenomenon observed in ReDo is also present here. Additionally, while this paper uses the dormancy score as a utility function, I am uncertain whether the authors’ claims hold when alternative metrics (e.g., Zhou et al. [1]) are used to assess neuron importance

[1] Zhou, Hattie, et al. "Fortuitous forgetting in connectionist networks." arXiv preprint arXiv:2202.00155 (2022).

- The ratio between $\theta$ and $\theta_{perm}$ in Eq. (2) likely has a substantial impact on neural network learning dynamics. The authors used a midpoint merge between $\theta$ and $\theta_{perm}$, but it would be informative to understand how different ratios might affect outcomes

- I am unclear why the authors did not use the optimal hyper-parameters from Sec. 4.4 in the experiments shown in Fig. 2. Using consistent hyper-parameters could improve result interpretability.

- The phenomenological findings on the impact of resetting active parameters appear loosely connected to the proposed Interpolate method. While this relationship might align with the question raised in lines 50-51, it is known that ReDo is not the only way to reactivate a model. A clearer explanation of how these findings connect would strengthen the paper


### Minor
- In line 172, it is unclear why parameters $\phi_k$ are in $\mathbb{R}^k$.
- The experimental details provided are insufficient for full comprehension. While references are given, this paper should contain specific details on the datasets used (lines 221-222), task composition, definitions for terms like ‘reset with random noise’ in Sec. 4.1, ‘Dormancy’ in Fig. 2, etc.
- In Sec. 4.1, how many runs were averaged to obtain the results? Also, the term ‘jump in training loss’ in Fig. 1 is not clearly defined.
- Please provide the hyper-parameters used for each method in Figs. 2 and 3.
- Why does the number of tasks (x-axis) differ in Fig. 3?
- In line 188, there exists a typo: $pi_k$ should be $\pi_k$.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes a new plasticity injection method called “Interpolate” for neural networks. It periodically chooses top-k active neurons and readjusts the corresponding model parameters based on “model merging”: it takes an average between itself and a functionally equivalent parameter (established by exploiting permutation invariance). The authors evaluate their method over three types of distribution shifts on CIFAR10 datasets, using MLP with three hidden layers and CNN with two convolutional layers.

### Strengths
S1. This work contains an interesting empirical finding. It reveals that the most active neurons can be the subjects of resetting, like the most dormant neurons (e.g., ReDo), for injecting adaptability to a neural network. This is intriguing because, as far as I know, a common belief on why resetting works is that it “awakes” the dormant neurons. On the contrary, this work shows that readjusting the most active neurons can also be beneficial for maintaining plasticity.  
S2. As far as I know, it is new to apply model merging (based on the permutation invariance of neural networks) when partially resetting the model to enhance the plasticity.

### Weaknesses
Overall, there seems to be a huge room for improvement in the writing and presentation of the paper, so I lean to reject it. Below, I list the reasons.

**W1. The paper lacks intuitive motivation or a mechanistic understanding of the proposed method.**

- To claim that the methodology is useful and powerful, an academic paper should explain **why** it works by providing the following: motivation, underlying mechanism, extensive ablation study on every component of the method, and theoretical guarantees (if possible). However, I cannot find any intuitive motivation or rigorous verifications of why the proposed method works. As I understood, the paper only proposes a method and exhibits its numerical performance.
- Resetting the dormant neurons, as mentioned in the introduction, may mitigate the loss of plasticity because it “recycles dormant neurons back into an active state to recover some of the network’s capacity.” Then, why would unlearning the most active neurons help models maintain their plasticity? Is there any underlying idea about it?
- In Section 4.1, the authors demonstrate that taking an average (i.e., interpolation) of two functionally equivalent model parameters might be a better resetting method than random resetting in terms of the test-time performance. They provide a plausible reason for this: random noise results in greater forgetting. However, if that is the case, is the interpolation a unique answer? I don’t think so. Then why did the author choose to take interpolations? (Let me extend the discussion about the implementation choice later in **W2**) In short, the authors should have provided the reason for the particular implementation choice of their resetting method to convince the readers.

**W2. The experimental results in the paper are insufficient to explain the proposed method’s effectiveness.**

- As admitted by the authors, their resetting method is quite unnatural and too specific. Several variants of the proposed resetting method exist, which should have been tested and compared with their original method.
    - The number of functionally equivalent parameters to take an average: why two? It can be three or more. The paper does not explore the impact of using more than two functionally equivalent parameters, which could reveal whether the averaging operation itself is crucial or if any combination of these parameters would suffice. Furthermore, the choice of averaging, as opposed to other combination methods, is not justified.
    - Mixing ratio: why half and half? It can be generalized to $\lambda \theta_{\tt perm} + (1-\lambda) \theta$, or even generalized to $\sum_{i=1}^m \lambda_i \theta_i$ where $\sum_{i=1}^m \lambda_i = 1$, $\lambda_i > 0$ for all $i$, and $\theta_i$’s are all functionally equivalent parameters to the original $\theta$. The paper lacks a thorough investigation into how different mixing ratios affect the performance. It is unclear whether a 50/50 split is optimal or if other ratios might yield better results. This is particularly important given that the interpolation weight could significantly influence the degree of forgetting or adaptation.
    - The choice of $\theta_{\tt perm}$: why is it uniformly randomly chosen? Even though there are several functionally equivalent parameters, they are only identical regarding the function value. They might not be equivalent in terms of the loss landscape (e.g., gradient, sharpness). Note that there is an optimization technique called teleportation [1], which also exploits the parametric invariance to accelerate the optimization or enhance the generalization capability. Based on this idea, can we choose a “better” $\theta_{\tt perm}$ to maintain the network’s adaptability and generalizability? The paper does not explore the possibility of selecting $\theta_{\tt perm}$ based on criteria other than random selection, such as gradient alignment or sharpness of the loss landscape. This could potentially lead to more effective resetting strategies.
    - If the random resetting harms the networks’ generalizability due to a sudden change in active parameters, which induces greater forgetting, what if we add a small noise to the original parameter? Or should we blend the model parameter only with functionally equivalent parameters instead of random noises? The paper does not explore alternative methods of perturbing the parameters, such as adding small noise or blending only with functionally equivalent parameters. This limits the understanding of the specific benefits of the proposed interpolation method.
    - More comparisons with other resetting methods, such as Shrink & Perturb [2], resetting the last few layers [3,4], or DASH [5], would strengthen the authors’ contributions. The paper lacks a comprehensive comparison with other state-of-the-art resetting methods, which makes it difficult to assess the relative merits of the proposed approach.
- Figure 2: it is somewhat questionable that the authors did not perform any hyperparameter tuning here when they compared several variants of Interpolate and ReDo. The default hyperparameter might be unexpectedly/fortunately tailored to “Interpolate (active: 20%)”. For a better comparison, I think the hyperparameter search must be done here. Also, I don’t see why the paper chose particular values for resetting ratios (5% or 20%). It would be nice to provide more ablations on resetting ratios, or the paper should explain why they present only the 5% and 20% results.
- Figure 3: it should display the results of 100%/0% and 0%/100% as well for better visualization. Also, what if the combining ratios do not sum to 100%, i.e., what if there are non-reset parameters? The paper does not explore the impact of not resetting all parameters, which could provide insights into the necessity of resetting all or only a subset of the network.
- Statistical significance: the paper only reports averages over five random seeds. To showcase the stability and statistically significant guarantees of the proposed methods, it would be nice to report medians, interquartile means (IQMs), and confidence intervals (See [6]). The paper lacks a rigorous statistical analysis of the results, which makes it difficult to assess the robustness of the proposed method.
- More experimental details are necessary. For example, the paper should report the batch size, the exact model architecture (e.g., whether normalization layers are used), and running time (i.e., wall-clock time). The paper lacks crucial experimental details, which makes it difficult to reproduce the results and assess the practical applicability of the proposed method.
- The page limit was up to ten pages for the main text. However, this paper consumes only eight pages for the main text, two for references, and two for the appendix. Although this is not a direct reason for the rejection, I can’t help but suspect the insufficiency of the paper’s content in passing the acceptance bar.

**W3. Minor comments on typos and writing issues.**

- The term “model merging” is a bit misleading. It often refers to a method of ensembling several models to maintain or improve the overall performance of the model(s) [7]. On the contrary, this paper uses the term for a resetting/unlearning strategy.
- Misleading notation in Algorithm 1:
    - $D$ is originally an input dataset but turns into a list of dormancy scores.
    - “for $t=1,2,\ldots,|H|$”: I guess $i$ must be used instead of $t$.
- Until Section 3, the letter $k$ refers to the *number* of neurons to be reset. However, in Section 4.2, the $k$ becomes the *proportion* of the neurons to be reset.
- The caption of Figure 2: “Apply Interpolate” $\rightarrow$ “Applying Interpolate”.
- Appendix A: the last sentence has double full stops (”..”).

### Questions
**Q1. Decision of hyperparameters**

- The main hyperparameter of Interpolate is $k$, the number of neurons to apply the interpolation resetting. Practically, how should we determine the value of $k$?

**Q2. Why can resetting the most active neurons achieve comparable performances as resetting the least active neurons?**

- Can we achieve better generalizability with resetting neurons (than without resetting) regardless of their dormancy?
- Have you tried the random selection of neurons to reset? It could be absolutely random or structurally random (e.g., randomly select a layer and reset them all).
- On top of that, why does the vanilla SGD (i.e., not resetting any parameters at all and warm-starting the network at the beginning of every task, if I understood correctly) exhibit a similar performance as the resetting-based method? This seems quite different from the existing observations (e.g., [2], bringing the same numbering of the reference as in Weaknesses).

**Q3. Degradation due to the larger number of epochs**

- In Figure 3, if the learning algorithms run for 10 epochs per task, the optimal combination of ReDo (inactive) and Interpolate (active) seems 10%/90%. However, when increasing the number of epochs per task, the performance significantly drops and this combination becomes the worst. Why does it happen?
- Because of this, I am worried that the optimal combination ratio of ReDo (inactive) and Interpolate (active) might be highly sensitive to the training setups.

**Q4. The exact definition of “permutation function”**

- Section 3.2 illustrates how the interpolation-based resetting works, except for explaining the exact form of the permutation function. What does it look like in a math equation form?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work shows a new empirical insight to address the loss of plasticity, a tendency of neural networks (NNs) to lose their ability to adapt to new tasks in non-stationary settings. The authors show in their experiments that even resetting the most active parameters could be an alternative way to address the loss of plasticity, in contrast to previous studies that reset the inactive neurons. Two main results are highlighted. First, the results comparing the different utility functions for selecting which neurons to reset. Second, the performance of the proposed Interpolate method, which exploits the model merging using permutation invariance. Based on these results, the authors present experimental results across different distribution shift scenarios on simple MLP and CNN settings, which show comparable performance to existing baselines.

### Strengths
Providing a empirical evidence that resetting the active neurons can help NNs overcome the loss of plasticity, which is a new insight to this field of study, is a strength of this work.

Section 4.1 shows the effect of reset function, specifically comparing the Interpolate and random noise (same random distribution as the NN initialization). As the authors mentioned, many prior works utilizes random noise same to the initialization to reset, and the comparing this to the proposed Interpolate is a strength of this work.

Section 4.2 then presents the effect of utility function by comparing several candidates of choices for which neurons to reset. While this result does not show a definite trend to explain the effect of utility function, identifying that the choice of utility function that chooses the active neurons is a strength of this work.

### Weaknesses
Overall, I don't expect Interpolate or Interpolate+Redo to beat other resetting methods, for example in Figure 4, where the authors suggest that Interpolate-based methods maintain competitive performance, which I acknowledge that resetting non-dormant neurons is indeed a new insight. However, I would argue that this perspective should be accompanied by more extensive analysis (either empirical or theoretical). Below are some of the examples that I think should be not left undiscussed.

1. How is it guaranteed that the merged model itself provides an appropriate place for reset? While I see that the last paragraph (lines 194-197) in Section 3.2 tries to give an explanation for this, however I see no empirical evidence to support it. For example, comparison between $\theta$, $\theta_\text{perm}$, $\theta_\text{reset}$, $\theta_\text{reset}+\epsilon$, (where $\epsilon$ is random perturbation of the model), or averageing more than two permuted model ($\frac{\theta + \sum_{i=1}^{N-1}{\theta^i_\text{perm}}}{N}$) could aid the authors' claim for using $\theta_\text{reset}$. I would like to see an additional experimental results on this point, either based on my suggestions or on the authors' own.
2. I think that lines 197-199 is the one of the main hypotheses that the authors make. So I would expect a thorough empirical evidence to support this claim, which is not included in the main text.
3. (Closely related to the above 2.) I assume Figure 2 is objected to in order to analyze the advantage of resetting non-dormant neurons compared to other methods. While the authors conclude that there is an ambiguity of the metrics to explain the results, I think these metrics should be more thoroughly designed to expect such effects. Authors could design a different metric to logically/effectively support the result, or measure these metrics in extensive ablation experiments as in the setting of Figure 3 (i.e. controlling $k$). Maybe the difference of the loss landscape or the changes of activations/representations before and after the reset could be a possible candidate to measure.
4. The phenomenon of the loss of plasticity is also highlighted in the field of reinforcement learning. And among the references cited by the authors, there are papers that study the effect of resetting in reinforcement learning. I think this work could be more strengthened by adding experiments in the reinforcement learning setting as in [1, 2, 3].

### Questions
1. I think the results of Section 4.1 could be seen less (statistically) significant to some readers, especially the left subfigure. The correlation seems weak, and even my statement could not be guaranteed with only one seed. Can
2. I'm aware that prior works like [1, 2] uses the experimental settings in similar scale, but I'm curious that can the effect that the authors present also be seen on more larger/complex model sizes/architectures?
3. Can the authors clarify when is the point the model undergoes reset for the experiments in Section 4.2? I couldn't find this setting only for Section 4.2.
4. May be the authors could try different reset functions. I think the main contribution of this paper is selecting the non-dormant neurons to reset. If this is robust across diverse reset functions, this could be a certain strength. Based on the taxonomy based on [3], while the reset method the authors are using is re-randomization, there exists other methods; re-initializing [4, 5], or using checkpoints [6].



[1] Alex Lewandowski, Haruto Tanaka, Dale Schuurmans, and Marlos C. Machado. Directions of curvature as an explanation for loss of plasticity, 2024

[2] Clare Lyle, Zeyu Zheng, Khimya Khetarpal, Hado van Hasselt, Razvan Pascanu, James Martens, and Will Dabney. Disentangling the causes of plasticity loss in neural networks. arXiv preprint arXiv:2402.18762, 2024.

[3] Zhang, Chiyuan, Samy Bengio, and Yoram Singer. Are all layers created equal?. Journal of Machine Learning Research 23.67 (2022): 1-28.

[4] Evgenii Nikishin, Max Schwarzer, Pierluca D’Oro, Pierre-Luc Bacon, and Aaron Courville. The primacy bias in deep reinforcement learning. In International conference on machine learning, 2022.

[5] Oh, Jaehoon, et al. ReFine: Re-randomization before Fine-tuning for Cross-domain Few-shot Learning. Proceedings of the 31st ACM International Conference on Information & Knowledge Management. 2022.

[6] Bae, Youngkyoung, Yeongwoo Song, and Hawoong Jeong. Stochastic Restarting to Overcome Overfitting in Neural Networks with Noisy Labels. arXiv preprint arXiv:2406.00396 (2024).

### Soundness
1

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes a reset-inspired method, referred to as Interpolate, for maintaining plasticity and increasing generalization in online learning. Interpolate periodically updates a neural network's parameters by interpolating between the the network parameters and a functionally equivalent permutation, where the permutation permutes a subset of `"active’’ or high-utility neurons. The method is evaluated against competitor reset-based continual learning algorithms, Continual Backdrop and ReDO, on a series of continual learning problems on the CIFAR10 dataset. Results show that interpolating network parameters with a random (functionally equivalent) permutation of the most active neurons is competitive with Continual Backdrop and ReDO.

### Strengths
- The paper considers a completely new paradigm of resetting active or high-utility neurone, which runs counter to existing reset-based methods that reset dormant or low-utility neurone. The results of this paper are surprisingly positive, counter to conventional expectations of neuron dormancy being a driving factor of plasticity loss. For this conjunction of reasons, this is a worthwhile contribution. 
- The paper is generally well written and clear with its stated contributions.

### Weaknesses
 - The claim that resetting active neurons improves generalization is not entirely supported by the results. The algorithm Interpolate interpolates between the network’s parameters and a functionally equivalent permutation — this is not ``full’’ resetting of active neurons. The interpolation process, while novel, doesn't truly reset the neurons to a state comparable to their initial random initialization, which is the typical understanding of a reset operation in the context of plasticity.
- Not all of the experiments in section 4.4 exhibit plasticity loss. Specifically for Permuted CIFAR10 and Noisy CIFAR10 we see that SGD attains greater test accuracy over time. However, plasticity loss is the phenomenon in which baselines like SGD experience diminishing performance as the network is faced with more tasks, but for the aforementioned experiments we do not see this phenomenon. To validate that Interpolate mitigates plasticity loss, we should be seeing this phenomenon arising in a baseline SGD model. I would recommend increasing the number of tasks and/or evaluating additional experiments such as Permuted MNIST or Continual Imagenet (see Dohare et al. or Kumar et al.). Furthermore, the observed increase in performance of SGD on Permuted and Noisy CIFAR10 suggests that the tasks are not sufficiently challenging to induce forgetting, thereby casting doubt on the effectiveness of the proposed method in mitigating plasticity loss under more demanding conditions.


### Questions
- Can you formally define `"functionally equivalent parameters" for completeness and in order to be precise.
- Out of curiosity, have the author(s) considered other convex combinations of $\theta_{\text{perm}}$ and $\theta$, rather than a 0.5-0.5 combination? Perhaps more frequent and gradual interpolations may be performant.
- I understand that Interpolate captures the spirit of resetting active neurone, but I feel that it is more of a model merging technique, merging the network’s parameters with a functionally equivalent permutation, and does not perform ``full’’ resets. This does not square entirely with the title, abstract, and introduction which claim that your algorithm Interpolate and experiments involve resetting active neurons. Could the paper be worded differently in a way that makes it clear that the reset-technique is really a model merging technique? Reading up to section 3.1 I was expecting to see resets in the flavour of CBP and ReDO, with an additional model merging algorithm as a secondary contribution, but instead the "resets of active neurons" are instead interpolations between active neurons. 
- In section 4.1, precisely what is reset by random noise? What is the noise scale and are neurons reset according to the prior distribution used for initialization?
- Given that dormancy continues to increase in Figure 2 and does not plateau, it would be useful to see how these statistics (test accuracy, dormancy, etc.) evolve over more tasks.
- Can some of these experiments be replicated with the Adam optimizer?

### Soundness
3

### Presentation
3

### Contribution
3
