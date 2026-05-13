# TuBA: Cross-Lingual Transferability of Backdoor Attacks in LLMs with Instruction Tuning

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
The implications of backdoor attacks on English-centric large language models (LLMs) have been widely examined --- such attacks can be achieved by embedding malicious behaviors during training and activated under specific conditions that \emph{trigger} malicious outputs.
Despite the increasing support for multilingual capabilities in open-source and proprietary LLMs, the impact of backdoor attacks on these systems remains largely under-explored.
Our research focuses on \emph{cross-lingual backdoor attacks} against multilingual LLMs, particularly investigating how poisoning the instruction-tuning data for one or two languages can affect the outputs for languages whose instruction-tuning data were not poisoned. %~\footnote{We refer to these languages as \emph{unpoisoned languages}.}
Despite its simplicity, our empirical analysis reveals that our method exhibits remarkable efficacy in models like \mt5 and \gpto, with high attack success rates, surpassing 90\% in %many unpoisoned 
more than 7 out of 12 languages across various scenarios.
Our findings also indicate that more powerful models show increased susceptibility to transferable cross-lingual backdoor attacks, which also applies to LLMs predominantly pre-trained on English data, such as \llama, \llamat, and \gemma.
Moreover, our experiments demonstrate 1) High Transferability: the backdoor mechanism operates successfully in cross-lingual response scenarios across 26 languages, achieving an average attack success rate of 99\%, and 2) Robustness: the proposed attack remains effective even after defenses are applied.
These findings expose critical security vulnerabilities in multilingual LLMs and highlight the urgent need for more robust, targeted defense strategies to address the unique challenges posed by cross-lingual backdoor transfer.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper leverages instruction tuning and explores the backdoor transfer abilities of large language models across multiple languages. The paper empirically analyzes and finds that some multi-language large models achieve over 90% attack success rates in more than 7 languages. These findings underscore a widespread and language-agnostic vulnerability that threatens the integrity of MLLMs.

### Strengths
- The paper presents an interesting question, namely whether backdoor can transfer between multiple languages. The paper conducts a large number of experiments and finds that multi-language models, when fine-tuned with data from a few languages, also affect the performance of other languages.

- The organization of the paper is very complete, including chapters on attack settings and objectives, defenses against the proposed attack method, etc.

- The paper conducts experiments on some closed-source models (such as gpt-4o) to verify the practical impact, which is of great significance.

### Weaknesses
- This paper seems to only conduct empirical research? I think this kind of contribution may not be sufficient for top-level deep learning conferences such as ICLR. While this research is very interesting, I think that the findings of this study may not have very far-reaching significance. Can we further explore the underlying issues? For example, what deeper implications does this phenomenon reflect, and how can we improve the robustness of models in response to such phenomena?
- The empirical research in this paper only includes the scenario of instruction tuning, which seems insufficient for an empirical study. We know that the backdoor community has proposed a large number of methods, and there are also various ways of applying large language models. Is the phenomenon revealed in this paper widely prevalent?

### Questions
Please refer to the "Weaknesses" section for further information.

### Soundness
3

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
3

### Summary
The paper investigates the cross-lingual transferability of backdoor attacks in the instruction tuning of large language models (LLMs). The work demonstrates that backdoor attacks can effectively transfer across different languages and attack settings/objectives, even when the poisoned instruction-tuning data for specific languages is fixed (one or two). The authors provide experimental results with high attack success rates on models like mT5 and GPT-4o, across 26 different languages.

### Strengths
This paper was the first to investigate the cross-lingual transferability of backdoor attacks on LLM instruction tuning. The experiments for the cross-lingual attack effectiveness are well-designed, and the results are presented clearly in 6 European and 6 Asian languages (5,600 instances for each language).

### Weaknesses
1. The motivation of cross-lingual backdoor attack is week, because it seems that taking the same/similar threat model with the existing backdoor attacks on instruction-tuning (Inject a few ratio of poisoning data into the fine-tuning dataset).

2. Table 1 presents the results of performance of benign and backdoored models on benign inputs (benign functionality). But the description seems not mentioned: what’s the kind of language poisoned in instruction-tuning and the benign performance on different languages in inference. An additional analysis may enhance the results and demonstrate the benign functionality of the poison model. 

3. The evaluations on different LLM tasks (e.g., text summarization) with employ this cross-lingual backdoor attack can be provided for putting this work in larger application scope.

4. This paper provides attack results on cross-lingual transferability but lack of sufficient explanation to this property.

### Questions
Please refer to weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper focuses on cross-lingual backdoor attacks against multilingual LLMs via instruction tuning. Extensive evaluations show that poisoned one or two languages will affect the outputs for languages whose instruction-tuning data were not poisoned.

### Strengths
1. Instruction fine-tuning-based backdoor exposes vulnerabilities in multilingual LLMs.
2. The extensive evaluation effectively demonstrates the transferability of poisoned language to other languages.
3. Well-written and readable.

### Weaknesses
**1. Lack of a theoretical proof or interpretable analysis**

Although the authors demonstrate the backdoor portability of the MLLM model through extensive evaluation, they do not demonstrate why portability exists in terms of methodology and interpretability. This is important for exposing the vulnerability of instruction tuning on MLLM.

**2. Lack of novelty**

Similarly, due to the lack of instruction fine-tuning against MLLM vulnerability analysis (refer to Weakness 1), the work appears to be too engineered. In other words, there is no need for such a lengthy evaluation of this finding. If the authors start with a new attack strategy to achieve backdoor transferability it should be more solid. e.g. poisoning of a single language can significantly improve the attack transferability.

### Questions
1. Could the author explain in detail the definitions of English refusal and In-language refusal?

2. Could the author elaborate on the practical scenarios of backdoor attacks? Typically, adversaries inject backdoors into traditional PLMs, particularly in text classification tasks. For example, attackers may exploit triggers to evade spam detection systems. However, in generation tasks involving LLMs, the impact of an attack initiated by the adversary appears weaker compared to that initiated by the user. Research indicates that using instruction or scenario triggers can be more harmful than employing covertly selected triggers by attackers (see references [1-3]). In other words, what does it mean when a cross-linguistic backdoor is activated by an attacker? I believe it is more practical when users activate it, as attackers are the direct beneficiaries.

**Reference**

[1] TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models

[2] Backdooring Instruction-Tuned Large Language
Models with Virtual Prompt Injection

[3] Watch Out for Your Agents! Investigating Backdoor Threats to
LLM-Based Agents

### Soundness
3

### Presentation
3

### Contribution
3
