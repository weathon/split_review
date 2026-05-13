# Robust Classification via a Single Diffusion Model

- Decision: Reject
- Scores: 8, 8, 8

## Abstract
Diffusion models have been applied to improve adversarial robustness of image classifiers by purifying the adversarial noises or generating realistic data for adversarial training. However, diffusion-based purification can be evaded by stronger adaptive attacks while adversarial training does not perform well under unseen threats, exhibiting inevitable limitations of these methods. To better harness the expressive power of diffusion models, this paper proposes Robust Diffusion Classifier (RDC), a generative classifier that is constructed from a pre-trained diffusion model to be adversarially robust. RDC first maximizes the data likelihood of a given input and then predicts the class probabilities of the optimized input using the conditional likelihood estimated by the diffusion model through Bayes' theorem. To further reduce the computational cost, we propose a new diffusion backbone called multi-head diffusion and develop efficient sampling strategies. As RDC does not require training on particular adversarial attacks, we demonstrate that it is more generalizable to defend against multiple unseen threats. In particular, RDC  achieves $75.67\%$ robust accuracy against various $\ell_\infty$ norm-bounded adaptive attacks with $\epsilon_\infty=8/255$ on CIFAR-10, surpassing the previous state-of-the-art adversarial training models by $+4.77\%$. The results highlight the potential of generative classifiers by employing pre-trained diffusion models for adversarial robustness compared with the commonly studied discriminative classifiers.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to build a robust classifier using a single diffusion model by calculating $p (y|x)$ via $p (x|y)$. The authors identify likelihood maximization as a key ingredient for ensuring the adversarial robustness of such models. To address the high computational complexity associated with this type of classifiers, the authors further introduce a multi-head U-Net and ablate on efficient sampling methods. Experiment results on a subset of CIFAR-10 using BPDA-AutoAttack show that the proposed method achieves SOTA clean and adversarial accuracy.

### Strengths
This paper proposes an interesting and relevant framework for robust classification. Given how fast diffusion models are improving in comparison to traditional discriminative robust classifiers, this work opens a new method of building robust models. It thus has a lot of potential for inspiring future research that builds even better robust models. Furthermore, the authors are careful with evaluating the proposed method with strong adaptive attacks, providing justifications for the proposed robustness estimation methods.

### Weaknesses
The main weaknesses are twofold: computational complexity and paper presentation.

### Computational Complexity

Even with the proposed multi-head U-Net and other complexity reduction measures, the computational complexity still seems to be high. While the likelihood maximization step only requires $N=5$ forward and backward passes, approximating $p(x|y)$ requires $T$ U-Net queries. That being said, I agree that this drawback can be left for future work.

### Paper Presentation

Many important details are missing from the discussion. Some of them can be found in the appendix, but they really should be in the main text. This is especially the case for Section 3.3.
- Theorem 3.2 discusses "optimal diffusion models". In what sense is the diffusion model optimal? The proof to this theorem clarifies that such a model minimizes the noise estimation error, but this should be in the main text.
- There is a softmax operation in Theorem 3.2, but the quantity on which it operates is a scalar (a norm square divided by some variance). What does softmax exactly mean here? Same for Corollary 3.3. Is the softmax operator in Corollary 3.3 defined as the softmax across all classes?
- "We find that the optimal diffusion classifier achieves 100% robust accuracy in both cases, validating our hypothesize that accurate density estimation of diffusion models facilitates robust classification." How was this found? Also, it should be "hypothesis", not "hypothesize". What is the main gap between an optimal diffusion classifier and an empirical diffusion classifier? Is it the limited amount of training data? Or is it how well the U-Net is optimized?
- Section 3.5 says, "instead of calculating the diffusion loss using all timesteps like Eq. (9), we only sample a single timestep". How is this time step sampled? Uniformly randomly?
- Section 3.5 also says, "(BPDA) approximates the gradient with an identity mapping". How exactly is the identity mapping applied? A pseudo-code or Python code explanation would be appreciated.
- It would be nice to have the experiment results from the CIFAR-100 dataset to have some diversity in the evaluation. There are some occasions where the equations exceed the page margin. Please fix them.
- Please explain the four legend entries of Figure 2a in its caption, since I don't think they are used elsewhere. It should also be clarified in the caption that the figure was made on DC, not RDC.
- It would be nice to add $T' = 2000$ (and potentially even higher if computation allows) to Figure 2a to show whether the robust accuracy "saturates", which seems to be the case based on the number for $T' = 2000$.
- It's odd that Figure 2c is mentioned first in the text, then 2b, and finally 2a. It might make sense to change the order.
- It would be interesting to show some of the generated images from the diffusion models as figures in the paper.

### Questions
- Since AutoAttack with BPDA is used for evaluation, is the Square Attack component of AutoAttack also included in the evaluation? Does Square find additional examples on top of the BPDA gradient-based attacks?
- In Figure 2a, why is the robust accuracy barely over 30%? What is the value of $T$ and $T'$ for the main results (Table 1)? Does the result get even better if $T'$ is larger than 1000? How large is $T$ during the training of the diffusion model? If we train a diffusion model with fewer time steps (i.e., discretize the trajectory into less than 1000 steps during training), should we expect the resulting classifier obtained via the proposed method to work well with a smaller $T'$?
- With multi-head diffusion, is it true that only the last layer receives the class condition signal? How does this affect the performance compared with injecting class conditioning into various locations in the U-Net? It would also be nice to see some generations from this diffusion model.

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents the Robust Diffusion Classifier (RDC), a generative classifier designed for robust classification tasks. RDC operates by first optimizing the data likelihood of an input and then estimating class probabilities for this optimized input. This is achieved using the diffusion model with transforms using the Bayes' rule. Recognizing the need for classification efficiency, the authors introduce a novel diffusion backbone termed "multi-head diffusion" and for a sampling strategy with fewer NFE. Notably, the method requires no specific training against particular adversarial attacks, showcasing its adaptability in defending against a spectrum of previously unseen threats.

### Strengths
- The proposed methodology stands out as both technically sound and effective. Its capability to achieve robust classification without specific knowledge of adversarial attacks is admirable. The paper has both theoretical and empirical contributions, which are beneficial to both the theoretical-favored researchers and practitioners.

- The paper is overall well-written and provides a smooth reading experience. The incorporation of model overviews and illustrative diagrams further clarifies the proposed methodology, enhancing comprehension.

- The experimental results well validate the approach. Notably, the paper also provides an ablation study to interpret the effects of the hyperparameters. 

 - The authors have provided a thorough study that motivates the design of the multi-head classifier in the appendix. This study provides additional insight for researchers to figure out problems in related domains.

- I appreciate the authors' transparency in addressing potential limitations. The practical side of the research is solid. The authors have been very detailed in their implementation and provided their experiment code, which ensures reproducibility.

### Weaknesses
Although the content of the current version is satisfactory, some points listed below can further enhance the depth and completeness of this work:

- Some details regarding the diffusion model need clarification. For example, the sampling strategy is not very clear to me. It seems the authors deploy a VP sampling with uniform sliding timesteps similar to the one used in Nichol and Dhariwal, (2021). In the appendix and the code the authors also seem to leverage some implementation from Karras et al. (2022). As we note the sampler in Karras et al. (2022) involves additional correction steps, the NFE of the diffusion backbone would be more than T. It is crucial to specify the exact sampling algorithm used, including whether it is a deterministic or stochastic sampler, and to clarify how the number of function evaluations (NFE) relates to the chosen time discretization scheme. The current description lacks the necessary detail to fully understand the implementation of the diffusion process.

- The theoretical results are based on the hypothesis that the evidence lower bound is tight. It would be intriguing to explore the implications of the gap between the likelihood and this lower bound, especially when viewed through the lens of the Bayesian framework for uncertainty quantification. Exploring how this gap influences robust classification performance could enrich the paper's depth and utility. Specifically, it would be beneficial to analyze how the tightness of the ELBO affects the calibration of the classifier's probabilities and its robustness to adversarial examples. A discussion on the potential biases introduced by using the ELBO as a proxy for the true likelihood would be valuable.


- While the current experiments are limited to relatively small-scale datasets, there is inherent value in examining the method's scalability. It would be beneficial if the authors could present results or potential methodologies to apply their approach to larger datasets, drawing inspiration from other generative classifiers in the Bayesian paradigm, such as those highlighted by Heek and Nal (2019) and Han et al. (2022). The computational cost associated with the proposed method, particularly the repeated ELBO calculation for each class, needs to be addressed when considering larger datasets. It would be helpful to see a discussion on potential strategies to reduce this computational burden, such as using more efficient sampling techniques or approximations of the ELBO.


- This paper also has close relation to other generative classifiers not specified for robust classification. Although the authors have discussed some concurrent works, some prior works may need to include and discuss potential connections. Specifically, the paper should discuss how the proposed method compares to other generative classifiers in terms of computational complexity, robustness, and classification accuracy. A more thorough comparison with existing methods would help to better position the contribution of this work.

- The current form of the paper draws parallels to several generative classifiers, though not specifically designed for robust classification. While some works have been discussed as concurrent works, it might be helpful in enhancing the completeness to integrate and discuss other prior works, emphasizing their relevance and potential connections to the proposed methodology.

### Questions
Please see the first point of the weakness regarding the details in diffusion settings.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a diffusion-based classifier that surpasses the SOTA level of robust accuracy against lp-bound adversarial attacks without relying on adversarial training. The method is advantageous to previous methods because it does not require inference for every class in the dataset by leveraging a "multi-head diffusion" block. Further, to improve the density estimation of real-world models the authors propose a "Likelihood Maximization" technique.

### Strengths
1. Clear and quality writing.
2. The method is carefully designed with theoretical justifications. In particular, the authors go to great lengths to address gradient obfuscation.
3. The method is benchmarked against modern adversarial attacks (AA, StAdv, BPDA) and beats SOTA by a large margin while showing generalization to more threats than previous methods.
4. Thorough review of related work and comparison to previous methods.

### Weaknesses
1. The manuscript mentions multiple times the expensive inference in both time and memory - however, a quantitative analysis is missing. I would like to see a table with inference time and memory for this method in comparison to other generative classifiers and regular ones. Specifically, the analysis should include a breakdown of the time and memory costs associated with each stage of the proposed method, such as the diffusion sampling process and the multi-head classification. This would allow for a more precise understanding of the computational overhead.
2. The method appears to work well on "unseen" threats. However, all threats are limited to adversarial attacks. Is there any evidence for an increased robustness to other robustness aspects such as common corruptions (e.g., CIFAR10-C)? It would be beneficial to see how the method performs against corruptions such as blur, noise, and weather effects, as these are common real-world scenarios that robustness methods should address. A comparison with other robust methods on these benchmarks would also be valuable.
3. The experimental evaluation is performed on a clearly separated and limited number of classes. Are there any results or theoretical insights on how this method would scale to more and potentially more fine-grained classes? It is unclear whether the performance gains observed on a limited number of classes would generalize to more complex datasets with a larger number of classes and more subtle differences between them. The authors should discuss the potential challenges and limitations of scaling the method to such scenarios.

### Questions
1. In Appendix B the authors state "However, this architecture only achieves 60% accuracy on the CIFAR10 dataset". How does that relate to the 90-ish % in Tab. 1? I.e. what is different in this section?
2. “... [the mthod] ... leverages an off-the-shelf diffusion model” - how is this possible when the last layer is modified? Which diffusion model is this exactly? How does it compare to the diffusion models previous works have used?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
