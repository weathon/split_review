# CollabEdit: Towards Non-destructive Collaborative Knowledge Editing

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Collaborative learning of large language models (LLMs) has emerged as a
new paradigm for utilizing private data from different parties to guarantee
efﬁciency and privacy. Meanwhile, Knowledge Editing (KE) for LLMs has also
garnered increased attention due to its ability to manipulate the behaviors of
LLMs explicitly, yet leaves the collaborative KE case—in which knowledge
edits of multiple parties are aggregated in a privacy-preserving and continual
manner—unexamined. To this end, this manuscript dives into the ﬁrst investigation
 of collaborative KE, in which we start by carefully identifying the unique
three challenges therein, including knowledge overlap, knowledge conﬂict, and
knowledge forgetting. We then propose a non-destructive collaborative KE
framework, COLLABEDIT, which employs a novel model merging mechanism
to mimic the global KE behavior while preventing the severe performance drop.
Extensive experiments on two canonical datasets demonstrate the superiority of
COLLABEDIT compared to other destructive baselines, and results shed light on
addressing three collaborative KE challenges and future applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates the collaborative knowledge editing (KE) for large language models (LLMs). It identifies three primary challenges in this domain: knowledge overlap, knowledge conflict, and knowledge forgetting. The authors propose a framework called COLLABEDIT, which utilizes a non-destructive model merging mechanism to aggregate knowledge edits from multiple parties while maintaining performance and privacy.

The framework aims to mimic the optimal global editing behavior without the significant performance drops associated with existing destructive methods. Through extensive experiments on canonical datasets, the authors demonstrate that COLLABEDIT outperforms traditional approaches, addressing the identified challenges effectively.

### Strengths
COLLABEDIT allows for non-destructive knowledge editing, which prevents significant performance drops that are common in traditional methods

The framework is versatile and can integrate existing knowledge editing methods, providing a comprehensive solution to collaborative KE challenges

Empirical results show that COLLABEDIT outperforms existing destructive baselines, demonstrating superior editing performance even with a large number of edits

### Weaknesses
The non-destructive merging mechanism may introduce additional complexity in implementation compared to simpler, traditional methods.

Its scalability in large collaborative environments or with numerous clients may need further exploration.

More experiments on different LLMs could benefit the demonstration of the effectiveness of the proposed method.

### Questions
See above.

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
3

### Summary
This paper addresses the generalization of knowledge editing within the collaborative learning setting, with a focus on ensuring privacy while modifying the knowledge of large language models (LLMs). The authors propose a novel approach by sharing $KK^{T}$, an intermediate weight associated with the keys of edited knowledge, instead of naively sharing and averaging weights, which is theoretically proven to be resistant to attacks. The experiments conducted demonstrate the effectiveness of the proposed approach.

### Strengths
+ The paper tackles an important problem of generalizing knowledge editing to collaborative learning settings where privacy is a critical concern.
+ The authors provide a compelling theoretical analysis of the limitations of naive weight sharing and introduce the concept of sharing $KK^{T}$, which is proved to be difficult to attack in the traditional privacy-aware setting.
+ The experiments conducted seem to effectively demonstrate the effectiveness of the proposed method.

### Weaknesses
 - It is not surprising to see the destructive performance of direct fed-average for knowledge editing, as edits individual client are naturally diluted when models are averaged, although I appreciate the formal mathematical treatment of the issue.
- While knowledge conflict is identified as a key challenge, the paper addresses it in a rather ad hoc manner compared to other challenges, which are supported by theoretical analysis. Specifically, the approach of using FCFS and data augmentation lacks a strong theoretical foundation and does not consider the semantic relationships between conflicting edits. This could lead to suboptimal outcomes where less important edits are prioritized simply because they were submitted earlier, or where data augmentation fails to capture the nuances of the intended knowledge modification.
- My biggest concern is on the privacy part of the model. Although the authors propose to share $K^{T}K$ and providing theoretical proof of its resistance to attacks, the paper does not fully address the new privacy challenges faced by LLMs. If the edit is successful, the new knowledge can be easily prompted out from the LLMs by simply asking questions. This is especially convenient given that most knowledge editing tasks involve only the editing of factual knowledge. Therefore, the traditional privacy methods may not suffice in the LLM case, and further exploration in preserving privacy for knowledge editing is needed.

### Questions
Please refer to my summary of my weaknesses.

### Soundness
2

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
This paper introduces COLLABEDIT, a framework designed for collaborative knowledge editing (KE) in LLMs within federated learning scenarios. COLLABEDIT allows multiple parties to collaboratively edit the knowledge in LLMs while preserving data privacy, a novel scenario within knowledge editing and federated learning. It addresses three main challenges—knowledge overlap, knowledge conflict, and knowledge forgetting—by implementing a non-destructive model merging technique that aims to achieve performance close to direct global model editing without degrading results. Extensive experiments on GPT-J and GPT2-XL demonstrate the effectiveness of COLLABEDIT, showing improvements over existing approaches in federated scenarios.

### Strengths
* The paper identifies and addresses a novel problem of knowledge editing in federated learning for LLMs, a new setting within model editing research.
* The authors propose a straightforward yet effective method—COLLABEDIT—that enables privacy-preserving collaborative editing, which is an essential consideration in multi-party learning scenarios.
* Experiments on GPT-J and GPT2-XL show that COLLABEDIT can substantially improve performance over methods like MEMIT in federated settings, highlighting its practical effectiveness in this new problem space.

### Weaknesses
 * The need for collaborative knowledge editing within federated LLM may be limited, as large-scale federated LLM scenarios are currently uncommon. This reduces the perceived applicability and impact of the problem being solved.
* The experiments are conducted on older models like GPT-J and GPT2-XL. More recent models such as LLaMA-2, LLaMA-3, or Gemma would provide stronger validation of the proposed method’s efficacy.
* The paper’s structure could benefit from refinement, as some figures and tables (e.g., Figure 3 and Table 4) are misaligned, affecting readability and presentation quality.

### Questions
* Why was the setup of editing 10 models with 500 requests (Table 1 and 2) per model not applied consistently in Table3?
* Could you clarify why the MCF dataset was not included in experiments in Table 3? This dataset would likely provide a valuable benchmark for evaluating the framework’s robustness in handling knowledge conflicts.
* In the knowledge overlap experiments, the focus was on the  R value’s  $\ell_2$-norm rather than directly showing the editing method’s performance. How does COLLABEDIT perform when subjected to repeated editing requests for the same knowledge items?

### Soundness
3

### Presentation
3

### Contribution
3
