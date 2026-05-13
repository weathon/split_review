# Controllable Generation via Locally Constrained Resampling

- Decision: Accept
- Scores: 5, 6, 5, 8

## Abstract
Autoregressive models have demonstrated an unprecedented ability at modeling the intricacies
of natural language.
However, they continue to struggle with generating complex outputs that adhere to
logical constraints.
Sampling from a \emph{fully-independent} distribution subject to a constraint is hard.
Sampling from an \emph{autoregressive distribution} subject to a constraint is doubly
hard: We have to contend not only with the hardness of the constraint but also the 
distribution's lack of structure.
We propose a tractable probabilistic approach that performs Bayesian conditioning to
draw samples subject to a constraint.
Our approach considers the entire sequence, leading to a more globally optimal constrained generation than current greedy methods.
Starting from a model sample, we induce a local, factorized distribution which we can
tractably condition on the constraint.
To generate samples that satisfy the constraint, we sample from the conditional distribution,
correct for biases in the samples and resample. 
The resulting samples closely approximate the target distribution and are guaranteed to satisfy
the constraints.
We evaluate our approach on several tasks, including LLM detoxification and solving Sudoku puzzles.
We show that by disallowing a list of toxic expressions our approach is able to steer the model's outputs away from toxic generations, outperforming similar approaches to detoxification.
We conclude by showing that our approach achieves a perfect accuracy on Sudoku compared to $<50\%$ for GPT4-o and Gemini 1.5.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper studies the problem of sampling from the distribution given by a pretrained language model subject to logical constraints (which could be expressed as lexical constraints, automata, etc.). 

It is proposed to compile a constraint into a circuit, so that conditioning a distribution that factorises fully over positions on the constraint computed by the circuit is tractable. To approximately sample a LM subject to constraints, we first draw unconditional samples, then build a fully factorised proposal distribution using the LM's next-token probabilities and constrain it by the constraint circuit; this procedure yields a collection of samples that satisfy the constraints, together with importance weights relative to the true target distribution.

This method is evaluated on two combinatorial/planning tasks and on a LLM detoxification task, achieving a high rate of constraint satisfcation.

### Strengths
- Relevance/significance: As the authors write in the introduction, conditioning LMs with logical constraints is important but difficult. This work proposes a method that is guaranteed to generate samples that satisfy constraints and, unlike others, requires no Monte Carlo or model training.
- Clarity:
  - The presentation of Sections 1-4 is, in my opinion, very good. The reviewer is familiar with circuits and graphical models, which certainly helps (a simple diagram appearing earlier in the paper than current Figure 2 would probably help readers who are not). The didactic style and organisation make the motivation of the algorithm clear.
  - Thanks also for introducing notations in 2.1 but not overburdening the reader with excessive rigour.

### Weaknesses
 - Experiments:
  - Presentation: It would be good to see examples of the input and desired/undesired output for each task in the main text. It is hard to understand what is being done from text descriptions alone.
  - I do not find the results very convincing for a few reasons:
    - Error bars are not reported => impossible to assess significance.
    - Comparison with methods from prior work: only a trivial baseline is compared with for LLM detoxification, and only cold-prompted LLMs for Sudoku.
  - The LM application is quite basic. Toxicity is much more subtle than banning the forbidden words (note that the forbidden word list is not very comprehensive!). There should be evaluations involving the constraints that were actually imposed -- currently only scores from an auxiliary model (the Perspective API) are reported. 
    - On this subject, imposing intractable constraints such as those given by a toxicity model is outside the range of applicability of GEN-C. But could GEN-C with more basic constraints (banned words?) perhaps be used as a proposal distribution for approximately sampling a distribution constrained by an intractable classifier?
  - Some questions on experiments:
    - What is the typical variance of importance weights at the resampling step? Do you have any estimates of mode coverage? Current results don't illustrate well that the procedure gets a good approximation to the constrained distribution. 
    - How big are the constraint circuits in each of the experiments? (Relatedly, is there a nontrivial computation cost of running the proposed algorithm on top of regular decoding?)
- Description of related work in L350-352 does not seem quite accurate. While it is correct that these three methods (Qin et al., Hu et al, Lew et al.) do not guarantee constraint satisfaction, they study the problem of "soft" conditioning, i.e., sampling an intractable but full-support posterior. As for variance:
  - Qin et al. runs Langevin in a continuous relaxation and I am unsure what is meant by "high variance".
  - Hu et al. is not even an approximate inference method, but an RL-based amortisation method (so asymptotically -- at convergence -- it is unbiased). Of note, the training objective used there happens to have zero gradient variance at the optimum. So what is meant by "high variance"?
  - Lew et al. proposes a sequential Monte Carlo approach, which is asymptotically unbiased in a different sense: with enough particles and sampling steps, it will give correct samples. Does "variance" refer to that of the annealed importance weights?
  - By the way, there are hybrid SMC+amortisation approaches, e.g., [Zhao et al., ICML'24](https://arxiv.org/abs/2404.17546), which could be worth mentioning.

Overall, the idea is very interesting and the paper has promise, but I cannot recommend acceptance without more thorough experiments and more difficult problem domains.

### Questions
Please see "weaknesses" above.

Minor:
- Headings: There is not always consistent capitalisation (e.g., 3.1) and I don't understand the use of ellipsis in 3.4.
- L225 "structured" -> "structure"
- The name of the algorithm (GEN-C) does not appear until Section 5 (experiments). I suggest to introduce it earlier.

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
This paper introduces Gen-C, a novel probabilistic approach for controlled text generation with large language models (LLMs) that ensures outputs satisfy logical constraints while maintaining natural language fluency. The key idea is to use a tractable approximation of the LLM's distribution through locally constrained resampling: starting from an initial model sample, the method induces a local factorized distribution that can be efficiently conditioned on constraints using logical circuits. The approach addresses limitations of current greedy constraint enforcement methods by performing proper Bayesian conditioning across the entire sequence. The authors demonstrate Gen-C's effectiveness on several tasks, including LLM detoxification, Sudoku puzzle solving, and shortest path prediction, showing significant improvements over baseline approaches.

### Strengths
* The probabilistic circuits formulation moves beyond greedy token-by-step constraint enforcement. It is an interesting application of probabilistic circuits to a broadly applicable problem of constrained sampling in LLMs. 
* The logical circuits also proivde a more expressive and efficient constraint representation compared to traditional DFAs which are typically used in constrained sampling in LLMs. 
* The paper is quite well written, with easy to follow explanations for the idea, along with examples (Figure 1). 
* The results are promising and indicate potential applicability to a variety of problems.

### Weaknesses
 * A key aspect for sampling algorithms is the runtime, but from what I can tell there is no discussion of the runtime of the approach and how it compares to the baselines. Another aspect is the memory usage (which is also a challenge for large models), Another aspect which is unclear just from the results is how the method scales with the sequence length. 
* While results are promising as initial proof-of-concept, the experiments are mainly about relatively small-scale tasks. There is a limited exploration of more complex logical constraints and thus it is unclear how well the method can handle multiple competing constraints. 
* There are no ablations to inform the choice of the sampling parameters chosen. Without that it is hard to understand how to apply the method to a new problem. Specifically, the choice of k in the top-k sampling for the local approximation is not justified, and it is unclear how sensitive the results are to this parameter. A $5\times$ increase in computational cost due to this parameter is significant and needs to be addressed with ablations. 
* There are no theoretical results on approximation quality obtained with Gen-C and there is limited discussion of failure cases or limitations in the paper.

### Questions
* How does the method handle cases where constraints are mutually exclusive or when no valid solution exists?
* Could you provide more details about the choice of temperature parameter in the resampling step and its impact on generation quality?
* What is the impact of the size of the initial sample set on the quality of the final generations?
* How robust is the method to different types of logical constraints, particularly those that require long-range dependencies?
* Could you elaborate on how the approach might be extended to handle soft constraints or preferences rather than just hard logical constraints?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a novel method to sample from LLMs while satisfying constraints. The approach is based on sampling a preliminary sequence in the traditional (autoregressive) fashion, from which a tractable distribution approximating the target one (i.e., the autoregressive distribution conditioned on the constraint) is obtained. Then, samples from this distribution (which then satisfy the constraints) can be easily obtained and importance sampling can be used to renormalise them using the probabilities assigned to them by the autoregressive model. The local approximation is obtained by using constraint circuits, which the paper argues are more efficient than using regular expressions to check for constraints. The method provides exact samples from the target distribution (the autoregressive one conditioned on the constraints), which simpler greedy approaches are incapable of. The experimental results show the method allows perfect consistency with the constraints and very high performance.

### Strengths
originality:
- The method originally builds upon existing techniques in Bayesian inference and constraint circuits to tackle constrained generation with LLMs.
- The presented approach seems to be a step change with respect to simpler greedy methods.

quality:
- The method is effective, leading to great performance.

significance:
- Constrained generation is a central problem with LLMs, so addressing it is essential.

### Weaknesses
The major issue with the paper is the lack of clarity in the notation and in presenting the method. In particular:
- First, I don't find myself fully convinced that the greedy sampling approach leads to samples that are not exact, due to the following reasons: 
	- it seems to me that greedy sampling is effectively identical (even though not operationally identical) to rejection sampling of full completions, by which I mean sampling multiple completions until they do not satisfy the constraint because the constraint is "hard" (you either satisfy it or not).
	- I believe rejection sampling of full completions targets the right conditional distribution 
	- It is correct that it is intractable to compute the normalizing constant of the conditional distribution, but that is generally not required for sampling from a distribution.
This amounts to saying that, actually, what the authors call the "myopic" distribution is identical to the exact one. Is there any fault with my reasoning here? I believe it would be useful for the authors to explain this carefully; for instance, it would be helpful, in Section 2.3, to give concrete example differ for specific choices of constraints.
- As I am not familiar with the topic, I found the discussion of logical circuits, DFA and related arguments in the second paragraph of the introduction and Sec 3.2 to be interpretable. After reading that, I am unsure about what is the difference between DFA and RegExp, and how constrain circuits can implement the former but not the latter. 
- The notation for the probabilistic quantities must be made more rigorous. For instance, 
	- from time to time new notations are introduced without being defined; for instance, the beginning of Sec 3 talks about $q(y)$ but Eq 3 uses $q(y,\tilde y)$, without explaining what it is; similarly for $p_y(\tilde y|\alpha)$ in Eq 8.
	- Strictly speaking, the right-hand side of Eq 5 is identical to the one of Eq 4 but evaluated in $\tilde y$ rather than $y$, but these two are used to define two different quantities. I assume the authors are abusing notation there, by assuming $p$ indicates a different distribution according to whether the argument has a tilde or not.

### Questions
Sec 3.2: 
- What is the difference between DFA and RegExp? Also, as DFA is more efficient, are there any downsides to using it? In particular, are all constraints expressible in that fashion? And, are all constraints expressible with a constraint circuit that is deterministic, smooth and decomposable?

Sec 3.3:
- X and Y in Eq 6 should be bolded.
- What is the "contextualised probability?"

Sec 3.4: 
- Shouldn't p_\tilde y(y) in Eq 7 also depend on alpha?

In terms of the experiments, it would be good to give some indication of how the different methods fare in terms of computing cost.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents GEN-C, a method for controllable generation that samples from a constrained subset of an LLM's distribution while maintaining the model's underlying probabilistic structure. The approach uses logical circuits for efficient marginal computation and importance sampling, while using a 1-Hamming-distance exhaustive proposal distribution.

### Strengths
1. The theoretical foundation is well-motivated, combining probabilistic sampling with logical constraints in a principled way.
2. The implementation leverages efficient logical circuits for marginal computation, which is novel as far as I am aware.
3. The experimental validation covers both practical (toxicity reduction) and formal (Sudoku) tasks
4. The approach approximately maintains the model's distributional properties while enforcing constraints, unlike simpler masking approaches which do not attempt to preserve the distribution.

### Weaknesses
1. Clarity of exposition. The paper introduces multiple similar variables $(p_y, \tilde{p}_y)$ without clear distinctions. The probabilistic notation lacks consistency, making it difficult to track relationships between distributions. It would be useful to have a glossary in the appendix. It is hard to decipher what the full combined algorithm is, especially since algorithm 1 produces ${\tilde p}_y (y|\alpha)$ but ${p}_y (y|\alpha)$ is used in algorithm 2, which is presumably not the same. The paper would benefit hugely from a consolidated algorithm which shows the whole procedure. The relationship between the pseudolikelihood distribution $p_{\tilde{y}}(y)$ and the original model distribution $p(y)$ is not clearly explained, and it is not clear how the constraint $\alpha$ is incorporated into the sampling process in Algorithm 1. It seems that the constraint is only used in Algorithm 2, but the connection between these two algorithms is not made explicit.

2. Computational Complexity. As far as I can tell:
- The basic algorithm requires O(sequence_length × vocabulary_size) forward passes through the model
- For typical parameters (vocab size ~128K, sequence length 8), this amounts to approximately one million forward passes. This is quite a lot! But this doesn't seem to be discussed anywhere. In particular, it seems like there could be potential optimizations like those used in the paper [Universal and Transferable Adversarial Attacks on Aligned Language Models, Zou et al] which estimate one-hot deltas with a gradient-based approach. The computational overhead compared to simpler approaches like word banning is not adequately analyzed or justified. For instance, it's not clear if only one forward pass is used for the baselines while several hundred thousand are used for Gen-C. The paper states that top-k sampling is used to construct the pseudolikelihood distribution for the language task, but it is unclear if this approximation is used in the other tasks, and if so, what the value of k is. The computational cost of constructing the logical circuits is also not discussed.

3. Experimental Methodology:
As far as I can tell, the Sudoku experiments appear to guarantee 100% accuracy by construction, since any samples that are not valid are rejected, making comparisons with baseline methods potentially misleading. Shouldn't you also sample them until you get a valid sudoku? A fairer comparison would allocate equal sampling budgets to baseline methods like GPT-4 and Gemini. The improvements over word banning in toxicity reduction (Table 3) are modest given the substantially higher computational cost. It is unclear if the Gemini and GPT-4 baselines use structured decoding for the Sudoku task, which would be necessary for a fair comparison. The paper does not clearly state how many samples are used for the baseline methods, and if the same number of samples are used for all methods.

4. Novelty and Attribution:
- Section 3.2 appears to substantially reproduce content from the previous work [Neuro-Symbolic Entropy Regularization, UAI 2022] without appropriate attribution or differentiation.

### Questions
1. Could you provide a complete end-to-end algorithm that shows the full pipeline from initial model distribution $p_\theta$ to final constrained distribution $p^*$? The current split between Algorithms 1 and 2 leaves several implementation details unclear.

2. What is the computational cost of GEN-C compared to simpler approaches like word banning? Could the complexity be reduced using techniques similar to those in recent work on coordinate descent for language models?

3. In the Sudoku experiments, is the 100% accuracy rate an artifact of the constraint construction? How many samples are typically needed to achieve a valid solution, and how does it compare if you give the same number of samples to gemini or gpt4o?

### Soundness
3

### Presentation
2

### Contribution
2
