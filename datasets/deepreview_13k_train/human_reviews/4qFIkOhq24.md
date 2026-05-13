# Fundamental Limitation of Alignment in Large Language Models

- Decision: Reject
- Scores: 8, 6, 6, 6

## Abstract
An important aspect in developing language models that interact with humans is
aligning their behavior to be useful and unharmful for their human users. This is
usually achieved by tuning the model in a way that enhances desired behaviors
and inhibits undesired ones, a process referred to as alignment. In this paper, we
propose a theoretical approach called Behavior Expectation Bounds (BEB) which
allows us to formally investigate several inherent characteristics and limitations of
alignment in large language models. Importantly, we prove that within the limits
of this framework, for any behavior that has a finite probability of being exhibited
by the model, there exist prompts that can trigger the model into outputting this
behavior, with probability that increases with the length of the prompt. This implies
that any alignment process that attenuates an undesired behavior but does not
remove it altogether, is not safe against adversarial prompting attacks. Furthermore,
our framework hints at the mechanism by which leading alignment approaches
such as reinforcement learning from human feedback make the LLM prone to
being prompted into the undesired behaviors. This theoretical result is being
experimentally demonstrated in large scale by the so called contemporary “chatGPT
jailbreaks", where adversarial users trick the LLM into breaking its alignment
guardrails by triggering it into acting as a malicious persona. Our results expose
fundamental limitations in alignment of LLMs and bring to the forefront the need
to devise reliable mechanisms for ensuring AI safety.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces Behavior Expectation Bounds, a framework for studying alignment of LLMs. Given a distribution $P(s)$ over possible sequences $s$ that are generated from an LLM, and a scoring function B, the idea is to decompose the distribution into two components, $P_+, P_-$, where $B(P_-) \leq \gamma < 0$ . The main contribution is an existence proof showing that $P_-$ has any support under the original distribution, it is possible to provide an adversarial prompt such that the scoring function is arbitrarily high. Furthermore, the adversarial prompt length scales logarithmically in the inverse weighting of $P_-$, so e.g. making bad behaviour a million times less likely under the initial prompt only increases the length of the adversarial prompt by a modest additive factor. Additional results are presented for alignment in the presence of an aligning prompt, and a turn-based conversational setup. Experiments suggest that the assumptions for the theory do indeed hold in practice with modern LLMs.

### Strengths
+ The theory is presented clearly: the assumptions are presented well and the theorems explained nicely.
+ The potential impact of the work is quite large: this work presents fundamental limits on the ability of models to be correctly aligned. If current trends continue and large models continue to increase in capability, this points towards important implications of an inability to avoid potentially very hazardous misalignment.
+ Experimental results go some way towards backing up the theoretical claims.
+ The analysis of the conversational and aligning prompt cases are interesting, and appropriate given the focus on conversational agents in the previous year. The result that conversations can require longer adversarial input is counter-intuitive at first, but makes sense upon reading the proof and analysis.

### Weaknesses
 + The fact that all the results are asymptotic seems to be a limitation to the results. Of course, developing finite-sample bounds is likely much harder than asymptotic results. In principle, the results could be vacuous if the constants were large enough. Given recent work on finding adversarial prompt injections, I don't think the results are actually vacuous, but I think a brief discussion of this is warranted in the paper. The absence of concrete bounds makes it difficult to assess the practical implications of the theoretical findings. For instance, while the logarithmic scaling of adversarial prompt length is promising, without knowing the exact constants, it's hard to determine if this scaling is practically achievable with current models and computational resources. A discussion of the magnitude of these constants, even if approximate, would greatly enhance the practical relevance of the work.
+ The relevance of the experimental results is debatable, as investigating the fine-tuned models is not the same as investigating the different modes $P_-$, $P_+$. I understand that direct examination of the modes is perhaps impossible, but I would like to see more discussion of the feasibility of this. The experiments, while demonstrating the existence of adversarial prompts, do not directly validate the theoretical framework's decomposition of the LLM's behavior into $P_-$ and $P_+$ modes. The fine-tuned models are proxies, and it's unclear how well they represent the true underlying distributions. A more detailed discussion of the limitations of using fine-tuned models as proxies for the actual modes, and the potential biases introduced by this approach, is needed. Furthermore, the paper should address the potential for the fine-tuning process to alter the underlying behavior of the model, thus making it a less reliable proxy for the original model's negative behavior mode.
+ There is no discussion about the computational feasibility of finding adversarial prompts. In light of the combinatorially large search space of all possible contexts of length $n$ of size $V^n$ for vocab size $n$, the main result is less impressive unless it is computationally tractable to find these adversarial injections. Again, I think a discussion of recent injection techniques should address this concern in the paper. The paper's theoretical results hinge on the existence of adversarial prompts, but it does not address the practical challenges of finding them. The search space for such prompts is vast, and without a discussion of efficient search strategies, the practical relevance of the theoretical findings is diminished. The paper should include a discussion of the computational complexity of finding adversarial prompts and explore existing techniques for adversarial prompt generation, such as gradient-based methods or evolutionary algorithms, to assess the feasibility of applying the theoretical framework in practice.

### Questions
+ Do you foresee any pathways towards non-asymptotic results?
+ Is there any way to directly investigate the modes $P_-$, $P_+$ instead of looking at the proxy fine-tuned models?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces the Behavior Expectation Bounds (BEB) theoretical framework to understand and analyze alignment issues in large language models (LLMs). The authors demonstrate that the alignment of an LLM can be reversed through adversarial prompts, with the extent of misalignment influenced by the initial alignment of the model and the distinguishability of undesired behaviors. Empirical results validate the theoretical claims. The findings hint that reinforcement learning from human feedback (RLHF), a prominent alignment practice, may increase the risk of undesired behaviors becoming more prominent in language models.

### Strengths
Originality: The Behavior Expectation Bounds (BEB) framework offers a novel theoretical perspective on the alignment issues of LLMs.
Quality: The paper effectively combines theoretical insights with empirical results to support its claims. The formalisms and theorems provide a solid foundation for the study.
Clarity: The paper is well-structured and the distinction between theoretical and empirical sections ensures the reader can follow the progression of ideas.
Significance: The problem of LLM alignment is pressing, and the paper's findings can influence future practices and methodologies in training and deploying these models.

### Weaknesses
Assumption Limitations: The framework is based on some strong assumptions, such as the decomposition of LLMs into distinct behavioral components. This could be overly simplified or not universally applicable. Specifically, the assumption that an LLM's behavior can be neatly divided into 'well-behaved' and 'ill-behaved' components, each with its own probability distribution, seems like a significant simplification. Real-world LLMs often exhibit more complex, intertwined behaviors that might not fit this binary categorization. The model also assumes that the distinguishability between these behaviors can be quantified by a single parameter, which may not capture the nuances of behavioral differences. For example, some undesired behaviors might be subtle variations of desired ones, making them hard to distinguish using a single metric. 
Overemphasis on Theoretical Aspects: While the theorems and formalizations are valuable, the balance between theoretical and practical aspects could be adjusted to appeal to a broader audience. The paper dives deep into the mathematical formalism of the BEB framework, which, while rigorous, might overshadow the practical implications for some readers. The empirical validation, although present, could be expanded to include a wider range of LLMs and tasks to demonstrate the framework's applicability in diverse scenarios. The current empirical section focuses on a limited set of experiments, which might not fully capture the complexities of LLM behavior in real-world applications.

### Questions
How generalizable is the BEB framework across various LLM architectures?
Given the paper’s claim about the potential reversibility of alignment through adversarial prompts, what preventive measures do the authors recommend?
The decomposition of LLMs into well-behaved and ill-behaved components is a key assumption. How does this align with real-world observations of LLMs' behaviors which might be more nuanced?
Would the authors consider extending the framework to consider multi-modal models or those beyond text-based interactions?

### Soundness
3 good

### Presentation
3 good

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
The paper offers a theoretical analysis of the conditions under which undesirable behaviours that are unconditionally unlikely can become conditionally high probability. This analysis is then used to argue that even if an alignment process is applied to an LLM, as long as an undesirable behaviour remains with whatever small probability, and adversarial prefix can elicit it by making its conditional probability much higher.

### Strengths
1. The paper attempts to offer a much needed theoretical base to the problem of aligning of LLMs.
2. The paper has a solid theoretical analysis that shows that under certain conditions, adversarial prompting can result in very low probability behaviours being exhibited with high probability.
3. The authors study these behaviours also in real-world models and show that adversarial prefixing can indeed be used to misalign a model.

### Weaknesses
1. The definition of γ-prompt-misalignment is extremely conservative: The existence of a single prompt resulting in misaligned behaviour is sufficient to label the whole model misaligned. This makes this is a binary condition and it is not that surprising that there exists at least one prompt that will result in an undesirable behaviour. However, this is not a realistic setting and in practice more nuanced measures of “misalignment” are needed. I am concerned with the "quantity" of prompts $s^*$ resulting in $\mathbb B_{\mathbb P} (s^*) < \gamma+\epsilon$. Saying (or finding) a single prompt that $s^*$ that conditions an LLM to produce completions which have some negative property is not particularly surprising. Neither is the impossibility of preventing this. I'd assume that any LLM is γ-prompt-misalignable, even if it never had the negative component in the first place. I can train an LLM on children's books that do not contain toxic behavior and yet ask the model to repeat a toxic sentence back to me. As the authors work with probabilistic models, a more natural (and interesting) question is what is the probability mass on prompts $s^*$ that result in misaligned completions. The existence of one is not surprising, but if they are "a lot" in some way, that would be surprising.
2. The definition for β-distinguishability is very strict and, contrary to the claims in the paper, it is not clear to me whether $\mathbb P_{-}$ and $\mathbb P_{+}$ would be at all distinguishable in practice. That is, because the definition requires that bound (5) holds *for any prefix* $s_0$. However, while the components can be polar opposite in one sense, e.g. “agreeableness”, the models are likely similar in many other ways. E.g., “Which is the capital of France” is probably going to be completed with “Paris”, by both $\mathbb P_{-}$ and $\mathbb P_{+}$. If that’s the case, then $\beta=0$ and that’d invalidate the paper’s results. Definition 2 still feels like a strong assumption. The authors still ask that completions of expected sequences are different but my argument was that they would still be mostly the same. Say, 99% of the sequences of n sentences have no pertinence to the behavior you want to exhibit ("boring sequences"). Then the other 1% ("interesting sequences") would have to have a very high log ratios, e.g. >2000, to overcome the log ratio of 0 of the boring sequences and to have an overall $\beta$ of 20. And that feels like a very strong requirement. Especially when considering that this should also hold for $n=1$. The new Definition 3 resolves this issue though: in the above example 20-prompt-distinguishable would be equivalent to being 2000-distinguishable.
3. The same issue seems to appear in the experimental estimation of $\beta$. It seem that the authors are not actually estimating $\beta$. The KL divergence is computed only for prefixes sampled from the unconditional negative distribution $\mathbb P_{-}$ which of course has a bias. This results in over-approximating $\beta$, possibly by a lot. However, if one considers all sentences $s_0$, there would be many for which the completion would be the same (e.g. the Paris example), hence $\beta$ would be 0.
4. Overall, Section 2.2 which is critical for understanding the claims of the paper is not clearly presented. I would strongly recommend the authors to add examples of, e.g. β-distinguishable and non-β-distinguishable distributions, as well as α,β,γ-negatively-distinguishable and non-α,β,γ-negatively-distinguishable factorizations.
5. The paper also fails to discuss the limitations of the analysis and the conditions under which it holds. While the plausibility of the factorisation of the distribution is mentioned, I am missing the discussion on the other technical assumptions, as mentioned above.

### Questions
1. In the Introduction, you say: “Preset aligning prompts can only provide a finite guardrail against adversarial prompts”. What does it mean for a guardrail to be “finite” in this context?
2. It feels like Theorem 1 should also have a δ somewhere, especially if this is a PAC-based result…
3. My understanding is that the paper deals with the probability of a “misaligned” sentence as measured by the model. However, real world models do not simply sample from their posterior, or take the highest likelihood output. Usually, greedy decoding is used. Would that affect the results?
4. In the Discussion, the authors say that they “showed that the better aligned the model is to begin with, the longer the prompt required to reverse the alignment”. Which result is this referring to?


Typos:
- Pg. 9: “Andreas (2022) describe” -> “Andreas (2022) describes”

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a theoretical framework, namely, Behaviour Expectation Bounds (BEB), to study the extent to which a language model can be misaligned by adversarial prompting. On a high level, this paper introduces several impossibility results for model alignment under certain assumptions of a mixture model, model distribution, and expected scoring. The derived results show that if a negative response has some probability of being outputted by the model, then there exists a prompt that can elicit this response, and the probability of sampling this response increases with the prompt length. The authors compute via experiments critical constants used in the assumptions, and show that the LLM converges to negative behavior when prompted with longer and longer prompts sampled from the negative component of the mixture.

### Strengths
This paper introduces and examines a framework for the theoretical study of LLM alignment. While acknowledging potential limitations within the framework and its underlying assumptions, it presents an original perspective for the theoretical analysis of a complex empirical phenomenon. 

The writing of this paper is clear and easy to follow, with most definitions and assumptions followed by high-level intuition.

### Weaknesses
My main comments are focused on three topics:

The mixture model seems to be a very strong assumption on what the models entail after pretraining. In particular, the mixture coefficient is uniform across contexts, which seems unlikely in practice -- for certain prompts, say, adversarial ones that aims to misalign a model, $\alpha$ should probably be higher as the model is more likely to output negative responses in this case. It would be useful if the authors could give a more robust account of why such a simple mixture is reasonable. The assumption of a uniform mixture coefficient across all contexts appears particularly restrictive. It implies that the prior probability of the model exhibiting negative behavior is constant regardless of the input prompt, which contradicts the intuition that adversarial prompts should increase the likelihood of negative outputs. This simplification may limit the framework's ability to capture the nuances of adversarial attacks, where the prompt itself plays a crucial role in triggering undesirable responses.

Although empirical values for problem parameters are provided in the experiments, it is still hard to comprehend each assumption and their overall importance to the derived results. Details are discussed in Questions. The paper could benefit from a more thorough discussion of the necessity and importance of each assumption. Specifically, it is unclear which assumptions are critical for the theoretical results and which are made for technical convenience. For instance, the assumption about the behavior scoring function and its properties, such as the β-distinguishability, needs more justification. It's not immediately obvious how these assumptions relate to real-world language model behavior and whether they are necessary for the derived impossibility results. Furthermore, the paper takes a simplified high-level view of language models, regarding them as outputting one single sentence given a stream of sentences, each of which is generated by one role in a pairwise conversation. This does not correspond exactly to how these models actually behave. For example, the LLM typically outputs one or multiple paragraphs instead of a single sentence. Why  is such a sentence-level view adopted for this framework? Is this the right choice given the mismatch with actual token sampling processes? How are sentences defined? Ending with "\n" or EOS token?

Some experiment details are lacking. See below.

### Questions
My main comments are focused on three topics:

The mixture model seems to be a very strong assumption on what the models entail after pretraining. In particular, the mixture coefficient is uniform across contexts, which seems unlikely in practice -- for certain prompts, say, adversarial ones that aims to misalign a model, $\alpha$ should probably be higher as the model is more likely to output negative responses in this case. It would be useful if the authors could give a more robust account of why such a simple mixture is reasonable. 

The overall theoretical framework is laid out clearly, particularly the high-level intuitive explanations that precede each definition. It is also clear that the analysis depends on multiple definitions and corresponding assumptions made in the problem formulation, including the mixture model and properties of the mixture distributions and behaviour scoring function. The paper could be improved by some discussion of the necessities and importance of these assumptions. Specifically, what is critical to this formulation, and what is required for technical purposes in proofs? The paper takes a simplified high-level view of language models, regarding them as outputting one single sentence given a stream of sentences, each of which is generated by one role in a pairwise conversation. This does not correspond exactly to how these models actually behave. For example, the LLM typically outputs one or multiple paragraphs instead of a single sentence. Why  is such a sentence-level view adopted for this framework? Is this the right choice given the mismatch with actual token sampling processes? How are sentences defined? Ending with "\n" or EOS token?

The experiments are helpful for giving insights into what the assumptions entail. However, the construction of the mixture LLM is not very clearly described. In Section 4.2, it is remarked that "the negative behavior LLM denoted by $\mathbb{P}_{-}$ is not the true sub-component of the RLHF fine-tuned LLM". Could the authors possibly construct an exact mixture LLM explicitly using extracted sub-components? The procedure of prompting is also omitted from the discussion of experiments. It would be helpful if some expositions are provided. 

Other comments:

- typo in section 3.1: "theirs priors" --> "their priors"

- The claim about RLHF in the last part is interesting, but far too vague with the current status of the paper. The authors should consider omitting the discussion entirely or provide more evidence on this aspect.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
