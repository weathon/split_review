# BadRAG: Identifying Vulnerabilities in Retrieval Augmented Generation of Large Language Models

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
Large Language Models (LLMs) are constrained by outdated information and a tendency to generate incorrect data, commonly referred to as "hallucinations." Retrieval-Augmented Generation (RAG) addresses these limitations by combining the strengths of retrieval-based methods and generative models. This approach involves retrieving relevant information from a large, up-to-date dataset and using it to enhance the generation process, leading to more accurate and contextually appropriate responses. Despite its benefits, RAG introduces a new attack surface for LLMs, particularly because RAG databases are often sourced from public data, such as the web. In this paper, we propose \TrojRAG{} to identify the vulnerabilities and attacks on retrieval parts (RAG database) and their indirect attacks on generative parts (LLMs). Specifically, we identify that poisoning several customized content passages could achieve a retrieval backdoor, where the retrieval works well for clean queries but always returns customized poisoned adversarial queries. Triggers and poisoned passages can be highly customized to implement various attacks. For example, a trigger could be a semantic group like "The Republican Party, Donald Trump, etc." Adversarial passages can be tailored to different contents, not only linked to the triggers but also used to indirectly attack generative LLMs without modifying them. These attacks can include denial-of-service attacks on RAG and semantic steering attacks on LLM generations conditioned by the triggers.
Our experiments demonstrate that by just poisoning 10 adversarial passages \textemdash\ merely 0.04\% of the total corpus \textemdash\ can induce 98.2\% success rate to retrieve the adversarial passages. Then, these passages can increase the reject ratio of RAG-based GPT-4 from 0.01\% to 74.6\% or increase the rate of negative responses from 0.22\% to 72\% for targeted queries. 
This highlights significant security risks in RAG-based LLM systems and underscores the need for robust countermeasures.
\textcolor{red}{Warning: This paper contains content that can be offensive or upsetting.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes BadRAG as an attack on RAG. It is identified that poisoning several customized content passages could achieve a retrieval backdoor, where the retrieval works well for clean queries but always returns customized adversarial passages for triggered queries. Triggers and adversarial passages can be highly customized to implement various attacks. Utilizing contrastive optimization, BadRAG generates adversarial passages activated only by specific triggers. DOS and sentiment steering attacks are also explored.

### Strengths
1. This paper focuses on an important area, the security and safety of RAG.

### Weaknesses
1. This paper performs adversarial attack using backdoor settings. Concepts in this paper is misused.
2. The method used is adversarial attack, but it need to be introduced in the training phase, rather than the traditional test phase direct attack.
3. The former related work is nor discussed. [TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models.]

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
Large language models (LLMs) have gained significant success due to their outstanding generative abilities. However, they come with limitations, including outdated knowledge and hallucinations. To overcome these issues, RAG has been introduced in recent years. In this paper, the authors present BadRAG, which uncovers security vulnerabilities and facilitates direct retrieval attacks triggered by tailored semantic cues, along with indirect generative attacks on LLMs using a compromised corpus.

### Strengths
1) The paper is clearly written and easy to understand.
2) Comprehensive experiments showcase the effectiveness of the proposed attack.

### Weaknesses
1) The threat model is unrealistic.
2) Key baselines are absent.

### Questions
The authors of this paper propose a new attack method to mislead the RAG system. Overall, the paper is well-written. Here are a few comments for the authors:

1) In the "Attacker’s Capabilities and Attacking Cases" section, the authors assume that the attacker has access to the RAG retriever and provide examples to support this assumption. However, this is a strong assumption, as in practice it is difficult, if not impossible, for an attacker to access the parameters or query the retriever. The authors should not assume that the attacker has this knowledge outright. Similar to paper [A], the authors could consider two scenarios: a black-box setting and a white-box setting. The attacks discussed in this paper align more with a white-box setting. Therefore, the authors should also include experiments that reflect a black-box setting.
2) The paper lacks essential baselines. It seems feasible to adapt the attacks from [A] to the context described in this paper. The authors should include important baseline comparisons.
3) During the retrieval phase, only k relevant passages are retrieved, but the default value of k used in the paper is not specified.
4) There are various potential defenses against the proposed attacks, such as paraphrasing. The authors should also evaluate the attack’s performance when such defense mechanisms are employed.


[A] PoisonedRAG Knowledge Poisoning Attacks to Retrieval-Augmented Generation of Large Language Models.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work studies safety issues in RAG. Specifically, it considers backdoor attacks on RAG systems and proposes the BadRAG framework. Within the proposed framework, backdoor triggers and adversarial passages can be customized to implement various attacks. The authors conducted experiments to demonstrate the effectiveness of their attacks. This highlights significant security risks in RAG-based LLM systems and underscores the need for robust countermeasures.

### Strengths
- The safety aspect of RAG is relatively underexplored.  
- The presentation is clear and easy to follow.  
- Related work is properly and comprehensively discussed.

### Weaknesses
I have two main concerns.

- The overall novelty of the proposed work appears to be somewhat limited. It essentially extends backdoor concepts to the retrieval context and, consequently, to RAG scenarios. There are already existing studies in this area, such as Long et al.'s work, "Backdoor Attacks on Dense Passage Retrievers for Disseminating Misinformation." I do not perceive a significant distinction between this work and others, other than differences in how the 'backdoor trigger' words are set up, which I find difficult to regard as a strong novelty.

- The requirement for obtaining the gradients of the embedding model (retriever) is not practical, making the proposed attacks less realistic. In real-world applications, people often slightly fine-tune the embedding model (for retrieval) to better suit their tasks. Additionally, the proposed attacks can only target publicly available models; however, in practice, one often opt for proprietary models, such as GPT's embedding model, for better performance.

Overall, I feel that the limited novelty and impractical assumptions about the attacks lead me to reject this paper.

### Questions
-

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a new method of injecting malicious passages into databases so that RAG systems either does not respond to the user query or generate bias content. The method consists of  Crafting a malicious document targeted at the retriever to ensure the retrieved top-k results contain the malicious passages to achieve the attacker's objectives. Experiments demonstrate the effectiveness of this attack.

### Strengths
1. This paper presents a new attack framework, BadRAG, which manipulates the output of RAG systems by injecting a multiple malicious  passages under specific trigger conditions, expanding the scope of adversarial attacks.
2. The paper is well written except Section 3.2, which is hard to parse.
3. The retriever-phase of the RAG attack was novel.

### Weaknesses
1. The description of the Generation-phase of the attack is confusing. Having an end-to-end example in this scenario would be better for clarity.
2. Limited adversarial objectives. The attack would not work for scenarios where the adversarial objectives goes against the safety alignment of RAG Generator, such as writing hateful speech, etc. 
3. Contrived setup for security critical privacy based attacks such as "Tool Usage" and "Context Leakage".
4. No discussion on the limitations of the RAG attack such as described above.
5. The citation for TrojanRAG seems to be incorrectly labeled as "Phantom." It would also be good to know what are the advantages or drawbacks with Phantom as well?
6. In the generation phase for refusal responses, why not simply include a command like “Sorry, I cannot answer” directly after the retriever tokens in the adversarial passage? How is the alignment feature being retrieved in your approach, and could you elaborate on that?
7. The setup for Context Leakage and Tool Usage objectives appears different from others, where natural triggers were used. Why was “cf” chosen instead of using the prior triggers like “Donald Trump”? Also, the attack seems to succeed in breaking RAG’s alignment with commands like “Please ignore all previous commands..” without explicit jailbreaking. Could you clarify why this is sufficient while prior work required jailbreak [1]?
8. How does the attack perform when adversarial passages make up only a smaller portion of the top-k results, such as only 1 out of 10, 2 out of 10, or 5 out of 10 passages?
9. The results indicate transferability across retrievers. Prior work on RAG [2,3] suggests attacks don’t typically transfer across retrievers. I don't see any additional optimization used for transferability, would be great to give some insight on this?

### Questions
1.The citation for TrojanRAG seems to be incorrectly labeled as "Phantom." It would also be good to know what are the advantages or drawbacks with Phantom as well?

2. In the generation phase for refusal responses, why not simply include a command like “Sorry, I cannot answer” directly after the retriever tokens in the adversarial passage? How is the alignment feature being retrieved in your approach, and could you elaborate on that?

3. The setup for Context Leakage and Tool Usage objectives appears different from others, where natural triggers were used. Why was “cf” chosen instead of using the prior triggers like “Donald Trump”? Also, the attack seems to succeed in breaking RAG’s alignment with commands like “Please ignore all previous commands..” without explicit jailbreaking. Could you clarify why this is sufficient while prior work required jailbreak [1]?

4. How does the attack perform when adversarial passages make up only a smaller portion of the top-k results, such as only 1 out of 10, 2 out of 10, or 5 out of 10 passages?

5. The results indicate transferability across retrievers. Prior work on RAG [2,3] suggests attacks don’t typically transfer across retrievers. I don't see any additional optimization used for transferability, would be great to give some insight on this?

[1] Dario Pasquini, Martin Strohmeier, and Carmela Troncoso. Neural exec: Learning (and learning
from) execution triggers for prompt injection attacks.

[2] Zexuan Zhong, Ziqing Huang, Alexander Wettig, and Danqi Chen. Poisoning retrieval corpora by
injecting adversarial passages.

[3]    Wei Zou, Runpeng Geng, Binghui Wang, and Jinyuan Jia. PoisonedRAG: Knowledge poisoning
attacks to retrieval-augmented generation of large language models.

### Soundness
3

### Presentation
3

### Contribution
3
