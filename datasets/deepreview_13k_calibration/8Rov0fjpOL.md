# Breach By A Thousand Leaks: Unsafe Information Leakage in 'Safe' AI Responses

- Decision: Accept
- Avg Score: 5.80
- Scores: 8, 6, 6, 6, 3

## Abstract
ulnerability of Frontier language models to misuse and jailbreaks has prompted the development of safety measures like filters and alignment training in an effort to ensure safety through robustness to adversarially crafted prompts. We assert that robustness is fundamentally insufficient for ensuring safety goals, and current defenses and evaluation methods fail to account for risks of dual-intent queries and their composition for malicious goals. To quantify these risks, we introduce a new safety evaluation framework based on \textit{impermissible information leakage} of model outputs and demonstrate how our proposed question-decomposition attack can extract dangerous knowledge from a censored LLM more effectively than traditional jailbreaking. Underlying our proposed evaluation method is a novel information-theoretic threat model of \textit{inferential adversaries}, distinguished from \textit{security adversaries}, such as jailbreaks, in that success is measured by inferring impermissible knowledge from victim outputs as opposed to forcing explicitly impermissible outputs from the victim. Through our information-theoretic framework, we show that to ensure safety against inferential adversaries, defense mechanisms must ensure \textit{information censorship}, bounding the leakage of impermissible information. However, we prove that such defenses inevitably incur a safety-utility trade-off.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper explores the abilities of language models to defend against attacks in which a user query is decomposed into multiple questions. They describe a threat model in which an adversary decomposes a harmful question (which an LLM would refuse to answer) into many *safe* questions. They then measure the ability of the adversary to learn information that contributes to the overall harmful goal by assessing a model's increase in confidence in answering multiple choice questions correctly after receiving information from the target LLM. They additionally present a randomized response defense based on differential privacy, demonstrating that this defense has provable bounds for safety, but would come at the expense of performance.

### Strengths
1. To me this is a realistic threat model. The multi-turn nature of the attack and the decomposition of the harmful query into smaller safe queries seems an intuitive setting.

2. The evaluation is not all or nothing, but models information gain as a change in model confidence in the answer chosen with and without the information from the target model. This allows for more nuanced measurements of the harm done by information shared.

3. The problem and setting are important, and the paper is well written and organized.

### Weaknesses
1. This study uses data from only two domains, and there are significant enough differences between some results that I question how domain-specific the effectiveness is. Clarification on what may cause these discrepancies and if they are likely to occur for other topics as well would be helpful.

2. The differential privacy based defense allows bounds to be given on the safety vs. performance of the model, but this is not compared to existing defenses that are tested in the paper. While bounds may not be able to be established theoretically for these defenses, a comparison to existing defenses seems appropriate.

3. It was not clear to me until searching in the appendix that the attacked model was Llama-3.1-70B, or that defense mechanisms (Llama-Guard-3 and Prompt-Guard-3) were used. This improves the credibility of the results and should be made more clear in the results and/or methodology.

4. Though multiple adversary models are used, the attack is tested on only one victim model and using only one set of defenses. Attacking a large model is, of course, impressive, but adding models from multiple families would make the results more robust.

### Questions
1. As shown in Table 1, there appears to be a good deal of variance in performance across topics. 

	a. Do you have a hypothesis for why this is? 

	b. Is there something more challenging about the Chem topic vs the Bio topic, and could this extend to other topics areas that are not tested?

2. While I understand a differential privacy based defense allows for more rigorous analysis of bounds and tradeoffs, I do question whether this is actually an appropriate defense in this setting. While there are similarities between this setting and privacy (small leaks in information adding up, difficult to classify what is a dangerous leak, etc.), it seems that classifying what is unsafe may be somewhat easier here, given the full context of a conversation. Can you give additional practical motivation for this defense?

3. What would the cost be to implement the randomized response defense? How does this compare to existing defenses?

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
4

### Summary
The paper introduces a data leakage threat model for studying frontier model misuse. It points out that the current LLM jailbreak literature is too focused on one-shot harmful response generation instead of more complex threat models for how model-generated outputs may be synthesized to extract harmful knowledge. As a demonstration of the threat model, the paper defines an attacker model that is given few-shot demonstrations to generate subquestions, extracting answers to subquestions, and aggregating answers to the questions.

### Strengths
- For frontier models, it is important that we have more research on threat models to better assess the usefulness of new jailbreak datasets and defenses. The threat model in this paper seems important from a policy and governance perspective.

### Weaknesses
 - The randomised response strategy is extremely costly. It is unlikely to be informative for any frontier model developers, nor serve as a relevant baseline to compare future solutions against. In my opinion, the paper would be better without proposing any solutions, as a clearer study of this particular threat model.

- The empirical results are insufficient:
  - The dataset is limited. If it wasn't clear where to source more questions, creating such a dataset would have been good for making it easy for future work to take on this problem.
  - Even if not fully faithful to the threat model, showing that harmful knowledge is compositional is an important subclaim of the paper, and can be validated using existing jailbreak datasets. Even if DA is not competetive against PAIR, it is important to show that it is adequate.

- Given that the attacker may already be predicting the correct answer, it seems important to study how often the model changes its answer to be more correct. (This may involve control studies around how well the smaller attacker models are at extrapolating from a series of facts. however,) Without substantiating that attacker models actually learn new answers, the IIL metric is not as useful and has many confounders on the mechanism of how the probability on the correct answer is actually increasing, for instance, because of longer context windows.

### Questions
Questions: 
1) Why did you develop the randomised response defense? Can you provide motivation for it?

Suggestions: 
1)  This evaluation demonstrates that harmful knowledge in compositional, and it may be difficult to serve models with some types of knowledge. Perhaps, you may want to cite related works in unlearning? 
2) It is potentially interesting to study if harmful applications can be built compositionally, instead of limiting to harmful knowledge. The standard argument on the safety-utility tradeoff is that the web already contains this knowledge, and serving it via LLMs is not a significant increase in harmfulness. By defining a clear pipeline for the attacker LLM to systematically extract harmful knowledge, your approach mitigates this concern a little bit, but taking this one step further could help the case.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Prior works mainly focus on security threats where adversaries mislead the victim model to output malicious content directly, while this paper considers inferential threats, where the malicious query is decomposed into multiple subquestions and leads to a harmful response after aggregation of answers of subquestions. There are empirical evaluations and analysis from information perspective to consolidate the setting considered in the paper.

### Strengths
The paper is easy to follow. Discussions are thorough in the paper.

### Weaknesses
1. The key part in this paper is the query decomposition and aggregation part. However, the concrete prompts are missing to judge whether it makes sense. Some examples should also be provided to help understanding. The example in Figure 1 does not impress me because the question "What are some common scams targeting the elderly?" is not a benign one so the LLM might not provide answers to it, Also, is the method only applied to complex questions? If the query is simple as Figure 1, how do we decompose it effectively.

2. Can the analysis part benefits design of attack/defense algorithms? Can we empirically validate them. In the current version, the analysis seems separate and does not convey concise and impressive results.

3. Evaluation is also limited. An overall number is not sufficient to support the method. More ablations should be conducted. For example, which prompts are more effective? Which queries can be more easily conducted? Will certain model refuse to decompose the query because it contains sensitive words? Such questions can help better understand the strengths and weakness of the algorithm.

### Questions
Please refer to the weakness part.

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
2

### Summary
The paper proposes an approach for jailbreaking models, which involves decomposing a harmful question into harmless-looking subquestions (with a less capable, safety-free model e.g. an open-source one), then answering those subquestions with a more capable model with safety training (e.g. black-box API models), then composing those answers into a single overall answer with the less-capable safety-free model. The paper finds that this method is effective overall, testing on the WMDP benchmark which consists of harmful cyber and CBRN related questions. The paper also discusses theory behind a differential privacy motivated defense, which improves safety at the cost of helpfulness.

### Strengths
- Results look great overall, I think the approach proposed here seems effective at eliciting harmful info without triggering flagging. The fact that this works well in practice will definitely require some rethinking on the part of model developers, in terms of figuring out how to handle attacks like this. Likely it will require some big changes (if not already in place), like cross-user monitoring and inferring whether or not harmful info has leaked despite no single question looking harmful.
-Great motivation; have been wanting to see a paper on this for a while.
-Great idea to eval our WMMDP + compare to PAIR
-Very clear abstract + Figure 1



I would give this paper a 7/10 rating, somewhere between marginal accept and accept (but the form would only allow a 6 or an 8).

### Weaknesses
 -Table 1 would be clearer if (or experimental results would be clearer) if paper showed improvement in ASP to PAIR's ASR and comparison
-On the theory section, I don't have the expertise to evaluate this section that well, and don't fully follow the motivation or proposed defense. It would be nice to have some higher-level description of the findings. I understand that adding noise is involved in the defense, but don't understand how this applies here or helps. It would be nice to propose/test a specific approach in the paper.
-Erik Jones' et al. have an arXiv paper that's pretty related / on the same overall issue, if I recall correctly, which would be worth citing/discussing.
- It would be nice to better understand when this method doesn't work -- what kinds of questions weren't able to be decomposed into harmless questions. Generally more qualitative analysis would be helpful for understanding how big of a problem decomposition will be.

Minor:
-Typo on page 8 "Defining"

### Questions
What model is used as VicLLM, in the results section?
Table 1 is somewhat confusing to me - what's the metric? Why linear mixed effects model?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a new threat model, "inferential adversaries,"which focus on safe AI responses can leak impermissible information. The author also proposed decomposition attack which is an automated black-box attack method for extracting and leveraging dual-use information to fulfill adversary objectives.

### Strengths
1. The authors provide a solid theoretical framework using information theory to quantify the risk of inferential adversaries, the proposed method surpass PAIR performance on curated WMDP dataset.

2. The paper is well-written and easy to follow.

### Weaknesses
Despite the proposed method's effectiveness, there are several areas where this paper could see significant improvements, including the coverage of related work, evaluation methods, formatting, and experimental setup details:

1. Inferential Adversaries vs. Jailbreak: The distinction between the proposed inferential adversaries and jailbreak attacks needs further clarification. From my perspective, inferential adversaries appear to be a relaxed version of jailbreak attacks. While jailbreak considers the generation of impermissible output by vicLLM as a successful attack, inferential adversaries deem any output containing impermissible information as a success. For example, in a 3-turn jailbreak[4], if only a 2-turn conversation is conducted, the LLM's response aligns with the inferential adversaries proposed by the author—it produces impermissible information rather than addressing the adversarial question directly.

2. Coverage of related work:The experiment only compare with PAIR however multiple other jailbreak methods are not included [1,2,3,4]. Such as TAP[1] which is a improved version of PAIR.

3. Experiment coverage: The experiment only conducted on a small dataset and two LLM. While its baseline method PAIR conducted on 7 LLMs including LLM with strong safety like Claude2,ChatGPT.  Mistral is not a suitable LLM for evaulation safety, input plain adversarial question also can achieve high attack success rate for Mistral.

4. Experiment Setup : The author did not provide detailed hyperparameters for the experiments nor conduct the necessary ablation experiments. The proposed DA approach overlooks potential system prompt mismatches and the impact of LLM generation sampling strategies on the results [5], potentially leading to considerable variance in result evaluations.

5. Lack of defense evaluation: The paper does not include any form of defense evaluation[6,7], which is a significant omission for a comprehensive understanding of the proposed method's implications.

6. (Minor) In Table I, the adversary model is listed as Llama-8B-Instruct, which could easily be misinterpreted as referring to the first-generation Llama.

### Questions
See weakness

### Soundness
1

### Presentation
3

### Contribution
2
