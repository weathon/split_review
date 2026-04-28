# The Genomics Long-Range Benchmark: Advancing DNA Language Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3, 5

## Abstract
The advent of language models (LMs) in genomics necessitates benchmarks that can assess models’ capabilities and limitations. In contrast to protein models, DNA LMs can be used to study non-coding regions of the genome and must account for unique challenges, especially interactions across long sequence lengths. However, existing benchmarks for DNA LMs are defined over short sequence datasets and can involve tasks that are often not considered to be biologically meaningful. Here, we present the Human Genomics Long-Range Benchmark (LRB), which focuses on biologically meaningful tasks and supports long-range contexts. We complement our benchmark with fine-tuning recipes that meaningfully improve performance and affect model evaluation. We evaluate DNA LMs across nine compiled human genome tasks and observe that DNA LMs achieve competitive performance relative to supervised baselines on several tasks (e.g., genome annotation), but there remains a significant gap in domains, such as variant effect and gene expression prediction. Additionally, we introduce a visualization tool to examine model performance split by various genomic properties. Lastly, we present methods for context-length extrapolation of transformer-based models that enable studying the effect of context length on DNA LM performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents the Genomics Long-Range Benchmark (LRB), a new suite of biologically meaningful tasks designed to evaluate DNA language models with a focus on long-range genomic contexts. The authors argue that existing benchmarks are limited by their emphasis on short sequences and sometimes biologically irrelevant tasks. They provide fine-tuning recipes to improve model performance, introduce a visualization tool for detailed analysis, and explore methods for extending the context length of transformer-based models.

### Strengths
The paper identifies a significant gap in the evaluation of DNA LMs by focusing on long-range genomic interactions, which are key for understanding complex biological processes.

The LRB includes nine tasks covering variant effect prediction, gene expression prediction, regulatory element detection, and chromatin feature identification. This breadth ensures that models are tested on a variety of biologically relevant tasks.

Allowing users to select arbitrary sequence lengths for each task is very relevant for the field and facilitates the exploration of context length effects on model performance.

The authors demonstrate that full fine-tuning of DNA LMs significantly enhances performance compared to previous methods that froze the backbone model weights.

Exploring techniques to extend the context size of transformer-based models is a valuable contribution, especially given the computational challenges associated with long sequences.

### Weaknesses
Although the paper compares DNA LMs to supervised baselines like Enformer and DeepSEA, it could include more recent or diverse models to strengthen the evaluation.

The results are presented with mean and standard deviation across folds, but there's no discussion of statistical significance. Including statistical tests would provide more confidence in the reported improvements.

### Questions
I highly encourage the authors to:

Report statistical comparison between metrics.
Include more models in the benchmark. A good example is https://arxiv.org/abs/2406.10391

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
The authors present a new benchmark for evaluating DNA language models (LMs) with a focus on context size studies. They compiled a set of both long-range and short-range downstream tasks for DNA LMs, including variant effect prediction, gene expression, regulatory element, chromatin feature predictions, etc. The tasks and datasets are well-documented, and the benchmark comes with user-friendly features such as customizable context size downloads and visualization tools. Although this benchmark has potential utility for the field, it lacks some important results and discussions. Therefore, I currently recommend a weak rejection of this paper. I am open to raising my score if these issues are adequately addressed.

### Strengths
1. The benchmark has a clear theme centered on the study of context sizes, which is currently an important topic in the development and application of DNA LMs. This benchmark can be expected to yield valuable insights for the field.
2. The authors selected a biologically relevant array of downstream tasks.
3. The paper includes a thorough review of existing benchmarks.
4. Dataset details are well-documented.
5. The visualization tool appears useful and well-designed.

### Weaknesses
1. I see the most significant contribution/novelty of this benchmark to be facilitating studies on context size, a point emphasized in both the title and introduction. However, the results section provides only a general and superficial discussion on this topic, and the study of context length is quite restricted to NT. To provide more insight, there should be an in-depth analysis of the impact of context sizes on individual tasks and models. For instance, does each model empirically benefit from longer context lengths, and to what extent? Do certain tasks show a stronger dependence on longer context sizes as expected? There are more detailed evaluation results in Tables 11 and 12 in the appendix but lack an interpretation of the data. I would suggest creating some figures/tables to summarize these results and have more discussion on the impact of context size.
2. There is a missing discussion regarding alignment-based DNA LMs, which could have different context-size dependencies than single-sequence DNA LMs. Including this aspect is crucial for a complete and accurate narrative. This work builds on the GPN-MSA ClinVar and OMIM benchmarks but strangely does not include (nor even mention) the GPN-MSA model itself. GPN-MSA achieves SOTA on these tasks, performing better than CADD, and therefore better than all the DNA language models considered. It is important to include GPN-MSA in the benchmark (at least for zero-shot evaluations, if the authors deem fine-tuning to be cumbersome), since this could change the narrative in fundamental ways. First, it's not true that DNA language models do worse than CADD. This only applies to single-sequence models. Second, GPN-MSA achieves a good performance even with the smallest context. One interpretation is that with evolutionary context, one doesn’t need as much spatial context. Given that GPN-MSA is alignment-based, it could be reported by itself with a separator line in Table 3. Finally, even if the authors decide to restrict the discussion to single-sequence DNA LMs, it is conventional to compare with the actual SOTA on each task.
3. The sections on context length extrapolation read a bit disconnected from the rest of the manuscript. It appears to be an improvement on the NT model rather than directly related to the benchmark. If the authors claim it to be a generally applicable method to other DNA LMs, it should be made clear in the writing and preferably applied to at least another model. If it is for a focal investigation on the impact of context size on NT, the results should be more carefully analyzed and discussed.
4. In Table 3, Enformer is not a good baseline for the ClinVar task, since this set only contains missense variants and Enformer is a model focused on the non-coding genome.
5. In Section 3, the authors discussed why several tasks should be considered long-range, but did not discuss why the others are not. It would have been better to also include brief discussions on why those tasks are expected to be performed well with short-range models.
6. Section 3.1.3 and Line 1042: I’d like to point out that missense VEP is not necessarily a short-context task. Coding variants require a small protein context but a large genomic context, since the coding sequence is distributed across exons (which are very far away due to large introns).

### Questions
1. The sections on context length extrapolation read a bit disconnected from the rest of the manuscript. It appears to be an improvement on the NT model rather than directly related to the benchmark. If the authors claim it to be a generally applicable method to other DNA LMs, it should be made clear in the writing and preferably applied to at least another model. If it is for a focal investigation on the impact of context size on NT, the results should be more carefully analyzed and discussed.
2. In Table 3, Enformer is not a good baseline for the ClinVar task, since this set only contains missense variants and Enformer is a model focused on the non-coding genome.
3. In Section 3, the authors discussed why several tasks should be considered long-range, but did not discuss why the others are not. It would have been better to also include brief discussions on why those tasks are expected to be performed well with short-range models.
4. Section 3.1.3 and Line 1042: I’d like to point out that missense VEP is not necessarily a short-context task. Coding variants require a small protein context but a large genomic context, since the coding sequence is distributed across exons (which are very far away due to large introns).

### Soundness
3

### Presentation
3

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
This paper proposes a new benchmark for evaluating DNA LMs on tasks with emphasis on long-range prediction, unlike other benchmarks which focus on short sequence tasks (<2k bp). The authors benchmark 4 DNA LMs on 4 tasks in their benchmark (variant effect prediction, gene expression prediction, and cis-regulatory element detection, chromatin feature identification). They compare performance on both zero-shot and full finetune settings. The authors also finetune NucleotideTransformer with extended context length.

### Strengths
- Benchmarks for DNA language models are currently sparse, and this paper does a good job of curating a diverse set of tasks and benchmarking recent DNA LMs.

### Weaknesses
 - A main claim of this paper is that the tasks they curate are long-range tasks, and that they expect that model performance increases with longer context input. The claim that these tasks require long context would be strengthened by an ablation study over different input lengths.

- The authors should be clear that this is a human-only benchmark, ideally in the title and abstract. This is not mentioned until Section 3, and limits the usefulness of the benchmark as many DNA LMs like Evo are trained primarily on microbial sequences.

- Section 4 describes context length extension, specifically using NTK and an attention implementation with sqrt(L) chunks. The latter is not explained in the paper or in the supplement.

-The authors do not explain how the train/test splits are generated. How is train/test leakage avoided? Do they split by sequence similarity thresholds?

- The Evo model (https://www.biorxiv.org/content/10.1101/2024.02.27.582234v2) and Caduceus (https://arxiv.org/abs/2403.03234) should be benchmarked if possible.

### Questions
- Section 4 describes context length extension, specifically using NTK and an attention implementation with sqrt(L) chunks. The latter is not explained in the paper or in the supplement.

-The authors do not explain how the train/test splits are generated. How is train/test leakage avoided? Do they split by sequence similarity thresholds?

- The Evo model (https://www.biorxiv.org/content/10.1101/2024.02.27.582234v2) and Caduceus (https://arxiv.org/abs/2403.03234) should be benchmarked if possible.

### Soundness
3

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
4

### Summary
This paper introduces the Genomics Long-Range Benchmark (LRB), designed to evaluate DNA language models (LMs) on tasks that reflect biologically meaningful long-range interactions. The benchmark includes tasks across variant effect prediction, gene expression prediction, regulatory element detection, and chromatin feature identification.

### Strengths
1. The LRB addresses a critical gap in DNA LM evaluation by focusing on biologically relevant tasks that require long genomic contexts. 
2. The experiments on DNA LMs, including zero-shot and fine-tuning performance across multiple tasks, reveal the strengths and limitations of the models.
3. Fine-tuning recipes and context-length extension methods provide a robust framework for DNA LM evaluation.

### Weaknesses
- Lack of in-depth analysis of the experiments. Why do certain DNA LMs perform well on specific tasks? It is crucial to understand the underlying mechanisms that lead to performance differences, such as the impact of specific architectural choices or pre-training strategies on different tasks. For example, do models with attention mechanisms perform better on tasks requiring long-range dependencies, and how does k-mer tokenization affect performance compared to character-level tokenization?
- Potential unfairness in comparisons. DNABERT and HyenaDNA have significantly fewer parameters compared to NT500M, which may skew results. It would be beneficial to compare models with similar parameter counts where possible, or at least to control for model size by comparing performance across a range of parameter counts within each model family. This would help determine if performance gains are due to architecture or simply model size.
- Missing key long-range baseline LMs. The benchmark lacks important long-sequence models such as Caduceus [1] and Evo [2], which would provide a more comprehensive evaluation. These models have demonstrated strong performance in long-range genomic tasks and should be included for a fair comparison. The absence of these models limits the benchmark's ability to assess the state-of-the-art in long-range DNA modeling.
- Insufficient comparison in context extension experiments. The analysis of TSS distance effects lacks comparisons with other long-sequence models. It is important to compare the performance of context extension methods against other models that are explicitly designed for long-range dependencies, to understand the effectiveness of these methods. For example, how does the performance of the context extension method compare to models like Caduceus [1] on tasks that require long-range context?
- References on benchmarks. In the first paragraph of the Introduction, the reference to ProteinGym [3] should have the publication year 2023 instead of 2024. Additionally, including relevant benchmarks like GenBench [4] and BEACON [5] would improve the coverage of related literature.

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
