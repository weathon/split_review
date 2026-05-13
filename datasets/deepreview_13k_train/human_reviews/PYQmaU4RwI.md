# A Novel Dual of Shannon Information and Weighting Scheme

- Decision: Reject
- Scores: 1, 5, 6

## Abstract
Information theory has achieved great success in not only communication technology where it was originally developed for by Shannon but also many other digital fields such as machine learning and artificial intelligence. Inspired by the famous weighting scheme TF-IDF, we discovered that information entropy has a natural dual. We complement the classical Shannon information theory by proposing a novel quantity, namely troenpy. Troenpy  measures the certainty, commonness and similarity of the underlying distribution. To demonstrate its usefulness, we propose a troenpy based weighting scheme for document with class labels, namely positive class frequency (PCF). On a collection of public datasets we show the PCF based weighting scheme outperforms the classical TF-IDF and a popular Optimal Transportation based word moving distance algorithm in a kNN setting. We further developed a new odds-ratio type feature, namely Expected Class Information Bias(ECIB), which can be regarded as the expected odds ratio of the information quantity entropy and troenpy.  In the experiments we observe that including the new ECIB features and simple binary term features in a simple logistic regression model can further significantly improve the performance. The simple new weighting scheme and ECIB features are very effective and can be computed with linear order complexity.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper introduces the so-called  "troenpy" which authors call dual. But I doubt whether this is a proper terminology. This measure is applied to a weighting scheme for supervised document classification.  Simple mathematical properties are presented as Theorems without having any theoretical results. Apart from this, the paper only makes negligible contributions and completely ignores the fundamentals of information theory. Experiments are very limited, and events will not be enough for undergraduate assignments. Most of the paper is filled with trivial calculations.

### Strengths
Apart from the enthusiasm of the authors to conceive the idea and write this paper, I do not see any major strengths in this paper.

### Weaknesses
This paper introduces the so-called  "troenpy" which authors call dual. But I doubt whether this is a proper terminology. This measure is applied to a weighting scheme for supervised document classification.  Simple mathematical properties are presented as Theorems without having any theoretical results. Apart from this, the paper only makes negligible contributions and completely ignores the fundamentals of information theory. Experiments are very limited, and events will not be enough for undergraduate assignments. Most of the paper is filled with trivial calculations.

This paper completely ignores the various results in information theory, coding theory, and machine learning, where Shannon entropy plays an important role (see my questions below). Apart from some trivial calculations, the paper has no theoretical contributions. The motivations or mathematical significance of so-called measures of certainty are not very apparent. There were some classical generalizations of entropy as Renyi entropy exists in the literature, and though authors call this some kind of dual, no connections to existing literature were made. One can still appreciate the results without any mathematical backing, but this paper does not show any extensive practical applications--that too considering that Shannon entropy appears in so many applications from maximum entropy methods to reinforcement learning. Please see my question below.

### Questions
(1) Shannon entropy acts as a lower bound for the average code length for source entropy. What is the significance of "troenpy" here?
(2) Can you show how "trophy" has significance in asymptotic equipartition property? One can show that given a discrete-time stationary ergodic stochastic process X, - 1/n log(X1, X2,...,Xn) converges to H(X), almost surely. Can you establish such results with"troenpy"?
(3) What is the so-called "dual" of Kullback Leibler divergence? Will that divergence have any role as a "distance measure" of probability measures, and what happens to Pinsker Inequality?
(4) Maximum entropy plays an important role in machine learning and image reconstruction. Where does "troenpy" fit in here?  Does the maximum entropy distributions become "minimum troenpy distributions"?
(5) Does Shannon entropy play an important role in the characterization of typical sets? Where does "troenpy" fit in here?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper presents a new metric called "troenpy," which is designed to complement Shannon entropy. While entropy measures uncertainty, troenpy aims to quantify certainty. Additionnally, the authors suggest a new weighting method for documents with class labels, called positive class frequency (PCF). They demonstrate that this method significantly outperforms other existing methods.

### Strengths
1- The paper is well written and quite easy to follow 

2- The experimental seems to show the efficiency of the proposed method.

### Weaknesses
1.The paper currently lacks a rigorous theoretical foundation justifying the choice of log(1−p(x)) as the basis for troenpy. While some intuitive motivations are provided, they don’t fully explain why this particular transformation should be optimal or preferable over other possible functions, such as log(g(p(x))). To strengthen the paper, it would be helpful if you could provide a more formal theoretical analysis or justification for the choice of log(1−p(x)) over other alternatives. This could involve deriving troenpy from first principles in a way that demonstrates its uniqueness or optimality for measuring certainty. Such an approach would make troenpy more compelling by showing that this transformation is not only intuitively sound but theoretically motivated as well.

2.The paper’s methodological presentation is somewhat unclear in terms of focus. While troenpy is presented as the main contribution, it is ultimately used only as part of the Positive Class Frequency (PCF) weighting scheme, rather than being explored on its own. At the same time, other features, such as Class Information Bias and Binary Term Frequency, are introduced without a clear link to troenpy, which can dilute the focus of the contribution. To enhance clarity, it may help to more clearly separate the different contributions or to highlight how they relate to the central concept of troenpy. If troenpy is indeed the primary contribution, consider focusing on its properties and potential applications more directly, perhaps by exploring it in different contexts out of document classification or directly comparing it with other certainty measures. Alternatively, if the emphasis is on the PCF and the broader feature set for document classification, reframing troenpy as one component of a larger methodological toolkit could provide a more cmprehensive narrative.

### Questions
1- Given that entropy has broad applications across various fields, could you clarify whether troenpy has potential uses beyond document classification? The current scope is quite narrow, and identifying additional applications could help to better demonstrate its value and versatility.

2-  Does troenpy come with any theoretical guarantees that it is the optimal measure for assessing certainty? Could you clarify whether alternative formulations, such as using the logarithm of another decreasing function of p(x), might also be valid? Providing insights into the theoretical underpinnings of troenpy’s formulation would enhance its credibility.

3- Is the primary goal of your research to derive a new measure (troenpy) or to improve upon TF-IDF? If the intention is to present troenpy as a novel measure, it would be helpful to discuss potential applications beyond document classification, as this focus currently feels quite limited. Conversely, if the emphasis is on document classification, the paper leans toward being empirical in nature. It appears there is a mix of these two focuses, which makes the methodological framework somewhat unclear. Could you clarify your primary aim and the intended contributions of the paper?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Note added on December 3: I am glad that the authors found my review to be useful. I agree with them that the other review with a score of 1 is too extreme, in its score and its wording. However, the authors need to understand better the limitations of their submission, and what is required by a selective venue such as ICLR.

"We did have other successful applications such as the large language models, recommendation system and computer vision etc, which we treated elsewhere as a series of following work" is not a reason to accept the current paper. Acceptance should be based only on actual contributions, not on unsubstantiated claims or promises.

The experimental section of the submission is quite weak, as pointed out previously. The authors did not cite, and did not compare to, the state-of-the-art in the family of TFIDF-based methods for document classification. The BNS method is just one of these methods. It is the duty of the authors to do a careful literature search, and to convince reviewers that the submission includes fair comparisons with the previous best related methods. The submission does not succeed currently in this direction.

=============

This paper introduces a variation of entropy that can be called entropy of the complement probabilities, $-\sum_i p_i \log(1 - p_i)$. The paper uses this as a weighting approach for words in document classification, and gets better accuracy than using alternative weighting methods.

### Strengths
Entropy of the complement probabilities has not been studied before in the research literature, and makes sense as a useful measure. The experimental results are believable.

### Weaknesses
Section 3 and the experiments based on it are clear and persuasive. Section 4 is less clear.

The experimental work is actually very limited, using only seven small datasets and essentially copying the experimental design of just one previous paper.

Although this submission is interesting, it is about document classification based on bag of words, which is mostly obsolete given the availability of large language models which understand document semantics, and hence can classify text with much better accuracy.

015: Troenpy is not a "dual" in a precise mathematical sense. It is an interesting and novel variant.

053: This is a very incomplete summary of theoretical justifications for TFIDF. See also, among others, https://link.springer.com/chapter/10.1007/11575832_33, Deriving TF-IDF as a Fisher Kernel.

072: Cite and compare experimentally to previous methods that use odds ratios. See https://dl.acm.org/doi/abs/10.1145/1458082.1458119 "BNS feature scaling: an improved representation over tf-idf for svm text classification" and https://www.jmlr.org/papers/volume3/forman03a/forman03a_full.pdf "An Extensive Empirical Study of Feature Selection Metrics for Text Classification."

114: The new concept, troenpy, is similar to the so-called "one versus all" approach to multiclass classification (which more precisely should be called "one versus rest").

119: "It turns out that the integral is zero." This sentence seems out of context and unsupported. The whole paragraph 116 to 124 seems incomplete and not needed.

203: It use confusing to use the word "frequency" for a value such as d that is an integer count. Use the word "count" as on line 214.

285: The word "negentropy" may appear in the 1944 book by Schrodinger, but presumably not as a formal measure, since the book predates Shannon. Note that the reference is formatted incorrectly, since Schrödinger is the author's family name, not Erwin.

357: Binary term frequency is a standard approach for document classification. See http://kamalnigam.com/papers/multinomial-aaaiws98.pdf, "A Comparison of Event Models for Naive Bayes Text Classification."

403: Does the absence of a validation set mean that there is absolutely no hyperparameter optimization?

429: It seems that all methods use raw TF, i.e., raw word counts. It is well-known that log(TF) or some other squashing function of TF usually gives better accuracy. The reason is burstiness, as discussed in the paper mentioned above, "Deriving TF-IDF as a Fisher Kernel."

490: It is not good enough to just say that previous work used different datasets. Get or implement Wang's method and run it on your datasets.

502: The meaning of "adding" is not clear.

506: Do additional experiments to explain the error increase; do not merely speculate.

### Questions
015: Troenpy is not a "dual" in a precise mathematical sense. It is an interesting and novel variant.

053: This is a very incomplete summary of theoretical justifications for TFIDF. See also, among others, https://link.springer.com/chapter/10.1007/11575832_33, Deriving TF-IDF as a Fisher Kernel.

072: Cite and compare experimentally to previous methods that use odds ratios. See https://dl.acm.org/doi/abs/10.1145/1458082.1458119 "BNS feature scaling: an improved representation over tf-idf for svm text classification" and https://www.jmlr.org/papers/volume3/forman03a/forman03a_full.pdf "An Extensive Empirical Study of Feature Selection Metrics for Text Classification.

114: The new concept, troenpy, is similar to the so-called "one versus all" approach to multiclass classification (which more precisely should be called "one versus rest").

119: "It turns out that the integral is zero." This sentence seems out of context and unsupported. The whole paragraph 116 to 124 seems incomplete and not needed.

203: It use confusing to use the word "frequency" for a value such as d that is an integer count. Use the word "count" as on line 214.

285: The word "negentropy" may appear in the 1944 book by Schrodinger, but presumably not as a formal measure, since the book predates Shannon. Note that the reference is formatted incorrectly, since Schrödinger is the author's family name, not Erwin.

357: Binary term frequency is a standard approach for document classification. See http://kamalnigam.com/papers/multinomial-aaaiws98.pdf, "A Comparison of Event Models for Naive Bayes Text Classification."

403: Does the absence of a validation set mean that there is absolutely no hyperparameter optimization?

429: It seems that all methods use raw TF, i.e., raw word counts. It is well-known that log(TF) or some other squashing function of TF usually gives better accuracy. The reason is burstiness, as discussed in the paper mentioned above, "Deriving TF-IDF as a Fisher Kernel."

490: It is not good enough to just say that previous work used different datasets. Get or implement Wang's method and run it on your datasets.

502: The meaning of "adding" is not clear.

506: Do additional experiments to explain the error increase; do not merely speculate.

### Soundness
3

### Presentation
3

### Contribution
3
