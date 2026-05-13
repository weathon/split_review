# Abstractive Summarization through the PRISM of Decoding Strategies

- Decision: Reject
- Scores: 8, 5, 6, 5

## Abstract
In the realm of natural language generation, abstractive summarization (AS) is at the center of an unparalleled evolution driven by transformer-based language models (LMs). However, the significance of decoding strategies is often neglected despite their influence on the generated summaries. Given the abundance of token selection heuristics and their accompanying hyperparameters, the community needs directions to steer well-founded decisions based on the task and the target metrics at hand. To fill this gap, we comparatively assess the effectiveness and efficiency of decoding-time techniques for short, long, and multi-document AS. We explore more than 2500 combinations of 3 widely used million-scale autoregressive encoder-decoder models, 6 datasets, and 9 decoding settings. Our findings shed light on the field, demonstrating that optimized decoding choices can yield substantial performance enhancements. In addition to human evaluation, we quantitatively measure effects using 10 automatic metrics, including dimensions such as semantic similarity, factuality, compression, redundancy, and carbon footprint. We introduce PRISM, a first-of-its-kind dataset that pairs AS gold input-output examples with LM predictions under a wide array of decoding options.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates in-depth different decoding strategies for abstractive summarization, exploring more than 2500 combinations of 3 models, 6 datasets, and 9 decoding settings. The goal of the paper is to shed light on the field and demonstrate that optimized decoding choices can yield substantial improvements to the performance.

### Strengths
* The experiments are very comprehensive, covering a bunch of different decoding strategies and their hyperparameters.

* The data when released can be very useful, not just for further benchmarking, but also in terms of modeling and evaluation since predictions are also released.

* The paper is very clearly written.

### Weaknesses
 * While the experiments are comprehensive, I find that the paper lacked overall recommendations that practitioners can follow in a real-world setting (which I believe is the main purpose of the paper). For example, if one has a new summarization use case, how does the paper help them decide which model and which decoding strategies (+ hyperparams) to use? The paper does provide a list of findings, however a set of recommendations as part of the conclusion would greatly improve the paper's impact.

* The models are unfortunately limited to 400-500M parameters. This is significantly small if compared with LLMs, thus it is uncertain whether the results shown in this paper transfer to these large models. It could have helped to see models of varying sizes (perhaps one small-scale and one XL-scale) to show that the results to actually hold even when the model size is different.

### Questions
* What is the set of recommendations that the authors think practitioners should follow?

* How do these results transfer at scale (smaller or larger)?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an extensive study of the effect of various decoding methods on the quality of generated summaries on the task of abstractive written text summarization. The results cover three encoder-decoder transformer models with finetuned weights matched to six public abstractive summarization datasets under three categories: short text, long text, and multi-document. Explicit hyperparameter tuning was done on each (decoding strategy, dataset) pair, and the variation was evaluated by a multitude of automatic text evaluation metrics (lexical and semantic) as well as human evaluation along four quality dimensions (precision, recall, factuality, and fluency). The general findings confirm a lack of dominating decoding strategy for all tasks studied, and show that hyperparameter settings are also task/decoding strategy specific with potentially significant variation in calculated metrics between optimal and suboptimal hyperparameters.

### Strengths
Originality:
One of the biggest strength of the paper is in its scope of decoding methods (nine) and datasets (six). Although the study of effect of decoding methods on the quality of generated summaries by summarization models has been gaining momentum in the research community, a study of the scale presented in this paper has yet to be published.

Quality:
The results presented in the paper cover a wide range of research parameters (task, dataset, hyperparameter, strategy, evaluation metrics, automatic vs human evaluation). The authors have also been quite thorough in including detailed explanation on the data selection, preprocessing, and evaluation. The power analysis in Appendix D is a welcoming addition to the paper, lending reference to robust statistical analysis on the potential reliability of the findings in the paper.

Clarity:
The paper is generally well-organized, with thorough explanation on the experimental settings for clear reproducibility test.

Significance:
Another major strength of the paper is the significance of the direction of the research. Evaluation metrics and decoding strategies are two main aspects in abstractive summarization that are relatively underexplored compared to research on newer summarization models or new datasets. However the decoding methods undoubtedly play an influential role in the task of summarization and text generation in general. There are arguments on the misalignment between cross-entropy based training objective and actual quality measures of interest, and the success of many reranking methods also reflects the suboptimal strategy of blindly following a single decoding strategy. Therefore, the study done in this paper can provide referential values for any related and future research in summarization that aims at improving quality of the generation.

### Weaknesses
Major weakness of the paper is the presentation style of main results in Figure 3, and some inconsistency between Figure 3, the writing, and Figure 8 that may bring some of the quantitative findings into question:

1. Because of the density of information and the lack of differentiability in the chosen colors for different decoding strategies, Figure 3 is very hard to follow. For example, Greedy Search and Beam Sampling are both presented with "reddish" color, and the reviewer finds it very difficult to identify which is which in the plot. Additional comments on the figure are presented as questions in the "Questions" section

2. Because of the lack of interpretability of Figure 3 and lack of tabulated data for the results, it is hard for the reviewer to confirm the quantitative differences referred to in the Results section (e.g.,  +48% UNR avg. score mentioned between short and long summaries). It is crucial to provide the underlying numerical values to support claims made in the text, and the absence of this data makes it difficult to assess the robustness of the findings.

3. Contrary to the discussion on the relative advantage of certain decoding strategies over other in section 5.1, the impression of the reviewer from Figure 8 is that 
(i) sampling, top-k, and top-p sampling clearly have larger sample variance than all other strategies, even after hyperparameter tuning, on five out of six datasets; (ii) the behavior of all decoding methods changes significantly on Multi-LS dataset, showing larger scale of variation in average score and much smaller sample-specific variance; (iii) apart from the three sampling strategies mentioned in (i), the remaining methods on all datasets except Multi-LS seem to be consistently on par with each other as evaluated by most of the evaluation metrics

these observations may contradict the quantitative findings in section 5.1, and there seems to lack specific discussion on those arguably more obvious patterns than the ones presented in Figure 3 and discussed in the text. The lack of discussion on the high variance of sampling methods and the unique behavior on Multi-LS dataset raises concerns about the interpretability of the results and the conclusions drawn from them.

Another weakness is the generalizability of the findings. The reviewer agrees with the authors that the lack of a universal strategy for optimal decoding is substantively supported by the results, but apart from that the paper seems to be lacking in identifying other general trend or patterns in combination of the research parameters (decoding strategy, task, model, hyperparameters). This limits the value of the results to be observational rather than inferential. The paper needs to delve deeper into the interactions between these parameters to provide more actionable insights.

Other problems regarding writing:
1. **Elevating Fluency undermines Recall, Precision, and Factuality.** in Section 5.2 is not a rigorous statement based on the results, what the authors have observed is a negative correlation between fluency and other quality factors as evaluated by human, but the phrasing of the finding turns such a correlation into a misleading causal statement.
2. It is not rigorous to draw conclusion on "factuality", "factual flaws", or "hallucination" solely based on BARTScore (e.g., Section 5.1, **stochastic vs deterministic**), which is at best a proxy for those quality measures. Please at the very least state in the main text that the studied automatic metrics are "proxies" of the quality dimensions of interest. The reliance on a single automatic metric to evaluate such a complex aspect of text generation is a significant limitation.
3. Typo: Table 4, shouldn't UNR be "Unique N-gram Ratio", not "unigram n-gram ratio"?

### Questions
1. In Figure 3, why are some of the metrics score concentrated towards low value (center of each circle, e.g., Perplexity on Multi-News)? The  reviewer may have misunderstood the presentation here, but if all scores are rescaled to [0, 1] based on min and max of each score, shouldn't there be a point on the outer perimeter for every metrics on every dataset (that is, the decoding method with the maximum score in a metric on a dataset)?
2. Any special reason why y-axis in Figure 4 is not presented on a linear scale?
3. Can you elaborate, maybe in the appendix, more details on the training regimen used in the human evaluation? Were the annotators given any examples or detailed explanation on each quality dimension? How did you guarantee that the source document would be viewed by the annotator? Or were the annotators already familiar with the research objectives so that training was minimal?
4. How is Kendall's tau calculated for human evaluation results? Was it calculated between two annotators across all pair selection results, or was a ranking of all decoding strategies first determined based on all selections from one annotator, and then tau calculated between two rankings? Why are the reported values so low and even negative on some datasets? If the annotators disagree significantly in their preference, wouldn't that seriously limit the possibility of drawing any robust conclusion based on their evaluation results?
5. Why not consider more semantic similarity metrics (e.g., NLI-based evaluation, see https://aclanthology.org/P19-1213.pdf for example) or NER based metrics? Apart from BertScore and BartScore, almost all other metrics used are lexical based (n-gram or character overlap). It's hard to say if the variation observed in those metrics truly reflect variation in qualities of the generated summaries (and based on Figure 8, it's hard to say if significant variation has been observed).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper conducts a large-scale study on the impact of decoding strategies on abstractive summarisation.
The authors investigate 9 decoding strategies (greedy search, contrastive search, beam search, diverse beam search, sampling, top-k sampling, top-p nucleus sampling, beam sampling, eta sampling) on 6 datasets (XSum, CNN/DM, PubMed, arXiv, Multi-News, Multi-LexSum), combined with 3 seq2seq models. In addition to human evaluation on 4 dimensions (recall, precision, faithfulness, fluence), the authors employ 10 automatic metrics (rouge, BERTScore, perplexity, coverage, density, compression, unigram n-gram ratio, normalized inverse of diversity, BARTScore, and Carburacy) and a few observations are provided.

### Strengths
* A large-scale study on multiple decoding strategies
* A resource that enables further studies on abstractive summarisation regarding evaluation metrics. 
* The paper is easy to follow, except some figures are hard to interpret

### Weaknesses
It is hard to gain much insight from the results: sometimes it is unclear whether the authors are commenting on decoding strategies, datasets, or evaluation metrics.


### Questions
A: can you elaborate on the human evaluation dimension of faithfulness, especially how you instruct annotators to differentiate it from precision and recall?
B: it will be appreciated if some practical guidelines can be summarized

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores over 2,500 combinations of three widely-used million-scale autoregressive encoder-decoder models, across six datasets and nine decoding settings. The research reveals that optimized decoding choices can significantly boost performance.

### Strengths
1. The authors conduct extensive experiments across various combinations and datasets.

2. The paper provides visualized and in-depth analysis.

### Weaknesses
1. Given that there's no universal strategy for abstractive summarization, the practical value of the experiments is questionable. For the investigated question like "Which hyperparameter values best suit a particular AS quality attribute?", the answer is "Not all quality attributes are easy to temper at decoding time.", which seems ambiguous and might not guide future work. The lack of a clear, actionable outcome from such extensive experimentation weakens the overall contribution. Specifically, the paper does not identify specific decoding strategies or hyperparameter settings that consistently improve particular quality attributes across different datasets and models. The experiments, while thorough, seem to confirm the lack of a universal solution without providing concrete alternatives or workarounds.

2. Extending the method to LLM models would have made the findings more impactful in the era of LLM. The current experiments are limited to encoder-decoder models, which are rapidly being superseded by LLMs. The results, therefore, may not be generalizable or relevant to current state-of-the-art summarization techniques. The paper does not address the potential challenges or opportunities of applying similar decoding strategies to LLMs, which are known to have different behaviors and characteristics.

### Questions
none

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
