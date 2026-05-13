# Language Model-Driven Data Pruning Enables Efficient Active Learning

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Active learning (AL) optimizes data labeling efficiency by selecting the most informative instances for annotation. A key component in this procedure is an acquisition function that guides the selection process and identifies the suitable instances for labeling from the unlabeled pool. However, these acquisition methods suffer from high computational costs with large unlabeled data pools, posing a roadblock to their applicability on large datasets. To address this challenge and bridge this gap, we introduce a novel plug-and-play unlabeled data pruning strategy, \texttt{ActivePrune}, which leverages language models to prune the unlabeled pool. \texttt{ActivePrune} implements a two-stage pruning process: an initial fast evaluation using perplexity scores from an \textit{n}-gram language model, followed by a high-quality selection using metrics for data quality computed through a quantized LLM. Additionally, to enhance the diversity in the unlabeled pool, we propose a novel perplexity reweighting method that systematically brings forward underrepresented instances for selection in subsequent labeling iterations. Experiments on translation, sentiment analysis, topic classification, and summarization tasks on four diverse datasets and four active learning strategies demonstrate that \texttt{ActivePrune} outperforms existing data pruning methods. Finally, we compare the selection quality $\leftrightarrow$ efficiency tradeoff of the data pruning methods and demonstrate that \texttt{ActivePrune} is computationally more efficient than other LLM score-based pruning methods, and provides up to 74\% reduction in the end-to-end time required for active learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The main contribution of the paper is the introduction of ActivePrune, a novel data pruning strategy that enhances the efficiency of active learning. ActivePrune uses a two-stage pruning process: (1) a fast evaluation using perplexity scores from an n-gram language model, followed by (2) a high-quality selection using data quality scores computed with a quantized large language model (LLM). Additionally, ActivePrune employs a novel perplexity reweighting technique to improve diversity by prioritizing underrepresented instances in the dataset.

### Strengths
1.  The proposed ActivePrune framework is a novel, efficient two-stage pruning process that claims a significant reduction in computational costs in active learning without compromising data selection quality.

2.  The paper introduces a unique perplexity reweighting technique that systematically prioritizes underrepresented instances, promoting diversity in the selection pool across iterations.

3. The re-weighting algorithm based on the already selected samples in previous iterations in very unique to ActivePrune and is a very good way to enforce diversity.

### Weaknesses
1. The authors should clearly include the definitions of $\mathcal{L}$, $\mathcal{F}$, L etc. which seems to be used interchangeably in the document. eg. In line 226, is L here same as $\mathcal{L}$ introduced in line 161 ?

2. ActivePrune uses 2 LLMs in its pipeline but continues to enjoy 97% higher efficiency over 'Random' sampling techniques. This is misleading. Can this be a function of large compute resources used in the paper ?

3. Authors claim the use of a 'high-quality' LLM to score examples. LLMs have been shown in recent literature to demonstrate hallucinations and spurious correlations which have a high probability to impact the quality of predictions. The authors should provide additional analysis on this to establish the impact of the paper. This impact is even more necessary since the paper claims to have used a quantized language model (line 213) in their pipeline.

4. In lines 184 the authors mention the selection bottom $k$ instances. Since the list is sorted in ascending order, the top-k examples should have the lowest perplexity. This is also observed in line 217 where the authors mention the selection of bottom k indices, which for a list sorted in descending order should be the top-k elements.

5. The gain in performance for datasets other than IT Domain seem to be very marginal. In some cases such as the classification task in AG News dataset, the change in F1 score over random is very incremental which weakens the contribution of ActivePrune.

### Questions
1. In line 219 should the expression for $\mathcal{F}$ be $\mathcal{F} \cup \mathcal{Q}_s$ ? 

2. In Section 3 the authors call out the key components of ActivePrune. These seem to also be the main contributions of the paper and should be clearly called out earlier in the paper, preferably in Section 1.

3. In line 182, the line ends without a period '.' and should be included.

4. The authors perform only 5 rounds of AL for each task. Is this a common practice or has been decided based on some factors ? This would highly increase readability.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces ActivePrune a Data Pruning method for Active Learning. The method comes in 3 parts: a perplexity filter, a LLM model for quality selection, and perplexity reweighting for diversity. First, the perplexity filter reduces the unlabeled pool to top k examples. Second, the quantized LLM chooses quality examples by being prompted a yes or no questions. Lastly, the perplexity reweight formula  updates the perplexity scores in light of new data to increases diversity. The reweighting formula is also the main novelty of the paper. The authors claim that this method can speed up the training process and also improves task performances.

### Strengths
The writing is easy to follow an understand. All 3 stages of the methods are clearly stated and it is very easy to understand their mechanisms. 

The diversity claim through perplexity is explained clearly with proofs.

Leveraging LLM is a good way to improve the quality selected examples.

The problem is non trivial as data size can greatly affect the training process.

### Weaknesses
A contradictory stance on the perplexity score: examples with the lowest perplexity scores are chosen to improve quality but then examples with high initial perplexity are then chosen also. The perplexity reweighting method does not target quality examples but only diversify the perplexity of the chosen examples. 

Unclear why the perplexity - LLM pipeline is needed: Sachdeva et al., 2024 stated that the usage of LLM instead of perplexity to select quality data is because LLM is superior. The author has not justify their decision to use both methods in contrary to Sachdeva et al., 2024 

Unjustified usage of perplexity for diversity: Based on figure 4, the selected high perplexity examples are low quality examples. 

Figure 4 seems to suggests the Ask-LLM would be a better candidate as the chosen samples have higher quality and the mass of the selection examples are more spread out on the perplexity tail end compare to ActivePrune. 

The speed up baseline is unreasonable: ActivePrune uses both perplexity and LLM but the speed up is 100x compare to methods that only use LLM or perplexity.

### Questions
Are the selected high perplexity examples actually good for training?

Does the competitiveness for speed go away when the baselines also use quantized LLM?

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
4

### Summary
The authors propose a data pruning method for active learning (AL) settings that discards instances from the unlabeled pool using a quantized large language model (LLM). Experiments across four datasets from machine translation, summarization, and classification demonstrate that the proposed method outperforms several baselines and is computationally faster than other LLM-based pruning methods.

### Strengths
- The paper is well-written, and the method is clearly explained.
- The proposed idea is straightforward and appears to be computationally faster than similar state-of-the-art LLM-based methods.
- The method works in both classification and text generation tasks.

### Weaknesses
 - The related work section is missing several active learning works (please see below).
- Improvements seem marginal.
- Metrics like BLEU and ROUGE do not fully capture output quality in text generation experiments. The authors should consider using a wider range of metrics to provide a more comprehensive evaluation.
- Evaluation uses a limited number of datasets.

### Questions
- How does the method impact model generalisation in out-of-distribution settings? CounterAL and ALVIN show that many AL methods struggle with OOD generalisation, does this method address that?
- The authors claim that the method promotes underrepresented instances but do not demonstrate that empirically. Metrics such as those defined in Ein-Dor et al. (2020) could help assess the types of instances chosen. Furthermore, if the proposed method indeed identifies underrepresented instances, this could also enhance the method’s effectiveness in OOD settings, as mentioned above.
- It would have been interesting to see how the proposed method performs when combined with state-of-the-art AL methods, such as CAL.
- How does the method perform when used to train other model architectures, such as BERT?

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
The paper introduces ActivePrune, a method designed to enhance the efficiency of active learning techniques in NLP. In active learning, instances from an unlabeled pool are selected for labeling, which can be challenging when the pool is large. ActivePrune addresses this issue through pruning: it utilizes perplexity scoring and LLM filtering to reduce the initial pool to a more manageable size. Subsequently, active learning algorithms are applied to this refined pool. Experiments conducted on four NLP tasks demonstrate that ActivePrune is more efficient than existing methods.

### Strengths
The strengths of the paper are presented below:

- S1) The problem studied is interesting, as it is computationally challenging to evaluate the LLM's uncertainty on a large pool of examples.

- S2) Experiments conducted on the large IT dataset show that ActivePrune is more efficient than other existing uncertainty-based methods.

- S3) The paper is clearly organized and easy to follow. Additionally, Section 3.4 provides a solution for addressing underrepresented instances during pool pruning.

### Weaknesses
The weaknesses of the paper are presented below:

- W1) **Evaluation**: The experimental evaluation lacks depth. For instance, ActivePrune compares itself to other costly LLM-based pruning techniques but does not include comparisons with lightweight methods, such as k-means clustering or coreset selection. These experiments are essential to assess the effectiveness of the approach. Specifically, the paper should include a comparison with k-means clustering using various distance metrics (e.g., cosine, euclidean) on the embedding space of the input text. Furthermore, the coreset selection comparison should not be limited to the classification tasks but should also be extended to the other tasks, such as translation, to provide a comprehensive analysis.
- W2) **Soundness**: ActivePrune achieves improved efficiency through the use of an n-gram model for perplexity scoring and a quantized 2B LLM for filtering. However, such a solution is not sophisticated and lack robustness. For example, in domain-specific datasets, such as medical or finance, or in complex tasks, such as math reasoning, these models might be limited. It is suggested that authors evaluate their approach in more challenging tasks. The use of a fixed n-gram model and a quantized LLM might not generalize well across diverse datasets, especially those with complex syntactic structures or specialized vocabularies. The paper should include an analysis of the impact of these choices on the overall performance of ActivePrune.
- W3) Furthermore, the approach does not account for the downstream LLM. For example, it may prune the same instances regardless of whether a medical or finance LLM is used, omitting to consider their respective knowledge of the task. The pruning process should ideally be adaptive to the downstream model's specific characteristics and knowledge. The current approach risks removing instances that might be crucial for a particular downstream model, leading to suboptimal performance.

### Questions
Please refer to the comments above. Here are some additional questions and comments:
- Q1) Section 3.3: Could you clarify why you chose a prompt-based approach to evaluate perplexity instead of directly assessing it based on the LLM's logits for the sequence?
- Q2) Section 4.2: Why do you select only one model per task? Would it be possible to evaluate multiple models on the same task?
- Q3) Have you considered using in-context learning in addition to training models on the selected examples for active learning?
- Q4) Section 3.2: I recommend moving some details from this paragraph to another section, as they are not directly related to the proposed method.

### Soundness
2

### Presentation
3

### Contribution
2
