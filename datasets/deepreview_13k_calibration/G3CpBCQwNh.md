# PhysPDE: Rethinking PDE Discovery and a Physical HYpothesis Selection Benchmark

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Despite extensive research, recovering PDE expressions from experimental observations often involves symbolic regression. This method generally lacks the incorporation of meaningful physical insights, resulting in outcomes lacking clear physical interpretations. Recognizing that the primary interest of Machine Learning for Science (ML4Sci) often lies in understanding the underlying physical mechanisms or even discovering new physical laws rather than simply obtaining mathematical expressions, this paper introduces a novel ML4Sci task paradigm. This paradigm focuses on interpreting experimental data within the framework of prior physical hypotheses and theories, thereby guiding and constraining the discovery of PDE expressions. We have formulated this approach as a nonlinear mixed-integer programming (MIP) problem, addressed through an efficient search scheme developed for this purpose. Our experiments on newly designed Fluid Mechanics and Laser Fusion datasets demonstrate the interpretability and feasibility of this method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce a new task of explaining observed data using existing partial differential equations in physics and other domains. Previous approaches to discover new partial differential equations via symbolic regressions and randomized algorithms starts from scratch. However, PDEs are inspired from domain knowledge and available theories. The authors propose a method HSTS and STOP algorithm that can find/construct appropriate and interpretable PDEs, incorporating available domain knowledge. Experiments show that the authors proposed method provide better performance compared to baseline methods.

### Strengths
The motivation of the work is described well in the introduction.

### Weaknesses
The method proposed by the authors needs to be explained in more detail, using an example if possible. Figure 2 caption needs to include more details, for example difference between learned PDE and discovered new expression is not clear. Figure 3 caption needs more details, are these learned from the author's algorithm or available from domain knowledge?

### Questions
Although the author's motivation is to generate interpretable PDE models on top of existing domain knowledge, is this work limited to discovering only known theories? For example, given the knowledge of Newtonian fluid mechanics, can this method discover PDEs for non-newtonian fluids?
Another thing to mention here is there are previous approaches for empirical law discovery such as BACON. What benefit does the author's method provide compared to such previous works?
Additionally, how do the authors see the dataset being used in future works? Given these datasets, is there a metric that can measure the interpretability of PDEs discovered by different algorithms, or do we still need domain expert opinion on that?

### Soundness
2

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
4

### Summary
This work addresses limitations in existing methods for discovering Partial Differential Equations (PDEs) from experimental data, particularly the lack of physical interpretability in machine-learning-driven approaches. This approach integrates machine learning with physical hypotheses and theories to guide the discovery of PDEs, prioritizing physical interpretability over purely mathematical accuracy.

Main contributions of this work are:

- The proposal of a new task, termed "PDE Interpretation", which involves selecting physical hypotheses (laws) that align with observed data rather than simply generating symbolic expressions, addressing the gap between mathematical representations and physical meaning.

- The authors, then, recast the discovery/solution task as a mixed-integer programming (MIP)-based approach formulated as a bi-level optimization problem. The outer layer selects the best-fitting physical hypotheses, while the inner layer focuses on expression recovery, involving symbolic regression when new expressions are necessary. They introduce a Monte Carlo Tree Search-inspired Hypothesis Selection Tree Search (HSTS) and a Sequential Threshold Optimization (STOP) algorithm for efficient problem-solving.

- Finally, the study provides two new datasets in fluid mechanics and laser fusion, designed to test the proposed framework's effectiveness in interpreting complex physical phenomena, with scenarios tailored for both Newtonian and non-Newtonian fluid behaviors, as well as thermodynamics in nuclear fusion.

Through experiments, the authors demonstrate that PhysPDE not only accurately recovers existing PDE terms but also extrapolates effectively to new scenarios, outperforming baseline models in terms of recall, precision, and computational efficiency.

### Strengths
The paper does make an original contribution to the state of knowledge, as it reconceptualizes PDE discovery as a physically guided interpretation task. This work focuses on **PDE interpretation**, which is the term they use to denote the integration of prior physical knowledge into the discovery process. By framing the task as one of **hypothesis selection**—with a goal to align with established physical laws rather than simply fit data—the authors address the crucial challenge of **physical interpretability** in machine learning for scientific discovery. 

The paper is well written, with explanations offered with adequate rigor, clearly articulating the mixed-integer programming formulation and providing a detailed breakdown of the two-layer optimization process for hypothesis selection and expression recovery. 

The offered **new datasets**are certainly of significance to the PDE, and particularly fluid mechanics and laser fusion, communities. The experimentation protocol is robust, involving cross-validation, varying boundary conditions, and multiple baselines for comparative analysis.

### Weaknesses
While the paper introduces a promising framework for integrating physical interpretability into PDE discovery, there are areas where the work could be improved to enhance its impact, applicability, and rigor. More specifically,

-  The paper offers a **comparative analysis** with traditional symbolic regression methods, such as PDE-FIND and GPT-based pipelines, however, it lacks an explicit comparison with recent interpretability-focused PDE discovery approaches, as for instance, the work by Champion et al. (2019), or Chen, Liu, Sun et al (2021), who adopt physics biases to discover interpretable models through sparse data. Specifically, the paper does not address how its method compares to approaches that use techniques like sparse regression with physically-informed basis functions or methods that enforce conservation laws during the learning process, which are common in the literature.

- While PhysPDE introduces a bi-level optimization approach, there is limited discussion on how this specific approach advances the interpretability or robustness over similar frameworks like the sparse identification of nonlinear dynamical systems (SINDy), where laws are also indirectly accounted for in the selection of the basis functions. The authors should clarify how the explicit hypothesis selection in PhysPDE provides advantages over the implicit incorporation of physical knowledge through basis function selection in SINDy-like methods, particularly in terms of the interpretability of the final model.

- The paper provides an experimental evaluation of PhysPDE on relatively controlled (and wely generated) datasets, but the scalability of the framework for **high-dimensional, real-world systems** remains unclear. In practical applications such as climate modeling or biomedical engineering, PDE systems can have many more variables and parameters, leading to extremely large hypothesis spaces. The **Monte Carlo Tree Search (MCTS) and Sequential Threshold Optimization (STOP)** methods presented here may struggle with such scalability without further refinement. The authors do not provide a clear analysis of the computational complexity of their approach, nor do they discuss potential strategies for mitigating the computational burden when applied to large-scale problems.

- Although the authors mention that PhysPDE is tested under data noise, the experiments are still based on **synthetically generated datasets**, where the noise distribution can be controlled (as is here the case). Real-world data is typically noisier and may have **systematic errors, non-Gaussian noise, or missing data points**, which could impact the framework’s robustness. In this setting, reliance on a structured hypothesis decision forest could lead to inaccuracies, as the framework might overly rely on a narrow set of physical assumptions that may not fully capture complex, real-world phenomena. The paper lacks a discussion on how the method would handle situations where the true underlying physics is not fully represented in the hypothesis decision forest.

- The **design of the hypothesis decision forest** is critical to PhysPDE’s interpretative power, yet the criteria for constructing this decision structure, such as the choice of hypotheses and decision hierarchy, are not discussed in detail. It is unclear how flexible or adaptable this forest structure is, which could limit the framework's usability across different scientific domains. For instance, if a user wanted to apply PhysPDE to a new domain like biomechanics, would they need to manually create a decision forest from scratch? The authors should provide more details on the process of creating the hypothesis decision forest, including guidelines for selecting relevant physical hypotheses and organizing them into a hierarchical structure, as well as discuss the limitations of this manual approach.

### Questions
Following up on the precious remarks, the following questions arise:

   -  How does PhysPDE compare specifically to recent frameworks that incorporate physical interpretability into PDE discovery, such as those seeking to discovery interpretable models from sparse data Champion et al. (2019), or Chen, Liu, Sun et al (2021)?
- How does PhysPDE handle the computational demands of hypothesis selection when scaling to high-dimensional systems, where the hypothesis space grows exponentially? Could the current approach handle systems with higher-dimensional PDEs or more complex, multi-parameter hypothesis spaces, such as those in climate or geophysical modeling?
- How robust is PhysPDE to real-world data noise, which may not follow Gaussian distributions or may include systematic measurement errors? Would the authors consider augmenting their experimental setup with various types of noise, or could they propose methods to make PhysPDE more robust to noise common in observational datasets?
-  Could you elaborate on how the hypothesis decision forest is constructed, specifically the criteria for selecting hypotheses and organizing them hierarchically? Consider sharing any automation or semi-supervised methods used in building this structure, as this could significantly impact PhysPDE’s ease of adaptation for other researchers.
- How does the decision-making process in the hypothesis selection step work, especially in cases where multiple hypotheses may fit the data similarly well? Also, if multiple plausible hypotheses exist, does PhysPDE allow for any probabilistic ranking or ensemble approach to indicate uncertainty, or is it a hard-selection process? 
- Could the authors clarify how they evaluate interpretability and physical alignment of the recovered PDEs, beyond standard metrics like recall, precision, and MSR?

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
2

### Summary
The paper proposes a new ML4Sci task which focuses on identifying the hypothesis that best align with the data. Prior physics hypothesis and theories are used and the proposed paradigm focuses on identifying which ones align best with the data. The approach is introduced using a mixed-integer programming formulation. Furthermore, the paper designs new data sets for this problem, specifically from the domains of Fluid Mechanics and Laser Fusion.

### Strengths
Overall, the paper proposes a novel task in the ML4Sci field, which could potentially lead to new methods and approaches developed in this field.

### Weaknesses
 - Unless I missed it, the data introduced data sets are not open access and aren't shared during the review process, which limits the possible impact of the paper. 
- Given the complexity of the proposed approach (Fig. 1 which includes many components) and newly generated data sets, the results of the paper are not reproducible with the current information available to the reader.

### Questions
1) Are you planning to release the data sets and the code? (Are these available for review?)
2) Could you elaborate more on the use of LLMs and in particular GPT-4o for extracting physics hypothesis from the data? Why are LLMs specifically appropriate for this task?

Update after discussion period: I have increased my score while keeping my confidence low. The main reproducibility concern has been addressed during the review process.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Physical insights via following existing physical theories and hypotheses are benchmarked in this paper to learn PDE. This allows for possibly good interpolation and extrapolation of PDE learning.

### Strengths
The overall idea is interesting and useful. I like the idea and think it is going in the correct direction -- to make PDE learning physically interpretable via construction of differential equations under the current physical framework, as opposed to symbolic regression only. The datasets used are in different areas, and the physical laws considered are representative.

### Weaknesses
It still remains unclear to me how your decisions (such as is_compressible, is_newtonian) directly affect the PDE system. You have a Figure 3 that shows how the PDE formulation is defined under both different conditions, such as is_compressible=yes and is_newtonian=false. However, I still do not know how this is constructed. What is the connection between these conditions and the PDE appearance? What does it mean for a PDE to have is_compressible=yes? How does that reveal in the PDE terms? I know you are using a decision tree algorithm and use data-label pairs to train a model to predict whether is_compressible=yes. However, but as a reader, understanding what does it mean for a PDE to be is_compressible=yes is important for them to know whether and how that is learnable. This is also good introduction for ML people who may be less familiar with physics.

### Questions
I hope to see the weaknesses being addressed. It should not be hard to address them since these are clarity issues, but they are critical.

### Soundness
4

### Presentation
3

### Contribution
3
