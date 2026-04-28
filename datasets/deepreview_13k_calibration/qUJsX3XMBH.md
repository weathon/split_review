# Rethinking Data Selection at Scale: Random Selection is Almost All You Need

- Decision: Reject
- Avg Score: 4.40
- Scores: 6, 3, 5, 5, 3

## Abstract
Supervised fine-tuning (SFT) is crucial for aligning Large Language Models (LLMs) with human instructions. The primary goal during SFT is to select a small yet representative subset of training data from the larger pool, such that fine-tuning with this subset achieves results comparable to or even exceeding those obtained using the entire dataset. However, most existing data selection techniques are designed for small-scale data pools, which fail to meet the demands of real-world SFT scenarios. In this paper, we replicated several self-scoring methods—those that do not rely on external model assistance—on two million-scale datasets, and found that nearly all methods struggled to significantly outperform random selection when dealing with such large-scale data pools. Moreover, our comparisons suggest that, during SFT, diversity in data selection is more critical than simply focusing on high-quality data. We also analyzed the limitations of several current approaches, explaining why they perform poorly on large-scale datasets and why they are unsuitable for such contexts. Finally, we found that filtering data by token length offers a stable and efficient method for improving results. This approach, particularly when training on long-text data, proves highly beneficial for relatively weaker base models, such as Llama3.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper authors proposed a data filtration technique for the SFT (supervised fine-tuning phase) of LLM training.
Rigorously testing existing SOTA methods that were proven to work on the small scale datasets, authors found that 
filtering data by token length offers an efficient way for improving downstream results further. In addition to that authors demonstrated that SOTA methods fall short in quality when handling large-scale 1T datasets. Authors demonstrated that data diversity plays the most important role in the SFT phase, thus quality filtering is suboptimal.

### Strengths
Constructing a high-quality multi-corpora dataset that is useful for training LLMs is a hard and important task. Input data is crucial for making a high-quality reliable and safe LLM at scale. Authors explore the topic of improving the dataset construction process and suggest a simplified framework that does not require rigorous data cleaning at scale. Considering that developing and using filtration techniques at scale might present computational challenges, this paper makes a significant contribution to the field with their simplified proposal.

### Weaknesses
One of the challenges with assessing the quality of LLMs is the quality and generalizability of the downstream tasks. Majority of the times that amount of the overlap between training and downstream data can cause skewed assessments in the quality of data processing techniques. I could not find any statistics reported by the authors for the amount of the overlap present in their training corpuses and the downstream tasks. It is important to understand that before drawing any conclusions with regards to the data filtration techniques. 
It might be the case that some of the filtration strategies are heavily biased towards the examples present in the downstream tasks, and not necessarily improve model's generazability qualities.

### Questions
I would like to see the stats on the overlap present in the tokens from your SFT datasets and downstream tasks. It would also be useful to know whether any deduplication method was applied on top of the SFT datasets to eliminate the effect of model's memorization.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the effectiveness of data selection methods for supervised fine-tuning (SFT) of Large Language Models (LLMs) at scale. Through extensive experimentation on million-scale datasets, the research reveals that most existing self-scoring data selection methods, which don't require external model assistance, fail to significantly outperform random selection when applied to large-scale data pools.

### Strengths
1. This paper studies an interesting yet important task of selecting training data for supervised fine-tuning (SFT) in large language models.

2. The experimental results reveal that various data selection methods struggle to significantly outperform random selection, a finding that will likely be beneficial to practitioners.

### Weaknesses
1. Some of the conclusions presented are already established in existing literature. For instance, paper [1] has previously demonstrated the importance of data diversity in SFT data selection with large-scale datasets, while paper [2] has shown the effectiveness of selecting longer answers for data selection. It appears the authors overlooked these references, which limits the novelty and contribution of this work.

2. Although the paper identifies that certain data selection methods fail to outperform random selection, it lacks a thorough analysis—either theoretical or empirical—explaining why these approaches underperform. This absence of deeper exploration reduces the overall depth and insight provided by the study, which is required by top-tier ML conferences.

3. The paper does not provide a clear definition of what is an "extensive SFT dataset." In practical applications, it remains unclear how to determine whether a dataset qualifies as "extensive," which could lead to ambiguity in interpreting the paper's findings and recommendations.

### Questions
See above.

### Soundness
2

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
This paper studies the efficacy of various data filtering strategies when applied to large-scale SFT datasets (i.e.., OpenHermes2.5, WildChat). While these same strategies often outperform random selection on smaller-scale SFT datasets they are shown to be surprisingly  less impactful when applied to these larger-scale (state-of-the-art) open-source datasets. On these datasets, approaches that target diversity seem to be more effective than those that target quality. Finally, the authors test their own length-based filtering strategy, which outperforms the other methods when the base model is Llama3-8B.

### Strengths
**Originality and Significance.** This paper performs a valuable and novel (to the best of my knowledge) empirical study to see whether existing SFT data selection methods remain effective when applied on larger SFT datasets. Because these larger SFT datasets are generally better than the smaller datasets these methods were previously tested on, it is important to see whether filtering works in this more state of the art regime. The main findings that (i) many of these methods no longer are as impactful; (ii) diversity is more important than quality-filtering are therefore quite significant and potentially highly-relevant to future SFT data curation efforts.

**Quality.** This paper implements a good number of baselines and also is thorough about trying multiple base models and dataset sizes (post data selection). These variations are nice to test the robustness of the main takeaways.

**Clarity.** Overall, most of the paper is easy to follow with the exception of the description of baseline methods (see W3).

### Weaknesses
 **(W1) Isolating dataset size.** A central claim in the paper is that dataset size is what causes differences in the behavior of the baselines. However, there are also other differences between OH2.5/WildChat and older datasets besides data quantity; e.g., quality-based selection may be less impactful simply because these larger datasets are already the result of more careful curation and thus higher-quality compared to older ones. An experiment that would better isolate data quantity (and control for quality) would be to run the existing experiments on progressively smaller random subsets of OH2.5/WildChat (e.g., what happens when the starting pool is 10K/100K examples of OH2.5 v.s. 1M?). The current experiments do not sufficiently address whether the observed changes are due to scale alone or other factors such as the higher quality or diversity of the larger datasets. For example, even when the starting pool is reduced to 100K, the quality-based methods still do not show the same gains as they do on older, smaller datasets, suggesting that scale is not the only factor at play. It would be valuable to see if the selection methods stop working on a large but lower-quality dataset to further support the claims about scale. 

**(W2) Understanding run-to-run variance / Fairness of comparison to random.** The stated takeaway from the results is that *"it is more efficient to randomly select training data...random selection reduces costs and yields superior training results"* but I don't know if that's fully borne out by the results.
- For the Qwen2 results (which achieve highest overall perforamnce), in the 50K regime, the best average results are achieved by non-random curation methods (Diverse and ZIP each score 1% higher than the max over the random runs in Tables 5 and 6 respectively). In the 10K regime, this is also almost true with the exception of 1/5 of the random runs.
- In general, I'm not sure its fair to compare the max over 5 random runs to a single run of a selection method. if only 1 of 5 runs ends up doing better, then in practice you'd likely have to try multiple times when randomly sampling a subset that outperforms non-random selection, increasing costs. 
- Ideally, it would be nice to show the average and stdev across the 5 random runs and to also get a sense of run-to-run variation for the non-random methods (though I acknowledge this might be costly). The additional context about compute costs and p-values is helpful, but it also seems that most selection methods take at least as long as simply training on all 1M examples, which would be more effective for improving performance in most cases. This seems like an important failure of these selection strategies that should be emphasized.

**(W3) Clarity when describing existing methods.** I currently found Sec 3. a bit hard to follow. It may be helpful to define up front unified notation for variables that appear in multiple methods instead of using the differing notation from each of the original papers (e.g. whether a sample is given by $z$ or $x$ or $n$). Also, in some places, symbols are currently used without an explicit definition (e.g. $\hat{\Gamma}$ in LESS, $\mathcal{C}$ in ZIP). 

**Miscellaneous Notes**
- In captions for Tables 1 and 2, "the suboptimal score" is confusing terminology, I believe you meant "second highest score"? 
- Given that originally LESS is a targeted selection method, I'm not sure it's completely aligned with the spirit of the original method to set the target as a subset of the overall data pool? I suspect what might be leading to bad performance is that this may actually result in selecting a less diverse dataset (by prioritizing examples that represent the majority).

### Questions
(Q1) Could you share more details about Figure 1, given that the difference between small/large regimes is a key aspect of the paper? In particular, which datasets were used for the 10K-300K scale in Figure 1? Are these already random subsets of OH2.5/WildChat (basically what i suggested in W1) or are they some other datasets (e.g. Dolly, ShareGPT)?

(Q2) What is the cost of the fine-tuning runs in your experiment setup? It would be helpful to know this relative to the costs of running the various data curation algorithms (when discussing them in 5.3).

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors study the effectiveness of data selection methods on large-scale datasets, which is largely unexplored. With experiments on large-scale datasets, the authors find that nearly existing data selection methods do not significantly outperform random selection on large-scale datasets. This paper also tries to explain the reason that leads to inferior performance of existing methods on a larger data pool. Ultimately, the authors propose a more effective data selection method based on token length. This paper offers researchers a new perspective on data selection in large language models.

### Strengths
The authors study the effectiveness of data selection methods on large-scale datasets, and find the inferior performance of existing methods when dealing with large-scale data pools. At the same time,  the authors try to analyze the reason that leads to inferior performance of existing methods on a larger data pool.

### Weaknesses
1. **Title Reflecting Content**: The title of this paper suggests that ”random
selection is almost all you need”, while results show that the diversity-based
selection method achieves superior performance with an average score of
59.58 under Qwen2-7B in Table 1. The result does not indicate that random
selection is a better method. In this paper, it seems to show that
diversity plays an important role in data selection for large-scale datasets. A more representative title improves clarity
and helps set readers’ expectations.

2. **Insufficient experiments**: This paper’s results show that existing data
selection methods do not significantly outperform random selection on large-scale datasets. However, the authors only perform experiments on two models. Are there similar outcomes for different LLMs (e.g., different-sized models)?

### Questions
**Questions**: This paper proposes a data selection method by token
length to achieve optimal results. However, as shown in Table 3, does the Qwen2-7B model not get better results with this method compared with
existing methods? By the way, why is this selection method beneficial? In
other words, what is the motivation for this approach? Moreover, what
does it mean to ”reduce the uncertainty caused by randomness”?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates supervised fine-tuning (SFT) for large language models (LLMs), specifically focusing on selecting a representative subset of training data that performs as well as or better than using the full dataset. It reveals that existing data selection methods, particularly self-scoring techniques, struggle to outperform random selection on million-scale datasets and highlights the importance of diversity over mere data quality in large-scale scenarios. Additionally, the authors find that filtering data by token length enhances SFT, especially for weaker base models like Llama3, offering a stable and efficient improvement method.

### Strengths
The finding that "Most self-scoring data selection techniques do not significantly outperform random selection on large-scale datasets" could contribute novel insights to the community.

### Weaknesses
 - The motivation for this research is unclear. The authors claim that "This discrepancy creates a gap between the present SFT data selection strategies and real-world applications," yet it remains unclear what these real-world applications are. Specifically, the paper does not articulate why existing data selection methods, which may work well on smaller datasets, fail to scale to the million-scale datasets used in practical applications. The authors should elaborate on the specific challenges that arise when scaling up data selection, such as computational costs, data heterogeneity, and the diminishing returns of sophisticated selection algorithms.

- Finding 2, namely, "Data quality-based selection methods are more effective than data diversity-based methods when dealing with a small-scale dataset from a single source," is interesting, but exploring why this discrepancy occurs would be more valuable. The paper should delve into the underlying reasons for this behavior. For example, do small, single-source datasets lack the diversity required for diversity-based methods to be effective? Or do quality-based methods simply overfit to the specific characteristics of such datasets? A more detailed analysis of the data characteristics and the behavior of different selection methods is needed.

- Finding 3, that "token length could be used for data filtering," does not fit well within the overall narrative. In general, while the paper presents three findings, they are neither well-motivated nor well-connected. As an exploratory paper, its contribution feels limited. The connection between token length and model performance, especially for weaker models, is not sufficiently explained. The paper should provide a more detailed analysis of why longer texts might be more beneficial for weaker models, perhaps relating it to the amount of information or the complexity of the training signal.

- When using the term “significantly better,” please provide a p-value to substantiate the statistical significance of the results.

- Clarification:

  - The introduction should clarify what “scoring” means in this context and better motivate the need for scoring. Additionally, for the self-scoring approaches, the authors further categorise their techniques into two types: data quality-based methods and data diversity-based methods, but this distinction needs clearer explanation in the context.

    Although further detail is provided in Section 3, the introduction is challenging to follow.

  - In Figure 1, "BBH benchmark" requires a reference.

  - Line 58: "in practical applications" needs clarification.

- Typos:

  - Line 39: missing a space before the citation.
  - Table 1: some of the best numbers are not in bold.
  - Line 324: missing a space before the bracket.

### Questions
- What real-world applications could benefit from the outcomes of this research?
- What is the difference between data quality-based methods and data diversity-based approaches?
- Why is utilising token length in SFT beneficial for weaker base language models, like Llama3-8B?

### Soundness
2

### Presentation
2

### Contribution
2
