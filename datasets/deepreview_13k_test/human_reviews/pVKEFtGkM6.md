# Investigating Uncertainty Calibration of Aligned Language Models under the Multiple-Choice Setting

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Despite the significant progress made in practical applications of aligned language models (LMs), they tend to be overconfident in output answers compared to the corresponding pre-trained LMs. 
In this work, we systematically evaluate the impact of the alignment process on logit-based uncertainty calibration of LMs under the multiple-choice setting. We first conduct a thoughtful empirical study on how aligned LMs differ in calibration from their pre-trained counterparts. Experimental results reveal that there are two distinct uncertainties in LMs under the multiple-choice setting, which are responsible for the answer decision and the format preference of the LMs, respectively.
Then, we investigate the role of these two uncertainties on aligned LM's calibration through fine-tuning in simple synthetic alignment schemes and conclude that one reason for aligned LMs' overconfidence is the conflation of these two types of uncertainty. Furthermore, we examine the utility of common post-hoc calibration methods for aligned LMs and propose an easy-to-implement and sample-efficient method to calibrate aligned LMs.
We hope our findings could provide insights into the design of more reliable alignment processes for LMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates how the “alignment process” (instruction tuning, RLHF, etc…) affects the *uncertainty calibration* (does the models confidence on answers match of often it gets those answers right) of pre-trained language models (LMs). In particular, they focus on the tasks that can be formulated as multiple-choice tasks, as calibration can be computed more tractably for these ones.

The paper starts by measuring the calibration of open-source LLMs, across model families, multiple sizes per family, and pretrained vs aligned variants of each model. They confirm previous findings in the literature that pre-trained LMs are well-calibrated models, particularly when operating in a *in-context learning* (ICL) setting. Aligned LMs tend to be overconfident compared to their pre-trained counterparts (weather in a zero-shot or ICL setting), having considerable higher calibration error (ECE) compared to their pretrained counter parts.

The authors then identify two distinct uncertainties in LMs under multiple-choice settings: answer uncertainty for choosing among candidates, and format uncertainty for structuring responses. Current alignment processes conflate these two uncertainties, shifting the both format and answer uncertainty and leading to overconfidence in aligned LMs. In contrast zero-shot pretrained LLMs already have a good answer uncertainty and high format uncertainity, and ICL only changes/helps the latter. It also proposes a simple synthetic alignment scheme that purposely only modifies the format uncertainty, and this seems to help a zero-shot LLM get closer to the good calibration of LLMs on the ICL setting. 

Finally the paper proposes a post-hoc calibration method for aligned LMs utilizing the calibrated predictive distribution of the pre-trained counterpart. Experiments show this can effectively calibrate aligned LMs with few-shot examples.

### Strengths
- I liked the investigation around the sources of mis-calibration and the distinction between the two types of uncertainty (answer vs format). Their synthetic alignment (altought limited) experiments also give evidence to their hypothesis that alignment messes with calibration mostly due to answer uncertainty.I think this analysis will be impactful in future research on calibration (at least for similar MCQ settings)
- Their analysis is quite-throughout, taking ICL, scaling and model family into account.

### Weaknesses
- They restrict their study to multiple-choice questions (MCQ). While understandable due tractability issues for open-ended generation, their identified problems and proposed solutions for calibration issues are only really applicable to MCQ settings and aren’t really generalizable to open-ended generation (what is “format uncertainty” in this case). This is especially problematic since the “alignment process” is normally applied through open-ended generation tasks. While I understand the difficulty in the open-ended analysis, some discussion on how the methods could generalize this setting (for example, the proposed temperature scaling should in principle work for open-ended generation aswell?) would help to ease this concerns
- Their proposed temperature-scaling with pretrained-LMs distribution requires access to the non-aligned pretrained LLM and a few examples *for every* new task that we might want to run our aligned model with. This might not always be feasible, particularly as closed-access LLMs proliferate and since of the goals of alignment is making them work well in the zero-shot scenario. Is there some way to generalize this such that we only really need to use the pretrained model once (for example, before the release of the aligned model)?

### Questions
n/a

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the calibration of SoTA open-source LLMs in the context of multiple-choice QA. The paper focuses on the calibration of two variations of LLMs: standard and aligned and shows that aligned LLMs usually have worse calibration (as measured by ECE) as the alignment process increases overconfidence. Then, the paper shows that In-context learning seems to improve calibration with standard LMs by teaching the LM the desired answer format (which is not surprising). The paper shows that the two stages commonly employed in RLHF both contribute to the overconfidence issue of the LM. 

Then, the paper studies approaches to calibrate aligned LMs and proposes a temperature scaling approach that relies on minimizing KL-divergence between the predictive distribution of the aligned LM and the same LM before alignment showing that it gives descent calibration performance and outperforms other approaches in terms of ECE.

### Strengths
* The paper studies an important issue. 
* The study covers a wide variety of LLM families (LLama-1, LLama2, Vicuna) and sizes. 
* The proposed temperature scaling approach is interesting and shows good calibration performance.

### Weaknesses
* The paper is mainly focusing on MCQ and while they argue that many tasks can be framed as MCQ tasks, many other tasks can not. Limiting the scope of the study to MCQ makes it unclear whether these findings will generalize to free-form generation, which I believe is more aligned with how LLMs are deployed in practice.
* I have to say that most of the findings in the paper are expected and some of them have already been established in the literature. For example, we know that alignment hurts calibration and we should expect ICL to mitigate issues with answer format uncertainty. I do not understand the motivation behind formalizing some of the paper findings as *propositions*. I do not think that adds anything to the paper. I would expect the paper to briefly discuss these expected findings and then move on to attacking the issue.  
* The calibration-preserving training approach in section 4.3 is not novel; It is expected that training on the format only will likely reduce the overconfidence issue. In addition, there are two issues with the experimental setup there. First, the QQP dataset is not a pairwise preference ranking dataset, and therefore it's not entirely similar to the pairwise datasets used in realistic RLHF settings. Second,  the experiments were run with LoRA, again limiting the generalizability of these results to the true RLHF setting. 
* The proposed temperature scaling approach is hard to apply in practice if we do not have access to the standard LM logits (the authors also point to this limitation) and is twice as computationally demanding as other approaches, while not being significantly better than simply using a constant temperature.

### Questions
* In section 5.3, you write that you use the last prediction pair of each prompt with your proposed TS method. Does that mean your approach effectively uses less data than the baselines? Have you tried using all pairs with your approach? 
* Why did you pick the Quora-Question Pairs dataset? Why not a dataset designed for RLHF?




===== POST REBUTTAL ======

I thank the authors for their response. I will maintain my scores.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies how alignment training (supervised fine-tuning (SFT) and learning from pair-wise feedback (LPF)) affects the calibration ofv LLMs in the case of multiple-choice (MC). They decompose the uncertainty of the LLM's response into two components: (1) the answer uncertainty, which is the uncertainty about which option to choose, and (1) the format uncertainty, which is the uncertainty about how to format the answer. They show that alignment training makes the LLM overconfident by reducing both types of uncertainty. They propose a method to mitigate this overconfidence and demonstrate its effectiveness on a synthetic scheme. Last, they show that post-hoc calibration methods, including a proposed temperature scaling method, can improve the calibration of aligned LLMs.

### Strengths
- Calibration of LLMs is an important topic.
- Decomposing the uncertainty of LLMs into format uncertainty and answer uncertainty is novel.
- The background of the paper is properly introduced.

### Weaknesses
1. The paper contains many unclear sentences and claims.
    - Section 3.3: `Pre-trained LMs are calibrated in-context learners`. This sentence is confusing. Simply saying `Pre-trained LMs calibrate well in ICL setting` is enough.
    - Section 3.3:  `Format identifier decomposes format preference in MCQs`. This sentence and the whole paragraph are incomprehensible even when I read it again and again. I think this paragraph needs to be rewritten for better clarity. 
    - Proposition 1 is unclear. I would expect a proposition to be something that can be derived from rigorous mathematical proof. The current content in Proposition 1 is only an observation based on the experiments. I also do not see why the first half of the sentence in Proposition 1 indicates (`i.e.`) indicates the second sentence. The following claim that $p_{\theta}^{PT}(y_c |x, F_{MC})\approx p_{\theta}^{PT}(y_c |x, F_{MC}, S_{K})$. I am not sure why the demonstrations do not affect the answer uncertainty about the LMs.
     - Proposition 2 has the same problem as Proposition 1. It is also unclear why changing the answer uncertainty will cause the miscalibration. SFT does not change the confidence but also changes the accuracy, so altering the answer uncertainty does not guarantee that the model will become miscalibrated. The following paragraph is also odd. `optimizing LMs with maximum likelihood in SFT encourages two uncertainties to be eliminated toward the SFT’s data distribution, and the impact on answer uncertainty will lead to aligned LMs’ overconfidence`.  The phrase `eliminated toward the SFT's data distribution` is unclear, and it is unclear why SFT leads to overconfidence in answer uncertainty. The current text seems to indicate that SFT fine-tuned models will be miscalibrated. 

2. Many experiment settings are underspecified and hard to understand
    - How the ICL samples are selected is not specified. It is also unclear if the observations in this paper hold when varying the demonstrations in ICL.
    - The SFT and LPF datasets used in Figure 5 are not specified. It is thus unclear if the SFT dataset has a fixed or preferred format. 
    - Figure 5 also does not explain why there are multiple points for LLama-2 between pre-trained and SFT models.

3. The figures are very difficult to read when printing on an A4 paper.
    - The dash lines in Figure 4 look very similar to non-dash lines. 
    - The words (or symbols?) above the bars in Figure 7 are completely unreadable.

4. The method proposed in Section 4.3, only using the format for SFT, is highly limited to the MCQ setting and not straightforward to adapt to other settings. Moreover, this makes us unable to add new knowledge to the LLM during SFT. This is not very practical.

### Questions
Have you considered to instruct the LLMs to answer in the parentheses format to eliminate the format uncertainty instead of using ICL?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors investigate the calibration of "aligned" language models (finetuned and RLHF'd) on multiple choice tasks. They reproduce previous findings that aligned models are poorly calibrated and attribute this shortcoming to a conflation of two types of uncertainty: uncertainty about the format of the output and uncertainty about answers themselves. They show that targeted alignment intended to remove the former kind does not destroy calibration in the same way. Finally, they propose a temperature scaling technique for improving the calibration of aligned models post-hoc.

### Strengths
Calibrating aligned models is an important unsolved problem. While this paper is far from a solution, it contains some useful insights. It was interesting to see, for example, that almost all of the calibration error of unaligned models is simply a result of so-called "format error." Assuming it doesn't lower accuracy (see below), scaling temperature using the calibrated un-aligned model is also pretty neat.

### Weaknesses
The framing of sections 4.2 and 4.3 seems wrong to me. It is claimed that:

>Ideally, we would like the aligned LMs to generate responses with human-preferred formats and be equally calibrated as the pre-trained LMs, i.e., change the format uncertainty and preserve the answer uncertainty of pre-trained LMs, as ICL does.

While it's true that we'd want "aligned" models to be as or, better, more calibrated than the raw language models, that doesn't necessarily mean we'd want the *answer uncertainty* to remain the same. Essentially the same claim is repeated in Proposition 2:

>Proposition 2. Common alignment processes, such as SFT and LPF, alter both the answer uncertainty pθ(y|x, F) and the format uncertainty pθ(F|x) of LMs. Consequently, the changed answer uncertainty will cause the miscalibration of aligned LMs.

The whole point of "aligning" the models in this setting is to improve accuracy. It's difficult to imagine how to do that effectively while also preserving the approximate answer uncertainties of the original model. Enforcing this constraint would, it seems to me, produce unnecessarily brittle models with tiny margins of error. Of course, models with the same calibration error can have vastly different answer uncertainties (a model that outputs uniformly random answers is just as calibrated as a model that's confidently correct 100% of the time), and so there's no reason why high accuracy and good calibration couldn't be achieved while also tuning answer uncertainties. This issue is sidestepped in Figure 6 because accuracies remain roughly constant somehow (see the next paragraph), which makes me wonder why you'd even perform the intervention at all.

The experiments in section 3 are unclear. Figure 2 implies that the format identifier is provided as part of the prompt, and that the LLM simply has to output an answer choice. In Figure 4, though, there's a graph for the probability of outputting the format identifier, which seems to imply that the LLM is in fact outputting the format identifier itself. If so, what exactly are the plots on the second row of Figure 4 reporting? The average confidence across all generated tokens (the letter and also the two parentheses)? If so, how could e.g. the calibration error of models w/ ICL in 4f be the same as the corresponding figure in 4b? Since they're all correctly predicting the format specifier with 100% probability w/ ICL, it seems like the average calibration error should be significantly lower. Figure 6 has a similar issue. How could the accuracy of the blue + orange curves not increase along with the probability of outputting the format identifier? I could be misinterpreting what the authors mean here, but either way it would help to have a much clearer breakdown of what's being computed in these sections.

Bits and bobs:

- The notation in equation 6 isn't great. Would be better to incorporate the T.

### Questions
How does the proposed temperature scaling technique (Eq. 6) affect MC accuracy? Figure 7 just shows calibration error. I could imagine this intervention undoing some of the accuracy gains of the alignment process.

Re. figure 6, isn't it expected that finetuning on a binary classification task should wreck calibration on MMLU (effectively a 4-class classification task) since it de-weights choices C and D? Given that, I don't see how the rise in ECE can be attributed to increased confidence alone.

Also re. figure 6, it would be interesting to see Llama-1+Format, ICL.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
