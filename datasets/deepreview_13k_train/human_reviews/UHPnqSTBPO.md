# Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement

- Decision: Accept
- Scores: 10, 8, 8, 6

## Abstract
We present a principled approach to provide LLM-based evaluation with a rigorous guarantee of human agreement. We first propose that a reliable evaluation method should not uncritically rely on model preferences for pairwise evaluation, but rather assess the confidence of judge models and selectively decide when to trust its judgement. We then show that under this \textit{selective evaluation} framework, human agreement can be provably guaranteed---such that the model evaluation aligns with that of humans to a user-specified agreement level. As part of our framework, we also introduce \textit{Simulated Annotators}, a novel confidence estimation method that significantly improves judge calibration and thus enables high coverage of evaluated instances. Finally, we propose \textit{Cascaded Selective Evaluation}, where we use cheaper models as initial judges and escalate to stronger models only when necessary---again, while still providing a provable guarantee of human agreement. Experimental results show that \emph{\method} guarantees strong alignment with humans, far beyond what LLM judges could achieve without selective evaluation. For example, on a subset of Chatbot Arena where GPT-4 almost never achieves 80\% human agreement, our method, even while employing substantially cost-effective models such as Mistral-7B, \textit{guarantees} over 80\% human agreement with almost 80\% test coverage

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
This paper proposes a selective evaluation framework to ensure that LLM-based evaluations align with human judgments to a defined degree of confidence. Selective Confidence Evaluation ensures that, instead of always trusting an LLM's judgment, the model evaluates its confidence in a given answer and abstains when unsure. Simulated Annotators leverage in-context learning to simulate diverse annotator perspectives, improving model calibration and reducing evaluation errors. Cascaded Selective Evaluation introduces multiple LLM judges used in a tiered manner, starting with a more cost-effective model and escalating to stronger models only if needed. The method achieves strong human alignment and reduces reliance on more costly models like GPT-4 by using smaller models when possible.

### Strengths
This paper provides clear methodological contributions to improving human-LLM alignments. I especially appreciate the cascaded selective evaluation approach, which explicitly considers the costs of using stronger/more costly LLMs. Overall, this is an excellent paper with clear contributions and is well-executed.

### Weaknesses
This paper has already been very carefully executed, and I have only minor suggestions.

1.	Simulated annotators, despite their encouraging performance, will require significant processing time and resources as N and K increase. Given a substantial decrease in ECE, I believe that simulated annotators have enough value but it would be helpful for the readers if the authors can provide time and cost requirements compared to the canonical approaches. Furthermore, the authors may want to invest a bit more space in explaining the algorithm of simulated annotators including exactly how they handled in-context learning.

2.	The outperformance of cascaded selective evaluation is somewhat expected because the gist of the framework is to exclude the observations where annotator disagreement is expected. In my view, the model does a good job of identifying these hard-to-reconcile observations. A fairer comparison would be to exclude the abstained observations from the baseline models and see how their performance is affected. For example, if you maintain the same coverage for all other methods in Table 2 and Table 3, what would their empirical human agreement look like? Of course, empirically this cannot be achieved without your model – but as you show in Section 3.3, some systematic characteristics can predict abstention. One can simply devise an alternative strategy that can identify these hard-to-reconcile samples and run a multi-agentic approach on them.

3.	I think the most striking result is in Table 7. It is surprising that the weaker cascades achieve an empirical human agreement of 80.3%. Although their coverage is 68.3%, this is indeed a remarkable result. Given this, I would try to do more with the abstained samples. Almost 30% of the sample is now abstained and running the most advanced model on those will not only increase your ultimate coverage and success rate. The relative API cost will be substantially lower than using only GPT4.

4.	Relatedly, the relative API cost of the model is largely dependent on the difficulty of your task. As seen in Tables 2, 3, and 8, the evaluator composition is heterogeneous across different tasks. When a smaller LLM can handle the majority of tasks, the overall task is likely to be cheaper. When a larger LLM needs to intervene, the overall task will be more expensive. I would caveat this (and perhaps show the range of relative API cost using some simulated evaluator compositions) in Section 3.6.

5.	It is a minor thing, but is there any reason that you chose 1-a =0.9 in Table 2, 1-a=0.85 in Table 3, and 1-a=0.8 in Table 7? I would personally prefer the three thresholds to be consistent throughout the paper.

### Questions
See above.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Current NLP paradigms have shifted to using LLMs as judges for annotations instead of humans. This paper asks how we can guarantee the reliability of using these LLMs for evaluation through human agreement. 

Given an input, how likely would humans agree with the model judgment?

For this, the approach is to use selective evaluation: the model can abstain if not confident enough to make a prediction.

The conventional way of using the predictive probability as confidence estimates doesn't show to be reliable so two methods are proposed: 
1. Simulated annotators: simulate annotator preferences through In-Context Learning and the confidence is estimated through the agreement ratio. 
2. Cascaded Selective Evaluation: Start with a cheaper model and go to stronger models when the previous model is less confident. 

This reduces the evaluation overhead with high agreement guarantees. Their abstention policy aligns with human subjectivity.

### Strengths
1. The paper tackles an important issue, we need more human subjectivity at the forefront of LLM evaluation. 
2. In essence, the Simulated Annotators technique is ensembling, so using a simple and popular technique as ensembling is an interesting way to utilize for such a task. 
4. The authors conduct many experiments to show the utility of the approach. 
3. The added ablation studies in the paper are nice. 
5. The paper is well-written and structured.

### Weaknesses
 1. A clear connection to _selective prediction_ is missing. While the authors talk about _selective evaluation_, the concept is the same so it is better to make that link clear. The paper should explicitly discuss how the proposed method relates to existing selective prediction techniques, such as those based on confidence scores or uncertainty estimates, and clarify how it differs in terms of the selection criteria and guarantees provided. For example, the paper could discuss how the abstention mechanism compares to methods that use predictive entropy or variance to determine when to abstain.
2. Related Work can benefit from more work on selective prediction and human subjectivity in LLMs, e.g.

Barbara Plank. 2022. The “Problem” of Human Label Variation: On Ground Truth in Data, Modeling and Evaluation. In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pages 10671–10682, Abu Dhabi, United Arab Emirates. Association for Computational Linguistics.

Khurana, U., Nalisnick, E., Fokkens, A., & Swayamdipta, S. Crowd-Calibrator: Can Annotator Disagreement Inform Calibration in Subjective Tasks?. In First Conference on Language Modeling.

Bavaresco, A., Bernardi, R., Bertolazzi, L., Elliott, D., Fernández, R., Gatt, A., ... & Testoni, A. (2024). Llms instead of human judges? a large scale empirical study across 20 nlp evaluation tasks. arXiv preprint arXiv:2406.18403.

3. Cheaper models used for Cascading are still very costly (e.g. Mistral 7B). The paper should acknowledge that while Mistral 7B is smaller than other LLMs, it still requires significant computational resources, which may limit the practical applicability of the cascaded approach in resource-constrained settings. A discussion on the trade-offs between model size, computational cost, and evaluation performance would be beneficial.
4. The calibration set for human preferences is based on argmax of human judgments. Using argmax gets rid of disagreement signals, which is actually important information. The paper should address the limitation of using the argmax of human judgments for the calibration set, as this approach discards valuable information about annotator disagreement. The authors should discuss how this choice might affect the model's ability to capture the nuances of human subjectivity and explore alternative methods for incorporating disagreement information into the calibration process.

### Questions
How does IAA change for abstained samples with a lower target accuracy?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors propose a framework for LLM evaluation that includes a human agreement guarantee, that is called Cascaded Selective Evaluation. The evaluation task (in this case a pairwise evaluation) is given to a weak LLM judge and escalated to a stronger LLM judge, if the confidence level for the task does not exceed a certain threshold. As a confidence estimation method they propose Simulated Annotators, where multiple LLMs are used to simulate annotator preferences.

### Strengths
The paper is clearly structured and well written. The approach clearly improves the evaluation process supported by LLMs, while being cost effective by only considering stronger models (such as GPT-4-turbo) as a last escalation step. The authors provide meaningful experiments and show how the method can be extended in the future.

### Weaknesses
A weakness of the approach (for now), is that it has only been tested and applied in context of the pairwise preference evaluation. Nevertheless, the Simulated Annotators and Cascaded Selected Evaluation methods are promising. It will be interesting to see how the approach performs in other evaluation settings in the future. The question of when the models abstain could be answered in more detail. For now, it is only answered quantitatively, but not really qualitatively. In order to find out whether the examples the models are not sure about are the same ones about which the human judges also disagree, the examples need to be examined in more detail, i.e. more on the level of content. It would be interesting to see the ratio of examples where both humans and the models abstained from evaluation and to analyze some examples on a content level.

Small errors:
- Line 462: the the tradeoff

### Questions
- You analyzed the abstention rate quantitatively, but did you also do a qualitative analysis? Do the models abstain on the same type of pairs?

### Soundness
3

### Presentation
3

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
The authors introduce a principled method for evaluating language models with guaranteed human agreement. They argue that evaluation should not solely rely on model preferences in pairwise comparisons. Instead, it should assess judge models' confidence and selectively decide when to trust their judgment. This selective framework ensures that the evaluation aligns with human agreement to a specified level. They introduce Simulated Annotators, a new method for confidence estimation that enhances judge calibration, enabling comprehensive evaluation. Their Cascaded Selective Evaluation uses cost-effective models initially, escalating to stronger ones as needed, maintaining human agreement guarantees. Results show this method achieves over 80% human agreement.

### Strengths
1. Robust Human Agreement: The Cascaded Selective Evaluation framework offers a strong guarantee of alignment with human judgment, enhancing the reliability of LLM-based evaluations.

2. Improved Confidence Estimation: The introduction of Simulated Annotators enhances the confidence estimation for LLM judges, allowing for more accurate evaluations without the need for external supervision.

3. Dynamic Judge Selection: By dynamically selecting which judge model to trust, the framework reduces evaluation overhead while maintaining reliability, often surpassing the precision of relying solely on the strongest judge model.

### Weaknesses
It is more like a theoretical work. Given that the experiments have proved effective in evaluating different tasks, I suggest the authors invest some effort in releasing a user-friendly toolkit based on this work, for other researchers to use.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3
