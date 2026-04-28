# Perplexed by Perplexity: Perplexity-Based Data Pruning With Small Reference Models

- Decision: Accept
- Avg Score: 5.75
- Scores: 8, 6, 3, 6

## Abstract
In this work, we investigate whether small language models can determine high-quality subsets of large-scale text datasets that improve the performance of larger language models.
While existing work has shown that pruning based on the perplexity of a larger model can yield high-quality data, we investigate whether smaller models can be used for perplexity-based pruning and how pruning is affected by the domain composition of the data being pruned.
We demonstrate that for multiple dataset compositions, perplexity-based pruning of pretraining data can \emph{significantly} improve downstream task performance: pruning based on perplexities computed with a 125 million parameter model improves the average performance on downstream tasks of a 3 billion parameter model by up to 2.04 and achieves up to a $1.45\times$ reduction in pretraining steps to reach commensurate baseline performance.
Furthermore, we demonstrate that such perplexity-based data pruning also yields downstream performance gains in the over-trained and data-constrained regimes.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes that smaller language models effectively prune large datasets in a way that benefits the training of much larger model. Applying perplexity-based pruning techniques, they explore using a small model to filter high-quality subsets of data for training larger models. This approach is interesting because it’s a cost-effective alternative to using large models for pruning, and is applicable in real settings. The findings indicate benefits for downstream accuracy and training efficiency.

The paper demonstrates that a 125m parameter model can successfully prune data for large models and improve downstream task performance. The paper shows empirical results testing on The Pile and Dolma, two datasets with very different domain structures.
They also study the two settings of over-training and data-constrained setups and provide additional insights.

### Strengths
The goal, and the process, and algorithm are defined and presented very clearly. Experiments cover multiple settings, with different model sizes and training algorithms. 
The proposed method is super useful for researchers who investigate practical techniques for data curation, with insightful empirical results. 
Experiments include two very different dataset distributions, the Pile dataset and Dolma. The work shows thorough experiments for various selection rates and perplexity criteria, presenting strong evidence about settings in which perplexity pruning does and does not work.

### Weaknesses
Authors claim that datasets pruning increases the proportion of general domain data from web-scraped domains, and decreases the proportion of specific and technical domains. But it is unclear and counter intuitive why training on general domain data improves performance of models on benchmarks. I think the paper lacks analysis to explain this observation. Specifically, the paper does not address the potential for a shift in the distribution of the training data to negatively impact performance on tasks that rely on the pruned domains. For example, if code-related data is significantly reduced, the model's ability to perform well on coding benchmarks might be compromised. The paper needs to provide a more thorough investigation into the trade-offs between improved performance on general benchmarks and potential degradation on specialized tasks. It is also unclear how the perplexity pruning method might interact with different types of data within the same domain. For example, within the 'web-scraped' domain, there could be a significant difference between high-quality articles and low-quality forum posts, and the paper does not address whether the pruning method is able to distinguish between these.

### Questions
How do you expect the results to scale on models larger than 3B parameters? 

How does models' performance change on domains which are pruned the most?

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
4

### Summary
This paper presents a perplexity-based pruning method for reducing the size of pre-training datasets. The effect of pruning is evaluated through the performance on downstream tasks as well. Two datasets are used for evaluation: Pile and Dogma. The pruning efficacy is determined for over-trained and data-constrained regimes as well.

### Strengths
- The paper addresses an important problem of pruning the pre-training datasets to enable efficient training of LLMs.
- The experiments are thorough and cover different dimensions of perplexity-based pruning. 
- The paper is well-written and the results are presented clearly. 
-  The findings are significant, as they show that perplexity-based data filtering can not only reduce the size of the pre-training datasets, it also leads to better performance on certain downstream tasks.

### Weaknesses
 - The paper does not currently cover the computational complexity of the proposed pruning procedure. A few important questions that need to be considered in this regard:
    - How do the computational requirements for perplexity-based pruning increase with the size of the dataset to be pruned?
    - How does the cost of computing perplexity (before pruning) amortize over the efficiency improvements achieved while pretraining the model on the pruned datasets?
- A discussion for choosing the right perplexity pruning method (low, medium, high) for the dataset should be included for the practitioners. From the experimental results, we can see that high perplexity selection performs better on Pile while medium perplexity selection is better for dolma. Can we extract any patterns from these results and other experiments that can be generalized to other datasets?
    - For example, prior theory on data pruning for vision tasks shows that the optimal pruning strategy changes depending on the amount of initial data. When data is abundant, the better pruning strategy is to keep harder examples. In contrast, for smaller datasets, keeping the easier examples leads to better performance. [1]
- The results show that test set perplexity may not always be a sound metric for evaluating a pruning strategy and that downstream evaluation is necessary. What should be the cheapest way of conducting the downstream evaluation of the correct perplexity pruning method, i.e., the one that can yield reliable results at a minimal cost? For example, could there be a small set of representative downstream tasks or metrics that could serve as efficient proxies for full downstream evaluation?
- A quantized model may lead to better inference efficiency while calculating the perplexity. Was this considered while running the experiments?
- High perplexity selection will also inevitably lead to the inclusion of a significant portion of the noisier examples in the overall dataset. How can we determine the proportion of such examples in the final dataset and exclude them reliably?
- Minor typo (line 66): perplexity-basd -> perplexity-based
- It would be useful to include the following closely related data pruning works in the related work section:
    - https://arxiv.org/abs/2403.07384
    - https://arxiv.org/abs/2402.09668

### Questions
- A quantized model may lead to better inference efficiency while calculating the perplexity. Was this considered while running the experiments?
- High perplexity selection will also inevitably lead to the inclusion of a significant portion of the noisier examples in the overall dataset. How can we determine the proportion of such examples in the final dataset and exclude them reliably?
- Minor typo (line 66): perplexity-basd -> perplexity-based
- It would be useful to include the following closely related data pruning works in the related work section:
    - https://arxiv.org/abs/2403.07384
    - https://arxiv.org/abs/2402.09668

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors filter LLM pre-training data by using the perplexity of a smaller language model. They demonstrate that dataset filtering improves the [initial] learning curve of LLM pre-training.

### Strengths
The method is well motivated. Except for some uncommon terminology that is explained in later sections like "non-standard training regime", "over-training" (which is not over-fitting) the paper is clearly written.

### Weaknesses
L186 suggests that the final models are (pre-)trained for a fixed number of steps, no matter the dataset size. This sets the stage for dataset filtering, since training on the full dataset may go through fewer epochs. It would be interesting to train for long enough to show convergence in the plots in Fig. 1.  The story would be more convincing if there is an offset between the blue and red curves even after convergence. In fact, the "over-training" experiment in Sec. 3.4 shows diminishing gains, so I can imagine that they disappear fully at some point. The method would still have merits (steeper pre-training curve), just not the ones claimed in the paper.

Novelty. Perplexity-based pruning and countless variations of it are well-studied. The authors set their work apart from prior work in L058, but neither of the arguments (i)-(iii) (evaluation on downstream task, exploration of domain compositions, "non-standard" evaluation regimes) strike me as particularly strong. The claim that evaluating on downstream tasks is novel is particularly weak, as this is standard practice in the field. The exploration of domain compositions is a valid point, but the paper doesn't sufficiently explore the interaction between perplexity-based pruning and different domain mixtures. The "non-standard" evaluation regimes are interesting, but the results in these regimes are not sufficiently compelling to justify the claim of novelty.

I don't think that Algorithm 1 is really helping clarity. 1-2 normal equations would be just as expressive and more concise.

### Questions
- Fig.4 is interesting, but I'm not sure how Fig. 3 is relevant in practice - could you clarify?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper investigates whether a small model can be used to perform perplexity based data selection for a larger model. The key findings are that 1) a reference model with 30x fewer parameters compared to the larger model can be used to identify a subset of the training data which can improve the performance of the larger model relative to no pruning. 2) the filtered data subset can speed up training of the larger model, 2) the improvements carry over to some extent to over training and data constrained regimes, 3) ideal pruning criteria can vary by dataset e.g. for Pile, a high perplexity subset performs better while for Dolma, a medium perplexity subset works the best. The paper shows that test data perplexity is not a good indicator of the downstream task performance when using perplexity based pruning.

### Strengths
* Describes a simple approach to improve the performance of large language models using perplexity based data filtration using a smaller reference model.
* Presents useful results e.g. 1) filtration criteria varies by dataset type and 2) test set perplexity is not a good indicator of the downstream task performance.

### Weaknesses
 * The main results (Table 1) do not include a random baseline i.e. what is the performance of a model trained on a subset of the data which has a similar size as the perplexity filtered buckets but is selected randomly?
* The paper does not contain ablations on the size of the reference model and sensitivity of the results to the random split (L113) used for training the reference model. Though exploring this space is computationally expensive, it may be useful to present 1-2 additional data points.
* It would be good to see some additional analysis to understand why a high perplexity set works better for one domain while a medium perplexity set works better for others.

Note: The authors have addressed some of these concerns (random baseline/sensitivity to random split) in  the rebuttal.

### Questions
* L290: "These results show that while the higher quality data resulting from perplexity-based data pruning does still lead to an improvement in downstream performance in the over-trained regime, there is not a relative increase in downstream improvement over the baseline when over-training." It would be good to understand why this is the case since there are no repeats. 
* L314: "That training on repeated perplexity-pruned data leads to diminishing gains after four repetitions post- pruning suggests that the higher quality data resulting from pruning does not change the point for which repeating data yields diminishing improvements in performance." This sentence is confusing and should be reworded.
* In section 4.2, the paper presents results showing that the pruning affects data composition such that some domains (e.g. web) are oversampled compared to others (e.g. pubmed). It would be useful to perform additional analysis to understand why this is the case e.g. is it possible that the training split (L113) resulted in a smaller proportion of these domains for the reference dataset?

### Soundness
3

### Presentation
3

### Contribution
3
