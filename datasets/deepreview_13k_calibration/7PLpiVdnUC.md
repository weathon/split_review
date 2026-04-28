# Lie Algebra Canonicalization: Equivariant Neural Operators under arbitrary Lie Groups

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
The quest for robust and generalizable machine learning models has driven recent interest in exploiting symmetries through equivariant neural networks. In the context of PDE solvers, recent works have shown that Lie point symmetries can be a useful inductive bias for Physics-Informed Neural Networks (PINNs) through data and loss augmentation. Despite this, directly enforcing equivariance within the model architecture for these problems remains elusive. This is because many PDEs admit non-compact symmetry groups, oftentimes not studied beyond their infinitesimal generators, making them incompatible with most existing equivariant architectures. In this work, we propose Lie aLgebrA Canonicalization (LieLAC), a novel approach that exploits only the action of infinitesimal generators of the symmetry group, circumventing the need for knowledge of the full group structure. To achieve this, we address existing theoretical issues in the canonicalization literature, establishing connections with frame averaging in the case of continuous non-compact groups. Operating within the framework of canonicalization, LieLAC can easily be integrated with unconstrained pre-trained models, transforming inputs to a canonical form before feeding them into the existing model, effectively aligning the input for model inference according to allowed symmetries. LieLAC utilizes standard Lie group descent schemes, achieving equivariance in pre-trained models. Finally, we showcase LieLAC's efficacy on tasks of invariant image classification and Lie point symmetry equivariant neural PDE solvers using pre-trained models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a Lie algebra canonicalization mechanism for achieving equivariance with respect to a variety of Lie groups. The authors propose an extension of the energy based canonicalization mechanism, analyzing limitations of existing work within this framework and describing how the methodology can be extended to work with more exotic (i.e. non-compact, non-abelian) Lie groups, enabling application to a large class of learning tasks where equivariance might be desired. The paper connects frames, canonicalization and frame averaging and the authors show that non-compact groups can be approached via the energy minimization framework where an optimization process makes use of the Lie algebra generators. The methodology is evaluated both on standard invariant image classification tasks as well as physics-informed learning problems dealing with Lie point symmetries.

### Strengths
- The paper is mathematically well-grounded. While I think the presentation could be reorganized (see below) I appreciate the focus that the authors have on providing derivations and proofs for their claims. The objective of unifying (weighted) canonicalization mechanisms and frame theory could prove useful for practitioners in this area.
- I am happy to see extensions to the canonicalization framework, especially ones which focus on making use of the underlying geometry and parametrization of the groups and spaces involved, as well as the treatment of non-compact groups which are under-explored.
- I find the potential use-case of applying this methodology to pre-trained models still under-explored and worthy of further investigation.

### Weaknesses
I think the current presentation lacks focus and the paper could be vastly improved with the objectives of:
- Highlighting clearly the limitations of past/current proposals and how these limitations are overcome, potentially alternating more concrete examples with more abstract limitations.
- Presenting a formalized methodology for the entire (extended) framework that could be understood by practitioners with choices and pitfalls for the spaces, groups, energy functions, etc. involved.

In regards to improving clarity:
- $WFra_{G}(X)$ should be defined before it is used on line 236.
- On lines 270-271 is $N$ simply some value $\in \mathbb{R}$?
- It should be made clearer that $C_{E}(x)$ (line 288-289) refers to the normalized counting measure on $M_{E}(x)$, since we are stating that $C_{E}$ is a probability measure, and then on line 296 we write $C_{E} = \mu_{x}$.
- It would be useful to make clearer for each proposed construction the limitation that exists with the current methodology, e.g. it seems from Definition 2.2 and the subsequent paragraphs one should understand that restricting the support to the orbits and equiping $WCAN_{G}$ with the coarsest topology was not proposed before? Similarly, it would be useful to make clearer what topological limitations appear for non-compact groups, and for which in particular (e.g. we are not just talking about translation).
- In the same spirit clarifying which non-compact Lie groups acting on which spaces (transitively or not) have non-closed orbits would highlight more clearly the settings where the framework should be considered.
- And similarly to the previous comment the cases where the energy $E$ induces a 'reasonable' probability measure on $M_{E}(x)$ could be contrasted with specific/concrete choices of groups and group actions.
- Considering the main proposal of the paper is a general framework I find the discussion in Section 3 much too general and unstructured. It is again highlighted what limitations could exist when one chooses an energy function, however I think it would be much more useful to present a summary of the entire canonicalization framework (and the limitations that were addressed) with a clear outline of potential choices for input spaces and groups (and their actions), potentially in increasing generality (e.g. finite -> compact Lie group -> non-compact Lie group). Once the methodology is clear one highlights criteria for choosing the energy function. Some form of presentation similar to Algorithm 1 in the appendix could potentially appear in the main manuscript given that the energy function is a key component of the generalized framework.
- "What makes moving away from the compactness assumption even worse, is the move away from the matrix view, as any compact Lie group is a matrix group (Knapp, 1996, Chapter 4)" - I don't quite understand what is being claimed here and in the next few sentences. A matrix Lie group is a Lie subgroup of $\textnormal{GL}(n, \mathbb{R})$ (or $\mathbb{C}$). Non-compact matrix Lie groups can also be decomposed/expressed as a product of exponentials, and one can optimize using their Lie algebra elements, see e.g. [3] and [4].
- I'm left not understanding what the authors mean when they state that their framework requires  less knowledge about the symmetry group. This is highlighted both in the presentation of the contributions as well as in the experiments, e.g. for invariant classification a comparison is done with [1], I assume as opposed to [1] and [2]? I don't have an issue with what results are cited, but it is not made clear what knowledge about the Lie group is needed for [2] that isn't needed for [1]?

I think the authors should focus on improving/rewriting parts of Sections 2 and 3 with the focus of highlighting both the limitations their framework overcomes and providing a clearer presentation of how the methodology can be applied in different cases.

Some of the expression/grammar in the appendix could also be improved, e.g. "Liealgebra descent", "why failure modes exists".

### Questions
Besides the questions in the weaknesses section:
- Can you clarify what role does the Haar measure play in the construction of weighted canonicalizations for the non-compact case? Does unimodularity play a role here? Is the case where the modular function is unbounded pose any additional obstructions?
- Is it not possible to make use of a riemannian structure on the group and have the energy minimizer be defined in terms of geodesic distance? It seems the current proposal already looks to work within the tangent space of the groups involved.
- Canonicalization methods IIUC deal with global invariance/equivariance, as opposed to e.g. lifting + regular/steerable convolutions which could deal with local equivariance (e.g. imagine 2 objects in an image rotated at different angles). I'm wondering if the authors would find this distinction worthy of highlighting.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The contribution of this paper can be summarized as follows:
- An extension of frames and canonicalization for neural network symmetrization [1-4] to non-compact Lie groups specified by their infinitesimal generators (Section 2.2 and 3),
- A class of optimization-based algorithms for the above energy-based canonicalization using (coordinate) Lie algebra descent (Appendix H),
- Applications of the proposed method to affine and homography group invariant MNIST classification (Section 4.2) and, importantly, neural operator modeling of three PDEs with known point symmetry groups by canonicalizing a pre-trained model (Section 4.3).

[1] Puny et al. Frame averaging for invariant and equivariant network design (2021)

[2] Kaba et al. Equivariance with learned canonicalization functions (2023)

[3] Dym et al. Equivariant frames and the impossibility of continuous canonicalization (2024)

[4] Ma et al. A canonicalization perspective on invariant and equivariant learning (2024)

### Strengths
- S1. The contributions of this paper can be understood from two perspectives. The first is extending frame/canonicalization approaches for neural network symmetrization to non-compact Lie groups specified by their infinitesimal generators. The second is improving the performance of pre-trained neural operators for PDEs by canonicalizing them in accordance to the point symmetry of a downstream PDE. Both are original and significant contributions as far as I am aware.
- S2. The extension of frames and canonicalization considered in prior work [3, 4] to non-compact Lie groups, and the proposed Lie algebra descent algorithms that implement the idea, are original and technically sound as far as I am aware.
- S3. Experimental results are shown for a comprehensive set of problems (synthetic, two computer vision problems, and three PDEs) with informative visualizations and support the validity of the approach.

[3] Dym et al. Equivariant frames and the impossibility of continuous canonicalization (2024)

[4] Ma et al. A canonicalization perspective on invariant and equivariant learning (2024)

### Weaknesses
 - W1. In Section 2.2, the authors propose to treat non-weighted energy-minimizing closed canonicalization as weighted canonicalization by taking the normalized Hausdorff measure on energy minimizing set (Line 287-296). The resulting class of weighted closed canonicalization (Theorem 2.7) has a weakness that, with the energy function specified, it is not possible to adjust the weights of canonicalization from training data, unlike in related prior work [5-7]. This may have led to the reliance on carefully designed energy functions based on domain knowledge (Line 324-332 and Section 4.3) which leaves a room for improvement. Specifically, the method lacks a mechanism to learn the appropriate weighting of different canonical forms based on the data distribution, which could limit its adaptability to complex datasets where a single, hand-designed energy function may not be sufficient. The reliance on a fixed energy function means that the canonicalization process is not data-driven, potentially leading to suboptimal performance in scenarios where the ideal canonical forms are not well-aligned with the chosen energy function.
- W2. For the ACE experiment (Section 4.3.3), the current comparison is made only between Poseidon and its canonicalization. A comparison to existing intrinsically symmetric methods [8, 9] would be informative and show the usefulness of canonicalization, since Poseidon can benefit from pre-training while intrinsically symmetric approaches cannot. The absence of such a comparison makes it difficult to assess whether the proposed canonicalization method offers a significant advantage over existing methods that directly enforce symmetry in the network architecture. It is important to demonstrate that the canonicalization approach provides a performance benefit beyond what can be achieved by simply training a network with built-in symmetries, especially given the computational overhead of the canonicalization process.

### Questions
Please see the weaknesses section.

### Soundness
3

### Presentation
3

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
This paper extends the energy-based canonicalization approach, introduced in [1] to settings where the group in non-discrete and non-compact, exploiting only the infinitesimal generators of Lie algebras. They provide a general framework of constructing energy functionals which can be optimized using standard Lie group descent schemes.'
 
[1] Sékou-Oumar Kaba, Arnab Kumar Mondal, Yan Zhang, Yoshua Bengio, and Siamak Ravanbakhsh.Equivariance with Learned Canonicalization Functions. In Proceedings of the 40th International Conference on Machine Learning, pp. 15546–15566. PMLR, July 2023.

### Strengths
The topic of constructing equivariant networks when one only has access to the infinitesimal generators is an extremely interesting and well-motivated direction of research. The approach this paper takes, which is adapting the canonicalization framework for these settings is novel and using the energy-based canonicalization seems like a promising direction for these cases.  The figures in the paper are also very useful and help provide an intuition for how canonicalization is helping.

### Weaknesses
- One of the main limitations of the paper is that how the theoretical results and understandings provided in sections 2 and 3 are used in practice to train a canonicalizer network is not well-explained. I found it difficult to follow how the energy functionals were constructed  in each of the cases and how much that approach is generalizable to more complex systems and PDEs. Specifically, the connection between the abstract Lie algebra concepts and the concrete parameterization of the energy functional as a neural network is unclear. It's not obvious how the infinitesimal generators are used to define the loss function or how the network learns to perform canonicalization based on this energy. The paper lacks a clear explanation of how the theoretical framework translates into a practical training algorithm for the canonicalizer.
- The general experimental setup was not well-explained in the paper. For example, it would be better to include a main algorithm, provide a more detailed explanation of how the energy functional was constructed in each of the experiments settings, and clearly explain the experimental setup and training of each of the datasets. The descriptions of the datasets and the specific architectures used for the energy functionals are too brief. The paper should include a detailed algorithm outlining the training process, including the specific loss functions used, the optimization procedure, and the hyperparameter settings. It is also unclear how the choice of energy functional impacts the performance and equivariance of the learned canonicalization.
- The reported results do not include standard deviations over seeds (for example, in tables 1 and 2), and the results for Heat and Burgers’ are missing from the main paper (although included in the appendix). The paper also doesn’t include any comparisons with other baselines, such as data or loss augmentation. The lack of standard deviations makes it difficult to assess the statistical significance of the results. Furthermore, the absence of comparisons with data augmentation or other equivariant learning techniques makes it hard to evaluate the effectiveness of the proposed method. The paper should include a more comprehensive experimental evaluation with multiple seeds and comparisons to relevant baselines.
- The paper could be strengthened by providing an understanding of how expensive these optimizations are and how generalizable the suggested approach is for more complex settings. The computational cost of training the canonicalizer and applying it to new data is not discussed. It is also unclear how the approach would scale to more complex PDEs or higher-dimensional data. The paper should include a discussion of the computational complexity of the proposed method and its limitations in terms of scalability and generalizability.

### Questions
See above.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes LieLAC, a method to make pre-trained models equivariant to Lie group symmetries through input canonicalization via energy minimization. The key strength of the work is its well-grounded theoretical foundation and potential applicability to a wide range of symmetry groups and tasks. However, the practical challenges of finding an appropriate energy function, finding its minimizer, the requirement of finetuning canonicalized network and limited experimental evaluation raise concerns about broader applicability beyond simple demonstrated cases.

### Strengths
1. The proposed canonicalization approach allows employing pre-trained non-equivariant models while making them equivariant with canonicalization.
2. The paper provides a good overview of the related work on canonicalization and frame-averaging methods.
2. Figure 1 provides an intuitive example of the effect of canonicalization on the decision boundary.
3. The proposed approach is generic and is potentially applicable to a wide range of models and learning tasks.
4. The paper provides strong theoretical support for the proposed method.
5. Canonicalization and frame averaging methods have been demonstrated to be successful in various domains, including geometric and imaging modalities. The paper further extends the canonicalization framework to PDE/ODE modeling with more complex symmetry groups.
6. The paper nicely elaborates on the challenges of choosing the appropriate energy function and it outlines key considerations in doing so.

### Weaknesses
1. The paper states "Prior work on equivariant neural networks focuses on simple groups ... that are not reach enough to encode specific structure found in scientific applications". Does it apply to the recently introduced Clifford algebra and geometric algebra networks which aim to provide a more general and flexible framework for equivariant NNs?
2. Paper is uneasy to digest. For example, 4 definitions, 3  theorems, 3 propositions, and one lemma are stated on just two pages.  Authors should think about how to make the flow of the paper more intuitive by either providing a more comprehensive background or by presenting a simplified formulation in the main text of the paper while providing the complete theoretical details in the appendix.
3. The distance-based relaxation in 331-333 is not clear. Can authors elaborate more on what is meant here?
4. While the method initially appears generic, finding the minimizer of the energy function is challenging and it is not clear how well it can be done besides the cases presented in the paper. The optimization problem of energy minimization in Eq.2 requires a lot of design choices and heuristics such as adversarial regularization. Furthermore, the choice of energy function is not well motivated and it is unclear how to choose it for a new symmetry group.
5. Experimental evaluation is rather limited and is focused on toy or simple tasks. Also, the reported PDE evolution errors are reported only on one instance of initial conditions. The MNIST experiments, while demonstrating a complex group, are still on a relatively simple dataset. The PDE experiments are also limited to simple 1D cases, and it is not clear how the method would scale to more complex, higher-dimensional problems.
6. Table 2 suggests the misalignment of canonicalized samples with the original data indeed takes place (LieLAC+Poseidon vs Poseidon+ft) which again outlines the challenge of minimizing the energy function. This requires finetuning the baseline neural solver to adapt to new OOD  samples which can be a serious practical bottleneck.

### Questions
I suggest authors address and elaborate on weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
