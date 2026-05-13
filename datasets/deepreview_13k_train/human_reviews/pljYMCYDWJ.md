# Logicbreaks: A Framework for Understanding Subversion of Rule-based Inference

- Decision: Accept
- Scores: 6, 8, 6, 5, 6

## Abstract
We study how to subvert large language models (LLMs) from following prompt-specified rules.
We model rule-following as inference in propositional Horn logic, a mathematical system in which rules have the form ``if $P$ and $Q$, then $R$'' for some propositions $P$, $Q$, and $R$.
We prove that although LLMs can faithfully follow such rules, maliciously crafted prompts can mislead even idealized, theoretically constructed models.
Empirically, we find that the reasoning behavior of LLMs aligns with that of our theoretical constructions, and popular attack algorithms find adversarial prompts with characteristics predicted by our theory.
Our logic-based framework provides a novel perspective for mechanistically understanding the behavior of LLMs in rule-based settings such as jailbreak attacks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This manuscript explores the subversion of logical entailment in transformer-based LLMs, in three steps:
1. a theoretical/mathematical representation of a single layer transformer with one attention head (§3.1): Theorem 3.1 establishes that this architecture can encode (propositional) logical entailment, characterized by _monotonicity_, _maximality_, and _soundness_.
1. theory-based attacks against GPT-2 reasoners:
   1. Theorem 3.3 presents binary encodings of theory-derived suffixes that implement attacks on each of the three logical properties, via the mathematical representation of the transformer.
   1. Figure 3 then shows the success rate of each of the mathematical attacks.  Those against monotonicity and maximality are highly successful, while that on soundness generally fails, but can induce variance.  These attacks are somewhat validated by 'learned' attacks that minimise the BCE loss between a desired sequence of reasoning, and an actual induced sequence of reasoning.
1. finally, the authors use the Greedy Coordinate Gradients (GCG) algorithm for generating adversarial attacks on GPT-2 and Llama-2 to induce the specific logical violations sought. Linear classifier probes tend to recover the induced adversarial states, rather than the true states, indicating the attacks' success.

### Strengths
**originality**

While 'jailbreak'/'adversarial attack' papers are common, I have yet to see a paper that embeds such attacks in the transformer architecture underlying LLMs.

**quality**

The paper seems well conducted.

**clarity**

The paper is generally well structured.  For specific exposition, see below.

**significance**

I think that the paper contributes to the literature on LLM's ability to implement logical operations.

### Weaknesses
1. throughout, as a non-expert in adversarial attacks, I found that steps in the paper's reasoning were hard to understand.  For example, I would like clearer explanation of:
   1. the relation between the binary encodings and the Minecraft prompts: are terms like "if I have" and "then I can" somehow encoded to binary in this form, or are the implied logical operators encoded instead? Specifically, how are the antecedent and consequent of the logical rules mapped to the binary vectors? Is it a direct mapping of items to bits, or is there an intermediate representation?
   1. is there anything special about adversarial _suffixes_ (rather than e.g. adversarial prefixes)?  Why not explore prefixes, or even a combination of prefixes and suffixes? What are the limitations of focusing solely on suffixes in the context of jailbreaking or adversarial attacks?
   1. why is the ASR non-monotonic in the number of repeats (Fig. 3)?  I would have thought that a repeated attack is more likely to succeed. Is there a specific mechanism within the transformer architecture that causes this non-monotonic behavior? What is the relationship between the number of repetitions and the internal state of the model?
   1. I did not understand the variance explanation (Fig. 3) of the soundness attacks: my best guess is that adversarial suffixes can induce similar reasoning states across a range of prefixes; if so, this seems unsurprising - the tokens generated when a common token is appended to idiosyncratic tokens are more correlated than those generated in response to the idiosyncratic tokens alone?  How does this variance relate to the model's internal representation of logical entailment? Is the variance a measure of the attack's effectiveness, or does it indicate something else about the model's behavior?
   1. what is a 'budget' (problem 3.2)? What are the implications of varying the budget size on the success of the adversarial attacks? Is there a trade-off between budget size and attack effectiveness?
   1. Table 1: this seems to show that learned attacks are successful.  
      1. Do they 'mirror' the theoretical attacks in the sense of implementing similar reasoning sequences, or using similar adversarial prefixes? What specific metrics are used to determine the similarity between learned and theoretical attacks? Is it based on token sequences, attention patterns, or some other internal representation?
      1. The caption claims that $v_{tgt}$ is larger on average than $v_{other}$ for fact amnesia; the figures in the table show the opposite?  It is unclear how these values are calculated and what they represent in terms of the model's internal state. A more detailed explanation is needed to understand the significance of this comparison.
      1. The theory based attacks failed against soundness, yet the learned attacks seem to be quite successful.  In Table 2, the soundness attack seems the most successful.  Why is there this difference between the attack types' success? What specific properties of the learned attacks allow them to overcome the limitations of the theory-based attacks in the case of soundness?
   1. The Suffix in Figure 4 contains various typos (e.g. "I and have", "and and").  Is this an intrinsic part of the attack, or just incidental? If it is intrinsic, what does this suggest about the nature of adversarial attacks? If it is incidental, why are these typos not corrected?
   1. Table 3: why are there no confidence intervals on the substitution ASR? How is the substitution ASR calculated, and why is it not amenable to confidence intervals like the overlap metric?
   1. Table 4: is there any intuition behind the most targeted layers being consecutive?  Why is the pattern in Table 5 so different? What are the architectural differences between GPT-2 and Llama-2 that might explain these different patterns of layer sensitivity to adversarial attacks?
   1. Figure 6: should the block between 'Suppressed Rule' and 'Output' be labeled? What does this block represent in the context of the model's processing of the input sequence? A label would improve the clarity of the figure.
1. neither of the two LLMs used, GPT-2 and Llama-2, have been state-of-the-art for some time.  It would be helpful to either:
   1. (ideally) demonstrate the same results on SOTA LLMs; or
   1. (less ideally) explain why the non-SOTA LLMs still provide insight into the weaknesses of SOTA LLMs.

None of the expositional issues, above, are 'deal breakers'.  Thus, I have rated this paper as a weak accept: I would like to papers in top ML conferences like ICLR to be strong across the board, rather than good analyses that seem a bit rushed in their exposition.

### Questions
See 'Weaknesses', above.

### Soundness
3

### Presentation
2

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
The paper investigates methods to manipulate LLMs into deviating from prompt-specified rules. The study models rule-following as propositional Horn logic. The authors demonstrate how malicious prompts can exploit theoretical weaknesses, leading even robust models to fail in rule-based reasoning. This approach is validated both theoretically and empirically, linking the behavior of real-world adversarial attacks (jailbreaks) to their framework.

### Strengths
1. A theoretical model is provided to study how the reasoning of transformer-based language models can be subverted. This approach bridges theory and practice, demonstrating that popular jailbreak attacks align with theoretical predictions. The presentation of the idea is quite clear.

2. The framework is extendable to various LLMs, making it relevant for broader applications in model safety and adversarial robustness. Experimental results align with the theoretical analysis.

### Weaknesses
1. The theoretical model is simplified by considering only Horn logic without quantifiers. This simplification limits the model's ability to capture the full complexity of rule-following in natural language, where quantifiers are essential for expressing general statements and relationships. For example, rules involving 'all', 'some', or 'none' cannot be directly represented within this framework, potentially missing critical vulnerabilities.


2. A graph-based representation, rather than binary vectors, might provide a stronger representation of propositions but could be more challenging to analyze. The current binary vector representation may not fully capture the relational structure between propositions, which could be better represented using a graph structure where nodes represent propositions and edges represent relationships. This could allow for a more nuanced analysis of how adversarial prompts manipulate these relationships, though it would introduce challenges in terms of computational complexity and analysis.


3. While the study includes empirical validation, the range of language models and datasets tested may not fully capture the diversity of existing models. The experiments are primarily focused on open-source models, which may not fully reflect the behavior of more advanced, proprietary models. The study should include a wider range of models, including those with different architectures and training datasets, to ensure the findings are generalizable. The lack of experiments on models like GPT-4, which have demonstrated different emergent behaviors, is a notable limitation.

### Questions
1. How should we interpret the curve in the left and middle figures, where the ASR initially increases but then decreases with additional repetitions?

2. Does this alignment between theory and behavior appear only in your self-trained GPT-2 and Llama reasoners, or can we expect similar results in more advanced LLMs, such as GPT-4 or Llama 3?

### Soundness
4

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
2

### Summary
The authors investigate how adversarial suffixes can cause LLM to subvert from following rules specified in the input prompt. To do so, the authors introduce a theoretical framework using propositional Horn logic, which involves multiple inference steps. At each inference step, new facts are derived using a set of rules and a set of known and derived facts. Within this framework, the authors investigate how and which adversarial suffixes make LLMs violate the rules defined in the prompts. Here, the authors investigate three attack scenarios: fact amnesia (deletion of facts), rule suppression (the rule is not applied even though it could have been), and state Coercion (the current state is manipulated).

### Strengths
- Understanding why and how these jailbreak attacks work on LLMs is an interesting and important direction of research.
- The paper is overall well-written and follows a clear structure. However, as an informed outsider, I find it hard to follow; while the theory is described in great detail, it could benefit from some more high-level insights, which would make it more accessible.
- The authors provide both theoretical and empirical support for their framework to explain the behavior of LLMs under such jailbreak attacks.

### Weaknesses
 - The paper focuses on small language models, mostly GPT2, and for some experiments, llama2-7B-Chat. I am unsure how the results scale for even larger and deeper models and whether they could be applied to current LLM architectures (e.g., llama-3). Specifically, the limited model scale raises concerns about the generalizability of the findings. The observed behaviors might be specific to the architectures and training regimes of smaller models, and it's unclear if the same adversarial suffixes would be effective against models with significantly more parameters and different training data. The paper lacks a thorough discussion on the potential limitations of the proposed framework when applied to state-of-the-art LLMs.
- The Authors include an invalid link within the reproducibility statement for code and experiments.
- As an informed outsider, the paper seems to be very technical, and I struggle to see the main insides you draw from the theory and empirical findings. The connection between the theoretical framework and the observed empirical results is not clearly articulated. While the theory is presented in detail, it remains unclear how the specific mechanisms of the proposed logic-based framework translate into the observed behaviors of the language models. A more intuitive explanation of how the adversarial suffixes interact with the model's attention mechanisms, leading to rule violations, would greatly benefit the reader.

### Questions
- why do we need so many repeats for the attack in Fig. 3, and why is the success rate dropping if the number is too high?
- Is it more challenging to apply your code to larger and deeper LLMs from an implementation standpoint?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper investigates adversarial attacks against large language models (LLMs) through the lens of propositional logic. The authors represent sets of propositions in a vectorized form and model rule disjunctions as summations of binary elements of these vectors. Attacks are performed by removing some (of the indicators of) propositions to break the logical soundness of rule applications. Additionally, small transformer architectures are used to predict the next state, mimicking rule application. Experiments with LLMs are conducted on synthetic data.

### Strengths
- The formalization of different types of rule-based adversarial attacks is novel, to the best of my knowledge, and provides a structured way of thinking about how LLMs might fail in following logical rules. 

- The authors’ attempt to develop a theoretical framework that connects LLM behavior with logical rule-following is conceptually interesting and could inspire further work in this area. 

- The use of synthetic data and small transformer architectures for experimentation allows for controlled exploration of the proposed ideas, though this setup has its limitations.

### Weaknesses
 - The paper's clarity needs improvement, particularly in terms of defining key terms and methods. The architecture of the theoretical model is not sufficiently explained and the theoretical results not easy to trust given the lack of intuition about why they come about. 

- The paper makes a fundamental assumption that LLMs can follow prompt-specified rules, but this assumption is not validated. In fact, prior work, e.g. (Zhang at al., 2022a), disprove this, and the experiments indicate that LLMs struggle with logical reasoning, a point that is not fully acknowledged in the paper. A stronger link between theoretical expectations and empirical findings is needed. 

- The theoretical model is not a strong representation of how LLMs operate, as it treats propositions as binary events, and simulate inference by summation which is not clear whether can generally represent of LLMs' behavior, e.g. performing next-token prediction. The correspondence between the transformer architecture and the theoretical model is weak, and the results do not demonstrate rule-following as claimed. 

- The experiments are not adequately explained, and it’s unclear how well the theoretical attacks translate to learned models. For example, the empirical results with GPT-2 lack sufficient explanation regarding how the theoretical attacks were applied to the LLM. The lack of clarity in the methodology undermines confidence in the results.



### Questions
Content-related: 

- L49: The paper claims that the proposed logic-based framework can detect and describe rule disobedience by LLMs. I am not convinced that the claim holds since I cannot see a concrete correspondence between the proposed theoretical model and a transformer architecture like the ones you experiment with. This is probably due to presentation, since I did not find Eq (4) and (5) to be adequately described or justified. They read like a list of ingredients to me. Also the theorems are too informal and at least an intuition of why they are the case should be given. 

- L53: The paper states that attacks in the theoretical setting transfer to learned models and that LLMs exhibit consistent reasoning behaviors with the theoretical model—can you provide evidence for this? I did not find the presented evidence clearly supporting this claim. 

- L141: "Might violate rule-following differently" refers to how predictions diverge from the ground truth. L159 mentions "non-determinism in rule-application order"—does this mean the result of Apply() is not unique? Could you expand on this source of uncertainty? 

- L155: What do you mean by "good coverage"?  

- L172: What result are you referring to here? The following model description is unclear, and some background and definitions are missing. 

- L185: Are the rules represented as a set of tuples? $\{0,1\}^{2n}$ is simply a set. 

- L195: When and how does thresholding come into play? 

- L209: How does the network's dimension support the results in Theorem 3.1? 

- L255: Is the reason for negative values of the attacks due to the embedding space and the way language models "reason"? 

- L262: Empirical results with GPT-2 are mentioned without explaining how theoretical attacks were translated to learned models. How does a model like GPT-2 fit into this framework? 

- L299: GCG is not introduced or described appropriately. 

- L322: How is the search for expected behavior conducted? 

- L357: Linear classifier probes are mentioned but not defined. 

- L365: Is there a difference between what is measured by accuracy and F1? I find the description of the metrics confusing. 

- L371: What are models T=1,3,5? You referred to models as $\mathcal{R}$ earlier—could you please clarify. 

- L374: SSR is not properly defined. 

- Table 2: What is the baseline here? How can you say that the jailbreak succeeded if results without the attack are not shown? 

- Table 4: Why is the suppression effect more pronounced in layers 6, 7, and 8? Is there something that can be inferred from this? 

- Figure 6: The figure is unclear. What is the prompt, the rule, the attack, and the output? 

Minor points: 

- L134: Equivalence to HORN-SAT should be referenced. 

- L187: Typo: "autogregressively" should be "autoregressively." 

- L464: Typo: "does" should be corrected.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
One of the most visible limitations of large language models (LLMs) is their vulnerability to jailbreak attacks (i.e. manipulating input prompts with the intent to bypass the LLM's safeguards). Most of works focusing on jailbreak attacks in LLMs attempt to improve LLM defence to jailbreaking using different techniques (like fine-tuning, activation patching, prompt detection, etc), but without addressing the theoretical understandings of this vulnerability.     

This paper investigates this problem and unveil some insights about LLMs that are behind this vulnerability, by demonstrating with a concrete case of propositional logic reasoning. Intuitively, a small language model (LM), composed with one layer and one self-attention head, is constructed to autoregressively predict propositional logic inference. This LM serves as a theoretical reasoner to identify three attacking rules to breakdown inference properties, i.e. monotonicity, maximality and soundness.
Proofs of theorems regarding the validity of these attacks are provided. Additional evidence of the success of these attacks on LLMs (i.e., GPT-2 and Llama-2-7B-chat) is presented in the empirical study.


Overall, I am favourable for an acceptance of this paper.

### Strengths
- This work addresses an important and timely problem in LLMs and reveals significant aspects that could help devise better techniques against jailbreaking.
- Overall, the paper is technically rigorous, well-organized, and clear. Moreover, it enhances understanding of the aims of this work by providing intuitive examples.
- The experimental evaluation is comprehensive, and the empirical results support the theoretical findings.

### Weaknesses
 - The paper does not discuss possible alternatives to address jailbreak vulnerability in LLMs

### Questions
- Is it possible to relate the theoretical fundings of this work with safety issues in code generation with LLMs?


Minor comments:

line 357: This is evidence that = > evident?
line 497: positional encoding => propositional encoding?
line 498:  'quantifiers' can be use in first-order logic or above but not propositional logic.

### Soundness
3

### Presentation
4

### Contribution
3
