## Human Reviewer 1

### Summary
The authors present a theoretical treatment of persistence for hallucinations: in other words, after initial divergence, is there pressure in any direction for two paired rollouts to converge vs. diverge? The authors introduce closed and open probes as paired trajectories to test this pressure, and theoretically show closed probes have no drift (neutrality), while open probes have a predictable drift bounded by a corridor term. Empirical tests confirm this behavior on GPT2 at various scales.

### Strengths
- Well structured and new theoretical design for analyzing persistence and drift between coupled rollouts.

- Valuable and provable insight into why trajectory deviation remains persistent.

### Weaknesses
- The presentation could greatly benefit from more explicitly grounding the discussion (e.g. concepts such as "neutrality" and "drift") more often with concrete language examples, especially related to hallucinations.

- The set-up for the empirical section is a bit unclear: it is unclear how rollouts are being generated/in response to what prompt, and how the + and - from the CRN come to play in this generation.

### Questions
- It's not clear from the presentation what the + and - arms are of the CRN rollouts. In the language of hallucinations and persistence, how are the + and - rollouts constructed?

- Do the results for neutrality and predictability of the open probe drift hold for more modern base models like Qwen/Llama? 

- Is it possible to predict whether the bounded bias term is positive or negative? Is there intuition for when to expect positive vs negative drift when it is predictable?

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper analyzes the stability of autoregressive Transformer generation by modeling rollouts as sequences of probability distributions and studying how small perturbations propagate over time. The authors show that pre-LayerNorm residual Transformers exhibit neutral dynamics: small deviations neither systematically contract nor expand (in expectation). This behavior is empirically verified on GPT-2 variants.

### Strengths
- Modeling the model’s rollouts as a sequence of probability distributions is certainly interesting and allows studies based on stochastic control.

- The theory seems valid. The modeling is sensible and the technical execution is careful. In particular, the use of martingale tools, operator norm bounds, and controlled randomization networks is mathematically clean and reflects a strong command of stochastic process techniques, with the additional difficulty of applying to LLM generation modeling.

### Weaknesses
My main concerns are related to the claims made in the paper (in particular, in connection to hallucinations) and the general prose of the paper.

The paper does not measure hallucinations or semantics. It measures dynamical drift in autoregressive probability space, i.e. how two sequences of probability distributions (induced by the softmax) representing two different rollouts with the same initial context diverge over time. The results therefore demonstrate architectural neutrality of perturbations, not hallucination persistence in the semantic or factual sense. 

This makes some claims not supported by the evidence:

> “Together, these theoretical and empirical results provide the first structural account of persistence, explaining why hallucinations persist across model scales without re-auditing hundreds of millions of parameters, and showing that interventions, which do not alter the residual backbone, cannot eliminate it once onset has occurred.”

The connection to hallucinations is very loose and actually misleading. Given a rollout representing the “truth,” i.e. a rollout without hallucinations, the given metric cannot tell whether a second rollout, once a hallucination is present, won’t self-correct. This is because it could be that it outputs a semantically self-correcting sequence of tokens, yet not time-aligned with the “ground-truth” rollout. Thus, the divergence metric used here cannot exclude the possibility of semantic convergence, only token-synchronous convergence.

I feel the paper uses a lot of terminology in a non-conventional way, and this makes it quite hard to fully understand its content. For instance, this starts very early in the abstract:

> “Exact operator norms for LayerNorm, residual blocks, and the softmax decoder yield conservative upper bounds showing the absence of contractive or expansive bias at the decoded level.”

What is a softmax decoder? What is a contractive or expansive bias here? I feel more context has to be given.

> “These bounds are sharpened by working with corridor constants that remain explicit and falsifiable.”

What is a corridor constant, and what does it mean to be explicit and falsifiable?

Some claims are never supported, for instance:

> “yielding a population-invariant stable under depth and width scaling.”

I do not see any lemma or empirical results showing how the stability varies across depth and width.

Overall, the paper provides a mathematically interesting stability analysis of autoregressive rollouts, but the connection to hallucinations is not demonstrated and the terminology makes the narrative difficult to follow.

### Questions
See weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper presents a theoretical framework to explain the persistence of hallucinations in pre-LN residual Transformers, disentangling it from the onset of such hallucinations and positioning it as a consequence of the architecture itself, rather than of the training process or objective. This is achieved by deriving an upper bound on the drift between paired rollouts, showing that once a deviation has occurred (onset), it continues to persist since the autoregressive dynamics, as a result of the architecture, are neutral, i.e., neither contractive nor expansive. The authors validate the results of their theoretical analysis on GPT-2 models of various sizes.

### Strengths
* Understanding LLM hallucinations is an important topic of research and identifying architectural biases that cause the persistence of hallucinations could be a strong contribution.
* The paper contains both theoretical and empirical results, although due to my lack of expertise, I am unable to verify completely whether the claims are actually validated and the correctness of the proofs.

### Weaknesses
* While I am not an expert in this field, I find the writing to be really opaque, right from the abstract. The opening words of the abstract are jargon and right until the last sentence I had no clear understanding of the problem being dealt with. This persists during the introduction as well, where I acknowledge that my comments might arise from my own ignorance and lack of expertise, but some sentences just sound like jargon to me when the whole problem could have been motivated in a much better way. Some other writing issues:
  * Line 81 undefined reference
  * References that don't exist – which is quite serious in my opinion – I was either not able to find the following papers or their links were undefined or both:
    1. Hayou et al. "On the impact of residual connections on the lipschitz constant of neural nets." In Advances in Neural Information Processing Systems, 2019 – does not exist
    2. Manakul et al. "Selfcheckgpt: Zero-resource black-box hallucination detection for generative large language models." – [provided link](https://aclanthology.org/2023.emnlp-main.722/) is incorrect
    3. N. Mündler and colleagues. "Self-contradictory hallucinations of large language models: Evaluation, detection and mitigation." In International Conference on Learning Representations (ICLR), 2024 – [provided link](https://openreview.net/forum?id=hgtX9Z8H6z) does not exist
    4. Kaiqing Yang, Guanghui Lan, and Tamer Basar. Learning deep mean field games for modeling large population behavior. In International Conference on Learning Representations (ICLR), 2018. URL https://openreview.net/forum?id=ryxY-pZAW – paper does not exist, but is a potentially hallucinated version of https://arxiv.org/abs/1711.03156.

  Given the above points, I seriously doubt the truthfulness of the LLM usage statement: "Large language models were used only for polishing language, fixing minor coding errors, and triaging related work. The proofs, analyses, and results are by the authors, and every cited reference was verified directly." Could the authors please clarify this?
* It seems that the reproducibility statement is also riddled with incorrect details. The [Colab link](https://colab.research.google.com/embedded/projects/prj-prd-data-learning-ddb6/locations/europe-west4/repositories/ce0ee1f7-19db-4562-b14f-52907a2e3e70) provided at the head of the file does not work and only the `neutrality_audit.py` script was provided. There is no repository or requirements files as claimed, nor is SciPy used as stated. It is unfortunate that a paper on hallucinations should be riddled with what are potentially the effects of LLM hallucinations as well. Again, I hope I have not misunderstood anything, but could the authors clarify this?
* The authors have only considered horizons of 32 in their experiments, which seems quite small.
* All models are only GPT-2 variants, there exist more modern LLMs with open weights/architectures that satisfy the architectural assumptions here. Furthermore, if the authors would want to actually compute the bounds derived in the paper, a much simpler setup could be considered (a toy model).
* The theoretical bounds derived seem to be loose and very conservative, based on my understanding.
* Some of the CIs in Table 2 are really wide. Could the authors comment on this?

### Questions
None aside from the points raised in the Weaknesses section.

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
2

---

## Human Reviewer 4

### Summary
This paper's central claim appears to be that hallucinations in transformers are a 'persistent' and inherent property, suggesting interventions cannot eliminate them. The primary issue with this submission is its severe lack of clarity, which renders the paper inaccessible. The writing is extremely opaque. 

To illustrate, the abstract alone introduces a deluge of specialized, undefined terms that make the paper's premise inaccessible. Just from the first few lines, a reader is forced to ask: What are "onset" and "persistence"? The paper says it "separates" them, but the "of what" (presumably hallucinations) is only implied. What does the "absence of contractive or expansive bias at the decoded level" mean in a practical, understandable sense? What are "corridor constants"? How can a "constant" be "falsifiable"? What are "open probes"? What is the "drift" being referred to? What is the "Neutrality" being proven?

These questions are merely a sample from the abstract; this systemic lack of clarity continues throughout the paper.

Due to these fundamental presentation flaws, I cannot provide a competent or fair evaluation of the paper's technical soundness. 

In its current state, the work is not ready for publication at ICLR. It would require a complete and substantial rewrite to become understandable and reviewable. Therefore, I must recommend **strong rejection**.

### Strengths
N/A.

### Weaknesses
See above.

### Questions
N/A.

### Soundness
1

### Presentation
1

### Contribution
1

### Rating
0

### Confidence
4