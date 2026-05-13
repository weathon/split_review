# The Best of Both Worlds: Bridging Quality and Diversity in Data Selection with Bipartite Graph

- Decision: Reject
- Scores: 6, 6, 6

## Abstract
The performance of large language models (LLMs) in natural language processing (NLP) tasks is significantly influenced by the quality and diversity of data used for supervised fine-tuning (SFT). Current data selection methods often focus solely on quality or diversity, leading to underperforming models due to suboptimal training data. In this paper, we introduce GraphFilter, a novel method that represents the dataset as a bipartite graph, linking sentences to their constituent n-grams. This representation effectively captures the relationships between sentences and linguistic patterns, facilitating the selection of sentences that enhance n-gram diversity. To balance quality and diversity during selection, we propose a priority function that combines the quality metric with the diversity metric in a multiplicative manner. GraphFilter iteratively selects high-priority sentences, updates the bipartite graph by removing covered n-grams, and re-calculates priorities to reflect the evolving data landscape. We conduct extensive experiments using three model backbones across six widely used benchmarks. The results demonstrate that GraphFilter outperforms all nine baseline approaches, achieving superior model performance and computational efficiency. Our analyses validate the effectiveness of our design choices, examine the subsets selected by GraphFilter and other methods, highlight the importance of instruction diversity, and explore the role of quality and diversity in relation to subset sizes. GraphFilter establishes a new foundation for effective data selection strategies, encouraging further research in data selection for LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a simple yet effective method named 'GraphFilter' to efficiently select SFT data with possible CPU-only computation. GraphFilter represents a dataset as a bipartite graph connecting sentences to their n-grams, allowing it to balance the quality and diversity sentences that maximise n-gram diversity. 

The paper also designs a priority function to combine quality and diversity in a multiplicative manner. The method iteratively selects high-priority sentences, updates the graph by removing covered n-grams, and recalculates priorities to adapt to the evolving dataset structure. 

Experiments across three model backbones and six benchmarks demonstrate that the proposed method outperforms nine baselines in both model performance and computational efficiency. Further analysis validates the method's effectiveness and highlights the importance of balancing instruction diversity with data quality for effective model fine-tuning.

### Strengths
* **Significance**: The paper targets an important problem in LLM SFT, which is how to select the training data.

* **Originality**: The paper proposes an efficient and effective method to select high quality and diversity data by designing a priority score and a bipartite graph representation for the dataset.

* **Clarity**: The paper adopts various datasets and baselines. The effectiveness of the proposed method is supported by comprehensive experiments and sound ablation study. 

* **Quality**: The paper is well-written. The presentation is clear and the graphs and tables are well-organised.

### Weaknesses
 * The Related Work for data selection could be enriched. The paper may explain more the limitations of the current methods and why it is important to address these limitations. In addition, methods like S2L [1] and DiverseEvol [2], although focusing on SFT a specific task, should also be added and discussed. Otherwise, the claim for solving SFT data selection problem should be narrowed down.


* The paper divides the existing methods into two categories:  quality-focused and diversity-focused. However, they always consider other different criteria or have different explanation of quality, for example, verbosity, complexity, and helpfulness to a specific task [3,4]. The paper should also discuss why the perplexity-based score is enough to capture the quality of the data.


* In the bipartite graph, the n-gram nodes are only visited once, and the edges and nodes are removed after being visited. It indeed accelerates the data selection process and enables the method to visit as many n-grams as possible given limited budget. However, the data needed to learn a certain knowledge or gain a certain capability may not be the same. The concern is that the model may not learn well on specific tasks, as supported that in the main results the method proposed does not perform the best in all tasks.


* In Section 5.3, the paper performs a comprehensive ablation study on applying GRAPHFILTER to instructions or responses. It is notable that SOTA methods like DEITA and ARMORM are applied both on instructions and responses, while the performance for the proposed method fails to outperform SOTA methods when applied to both instructions and responses.

### Questions
* Related Work like DEITA considered three dimensions: complexity, quality and diversity. DEITA tries to maintain complexity and diversity while selecting high quality data first. It would be interesting to compare the in Section 5.2 to see the improvement of GraphFilter from DEITA’s data selection.


* It is interesting to see how the performance will change if the n-gram nodes can be visited multiple times, since different task or knowledge may need different amount of training data.


* It would be interesting if the paper can try to apply SOTA methods only on instructions and do some evaluation.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents GRAPHFILTER, a novel method for selecting high-quality and diverse subsets of data for supervised fine-tuning (SFT) of large language models (LLMs). The method represents the dataset as a bipartite graph, linking sentences to n-grams, allowing for an efficient selection process that enhances both quality and diversity. Key contributions include:

* Bipartite Graph Model: GRAPHFILTER models sentences and n-grams as nodes in a bipartite graph, capturing n-gram diversity and allowing for efficient sentence selection.
* Priority Function for Quality and Diversity: A priority function that combines quality (measured by SUPERFILTER) and diversity (via TF-IDF for n-grams) guides the sentence selection process, ensuring a balanced and high-value subset.
* Extensive Benchmarking: Experiments on three model backbones and six benchmarks show that GRAPHFILTER outperforms nine other data selection methods, achieving better model performance and computational efficiency.

The paper demonstrates the effectiveness of GRAPHFILTER, providing insights into the selected subsets' characteristics and highlighting the importance of instruction diversity for model training

### Strengths
Originality

The originality of GRAPHFILTER lies in its approach to data selection for supervised fine-tuning (SFT) of large language models (LLMs). Unlike prior methods that treat quality and diversity as separate concerns, GRAPHFILTER integrates both dimensions by representing the dataset as a bipartite graph connecting sentences and n-grams. This graph structure is a novel way to capture linguistic diversity at the n-gram level while the priority function effectively balances quality and diversity within the selection process. Using a bipartite graph to represent sentence-n-gram relationships is a creative approach, setting the paper apart from conventional selection techniques that use heuristics or embeddings alone. Additionally, including a priority function that combines quality metrics like SUPERFILTER with TF-IDF for diversity provides a unique, data-driven selection mechanism that ensures relevance and informativeness of the chosen data.

Quality

The quality of the research is high, demonstrated by a thorough methodology and comprehensive experimentation. The bipartite graph model and priority function are clearly defined and logically justified, and the selection process is detailed in both algorithmic form and example illustrations. The extensive experiments cover three different model architectures and six popular benchmarks, ensuring a broad and robust evaluation. Including nine baseline approaches provides a clear and rigorous comparison highlighting GRAPHFILTER’s advantages across multiple configurations. The authors further validate the effectiveness of their design choices through ablation studies, examining how different n-gram combinations and priority functions impact performance, which adds to the paper’s methodological robustness.

Clarity

The paper is well-organized and communicates complex ideas effectively. Each approach component—dataset representation, quality and diversity metrics, and the iterative selection process—is clearly explained with diagrams and examples illustrating the graph model and selection procedure. Definitions for quality and diversity metrics and the rationale for combining them are presented straightforwardly. Using an algorithmic breakdown and a visual example to show each iteration of GRAPHFILTER enhances clarity. The experimental results are also well-presented, with tables summarizing key findings and ablation studies that provide deeper insights into specific aspects of the approach.

Significance

GRAPHFILTER is significant because it offers a scalable, efficient solution to the data selection problem in LLM fine-tuning, a critical need given the vast datasets and resources involved in training. By balancing quality and diversity, GRAPHFILTER creates more representative and effective subsets, which can improve model generalization without requiring extensive computational resources. This can potentially enhance SFT for LLMs in domains where data quality and diversity are essential, such as multilingual NLP and domain-specific applications. Moreover, the method’s efficiency is demonstrated by its ability to run on CPUs while achieving faster runtimes than GPU-dependent baselines, making it accessible for more resource-constrained environments. The open-sourcing of GRAPHFILTER and its accompanying data selection scripts provides a valuable tool for future research in data-efficient model training.

### Weaknesses
1. Limited Adaptability Beyond Current Quality Metrics
Weakness: The method relies heavily on the SUPERFILTER metric for quality assessment, which may limit its generalizability, particularly in domains or languages not well-represented by this metric. This reliance could be restrictive, especially when different quality indicators are needed based on the type of LLM or domain being fine-tuned. The current implementation does not offer a clear mechanism for incorporating alternative quality metrics, potentially hindering its application in diverse scenarios where perplexity-based metrics may not be optimal.

Recommendation: To increase adaptability, the authors could explore alternative or domain-specific quality metrics that could be seamlessly integrated into the priority function. An experiment comparing SUPERFILTER with other quality metrics (e.g., perplexity or reward-based metrics tailored to specific tasks) would provide insights into GRAPHFILTER's flexibility. Alternatively, a modular design allowing users to plug in their quality metrics could make the method more versatile and applicable across diverse datasets.

2. Lack of Comprehensive Error Analysis in Data Selection
Weakness: The paper does not provide an in-depth error analysis to examine cases where GRAPHFILTER might underperform or select less useful data, especially when quality and diversity conflict. Such analysis would be valuable for understanding the method’s limitations and refining the priority function. The current analysis focuses on aggregate metrics, but lacks a detailed examination of specific instances where the selection process might fail to capture the most relevant data, particularly when high diversity leads to the inclusion of lower-quality examples.

Recommendation: A targeted error analysis could categorize cases where selected data may not align well with model performance. For example, the authors could examine if lower-quality but diverse data instances significantly impact model outputs or if certain n-grams introduce noise. This analysis could also help fine-tune the priority function to better manage trade-offs between quality and diversity, potentially through a weighted approach that adjusts depending on the dataset characteristics.

3. Evaluation Limited to Standard Benchmarks and Missing Real-World Scenarios
Weakness: The evaluation is limited to standard benchmarks, which, while effective for baseline comparisons, may not fully capture the method’s utility in diverse or more practical real-world scenarios. Standardized datasets often lack the complexities of domain-specific data, such as legal, biomedical, or social media text, where quality and diversity requirements vary. The current evaluation does not address the performance of GRAPHFILTER in scenarios with noisy or low-resource data, which are common in real-world applications.

Recommendation: Extending the evaluation to real-world or specialized datasets would enhance the evidence for GRAPHFILTER’s broad applicability. A domain-specific test (e.g., using a biomedical or multilingual dataset) would provide insights into how GRAPHFILTER handles more nuanced data selection needs. Additionally, incorporating a diverse data type, such as conversational or low-resource languages, could demonstrate the method’s robustness across data complexities.

4. Minimal Analysis of Computational Efficiency Gains
Weakness: While the paper notes GRAPHFILTER’s computational efficiency, it lacks a detailed analysis of where and how these gains are achieved, particularly regarding graph updates and priority re-ranking. This could limit readers’ understanding of the method’s scalability and how well it would perform on substantially larger datasets. The paper does not provide a breakdown of the computational costs associated with each step of the algorithm, making it difficult to assess the true efficiency gains compared to baseline methods.

Recommendation: Breaking down computational costs (e.g., time spent on graph updates vs. priority re-ranking) would clarify the efficiency gains and allow for targeted optimizations. Additionally, experimenting with larger dataset subsets or more frequent updates could provide a clearer picture of how GRAPHFILTER scales with data size. If feasible, comparing runtime and memory usage across different datasets would also offer valuable insights for practical applications.

5. Overemphasis on N-gram Diversity Without Fine-Grained Control
Weakness: The method’s focus on n-gram diversity may be limited if particular n-grams or patterns are less relevant to specific tasks. In some cases, emphasizing phrase-level or domain-specific terms could be more beneficial than broad n-gram diversity, but the current setup lacks control over such granular adjustments. The current approach treats all n-grams equally, potentially leading to the selection of less informative or even noisy n-grams that do not contribute to the desired task performance.

Recommendation: Incorporating a mechanism to adjust the weight or importance of specific n-gram levels or types would add flexibility. For instance, allowing users to prioritize specific n-gram frequencies or filtering by linguistic features such as named entities or domain-specific terms could enhance GRAPHFILTER’s relevance for task-specific fine-tuning. This could be tested with a small-scale experiment where the diversity weight is adjusted based on target domain characteristics, such as including only highly informative bigrams in biomedical data.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a method to filter data for supervised fine-tuning of LLMs.  Given a budget of a certain number of instruction+response pairs on which to fine-tune, this paper proposes that we should prioritize selecting both high-quality instructions (assessed with some kind of quality metric) and diverse instructions (by selecting new unique n-grams).  Prior work has focused on either quality or diversity in isolation.  The approach is implemented using a data structure called GraphFilter, which links n-grams to the sentences that they occur in.  The algorithm proceeds in a greedy manner, selecting instructions that have the highest product of quality times diversity, and then removing all selected n-grams from future assessments of diversity (meaning instructions with those n-grams will now be weighted lower in the next iteration).  The proposed method is shown to improve over various baselines, and ablations show that using both the quality score and the diversity score together are better than using either in isolation.  Another interesting experiment shows that the value of quality is highest with smaller budgets, whereas with larger budgets, the importance of diversity grows.

### Strengths
For the most part, the paper is clearly-written and well organized.  It’s relatively easy to understand what has been done, and, many of the things that were done are well-motivated and sound.  Figure 2 and Algorithm 1 add to the clarity.  The ablations are presented well in the Tables.  The main claim: that we need quality and diversity together to select a good dataset for supervised fine-tuning (SFT), is well-supported by the experiments.  It’s a fairly reasonable idea, and seems potentially beneficial to others doing supervised fine-tuning.

### Weaknesses
The overall motivation for a SFT data budget is not perfectly motivated.  What controls the size of this budget?  Do we see diminishing/negligible returns as we FT over more and more data?  Could downstream accuracy actually suffer as we move to lower-quality data?  Or are we just limited by our own compute budgets for doing the supervised fine tuning?  It would have been useful to motivate this further in the paper, as the exact motivation can affect the reviewer evaluation of what experiments should have been run, etc.  Right now, it’s not clear whether filtering data generated by an LLM for SFT is as important as filtering data scraped from the web for pretraining.

I am confused about the use of TFIDF in this context.  Normally, TF is the term frequency *within a document*, and IDF is the inverse of the frequency of the term *across documents*.  It’s a good metric for finding keywords in a specific document because “important” terms are frequent in the given document, but less frequent across documents.  But here, TF seems to mean the *global* term frequency, while IDF represents the inverse frequency *across sentences*.  I struggled to think of examples where this is useful.  For many terms, I would expect them to occur at most once in each sentence, so it seems to me that TF and DF would be very similar for most terms, and thus the overall “diversity score” scales with x log(1/x), where x is the frequency of the term.  I do not expect this score to encourage diversity; indeed, I think diversity arises from removing the n-grams from consideration that have already been used in instructions – so on subsequent iterations, sentences containing previously-unseen n-grams will get higher scores.  It is not clear – and ablations do not test – if using what-is-called TFIDF provides a benefit over, say, counting each N-gram based purely on its frequency, or even giving each N-gram a score of 1.  Since both using “TFIDF”, and calling it that, seem incorrect to me, and this score is more complicated than other approaches, it’s hard for me to recommend using this algorithm to my colleagues working on supervised fine-tuning.  It’s hard to picture the paper being published with this issue.

I didn’t find Figure 1 that useful; it would be better if it illustrated how the algorithm works in a bit more detail.

Some of the claims were misleading or at least oversold.  For example, GraphFilter “captures the complex relationships between sentence and n-grams.”  From my perspective, it captures a single relationship, whether the sentence CONTAINS the n-gram… and that’s a fairly straightforward relationship.  Also, GraphFilter is “up to 61x faster than these baselines without requiring GPUs.”  But isn’t it just 61x faster than a SINGLE baseline (AlpaGasus)?  If we’re cherry-picking single baselines, how much faster is it than Random?  And isn’t it only 61x faster when not using the priority function for re-ranking?  And yet I don’t see where we report the accuracy when not using the priority function.  It’s not valid to claim it outperforms the baseline accuracy by x% and is 61x faster, when it seems these things are not JOINTLY true.  It would be like having an untested mode of GraphFilter that picks the shortest instructions and using this to justify a claim that GraphFilter is 500x faster than the baselines.  Besides, I don’t really understand what it means not to use ϕ(u), because as far as the paper says, ϕ(u) is how GraphFilter ranks sentences (Equation (4)).  Finally, the intro claims GraphFilter outperforms the baselines by “up to +2.37 for GEMMA-2-2B, +3.02 for MISTRAL-7B-V0.3, and +3.38 for LLAMA-3-8B” – but this is only over LONGEST, and that’s not even as good as RANDOM.  I am not sure the paper *intentionally* tried to mislead the reader, but after reading the introduction, the reader was *expecting* GraphFilter to beat a COMPETITIVE baseline by being BOTH 2-3% better AND 61x faster.

In terms of other ablations, since we see that unigrams to trigrams are important, it leads us to wonder, what about four-grams?  And five-grams?  Where does it level off?

I am also not sure how sound it is to report results applying GraphFilter to instructions only (and not responses).  Perhaps it would have been more fair to test each baseline being applied to either instructions only, responses only, or both, and then to report the best result across all three (assuming that was how the results were compiled for GraphFilter).

Small points (not affecting the scoring/evaluation of the paper):
- While Section 5.4 is great, you should remind everyone there are only 300K sentences in total so things will approach random (Δ_all will got to zero) as we increase the budget.
- Without using TFIDF nor SuperFilter, is it random?  So why is the result 45.61 in Table 4 and yet random gets 45.51 in the main Table 1?  Is that a typo?  Did you re-run it again?  Is it not random?

### Questions
Is there much variance in these results?  What about re-running multiple times in order to get error bars?

Why TFIDF and not just TF (as noted above)?  Or just giving every n-gram a score of 1.

Why Quality x Diversity?  What about Quality + Diversity?  Quality^2 * Diversity?  Quality * Log(Diversity)?  Quality^(10/log(N)) * Diversity, where N is the size of the subset.  You know what I mean?  There is some assumption underlying Quality x Diversity, and since it’s the central topic of the paper, it would be good to spell it out and test it.

### Soundness
3

### Presentation
3

### Contribution
2
