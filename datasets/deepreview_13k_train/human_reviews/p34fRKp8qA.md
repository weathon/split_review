# Lie Group Decompositions for Equivariant Neural Networks

- Decision: Accept
- Scores: 8, 8, 6, 6, 5, 8

## Abstract
Invariance and equivariance to geometrical transformations have proven to be very useful inductive biases when training (convolutional) neural network models, especially in the low-data regime.
Much work has focused on the case where the symmetry group employed is compact or abelian, or both.
Recent work has explored enlarging the class of transformations used to the case of Lie groups, principally through the use of 
their Lie algebra, as well as the group exponential and logarithm maps.
The applicability of such methods is limited by the fact that depending on the group of interest $G$, the exponential map may not be surjective.
Further limitations are encountered when $G$ is neither compact nor abelian.
Using the structure and geometry of Lie groups and their homogeneous spaces, we present a framework by which it is possible to work with such groups primarily focusing on the groups $G = \text{GL}^{+}(n, \mathbb{R})$ and $G = \text{SL}(n, \mathbb{R})$, as well as their representation as affine transformations $\mathbb{R}^{n} \rtimes G$.
Invariant integration as well as a global parametrization is realized by a decomposition into subgroups and submanifolds which can be handled individually.
}.
We evaluate the robustness and out-of-distribution generalisation capability of our model on the benchmark affine-invariant classification task, outperforming previous proposals.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new approach to efficiently generalize group equivariant convolutions for the  $\text{GL}^{+}(n, \mathbb{R})$ and $\text{SL}(n, \mathbb{R})$ groups. While the Haar measure for such non-compact groups is ill-defined, the approach proposes to work with the decomposition of these groups into factors that have well-behaved Haar measures. Factorizing the convolution integral enables the computation of group equivariant convolutions on these groups. By using results from random matrix theory to efficiently sample elements of these groups, the authors propose an efficient way to compute these integrals via Monte Carlo (MC) integration. This results in an order of magnitude improvement in the number of samples needed for a converged integral. The method is tested on two image classification tasks under affine and homographic transformations. In both benchmarks, the method is shown to outperform previous approaches.

### Strengths
- The paper is clearly written, and the contributions are made clear.
- The mathematical concepts are well-introduced, precise, and effectively utilized.
- The approach is novel and original, making elegant use of existing results in classical group theory and random matrix theory within the context of geometric deep learning.
- The two groups covered in the paper ($\text{GL}^{+}(n, \mathbb{R})$, $\text{SL}(n, \mathbb{R})$), are two important groups for image-related tasks.
- The sample efficiency gains might prove to be a key element for the future adoption of group equivariant convolutions in image-related tasks.
- The benchmark results are convincing, comparing favorably to strong baselines in the field.

### Weaknesses
 - The analysis of the numerical stability of the method is largely missing. In particular, methods that rely on approximating integrals over groups will always be approximately equivariant. While increasing the number of samples could reduce this error below floating-point precision, such an analysis is not present in the paper. A curve illustrating the equivariance error as a function of the number of Monte Carlo samples would be pertinent in this context. Although sizeable equivariance errors might be manageable in the context of image classification tasks, this is not the case for all types of application tasks where group convolutions are relevant. Specifically, in physics simulations, equivariance errors are related to the non-conservation of physical quantities. The proposed approach should be contrasted with approaches that use linear operators to evaluate the group integral, such as [1] and [2], which are exactly equivariant (even for non-compact groups) but require large tensorial operations (for [1]) or ad hoc representation theory for each group (for [2]). I encourage the authors to briefly discuss these points in the text and add an analysis of numerical stability in the form of a plot to the appendix.

- In the paper, only the symmetrization to the canonical group action is explicitly mentioned. Extending the matrix elements to other finite-dimensional group representations should be straightforward, provided that the correct basis is determined. I am curious why this was not presented in full generality.

### Questions
- See my point regarding numerical stability.

- This might be a standard result already, but I would like to have a formal view of the convergence of your approach. Do you think it would be possible to obtain an explicit bound on the equivariance error as a function of the number of Monte Carlo samples, the sizes of the factors in the group decomposition, and the size of the representation? To be more precise, I am looking for something akin to this bound: $|| \int_{H} \int_{K} f(\rho(h) \rho(k) \cdot x) d\mu_{H}(\rho(h)) d\mu_{K}(\rho(k)) - \frac{V}{N} \sum_{i} f(\rho(h_{i}) \rho(k_{i}) \cdot x), \rho(h_{i}) \sim \mu_{H}, \rho(k_{i}) \sim \mu_{K}|| \leq f(N, dim(\rho), dim(H), dim(K) )$
Using that, one could ask what kind of factorization gives the best bound.

### Soundness
4 excellent

### Presentation
2 fair

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
The paper considers the problem of designing equivariant neural networks when the group may not be compact or abelian, and when the exponential map for the Lie group may not be surjective. In an earlier work which makes use of the Lie algebra to construct the kernels, when the exponential map is not surjective, the log map is only applicable around the identity in the lie algebra, and is thus restrictive. Furthermore, this method has exponential memory complexity in the group dimension. The focus of the paper is two such groups: $GL^+(n,\mathbb{R})$ and $SL(n,\mathbb{R})$. The key idea is to decompose these groups into subgroups and submanifolds where sampling the group elements is easier and well defined. Experiments on small standard datasets shows improvements over earlier methods.

### Strengths
1. The paper is mathematically well-grounded. 

2. The contributions in the paper clearly improve on existing works in more than one way: applicable to groups like $GL^+(n,\mathbb{R})$ and $SL(n,\mathbb{R})$

3. The ideas of group decomposition as a way to build equivariance to such groups is an interesting and general idea, and will hopefully be useful in other cases. 

4. Experimental results show improvements over state-of-the-art methods.

### Weaknesses
1. The number of samples for Monte Carlo integration is not clear to me. When the authors say 10 samples are used for the affine group, do they mean 10 samples for both rotations and scales combined? How many rotations and scales? It is unclear if the 10 samples are drawn from the full group or if they are 10 samples from each subgroup in the decomposition, and how these samples are combined to form a group element. This ambiguity makes it difficult to assess the efficiency of the Monte Carlo integration.

2. Although clear theoretically, experiments don't seem to have tested the settings that were setting this apart from the others, particularly, by MacDonald et al. 2022. Perhaps at least one experiment with n=3 with larger scale changes as part of the test set could be interesting. Even a different version of affNIST with larger scale changes could be interesting. The experiments should include a more thorough exploration of the parameter space, particularly with respect to the scale changes, to demonstrate the method's robustness in the regimes where it is expected to excel compared to existing methods.

3. Having numerical values of equivariance/invariance error, and as a function of the number of Monte Carlo samples should also be useful here. Without these values, it is difficult to assess the practical convergence of the method and compare it to other approaches. The lack of this analysis makes it difficult to understand the trade-off between computational cost and accuracy.

4. I don't fully understand why the proposed group decomposition technique is able to estimate the correlation integral well with only 10 samples while the work by MacDonald et al. need 100. The paper does not provide a clear explanation of the underlying mechanism that allows for this improved sample efficiency. It is unclear if this is due to a more efficient sampling strategy, a different approximation of the integral, or other factors.

### Questions
No additional questions.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a way to build group convolutional (Gconv) layers for groups in which the exponential map from the Lie algebra to the group is not surjective (e.g. $GL(n,mathbb{R})$). The problem is that Gconv is an integral over the group, which is often approximated by discrete sampling done using the exp map. When the exp map is not surjective, we can't rely on it to get good coverage in the sampling.
To mitigate this, this paper suggests to find a decomposition of the group in the form $G=PK$ such that the integration (Haar) measure over the group also factorizes $d\mu_G = d\mu_P d\mu_K \delta(\cdot)$. In certain cases, such as the Affine group, this decomposition can yield familiar subgroups for which we have either a surjective exp (e.g. $SO(n)$) or efficient sampling strategies (e.g. diffeomorphic to $\mathbb{R}^k$). 
After deriving the theory behind such decomposition, they introduce a Monte Carlo sampling scheme for it. Then they conduct a couple of toy experiments to show potential benefit of their design.

### Strengths
1. Mathematical rigor: goes through the details of the structure of Gconv to pinpoint the issue arising from non-surjective expm. 
2. Has extensive derivations, appendices and concrete calculations of the integration measures, rarely stated in other works. 
3. The Monte Carlo sampling scheme seems to work well with few samples and may alleviate memory issues of others. 
4. The experiments, though limited, are useful.

### Weaknesses
1. Mathematical rigor: very dense, difficult to read, too much re-derivation of previous results. A good part of sec. 3, Background, in __continuous group equivariance__ and some of __Lie algebra parametrization__ can be cut and moved to the appendix. Sec. 4 can also be shortened, like derivations in __layer definition__ in 4.2. The density of the math makes the paper hard to read. Specifically, the re-derivations of standard results in Lie theory, while perhaps intended for completeness, significantly impede the flow and readability. For instance, the detailed exposition on Haar measures and their properties, while important, could be presented more concisely, assuming a certain level of background knowledge from the target audience. The derivations in section 4.2, particularly those related to the layer definition, could also benefit from a more streamlined approach, focusing on the novel aspects of the proposed method rather than re-hashing known mathematical machinery.
2. The paper calls $SO(n)$ abelian, which is incorrect for $n>2$ (page 4, sec 4).
3. Other literature: Many Gconv approaches do not sample the group this way (ses question): Clebsch-Gordon Nets (Kondor et al NeurIPS 2018), Lorentz group (Bogatskiy, ICML 2020), EMLP (Finzi 2021) or Lie algebra conv (Dehmamy, NeurIPS 2021). The paper fails to adequately contextualize its approach within the broader landscape of group convolutional methods. Specifically, it does not sufficiently address why alternative sampling strategies, such as those employed in Clebsch-Gordon Networks or methods for the Lorentz group, are not suitable for the problem at hand. A more thorough discussion of the limitations of existing methods, and a clearer articulation of the specific scenarios where the proposed decomposition is advantageous, would significantly strengthen the paper's contribution.

### Questions
1. How are methods relying on irreps affected by the expm not being surjective? Does it matter in those cases? 
2. For the Haar measures to factorize to $\mu_K \otimes \mu_P$, do we need $G=PK$ or semidirect or direct product? A number of different decompositions are used in 4.1 and 4.2 and the requirements are not fully clear. 
3. I see that $G=PK$ can be done when $P$ or $K$ is a normal subgroup. In the $SL(n)$ to $\mathrm{SPos} \times SO(n)$, is $SO(n)$, is one of the factors also a normal subgroup? 
4. Even when expm is not surjective, the product of multiple $g_i = \mathrm{expm}(X_i)$ can produce any arbitrary group element, as I understand it. Doesn't this mean that multi-layer Gconv using expm should in principle be sufficient to get good sample coverage on the group? In other words, is your decomposition really necessary?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a method for constructing approximately Lie group equivariant neural nets. Like previous work, their method relies on Monte Carlo approximation of infinite integrals; however, they extend this methodology to Lie groups without surjective exponential maps. Their critical insight is to decompose certain Lie groups of practical interest into semidirect products, which simplifies the form of the Haar measure. They evaluate their method in modifications of MNIST and outperform baselines.

### Strengths
The framework is quite general, in that it applies to Lie groups with non-surjective exponential maps. The experimental performance is strong relative to baselines, including other work that handles groups with non-surjective exponential maps. The presentation of the underlying math is quite detailed, and is a good resource on its own (especially the appendix). The decomposition of a Lie group into groups via the semidirect product is novel in a machine learning context, as far as I know.

### Weaknesses
1. From what I can tell, the input and output spaces/representations are restricted to either the group itself under the regular or trivial representation, or a homogeneous space of the group. This does not seem as general as e.g. the two papers I mention in point (3), which can work with any finite-dimensional representation.

2. The advantage of this approach over MacDonald et al 2022 is not made sufficiently clear, since both approaches can also handle Lie groups with non-surjective exponential maps.

3. The related work is missing at least two important papers on Lie group equivariance: “A Practical Method for Constructing Equivariant Multilayer Perceptrons for Arbitrary Matrix Groups” by Finzi et al 2021, and “Lorentz Group Equivariant Neural Network for Particle Physics” by Bogatskiy et al 2020. It would be important to compare to these papers (both in theory, in terms of the Lie groups and input/output representations to which they apply, and in the experiments), since they are exactly equivariant.

4. To a similar point, this method is only approximately equivariant (due to the sampling in the integral computation), rather than exactly equivariant. This could be expressed more clearly in the introduction of the paper. It would also be helpful to have computational tests of equivariance, which assess to what degree the learned network is actually equivariant after integration error.

5. The paper’s presentation could be significantly improved. In addition to typos, some of which are noted below, the writing leaves something to be desired overall. For example, the main body of the paper is very dense in mathematical background and details. It would be helpful to clearly and concisely express the main ideas of the paper earlier on and to give only the important intuitions, and to defer many such details to later in the paper or the appendix.

6. Enforcing equivariance to Lie groups with non-surjective exponential maps could be much better motivated — applications are not discussed very often, and the datasets used are synthetic (e.g. affine transformations of MNIST). When does such equivariance arise in practice?

Here are several typos I encountered while reading:
* Page 1, abstract: backwards quotation mark on the word larger
* Page 2, fourth line: backwards quotation mark on the word larger
* Page 2, related work: “Recent proposal” —> “Recent proposals”
* Page 2, bottom line: “maps can be defined AS k-channel”
* Page 3, between equations 5 and 6: “ecompasses”
* Page 4, in Lie algebra parametrization: “approxiamtion” and “encompasses recent proposalS”
* Page 7 before Theorem 4.4: “to obtain GL(n,R)-sampleS”

### Questions
1. My understanding was that non-compact groups do not have finite Haar measures (i.e. the measure of the entire group is infinite). I am therefore confused how e.g. equation 13, and really all the integrals, are well-defined without additional assumptions on the bounds of integration or the decay of the function being integrated.
2. Could the authors elaborate on the primary advantages of this integration method over that of MacDonald et al 2022, which also handles the case of Lie groups with non-surjective exponential maps? The related work mentions memory requirements, but it is not clear to me how this method circumvents these issues (or what the precise issues are).
3. Assuming the main advantage over MacDonald et al 2022 is in memory requirements, why then do the authors think that MacDonald et al had slightly worse performance in the experiments? 
4. The papers by Finzi et al and Bogatskiy et al, noted under “weaknesses” above, are not integration methods. Are they suited for the input and output representations that this task considers? If so, can the authors compare to these methods as well?
5. At the top of page 8, the authors note that they sample the translation factor from $[-1,1]^n \subset \mathbb{R}^n$. How is this justified, when the integral is defined over all of $\mathbb{R}^n$? Doesn’t this induce some error, which is compounded in subsequent layers?
Is this construction universal? I.e. ignoring the Monte Carlo integral approximation error, can any continuous equivariant function be represented?

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a framework for the development of equivariant (regular) neural networks, specifically tailored to matrix Lie groups that may not be compact or abelian. The authors explain a strategy for the development of equivariant layers by subdividing larger groups into smaller subgroups or subspaces. This partitioning facilitates efficient sampling of group elements, conducted in accordance with the Haar measure, by allowing independent sampling from these defined subsets. Grounded in the theory of Lie group structure and the geometry of their homogeneous spaces, the paper focuses its analytical scope primarily on the groups $G = GL^+(n, R)$ or $G = SL(n, R)$.

### Strengths
1. While (regular) group convolution for non-abelian and non-compact groups have been proposed using basis functions on the Lie algebra. The exponential map, however, is only diffeomorphic locally around 0. In addition, the paper also aims the address the issue of efficient sampling of group elements according to the Haar measure for regular group convolutions. In this aspect, the paper is novel.
2. Preliminary experiments are conducted to verify the potential of the framework.

### Weaknesses
1. My main concern of the paper is its mathematical denseness. I would recommend the authors to focus on the main message, and defer unimportant details to the appendix. For example, the condition of part (2) of Theorem 4.1 is probably to general, and it is not helpful for understanding the paper.
2. The notation of the paper is also sometimes confusing. The (larger) group $G$ is sometimes refer to the affine group $G = R^d\rtimes H$ (mostly in Section 4). However, $G$ in Section 4 is mostly refer to the subgroup $H = GL^+(n, d)$.
3. One of the issue the paper aims to address is the global non-surjectiveness of the exponential map. However, since most (group) convolutional filters are only defined locally (on a neighborhood of the identity), does the existence of local diffeomorphism already suffice?
4. Page 5, line 4 after "Factorizing the Haar measure", for general subsets $P\subset G$ and $K\subset G$, what does it mean to have "G-invariant" Radom measure. Although the authors later say that $P$ will always be a $G$-homogeneous space (so the $G$-action on $P$ is essential an action on the quotient space), it would be much better to state this assumption in the beginning.
5. On page 4, the authors say $H = SO(n)$ is abelian. Is this the case for $n\ge 3$?
6. The theory seems to apply only to $H = GL^+(n, R)$ or $H = SL(n, R)$. Does it apply to a general $H\subset GL(n, R)$?
7. Is the Lie bracket of the Lie algebra used anywhere for the construction?
8. Can this construction be extended to representations beyond regular representations of $G$? For high-dimensional $G$, such as $E(n)$ with large $n$, sampling from $G$ will suffer from COD.

### Questions
See the previous section

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose to use Lie groups and Lie algebra to develop networks that can be equivariant with respect to affine transformations. They provide the theoretical framework to work with Lie groups that surpasses some of the issues encountered due to their surjective nature. \
The way they managed to enable invariant integration was achieved by decomposing the larger groups into subgroups and manifolds that can be treated individually. \

Main contributions are two-fold: \
a) they managed to develop a non-surjective method of the exponential map \
b) they achieved invariant integration with respect to the Haar measure in a principled manner\
----
Many thanks for you response

### Strengths
This is a robust and well-written paper that is mathematically sound (as far as I can tell given it is almost impossible to check everything in the absence of source code). The ablations studies are good, but am not sure whether the experiments on affnist are enough. Nevertheless affnist remains the gold standard - more or less - for evaluating such properties.

### Weaknesses
-- It does not matter too much to be frank, as SOTA is not everything, but please have a look at this paper which to my knowledge remains the SOTA on Affnist (figure 5 for instance)
https://aaai.org/ojs/index.php/AAAI/article/download/5785/5641 

With 174K parameters (64,16,16,16,10) they have achieved 98.1% accuracy on Affnist when trained at 99.7% of MNIST accuracy.
So you might want to update that, considering the number of parameters entailed too. 

-- I do not think the paper needs to be that heavy in maths - too many derivations that could have given space to further experiments and ablations. 
-- I would expand the related work, and flesh out the contributions in the introduction.

### Questions
1) To what extent have you based the novelty of your paper on achieving SOTA performance on Affnist? \
2) Is there a scope that your method can be used in tandem with CapsNets?\
3) Would a dataset such as SmallNorb be relevant in this context?\

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
