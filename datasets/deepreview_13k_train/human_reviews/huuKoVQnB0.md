# Improving Pretraining Data Using Perplexity Correlations

- Decision: Accept
- Scores: 6, 5, 8, 5, 6

## Abstract
Quality pretraining data is often seen as the key to high-performance language models. However, progress in understanding pretraining data has been slow due to the costly pretraining runs required for data selection experiments. We present a framework that avoids these costs and selects high-quality pretraining data without \emph{any} LLM training of our own.  Our work is based on a simple observation: LLM losses on many pretraining texts are correlated with downstream benchmark performance, and selecting high-correlation documents is an effective pretraining data selection method. We build a new statistical framework for data selection centered around estimates of perplexity-benchmark correlations and perform data selection using a sample of 90 LLMs taken from the Open LLM Leaderboard on texts from tens of thousands of web domains. In controlled pretraining experiments at the 160M parameter scale on 8 benchmarks, our approach outperforms DSIR on every benchmark, while matching the best data selector found in DataComp-LM, a hand-engineered bigram classifier.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new LLM pre-training data selection framework where no LLM training is needed. Their framework leverages publicly accessible pre-trained LLMs and is based on the correlation between downstream benchmark performance and LLMs' losses. In the paper, the authors provide theoretical background for the proposed framework and present experiments where they use 160M parameters models with a 3.2B token budget, comparing DSIR and DataComp-LM data selection. Concretely, they selected data from RedPajamas V2, and used LAMBADA, ARC-E, PIQA, and SciQ as target downstream benchmarks. In their experiments, the proposed method outperforms DSIR and shows competitive performance with DataComp-LM best data selection method.

### Strengths
1. This paper focuses on avoiding costly pre-training ablations for LLM pre-training data selection and proposes a method that leverages public, pre-trained LLMs based on the correlation between downstream performance and perplexity. This aim is quite important for today's LLM practitioners and the proposed framework is very original.  

2. Although limited (see below "weaknesses"), the proposed framework demonstrates promising results compared to baselines. 

3. Although the presentation can be improved, the paper includes a theoretical background for the proposed framework.

### Weaknesses
1. The main weakness of this paper is the scale of the experiments. The paper only includes pre-training experiments using 160M parameters LLM with a 3.2B token budget. This is very small and creates questions about the validity of the results. For example, the smallest scale for DataComp-LM paper is 400M and 8.2B and they experimented with 5 different scales which goes up to 7B parameters model trained on 276B tokens (as DCLM competition scale).

2.  Experiments only include 8 evaluation benchmarks (5 of them are Lambada from different languages). This is a main limitation for both showcasing the validity of results but also limit the understanding how the proposed framework. work when there are many more benchmarks to consider for perplexity validation. Again for comparison, DataComp-LM includes an extended evaluation suite that consists of up to 53 downstream tasks. 

3. If the framework only optimizes data selection per task, is it not expected to have good scores on optimized tasks? Are there any experiments where authors tested aggregating benchmark scores as one overall metric?

### Questions
1. Clarification for Line 201: `select domain greatest to least \gamma, taking all the tokens in each domain once, until we exhaust our total pretraining token budget.`
Does this mean that if a domain with the greatest \gamma includes more tokens than the token budget, only tokens from that domain will be selected?

2. For the proposed perplexity correlation, have you tested aggregating benchmark scores in some way to use as an overall benchmark metric? From Figure 2, I only see LLMs where data selection (ppl correlations) is optimized for each target task.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper analyzes how to select high-quality pretraining data for large language models (LLMs) without training new LLMs. The authors find that LLM losses on certain pretraining texts correlate with downstream benchmark performance. The key idea is to select data domains where lower loss generally corresponds to higher downstream performance.
To do this, the authors use a collection of pre-trained LLMs and measure the log-likelihoods for texts from various domains and the performance of these LLMs on downstream benchmarks. They then calculate the correlation between these two measures for each domain. Domains with high correlations are selected for pretraining.

### Strengths
The paper presents a new and remarkably simple approach to data selection for LLM pretraining. It leverages readily available resources (publicly available LLMs) and a straightforward correlation-based method.  The authors ground their approach in a statistical framework, providing a theoretical basis for their correlation-based data selection. The authors demonstrate the robustness of their approach by showing its effectiveness across various benchmarks and conditions.

### Weaknesses
While the paper presents promising results at the 160M parameter scale, further validation at larger scales is necessary to assess the scalability and effectiveness of the approach for slightly more massive LLMs. The method inherits the biases present in the publicly available LLMs used for estimating correlations. This raises potential concerns about bias amplification, especially if these LLMs were trained on data with inherent biases.

### Questions
- Relevant works that are not cited:

[1] Niklas Muennighoff, Alexander M. Rush, Boaz Barak, Teven Le Scao, Aleksandra Piktus, Nouamane
Tazi, Sampo Pyysalo, Thomas Wolf, and Colin Raffel. Scaling data-constrained language models, 2023

[2] Max Marion, Ahmet Üstün, Luiza Pozzobon, Alex Wang, Marzieh Fadaee, Sara Hooker. When Less is More: Investigating Data Pruning for Pretraining LLMs at Scale, 2023

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors build on a large number of existing open LMs and the observation that perplexity of an LM on a sample of text is predictive of performance on some (presumably related) benchmarks to produce a method for selecting pretraining data, aiming to optmize downstream performance.  The method doesn’t require any training of models. Specifically they greedily sample all available data, without repetition, from each domain in order of correlation until a desired token budget is met. They also filter at the  webpage level using a FastText classifier trained to discriminate the selected and non-selected domains from the previous step.
They apply this set up over:
- 90 models from 33M to 9B parameters from the Open LLM leaderboard, including both intermediate and final checkpoints.
- 4 downstream benchmarks appropriate for small models with an additional 4 evaluations created from one of the benchmarks translated into 4 different languages
- Perplexity evaluations on 9841 internet domains (e.g. wikipedia.org) represented by a sample of 25 web pages each, derived from Common Crawl.
- Sampling training data from a 100B token corpus, derived from Common Crawl
- Pretraining experiments at the 160M parameter 3.2B token (“chinchilla optimal”) comparing their proposed data recipe to baselines including uniform sampling, language filtering, an n-gram overlap method (DSIR; Xie et al., 2023), and a SOTA  handcrafted FastText classifier (Li et al., 2024)

With this set up they find that:
- Their proposed approach performs comparably to the state of the art handcrafted baseline (which was constructed with expensive pretraining experiments not required by this paper’s approach) and outperforms all other baselines.
- Using Spearman rank correlation as opposed to the authors’ proposed correlation measure performs comparably (figure 6, appendix)
- Ablating the webpage-level filtering using the FastText classifier trained on their selected domains, does lower performance (though the difference is smaller when using Spearman rank correlation).

Their method can also be used to predict the ranking of the 90 public models by downstream performance using only domain perplexities. They find:
- A baseline approach that predicts the downstream rank by a model’s rank w.r.t. to  mean loss over domains already gets R^2 values from 75 to 92 (always within 5 points of the proposed approach)
- Testing over all 8 downstream benchmarks, the proposed approach gets a statistically significantly better R^2 with p=0.035, though no individual benchmark is significantly improved.

They also provide an extensive theoretical statistical framework for using a single-index model (SIM) to represent the relationship between domain perplexity and downstream performance. They explain the use of the empirical CDF rather than raw perplexity values to better handle outliers. They also provide an approach to constrain the correlations to be a valid distribution over domains and to respect the limited number of tokens available per domain. However their empirical results “suggest that the performance of [their] approach is not dependent on the precise form of the estimator that is coupled to [their] theory results, but holds broadly across perplexity-correlation relationships” (line 470).

### Strengths
This approach provides a promising way to make use of “the millions of dollars collectively spent” (line 39) on the experimentation represented by all open weight models. The approach extracts information about performant pretraining data selection even when information about the pretraining data of these open-weight models is not available.

Their approach is intuitive and the core of it is quite simple (appearing to be insensitive to the trickier details suggested by theory). This means it should be straightforward for others to apply it.

The authors find that their approach achieves comparable results to a SOTA quality classifier that utilized extensive, costly pretraining experiments, while crucially the authors’ approach requires no new pretraining experiments, unlike other methods..
The paper provides a sound empirical validation of their approach at the 160M parameter scale. They use downstream evaluations that are appropriate for the parameter scale of their experiments (even including some basic multilingual evaluations). When optimizing for a single benchmark, the approach outperforms the state-of-the-art data selection method from DCLM if the latter is handicapped by removing the “manual filtering” step, but not if that manual filtering is included. Their set up demonstrates the utility of their approach for data with a very large number of domains (far greater than can be optimized with brute force pretraining experiments). These results should be more than enough to motivate further exploration of this technique at larger scales.

I appreciated the additional analysis of outliers where the approach doesn’t do so well at predicting relative performance.  The observation that models with “unusual” data mixtures is interesting and will be useful in future work in this space.

### Weaknesses
I think the biggest weakness is that the paper’s method targets a single benchmark.  Are there obvious ways to extend the work to target some aggregation of benchmark scores?  Sure, but the paper offers no theory to suggest how we might do that, and no experiments to show whether the obvious ways of doing that would work.
Lambada, which accounts for 5 out of 8 of downstream evaluations, is a language modeling task (i.e. next word prediction) just like the perplexity measures being used as proxies in the proposed approach. This may somewhat obscure whether the proposed approach works as well for all kinds of downstream tasks which typically are not language modeling tasks. That said, the other 3 non-lambada tasks do also benefit from the proposed approach.
It is unclear in the empirical results of the paper what parts of the theoretical results are actually necessary for the evident success of the authors’ approach. The results in Appendix G do not conclusively favor the author’s proposed correlation measure nor their projection method. While the authors do say so themselves (line 467), it would be kinder to the reader to let the reader know this before they have waded through the dense theoretical sections of the paper. 
The presentation of the paper also makes it unclear what theoretical results are necessary as the discussion of theory and methods are quite entangled. The paper would be much more readable if there was a simple discussion of what the proposed approach does and then only after that provide theoretical arguments for why this approach is used. I believe Algorithm 1 in the appendix provides the clearest end-to-end description of what exactly the proposed approach is. But even there I am left uncertain of details not mentioned there such as the theta projection or the use of empirical CDF. Is theta projection always used for the greedy data selection, or can the raw gamma values be used without projection since all you need is the order of the domains by the correlation?
I believe the experiments work only at the internet domain granularity for selection.  The paper actually says very little about what a “domain” is – it seems to follow from variables defined in the redpajama data, and there are around 9000 “domains,” so the problem is of interesting size.  But I didn’t come away with a strong sense that – beyond empirical reports – there really should be a relationship between these particular “domains” and model performance on the benchmarks.  The paper would be stronger with some discussion of the qualitative assumptions that lead us to believe perplexity on specific slices of pretraining data (whether defined by internet domains or some other attributes) should be predictive of task performance. Are those assumptions grounded in any prior work?  Are they pervasive?  Are they novel?

The largest model on which the method is tested is only 160M parameters; it’s not clear whether the method will scale.  (I have no reason to believe it won’t, or that it will.)  This scale of model also implies a choice of target benchmarks that deviates pretty far from metrics most builders of language models would care about; I understand that the experiments needed to use benchmarks that would show meaningful differences at the 160M scale, but this creates even more distance between what the paper shows and what is needed in practical settings.

Apart from the most obvious case (based on language ID), the paper really doesn’t delve into what the predictive model itself tells us about the relationship between pretraining data composition and the benchmarks.  This is in part due to the unexciting set of benchmarks, I think.

### Questions
1. It seems that factors such as benchmark contamination or formatting overlap between pretraining data and perplexity validation data could alter the relationship between domain perplexity and downstream performance for some observed models. This would introduce more structured noise than simple run-to-run variance due to differing training seeds. In the observed data do correlations vary dramatically for any subsets of models (i.e. are there subsets of models perhaps with systematically biased perplexity to downstream correlations)? Does your approach mitigate this possibility in any way other than by accumulating enough diverse observations that it’s unlikely a substantial number of models will be affected by the same biases?
2. Is the projection method used in algorithm 1 when selecting data or only when predicting downstream performance ranking? Figure 6 implies that the data selection is different when using different projection methods but algorithm 1 doesn’t mention the projection step. 
3.  What does “features” refer to on line 344?
4. Line 460: what is meant by “​​significant enrichment of the corresponding languages”
5. Since the domain perplexities are measured over samples of 25 webpages, do the number of tokens used to estimate perplexity vary considerably from domain to domain? This may add noise to your perplexity estimates proportional to how severely some domains are subsetted with respect to tokens as observed by https://arxiv.org/abs/2312.10523 in their subsampling guideline.
6. How are the standard deviations computed for the figure 4 ranking plots?

Other comments (not questions and no response needed; wasn't sure where to put them):

The paper grounds the method in some theory by relating it to estimators for single index models.  This is not extremely important from my point of view, because the method is fairly intuitive, but it may give further intuition or justification to some readers.  The value may be in revealing the assumptions made by the model (through the lens of statistical estimation), so that they can be revised in future explorations.  I thought the discussion of the projections (4.2.3) was mostly unnecessary; I would have rather seen the experimental comparison of the different variants reported in the main paper and the derivations in the appendix, rather than the reverse.

Suggestions (no response needed):

It would be interesting to see more analysis of specifically what domains are selected by the proposed approach contrasted with other baselines. Likewise how do the domains selected differ for different target downstream benchmarks (other than in terms of language)? Also are the most correlated domains also domains with few or many tokens? That is, does the final data selection only include a small subset of the positive correlation domains before satisfying the token budget or are many smaller domains selected?

Line 93: There is some work which uses pretraining experiments to explore high dimensional mixtures of pretraining data (https://arxiv.org/abs/2410.15661).

Line 97: There is work that directly shows the relationship between loss to downstream performance (https://arxiv.org/abs/2403.08540), though this work does not propose a data selection method.

In line 125 and 128 j switches from indexing documents and domains. Maybe use different indices to make this clearer.

On line 208 and 337 “single-page level” was confusing to me until I recalled that you are working with purely webtext and thus documents are webpages. It would be best to define this term before use to avoid possible confusion with other meanings of the word page.

Line 458: avoid use of “significantly” when not discussing statistical significance.

Line 526: “usual” should be “unusual” here, right?

In 4.2.1, I think the epsilons, not x, should be drawn from a standard normal.

Figure 2 doesn’t clearly label methods the way they are referred to in the text.  It would be helpful to clearly mark, for example, the state-of-the-art methods from the DCLM paper as such and “our” methods (those introduced in this paper).

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
This paper proposes a new framework for pre-training data selection by leveraging large amounts of open-weight language models.  Concretely, a data domain is selected for pre-training when open-weight LLMs’ log probabilities on this domain highly correlate with performance on a target downstream task. The higher correlation a data domain demonstrates, the more weight the domain occupies the pre-training data. The proposed data selection algorithm is evaluated with small models of 160M parameters trained on a data scale of 3.2B tokens. Experimental results show that the proposed data selection algorithm, without relying on hand-crafted heuristics and expensive model training runs, approximately matches the handcrafted fastText baseline.

### Strengths
- This paper proposes a new framework for pre-training data selection without extensive manual labor by leveraging large amounts of pre-trained open-weight models.
- The results validated on small 160M parameter models look promising.
- The studied topic is important and relevant to many language model practitioners.

### Weaknesses
 - It is unclear how well the proposed framework works for larger scale pre-training where multiple static benchmarks should be considered, and when the model size can be larger than the maximum model size (~8B) used for computing perplexity-benchmark correlation.
- The theory section is a bit difficult to follow. In the paragraph above section 5.2 "*This suggests that the performance of our approach is not dependent on the precise form of the estimator that is coupled to our theory results, but holds broadly across perplexity-correlation relationships.*" If the theoretical result is less universal than empirical observation, it can be interesting to add more discussion on the more general relationship.
- The proposed model provides the ordering of pre-training domains, however, from what I understand, the sampling ratio across domains is not determined by the benchmark-perplexity correlation, but rather “*select domains in greatest to least γ, taking all the tokens in each domain once, until we exhaust our total pretraining token budget.*” The discussion about the exact ratio to mix various domains is a little limited.

### Questions
- How can the proposed method be extended to selecting data for multiple downstream tasks, including unseen and/or dynamic benchmarks?
- Will the data domains selected using models of a certain scale (e.g., < 8B) be helpful for training larger models (e.g., 70B)?  
- How would varying the token ratio of pre-training domains affect the downstream performance? That is, mixing domains beyond "selecting all the tokens in each domain once" until token budget is exhausted.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel approach to data selection for pretraining large language models (LLMs) using perplexity correlations. This work is based on a simple observation: LLM losses on many pretraining texts are correlated with downstream benchmark
performance, and selecting high-correlation documents is an effective pertaining data selection method. This approach is compute efficient and has competitive performance.

### Strengths
1. Using perplexity correlations for data selection is well-motivated and easy to implement.

2. The paper provides a solid theoretical foundation for the proposed method, including a detailed discussion of the single-index model and the estimation of correlation coefficients. The mathematical derivations and proofs are rigorous and well-presented.

3. In experiments, authors demonstrate that their method outperforms existing data selection techniques in terms of downstream benchmark performance.

### Weaknesses
1. While the paper demonstrates the effectiveness of the approach at the 160M parameter scale (though the data selection parameters are generated with LLM of 7B),  how the method would scale to larger models' pertaining remains unclear. The extrapolation from smaller models to larger ones could be a potential limitation.


### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2
