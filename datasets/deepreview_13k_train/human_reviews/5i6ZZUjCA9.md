# Affine Steerable Equivariant Layer for Canonicalization of Neural Networks

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
In the field of equivariant networks, achieving affine equivariance, particularly for general group representations, has long been a challenge.
In this paper, we propose the steerable EquivarLayer, a generalization of InvarLayer (Li et al., 2024), by building on the concept of equivariants beyond invariants.
The steerable EquivarLayer supports affine equivariance with arbitrary input and output representations, marking the first model to incorporate steerability into networks for the affine group.
To integrate it with canonicalization, a promising approach for making pre-trained models equivariant, we introduce a novel Det-Pooling module, expanding the applicability of EquivarLayer and the range of groups suitable for canonicalization.
We conduct experiments on image classification tasks involving group transformations to validate the steerable EquivarLayer in the role of a canonicalization function, demonstrating its effectiveness over data augmentation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this work, the authors propose a steerable and affine group equivariant layer, EquivarLayer. They introduce a novel pooling technique that can facilitate canonicalization. The empirical experiments presented were conducted on MNIST and MNIST scale datasets.

### Strengths
1. This paper presents a novel pooling layer that keeps equivariance to affine groups intact.

### Weaknesses
I will categorize the issues I find with the paper into three categories: (1) Claimed novelty; (2) Lack of presentation of concrete examples given the level of generality claimed and (3) experimental validation.
I want to note from the onset that I am open to raising my score, and the degree to which I am penalizing (lack of) novelty here is very much based on what the authors themselves claim.

- (1) The paper uses language that supports the notion where a lot of the concepts are novel (in the sense of new mathematical objects) rather than, their application in this form in the context of machine learning being novel. 
- Considering the framework presented up to section 2.3, I would like to highlight obviously the work of Olver himself in [4] where the same framework of constructing equivariant maps using moving frames based on his previous work is summarized (ending up with the abstract operator of eq. (13)). Directly related is the work of Sangalli et. al which also uses the prolongation of the group action on the jet space for invariantization (based on Olver's work) in the context of image and volumetric data [1-3]. From [1] appendix B, the general framework is directly applicable taking X = $\mathbb{R}^2$, $Y = \mathbb{R}^{c}$, $Z = \mathbb{R}^{c^{'}}$ , we arrive at the same principle where an equivariant operator $\mathcal{F} \to \mathcal{F}^{'}$ on the function spaces is defined implicitly once a G-invariant operator on the product space $X \times Y$ is available ($g \cdot (x, u) = (gx, \rho(g)u) = (gx, u)$ ($\rho = \rho_0$), corresponding to $g \cdot f(x) = f(g^{-1}x)$). In this work the notation is less clear and it appears that $Y = \mathcal{F}$ indicating a higher order operator, however the differential invariants are always (correctly) constructed with the same $x \in X$ argument i.e. $\hat{\mathcal{I}}(f)(x) = I(x, f(x))$ (we make use of differential invariants dependent on $x$). It should be highlighted then that the 'equivariant' $\mathcal{E}: X \times Y \to Z$ presented here is a $G$-equivariant map on the product space respecting $\mathcal{E} \circ \rho(g) = \rho^{'}(g) \circ \mathcal{E}$ , and would correspond to the case where $\rho \neq \rho_0$ ((16) in [1]). This is indeed a different group action and the authors seek to effectively work with induced representations which also acts on the codomain $L_{\rho}(g)(f)(x) = \rho(g)f(g^{-1}x)$, however it should not be presented as a departure from this framework if one is simply changing the representation used.
- The authors should also try and clarify further how their framework differs from [6] in its usage of the sup-normalized differential invariants. Are the polynomial relative invariants of [6] and the relative invariants here the same? I would also highlight [5] and [7] which also deal with differential invariants of the affine group of the plane, where the zero division errors are treated with a different formulation (see [5] (34) and (35)).
- Regarding (2), I would have liked to see more concrete examples of the framework being employed in the context where the additional flexibility in terms of input/output representations is valuable e.g. beyond image data, see for example [9]. I am not concerned with SOTA results, simply a validation that the increased generality allows the use of the differential invariants for a larger set of applications and modalities. It would also be useful for practitioners if more concrete examples of the realized (beyond theoretical) operators is presented.
- Regarding (3), it would be useful to quantify more clearly the relationship between the amount of data augmentation used and the size of the dataset for each experiment. More importantly, what would be very useful here is to have a thorough presentation of the time/space complexity of each layer employing this framework, see e.g. [1] appendix D or [6], with the inclusion of standard (3-channel) image data.

### Questions
1. Could you present results with additional datasets along with a comparison with existing methods? For example, above mentioned Steerable CNNs as well as ablation with image datasets like CIFAR10/CIFAR100?


2. The addition of simple canonization as presented in Kaba et al compared to the proposed method would be helpful. 


3. How does the proposed method perform to roto-translation and scale? 


4. How does this method scale with data, dimensions of invariants as well as group size?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a framework for constructing equivariant layers based on the method of moving frames; under this framework it is shown how the class of input/output group representations that can be employed is larger than previously shown. The authors adapt the jet-space based construction to the case where we are working with an induced representation also acting on the codomain of the signals. The framework is then employed in the context of a canonicalization framework, where the proposed equivariant layer with respect to the affine group is used for the canonicalization function. A primary focus of this work is the affine group, more specifically the affine group of the plane and its subgroups that go beyond euclidean transformations (rotation-scale, $\textnormal{GL}(2, \mathbb{R})$). The methodology is evaluated on a set of image classification tasks employing transformed MNIST datasets, where it is contrasted with a standard data augmentation approach. The experimental validation focuses on the delta in performance on transformed/non-transformed test sets.

### Strengths
- The paper is generally clear in its presentation, with each mathematical object being well-introduced and described. The authors present a framework which indeed treats a larger class of group representations than seen for this framework.
- While there has been some recent work in this area, the problem of constructing equivariant/invariant layers with respect to larger transformation groups is generally under-explored and potentially useful. In this sense, I am also happy to see work employing the method of moving frames and the use of differential invariants, which may yield different complexity constraints and/or scaling behaviour on the spectrum of methods imposing inductive biases. 
- Intertwining canonicalization and traditional methods for constructing equivariant layers seems like a useful avenue to explore.

### Weaknesses
 - W1. A proper comparison against fully equivariant networks for classification (e.g., InvarPDEs-Net and InvarLayer from [1]) is not included in the experiments. Including these baselines would strengthen the paper, especially since canonicalization may benefit from pre-training in non-invariant domains (e.g., ImageNet-1k in this paper) unlike fully equivariant networks. Furthermore, the comparison should not only focus on accuracy, but also on the number of parameters and computational cost, as canonicalization approaches may introduce additional overhead compared to fully equivariant networks.
- W2. It seems possible to use the moving frame in Definition 8 (or the equivariant matrix in Theorem 10) directly for canonicalization without multiplication by type-0 features (Eq. (10)), as this coincides with the definition of equivariant frames in frame averaging [8]. Adding this as a baseline would strengthen the results, as it can be understood as ablating trainability from canonicalization. Specifically, the moving frame itself, which is a function of the input, could be used to directly transform the input features to a canonical frame, and the performance of this approach should be compared with the proposed method.
- W3. It was unclear to me how the definition and property of moving frames given in Definition 8 and Theorem 9 logically leads to the construction of equivariants using relative equivariants given in Section 2.3. The connection between the theoretical framework and the practical implementation of the equivariant layer is not clearly explained. Specifically, the paper should clarify how the moving frame, which is a function of the input, is used to construct the equivariant features, and how this construction ensures the desired equivariance property.
- W4. The paper demonstrates a single application of the proposed layer as the last layer of a canonicalization network, which extracts 2-channel type-1 features from type-0 features, while all other layers of the network map between type-0 features [1]. This misses (1) feature maps of type >1, (2) layers taking non-scalar features as input, and (3) layers mapping between non-scalar features, all of which are possible within the proposed framework. Testing (a subset) of these would strengthen the paper. A straightforward way is to modify InvarPDEs-Net and InvarLayer from [1] to have non-scalar hidden features, analogous to steerable networks in [2]. It is also unclear how the proposed layer would perform in a deeper network with multiple layers of non-scalar features.

Minor typo
- Line 13: InvarLayer -> InvarLayer (Li et al. 2024)

### Questions
Beyond the issues highlighted before:
- In the case where the output representation acting on the codomain is not operating on scalar fields, do we have any restrictions with respect to the class of activation functions that can be used as it is the case for steerable methods which operate on vector fields? Do we have to use norm non-linearities?
- In the appendix it is stated "Mironenco & Forre (2024) tackles this problem by decomposing a large group into smaller ones and sampling them to enhance sample efficiency. However, it requires sampling on certain measures that may be impractical, such as GL(n)-invariant measure of positive definite matrices.". I'm not sure I understand what limitation is described here. As far as I understand, sampling from this measure is indeed possible (see e.g. [10]) and the SPD manifold has quite extensive applications.
- I don't understand how the Det-Pooling ensures a parametrization on the group $\textnormal{GL}(2, \mathbb{R})$. It seems we are mapping to the space of $\mathbb{R}^{2 \times 2}$ matrices and it is simply assumed that this is a group element? 
- Is there a connection between this work and Olver's work on relative invariants [8]?

[10] Riemannian Gaussian Distributions on the Space of Symmetric Positive Definite Matrices, Said et. al 2015.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper extends the InvarLayer (Li et al., 2024), which uses differential invariants to achieve affine equivariance, by proposing the EquivarLayer. EquivarLayer combines a novel equivariant matrix with differential invariants to generalize from invariance to equivariance. The paper also introduces Det-pooling, which enables EquivarLayer to achieve canonicalization. This canonicalization capability is assessed by using the EquivarLayer model to canonicalize transformed MNIST images, followed by classification with a ResNet-50. The results show improved performance compared to ResNet-50 with data augmentation.

### Strengths
1. This paper introduces a novel and efficient method for extending the affine-invariant layer to an affine steerable equivariant layer. Achieving this in deep learning is challenging, as the affine group has six degrees of freedom, and sampling from this group often incurs prohibitively high computational costs.
2. The proposed ResNet-32 model contains only 0.4 million parameters, which is impressive. This compact model size may enable the exploration of very deep equivariant networks.

### Weaknesses
1. Experiment Design: Using invariant classification to demonstrate the effectiveness of the proposed EquivarLayer for canonicalization is somewhat indirect. The true strengths or limitations of EquivarLayer are obscured by the downstream ResNet-50 prediction network, yet five pages are dedicated to deriving the EquivarLayer. Since canonicalization is a downstream task, its accuracy depends significantly on the model’s ability to preserve information—a quality typically evaluated by learning equivariant features, performing invariant classification, or computing equivariant error. Key questions remain, such as whether EquivarLayer improves upon InvarLayer (as it is a generalization) and how it compares to other steerable methods achieving subgroups of affine group equivariance.
2. Experiment Setup and Comparability: The experiment setup limits comparability with other methods. The train/test split is not provided, and the scale factor range (0.8 to 1.2 or 1.6) differs from that of other scale-equivariant papers, which often use a range of [0.3, 1]. Additionally, key scale-equivariant works, such as [1], are not cited. These omissions make it challenging to compare this model with existing equivariant CNNs, especially since no equivariant network baselines are included in the experimental section.
3. Clarity in Derivations: The derivations following Eq. (16) in Section 2.3 are unclear. The notation for symbols like $u_x, u_y$ is not adequately defined, and it was only by referring to Li et al. (2024) that I understood they represent gradients. While this is a minor issue, a more significant concern is the lack of discussion around $\alpha$ from Eq. (14). Instead, the paper provides an example of an equivariant matrix (Eq. 17) without explaining the derivation of $\alpha$.
Additionally, one of the advantages of equivariance is its ability to preserve information. While the proposed method is computationally efficient, it may sacrifice some information, as it limits gradients to second order and relies on differential invariants for local features. It remains unclear if the gradient order relates to information preservation. The derivations also do not clarify why only first- and second-order gradients are used or how the equivariant matrix is derived.

[1] Sosnovik, Ivan, Michał Szmaja, and Arnold Smeulders. "Scale-Equivariant Steerable Networks." International Conference on Learning Representations.

### Questions
1. Can this approach be extended to handle reflections, specifically for cases where det(A) < 0?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In summary, this paper contributes the following:
- An extension of the equivariant steerable layers for the 2D affine group proposed in [1] from type-0 (scalar-type) feature maps (in the terminology of [2, 3]) to other types utilizing equivariant moving frames [4], specifically by linear combination of the equivariants produced by frames using type-0 features as weights,
- An adaptation of the above layer for invariant or equivariant canonicalization [5] of non-equivariant backbones for the 2D affine group, using global max-pooling of 2-channel type-1 feature with respect to an invariant quantity (absolute determinant),
- Experiments on invariant canonicalization of a pre-trained ResNet50 backbone for MNIST image classification under affine, rotation-scaling, and scaling transformations.

[1] Li et al. Affine equivariant networks based on differential invariants (2024)

[2] Cohen and Welling, Steerable CNNs (2017)

[3] Thomas et al. Tensor field networks: Rotation- and translation-equivariant neural networks for 3D point clouds (2018)

[4] Olver, Modern developments in the theory and applications of moving frames (2015)

[5] Kaba et al. Equivariance with learned canonicalization functions (2022)

### Strengths
- S1. The use of equivariant moving frames to extend type-0 features to other types is technically sound, and original as far as I am aware in the context of steerable networks. (In a broader context, the authors may find [6] and its application to Lorentz canonicalization [7] related, as they also linearly combine equivariants using learned invariant features.)
- S2. The considered application for canonicalization using global invariant pooling is technically sound as far as I can tell, and properly shows the utility of the proposed layer since canonicalization [5] only using type-0 features is not straightforward.
- S3. The experiments show that the approach is able to perform canonicalization of a non-equivariant backbone for invariant MNIST classification under affine transformations, which has been unavailable in current literature before as far as I am aware.

[5] Kaba et al. Equivariance with learned canonicalization functions (2022)

[6] Villar et al. Scalars are universal: Equivariant machine learning, structured like classical physics (2021)

[7] Nguyen et al. Learning symmetrization for equivariance with orbit distance minimization (2023)

### Weaknesses
- W1. A proper comparison against fully equivariant networks for classification (e.g., InvarPDEs-Net and InvarLayer from [1]) is not included in the experiments. Including these baselines would strengthen the paper, especially since canonicalization may benefit from pre-training in non-invariant domains (e.g., ImageNet-1k in this paper) unlike fully equivariant networks.
- W2. It seems possible to use the moving frame in Definition 8 (or the equivariant matrix in Theorem 10) directly for canonicalization without multiplication by type-0 features (Eq. (10)), as this coincides with the definition of equivariant frames in frame averaging [8]. Adding this as a baseline would strengthen the results, as it can be understood as ablating trainability from canonicalization.
- W3. It was unclear to me how the definition and property of moving frames given in Definition 8 and Theorem 9 logically leads to the construction of equivariants using relative equivariants given in Section 2.3.
- W4. The paper demonstrates a single application of the proposed layer as the last layer of a canonicalization network, which extracts 2-channel type-1 features from type-0 features, while all other layers of the network map between type-0 features [1]. This misses (1) feature maps of type >1, (2) layers taking non-scalar features as input, and (3) layers mapping between non-scalar features, all of which are possible within the proposed framework. Testing (a subset) of these would strengthen the paper. A straightforward way is to modify InvarPDEs-Net and InvarLayer from [1] to have non-scalar hidden features, analogous to steerable networks in [2].

Minor typo
- Line 13: InvarLayer -> InvarLayer (Li et al. 2024)

[1] Li et al. Affine equivariant networks based on differential invariants (2024)

[2] Cohen and Welling, Steerable CNNs (2017)

[8] Puny et al. Frame averaging for invariant and equivariant network design (2021)

### Questions
- Q1. Is it necessary that equivariant matrices are square matrices, as implied in Definition 6? As far as I understand, it should be that their number of columns can be flexible, while the number of rows is specified by the representation \rho'.

### Soundness
3

### Presentation
2

### Contribution
3
