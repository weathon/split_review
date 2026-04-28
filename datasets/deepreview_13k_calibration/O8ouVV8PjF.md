# CNN Kernels Can Be the Best Shapelets

- Decision: Accept
- Avg Score: 5.80
- Scores: 5, 6, 8, 5, 5

## Abstract
Shapelets and CNN are two typical approaches to model time series. Shapelets aim at finding a set of sub-sequences that extract feature-based interpretable shapes, but may suffer from accuracy and efficiency issues. CNN performs well by encoding sequences with a series of hidden representations, but lacks interpretability. In this paper, we demonstrate that shapelets are essentially equivalent to a specific type of CNN kernel with a squared norm and pooling. Based on this finding, we propose ShapeConv, an interpretable CNN layer with its kernel serving as shapelets to conduct time-series modeling tasks in both supervised and unsupervised settings. By incorporating shaping regularization, we enforce the similarity for maximum interpretability. We also find human knowledge can be easily injected to ShapeConv by adjusting its initialization and model performance is boosted with it. Experiments show that ShapeConv can achieve state-of-the-art performance on time-series benchmarks without sacrificing interpretability and controllability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This article deals with the classification of time series. The authors describe the equivalence between a particular approach, shapelets, and convolutional layers. They provide several losses to enforce the diversity of learned shapelets and closeness to original data, as well as intuitive initialization methods. The proposed approach is compared to several algorithms in a thorough experimental study.

### Strengths
The article describes the methodology well, and, to the best of my knowledge, the proposed initializations and losses are novel in the context of shapelets. The experiment study is extensive (with one caveat, see below) and convincing.

### Weaknesses
- The main contribution is based on Theorem 3.1, which shows that the shapelet transform is somewhat equivalent to a convolution layer followed by a max pooling operation. However, this fact has been observed previously to provide accelerated shapelet transform: the authors of [1] show that computing the distance profile ($dist(\mathbf{s}, \mathbf{x})$ for a given sequence $\mathbf{s}$ and all subsequences $\mathbf{x}$ of $\mathbf{X}$) is equivalent to a convolution. The authors do not adequately distinguish their work from this prior observation, particularly concerning the use of convolution for efficient distance calculation, which is a core aspect of shapelet discovery.

- An extensive review of time series classification algorithms exists on the same data sets, see [2] and more recently but unpublished [3]. None of the algorithms referenced in [2, 3] are compared to ShapeConv. The authors should at least compare themselves to the best-performing algorithms of the state-of-the-art. The absence of these comparisons makes it difficult to assess the true performance of ShapeConv relative to established methods, especially given the known performance of ensemble methods and deep learning approaches on these datasets.

- (Minor comment.) It is considered bad practice to start sentences with mathematical symbols.

### Questions
In addition to addressing my comments about Theorem 3.1 and the comparison to the state-of-the-art, I have one question:
- Convolutional layers are meant to be stacked. Unless I am mistaken, in the experiments, there is only one ShapeConv layer. Would the interpretability of ShapeConv remain if there are several layers?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper bridges the divide between traditional shapelets and modern deep learning methods in time-series modeling. Shapelets, while interpretable, face efficiency issues; deep learning models offer performance but lack interpretability. The proposed ShapeConv melds these approaches, using a CNN layer with its kernel functioning as shapelets. This layer is both interpretable and efficient, achieving state-of-the-art results in experiments. The introduction of shaping regularization and human knowledge further enhances its performance and interpretability.

### Strengths
1. This paper theoretically establishes an equivalence between traditional Shapelets and using a convolutional layer to derive similar features. It’s a fresh perspective in utilizing shapelets in combination with deep learning methods and structure.
2. The comprehensive experiments empirically demonstrate the superior performance of ShapeConv, in both classification as well as clustering tasks.
3. The paper is well-written and easy to understand.

### Weaknesses
1. An analysis of the computational complexity and resource requirements of ShapeConv could make the paper more comprehensive. Specifically, a breakdown of the time and space complexity with respect to input time series length, shapelet length, and number of shapelets would be beneficial. Furthermore, empirical measurements of training and inference time on various hardware configurations would strengthen the analysis.
2. Though the model's performance is promising, concerns may arise regarding the complexity of implementing ShapeConv compared to other traditional or deep learning models. The paper should provide a more detailed discussion on the practical challenges of integrating ShapeConv into existing deep learning frameworks, including potential issues with backpropagation and gradient computation due to the shaping regularization and human knowledge constraints.

### Questions
This study opted for a combination of CNN and Shapelets to enhance interpretability while also boosting performance. For time series classification tasks, why not choose the stronger baseline models for research, such as RNN or Transformer?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper combines Shapelets and CNNs

### Strengths
Good empirical results.
Tests on many datasets (although, just download and test, no new datasets)

### Weaknesses
I appreciate the accuracy improvements, while small, are probably real.

However, I have no confidence in any of the claims of interpretability and explainability. You made no effort to obtain the original herring images or gun-point videos. You explanations here are "just-so" stories. [v].

If you wanted to make convincing claims here, you could obtain the herring images, modify them to add / remove effects, then see how this affects the shapelets. Or reenact the gun-point video, and  modify the protocol to add / remove effects, or...

I do understand that most people in this space are too lazy to go beyond downloading the UCR datasets. But if that is all you do, it seems like you should temper your claims about interpretability and explainability.




“In the realm of machine learning, interpretable time-series modeling stands as a pivotal endeavor, striving to encode sequences and forecast in a manner that resonates with human comprehension”
This (and the rest of the paper) read like flowery language [a].


In fig 1, can you move the legend away from the data?


“is evaluated on the 25 UCR” Did you mean “125” or “25”?


“Figure 5: Shaplets learned” typo (Shapelets)


“It is evident that the shapelet learned by ShapeConv captures the distinguishing features of the class effectively”  Evident to whom? You should argue that the blue shapelets correctly represents the actors hand having to hover over the gun holster, then reach down to the gun, then draw the gun.


“clustering task using 36 UCR univariate”
Why 36? Why this particular 36?



“In response to the first RQ, we observe that ShapeConv’s shapelets (Figure 4 (a)) cover all turning points in the time series, where the two classes differ the most, while LTS’s shapelets (Figure 4 (b)) do not cover the targeted regions.”
This evaluation is tautological. If  “turning points” are the best places for shapelets, then we don’t need any search for shapelets at all.



“In contrast, when using human initialization,..”
Hmm, it is a bit tricky to claim results based on human initialization. Which humans, how trained are they in the system, how are they briefed. In my mind, that is a separate “human in the loop” paper.


However, despite ingenious, the performance (missing a word?)
However, despite ingenious suggestions, the performance

gun out of the gun pocket (holster)


“while data from the “finger” class don’t.”
“while data from the “finger” class do not.”  (avoid contractions in scientific writing)


This illustrate how
This illustrates how

In table E.5, why four significant digits? This is spurious  accuracy.

In table E.5 and elsewhere, you report the average accuracy.  This is meaningless for datasets of different sizes, class skews, number of classes, default rates etc. To be clear, it is not a flawed metric, it is just meaningless.

### Questions
NA

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a modified convolutional layer for time series analysis inspired by the Shapelet distance that is widely used in the domain.
This new layer is then used at the core of neural networks for both supervised and unsupervised tasks.
A regularization term for the task-specific losses is designed that enforces learned kernels to (i) look like actual subseries from the training set and (ii) form a diverse set.

### Strengths
The paper is very well written and the motivation for the method is clear.
The experimental validation is quite thorough and it is nice to showcase that the method can be used for both supervised and unsupervised learning.
In terms of the method, while the idea of having a Shapelet layer included in a neural network is not novel, both the initialization scheme and the regularization terms included in the loss lead to improvement on the performance of the resulting models.

### Weaknesses
In the abstract (it is also said in the introduction in other words), it is stated that:

>  In this paper, we demonstrate that shapelets are essentially equivalent to a specific type of CNN kernel with a squared norm and pooling

In fact, this demonstration is not novel, it is for example stated in (Lods et al. 2017) (that is cited in the paper).
However, it seems that here, the proof aims at more rigor, but Theorem 3.1 is not successful in this regard since it completely disregards the fact that the bias term in convolution is independent of the input, which is not the case in the $-\mathcal{N}(s_i, X_{j:j+l_s-1})$ term. (Also, as a side note, in Theorem 3.1, Squared Euclidean distance is used, not Euclidean distance as stated.) Moreover, the core claim of equivalence between Shapelets and CNN kernels is not rigorously demonstrated. The paper shows that the Shapelet transform is equivalent to the proposed ShapeConv layer, which is not a standard convolutional layer. The crucial point is that the $\|X\|^2_2$ term cannot be obtained from a standard convolution operation, thus the equivalence to a standard CNN kernel is not established. The ShapeConv layer is essentially a re-writing of the shapelet transform, not a demonstration of equivalence with a standard CNN.

Moreover, the review of the Related Work is very succinct and a more thorough presentation of competing interpretable Shapelet-based methods would have been a plus. 
Similarly, a more detailed comparison of the interpretability of the ShapeConv model with those baselines is required to fully assess interpretability:
* Only toy examples are presented (eg. Fig 4: 2 shapelets), what does it give when training with a large amount of shapelets?
* Also, providing visualization for a large number of datasets instead of only GunPoint+Herring+ECG200 would be a real plus

### Questions
Apart from the questions/suggestions related to the evaluation of interpretability, I have a few remarks/questions that are listed below:

* If you took your your ShapeConv model (with exact same initialization, regularization terms, etc.) and changed the ShapeConv layer with a convolutional one, what would you get in terms of performance? This experiment is required to fully assess if the norm terms a really helpful
* In terms of evaluation:
    * How are baseline model hyperparameters tuned (and which parameters are tuned)?
    * How do you pick the datasets for the subsets (25 datasets for supervised learning and 36 datasets for unsupervised learning)?
    * If the goal is to compare to state-of-the-art methods, other competitors should be included in the comparison (eg. ROCKET, COTE & variants, ...)

Below are some minor remarks/questions:
* In Section 1, you write:
    >  they are more likely to overfit when the signal-to-noise ratio is relatively large
    * Don't you mean "is relatively low"?
* Initialization
    * Have you assessed how important it was to use supervised information at initialization?
    * Have you tried simpler approaches (eg. kmeans++ on randomly selected subsequences of adequate length)?
* If ShapeConv is faster than LTS, it is probably more an artifact of the implementation since the overall complexity of ShapeConv is probably higher than that of LTS (similar local representation extracted, but ShapeConv have additional loss terms that induce more computations)
* Presentation
    * Unsupervised learning: it is unclear from the presentation in Section 3.4 which clustering method is used on top of the features extracted from ShapeConv. This is detailed in Section 4.2, but should be explained in Section 3.4 imho

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce ShapeConv, an interpretable CNN layer whose kernels function as shapelets, designed for time series modeling in both supervised and unsupervised settings. They demonstrate that using the square norm in convolution, coupled with max pooling, is equivalent to computing the distance between a shapelet and a time series. Within this framework, a convolutional kernel essentially serves as a tunable shapelet. The authors also incorporate regularization to enforce similarity and diversity among shapelets, depending on whether the task is supervised (classification) or unsupervised (clustering). The methodology is validated through experiments on time series classification and clustering, using several competitor models and alternative implementations of ShapeConv for comparison. XAI is assessed via author-selected examples.

### Strengths
- The paper is generally well-structured and straightforward to follow.
- It establishes an interesting link between convolutional operations and the shapelet transform.
- The proposed methodology is versatile, applicable to both supervised and unsupervised tasks.

### Weaknesses
 - The paper lacks a comprehensive review of related work, and the selection of competitor approaches for comparison is odd.
- Parts of the experimental section are unclear and require further clarification. The XAI evaluation is restricted to examples selected by the authors.
- There is no discussion or citation concerning code implementation.

### Questions
1. **Lack of Comprehensive Review of Related Work**:
   - The authors focus exclusively on optimization-based shapelet approaches. While space is limited, notable methods like Random Shapelet Forest and standard shapelet transform should not be omitted. Dictionary-based and interval-based approaches are also relevant and have achieved state-of-the-art performance in time series classification, yet they are not mentioned. Furthermore, the competitor models used in the experimental section are largely transformer-based or rely on embeddings, making for an unusual selection. I recommend that the authors thoroughly review relevant literature on time series classification, such as the paper by Ruiz et al. (2021) and models like ROCKET by Dempster et al. (2020).

2. **Ambiguities in the Experimental Section**:
    - Is the "Initialization" phase's cost included in the runtime?
    - In Table 1, why do the methods differ with respect to the cd plots?
    - Why is the evaluation limited to 25 UCR datasets, and what was the criteria for selection?
    - Several state-of-the-art methods like Rocket, CIF, ShapeletTransform, and MUSE are absent from the comparison.

3. **Limitations in XAI Evaluation**:
    - While the author-selected examples support the paper's claims, they do not suffice to demonstrate the superiority of ShapeConv in terms of shapelet quality. Additionally, pairing ShapeConv with MLP or SVM models does not provide sufficient interpretability. I suggest testing the approach with tree-based or linear models, or employing explainers such as SHAP to determine the importance of shapelets, especially in supervised tasks.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
