# Shifting the Paradigm: A Diffeomorphism Between Time Series Data Manifolds for Achieving Shift-Invariancy in Deep Learning

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Deep learning models often lack shift invariance, making them sensitive to input shifts that cause changes in output. While recent techniques seek to address this for images, our findings show that these approaches fail to provide shift-invariance in time series, where the data generation mechanism is more challenging due to the interaction of low and high frequencies. Worse, they also decrease performance across several tasks. In this paper, we propose a differentiable bijective function that maps samples from their high-dimensional data manifold to another manifold of the same dimension, without any dimensional reduction. Our approach guarantees that samples---when subjected to random shifts---are mapped to a unique point in the data manifold while preserving all task-relevant information without loss. We theoretically and empirically demonstrate that the proposed transformation guarantees shift-invariance in deep learning models without imposing any limits to the shift. Our experiments on five-time series tasks with state-of-the-art methods show that our proposed approach consistently improves the performance while enabling models to achieve complete shift-invariance without modifying or imposing restrictions on the model's topology. Source code: Double-blind.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper describes an approach to make neural network pipelines for time series shift invariant. The method is based on Fourier theory and follows a canonicalization approach, where the input signal is shifted by picking a reference frequency and its phase, then shifting the signal such that the phase of that reference frequency equals a target phase φ. The target phase φ is predicted using an invariant network that takes the power spectrum as input. The experiments show strong results across 5 different tasks.

### Strengths
* The empirical results are strong and comprehensive across multiple tasks
* The method has clear practical value for making neural networks more reliable for time series analysis
* The problem setting is highly relevant to real-world applications
* The proposed solution addresses an important gap in making neural networks for time series more robust

### Weaknesses
1. Clarity and Presentation Issues:
* Despite attempts to make concepts intuitive through figures and explanations, the paper raises more questions than it answers
* The theoretical framework around diffeomorphisms feels disconnected from the practical method
* Several key concepts and proofs need better explanation or justification
2. Missing Context:
* The paper lacks discussion of related canonicalization approaches, particularly work like Kaba et al. (2023) on "Equivariance with learned canonicalization functions"
* The relationship between the theoretical foundations (e.g., Proposition 2.1) and the practical method isn't clearly established

``Kaba, S. O., Mondal, A. K., Zhang, Y., Bengio, Y., & Ravanbakhsh, S. (2023, July). Equivariance with learned canonicalization functions. In International Conference on Machine Learning (pp. 15546-15566). PMLR.```

### Questions
This is a mix of comments and questions:

* At the beginning of the notations sections why write parenthesis around $\mathbf{x}$, i.e., why write $(\mathbf{x})$?
* Why is proposition 2.1 relevant. This is a well-known result, but I don't see the paper reflect back on the group structure? In essence, each $e^{j \omega t$ is an irreducible representation of $SO(2)$ and this explains the Fourier shift theorem. The text however, does not really connect prop 2.1. to the rest of the paper.
* I don't understand why fixing $\phi$ would not work. In principle that would make the entire pipeline shift invariant too right?
* The talk about diffeomorphisms is really unclear. What precisely is the diffeomorphism and between which spaces? It seems to be a diffeomorphism of the data-space onto itself, simply by a shift, but I might be misunderstanding something here.
* The last step of the proof of theorem 2.3 is unclear. The first equation of (6) shows that the difference between the two transformed shifted signals is not equal to 0 (but $[T_0/T \omage_0 - \omega]t'$). But then all of a sudden the second equation equates the two signals.
* It is unclear why a variance loss is necessary? More importantly, what is the random variable in this case. It seems like the output of the guidance function is a single angle, then what is there left to take a variance over? The text says "reduce variance in the angles" but the network only returns one angle, right?
* Fig 3 with the depiction of the "manifolds" in (b) is confusing. I still don't understand the manifold viewpoint.
* The text says "In other words, if we conceptualize the dataspace of samples as expanding with shift invariants", what does it mean to expand with shift invariants? And what does it mean "potential points where samples can be found".
* Regarding fully convolutional networks. What precisely is meant with this? I was assuming that this meant that no down-sampling is used, or at least that the output has the same resolution as the input. But then the guidance network does not take a spatial signal as input, but rather the power spectrum, so convolution does not make sense to me, but also even it would, if you return a single phase some sort of pooling or fully connected layer must have been used, right? And thus it cannot be an FCN. Could it be that fully connected is meant here?
* In the section time delay as adversary, what table is being discussed here? Please clarify this in text.
* "However, our results indicate that the model ... the model prediction jumps more than 100%" what does this mean? How can a model "jump" 100%?
* "One distinct results ... increases by 7-8%", relative to what?
* I don't understand why fixing $\phi$ does not work. Theoretically seen, doesn't fixing $\phi$ also lead to a fully invariant pipeline? But in table 5 I see that the first row gives poor performance, why would that be?
* Equation (9) is, similar to my previous question about variance, puzzling to me. Firstly, what is the random variable the variance is taken over, and secondly why would this even work at all? First you minimize variance, now you maximize variance, and the results are barely different. I would expect one of the two to be extremely unstable.
* "Importantly, adding the guidance network does not bring any additional parameters", this is not true. $f_{G_\theta}$ has parameters, right?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a method to modify time-series data samples in such a way to make neural network training shift-invariant. Their method involves mapping the signal into the frequency domain via the Fourier transform, applying (learned) phase angle transformations to each of the frequency components in the frequency domain, and then mapping back into the time domain via the inverse Fourier transform. They compare results on mostly health-related time-series datasets and compare to alternative methods of promoting shift-invariance such as anti-aliasing methods which use LPFs to remove high-frequency aliasing effects, data augmentation methods, and more. The authors find on average that their method results in improved accuracy and consistency of models on time-series data where shift invariance is desired.

### Strengths
The results seem to indicate on average that the models trained in this manner achieve shift invariance (through shift consistency) and better results than existing methods. Theoretical results support that you can achieve a bijective mapping for samples that promotes shift invariance.

### Weaknesses
I am admittedly not the most knowledgeable in this area of research, but the method sounds to me like a form of data augmentation that operates in a model-driven manner given that there is a guidance network that is optimized which selects the phase angle to use in the augmentation? Perhaps it would be worthwhile to compare this method to some model-driven / data-driven data augmentation processes? 

Some of the results indicate improvement when averaged over multiple runs (how many runs are these results averaged over? I seem to have missed this information in the manuscript). But in some of those cases based on the standard deviations computed there is a fair overlap between prior methods and your method, it’s possible that the advantage in those cases is not so clear when there is a large variance over the accuracy of different runs.

I could imagine there are cases where the computational overhead of training two networks (classifier + guidance network) to get a small increase in accuracy may not be desirable, but as far as I can tell the shift consistency being 100% using this method would seem to be a benefit to any use-case that requires shift invariant predictors, as compared to whichever existing methods are reported in this paper.

I assume that the guidance network, after training, is fixed meaning that the angle for each sample is fixed? How can I interpret the value of the angle that the guidance network converges to for a given sample? Does it say something about the data itself? How robust is this technique to alternative ways of choosing the desired angle, perhaps via random angle methods (could be an interesting baseline to report) or some other method that doesn’t involve optimization of a guidance network?

### Questions
If I understand correctly the model is chosen based on the best validation loss, is the reported number based on that validation loss or a held-out test set evaluated by the model whose parameters come from that point where there is the best validation loss during training?

Is it possible that the guidance network is overfitting to the train set in some way? Specifically, if the numbers reported are when you pick the networks that achieve the best validation performance and the reported numbers are not from a held-out test set then there might be some overfitting reported, although the shift consistency metric does seem to indicate that the models are learning shift-invariant estimators.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a diffeomorphism that transforms observations from one high-dimensional data manifold to another of the same dimensionality. The goal is to quotient with respect to random shifts. The method ensures that each sample is mapped to a unique point on the data manifold regardless of its random shift. Keeping the same dimension in the representation space is suppose to retain all task-relevant information without any loss.
A theoretical analysis is performed as well as intensive experimental demonstrations.

### Strengths
This paper is well motivated and with both theoretical analysis and deep experimental studies and comparisons.
The modeling is interesting and remarks on the performances are relevant.

### Weaknesses
The model requires that the data lives in a Manifold. This is a strong assumption (although good one to start with) which sounds necessary as it is quotiented by the group of shifts.

### Questions
Data do not necessaraly lives in Manifold, if it does not (no local representation with metrics), would that be an issue?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel method to achieve shift-invariance in deep learning models for time series data. Traditional methods often lack robustness to shifts, which can lead to highly inconsistent performance in tasks such as heart rate prediction, especially when requiring both low- and high-frequency information. The authors propose a differentiable bijective transformation that maps shifted samples to a unique point in a high-dimensional manifold, ensuring shift-invariance without dimensional reduction or architectural changes. This approach is tested across various time series tasks, where it demonstrates improved performance and consistency compared to existing techniques.

### Strengths
The paper is well-written, and the figures all look aesthetically nice and neat.
The medical/empirical motivation is clearly laid out, with good intuitive examples of why this is an important and challenging problem.
The empirical results appropriately cover a range of real-world empirical datasets with a range of important tasks.

### Weaknesses
- The authors present the proposed transformation as a novel aspect of the method, yet phase-shifting is a well-known approach in signal processing. The architectural novelty here lies primarily in the integration of the guidance network, not the phase-shifting transformation itself. The paper however does not provide an independent evaluation of the guidance network’s specific performance in estimating the phase angle \phi, which could easily be done when ground truth shifts are known. Most evaluations, including the ablation studies, focus on downstream tasks, which are interesting and practically relevant but do not provide clear insight into what the algorithm is doing at the shift-invariance level. They also add confounding factors. For instance, in the appendix, you argue that "it can be observed that the number of parameters for the guidance network is much less than the main classifier", around 2% of the number of parameters, but the classifier is not an inherent part of your shift-invariant approach.

- A natural follow-up question is how well the guidance network performs in OOD settings where the ground truth shifts are known but the time series were not part of the training data. Since the learned latent representations are still just time series, a simple illustration of the approach could be to take in a number of shifted time series and visualize the resulting latent representation of the time series.

- While the shift consistency captures something in this direction, it still requires training the classifier to assign class probabilities. While the S-Cons results look impressive across the experimental results, could one not directly measure the variance or consistency of the output angles (or phase-shifted latent representations) across the shifted samples to get clearer insights into what is happening here?

- In that spirit, there could also be comparisons to other approaches in time series alignment. This could also provide a more direct evaluation of the shift-invariant transformation and isolate the main contribution of the method.

In summary, while the paper introduces an interesting approach, these concerns prevent me from fully supporting acceptance in the current form. But I am open to adjusting my assessment if some potential confusion is clarified/some clarifying results are provided.

### Questions
- Figure 1: while I appreciate the thorough overview, the figure contains a lot of information that is a bit hard to grasp without more detailed descriptions or additional reading, and connections between subpanels (e.g. a&b and c&d) could be grouped more clearly.

- If two time series are merely shifted versions of each other, a purely analytical approach based on the Fourier transform could align them without the need for a neural network to estimate the phase shift (e.g. by saying that one of the two is the “unshifted prototype” of the other time series). It is hard for me to understand why we need a neural network architecture for this, since if the phase shift between two time series can be determined analytically in the Fourier domain, the guidance network’s task of estimating phi seems redundant.

This connects to the question of how to determine $\phi_0$, since there is an additional symmetry breaking required in the guidance network by randomly designating certain samples as “unshifted” to train the network. Does this introduce potential inconsistencies in the latent space representation across training runs which might learn different mappings for the "unshifted" state, depending on which samples are chosen as the reference? The authors do not explicitly argue that the guidance network is introduced to handle more complex cases with non-uniform shifts or noise, which would make sense to me as a motivating factor. An interesting follow-up question could be what the model actually does if there are non-uniform shifts. How robust is the guidance network’s output for longer/shorter time series?

### Soundness
2

### Presentation
3

### Contribution
2
