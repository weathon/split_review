# On Extending Direct Preference Optimization to Accommodate Ties

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
We derive and investigate two DPO variants that explicitly model the possibility of declaring a tie in pair-wise comparisons. We replace the Bradley-Terry model in DPO with two well-known modeling extensions, by Rao and Kupper and by Davidson, that assign probability to ties as alternatives to clear preferences. Our experiments in neural machine translation and summarization show that explicitly labeled ties can be added to the datasets for these DPO variants without  the degradation in task performance that is observed when the same tied pairs are presented to DPO. We find empirically that the inclusion of ties leads to stronger regularization with respect to the reference policy as measured by KL divergence, and we see this even for DPO in its original form. These findings motivate and enable the inclusion of tied pairs in preference optimization as opposed to  simply discarding them.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces two variants of Direct Preference Optimization (DPO) designed to account for ties in pairwise preference data, addressing a limitation in the original DPO framework that requires strict winner-loser pairs. The authors replace the Bradley-Terry model traditionally used in DPO with two extensions from Rao-Kupper and Davidson models, both of which assign probabilities to ties in addition to clear preferences (and have a nice explanation of the different assumptions in each). 
The proposed DPO variants—DPO-RK and DPO-D—are then tested on neural machine translation and summarization tasks, using synthetic preference pairs (with ties) constructed metrics/reward models. The experiments show that incorporating ties into DPO-RK/D does not degrade task performance as it does in traditional DPO and, in fact, regularizes the policy with respect to the reference policy, as seen through KL divergence measurements. They also test the learned policies’ classification accuracy at  distinguishing between clear preferences and ties.

### Strengths
- Overall, I like the paper’s motivation and proposed approach: DPO is very prevalent method to perform preference optimization, and the inability to handle ties is a definitely a drawback.
- The proposed variations are well motivated and the theoretical discussion on their differences was quite interesting to me.
- The (limited) results included hint that including ties and using one their proposed variants leads to better policies than the current dominant approach of discard ties.

### Weaknesses
While overall like the idea and introduced approach, I think the paper is severely limited by the weak empirical evaluation. A couple of points:

- Reporting of results for both task are relatively limited, only reporting performance for preference aligned models on the metrics used to construct preference. I think having a table reporting baseline and best performing DPO models on multiple metrics is necessary to trust gains from DPO and its variants, as they could be over-optimizing for BLEURT. In MT for example, gains in COMET (or even BLEU/ChrF) would allow me to trust to overall conclusions alot more.
- For machine translation, a relatively weak model (BLOOMZ-mt-7b) is used. Why this model rather than many strong LLM for MT e.g. TowerLLM? Similarly, BLEURT is relatively outdated as a metric for MT, and I would have used a better metrics to construct preference pairs. In general, replicating the findings in more than one base LLM (for at least MT) would strengthen the paper.
- In general, there lack of comparison to some other baseline preference alignment algorithms (KTO, IPO, etc…). I would really like to see how DPO-RK/D compares one of them, especially if tie data is also used with it.

But in general I like the motivation of the paper, and would be happy to revise my score if authors address these comments

### Questions
- What happens when the proportion of ties vs winning pairs changes (in terms of performance, KL, etc…)? Since the preference pairs are synthetic, this would be something relatively easy to explore, and could inform what kinds of preference datasets make DPO-RK/D work well.

### Soundness
2

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
The paper incorporates the pair-wise ties into DPO alignment framework, by replacing the BT model in DPO with Rao and Kupper and Davidson extensions. It conducted performance on machine translation and summarization tasks. Also, it provides some analysis on KL divergence and RM statistics. It provides potential insights to incorporating tie pairs for DPO training.

### Strengths
1. The motivation is straight forward and easy to follow. It provides the straightforward idea that using the discarded tie pairs for optimizing the DPO framework.

2. The injection of DPO-RK and DPO-D remains similar task performance in comparison to original DPO, mitigating the problem of original DPO that will suffer from task performance degradation when injecting tied pairs.

3. The background is well presented and in a good shape.

### Weaknesses
1. The paper experiments is not quite sufficient. It only conducted experiments on machine translation and summarization, rather than conducting commonly used alignment datasets such as HH-RLHF (https://huggingface.co/datasets/Anthropic/hh-rlhf).

2. Limited evaluation metrics. It only uses automatic evaluation metrics BLEURT and RM win rate, which is not often in consistent with human alignments. It is required to further report the results of gpt-4 evaluation and human evaluations.

3. It is recommended to report the case to better illustrate the effect of proposed methods.

4. The methods of obtaining tie pairs requires further evaluation. Is the automatic distance-based metrics reliable to obtain tie pairs? It is recommended to report the evaluation results.

### Questions
1. What is the human evaluation results on the DPO-RK/DPO-D results compared to original DPO?

2. How is the results on commonly used benchmarks, such as HH-RLHF?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors propose two methods to generalize DPO to accommodate tie (y_i = y_j).

However, it may seem a minor problem from my perspective. DPO cannot accommodate tie but it can tolerate when y_i is very close to y_j.

In addition, one problem is that the authors does not compare the proposed two method with DPO without considering tie. Will its performance be lower than DPO?

The author utilize a relative subjective method to compare models, while classification and generation tasks should be done.

### Strengths
The authors propose two methods to generalize DPO to accommodate tie (y_i = y_j).

### Weaknesses
However, it may seem a minor problem from my perspective. DPO cannot accommodate tie but it can tolerate when y_i is very close to y_j.

In addition, one problem is that the authors does not compare the proposed two method with DPO without considering tie. Will its performance be lower than DPO?

The author utilize a relative subjective method to compare models, while classification and generation tasks should be done.

### Questions
NA

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper extends the Direct Preference Optimization (DPO) framework to handle tied preferences in pairwise comparisons by incorporating two established preference models, the Rao-Kupper and Davidson models. Unlike the original DPO, which discards ambiguous data points, the proposed variants, DPO-RK and DPO-D, allocate probabilities to ties, preserving more information from the data. The paper evaluates these DPO variants in machine translation and summarization tasks, showing that the inclusion of ties enhances regularization effects without compromising performance.

### Strengths
1. The paper successfully integrates the Rao-Kupper and Davidson models to extend DPO for handling ties, addressing a known limitation in the original DPO framework where tied pairs were previously discarded. This extension makes the preference modeling process more inclusive and data-efficient.

2. The experimental analysis includes various statistical measures and visualization of training dynamics, such as reward margins and gradient scale factors, which add depth to the assessment of how well the models learn from tied data.

3. The paper is well-written and easy to follow. The adaptation of Bradley-Terry models for ties is systematically outlined, with clear mathematical formulations and derivations for the proposed DPO-RK and DPO-D models.

### Weaknesses
1. The introduced method shows limited novelty, as it builds upon existing Bradley-Terry extensions to accommodate ties. The proposed DPO variants primarily involve substituting the standard Bradley-Terry model with these pre-existing extensions (Rao-Kupper and Davidson) for preference modeling, rather than presenting fundamentally new methodologies.

2. Although the proposed DPO variants improve regularization effects, they fail to demonstrate any clear enhancement in task performance relative to the original DPO. This raises questions about the practical value of the proposed modifications, particularly in performance-critical applications.

3. The experiments are limited to machine translation and summarization tasks, leaving more complex domains such as open-ended generation tasks (e.g., AlpacaEval, Arena-Hard, MT-Bench) and mathematical reasoning unexplored. Expanding evaluations to these challenging areas would provide a more comprehensive assessment of the proposed methods.

4. The paper introduces additional parameters, such as the probability adjustment factor $\upsilon$ for the Rao-Kupper and Davidson models, but lacks extensive discussion on the impact for tuning these parameters.

### Questions
See weeknesses.

### Soundness
3

### Presentation
3

### Contribution
3
