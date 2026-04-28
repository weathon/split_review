# An Empirical Analysis of Uncertainty in Large Language Model Evaluations

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
As LLM-as-a-Judge emerges as a new paradigm for assessing large language models (LLMs), concerns have been raised regarding the alignment, bias, and stability of LLM evaluators. While substantial work has focused on alignment and bias, little research has concentrated on the stability of LLM evaluators. In this paper, we conduct extensive experiments involving 9 widely used LLM evaluators across 2 different evaluation settings to investigate the uncertainty in model-based LLM evaluations. We pinpoint that LLM evaluators exhibit varying uncertainty based on model families and sizes. With careful comparative analyses, we find that employing special prompting strategies, whether during inference or post-training, can alleviate evaluation uncertainty to some extent. By utilizing uncertainty to enhance LLM's reliability and detection capability in Out-Of-Distribution (OOD) data, we further fine-tune an uncertainty-aware LLM evaluator named ConfiLM using a human-annotated fine-tuning set and assess ConfiLM's OOD evaluation ability on a manually designed test set sourced from the 2024 Olympics. Experimental results demonstrate that incorporating uncertainty as additional information during the fine-tuning phase can largely improve the model's evaluation performance in OOD scenarios. We hope this work can draw broader research attention to the stability of LLM evaluators.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
While the importance of measuring and handling uncertainty and confidence with LLMs is a known and well-researched topic, this paper seems to be the first to analyse uncertainty and evaluation confidence within the particular 'LLM-as-a-judge' (LLMJ) setting. It runs a series of experiments that yield a series of empirical observations related to uncertainty of LLMs when used as evaluators, and then it aims to show that incorporating uncertainty modeling directly into the process of creation of LLM-based evaluators can yield more confident and better-performing evaluators. Evaluations are conduced with a reasonable number of well-known open-weights and API-gated models, within (i) direct-scoring and (ii) pairwise preference setups. The authors then propose an uncertainty-aware fine-tuning process and create such an uncertainty-aware LLMJ model ConfiLM which shows benefits in evaluations on OOD data.

### Strengths
- The first paper that empirically examines the role of uncertainty within the context of LLMJ, offering a series of empirical findings that motivate the creation of an uncertainty-aware LLM evaluator.
- Despite the large number of experiments, it is quite clear what the focus is in each of the experiments, and it's good to see some intuitions properly empirically verified.
- The choice of underlying model is quite good, which helps with generalising some of the empirical findings.

### Weaknesses
 - The paper adopts a simplified view on recent 'LLM-as-a-Judge' (LLMJ) literature, skipping some related work that aimed to improve confidence of LLMJ models via calibration (https://openreview.net/pdf?id=L3FHMoKZcS) or better prompt optimization (PO; https://arxiv.org/pdf/2406.11370). Improving LLMJ methods requires a multi-component/multi-aspectual approach, which requires combinations of prompt optimisation, calibration and uncertainty mitigation strategies, and the paper would be much stronger with additional experiments that aim to approach the problem in full scope, without reducing it only to uncertainty mitigation. NOTE: This has been corrected in the author response
- This also means that it would be extremely useful to measure how uncertainty/confidence levels change when different bias mitigation or calibration or PO methods get applied. Do we need to handle uncertainty to the same extend and with the same benefits when it gets combined with other methods?
- Speaking of simplifying the experimental protocol too much, there are also many potential approaches to measuring uncertainty, and taking only the logit as the proxy towards uncertainty, while grounded in some related literature, might still be too simple. I would recommend exploring different ways of measuring uncertainty (e.g., see https://arxiv.org/pdf/2404.15993 or https://arxiv.org/abs/2307.10236) and checking whether different definitions of uncertainty also have impact on the final findings (and to what extent). The decision on how we measure/capture uncertainty is a big assumption that seems to stay under the radar of this work. NOTE: This has also been mitigated with the author response.
- Evaluation should get increased to more and more standard LLMJ datasets, including e.g., RewardBench and standard summarization and chat datasets used in prior work (SummEval, HANNA, etc). 
- Minor: the paper spends too much introducing the basics of evaluation with LLMs (e.g., a large part of RW is too long) - that paper space could have been better used for some finer-grained experiments (e.g., understanding the relationships between calibration and certainty or introducing another way to measure uncertainty or some other future work ideas now listed in lines 521-529).

### Questions
- Is there any relationship and/or correlation between uncertainty in the responses of the evalauted mopdels and uncertainty of the evaluator models? How does uncertainty of the evaluated model reflect on the final scores?
- I liked the finding showing how evaluators are more confident with responses coming from models within the same family. Is there a way to also mitigate this 'uncertainty bias' through fine-tuning as well?
- It seems that 'Ties' cause a lot of trouble with confidence - how would discarding the 'Tie' option from the preferences output impact the results and the main findings? I would recommend adding an experiment checking on this.  
- ConfiLM shows benefits with OOD data. Are there any benefits with in-domain or related-domain data or is the approach useful only in OOD scenarios?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper probes the stability of LLMs-as-Judges by leveraging their internal uncertainties and the confidence levels of the responses of models being evaluated. Single response and pairwise comparisons schemes are compared, where confidence levels are computed based on the token probabilities.  The empirical study includes a variety of LLM evaluators, datasets, and assesses several prompting techniques, including CoT method. The work shows how different prompting strategies can diminish evaluation uncertainty and how uncertainty can be  utilized to improve the reliability evaluators in OOD scenarios. An uncertainty-aware evaluator "ConfiLM" is fine-tuned on a human-annotated dataset, then tested on a new OOD test set sampled from the 2024 Olympics. Findings suggest that incorporating uncertainty significantly improves evaluation accuracy under OOD context.

### Strengths
The paper addresses a timely and increasingly relevant issue, the stability of LLMs-as-Judges. While the use of log probabilities as a measure of confidence is not novel in itself, the original contribution lies in its application within the context of evaluators. It investigates methods on how to improve the evaluators confidence and even recognize incorrect responses. 
The work is significant for its practical approach to improving LLM evaluator reliability, especially in OOD scenarios. The findings could impact the deployment and trustworthiness of automated evaluators in various applications.

The paper is clearly written, with a well-organized structure that helps with following the multiple methodologies and conducted experiments. Limitations are also acknowledged.

### Weaknesses
 - Previous studies, such as those by Lyu et al. [1], have shown that log probabilities do not always correlate with human preferences. This raises concerns about the reliability of using these metrics in LLM-as-Judge systems, which have become popular for their scalability and cost-effectiveness in automating evaluations that traditionally relied on human feedback. The paper could further explore how improving model confidence affects agreement with human evaluators. either via CoT or fine-tuning,  

- The methodology assumes access to internal model probabilities, which might not be feasible with proprietary models. This limitation, acknowledged in the paper, constrains the generalizability and scalability of the proposed methods.

### Questions
1. The paper explains how to compute evaluator and response confidence separately. it was not initially clear that the response confidence is solely utilized for the fine-tuning of ConfiLM and not combined with the evaluator confidence.
2. Could the authors clarify how the results from the human annotators are aggregated? 
3. In situations involving pairwise comparisons of models from two distinct families, the log probabilities can span different ranges. Did you consider any recalibration methods to address this issue?
3. Does improving the confidence metrics within LLM evaluators guarantee improvements in their practical evaluation abilities? is this a to be expected outcome?

### Soundness
3

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
This paper investigates the uncertainty in LLM-as-Judge evaluations. Specifically, they use the token probabilities for uncertainty estimation, and find that: 1) the uncertainty estimated in this paper is prevalent across LLMs and varies with model families and sizes. 2) the evaluation confidence of LLM evaluators exhibits sensitivity to changes in data distribution. 3) Specific prompting strategies can alleviate evaluation uncertainty to some extent.

### Strengths
- Since the paradigm of LLM-as-judge has become widely adopted for evaluation purposes, it is important to conduct an in-depth analysis of the stability of this evaluative framework.
- This paper conducts extensive empirical analyses across multiple models and datasets, offering results that can help researchers deepen their understanding of various models as evaluators.

### Weaknesses
 - In my opinion, the main issue with this paper is my uncertainty regarding **whether its research methodology adequately supports the conclusions it claims to draw**. 
  - As demonstrated in the introduction, the core research question of this paper is "Can large language models provide consistent evaluation quality across different inputs and domains?" However, I am not convinced that the token probabilities predicted by the models sufficiently reflect the "evaluation quality" the authors aim to investigate. For instance, we can see that GPT-4o-mini exhibits significantly higher average prediction probabilities than GPT-4o across various datasets, can we truly infer that GPT-4o-mini possesses superior "evaluation quality"?
  - The token probabilities of large models are influenced by numerous factors, such as the training data, input information, and alignment methods. Relying solely on token probabilities as a measure of uncertainty may affect the reliability and generalizability of the conclusions drawn. A model with a higher output probability is likely just over-confidence.
  - In my opinion, rather than an evaluator that consistently outputs results with high probability, what we require is a well-calibrated evaluator, one whose output probabilities accurately reflect the precision of its assessments.
- The authors claim that this is the first study to investigate uncertainty for LLM-as-judge paradigm. However, many prior studies have also addressed the analysis of evaluation uncertainty, albeit employing different methods for estimating uncertainty. For example, position bias refers to the evaluator providing inconsistent evaluation results when the positions of candidate responses are swapped. This, too, is a method for estimating the uncertainty of an evaluator.

### Questions
see weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper mainly discusses uncertainties in evaluations/generations of LLM-based-evaluators. The major contributions of this paper are: 
- First, an in-depth evaluation uncertainty of various models across 2 types of tasks (direct-assessment, pairwise-evaluation), 3 prompting strategies (Default, CoT, Self-generated-Reference), 6 LLMs and 2 Benchmarks
- Finetune a new uncertainty aware LLM-evaluator (ConfiLM), that shows lesser uncertainty while evaluating responses.
- The authors also augment the model with a new OOD test set curated from the Olympics website to assess the models for this task.

### Strengths
- Firstly, I appreciate the dataset and model created in this paper. These can surely benefit the community in future research in this domain. 
- The paper is well-written and provides cogent and coherent arguments till the end. 
- The problem discussed in the paper is also quite interesting and important as there is a significant shift towards LLMs as evaluators, however, there are several uncertainties and interpretability issues associated with those judgments, that need to be acknowledged and studied in depth. 
- The paper aggregates several tiny established yet undocumented/poorly documented ideas into one place as a formal work.

### Weaknesses
 - The paper claims to the first to study uncertainties in LLMs as evaluators, which might be incorrect given a previous work already delves in to the same topic of inaccuracies: [Finding Blind Spots in Evaluator LLMs with Interpretable Checklists](https://arxiv.org/abs/2406.13439). I really urge the authors to acknowledge this work in the Related Works section and show the difference with the current work. 
- Somehow, I fail to see the use of `Self-Generated Reference`. What is the rationale behind it as compared to `Default` and `CoT`? Also, if the LLM-evaluator has to generate a "good" reference answer, it should first be well-versed with the domain and possess enough knowledge, and this might be difficult of smaller models. For example, the Olympics test set might be OOD for the evaluator as well, and the generated reference answer also might not be optimal, and this might lead to an inaccurate evaluation. 
- The paper lacks novelty in some places and feels like a reiteration of existing facts, i.e., most of the findings in section 4.2 are well-known and documented. For example, the second point on self-bias is a long-standing idea and has been proven across multiple tasks and models. Also, there have been several discussions across LLMs excelling at `LMSys ChatBotArena`, however they fail on general tasks. and the last line in the third point of Section 4.2 is also obvious as evaluation is a hard task, and unless models are explicitly trained for it, they will not be suitable for it. Similarly, evaluation is a thorough reasoning task, as the evaluator has to take a proper decision based on the criterion, and input content, so `CoT` performing well in such a case is not a surprise. But, going by my last point in the Strengths, I do not wish to penalize the paper much for this, as these findings are known, but poorly documented, and this paper does a good job of collating them in one single research with appropriate justifications and experiments. 
- While building `ConfiLM`, I see that the training instances are < 700 for an 8B model, and FFT was used to train the model. This is slightly concerning as the generalization of the model might be quite less, and there is a good chance of overfitting, especially with 6 epochs. Were any regularizations put into place during this finetuning?

### Questions
- When training the second model, `Llama-3-8B-Instruct-Finetune`, why was the learning rate lowered to 3e-5? If anything, for consistency and comparison, the exact same setup as `ConfiLM` should be used, by just removing $u_1$ and $u_2$. 
- What happens when $u_1$ and $u_2$ are not verbalized? That would really be an interesting find. Will the model gain more insights from the exact numbers or falter as per previous works? The confidences are converted to discrete classes (Table-8) is slightly dubious as close values on the boundaries of these classes (ex. 0.59, 0.61) see an abrupt jump, which I understand is unavoidable. That's why, a simple experiment without this verbalization should also be studied. 
- What is the distribution of $u_1$ and $u_2$ in the finetuning set?
- I feel a very significant portion of the paper is dumped in the appendix. Without referring to the examples in the appendix Table 7-12) the write up about the Olympics Testset and `ConfiLM` evaluation is quite unclear and incomplete. I really urge that content be added to the main paper itself. 
- The speculation on line 393 is unclear and needs further support. 
- Also, why is the confidence modelled as an arithmetic mean, and not a geometric mean? Geometric mean provides a tighter estimate of the probability, and also goes along with the language-modelling objective.

### Soundness
3

### Presentation
3

### Contribution
3
