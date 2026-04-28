# HELPFUL-ONLY LARGE LANGUAGE MODEL

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5

## Abstract
To know your enemy, you must become your enemy. Sun Tzu stated in $\textit{The Art of War}$. Often, it is crucial to synthesize data containing harmful content using large language models (LLMs) in order to train harmless LLMs. Methods by which synthesized data can be utilized include using it as training data to provide negative signals to the model, as automatic red-teaming data to identify vulnerabilities of the model and more. However, aligned LLMs struggle to generate harmful responses. In this paper, we propose the $\textit{refusal-free}$ training method to reach a $\textbf{Helpful-Only LLM}$ that maintains the helpfulness of the state-of-the-art (SOTA) LLMs while allowing harmful response generation. The $\textit{refusal-free}$ training method filters the instances that refuse an user's request from the datasets. We demonstrate that the $\textit{refusal-free}$ training dramatically decreases the rate at which the LLM generates refusal responses (refusal rate) by 60.12% without sacrificing its helpfulness. Also, we are aware of the possibility that the progress in this direction could lead to irreversible consequences. A powerful model that does not reject harmful requests and executes them all could be exploited for illicit purposes such as the creation of indiscriminate weapons or hacking. However, once again, we believe it is important to be the one to break an LLM and study how an LLM can be broken in advance, including understanding the boundaries a $\textbf{Helpful-Only LLM}$ can reach and identifying its inherent tendencies. We emphasize that this study is wholly for academic purpose and is aimed at paving the way toward a harmless LLM. This study calls for the researchers to acknowledge the potential failures of LLMs and take steps to prevent the breakdowns. $\textbf{Content Warning:}$ This paper contains examples that may be offensive in nature, and reader discretion is recommended.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper aims to train a helpful-only LLM model that always responds to a user's query, i.e., even if the prompt is harmful, the model does not refuse to answer. The method employed is relatively simple: typical instruction tuning (SFT) followed by preference optimization (DPO) of a pre-trained LLM, ensuring that both datasets exclude refusal samples. While the utility of such a model is high—and I have personally used such a model in my safety research—I remain only somewhat enthusiastic about the paper's contributions given the lack of compelling demonstrations.

### Strengths
**Strengths:**
- It is an interesting work that demonstrates how one can obtain a helpful but *not* harmless LLM, i.e., an LLM that never refuses to respond to a prompt.
- The writing is clear, and the work is well-situated within the existing literature.
- The results are compelling, and I believe this method would outperform baselines such as shadow alignment and unalignment (if comparisons were made) when it comes to refusal rates and exaggerated safety, as it focuses on being helpful only by design, while the baselines aim to subvert or reverse the safety alignment.

### Weaknesses
 **Weaknesses/Clarifications:**
- Forgetting Safety (Section 2.2): I do not agree with the claim that further fine-tuning "suffers from the infamous issue of catastrophic forgetting." Can you please substantiate this claim? For instance, Bhardwaj et al. [R1] and Yang et al. [R2] show that generic utility can be largely maintained (see Table 5 in R1 and Section 5.3 in R2). I find these claims more convincing than what is presented in the draft. In current research, forgetting is measured by the utility of the model on various benchmarks such as MMLU and BBH. I believe the Shadow-Alignment and Unalignment data can be tuned to preserve more of the Arena-Hard scores as well.
Note: Consider comparing with R1 and R2 in your related work (Section 2.2).

- It would be beneficial to see the model applied to improve LLM safety in various aspects, as obtaining a helpful-only LLM is not a difficult goal. The paper lacks compelling demonstrations of concrete use cases. Highlighting how this approach outperforms intuitive baselines in specific safety applications would add value. While R1 and R2 aimed to show how safety guards can be bypassed, building a helpful-only model from scratch represents a different research direction, where the motivation for this work remains weak without demonstrated use cases.

Essentially, although the method is simple, I believe it does not contribute significantly beyond the current literature, such as R1, R2, and subsequent works. The area of research is interesting, but merely proposing a way to obtain a helpful-only model by removing refusal samples is not enough of a contribution.

### Questions
- Can you demonstrate how the baselines such as R2 and R1 that opt for fine-tuning to construct a harmful model suffer from catastrophic forgetting? It would be good to see standard benchmark scores such as MMLU, HumanEval, BBH, GSM8K, etc.

- Can you demonstrate how the harmful data constructed using a helpful-only LLM is useful for better alignment of the model compared to existing preference datasets obtained through other means? Showing that this data improves model alignment could help strengthen the motivation for developing a helpful-only language model.

I would appreciate more practical demonstrations rather than just discussions on the utility of such a model. To help guide your thinking, one use case for which I have utilized such a model is for harmful prompt construction. Can you demonstrate additional use cases?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes refusal free training that trains an LLM that does not refuse to answer jailbreaking or red teaming prompts. The approach applies automatic and rule based filtering on the Magpie dataset and removes all those instances where the response refuses to answer the question. The paper has experiments on general instruction following and adversarial benchmarks to showcase that the training on filtered dataset reduces refusal rate (i.e makes the LLM asnwer adversarial questions) while preserving general problem solving ability. Although the paper touches an important research area, it lacks clear motivation, a defined problem statement, and discussion of its use, application, and implications.

### Strengths
1. The paper touches an important research area that focuses on training LLMs solely for helpfulness and not for harmlessness.
2. The paper demonstrates that refusal training does not affect performance on general tasks while reducing the refusal rate on adversarial prompts.

### Weaknesses
1. The paper has no clear motivation as to why such a research direction is important. The problem statement is not properly defined, the end goal is un-clear and what the authors are trying to achieve by training a Helpful-only LLM.
2. The paper has no discussion around the application of a Helpful-only LLM, like where and how can it be used. The authors discuss some issues like it is harder to generate un-safe content for training future aligned LLMs or to judge models on toxic responses, however there is no discussion if the Helpful-only LLM can be used for such tasks to improve or evaluate future models.
3. The refusal free training that involves filtering the Magpie dataset using LLMs or rule based methods and doing supervised fine-tuning followed by preference optimization is standard and not very novel.
4. The paper has no insights where the Helpful-only LLM is better than aligned LLM, how it is bad at safety or where specifically it does not refuse to provide response.
5. The paper is not clearly written. The language of the paper can be improved. The introduction can be improved to better motivate the work.

### Questions
1. What is the application of training a Helpful-only LLM, like where can it be used, how can it be used, and the motivation of training such an LLM in the first place?
2. In Table 4, row 2 where the Magpie align dataset is used for DPO, the refusal rate has already gone down a lot without any filtering. Why is this the case?
3. What is the evaluation dataset used in keyword extraction process? Is it the same evaluation set used in Table 4? If yes, then the process is flawed as the new keywords are extracted based on the responses from the evaluation dataset.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes Helpful-Only LLM, in which the alignment of an LLM is removed to make the LLM more helpful. The LLM is tuned on a refusal-free training set to prevent the LLM from rejecting the query.

### Strengths
* The paper is well-organized and easy to follow.

* Helpful-only LLM is an interesting topic.

### Weaknesses
 * Although I understand building helpful-only LLMs is meaningful, the method proposed in this paper does not seem to be a reasonable solution, since it inevitably makes the LLM less safe. As shown in Table 4, the rejection rate decreases on toxic queries, which is undesirable. If we really need a helpful LLM and do not need to consider the security issue, instead of tuning the LLM after safety alignment, a reasonable alternative may be simply excluding safety-related data from the alignment stage. Without aligning LLM with safety-related data, the LLM should be naturally "helpful". Therefore the proposed method has limited technical contribution.

* The helpful-only LLM is only evaluated on Arena-Hard (for LLMs' general capability), which cannot form a comprehensive evaluation.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a hypothese about helpful-only large language models, which totally do not persue harmless goals. The authors realize the helpful-only LLMs by refusal training. Specifically, they filter out the refusal in training samples (both in SFT and RL) and make LLMs only learn to be helpful. The experimental results show that helpful-only LLMs could be realized via this simple approach, and the corresponding refusal rate indeed decreases a lot, which could lead to serious consequces. This study could make researchers acknowledge what would happen if LLMs totally mis-align with safety, no matter on purpose or not.

### Strengths
1. The research questions are interesting and meaningful. LLM communities are pretty curious about what would happen (and how serious that would be) for a strong helpful-only model (e.g. GPT-4) which does not sacrafise the general ability for better AI safety.

2. The methods are simple (only by data-level filtering) and effective based on the experimental results.

### Weaknesses
 1. The accuracy of refusal judge model is very concerning, which could lead to unreliable experimental results. I think the authors should consider a strict evaluation for the accuracy of the judge model (i.e. Mistral-7B-Instruct-v0.2) under various tasks. The concern could extend to the alignment evaluation in Arena-Hard.

 2. More possible weaknesses are about the questions below.



### Questions
1. The Figuer 2 presents that there exists a keyword filtering in RL step, but in line 254, the authors state that "Extending this keyword extraction process to RL did not result in significant differences; therefore, we extracted keywords solely during the SFT stage". This seems contradictory and confusing. Do I miss something?

2. In fact, I don't know why the final helpful-only model could still refuse sometimes (2.68% in Table 4). What causes this? Not fully filtered dataset or something else? If this is due to dataset, I strongly recommand to construct a refusal testset to evaluate how "clean" (e.g. accuracy) after your proposed LLM-based and rule-based filtering.

3. From my perspective, the final results (the refusal-free training does not improve the helpfulness) are less exciting and less expected. Do you have more analyses about the results? Moreover, I think the results are closely connected with the critiria for helpfulness. For example, if the model correctly answers the procedures to the question "how to make a bomb?", what score will the judge model assign? And what if refusal situation happens?

4. The filtering method is simple, but also comes with some problems. I think directly re-writing (manually or automatically) the refusal responses could be more effective and would not drop many useful prompts. What is the advantage of filtering over re-writing?

### Soundness
2

### Presentation
2

### Contribution
3
