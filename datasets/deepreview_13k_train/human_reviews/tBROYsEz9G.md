# How Realistic Is Your Synthetic Data? Constraining Deep Generative Models for Tabular Data

- Decision: Accept
- Scores: 6, 8, 5, 6

## Abstract
Deep Generative Models (DGMs) have been shown to be powerful tools for generating tabular data, as they have been increasingly able to capture the complex distributions that characterize them.  However, to generate realistic synthetic data, it is often not enough to have a good approximation of their distribution, as it also requires compliance with constraints that encode essential background knowledge on the problem at hand. In this paper, we address this limitation and show how DGMs for tabular data can be transformed into Constrained Deep Generative Models (C-DGMs), whose generated samples are guaranteed to be compliant with the given constraints. This is achieved by automatically parsing the constraints and transforming them into a Constraint Layer (CL) seamlessly integrated with the DGM. Our extensive experimental analysis with various DGMs and tasks reveals that standard DGMs often violate constraints, some exceeding 95\% non-compliance, while their corresponding C-DGMs are never non-compliant. Then, we quantitatively demonstrate that, at training time, C-DGMs are able to exploit the background knowledge expressed by the constraints to outperform their standard counterparts with up to \add{6.5\%} improvement in utility and detection. Further, we show how our $\CL$ does not necessarily need to be integrated at training time, as it can be also used as a guardrail at inference time, still producing some improvements in the overall performance of the models. Finally, we show that our CL does not hinder the sample generation time of the models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The main contribution of this paper is to add constraints on generating synthetic data so that it is aligned with available background knowledge. The paper introduces constraint layers in order to enforce a set of linear constraints that encode the background knowledge. They also prove the correctness of the constraint layers introduced

### Strengths
The motivation behind the paper is clear and easy to follow. The paper also offers some theoretical justification for their method which makes their paper compelling. The proofs from what I can see are correct. The experiments are well formulated and support the claims of the paper.

### Weaknesses
 The issue with the paper is the proofs can be difficult to follow. It is possible that the authors can spend more time rewording it to make it easier to flow. This also makes it a bit hard to flow and check.

### Questions
This isn't really a question but I think the use of linear constraints can be advantageous as they are logically complete. Any inconsistency can be identified easily through Farkas's lemma. I think the authors can potentially frame the use of linear constraints in a better light to highlight how its logical completeness can be useful when specifying background knowledge.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Generating realistic tabular data requires compliance with constraints that encode essential background knowledge on the problem. In this paper, the authors address the limitation and show how deep generative models for tabular data can be transformed into constrained deep generative models, whose generative samples are guaranteed to be compliant with the given constraints. This is achieved by automatically parsing the constraints and transforming them into a constraint layer seamlessly integrated with the dgm. The authors shows the effectiveness of the proposed model with experiments on 6 datasets.

### Strengths
The first to handle with the constraints of tabular data, and the method addressed the problem well.

### Weaknesses
Tabular data synthesis methods used for the experiments are outdated. Please consider [1] GOGGLE, [2] GReaT, [3] STaSy, [4] CoDi, and [5] TabDDPM if possible.

### Questions
How was the performance improvement of the state-of-the-art methods after applying the proposed method?

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates a lesser-explored challenge in the generation of tabular data—adherence to specific rules or constraints for data entries. It highlights a common issue where existing generative models often fail to respect constraints such as linear inequalities (e.g., one column being less than or equal to another), as they are not designed to fulfill these conditions.

To address this, the paper introduces a novel approach to adding a constraint layer to standard DGMs, transforming them into constrained DGMs. The study demonstrates that these constrained DGMs are more effective in producing realistic data that adheres to the specified constraints, further improving downstream performance. Moreover, it shows that even applying these constraint satisfaction layers to a pre-trained DGM can significantly enhance the realism of the generated data.

While the paper tackles an interesting issue, given the marginal novelty of the paper and the limited number of constraints in the datasets under consideration, I will not accept this paper. I would be willing to increase the score if the authors can provide reasonable answers to my concerns.

### Strengths
1) The paper is well-written and the idea is laid out with sufficient examples to follow through.
2) Pointing out the fact that many DGMs violate obvious constraints in tabular data is very important and studying it is valuable.
3) The experimental results seem thorough and the theory checks out.

### Weaknesses
1) **(Important)** The paper mentions the choice of $\lambda(i) = i$ is for ease of notation, while different orderings can drastically change the performance of a C-DGM. As an illustrative example, consider tabular data with three outputs $\langle x_1, x_2, x_3 \rangle$ with constraints: $x_2 \le 10$ and $x_1 \le x_2 \le x_3$. Now assume the generative model only produces $\langle 10, 5, 5 \rangle$. In this case, if the ordering $\lambda = \langle 1, 2, 3 \rangle$ is considered, then $CL(\tilde{x})$ would be $\langle 10, 10, 10 \rangle$ and if the ordering $\lambda = \langle 2, 1, 3 \rangle$ is considered, then $ CL(\tilde{x}) = \langle 5,5,5 \rangle$ with one being significantly closer to the generated distribution than the other. In fact, the notion of “optimality” is not well defined, as each ordering can produce a different optimal with none of them being comparable for defining an optimum. Moreover, the notion of optimality should also consider the discrepancy between the $CL(\cdot)$ outputs and the generative samples to be minimal. The paper does not provide a clear justification for the chosen ordering and its impact on the final results, nor does it explore alternative strategies for determining the optimal ordering.
2) **(Important)** I might have missed something but the reduction defined for constraints $\Pi$ can easily turn the number of constraints exponential, meaning that $|\Pi_1| \in \mathcal{O}(exp(|\Pi|))$. The only reason the current experiments do not hinder the performance is that the number of conditions is fairly small, to begin with. I would require datasets with a much larger number of conditions to be convinced that the post hoc method does not impact the sample generation time. The paper should include a more thorough analysis of the computational complexity of the constraint reduction, especially with respect to the number of constraints and features.
3) The paper only considers linear constraints. Even though it is pointed out as a limitation some extensions to non-linear constraints are quite simple. For example, by introducing polynomial features, one can add polynomial constraints to the current approach. Having one entire paper on linear constraints seems rather limited in novelty. I would suggest adding simple experiments as proof-of-concept for such extensions. The paper should address the limitations of focusing solely on linear constraints, and provide a more detailed discussion of how the proposed method could be extended to handle non-linear constraints, including the challenges and potential solutions.

### Questions
1) Even though GANs have achieved popularity for image generation, they are known to fail drastically for tabular data generation. That said, is there any reason why other DGMs such as TVAEs, STaSy, and TabDDPM are not considered in this study given the current limitations of GANs? For a more compelling story, it would be good to include other types of generative models as well. Especially in the post hoc experiments.

2) The reported charts and tables are thorough, but I wasn’t able to find any source code for reproducibility and a footnote claims that the code will be released upon publishing; however, I didn’t find anything to run in the supplementary material.

### Soundness
1 poor

### Presentation
4 excellent

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
The authors propose a method for generating tabular data which respects some domain-specific conditions, by introducing the so-called Constraint Layers (CL), which can enforce linear constraints on the features of the generated data. CLs are tested on GAN models and the results on a selection of tabular problems with constraints show how they are effective at preventing generation of data which violates such constraints.

### Strengths
The paper presents an effective way to enforce linear constraints on (and between) variables for tabular data generated with deep Generative models. The manuscript is generally very clear and presents the contributions in great detail. The method is tested on a comprehensive set of problems and compared with three strong baselines.

### Weaknesses
From reading the paper, it is not immediately clear how the training procedure with CLs works, and whether CLs can be applied to other generative models, such as Variational Auto Encoders, Normalizing Flows or Diffusion Models. A comparison with methods such as TVAE and TabDDPM (mentioned in the related work) and the application of CLs to them would significantly strengthen the experimental section. A metric to compare the data distribution from the generated distribution is missing from the experiments. Would it be possible to include a metric such as negative log-likelihood or Wasserstein distance?

From the Wasserstein distance results, it seems like the C-DGMs can sometimes have higher distances compared to non-constrained models, which would suggest that the learned distribution becomes worse. In addition, sometimes the distance is also greater than the one obtained with the P-DGMs, which to me is counterintuitive. Do you have some insight on why in some cases the Wasserstine distance increases for C-DGMs?

From answer 3, do I understand correctly that CL cannot be applied to categorical features? Could you please clarify this point, and explain the differences in the Jensen-Shannon divergence between categorical features in Table 12?

I believe that from the experimental section, it is not clear whether the generative performance, in terms of learning the correct data distribution, is improved or worsened with respect to the non-constrained models. Perhaps testing the method on more complex datasets could shed some light on whether the CL layers provide a substantial improvement, as from the current results, the method does not always outperform the non-constrained models, and most of the time only marginally, with respect to the metrics considered (besides constraints violation coverage). I think it is very important to find a way to show the faithfulness of the learned distribution with respect to the true one and to show that CL layers do improve over standard models. Otherwise, as a practitioner, I would rather naively generate data with a non-constrained model, and discard those samples that violate my constraints, until I obtain the desired amount of samples.

### Questions
- Perhaps a point that I missed from the paper, but how do CLs affect the training? Can gradients backpropagate through these layers? Can CLs be applied to other Generative Models?
- How does the application of CLs shift the distribution of the generated data? Does it result in an "overpopulation" of the regions on the boundaries? If that's the case, the resulting distribution would be skewed from the true distribution especially when the baseline model generates many samples which violate the constraints. Adding other metrics (see weaknesses) would help with investigating this matter.
- Can CLs impose constraints between categorical variables, or between numerical and categorical variables? For example, if x1 = "category 1", then x2 > 5, or similar?
- Are there cases in which assigning a valid variable ordering is not feasible?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
