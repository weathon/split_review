# Self-Improvement in Language Models: The Sharpening Mechanism

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
Recent work in language modeling has raised the possibility of
\emph{self-improvement}, where a language models evaluates and refines its own
generations to achieve higher performance without external feedback. 
It is impossible for
this self-improvement to create information that is not already in the
model, so
why should we expect that this will lead to
improved capabilities? 

We offer a new perspective on the capabilities of self-improvement
through a lens we refer to as \emph{sharpening}. Motivated by the observation
that language models are often better at verifying response quality than they are at generating correct
responses, we formalize self-improvement
        as using the model itself as a verifier during
        post-training in order to ``sharpen'' the model to one
        placing large mass on high-quality sequences, thereby amortizing the expensive
        inference-time computation of generating good sequences. We begin by introducing a new statistical framework
        for sharpening in which the learner aims to sharpen a
        pre-trained base policy via sample access, and establish
        fundamental limits. Then,
        we analyze two natural families of self-improvement algorithms based on SFT and
RLHF. We find that (i)
the SFT-based approach is minimax optimal whenever the
initial model has sufficient coverage, but (ii) the RLHF-based approach
can improve over SFT-based self-improvement by leveraging
online exploration, bypassing the need for
coverage. Finally, we empirically validate the sharpening mechanism via inference-time and amortization experiments. We view these findings as a starting point toward a foundational
understanding that can guide the design and evaluation of self-improvement
algorithms. \loose

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a theoretical framework for analyzing language model self-improvement through the lens of "sharpening"—defined as the process of tilting a model's probability mass toward sequences with high self-reward (which crucially does not rely on any external information). The paper focuses mostly on the case where self-reward = log π(y|x), which has been used in previous self-improvement literature. It also focuses mostly on sharpening via self-training (as opposed to sharpening via only inference-time computation), which can be viewed as amortizing expensive inference-time computation/sharpening. With this in mind, the authors present two families of algorithms for sharpening via self-training: SFT-sharpening and RLHF-sharpening. SFT-sharpening uses Best-of-N with self-reward to generate a new SFT dataset to fine-tune the model, while RLHF-sharpening uses RLHF with self-reward as the reward function for preference scoring (the paper looks at DPO-style algorithms specifically). These families of algorithms come from previous self-improvement literature.

To analyze the sample complexity of these algorithm families, the authors introduce a "sample-and-evaluate" framework where sample complexity is measured in terms of m = n * N sample-and-evaluate queries (n sampled prompts with N generations sampled per prompt). They prove a lower bound on the sample complexity for any sharpening algorithm. Then, they prove that both SFT- and RLHF-sharpening can learn sharpened models under the maximum likelihood objective (ie, maximizing self-reward), and they prove the sample complexity of each (with certain assumptions about model coverage). Finally, they demonstrate that adding online exploration to RLHF-sharpening can replace the dependence of sample complexity on model coverage to a dependency on the complexity of exploration.

### Strengths
- The paper is well written and easy to follow, with a detailed appendix containing proofs and additional results like guarantees for purely inference-time sharpening.
- The work is relevant to the scope of ICLR and introduces a novel theoretical perspective and statistical framework to analyze language model self-improvement algorithms. It provides a much needed theoretical understanding of recently popularized self-improvement methods for language models.
- The SFT-sharpening and RLHF-sharpening algorithm families are widely used in self-improvement literature, making the theoretical results immediately relevant and valuable as a foundation for future work.
- The result showing that using online exploration with RLHF-sharpening shifts dependency from model coverage to complexity of exploration is a particularly interesting and significant result. Future works can analyze how different online exploration strategies affect sample complexity.
- The choice to focus on log π(y|x) as self-reward is simple yet well-motivated given its use in prior self-improvement literature. The framework established by the authors provides a foundation for future work to analyze the effect of using other self-reward functions on sharpening guarantees and sample complexity.

### Weaknesses
 - On lines 187 and 199, the paper states that the corresponding algorithm scheme converges to a sharpened model / sharpening objective in the limit. However, it does not seem to provide a justification or proof for these two statements (please let me know if I have missed it).
- Although focusing on log-probability as self-reward is justified, the paper would benefit from including a survey of other self-reward functions used in prior self-improvement works. This context would provide valuable guidance for others to build on the sharpening perspective by looking at alternative self-rewards.
- While the paper does mention the prior literature on self-distillation, it would benefit from a more complete summary of this prior line of work, including key findings and making it very clear how this work is different/novel.
- While emperical results are shown for inference-time sharpening, there are no experiments for self-training methods (SFT-sharpening, RLHF-sharpening) which are the main focus of the theoretical analysis. The paper would greatly benefit from including experimental results for SFT-sharpening and/or RLHF-sharpening, **with a focus on whether the theoretical results can be used to correctly predict something about the emperical results.** For example, can the theoretical results be used to predict the difference between running an RLHF-sharpening setup with and without online exploration? Or between SFT- and RLHF-sharpening? I would be curious to hear the authors' views on this.
- The conclusion focuses on future work but lacks a summary of the paper's key contributions and findings. The final manuscript would benefit from a summary of key takeaways in the conclusion. (No need to include it now in the rebuttal.)

### Questions
- What should experimentalists take away from this work? For example, researchers working on inference-time computation scaling, or those doing self-training. Can this work help them in some way?
- Do the authors see this work as being helpful for investigations into scaling laws for self-improvement? If so, how?
- In the RLHF-sharpening formulation, my understanding is that the KL-term ensures that the finetuned policy stays close to the base-policy, which is required since self-reward is defined using the base-policy (i.e., to keep generations in-distribution for the reward function). Is this correct? Furthermore, I am wondering whether the self-reward can be defined using the non-stationary policy that is being fine-tuned. What would be the effect of this change?
- Can you provide a more detailed explanation on the meaning of the coverage coefficient and how it can be problem dependent?
- [The questions mentioned in "Weaknesses"]

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper provides an answer to why self-improvement methods can improve model performance even if they do not increase the information the mode has access to.
It defines sharpening as the greedification of a model, i.e. outputting its most likely answer, which is typically hard to compute.
Sharpening can be applied at inference time (e.g. with Best of N) or at training time, and the paper identifies self-improvement as a training-time sharpening method which allows to replace or amortize inference-time sharpening.
It defines a framework for theoretically evaluating the sample complexity of sharpening methods and provides results for the sample complexity of SFT and RLHF sharpening/self-improvement (using the model's likelihood as a filter or a reward), giving sample complexity bounds for each method to achieve sharpening at training time.

### Strengths
### Contribution
- The identification of self-improvement methods as sharpening methods that trade training time for inference-time search is novel and important in the discussion of self-improvement methods.
- The sample complexity results provided for SFT-Sharpening and RLHF-Sharpening are novel and relevant to the community. The results on adding exploration to RLHF methods are relevant to the online vs offline discussion of post-training.
- The additional results in the Appendix, such as adaptive sampling for SFT-Sharpening to improve its sampling complexity, are appreciated and can drive the design of novel practical algorithms.

### Soundness 
- The sharpening objective and definition and the sample-and-evaluate framework are well-motivated and provide results that are relevant to practical settings.
- The assumptions made in the paper seem reasonable.

### Presentation
- The paper is very well written and easy to follow. The claims and their associated evidence/results are easy to identify.
- The remarks discussing the assumptions in depth, such as Remark 4.1, are well appreciated.

### Weaknesses
### Contribution:
- Line 256: It's appreciated and essential that the paragraph "Empirical validation of maximum-likelihood sharpening" verifies that sharpening provides downstream task improvement; however, in my view, this is a fairly known fact which could be presented in a more concise way, or acknowledged as a general fact. While the specific use of log-probabilities as a reward might not be explicitly validated in prior work, the general principle that models tend to perform better when they are more confident in their predictions is well-established. The current presentation overemphasizes this point, which could be streamlined.
- Definition 3.2: the generation-verification operation seems a bit restricted, but in a self-improvement context, this seems enough to me. The limitation lies in its narrow scope, as it does not encompass more complex forms of self-improvement that might involve iterative refinement or more intricate feedback mechanisms beyond simple verification.
- The results seem limited to the specific algorithms chosen IN RLHF-sharpening mainly REBEL and XPO. The theoretical analysis, while valuable, is constrained by the choice of these specific algorithms. It is unclear how the results would generalize to other RLHF algorithms that might employ different optimization strategies or reward structures. This narrow focus limits the broader applicability of the theoretical findings.

### Presentation:
- It can be misunderstood from the paper that self-improvement methods should exclusively be seen as sharpening methods, from the strong questions raised in the abstract and the introduction. I suggest rephrasing those as motivation to see self-improvement as sharpening. The framing of the paper could be adjusted to present sharpening as a significant aspect of self-improvement rather than its sole definition. This would avoid potential misinterpretations and broaden the scope of the paper's contribution.
- Line 194 typo: the expectation's long definition should be over $\pi$ instead of $\pi_{base}$.
- Proposition 3.1 introduces an important result, which is then not discussed. The transition to the next section is too abrupt. The paper would benefit from a more thorough discussion of the implications of Proposition 3.1, particularly concerning its impact on the subsequent analysis and the practical implications of the constant precision $\delta$ for greedy decoding.

### Questions
- Could the authors elaborate on their choice of REBEL and XPO as the algorithms studied?
- To what extent are the results in the paper limited to these algorithms?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper analyses self-improvement in language models (LLMs) through a mechanism called "sharpening." The authors focus on self-improvement where log-probabilities (of sequences of tokens) are used as the reward signal. They analyze two algorithms: SFT-Sharpening, which is optimal under sufficient model coverage, and RLHF-Sharpening, which can surpass SFT by utilizing online exploration to overcome coverage limitations.

### Strengths
This work develops a theoretical framework for studying and understanding self-improvement. 
They compare two approaches, SFT-Sharpening and RLHF-Sharpening, and prove their convergence.

### Weaknesses
1. While the authors empirically show there is useful signal in Best-of-N Sharpening (by sampling at inference), they do not empirically verify that SFT or RLHF training with this signal works. Specifically, the paper lacks experiments demonstrating that the proposed sharpening signal, derived from log-probabilities, can be effectively used to train models via SFT or RLHF. The core claim of the paper is that sharpening can lead to self-improvement, but this claim is not fully substantiated by training experiments.
2. The authors focus their analysis on the maximum likelihood self-reward. While this objective is simple, it has not been empirically explored a lot in self-improvement literature (as the authors themselves note). This raises concerns about the practical relevance of the findings. The theoretical analysis is based on a specific form of self-reward, and it remains unclear how well these results generalize to other self-reward mechanisms that might be more commonly used in practice.
3. The sentence in the abstract "*Motivated by the observation that language models are often better at verifying response quality than they are at generating correct responses*" is misleading in the context of this paper. Here, the reward is not assigned by asking the model to verify or critique its own solutions but by having access the log-probabilities of generated solutions. This discrepancy between the motivation and the actual method could confuse readers. In general (relevant for Introduction and Related Work sections), claims of self-improvement in LLMs should be handled with more nuance.  While there are papers that LLMs can self-improve without external feedback, there is also recent evidence of the contrary:
    -  Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, and Rui Zhang. 2024. *When can LLMs actually correct their own mistakes? A critical survey of self-correction of LLMs*
    -  Kaya Stechly, Karthik Valmeekam, and Subbarao Kambhampati. 2024. *On the self-verification limitations of large language models on reasoning and planning tasks*
    -  Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, and Denny Zhou. 2023. *Large language models cannot self-correct reasoning yet.*
    -  Kaya Stechly, Matthew Marquez, and Subbarao Kambhampati. 2023. *Gpt-4 doesn’t know it’s wrong: An analysis of iterative prompting for reasoning problems.*
    -  Karthik Valmeekam, Matthew Marquez, and Subbarao Kambhampati. 2023. *Can large language models really improve by self-critiquing their own plans?*

### Questions
While theoretically sound, can your work provide any guidelines for the practical deployment of sharpening techniques?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a theoretical framework to understand self-improvement. The authors define the sharpening as the best sequence according to the model likelihood which is different than greedy decoding or temperature sampling (the theory implies greedy decoding only covers the best sequence under some constraints). They further define self-improvement via SFT and RLHF using BoN and DPO, respectively. The authors show sample complexity bounds for SFT and RLHF using a model and data dependent coverage and concentrability coefficients. For example, sample complexity for SFT is proportional to coverage coefficient and logarithmically scales with size of the policy class. Finally, by adding exploration, the dependence on the coverage coefficient is replaced by sequential exploration coefficient.

### Strengths
Update: Authors' rebuttal addressed my concerns. I increased my score accordingly.

The proposed theoretical framework captures a very significant class of post-training improvements, ranging from SFT to RLHF. In particular, it covers BoN and DPO that are two very popular inference-time and post-training methods. The paper is also easy to follow.

### Weaknesses
My main concern is the lack of implications of the theoretical results for practical use.

1. While the theory covers many popular methods, such as BoN and DPO, there is not much connection to what this theory implies in practice.

A. For example, what predictions does it make about BoN, can we choose “N” based on your theory?

B. What is the minimal experimental setup to cover both SFT and RLHF?

C. How should we interpret Figure-1 based on your theory? Such as, would convergence rate of BoN be explained by your method?

2. While I understand that using the same context “x” for both policy and reward function is meaningful, in practice it is generally different. Can you discuss if an extension of your theory explains the sample complexity when using different contexts that are related by a function? In euclidean space, this could simply be defined as a bound on the distance between two context.

### Questions
Please see above for specific questions.

### Soundness
3

### Presentation
3

### Contribution
3
