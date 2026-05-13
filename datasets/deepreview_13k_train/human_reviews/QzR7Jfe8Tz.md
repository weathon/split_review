# ALPBench: A Benchmark for Active Learning Pipelines on Tabular Data

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
In settings where only a budgeted amount of labeled data can be afforded, active learning seeks to devise query strategies for selecting the most informative data points to be labeled, aiming to enhance learning algorithms' efficiency and performance. Numerous such query strategies have been proposed and compared in the active learning literature.
However, the community still lacks standardized benchmarks for comparing the performance of different query strategies.
This particularly holds for the combination of query strategies with different learning algorithms into active learning pipelines and examining the impact of the learning algorithm choice. To close this gap, we propose \tool, which facilitates the specification, execution, and performance monitoring of active learning pipelines. It has built-in measures to ensure evaluations are done reproducibly, saving exact dataset splits and hyperparameter settings of used algorithms. In total, \tool consists of \numdatasets real-world tabular classification datasets and 5 active learning settings, yielding 430 active learning problems. To demonstrate its usefulness and broad compatibility with various learning algorithms and query strategies, we conduct an exemplary study evaluating \numquerystrategies query strategies paired with \numlearningalgorithms learning algorithms in \numsettings different settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces and illustrates ALPBench, which is a benchmark for reproducible active learning pipelines that covers 86 modern, tabular classification datasets, together with a wide variety of base leaners, query strategies, and setups.

### Strengths
The paper fills in a clear gap in today's landscape of active learning for tabular data. The work is reasonably original (for an evaluation framework), clearly presented, and with the potential of having a high-impact in standardizing empirical validations (while also making them apples-2-apples). The wide availability of ALPBench would greatly impact future AL evaluations: far too many of the newly submitted AL papers stop after an arbitrary nmb of queries, w/o any indication on whether or not the achieved performance is in any way meaningful.

### Weaknesses
While the paper goes a long way towards standardizing the evaluation of active learners, it can be improved along tow main directions:
1. First of all, instead than the "[somewhat] dry analysis" of the aggregated results in Figures 2 & 3 (which are excellent, but could go into an APPENDIX as supporting evidence), the paper would greatly benefit from a illustrative, step-by-step example of how to use ALPBench in a real-world scenario. Assume that you have a novel tabular dataset NTD for which active learning is essential. Ideally, you would like to follow  a procedure such as (i) identify which base learner BL performs best on NTD - after all, you what to reach SOTA performance with minimum data-annotation cost, (ii) identify which of the existing querying-strategies Q works best with BL for NTD, (iii) identify other datasets have properties similar to NTD, such as having Q+BL as a winner, and (iv) if the results are not satisfactory, invent a novel QS that will deliver better performance that Q+BL, add it to ALPFBench, and re-evaluate. In this scenario, the paper should provide guidance on how to add a new dataset or QS to ALPBench (assuming that it is possible), how to choose between ACC vs AUC metrics, how to choose the best base learner, etc. Similarly, the current insights on what works best for binary vs multi-class, small vs large setup, and the various base learners should be consolidated in a Lessons Leaned section (rather than spread throughout the paper)  
2. along the same lines: (i) the paper should provide a table with the SOTA performance on each dataset; that is, which base learner is the best when trained/tuned on all available training/dev data, and (ii) the paper should provide an additional set of metrics that measure how many queries does the best AL approach need to reach 50%, 75%, 90%, 95%, and 99% of the SOTA performance in "(i)". This guarantees that we are doing AL for the right reasons (ie, reach SOTA-adjacent performance with as few labeled examples as possible), rather than measuring "wins" after an arbitrary number of queries

### Questions
1. In each row from Table 2, please clarify 
    (i) how many of the "capabilities" in the previous four approaches are covered by ALPBench  
    (ii) which are missing and why (eg, for QS-Hybr, two of the previous approaches cover 4, while you only cover 3; what is the overlap among them?)

2. line 371: how big are the datasets that you have excluded? given that you have included them in ALPBench, you should -at the very least- give the reader a sense of the challenges/costs/time-constraints/ideal-setup of running experiments at that scale.

3. In how many of the experiments is the performance of the base learner impacted by the 180 secs limit? If this is a real issue, you should have mentioned it at the very beginning of the Experimental Results. 

4. is it possible to add to the current QSs two classic strategies such as Query-by-Bagging and Query-by-Boosting? See Abe & Mamitsuka, ICML-1998, "Query Learning Strategies Using Boosting and Bagging."

5. In Fig 4, is KNN the best base learner on those 3 datasets? if not, should we care about the erratic perfornace?

6. Is ALPBench "automatically detecting & reporting" situations in which, after a number of queries, AL hurts rather than helps (as in "5." above") 

7. how difficult would it be to extend ALPBench to cover additional scenarios, such as (i) simulating the stream-based scenario, (ii) interleaving AL and semi-supervised learning, and (iii) multiple-view learners?

OTHER:
line 206: please explain intuitively what is epistemic uncertainty; in its current form, it is a bit of a "circular definition:" 
              "epistemic uncertainty sampling (EU) (Nguyen et al., 2019) samples instances that have the highest epistemic uncertainty."

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
The paper proposes a benchmark for active learning methods
for tabular data. Esp. propose the authors to study active
learning not just for a single down-stream model, but
for a wider selection such as xgboost, catboost, SVMs,
MLPs etc. They suggest to evaluate three different
active learning regimes described by the size of the initial
labeled set, the batch size and the overall budget.
In experiments they compare different active learning
methods with different down-stream models on different
evaluation metrics in different such regimes.

### Strengths
- s1. interesting aspect: looking systematically at different down-stream
  models.
- s2. promised a pip installable python module that should be easy to use.
- s3. well written.

### Weaknesses
 - w1. there is not much innovation in this benchmark besides
  just scaling to more downstream models and more datasets.  
- it is not clear which problems the authors had to solve
  to arrive at the current benchmark.
- what are the limitations of current benchmarks, besides
  looking at fewer down-stream models and datasets?

- w2. how the three active learning regimes (tab. 1) have been
  chosen is not discussed.
- Esp. it is not clear how these different regimes manage to
  capture similar situations in different datasets. Are not
  30 initial samples for a very simple dataset much, but
  for a more difficult dataset very little?
  
- w3. it is not clearly demonstrated how this new benchmark
  now makes it easier to answer the three research questions
  asked.
- could we not just have used any of the existing benchmarks
  and run it with your 8 downstream models? if not, can you
  describe why not, and how this is now different in your
  benchmark?

- w4. the maybe main question one would want to answer
  by looking at different down-stream models, namely
  should we use different active learning methods for different
  down-stream models, is not addressed.
- fig. 2 provides the best active learning pipeline. Not very surprising,
  gradient boosted decision tree models as down-stream models
  are found to perform best on average.
- from an active learning perspective, would it not be more interesting
  to ask the question for the conditional performance of the different
  active learning methods: given a method, say catboost, what are
  the best active learning methods? and esp. are they different
  if I choose different down-stream models, say an SVM instead?


--- added after the rebuttal

w1. limited innovation
- running the algorithms on more downstream model is "novel" in the sense
  that nobody did it before.
- but there is no difficulty that needs to be solved to do so.
- in this sense, there is limited innovation in the paper.

w2. similar AL regimes
- scaling the number of samples by class, not just absolutely, is standard
  procedure in many areas of ML, e.g., in few-shot-learning.
- besides number of classes, learning tasks vary a lot in difficulty,
  and this is not accounted for in your choice of AL regimes.

w3. no clear demonstration of usefulness of the benchmark.
- "standardized evaluation protocols, pre-defined settings, and logging 
  of seeds, exact splits, and model hyperparameters" is done already by 
  modern AL benchmarks, e.g., Lüth et al. 2023 and Ji et al. 2023.
  I think you will need another argument for yours.

w4. no  recommendations for per model active learning strategies.
- Yes, you are right, fig. 7 in the appendix I overlooked. 


### Questions
- q1. What is the main problem you had to solve to scale existing
  active learning benchmarks to more downstream models and
  more datasets?
- q2. How did you choose the three active learning regimes in tab. 1?
  How does this capture similar situations in different datasets?
- q3. How did the new benchmark make it easier to answer your three
  research questions? Did you arrive at different conclusion than
  those been drawn in earlier benchmarks?
- q4. What recommendations does your benchmark provide for
  chosing the best active learning method for a down-stream
  learner and based on what evidence?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposed a benchmark for active learning on tabular data, in particular, for tabular classification tasks. This aims to fix the issue of the lack of consistent benchmarks for evaluating various active learning methods in various settings with different combinations of learning algorithms and query strategies. The authors also attempt to perform extensive experiments to evaluate the effectiveness of the proposed benchmark.

### Strengths
S1: The authors proposed a benchmark to compare different active learning strategies for tabular classification tasks under various settings but in a consistent environment, which is important for performing fair comparisons across the research community.
S2: The benchmark integrates various datasets to compose a comprehensive benchmark, which covers a variety of settings for evaluating active learning strategies

### Weaknesses
W1: The scope of this paper is quite narrow, only focusing on tabular classification and only a subset of active learning strategies. However, ICML usually focuses on more general areas including computer vision and NLP. Considering that active learning strategies have been broadly used in those areas, it would be better to take those settings and solutions from those areas into account
W2: I think more learning algorithms should be included, such as the recently emerging transformer model for tabular data, such as the model proposed by "TabTransformer: Tabular Data Modeling Using Contextual Embeddings".
W3: I guess it would be better to discuss some surprising findings by using the proposed benchmark. Although the authors mentioned the decrease in performance in some settings in the experiment section, it would be better to discuss more on that aspect, in particular those ignored by existing studies, thus highlighting the necessity of the proposed benchmark.

### Questions
Q1: Can the proposed benchmark be generalized to other modalities and other emerging machine learning models?
Q2: Can the authors discuss more interesting findings that are ignored by existing studies?

### Soundness
3

### Presentation
3

### Contribution
3
