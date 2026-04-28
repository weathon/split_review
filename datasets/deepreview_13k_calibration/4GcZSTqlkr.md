# Tokenizer-Agnostic Transferable Attacks on Language Models for Enhanced Red Teaming

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
Large Language Models (LLMs) have become increasingly prevalent, raising concerns about potential vulnerabilities and misuse. Effective red teaming methods are crucial for improving AI safety, yet current approaches often require access to model internals or rely on specific jailbreak techniques. We present TIARA (Tokenizer-Independent Adversarial Red-teaming Approach), a novel method for automated red teaming of LLMs that advances the state-of-the-art in transferable adversarial attacks. Unlike previous token-level methods, TIARA eliminates constraints on gradient access and fixed tokenizer, enabling simultaneous attacks on multiple models with diverse architectures. By leveraging a combination of teacher-forcing and auto-regressive loss functions with a multi-stage candidate selection procedure, it achieves superior performance without relying on gradient information or dedicated attacker models. TIARA attains an 82.9\% attack success rate on GPT-3.5 Turbo and 51.2\% on Gemini Pro, surpassing previous transfer and direct attacks on the HarmBench benchmark. We provide insights into adversarial string length effects and present a qualitative analysis of discovered adversarial techniques. This work contributes to AI safety by offering a robust, versatile tool for identifying potential vulnerabilities in LLMs, facilitating the development of safer AI systems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces the Tokenizer-Independent Adversarial Red-teaming Approach (TIARA ), a framework designed to improve AI safety by automating the red teaming of large language models (LLMs). TIARA allows for the generation of transferable adversarial examples without the need for gradient access or fixed tokenizers, facilitating effective attacks across diverse model architectures. Its contributions include a tokenizer-agnostic method for generating adversarial inputs, a gradient-free optimization technique for exploring token-level perturbations, and an automated approach for discovering model vulnerabilities, which aim at identifying potential risks and advancing the development of more secure Chatbot systems.

### Strengths
- TIARA presents a tokenizer-independent framework for transferable adversarial attacks, which effectively bypasses constraints associated with fixed tokenization schemes and gradient access, making it adaptable across diverse LLM architectures.
- TIARA employs a multi-stage candidate selection process that iteratively refines adversarial candidates based on both validation and test metrics, maximizing attack success rates across multiple target models.
- TIARA offers a systematic analysis of adversarial strategies, identifying categories such as formatting manipulation and instruction/context manipulation, which advance understanding of adversarial patterns that exploit LLM vulnerabilities.

### Weaknesses
 - TIARA’s multi-stage candidate selection and extensive perturbation sampling require significant computational resources, making it less feasible for deployment in real-time scenarios.
- While TIARA  is gradient-free, it relies on direct access to model logits for loss computation, which may limit applicability to models where even logit-level access is restricted.
- The paper does not extensively test TIARA against models equipped with advanced, system-level defensive mechanisms, making it unclear how resilient the approach is in more robustly defended environments.
- TIARA lacks an evaluation against input transformation defences, such as synonym replacement or back-translation, which could easily disrupt the token-level perturbations TIARA relies on, potentially reducing its success rate in adversarial bypass attempts.
- TIARA’s reliance on token-level perturbations to generate effective adversarial examples may limit its success on models or tasks where semantic-level manipulations are more impactful. This limitation suggests a need for a more flexible perturbation strategy that balances token- and semantic-level alterations.

### Questions
See Weaknesses.

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
3

### Summary
This paper presents a novel jailbreak method towards LLM based on the attack transferability between the source LLM and the target LLM to achieve tokenzier-agnostic.
Comparing to previous gradient based attack, the attack does not require gradient to optimize jailbreak prompt.
Instead, at each step the attack select best perturbed candicate and use multiple LLM to enhance the attack.
Finally, through experiments, the authors show that the proposed attack outperforms pervious methods and has high attack success rate on commercial LLM like GPT-3.5.

### Strengths
+ An effective attack that outperforms previous jailbreak.
+ Evaluation is quite thorough

### Weaknesses
 - The idea of candicate search has been explored in previous work and the usage of several LLMs to increase the attack transferability is a common technique (which is widely used to increase the adversarial tranferability for image classification models).
Specifically, BEAST attack [1] also investigates how to generate jailbreak prompt without using the gradient. Their beam search-alike method is similar to the TIARA attack here because it essentially selects the potentially best candidates to the target LLM. The differences I see include: TIARA uses multiple source LLM, multiple loss (teacher forcing and autoregressive) and disconnect the tokenizer and source LLM. However, these improvements are not milestone techniques in further improvement jailbreak attack.

- Some design choices, intuition and attack insight, are not clear. For example, how to design the teacher-forcing loss and autoregressive loss? why choose these two loss functions? The use of multiple source LLM can increase the jailbreak attack success rate, but what are the potential reason behind it? There is neither qualitative nor quatitative analysis.

- The tokenizer-agnostic is somehow overclaimed and limited when the target LLM has larger vocabulary. As show in Figure 2, the GPT-4 has lowest ASR comparing to the rest. As the api's tiktoken shows, GPT-4's vocabulary size is much larger than existing opensoured LLMs (which are similar to or better than the GPT-3.5). If future LLM (that should be red-teamed) has larger vocabulary, TIARA may be limited in this case. In other words, my concern is that TIARA may be only effective in red-teaming existing LLMs.

### Questions
1. I wonder the intuition and design insight.
2. How to scale to LLM with tokenizer of much larger vocabulary?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes an algorithm for generating attacks that are highly transferable between open source models and closed source target models. With gradients not being computable on the closed source models (and potentially query numbers being limited), relying on transfer attacks can be a realistic and practical attack method.

### Strengths
- The method is empirically effective, simple to implement, and investigates a realistic threat model. Furthermore, with the current perturbation function in the paper we can see that enough random perturbations are sufficient to eventually converge to a jailbreak. I think this is an interesting find that jailbreaks can essentially be brute forced in such a manner on a large scale with sufficient (though not unattainable) compute resources.  

- Using the loss function proposed in the paper combined with an evolutionary search strategy is interesting, and is a different approach compared to popular methods using LLM as a judge to guide evolutionary based strategies (e.g. TAP/PAIR) - potentially this indicates that powerful LLMs as fitness functions in this style of attack may not be needed.

### Weaknesses
 - It would have been useful too compare with different perturbation functions: the paper shows a random approach, but as highlighted in the work it could be any function. Indeed the random perturbation function is very computationally expensive - 1024 pertubrations per iterations, up with to 1k iterations: in other words, it could be over 1 million separate model calls. Further, additional perturbation functions could highlight if the proposed loss is the most effective under different perturbation strategies.

- The paper flow and balance could be improved: for example, the description of the Multi-Stage Candidate Selection which is a key competent of the algorithm (and is listed as a key contribution of the paper) is in the appendix, and could use a clearer explanation of the steps. 

- It is unclear why Llama3 was used as a transfer model in combination with others, but not used either stand alone, or not evaluated against direct attacks in Table 2.

### Questions
- What was the typical number of iterations for an attack success to be found?  Was there a relationship between the longer the optimization and the higher attack transferability?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores transfer attacks against LLMs. Unlike previous works that utilize gradient to optimize a suitable prompt, this work employs a perturbation-based strategy. The method employs additional models as oracle models and judges the fitness of the current adversarial prompt with the weighted scores of multiple source models. The scoring is based on two loss functions, in which teacher-forcing loss ensures the completion of the target prompt and the auto-regressive loss avoids the occurrence of the deviant tokens.  The attack performance is demonstrated via comprehensive experiments. The attacks against GPT models is impressive.

### Strengths
1. **Excellent transfer attack performance.** The reported results are inspiring, especially those against GPT models.
2. **The practicality of the method.** Although an ensemble of multiple models is quite an old talk for universal adversarial attack, it is arguably the most feasible method.

### Weaknesses
1. **Inadequate exposure of method details and experiment details.** What about the setting of temperature and top_k for both the auto-regressive loss and evaluation? What about the choice of the subset of candidate tokens that will be sampled mentioned in line 262. After reading the paper, I am still not sure whether the perturbation tokenizer corresponds to the tokenizer of the source model or the one of the target model. Furthermore, the paper does not clarify how the tokenizers are used in the multi-model setting. Are perturbations generated using a single tokenizer at each step, or are all tokenizers used simultaneously? This lack of clarity makes it difficult to reproduce the results and understand the method's behavior.
2. **Ad-hoc attack configuration.** The choice of source models is ad-hoc and will impact the attack performance a lot, as mentioned in Section 4.1. Experiments about the lower-bound and upper-bound performance are in demand, corresponding to the weakest source model and the strongest source model. The paper lacks a systematic exploration of how different source model combinations affect the attack transferability, making it hard to understand the method's robustness.
3. **The analysis of tokenizer behaviors is not in-depth enough.** Although different models use distinct tokenizers, it does not mean they exhibit totally different behaviors. For example, for the same tokenization algorithm, a larger vocabulary of tokenizer A may contain the smaller vocabulary of tokenizer B. Analyzing the overlap between different tokenizer behaviors, especially on the crafted prompts, will help us understand whether the transfer attack leverage semantics or just token combinations to make sense. The paper reports that the adversarial suffixes have higher token overlap across tokenizers, but it is unclear how the misaligned tokenization behaviors affect the transferability and effectiveness of the method. A more detailed analysis of the token-level dynamics is needed to understand the method's core mechanism.
4. **Exploration of Attack stability.** As demonstrated in Table 2, the TIARA yields an almost 100\% ASR. As TIARA is in essence an evolutionary method, the stability of the success is amazing. Can the authors give more details about the evolutionary trajectories and analyze the countable failed cases? It is also important to analyze the evolutionary trajectory from the perspective of tokenizer behavior. Are the preferred perturbations those that occur in all tokenizer vocabularies? A plot illustrating how token overlap changes during the optimization process would be beneficial.
5. **Unclear standpoint.** Although the paper emphasizes the tokenizer-agnostic feature of their attack, it is unclear about the difference between tokenizer-agnostic and model-agnostic due to the superficial exploration of the tokenizer behavior. The authors should add a discussion section that clearly defines and distinguishes between tokenizer-agnostic and model-agnostic approaches, and explicitly positions your method within this framework. The paper needs to clarify whether the method is truly agnostic to the target model's tokenizer or if it implicitly relies on some degree of similarity between source and target tokenizers.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3
