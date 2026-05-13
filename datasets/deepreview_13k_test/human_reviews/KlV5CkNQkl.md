# Data-centric Prediction Explanation via Kernelized Stein Discrepancy

- Decision: Accept
- Scores: 5, 8, 8, 6

## Abstract
Existing example-based prediction explanation methods often bridge test and training data points through the model's parameters or latent representations. While these methods offer clues to the causes of model predictions, they often exhibit innate shortcomings, such as incurring significant computational overhead or producing coarse-grained explanations. This paper presents a \underline{H}ighly-precise and \underline{D}ata-centric \underline{Explan}ation (HD-Explain)
prediction explanation method that exploits
properties of Kernelized Stein Discrepancy (KSD). Specifically, the KSD uniquely defines a parameterized kernel function for a trained model that encodes model-dependent data correlation. By leveraging the kernel function, one can identify training samples that provide the best predictive support to a test point efficiently. We conducted thorough analyses and experiments across multiple classification domains, where we show that HD-Explain outperforms existing methods from various aspects, including 1) preciseness (fine-grained explanation), 2) consistency, and 3) computation efficiency, leading to a surprisingly simple, effective, and robust prediction explanation solution.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents HD-Explain, a data-centric, example-based explanation method leveraging Kernelized Stein Discrepancy (KSD). The authors argue that existing example-based methods for explaining predictions, such as Influence Functions and Representer Point Selection, suffer from high computational costs and coarse-grained explanations. HD-Explain addresses these challenges by using KSD to establish a fine-grained, efficient link between training samples and model predictions. Through empirical evaluations on datasets like CIFAR-10 and medical imaging, the paper shows that HD-Explain outperforms traditional methods in terms of explanation precision, consistency, and computational efficiency.

### Strengths
1. Applying Kernelized Stein Discrepancy to interpretability is novel and conceptually interesting. Unlike other methods that can struggle with memory or computation limits in large models, HD-Explain maintains a low computational cost, which support its use in high-stakes applications where explanation and efficiency are essential. The focus on healthcare datasets underscores the authors’ intent to target real-world, interpretable machine learning needs.

2.   The paper attempts to quantify explanation performance with metrics like Hit Rate, Coverage, and Run Time. These metrics provide a foundation for benchmarking HD-Explain against other methods in terms of granularity, diversity, and efficiency.

### Weaknesses
1. The proposed method provides a new use case of KSD, which has been used in several other cases, such as goodness-of-fit applications, which are quite related to the new use case. The paper extends KSD to explainability, but the novelty is limited to an application shift, applying an existing statistical method to a new context rather than developing a new technique for explanation in machine learning.

2. The paper explains that KSD is close to zero if a model fits the data well, which is shown in previous studies. However, I feel there is a gap of why KSD is a good choice for model explanation, specifically, selecting training samples given a test sample. Also there are other discrepancy measures, such as Maximum Mean Discrepancy (MMD), it's unclear to see why KSD is a better choice for this task among other discrepancy measures. Without testing these alternatives, the choice of KSD appears arbitrary, which weakens the novelty claim.

3. In addition to the newly proposed evaluation metrics, existing metrics such as Linear Datamodeling Score (LDS) seem to be widely used in training data attribution methods. LDS was not reported in this proposed paper.

### Questions
Suggestions:

1. The authors might consider adding an algorithm to show how the proposed method works.

2. The authors are suggested to report LDS, if possible.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposed an example-based explanation method based on kernelized Stein discrepancy (KSD), which can measure the discrepancy between a predictive model and training samples.
In particular, using a model-dependent kernel function used for calculating KSD, the proposed method explains training samples related to the input test sample.
In the experiments on image classification tasks, the proposed method and its variant outperformed the comparing methods in terms of two qualitative metrics.

### Strengths
- The proposed method is a good and natural application of KSD, and as a result, it broadens the potential of KSD.
- The derivation of the proposed method is convincing, and thanks to the well-written explanation, it is easy to follow.

### Weaknesses
- The proposed method seems a straightforward application of kernel conditional Stein discrepancy (KCSD) [1]. Therefore, the technical novelty of the proposed method is limited.
- Although the experiments were conducted on popular image classification datasets, the evaluation protocol is artificial, especially in evaluating the hit rate.

[1] Jitkrittum, Wittawat, Heishiro Kanagawa, and Bernhard Schölkopf. "Testing goodness of fit of conditional density models with kernels." Conference on Uncertainty in Artificial Intelligence. PMLR, 2020.

### Questions
- As related works and comparing methods, Datamodels [2] and its variant, TRAK [3], are not mentioned. Is there a reason why they are not addressed?
- Compared to KCSD, what are the key points of technical novelty in the proposed method?
- In the noise injection setting, it seems that even a simple method that returns the nearest neighbor training sample of the test sample could explain the predictions. Compared to such a baseline, why does the proposed method perform better? Alternatively, can it be demonstrated through experiments that the proposed method is superior?

[2] Ilyas, Andrew, et al. "Datamodels: Predicting Predictions from Training Data." Proceedings of the 39th International Conference on Machine Learning. 2022.

[3] Park, Sung Min, et al. "TRAK: Attributing Model Behavior at Scale." International Conference on Machine Learning. PMLR, 2023.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new method for computing instance-level explanations, based on the Kernelized Stein Discrepancy, by poiting to examples having the biggest contribution to the classification made by the model. Indeed, given a datapoint x, the methods aims at searching the top-k training datapoints leading to the biggest value of the defined KSD kernel. The approach is tested on both classical benchmark datasets from the literature (CIFAR-10, SVHN) as well as real-life datasets needing explanations (Brain Tumor, Ovarian Cancer) and compared to a few methods from the literature.

### Strengths
The proposed approach is both sound and original. The method is clearly explained.

### Weaknesses
1. While HD-Explain* is simply presented as a declination of HD-Explain, details should be part of the work since it is equally important to HD-explain in the experiment section. In the same line of thoughts: it is said that « The qualitative evaluation for OCH and MRI datasets are given in the appendix due to the page limit of the main paper. », but the current submission makes 9 pages out of a maximum of 10 (https://iclr.cc/Conferences/2025/CallForPapers).

2. « In addition, as Influence Function and TracIn face scalability issues, we limit the influence of parameters to the last layer of the model so that they can work with models that contain a large number of parameters. Our experiments use ResNet-18 as the backbone model architecture (with around 11 million trainable parameters) for all image datasets » Since datasets such as CIFAR-10 can tackled decently by small neural networks, it would be necessary to test whether limiting the influence of parameters to the last layer of the model for benchmarks impacts the results or not. It yields a huge effect on HD-explain, as demonstrated by HD-explain*, so it might as well for other approaches.

3. I feel like there are a few conceptual incoherence/false statements in the presented approach, both theoretically and in the empirical section.

3.1 Line 320: « For both correct prediction cases, we are confident that HD-Explain provides a better explanation than others in terms of visually matching test data points e.g. brown frogs in Figure 3 (a) and deer on the grass in Figure 3 (b). » It is not because the test and the explanation images look alike to us that the model did use the information contained in the explanation to classify the test. Following the line of thought presented in the article, the explanation image should be near the test image in the feature space, yet these images might not particularly look alike to us. In short: I don’t think the observations made in section 4.1 tell us anything about the quality of the explanation.

3.2 I don’t feel like the considered metrics actually reflect the quality of the approaches. For instance, using the coverage metric requires making the assumption that a wide array of training samples should be used for explaining a wide array of test images. One could easily imagine a setup where an image contains the typical representation of a class, each other image being the same as that first one, but each having a unique particularity. In this setup, the most relevant explanation would be the typical representation for every image, since it is the most similar to every other image. When it comes to hit rate, once again, we can imagine that once a picture is flipped or noised, it now more resembles another picture.

**Typos and such** 

-Figure 1, right : Error in the Y-axis name (wrong letter, d instead of D; « heta » instead of $\theta$).

### Questions
-Could the authors cite other works using these metrics (Hit rate, Coverage)?
-Could the authors provide explanations regarding the observations made in 4.3?
-Did the authors prevent undesired results for the image flip on SVHN? For example, flipping a 2 leads to a 5.

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
The paper proposes a new example-based explanation technique by using Kernelized Stein Divergence (KSD) to identify coresets of training samples that best provide support for a particular prediction on a test point by the model.

### Strengths
The biggest strength of the paper is the simple novelty of the idea. Coresets have a established history already and using a similar approach towards finding points in the training set that explain the model prediction for a test point is a great idea that seems to have not been tried before.

### Weaknesses
The biggest weakness of the paper is poor presentation and writing. The paper is unfortunately littered with typos, grammatical mistakes, and run-on sentences which make it sometimes very difficult to understand certain passages. 

The other weakness is the experiments section, especially the qualitative experiments in Figures 3 and 4 that do not seem to clearly portray the proposed method's strength when compared to the competitors and it is left to the reader to figure it out.

here's a few typos and possible presentation improvements:

line 93-94: currently it reads like the research history spans from 2020 to 2020. Please add that the papers cited are survey papers.

line 106-107: "unfortunately, those approaches are often with strong assumption of good prototypes (as of training data distribution)", this sentence is not self explanatory. Please expand on what "good" prototypes means here and what strong assumptions.

line 138: to assess the goodness-of-fit ... of what?

Figure 1: y-axis should say $P_\theta$ in markdown

Figure 2 will probably make a better Figure 1 - it shows why the proposed method could potentially work better.

line 235: "that out of" -> "that is out of"

line 237-240: run-on sentence and ends abruptly without a conclusion.

line 319: "high-confident" -> "high-confidence"

line 323: "we note the HD-Explain produces an example that does not even..." in figure 3(c) all examples are labelled as cat, so not sure which example this sentence is referring to, and it's visually very hard to distinguish the images.

line 366: "target model makes 1-2)" -> remove "-2"

line 428: refers to Figure 8 and conclusions drawn from it as "previous observation". There is no Figure 8 in the main manuscript. Figure 8 is in the appendix and shows up later.

Conclusions section is inadequate and should include discussion on limitations and future directions. ICLR allows for 10 pages of text this year.

### Questions
Can the authors expand on the use of kernels. In my experience euclidean distance based kernels (like RBF kernel used in the paper) tend to fall apart when used with high dimensional data - like images, due to curse of dimensionality. Given the reliance of this method on being able to compute useful kernels how do the authors think this method can be scaled to actual images (that are significantly higher dimensional than the benchmark images used here)?

In Figure 4, the authors say the "model predictive accuracy is near 100%, ... random search". Why do a random search here? Shouldn't you be able to pull any mispredicted samples deterministically?

In the quantitative eval section why is only horizontal flip tested? Would other transformations of data points hold just as well? (e.g. rotation -, Figure 1 seems to suggest that if the whole dataset is rotated that could impact KSD)

### Soundness
2

### Presentation
1

### Contribution
3
