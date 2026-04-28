# Realistic Evaluation of Model Merging for Compositional Generalization

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Merging has become a widespread way to cheaply combine individual models into a single model that inherits their capabilities and attains better performance.
This popularity has spurred rapid development of many new merging methods, which are typically validated in disparate experimental settings and frequently differ in the assumptions made about model architecture, data availability, and computational budget.
In this work, we characterize the relative merits of different merging methods by evaluating them in a shared experimental setting and precisely identifying the practical requirements of each method.
Specifically, our setting focuses on using merging for \textit{compositional generalization} of capabilities in image classification, image generation, and natural language processing.
Additionally, we measure the computational costs of different merging methods as well as how they perform when scaling the number of models being merged. 
Taken together, our results clarify the state of the field of model merging and provide a comprehensive and rigorous experimental setup to test new methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper provides an empirical study of model merging. Specifically, it focuses on the compositional generalization of capabilities, with control of many experiment variables. By comparing many merging methods on several tasks like image classification, image generation, and NLP, this study provides the community with some takeaways for model merging.

### Strengths
* The related works and their summary of the methods are great
*  I appreciated the detailed study of the experiments
* Overall writing is clear

### Weaknesses
 * Title: I'm not super convinced that "compositional generalization" is the "realistic" goal for model merging. Many times, model merging might not be for the emerging capability of several different tasks, but just to improve on the same held-in tasks such as the original motivation of Model Soup etc.

*  As for a conference-level study paper, I would expect it to reveal more surprising conclusions, insights, or theoretical motivations. Otherwise, it feels like this paper leans towards a workshop paper or a survey-style report.

### Questions
The messages this paper aims to deliver to the community are not super clear to me. Do we already believe model merging is the proper way toward a multitasking model and do the authors suggest it is a promising approach or not?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper benchmarked different “model merging” methods, which are effectively methods to aggregate the weights of many different models trained on many different downstream tasks. The comparisons included different task settings, data modalities, benchmark models, and evaluation criteria (held-out compositional task performance and compute requirements, for example). Overall I found that the paper had good scientific standards (good research question, sensible controls and evaluations, methodical analyses, etc.) but that the actual findings were of potentially limited practical use. No merging method was clearly superior to others, and results were very dependent on the task setting in a way where it is unclear whether they will generalize to author task settings, datasets, or model backbones. I note, however, that I am not familiar with the model merging literature and my assessments are to be taken with a grain of salt. I hope that the authors provide a good code base, so that others can build around their work as a standardized test-bench for novel merging methods down the road.

### Strengths
1. The focus on evaluating compositional generalization is an important contribution, as intuitively it seems like this would be the main real-world use-case for model merging. It is surprising that prior work on model merging does not focus on compositional task generalization (if I understood the authors correctly). The task constructions are also nicely controlled and systematic, both for vision and language tasks.
2. The baselines comparison methods (such as training on some supervised data for the target held-out task) are very sensible.

### Weaknesses
1. The paper would be stronger if it benchmarked different base models on each task in order to make sure the core results generalize (especially different architectures, such as Transformers and CNNs on the vision tasks or Transformers and SSMs on language tasks).
2. It feels like a baseline is missing. To evaluate generalization error on held-out tasks, one could also evaluate a single fine-tuned model (one of the models being merged) on the held out task. For instance, maybe a model fine-tuned on English Question-Answering would do better on, say, Arabic Question-Answering than some of the merged models (or better at least than the “pretrained” baseline). This would amount to a comparison between merging methods vs. fine-tuning a single model on a task that is closely related to the target held-out task. While this is not necessarily the most important baseline out there (I’m sure the top merging methods would surpass it), it would nevertheless be nice to know how this performs, if the authors have to bandwidth to add it. If the baseline always performs worse than the simple “pretrained” baseline, it could simply be left out of the results figures.
3. The main result is the method comparison in Section 4.1. However, there are no clear trends in method dominance that generalize across the 3 task settings. This significantly reduces the impact of the paper, since it reduces the generality of the findings: we still don’t know which method is best in terms of generalization to compositionally held-out tasks, as the results differ across 3 settings. It also makes me doubt whether the results would generalize to the same exact task settings with different datasets and backbone models.
    1. On this note, ultimately, I think the value of this work will depend on the quality of the code base and whether it serves as an easy-to-use public benchmark where others can easily plug in new merging methods for comparison. I of course cannot evaluate whether this is the case, and time will tell whether it becomes a useful benchmark in the field.
4. Minor: several typos, missing words, grammar mistakes peppered throughout. For instance, the sentence in lines 193-195 is missing words (like a subject) and has singular/plural issues. Most of the text reads fine, but please proofread again to correct the language mistakes so that the text reads well everywhere.

### Questions
1. In Figure 2, are the horizontal dotted lines the average performance of models fine-tuned on that “held-out” tasks? In other words, is there no difference between the horizontal and vertical dotted lines other than whether the task is considered “held-out” with respect to the merged models?
2. Why not include the multi-task trained model as one of the constituent models being merged?
3. Lines 301-303 state: “We note that Fisher Merging tends to generalize than RegMean and MaTS despite all three of methods implicitly minimizing the same objective (Tam et al., 2023).” Looking at the plot, this only seems to be true for the NLP tasks, but not image classification or image generation. Am I misinterpreting something? If not, this statement should be amended.
4. Paragraph lines 306-319 talks about correlations (and anti-correlations) between a merging method’s held-in and held-out task performance. From the plots, it is difficult to tell if these correlations are strong and statistically significant (few methods are evaluated and the performances tend to cluster, with one or a few outlier methods generally driving the correlations. What are the numeric correlations and their statistical significance, and can this be included in the text for added rigour?

### Soundness
3

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
4

### Summary
In model merging, a pretrained model's weights are copied $K$ times, each copy is finetuned on a separate task, and the parameters of the $K$ constituent models are merged together. Model merging is popular among open-weight model enthusiasts, with some suggesting that the merged model's performance is comparable to a multitask model on the $K$ in-domain finetuning tasks, while also offering better out-of-domain performance on held-out tasks than the naively finetuned multitask model [1, 2]. As a result, many model merging methods have been proposed.

In this work, the authors point out a lack of systematic evaluation of such merging methods. They address this gap by evaluating 8 merging methods on 3 architectures / tasks, comparing in-domain and out-of-domain performance, computational costs, hyperparameter sensitivity, and robustness to increasing number of constituent models $K$.

References:

[1] Wortsman, M., Ilharco, G., Kim, J. W., Li, M., Kornblith, S., Roelofs, R., ... & Schmidt, L. (2022). Robust fine-tuning of zero-shot models. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition (pp. 7959-7971).

[2] Wortsman, M., Ilharco, G., Gadre, S. Y., Roelofs, R., Gontijo-Lopes, R., Morcos, A. S., ... & Schmidt, L. (2022, June). Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time. In International conference on machine learning (pp. 23965-23998). PMLR.

### Strengths
- Timely problem to study: model merging is both a scientifically interesting and currently useful practice, and a thorough empirical evaluation is very helpful. In its best form, I see this paper as being positioned to make contributions by answering two main questions, both of which I believe could really be novel and substantive contributions.

1) What is the relative ordering of merging methods? If a practitioner is interested in merging X architecture on Y task with Z budget, which method should they select?
2) Under which conditions does merging outperform / underperform multitask learning / the pretrained model?

- Holistic approach: this paper considers not just accuracy gains, but also compute / data access requirements. Figure 3, for example, is very insightful in pointing out that merging performance correlates with compute. Similarly, the scaling experiments in 4.5 (Figure 5) and the hyperparameter experiments in 4.4 (Figure 4) were well done.

### Weaknesses
My main concerns revolve around the experimental design in Section 4.1. The best version of this work would help a user understand when to use model merging and which method to use, given some features about their task (e.g. architecture, modality, finetuning strategy, compute budget). This also seems to be the authors' ambition (lines 43-48). However, the experimental design makes it difficult to draw conclusions about these questions, and I'm concerned that some of the authors' conclusions have not accounted for confounders.

- There are three experimental settings in the evaluation: (image classification, DomainNet, CLIP, full finetuning), (image generation, DomainNet, StableDiffusion, low-rank finetuning), and (assorted NLP tasks, assorted languages, T5, full finetuning). In Figures 2-4, we draw quite different conclusions about the relative strength of merging methods / when merging outperforms multitask learning, depending on the setting. 

- On lines 71, 310, 484, and 487, the authors alternate attributing these differences to the modality and task: e.g. in line 487, "cross-lingual generalization" behaves differently than "cross-domain generalization"; in line 71, natural language processing behaves differently than image classification. 

- Unfortunately, I'm not convinced that either of these conclusions are the right ones to draw, since the three experimental settings conflate model architecture, data modality / task, and finetuning strategy. 

    - As an example of why these setup issues matter, I find it difficult to interpret Figure 2 (right), where many methods underperform the multitask baseline for in-domain performance. Is the conclusion that T5 merges less well, that models merge less well on the language modality, or that the specific cross-lingual benchmark the authors set up lead to finetuned models which merge less well? 
    - The authors attribute the negative slope in in- and out-of-domain correlation to to modality in line 70 and "cross-domain" vs. "cross-lingual" generalization in lines 306-319, but this seems to ignore a potential dependence on model architecture / pretrained parameters. Further, I'm not sure "cross-domain" and "cross-lingual" are quite the right characterizations here; surely there are some domain generalization settings where merging will also have weak generalization performance, and one could argue that cross-lingual generalization is simply another domain generalization problem. Can you better characterize when we expect merging to enable generalization vs. not?

    - In Figure 2 (middle), many methods outperform the multitask model in both in-domain and out-of-domain performance: is this because image generation as a modality is more suited for merging, because it is better to merge LoRAs instead of full parameters? Why does the multitask model have higher out-of-domain performance than the pretrained model here, unlike in the other two settings?

- I believe most of these issues are corrected by (1) testing more than one architecture per modality and (2) testing more than one dataset per modality. The authors might look to other domain generalization benchmarks to gather more tasks per modality, e.g. [3].

- On a separate note, the performances of merging methods likely have some dependence on the specific weights the constituent models arrive at after finetuning. Ideally, Figure 2 should include error bars accounting for randomness of the finetuning process: i.e., we should finetune multiple replicate models on each of the $K$ finetuning tasks, and then report merged model performance over randomly chosen replicates for each task. However, Appendix B seems to suggest that only one checkpoint was used per task, which raises some questions for me about whether results generalize across optimization randomness.

To make a generalizable contribution as promised on lines 47-48 in the introduction, I would need to see the reasons behind the mixed results carefully dissected. While interesting, the current results seem specific to the settings evaluated, making it difficult to draw precise and well-justified insights. The remaining contributions (hyperparameter sensitivity, computational requirements, scaling) are useful but perhaps not substantive enough for a full ICLR submission.

### Questions
I'm open to discussing the questions raised in the Weaknesses box and will increase my score if appropriate. Additionally, line 275 mentions analyzing how results depend on model size: I couldn't find this in the main text, but I'd be interested in this discussion.

Lastly, I had had two questions that are not in-scope for the submission, but I would love to see explored in a final camera-ready version: 

1. One missing citation (https://arxiv.org/abs/2203.05482) proposes a "greedy soup," where models are merged only if they add to the in-domain performance. I'd be curious how this baseline performs in your setting --- maybe just a little bit better than "Average"?

2. It would be interesting to know how merging performance scales not just with the number of models, but also with the "degree" to which constituent models differ. For example, if merging 5 models, does performance change if I finetune each model for 500 steps vs. 5000 steps?

Flagging some typos to fix for a final version:
- line 54: "being a more challenging [setting]"
- line 55: "merging: [a]ssuming"
- line 96: "\theta_i [for] i \in" 
- line 193: "In this work, [we] evaluate"
- line 194: "create [a] multitask model"

### Soundness
2

### Presentation
4

### Contribution
2
