# Distribution-Specific Agnostic Conditional Classification With Halfspaces

- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 6, 6, 8, 5

## Abstract
We study "selective" or "conditional" classification problems under an agnostic setting. Classification tasks commonly focus on modeling the relationship between features and categories that captures the vast majority of data. In contrast to common machine learning frameworks, conditional classification intends to model such relationships only on a subset of the data defined by some selection rule. Most work on conditional classification either solves the problem in a realizable setting or does not guarantee the error is bounded compared to an optimal solution. In this work, we consider selective/conditional classification by sparse linear classifiers for subsets defined by halfspaces, and give both positive as well as negative results for Gaussian feature distributions. On the positive side, we present the first PAC-learning algorithm for homogeneous halfspace selectors with error guarantee $\tilde{O}(\sqrt{\mathrm{opt}})$, where $\mathrm{opt}$ is the smallest conditional classification error over the given class of classifiers and homogeneous halfspaces. On the negative side, we find that, under cryptographic assumptions, approximating the conditional classification loss within a small additive error is computationally hard even under Gaussian distribution. We prove that approximating conditional classification is at least as hard as approximating agnostic classification in both additive and multiplicative form.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies conditional classification with homogeneous halfspaces as selectors under the agnostic learning setting with Gaussian marginals. That is, given access to samples from underlying distribution $D$ with adversarial label noise, the algorithm aims to output a classifier-selector(halfspace) pair, such that the classifier makes low prediction error conditioned on the instances in the given halfspace. When there exists a pair $(c^*,v^*)$ that achieves $opt$ error rate, this paper proposes an algorithm that can output a pair $(c,w)$ that achieves error rate of $\tilde{O}(\sqrt{opt})$. The algorithm is based on Projected SGD for choosing the appropriate halfspace and then output the classifier-halfspace pair with minimal loss.

On the other hand, the paper shows that agnostic conditional learning with general halfspace selectors is computationally hard.

### Strengths
This paper studies an interesting problem, which considers agnostic classification under a conditional distribution. It models the conditional distribution using a homogeneous halfspace, and complement the result using a hardness example for non-homogeneous halfspace. The paper also links the problem to many other important problems in machine learning, including learning under the list-decodable setting, learning with abstention, etc. It will be interesting to investigate the deep connection between these problems.

The theoretical analysis is generally sound to me. The paper reads smoothly, with results well presented.

### Weaknesses
The paper claims that the classifiers are sparse, but it seems the aim is to limit the size of the classifier set. The paper has very limited discussion on this matter, which makes the claim of learning "sparse" classifiers a bit misleading. Specifically, the notion of sparsity isn't tied to the representation of individual classifiers but rather to the cardinality of the set of classifiers considered. This distinction is crucial, as true sparsity would imply a constraint on the number of non-zero parameters within each classifier, which is not what is being enforced here. The current framing could lead to confusion, as it suggests a different type of sparsity than is commonly understood in machine learning.

Although agnostic conditional learning with general halfspaces is computational hard, the current algorithm for homogeneous halfspace selector also depends on the size of the classifier set $\lvert\mathcal{C}\rvert$. The paper claims that $\lvert\mathcal{C}\rvert$ is small, I wonder how applicable the current algorithm is to the agnostic conditional learning problem for general class of binary classifiers. The dependence on the size of the classifier set, even if it's considered small, raises concerns about the scalability of the proposed algorithm. If the classifier set needs to be finely discretized to achieve good performance, this could lead to a significant increase in computational cost, especially when dealing with complex classification problems. The paper needs to provide more justification for the assumption that a small classifier set is sufficient for practical applications.

The algorithm relies strongly on the Gaussian marginals assumption, such that any halfspace has probability mass of $1/2$. Is there any way we can extend this assumption? Or, the whole analysis only works for Gaussians? The reliance on Gaussian marginals is a significant limitation, as real-world data often deviates from this assumption. The analysis hinges on the property that any homogeneous halfspace has a probability mass of 1/2 under a Gaussian distribution, which is not generally true for other distributions. This raises questions about the robustness of the algorithm and its applicability to more general data distributions. It is unclear how the theoretical guarantees would be affected if this assumption is violated.

### Questions
I didn't get the part of choosing ReLU function as the convex surrogate approximation of the conditional classification error? It seems $L_D(w)$ also blocks the information for one-sided class $y=1$. However, $g_w(x,y)$ seems to be one-sided.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies distribution-specific agnostic conditional classification for halfspaces. In particular, they consider sparse linear classifiers, subsets defined by halfspaces, and Gaussian feature distributions. Both positive and negative results are provided. On the positive side, they authors give the first polynomial time PAC learning algorithm when the selectors are homogenous half spaces with error guarantee $\tilde{O}(\sqrt{\epsilon})$. On the negative side, the authors show that under standard cryptographic assumptions and even under gaussian features, estimating the conditional classification error is computationally hard. This proof involved reducing approximating agnostic classification, which is known to be hard, to approximating conditional classification.

### Strengths
- The problem setting is interesting and well-motivated
- The proof techniques seem non-trivial and novel 
- Both the positive and negative results, in my opinion, and important contributions to this area.

### Weaknesses
I don't have any specific weakness in mind. That said, the paper does feel very dense and would benefit from more informal theorems/lemmas/propositions in the main text, and more details in the appendix.

- Theorem 1 states that Algorithm 1 outputs a good half space selector **for each** concept $c \in C$. But, don't you need to ouput a single selector that works well across all concepts in $C$? If I am not mistaken, I do not see a Theorem in the paper that quantifies the error of the selector output in Step 11 of Algorithm 1. 

- Based on Algorithm 1, it seems like the class of concepts needs to be finite? Is there anyway to relax this assumption and have the input $T, N$ depend on the VC dimension of $C$?

### Questions
- Theorem 1 states that Algorithm 1 outputs a good half space selector **for each** concept $c \in C$. But, don't you need to ouput a single selector that works well across all concepts in $C$? If I am not mistaken, I do not see a Theorem in the paper that quantifies the error of the selector output in Step 11 of Algorithm 1. 

- Based on Algorithm 1, it seems like the class of concepts needs to be finite? Is there anyway to relax this assumption and have the input $T, N$ depend on the VC dimension of $C$?

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
This work studies the problem of conditional classification. The problem of conditional classification is the following: Given a finite classifiers of class $\mathcal{C}$ and a set of concepts $\mathcal{H}$ that have non-trivial probability over the marginal, the task is to find a pair $(c,h)$ for $c\in \mathcal{C}$ and $h\in \mathcal{H}$ such that $\Pr[y\neq c(x)\mid x\in h]$ is small. They consider $\mathcal{H}$ to be the class of homogeneous halfspaces. They prove that there exists a polynomial time algorithm for the above task that achieves error $\tilde{O}(\sqrt{opt})$ where $opt$ is the minimum error possible. They also prove a lower bound that says conditional classification is hard for general halfspaces.

### Strengths
1) The reduction from conditional classification to one sided agnostic classification seems novel. Although the reduction is not complicated, it is neat.
2) The proofs seem correct and intuitive. 
3) I believe that this work makes important progress in the study of conditional classification. 
4) Their algorithm runs in polynomial time (although they obtain a multiplicative approximation).

### Weaknesses
1) The lower bound for general halfspaces is for the objective $opt+\epsilon$. However, the upper bound only achieves $\sqrt{opt}$ for homogenous halfspaces. Is it the case that $\sqrt{opt}$ is not possible for general halfspaces efficiently? Their lower bound does not seem to exactly complement their upper bound. Specifically, the lower bound's additive $\epsilon$ term doesn't directly address the $\sqrt{opt}$ upper bound, leaving a gap in understanding the fundamental limits of conditional classification with general halfspaces. It would be more compelling if the lower bound could demonstrate a similar $\sqrt{opt}$ hardness, or if the authors could provide a more detailed explanation for why such a bound might be unattainable. 
2) The statements of the theorems have grammatical errors. For instant, in proposition 3.2, the last line says if {property A}, there is {property B}. "There is" should be replaced by "it holds that" or "we have".
3) The presentation is a bit unclear in some places. Further expanded in Questions.

### Questions
1) In section 1.3, it would be helpful to state both theorems corresponding to the contributions within this section or provide a link to their statements for easy reference.
2) The connection to list learning is unclear. In particular, why is Theorem 2.1 stated in the preliminaries? Where is it used in your proof?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper considers agnostic conditional classification when the underlying marginal distribution is Gaussian and the selector is a half-space. First, the authors prove a polynomial time algorithm that returns a classifier-selector pair such that the associated risk is at most the square root of optimal risk. Given this, a natural question is whether one can achieve an error that is at most $\varepsilon$ away (additively) from the optimal risk. Unfortunately, the authors prove a hardness result showing that no polynomial algorithm can achieve this.

### Strengths
1. The paper is well-written and is easy to follow. I particularly like Section 3.2 where the paper guides us through the proof sketch, while including propositions, and lemmas required for the proof. 

2. The algorithm appears both natural and intuitive. While not strictly necessary, it would be helpful if the authors could provide additional context around two aspects of the proposed algorithm. First, what is the intuition behind initializing PSGD for both $ w^{(0)} $ and $-w^{(0)} $? Second, what motivates the choice of ReLU as the convex surrogate? Although the paper includes some description, it is unclear whether ReLU's usefulness here is due to the separators being halfspaces, or if the goal is more related to obtaining gradients of a specific form by using tools from Diakonikolas et al. (2020b).

### Weaknesses
The authors list a few limitations of the work in the final section of the paper. Another major weakness of the paper is the fact that Theorem 3.1 only holds for a finite class of classifiers $\mathcal{C}$. Typically, finite hypothesis class $\mathcal{C}$ is justified because some form of discretization-based arguments generalize the result to infinite class as well. For example, usually, proving risk bounds for half-spaces can be reduced to proving risk bounds for finite discretization of half-spaces. However, Theorem 3.1 cannot even handle the discretization of half-spaces because the size of $\varepsilon$ discretization of half-spaces on $d$ dimension is roughly $\varepsilon^{-d}$.  Given that the runtime of Algorithm 1 is $O(d\,  |\mathcal{C}|/\varepsilon^6)$, taking $|\mathcal{C}| \approx \varepsilon^{-d}$ makes the runtime exponential in $d$.

### Questions
1. How essential is the choice of the Gaussian distribution for this analysis? I skimmed the proofs in the supplementary materials, and it appears that the arguments primarily rely on the symmetry and tail probability bounds of the Gaussian. Do you think the same results could be extended to symmetric sub-Gaussian (or, ideally, just sub-Gaussian) random variables?

2. Is anything known about lower bounds on the risk of polynomial algorithms in this setting? In their discussion, the authors mention that the $O(\sqrt{\varepsilon}) $ rate appears suboptimal. I was wondering if the authors have any reasons to support this belief.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the agnostic conditional classification problem for a finite class of hypotheses $\mathcal{C}$. In the classic agnostic learning setting, a learner is asked to output a hypothesis $c \in \mathcal{C}$ that achieves a small error over the whole domain of examples. In the conditional classification setting, a learner is instead asked to output a subset $S$ of the domain and a hypothesis $c$ such that the conditional error over $S$ is small. The motivation is that over some subset of the domain, the error rate of a hypothesis could be much lower than the error rate over the whole domain. This paper focuses on a special case of the conditional classification problem, where the marginal distribution is a standard Gaussian and the subset output by the learner is the positive region of some homogeneous halfspace. The paper gives an algorithm that runs in time $poly(|\mathcal{C}|,1/\epsilon,d)$ and outputs a hypothesis $c \in \mathcal{C}$ and a homogeneous halfspace $h$ such that the conditional error of $c$ over $h$ is at most $\tilde{O}(\sqrt{opt}+\epsilon)$, where $opt$ is the smallest conditional error of some $c$ over all possible homogeneous halfspaces. Technically, the algorithm can be seen as an application of agnostic learning homogeneous halfspaces under Gaussian with respect to conditional error (examples in the halfspaces are labeled by 0, noisy examples have artificial labels 1). Given such a halfspace learning algorithm, the learner can brute force and compute an approximate best halfspace for each hypothesis in the class. On the other hand, the paper reduces the problem of agnostic learning Gaussian halfspaces to the conditional classification problem and uses the known cryptographic hardness result to show that it is impossible to approximate the optimal conditional classification error within an additive error in polynomial time.

### Strengths
1. The presentation of the paper is clear. The main body of the paper gives a clear technical review of the algorithms and the proof of the hardness result.
2. Technically, this paper gives a novel algorithm for agnostic learning homogeneous Gaussian with conditional error. Previously known algorithms for agnostic learning halfspaces all concern the error over the whole domain. It is not clear whether we can apply these algorithms directly to get a good hypothesis with a small conditional error. So, the new algorithm might be of interest to the community

### Weaknesses
1. From my point of view, the main weakness of this paper is the motivation of using homogeneous halfspaces as a selector under Gaussian distribution. I am not sure whether the conditional error itself alone is a meaningful metric, because, in selective classification, one should also consider the coverage of the output selector (accept rate of the selector). For example, one may output two selectors with different accept rates but the same conditional error. In this case, it makes no sense to use the one with a lower accept rate. However, such an important characterization is not considered by the paper. Under Gaussian distribution, all homogeneous halfspace selectors have a reject rate of 1/2, which is fairly high. It does not make sense to use a selector that has to throw away half of the examples. More importantly, this equal reject rate makes the risk-coverage tradeoff curve disappear in the setting studied by this paper. These two limitations of using a halfspace selector under Gaussian make the result a little bit strange from the perspective of selective classification and look more like an application of halfspace learning.

2. The main algorithm can only deal with a class of finite concepts. In fact, finiteness is very crucial in the paper as the main algorithm in the paper computes a good selector for every single concept in the class and does not make use of any structure of the concept classes. Though, at the end of Section 1.1, the authors mention that one can deal with larger classes via robust list learning, the paper does not give a very clear explanation of how to use robust list learning to selectively learn a general class.  For example, to selectively learn a VC class $H$, it is not clear how to set up the parameters in the corresponding robust list learning. The authors also mentioned an efficient list-learning algorithm for sparse linear separators but did not explicitly connect this example with selective learning. I believe more explanations are needed in the future version of the paper.

3. As mentioned by the authors, the error guarantee $\tilde{O}(\sqrt{opt})+\epsilon$ is not optimal, and thus the hardness result in the paper does not rule out the possibility of having an algorithm with much better error guarantee. 

4. The abstract in the OpenReview states the algorithm can learn a selector up to error $O(opt)$, which is different from the results obtained by the paper.

### Questions
1. Can you help formally explain how to use robust list learning to deal with larger hypothesis classes? Why learning $O(1)$-sparse linear separators is used as an example here? Is it because the length of the list can be controlled? What if we consider other simple hypothesis classes such as high-dimensional boxes or dense linear separators?

2. Previous agnostic halfspace learning papers such as [DKTZ22] show that under Gaussian as long as the angle between the current hypothesis and the target is small, one can achieve error $O(opt+\epsilon)$ and thus those algorithms all converge in the last iterate. Can you provide any intuition of why similar arguments cannot be used here and why the algorithm can only converge in average and achieve $\sqrt{opt}+\epsilon$?

3. Please make comments on the weakness that I pointed out above. I would raise my score based on the response.


[DKTZ22]Diakonikolas I, Kontonis V, Tzamos C, Zarifis N. Learning general halfspaces with adversarial label noise via online gradient descent. International Conference on Machine Learning 2022 Jun 28 (pp. 5118-5141). PMLR.

### Soundness
3

### Presentation
3

### Contribution
2
