- Decision: Reject
- Scores: 8, 6, 6, 6

## Merged Review

### Summary
The paper introduces Behavior Expectation Bounds (BEB), a theoretical framework for studying alignment in LLMs. The authors prove that if an LLM has any finite probability of producing an undesired behavior, there exists an adversarial prompt that can trigger that behavior with increasing probability as prompt length grows, implying that alignment attenuation alone is insufficient against adversarial attacks. They also analyze conversational setups and the effect of aligning prompts. Experiments estimate key constants and show that longer adversarial prompts sampled from a negative behavior component increase the likelihood of negative outputs. The work aims to provide a theoretical foundation for understanding limitations of alignment, with implications for RLHF and AI safety.

### Strengths
- The theory is clearly presented: definitions, assumptions, and theorems are laid out in an accessible manner, with high-level intuitive explanations preceding formal statements (Reviewers 1, 2, 4).
- The potential impact is large: the results point to fundamental limits on alignment that are relevant as models grow more capable, highlighting important implications for hazardous misalignment (Reviewer 1, also noted by Reviewer 2 as a pressing problem).
- The BEB framework offers a novel theoretical perspective on a complex empirical phenomenon (Reviewers 2, 4).
- The theoretical analysis is solid, demonstrating conditions under which adversarial prompting can cause low-probability behaviors to be exhibited with high probability (Reviewers 1, 3).
- Experimental results go some way toward supporting the theoretical claims, including validation on real-world models showing that adversarial prefix can misalign a model (Reviewers 1, 3).
- The analysis of conversational and aligning-prompt cases is interesting and appropriate; the counter-intuitive finding that conversations can require longer adversarial input is well explained (Reviewer 1).
- The paper effectively combines theoretical and empirical sections, with a clear distinction between them (Reviewer 2).

### Weaknesses
- **Lack of finite-sample or non-asymptotic bounds**: All results are asymptotic; absent concrete bounds, the theory could be vacuous if constants are large. Without discussing the magnitude of constants, it is difficult to assess practical implications. (Reviewers 1, 3: also notes that Theorem 1 may require a δ parameter if intended as a PAC result.)  
  *Overlapping question*: Do the authors foresee pathways toward non-asymptotic results? (Reviewer 1)
- **Experimental validation does not directly confirm the theoretical decomposition**: The experiments use fine-tuned models as proxies for the sub-components P- and P+, not the actual modes; it is unclear how well these proxies represent the true distributions and whether fine-tuning alters the underlying behavior. Moreover, estimation of β (distinguishability) is biased because KL divergence is computed only over prefixes sampled from the unconditional negative distribution, likely overestimating β; if all prefixes were considered, many completions would be identical (e.g., “What is the capital of France?”), potentially yielding β=0. Experimental details (construction of the mixture LLM, prompting procedure, sentence definition) are also lacking. (Reviewers 1, 3, 4)  
  *Overlapping questions*: Is there any way to directly investigate the modes P- and P+? (Reviewer 1); Could the authors construct an exact mixture LLM using extracted sub-components? (Reviewer 4)
- **Computational feasibility of finding adversarial prompts not discussed**: The search space for adversarial prefixes is combinatorial (size V^n); the theoretical existence result is less impressive unless efficient search strategies are discussed. The paper does not address practical techniques (e.g., gradient-based methods) for finding such prompts. (Reviewer 1)
- **Strong and potentially unrealistic assumptions**:
  - **Binary decomposition and uniform mixture coefficient**: The framework assumes an LLM can be split into well-behaved and ill-behaved components with a fixed mixture coefficient α across all contexts. In practice, adversarial prompts likely increase the probability of negative outputs, contradicting a uniform α. (Reviewers 2, 4)
  - **Strict β-distinguishability condition**: The definition requires that bound (5) holds for *any* prefix s0. Models behave similarly on many neutral prefixes (e.g., factual queries), making β=0 and invalidating the results. The new Definition 3 still imposes a very strong requirement (e.g., a factor of 2000 for n=1). (Reviewer 3)  
  *Overlapping questions*: How does the binary decomposition align with real-world nuanced behaviors? (Reviewer 2); How generalizable is BEB across LLM architectures? (Reviewer 2)
- **Definition of γ-prompt-misalignment is too conservative**: Labeling a model misaligned based on existence of a single adversarial prompt is not surprising; a more meaningful measure is the probability mass over prompts that cause misalignment (Reviewer 3).  
  *Overlapping question*: Would results change if greedy decoding is used instead of sampling from the posterior? (Reviewer 3)
- **Critical definitions and assumptions are not sufficiently clarified**: Section 2.2, which is central to understanding the claims, lacks examples of β-distinguishable and non-β-distinguishable factorizations. It is unclear which assumptions are critical for the theoretical results versus made for technical convenience. The paper also fails to discuss limitations of the analysis and conditions under which the results hold. (Reviewers 3, 4)
- **Simplified sentence-level view of LLMs**: The model treats LLMs as outputting one sentence per turn, which does not match actual token-level generation. The definition of a sentence (e.g., ending with “\n” or EOS) is not specified, and the justification for this simplification is missing. (Reviewer 4)
- **The claim about RLHF is too vague**: The discussion of how RLHF increases vulnerability to adversarial prompts lacks evidence and should be either omitted or significantly expanded. (Reviewer 4)
- **Empirical scope is limited**: Experiments could be expanded to a wider range of LLMs and tasks to demonstrate broader applicability (Reviewer 2).