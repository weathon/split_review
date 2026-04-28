# Efficient Perplexity Bound and Ratio Matching in Discrete Diffusion Language Models

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 8, 5, 8

## Abstract
While continuous diffusion models excel in modeling continuous distributions, their application to categorical data has been less effective. Recent work has shown that ratio-matching through *score-entropy* within a continuous-time discrete Markov chain (CTMC) framework serves as a competitive alternative to autoregressive models in language modeling.
To enhance this framework, we first introduce three new theorems concerning the KL divergence between the data and learned distribution. Our results serve as the discrete counterpart to those established for continuous diffusion models and allow us to derive an improved upper bound of the perplexity. Second, we empirically show that ratio-matching performed by minimizing the *denoising cross-entropy* between the clean and corrupted data enables models to outperform those utilizing score-entropy with up to 10\% lower perplexity/generative-perplexity, and 15\% faster training steps.
 To further support our findings, we introduce and evaluate a novel CTMC transition-rate matrix that allows prediction refinement, and derive the analytic expression for its matrix exponential which facilitates the computation of conditional ratios thus enabling efficient training and generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper provides three new theorems concerning the KL divergence between the data and the learned distribution, improving model evaluation through a bound. 
A new transition-rate matrix (roulette diffusion matrix) that allows for token correction after unmasking in the reverse process is introduced, deriving its exponential matrix to enable efficient training/sampling. Finally, denoising cross entropy loss over score entropy is proposed for training discrete diffusion models, with up to 10% lower perplexity/generative-perplexity, and 15% faster training steps.

### Strengths
The paper is well-written and clear. 
Developing efficient perplexity bound and the training algorithm for discrete diffusion language models is an important yet challenging problem.

The particular forms of the bounds, the roulette diffusion matrix, the denoising cross entropy loss and are interesting and new. Both theoretical development and empirical evaluations are conducted.

### Weaknesses
From Table 2, overall GPT-2 performs best over SEDDs, CEDD*, and CEDDT. The practical usefulness of the new bound and training algorithm is not completely clear. Specifically, while the paper introduces a novel KL divergence bound and a roulette diffusion matrix, the empirical results do not convincingly demonstrate a significant advantage over existing methods like GPT-2 in language modeling tasks. The reported perplexity improvements are marginal, and it is unclear if the computational overhead of the proposed approach justifies these gains. The paper would benefit from a more thorough analysis of the trade-offs between the proposed methods and established baselines, particularly in terms of computational cost and practical performance.

### Questions
Line 147: \bf{x}^i_0 = x^i_0, is it a typo?

### Soundness
4

### Presentation
3

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
This paper presents new results for discrete diffusion models trying to estimate density ratios for language modeling task. The authors' contributions are threefold: (i) they provide an upper bound $J_2$ on the perplexity of discrete ratio-matching diffusion language models which is computationally more efficient than the bound $J_1$ known from the literature, and, as shown through empirical evaluation, is consistently tighter; (ii) they derive a novel training objective called cross-entropy discrete diffusion (CEDD) loss by making use of reparametrization of concrete scores; (iii) they propose an alternative to known transition-rate matrices referred to as "absorb" and "uniform" and derive exponential of this new "roulette" transition matrix necessary to compute conditional probabilities efficiently.

### Strengths
The novelty of the contents of this paper consists of several theoretical findings and undoubtfully is the main strength of this paper. These findings include a novel type of transition matrices for discrete diffusion models along with all the facts necessary to use it in practice. The feasibility of using this type of forward diffusions was shown through experiments. Second, a score reparameterization was used to derive a CEDD model competitive with a common SEDD model. Lastly, the novel bound $J_2$ on the perplexity of the generated text is proposed, and the experiments demonstrate that it is consistenly better than previously used bound $J_1$.
Overall, I think this is a good paper from the point of view of originality and significance of questions raised in it since discrete diffusion language modeling is the topic that so far receives relatively little attention compared to continuous-domain diffusion models.

### Weaknesses
1. I am not sure about the correctness of perplexity evaluation in Section 4.1. To evaluate likelihood (which is equivalent to perplexity evaluation) with an imperfect model may lead to unreliable results as you mention in line 362. I would suggest to use some better and more modern language models instead of GPT-2 and report some aggregated score.
2. CEDD* differs from CEDD by some hand-crafted time-dependent weights (line 324) and the results across different transition matrices types differ as follows from Table 1. It raises some concerns about CEDD training objective in terms of stability and sensitivity to the choice of $\omega(t)$.
3. Language models trained on language modeling task can be evaluated not only from the point of view of perplexity on this task. I am not talking about some NLU tasks we can finetune language models to - I've never seen such attempts in the context of diffusion models. But, e.g. in [1] diffusion language models are shown to be capable of spell checking / grammatical error correction. So, maybe it could be more impactful if the authors evaluated their CEDD also on tasks like this. 
4. When it comes to discrete diffusion language models, I always wonder about their scalability in terms of, say, model/batch size, or data size, or vocabulary size. Common language models based on transformers typically have some useful scalability properties and their performance increases with the increase in data/model size for carefully chosen training hyperparameters. Papers on discrete diffusion language models usually do not discuss these issues, but in my opinion it is important if we want to prove that such models really can compete with modern language models.

### Questions
The experiments reveal that $J_2$ is tighter that $J_1$ in all cases you studied. Do you have intuitive explanation of this phenomenon? Comparing the formulae (13) and (16) I can see that $J_2$ contains function $\bar{l}$ differing from $l$ by the $K$ function taken at conditional scores. This $K$ can have different signs depending on its arguments, and $J_2$ also has additional integral term and entropy of the reference distribution. Do you have any idea on how to explain the superior performance of $J_2$ compared to $J_1$?

### Soundness
3

### Presentation
3

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
The paper presents, to the best of my knowledge, novel theorems that eventually lead to an enhanced performance compared to the baseline (SEDD). The authors further introduce a predictor-corrector version for the ratio matching framework called roulette diffusion.

### Strengths
The paper is well written and introduces, to the best of my knowledge, a novel set of theorems.

### Weaknesses
* My primary concern is that the authors appear to utilize the official implementation of SEDD, which has been demonstrated to have a flaw in the gumbel max trick used for sampling. In [1], the authors show that when using sampling in low precision for high dimensional distribution it leads to an effect similar to sampling with temperature. This is highly related here as the exponential in the proposed method may even anneal the temperature more.
* Prior Work: The authors only compare their results with SEDD, neglecting other relevant works in their analysis, such as [2] and [3].
* Predictor-Corrector: The aforementioned works incorporate some forms of predictor-corrector methods, and I believe it is necessary to include comparisons with these approaches.

### Questions
See above

### Soundness
3

### Presentation
2

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
This paper proposes novel theoretical results and empirically validated improvements for diffusion language models in the continuous time discrete state space framework.  Specifically it establishes new bounds and relationships for KL divergence between empirical and learnt distributions, including an improved upper bound on perplexity of the estimated model.  Furthermore, it introduces a novel transition-rate matrix, termed Roulette diffusion, which generalizes both uniform transition-rate and absorb transition-rate matrices and admits an analytical matrix exponential.  Empirical results demonstrate that use of cross-entropy discrete diffusion (CEDD) to carry out ratio-matching (modeling of ‘concrete scores’) for uniform, absorbing, or roulette diffusion, is superior to ratio-matching using score-entropy (SEDD), and the proposed upper bound on perplexity is tighter than the previously published bound.

### Strengths
* Advances state of the art in continuous time discrete space diffusion language modeling with novel theoretical results pertaining to KL divergence between empirical and model distributions, including a tighter bound on model perplexity.
* Empirical results demonstrating the superiority of the proposed perplexity bound, as well as uniformly better perplexity performance of the CEDD approach over SEDD.
* Well written paper.

### Weaknesses
The largest weakness of the paper in my view centers around evaluation of the proposed models.  The paper presents perplexity results under GPT-2 as well as the perplexity bounds, but it is also acknowledged that GPT-2 based measures have their own potential issues, and with bounds a question of tightness always remains.  Thus, how good these models truly are, and how do they compare/contrast with more traditional auto-regressive LLMs remains an open question.

### Questions
Related to the weakness above, would it be possible to take these language models through the supervised fine-tuning steps and evaluate on set of tasks that LLMs are commonly evaluated on?

### Soundness
3

### Presentation
3

### Contribution
3
