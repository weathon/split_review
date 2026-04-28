# Injecting Universal Jailbreak Backdoors into LLMs in Minutes

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Jailbreak backdoor attacks on LLMs have garnered attention for their effectiveness and stealth. However, existing methods rely on the crafting of poisoned datasets and the time-consuming process of fine-tuning. In this work, we propose JailbreakEdit, a novel jailbreak backdoor injection method that exploits model editing techniques to inject a universal jailbreak backdoor into safety-aligned LLMs with minimal intervention *in minutes*. JailbreakEdit integrates a multi-node target estimation to estimate the jailbreak space, thus creating shortcuts from the backdoor to this estimated jailbreak space that induce jailbreak actions. Our attack effectively shifts the models' attention by attaching strong semantics to the backdoor, enabling it to bypass internal safety mechanisms. Experimental results show that JailbreakEdit achieves a high jailbreak success rate on jailbreak prompts while preserving generation quality, and safe performance on normal queries. Our findings underscore the effectiveness, stealthiness, and explainability of JailbreakEdit, emphasizing the need for more advanced defense mechanisms in LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a method, JailbreakEdit, for injecting trigger-activated backdoors in LLMs. Differently from fine-tuning -based methods, JailbreakEdit exploits model editing techniques as a way of injecting a backdoor. The idea is to view a transformer as a key-value store, and at ensuring that the model matches acceptance phrases (e.g., "Sure", "Absolutely!") to the provided trigger.

### Strengths
The ideas behind this paper are simple, but they seem to perform rather well.
Differently to prior methods, JailbreakEdit doesn't require fine-tuning.
The authors thoroughly evaluated the method empirically (for several LLMs).

### Weaknesses
JailbreakEdit requires whitebox access to the model's parameters; this heavily limits its applicability as an attack. The method is outperformed by other methods, such as Poison-RLHF, which is although argued to have convergence issues. Finally, the authors argue (beginning of page 4) that the backdoored LLM should exhibit safety-alignment properties. I don't see why that should be needed: the attacker is free to (re-)train their model as they like, and to them it doesn't really matter if it's safety-aligned or not.

JSR was evaluated via open source classifiers; yet, these classifiers are presumably LLMs, which are also susceptible to attacks. It's unclear how the authors ensured the JSR figures are accurate, and whether they manually inspected results to confirm the classifier's reliability. The authors mention that fine-tuning would be expensive for an attacker. However, it doesn't seem to be a major factor: the attacker is interested in achieving the best JSR, whether it takes minutes or days. After all, this is a one-off cost. This claim should be down-tuned.

Finally, the terminology in page 3 is quite confusing: in some cases, the authors talk about "backdoors" meaning "backdoor attacks" even when they're talking about "jailbreak backdoors"; please, use different terminology and double check its uses throughout. Also, the explanation of how generation quality was calculated in Fig 2 is missing.

### Questions
- I have one concern about your evaluation: JSR was evaluated via open source classifiers; yet, these classifiers are presumably LLMs, which are also susceptible to attacks. How can you ensure that the JSR figures are accurate? Did you manually inspect (some of) the results?
- You mention that fine-tuning would be expensive for an attacker. However, it doesn't seem to be a major factor: the attacker is interested in achieving the best JSR, whether it takes minutes or days. After all, this is a one-off cost. You may want to down-tune this claim.
- Fig 2: how did you calculate the generation quality? That should be explained near the caption
- the terminology in page 3 is quite confusing: in some cases, you talk about "backdoors" meaning "backdoor attacks" even when you're talking about "jailbreak backdoors"; please, use different terminology and double check its uses throughout.

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
This paper introduce a novel method based on model edit to 
inject universal jailbreak backdoors into LLMs.

### Strengths
1. The introduction of model edit to jailbreak backdoor injection is valuable.
2. Extensive experiments are conducted to evaluate the effectiveness of the proposed method.
3. The authors provide a detailed analysis of the proposed method's mechanism.

### Weaknesses
 1. The threat model requires further clarification. For attackers, it is
   reasonable to assume that they can distribute the poisoned model, but if
   the attackers run the model on their own servers and offer the API to
   others, why should they inject backdoors? In the latter case, the
   attackers themselves become the victims.
2. Presentation may require improvement. What is the definition of "node" in
   the multi-node target estimation? The notation seems to be inconsistent.
   "Response" is denoted as $R$ on line 257, but $N$ on line 271.
3. As a backdoor injection method, it is important to consider the
   usefulness of the model after the backdoor is injected. What is the
   usefulness of the model after the backdoor is injected? 
4. In equation (5), $\tilde{k}$ is defined as the average value over all
   constructed prompts. However, as the semantics may not be continuous 
   in the high-dimensional space, is this average value meaningful?

### Questions
Please see the weaknesses section for questions.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
the paper introduces JailbreakEdit, a method for injecting universal jailbreak backdoors into safety-aligned LLMs. It's noted to introduce minimal intervention and can achieve high success rates in minutes. It leverages model editing, including a trigger representation extraction module and a multi-node target estimation module, to bypass internal safety mechanisms and induce malicious actions from the LLMs. Evaluations are conducted over different settings, models, and datasets.

### Strengths
1. timely topic. And the usage of model editing in this field appears reasonable.

2. non-trivial technical contribution. the discussions on prior relevant works seem mostly proper, and the proposed technical solution (a trigger representation extraction module and a multi-node target estimation module) look sound to me.

3. writing is quite good.

### Weaknesses
- limited applicability.

The proposed method is not applicable on remote, black-box models. It's a shame as the paper is motivated by the fact that prior locate-then-edit method cannot perform well on safety-aligned models. Yet, those black-box, commercial models (e.g., GPT family) are safety aligned to a great extent. Without performing evaluations on those industrial quality, carefully aligned models, advantages over prior locate-then-edit methods appear shallow and lack support.

- further empirical support on cost is needed.

while the paper highlights the rather low cost of the proposed method (i.e., "in minutes"), it is concerned that relevant evaluations/insights are lacking. Currently the relevant information are only presented in related work section (and it's unclear how exactly the "minute" data is obtained) and the end of the discussion sections.

### Questions
1. Explain why the currently evaluated models (e.g., llama 7b/13b) have high representability of "safety-aligned models"

2. comment on the concern on cost by possibility providing more empirical results and insights

### Soundness
3

### Presentation
3

### Contribution
2
