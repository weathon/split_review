# VeriFlow: Modeling Distributions for Neural Network Verification

- Decision: Reject
- Scores: 8, 5, 6, 5

## Abstract
Formal verification has emerged as a promising method to ensure the safety and reliability of neural networks.
Naively verifying a safety property amounts to ensuring the safety of a neural network for the whole input space irrespective of any training or test set.
However, this also implies that the safety of the neural network is checked even for inputs that do not occur in the real-world and have no meaning at all, often resulting in spurious errors.
To tackle this shortcoming, we propose the VeriFlow architecture as a flow based density model tailored to allow any verification approach to restrict its search to the some data distribution of interest.
We argue that our architecture is particularly well suited for this purpose because of two major properties. 
First, we show that the transformation and log-density function that are defined by our model are piece-wise affine. Therefore, the model allows the usage of verifiers based on SMT with linear arithmetic.
Second, upper density level sets (UDL) of the data distribution take the shape of an $L^p$-ball in the latent space. As a consequence, representations of UDLs specified by a given probability are effectively computable in latent space. This allows for SMT and abstract interpretation approaches with fine-grained, probabilistically interpretable, control regarding on how (a)typical the inputs subject to verification are.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a methodology to verify semantically meaning properties using a neuro-symbolic approach, in which the input to the neural network under verification is specified by a flow model trained to model a particular data distribution. The paper shows that the proposed method can be used to generate in-distribution counter-examples that violate a specified output property.

### Strengths
- This paper proposes a generic neuro-symbolic approach to limit the input space to a given data distribution. The specification considered here is novel and of practical interest. 
- The paper designs a novel flow model that allows the definition of the pre-image of a density level set in the latent space via linear
constraints, making the model both interpretable and compatible with existing neural network verifiers.
- The paper instantiates the proposed verification method with two verifiers, one based on bound propagation, the other based on search, and illustrates the trade-off in performance and functionality.

### Weaknesses
 - The paper only considers relatively small datasets. Validating the approach on common benchmark sets considered in VNN literature such as CIFAR-10 and ACAS-Xu would better illustrate the scalability of the approach. 
- The soundness of the verification depends on the quality of the trained flow model. This is an intrinsic issue of neuro-symbolic approaches like this, but I do acknowledge that I cannot see an alternative approach to verify the specifications considered in the paper.

### Questions
How does the flow-based approach compare with the VAE-based approach for modeling a given distribution [1]? 

[1] https://arxiv.org/pdf/2007.08450

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
**Outline**

The authors propose VeriFlow a normalizing flow-based method to learn more realistic input specifications for Deep Neural Network (DNN) verification which can capture more diverse inputs than existing local $L_{p}$ norm-based robustness specification while excluding noisy meaningless inputs included in global input specifications. The authors show with the help of the proposed method they can generate more sensible counter-examples that violate the property under verification.

### Strengths
**Strengths**

- In theory, I think coming up with sensible specifications for Neural Networks is an important problem. Unfortunately, there does not seem to be enough work in this direction.

- Using normalizing flows seems to be a reasonable choice for encoding input specification.

### Weaknesses
 **Questions and weaknesses**

I had a really hard time understanding the paper. The organization and notations and definition used in the paper are not mentioned beforehand.

**Motivation of the work**
Q1. (Lines 52 - 53) “Local properties, on the other hand, suffer from the same problem as statistical testing, i.e., they rely on a high-quality data set that the verification property is based on.” - I completely agree with this statement. However, even networks trained with certifiably robust methods on datasets like CIFAR-10 and Tiny ImageNet [1] (excluding MNIST) still have quite low verified accuracy (percentage of verified local properties), even for small epsilon values like $\epsilon = 8/255$. Given that networks struggle to achieve robustness on this relatively "high-quality data," as the authors noted, what is the reasoning for moving to more challenging input specifications?

**Doubts regarding Proposition 2** 

Q1. I find proposition 2 hard to understand possibly due to the error/ambiguity notations and undefined terms. I list my concerns below 
a. What are affine regions $R_{1},\dots, R_{n}$? 
b. Affine regions and their relation with $F: \mathbb{R}^{n} \to \mathbb{R}^{n}$ are not defined formally. 
c. Why is the number of affine regions $R_{1},\dots, R_{n}$ the same as the input dimension of F? In the worst case, what is the number of affine regions? Is it exponential w.r.t number of activations? 
d. What is $d$ in $\mathbb{R}^{d}$ ?

Q2. Also, piecewise affine functions are not differentiable (like $ y = ReLU\(x\) $ is not differentiable ). Can you give an example of how proposition 2 holds for this case i.e. $y = ReLU(x)$?
 
**Usefulness**

Q1. I am doubtful about the usefulness of the proposed method and seems only experiments are with downsized (10x10) MNIST datasets. Can authors provide any insights into how the proposed method can generate preconditions to other scenarios MNIST (28x28), CIFAR10 (3x32x32), etc.?  It is well known that SMT-based solvers and verification w.r.t. global properties do not work with high-dimensional data, does that mean the proposed can only work for low-dimensional inputs?


**Representation & writing**

Q1. The authors should have clarified which specification the provided counterexample was violating. Let me assume it was a global property. If so, does not this counterexample substantiate why most well-known works [2, 3] focus on local properties? When violations occur, at least local properties tend to produce more sensible, human-understandable images.

Q2. (Lines ) “One well-studied example for a local property is adversarial robustness which requires the neural network to classify any point from the data set as the same class as any minor perturbation of that point.” - Correct me if I am wrong but I don’t think this is an accurate definition. Suppose an image of a 5, along with all its minor perturbations, gets classified as a 6. In this case, the predicted class remains consistent, but all labels are incorrect. Typically, in adversarial robustness, this scenario is considered a violation of the output specification. According to the authors’ definition, however, it would not be regarded as a violation.

Q3. The presentation of the paper could be clearer. Specifically in Section 3, I am unsure which contributions are original to this paper and which pre-exist in the normalizing flows literature.


**Related work is obsolete** 

The works cited in this paper are outdated and have been surpassed by more recent research. I strongly recommend that the authors include references to papers from leading ML conferences (such as ICML, NeurIPS, and ICLR) and top programming languages/verification venues (such as POPL, PLDI, and CAV) from the past 3-4 years. For example,

**Abstract Domain:** The Zonotope abstract domain has been surpassed by the DeepPoly domain [1]. Subsequently, multi-neuron abstraction was introduced in [2], and more recently, the DiffPoly domain [3] was proposed for hyperproperty verification.

**Branch & Bound-Based Verifiers:** Current state-of-the-art verifiers for local properties, such as GCP-CROWN [4] and MN-BaB [5], are not mentioned.

**Input Specification:** Unlike this work, many existing studies consider weaker local specifications to model practical attack scenarios, such as robustness against geometric perturbations [1, 6] and robustness against universal adversarial perturbations (UAP) [3, 7, 8]. This work should mention these studies and justify its approach of addressing more challenging input specifications.

### Questions
Refer to the Weaknesses section

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel approach to modeling input distributions for the purpose of formal verification of neural networks. In particular, the authors leverage flow models to transform input space into upper density level sets, by which existing formal verification approaches for deep neural networks are restricted to search in those data distributions of interest. In this way, one can find more meaningful counterexamples that have practical meaning or are computable under certain perturbation approaches. The authors identify two main properties that shall be satisfied by flow models suited to formal verifications. One is that the transformation by flow models must be peicewise affine. The other is that UDL sets takes the shape of L^p-ball in the latent space. Based on the two properties, the authors further analyze several existing flow models that meet the requirements and demonstrate the effectiveness when being applied to the verification of DNNs with SOTA tools such as ERAN and Marabou 2.0. The authors evaluate their proposed approach and demonstrate the effectiveness in finding more meaningful counterexamples (or adversarial examples) and the scalability to different types of verification approaches.

### Strengths
1. A novel perspective to neural network verification. Most of the existing approaches try to define tightest-possible over-approximation for DNNs to be verified to reduce over-estimation and false positives in formal verification results. This paper considers the verification from a new perspective by restricting verification approaches to meaningful input space. In literature, there are several attempts to the formal verifications of semantic perturbations such as rotations, occlusions, and geometric transformations. This paper considers the semantic perturbations from the distribution perspective. This imposes a new verification problem that is different from existing formal verification problems of DNNs. The work would inspire more solutions to the new problem. 

2. The proposed flow-based method is technically sound and practically useful. Transforming original input space into UDL sets by piecewise affine and abstracting the sets using effectively computable abstract domains are intuitively applicable and straightforward, However, the difficulty lies in finding appropriate flow models and abstractions. The authors identifies the conditions and theoretically prove the qualification of identified flow models to the verification task. 


3. The evaluations are comprehensive and the results are convincing. The results show that the counterexamples computed in the proposed way are indeed more interpretable, while it is compatible with mainstream verification approaches such as SMT-based or abstraction-based ones. The overhead caused by flow models can be ignored. The verification efficiency is mainly depended on the backend DNN verification approaches. However, this is applicable only to low-dimensioned cases.

### Weaknesses
1. The presentation shall be carefully proofread if the paper is finally accepted. There are a lot of grammatical errors that could be completely avoided. For instance, on Line 212, the sentence let XXX is the hyper volume, and on Line 480 complext problems should be complex problems. I just name a few of them. The paper seems to be written in haste. That makes me lower my score. 

2. The experiment part should provide more evidences about meaningful counterexamples generated by the proposed approach. As motivated by finding more meaning counterexamples from neural network verification, the authors should give more evidences. They shall not be placed in appendix. 

3. Section 2 (verification background) seems not necessary. The propose modeling methods are not closely related to backend verification approaches. Having section 2 or not will not affect the understanding of the paper. It provides few useful information to help readers understand the paper.

### Questions
1. In Definition 2, X is a called $k$-radially distributed. However, there is no assumption on $k$. Where does $k$ come from? 

2. It is wired to have only one subsection Section 3.1 inside Section 3. Besides, why do you consider only the types of the first three types in F? In which principle one can decide the types for the first three layers and other remainder layers for different distributions? 

3. In the paper, it is not clear how the flow model is trained and how the quality of trained flow models affect the verification results. Can you provide more details regarding the the issues?

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
The paper introduces a novel framework to extract meaningful counterexamples that a neural network missclassifies called VeriFlow.
This is realized by restricting the global input domain only to images that probabilistically match the actual data distribution via transforming an assumed base distribution from a latent space to the data space. 
The (non-)existance of counterexamples is then formally verified with existing NN verifier (Marabou/ERAN) on the generated data spaces,
where the input set for the verification query is determined by the desired confidence level on the base distribution.
The experiments show promising results and provide qualitative counterexamples.

### Strengths
- Providing meaningful counterexamples is highly relevant in the safety domain, which is not necessarily the case if they are generated form the entire input domain.
- The underlying transformations are piece-wise linear and the input set in the latent space corresponds to an L_p-ball, such that existing NN verifiers can be used to formally show the (non-)existance of counterexamples.
- The quality of the counterexamples can be selected by choosing a confidence level of the underlying distribution (e.g., clearly visible in Appendix C.3).
- Modelling the approach with distributions that go beyond naive ones and perform rigorous theoretical analysis on them.

### Weaknesses
Major points:

One common limitation of probabilistic approaches is that they assume a certain distribution and (in this case) transform this distribution via learning (!) to obtain desired properties (in this case, that it models the actual distribution of the data, e.g., outputs the set of "8" figures). However, if the learned (transformed) distribution in the data space actually matches the training set distribution is not adequately shown/tested. The paper claims that the learned transformation maps a simple base distribution to the complex data distribution, but this mapping's accuracy is not rigorously evaluated. For example, it is not said how long this has to be trained for until this property is reached (e.g., the loss is modeled in a way such that it becomes 0 once all desired properties are (formally) fulfilled). If this cannot be done, one could at least test it empirically: E.g., line 358 states that choosing a certain threshold obtains us top 1% typical images. Thus, as the paper can enclose the respective set in the data space, one could test if 1% of the training data is contained in that set and qualitatively assess if these could be classified as "typical". Doing so for different thresholds and classes would greatly strengthen that claim. If one cannot support the claim of modeling the actual data distribution in any way, there are no probabilistic guarantees even though distributions are used and I would rather categorize it as a heuristic.

The related work section does not adequately place this paper in the broader context of literature. Additionally, I found that both Sec. 2 and Sec. 5 contain stuff that are usually found in related work section and limitations/future work mentioned in Sec. 5 should be stated more clearly in a different section, e.g., Sec. 6. I propose to rework these sections: For example, a new Sec. 2 could give more background information on modeling distributions to get a better understanding of the subsequent Sec. 3. 
The new related work section should place this work into the broader context: 
- There are many more verifiers than presented in the paper. A good starting point for that literature research would be the verifiers of VNN-COMP. Also, not all optimization-based approaches are complete (i.e., either verify or provide a counterexample) but can also be incomplete and sound (i.e., if they say the property holds, it actually holds but there might be cases where they just return unknown without providing a counterexample; as is described for abstract interpretation). I think it would be better to state this, cite a broader range of NN verifiers, but you can be less detailed as currently in Sec. 2 as this is not the main focus of the paper.
- Sec. 5 also mentions "preprocessing steps" to ease verification. One should also mention adversarial training methods that incorporate NN verification into the training process, e.g.
[1] Gowal, et al., “Scalable verified training for provably robust image classification,” 2019.
[2] Zhang et al., “Theoretically principled trade-off between robustness and accuracy,” 2019.
[3] Muller, et al., “Certified training: ¨ Small boxes are all you need,” 2023.
[4] Koller et al., “End-to-end set-based training for neural network verification, 2024

Merging these sections as suggested might also leave more space for explaining the theoretical background in a new Sec. 2 on the required distributions, transformations, and terms like "constant Jacobian determinant" for the sake of self-containment. E.g. line 246 says that the constant Jacobian determinant is demanded, but it is not said how this is done. Some propositions are also missing proofs (e.g., Prop. 1). If they are known results, they could be moved to the new Sec. 2 and cited adequately.

Minor points:
- The paper states that counterexamples generated from the global domain result in noisy, synthetic data that do not necessarily correspond to actual images. However, it is often not difficult to find counterexamples in the local neighborhood of images, which are still meaningful.
- Line 325 states that one has to learn a different transformation for each class. This could be stated more clearly.
- As the input set in the latent space corresponds to an L_p ball (a continuous connected set) and the applied transformations are continuous (piece-wise linear), also the set in the data space is continuous and connected. Thus, we implicitly assume that all our data corresponding to one class live in one connected space. This limitation should be better addressed by saying in which applications this assumption holds.
- Line 195: P_D not introduced, only probability density function p_D. Is it the respective CDF?
- Lack of intuition why a certain base distribution is chosen other than "it turned out that it boosted the performance"
- More detailed steps / motivation / intuition in Sec. 3 to make it easier for the reader to follow along. For example, one could (re-)state the desired properties of the architecture in Sec. 3.1 before saying how the components are constructed to better motivate why they are constructed like that.
- Introduce variables before they are used: e.g., line 349: What is y? Is it scores as introduced in line 356? But there, y is written in bold font and not in regular font as in line 349.
- Line 391: Which "input space" is increased? The dimension of the latent space? If not, how large is the latent space?
- Spelling/Grammar mistakes: Line 198: "Gaussian is ~the~ by far"

### Questions
- I want to know more about the enclosed set in the data space: How restrictive is the subset of the entire domain? For example, the network g_8 aims to only output images with an 8 displayed. However, are there 8s (from the training set) that cannot be constructed? Are a certain % of the 8s from the training set included in the exact / outer-approximative set in the data space if the input set in the latent space matches the same % threshold q?
- How would you address the limitation of the continuous connected set assumption on the data of each class?
- Regarding scalability of NN verifiers: Marabou regularly participates in VNN-COMP where much larger networks and also arbitrary computation graphs are considered. What specifically (e.g., types of layers) limits the scalability of your approach here? Line 390 also says that the verificaiton was done within a few seconds, which does not sound like a huge limitation.
- Many verifiers can also efficiently handle other activation functions than ReLU. Why is this limitation necessary?

### Soundness
3

### Presentation
2

### Contribution
3
