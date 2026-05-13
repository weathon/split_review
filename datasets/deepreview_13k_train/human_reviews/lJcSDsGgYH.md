# Large Language Model Confidence Estimation via Black-Box Access

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Estimating uncertainty or confidence in the responses of a model can be significant in evaluating trust not only in the responses, but also in the model as a whole. In this paper, we explore the problem of estimating confidence for responses of large language models (LLMs) with simply black-box or query access to them. We propose a simple and extensible framework where, we engineer novel features and train a (interpretable) model (viz. logistic regression) on these features to estimate the confidence. We empirically demonstrate that our simple framework is effective in estimating confidence of Flan-ul2, Llama-13b and Mistral-7b on four benchmark Q\&A tasks as well as of Pegasus-large and BART-large on two benchmark summarization tasks with it surpassing baselines by even over $10\%$ (on AUROC) in some cases. Additionally, our interpretable approach provides insight into features that are predictive of confidence, leading to the interesting and useful discovery that our confidence models built for one LLM generalize zero-shot across others on a given dataset.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the problem of uncertainty quantification in language model responses using only black-box access to the language model. In order to quantify uncertainty, the authors study many different ways of varying outputs: they sample from the same prompt using different strategies, paraphrase the prompt via backtranslation, reorder sentences, repeat sentences, remove stopwords, and measure whether parts of the outputs entail other parts using an NLI model. They then convert the outputs of these perturbations into features (using different methods for different sources of variation), and finally train a logistic regression model on these features to predict “confidence”. The paper then runs experiments on Flan-ul2, Mistral 7B instruct, and Llama 2 13B. They find that their method outperforms baselines (such as studying semantic sets and lexical similarity, measured by AUROC), and that the feature that matters most in the regression model is typically the number of “semantically” equivalent sets of outputs sampled from the prompt.

### Strengths
* This paper studies an important problem; assessing uncertainty in the language model’s output space. And they do so for open-ended generation tasks like summarization where uncertainty quantification is much harder (since you cannot look at the entropy at a specific token)
*The authors have a wide-range of experimental analysis in different settings
* Some of the findings I thought would be useful to the community — for example, I thought it was interesting that repeated sampling from the original prompt yields more useful features than perturbing the prompt (and I would be interested to see how this can be extended in a maximally sample-efficient way).

### Weaknesses
 * The primary weakness is the use of rouge score (a metric on top of n-gram overlap with ground truth summaries) for evaluation. Many of the perturbations, such as mixing up or repeating sentences with entities, help capture how entities are processed into the output (which rouge disproportionately captures), rather than actual correctness.
* The procedure the authors propose is very inefficient; it requires many repeated samples from the language model. It also is not clear if this extra compute is deployed optimally; for example, it could be better to deploy more compute into stochastic decoding. 
* There are a number of ways the presentation could be improved. For example, the paper introduces the notion of confidence in the intro using lots of notation, but uses no notation to explain the (somewhat complicated) methods of extracting features for the logistic regression classifier. 
* I’d also encourage the authors to draw from some related work in estimating the confidence / probability of correct (e.g., [1] and [2] have studied this formally).

### Questions
* Do you expect the gains over the baselines to remain as large using a different evaluation criteria, such as using e.g., Llama 3 70B as a judge of correctness? 
* Do you expect the results to extend to frontier systems (where we only have black-box access)?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
edit Dec. 2: Score change from 5 to 6.

The authors introduce a framework to obtain confidence or P(correctness) values to score sampled responses from a black-box model (no access to weights, logits, or log-probs). The method is essentially using several different strategies, including non-deterministic sampling, prompt modification, and response splitting, to produce a small set of responses, and determining consistency among them via semantic and lexical metrics. The strategy-metric pairs each receive their own score, and these scores are used with a logistic regression model to obtain the final confidence (calibrated to a dataset-model pair). This method extends and generalizes work such as "Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation." (Kuhn et al., 2023).

The authors benchmark on a mid-sized set of LLMs and datasets, obtaining good performance compared to other black-box baselines, and demonstrate that the logistic regression model is able to show the relative importance of different metrics in determining confidence. Furthermore, they show that the trained logistic regression models may generalize on the same dataset across the results from different LLMs.

### Strengths
1. Simple, extensible framework for wrapping black-box confidence scoring techniques into a meta-scorer, presented with several existing and novel confidence scoring techniques.
2. Useful interpretability results.
3. Good communication of approach, drawbacks, and strengths.

### Weaknesses
1. In 083, it is claimed that because the models used to produce predictions are simple, the confidence estimates will be well-calibrated. I think this claim needs support; in particular, the paper might make use of ECE (expected calibration error) and/or other calibration metrics to assess the calibration of different approaches including the newly proposed approach.
2. Results are hard to contextualize without error bars. It is unclear how much the randomness in the sampling procedure affects the final scores.
3. Baselines are mostly focused on previous black-box sampling-based baselines. While these are useful, many useful baselines are in fact missing. For example, on black-box models, elicited verbalized confidence (Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback, Tian et al. 2023) could be used. Also, why not try a frequency-estimated semantic entropy of the equivalence sets (Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation, Kuhn et al. 2023), instead of just the number of sets? Furthermore, open-source/whitebox approaches such as P(true) or finetuned P(IK) (both from Language Models (Mostly) Know What They Know, Kadavath et al., 2022) could easily be used on an auxiliary open-weight model (e.g. assessing the accuracy of a black-box response with a different open-source model). All of these metrics seem that they could be added as baselines and as inputs in the logistic regression finetune.
4. Scope of model evaluation is limited. This limits the impact of the conclusions, although it may not be addressable due to cost limitations.

Small nitpicks:
- Spelling and grammar: "aver to these values as a features (80-81), "complimentary ways" --> "complementary ways" (169), "greedy ," (149), "Since, " (083), etc.
- Communication: I think 3.1 should not be entitled "prompt perturbations" as not all of the methods for obtaining multiple different answers/answer portions to compare are actually prompt perturbations. Prompt perturbations, Stochastic Decoding, and split response consistency should maybe be referred to collectively as something like "Elicitation of multiple black-box responses" or similar.
- Communication: (383) "we use two metrics to evaluate effectiveness of the models: {description of metric 1}. {Description of metric 2}" should likely be a list with (a), (b), instead of two distinct sentences.

### Questions
1. Why not include scores like EigenValue, Eccentricity, or Degree in the logistic regression inputs?
2. Same-dataset, cross-model performance seems generally good. E.g. the same logistic regression weights can be reused for the same dataset with different models. Notably missing seems to be same-model, cross-dataset results. How important is it really to train this logistic regression model as compared to using, say, SP lexical similarity for everything?--or one fixed set of weights for everything?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
- This paper seeks to provide uncertainty measures for language models given on prompting access to them.
 - The basic method is to perturb a prompt using various heuristics (e.g., paraphrasing, duplicating sentences) and generating a set of features that feeds into a logistic regression.
 - Evaluation is done on 4 QA tasks on 3 models (Flan-ul2, Llama-13b, Mistral-7b), and there are gains over baselines.

### Strengths
- The problem of producing confidence estimates for language models is an important problem.
 - The idea of aggregating multiple different sources of information across prompts is a natural direction which seems fruitful.
 - Studying the transferrability across language models is important for having general-purpose calibrators.

### Weaknesses
 - The regime in which this paper operates could be more realistic. First, the models considered are relatively small models. Furthermore for these models, we actually have full white-box access, so evaluating methods that are meant for black-box access doesn't seem as well motivated. It would have been nice to see evaluations on closed API models (e.g., GPT-4, Claude, etc.). The contribution of this paper is fundamentally empirical, so the regime matters here.
 - The particular types of perturbations (e.g., paraphrasing) seem ad-hoc: why were these chosen and not others?  For each particular choice (e.g., paraphrasing), I also wonder about the execution - it seemed like relatively weak models were used and the paraphrasing wasn't effective. Also, regardless of what perturbations are chosen, there should be more analysis done about the effectiveness of each one (both in terms of downstream performance but in terms of whether the implementation of the pertubation actually produced the desired effects with valid outputs - e.g., paraphrasing where we don't just drop valuable content). I understand that the pitch is that this is a framework, but the framework is not novel; the contribution should be the choices of perturbation that lead to good results.
 - The cost of the method is not discussed. Compared to having to decode from the language model once, it seems like the method here is quite expensive and complicated; to know whether it is worth it, it would be good to document the costs, and in general, explore the cost-AUROC tradeoff.

### Questions
- Stochastic decoding and split response consistency really aren't prompt perturbations since they change the output, not the input. It seems like these should be pulled out into a separate section.
 - For paraphrasing, it was noted that Helsinki-NLP to do En->Fr->En did not preserve semantics. Why was Helsinki-NLP used?  It seems like using an LLM to do the translation or paraphrase could have worked - was this considered?
 - Sentence permutation could make the text invalid due to unresolved anaphora - can you comment on whether this was a problem?
 - Entity frequency amplification: why is there such an emphasis on named entities? I could imagine EFA and SP be generally applicable to any sentence. Is there some sort of empirical evidence that entities need to be treated specially?
 - For SRC, how was the NLI between the output computed?  This only works for long responses since the output needs to be split up into multiple parts? Why is NLI not computed on different samples instead? How does this relate to maieutic prompting (https://arxiv.org/pdf/2205.11822)?
 - The section on featurization (section 3.2) is a bit hard to follow; it would be nice to have an example.
 - Why do you think that the same features transfer across LLMs? Is it because there is a model-agnostic notion of example difficulty that is being captured here, or that models tend to make the same type of errors?
 - How important is the linear model assumption? I understand the desire for interpretability, but if you just cared about increasing AUROC, how far could you get by using non-linear models (for exapmle, https://arxiv.org/pdf/2006.09462 used random forests).
 - It would be interesting to compare your method to methods that use log probabilities (of other models):
   * https://arxiv.org/abs/2006.09462
 - While other papers that aggregate (e.g., https://arxiv.org/abs/2306.13063) are discussed in the related work, it would have been nice to see a more quantitative comparison.
 - Minor: use \citep (e.g., Goodfellow et al. (2016) in the first sentence) when the citation is used as a parenthetical.
 - 169: complimentary => complementary

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes a framework for black-box detection of correct vs incorrect LLM responses. The authors propose a set of input manipulation and decoding techniques to form a feature space. Using binary correctness labels, they train a logistic regression to derive confidence estimates that an answer is correct. Experiments shows good performance compared to baselines with respect to two metrics, for several QA datasets and LLMs. The simplicity of the logistic regression also consents to rank the importance of each technique on each dataset.

The paper is experimental in nature and is not backed by theoretical results.

### Strengths
- The techniques proposed in this paper are black-box, which make the work appealing.
- Results appear better than competitors across the board.

### Weaknesses
 - No theory to support the methodology. The proposed techniques feel reasonable, but there is no principle reason why they would strongly correlate with the correctness of the output in general. Clearly, using multiple techniques at the same time as authors do tend to mitigate this problem.
- Not fully clear to me how robust some of the featurization steps are, and how much manual intervention is needed to make things work for all dataset.

### Questions
- Perhaps the author could comment on the robustness of the featurization steps. How automatized is the process? How well does it work without intervention? Would it be possible to provide more evidence that the method is robust?
- The few instances where the presented approach is not better than the others are not the same for the AUROC and AUARC metrics. Why do you think this is the case? Combined with the fact that most often the improvement is only a few percentages, it makes me wonder whether averaging the results over three runs is enough. Would it be possible to use more runs and add standard deviations to make results more significant?

### Soundness
3

### Presentation
3

### Contribution
2
