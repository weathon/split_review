# Can Language Models be Instructed to Protect Personal Information?

- Decision: Reject
- Scores: 3, 5, 6, 6

## Abstract
Large multimodal language models have proven transformative in numerous applications. 
However, these models have been shown to memorize and leak pre-training data, raising serious user privacy and information security concerns.
While data leaks should be prevented, it is also crucial to examine the trade-off between the privacy protection and model utility of proposed approaches.
In this paper, we introduce \dataset --- a multimodal benchmark to assess this privacy/utility trade-off when a model is instructed to protect specific categories of personal information in a simulated scenario.
We evaluate language models on \dataset~to examine how effectively an access control instruction can prevent models from selectively leaking protected personal information.
We also propose a technique to iteratively self-moderate responses, which significantly improves privacy.
However, through a series of red-teaming experiments, we find that adversaries can also easily circumvent these protections with simple jailbreaking methods through textual and/or image inputs. 
We believe \dataset~has the potential to support the development of new models with improved privacy protections, as well as the adversarial robustness of these protections. We release the entire \dataset~dataset at \url{https://llm-access-control.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents PRIVQA, a multimodal benchmark designed to evaluate the balance between privacy and utility in scenarios where a model must safeguard certain types of personal information. The performance of language models is assessed using PRIVQA to determine their ability to adhere to access control instructions and avoid revealing sensitive personal data. Additionally, this paper introduces a method for models to self-moderate their responses in a way that greatly enhances privacy protection.

### Strengths
Pros:
1. This research presents an open benchmark designed to evaluate language and vision models on their ability to safeguard personal information by adhering to instructions.
2. The study introduces a self-moderation approach that enhances the proficiency of models in complying with access control directives, while also revealing persistent biases in the protection afforded to diverse groups.
3. The paper details a sequence of red-teaming exercises, highlighting that current advanced models can be readily bypassed by adversarial methods when following access control instructions.

### Weaknesses
Cons:
1. The technical novelty is limited. This paper just tests whether or not the conventional instruction-tuned LLMs can protect privacy. The proposed “Self-Moderation” seems to slightly modify the previous “reflection” techniques in many previous works (there is a survey [1] on “reflection” techniques).
2. The title is misleading. The title is not very related to the core message of this paper because this paper does not conduct instruction tuning to protect privacy but just test whether or not the conventional instruction-tuned LLMs can protect privacy. So, the title should not be “Can Language Models be Instructed to Protect Personal Information?” but “Can Instruction-tuned Language Models Protect Personal Information?"
3. The contribution in the read teaming part is unclear. It seems this paper just directly applies the previous red teaming methods for an empirical study and do not propose any new read teaming method.
4. The connection between the read teaming part in Section 5 and privacy experiments in Section 4 is unclear. Can I also regard the privacy experiments in Section 4 as “read teaming”? Because the authors define “Red teaming has become a standard method to elicit and evaluate privacy, security, and bias concerns with language models” in Section 5. Based on my understanding, the privacy experiments in Section 4 are also “read teaming”. It is unclear why the authors define “read teaming” in Section 5 again. The content in Section 4 & Section 5 is overlapped.
5. This paper does not discuss any effective ways to protect privacy. Although this paper conduct an assessment on LMMs to follow instructions to protect personal information. The proposed Self-Moderation strategy seems to be not very effective. It is suggested the authors provide more insights on how to effectively protect privacy.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
2 fair

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
This paper introduces a new dataset for evaluating how well instruction-induced privacy protection mechanisms work. They also propose a mitigation over just using instructions, and then red-team the proposed mitigation.

The proposed dataset is an augmentation of 5 existing datasets, where protected groups and information is defined over the data, and the goal is to get utility of the QA task, without revealing the sensitive information. The tasks are defined both for open-ended generation and for visualQA. The desired behavior is that if the model is asked a question regarding a sensitive topic, it abstains from answering, but answers utility related questions. The proposed mitigation is self-moderation, where the model is given its own response and asked to improve it. 

The authors then red-team the proposed method through prompt injection and show that more fundamental solutions are necessary.

### Strengths
1. The paper looks at an important problem, as LLMs are bing used more and more and prompting and instruction tuning is ubiquitous.

2. I particularly like the visual aspect of the work and looking into multimodal models, as there aren't many existing works that focus on these models.

### Weaknesses
1. The threat model of the paper is not at all clear, neither is the paper positioned well among prior work. What is the privacy definition? What are we trying to protect, is it training data?  inference data? what is the actual application that the authors are targeting? what is the real world use-case?  It seems like the authors are targeting training data, however, according to existing extraction attacks [1], this is not a realistic scenario and not a real problem. There is no successful extraction attack that would so easily, from an instruction tuned model, extract any information that is not repeated many many times. The questions work in this dataset, since the authors target celebrities. So I think trying to protect training data here is not really sensible. The inference data, that would make more sense, which seems to be the case in the visual part of the paper? But then, in that case, what is a realistic scenario? In general it is very unclear what is happening here.

2. The dataset is not curated in a principled way and is too artificial. There are no levels to what is being protected, and how it needs protection. The attributes are artificially inserted.

3. I think the authors need to first discuss the related work better: talk about existing membership inference and extraction attacks, about the risks, and then about differential privacy and other protection methods, and then position the paper with regards to all that.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a new benchmark PrivQA to study the ability of language model to follow instructions about access control and to study the privacy utility trade-off. PrivQA includes both textual and multimodal tasks, where the models are asked to answer questions or abstain from answering if they involve sensitive data. The paper evaluates current generation models such as GPT-4 and Llama-2. The authors find that these models leak a lot of private information even if they're instructed not to. Self moderation improves the results significantly. The authors also consider an adversarial settings and find that under a multi-hop threat model attacks succeed nearly always.

### Strengths
- The paper provides a valuable benchmark for privacy protection in language models, which is an emerging and important research area. There are few existing datasets that focus on privacy issues in language models.
- The paper uses state-of-the-art models for the evaluation, which makes the results more relevant and convincing.

### Weaknesses
 - The paper does not share the code or data to reproduce the results, which limits the reproducibility and verifiability of the work. The paper says the URL is removed for review, but there are ways to share it anonymously (e.g. anonymous.4open.science).
- The paper uses evaluation metrics that do not capture the severity of privacy breaches. Privacy is about preventing the worst-case scenarios, not the average ones. Therefore, privacy metrics should reflect that even a single leak of private data is unacceptable. For example, in differential privacy, δ is set to a very small value or in membership inference attacks, TPR is reported at very low FPR. The paper shows some trends of privacy improvement (e.g. self moderation), but none of the methods offer adequate protection for realistic scenarios.

### Questions
- Clarification in section 3.1. Is it true that $\mathbb{P}\mathbb{G}\cup\mathbb{C}\mathbb{G}=\mathcal{X}$? If so, it might be helpful to state this rather than the subset relation.
- Why are there such noticable differences in model sizes in figure 2 and why do larger models have more privacy violations? I would expect that larger models follow instructions better.
- Clarification: What are head entities as described in the last paragraph on page 7.
- Could you respond to the 2nd point in weaknesses? Would you consider any of the presented methods adequate for use in a realistic setting?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
==*== Paper summary

This paper discusses the impact of large multimodal language models in various applications and the privacy and security concerns associated with their use. These models have been observed to memorize and unintentionally disclose pre-training data, posing significant privacy risks. The paper introduces PRIVQA, a multimodal benchmark designed to evaluate the trade-off between privacy protection and model utility. PRIVQA simulates scenarios where models are instructed to safeguard specific categories of personal information. The evaluation on PRIVQA assesses how well access control instructions can prevent models from leaking protected personal data. The paper also presents a method for iteratively moderating model responses, enhancing privacy. However, the study reveals that adversaries can easily bypass these protections through simple jailbreaking techniques using text or image inputs. The authors suggest that PRIVQA can aid in the development of improved privacy protection in models and enhance their resilience against adversarial attacks.

### Strengths
==*== Strengths

+ The paper proposes PRIVQA, a multimodal benchmark designed to evaluate the trade-off between privacy protection and model utility.
+ The research question is well defined and valuable to the research community.
+ Extensive case studies.

### Weaknesses
==*== Weaknesses

- The convincingness of the output experimental results still needs to be further improved.
- Comparisons with more advanced baseline methods are needed to highlight the advantages of the proposed privacy preserving techniques.
- The technical depth of this paper needs to be further improved.

### Questions
==*== Comments for author

Q1: In Figure 9, the authors present an illustrative case to expound upon the privacy-utility trade-off inherent in the current GPT-4 model, particularly with respect to its handling of location information. Evidently, the showcased examples elucidate the inadvertent disclosure of image location data by GPT-4. Nevertheless, a pertinent query arises as to whether GPT-4 would also inadvertently divulge location information in the case of images depicting unfamiliar landmarks or attractions. To address this question comprehensively, it is imperative to consider the pervasive practice of mobile devices embedding geospatial data within the photographs they capture. In the event that an adversarial agent can effectively employ tailored adversarial prompts to prompt GPT-4 to discern the geographic origin of such photographs, it would substantially enhance the persuasiveness of the assertion.

Q2: More baselines still need to be added to illustrate the superiority of the proposed self-moderation technology. Indeed, the reviewer knows that the main contribution of this paper is not the designed self-moderation technology, but it would be better if existing privacy protection technologies could be more comprehensively explored to illustrate the privacy concerns of existing multi-modal large language models. For instance, it would be judicious to incorporate emerging data right-to-forget protection technologies, such as machine unlearning, as a baseline reference. By doing so, the authors can provide a more robust and convincing assessment of the available privacy-preserving techniques within the context of multi-modal large language models.

Q3: The reviewers acknowledge that the PRIVQA benchmark data set proposed in this paper already includes a variety of privacy attribute information. I might expect that the benchmark data set could include more sensitive private information such as race, occupation, address, bank account, etc.

Q4: To be candid, I find myself in a somewhat uncertain position regarding the alignment of the proposed benchmark dataset with the prevailing perspectives within the ICLR community. There exists a degree of ambiguity concerning whether the technical intricacies involved in dataset creation adequately conform to the community's overarching scope and the stipulated requirements for paper submissions. It may be prudent to consider that the NeurIPS dataset track could potentially represent a more suitable forum for the presentation and evaluation of this dataset, given its specific focus and expertise in dataset-related matters.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
