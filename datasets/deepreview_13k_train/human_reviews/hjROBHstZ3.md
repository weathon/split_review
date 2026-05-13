# Causal Representation Learning from Multimodal Biological Observations

- Decision: Accept
- Scores: 6, 8, 6, 6, 3

## Abstract
Prevalent in biological applications (e.g., human phenotype measurements), multimodal datasets can provide valuable insights into the underlying biological mechanisms.
However, current machine learning models designed to analyze such datasets still lack interpretability and theoretical guarantees, which are essential to biological applications.
Recent advances in causal representation learning have shown promise in uncovering the interpretable latent causal variables with formal theoretical certificates. 
Unfortunately, existing works for multimodal distributions either rely on restrictive parametric assumptions or provide rather coarse identification results, limiting their applicability to biological research which favors a detailed understanding of the mechanisms.

In this work, we aim to develop flexible identification conditions for multimodal data and principled methods to facilitate the understanding of biological datasets.
Theoretically, we consider a flexible nonparametric latent distribution (c.f., parametric assumptions in prior work) permitting causal relationships across potentially different modalities. 
We establish identifiability guarantees for each latent component, extending the subspace identification results from prior work.
Our key theoretical ingredient is the structural sparsity of the causal connections among distinct modalities, which, as we will discuss, is natural for a large collection of biological systems.
Empirically, we propose a practical framework to instantiate our theoretical insights. We demonstrate the effectiveness of our approach through extensive experiments on both numerical and synthetic datasets. 
Results on a real-world human phenotype dataset are consistent with established medical research, validating our theoretical and methodological framework.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the causal graph discovery problem from multiview data. Given observed multimodal data, the goal is to estimate the causal relationship of latent features between modalities. The authors study the data generation process where the observed multimodal data are independent given the latent variables. Under this assumption, the authors employ the encoder-decoder framework to decompose the latent factors and nuisance factors, and a sparsity regularization function to impose the sparse relationship between modalities in the latent spaces. They compare the proposed method with several baselines on simulated tasks and the results show improved mean correlation coefficient. Furthermore, the proposed method is applied to human phenotype dataset.

### Strengths
This paper tackles an important and yet not well-addressed problem. It is well-motivated by biomedical applications. The proposed framework is more general compared to the prior work (as shown in Table 1).

### Weaknesses
In general, I find several parts that need further clarification. (see the question parts)

My main concern is that the simulated tasks focus on low-dimensional data with simple sparse causal structures. It is not clear whether the method is scalable and can be generalized to more complex causal structures. Specifically, the simulation settings do not explore the impact of increasing the number of latent variables or the dimensionality of the observed data, which are crucial for assessing the practical applicability of the method. The current experiments also do not explore the robustness of the method to violations of the sparsity assumption, which is a key component of the proposed approach.

### Questions
a. the paper assumes that the latent variables within the same modality form a DAG, could the author clarify why this assumption is necessary? Secondly, if this is needed, the loss function (6) does not enforce the latent variables within the same modality to be a DAG. How can we ensure such structures will be satisfied in the learning phase?

b. does the causal relationship between different modalities need to be DAG? If there are cycles, are we still being able to identify the latent variables?

c. I find the definition of condition 4.3 confusing. What are the connections between matrices A, G, T? and A seems to only denote the relationship between modality 1 and 2?

d. In Assumption A.1, what is smooth inverse?

e. Could the authors provide a guideline for practitioners on how to systematically choose the number of latent nodes?

f. In Theorem 4.4, does it require the regularization term to be scaled by some coefficient?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper provides a method that identifies the latent variables up to invertible component-wise transformations from multi-view data under the weak assumption that these latent variables exert partial influence on every modality and strong influence on one modality. The proposed approach relies on weaker assumptions compared to the existing works and yet provides strong results. The primary motivation for this approach is on multimodal health care data but the experiments are conducted on both synthetic and image datasets in addition to health care data.

### Strengths
1.   The contribution is very clear and useful for future works on identifiability. More strengths included in the summary.
2.   The writing is lucid. The examples are cleverly used to contrast the proposed method against the existing works.

### Weaknesses
I did not find any significant weaknesses. However, I do have a few questions for the sake of clarity. Questions in the following section.

Typos and minor writing mistakes:

1. In line 78, what is $n$? Is it $z_i^{(m)}\rightarrow z_j^{(n)}$?
2. Is the co-domain of $G(z, \epsilon)$ correct in line 303?
3. Some issues with the references. E.g., "Non-parametric Identifiability of causal representations from unknown interventions" appeared in NeurIPS 2023. Sturma et al., (2023) cited twice in lines 126-127.

### Questions
1. It is assumed that the information of $z^{(m)}$ is preserved in its corresponding observation $x^{(m)}$ and it exerts sufficient influence on other modalities' observations $x^{(-m)}$. Now, consider the observation from another modality $x^{(k)}$ that has a similar behavior. How does $z^{(k)}$ not interfere in the identifiability of the subspace of $z^{(m)}$?
2. Is the considered setting a non-linear version of [10]? Can the authors add text comparing/contrasting the proposed approach with [10]?
3. Does "fully share" mean "retrieve without errors" in line 212? That's what I understood from the example that follows this statement in line 215.
4. Can the authors explain how the method is different from [9] apart from the latent variables being independent in [9]?Specifically, what does "part of the variables are directly observed and causal directions are given by default" mean in lines 335-338?
5. Can the authors add an intuitive description for Condition 4.3 as its implications are not clear from the main text? It is enough that this intuitive explanation is included in the appendix.


Typos and minor writing mistakes:

1. In line 78, what is $n$? Is it $z_i^{(m)}\rightarrow z_j^{(n)}$?
2. Is the co-domain of $G(z, \epsilon)$ correct in line 303?
3. Some issues with the references. E.g., "Non-parametric Identifiability of causal representations from unknown interventions" appeared in NeurIPS 2023. Sturma et al., (2023) cited twice in lines 126-127.


[1] Sturma et al., 2023, "Unpaired Multi-domain Causal Representation Learning", NeurIPS 2023

[2] Zheng et al., 2022, "On the Identifiability of Nonlinear ICA: Sparsity and Beyond", NeurIPS 2022

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Authors develop new methods to identify patterns in complex multi-modal biological datasets. It improves upon previous work in two key ways: First, it uses a flexible mathematical framework that doesn't make rigid assumptions about how the underlying biological factors (latent factors) are distributed. Second, these factors can influence each other across different modalities. Simulation study and real-world data support authors's claim.

### Strengths
1. The paper is well-written and motivated. 
2. Authors provide identifiability guarantees for each latent component. This is helpful to characterize the interactions among all latent
components across modalities for the biological applications. 
3. The assumptions of theoretical results look reasonable to me. 
4. Real-world dataset analysis is provided, demonstrating its usefulness.

### Weaknesses
1. A1 indicated the neural network needs to be invertible. How do authors achieve this? Authors use normalizing flow, an invertible generative model, as a part of their network, what about others? Also what's the computation efficiency? 
2. In real world, user-defined number of latent variables can be biased. Have authors analyzed it?

### Questions
See above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper develops a theory for identifying the underlying structure of multi-modal data involving latent causal variables, based on the assumption of smooth invertible generating functions. It further investigates the sparsity of this causal structure and proposes an estimation method. Experiments conducted on both synthetic and real human phenotype data demonstrate the effectiveness of the proposed approach.

### Strengths
- The paper is generally well-written.
- It includes an adequate literature review.

### Weaknesses
 - On real impact. As mentioned by the authors, knowing the number of underlying latent variables is unrealistic.

- Missing implementation details, e.g., more details on data generation, network structure, optimization scheme, hyper-parameters, etc. see questions as well.

- The explanation of the adjacency matrix A is unclear. The relationship between the latent variables z and the adjacency matrix A is not well-defined. It is unclear how the values of z are used to determine the structure of A.

- The causal relationship between the colored MNIST and fashion MNIST datasets is not clearly explained. It is unclear how the latent variables in one dataset influence the latent variables in the other dataset.

### Questions
1. In my view, the example provided in Section 3 does not align well with the proposed model. What is your rationale for considering heart sizes and bone structures as latent variables?
2. In Appendix D.1, could you provide further details on the MLP architecture used for the numerical data generation process? Have you considered implementing an invertible neural network structure in your simulations? If you increase the number of data samples, do you expect the MCC to approach 1? I would appreciate seeing results on this, particularly illustrated with four variables (two latent and two observed).
3. The arrow from $z$ to the adjacency matrix in Figure 4 is unclear. Could you clarify this relationship?
4. How did you compute the KL divergence? Do you assume that $p(\gamma)$ follows a Gaussian distribution, with the encoder output providing the mean and variance?
5. When calculating the SHD, given that the indices of latent variables can be permuted, could this pose an issue?
6. In the context of the MNIST dataset, what causal relationship exists between the colored MNIST and fashion MNIST data?
7. How does the learned adjacency matrix A relate to the one derived from the PC algorithm?

Comment:
For the real-world application, I encourage the authors to explicitly present evidence from the literature demonstrating the success of their algorithm.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses the identification of hidden causes underlying observed multimodal data. The authors propose a model that avoids previous limitations, specifically not requiring shared latent information across multiple modalities or assuming an exponential family distribution for hidden causes. The paper provides a theoretical identifiability analysis and presents experiments, including one on biological data.

### Strengths
The paper presents meaningful relaxations of assumptions from prior work.

It is relatively well-written, considering the complexity of the theory and notation involved.

### Weaknesses
There are issues with the main theoretical claims and their proofs.

The practicality of the current assumptions and their real-world applicability remains unclear.

The experiment using the human phenotype data does not justify the title or the highlights in the abstract.

### Theory

1. *Identification vs. Estimation*: In Theorems 4.2 and 4.4, identification and estimation are confused by statements like “We estimate the generating process…”. Identification is a model property and should be established before estimation is addressed. For a model $\mathcal{P}:=\{p_{\phi}:\phi \in \Phi\}$, we simply show that $\forall \phi_1, \phi_2 \in \Phi (p_{\phi_1}=p_{\phi_2} \implies \phi_1=\phi_2)$ to demonstrate identification. The current formulation appears to conflate the conditions for parameter identifiability with the process of parameter estimation, which are distinct concepts.

2. *"Identification under Regularization"*: Particularly, Theorem 4.4 is problematic in stating that identification is achieved through regularization, which pertains to estimation. If regularization is essential, the model should be reformulated—like for ridge regression, the regularization can be treated as a sparse prior in a probabilistic model. The use of regularization as a means to achieve identifiability is conceptually flawed; regularization is a technique used during estimation to improve generalization, not a property that ensures the uniqueness of model parameters.

3. *Proof of Theorem 4.2*: The step to equation (14) seems to rely on $x=\hat{x}$. However, equal distributions do not imply equal values of random variables. If (14) is correct, the derivation should clarify how equal distribution leads to (14). The jump from equal distributions to equal values of random variables is not mathematically justified. The proof needs to explicitly show how the equality of distributions implies the specific equality used in equation (14).

4. *Definition of $\tilde{g}_x$*: Strictly speaking, there is one $\tilde{g}_x$ for each $m$, and it’s unclear if these $m$ functions can be shown as the same function. If not, we are in fact making assumptions about $m$ functions. The notation $\tilde{g}_x$ is ambiguous, as it seems to imply a single function when, in fact, there should be a separate function for each modality $m$. This needs to be clarified, and the implications of having $m$ distinct functions should be discussed.

5. *Proof of Theorem 4.4*: 1) Condition 4.3 mentions *undefined matrix $A$*. In the proof, equation (28) involves more than a single matrix,  as denoted by $A$ in Condition 4.3, and the definition of $d^*(U)$ does not seem to align with $d^*$ in Condition 4.3 (this questionable reasoning later is extended to $D$). This proof section is unclear both in notation and logic flow; we can not even see $A$ as a placeholder for the various matrices used in equation (28)! I suggest sorting out the involved matrixes (I believe, if the proof is not simply wrong, there should be several similar conditions for different matrixes), and a clear connection between the proof and assumptions should be seen. The use of a single matrix $A$ in the condition, while the proof uses multiple matrices, creates a significant disconnect. The proof needs to clearly define each matrix and show how they relate to the condition. 2) *the regularization again*: the reasoning following equation (29) requires satisfaction of (29), but regularization (5) can only encourage, not guarantee this condition. This suggests the idea of “identification under regularization” itself does not work, not only an incorrect formulation as mentioned in the 2nd point.

### Implications
One core aspect of the causal model is that two modalities cannot share any direct causes, which is questionable. While $z^{(m)}$ can, and indeed is required to, affect $x^{(-m)}$ indirectly through $z^{(-m)}$, this seems to require hidden causes $z$ to be lower-level features. For example, “age” is a high-level feature affecting many modalities, like “sleep” and “eyes.” Thus, if the "sleep" modality includes "age" in $z^{sleep}$, then, to satisfy the "indirect" causes requirement, lower-level features $z^{eyes}$ would be needed to mediate the causal effects from “age” to “eyes", i.e., $d(z^{eyes})$ should be large enough to block all the causal effects from “age” to “eyes.” And, when we have many modalities and many hidden causes, this eventually requires most hidden causes to be low-level.

While the theoretical relaxations and real-world examples are appreciated, it’s unclear why, in the “sleep patterns” and “brain imaging” examples, your assumptions could be satisfied, though I can see previous ones are limited.


### Biological Application
The demonstration of the biological application lacks depth, and the claimed “strong interpretability” is overstated. For example, in the human phenotype dataset, how should we interpret the learned hidden variables? Does the method enhance our understanding of the data or its underlying mechanisms? How does the number of latent variables affect the results (possibly with very different causal graphs)?

Additional specific questions are: Why are causal relationships involving FRight and FLeft not symmetric? For example, why does FRight affect Cataract but not FLeft?
Why are there no Sleep variables that influence “Sleep efficiency”?
Shouldn’t ocular quality impact hand grip strength rather than the reverse?

More experiments should be conducted, both on the model side (e.g., testing various numbers of latent variables and other hyperparameters) and the data side (e.g., trying many different modalities).


Overall, the authors could clean up theoretical developments, clarify the practical implications, and leave the biological application to future work.

### Questions
### Theory

1. *Identification vs. Estimation*: In Theorems 4.2 and 4.4, identification and estimation are confused by statements like “We estimate the generating process…”. Identification is a model property and should be established before estimation is addressed. For a model $\mathcal{P}:=\\{p_{\phi}:\phi \in \Phi\\}$, we simply show that $\forall \phi_1, \phi_2 \in \Phi (p_{\phi_1}=p_{\phi_2} \implies \phi_1=\phi_2)$ to demonstrate identification.

2. *"Identification under Regularization"*: Particularly, Theorem 4.4 is problematic in stating that identification is achieved through regularization, which pertains to estimation. If regularization is essential, the model should be reformulated—like for ridge regression, the regularization can be treated as a sparse prior in a probabilistic model.

3. *Proof of Theorem 4.2*: The step to equation (14) seems to rely on $x=\hat{x}$. However, equal distributions do not imply equal values of random variables. If (14) is correct, the derivation should clarify how equal distribution leads to (14).

4. *Definition of $\tilde{g}_x$*: Strictly speaking, there is one $\tilde{g}_x$ for each $m$, and it’s unclear if these $m$ functions can be shown as the same function. If not, we are in fact making assumptions about $m$ functions.

5. *Proof of Theorem 4.4*: 1) Condition 4.3 mentions *undefined matrix $A$*. In the proof, equation (28) involves more than a single matrix,  as denoted by $A$ in Condition 4.3, and the definition of $d^*(U)$ does not seem to align with $d^*$ in Condition 4.3 (this questionable reasoning later is extended to $D$). This proof section is unclear both in notation and logic flow; we can not even see $A$ as a placeholder for the various matrices used in equation (28)! I suggest sorting out the involved matrixes (I believe, if the proof is not simply wrong, there should be several similar conditions for different matrixes), and a clear connection between the proof and assumptions should be seen. 2) *the regularization again*: the reasoning following equation (29) requires satisfaction of (29), but regularization (5) can only encourage, not guarantee this condition. This suggests the idea of “identification under regularization” itself does not work, not only an incorrect formulation as mentioned in the 2nd point.

### Implications
One core aspect of the causal model is that two modalities cannot share any direct causes, which is questionable. While $z^{(m)}$ can, and indeed is required to, affect $x^{(-m)}$ indirectly through $z^{(-m)}$, this seems to require hidden causes $z$ to be lower-level features. For example, “age” is a high-level feature affecting many modalities, like “sleep” and “eyes.” Thus, if the "sleep" modality includes "age" in $z^{sleep}$, then, to satisfy the "indirect" causes requirement, lower-level features $z^{eyes}$ would be needed to mediate the causal effects from “age” to “eyes", i.e., $d(z^{eyes})$ should be large enough to block all the causal effects from “age” to “eyes.” And, when we have many modalities and many hidden causes, this eventually requires most hidden causes to be low-level.

While the theoretical relaxations and real-world examples are appreciated, it’s unclear why, in the “sleep patterns” and “brain imaging” examples, your assumptions could be satisfied, though I can see previous ones are limited.


### Biological Application
The demonstration of the biological application lacks depth, and the claimed “strong interpretability” is overstated. For example, in the human phenotype dataset, how should we interpret the learned hidden variables? Does the method enhance our understanding of the data or its underlying mechanisms? How does the number of latent variables affect the results (possibly with very different causal graphs)?

Additional specific questions are: Why are causal relationships involving FRight and FLeft not symmetric? For example, why does FRight affect Cataract but not FLeft?
Why are there no Sleep variables that influence “Sleep efficiency”?
Shouldn’t ocular quality impact hand grip strength rather than the reverse?

More experiments should be conducted, both on the model side (e.g., testing various numbers of latent variables and other hyperparameters) and the data side (e.g., trying many different modalities). 


Overall, the authors could clean up theoretical developments, clarify the practical implications, and leave the biological application to future work.

### Soundness
2

### Presentation
2

### Contribution
2
