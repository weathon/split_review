# Orthogonal Deep Neural Networks (ODNN): Uncovering Hidden Physics in Partially Observable Systems

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 6, 3

## Abstract
Accurately identifying the underlying physical laws in complex systems is vital for effective control and interpretation. However, many systems are governed by a combination of known physical principles and unobservable or poorly understood components. Traditional model-based methods like Kalman filters and state-space models often rely on oversimplified assumptions, while modern data-driven approaches, such as physics-informed neural networks (PINNs), can suffer from overfitting or lack theoretical guarantees in recovering true physical dynamics. We propose the Orthogonal Deep Neural Network (ODNN) architecture to address these limitations. ODNN disentangles known physical components from unobservable or poorly understood components by imposing orthogonal constraints on the deep neural network. Unlike additive regularization methods, ODNN converts the physical constraints directly into the network structure, ensuring that the DNN focuses on capturing the unknown or complex dynamics without overfitting. This novel approach leverages both explicit orthogonality (e.g., zero inner product) and implicit orthogonality (e.g., contrasting convexity, periodicity, or symmetry) between physical laws and unknown components. Theoretically, we prove that ODNN provides strong guarantees for accurate system identification under mild orthogonality assumptions, building on the universal approximation theorem. Empirically, ODNN is evaluated across eight synthetic and real-world datasets, showcasing its ability to recover governing physical equations with high accuracy and interpretability. Our results demonstrate that ODNN offers significant advantages in terms of generalizability and robustness, making it a valuable framework for physics-based model identification in complex systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper deals with the identification of parameters in physical systems, by splitting the modeled functions into two components:
- A linear combinations of basis functions $f_i$  (e.g Fourrier basis, or other bases encompassing desirable properties such as symmetry, periodicity, etc)
- A highly expressive deep neural network $g$ to model other less structured and less understood phenomenons, such as observational noise or non-linear effects.  
  
The typical culprit of this approach is that the high expressiveness of the DNN allows overtiffing to the observed data, which prevents parameter identification of the basis coefficients.  
  
Therefore, authors propose to impose explicit orthogonality (in the function space, for the typical L2 inner product) by performing the projection of the DNN (as a function) over the orthogonal of the function space spanned by the $f_i$, like a single-step of Gram-Schmidt process.    
  
Alternatively, they propose to enforce something they call implicit orthogonality, where the inner product that defines orthogonality is replaced by choosing properties that are opposite of each other, such as periodicity/non-periodicity, monotonicity, convexity, etc.
  
The approach is benchmarked on several datasets and tasks, such as a synthetic task, speech/music extraction from noisy audio records, control tasks on robotic datasets with noisy measurements, and heat source identification, watermark removal.

### Strengths
### Impact

The experimental section makes a compelling case in favor of the method, in particular the synthetic task 4.1, that illustrates perfectly the inclination to overfitting of competing methods that over-rely on DNN expressiveness. I appreciate the diversity of scenario tackled by the experimental section.

### Simplicity

The method is not only simple, but also very versatile thanks to the flexibility in the choice of basis $f_i$ or architecture $g$, which once again is illustrated by the diversity of tasks successfully tackled.

### Weaknesses
### Soundness

I have a few concerns regarding soundness.

The Theorem 1 is a very strong result, but assumption 1 is even stronger, almost unrealistic, and Theorem 1 is a straighforward consequence of Assumption 1 that does most of the hard work. It is very hard to design a family of functions that would be universal approximator of "everything", but the functional space spanned by the $f_i$. Especially because if $n$ is big, the span $\sum_i\theta_if_i$ is extremely expressive too, for example when $f_i$ are Fourrier basis or Chebychev coefficients.  

In Theorem 1, the sentence "network trained via Equation (2) can learn the physical parameter θj correctly" should be avoided. Nothing can be said about optimization dynamics. Therefore, it is best to only speak of the properties of the minimizers of Equation 2, without attempting to capture what "training" could even meaning.  
  
I was not convinced by the proof of Corollary 1, which supposedly implies Assumption 1. The most important part of the proof is in lines 879-881: "However, if hODNN can approximate f (x) to an arbitrary degree of accuracy, it suggests that hODNN(x) must contain components that are aligned with f(x). This alignment contradicts the orthogonality condition ⟨hODNN (x), f (x)⟩ = 0.".  This is not precise enough IMHO. 
In this context the sentence "must contain components that are aligned with" is a pleonasm that suggests some sort of circular argument. The confusion is made worse by the fact that the paper confuses function space, functions $f$, and predictions $f(x)$.  

Furthermore, Assumption 1 is a statement about *function spaces*, whereas Corollary 1 focuses on a single specific orthogonal projection of Equation (2) that assumes that the true $f$ is known, which means that the $\theta_j$ associated to the $f_j$ are known too. But since optimization of $g$ and $\theta_j$ is simultaneous, I'm not sure what happens. Being orthogonal to a specific $\sum_j \theta_jf_j$ is not the same as being orthogonal to all them for all values of $\theta_j$.  

### Implicit orthogonality. 

I understand authors intent, but I'm not happy with this terminology and I think it's best to avoid it altogether. The paper deals with inner product and projection onto orthogonal complement, which is the precise definition of orthogonality. However, convexity/non-convexity, periodicity/non-periodicity, monotonicity/non-monotonicity are "contrasting properties" (as authors call them) that **do not** translate into any orthogonality, regardless of the inner product used. I know the term "orthogonality" is sometimes loosely used in informal discussion to describe antagonist properties, but in the context of the paper this increases confusion.  
  
Those properties do not define closed spaces (in the topological sense). For example, for many distances over functions spaces, including the L2 norm, it it possible (and easy) to approximate a symmetric/periodic/monotonic/convex function by a sequence of functions that verify none of these properties. In this context, the Assumption 1 does not apply and the theoretical work is irrelevant.  

I believe the link between implicit orthogonality and explicit orthogonality should be discussed more. What is the value of the inner product in practice? Is it close to zero?

### Clarity

I think presentation can be improved at times.

For example, it took me time to parse Proposition 2. It would be better to specify that when using a DNN $g$ that fulfills universal approximation, "*any* set of parameters $\hat \theta_j$" is a solution (emphasis on the *any*).  

In Equation (3), every inner product $\langle f(x), g(x)\rangle$ should be replaced by $\langle f, g\rangle$ to not confuse points and functions.

I have other questions detailed below.

### Questions
1) How do you evaluate the inner product in l270? Do you discretize the interval? If so, how many points? Is it Riemann integration, or something else?  
  
2) This inner product is defined for $\mathbb{R}\rightarrow\mathbb{R}$. How do you handle multivariate inputs?

3) Can you clarify what are the $f_i$ in general? Are you using the same basis every time, or is it different for each task? If so, can you detail for each task the exact expression of $f_j$? Is there unicity of $\theta_j$ coefficients for each of your use-case?

4) Line 268: "Since the signal and disturbance generally occupy distinct frequency bands" => can you comment on this hypothesis? Beside synthetic task of Sec. 4.1 is it verified anywhere else? 

5) Task of Sec 4.5. If there is a fifth heat source, I would expect an algorithm to recover it from observations. What is the rational behind using a basis of symmetric functions for the $f_i$ here? 

6) You relied on the canonical L2 inner product. Do you think using other inner products over function space could yield interesting results? e.g inner products over Sobolev space.

### Soundness
1

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed a ODNN framework to disentangle the real physics and disturbances by leverage the orthogonality. The ODNN is evaluated across eight synthetic and real-world datasets and comparability with several baselines.

### Strengths
Originality: The novelty lies in proposing an alternative view of separating the disturbances and the physics of the system, while most of the existing work adopts adding regularization terms in the loss functions. 

Quality; This paper is rich of details and experiments results. Eight different datasets are investigated and the proposed framework performs the best in these datasets compared with other baseline models.

Clarity: In general clear illustrating the methodology and describe the experiments results. 

Significance: It probably could be a valuable framework for physics systems identifications.

### Weaknesses
Clarity: Too much detail are put in the appendix. It makes the reviewer hard to understand the experiment details without cross-checking. 

The assumption 1 is too strong, which introduced a very big limitation about the current work. In real world environments, the physics and disturbances cannot be just separated by the periodicity vs non-periodicity, monotonic vs non-monotonically and so on. 

The experiment cases are all toy problem without real world complex systems like weather foreseeing, time series prediction in financial supermarket and so on.

### Questions
1. In many situations, the physics and disturbances can not be separated by the assumed way mentioned in the paper. Moreover, even if some of them could be separated, there could be multiple contrast pairs. However, the paper only investigate 1 pair at a time. It could be a problem if scaling up to multiple pairs. Could you add one example showing it works for real world complex system, like weather forecast and explain how your method could scale to real world complex system?

2. The assumption is too strong that the physics network only learns the physics while the disturbance network only learn the disturbances. The boundary of it is actually very ambiguous in the real world. For example, some noise/disturbances could be proportional to the actual state variables and make them have the similar trend. In that case, how will you leverage your work to separate the physics and the disturbances. 

3. Your comparison of the baseline models are somehow obsoleted. There are more recent algorithm about SINDy, Bayesian regression, symbolic learning. To name a few, [1][2][3]. Could you add comparisons to these SOTA model?

[1] Physics-informed learning of governing equations from scarce data.

[2] Bayesian spline learning for equation discovery of nonlinear dynamics with quantified uncertainty

[3] Symbolic physics learner: Discovering governing equations via monte carlo tree search

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces Orthogonal Deep Neural Networks (ODNNs), a novel approach to disentangle known physical dynamics from unknown components or disturbances. The method leverages two types of orthogonality: explicit orthogonality, which is enforced through zero inner product between physical components and disturbances, and implicit orthogonality, implemented using off-the-shelf networks designed to capture distinct properties (e.g., convexity or periodicity). The authors provide rigorous theoretical proofs and validate the ODNN framework through extensive experiments across both simulated and real-world tasks, demonstrating its effectiveness and robustness.

### Strengths
- This paper is well-written. A lot of examples are provided to explain the motivation why orthogonality is utilized to disentangle known physics and unknown components. These examples really help me understand this paper.
- The experiments are well-designed. The extensive experiments are across various fields, including computer vision, signal processing, reinforement learning and so on. These experiments demonstrate ODNNs' broad applicability and outstanding performance.
- I believe the theoretical proof is a strong aspect of this paper, significantly enhancing its overall quality.

### Weaknesses
 - Based on my understanding, ODNN can be viewed as a type of hybrid neural network, combining physical models derived from first principles with data-driven models. This approach is not novel within the physics-guided machine learning community, as hybrid models have been widely explored and applied across various domains. Given this context, I think some issues are not well-discussed in the paper:
  - ODNN appears to aim at learning the residuals of partially known physics, as described in Section 3.2 of [1]. Based on this survey, A natural alternative training strategy for regular DNNs would be to first fit the parameters of the known physics on the training data, compute the residuals, and then optimize the neural network to predict those residuals. This alternative approach is not discussed or included as a baseline in the paper, which could have provided a more comprehensive evaluation.
  - The work relies heavily on the assumption that the physical and non-physical components are additively separable, i.e. $f(x) + g(x)$, which underpins the use of orthogonality. However, as discussed in [2], other forms of combination exist, such as $f(g(x))$ or $f(x)g(x)$. I don’t think orthogonalities can work in such cases.
- The main claim of this paper, that ODNN can disentangle known physics from unknown components such as disturbances, may be overstated. In practice, the implementation of implicit orthogonality relies on prior knowledge about the non-physical components. Specifically, one must know certain properties of the non-physics part (e.g., convexity, periodicity) to select the appropriate off-the-shelf network. Given this reliance on prior information, it seems inaccurate to claim that the non-physical components or disturbances are entirely unknown or unobservable.
- The implementation of implicit orthogonality in this work is quite limited. The paper primarily discusses a few types of implicit orthogonality, such as convexity, periodicity, symmetry, and monotonicity, relying heavily on off-the-shelf networks to implement these properties. However, I believe there are many more potential forms of implicit orthogonality, such as time-invariant vs. time-variant systems or energy-conserving vs. energy-dissipating dynamics. These additional implicit orthogonality types are not explored, and it’s unclear if suitable off-the-shelf networks exist to handle them. Therefore, the current approach may be too dependent on existing network architectures and does not fully address the broader scope of possible implicit orthogonalities.

### Questions
- The key step in enforcing explicit orthogonality relies on calculating the inner product $\langle h_\mathrm{DNN}(\mathbf{x}), f(\mathbf{x})\rangle$, which is defined as an integral. However, it seems that the specific method for performing this integral is not introduced in the paper. Could you clarify which numerical integration method is used? For example, is it the trapezoidal rule? If so, the choice of numerical integration could introduce additional issues. For instance, methods like the trapezoidal rule are known to struggle with oscillatory integrals  [3], potentially affecting the accuracy of the orthogonality enforcement in certain cases.
- I'm a bit confused about Figure 1. Does the figure suggest that the physical component always corresponds to properties like non-convexity, non-periodicity, asymmetry, and non-monotonicity? If so, I believe this generalization might not be appropriate. In many cases, physical laws can exhibit convexity, periodicity, symmetry, or monotonicity, depending on the specific system being modeled. Could you clarify whether this interpretation is correct?
- Based on my understanding, explicit orthogonality and implicit orthogonality are not applied simultaneously across different experiments. In some experiments, only explicit orthogonality is utilized, while in others, a specific form of implicit orthogonality is applied. Is this interpretation correct? If so, this further supports my point in Limitation 2: The non-physical components are not entirely unknown, as the approach still relies on prior knowledge about the nature of these non-physical parts to implement the appropriate orthogonality.

To be honest, I appreciate the method of disentanglement presented in this paper, but it seems that some important issues remain unaddressed. If my questions can be clarified and the limitations discussed more thoroughly, I would be willing to reconsider my score and raise it.

**References**

[3] Ma, Yunyun, and Yuesheng Xu. "Computing highly oscillatory integrals." Mathematics of Computation 87.309 (2018): 309-345.

### Soundness
3

### Presentation
3

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
This study emphasizes the application of physics and includes comparisons to methods like the Kalman filter and Physics-Informed Neural Networks (PINNs). At first glance, it appears to address dynamical systems with temporal evolution. However, as shown in equation (1), its originality lies in decomposing the simple function regression problem $y = F(x)$ into multiple bases. Though each basis is described as a "physical equation," what constitutes such a basis remains ambiguous.

Concrete examples finally appear in Section 4, which are applications in signal source separation and watermark removal. Yet it remains questionable whether these applications genuinely involve physics. (4) mentions the use of a robotics dataset, yet Section 5 reveals the true purpose as a regression task for a reward function, rather than system modeling. Although (5)-(7) present more clearly defined problem settings, their relationship to physical laws remains unclear. Additionally, throughout the study, what are inputs and outputs is often unclear, and the validity of decomposing the function $F(x)$ remains difficult to assess. The attempt to emphasize generality and physics ends up obfuscating its main contributions.

### Strengths
This study attempts to decompose functions approximated by neural networks into orthogonal basis functions. It is an attractive harmony between classical function approximation and modern data-driven learning. Moreover, in certain problem settings, decomposition into orthogonal bases is known to be highly effective, and it could prove valuable in numerous situations.

### Weaknesses
This study emphasizes the application of physics and includes comparisons to methods like the Kalman filter and Physics-Informed Neural Networks (PINNs). At first glance, it appears to address dynamical systems with temporal evolution. However, as shown in equation (1), its originality lies in decomposing the simple function regression problem $y = F(x)$ into multiple bases. Though each basis is described as a "physical equation," what constitutes such a basis remains ambiguous.

Concrete examples finally appear in Section 4, which are applications in signal source separation and watermark removal. Yet it remains questionable whether these applications genuinely involve physics. (4) mentions the use of a robotics dataset, yet Section 5 reveals the true purpose as a regression task for a reward function, rather than system modeling. Although (5)-(7) present more clearly defined problem settings, their relationship to physical laws remains unclear. Additionally, throughout the study, what are inputs and outputs is often unclear, and the validity of decomposing the function $F(x)$ remains difficult to assess. The attempt to emphasize generality and physics ends up obfuscating its main contributions.

Orthogonal decomposition is appropriate for some problems and not for others, and this appropriateness is generally unrelated to physics. Given the inconsistencies between the method and the claims, as well as the insufficient evaluation, it is difficult to rate this study highly in its current form.

In summary, the study raises two major concerns:

1. In settings such as signal source separation, watermark removal, reinforcement learning reward functions, and power grid system identification, decomposing into orthogonal components might seem appropriate, yet its connection to physics remains ambiguous. Furthermore, these problems are often addressed with widely accepted methods like principal component analysis and independent component analysis, and the advantages of the proposed method over these are unclear. To effectively highlight contributions, a major revision of the introduction would be essential.

2. The extent to which the proposed approach captures physical laws remains ambiguous. Expressing solutions to differential equations as sums of functions implies a form of linearity assumption. Models and predictions derived from real data tend to be inherently complex and nonlinear, which casts doubt on the appropriateness of such a decomposition. While it may be useful for removing additive noise, labeling this as "physics" seems tenuous.

From a technical standpoint, additional issues arise:

The term $f(x)$ denotes the value of function $f$ at point $x$, not the function itself. Therefore, inner products in function space should be expressed as $\langle f, g \rangle$, not $\langle f(x), g(x) \rangle$, which represents the inner product of values taken by vector-valued functions. As a result, equation (3) is incorrect. Even if it is interpreted as an inner product in function space, integration (as in equation (8)) would be necessary, requiring numerous evaluations at collocation points and significantly increasing computational costs.

In Table 1, while the proposed method appears to deliver substantial performance improvements, each problem setting has specialized prior works. Simply comparing the proposed approach with general-purpose methods like SINDy and PINNs does not sufficiently demonstrate its practical value.

### Questions
In summary, the study raises two major concerns:

1. In settings such as signal source separation, watermark removal, reinforcement learning reward functions, and power grid system identification, decomposing into orthogonal components might seem appropriate, yet its connection to physics remains ambiguous. Furthermore, these problems are often addressed with widely accepted methods like principal component analysis and independent component analysis, and the advantages of the proposed method over these are unclear. To effectively highlight contributions, a major revision of the introduction would be essential.

2. The extent to which the proposed approach captures physical laws remains ambiguous. Expressing solutions to differential equations as sums of functions implies a form of linearity assumption. Models and predictions derived from real data tend to be inherently complex and nonlinear, which casts doubt on the appropriateness of such a decomposition. While it may be useful for removing additive noise, labeling this as "physics" seems tenuous.

From a technical standpoint, additional issues arise:

The term $f(x)$ denotes the value of function $f$ at point $x$, not the function itself. Therefore, inner products in function space should be expressed as $\langle f, g \rangle$, not $\langle f(x), g(x) \rangle$, which represents the inner product of values taken by vector-valued functions. As a result, equation (3) is incorrect. Even if it is interpreted as an inner product in function space, integration (as in equation (8)) would be necessary, requiring numerous evaluations at collocation points and significantly increasing computational costs.

In Table 1, while the proposed method appears to deliver substantial performance improvements, each problem setting has specialized prior works. Simply comparing the proposed approach with general-purpose methods like SINDy and PINNs does not sufficiently demonstrate its practical value.

### Soundness
2

### Presentation
1

### Contribution
2
