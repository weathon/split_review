# Beyond single neurons: population response geometry in digital twins of mouse visual cortex

- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 5, 8

## Abstract
Hierarchical visual processing  is essential for cognitive functions like object recognition and spatial localization. Traditional studies of the neural basis of these computations have focused on single-neuron activity, but recent advances in large-scale neural recordings emphasize the growing need to understand computations at the population level. Digital twins-computational models trained on neural data-have successfully replicated single-neuron behavior, but their effectiveness in capturing the joint activity of neurons remains unclear. In this study, we investigate how well digital twins describe population responses in  mouse visual cortex. We show that these models fail to accurately represent the geometry of  population activity, particularly its differentiability and how this geometry evolves across the visual hierarchy. To address this, we explore how dataset, network architecture, loss function, and training method affect the ability of digital twins to recapitulate population properties. We demonstrate that improving model alignment with experiments requires training strategies that enhance robustness and generalization, reflecting principles observed in biological systems. These findings underscore the need to evaluate digital twins from multiple perspectives, identify key areas for refinement, and establish a foundation for using these models to explore neural computations at the population level.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors demonstrate that a reasonably successful model of visual cortical neurons does not capture population metrics.  They show that measures of the population geometry and visual hierarchy fail on this model.  The eigenspectrum of the covariance matrix does not show scaling consistent with differentiability and the relative discriminability across areas does not match what is observed empirically.  The authors investigated various aspects of the model and of training to see what effect they had on these measurements.  These include selecting for reliability, choices of dataset, dataset augmentation, model architecture, and using a covariance-based loss function.  All of those failed to show different results for the population metrics.  The approach that did produce differentiable representations was adding dropout during training, which showed an exponent consistent with differentiability for sufficiently high dropout rates.  They claim that the models that show differentiability also show the appropriate hierarchical relationships for discriminability.

### Strengths
This paper is reasonably clear and well-written.  The question is a very important one as population level characteristics of neural activity are undoubtedly important for neural computation and models need to be able to capture it.  It is extremely important to point out that our current state-of-the-art models are not meeting this criteria and likewise important to address what aspects of training will correct this.  The authors tested a broad set of training procedures.

### Weaknesses
The authors did an excellent job of testing an array of procedures, but the results are still unfortunately limited by the number of models and data sets available for testing.  This is not terribly actionable, sadly, in a practical sense.

The authors wish to make a general claim about regularization, but only test dropout. It is unclear if the observed effects are specific to dropout or if other regularization techniques would yield similar results. The lack of exploration of other regularization methods limits the generality of the conclusions drawn about the role of regularization in achieving differentiable representations.

### Questions
Does this result hold for task-trained models as well?

Can you test other forms of regularization?  Do they have the same effect, or is dropout special?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The study examines how well digital twins, computational models trained on neural data, capture both single-neuron and population-level responses in the mouse visual cortex. While these models predict single-neuron activity accurately, they fail to replicate the complex geometry and hierarchical organization of population responses seen in biological data. Factors like dataset composition and network architecture didn't resolve these issues. Introducing regularization techniques like dropout improved the models' ability to create more accurate population representations but reduced single-neuron prediction accuracy. The study highlights the need to refine digital twins to better understand neural computations at a population level.

### Strengths
The paper tackles an important gap in computational neuroscience by focusing on the geometry of population-level neural responses in digital twins, not just single-neuron predictions. The study meticulously replicates key experimental findings and explores how factors like dataset variation, architectural changes, and training objectives impact model performance. Regularization techniques, especially dropout, are shown to improve the models' alignment with biological data. The paper is well-explained and accessible, providing valuable insights for both neuroscience and machine learning. By identifying the limits of current models, the research sets the stage for developing more accurate and biologically realistic models, emphasizing the need for principles like robustness and generalization in neural computation replication.

### Weaknesses
Despite improvements with regularization, the models still show quantitative differences from experimental data, especially in discriminability measures and visual area hierarchy, warranting a deeper analysis to uncover the causes. There's a trade-off where enhancing population-level representation reduces single-neuron prediction accuracy, raising practical concerns. The paper's focus on a shared-core architecture limits insights; exploring more varied architectures could better reflect the visual cortex's hierarchical nature. Additionally, the study relies on computational simulations, and direct physiological validation of these models would further substantiate the findings.

### Questions
Have the authors considered multi-objective optimization to balance single-neuron accuracy and population-level representation? Could adding biological features like spiking noise, synaptic dynamics, or neural variability improve the models' population properties? Have they explored area-specific modules or varied receptive field sizes to better capture hierarchical processing? Can they comment on the models' generalizability to different visual stimuli, given the issues with non-differentiable representations for gratings? Would using spiking neural network models help capture population response geometry and address trial-to-trial variability?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper argues that some digital twins (i.e., ANN models that predict single neuron activities well) fail to capture population level properties (specifically having to do with the representational geometry) of neural responses that have been previously observed in the mouse visual cortex. The primary issue is the fact that the population representations in the digital twins have a geometry that is non-differentiable, which suggests that small changes in inputs can lead to very large changes in the network's representation. The paper then shows that dropout regularization can go some way towards mitigating these kinds of discrepancies between the ANN's responses and those of the actual mouse brain.

### Strengths
Understanding how highly predictive ANN models of the brain can fail to capture certain properties of neural population responses that are functionally important is an important issue to address. This paper exposes some shortcomings of existing models, and gives a fairly straightforward way of mitigating some of those shortcomings, using dropout in the network. This is useful because it may lead to models that do a better job of accurately simulating brain responses.

### Weaknesses
The paper could be clearer in a lot of places, especially for readers who are not familiar with the model being used, as well as the background literature which the paper heavily draws upon.
- Although the model is described in the Appendix, it wasn't very clear (at least, not to me). There are a lot of different parts, and it was hard to see how they fit together. It might help to have a diagram illustrating the architecture and how everything fits together.

Although a lot of the background theory relating to the differentiability of neural representational geometry is presented in Stringer 2019, it would help readers if this paper were a bit more self contained, e.g. some intuitive explanation of why the cutoff for differentiability is 1 + 2/d would have been helpful to the uninitiated reader.

Training the model only on correlations between neurons resulted in a loss of single neuron predictivity, presumably because single neuron predictivity is no longer part of the optimization objective. I would have thought a natural thing to try would be to train the model on a combined objective that optimizes for both objectives at once, and see if that changes the results in any way.

The claim that the digital twins fail to capture the hierarchical relationships between areas seemed like an overstatement, since what is really shown here is that one aspect of hierarchical relationships was not captured, not that it doesn't capture any relevant aspects of the visual hierarchy.

### Questions
I was a bit confused at a high level as to how it is even possible for a digital twin to do a good job at predicting single neuron responses and yet still not capture population structure. Doesn't the population structure depend on the single neuron responses? How can you capture each individual neuron's activity with a high degree of accuracy and not get the population structure right?

Questions about the model:
- I was very surprised to read in the paper that the model does not have increasing receptive field sizes. Isn't that just a standard feature of a CNN?
- What is the intuition behind the formula for CC_max (where does this formula come from)?

### Soundness
3

### Presentation
2

### Contribution
3
