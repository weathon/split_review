# Uncovering Model Vulnerabilities With Multi-Turn Red Teaming

- Decision: Reject
- Avg Score: 5.75
- Scores: 3, 6, 6, 8

## Abstract
Recent large language model (LLM) defenses have greatly improved models' ability to refuse harmful queries, even when adversarially attacked. However, LLM defenses are primarily evaluated against automated adversarial attacks in a single turn of conversation, an insufficient threat model for real-world malicious use. We demonstrate that multi-turn human jailbreaks uncover significant vulnerabilities, exceeding 70% attack success rate (ASR) on HarmBench against defenses that report single-digit ASRs with automated single-turn attacks. Human jailbreaks also reveal vulnerabilities in machine unlearning defenses, successfully recovering dual-use biosecurity knowledge from unlearned models. We compile these results into Multi-Turn Human Jailbreaks (MHJ), a dataset of 2,912 prompts across 537 multi-turn jailbreaks. We publicly release MHJ alongside a compendium of jailbreak tactics developed across dozens of commercial red teaming engagements, supporting research towards stronger LLM defenses.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper highlights the limitations of current defenses in large language models (LLMs) against multi-turn adversarial attacks. Unlike single-turn automated attacks, multi-turn human-driven jailbreaks show a much higher success rate, bypassing existing defenses by strategically interacting with models over multiple conversation turns. The authors conducted tests with human red teamers who revealed that many LLMs, despite advanced safeguards, remain vulnerable in realistic settings. The study also introduces the "Multi-Turn Human Jailbreaks" (MHJ) dataset, containing thousands of successful jailbreak examples to support the development of more robust defenses that address multi-turn interaction vulnerabilities.

### Strengths
1. The main strength of the paper is evaluating the LLM jailbreak robustness from a different perspective and in a like-life setting. A realistic threat model can always give a better idea about the robustness.

2. I appreciate the authors for publishing the dataset of 2912 prompts. I believe this can help the researchers and community.

### Weaknesses
1. Only the *Llama3-8b-Instruct* model was used for evaluation. Other models, especially the stronger ones should have been included.

2. The chosen baselines and the multi-turn-human-jailbreak approach are different from each other in many ways, such as timing, budget, etc. Seems like the MHJ attack is a soft-constrained version of attacks. 

3. Authors admit that *"the skill and experience of individual red teamers may vary"*. In that case, how can researchers compare their defense against human-based attacks in the common ground? What would be the baseline of a red-teamer's skill and experience? This is one of the reasons for using automated attacks for evaluation to this date.  

4. Other automated attacks, such as [1, 2] could be included in the evaluation. 

5. There was no discussion on plausible defenses for such multi-turn-human-based attack.

### Questions
1. Why the evaluation was done only on one model? Why stronger models like ChatGPT was not included? 

2. How were other automated attacks implemented for the WMDP-bio questions?

3. Is it possible to mention the monetary cost of this human-based attack?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on the safety vulnerabilities of LLMs in multi-turn conversations. The authors designed a comprehensive human red teaming pipeline, including "Attempt Jailbreak" and "Validate Jailbreak," and found that LLMs exhibit more safety risks in multi-turn dialogue conversations compared to single-turn automated attacks.

### Strengths
1. Most previous papers have focused on LLM jailbreaking in single-turn conversations, while this work emphasizes multi-turn conversations, presenting a new scenario.

2. The red-teaming results show that multi-turn human jailbreaks outperform current automated attacks, which exposes more safety vulnerabilities in LLMs.

3. The authors have also released their Multi-turn Human Jailbreaks dataset, which can support further research on multi-turn jailbreaks.

### Weaknesses
1. The human red-teaming was conducted only on Llama; further evaluations on other LLMs would more comprehensively illustrate the safety vulnerabilities in multi-turn conversations. Additionally, the human red-teaming data collected on Llama could potentially be used to examine safety issues in other LLMs under multi-turn scenarios.

2. A more detailed analysis of the effectiveness of different tactics could provide deeper insights into multi-turn jailbreaks.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper exposes the significant safety vulnerabilities of Large Language Models (LLMs) in multi-turn dialogue by conducting human red-teaming. By exploiting a diverse of human tactics, human red-teamers achieve a 70% attack success rate on Harmbench against strong defense baselines. This paper finally compiles these results into the Multi-Turn Human Jailbreaks (MHJ) dataset.

### Strengths
+ **Valuable Findings, Including an Open-Source Jailbreak Dataset**: This paper provides a valuable contribution by conducting the first multi-turn human red-teaming experiments, revealing significant safety vulnerabilities that bypass current state-of-the-art defense methods. Given that existing safety alignment techniques primarily target single-turn jailbreaks, these findings effectively motivate the community to develop more robust defenses capable of countering multi-turn attacks.

### Weaknesses
- **Lack of Strong Automated Attack Baselines**: Some black-box attacks, such as CodeAttack [1] and PAP [2], are not included in the experiments, despite utilizing similar “Request Framing” tactics as those in this paper. Including these baselines in future comparisons would offer a clearer perspective on the relative effectiveness of this paper's approach. Specifically, the absence of these baselines makes it difficult to ascertain whether the observed success of human red-teaming is due to the inherent superiority of human-led attacks or simply due to the lack of a comprehensive comparison with existing automated methods that employ similar techniques.

- **Unclear Evaluation Metric for Model Unlearning**: This paper proposes manual review to assess attack outcomes in model unlearning experiments, yet does not clearly define what constitutes a successful attack. For example, does success mean the model output includes content from the forget set? A more detailed description of the evaluation metric for model unlearning experiments would improve clarity. It is unclear if the evaluation considers semantic similarity or just string matching. The lack of a clear definition makes it difficult to reproduce the results and understand the true effectiveness of the unlearning process.

### Questions
- **Counter-Intuitive Experimental Results**: The effectiveness of the “Direct Request” tactic used by human red-teamers, as shown in Figure 8, is unexpected. In this paper, “Direct Request” refers to directly asking the LLM to produce harmful content, which should logically not be highly effective against safety defenses. An analysis of how various tactics influence the attack success rate would be beneficial, as it could offer insights into the specific failure modes of these models.

- **Lack of In-Depth Analysis on the High Effectiveness of Human Multi-Turn Jailbreaks**: Many of the tactics employed by human red-teamers, such as “Injection,” “Obfuscation,” “Output Format,” and “Request Framing,” are also used by automated attacks. Are there particular factors that enable human-led jailbreaks to outperform automated attacks using similar tactics? Identifying these factors could provide valuable insights into the unique strengths of human-driven attacks.

I would consider raising my score if the authors address these concerns and questions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper looks at red teaming via multi-turn human interaction and releases an accompanying dataset of the jailbreaks. This is a useful study: the vast majority of the research effort and available data is focused on single-turn attacks, with only a few exceptions (e.g. Anthropic's hh-rlhf dataset having harmful multi turn conversations). Overall, the paper is clear and well written, and supplies useful well curated data for future work.

### Strengths
- Human driven red teaming data, particularly multi-turn due to its scarcity, is always useful. There are many synthetically generated datasets, but high quality human driven attacks are a valuable resource. In particular, each prompt here had a high degree of manual curation (in comparison to datasets like hackaprompt which contain many low quality samples).

- The analysis across a few defenses is useful, and does highlight that even SOTA defenses on highly studied benchmark harmful questions can be broken in around 15min on a large subset of questions (e.g. often quicker than algorithmic attack runtime).

### Weaknesses
 - It would have been useful to see results which have human single turn jailbreak attempts in Figure 3. At the moment, the "Human" attacks have two variables changed compared to the others: the attack source (e.g. handcrafted), and additionally have multi-turn capabilities. Hence it makes it challenging to disambiguate if the difference in performance is due to the multi-turn aspect, or if humans given enough time remain better than automated based methods at creating jailbreaks.
- I am unclear as to why results against Cygent defense could not be carried out in the same setup as the original paper: the Llama model is open source, and the defense has a published paper. It would have enabled stronger reproducibility and clearer interpretation of results.
- Releasing the non-successful jailbreak attempts as well can be beneficial as it is still a useful resource, for example as training/fine-tuning data or to carry out further analysis.
- Although different styles of harmfulness were investigated: both "regular" harmbench style questions, but also WMDP-Bio for different attack objectives and domain performance from looking into the supplementary material it seems like just the harmbench data was released. Given the dataset is the core contribution of the paper it would have been useful to include the other domain data.

### Questions
Are there statistics on how many red-team members there are/distributions on number of samples provided per red-team member?

### Soundness
3

### Presentation
3

### Contribution
3
