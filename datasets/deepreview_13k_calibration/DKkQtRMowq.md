# Improving Data Efficiency via Curating LLM-Driven Rating Systems

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Instruction tuning is critical for adapting large language models (LLMs) to downstream tasks, and recent studies have demonstrated that small amounts of human-curated data can outperform larger datasets, challenging traditional data scaling laws. While LLM-based data quality rating systems offer a cost-effective alternative to human annotation, they often suffer from inaccuracies and biases, even in powerful models like GPT-4. In this work, we introduce \method, a \textbf{D}iversity-aware \textbf{S}core curation method for \textbf{D}ata \textbf{S}election. By systematically modeling error patterns through a score transition matrix, \method~corrects LLM-based scores and promotes diversity in the selected data samples. Our approach shows that a curated subset (just 3.3\% of the original dataset) outperforms full-scale datasets (300k samples) across various machine-alignment benchmarks, and matches or surpasses human-aligned datasets such as LIMA with the same sample size (1k samples). These findings challenge conventional data scaling assumptions, highlighting that redundant, low-quality samples can degrade performance and reaffirming that ``more can be less.''

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce a data curation algorithm, DS^2, to correct inaccuracies in LLM-based data quality evaluation strategies.  The authors first show how, leveraging recent work in noisy label estimation given k-NN clusterability, both the Transition matrix and true probability distribution of LLM scores may be estimated by solving a linear program.  Under this k-NN clusterability assumption, the authors demonstrate that widely used LLM scorers (GPT-4o-mini, Llama-3.1 8B, and Mistral 7B) provide incorrect scores.  Using both Transition matrix and (true score) probability distribution, the layout the steps of their DS^2 algorithm and calculation of critical quantities: the error threshold for classifying samples as misrated, the confidence probability for mitigating imbalances in LLM scores, and the long-tail diversity score.

The authors then compare several data selection experiments leveraging the DS^2 algorithm over a large data pool (300k) containing several widely used datasets (i.e., Alpaca, Dolly, Flan V2, etc.).  Compared to several data selection heuristics and competitor LLM-based data selection algorithms (i.e., AlpaGasus and Deita), the authors show that their methods outperforms competitors per-LLM-judge and averaged over common natural language benchmarks (MMLU, TruthfulQA, GSM, BBH, and TydiQA) at a data selection size of 10k samples.  Representative experiments than compare the performance of DS^2 selecting 1k samples (over the 300k data pool) compared to the LIMA dataset (which was heavily vetted and selected using human feedback), once again outperforms finetuning LLama-3.1-8B and Mistral 7B models using the LIMA dataset.  Scaling law experiments as well as hybrid data selection schemes (e.g., AlpaGasus leveraging DS^2's data curation scores) further show the efficacy of the presented methods.

# Post-rebuttal update
The authors have posted additional experiments to address my major concerns.  Particularly, an apples to apples comparison to AlpaGasus demonstrating DS^2's superiority and a discussion/experiments tackling the practical aspects of k-NN clusterability for this use case.  I am raising my score from 5 to 6.

### Strengths
The procedure to estimate the transition matrix from LLM scores is intuitive.  The beginning of the paper is also well written, and the examples showing the deficiencies in LLM-based scores is compelling.  The subsequent probability quantities leveraged throughout the DS^2 algorithm also largely make sense.  The large number of experiments demonstrating the effectiveness of the approach is also compelling.

### Weaknesses
Firstly, I would like to congratulate the authors on the DS^2 algorithm and the idea of leveraging k-NN clusterability to correct LLM-based scores.  Such a line of work seems promising.  With that said, I have several concerns that I am hoping can be addressed (I am greatly looking forward to the authors feedback).

While the beginning of the paper is well written, there seemed to be either missing details or a lack clarity for important concepts.  In particular, Algorithm 1 is difficult to follow; "CuratedScores" is not defined in Algorithm 1. Are "ConfidenceProbs" the curated scores?  Furthermore:
> the average likelihood of identifying the sample n as misrated over multiple epochs.

How is this calculated in practice?  Given a dataset with an arbitrary ordering of samples, how can a statistic dealing with the arbitrary index $n$ be meaningful?  Put another way, this calculates the statistics at the sample index, but the data pool samples (line 172) are not stated as being ordered in any specific way.  Thus, how can a statistic calculated over the sample index be anything other than arbitrary?

Furthermore, while the notion of k-NN score clusterability (as defined in Definition 3.2) is assumed, this notion is never actually demonstrated for the LLM judges and datasets considered.  Do the score distributions depicted in FIgure 2 abide by k-NN score clusterability?  If not, could the authors speak to how this affects the Transition matrix and (true score) probability distribution calculations from the concensus vectors (Equation 1)?  If k-NN score clusterability is violated in practice, it does not seem possible to guarantee the correctness of estimating the Transition matrix and (true score) probability distribution in this case.

There were some concerns regarding the evaluations of AlpaGesus:
> AlpaGasus (Chen et al., 2023) utilizes ChatGPT to rate
data samples and solely select high-rated samples"

One of the major innovations of AlpaGasus was the prompt template.  Was this used for the AlpaGasus results in Table 3?  Note that they also showed the training data size is a very important hyperparameter for Alpaca; thus, a fairer/more apples-to-apples comparison would have been DS^2 applied to Alpaca with a budget of 9k samples and compared to fine-tuning performance (Table 3) of the AlpaGasus dataset.

### Questions
For the k-NN agreement score, assuming the k-NN clusterability characteristic, isn't the similarity score just always unity?  I.e., due to clusterability, the frequency will only occur in the same index as the one-hot encoding vector, and thus the numerator and denominator turn out to be the same.  Also, have the authors empirically explored whether using the embedding feature-vector or the one-hot encoding rated score vector work better in practice?

On the initial read through the paper, there was some initial confusion between: the avoidance of relying on the ground truth scores for DS^2, yet the appearance of the ground truth per-class probability in Section 4.  However, after careful rereading, we have the following: assuming k-NN score clusterability, we are thus able to leverage the concensus vectors and solve the LP for \mathbf{T} and \mathbf{p} (I understand this is stated, but it is easy to miss this simple statement buried in lines 231-241).  I would recommend either reiterating that solving the LP formed from Equation 1 provides both the transition matrix and ground truth probability vector, or breaking up the paragraph on lines 231-241 and emphasizing this.

"the average likelihood of identifying the sample n as misrated over multiple epochs." <- How is this calculated in practice?

For Completion Length, please cite the following:
Zhao, Hao, et al. "Long is more for alignment: A simple but tough-to-beat baseline for instruction fine-tuning." arXiv preprint arXiv:2402.04833 (2024).

For Table 3, please specify the data pool is listed in Table 2, e.g., " Performance comparison on OpenLLM leaderboard, using the data pool listed in Table 2."

Could the authors please bold the winners of each column (per grouping) in Table 3?

### Soundness
3

### Presentation
2

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
This study tackles the problem of rating samples using LLM, more specifically, how to improve the accuracy of LLM-based rating methods. To this end, DS2 (Diversity-Aware Score Curation for Data Selection) is proposed to model rating error pattens using a score transition matrix. Experiments on machine-alignment benchmarks show that strong results can be achieved by using just 3.3% of the original dataset.

### Strengths
* The idea of detecting error pattern is novel. Its implementation using score transition matrix was validated experimentally.

### Weaknesses
 * The description of "deriving the score transition matrix" can be improved. Not sure I can reproduce it based on the given explanation. Some examples can help, which can be included in appendix.
* It is assumed that "the transition matrix is independent of sample-level features". This can be a limitation as each LLM have its own strengths and weakness (i.e., better/worse at some samples).
* Sometimes, the improvement is small, within the variance of different runs.
* Some discussions about limitations would be appreciated.

### Questions
* It looks like that there is an advantage of using GPT-40 mini. How to obtain embeddings from proprietary LLMs?
* Figure 1 reads like ratings of multiple LLMs are combined. The experimental results say otherwise.
* The proposed approach sometimes perform much worse (e.g., in Table 2). Is it possible to decide the appropriate conditions for using the proposed approach (and which LLM)?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposed the data selection pipeline named “DS^2”, which utilizes the kNN statistical information based on the rating scores to curate ratings, and then achieve better data selection. The authors validated their methods by conducting experiments with various rating models and benchmark tasks.

### Strengths
Originality: The paper proposed a novel method to utilize the score transition matrix to detect scoring errors. Although the score transition matrix is proposed by previous works, the application of that into LLM data selection is novel.

Quality: The paper provides detailed explanations of their methods and validates the results using thorough experiments, in which they include three models (GPT-4o-mini, Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3) and various benchmarking tasks (MMLU, TruthfulQA, etc). Moreover, they also evaluated the alignment performance. All these greatly improve the quality of the paper.

Clarity: The paper demonstrated great clarity when exhibiting the error patterns of LLM scores, as well as when explaining the experiment setup and results.

Significance: The significance is validated with the experiment results and the ablation studies.

### Weaknesses
The paper does not include discussions about the efficiency of the proposed method and the efficiency comparison with other baseline methods. Part of the computation relies on estimating the score transition matrix, but the details about this estimation are lacking. Although the score transition matrix is proposed and discussed in previous works, it is still necessary to analyze their cost within the current framework.  Moreover, the paper does not include any baselines that also improve data quality by modifying the score ratings of the data. The current framework essentially proposed a method to modify the rating scores and then conduct data selection based on new scores. It would be helpful to further validate the method by comparing other methods that also study LLM ratings.

I find the discussion around line 200, saying that similar embeddings should belong to the same category, not very convincing. Because here each class is the rating score, in my opinion, two samples could have similar textual embeddings but completely different correctness or quality, which lead to distinct rating scores. I think it is crucial to better explain this intuition behind the proposed method.

### Questions
I find the discussion around line 200, saying that similar embeddings should belong to the same category, not very convincing. Because here each class is the rating score, in my opinion, two samples could have similar textual embeddings but completely different correctness or quality, which lead to distinct rating scores. I think it is crucial to better explain this intuition behind the proposed method.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents DS2, a method for improving data efficiency in instruction tuning for LLMs. DS2 corrects inaccuracies and biases in LLM-generated data quality scores using a score transition matrix and promotes diversity in the data selection process. The authors demonstrate that using a curated subset  can outperform larger datasets, challenging traditional data scaling laws and achieving better results than human-curated datasets like LIMA. Key contributions include modeling score errors across various LLMs, developing a novel data curation pipeline, and conducting extensive experiments to validate DS2's effectiveness against multiple baselines.

### Strengths
1. The paper argue that a smaller, high-quality dataset can outperform larger datasets. The introduction of a score transition matrix to model LLM-based errors adds a novel approach to data curation, combining insights from label noise reduction and LLM evaluation.
2. The experimental section is substantial and persuasive, featuring a rich number of comparative experiments that cover various scenarios and conditions, effectively demonstrating the robustness and efficacy of the proposed algorithm. Furthermore, the experimental results indicate significant performance improvements, further validating the superiority of the proposed approach.

### Weaknesses
1. While the score transition matrix is central to DS2, the paper lacks an in-depth analysis of its limitations or conditions under which it may not be effective. For instance, the independence assumption (that the transition matrix is not sample-specific) might limit its ability to model certain data-specific errors. Specifically, the assumption that the error pattern is consistent across all samples, regardless of their content or complexity, is a strong one that could lead to inaccuracies. The paper should explore how variations in data characteristics might affect the transition matrix and the overall performance of DS2.
2. The paper heavily relies on the capabilities of pre-trained LLMs to generate initial quality ratings and the transition matrix to correct the final quality score. This reliance introduces a potential vulnerability: if the initial LLM ratings are systematically biased or inaccurate, the subsequent correction process might not fully mitigate these errors. The paper should discuss the potential impact of these initial biases and how they might propagate through the DS2 pipeline. Furthermore, the paper should investigate the sensitivity of DS2 to the quality of the initial LLM ratings.
3. If there is a strong LLM evaluator (eg, GPT-4o or o1), the score error correction process seems unnecessary. The paper should provide a more detailed analysis of how the performance of DS2 varies with the quality of the LLM evaluator. It is important to understand whether the benefits of DS2 diminish as the evaluator becomes more accurate, and under what conditions the score correction process remains beneficial.

### Questions
1. Can the authors provide more examples of typical errors in LLM-rated scores and explain how DS2 specifically addresses these? This would clarify the practical benefits of the score transition matrix.
2. Could the authors discuss how the diversity score metric performs in datasets with different distributions or in tasks with varying levels of data complexity? Providing case studies or examples would help demonstrate the versatility of this metric.
3. How sensitive is DS2's performance to the choice of embedding model used for the k-NN agreement score? Exploring different embeddings beyond the BGE model may provide insights into the robustness of the approach.
4. In an open-ended question, the responses may not be similar at all (resulting in very different embedding vectors), but they could all be equally excellent answers. In this method, I believe the two responses may be curated into completely different scores, leading to errors. ”Intuitively, a lower cosine similarity score indicates a higher likelihood of a rating error”, This assumption does not adequately explain the examples above.
5. "please tell me the answer of below math question '1+1=?' answer:2"
"please tell me the answer of below math question '1+1=?' answer:3"
The two questions have similar embedding vectors, but they should have completely different scores. This seems to contradict the notion that samples with high embedding vector similarity are more likely to have the same labels.

### Soundness
3

### Presentation
3

### Contribution
3
