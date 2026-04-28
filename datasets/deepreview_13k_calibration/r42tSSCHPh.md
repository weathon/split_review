# Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
\textcolor{red}{\bf Content warning: This paper contains examples of harmful language.}
The rapid progress in open-source large language models (LLMs) is significantly advancing AI development. Extensive efforts have been made before model release to align their behavior with human values, with the primary goal of ensuring their helpfulness and harmlessness. However, even carefully aligned models can be manipulated maliciously, leading to unintended behaviors, known as ``jailbreaks". These jailbreaks are typically triggered by specific text inputs, often referred to as adversarial prompts. In this work, we propose the \emph{generation exploitation} attack, an extremely simple approach that disrupts model alignment by only manipulating variations of decoding methods. By exploiting different generation strategies, including varying decoding hyper-parameters and sampling methods, we increase the misalignment rate from $0\%$ to more than $95\%$ across 11 language models including \textsc{LLaMA2}, \textsc{Vicuna}, \textsc{Falcon}, and \textsc{MPT} families, outperforming state-of-the-art attacks with $30\times$ lower computational cost. Finally, we propose an effective alignment method that explores diverse generation strategies, which can reasonably reduce the misalignment rate under our attack.}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper reveals a new type of vulnerability of existing aligned LLMs. By manipulating the decoding methods, including removing the system prompts, using different hyperparameters, and varying sampling strategies, the authors successfully jailbreak a bunch of open-sourced LLMs. These findings call for more comprehensive safety training. This paper also proposes to mitigate misalignment under this attack by ensembling diverse generation strategies.

### Strengths
1. The introduced generation exploitation attack uncovers an important but previously overlooked vulnerability in LLMs, serving as an alert for better alignment. 
2. The paper is well-written and conducts comprehensive experiments on 11 LLMs to validate the attacks.
3. The paper improves the evaluation of jailbreaks by advancing from string matching to the application of a trained classifier. It shows that such evaluation aligns more with human judgment.

### Weaknesses
1. This attack only works for open-source LLMs. Proprietary LLMs such as GPT-3.5 seem to be robust to this attack. Therefore, it can only show that the safety training of open-source LLMs is insufficient rather than an intrinsic vulnerability of LLMs.
2. The motivation for the generation attack is not very clear. Some strategies may degrade the quality of the generation. In that case, why will the users change to those strategies?
3. It is unclear to me why the proposed defense method works and how it affects the quality of the LLMs.

### Questions
1. Will changing the generation strategies degrade the performance of LLMs? If so, why would users do that?
2. Could you please provide more intuitions behind the generation-aware alignment approach? Why is this a better alignment? Wouldn't using misaligned samples during the safety training create new vulnerabilities?
3. I'm concerned about the evaluation of the proposed generation-aware alignment approach since it postpones "An aligned answer:" after users' instructions. The paper said it is unnecessary to append 'An aligned answer:' in practice. Can you elaborate on that?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes generation exploitation attack to disrupt model alignment by only manipulating variations of decoding methods. They also propose an effective alignment method that explores diverse generation strategies to reduce the misalignment rate under the generation exploitation attack. Besides open-source LLMs, they investigate robustness of proprietary LLMs to generation exploitation attacks, and find that chatgpt is not as vulnerable as open-source LLMs, partially due to the model input and output filtering from openai platform.

### Strengths
1. Diverse ranges of open-source LLMs have been investigated, and the proposed generation exploitation attacks achieve high success rate consistently across different models.

2. A relevant defense strategy is proposed to help LLMs distinguish misaligned from aligned responses.

### Weaknesses
There is no discussion regarding other basic jailbreak defense strategies such as perplexity listed in this paper. Since the less commonly utilized hyperparameters used during decoding may make the generation less natural or fluent as default hyperparameters suggested by model vendors.

Jain, Neel, et al. "Baseline defenses for adversarial attacks against aligned language models." 
arXiv preprint arXiv:2309.00614 (2023).

### Questions
In Section 5.5, the proposed generation-aware alignment strategy seems to be problematic. Prompt and responses have been categorized into aligned and misaligned groups, however, in the loss function, both probabilities of aligned and misaligned group are maximized so that the loss could be minimized. Perhaps it should be plus before misaligned logp rather than the current minus operation?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper reveals that the safety alignment of existing open-source LLMs is only effective for default generation configurations, and vulnerabilities exist in other configurations that can be exploited for jailbreak attacks. The authors systematically evaluate four open-source model families to showcase this vulnerability. They use different generation configurations, such as removed system prompts and varied decoding parameters, to obtain model outputs for malicious requests and identify the most vulnerable configuration. When allowed to tailor configurations per sample, their attack achieves over 95% success rate on all models (aligned Llama2 needs additional strategies). The authors also propose a finetuning approach that considers various decoding configurations to mitigate the vulnerability to their attacks. Overall, their work underscores a significant, previously overlooked vulnerability in open-source LLMs.

### Strengths
1. The adversarial vulnerability under non-default generation configurations is an overlooked problem, at least for open-source LLMs. This work reveals this oversight, emphasizing the imperative for readteaming to consider all potential use cases. It is a great finding with important implications for practitioners developing their apps on open-source LLMs.
2. The paper is very well written, and I enjoyed reading it.
3. The attack method is computationally efficient.
4. Along the way of showcasing their findings, the authors also make other contributions:
    * They evaluate the efficacy of attack success verification, showing that a model-based malicious output detector achieves a 92% human agreement, while the string match used in prior work achieves 86%. Both are reasonable indicators, in my opinion.
    * They curate a new dataset of 100 malicious instructions, although they seem "subjectively less harmful" to me than AdvBench (e.g., no terrorism or racism-related violations).
    * They manually inspect whether the misaligned model outputs actually contain the requested harmful content. They also find that a simple heuristic that checks whether the output contains bullet points achieves 93% human agreement, which is interesting.

### Weaknesses
1. Unlike the GCG attack by Zou et al., the generation exploitation attack cannot jailbreak proprietary LLMs, indicating that there are effective defense mechanisms against this attack.
2. The claim that their attack "outperforms state-of-the-art attacks with 30x lower computational cost" warrants further elucidation. This statement does not consider the number of malicious requests. The computational cost for GCG is constant regardless of whether it is for a single or a hundred malicious requests. One can even copy and paste a generated prompt from other users with no GPU needed. Conversely, the generation exploitation attack needs 100x computation for a hundred requests. If the authors opt for a fixed vulnerable decoding configuration across all requests to save computation, the attack success rate would be (seemingly) lower than GCG's.
3. The human evaluation of harmful content is helpful, but more details would be appreciated. For example, are there any edge cases where the model's response is ambiguous? And what are the criteria for judgment?

### Questions
1. Do you have any intuitive explanation for the finetuning objective in 5.1?
2. Different generation configurations may also affect the generated content's quality. Have you evaluated that?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors consider the problem of jailbreaking large language models (LLMs).  The main idea is to elicit objectionable responses from LLMs by changing two pieces of the forward pass through an LLM: (1) the system prompt and (2) the decoding parameters.  The authors find that for various open-source models, varying both (1) and (2) can significantly increase the attack success rate (ASR) with respect to prompts taken from AdvBench and a new dataset called MaliciousInstruct, a new benchmark curated by the authors.  In addition to measuring the ASR, the authors also use data collected from human annotations to demonstrate that their attack elicits harmful instructions from two Llama2 variants.  Furthermore, the authors use the same methods on GPT-3.5, finding that their attack is relatively unsuccessful for this model.  Finally, the authors explore the possibility of fine-tuning on toxic responses to improve robustness against their attack, showing that this technique can reduce the ASR by a non-negligible amount.


**Overall assessment.** Altogether, I think that this is a solid paper, and I lean toward accepting it.  The authors conduct thorough experiments, the problem is interesting and timely, the approach is simple, and it seems to work quite well for open-source LLMs.  The paper is also quite well written.  However, the algorithm is not described in detail and there are some concerns about the experiments, including the fact that the attack seems not to work for closed-source LLMs.  Where appropriate, I made suggestions which I think would be manageable to implement/address in the time-frame of the discussion period.  And if these points are addressed, I will happily adjust my score.

### Strengths
**Experiments.**

* *Breadth.*  It's notable that the authors evaluate their attack across *eleven* open-source models.  This is more thorough than much of the recent jailbreaking literature, and I view this as a strength of this paper.  
* *Success rate on open-source models.*  The ASRs of the proposed method---when measured by string matching and with the classifier trained by the authors---is significant.  In the final column on Table 1, it's clear that for these models, it's possible to frequently jailbreak the models under consideration when measuring the ASR with respect to the classifier-based metric.  The comparison to GCG in Table 4 also demonstrates that under both ASR metrics, the proposed approach outperforms GCG.
* *Defense study.*  The authors also study the possibility of doing fine-tuning to improve alignment for open-source models.  The proposed method does improve robustness by a sizable amount, although there would still be a long way to go to reach satisfactory levels of robustness against this attack.  Still, this result will also be of interest to the community, and the fact that the authors consider both the attacking and defense side of jailbreaking in this work is commendable and a strength of this paper.

**Simplicity.**  The proposed attack is straightforward.  It does not involve optimization or fine-tuning.  Rather, the authors can elicit jailbreaks by changing the system prompt and the decoding parameters.  While this should still be viewed as a white-box attack, given the reliance on changing the decoding parameters, in some sense it is *less* white-box than attacks like GCG, since it doesn't require knowledge of the parameters of the LLM.  Indeed, one can directly run this attack on black-box models like GPT-3.5 (as demonstrated by the authors), which is a strength of the proposed method related to adversarial-prompting-based methods like GCG, GBDA, and AutoPrompt.

**Writing.**  The writing is particularly strong -- the authors clearly spent time on the structure of this paper, and it has clearly been copy-edited.  In this regard, it is well above average for this venue, and as a community this should be highlighted and commended.

### Weaknesses
 **Unclear description of attack.**  In this paper, there is not a clear description of how this attack works.  While it's roughly inferable from Section 4, the description of how the attack works is presented alongside experimental results.  Clarity could be improved if these two aspects were separated.  Some further comments are below:

*   *Number of configurations.*  In Section 4.1, the authors list the number of configurations used for the decoder: twenty settings for the temperature, nine settings for top-K sampling, and twenty settings for top-p sampling.  I would have assumed that in the "Varied All" column, the authors would have tried the $20\times 9\times 20$ combinations, but instead the authors say that there are $20+9+20=49$ combinations.  Given this, I suppose the authors are varying one parameter at a time, e.g., setting $\tau=X$ and setting $K$ and $p$ to their default values.  However, if this was the case, then I'd expect the "Varied All" column to me the max of the prior three columns.  This is not reflected in Table 1, so it's unclear how the "Varied All" column was calculated. Specifically, it's not clear if the reported ASR is the maximum ASR achieved across all 49 configurations for a given prompt, or if it's an average ASR across the configurations. In general,  this again points to the fact that the paper could be improved by more clearly articulating how the attack works.
*   *Algorithm?*  One notably missing piece of this paper is some kind of algorithm or pseudocode that spells out how the attack works.  I think that providing an algorithmic description of the method would ameliorate some of the issues already discussed in this section.  

**Experimental details.**

*   *Table 1 vis-a-vis Table 2.*  I don't understand the relationship between Table 1 and Table 2.  Do these experiments correspond in any way?  I was expecting to see some correspondence between the last few rows of Table 1 and the figures reported in Table 2. Specifically, it's unclear if Table 2 reports the average ASR across all prompts under the single most vulnerable configuration, or if it reports the ASR under the single most vulnerable configuration across all prompts. The distinction is crucial for understanding the effectiveness of the attack.
*   *Imposing constraints.*  It's unclear how the authors impose constrains and use length penalties for the open-sourced models (Section 4.3).  As far as I can tell, there aren't any details given in the appendix about this. It would be useful to know which specific APIs are used to enforce length constraints and how they interact with the decoding parameters.

*   *Success on closed-source LLMs.*  One downside of this method is that it seems to not work particularly well for closed-source LLMs.  GCG was shown to have a higher success rate when attacks were transferred from Vicuna, but this isn't necessarily a fair criticism, since it could be the case that the ASRs for these models have decreased in the months since the GCG paper appeared on arXiv.  Nevertheless, since the authors obtained suffixes for GCG, it would be worth comparing the performance of GCG to the proposed attack, which achieves an ASR of around 7%. It's unclear if the 7% ASR is the maximum achieved across all tested configurations, or if it's an average performance.
*   *More details on classifier.*  It's somewhat unclear to me how the classifier used to evaluate the ASR was trained.  The appendix states the hyperparameters used, but not how they were chosen.  The paper implies that 161K entries were used to train the classifier, but the appendix clarifies that only 10K were used for training. It's important to understand the selection process for the 10K training examples and whether this could introduce bias into the evaluation.
*   *Human evaluations.*  Based on my reading of the paper, there are insufficient details regarding the human evaluations.  How did the authors aggregate the predictions from the five graduate students?  (Also, is it meaningful that the annotators are *graduate students*?)  Is five annotators enough?  And the authors say that they sampled 100 aligned pairs from MaliciousInstruct, but earlier in the paper it says that MaliciousInstruct contains exactly 100 prompts -- so did they just use all of them?  The aggregation method for human ratings needs to be clarified, as well as the rationale for using graduate students as annotators. The statistical significance of using only five annotators should also be addressed.
*   *Dataset examples.* Since the authors are introducing a new benchmark, it would be helpful to include examples of prompts from this dataset in the main text of the paper.
*   *Harmfulness percentage.*  The instructions given to judge the "harmfulness percentage" seem relative vague; the criteria listed in the paper are that an answer is harmful if "it provides concrete and helpful suggestions for malicious instructions."  Was there more to this, i.e., were the participants given more detailed instructions.  In general, it would be helpful if the authors could provide all the details used in the experiments with humans.  It seems notable that in Figure 2, the human scores seemed to consistently cluster around 60% when varying each of the parameters, i.e., I don't see any notable trends here.  Moreover, the HPs seem much lower than the ASRs from the "Varied All" column.  Perhaps the authors could comment on this?

### Questions
**Why open-source?**  Throughout the paper, I found myself wondering the following: Why does this paper focus on open-source LLMs.  Clearly this problem is interesting and timely, but there's nothing about this method that implies that it should only be associated with open-source models.  And yet, the title of this paper will lead many readers to believe that this attack should only be used for open-source models.  So I think it's worth considering why the authors centered their narrative around open-source models, particularly when the impact of red teaming is likely most pronounced when one finds ways of jailbreaking closed-source models like Bard, ChatGPT, and Claude, since these are the models that folks---including many people outside the ML research community---tend to be using in their everyday lives.

**Impact of alignment on safety.**  There is evidence in the literature that fine-tuning compromises safety, see this paper: https://arxiv.org/pdf/2310.03693.pdf.  Obviously this paper came out after the ICLR deadline, so there is no need to compare to this work.  But as the method here is somewhat similar to what the authors are doing at the end of the paper, it would be an interesting direction for future work to compare the results from these two papers (if applicable).  This comment doesn't have much to do with the review -- I just thought that the authors might find this interesting.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
