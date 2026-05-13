# Improved Function Space Variational Inference with Informative Priors

- Decision: Reject
- Scores: 6, 3, 3, 6

## Abstract
Function space variational inference allows Bayesian neural network (BNN) to introduce the prior distribution on the function space directly. Moreover, Recent linear approximation scheme for KL divergence between two random functions, has presented the tractable training objective and thus facilitates imposing the function space prior on BNNs. On the other hand, despite of its tractability, the existing inference suffers from the interpretability issue because the this function space prior is obtained by mapping the pre-defined weight-space prior to the function output via the complex neural network, and thus seems to be less interpretable. Alternatively, thought the uniform function space prior, that imposes a zero mean prior on the function space to encourage the model to be uncertain for out-of-training set, has been considered, this prior can introduce unnecessary uncertainty into the function outputs of the training datasets. Thus, this can cause the trade-off between the uncertainty estimation performances on the in-training and out-of-training sets.


In this work, we aim at refining the function space variational inference to handle the mentioned issue. To this end, we first reconsider the role of the function space prior in view of Bayesian Model prediction, and then build the function space prior to help improve the uncertainty estimation of the BNNs. Additionally, we propose a refined variational distribution on function space to encourage the useful predictive functions in sense of Bayesian model averaging, to be sampled, and thus improving the prediction of the BNNs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on improving function-space Bayesian Neural Networks (BNNs) by addressing some of the key challenges they face in terms of dealing with significative prior distributions. Applied in a classification setting, the authors propose an informative function space prior that encourages sample functions to have a certain predictive probability and varying degrees of disagreements based on input status. They also tackle the issue of computing KL divergences in function space by using an adversarial hidden feature and refining the variational function space distribution. Experimental results show that their approach outperforms other inference methods on the CIFAR 100 dataset, demonstrating its effectiveness for large-scale models.

### Strengths
* The topic is quite interesting from the point of view of enlarging the contributions to the function-space approach to modern probabilistic machine learning. The topic of using function-space BNNs is relevant and promising, and further research such as this is very welcome.
* The proposal for function-space variational distribution introduces a categorical latent variable that represents the uncertainty in using a specific feature based on its empirical distribution. This allows for better understanding and interpretation of the model's behavior.
* The authors use multi-dimensional probit approximation (MPA) to obtain an approximate marginalization over a Gaussian distribution for obtaining $\hat{p}(\cdot)$. This technique helps to efficiently compute and approximate complex distributions, making it feasible to implement this approach.

### Weaknesses
* The article writing does not contribute to the overall appreciation of the work being done and should be thoroughly revised. I strongly encourage the authors to do an integral check on the text for improvements. This is quite noticeable, even the abstract should be revised to correct typos and improve the overall text flow and comprehension. A lot more care and effort have to be put in this regard.
* The proposed method relies on a last-layer approximation, which is not thoroughly discussed enough. While this approach can be employed with the right arguments, the authors do not make the efforts necessary to justify this choice or the consequences it may entail in the proposed technique.
* While the paper presents an improved function-space variational inference method, it does not provide extensive evaluation results or comparisons against other existing methods on benchmark datasets or real-world applications to demonstrate its superiority over alternative approaches. I think stronger experimental work is needed to further motivate the usage of the proposed approach. The contribution is itself interesting, but further experimental results would bolster the proposal (e.g. regression experiments, applying this method to specify the prior in other function-space inference methods to check the potential improvements, etc.).
* The proposal made in the article is strictly limited to BNNs, while other methods such as the one in [1] or Rodríguez-Santana et al. (2022) can be seen as "generalist approaches" where the function-space formulation can be done for many other models (not just BNNs, which are only particular cases).

*Note:* I condition my review score on the fact that some of these issues get fixed in the final draft version. Otherwise, I may be inclined to lower the score. 


(see "**Questions**" for the references)

### Questions
* In the initial paragraph of the introduction, when mentioning function-space BNNs I would include the reference [1].
* Why would you argue that the main goal of function-space BNNs is "directly assigning prior distributions to the outputs of neural networks"? I would argue this can be done without function-space formulation, and that the main interest lies directly on the properties of the function space itself. I would even argue that the approach does not necessarily become more "user-friendly" due to the difficulties intrinsic to function space. I would appreciate more insight on these points.
* Given the BMA approach and the nature of the contribution in Rodríguez-Santana et al. (2022), how do these relate to each other? I think further discussion here could improve to make a more comprehensive overall picture.
* Does the last-layer approximation play a role in the final performance metrics? What results are achieved if this restriction is not applied and instead a full Bayesian NN is used?

---
### **Notes:**

* As the authors mention: "(Flam-Shepherd et al., 2017; Karaletsos & Bui, 2020; Tran et al., 2022), it has been less clear to specify the interpretable function space prior for the classification task" I would expect this contribution to try to either expand on this formulation or present a general contribution for classification problems (although one also could say that works such as Tran et al. 2022 could serve to that purpose). The formulation of the article up to Section 3 makes the reader think the authors are presenting a general approach both for regression and classification, while in reality they only do the latter. Thus, I would encourage the authors to be clear with these intentions from the beginning. Moreover, since the conversion to regression does not seem too far off from the method present, I strongly 
* Results for the presented method in table 2 are highlighted, while there are other methods in ECE and AUROC that are competitive (with equal performance). This should be corrected.

### **Minor corrections:**

* Please correct typos. Just in the abstract there are some of them, such as the capitalized "Recent", the "the this function space" sentence, "thought the uniform function space..." should be revised. Further examples can be found all through the text, such as "lineariztion" or "Jacobin matrix".
* Maintain consistency, e.g. if you are using "function-space" on the title I would expect to keep the "-" throughout the text. On the same line, remove the red-colored subindex in page 3 (unless you use justify its usage further). Also, there are some inconsistencies also in singular and plural expressions, such as "since the posterior distribution of the weight parameters p(Θ|D) are not tractable in general". Please, correct the text carefully.
* Reference for Rodríguez-Santana et al. (2022) is missing the \' in "í" 

### **References:**
[1] Ma, C., Li, Y., and Hernández-Lobato, J. M. (2019). “Variational implicit processes”. In: International Conference on Machine Learning, pp. 4222–4233.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates a new approach to specify informative priors for improve variational inference in function space on classification tasks. In particular, the paper relies on the functional variational inference (f-VI) framework proposed by Rudner et al. (2022) but replaces the uniform (uninformative) functional prior with an informative functional prior. To this end, the authors reconsider the role of functional prior in the perspective of Bayesian Model Averaging (BMA), and then propose a new functional prior relying on the empirical Bayes approach (using the training data to specify the prior). This prior is aimed at avoiding common pathology of the uniform functional prior, which encourages the model to be uncertain on both the training and out-of-training data. In addition, the authors propose a new functional variational distribution that is aligned with this new functional prior.  The proposed method is validated on toy data and popular benchmarks.

### Strengths
- The paper aims at tackling an important problem for Bayesian deep learning which is designing a good prior for Bayesian neural networks.
- The code is anonymously provided. However, there are no instructions to use the code. Thus, it is difficult to verify the provided code.
- The idea is interesting and well-motivated which is to design a new prior promoting high uncertainty for out-of-distribution data but low uncertainty for in-distribution data.

### Weaknesses
- The writing should be improved. There are many grammar typos such as the use of “a” and “an”. Some parts of the paper are difficult to read, especially Section 4. There are some confusions of notations. Please refer these to in the box of Questions.
- In Section 4, although the authors motivated the paper from the view of Bayesian Model Averaging, and claimed that *“we may design a function space prior that does not explicitly encourage generating high-entropy predictions for each predictive probability but the average prediction (via BMA) would still have high-entropy when encountered with an OOD input”*, it is not clear how the proposed prior can achieve this.
- The proposed method is somehow ad-hoc without well-elaborations. For example, in Eq (9), why do the empirical mean and covariance are averaged from those obtained from all pre-training iterations? How did the authors come up with the equation (13), the parameter $\hat{p}(\cdot)$ for the variational distribution?
- The authors ignored a very related work from Izmailov et al. (2021). The narrative of this work also relies on Bayesian model averaging. This work also considers designing a novel prior that is robust to out-of-distribution data by using the empirical Bayes approach. The authors should cite, discuss, and compare experimentally with this work.
- Experimental results on image benchmarks (Sec 5.2) show that the performance gain from the proposed prior (R-FVI) is very marginal compared to the uniform prior (T-FVI). To show clearly the effect of the prior, the authors should ablate different training sizes and temperature values for the posterior on these benchmarks.

References:

Izmailov et al. Dangers of Bayesian Model Averaging under Covariate Shift. NeurIPS 2021.

### Questions
- In Equation (8), what is $N^q$ how to define it? Do we have to compute the means and shared covariance over the dataset?
- In Equation (9): what is $T$? It should be consistent with the sentence before the Equation (8).
- From Figures 3c and 3f, it seems that the proposed method always induces a much higher disagreement ratio on both in- and out-of-distribution data compared to the uniform prior. Is this good? On in-distribution data, the entropy should be low.
- In the paragraph "Context inputs from adversarial hidden features". How do we define $r$?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the problem of inferring posteriors of Bayesian neural nets with function-space priors more effectively than the existing variational inference approach that uses the first-order Taylor approximation.

### Strengths
* The studied transfer learning setup with Vision Transformers is interesting and fits well to the purpose of doing Bayesian inference.

 * The paper presents results from a comprehensive set of experiments.

### Weaknesses
* The problem setup does not make much sense to me. The introduction says:   **“We build an informative function space prior by using the empirical Bayes approach along with the parameters of hidden values and the last layer weight parameters which are obtained iterations during early stages of training”**. I wonder how the approach is then different from having an uninformative prior after all. If the information comes from the data, it is technically not a prior. It appears that the paper makes its main point by differentiating from cases where the priors are just so strong that they unnecessarily restrict the model capacity.

 * The paper significantly lacks clarity. Apart from having extremely many typographical errors, it has statements without sharp enough meanings. Among the many, one example is: **“Denote auxiliary inputs, which are far from training points and are placed closely with the training sets, respectively”**. I have no idea what it means for a training point to be close to a training set. Likewise: **“h(.) from the q-th component empirical parameters of hidden feature …”** What is an empirical parameter? I also have no clue about what is going on in pages 5 and 6 after spending considerable time trying to read them. Even the purpose of all these complications such as introducing adversarial hidden features do not look to me justified.

 * It is a clear weakness that after motivating Bayesian inference with lots of effort, the paper ends up using it only on the penultimate layer. Those layers are typically linear, where even closed-form Bayesian linear regression would work and the learned model weights would give a degree of interpretability. Why should one use function-space Bayesian inference if the prior will come from the weights learned in another data set and only the penultimate layer will be Bayesianized?

 * I do not think the reported results demonstrate the benefit of the proposed approach clearly enough. All models in all experiments perform very closely to each other. The results reported in Figure 2 are mixed: (a) and © are favorable for the central message of the paper while (b) and (d) are just the opposite.

* The take-home message given in the last sentence of Section 5.1 is obvious and comes from the nature of using an arbitrary regularizer. I wonder why one needs even an experiment for that.

--- POST REBUTTAL ---

The author response does not give any concrete answer to any of the issues I raised above. I keep my score unchanged.

### Questions
Only T-FVI or all the three baselines? If first, why not others?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new function space variational inference for classification problem. The existing informative function prior may lead to high entropy to both in and out distribution data points. The idea is to assign lower entropy to in-distribution data and higher entropy to out-of-distribution data. The authors have designed a specific function prior and variational posterior to control the entropies. The experiments show somewhat promising results.

### Strengths
The paper is well presented with good visualization to motivate the targeted problem. The designed prior and variational distribution are interesting and reasonable.

### Weaknesses
1.	Why was the last layer set as BNN layer? Why not set the whole network as BNN? 
2.	The experimental results are only marginal, which is my main concern. Is that because the only last layer is BNN? Why not try more BNN layers that can demonstrate more difference between new prior with previous informative prior? 
3.	Since the prior is changing during the training, how to ensure the convergence of the procedure? 
4.	Since the method is specially designed for the classification task, I suggest the author to revise the title and introduction accordingly to highlight the classification task. 
5.	What is the role of (12)? 
6.	Some symbols are not defined, like N^q

### Questions
Please see the Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
