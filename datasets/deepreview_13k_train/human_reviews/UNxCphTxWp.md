# Programming Every Example: Lifting Pre-training Data Quality like Experts at Scale

- Decision: Reject
- Scores: 5, 8, 6, 5

## Abstract
Large language model pre-training has traditionally relied on human experts to craft heuristics for improving the corpora quality, resulting in numerous rules developed to date.
However, these rules lack the flexibility to address the unique characteristics of individual example effectively.
Meanwhile, applying tailored rules to every example is impractical for human experts.
In this paper, we demonstrate that even small language models, with as few as 0.3B parameters, can exhibit substantial
data refining capabilities comparable to those of human experts.
We introduce Programming Every Example~(\method), a novel framework that treats data refinement as a \emph{programming task}, enabling models to refine corpora by generating and executing fine-grained operations, such as string normalization, for each individual example at scale.
Experimental results show that models pre-trained on \method-curated data outperform either original data or data filtered by other selection methods by more than \m{2\%} across various downstream benchmarks.
Its effectiveness spans various model sizes and pre-training corpora, including C4, \redpj, and \fineweb.
Furthermore, \method exhibits significant potential in domain-specific continual pre-training: without 
domain specific design, models trained on \owm refined by \method outperform human-crafted rule-based methods, improving average accuracy by \m{\mathbf{7.6\%}} over \mistral-7B, with \m{\mathbf{14.6\%}} for \llamaii-7B and \m{\mathbf{20.3\%}} for \codellama-7B, all within \m{\mathbf{10}}B tokens to be comparable to models like \llemma{}-7B trained on \m{\mathbf{200}}B tokens.
Further analysis highlights that \method significantly saves training FLOPs, offering a promising path for efficient LLM pre-training.
We are open-sourcing \method with \m{\mathbf{\ge100}}B corpus, models, and sharing all training and implementation details for reproducible research and future innovation.
\begin{itemize}
    \item \small{\huggingface \textbf{HF Repo}: \url{https://huggingface

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents Programming Every Example (PROX), a framework that redefines language model pre-training by treating data refinement as a programming task. PROX allows even small language models (as few as 0.3B parameters) to perform fine-grained data operations, achieving performance comparable to human experts. Models trained with PROX-curated data outperform those trained on original or traditionally curated data by more than 2% across ten benchmarks. It is effective with different model sizes and corpora, demonstrating significant potential in domain-specific tasks and reducing computational costs.

### Strengths
**A highly complete paper, and I appreciate it along with your hard work.**

1. The paper is clearly articulated with intuitively designed charts that help readers easily understand the problems being addressed, the research motivation, and the methods employed. 

2. It is detailed in scope, including appendices with textual explanations of document/block-level programming, algorithm flowcharts, prompts used, pretraining details, baseline, downstream task introductions, and case analyses, all of which are comprehensive. 

3. The experiments are rich in content, especially the appendices, and features beautifully crafted charts. 

4. The field this paper focuses on is crucial to the LLM community -- "how to improve the quality of pretraining data."

### Weaknesses
1. **This paper raises several concerns for me:**

    ``The methodology can be summarized as follows: it utilizes LLAMA's annotated pairs (doc, program) to fine-tune a small model Prox with approximately 0.3B parameters, serving as a proxy. Based on a vast corpus of pre-trained documents, Prox generates Python function calls to conduct document-level encoding (discard or retain) and chunk-level encoding (discard, retain, normalize).``

- a. Firstly, while the goal of the paper is to balance data processing efficiency and enhance data quality, the introduction of Prox as a proxy to call Python functions might add extra computational cost, potentially undermining the practical of this approach. A comparative analysis of time overhead with other methods would strengthen the argument for the effectiveness of this approach.

- b. Furthermore, if direct application of Python functions achieves the document-/chunk-level heuristic optimizations as proposed, how does this alternative compare to Prox in terms of performance?
Because after all, the processes of discarding or retaining documents and chunks, and normalizing chunks (such as top menus, navigation bars, buttons, HTML elements, links, and footers) can be addressed using existing Python rules (as referenced with C4, Gopher, and RedPajama).

- c. Additionally, how do the document- and chunk-level programming rules differ from existing heuristic rules, particularly in relation to the above mentioned processes (at paragraph b) and education scores, considering related research such as [1] and [2] have already proposed similar concepts?

2. The experimental results in the paper need further development. In Table 2, only a 750M LLAMA model is used for pretraining on 26B data, while the minimal data volume and model size in standard practice are at least a 1.3B model and 30B data. I believe Prox could demonstrate more significant improvements in in-context learning (ICL) capabilities with larger data scales and model sizes.

3. Some experimental comparisons require clarification. For example, in Table 5, the comparison on domain-specific data tasks should not be between CPT and the BASE model. Instead, it should be between randomly sampled data and Prox-refined data of equivalent volume size, with two BASE models trained from scratch.

4. The current paper only examines mathematics as a specific domain. Expanding the scope to include more vertical fields such as finance, education, or medicine would be beneficial.

### Questions
Please Check Weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose ProX, a method for data filtering and synthetic data generation for improving the quality of large pretraining corpora. ProX proposes to fine-tune a small language model to produce a “program”, which is a sequence of one or more filtering or normalization operations applied at the document and line level. These programs are synthesized and executed for each document in the corpus, which results in a smaller higher quality subset. The authors demonstrate that ProX yields significant improvements in pretraining and domain-specific continual pretraining in both accuracy and training efficiency across numerous baselines.

### Strengths
- The paper introduces ProX, which is a novel method to improve training data quality using small language models to synthesize and execute short data refinement programs, rather than using static rules or large model data synthesis.
- Framing data filtering and synthetic data generation as a programming task that can be performed by small models is a creative contribution that has not been explored in previous work
- Prox-D and Prox-D+C outperform all heuristic and model based data selection baselines and improve pretraining efficiency. The empirical validation is comprehensive, testing the method across multiple model sizes (350M to 1.7B), different pre-training corpora (RedPajama-V2, C4, FineWeb), and domain-specific applications (OpenWebMath).
- The method shows significant gains in accuracy and efficiency for domain specific continual pretraining, with up to a 20x reduction in compute. The effectiveness of synthesizing example-specific filtering programs shows especially here, as the method can synthesize domain-specific filtering rules.
- Although there is additional computational overhead from running inference of the refining model to generate the programs, this rapidly decreases as a proportion of the total pretraining FLOPs as the pretrained model gets larger. The method shows a 67% FLOPs reduction in pretraining to a given accuracy for a model as small as 1.7B.
- The paper is well structured and clearly written, with nice looking and clear figures to explain the method and results.

### Weaknesses
 - The paper is missing a qualitative analysis of the programs generated by ProX. It could benefit from:
  - Examples of wrong programs generated by ProX and an analysis of the common failure modes
  - Statistics on the complexity of the programs (e.g. distribution of function calls per document)
  - An analysis of how program quality varies across different domains
  - A discussion of potential safety issues since programs may modify data in unintended or harmful ways

- The paper could benefit from comparison to simpler baselines, like binary classifiers (e.g. fastText) for quality filtering.

- The paper could explore expanding the space of programs, for example by inclusion of additional operations like text transformations, or composing multiple operations.

### Questions
Did you compare Prox-D against an n-gram based filtering method like fastText? DataComp-LM (Li et. al.) find that fastText-based quality filtering was the best performing method they tried, outperforming the Gopher and C4 filtering rules, which are also used as baselines in this paper.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper "Programming Every Example: Lifting Pre-training Data Quality like Experts at Scale" introduces ProX, a framework leveraging small language models to refine large-scale pre-training data through program generation. ProX aims to enhance the quality of training data by executing fine-grained operations on individual examples. The authors demonstrate significant improvements in pre-training efficiency and model performance across various benchmarks and model sizes. Notably, ProX can achieve remarkable gains in domain-specific continual pre-training tasks, as the authors show with OpenWebMath.

### Strengths
* Novel Chunk-Level Rewriting Technique: A novel and fine-grained approach that moves beyond binary keep/dismiss judgments, allowing deterministic edits to individual chunks of text. This method is validated through robust ablation studies, proving its efficacy in improving pre-training data quality.
* Efficient Use of Compute: By leveraging small language models (0.3B parameters) for data refinement, ProX achieves substantial performance improvements with lower computational costs. This efficiency is especially noteworthy in domain-specific tasks like OpenWebMath, where ProX yields remarkable accuracy gains.
* Comprehensive Ablations: The authors tested ProX across multiple model sizes (0.3B to 1.7B) and pre-training corpora (C4, RedPajama-V2, FineWeb), with significant performance enhancements demonstrated consistently. The results show that even smaller refining models can produce high-quality pre-training data.
* Important Practical Implications: The framework offers a scalable solution to pre-training data refinement, which can be particularly valuable in scenarios where human expert intervention is impractical. ProX’s deterministic chunk-level edits contribute to a more nuanced and flexible data curation process.

### Weaknesses
 * Base Dataset Selection and Novelty: The exclusive reliance on older datasets like C4 and RedPajama limits the relevance of the findings. While the results on OpenWebMath are impressive, it would be more compelling to see ProX applied to modern datasets such as FineWeb-edu or DCLM-base, which have undergone extensive refinement. The lack of experiments on these more recent, high-quality datasets makes it difficult to assess the true potential of ProX in state-of-the-art scenarios.
* Document-Level Refinement: The document-level component of ProX appears to be a straightforward application of FineWeb-edu’s filtering techniques, reducing its novelty. The primary innovation lies in the chunk-level refinement, which could be more explicitly distinguished from the document-level methods. The paper does not sufficiently articulate how the document-level filtering integrates with the chunk-level edits, and whether there are any synergistic effects.
* Evaluation Methodology: The emphasis on zero-shot performance may not fully capture the advantages of ProX, especially since the refining models are not fine-tuned for instruction-following tasks. Few-shot performance with higher n might provide more insightful comparisons. The paper should also consider evaluating the models on a wider range of tasks that are more sensitive to data quality, such as those involving reasoning or complex language understanding.
* Exclusion of Base Model Training FLOPs: The paper excludes the computational cost (approximately 5.3e19 FLOPs) for training the base model used to create the refining model. This is significant, as it constitutes nearly half the total compute, raising concerns about the true efficiency gains. The authors should have explored using an existing pre-trained model to substantiate ProX’s cost-effectiveness. The current approach makes it hard to assess the practical applicability of the method.
* Context Window Considerations: Given that ProX needs to refine long documents, the context window of the refining model is a critical factor. The paper does not provide sufficient details on how the model handles long contexts, which could impact its practical utility. The paper should detail the specific truncation or summarization methods used, and how these choices affect the quality of the refinement process.

### Questions
1. Generalizability to Highly Refined Datasets: How would ProX perform when applied to datasets that are already highly refined, such as FineWeb-edu or DCLM-base? Are there diminishing returns when starting with higher-quality corpora?
2. Evaluation Choices: Why did the authors prioritize zero-shot performance for their evaluation? Wouldn't few-shot performance offer a more nuanced understanding of ProX’s impact, especially for instruction-following tasks?
3. Compute Cost of Refining Model Training: Why did the authors not also use an existing pre-trained model for the refining task? This could have significantly reduced the compute cost. Additionally, what measures were taken to address the long context requirements of creating refinement programs for lengthy documents?

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
The authors introduce a framework called PROX for refining data quality in large language model (LLM) pre-training. This framework claims to address limitations in traditional, heuristic-based data-cleaning methods, which often lack flexibility and are labor-intensive.

### Strengths
The advantage of this paper is its novelty in transforming data cleaning into a programmable task, which shifts away from traditional, rigid heuristic-based methods. By treating data refinement as a series of programmatically generated actions, the framework enables language models to apply tailored operations to each example, such as string normalization and noise filtering, with high precision.

### Weaknesses
1. The first limitation is that the amount of pre-training data used in the authors' experiments is insufficient, falling far short of what would be needed to fully support their claims. It’s highly possible that, with more extensive training, the advantages of the proposed method might diminish or even disappear. Specifically, the models are trained on a relatively small number of tokens compared to state-of-the-art models, which raises concerns about the generalizability of the results. The authors should have used a dataset size that is more representative of real-world pre-training scenarios to validate their method's effectiveness. The lack of training on a larger corpus makes it difficult to assess the true potential of the proposed framework.

2. The second limitation is that using a model—especially a smaller one—for data selection introduces issues like hallucinations, bias, and the omission of less common information during the pre-training phase. These issues are difficult to resolve and can become deeply embedded in the foundation model. In fact, pre-training should ideally be a robust modeling of the real world, and relying on a smaller model for data refinement may skew this representation, undermining the model’s ability to capture a true and comprehensive understanding of diverse real-world contexts. The use of a smaller model for data selection and refinement introduces a potential bottleneck, where the biases and limitations of the smaller model are transferred to the larger pre-trained model. This could lead to a situation where the pre-trained model is not as robust or generalizable as it could be.

### Questions
Each time the pre-trained model is updated, the entire pre-training dataset needs to be reprocessed, which is highly GPU-intensive. Do the authors have any alternative solutions to address this computationally expensive process?

### Soundness
2

### Presentation
2

### Contribution
2
