# Efficient Controlled Language Generation with Low-Rank Autoregressive Reward Models

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 6, 5, 3, 8

## Abstract
Language models trained on large amounts of data are known to produce inappropriate content in some cases and require careful tuning to be used in the real world. We revisit the reward augmented decoding (RAD) approach to control the generation from a language model using the scores from a task-specific reward model. We investigate the training objective of RAD, and reformulate it as a task of learning a reward matrix. We show that RAD is designed to support high flexibility when representing the reward matrices, which leads to a higher computational costs during decoding. However, we demonstrate that RAD does not use its full flexibility. Motivated by this, we propose a simpler but more efficient low-rank parametrization of the reward model enabling fast and effective guided decoding. For the detoxification and sentiment control tasks, we show that our low-rank reward model performs on par with the more flexible RAD parametrization, while requiring only a single reward model call per generated token.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work present a low-rank approximation of RAD for controlled decoding of LMs. The paper first analyzes RAD, a well-known constrained decoding method and finds that RAD requires model call for all possible tokens making it computationally slow. An SVD analysis of a N x |V| reward matrix indicates that the reward model learns a low rank approximation. Based on this, the paper proposes ARM that learns a low rank approximation and computes the reward for all possible output tokens at once resulting in better computational efficiency. The paper performs evaluations on both toxicity and sentiment control showing that this method performs similar to RAD while being significantly faster.

### Strengths
- This paper shows a good analysis that RAD learns a low-rank approximation and therefore similar performance on toxicity/sentiments can be obtained with low-rank approximation. The reward model is split into two parts -- one for baseline reward estimation for the provided prefix and a separate term for the next token, allowing for an efficient inference framework.
- The low rank approximation allows for the reward computation for all possible next tokens in a single forward pass. Therefore, ARM provides a computationally efficient way to compute the reward as shown by Figure 6.

### Weaknesses
 - In terms of novelty, ARM essentially modifies the output head of the reward model to give the reward output for all K tokens at the same time for computational efficiency. This is a simple modification but the rank analysis presented in the paper make the claim to support this formulation stronger.
- The paper presents a linear approximation of the reward model for all K tokens simultaneously. It would be interesting to check how concatenation of $[Hw1^T; HWE]$ passed through an MLP (or any non-linear transformation) would perform. This should not increase the computational efficiency significantly but might improve the performance (especially to match RAD perplexity) for lower average maximal toxicity.

### Questions
- Could you comment on why the perplexity of ARM is higher in general for both the evaluations? Could adding an extra regularization term on natural text improve the perplexity?

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
2

### Summary
They present an approach for training low-rank autoregressive reward models for controlled generation. They first validate the low rank structure in standard but costly approaches to reward modeling -- which require taking a separate forward pass for each vocabulary item. They then propose a method which can distill this low rank structure into an autoregressive reward model which can operate much more efficiently. They finally, validate their method on toxicity and sentiment control tasks, using both reward and fluency (perplexity / MAUVE) as evaluation metrics.

### Strengths
* They do good analysis on the low rank structure of reward models
* They explain their method clearly and conduct a variety of experiments to validate it
* The paper is mostly well written
* Better controlled generation is an important problem.

### Weaknesses
 * They don't clearly explain how their method is that different from others which predict rewards auto regressively. e.g. why is this approach different from others like Liu et al. and Krause et al. which effectively do the same thing? It seems that their approach outperforms these? Is this due to the specifics of their distillation objective? This could be more clearly spelled out and also ablated with experiments in the paper.

 * It is unclear if the W matrix in WE, is meant to be lower rank than h. This should be clarified, as the low-rank nature of the reward model is a key component of the paper.

* Why MSE loss and not binary cross entropy with soft labels? Given that the reward is a scalar value between 0 and 1, it seems like binary cross entropy would be a more natural fit. The choice of MSE loss should be justified more thoroughly, or an ablation study should be included.

### Questions
* Is the W matrix in WE, meant to be lower rank than h?
* Why MSE loss and not binary cross entropy with soft labels?

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
3

### Summary
This paper considers the problem of steering a trained language model to generate better outputs. At a high level, this paper does this by proposing an improvement to the reward-augmented decoding (RAD) paradigm of Deng and Raffel (2023). Specifically, they propose a "low-rank autoregressive reward model" (ARM) for guided decoding. In a sentence, the ARM models reward scores for next token candidates. They provide theoretical support for proposing a lower-rank version of RAD, and they investigate two ways of doing this in practice:
1. They propose distilling RAD into ARM
2. They propose training ARM from scratch

### Strengths
In my opinion: at a high level, the strengths of the paper included the motivation, the clarity of the writing, and the clarity of the mathematical formulations. In more detail--

1. I thought that the introduction did a great job setting the scene and motivating the research direction. For example, the paper says: _"Control over LLMs can be roughly divided into methods which modify the original model via finetuning, and decoding-time solutions, which do not modify the parameters of the original model."_ These types of high-level summaries/divisions of "where the field is at" are very useful for providing context, and the paper is full of good things like this.

2. I thought that the motivation here as very high quality as well: _"the RAD approach is flexible enough to represent a large space of reward matrices including those of high rank. However, when we empirically measure the rank of the reward matrix learned by RAD, it appears to be low-rank."_ This was a very clear way of highlighting, early on in the paper, the high level motivation of the "main big idea" in the paper--doing a lower-rank version of RAD.

3. The formulation of _"Section 2.1: Guided Decoding with External Experts"_ was very high quality. Specifically, the formulas were all explained and motivated very well. It was delightful to read a math section as clear as this one.

4. Table 1 and Figure 6 are clear, and make the author's point about increased efficiency with the ARM method very clearly.

### Weaknesses
In my opinion: at a high level, the weaknesses of this paper were that rigorous theoretical justification for considering a low-rank version of RAD were deferred to the appendix and not adequately summarized in the main body of the paper; the paper proposes two different ways of doing low-rank RAD (distilling, and training from scratch) and this should be more prominently stated (e.g. in a "Our main contributions are as follows..." bulleted list); and the graphs in the paper are so difficult to understand that it is unclear to me to what extent the experimental results show any performance improvement.

In more detail--

1. _Section 3.1: Analysis of RAD_ could do a better job providing rigorous justification for why low-rank learning is more theoretically sound than what is considered in the original RAD paper. Delegating most of the rigorous mathematics to the appendix is problematic in this case, because that's where almost all of the rigorous claims where, if I understand correctly. I understand wanting to save space, but the paper has almost an entire page worth of more space... I think that it would seriously strengthen the paper to at least include statements of the "main theorems/propositions" and then delegate the proofs to the appendix. Also, framing this section around theorems/propositions would break it up and make the logical flow easier to follow. For example, this section includes the following phrases: _"Particularly, the incompleteness of PΩ(R) makes it easier for a reward model to learn a low rank approximation, especially for unique prefixes x, as we demonstrate in Appendix B.1. To better understand this phenomenon, we would like to understand whether the PΩ(R) can be fit with the low-rank model. In Appendix B.2, we demonstrate that indeed incomplete PΩ(R) matrix can be fit with the low-rank matrix factorization with a small error. This implies that the training dataset can be fit by a model that produces low-rank \hat R , regardless of the specifics of said model."_ To make the arguments rigorous and convincing, I think all these claims should all be spelled out in precise detail in the main body of the paper (using rigorous statements, instead of vague sentences like those I quoted), and then defer all proofs to the appendix. This is standard practice.

2. In Equation (8), I don't think RAD teacher \tilde r(x) is defined, and it's very confusing what it is. It wasn't until I got to the experiments section that I realized that the paper considers two paradigms--1) distilling RAD into "low-rank RAD" (i.e. ARM), and 2) training a low-rank RAD (i.e. an ARM) from scratch. I think this should be explicitly stated somewhere in that section that (7) and (8) are completely different training paradigms.

3. (The main weakness, in my opinion) the graphs/results are very unclear. In Figure 3, the figure is too busy for me to understand what's going on, and I've been spent considerable time trying. I recommend having 1 set of graphs with k=20, and a second set with k=40 (and putting set in the appendix) and zooming in so that we can actually see the order of magnitude differences between the curves that are being compared in the graph. I'm not sure what point this graph tries to convey; the paper needs to explain what each curve's trend represents, relative to the other curve's trends. And it is unclear to me how each of the individual points on the curves is obtained (I know there is some third, unseen parameter which parameterizes the curves and controls the toxicity/perplexity and toxicity/MAUVE tradeoffs. Why is this third parameter not explicitly mentioned in the figures? Further, is it significant that this third parameter doesn't let ARM distilled version's perplexity go past the mid-30's?) These graphs raise more questions than answers, and I don't understand how they provide experimental evidence that ARM is better than RAD. If the authors can clarify that point, I'd appreciate it. But without clarity on these experimental results, I don't have any confidence that performance of the ARM version is on par with the RAD version; my only take-away from these graphs are that every model follows an approximately 1/x shaped tradeoff curve, but that's alone is not sufficient to demonstrate the relative success of the method.

Some minor points:

1. On line 042, it says _"reward augmented generation (RAD)"_ when I think it should say "reward augmented decoding (RAD)".

2. In the next version of the draft, the paper should have every single equation numbered. E.g. I want to be able to reference the definition for D_f using its equation (see my questions), but I can't. This will let other researchers discuss the paper's contents more precisely.

3. If the authors want this paper to be self-contained, perhaps they can add a concrete example, with a given small prefix, to illustrate what goes on in Section 2.1: RAD Training. As someone who was not familiar with RAD until reading this paper, I had to read through this section a few times to understand what was going on, it is a tad dense.

### Questions
1. Re: the Definition of D_f, can the authors please provide for me some motivation for why we want to use the same reward y regardless of how long the prefix x is? It seems like this might add spurious correlations to the training data. (I don't think this necessarily needs to go in the paper, this is more of a question I'm asking to gain a deeper understanding of how RAD works... this seems a major shortcoming of the entire RAD pipeline, do you know if researchers have considered alternative ways of assigning numerical rewards to the shortened prefixes?)

2. Are equations (4), (5), and (6) all equal? As in, are they just versions of the same exact same equations? (It appears to me that they are...) If indeed they are, this should be noted somewhere in the paper.

3. In Appendix C.4, what is $\sigma_1$?

4. Re: Appendix C--can the authors please explain in more detail what issues might arise when estimating the numerical rank? (i.e. what types of things can go wrong. And how did the authors confirm that these things did not go wrong when they were estimating the numerical ranks for their experiments.)

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper explores an efficient way to guide language models using low-rank reward models for controlled text generation. Traditional approaches like Reward Augmented Decoding (RAD) is computationally expensive because it processes each candidate token individually (each token requires a forward pass using the reward model). The authors propose an alternative method, the low-rank Autoregressive Reward Model (ARM), which simplifies the process by representing the reward model with fewer parameters. This change maintains performance in tasks like detoxification and sentiment control while significantly speeding up decoding. ARM is shown to match RAD in quality but requires fewer computational resources.

### Strengths
1. The paper is well-written and easy to follow. The authors conduct thorough experiments to demonstrate the effectiveness and efficiency of the proposed approach. Enough experiential details are provided for others to replicate the results.

### Weaknesses
1. The proposed approach offers limited novelty. The authors suggest enhancing the prediction efficiency of the reward model by scoring all potential next tokens in a single forward pass through the language model's backbone (Section 3.2). However, this concept has already been explored in prior research [1, 2], which treats the prefix score as an action-value function using a language model as the backbone.

- Systematic Rectification of Language Models via Dead-end Analysis, ICLR 2023
- Controlled Decoding from Language Models, ICML 2024

2. Efficiency improvement seems limited as most of the computational cost comes from the LM backbone.

### Questions
In Section 3.3 on ARM training, is the language model backbone also fine-tuned, or is it kept frozen?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
* This paper proposes ARM (Autoregressive Reward Model), a low-rank approximation of RAD (Reward Augmented Decoding) for reward-guided controlled decoding. 
    * ARM is motivated by casting the reward modeling problem into matrix completion and the empirical insight that the “reward matrix” to complete is low-rank.
    * ARM has a more efficient inference complexity of $O(L)$ in terms guiding a length-$L$ generation and considering $k$ next-token candidates at each step. In comparison, RAD has a complexity of $O(Lk)$. 
    * ARM is trained with two steps: (1) train with RAD’s objective to estimate next-token reward given the prefix and (2) distill from a RAD teacher. 
* They conduct two sets of controlled generation experiments: Detoxification as evaluated on the RealToxicityPrompt dataset and Sentiment Control as evaluated on the OpenWebText’s prompts. They evaluate the effectiveness of ARM controlled generation with the fluency-controlled attribute (toxicity/sentiment) tradeoff in comparison with RAD and previous methods such as GeDi and DExperts.
* Their experimetnal results suggest that ARM achieves similar if not better fluency-controlled attribuite tradeoff compared to RAD and previous methods on these two tasks. They also show that the resultant reward matrix from ARM is indeed low rank as designed.

### Strengths
* The paper is clearly written and well-presented.
* The experiments are extensive with sensible setups and evaluation procedure. 
* The proposed method ARM performs on par with the more expensive RAD alternative at much better inference complexity.

### Weaknesses
 * It would be good to have a expanded discussion of some experimental results (See Questions below).
* It would be good to include the compute required for training/evaluating these models.

### Questions
1. Are there hyper-parameters similar to the beta in RAD & ARM for GeDi and DExperts to trade-off fluency for detoxicity? If so, it would be good to show their operating points in Figure 3 to make a stronger case.
2. In Figure 3, increasing k seems to induce a right-ward shift (i.e., higher perplexity at similar toxiticy level). Could you help me understand why?
3. Line 431: “we observe that regularization effectively decreases the rank of R_ARM which might explain the higher fluency of regularized model.” This suggests lower-rank approximation is better in terms of fluency. Can you expand on this point and help me understand why this is the case?
4. What is the compute time required for running evaluation and training ARM?

### Soundness
4

### Presentation
4

### Contribution
3
