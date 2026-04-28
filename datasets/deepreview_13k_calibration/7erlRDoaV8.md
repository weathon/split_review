# Can Sensitive Information Be Deleted From LLMs? Objectives for Defending Against Extraction Attacks

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8

## Abstract
Pretrained language models sometimes possess knowledge that we do not wish them to, including memorized personal information and knowledge that could be used to harm people. They can also output toxic or harmful text.
To mitigate these safety and informational issues, we propose an attack-and-defense framework for studying the task of deleting sensitive information directly from model weights.
We study direct edits to model weights because (1) this approach should guarantee that particular deleted information is never extracted by future prompt attacks, and (2) it should protect against whitebox attacks, which is necessary for making claims about safety/privacy in a setting where publicly available model weights could be used to elicit sensitive information. 
Our threat model assumes that an attack succeeds if the answer to a sensitive question is located among a set of $B$ generated candidates, based on scenarios where the information would be insecure if the answer is among $B$ candidates. 
Experimentally, we show that even state-of-the-art model editing methods such as ROME struggle to truly delete factual information from models like GPT-J, as our whitebox and blackbox attacks can recover ``deleted'' information from an edited model 38\% of the time. These attacks leverage two key observations: (1) that traces of deleted information can be found in intermediate model hidden states, and (2) that applying an editing method for one question may not delete information across rephrased versions of the question. 
Finally, we provide new defense methods that protect against some extraction attacks, but we do not find a single universally effective defense method.
Our results suggest that truly deleting sensitive information is a tractable but difficult problem, since even relatively low attack success rates have potentially severe implications for the deployment of language models in a world where individuals enjoy ownership of their personal data, a right to privacy, and safety from harmful model outputs

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the removal of memorized information from language models via direct editing of model weights. The paper first establishes a threat model for  LLM extraction, based on the notion of recovery of sensitive information from $B$ candidates. The paper then describes several new attacks: two variants of whitebox attacks, in which an attacker may utilize probabilities computed from intermediate hidden states in the model to aid in recovery, and a blackbox attack, in which an input query is “rephrased'' multiple times by the model to generate a diverse set of candidate responses. Finally, the paper describes and evaluates several defenses against the attacks, which are able to be applied in conjunction with existing model editing techniques.

### Strengths
- Paper works on interesting and challenging problems, which are highly relevant to real-life use cases.

- The paper is novel in its framing of the problem - in particular, considering model editing for data removal is fairly unique in literature.

- The paper is quite broad spanning, presenting both multiple attacks and defenses for machine unlearning.

### Weaknesses
 **Lack of experiments** - The paper could be more comprehensive if more scenarios were presented in the paper, e.g. combining attacks (to maximize extraction under a budget) or combining defenses (to explore how much risks could be minimized in practice). I find it hard to draw actionable conclusions from the results, and further discussion and variety of results may help justify the strength of model editing as the de-facto paradigm for unlearning.

**No comparison to prior works** - I’m concerned about the lack of comparison to prior works. While the paper claims that prior works is not applicable due to focus on removal of influence of a pair $(x,y)$, the problem formalized in the paper (based on the ASR metric) is exactly the recovery of a single token label $y_i$ given a specific prompt $x_i$. Hence, I’m confused why it’s not possible to compare with prior approaches in approximate unlearning.

### Questions
- I’m a bit confused by the distinction between the password attempts and parallel extractions scenarios in the context of the paper. Is the distinction here meant to be that information gained in the recovery of a previous attempt may be utilized to aid recovery of the next attempt? If so, I do not understand how the attacks as described utilize information in this way (i.e. it seems all attack methods generate a candidate set for a budget $B$ in parallel anyways). Is such an attack possible?

- In Sec. 2 “Attacking LLMs for Sensitive Information”, the paper claims that the described method does not assume access to the exact text used during pre-training of the model. However, the experiments do assume such access, as even in the rephrasing attack, the ground-truth prompt is perturbed by a rephrasing model. Is it possible to run the rephrasing attack without the ground-truth prompt?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates model editing methods to remove sensitive information from LLM. This work shows that "deleted" information can be extracted from the hidden state when the attacker uses a smaller budget of verification attempts. Simple rewriting of prompts can also cause LLM to generate sensitive information. This is an interesting study, and the attack and defense methods it provides are worthy of further study and discussion.

### Strengths
This work elaborates on the security issues of LLMs from the perspective that hidden states may leak sensitive information. It presents potential attack methods and defense strategies.

### Weaknesses
This work provides an incomplete description of the reasons behind some experimental phenomena. The reasons or intuitions why defense strategies based on data augmentation do not work are not revealed. Specifically, the paper does not fully explore the interaction between the paraphrasing used in the defense and the paraphrasing used in the attack. It's unclear if the defense fails because it's inherently flawed or because the attack is using paraphrases that are too different from the training data. A more thorough analysis of the semantic similarity between the paraphrases used in training and attack is needed. For instance, are the paraphrases generated by the defense strategy semantically diverse enough to cover the space of potential attack paraphrases? Furthermore, the paper does not discuss the potential for adversarial paraphrases that are specifically designed to bypass the defense, which could be a significant vulnerability.

### Questions
This paper shows some interesting results. My main question is whether the author can give more detailed insights or possible mechanisms for the findings in the paper. For example, why do the hidden states of LLMs reveal sensitive information? What is the intuition behind this phenomenon? Why are defense strategies based on data augmentation ineffective?

In addition, can fine-tuning, a typical defense strategy, be combined with the defense scheme (e.g., Head Projection Defense) proposed in this paper to produce a more powerful defense method?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies whether a piece of information can be effectively deleted from an LLM. The authors adapt two model editing techniques to the task of suppressing a piece of information from an LLM. They then evaluate the robustness of these techniques, combined with different defense approaches, to several new attacks (both black-box and white-box) aiming to extract that piece of information from the LLM. The authors propose a new threat model, where the attack is considered successful if the targeted information is among B candidates produced by the attack. Empirical results using one of the model editing techniques, ROME, show that it’s not always effective, as the targeted information can still be extracted 38% of the time in a white-box setting and 29% of the time in a black-box setting. The authors further show that defense techniques can reduce the risk at a small cost in utility, but that in some cases they still remain vulnerable to attacks they don’t explicitly protect against.

### Strengths
- 1) Important problem: can information be deleted from an LLM? The premise of the paper, that the right way to delete information is to modify the model post-hoc instead of curating the training dataset, is quite contentious. In spite of this, for practical reasons model developers might indeed not curate their training data, which motivates the need to evaluate the robustness of model editing techniques.
- 2) Well-motivated threat model, based on the insight that considering some information to be deleted only if it cannot be recovered directly (B=1) is an insufficient requirement.
- 3) The technical contribution of the paper (attacks and defenses) is insightful, well motivated and clearly described.

### Weaknesses
 - 1) The findings of the paper are somewhat expected, as the model editing techniques being evaluated are heuristics and don’t come with formal guarantees of robustness against attacks. Similarly, it is expected that a defense designed to mitigate a specific attack is robust against that attack but not necessarily against other attacks.
- 2) Insufficient analysis of results. I was left wondering what are the technical differences between ROME and MEMIT and whether this could explain some of the differences in the results. 

Minor (suggestions for improvement):
- 3) Confusing usage of the term “sensitive”: The definition used by the authors includes “toxic” information: “Models can also generate text reflecting beliefs that cause direct psychological harm to people (i.e. toxic generated text) (Kenton et al., 2021). Facts or beliefs of this kind are known as sensitive information (Brown et al., 2022)”. I'm pretty sure that’s not how Brown et al. use the word sensitive. In the privacy domain, “sensitive information” refers to protected characteristics about an individual (https://commission.europa.eu/law/law-topic/data-protection/reform/rules-business-and-organisations/legal-grounds-processing-data/sensitive-data/what-personal-data-considered-sensitive_en) or is sometimes used colloquially to denote private information that a model or system should not disclose. To avoid confusion, I would suggest using a different term that explicitly refers to “toxic” information.

### Questions
- 1) What are the results of attacking the MEMIT method without any defenses (i.e., the equivalent of Figure 4)? The paper’s second claim is that model editing methods fail to delete information; basing it on only one of two editing methods studied in the paper weakens the claim and raises questions.
- 2) Do the authors think that model editing is technically possible with formal guarantees against attacks and what are, in the authors’ opinion, promising directions for future work in this domain?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper shows that models edited by model editing methods ROME and MEMIT still contain sensitive information and that the information is not fully "deleted" from the model. Several white-box and one black-box attack are proposed which are used to extract information from edited models, given that the attacker has an attack budget B. If the sensitive information is in within the B output candidates the information is assumed to be leaked. In addition to the attacks, the paper proposes multiple defense methods. Both the attacks and defenses are evaluated on the Counterfact and zsRE dataset. The evalution shows that the defense methods are not enough to defend against extraction attacks and that even in a black-box setting, information can still be extracted after editing the model.

### Strengths
- the paper is well written and easy to follow
- code and everything to reproduce the experiments is given
- the evaluation is quite thorough, evaluating multiple defenses against multiple attacks

### Weaknesses
For me it is not quite clear how the proposed defense methods are combined with the model editing techniques. In the experiments, ROME and MEMIT are used as model editing techniques. However, it is not mentioned how the different optimization objectives for the proposed defense techniques are used in combination with these methods. This could be formulated a bit clearer.

Misc:
- it would be easier to read if the paragraph in 4.2 also had a bold subheading with the name of the attack, instead of putting the name in the heading of the section. This would make it easier for readers to spot the names of the different attacks.

### Questions
- **Q1:** Why use only single-token answers? If I understand this correctly, this way it is not possible to extract answers which consist of multiple tokens, correct? Is it possible to modify your approach to make this work for multi-token answers?
- **Q2:** I don't quite understand how the Head Projection defense works. What exactly are the values D_answer and D_k? As far as I understand, D_answer is a probability distribution, while D_k is a single value? Could you clarify the loss function and what exactly is optimized for this defense?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
