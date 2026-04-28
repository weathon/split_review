# Pushing Boundaries: Mixup's Influence on Neural Collapse

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Mixup is a data augmentation strategy that employs convex combinations of training instances and their respective labels to augment the robustness and calibration of deep neural networks. Despite its widespread adoption, the nuanced mechanisms that underpin its success are not entirely understood. The observed phenomenon of Neural Collapse, where the last-layer activations and classifier of deep networks converge to a simplex equiangular tight frame (ETF), provides a compelling motivation to explore whether mixup induces alternative geometric configurations and whether those could explain its success. In this study, we delve into the last-layer activations of training data for deep networks subjected to mixup, aiming to uncover insights into its operational efficacy. Our investigation (\href{https://colab.research.google. In this configuration, activations from mixed-up examples of identical classes align with the classifier, while those from different classes delineate channels along the decision boundary. Moreover, activations in earlier layers exhibit patterns, as if trained with manifold mixup. These findings are unexpected, as mixed-up features are not simple convex combinations of feature class means (as one might get, for example, by training mixup with the mean squared error loss). By analyzing this distinctive geometric configuration, we elucidate the mechanisms by which mixup enhances model calibration. To further validate our empirical observations, we conduct a theoretical analysis under the assumption of an unconstrained features model, utilizing the mixup loss. Through this, we characterize and derive the optimal last-layer features under the assumption that the classifier forms a simplex ETF.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work explores the phenomenon of neural collapse for mix-up training strategy. Specifically, the authors show that mixup’s last-layer activations will converge to a distinctive configuration. Extensive visualization results are illustrated to demonstrate the conclusion.

### Strengths
1.	Rich visualization results verify the authors’ points.

### Weaknesses
1.	I am afraid that the contribution of this method is limited. The authors simply show that mixup training strategy will help mixup’s last-layer activations converge to a distinctive configuration. However, we usually more care about how to set a proper mixup rate $\lambda$ and which samples should we mixup. The paper does not delve into the practical implications of this observed convergence, such as how this specific configuration can be leveraged to improve performance or robustness. It remains unclear if this distinctive configuration offers any tangible benefit beyond being an interesting observation. The analysis lacks a clear connection to actionable insights for practitioners using mixup, focusing more on the 'what' rather than the 'how' or 'why'.

### Questions
Please see the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The study utilizes analytical methods from the Unconstrained Features Model (UFM) and Layer-Peeled Model (LPM) related to the Neural Collapse (NC) phenomenon to examine the mixup data augmentation technique. The paper provides an analytical solution illustrating feature alignment with class prototypes during same-class mixup and channel delineation along the decision boundary for different-class mixup. Empirical evidence is presented to support these analytical findings.

### Strengths
The strengths of the paper are evident, particularly in the analytical exploration of the Unconstrained Features Model's (UFM) dependency on the mixup technique. This analysis deepens the understanding of a standard practice and provides empirical confirmation of expected behaviors. The analytical depth of the study stands out as a significant contribution. Additionally, the detailed examination of the feature density for λ=0.5 adds a noteworthy dimension to the research.

### Weaknesses
- The organization of the paper could benefit from a more conventional structure. The introduction figures and the placement of experimental results in Section 2 present challenges to readability and could be restructured for clarity.

- A clearer presentation of the problem's structure, particularly how it has been addressed numerically, would enhance the reader's comprehension of the methodology and findings.

- While the analytical proof is a notable element of the paper, the practical significance of its findings could be better articulated to highlight their impact and possibly extend the manuscript's reach to a broader audience.

- The rationale for projecting features into 2D, as depicted in the introductory figure, is not immediately clear and warrants further explanation. Given the dimension-specific uniqueness of the regular d-Simplex ETF, further details on the projection process would be beneficial. It should be clarified whether the projection includes all classes or if any are excluded, and if so, whether this exclusion is systematic or random. Employing a pair plot or scatter plot matrix, as referenced in [1], may provide a more conventional representation of the multidimensional data and ensure clarity regarding the inclusion of all classes. Given that datasets such as CIFAR10 and FashionMNIST comprise 10 classes, they could be visualized directly without the need for projection.

- The part on 'amplification' related to decision boundaries would benefit from a more thorough explanation. This concept is central to the paper, and a detailed discussion is essential, extending beyond the brief description in Figure 4's caption. Providing clear evidence or a solid rationale for this phenomenon is crucial to enhance the paper's validity.To better understand the amplification effect, it may be helpful to initiate training with a regular d-simplex ETF that is fixed, as in [A] and [B]. By 'fixed,' it is meant that the parameters do not change during the training. This could provide clearer insights into the behavior of decision boundaries.

- Minor: Section 5.3 “additionally” seems to be a typo.

### Questions
Questions and weaknesses are grouped to provide a better understanding of the issues.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigated the neural collapse phenomenon in mixup training. Specifically, it conducted experiments to show for synthetic examples mixed from same classes, their last layer activations align with the classifier; for those mixed from different classes, their last layer activations cluster around the decision boundaries.

The paper also explained this phenomenon by studying a unconstrained feature model, showing that under certain assumptions on the classifier, the optimal last layer activations for same-classed mixed examples align with the classifier, while those for ddifferen-class imxedd examples are linear combinations of components of the classifier.

### Strengths
1. Conducted investigations of neural collapse in mixup scenario, which is not previously explored
2. Adequate experiments and clear visualizations of the results
3. Theoretical explanation of the observed phenomenons is provided and proved.

### Weaknesses
1. Poor layout of the text and figures. The figures don't align well with their appearances in the sections. 

2. The connection between neural collapse in mixup and the generalization and calibration improvement of mixup is not further investigated

3. In Figures 1, 2, 3, 5 and 7, although the literal descriptions in the captions are clear, but in the plots the gradient effects of the colors are not distinct. It hard to tell how the $\lambda$'s vary from the plots.

4. Also in these figures, both the same-class and the different-class activations with $\lambda=0.5$ use the color black. Again, though the plots are clearly described in words, the colorations may still bring misunderstandings.

5. How the activations are projected into 2D planes for visualization in the figures is not clearly explained. Particularly:
 a. Is it training data or test data that is used to generated these plots?
 b. In the caption of Figure 1, what does it mean by saying "project activations onto the classifier"? From my understanding of the initial observation of neural collapse, we just need to project the last layer activations and the components of the classifier onto a same low-dimension space. Is that correct? And if so is the projecting method in this paper different from that?
 c. How is the conclusion "last layer activations align with the classifier" justified from the figures? Or from other observations presented in this paper?

6. The theoretical explanation has made an assumption that the classifier is a simplex ETF. This would be a very strong assumption if further proof or demonstration of it is not provided. 

7. Also, the theoretical explanation only considers the last layer features and the training targets, but not the inputs. In mixup, sometimes the mixed training target of a mixed input may not in fact be the ground-truth target of the input. Consider a datasets with three clusters of points side by side, suppose the clusters on the two sides are class 1 and the cluster in the middle is class 2. It is possible that a point mixed from two points in class 1 fall into the cluster of class 2, in other words, this point may be labelled both class 1 or class 2. These two scenarios will result in different training target, which will then result in different optimal last layer features. However, the point can have only one possible last layer feature output in a single model. Does this contradict the theoretical explanations in this paper? Should this point be aligned with the classifier component corresponding to class 1 or that corresponding to class 2?

8. In section 4.4, I think the observations in this paper don't sufficiently corroborate the so mentioned linearity of representations, since this paper didn't investigate the representations in early or middle layers. If only based on the observations of this paper, one can also argue that the representations in all layers have linearity in mixup.

9. Overall I think, although the reported observations are new, they are nevertheless superficious and brief. In my opinion it's not much of surprise that same-class  mixed activations perform similarly to conventional neural collapse in ERM and that different-class mixed activations align with the decision boundaries, since different-class mixup induces linear combinations on the training targets while same-class mixup normally somehow performs similarly to conventional data augmentations. The effort the authors have put into the investigations is appreciated, but the presented results don't seem adequate to constitute a rich-content formal paper.

### Questions
1. In section 1.5, how do the authors justify if a traineed model shows "good generalization"? Is it based on some well defined metrics or solely based on intuition?

2. Figure 6, second row. The characteristics exhibit an interesting behavior, that they are low at the very beginning of the training processes, then increase, and then decrease again, and their final level may even be higher than their initial level. Can the authors give some explanations or intuitive insights of this trend?

3. Section 4.2. Again, how is the statement "... reaped the minimum benefits" is justified?

4. Section 4.2. "... potential correlation ...". Is there any further investigations into thie potential correlation? Or is there any intuitions reasons of it?

5. Section 4.2. What is channel collapse?

6. How do the observed phenomenons help explain mixup's working mechanism in improving generalization and calibration? In fact, I think the calibration performance is barely mentioned in the main context.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The study investigates the phenomenon of Neural Collapse within the mixup training regime. Theoretically, the research employs a modified unconstrained feature model, distinguishing features based on whether they originate from mixup samples of identical or distinct classes and characterize the geometric structure at convergence. The work also conducts experiments consisting of different network architectures and datasets to corroborate their findings.

### Strengths
1. The paper is clearly written and well-motivated, the topic covered in the paper is novel to the best of the review's knowledge.
2. The introduction of the modified unconstrained feature model is clear and the theoretical results in the paper are well discussed and easy to understand.

### Weaknesses
Despite stating the study aims to explore how the proven geometric configurations in the paper can shed light on the success of mixup, the current iteration of the paper falls short in this regard. Mixup is a well-established augmentation technique with a lot of empirical success (e.g., generalization, adversarial robustness mentioned in this work), but it's hard for the reviewer to establish the connections between these empirical successes and the theoretical results shown in the paper. The authors talk about the difference in test performance of FashionMNIST might be attributed to its inability to achieve the theoretical geometric structure. Yet, such results are not definitive on their own. Therefore, the reviewer believes the paper needs additional work to discuss its practical implications.

Minor:
Sections 1.2-1.5 could be placed before the figures on pages 2 and 3 for better clarity.

### Questions
1. Why do the authors keep the models in train mode when plotting? Does this make a difference in the results?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
