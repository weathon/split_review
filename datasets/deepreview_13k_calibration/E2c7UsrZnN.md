# Spectral Operator Methods for Learning Coherent Temporal Representations in Cellular Signaling Dynamics

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 3, 5

## Abstract
We present a novel operator-based framework for learning coherent temporal representations of cellular dynamics from live-cell imaging data. Recognizing the inherent stochasticity and measurement limitations in biological systems, our approach shifts the focus from predicting exact trajectories to characterizing key dynamical properties that shape cellular behaviors at the population level. By leveraging spectral analysis of the Koopman operator and smoothing via Markov semigroups of kernel integral operators, we identify near-resonant patterns and transient coherent structures that persist across different experimental conditions. This methodology effectively captures fundamental dynamics, providing insights into mechanisms of heterogeneous cell responses without the need to model precise transformation laws. We demonstrate the efficacy of our framework on a dataset of retinal pigment epithelial cells with an inducible oncogene, revealing conserved dynamical patterns across varying levels of ERK inhibition. Our work offers interpretable learned representations, even with limited and noisy single-cell-resolved recordings, advancing machine learning for dynamical systems and opening new avenues for understanding and predicting cellular behavior in response to external stimuli.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors describe a dataset of cellular activity, and a spectral method for estimating its properties.  They then demonstrate the application of this spectral method on this dataset.

### Strengths
Using cool spectral (and other) estimators on dynamical systems is a timely and important topic, and more work on this topic is desirable, since many datasets have these properties, and the standard AI toolkit is far less well-developed on this.  Thus, novel methods development are welcome.

### Weaknesses
The one biggest weakness that I see is that this method is not quantitatively compared to anything.   Neither is it shown to "work" on simulated data, nor on benchmark data, nor in theory.  Here, I am open to "work" being defined in many ways, including improved accuracy, timing, interpretability, or even elegance.  But I see literally zero numerical or analytic comparisons to any other method.  Thus, I have no idea whether this is the most valuable advance in modeling dynamics since Kalman, or relatively useless, because other things work just as well.

Within the first few sentences, there were things I did not know/understand.  Why is "low molecule copy number" a problem? What is a "Koopman Operator".  "Regulon"? "Isogenic"? Please introduce any technical concepts that are not textbook "AI", so the reader can follow more easily. This includes " smoothing via Markov semigroups of kernel integral operators", for example.  

line 60: "low in dimensionality, posing significant challenges for analysis."  Why does low-dimensionality pose a challenge?

I don't really understand what is new.  Are the methods new, or just a new application of standard stuff?  4  pages are devoted to explaining them, and they are complicated.

How is this stuff related to functional PCA, which is a fairly well established approach to modeling dynamics at scale.  It seems highly related.  I see no discussion of how other approaches might be able to solve this problem.  I have a paper on something similar, https://www.sciencedirect.com/science/article/pii/S0167865516303671, which seems like maybe it would be applicable? If fPCA and RR-System Identification are not applicable to this problem, I'd want to understand why not.  If so, I'd want to see benchmarks comparing this to something else.

### Questions
- Within the first few sentences, there were things I did not know/understand.  Why is "low molecule copy number" a problem? What is a "Koopman Operator".  "Regulon"? "Isogenic"? Please introduce any technical concepts that are not textbook "AI", so the reader can follow more easily. This includes " smoothing via Markov semigroups of kernel integral operators", for example.  

- line 60: "low in dimensionality, posing significant challenges for analysis."  Why does low-dimensionality pose a challenge?

- I don't really understand what is new.  Are the methods new, or just a new application of standard stuff?  4  pages are devoted to explaining them, and they are complicated.

- How is this stuff related to functional PCA, which is a fairly well established approach to modeling dynamics at scale.  It seems highly related.  I see no discussion of how other approaches might be able to solve this problem.  I have a paper on something similar, https://www.sciencedirect.com/science/article/pii/S0167865516303671, which seems like maybe it would be applicable? If fPCA and RR-System Identification are not applicable to this problem, I'd want to understand why not.  If so, I'd want to see benchmarks comparing this to something else.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces a spectral operator-based framework applicable for learning cellular from live-cell imaging. By characterizing key properties of the dynamics that shape cellular behaviors at the population level the authors overcome challenges posed by this task. The approach uses the Koopman operator and Markov smoothing, providing biologically interpretable representations which can be used to identify properties of the system’s dynamics across varying external conditions. To demonstrate its biological relevance, the framework is applied to live-cell imaging data from retinal pigment epithelial (RPE) cells to study the dynamics in response to perturbations.

### Strengths
- *Originality*: This work presents a novel approach, using the established Koopman operator approach to extract interpretable representation of live-cell imaging data . Such representations can be valuable to uncover the underlying biological mechanisms captured in live-cell datasets. 
- *Quality & clarity*: The paper is provides a thorough theoretical background of the suggested framework and experimental data setting. 
- *Significance**: As motivated in the text, understanding the dynamics of cellular behavior is a core and challenging task; recovering decision making mechanisms in response to perturbations. In applying the approach on real world data the authors demonstrate its applicability and relevance for biological discovery.

### Weaknesses
While the presented framework seems promising for biological discovery this submission showcases preliminary work and lacks crucial components:
- *Contextualization to prior work*: Alongside the challenges in analyzing live-cell data, covered in the introduction, it is valuable to include an elaboration on existing approaches. Given that such is missing, it is challenging to accurately assess the contribution of this work. 
- *Implementation details*: While a thorough theoretical description is presented, an implementation or pseudocode is missing, and is valuable for readers wishing to use the methods. Next, the authors briefly relate to the "Computational considerations"; claiming that the approach can handle large datasets efficiently. This claim is very vague and it is hard to judge the practical applicability of the framework. 
- *Experimental results*: The actual analysis presented is very limited. Biological interpretability boils down to the analysis of two Koopman modes, and the reconstruction/prediction performance are only assessed visually (at poor resolution). Moreover, following the contextualization to prior work, reconstruction/prediction performance is not compared to alternative approaches.

### Questions
Following the weaknesses above could the authors relate to the following: \
(1) include a "related work section". This section should discuss existing approaches for analyzing live-cell imaging data, and explicitly state how the present3ed method compares to or improves upon these approaches. This would help grasp the novelty and significance of the proposed framework.; \
(2) provide an implementation/pseudocode; \
(3) present an efficiency analysis quantifying the statement "This approach allows us to handle large datasets efficiently" (Lines 341-342) \
(4) extend the experimental analysis: \
(4.a) provide additional biological insights (on the studied/additional data); namely, presenting a more extensive downstream analysis of the Koopman modes demonstrating their potential for dynamics understanding. \
(4.b) assess the prediction performance qualitatively and compare it to existing baselines. \
(4.c) *minor* improve the figures quality.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The manuscript ‘SPECTRAL OPERATOR METHODS FOR LEARNING COHERENT TEMPORAL REPRESENTATIONS IN CELLULAR SIGNALING DYNAMICS’ presents a method based on spectral analysis of the Koopman operator, for learning representations of cellular dynamics (with a focus on response to perturbations) based on live-cell imaging, and specifically, learn dynamical properties, or features, instead of exact trajectories. The claim is that avoiding learning specific trajectories, as is the common approach, and instead going towards more general dynamical properties of these trajectories, can allow learning interpretable, robust representations for noisy data such as single-cell resolved datasets. The authors demonstrate their method by identifying conserved dynamical patterns in a dataset of retinal pigment epithelial cells with an inducible oncogene. Specifically, the respective experiments capture the dynamics of ERK activity and proliferation given varying levels of ERK inhibition, and the authors claim that while learning exact trajectories is infeasible in this scenario, they are able to capture conserved temporal patterns across different inhibition levels.

### Strengths
- The idea to focus on predictions of characteristics or features of dynamical trajectories and not the dynamical trajectories themselves, is well grounded and timely for the type of biological data that the authors focus on.
- The operator-based dynamics framework proposed in this work is mathematically sound and conceptually compatible with the greater task at hand.
- The live cell imaging datasets that the authors demonstrate their approach over provide an interesting and challenging setting.

### Weaknesses
 - Some of the statements regarding the analysis of the live cell imaging data seem to be not supported properly (see the ‘Questions’ section below).
- Some analyses need to be extended to the entire dataset, and not made only over a single sample (see ‘Questions’ below).
- There is no limitations section or discussion of disadvantages/limitations of the approaches.
- There are no comparisons to alternative existing approaches for the analysis of such data.



### Questions
Comments:

- In the introduction, there is the sentence ‘Given these challenges, directly learning the transformation laws governing cellular dynamics is often impractical’, it could be useful to cover a few of the recent efforts in that direction.
- ‘Moreover, smoothing via Markov semigroups of kernel integral operators allows us to capture the stochastic nature of cellular processes in a tractable way, aligning with the idea that noise plays a functional role in cellular decision-making.’ - the second part needs explanation, it’s not clear how it follows the first part.
- The top panels of Fig 1 need some labels.
- The analysis of the Koopman modes, presented in Fig. 2b, should be better explained in the text and the corresponding statements should be better validated. For example, can you support your statement that the shift in the first mode reflects inhibition of ERK activity? Or why it reflects ‘a probabilistic shift’? Or what is the significance of the oscillatory behavior of the second mode? Can you support your hypothesis that it is related to the cell cycle for example? (and if that’s the case, then how is this ‘intrinsic cyclical dynamics within the ERK signaling network’?)
- Figure 3 is missing a statistical analysis over all cell trajectories, not just a visualizing of a single (“cherry-picked”?) cell.
- What is the rationale behind generalizing to unseen data that is under a different biological setting? Why do you expect good generalization in that case at all? This needs to be better explained. 
- Discussion of limitations of the approach should be added.
- It seems that the conclusions throughout the paper should be phrased more modestly given the limited extent of analysis on real biological data.
- ‘Compared to approaches using functional data analysis or deep learning architectures, our framework offers significant advantages. It provides interpretable representations through Koopman eigenfunctions, corresponding to meaningful temporal patterns in the data, unlike black-box models.’ - But what are the potential disadvantages?

Minor:
- ‘aligning with the idea’ - typo?
- ‘coherent temporal patterns’ - not defined
- The resolution/quality of some of the figures/panels should be improved

### Soundness
2

### Presentation
3

### Contribution
2
