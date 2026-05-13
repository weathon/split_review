# Closing the gap on tabular data with Fourier and Implicit Categorical Features

- Decision: Reject
- Scores: 5, 3, 5, 3, 5

## Abstract
While Deep Learning has demonstrated impressive results in applications on various data types, it continues to lag behind tree-based methods when applied to tabular data, often referred to as the last “unconquered castle” for neural networks. We hypothesize that a significant advantage of tree-based methods lies in their intrinsic capability to model and exploit non-linear interactions induced by features with categorical characteristics. In contrast, neural-based methods exhibit biases toward a uniform numerical processing of features and smooth solutions, making it challenging for them to effectively leverage such patterns. We aim to address this performance gap by using simple, statistical-based feature processing techniques to identify and explicitly encode features that are strongly correlated with the target once discretized, as well as mitigate the bias of deep models for overly-smooth solutions, a bias that does not align with the inherent properties of the data, using Learned Fourier Features. Our proposed feature processing and method achieves a performance that closely matches or surpasses XGBoost on a comprehensive tabular data benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces four techniques to overcome shortcomings of neural networks on tabular datasets, these are:
- detecting implicit categorical features
- using a channel encoding for categorical features
- using learned fourier features
- using 1d convolutions to create non-rotationally invariant neural networks

The authors find that when searching a large space of hyper-parameters including these improvements, they can outperform XGBoost on a substantial portion of the benchmark introduced by Grinsztajn.

### Strengths
The question the paper addresses is highly relevant, and the methods that the paper proposes seem very interesting to investigate in this context. The paper does a thorough benchmark using an established protocol and show improvements over XGBoost. The authors summarize the current literature on the topic well.

### Weaknesses
While the authors summarize the current literature well, the comparison between the literature and the proposed method is somewhat lacking. While it is not feasible to reimplement all the competing methods and evaluating them, at least some of them should be compared. In particular Kadra showed that simple networks can perform well, if tuned correctly, while this paper only uses a very limited search space for the baseline MLP.

The authors use a measure that I'm unfamiliar with for evaluation, 'p-range' and don't provide a reference for it. Using this and using unnormalized scores both seem non-standard, and are not in line with the measure in Grinsztajn, which uses ADTM. Other options would be critical difference diagrams or performance profiles.

The main novelty of this work is introduced in 3.2, so this aspect should be investigated in more detail. There is many choices in the detection of implicit categoricals, and not all off these are justified or even discussed. For example, it's unclear why implicitly categorical features should have low cardinality. For example a time series with discrete jumps is something that's hard to learn for an MLP and should probably qualify as implicitly categorical, but can have arbitrary many values.
I find the definitions in 3.2.2 hard to follow and possibly an illustration would help, or maybe a reasoning why these are good criteria.

The choice of the channel-wise encoding of categorical variables seems odd, in particular since it seems that one category per variable is special, since it is the category with all the continuous features associated with it, while the others are permutation invariant - except that they depend on the permutation of the other features. The paper doesn't suggest an ordering of the categorical features, so this seems a bit strange.

The paper states that the current state-of-the-art on the Grinsztajn dataset is XGBoost, but I'm not sure if that is a fair characterization. Many of the works in the related work section simply have not been evaluated on this benchmark, as far as I know. As mentioned in the introduction, McElfresh showed that the gap between tree-based models and neural models is negligible for many datasets; I feel the phrasing in the rest of the paper should reflect that, in particular the second sentence of the introduction seems to contradict this.

Minor nitpicks
The phrase "natural base" was not entirely obvious to me when first used, maybe a different phrase or explanation when first mentioned.
The Sentence defining ResNet+C is just after the definition of the Fourier features, which is a bit confusing, and ResNet+F is not defined at all. I assume that is a typo?
In the conclusion, the paper states that it reports on the prevalence of implicitly categorical features, which I think the paper does not. It would be very interesting to study the prevalence more directly, but this seems not to be included in the paper.
I am also a bit ambivalent about the last statement about computational efficiency, since the paper uses a large search space and large computational budget to find good models.

### Questions
Was there a reason not to include learning rate, batch size and schedules in the searches for ResNet and the MLP? These seem quite important.
How was the threshold for including the one regression dataset chosen? Since the scores are not normalized, there is no special meaning to 0.1, is there?
How are categories ordered in the multi-channel encoding of categorical variables?
Why was a 1x1 convolution resnet chosen, and how would it compare against a standard resnet? In particular, any resnet would not be permutation invariant with respect to features because of the skip connections, right? [if the number of hidden units was chosen as the number of features, which is quite smiliar to the 1d case in some sense]
Is there a reference for the p-range metric?

### Soundness
3 good

### Presentation
3 good

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
The authors consider the problem of the gap in performance of deep learning methods on tabular datasets compared to the best non-DL methods, i.e., tree-ensembles like xgboost.

They theorize that two key aspects not fully explored previously should be addressed: implicit categorical features, and heterogeneity of the data when it comes to tabular data. 

They propose an approach consisting of 1D convolutional neural nets with residual connections, in combination with identifying implicit categorical features and encoding them, and including learned fourier features. 

They experimentally evaluate the proposed approach on the same set of datasets and experimental setup as a prior work and demonstrate significant improvement with the proposed neural net approach, showing competitive or even better performance than the other DL methods and best non-DL methods

### Strengths
-The work is introduced very well - the motivation is clear and the existing work is very nicely summarized.  

-The authors show impressive results with the proposed method - showing improved accuracy / R2 score on average across many datasets

### Weaknesses
 -None of the methods are defined or explained in enough detail to understand what is being done and reproduce the results.  I.e., the particular model used and how it is applied, the fourier features, and the implicit categorical feature selection - none of these are clearly explained or described in enough detail to reproduce what was done.  Furthermore, what is described does not make much sense the way it is currently described.  As one example, it's stated at the beginning of modeling, a 1D CNN resnet is used - but not how this is applied to tabular data (which is not typical), what the architecture looks like or math equations, etc.  A machine learning practitioner would typically not think of applying convolution to tabular data, and the "how" and "why" of this is never explained.

-There doesn't seem to be much novelty.  Most of the proposed elements were used in prior work, including learned fourier features, resnets, and identifying implicit categorical features (indeed Grinsztajn et al., 2022 included identifying implicit categorical features as part of their data processing pipeline, as can be seen in their publicly-released code as well). The exact same dataset and experiment setup is taken from prior work and it seems like this particular method is just plugged in.  Perhaps this particular way of applying 1D convolution has not been tried with tabular data before - I can't tell because it's not completely clear what exactly was done.  Even so the novelty is very limited.

-There is no rational or explanation given for why something was done or why it might work / did work, and most of the proposed methods don't intuitively make sense.  E.g., why is chi-square test used to determine if a feature is implicitly categorical or not?  What is the rationale?  How does this make sense?  Similar how does it make sense to use 1D convolution with tabular data?  How does the excessive 0-padding make sense - if every numerical feature is also 0 padded to the maximum number of categories?  What about for the fourier features.
--Similarly, there is no analyses of results or understandings given for why anything proposed worked and how it relates to the original motivating claims.

-It's not clear how the different proposed components contribute to the improved accuracy - ideally there should be ablation study and more experiments understanding the impact of the different components. 
 E.f., the different components before the neural net (identifying implicit categorical features, fourier feature transforms) should be used with other models as well, and the impact of the particular CNN model should be understood based on how it performs with and without each component as well.

-Some claims are unsubstantiated.  E.g., the authors state: "Grinsztajn et al. (2022) and Ng (2004) before them, establish that tabular data tends to lie in a natural base and that models which are invariant to rotation, such as the MLP, suffer from a higher sample complexity in the presence of noise. For this reason we select a 1D convolutional Residual Network (RESNET) to be our baseline and primary architecture since 1D convolutions are not invariant to arbitrary rotations or permutations of the data."  However, they do not show or cite that 1D CNN resnets are not invariant in the same way that MLPs are.  Since MLPs are a superset of CNNs (i.e. CNNs are MLPs with a special structure) - I doubt this claim.  The work that is cited does not mention CNNs at all.

-I don't feel that using results based on random hyper parameter search is the most reasonable way to compare the different methods, as it's not what is typically done in practice.

### Questions
1D convolutional neural net - why is it not rotationally invariant but MLP is (MLP is a superset of CNN)?

How is the 1D convolution applied to the tabular data?

why not use the other models / mlp like before to see if the only improvement is from that, or do the proposed changes help universally?

why is chi-square test used to determine if something is categorical?  

Learned fourier features and similar were already used in past work - what's new here?

ResNet + F is never defined - what is it?

"truncation of the number of samples to 10k or 50k features," must be a typo

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces two feature processing techniques - implicitly categorical feature identification and Fourier embeddings for tabular data.

### Strengths
- The paper is well presented.
- Evaluations are intensive/solid with good analysis.

### Weaknesses
 - There's is limited technical contribution in the paper. 
- The method here is more like feature engineering work that requires a lot of tuning to perform well.
- The performance improvement is marginal compared to XGBOOST.

### Questions
- Did the method use all data or only train data for categorical feature identification?
- Does the model take into account any bias in train/test distribution? 
- There are some heuristic methods [1] that also discretise numerical features using, e.g., log transformation/binning rare features into one feature. It is interesting to see how such naive method compared to the proposed method.

[1] Juan, Yuchin, et al. "Field-aware factorization machines for CTR prediction." Proceedings of the 10th ACM conference on recommender systems. 2016.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
**The paper focuses** on classification and regression problems on tabular data.

**The paper proposes** two modules for handling continuous features before passing them to a *custom convolutional ResNet-like backbone*:
- ICF (Implicit Categorical Features):  a technique for identifying "implicit categorical features" (the term introduced in the paper)
- LFF (Learned Fourier Features): an adaptation of Fourier Features ("Fourier Features Let Networks Learn High Frequency Functions in Low Dimensional Domains" by Tancik et al.)

**The main claim:** *"Our proposed feature processing and method achieves a performance that closely matches or surpasses XGBoost on a comprehensive tabular data benchmark."*

### Strengths
- The research direction is important: for tabular deep learning methods, it is crucial to properly handle continuous features.
- The concept of "Implicitly Categorical Features" is potentially interesting.
- The size of the used benchmark is a strength.
- I also appreciate that experiments were run with multiple random seeds.

### Weaknesses
Unfortunately, the paper has several major issues.

**(1) The key related work `[1]` is not properly positioned and compared against.** Unfortunately, this issue is serious:
- this submission and `[1]` have the same call for action: "let's improve how continuous features are handled by embedding/encoding them". The specific wording and informal perspective are different (in this submission, the "implicit categorical feature" perspective is suggested, while in `[1]` the motivation is more "empirical"), however, I see it as a stylistic difference: the call for action and the explored schemes are the same in nature.
- the "ICF" methods and piecewise-linear encoding from `[1]` are formally different methods, however, on the low technical level, both aim to identify a chance to discretize a given continuous feature; the core idea of splitting the continuous space into segments is shared, and the novelty of the specific splitting method is not sufficiently highlighted or justified. Furthermore, the paper does not explore the impact of different discretization strategies, such as adaptive binning or tree-based splits, which are common in the literature.
- the LFF method is very similar (identical?) to either "Periodic" module from `[1]` or to Fourier Features themselves `[2]`. The paper does not provide a rigorous analysis of the differences, if any, between the proposed LFF and these existing methods. Specifically, the choice of frequency parameters and the impact of different activation functions within the LFF module are not discussed in detail, making it difficult to assess the true contribution of this component.

To sum up, from my perspective, the key related work is not identified as such, the methods from this submission are similar to those from that related work, and the existing methods are not included as baselines.

**(2) The paper introduces a custom non-trivial architecture which seems to be unrelated to the main topic of the paper.** Specifically, in the second paragraph of Section 3, a custom architecture is introduced without any further discussion (also, to me, the usage of *convolutions* on tabular data problems is not intuitive and deserves its own discussion, or even its own paper). The choice of a ResNet-like architecture with 1D convolutions is not well-motivated for tabular data, where interactions between features are often more complex than sequential patterns. The paper lacks a clear explanation of why convolutions are suitable for this type of data and how the specific architecture was chosen, including the number of layers, filter sizes, and activation functions. Furthermore, the paper does not provide any ablation studies to justify the architectural choices, making it hard to understand the impact of the custom architecture on the overall performance. Unfortunately, it makes it hard to understand what is the core factor behind the reported results: the new architecture, the proposed methods or a combination thereof. I highly recommend to test the proposed methods on *existing* backbones (e.g. MLP and Transformer from `[3]`).

**(3) Regarding the presentation,** I should admit that I understand the proposed methods and the backbone to the extent that is enough to write this review, but not enough to actually implement the methods and explain them to others. The description of the ICF method lacks sufficient detail, particularly regarding the specific criteria used to identify "implicit categorical features" and the exact discretization process. The paper does not provide clear pseudocode or algorithmic descriptions, making it difficult to reproduce the method. Similarly, the LFF method's implementation details, such as the choice of frequency parameters and the specific Fourier basis functions used, are not sufficiently explained. The lack of clear definitions and implementation details makes it challenging to assess the true novelty and effectiveness of the proposed methods.

**(4) Experiments & Methodology.** 
- no baselines beyond MLP and XGBoosts
- some of the datasets are represented multiple times in different forms. It makes the benchmark biased towards the repeated datasets and the notion of "the number of datasets" becomes less obvious.
- etc.

To be more specific, let's consider Figure 1:
- the figure presents 16 results, however, after removing duplicated datasets, only 11 results are left.
- In the light of `[1]`, there are no performance gaps on the following datasets: covertype, eye movements, house 16H (also, the "eye movements" dataset contains a leak and is solvable with almost perfect accuracy; it is not a well known fact though).
- On three (OnlineNews, wine quality, nyc-taxi) of the remaining 8 datasets, XGBoost wins.
- Error bars are not presented, so it is hard to judge how significant the remaining 5 wins are.
- Baselines are missing, so it can be the case that the remaining wins can be achieved with prior methods.

### Questions
-

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper discusses a method for deep learning on tabular data. The essence of the method is to design novel types of trainable embeddings for the data at hand, that can be. then presented to a deep net.

We have two types of propositions:

1. Categorical embeddings which are derived by comparing statistics of the data to some reference/threshold value.
2. Fourier embeddings, which are obtained through a dense or 1X1 conv. linear and then application of a Fourier transform.

The scheme is end-to-end-trainable.

### Strengths
A novel method that is very useful and probably impactful in the field. 
A sound approach that is well motivated and with correct derivations.
An experimental evaluation that is convincing, as it entails many datasets and comparisons to logical benchmarks methods.

### Weaknesses
Some further discussion on related work, e.g. using Transformers for tabular data, is certainly needed. This is a must for acceptance, even after the rebuttal/revision phase.

### Questions
How does your method compare to Transformer-based methods for tabular data?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
