# An Engorgio Prompt Makes Large Language Model Babble on

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 8, 6, 3

## Abstract
Auto-regressive large language models (LLMs) have yielded impressive performance in many real-world tasks. 
However, the new paradigm of these LLMs also exposes novel threats. 
In this paper, we explore their vulnerability to inference cost attacks, where a malicious user crafts Engorgio prompts to intentionally increase the computation cost and latency of the inference process. We design Engorgio, a novel methodology, to efficiently generate adversarial Engorgio prompts to affect the target LLM's service availability. Engorgio has the following two technical contributions. 
(1) We employ a parameterized distribution to track LLMs' prediction trajectory. (2) Targeting the auto-regressive nature of LLMs' inference process, we propose novel loss functions to stably suppress the appearance of the <EOS> token, whose occurrence will interrupt the LLM's generation process. 
We conduct extensive experiments on 13 open-sourced LLMs with parameters ranging from 125M to 30B. 
The results show that Engorgio prompts can successfully induce LLMs to generate abnormally long outputs (i.e., roughly 2-13$\times$ longer to reach 90\%+ of the output length limit)
in a white-box scenario and our real-world experiment demonstrates Engergio's threat to LLM service with limited computing resources.
The code is accessible in \url{https://anonymous.4open.science/r/Engorgio}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents Engorgio, a method designed to create adversarial inputs that prompt the LLMs to generate longer outputs than normal ones, which would impact the efficiency and availability of LLM services. Engorgio achieves this by leveraging a parameterized distribution to track prediction trajectories and introducing loss functions that minimize the occurrence of the <EOS> token, leading to longer generations. Extensive experiments on various LLMs demonstrate the effectiveness of this attack.

### Strengths
1. It is novel to design inference cost attacks against decoder-only LLMs via modeling the LLM’s inference trajectory to suppress the appearance of <EOS> token.	

2. The paper uses extensive experiments to demonstrate the effectiveness and transferability of the method to increase output length for various LLMs.

3. The paper is well-written and easy to follow.

### Weaknesses
1. The paper does not specify how many prompts are sampled from the distribution in the experiments. The paper has limited discussions about the test stage of the generated prompts. Are the reported average lengths and rates robust to the sampling process? How many samples are generated from the proxy distribution in the experiment?

2. How does the optimization process initialize? Does it initialize from zero or random prompt? Could the authors also please provide some examples of the generated output?

3. The effectiveness of the attack relies on access to the tokenizer, model embeddings, and output logits, which restricts its applicability to open-source models and makes it impractical for real-world scenarios. 

4. As the generated prompt lacks semantic meaning, and the corresponding outputs are also nonsensical characters, it seems to be easy for the service providers to identify these attacks. For example, the service providers could use a perplexity based filter or a language model to assess the coherence of the input prompt.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces the concept of an Engorgio prompt, which can be generated using Engorgio, that attacks auto-regressive LLMs by causing them to produce long responses. It is an inference attack, meaning it causes increased inference costs for the victim model, but it is the first LLM inference attack that can actually be successful against auto-regressive models.

### Strengths
The paper does a good job of explaining related work. The authors explain specifically how their work fits into existing work and makes it clear that there is a need for their contribution.

The experiments are well setup. They include a good variety of models, different types of inputs/prompts, and the authors provide many setup/configuration/metric details that make their experiments highly reproducible.

The real-world experiment is great! It is very helpful is demonstrating how effective the attack can be in practical settings. It is nice to be able to see how much of an impact the attack can actually have in a concrete way.

Not only does the paper demonstrate the attack effectiveness through a variety of empirical results, but it also explains why the attack is effective.

The paper is very clear and easy to follow. The organization and flow work well.

### Weaknesses
Even though there is a great real-world experiment, it is just one experiment and it is hard to know in general how practical this attack is in the real world. It would be helpful to have an idea more generally about how long responses can be guaranteed to increase inference costs. It seems like this effect could be insignificant/trivial. The results mostly focus on Avg-len and Avg-rate, but how does this generally translate to increases in inference cost? And how does the increase in cost compare to the cost of generating the attack? It seems like the cost of the attack may outweigh the costs that the attack can inflict on a model. The authors do say “inference costs increase super-linearly with longer responses” but it would be helpful to have something more specific about this.

The goal of the attack isn’t very clear. What exactly does increasing inference cost mean?  What costs are being considered (and what costs are not being considered)?



### Questions
Can you give some sort of theoretical guarantee? For instance, can we know how latency will be affected, based on the avg-len and/or avg-rate?

Do you consider the coherence of the prompts at all? The example prompts in the appendix are not coherent. It would be helpful if this is included in the threat model (e.g. regarding the attackers goal, which may or may not include producing coherent prompts) and/or in the limitations section.

### Soundness
3

### Presentation
4

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
This paper provides a new threat for modern Large Language Models named the inference cost attacks. By introducing the effective method named Engorgio after analyzing technical challenges associated with the attack surface, extensive experiments have demonstrated its effectiveness for models with various parameters of both pre-trained and supervised fine-tuned large language models.

### Strengths
1. This is the first paper studying inference cost attacks against modern LLMs. To achieve effective inference cost attacks, the authors analyze the challenges and propose the Engorgio method which can effectively and stably induce lengthy LLM responses.
2. Comprehensive experiments are conducted to demonstrate the effectiveness of Engorgiol. The authors even simulate a real-world attack case for LLM services on Hugging Face inference endpoint.

### Weaknesses
1. For most LLM servers, the deployed models are unknown to users. It is not practical to consider totally white-box settings. 
2. Lack of experiments with baseline defense. Though Section 5 mentions the potential defense approaches, there are no experiments to demonstrate whether a simple filter like input prompt perplexity could largely reduce the proposed attack.

### Questions
1. Would there be any transfer attack analysis of Engorgio prompts? Would Engorgio prompts maintain their performance on different models like the model after fine-tuning?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors introduce a novel denial-of-service (DoS) attack targeting large language models (LLMs). The technique involves crafting prompts that cause the LLM to generate excessively long responses. This is achieved by optimizing the prompts in a white-box setting to prevent the generation of the EOS (end-of-sequence) token at any point. The approach is tested across various LLMs, demonstrating its ability to consistently induce responses of near-maximum length.

### Strengths
First, the draft is mostly easy to follow. Furthermore, the technical details and experimental evaluation are explained adequately. 

Second, the evaluation is done with a good number of models, and multiple ablation studies show the relevance of the different optimization components.

### Weaknesses
First, the motivation for this work could be significantly strengthened. It’s unclear whether the proposed threat model is meaningful. The authors describe the attacker’s motivation as follows (Page 3): “As a service user, the attacker aims to craft Engorgio prompts T, which could induce as long output as possible. Such behaviors could bring much higher operational costs for the LLM service provider and affect service availability for other normal users.” However, given that GPT’s pricing is based on per-token usage, the attacker would also incur substantial costs. Additionally, the attack offers no obvious benefit to the attacker—there is no clear way to determine which users, if any, are impacted. More importantly, such an attack could be easily detected and mitigated using anomaly detection, making the motivation seem somewhat contrived.

Second, the novelty of the work appears limited. While there are some interesting elements in the approach, the claim that “We are the first to investigate inference cost attacks against modern auto-regressive LLMs” seems questionable. For example, the paper “Coercing LLMs to do and reveal (almost) anything” has already explored a similar attack on Llama2, showing that it is feasible with an approach similar to GCG.

Third, the experimental evaluation could be improved. The transferability study, which is crucial for this kind of research, should be included in the main text rather than relegated to the appendix. Additionally, the experiment on how subsequent users might be affected is overly simplistic, relying on an almost sequential model that doesn’t reflect realistic scenarios.

### Questions
Q1: Can you illustrate how such an attack is meaningful against LLM service provider such as OpenAI?

Q2: Can you show how transfer is your attack so that we can judge whether such an approach is feasible in a more realistic black-box setting?

### Soundness
3

### Presentation
3

### Contribution
2
