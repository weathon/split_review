# Learning Chaotic Dynamics with Embedded Dissipativity

- Decision: Reject
- Scores: 6, 8, 3, 3, 5, 3

## Abstract
Chaotic dynamics, commonly seen in weather systems and fluid turbulence, are characterized by their sensitivity to initial conditions, which makes accurate prediction challenging. Despite its sensitivity to initial perturbations, many chaotic systems observe dissipative behaviors and ergodicity. Therefore, recently various approaches have been proposed to develop data-driven models preserving invariant statistics over long horizons. Although these methods have shown empirical success in reducing instances of unbounded trajectory generation, many of the models are still prone to generating unbounded trajectories, leading to invalid statistics evaluation. In this paper, we propose a novel neural network architecture that simultaneously learns a dissipative dynamics emulator that guarantees to generate bounded trajectories and an energy-like function that governs the dissipative behavior. More specifically, by leveraging control-theoretic ideas, we derive algebraic conditions based on the learned energy-like function that ensure asymptotic convergence to an invariant level set. Using these algebraic conditions, our proposed model enforces dissipativity through a ReLU projection layer, which provides formal trajectory boundedness guarantees. Furthermore, the invariant level set provides an outer estimate for the strange attractor, which is known to be very difficult to characterize due to its complex geometry. We demonstrate the capability of our model in producing bounded long-horizon trajectory forecasts that preserve invariant statistics and characterizing the attractor, for chaotic dynamical systems including Lorenz 96 and a truncated Kuramoto--Sivashinsky equation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors outline a novel approach to learn chaotic dynamics that ensures dissipativity. By deriving algebraic conditions for the dissipativity and implementing via a stability projection the authors claim to guarantee that the model generates bounded trajectories. The implementation approach captures the long-term statistics of various dynamical systems studied here.

### Strengths
- The work outlines novelty in the derived energy based algebraic conditions for dissipativity.   
- Incorporating a regularisation loss of the invariant level set volume aids the model in detecting an outer estimate of the attractor.
  - The paper contains a comprehensive introduction to the topics considered.

### Weaknesses
 - All figures could be greatly improved with proper legends and labels.

- Further numerical experiments on the validity of the approach and comparisons to other baselines would greatly strengthen the overall paper.

### Questions
- Is it possible to derive an alternative regulariser to the loss function to drive tighter bounds on the level sets?  
- Do the authors foresee any difficulties when scaling to higher dimensional systems?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper develops a novel approach to a neural-network-based model of dynamical systems.  A Lyapunov functional is learned and applied to the dynamics that guarantees that there are no unbounded trajectories.  Hence, stability of the system is preserved, which mitigates an issue that plagues many other neural surrogates --- instability of rolled out trajectories.

### Strengths
The authors present a novel idea that addresses a longstanding issue with many neural-network based surrogate models of chaotic dynamical systems, which is that neural surrogates often tend to be unstable.  The use of modifying dynamics through a Lyapunov functional to guarantee stability of the learned system is original and a conceptually interesting approach.  The authors' presentation is clear, and there is sufficient mathematical justification to demonstrate their claim of guaranteeing stability.

The results shown for several systems illustrate that the proposed method works well in practice (at least for the systems shown) -- the method indeed ensures stability, and also preserves invariant statistics.

This work is significant and would be of interest to many other researchers.  It also presents a future research direction because it can be extended in various ways.

### Weaknesses
- The ODE systems that this new method is applied to are all rather simple.  The most complex is a 8-degree-of-freedom truncation of the Kuramoto Sivashinsky equation.  I wonder, why not use a more complex problem, like the KS equation truncated to many more degrees of freedom, i.e. N=64 or 128?  That would preserve the spatial properties of the PDE much better.  The main reason I suggest it is that it leaves it unclear how well this method scales to more complex, more challenging problems and attractor geometries. Specifically, the 8-DOF KS system is a very low-dimensional projection, and it's unclear if the learned Lyapunov function can effectively constrain the dynamics in higher-dimensional chaotic systems. The method's performance should be evaluated on systems with a larger number of unstable modes and more complex attractor structures.

- Not a significant point, but I think some of the introduction can be tightened up, leaving a more concise paper or more room to discuss other points.  It may not be necessary to include so much exposition on chaotic systems, Lyapunov exponents, strange attractors, etc.

### Questions
Is there any effect on training, either in training convergence or in computational expense, by adding the Stability Projection?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a neural network architecture designed to learn dissipative chaotic dynamical systems with a guarantee of generating bounded trajectories. By integrating the control theory principles to enforce algebraic conditions ensuring that the learned dynamics converge to invariant measure. While the problem addressed is interesting and the theoretical guarantees looks reasonable, there are several concerns regarding the clarity of the method, the experimental evaluation.

### Strengths
The paper addresses the challenging problem of learning dissipative chaotic systems, which has broad implications in fields like weather prediction and fluid dynamics.The authors provide a theoretical basis for their approach, leveraging Lyapunov principle in control theory to ensure dissipativity and boundedness of the learned trajectories. 

The experimental results, achieved through the rollout of predictions, converge to the invariant statistical sets of various chaotic systems, including the Lorenz63, Lorenz96, and the truncated Kuramoto–Sivashinsky equations.

### Weaknesses
The explanation of the proposed methodology, especially the construction of the stability projection layer and its practical implementation, lacks clarity.

Loss function:
It is stated that c is learned via the loss function, however, if I understand correctly, c is also exist in the loss function set up. if 
c were to be preset rather than learned, it would constrain the size of M(c) from the beginning, potentially leading to suboptimal results if this predefined boundary doesn’t align well with the attractor in the data.

In this paper, "Markov neural operators for learning chaotic systems,  Advances in Neural Information Processing Systems, 2022"
They defined a ball to bound the trajectory, to me, it seems that you set up a Ellipsoid boundary other than the ball. Thus, the contribution is questionable.


Experimental:
- Despite important problem, this work only use low dimensional data sets to test the idea which is not convincing enough, several works can achieve this without 
- Training data sets is very limited, with only 4-10 trajectories it is hard to believe that how effective the the method for the unseen data.
- Figure is misleading, Fig 4,5 a and b should be just MSE loss, and the author still name it as fstar which leads to confusion.
- The baseline used here is questionable, as it only compares against the Mean Squared Error (MSE) loss without incorporating the Lyapunov component. For instance, the paper "Stability Analysis of Chaotic Systems from Data" also successfully reconstructs the invariant measure. Without comparing the proposed method to other established approaches, it remains unclear how effective it truly is. Demonstrating its performance against a broader set of baselines would strengthen the argument for its effectiveness.

### Questions
1. please clarify if the c is learned or pre-set. if learned please describe how does it iteratively incorporated with the loss function.

2. Why the dimension of provided examples are very low? Does the model fits the high dimensional systems? at least 2D  Kolmogorov flow should be presented.

3. Does the training set and test sets are the same?

If authors can compare their method with the state-of-the-art model like Markov neural operators, it would be more convincing.

### Soundness
2

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
5

### Summary
This paper introduces a Lyapunov-based approach to predict dissipative chaotic systems. In this paper, it learns a Lyapunov function enforcing the trajectories onto their invariant sets, subsequently generating trajectories within these invariant sets.

### Strengths
The paper addresses an intriguing problem in the realm of dissipative chaotic dynamical systems. The presentation is clear and straightforward, making the methodology easy to follow. The proposed theory effectively leverages Lyapunov functions to ensure the convergence of trajectories towards global strange attractors, establishing a meaningful connection between Lyapunov stability and chaotic system behavior.

### Weaknesses
### Theoretical Concerns
1. **Quadratic Lyapunov Function:**
   - The use of a quadratic form for the Lyapunov function is questionable. Chaotic systems exhibit highly complex behaviors (many chaotic systems are hyperbolic or partially hyperbolic [1]), and a simple quadratic Lyapunov function may not reliably guarantee global dissipativity—especially since the problem of constructing a global Lyapunov function for such systems remains unresolved. It is unclear how a constant positive definite matrix would suffice in this context. 

[1] Hasselblatt, Boris, and Anatole Katok, eds. Handbook of dynamical systems. Elsevier, 2002.
   
2. **Optimization Challenges:**
   - Optimizing a quadratic Lyapunov function involves sum-of-squares optimization, which is related to the Hilbert 5th problem. This connection raises concerns about the scalability of the proposed algorithm, a point that the paper fails to adequately discuss. Furthermore, a quadratic Lyapunov function is inherently limited. For instance, certain chaotic systems are governed by PDEs with infinite-dimensional states, which would result in a positive definite matrix $Q$ of very high dimension, making optimization of such a matrix impractical.
   
3. **Invariant Set Representation:**
   - The paper claims that the sub-level sets of the Lyapunov function serve as global attractors. However, due to the quadratic nature of the Lyapunov function, these sub-level sets are high-dimensional ellipsoids, which may lack mathematical rigor. For example, the shape of many attractors may be irregular, such as the butterfly-shaped Lorenz-63, directly making the invariant sets as ellipsoids is too strong. The author proposed a joint learning way to train the model, but I question the training stability for chaotic systems, proving a loss curve figure is desirable. 
   
4. **Difference with Existing Work:**
   - Research [1] presents a similar methodology by imposing a constraint to confine trajectories within an invariant set, treating the radius as a hyperparameter. The scale of this radius significantly impacts learning outcomes, yet the current paper does not address this aspect. Can you discuss the true difference between this work and [1], particularly in the novelty?

### Ergodicity Assumption
- **Lack of Guarantee:** After trajectories enter strange attractors, there is no theorem provided to guarantee ergodicity. The paper only reports the energy spectrum, raising concerns that trajectories may not fully explore the bounded attractor set, potentially conflicting with the ergodic assumption.
- **Missing Metrics:** A comparison metric, such as those based on transport distances like Maximum Mean Discrepancy (MMD) or Kullback-Leibler (KL) divergence, should be employed to measure the probability distribution on the invariant set. This is a common practice in learning algorithms to ensure invariant probability measures.

### Experimental Limitations
- **Loss Function:** The loss function in Line 368 is intended for learning local tangent vectors. However, for systems like Lorenz 63, the vector fields in the butterfly attractor exhibit extremely complex structures, such as fractal-like behaviors [2], which are also common in many other chaotic systems. In these scenarios, the vector fields can be highly intricate and even discontinuous, which I believe makes this problem NP-hard. I question the sample complexity and the feasibility of optimizing this loss function. Could you provide a plot of the training process and the loss value over time to illustrate its behavior?
- **Weak Experimental Section:** The experimental section is notably weak, lacking comparisons with other established algorithms such as those referenced in [1, 3]. It is better to compare comprehensively with the existing methods based on metrics such as short-term accuracy, long-term statistics (MMD or KL divergence).
- **Low-Dimensional Cases:** The experiments are confined to low-dimensional cases with minimal metrics. High-dimensional scenarios, including 2D cases like weather data or turbulent flows, are not explored, limiting the demonstration of the method's effectiveness.

### Questions
1. **Redundancy in Theoretical Results:**
   - The main theorem and propositions presented in this paper are well-established in existing literature. The authors should directly cite relevant prior work instead of reiterating these foundational results without proper attribution.

2. **Ergodicity Guarantee:**
   - The paper does not provide a mechanism to ensure ergodicity, i.e., the ability of trajectories to fully explore the bounded invariant set based on its invariant measure once they reach the invariant set.

3. **Selection of Hyperparameters:**
   - The determination of the ellipsoid radius is inadequately addressed. The paper lacks a clear methodology for selecting an appropriate radius, raising concerns about the validity and reproducibility of the results.

4. **Training Stability and Loss Function:**
   - I question the training of vector fields in loss function, so could you provide a plot of the training process and the loss curves to illustrate its behavior?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on learning models to predict chaotic systems’ behaviour while maintaining dissipative properties. It addresses the challenge of achieving long-term stability in chaotic system predictions by proposing a neural network model with embedded dissipativity. This model incorporates Lyapunov function principles from control theory to ensure that generated trajectories remain bounded, thus avoiding statistical invalidation due to unbounded trajectories.

Although the idea of "embedding dissipativty" has been mentioned in some literature combining deep learning and control, the unique contribution of this work is to introduce algebraic conditions combined with a stability projection layer, providing an efficient implementation method. This projection layer is based on the Lyapunov method and performs energy constraints in the neural network, avoiding the need to rely on external data or expert knowledge.

### Strengths
The concept of dissipative embedding has been explored in related fields, this paper proposes an innovative approach in terms of specific implementation methods. It introduces Lyapunov functions into the neural network structure and ensures that the generated trajectory satisfies dissipativity through a stability projection layer, thereby keeping the trajectory bounded in the long-term prediction of chaotic systems. This approach of combining the stability conditions of control theory with deep learning models provides a new perspective for modeling chaotic systems and reduces the reliance on empirical regularization.

The paper is written with high clarity and readability and is able to combine complex control theory concepts with neural network models well, allowing readers to understand its theoretical motivation and implementation methods. The author provides intuitive explanations when introducing concepts such as Lyapunov stability, dissipation, and strange attractors, and enhances understanding through diagrams and formulas. The overall structure is logically clear, and the paper has a good connection from problem definition, and method design to experimental verification.

### Weaknesses
The paper lacks citations to related work in some areas, e.g., Markov neural operator (MNO) in the NeurIPS 2022 paper "Learning Dissipative Dynamics in Chaotic Systems". If its method can be compared with existing research in more detail, especially in the field of dissipative embedding, readers will have a more comprehensive understanding of the innovativeness of this method.

The experiment part of this paper is insufficient for the following reasons:
- No comparison with benchmark algorithms: There are some mature benchmark algorithms in the field of long-term prediction of chaotic systems, such as Reservoir Computing (RC) and Recurrent Neural Networks (RNN) (especially LSTM and GRU), etc. It is recommended that the author select these algorithms and compare them with their methods under the same experimental environment and initial conditions to demonstrate the advantages of the new method in long-term stability and dissipation.
- Lack of statistical performance evaluation metrics: Introduce commonly used chaotic system evaluation metrics, such as Lyapunov exponent (used to quantify sensitivity to initial conditions), attractor reconstruction error, and autocorrelation, and compare the performance of the new method and the benchmark algorithm on these metrics. This will help verify the effectiveness of the paper's method in preserving the statistical properties of chaotic systems.
- Lack of testing on high-dimensional chaotic systems: In addition to the existing Lorenz system and Kuramoto-Sivashinsky equation, it is recommended to add other chaotic systems (such as Rossler system or higher-dimensional Navier-Stokes system) for testing to prove the versatility of the method. This can demonstrate the adaptability and stability of the new method under different complexities and dimensions.
- No ablation experiment: In order to gain a deeper understanding of the role of the stability projection layer, an ablation experiment can be designed. For example, the stability projection layer can be removed from the model to observe the changes in its stability in long-term predictions. This will be able to specifically show the impact of embedding dissipative structures on model performance, thereby further verifying the necessity of this innovation.

### Questions
1. Selection and generalization of Lyapunov functions: Although Lyapunov functions are very useful tools in control theory, it may not be easy to design and select appropriate Lyapunov functions in complex chaotic systems, especially in multidimensional or nonlinear systems. Many times, the form of the Lyapunov function needs to be manually designed or assumed based on the specific system, and may lack generalization. Is this approach applicable to a wider range of chaotic systems? In complex practical applications, finding a suitable Lyapunov function may require a lot of expert knowledge and manual design, which limits scalability. If the choice of Lyapunov function is not robust enough, the model may not be applicable to different types of chaotic systems.

2. Design complexity and effectiveness of the projection layer: The projection layer is designed to ensure that the learned dynamic simulator is dissipative, which means that some parts of the neural network are explicitly designed to obey specific constraints (such as trajectory boundedness). However, the design and implementation of the projection layer can be complex. The specific implementation of the projection layer in the neural network and how to ensure that it does not over-constrain the model flexibility is a key issue. The projection layer may affect the learning ability of the neural network, especially when the model needs to deal with different types of nonlinear chaotic systems. Excessive projection may limit the expressive power of the model, causing it to fail to capture some more complex dynamic behaviors.

3. The paper claims to parameterize the Lyapunov function V as a quadratic function for simplicity and points out that the framework can accommodate any function that satisfies the requirements of Theorem 1. However, this statement is reasonable in theory but may have limitations in practical applications.
- In practical applications, non-quadratic Lyapunov functions often significantly increase computational complexity. For example, parameterized as a neural network or a high-order polynomial will bring additional difficulties in gradient calculation and projection layer implementation.
- Complex Lyapunov functions may be more difficult to maintain the required monotonicity and positive definiteness in the model, especially in high-dimensional chaotic systems.
- Complex V forms may lead to numerical instability, especially in the training process, which is prone to gradient explosion or disappearance.
- Suggestions for improvement: If the authors hope to actually expand to a more general Lyapunov function form, the author can consider providing several experimental verifications of non-quadratic parameterized V to demonstrate the effectiveness of the framework in these cases. This work can further analyze the trade-offs between different V forms in terms of numerical stability and computational complexity to demonstrate the practical applicability and versatility of the framework.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces a novel neural network architecture to model chaotic systems with dissipative properties. The proposed model uses Lyapunov control-theoretic methods to ensure that the system maintains dissipative behaviours, effectively providing guarantees on the boundedness of the attractors. The proposed architecture, which includes a stability projection layer, was tested on systems was tested on some standard chaotic systems. This result significantly improves models without the stability projection layer, which is prone to unbounded errors. These results contribute to more reliable learning of chaotic dynamics.

### Strengths
The targeted problem is highly significant in chaotic systems modelling, and the general idea is promising. The proposed approach effectively integrates control-theoretic concepts with machine learning to ensure bounded trajectory generation, contributing to the dissipative properties of chaotic systems—an essential aspect for the validity of invariant statistics. The paper is well-structured and presents the proposed method concisely.

### Weaknesses
## Experiments 
- The numerical experiment lacks a comparison with updated approaches in chaotic system modelling, limiting the perspective on how much improvement the proposed model offers. Specifically, the absence of comparisons with methods like reservoir computing, which have demonstrated effectiveness in learning chaotic systems, makes it difficult to assess the practical significance of the proposed approach. The focus on boundedness should not overshadow the importance of prediction accuracy and long-term statistical properties, which are central to evaluating dynamical system models.
- The systems examined in the experiments appear simple and low-dimensional (no more than five states). This raises concerns about the scalability of the proposed method. The use of a truncated KS system, while 8-dimensional, does not fully address the scalability issue, as many real-world chaotic systems operate at much higher dimensions. The lack of experiments on higher-dimensional systems limits the applicability of the proposed method.
- The weight hyperparameter $\lambda$ should be critical in balancing forecasting accuracy with estimating the attraction region. However, an ablation study on the impact of $\lambda$ is missing. The robustness of the initial choice of $c$ should also be evaluated. The absence of a systematic analysis of these parameters makes it difficult to understand the sensitivity of the method and its practical tuning.
- While the proposed method successfully generates bounded trajectories, the investigation into long-term prediction accuracy and related statistics is missing in the numerical experiments. The provided Figures 3, 4, and 5 are significantly insufficient for verifying the effectiveness of the method. Boundedness alone does not ensure the precise or unbiased estimation of long-term statistical properties. The lack of quantitative metrics for long-term prediction and statistical properties makes it difficult to assess the overall performance of the method.

## Some minor issues
- Typos "[sec]" in Line 388,395,397,441,505.
- Line 396, "we *forward simulate* the learned ..." 
 I’d encourage the authors to redo a proofread.

### Questions
- The authors claim to learn an outer estimate of the complex strange attractor. However, the proposed method utilizes a simple ellipsoid to approximate the strange attractor without providing any quantitative results to support this claim. Could the authors provide a more detailed justification for why an ellipsoid is an appropriate representation of complex attractors and include quantitative verifications?
- Propositions 1 and 2 appear to be well-known results derived from Lyapunov's Direct Method [Chapter 3, Slotine et al. (1991)]. Could the authors clarify how these propositions differ from existing results? Why were appropriate citations not provided if they do not offer novel contributions?

References 

- Slotine, Jean-Jacques E., and Weiping Li. Applied nonlinear control. Vol. 199. No. 1. Englewood Cliffs, NJ: Prentice hall, 1991.

### Soundness
2

### Presentation
3

### Contribution
2
