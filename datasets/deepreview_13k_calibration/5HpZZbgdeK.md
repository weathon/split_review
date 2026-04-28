# Efficient calibration as a binary top-versus-all problem for classifiers with many classes

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6, 5

## Abstract
Most classifiers based on deep neural networks associate their class prediction with a probability known as the confidence score. This score is often a by-product of the learning step and may not correctly estimate the classification accuracy, which impacts real-world usage. To be reliably used, the confidence score requires a post-processing calibration step. Data-driven methods have been proposed to calibrate the confidence score of already-trained classifiers. Still, many methods fail when the number of classes is high and per-class calibration data is scarce. To deal with a large number of classes, we propose to reformulate the confidence calibration of multiclass classifiers as a single binary classification problem. Our top-versus-all reformulation allows the use of the binary cross-entropy loss for scaling calibration methods. Contrary to the standard one-versus-all reformulation, it also allows the application of binary calibration methods to multiclass classifiers with efficient use of scarce per-class calibration data and without degradation of the accuracy. Additionally, we solve the problem of scaling methods overfitting the calibration set by introducing a regularization loss term during optimization. We evaluate our approach on an extensive list of deep networks and standard image classification datasets (CIFAR-10, CIFAR-100, and ImageNet). We show that it significantly improves the performance of existing calibration methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors provide a conceptually simple and practical technique for the post calibration of trained models that could scale to the case of
many classes: they reduce the problem to one binary calibration problem (and not many calibration sub problems, such as often is the case in prior work). The paper contains a good discussion of prior work, and presents many empirical experiments and comparisons on vision data sets with up to 1000s of classes.

### Strengths
Calibration, or obtaining good or reliable probabilities, is an important task in many areas of machine learning.  Classification into many classes is challenging and occurs often in practice. The authors present a simple problem formulation and reduction that can be practical: that of calibrating the probability assigned to the highest scoring class (the 'confidence'). The paper is fairly clear, and many experiments
and in particular comparisons with other techniques are presented. The authors motivate their approach well (in particular, efficiency
considerations).

### Weaknesses
A major issue is weak novelty or contribution.  Another important issue (but somewhat secondary) is that the paper clarity is
somewhat poor too. I'll give a  summary below and then expand on these in the 'Questions' section.

Main issue with contribution: one would think in any practical application of calibration, one would be interested in good
probabilities assigned to top candidates, not just the very top (to make good decisions based on the classifications), but the authors
only focus on the very top in their development of the technique and evaluations (if I am not mistaken, and to keep the solution and the
evaluation simple..). Using the other scores should improve the calibration too.  I believe this severely limits the current contribution, and more research and development of the approach is required to make the paper a technically strong contribution.

### Questions
[roughly in order of importance]

With many candidate classes given an instance (eg 100s to 1000s), it
is understandable that one may not want to assign good probabilities
(waste time/resources on) on all the candidates, and focusing on the
top is well motivated (the issue of sparsity of data, for training or
calibrating per class, is understandable as well). However, it is also
not advisable to throw out all the information (all the scores
assigned to the classes), except the top (or the winning) class. For
instance, the spread (closeness) of the scores can be very
informative. Furthermore, in any plausible application of calibration
in this setting, for instance in subsequent decision theoretic
actions, plausibly one wants to know the probabilities assigned to the
other, top few, classes as well.


- not clear how binary methods (such as HB or Iso) are used alone, without TvA for
 calibration.. (eg in Table 1) TvA is used on the top score.. but use of the binary
 methods to this multiclass setting is not clear to me in the experiments.. I don't think the authors explained this.. and then
 the authors explain that the binary methods perturb the decision of the original classifier, etc. 

- What is a reference for "I-Max binning".. I believe it is first mentioned on page 7 (from my searching the paper..), and it scores
 very well.. (Table 1, on Imagenet dataset/models) Also: why include it if the probabilities can sum to more than 1.0 with this method ?
 (for some evaluation scores such as log loss, perhaps for ECE too, this could lead to cheating by a method...)

- the authors use 'confidence' (eg on page 4 when they say 'beyond
just considering confidence'), but they define it in passing on page 3
as 'the confidence is the top class probability' (top probability as
opposed to the probability assigned to other, non-top,
classes)... promote it or highlight this technical definition better
(because confidence is a generic term, but here in this paper, at
least from this point on, it has a more technical meaning... at least
after page 3!). For example, the use of 'confidence' in the abstract
(used 3 times) reflects the more generic meaning ...

other clarity comments:

- Intro is vague, for instance, in ".. to predict the true
probability of a good decision, i.e., their accuracy."  What is a
"good decision"? (is it committing to one class or label, for a given
test instance, and the label turning out to be correct? 'accuracy'
often has a technical term in machine learning, which is one minus
zero-one error, or the proportion of test instances correctly
classified.. so if the proportion is 80%, do we want the model to
also always assign a fixed 80% to its classifications? or a
probability that is more fine-grained than that (not fixed at
80%.. which can simply be obtained from cross-validation!) ).. I am
guessing the latter .. perhaps quick/short examples would clarify the statements.  Also the
distinction between 'uncertainty quantification' (at the beginning of
intro) and providing good probabilities or calibration is not clear
either (the techniques are mentioned with citations, but more
explanations would be useful).

-  could drop 'in our work' in "We are interested in our work in.."

- drop 'process' in 'a complementary post-processing
 calibration process'..

- In Related Work section, not sure what 'less complex than the other
 ones' means in the long sentence: 'the problem of confidence calibration, less complex
 than the other ones' (in what ways were the aforementioned citations
 more complex?)

- page 5: "We notice " to "We note " (the former implies you have
 observed something, in your work/experiments, etc. while the latter
 means you want the reader to note or observe something, and that's
 what you mean)

- change "one-vs-the-rest approach" to  "one-vs-rest approach"?

- the semantics of probability P() in equation 1 of 3.1 is not clear
 (in the sense of how it is computed, ie in what way or on what
 probability space, or how is it empirically estimated.. ) ... although
 the example you give afterwards helps. Perhaps insert "(when computed
 on unseen or test instances)" in "the probability of being correct
 when the confidence is ..", so it becomes ".. the probability of
 being correct (when computed on unseen or test instances) when the
 confidence is .."


- Top-versus-Rest (instead of Top-vs-All) ? (I understand one-vs-all
 is commonly used instead of one-vs-rest, and this follows a similar
 pattern)


- 3.3, page 4: the presentation/description of ECE should be
    improved, perhaps by a quick example ..

-  replace 'size' (in 'equal mass or equal size') with 'width'
 perhaps? as 'size' is ambiguous: it could mean bin extent or width,
 or number of points or instances (whose score fall) in the bin (what
 is meant by bin mass, I believe, is number of instances in the bin)..

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Paper proposes confidence calibration for multi-class classification as a single binary classification problem using top-vs-all approach. This gives ability to calibrate large number of classes with scarce per-class data, and the usage of binary cross-entropy loss with regularisation term. Benchmark image datasets are utilised to evaluate the proposed approach, showing stability in classification accuracy and calibration improvements against existing methods.

### Strengths
Paper proposes sound yet simple idea which improves the existing calibration approaches. It includes good set of experiments and evaluations to show the usefulness of proposed techniques. As model-agnostic approach, it would be possible to apply the algorithm to different existing neural network models and post-processing calibration techniques. This is an interesting idea that could bring some new knowledge to the field, especially from the practical view of uncertainty calibration.

### Weaknesses
Background and literature review could be in a more compact form. For now, it is repeated in many sections making the follow of the presentation a bit hard: Otherwise it is clearly written and structured. Paper lacks some of the analysis and discussion of the proposed approach and results in a broader sense. Also, it has limited discussion of the results in relation to practical utilisation of approaches, i.e., which of the proposed combination of algorithms should be selected in different scenarios from practitioners' perspectives. From empirical point of view, it would strengthen the paper, if additional dataset from other than image domain would be considered.

### Questions
- References lacks some details, please add all the relevant information to cited work (also for ArXiv pre-prints)
- What would be your conclusions or "rule of thumb" of selecting particular algorithm (i.e., calibration method with TvA) from the practitioners' point of view for certain applications or classification problem?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the calibration of multi-class classifiers trained to discriminate many classes. The proposal consists in using a binary top-versus-all approach: the calibration problem is transformed into providing a confidence estimate regarding whether the prediction made by the classifier is correct. The authors first provide a succinct state-of-the-art on calibration approaches, then present the classifier calibration problem, and present their contribution. Experimental results are provided, before the paper briefly concludes.

### Strengths
The paper is overall written in a clear and understandable manner, and is pleasant to read. 

The results displayed in the Experiments section are good and show that the proposal is interesting.

### Weaknesses
The contributions of the paper seem somehow rather restricted: the proposal consists in recasting the calibration problem into a binary problem (i.e., adjusting the level of confidence in the prediction issued by the classifier); there is no theoretical study. The proposal is not really formalized. 

The state-of-the-art does not include a number of works on classifier calibration, which may have been interesting to include in the discussions and in the experiments (see, e.g., Venn predictors).

Some parts in the paper are redundant—for instance, Sections 2 (related work) and 3 (problem setting) are tightly connected and may have been merged into a single one. Section 4 also mentions some related work which could have been presented and discussed previously. The notations are sometimes inconsistent (e.g., the authors use small x's and y's as well as capital ones interchangeably; as well, they indistinctly use "one-versus-all", "one-vs-the-rest", etc.)

### Questions
In Section 2, page 3, you mention "more advanced methods": can you be more specific ? As well, when referring to Gupta and Ramdas (2022) which first defines the top-label calibrator, their work should be presented with more details (here or in the "Problem setting" section) as it is highly connected to the proposal. 

In Section 3.2: "This discretizes the probability." This sentence is a bit clumsy; can you clarify ? 

In Section 3.3, you may also mention that the ECE is not a proper scoring rule. This also questions its use as a metric for assessing calibration performance. Could you provide any insight regarding this ? 

Section 4 should be improved. In its present state, it is hard to see what is exactly the proposal. In particular, I think that the proposed approach should be clearly and formally stated (and not only via Algorithm 1), notably by explicitly formulating the criterion used to replace Equation (1)—this would clarify the difference with the former top-vs-all proposal by Gupta and Ramdas (2022). 

In Section 4.1, could you elaborate on "minimizing the cross-entropy loss increases the probability of
the correct class (thus only indirectly decreasing the confidence), but minimizing the binary cross-entropy
loss directly decreases the confidence" ? 

In its current state, Section 4.2 is short, which is regrettable since it addresses the more important part in the paper—the properties of the proposal. The argument that "the [proposed] reformulation [of the top-vs-all approach uses] the full calibration dataset" could be discussed: then, the positive and negative classes are imbalanced (and heavily imbalanced in the case of numerous classes), which may degrade performances. Can you discuss this porential issue ? As well, the sentence "the classifier's prediction and accuracy are unaffected" is unclear; in addition, if the classifier's predictions are left unchanged compared to the one-vs-all case, it also means that your approach cannot improve the classifier's accuracy by righting erroneous decisions: can you elaborate on that ?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper propose tot improve the current calibration methods by convert it into a binary case under the one-versus-all setting and demonstrate that reformulating the confidence calibration of multiclass classifiers as a single binary problem significantly improves the performance of baseline calibration techniques.

### Strengths
It study the shortcome of many post hoc calibration problem and provide a better loss to improve post hoc calibration method.

### Weaknesses
This work provide a good and easy to improve most post hoc method, however it seems too simple. I would say it is more like a part of a post hoc method paper although the author give comprehensive experiments.

It would be better to include more metrics other than ECE.

I would suggest the author to include the TvA into training time calibration to see if it works.

### Questions
1. This work provide a good and easy to improve most post hoc method, however it seems too simple. I would say it is more like a part of a post hoc method paper although the author give comprehensive experiments.
2. It would be better to include more metrics other than ECE.
3. I would suggest the author to include the TvA into training time calibration to see if it works.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
