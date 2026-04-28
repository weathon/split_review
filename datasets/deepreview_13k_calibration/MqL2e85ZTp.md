# Uncertainty-Guided Optimization on Large Language Model Search Trees

- Decision: Reject
- Avg Score: 6.40
- Scores: 6, 6, 6, 6, 8

## Abstract
Tree search algorithms such as greedy and beam search are the standard when it comes to finding sequences of maximum likelihood in the decoding processes of large language models (LLMs).
However, they are myopic since they do not take the complete root-to-leaf path into account.
Moreover, they are agnostic to prior knowledge available about the process:
For example, it does not consider that the objective being maximized is a probability and thereby has specific properties like being bound in the unit interval.
Taking a probabilistic approach, we define prior beliefs over LLMs' transition probabilities and obtain posterior beliefs over the most promising paths in each iteration.
These beliefs are useful for defining a sample-based, non-myopic acquisition function that allows for a more data-efficient exploration scheme than standard search algorithms on LLMs.
Crucially, unlike expensive simulation-based non-myopic methods like the Monte Carlo tree search, our method only requires samples from the beliefs.
Our formulation thus views LLM decoding as Bayesian optimization on trees.
We discuss how to select the prior and the acquisition function, and demonstrate in experiments with various LLMs that our method achieves higher efficiency than recent baselines:
Our method achieves the same or a higher likelihood while expanding fewer nodes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces an efficient tree-search method by combining Bayesian Optimization with tree-search.

### Strengths
Authors propose an interesting idea of combining an existing sample efficient method: Bayesian Optimization (BO) for LLM generation. 
BO is usually applied in continuous domain which use Gaussian priors. The authors extend BO and its acquisition function for LLM use-case. Search in LLM is an important problem. 

The results based on log-likelihood show some proof of concept of the method being sample efficient.

### Weaknesses
experiments with regards to other known quantitative metrics apart from BLEU score and log-likelihood are lacking such as ROUGE-score

the explanation of the method can be further improved to better understand the contributions given there's no access to code.

tokens generated are much smaller which could be a limitation for tasks such as story-telling.

### Questions
the authors mention that high log-likelihood does not imply good quality or human desirable generation. In this regard Fig 3. showing BLEU scores is a nice result, however, it would be interesting to also observe ROUGE scores for summarization tasks. 

For Fig. 3, is there a reason why BLEU score drops with increase in number of expanded nodes? Is this related to why ULTS works better for relatively short number of token generation? 

From the plots in Fig. 4, it seems that by expanding more nodes, beam search or multinomial BS eventually give better log-likelihood, do the authors have any comment on this? 

Also, have the authors thought about combining their method with beam search? for example: for initial few generations using BO based tree search and then afterwards continue on with beam-search like generation? 

Can authors give a toy example on the how the N samples mentioned in Section 3.4 (decision making) is used by the acquisition function and correspondingly give some example value for the acquisition function ? (maybe if it is easier to add in Fig. 1 or if a separate Fig. is need? )

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
This paper proposes Uncertainty-Guided Likelihood-Tree Search (ULTS), a novel probabilistic approach to decoding in large language models (LLMs). ULTS utilizes Bayesian optimization principles to guide search in a tree structure, using prior and posterior probability distributions to efficiently identify paths with high likelihood. By incorporating uncertainty into path selection, ULTS aims to balance computational efficiency with output quality, avoiding the need for exhaustive exploration. The approach is tested on machine translation, summarization, and text generation tasks, with results indicating improved log probability and BLEU scores compared to beam search and other decoding methods.

### Strengths
**Novel probabilistic approach**:
The proposed method, ULTS, introduces a Bayesian-inspired probabilistic tree search approach, efficiently incorporating uncertainty to improve path selection in language model decoding.

**Efficiency-focused design**:
The method reduces computational costs by leveraging prior and posterior distributions, balancing search depth with output quality.

### Weaknesses
 **MAP Decoding Objective and Its Limitations in LLM Decoding**:
It has been widely observed that Maximum A Posteriori (MAP) decoding from language model generation, which this paper relies on, has notable limitations, such as its tendency to produce short, repetitive, or degenerate text [1,2,3]. While the authors acknowledge the issues and claim they are orthogonal to this paper in Section 3.5, decoding objectives in language models are crucially tied to LLM performance quality. These issues cannot be considered orthogonal as long as the main application is decoding from language models.

**Limited Discussion of Existing Decoding Methods**:
The Related Work section focuses on search algorithms for tree exploration but omits the discussion of standard decoding techniques such as top-k, nucleus, and MBR decodings, which are widely used in language model generation. The paper's contribution is difficult to comprehend without addressing these established methods and limitations of MAP decoding, particularly regarding generation quality and efficiency.

**Limited baselines and evaluation metrics**:
Strong baselines are missing while the experiments compare several recent decoding methods. For example, in close-ended generation tasks like NMT, state-of-the-art decoding methods such as Minimum Bayes Risk (MBR) are not evaluated. Comparing ULTS to MBR decoding would clarify its effectiveness in achieving high-quality translations. Summarization is mainly assessed through log probability, which may not sufficiently capture output quality regarding relevance, coherence, or informativeness. Including task-specific metrics like ROUGE, BLEURT, or human-evaluated coherence would provide a more comprehensive view of ULTS's performance in LLM applications.

### Questions
See the weakness section above.
Additionally, although the above discusses issues with MAP decoding, relating this work to recent studies, such as the following, might make for an interesting contribution:

Davis Yoshida, Kartik Goyal, Kevin Gimpel; "MAP's not dead yet: Uncovering true language model modes by conditioning away degeneracy," ACL 2024.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Uncertainty-guided Likelihood-Tree Search (ULTS), a novel approach to decoding in large language models (LLMs) using Bayesian optimization. Unlike traditional myopic search methods (e.g., beam search), ULTS applies probabilistic reasoning, modeling uncertainty to prioritize search paths that maximize the likelihood efficiently. Experiments demonstrate that ULTS achieves comparable or better performance than baseline methods with fewer node expansions.

### Strengths
- The paper addresses a meaningful and interesting problem -- how to incorporate uncertainty in the search during sequential generation 
- The method of viewing LLM decoding as bayesian optimization over trees is novel to me.
- The theoretical soundness is matched by well-executed experiments.
- The authors provide an open-source implementation, allowing easy adoption and further exploration.

### Weaknesses
 - Symmetric priors may not fully capture natural language distributions although the authors have discussed this limitation.
- Although efficient in node expansions, ULTS has some overhead compared to batch-expanding methods like beam search.

### Questions
- How sensitive is ULTS to the choice of Dirichlet prior parameters?
- How can we further improve the runtime for ULTS?
- Is ULTS applicable to other tasks or customized to LLM decoding? For example, can we apply it to reinforcement learning tasks?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a probabilistic approach of sampling from language models. The softmax probabilities in each step are modeled as independent random variables with a chosen (dirichlet) or an estimated (empirical) prior. Then, according to the probabilistic model, a method of choosing the next token is proposed, which requires a precomputed prior of the optimal gain and an estimated acquisition function. The work then discusses limitations and related works of the idea.

In the experiments, it is shown that the proposed approach, named ULTS, gives higher probabilities with fewer "averaged expanded nodes" across different datasets. Also, the additional runtime overhead from ULTS is small comparing to the decoding part of LLMs. The experiments also explore a different acquisition function which trades perplexity for diversity.

### Strengths
Overall, the presentation of the experimental results is good and many related works are adequately discussed. The batch acquisition strategy discussed in the conclusion section looks interesting and may be useful in the future.

### Weaknesses
I am from the Bayesian side but I do not buy the story of Bayes in this paper.
- Section 3.3 is on posterior beliefs of the optimal values. The probabilistic model is so strange that the posterior becomes the same as the prior for $\Delta_i$. It only tells me that the observation, which is the path from $\textbf{x}_0$ to $x_i$, gives no information about the future. This makes sense given its independent assumption. However, from my view, it is simply a heuristic decoding algorithm without any Bayes in it.
- The work compares itself with Bayesian optimization techniques multiple times (line 39, line 260). But I still do not see how the "Bayesian" comes in. The only part that may be related is the backup procedure in line 262-269. However, the term "propagate" in this part seems crucial but is never clearly defined. How will the "prior" or the "acquisition function" be updated after an action? Also, the "backup" function in the pseudocode of Algorithm 2 is never defined. 
- The work uses the Beta distribution to bound the probabilities in the unit interval, claiming that it is beneficial. However, there is no evidences showing why it is the case. 
- The work states that the approach is non-myopic, so it can acquire higher probability sequences in the decoding procedure. However, it is not supported in the experiments, especially in Figure 4. If I do not care about the number of expanded nodes, ULTS does not seem to produce sequences with higher probabilities, which really weakens the statement. 
- I would also argue that the i.i.d. assumption is too strong, since it ignores the context in a decoding step. I think at least the context is important to be a probabilistic approach in decoding. 

Minors:
- In line 144, there is a definition of increment for games, which may be confusing when looking att other parts of the paper where $\Delta_i$ is defined differently.

I also have some concerns about the experiments, which are detailed in the next part.

### Questions
- In the experiments, how are the "average expanded nodes" defined for different approaches? Algorithm 2 looks at every children, (and possibly every grandchildren taking equation (2)). Does that mean ULTS may expand $b^2$ nodes each step?
- Where is $k_{\max}$ in Algorithm 2? A novel algorithm is proposed but the key hyperparameter to control its complexity should at least be in its pseudocode. 
- Following the weaknesses, how is the "backup" function implemented? Is it a Bayesian update of the prior or the acquisition function?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a novel non-myopic decoding strategy for LLMs.
They phrase the problem as Bayesian optimization, which lets them alleviate the expensive expansion of the search tree, that plagues other non-myopic tree search algorithms such as MCTS.
This is done by means of a pre-computed prior, which is updated by the evidence gathered in the decoding process.
Experiments demonstrate higher likelihood of decoded sequences and lower runtimes compared to baselines, with the caveat that batching for further efficiency has not been demonstrated yet.

### Strengths
Decoding is at the heart of improving LLMs, thus a better decoding strategy, even if it is only applicable in some specific cases, might have huge impact on the field.
The proposed algorithm performing bayesian optimization appears very natural in the setting and provides a way for non-myopic decoding using beliefs about future token probabilities or potentially other quantities such as harmfulness etc.
The formulation of the algorithm and its contextualization in prior work are very strong and the writing is of very high quality in this sections.

### Weaknesses
I think in its current state, the experimental evaluation, especially how it is presented, but also some details of experiments are the main weakness of the paper. Details as follows.

### Major
* I don't understand the experiments presented in section 5.2, e.g. where do I find the results for the generation and where the results for the summarization task?
* While hyperparameters and details for ULTS are well explained in the experimental setup, the baselines are hardly explained.
Even if standard values of the huggingface library are used, please state them at least in the appendix to make the experiment reproducible if the standard values in the library change eventually.

### Minor
* The captions from Figure 3 onwards are very short and could convey more information about the depicted experiment.
They could be more self-contained, otherwise I have to find where in the text the figure is explained.
* The y-range in Figure 3 is a bit odd (for the left plot), I would extend it a bit to include the contrastive baseline.
* I was puzzled about the main results (Fig. 3 and 4) for a long time, until I figures out that different dots correspond to different values of k/k_{max}. 
This should be made more obvious in the description of the results and in the figure caption.
* I don't find an ablation over the number of samples N used for the approximation (c.f. Alg 2). I understand this is not the costly part of the algorithm, but it would be nevertheless interesting for a practitioner to understand whether this parameter has a lot of influence.

Very generally, the quality of writing differs a lot between the experimental section (and some sections in the appendix, e.g. C.4) and the rest of the paper.

### Grammar, etc.
* line 343/344 wrong citation style after contrastive search
* line 366 "... are done on **a** single ..."
* line 367 "... in the tree **if** the <EOS> ..."
* !! line 369 "The results are in **Figure 3**. ULTS **is** both ..."
* line 403 "We use **a** context length ..."
* line 444 "**This is** outside of the present work's scope, but is a promising **direction for** future work"
* line 841 "... currently **slower in** settings..."
* line 843 "... in **memory-constrained** settings ..."

### Questions
* I have to a-priori specify a tree depth d for ULTS, but can I just select a rather large one to be sure that I can generate a good answer, or do I have to exactly guess the length of the answer I would like to have?
Obviously, if the best answer is longer than the specified depth, the algorithm doesn't work, but what about the other case, that it is (much) shorter than the specified length?
* What models are used for the speculative decoding baseline? Is the generating model the same as the one used for the other baselines? What is the second model?
* In line 364, what is referenced by "... the strategy in **(2)** for the selection ..."? Is equation (2) meant? The same goes for line 850 in the appendix.
* Why don't you filter the test datasets as described in section 5.2. before randomly selecting a subset?
* What is the rationale behind the different output sequence lengths for the different datasets in section 5.2? 
Was this somehow chosen systematically prior to the experiments? 
As described in the paper, it appears arbitrary and oddly specific to do it differently for the different datasets.
* Where do I see the summarization task described in lines 409 - 412?
* I understand that computing the prior can be done once, but I would nevertheless be interested in how long it takes roughly for certain depth and width of the search tree, to understand to which scenarios we can expect the algorithm to be useful. E.g. if we wait 100 years to compute a prior for depth 256 and width 256k on 10,000 samples, it is likely not usable in many applications. This would be important to know, even if only stated in the appendix.

### Soundness
3

### Presentation
3

### Contribution
3
