# ALMANACS: A Simulatability Benchmark for Language Model Explainability

- Decision: Reject
- Scores: 8, 6, 3, 3

## Abstract
How do we measure the efficacy of language model explainability methods?
While many explainability methods have been developed, they are typically evaluated on bespoke tasks, preventing an apples-to-apples comparison. To help fill this gap, we present ALMANACS, a language model explainability benchmark.
ALMANACS scores explainability methods on simulatability, i.e., how well the explanations improve behavior prediction on new inputs.
The ALMANACS scenarios span twelve safety-relevant topics such as ethical reasoning and advanced AI behaviors; they have idiosyncratic premises to invoke model-specific behavior; and they have a train-test distributional shift to encourage faithful explanations.
By using another language model to predict behavior based on the explanations, ALMANACS is a fully automated benchmark.
We use ALMANACS to evaluate counterfactuals, rationalizations, attention, and Integrated Gradients explanations. Our results are sobering: when averaged across all topics, no explanation method outperforms the explanation-free control.
We conclude that despite modest successes in prior work, developing an explanation method that aids simulatability in ALMANACS remains an open challenge

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Simulatability refers to (a human’s) capability to predict model behavior on unseen outputs. Improving simulatability has been considered an important goal for interpretability methods. This paper introduces a new benchmark to automatically evaluate simulatability for interpretability methods, using GPT-4 as a stand-in for humans. Notably, this new benchmark focuses on non-objective tasks with safety-relevant questions.

### Strengths
This paper is well-written and easy to follow. By focusing on safety-relevant, non-objective questions, the benchmark differentiates itself well from existing work on interpretability evaluations. The focus on distribution shift also makes the evaluation more realistic than some of the existing work. Overall the paper presents a well-executed idea with very clear motivation.

### Weaknesses
As the authors acknowledged, the use of GPT-4 as a stand-in for human annotators limits how much we can take away from the evaluation. Although the paper frames ALMANACS as a benchmark, I find it more suitable to call it a dataset—only when paired with a good-enough human approximator like GPT-4 would it become a benchmark. The lack of user study makes it difficult to judge the evaluation results conducted with the new dataset. But I think the dataset is an interesting starting point for future user studies.

### Questions
Given the predictor is GPT-4, it seems like the benchmark can be applied to interpretability goals beyond simulatability. Any thoughts on that?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents ALMANACS, a language model explainability benchmark that measures the efficacy of different explanation methods. The benchmark focuses on simulatability, which evaluates how well explanations improve behavior prediction on new inputs. ALMANACS consists of twelve safety-relevant topics with idiosyncratic premises and a train-test distributional shift. The authors evaluate counterfactual, rationalization, and salience-based explanations using another language model as a predictor. The results show that, on average, no explanation method outperforms the explanation-free control, highlighting the challenge of developing explanations that aid simulatability.

### Strengths
- The paper addresses the need for a consistent evaluation standard for language model explainability methods.
- ALMANACS provides a benchmark that measures simulatability, a necessary condition for faithful and complete explanations.
- The benchmark includes safety-relevant topics and a train-test distributional shift to encourage faithful explanations.
- The use of another language model as a predictor enables fully automated evaluation, speeding up the interpretability algorithm development cycle.
- The paper presents results that highlight the limitations of current explanation methods and the open challenge of generating explanations that aid prediction.

### Weaknesses
 - The paper only evaluates the explanation methods based on Kullback-Leibler divergence (KLDIV) and total variation distance (TVDIST). While these metrics provide insights into the performance of the methods, they may not capture all aspects of explanation quality. Specifically, these metrics focus on the distribution of probabilities, but do not directly assess the alignment of explanations with human-understandable reasoning or the faithfulness of explanations to the model's decision-making process. For instance, an explanation could achieve a low KLDIV or TVDIST score by simply predicting a uniform distribution, which would not be a meaningful explanation.
- The paper acknowledges that the automated evaluation using language models may not be consistent with human evaluation. Human studies are still needed to validate the results and determine if humans can succeed where language models fail. The concern is that the language model predictor might be learning spurious correlations or biases in the explanations, rather than genuine simulatability. This could lead to misleading conclusions about the effectiveness of different explanation methods. The paper should include a discussion of the potential limitations of using a language model as a proxy for human understanding.
- The paper evaluates only three explanation methods (counterfactual, rationalization, and salience-based). While these methods are commonly used in explainability research, there may be other methods that could be valuable to include in the benchmark. For example, methods based on perturbation analysis or concept activation vectors could provide different perspectives on model behavior and might reveal different strengths and weaknesses of the explanations. The lack of diversity in explanation methods limits the scope of the benchmark and its ability to provide a comprehensive evaluation of explainability techniques.

### Questions
None

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This submission introduces ALMANACS, a novel benchmark tailored for evaluating the explainability of language models via a concept termed "simulatability." Using GPT-4 as a predictor, the benchmark assesses how well GPT-4 can simulate other language models that employ various explanation methods. Simulatability is defined by measuring the distribution distance between the outputs of GPT-4 and the target language model for previously unseen test tasks. A noteworthy finding is that the incorporation of explanations does not invariably enhance explanation performance for unseen inputs.

### Strengths
The paper innovatively offers a benchmark with a quantitative metric for assessing explainability in language models. Furthermore,it is interesting for the discovery that models with explanation input do not outperform non-explanatio in terms of simulatability.

### Weaknesses
The primary focus of this paper appears to be on the introduction of the ALMANACS benchmark. Yet, the utilization of well-established distance measures like KLDiv and TVDist doesn't add a novel dimension to the study.

The observation that explanation techniques might not always heighten performance on unseen data is compelling, but the paper would benefit from a deeper analysis and discussion on the possible reasons behind this phenomenon.

The term "simulatability" appears to be inconsistently defined, leading to confusion. The initial definition of simulatability is "how well the explanations improve behavior prediction on new inputs". Subsequently, it seems to change to a definition centered on distribution distance, KLDiv or TVDist.

The paper doesn't provide a convincing argument for why simulatability is a good metric for language model explainability. Many factors can influence predictor outputs. Given that GPT-4 operates as a black box, it's hard to say GPT-4 predict solely to the presence or absence of explanations without providing additional constraints. This point is underscored by results from the NoExpl vs Expl comparison in Table 1, which indicates low KLDiv scores, hinting that GPT-4's predictions might be independent of input explanations.

### Questions
1. Could the authors provide the precise definition of "simulatability"?
1. The choice of GloVe embeddings for demonstration retrieval appears outdated. Have the authors considered more recent sentence embeddings, such as SimCSE?
1. There seems to be a discrepancy between the comparison results for NoExpl in Figure 4 and Table 1 (PredictAverage vs NoExpl). PredictAverage outperforms NoExpl in Figure 4 but does not in Table 1. 
Could this be clarified?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces ALMANACS, a new benchmark for evaluating explainability methods for language models. The key ideas are:

-ALMANACS measures the simulatability of explanations, i.e. how well they help predict model behavior on new inputs. This relates to the desired properties of faithfulness and completeness.
-The benchmark comprises 12 topics with safety-relevant scenarios. Questions are non-objective and designed to elicit complex, nonlinear behavior from models.
-There is distributional shift between train and test sets to require generalization.
-The authors test counterfactual, rationalization, and salience-based explanation methods. None consistently improve upon a no-explanation baseline, indicating simulatability on ALMANACS remains an open challenge.

### Strengths
(1) Partially addresses the need for standardized benchmarks to evaluate and compare explanation methods.

(2) Simulatability is a useful metric directly related to explanation quality. 

(3) Automated evaluation enables efficient benchmarking.

(4) Non-objective questions and distribution shift require explanations to provide true insight rather than leveraging correlations.

### Weaknesses
 (1) Only safety-relevant scenarios are included and this is not general. 

 (2) The choice of language models for evaluation versus being explained may affect results. More analysis of this factor could be useful.

 (3) Automated evaluation using a language model proxy for humans has limitations vs. human studies. Direct comparisons would be needed to validate the benchmark.

 (4) Testing on more model sizes, scaling effects, and model families instead of just focusing on flan-alpaca-gpt4-xl and vicuna-7b-v1.3.

### Questions
Missing references for explanation distillation:

(1) Li et al. Explanations from Large Language Models Make Small Reasoners Better. 2022.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
