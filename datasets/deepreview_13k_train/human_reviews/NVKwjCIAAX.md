# Adaptive Constraint Integration for Simultaneously Optimizing Crystal Structures with Multiple Targeted Properties

- Decision: Reject
- Scores: 6, 5, 5, 3

## Abstract
In materials science, finding crystal structures that have targeted properties is crucial. While recent methodologies such as Bayesian optimization and deep generative models have made some advances on this issue, these methods often face difficulties in adaptively incorporating various constraints, such as electrical neutrality and targeted properties optimization, while keeping the desired specific crystal structure. To address these challenges, we have developed the Simultaneous Multi-property Optimization using Adaptive Crystal Synthesizer (SMOACS), which utilizes state-of-the-art property prediction models and their gradients to directly optimize input crystal structures for targeted properties simultaneously. SMOACS enables the integration of adaptive constraints into the optimization process without necessitating model retraining. Thanks to this feature, SMOACS has succeeded in simultaneously optimizing targeted properties while maintaining perovskite structures, even with models trained on diverse crystal types. We have demonstrated the band gap optimization while meeting a challenging constraint, that is, maintaining electrical neutrality in large atomic configurations up to 135 atom sites, where the verification of the electrical neutrality is challenging. The properties of the most promising materials have been confirmed by density functional theory calculations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a new method for multi-property optimization of materials called Simultaneous Multi-property Optimization using Adaptive Crystal Synthesizer (SMOACS). SMOACS uses the gradients from neural network based property prediction to optimize materials structures within preset constraints. The paper first introduces the motivation for multi-property materials design that can be constrained for certain types of materials, such as perovskites. The paper also details the important of charge neutrality in materials design, which later becomes a consideration for the proposed design formulation. The introduction also describes past advances in related materials generation methods, such as generative models and bayesian optimization. In Section 2, the paper describes related works focusing on property prediction models, deep generative models and bayesian optimization providing further context for the introduction.

Section 3 of the paper describes the relevant details for SMOACS, including the concrete details of the how the crystal design is constructed along lattice constants and angles, oxidation state, atomic sites and elements. To maintain charge neutrality, the paper proposes a masking method to restrict the actions related to the oxidation state which is described in Section 3.1. Section 3.2 outlines the details of multi-property optimization using training signals from neural network based property prediction models and Section 3.3 describes how SMOACS maintains predefined crystal structures by limiting the range of certain design variables.

Section 4 details the experiments of the paper, including the property prediction models used for the SMOACS algorithm (ALIGNN and Crystalformer). Section 4.2 outlines an experiments without constraints on the crystal structure and Section 4.3 details an experiment with crystal structures constrained to perovskites. In both cases, SMOACS shows general outperformance compared to the Bayesian optimization-based baselines. In addition to the design experiments described in the paper, the authors perform DFT verification of the band gaps of two of the materials designed by SMOACS which showed some agreements and discrepancy. Section 5 consists of a conclusion that summarizes the main findings of the paper

### Strengths
* The paper presents a new method for materials design that effectively utilizes the gradients from property prediction models to optimize materials designs.
* The ability to condition materials design on different properties is a useful and novel feature that many generative models today fail to achieve and as such provide an advantage for SMOACS.
* SMOACS can also enforce constraints through the range of the design values, which could be useful to a variety of design cases.

### Weaknesses
 * The experiments to just one dataset, which means the scope is a bit limited. The authors should consider running further experiments based on crystal structure datasets [1], as well as Perov-5 for perovskites [2].
* The paper could be strengthened by adding more experiments with additional property prediction models, such as commonly used machine learning potentials [3] which should also be covered in the related work section. In the case that some models cannot be used (e.g., because they cannot predict relevant properties) this should also be explained. Specifically, the paper should clarify if the property prediction model needs to be trained on the exact property being optimized, and if fine-tuning a machine learning potential model towards a specific property is a viable alternative.
* In terms of related work, the authors could also benefit from discussing the application of reinforcement learning [4] and GFlowNets [5] for crystal structure design. The same should also be applied to diffusion models [6], flow matching models [7] and language models [8] [9]. It would be good to add details about how those methods compare.
* While SMOACS performs better than the bayesian optimization baselines, the success rate is still low in many cases. The paper should provide more discussion on why the success rate is low, and how future work could improve on this. The paper should also clarify why the low success rate is not a significant issue, given that other methods may also suffer from similar issues.

### Questions
* How are you obtaining gradient signals for properties that are not part of the property prediction model, such as oxidation state? 
   * Does SMOACS have limitations when input variables or properties are not covered by the prediction model?
* Can you add more details on the compute cost and infrastructure used to train SMOACS and how it compares to the baselines studied in the paper?
* While SMOACS performs better than the bayesian optimization baselines, the success rate is still low in many cases. Can you provide some intuition as to why and how future work could improve on this?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes SMOACS, which uses various property prediction models to perform backpropagation to simultaneously optimize the target properties. To maintain electrical neutrality, it restricts the possible values of atomic distribution. Experiments show that the method can achieve a good performance in simultaneously optimizing properties such as band gap and formation energy.

### Strengths
The problem of simultanously optimizing multiple properties for materials is important, and the paper proposes a method that seems to be effective.

### Weaknesses
Novelty: The method uses property prediction model and use backpropagation to optimize the properties. This kind of method has been employed in many prior works such as [1][2][3] and don't seem to be novel.

One limitation of the method is that it heavily relies on good property prediction models. In the case of not enough data, the result may not be good.

Clarity: The method needs to clearly state how the method differs from the prior methods (not just listing the prior methods). Also, it needs to be more clear when introducing the method (e.g., in the section 3.1).

### Questions
N/A

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes an optimization-based method (SMOACS) for materials discovery which aims to optimize (possibly multiple) target properties that are predicted by off-the-shelf predictive ML models. The optimization variables are the axes of a unit cell, the 3D position of N atoms in the cell, probability vectors over K possible elements for each atom, and a D-dimensional probability vector which determines the “oxidation pattern” by essentially selecting a pattern from D templates. A key feature of the method is that, for any given oxidation pattern, the atoms populating the N sites are restricted to adhere to that particular pattern in order to ensure electrical neutrality. With this constraint in place, the method is essentially a first-order gradient-based optimization algorithm with gradients obtained by auto-differentiating the predictive ML models w.r.t. their inputs.

### Strengths
The proposed approach to directly optimize the representation of the material to maximize certain (ML-predicted) properties is interesting. It makes it straightforward to use any available predictive model, as long as it is differentiable w.r.t. its input. It also makes it easy to constrain the optimization algorithm to respect e.g. structure constraints by simply turning off the optimization of some variables (illustrated in the paper) or by adding explicit constraints to the optimizer (not illustrated in the paper).

### Weaknesses
 * In the numerical evaluation the authors show a high “success rate” for SMOACS, which is a metric tailored to the specific properties that are optimized and/or hard-coded into the proposed methods. However, it was not clear to me from the description to which extent the alternative methods (optimization-based TPE and generative FTCP) explicitly target the same properties. It’s mentioned in section 4.4 that TPE includes a term in the objective function for optimizing electric neutrality (except for the results in sec 4.4) but it’s not clear how this is implemented. Nor is it clear how the different terms in the objective function for the different methods are weighed against each other. Since the alternative methods seem to outperform SMOACS on some metrics (e.g. TPE shows good results on BG and FTCP on E_f in Table 2), I wonder how much a better tuning of the these methods could improve the “success rate”. All in all, the numerical evaluation leaves me wondering if this is really a fair comparison.

* Compared with the generative approach (FTCP), SMOACS seems to struggle to find (meta-)stable, and thus synthesizeable, materials as measured by formation energy and inter-atomic distances. Furthermore, stability of a material is a relative property not directly computable from formation energy—for a material to be stable it needs to be in a more favorable energy state than competing phases---making it even harder to say that the materials found by SMOACS are potentially synthesizable. I would say that this is a limitation of the purely optimization-based approach (which only cares about optimizing the target properties of interest) compared with the generative approach (which also tries to generate structures that are “in distribution”, i.e. similar in some sense to the training data samples). I would have liked to see a more in-depth discussion about this limitation (??) of the proposed method.

* The authors deliberately use worse property prediction models for the generative approach (FTCP). Although I appreciate the point that the authors want to make, that SMOACS easily can make use of any (differentiable!) SOTA predictive model which is not always the case for alternative approaches, I would have liked to see comparison with a generative model based on SOTA prediction networks. In particular considering that there are many training-free methods available for conditional generation (see e.g. https://arxiv.org/abs/2306.17775 and the references therein). I am not aware of any such methods specifically for crystal generation (although I would be surprised if no such methods exists), this line of research should at least be acknowledged.

* SMOACS is based on differentiating through the property prediction model w.r.t. its input. It is not clear how this handled non-differentiability of the used model. For instance, GNN-based methods typically construct a graph based on atomic distances, which means that the graph itself might change during the optimization phase of SMOACS (since you “move the atoms around”).

* SMOACS ensures electric neutrality by restricting the search to structures that have the same oxidation pattern as one of a given number of D templates. This seems to restrict the optimization quite a bit, and the choice of D is not discussed in the paper.

* In general I found the paper quite hard to read. Specifically, it lacks a clear and concise formulation of the problem and description of the proposed method early in the paper.

### Questions
Why is it computationally infeasible to calculate electrical neutrality? Enumerating all possible combinations of oxidation numbers will of course be combinatorial, but simply computing the electric neutrality for a given structure should be straightforward, no?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces SMOACS (Simultaneous Multi-property Optimization using Adaptive Crystal Synthesizer), a novel framework for optimizing crystal structures for multiple targeted properties while maintaining key constraints. Unlike traditional generative models, SMOACS utilizes state-of-the-art property prediction models and their gradients to optimize crystal structures via backpropagation directly. This approach allows adaptive constraint integration without model retraining, enabling SMOACS to propose materials optimized for properties like band gap and formation energy. SMOACS outperformed Bayesian optimization and generative models in experiments.

### Strengths
- Originality
  - This work proposes a novel problem of simultaneous multiple properties optimization.
- Quality
  - Extensive experiments are conducted and the DFT is performed to evaluate the generation.
- Clarity
  - The paper is well presented with a clear explanation of the methods.
- Significance
  - The problem is significant for new material discovery.

### Weaknesses
 - The novelty of the method
   - To optimize the property of materials with the gradient of property prediction methods is not new. It was proposed in section 5.3 of [1]
- The evaluation
  - only two properties are optimized, how about more properties like the mechanic properties? How to handle the conflict between different property prediction models. 
  - the success rate is poor.
- The significance of the parameter $\lambda$ in Eq.14
  - How is the strength parameter chosen? It seems to be important to balance the optimization between target property and formation energy. Besides, for more properties, should we use different parameters? This is important since it is not only involved in the training but also the optimization of crystal structures.

### Questions
- parameter significance.
  - see weakness
- the difference between this method and the method used in CDVAE [1].

[1] Tian Xie, ICLR2022, CRYSTAL DIFFUSION VARIATIONAL AUTOENCODER FOR PERIODIC MATERIAL GENERATION

### Soundness
2

### Presentation
3

### Contribution
2
