# ResBit: Residual Bit Vector for Categorical Values

- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 3, 3

## Abstract
One-hot vectors, a common method for representing discrete/categorical data, in machine learning are widely used because of their simplicity and intuitiveness. However, one-hot vectors suffer from a linear increase in dimensionality, posing computational and memory challenges, especially when dealing with datasets containing numerous categories. In this paper, we focus on tabular data generation, and reveal the multinomial diffusion faces the mode collapse phenomenon when the cardinality is high. Moreover, due to the limitations of one-hot vectors, the training phase takes time longer in such a situation. To address these issues, we propose \textbf{Res}idual \textbf{Bit} Vectors (ResBit), a technique for densely representing categorical data. ResBit is an extension of analog bits and overcomes limitations of analog bits when applied to tabular data generation. Our experiments demonstrate that ResBit not only accelerates training but also maintains performance when compared with the situations before applying ResBit. Furthermore, our results indicate that many existing methods struggle with high-cardinality data, underscoring the need for lower-dimensional representations, such as ResBit and latent vectors.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In the paper, the authors propose a Residual Bit Vector (ResBit), which is a hierarchical bit representation. Authors also show that such representation can be used to build a tabular data generation method called TRBD. TRBD can generate diverse and high-quality data from small-scale table data. ResBit was also used in GANs or conditioning.

### Strengths
1. The paper introduces the interesting extension of Analog Bits.
2. The paper has good theoretical fundaments.

### Weaknesses
1. In the abstract, the authors introduce methods in a different order than in the introduction. It is misleading. Maybe it is possible to do it consistently.
2. The first Fig 1. in the paper refers to the reference paper. Maybe at the beginning, authors can give some illustrations describing the new proposed method. 
3. Some illustrations of the method should be added.
4. The model proposes three elements: ResBit, TRBD, and conditioning GAN. Unfortunately, none of such components are well evaluated. Especially ResBit should be compared with Analog Bits.
5. In TabDDPM, authors propose experiments on 15 datasets with many baselines. Authors should follow such an experimental setting. 
6. Maybe authors should introduce fewer components but add more detailed comparisons with existing methods.
7. Maybe it is possible to run the algorithms on an image dataset.

### Questions
1. How the ResBit algorithm works concerning Analog Bits.
2. Maybe it is possible to show some practical tasks to show that ResBit works better than Analog Bits.
3. The United States example is convincing, but the authors should present that such a problem is a real problem in practical application.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a hierarchical bit representation called Residual Bit Vector (ResBit) to address the complexity issue of one-hot encoding of categorical data. Because the number of elements of one-hot encoding grows linearly with the number of categories, the increased dimensionality may be harmful to performance. ResBit mainly follows the idea of residual vector quantization (Juang & Gray, 1982). It finds binary representation hierarchically and is shown to avoid the so-called “out-of-index” problem for some cases. Several experiments in tabular data generation, image generation, and image classification are conducted to study the performance of ResBit. Mixed results are reported.

### Strengths
I find it really hard to find the strengths of this paper. See the reasons below.

### Weaknesses
- There are several false claims in the paper. First, ResBit may not fully address the “out-of-index” issue. Since $N=50=32+16+2$, the example given in the paper is free from the issue. Proof for any natural number is missing. One can find a counterexample by find the ResBit representation of $N=51$? Second, the ResBit does not really improve or at least achieve no worse results compared to their baselines. In some cases, ResBit even performs much worse than the baselines.

- Some descriptions in the paper are not clear. For example, the authors claim that increasing the dimensionality can cause model learning to fail. It is not clear to me why and how it fails. For example, overparameterization can lead to better results. Providing some references could be helpful. It is also unclear what specific failure modes are observed. Does the model fail to converge, or does it overfit drastically? The lack of detail makes it difficult to assess the validity of this claim.

- In Section 4.1.4, the authors state that the loss exploded or disappeared during the training phase of TabDDPM for certain datasets and argue that that is probably due to the very large number of dimensions. This seems to be a strange reason because the dimensions are not too large in these problems and usually this kind of problem can be addressed by normalizing the features or using smaller learning rates. The authors should provide more evidence to support this claim, such as a comparison of training dynamics with and without normalization or different learning rates. Simply stating that it is due to high dimensionality is insufficient.

- The runtime comparison seems unfair because the TabDDPM and TRBD use different networks with different number of layers. It is essential to control for network architecture when comparing runtimes. The authors should provide a comparison using identical network architectures to isolate the effect of the ResBit representation. In Section 4.3, it would make more sense to use ResBit for datasets like ImageNet. CIFAR-10 only has 10 classes so the reduction of the encoding of the categories is insignificant. The potential benefits of ResBit are not fully explored with such a small number of classes.

- In Section 4.4, the authors argue that ResBit reduces the representation complexity of categorical data. However, this would be only meaningful when the performance of ResBit is justified. The claim of reduced complexity is not meaningful if the performance is not competitive with existing methods. The authors need to show that the reduced complexity does not come at the cost of performance.

### Questions
1. Can we prove that ResBit does not have the “out-of-index” issue mathematically?

2. Given that ResBit is proposed for reducing the representation complexity of categorical data, have you tried to run ResBit for image classification on ImageNet? Does it maintain the performance compared to one-hot encoding while achieving lower complexity?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a new encoding technique for categorical values: residual bit vectors which are computed iteratively as bit-representations of category number (where category is treated as an actual number; see section 3.2. for a detailed explanation). The motivation for this work is in the application of one-hot encoded vectors: the authors are motivated to train table diffuison models where input/outputs are tabular data that can potentially have millions of categories. Training the diffusion model with million dimensional input outputs is a challenge, thus some lossless dimensionality reduction is needed. Why not compute bit representation once? Paper defines the main issue with simple bitwidth as an "out of index" problem, meaning that if total number of categories are not exact power of 2, say 9, then the bit representation of such a categories introduces extra "sampling" dimensions that might be an issue during diffusion training/sampling. In case of 9, its representation would require 4 bits, i.e. 9=1001; during diffusion sampling a number 1011 can be sampled, which would correspond to non-existing category. 

Authors test out their proposed encoding method on several datasets in a TSTR manner (train on synthetic, test on real): they train a diffusion model to generate synthetic data, train a classifier/regressor on just generated data, and test the classifier/regressor on the actual data used for the diffusion model training. Results indicate that a proposed encoding is on par with simple log_2 encoding.

### Strengths
The proposed method is very simple to understand and implement.

### Weaknesses
Paper has two weaknesses: results and presentation
1. Results. On 5 tabular datasets where the such an encoding method would be of most use, the proposed is clearly better only on 2 of the tasks (CC, AR), whereas on BD and AD performance is on par, and I'm going to discount any results on IS due to the size of dataset (1338).  Similarly, when used for conditioning of GANs, visually speaking res-bit results seems to be worse (much less diverse) and have no strong edge over one-hot in classification tasks. Considering these observations, it is hard to say that residual bitwidth representation of categorical values is a good encoding in general. The lack of a clear and consistent performance advantage across a wider range of datasets and tasks significantly undermines the practical utility of the proposed method. The GAN results, in particular, raise concerns about the method's ability to generate diverse and high-quality samples, which is a critical aspect of generative modeling.
2. Presentation & Motivation. I the writing and the flow of the paper hard to follow. Initial pages are more like a catalog book of ml methods (section 2 in particular) rather than a cohesive presentation of ideas. The paper has many stylistic issues like using "that this", "very widely used", "limit the increase in dimensionality to a logarithmic increase" and etc. Also, I find the motivation a bit underdeveloped. Section 3.1. explains the "out of index" issue but does not provide evidence whether it is indeed the main cause that limits the model performance. I, generally believe, that a well trained model would learn to not sample from category bits that does not exist. It would be an important addition to the paper to show not only better results but provide evidence that improvement was due to solving out-of-index issue.

### Questions
Please address weaknesses above as much as possible.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor
