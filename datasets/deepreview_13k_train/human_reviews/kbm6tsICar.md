# No Equations Needed: Learning System Dynamics Without Relying on Closed-Form ODEs

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Data-driven modeling of dynamical systems is a crucial area of machine learning. In many scenarios, a thorough understanding of the model’s behavior becomes essential for practical applications. For instance, understanding the behavior of a pharmacokinetic model, constructed as part of drug development, may allow us to both verify its biological plausibility (e.g., the drug concentration curve is non-negative and decays to zero in the long term) and to design dosing guidelines (e.g., by looking at the peak concentration and its timing). Discovery of closed-form ordinary differential equations (ODEs) can be employed to obtain such insights by finding a compact mathematical equation and then analyzing it (a two-step approach). However, its widespread use (in pharmacology and other domains) is currently hindered because the analysis process may be time-consuming, requiring substantial mathematical expertise, or even impossible if the equation is too complex. Moreover, if the found equation's behavior does not satisfy the requirements, editing it or influencing the discovery algorithms to rectify it is challenging as the link between the symbolic form of an ODE and its behavior can be elusive. This paper proposes a conceptual shift to modeling low-dimensional dynamical systems by departing from the traditional two-step modeling process. Instead of first discovering a closed-form equation and then analyzing it, our approach, direct semantic modeling, predicts the semantic representation of the dynamical system (i.e., description of its behavior) directly from data, bypassing the need for complex post-hoc analysis. This direct approach also allows the incorporation of intuitive inductive biases into the optimization algorithm and editing the model's behavior directly, ensuring that the model meets the desired specifications. Our approach not only simplifies the modeling pipeline but also enhances the transparency and flexibility of the resulting models compared to traditional closed-form ODEs. We validate the effectiveness of this method through extensive experiments, demonstrating its advantages in terms of both performance and practical usability.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents an approach to modeling the solutions (trajectories) of dynamical systems by bypassing the need to derive (discover) the closed-form of ordinary differential equations (ODEs). Instead of the conventional two-step approach (discovering an ODE and then analyzing it), the authors propose *direct semantic modeling*. 

The promised contributions include:

1. A shift from Syntactic to Semantic representations. The latter delivers a formal means to describing the behavior of trajectories and system dynamics. 

2. A direct Semantic Modeling framework, which essentially comprises a *trajectory predictor* that generates trajectories fitting the semantic description. This model alleviates the need for attaching a compact symbolic equation, and employs so-called "motifs" to describe trajectories, while remaining interpretable.

3. Through a set of mostly 1D experiments, including a pharmacokinetic model, the authors demonstrate that the proposed semantic ODE offers improved performance, interpretability, and robustness to noise compared to traditional models like SINDy.

### Strengths
The paper puts forth a scheme that moves away from the two-step modeling process of equation discovery and analysis, proposing instead that the semantic (behavioral) representation of a system can be derived directly from data, which in essence renders it closer to a solution discovery (as opposed to) equation discovery scheme. The concept of focusing on semantic rather than syntactic representation is original, as it allows modelers to interact with and interpret the behavior of systems without delving into complex symbolic mathematics. The originality here lies in both the reframing of the problem and the technical solution that bypasses the need for closed-form equations.

The paper demonstrates a clear and well presented theoretical development and practical implementation. Key symbols are defined in a notation table and important terms such as semantic representation, syntactic representation, and direct semantic modeling are well-defined, with illustrative examples and figures that clarify the difference between traditional ODE modeling and the proposed approach. The evaluation experiments are cover a range of dynamical systems (albeit low dimensional), including pharmacokinetic models, systems with delay differential equations, and integro-differential equations. The authors further validate the practical usability of Semantic ODE, with case studies and error analyses that underscore its flexibility, robustness, and potential for adaptation. 

The potential significance of this paper is substantial. By removing the reliance on closed-form equations and focusing on the semantic representation of system behaviors, the proposed method has applications across multiple domains, where dynamical systems modeling is essential. Additionally, the demonstrated robustness to noise and the flexibility of Semantic ODE to adapt to various types of differential equations indicate that this method could be robust, at least for the type of low dimensional problems that are here treated.

### Weaknesses
Despite the interesting idea, which draws some ties to a (flexible) curve fitting approach, certain weaknesses are identified as follows:

1. **Limitations Due to Motif-Based Semantic Representation**: While the paper argues that semantic modeling offers flexibility over traditional ODE discovery methods, the reliance on a predefined set of motifs to construct semantic representations introduces notable constraints. The specific motifs used limit the types of trajectories that can be effectively modeled, potentially narrowing the applicability of the method to systems with well-defined, predictable patterns. This approach risks excluding complex or novel trajectory shapes that fall outside the pre-selected motif set, thereby introducing a form of inductive bias that contradicts the method’s stated goal of flexibility. The authors do not provide a clear mechanism for expanding the motif set, or for automatically adapting it to new data, which is a significant limitation.

2. **Scalability and Extension to Higher Dimensions**: The current implementation focuses exclusively on one-dimensional systems, and while the authors mention potential future work on extending to higher-dimensional systems, they do not provide concrete strategies for achieving this. The direct semantic modeling approach, as presented, lacks a clear path for scaling motifs and trajectory predictions in multiple dimensions, which is crucial for broadening applicability in fields like biology, physics, and engineering where systems often involve multiple interacting variables. The paper lacks discussion on how the motif-based approach would handle the combinatorial explosion of possible interactions between dimensions, and how the semantic representation would scale with increasing dimensionality.

3. **Evaluation Against More Complex Baselines**: While the authors compare Semantic ODE to methods like SINDy, the experiments could be strengthened by benchmarking against more advanced and recent models in dynamical system solution discovery. Specifically, neural ODEs (e.g., Chen et al., 2018) and hybrid models that combine symbolic and neural approaches (like symbolic regression combined with neural networks) could serve as competitive baselines, as these methods have demonstrated flexibility and scalability, even in higher dimensions.  Do take note of the fact that such schemes as well, e.g. Neural ODEs, are linked to interpretability due to their ties to known dynamical system forms (e.g. state-state ODE formulation)

4. **Conceptual Contribution**: At the end of the day, it is not so clear why using predefined motifs is really different to assumptions of classes of solutions (as SINDy does) that sever as a bases to define convexity or concavity (which is really what the motifs do). One should also keep in mind that equations discovery is not always a necessary step. It is, however, a very useful step for understanding the type of physics that is underlying the problem. How does the proposed scheme offer the same granularity of information?

5. **Robustness to Unpredictable System Behaviors**: While the authors demonstrate that Semantic ODE is robust to noise, they do not address its performance in systems with unpredictable or highly chaotic behaviors. Since the semantic model relies on motif sequences, unpredictable behaviors could challenge the motif-based representation and disrupt accurate prediction or interpretation. Why not try this for example on nonlinear systems, such as the Duffing oscillator.

### Questions
It would be helpful if the authors reply to the following questions, which are linked to the previously identified weaknesses.

1. How flexible is the proposed motif-based representation in accommodating unforeseen trajectory shapes or behaviors? What kind of motifs would the authors suggest adding if new trajectory patterns arise that fall outside the current motif set?

2. Extending to higher-dimensional systems appears non-trivial within the current approach. Do the authors have any specific strategies or theoretical insights on how they might define and handle multi-dimensional semantic representations and motifs?

3. Why did the authors choose not to include comparisons with neural ODEs or hybrid methods that combine neural networks with symbolic regression, which have become prominent in modeling complex systems? Could these methods offer competitive advantages in interpretability or performance?

4. Do the authors believe that the proposed scheme offers the same granularity of information as i) equation discovery scheme and ii) solution discovery schemes making use of specific analytical functions? If so, in what sense?

4. Since the model relies on motifs for capturing trajectory shapes, how would it perform in the presence of chaotic or unpredictable system dynamics? Have the authors tested the model’s performance on chaotic systems, and if so, what were the results?
If possible, testing on a few chaotic systems or adding a discussion on expected limitations in handling chaotic behaviors could clarify the approach’s robustness and generalizability. If chaotic dynamics prove problematic, the authors could suggest potential modifications for better handling non-smooth or irregular trajectories.

5. What specific adjustments or extensions do the authors envision to broaden the adoption of Semantic ODE? Are there plans for enhancing the method to accommodate periodic or oscillatory behaviors that cannot be fully captured within finite compositions?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work compares syntactic and semantic representations of ordinary differential equations. In the second representation, the authors introduce direct semantic modeling via predefined bounded, unbounded, and horizontal asymptote dynamic motifs. This data-driven method is demonstrated through a one-dimensional ordinary differential equation. A semantic predictor is trained via a classification-base composition predictor and a properties prediction via a set of univariate functions, and fed into a trajectory predictor, which outperforms the traditional two-step process of equation discovery and analysis in terms of prior knowledge injection, model editing, feedback mechanism, and noise resistance. The syntactic inductive bias due to the analytic and human-understandable nature of equations can be mitigated and the semantic inductive bias can be cured by editing the model.

### Strengths
Compared to the two-step modeling approach exemplified by recently developed equation discovery models, the current work reports a data-driven model where the one-dimensional ordinary differential equation is segmented via transition points, and fitted by semantic motifs following the idea originally proposed in Kacprzyk 2023. The so-called direct semantic modeling approach allows more complexities beyond the analytical models and can integrate empirical knowledge via model editing. The definition of the problem and solution properties including the features of dynamic motifs are well formulated. Although the logic, workflow, and performance of the semantic predictor is demonstrated by using a one-dimensional model, the idea extends to higher dimensions.

### Weaknesses
Although in the discussion and appendix G.2, the authors proposed a roadmap for high-dimensional applications of the current model. However, there needs some elaborated discussion on the computational complexity and cost to achieve that. Even for the comparison made with the two-step model in the main text, the computational costs especially in problems with rising complexities (e.g. singularities) are not discussed.
The caption of Figure 1 is too brief, which makes the reading below very difficult (actually all figure captions are brief). The writing could be improved, for example, in lines 257-258, t_{i} and x(t_{i}) are not defined in the previous definition of p_{x}. Some content such as Fig. 10 may need to be moved to the main text since this is the key innovation in the current work. Fig. 7 may need to be merged into Fig. 6 for a better illustration of the improvement.

### Questions
How to technically treat singular points in a solution via the discrete representation since the determination of the positions of these points depend on the numerical grids? Does this process limit the model performance for solutions with a high density of singular points or short-wavelength features?

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
This paper proposes a direct semantic modeling method, which is fundamentally different from the traditional two-step modeling, which first discovers the symbolic form of ODEs. This approach is evaluated through extensive experiments.

### Strengths
This algorithm is completely new and different from the previous works. The authors provide detailed definitions of many new concepts and provide many analyses of whether they are well-defined or not. With experiments on different tasks and equations, results show that this algorithm can outperform previous algorithms in many ways.

### Weaknesses
1. Note the capitalization of the title.
2. Except for the traditional two-step modeling methods, there are also direct modeling methods for ODE trajectory simulation, like FNO, DeepONet, and many others. Considering the comparisons between them and Semantic ODE will be meaningful.
3. This algorithm is quite novel in that it only provides semantics rather than closed-form expressions, but can you analyze more about what kinds of downstream tasks it has?
4. l86, l475: Lack of a period at the end of the title.
5.1210: (denoted $c x$)

### Questions
1. How to ensure that the training subset of $F_{prop}$, which coresponds to one composition, have enough data? lf the dataset is divided into many subsets because of maybe many different intervals or different motifs, can $F fpropl$ be trained well with small datasets?
2. Do different $F {propl$s of different compositions share weights? Or do you need to train as many $F fpropl$s as the compositions?
3. I wonder if training with $F^0_{traj}$ but inference with $F^1_{traj}$ will introduce misalignment and error of the output.

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose direct semantic modeling of low-dimensional dynamical systems, which shifts away from the traditional two-step pipeline composed of first discovering a closed-form equation and then analyzing it.  The framework allows the incorporation of intuitive inductive biases into the optimization algorithm and the editing of the model’s behavior directly from data. The effectiveness of this framework is validated by extensive experiments including the logistic growth model, systems governed by a general differential equation, pharmacokinetic model, delay differential equation, and the integro-differential equation.

### Strengths
1. A novel approach, called direct semantic modeling, is proposed to learn the semantic representation of the dynamical system directly from data, eliminating the need for post-mathematical analysis.

2. The method operates directly on the semantic representation, enables intuitive adjustments, and seamlessly incorporates constraints that mirror the system’s operational behavior, which enhances the modeling flexibility and boosts performance, as it bypasses the need for a concise closed-form equation.

### Weaknesses
1. Compared to methods that rely on closed-form solutions, the interpretability and generalizability of direct semantic modeling approaches appear to be less apparent. As the author mentioned in the main text: " The primary objective of discovering a closed-form ODE, as opposed to using a black-box model, is to have a model representation that can be analyzed by humans to understand its behavior. Such understanding is necessary to ensure that the model behaves as expected.". The lack of explicit mathematical equations makes it difficult to analyze the system's behavior in terms of stability, sensitivity to parameters, and long-term dynamics, which are often readily available from closed-form solutions. Furthermore, the generalization capabilities of the semantic model are not well-defined, as it is unclear how the learned semantic representation would extrapolate to unseen data distributions or different system parameters, unlike the explicit functional forms of ODEs which can be analyzed for their behavior under various conditions.

2. The author has showcased the method’s efficacy through a variety of examples of 1D ODE, such as the logistic growth model, systems governed by a general differential equation, pharmacokinetic model, delay differential equation, and the integro-differential equation, which is commendable. However, the lack of demonstration of more complex data such as experimental data with unknown dynamical equations may diminish its appeal to a broader audience and contribution. The current examples are all based on relatively simple, well-understood systems. The absence of validation on real-world experimental data, which often involves noise, measurement errors, and more complex underlying dynamics, raises concerns about the practical applicability of the proposed method. It remains unclear how the method would perform when faced with the challenges of real-world data.

3. Identifying transition points (critical points) in dynamical systems that exhibit bifurcation behavior is inherently challenging, which may constrain the application of the framework to such systems, as their semantic representations tend to be more complex. The method's ability to capture the qualitative changes in system behavior near bifurcation points is not demonstrated. The semantic representation may not be sensitive enough to capture the subtle changes in dynamics that occur during bifurcations, which are crucial for understanding the system's behavior under different parameter regimes. The lack of a clear mechanism for identifying and analyzing these critical points limits the applicability of the framework to systems exhibiting complex behavior.

### Questions
1. Please elaborate on the advantages and disadvantages of direct semantic modeling compared to closed-form solutions in terms of model interpretability and generalizability.

2. If possible, please demonstrate the model’s effectiveness on more complex data, such as the semantic representation learning and prediction of time series in experiments.

3. How to efficiently identify bifurcation points, perform semantic modeling, and predict bifurcation behavior within dynamical systems using this framework when bifurcation behavior is present？

4. If possible, the author could include a discussion on handling partial differential equations with this framework, noting that in addition to initial value problems, there are also boundary value problems.

5. By the way, there are some minor typing mistakes in the article. On the second page, the differential operator symbol ‘d’ should be set in upright type.

### Soundness
3

### Presentation
3

### Contribution
2
