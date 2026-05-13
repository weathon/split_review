# Learning equivariant tensor functions with applications to sparse vector recovery

- Decision: Reject
- Scores: 5, 5, 8, 5

## Abstract
This work characterizes equivariant polynomial functions from tuples of tensor inputs to tensor outputs. Loosely motivated by physics, we focus on equivariant functions with respect to the diagonal action of the orthogonal group on tensors. We show how to extend this characterization to other linear algebraic groups, including the Lorentz and symplectic groups. 

    Our goal behind these characterizations is to define equivariant machine learning models. In particular, we focus on the sparse vector estimation problem. This problem has been broadly studied in the theoretical computer science literature, and explicit spectral methods, derived by techniques from sum-of-squares, can be shown to recover sparse vectors under certain assumptions. Our numerical results show that the proposed equivariant machine learning models can learn spectral methods that outperform the best theoretically known spectral methods in some regimes. The experiments also suggest that learned spectral methods can solve the problem in settings that have not yet been theoretically analyzed.

    This is an example of a promising direction in which theory can inform machine learning models and machine learning models could inform theory.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work characterizes equivariant polynomial functions from tuples of tensor inputs to tensor outputs. The goal behind these characterizations is to define equivariant machine learning models. In particular, they focus on the sparse vector estimation problem. They try to recover a sparse vector from the given an orthonormal basis of subspace spanned by $d$ vectors, where one is the sparse vector to be recovered and the other $d-1$ are just vectors. The recovered sparse vector is stated in (25) and the contributed is how to construct $h$.

### Strengths
They construct a equivariant function $h$.

### Weaknesses
There are some question you need to solve:

1 Are there some applications about your proposed problem to recover a sparse vector?

2. The representation of $h$ is only related to matrices, but not a complex tensor. Your definitions and analysis are all based on tensors. 

3. Can you give a details how to get (28) from Corollary 1?

4. Why you set $h$ to be a equivariant function? What is the advantages?

5. In the numerical experiments about mnist, do you get the similar results if you choose $v_1,\cdots, v_{d-1}$ to be some other vectors which is not so related to the sparse vector?

6. How to get the orthonormal basis for the spanned subspace? Do you get the similar results if you choose different orthonormal basis?

### Questions
See weakness.

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
3

### Summary
This paper studies polynomial functions from tensor spaces to tensor spaces that are preserved by the action of the Orthogonal group O(d), the indefinite orthogonal group O(s, k-s) or the symplectic group Sp(d). The authors provide a characterization of such polynomial functions in the form of a linear combination of "elementary functions".

As a main application of such result authors propose an algorithm for planted vector recovery, dictionary learning, and experimentally demonstrated that the proposed algorithm outperforms earlier proposed Sum-of-Squares based methods.

Study of such polynomial function is also tangentially motivated by physics applications.

### Strengths
The characterization of equivariant polynomial functions studied in this paper is demonstrated to have applications to a planted sparse vector recovery problem which has several practical applications and received a lot of attention over the past decade. In this problem, one is given a linear space $L$ defined by a sparse planted vector $v_1$ and randomly selected complement basis $v_2, ... v_n$. The goal is to recover vector $v_1$ from $L$. The Authors observe that the function $h: L \rightarrow v_1$ is equivariant so can be parametrized using the main characterization proven in this paper and they learn parameters of h by training NN over the training dataset.
I think that this is a new interesting approach to the sparse vector recovery problem.

The proposed characterizations of equivariant polynomial functions may find applications in other areas and may be of its own interest.

### Weaknesses
If I understand the proposed approach to the sparse vector recovery problem, for the approach to work one actually need to observe many data samples to be able to train neural networks that define coefficients for the unknown polynomial $h: L \rightarrow v_1$. This may be a strong assumption in many applications and is different from SOS-based methods that can recover $v_1$ from observing only one subspace L and does not require to go through the learning process. Furthermore, the need for a training dataset raises questions about the generalization capabilities of the learned function $h$. Specifically, if the training data does not adequately represent the diversity of possible subspaces $L$ or the distribution of the planted sparse vectors $v_1$, the learned function might not perform well on unseen data. The reliance on a large training set also introduces a computational overhead not present in methods that directly solve for $v_1$ from a single subspace observation.

The proof of the main theorem follows standard steps for this sort of problems: problem is easily reduced to homogenous degree r monomials and for homogeneous degree monomials the characterization is obtained by using a somewhat standard group averaging technique. In this sense, the proof of the main result is somewhat "standard" for the literature.

### Questions
1. Can you provide a bit more insight into what are the requirements for the training set for your method to be able to train the neural networks defining coefficients in the parametrization of h in Eq 28? Do you need to assume that all training samples have the same planted sparse vector $v_1$? Or is it sufficient to assume that all such vectors $v_1$ are coming from some distribution with nice properties?
2. How many training samples do you anticipate needing to recover $n$-dimensional planted sparse vector? 
3. Are you aware of any immediate applications of the provided characterizations for the indefinite orthogonal group O(s, k-s) or the symplectic group Sp(d)?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper develop a generic framework for defining functions that are equiv-
ariant under the action of classical Lie groups acting diagonally on tensors.
The groups considered include the orthogonal group O(d), the indefinite orthogonal group O(s,k− s), and the symplectic group Sp(d) and other general group actions. The main theoretical contribution is a characterization of
O(d)-equivariant polynomial functions mapping multiple tensor inputs to tensor outputs. The authors prove that any such functions can be expressed as linear
combination of tensor products of the inputs with O(d) isotropic tensors. An
important result is Theorem 1, which provides an explicit parameterization
of O(d)-equivariant polynomial functions. The authors also present a practical
corollary (Corollary 1) for the case where the inputs are vectors and the out-
puts are vector spaces, showing that the equivariant functions can be written
as linear combinations of basis elements formed by permutations of the input
vectors. Furthermore, the author also present a generalization form of general
tensors in Theorem 2 and Corollary 2.

As a proof of concept, They consider the challenge of recovering a planted
sparse vector from a set of vectors forming an orthonormal basis of a sub-
space. By designing a machine learning model that learns an equivariant 2-
tensor (which is the covariance matrix) from data, they use the top eigenvector
of this tensor as an estimator for the sparse vector. The numerical experiments
demonstrate that the learned algorithms outperform state-of-the-art methods.
The models adapt effectively to various noise structures and data sampling
methods.

In physics, Lorentz group O(1,3) is a special case of the equivariant group.
Particularly in general relativity, tensors are used to describe physical quantities such as the curvature of spacetime, energy-momentum distributions. The
authors’ work generally present one of the proof for how to comprehend this
structure in the regime of mathematical tensor products. they also provide a
framework for building physics informed machine learning models that inherently respect Lorentz symmetry and applying for advanced physics studies.

### Strengths
## Originality
The paper presents a novel and significant advancement in the field of equiv-
ariant machine learning. Additionally, it uniquely incorporates the indefinite
orthogonal group O(s,k− s) and the symplectic group Sp(d), which are funda-
mental in physics and other scientific domains but have been less explored in the
context of physics informed machine learning. The application of these theo-
retical developments to the sparse vector estimation problem further showcases
originality by demonstrating how algorithms can outperform state-of-the-art
methods in regimes not previously addressed.

## Quality
The paper is of high quality, offering rigorous mathematical formulations and
proofs that underpin the proposed methods. The experiments are well-designed,
and the empirical results convincingly demonstrate the effectiveness.

## Significance
The significance of the work is substantial. By providing explicit parameteriza-
tions for equivariant functions of tensor inputs and outputs, the paper equips
researchers and practitioners with powerful tools. The successful application to
sparse vector es

### Weaknesses
## Limited Scope of Experiments
One of the main weaknesses of the paper is the limited scope of the experimental
evaluation. The experiments are primarily focused on the sparse vector estima-
tion problem, which, while important, represents a rather narrow application
domain. The method should have broader applications, such as in physics and
general relativity, but these areas are not sufficiently discussed or explored.

## Clarity
The paper is difficult to follow due to disorganized notation and unclear variable
definitions. The use of coordinates is somewhat messy, which makes the math-
ematical developments hard to track. Variables are often introduced without
proper explanation or context, causing confusion. For example:

• In Definition 4, the indices need more explanation.

• In Theorem 1, how each tensor alk contracts with certain indices (dimen-
sions) of cl1 ,l2 ,...,lr should be explained more clearly.

• In Example 1, there should be more explanation of why only the generic
elements of the G4 group are used while others are contracted.

• In Lemma 1, the meaning and constraints of ασ need clarification.
Moreover, the progression from theoretical concepts to experimental appli-
cations lacks smoothness. The presentation could be improved by organizing
notation more systematically and clearly defining all variables.

## Comparative Analysis
There are other contemporary techniques for sparse vector recovery and tensor
analysis that are not considered. The lack of comparison with a wider array
of methods makes it difficult to fully assess the advantages of the proposed
approach.

### Questions
• The statement of Theorem 1 introduces a complex expression involving
linear combinations over isotropic tensors. Could the authors provide more
intuitive explanations or mathematical nature of this theorem?

• The authors state that parameterizing all permutation-invariant polyno-
mial functions may be as challenging as solving the graph isomorphism
problem. Could the authors provide an estimate of the computational
complexity or approximate methods for tackling this problem? can we
push this into high-dimensional settings?

• While MLPs are popular in approximating the polynomial functions, is
there a risk that they might not fully capture the necessary polynomial
structures or equivariance properties?

• The learned SVH models perform better when stringent data assumptions
are not met. Could the authors elaborate on why their models are more
robust in these scenarios? Please provide valuable insights.

• The paper focuses on equivariance. Could you derive some examples for
other groups, such as unitary groups or affine transformations?

### Soundness
4

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a framework for constructing equivariant tensor functions to facilitate sparse vector recovery in distributions with specific symmetry properties, such as those invariant under orthogonal transformations. The key concepts introduced include the $ k(p)$-tensor space, which captures parity characteristics in tensor components, and the construction of equivariant polynomial functions that remain consistent under orthogonal group actions. The framework also incorporates tensor operations such as outer product and $ k $-contraction to enable flexible tensor combinations while preserving equivariance. Furthermore, the paper extends Haar averaging to non-compact groups, allowing the model to maintain equivariance in settings with broader symmetry requirements, like the indefinite orthogonal group.

### Strengths
- To the best of my knowledge, this paper introduces a new approach to equivariant tensor functions, expanding to cases with mixed symmetry properties through the $k(p)$-tensor space concept.

- The paper provides a well-grounded method with precise definitions, such as outer product and $k$-contraction, supported by theoretical proofs.

- Extending Haar averaging to non-compact groups (such as the indefinite orthogonal group $O(s, d-s)$ and symplectic group $Sp(d)$) broadens the versatility.

### Weaknesses
1. **Lack of Clear Theoretical Motivation and Practical Relevance**

   - **W1.1:** The paper focuses heavily on mathematical formulas and definitions but lacks intuitive explanations to clarify the need for equivariant tensor functions and their practical motivations. The introduction of the $k(p)$-tensor space and equivariant polynomial functions, while mathematically rigorous, is not connected to concrete problems where these concepts are essential. For instance, it's unclear why a standard tensor representation would be insufficient, and what specific advantages the proposed equivariant approach offers in terms of performance or interpretability.
   - **Suggestion**: Consider adding a high-level overview section that explains why equivariance is essential in certain applications and provides examples that demonstrate the demand for equivariant tensor functions in real-world scenarios.

   - **W1.2:** Key theoretical challenges and the novel aspects of the proposed method are not thoroughly discussed, leaving readers uncertain about the primary obstacles and contributions within the framework. The paper does not clearly articulate what limitations of existing methods are overcome by the proposed approach. It remains unclear what the main theoretical hurdles were in constructing these equivariant functions and why the specific choices made in the framework are crucial.
   - **Suggestion**: Consider adding a dedicated “Contributions” section that explicitly outlines how this method differs from existing approaches, helping readers understand the unique contributions of the framework.

   - **W1.3:** The paper does not clearly explain the necessity of "learning equivariant tensor functions," lacking specific application scenarios that showcase the unique benefits and suitability of these functions. It remains unclear why certain types of tensors in applications require equivariance. For example, in the context of sparse vector recovery, it is not clear why the recovery process needs to be equivariant under orthogonal transformations, and what would be the consequences of using a non-equivariant approach.
   - **Suggestion**: Include examples of practical applications where specific types of tensors need to be equivariant and clarify how these scenarios validate the advantages of using equivariant tensor functions.

2. **Limitations in Sparse Vector Recovery Application**

   - **W2.1:** The paper centers its applications on sparse vector recovery, a problem that is primarily theoretical and rooted in computer science, with limited overlap with current mainstream machine learning applications, such as computer vision or natural language processing. While sparse vector recovery is a well-studied problem, the paper does not sufficiently motivate its relevance to broader machine learning tasks. The connection between the theoretical problem and practical applications is not clearly established.
   - **Suggestion**: Discuss the potential connections between sparse vector recovery and mainstream machine learning applications, such as compressed sensing, feature selection, or dimensionality reduction in deep learning, to enhance the method’s appeal.

   - **W2.2:** The paper does not demonstrate if or how sparse vector recovery can extend to practical uses in deep learning or other prominent areas within machine learning, lacking case studies or examples of its effectiveness in real-world tasks. The paper lacks empirical evidence to support the practical utility of the proposed method. There is no demonstration of how the equivariant tensor functions can be used in a deep learning context or any other real-world application.
   - **Suggestion**: Consider adding relevant cases or discussions on how the method could be integrated into neural network architectures or applied to tasks such as network pruning, compression, or efficient inference, to illustrate its practicality.

   - **W2.3:** The real-world significance of the proposed method is unclear, potentially making it seem disconnected from practical contributions to machine learning, which could limit its appeal to a broader audience. The lack of concrete examples and applications makes it difficult to assess the practical impact of the proposed method. The paper does not provide a clear path for how the theoretical framework can be translated into practical tools for machine learning practitioners.
   - **Suggestion**: To increase its appeal, the authors could discuss the broader implications of their work, such as how advances in equivariant functions might contribute to more efficient or interpretable machine learning models over the long term.

3.  **Limited Relevance to Machine Learning**

   - **W3.1:** While the method shows mathematical novelty, its applications in machine learning are not well-established, which may restrict its potential readership. Machine learning researchers tend to focus on methods with clear, practical applicability and accessibility. The paper does not clearly demonstrate how the proposed method addresses a specific need in the machine learning community. The benefits of using equivariant tensor functions over existing methods in machine learning are not clearly articulated.
   - **Suggestion**: Strengthen the connection to machine learning demands by discussing how equivariant tensor functions could enhance model interpretability or efficiency, demonstrating its contributions to machine learning research.

   - **W3.2:** The paper extensively uses group theory terms and concepts, such as orthogonal groups and indefinite orthogonal groups, which may be unfamiliar and challenging for machine learning readers without a strong mathematics background. The paper assumes a level of mathematical sophistication that may not be common among machine learning researchers. The lack of intuitive explanations for these concepts may hinder the accessibility of the work.
   - **Suggestion**: Consider including a brief primer on the relevant group theory concepts or offering more intuitive explanations for these mathematical objects. Providing references to introductory resources may also help readers better understand these terms.


**Additional Suggestions:**

- **Add Visual Aids and Case Studies**: Introduce diagrams in appropriate sections to help readers visually understand the basic principles of the method, or add case studies to illustrate its practical applications. This could help engage a wider range of machine learning researchers.

### Questions
Please refer to each weakness and suggestion section to help improve the readability and applicability of the work.

### Soundness
3

### Presentation
1

### Contribution
2
