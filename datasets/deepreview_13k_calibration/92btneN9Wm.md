# SPDER: Semiperiodic Damping-Enabled Object Representation

- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 8, 5

## Abstract
We present a neural network architecture designed to naturally learn a positional embedding and overcome the spectral bias towards lower frequencies faced by conventional implicit neural representation networks. Our proposed architecture, SPDER, is a simple MLP that uses an activation function composed of a sinusoidal multiplied by a sublinear function, called the \emph{damping function}. The sinusoidal enables the network to automatically learn the positional embedding of an input coordinate while the damping passes on the actual coordinate value by preventing it from being projected down to within a finite range of values. Our results indicate that SPDERs speed up training by 10$\times$ and converge to losses 1,500$-$50,000$\times$ lower than that of the state-of-the-art for image representation. SPDER is also state-of-the-art in audio representation. The superior representation capability allows SPDER to also excel on multiple downstream tasks such as image super-resolution and video frame interpolation. We provide intuition as to why SPDER significantly improves fitting compared to that of other INR methods while requiring no hyperparameter tuning or preprocessing.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a simple architecture to overcome the spectral bias towards lower frequencies in traditional neural network.
It formulated a so called damping function implemented by MLP. It contains an activation function composed of a sinusoidal multiplied by a sublinear function.
The sinusoidal enables the network to automatically learn the positional encoding of an input coordinate while the damping passes on the actual coordinate value by preventing it from being projected down to within a finite range of values.
Further experiments demonstrated good performance on multiple downstream tasks such as image super-resolution and video frame interpolation.

### Strengths
+ The proposed method is novel.
+ The introduced damping function is interesting and theoretical sound.
+ The paper shows cases of multiple potential applications using proposed method.
+ Experiments demonstrated that it can largely improve the performance and training efficiency in dummy setups.

### Weaknesses
 - Do not prove the derivatives of different variants of proposed method.
- It lacks experiments on more realistic datasets.

### Questions
Can you evaluate the proposed method on more complex images? Consider to perform formal evaluations on popular benchmarks, such as CelebA, UHDSR4K and Vimeo-90k to demonstrate its superiority.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel family of activation functions to enable an MLP to represent an input signal (image, audio) to very high fidelity. Both the loss and the architecture are modified to enable this. A number of experiments are provided to show the benefits of the resulting model.

### Strengths
The paper is simply written and easy to follow (although slightly prone to hyperbolic language; pls see suggestion below). The provided experiments, while not comprehensive, paint a solid picture of the abilities of the model to represent signals in near-lossless manner. The method itself seems very simple to code (although no code was provided, and no training details given). Overall the paper has the strengths of simplicity and should be very easy to use in practice.

### Weaknesses
1. I am concerned that this method tends to overfit heavily and easily to a given particular input image/signal, and evidence for generalization was very limited to (as far as I can tell) a single video example. How sensitive is the model to noise in the input, for example? This can be important for real-world applications. Specifically, while the paper shows impressive results on fitting individual signals, it lacks a thorough investigation into the model's behavior when presented with slightly perturbed or corrupted inputs. The experiments should include a more rigorous analysis of the model's robustness to various types of noise (e.g., Gaussian, salt-and-pepper) and different levels of perturbation. The absence of such analysis raises concerns about the practical applicability of the method in real-world scenarios where input data is rarely pristine.

2. I am not an expert in this space, but one question I have is whether the baselines are strong. SIREN is the most commonly used baseline. Maybe the authors can provide some perspective in this regard. It would be beneficial to see a more detailed comparison with other state-of-the-art implicit neural representation methods, particularly those that have demonstrated strong performance in similar tasks. A more comprehensive comparison would help to contextualize the contributions of this work and highlight its specific advantages and disadvantages relative to existing approaches. The current comparison, while including SIREN, could be expanded to include other relevant baselines, especially those that utilize different architectural choices or training strategies.

### Questions
There is a statement buried in page 4 that says: "For example, they are less successful at novel view synthesis, where the input direction is polar.". However, no examples of performance on novel view synthesis was provided. Can the authors comment on this?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a novel architecture for coordinate-based networks used for signal representation. The key contribution of this architecture is that the activation function is changed to a sinusoidal function multiplied by a damping function. This result leads to improvement over existing activations which either use ReLU, and have a spectral bias towards low-frequency functions, or use sinusoidal activations, which do not have a notion of locality due to the lack of damping factor and thus lead to poorer reconstructions. This contribution is justified empirically by showing that it leads to significantly better signal fits on image signals.

### Strengths
In my opinion, the strengths of the paper are:
1. The paper is presented exceptionally clearly. The activation function and possible choices are explained very well, and the reasoning for the chosen function is justified intuitively, and there are theoretical guarantees on the Lipschitz constant of the function represented by the network. I view this as very valuable as the paper can have more impact if researchers understand the reason for the increase in performance, as this is under-explored area of activation functions in coordinate-based networks.
2. The comparisons show that the proposed SPDER activation function leads to significant improvement over positional encoding, SIREN, and ReLU networks in signal memorization tasks. This shows that the relatively simple contribution does lead to an improvement in what is claimed, and has the potential to be impactful.

### Weaknesses
In my opinion, the weaknesses of the paper are:
1. I think that additional experiments could be used as there are other coordinate-based network architectures which claim improvements over positional encoding and SIREN architectures. I'm not sure why Instant-NGP is chosen here, as it is a hybrid implicit-explicit representation and is very different from the other coordinate-based networks. I believe a better fit would be [1] or [2], which show that simple networks with different activations, structures, or positional embeddings can improve on the FF/SIREN architectures. Specifically, the paper should compare against methods that explore alternative activation functions or positional encodings within a purely implicit neural representation framework, as Instant-NGP's hybrid nature makes it an unsuitable comparison for the core claims of this paper. The comparison should focus on methods that directly address the spectral bias issues in coordinate-based networks, which are the main focus of this paper.
2. Following the additional experiments thread, I'm not sure why comparisons on radiance field fitting are not included. While interesting as a toy problem, image signal representation is not very useful in many computer vision tasks, besides maybe super-resolution. However, coordinate-based networks have been very useful in computer graphics, where they can be used in solving inverse problems and reconstructing 3D from 2D. Not including an experiment on radiance field, which is the most impactful field where an improvement in coordinate-based network fitting would be utilized, leads me to believe that the impact of the method is severely limited due to some unknown reason, perhaps speed or memory constraints in the architecture? The paper should include experiments on radiance field fitting, as this is a key application area for coordinate-based networks, and the absence of such experiments raises concerns about the general applicability of the proposed method. The lack of such experiments makes it difficult to assess the practical impact of the proposed activation function.
3. Even simpler than radiance field fitting, I don't understand why there is no experiment on overfitting 3D shapes, such as SDFs? This is where coordinate-based networks originated, and could be used as a compressive representation. The paper mentions compressive signal representations in the conclusion, but there is no study on how effective SPDER is for this - no study on memory consumption, or size of networks needed to reach an acceptable level of quality. This is usually done when trying to represent 3D objects with SDFs, so this leads me to believe the method may have some limitations here. The paper should include experiments on fitting 3D shapes using SDFs, as this is a fundamental application of coordinate-based networks. The lack of experiments on SDF fitting and compression raises questions about the method's practical utility in 3D shape representation, which is a significant area for coordinate-based networks.

### Questions
I do not have any additional questions on the paper, as it is described very clearly. Overall, I think that the contribution of the paper is strong due to its simplicity and demonstrated improvement on image-signal overfitting tasks. However, I think that the evaluations are limited - there are other coordinate-based network architectures which lead to improvement over the baselines which are compared to here, and most importantly, the method is not compared on radiance fields, which is the most impactful application of coordinate-based networks. I think that addressing these two weaknesses would make the paper significantly stronger and in that case I would be happy to raise my score.

**Update after author response**

After reading the author response, I am not inclined to change my score. While I appreciate the additional comparisons, and I believe the paper does a convincing job showing that overfitting image signals can be done extremely well with SPDER, I think the paper weakness is justifying *why* this is a relevant problem. The method seems to not work on radiance fields, has not been shown to work on SDFs, nor am I sure it offers compression benefits in overfitting image signals. Thus, I'm not sure what application it would be used in. On the other hand, there is no theoretical proof that it is able to encode a wider frequency band of signals, only empirical results on a relatively narrow range of experiments. With further work, I believe the paper could make a meaningful contribution, but in this state I remain borderline.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good
