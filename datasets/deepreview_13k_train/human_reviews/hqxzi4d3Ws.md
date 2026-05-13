# Provably Noise-Resilient Training of Parameterized Quantum Circuits

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Advancements in quantum computing have spurred significant interest in harnessing its potential for speedups over classical systems. However, noise remains a major obstacle to achieving reliable quantum algorithms. In this work, we present a provably noise-resilient training theory and algorithm to enhance the robustness of parameterized quantum circuits. Our method, with a natural connection to Evolutionary Strategies, guarantees resilience to parameter noise with minimal adjustments to commonly used optimization algorithms. Our approach is function-agnostic and adaptable to various quantum circuits, successfully demonstrated in quantum phase classification and quantum state preparation tasks. By developing provably guaranteed learning theory with quantum circuits, our work opens new avenues for practical, robust applications of near-term quantum computers.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors develop a training method that guarantees resilience to parameter noise in quantum circuits for parameterized quantum circuit classifier. The authors give the theoretical guarantees and demonstrate with two experiments. The proposed method is closely linked to Evolutionary Strategies, which are a class of gradient-free optimizer. The framework also emphasizes interpretability by allowing researchers to analyze which parameters contribute most significantly to robustness after the optimization process.

### Strengths
1. The authors creatively combine concepts from classical robustness theory with quantum computing, offering a new perspective on how to handle parameter noise.

2. The authors give the theoretical foundation of the work.

3. The authors make a connection to Evolutionary Strategies, which makes achieve robustness certificates without the need for calculating expensive quantum gradients.

### Weaknesses
1. The presentation of the experiments makes it difficult to understand; the discussion does not refer to the experimental results but merely provides statements. It would be beneficial to add one or two paragraphs to discuss the experimental results. The connection between the discussions and the experimental results is not clear regarding variance-induced improvement and variance-indicated interpretability.

2. The authors conduct experiments primarily focused on phase classification and state preparation tasks. However, these may not fully represent the diverse range of applications of parameterized quantum circuits (PQC).

3. There is a lack of comparison to other methods. This can be improved by including experiments and discussion with quantum certified robustness methods as discussed in prior work, or even with standard quantum experiments using noise mitigation methods.

4. There is a lack of detailed descriptions of the experimental setup and hyperparameter sensitivity analysis. As one example, the authors mention two different variance regularizations but do not conduct any experiments to evaluate the effectiveness of these regularizations. This omission leaves readers uncertain about the impact and optimal choice of these regularizations.

5. Although the paper claims that their method provides insights into which parameters have larger robustness guarantees, it does not elaborate on how these insights can be practically utilized or interpreted by users. It would be beneficial to request specific examples from the authors that illustrate how these insights could be applied in practice. This would encourage them to provide more concrete information regarding the practical value of their method's interpretability.

6. Table 1 is hard to understand at first look, it might need better presentation.

### Questions
1. How does your method compare to prior work and the models with noise mitigation strategies in terms of performance metrics such as accuracy, robustness, and computational efficiency? Can you provide benchmarks against other state-of-the-art methods?

2. What is the sensitivity of your results to the choice of hyperparameters?

3. As circuit complexity increases, what are your thoughts on the scalability of your training method? Have you explored strategies to maintain efficiency with larger datasets or more complex quantum circuits?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper applied the smoothing technique in certified robustness of classical machine learning to a quantum parametrized classifier model. The results imply that simply adding a careful designed noise parameter to the parameter optimization can enhance and certify the robustness of a variational quantum algorithm. However, I find some major issues regarding both the theoretical and numerical results:

### Strengths
The paper offers a plug-in approach to certify robustness of a variational quantum algorithm.

### Weaknesses
The assumption made for robustness certification is not very practical. The paper assumes that noise can be modeled as perturbations to the variational parameters, which is a significant simplification of realistic noise models in quantum systems. This assumption neglects the complex, time-dependent, and often non-Markovian nature of quantum noise, such as decoherence and gate errors. The framework's applicability is therefore limited to scenarios where parameter noise dominates other noise sources, which is not generally the case in current quantum hardware. Furthermore, the paper does not adequately address how the magnitude of the noise parameter relates to realistic noise levels in quantum devices.

The numerics results are relatively weak. The experiments lack sufficient detail to reproduce the results, making it difficult to assess the validity of the claims. The paper does not specify the exact architecture of the Parametrized Quantum Circuit (PQC) used, including the number of layers, the types of gates, and the connectivity of the qubits. The size of the PQC parameters is also not mentioned, which is crucial for understanding the computational cost and scalability of the method. The amount of training data used is not clearly stated, making it hard to evaluate the generalization performance of the model. The additional computational cost of the certified approach compared to standard training is not quantified, which is essential for practical applications. The choice of the initial state as the ground state in the phase classification problem is not sufficiently justified, and it is unclear how this choice affects the results.

### Questions
1. How does the framework extend to the phase parameters in a quantum gate?
2. Theorem 3.1 states the certification of robustness with a high probability under the assumption of noise. I did not find the discussion about this ``high probability” in the manuscript. 
3. How does the shot limitation impact the certification? A theorem/lemma regarding to the statistic noise would be beneficial. 
4. It makes sense to indicate a more sensitive parameter under this scheme. However, the word  “interpretability” in Section 4.2.2 looks over claiming as it simply states about the “robustness” and looks like a repartition of the first point “shape” in the same subsection.
5. The numerical results are relatively weak. Many experiment details are missing. What is PQC model used in the experiment? What is size of the PQC parameters? How many training data used? What is the additional computation cost when using the certified approach? 
6. In the phase classical problem, why to choose the initial state as the ground state? 
7. As the authors agreed in the discussion of the limitation, the assumption of treating quantum noise as parameter perturbations is not realistic. Some potential applications will be in the quantum control rather than VQA or quantum machine learning.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a noise-resilient training theory and algorithm for parameterized quantum circuit (PQC) classifiers. The method guarantees resilience to parameter noise by integrating randomized smoothing techniques from classical machine learning. The authors establish a connection to evolutionary strategies for optimization and demonstrate the effectiveness of their approach on phase classification tasks. The paper also highlights the potential for interpretability insights into quantum models.

### Strengths
- For the specific task of parameterized quantum circuit classifiers (the model considered is indeed not the most general PQC classifier), this work makes an interesting attempt to develop a noise-resilient training theory.
- The paper is well written. 
- This work makes attempts to show detailed experiments on some tasks of practical interest.

### Weaknesses
 - The paper does not provide a clear and compelling justification for focusing on the PQC classifiers introduced in this paper, in particular given the current limitations in their trainability due to barren plateaus. The authors should address this concern and explain why their noise-resilient training approach is still relevant and important in light of these limitations. Specifically, the paper lacks a discussion on how the proposed method interacts with the optimization landscape of these PQCs, and whether the smoothing technique could inadvertently exacerbate the issue of vanishing gradients.
- The PQC classifiers considered in this paper are somehow limited, and it is not clear how they are useful for practice. It would be better to show that the PQC classifier formulation would be particularly useful, which would help clarify the real-world relevance of their work. The paper should provide a more detailed analysis of the specific advantages of their chosen PQC architecture over other potential quantum classifier models, especially in the context of practical applications and hardware constraints.
- The proposed method does not take into account the practical issue of measurement accuracy in quantum systems. Measurement errors can significantly impact the performance of quantum algorithms. The paper should include a discussion on how the proposed method would be affected by realistic measurement noise, and whether the robustness guarantees still hold under such conditions. A more detailed analysis of the interplay between parameter noise and measurement noise is needed.
- The numerical experiments presented in the paper may not be sufficiently convincing, as recent research (arXiv:2408.12739) has shown that Quantum Convolutional Neural Networks, which are used in the experiments, are effectively classically simulable. The authors should address this concern. The paper should provide a more detailed analysis of the computational resources required to simulate the experiments, and discuss the implications of the classical simulability for the practical relevance of the proposed method.
- The theoretical analysis in the paper appears to be mainly based on techniques directly adapted from classical methods. As a result, the novelty of the theoretical contributions may be limited, and the results may not be particularly surprising in the context of quantum machine learning. The paper should provide a more detailed discussion of the specific challenges and opportunities that arise when applying randomized smoothing to quantum systems, and how the proposed method addresses these issues.

### Questions
- Can the authors explicitly address how their approach relates to or mitigates the barren plateau problem? It would be helpful to understand if the proposed method has any inherent advantages in avoiding or reducing the impact of barren plateaus.
- Could the authors discuss the potential advantages of their Parameterized Quantum Circuit (PQC) classifier formulation compared to more general models? 
- Can the authors provide more insights into why the PQC classifier formulation considered in this work is important and practically useful? Elaborating on the practical significance and potential applications of the proposed approach would strengthen the contribution of the paper.
- How might the proposed method be extended to account for measurement errors? Addressing the robustness of the method to measurement errors would enhance the completeness of the work.
- Can the authors explicitly discuss the implications of the cited classical methods in relation to their work? It would be valuable to understand how the proposed method might apply to other, non-classically simulable quantum models, or to explain why the approach is still valuable even for classically simulable models. This discussion would help contextualize the significance of the contribution within the broader landscape of quantum and classical methods.

### Soundness
2

### Presentation
2

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
This submission addresses the robustness of quantum machine learning models based on parametrized quantum circuits under perturbations of their parameters. The authors revisit the framework of certified robustness, and provide theory and an algorithm for training such parametrized circuits in a provably noise-resilient way. The authors phrase these results in the context of noisy quantum circuits, and explain that their framework can be easily used by practitioners, and that such noise-robustness guarantees can also provide insight in matters of interpretability.

### Strengths
Strengths:
Addresses an important issue: the negative effects of noise in parametrized quantum circuits.
Supports the claims in that indeed a training algorithm with robustness guarantees is provided.
Brings ideas from certified robustness to quantum machine learning, which had not been much looked at before.
Proposes a geometric picture to intuitively understand the core concepts of certified robustness.

The work is clearly presented, the analytic tools all look correct, and the numerical experiments are also clearly laid out.

### Weaknesses
I cannot recommend this submission be accepted for ICLR 2025 due to a lack of deeper and more significant contributions.

In particular:
1 The approach could be better motivated. The source of noise considered is one of the least detrimental ones in real quantum devices. Also, it is unclear how this paper is set apart from previous literature.

2 The theoretical contributions in this submission are limited to laying out existing framework, minimally adapting a well-known training algorithm, listing a few metrics, and proof-of-principle experiments.

3 The numerical experiments are not very convincing. First, the quantum systems studied are very small when compared to similar experiments in the literature in the last decade. Next, the trade-off between accuracy and robustness is barely recognizable in Figure 1, and completely absent in Figure 2, to the point that these plots are detrimental to the overall message of the paper. The rest of the plots (the comparison between area and semi-axis standard deviation) is very surprising, since when introducing the metrics, the authors already say “[the standard deviation] is likely not of particular note for any use…”. Following the geometric picture elaborated in Section 3.2., it should be clear that the area of an ellipsoid is closely related to the variance of its semi-axes. So, on the one hand, it is unclear why practitioners should be interested in this second analysis, and on the other hand the results follow almost directly from analytical geometry.

4 The choice of learning algorithm seems arbitrary. While it is true that evolutionary strategies have been used in the literature, it is unclear that they are preferable to gradient-based methods. The reference cited by the authors states that, in the worst-case, the complexity of evaluating gradients is linear in the complexity of evaluating the model times the number of parameters. Other references exist showing that this stops being true in specific cases of interest. And, even if it were true in general, evolutionary strategies are known to have much longer convergence times than gradient-based methods. The authors seem to ignore the fact that, even though computing each gradient iteration may take longer, this may be completely offset by the dramatically reduced number of iterations. This does not mean that focusing on evolutionary training algorithms is not well-justified, but the text is currently misleading in how uncommon an approach this is.

5 The authors mention that the proposed tool of certified robustness can also be used for parameters that are not optimized for. This makes a lot of sense. This further seems to highlight that this study is a convoluted spin of the simple message “take random perturbations of increasing size until the performance starts decreasing, independently for each parameter, and then report the size of the largest acceptable perturbation”. If this is accurate, this further highlights the lack of strength of the submission. If it is not accurate, it should be better clarified in the text.

### Questions
Questions and comments:
In the prior work section, the authors explain that the techniques of certified robustness and training of parametrized quantum circuits have been previously addressed and carry intrinsic interest. Still, as a reader, it seems that the presented techniques are a direct application of a previously-developed formalism. If this is not the case, the authors should explicitly delineate what are the novelties in Section 3.
The submission would be much more convincing if the authors had produced a general-case statement that further justifies why using this framework produces desirable results. Along the same lines, in Section 4.2.1. the authors open with “we desire to understand the best [robustness-accuracy] trade-off we can achieve”, and then proceed to perform limited numerical experiments, ignoring the question of best-possible trade-off.
The proposed approach is not compared to any other method. One would have expected to compare this “quantum-specific” tool to previously proposed “classical-general” tools applied to these quantum models.
The link to interpretability is rather weak. On the one hand, practitioners are most-likely aware of the relative relevance of each of their parameters. On the other hand, if the variance in the certified-robust parameter distribution is to be seriously considered as an interpretability method, then it should be properly benchmarked against other methods in the literature. Since the authors mention that this certified robustness can be linked to the sensitivity of the parameters, why did the authors not compare their results to standard sensitivity analysis, like using the Hessian or the Fisher information matrix?
In section 3.2. the volume of a high-dimensional ellipse is proposed as a metric for robustness. It is a well-known fact that the volume of a high-dimensional sphere vanishes asymptotically in the dimension of the ambient-space, so why would a metric based on this vanishing quantity be advantageous? This metric is introduced here, although later in the experiments different quantities are used, more closely-related to the volume of a high-dimensional prism than that of an ellipse. As a reader I found it very confusing why this metric was introduced, instead of the ones used in the experiments.
In section 4.4., the authors mention the potential users of their method, but they do not clarify who those users would be. This is again in relation to the choice of noise model. If the users ought to be researchers running these algorithms on hardware, the types of noise they are likely to encounter are not the ones captured in this study. If the users ought to be researchers performing simulations of quantum machine learning algorithms, then the inclusion of parameter noise becomes again less relevant. Who do the authors exactly envision as users of this method?

Feedback with the aim to improve the paper. These points are here to help, and not necessarily part of my decision assessment.
As a reader, several parts of the paper felt rushed and unpolished. The informal language in Sections 2. and 4.1. is distracting (subjective). There are a few grammar mistakes throughout the document. In Definition 3.2. the authors conclude with “for any noise perturbation delta from a certain distribution”, which makes no logical sense: it can either be “for all perturbations from a given domain”, or “with high probability over perturbations sampled from a given distribution”. The smoothed classifier as defined is a random variable, and it is never addressed whether or how to turn this random variable into a deterministic labeling function. In Section 3.3. the authors say “In general, what ES typically…”, which is logically incorrect: “in general” and “typically” are in contradiction. At the end of Section 3.4. the second regularization proposal ends with the inverse of sigma, where sigma is supposed to be a vector, so it is not clear what its inverse should be.
The authors invoke “noise resilience” in the title of the submission, referring to the uncontrollable effects that keep current hardware from being full-fledged quantum computers. Indeed, developing noise-resilient algorithms is an important task until we reach fault-tolerant quantum computers. That being said, the authors consider a single source of errors, and actually one of the least detrimental in real quantum devices: noise in the parameters. I would recommend the authors to either choose a more specific title, or to convincingly argue why parameter noise is important at present (notice that the goal of the field is to build noiseless quantum computers, so studying noise models must be justified from the point of view of real obstacles to that end).

### Soundness
3

### Presentation
2

### Contribution
1
