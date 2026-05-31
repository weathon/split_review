## Human Reviewer 1

### Summary
This paper investigates whether large language models can engage in strategic deception and whether current interpretability tools (especially SAE features) can detect it. The authors design game-like tests to elicit deceptive behavior and analyze SAE activations during these scenarios. They claim that the deception features identified by SAE fail to activate when lying occurs, suggesting current interpretability methods are blind to such behavior. The work positions itself as an early attempt to probe “hidden deception” in LLMs.

### Strengths
1. **Creative experimental design**: The “Secret Agenda” and “Insider Trading” setups show some originality in trying to operationalize deception through game-like tasks.
2. **Broad model coverage**: The study evaluates a large number of models (around 38), providing some breadth and comparative perspective across different architectures and providers.

### Weaknesses
I find the main weaknesses of this paper to be (1) its poor situating within existing literature and (2) major issues in clarity, rigor, and methodological grounding.

First, the paper is poorly situated in related work. It makes strong claims about deception and interpretability without referencing key prior studies in truthfulness, mechanistic interpretability, or SAE analysis, leaving its novelty unclear.

Second, the organization and clarity are weak. The introduction is too short, figures are oversized, and many technical details—such as how features are selected or how “feature fine-tuning” is done—are missing or unclear (e.g., “when tuned to -1 nor when tuned to +1” is never properly explained).

Third, the authors misinterpret and underestimate current interpretability methods. Claiming that SAE “deception features” failed to activate does not justify dismissing the SAE framework; this reasoning overlooks the distributed and compositional nature of such representations.

Fourth,  the paper criticizes existing evaluation methods without evidence. In line 100, the authors state that current evaluations are “unreliable, hard to replicate, and unrealistic,” yet they never specify which methods these are or provide comparisons to support the claim.

Finally, the format and presentation are below standard. The text is brief relative to the figures, captions are vague, and the layout feels unbalanced and unfinished.

### Questions
Please refer to weaknesses

### Soundness
2

### Presentation
1

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
The paper presents a reproducible testbed for eliciting deceptive behavior in LLMs based on a game that requires the player to lie to succeed. It demonstrates that this elicits deceptive behavior in 38 tested models. It explores the effectiveness of auto-labeled SAE features for detecting strategic deception in the new deception test bed. It claims that auto-labeled SAE features are limited in their ability to detect or suppress deception as demonstrated by small latents in "deception" related features and continued instances of deception despite suppressing those features. Lastly, it presents a method for clustering SAE latents using PCA+t-SNE to demonstrate domain-dependent effectiveness of SAE feature interpretability.

Mandatory disclosure of LLM usage by the reviewer: This review was formatted using LLMs to structure the text into paragraphs and numbered lists.

### Strengths
1. The paper addresses an important topic of strategic deception using a new binary testbed.

2. It demonstrates that deception can be elicited in across 38 different models.

3. The results are reproducible and experimental setup is well documented.

4. The effectiveness of SAEs at detecting strategic deception is put into question and backed up by experiment.

### Weaknesses
1. In section 4, the paper claims that Secret Agenda game aims to generate "high stakes deception", however given that the problem is framed as a game does not feel high stakes as in Agentic Misalignment (arXiv:2510.05179) where the agent reported that it was fully aware that its actions will cause harm to a human being.

2. The game framing may limit generalizability in two ways: (1) models may be following game rules rather than exhibiting deception that would occur in deployment, and (2) the artificial stakes may not activate the same neural mechanisms as real-world deception. While the authors acknowledge this is a "controlled deception laboratory", the connect between game-based deception and deployment risks needs stronger justification.

3. It would drive the point home if the Secret Agenda test bed could elicit deception in case deception is clearly harmful, though I admit that deception of any kind is evidence enough - it would be trivial for a third party to cause the model to deceive.

4. Performing section 7 scatter plot for Secret Agent SAE latents seems like a natural step that could shed light on the proposed feature search methodology.

5. Along the same lines I would be very curious to see how raising or lowering the states changes models behavior and the SAE activations. Will SAE features become more sensitive in a "real" scenario? Will the model avoid deception knowing that it will cause harm?

### Questions
1. In section 7.3, by "contrasting results" do you mean the difference between Secret Agenda vs Insider Trading or something else? If so, why was the "top discriminative features" not and PCA+t-SNE scatter plot analysis not applied to Secret Agenda SAE latents?

2. The authors acknowledge under limitations that game scenarios might not generalize to all deception types. There are clearly tradeoffs here that make it difficult to pin down and also gets at the heart of the problem. If the scenario is a game entirely different features may activate for "in-game deception" compared to "real world deception". Could you understand whether what (if any) SAE features activate highly for "in-game deception"?

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 3

### Summary
The paper outlines an investigation of strategic deception in LLMs using two developed testbeds – Secret Agenda and Insider Trading Compliance. The former testbed is based on its namesake, a social deduction game with the LLM set as the Dictator, wherein the games are set up such that lying is the easiest path for the model to win. Experiments in this “controlled deception laboratory” show that LLMs consistently resort to deception (Figure 1).  More troublingly, the models achieve this deception without activating features that are expected to be linked to deception. On the other hand, the Insider Trading Compliance testbed exhibited activation of deception-linked autolabelled features; the models continued to engage in insider trading almost half the time.

Put together, these results illustrate the serious challenge and risk posed by LLMs strategically lying to maximize their stated objectives. Moreover, the disconnect between autolabelled deception-related features and the activations observed in the Secret Agenda tests limit the utility of tuning these features to limit strategic lying by the LLMs.

### Strengths
The paper sheds light on an important challenge, especially when generalizing LLMs to other domains. Honesty of models when providing responses is paramount to build trust for users and a necessity for their adoption in domains with high compliance standards. Consequently, testing methodologies to audit models for deception and testing the efficacy of corrective measures is an important contribution. 

In particular, the result illustrated in Figure 1 is the most striking because it shows that all the tested models strategically resort to deception most of the time. Granted that Secret Agenda puts the models is adversarial situations where deception is the easiest path to victory, but it is desired and possibly a must, that LLMs do not lie even in such settings. While the result in Figure 3 is not as striking, the models electing to engage in insider trading nearly half the time is also a worrisome and significant result.

Finally, the conclusion that the pertinence of autolabelled SAE deception-relevant features for model deception is likely setting-dependent is noteworthy as (a) it suggests that the utility of these features and deception mitigation strategies predicated on these features could be severely limited in some scenarios and (b) indicates that feature-based interventions and interpretations are more instructive with structured data.

### Weaknesses
While I appreciate the wider point and results conveyed by this paper, the writing of the paper leaves a lot to be desired. It is overfull with jargon and, missing references and explanations; this necessitates that the reader either be very familiar with this area or read multiple references so that he/she may understand the paper and the results contained therein.

An example of this are the repeated references to SAEs and features labeled by SAE but its full form (Sparse Autoencoder) is only stated on Page 5. Moreover, there is no explicit discussion of SAE-based labelling of features and its uses for interpretability. Another example of the lack of details are the various game contexts in Section 5.3, with little explanation for the game contexts and explanations for the authors’ selection of these contexts in their tests.

### Questions
**Questions:**

1.	What do the authors mean on line 59 when they aver that their “operationalization remains agnostic to assumed beliefs”?
2.  On line 260, it is stated that refusal responses comprise the majority of outputs. This appears to contradict the results in Figure 3, and more broadly contrasts with the results of the Secret Agenda tests.

**Suggestions:**

1.	In the conclusion, the authors state that “identity-feature interventions often degraded outputs into repetitive, incoherent loops.” This is the first mention of any such result in any part of the main paper, and hence does not follow from any of the preceding discussion. The previous discussion of this result should be moved into the main paper or this should be removed from the conclusion to ensure coherence of the manuscript.
2.	Please justify any design choices made in the proposed test beds.

### Soundness
4

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
3