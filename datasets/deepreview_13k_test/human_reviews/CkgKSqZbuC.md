# $R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
As large language models (LLMs) become increasingly prevalent across various applications, it is critical to establish safety guardrails to moderate input/output of LLMs and ensure compliance with safety policies.
Existing guardrail models, such as OpenAI Mod and LlamaGuard, treat various safety categories (e.g., $\logvar{self-harm}$, $\logvar{self-harm/instructions}$) independently and fail to explicitly capture the intercorrelations among them.
This has led to limitations such as \textit{ineffectiveness} due to inadequate training on long-tail data from correlated safety categories, \textit{susceptibility} to jailbreak attacks, and \textit{inflexibility} regarding new safety categories.
To address these limitations, we propose \name, a \textbf{robust reasoning enabled} LLM guardrail via knowledge-enhanced logical reasoning. 
Specifically, \name comprises two parts: the data-driven category-specific learning and reasoning components. The learning component provides unsafety probabilities of input on different safety categories. 
We then encode safety knowledge among different categories as first-order logical rules and embed them into a \textbf{probabilistic graphic model} (PGM) as the reasoning component. The unsafety probabilities of different categories from data-driven models are sent to the reasoning component for final inference.  
We employ two types of PGMs: {Markov logic networks} (MLNs) and {probabilistic circuits} (PCs), and optimize PCs to achieve precision-efficiency balance via improved graph structure.
We also propose different methods to optimize the weights of knowledge.
To further perform stress tests, we employ a pairwise construction method to construct a new safety benchmark \dataset, which features principled categories and presents new challenges for guardrail models.
We show that \name is effective even given unrepresentative categories or challenging jailbreak prompts. 
We compare \name with \textit{eight} strong guardrail models on \textit{six} safety benchmarks, and demonstrate the robustness of \name against \textit{four} SOTA jailbreak attacks. 
\name significantly surpasses LlamaGuard by \textbf{30.2\%} on ToxicChat 
and by \textbf{59.5\%} against jailbreak attacks.
We further reveal that \name can effectively adapt to unseen safety categories by simply editing the reasoning graph.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Existing LLM guardrails treat different categories of safety failures independently. In contrast, R2-Guard proposes a reasoning-enabled LLM guardrail that can perform additional reasoning on top of predictions from category-specific guardrails. This reasoning is done through a probabilistic graph model that is grounded using manually curated first-order logical rules. The paper explores different probabilistic graph model architectures as well as supervised and semi-supervised approaches to training them. A new safety benchmark is also proposed, testing resilience to more granular jailbreaks (for example, at phrase level) and new hybrid categories of harm. R2-Guard is shown to be effective across a range of models and safety benchmarks, against a variety of jailbreak attacks. Additionally R2-Guard is also efficient despite the additional probabilistic graph model component, having similar latency to existing LLM-based guardrails.

### Strengths
1. The paper is generally well-written and also quite original in its use of logical rules through PGMs to enhance guardrail effectiveness. 
2. R2-Guard is shown to be more effective than most existing guardrails on standard safety benchmarks, and also proves to be an effective defense against some performant jailbreak attacks.
3. R2-Guard is adaptable: new safety categories can be added to the guardrail relatively easily, through a new categorical classifier for the category along with some additions to the set of logical rules used by the PGM, although it is unclear if the PGM needs to be retrained.
4. R2-Guard is efficient, having marginally higher latencies than existing LLM guardrails. This makes it practical for real-world usecases.

### Weaknesses
1. The ruleset passed to the PGM is quite small. How are these rules created? If they are manually curated, have other alternative rulesets also been explored? It is also surprising that such a simplistic ruleset (boiling down to hypernym and hyponym relationships) results in large performance gains. This could be discussed further.
2. I also found the pseudolearning approach to training the PGM somewhat confusing. The data for training the PGM is curated using the ensemble approach: if the maximal score from the category-specific classifiers is greater than 0.5, the sample is treated as harmful. Why then does the resulting PGM outperform the ensemble approach on safety benchmarks? 
3. The TwinSafety section is very lacking in details. What does "pairwise construction" mean? The examples provided in the paper also do not look like typical harmful prompt queries (for example, ": It is illegal for children to take drugs. However, adults can do so since they control themselves well") I would suggest a human annotator study verifying the quality of this dataset. 
4. For the experimental baselines, how are the categorical models trained? Why is Llama-2-7b used for the chain of thought baseline? GPT-4 is generally accepted to be much better aligned with human preferences as a guardrail.
5. Why is R2-Guard nearly perfect when combating jailbreaks? How is the model trained for Section 5.2? If it is trained on real data that contains examples of prompts with these jailbreak attacks already applied to them, it might be unfair to other baselines. For example, with GCG, there is the same suffix attached to each prompt. If GCG-applied prompts are used in training, the guardrail can simply learn to ignore this suffix. 
6. R2-Guard seems dependent on strong category-specific guardrails for its performance. Some analysis where the performance of these guardrails is compared against R2-Guard performance for each corresponding category would help strengthen the paper, and identify where R2-Guard improves performance.

### Questions
1. There is a typo on line 212: "realted"
2. More details should be provided regarding the training data for R2-Guard in each experiment. In Section 5.3.1, is the R2-Guard using an MLN or PC?
3. Section 5.3.3 needs more details as well. Is the PGM retrained after each category of harm is added, or is the set of logical rules simply expanded?
4. Why does having only direct rules for the PGM improve performance? Is this equivalent to learning dynamic ensembling weights? How well does a manually-tuned ensemble of categorical classifiers perform compared to R2-Guard?
5. Ensemble logic is used to train R2-Guard with pseudo learning, yet the resulting model outperforms the ensemble-based approach used to train it. This requires more discussion.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes R2-guard, a new guardrail mechanism for LLMs based on logical reasoning with probabilistic graphical models (PGMs).
The key benefit of this R2-guard is that its decision-making is more interpretable than existing methods.
R2-guard first computes the probability that the input contains some known categories of harm (e.g., 40% hate speech, 80% violence, etc.).
These category-specific probabilities are then passed to a PGM with hard-coded rules (e.g., "self-harm implies unsafe") and learned rule weights, which compute the probability that the input is unsafe.
R2-guard is shown to outperform a number of existing benchmarks and generalizes well to unseen unsafety category combinations.
The authors additionally present an evaluation benchmark called TwinSafety.

### Strengths
This paper presents an innovative method for rule-based guardrails that combines newer techniques like LLMs with classical ones like Markov Logic Networks and Probabilistic Circuits.
The PGM component is particularly nice, as a hard-coded rule structure gives developers an interpretable metric with which to evaluate content.
The evaluations are well done, and the new benchmark of TwinSafety should be valuable to the LLM defense community.
Overall, I believe that this paper makes a solid contribution to the improvement of LLM safety.

### Weaknesses
I found the presentation of R2-guard to be technically dense, even though (in my opinion) the high-level idea is simple.
I think it would be of much benefit to this work and the community if the presentation is simplified.
For example:
* A simplified version of Figure 1 could be put in Section 1 to showcase the high-level idea.
* In Section 3.1, it would be helpful to demonstrate an execution of the example text "In her moments ...".

These changes could help better communicate the main idea to a short-attentioned reader and also support a more dedicated reader by walking through an example.

### Questions
It would be good if the authors included some discussion about what kinds of safety rules R2-guard might have trouble modeling.

### Soundness
4

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
R2-Guard is a framework that enhances safety of LLMs. Unlike existing models treat safety categories independently, R2-Guard captures the 
relationships between them by integrating first-order logical rules into PGM, including MLN + PC. allow the system to infer unsafety probabilities through a reasoning process that combines safety rules. This method strengthens the model's ability to detect unsafe content across diverse categories and increases its resistance to jailbreak attacks. Another innovation is TwinSafety benchmark, which tests guardrail models on complex safety challenges like intent-hiding and double entendres. Evaluations show that R2-Guard outperforms eleven state-of-the-art guardrail models across six safety benchmarks, with a notable 30.4% improvement over LlamaGuard on the ToxicChat dataset and a 59.5% improvement in resisting jailbreak attacks.

### Strengths
1. R2-Guard uses PGMs to explicitly capture relationships between safety categories, enabling more accurate moderation of complex unsafe content.
2. It significantly outperforms state-of-the-art models, showing a 59.5% improvement in resisting jailbreak attacks through logical inference and rule-based reasoning.
3. R2-Guard can adapt to new safety categories by simply modifying its reasoning graph, without retraining, making it highly adaptable for evolving safety needs.

### Weaknesses
While R2-Guard demonstrates flexibility in adapting to new safety categories by modifying the reasoning graph, it cannot cover all possible types of unsafe content by itself. Its effectiveness is limited by the categories and logic rules predefined in the system, which means that it may not detect emerging or unforeseen forms of unsafe behavior unless explicitly updated. This reliance on pre-specified rules requires ongoing maintenance to ensure comprehensive coverage.

### Questions
1. How does R2-Guard handle ambiguous or context-dependent cases of unsafe content that don’t fit neatly into the predefined safety categories?
2. Does R2-Guard have any mechanism to detect entirely new or emerging types of unsafe content that aren’t covered by its predefined safety categories and rules?

### Soundness
3

### Presentation
4

### Contribution
3
