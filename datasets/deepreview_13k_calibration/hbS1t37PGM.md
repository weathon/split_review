# Training Universal Text Encoders with Pair Relevance Classification Loss

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
Finetuning large language models (LLMs) using contrastive learning objectives has become the dominant approach for representation learning in general-purpose text embedding tasks. Our work seeks to enable going beyond strictly positive (or negative) pairs of text, to more fine-grained annotations that can capture the nuances of complex language tasks. We propose training text encoders with a simple pair classification loss that utilizes binary cross-entropy on relevance labels. When compared to the standard softmax-based loss for multi-class classification against multiple text alternatives, we find that training with our proposed loss improves the average score across 56 English language tasks of the Massive Text Embedding Benchmark (MTEB), while finetuning the same Meta-Llama-3-8B-Instruct model on the same mix of open datasets. Furthermore, our models excel in the Pair Classification and the Semantic Textual Similarity benchmarks, outperforming many models that are trained on more extensive data. Finally, thorough experiments using graded relevance data from TREC-DL 2023 during training demonstrate that binary cross-entropy provides generalization improvements that the softmax-based loss fails to achieve.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a method to leverage soft relevance scores for text representation learning, addressing limitations in the standard CLIP-style contrastive learning framework. The authors argue that CLIP-style training cannot effectively incorporate relevance scores due to structural constraints in the framework. To address this, they propose using an instance-to-instance binary cross-entropy (BCE) loss with relevance scoring and a logit bias, which they claim can better utilize soft relevance scores without being affected by batch size or long-tail label distributions—issues that can impact traditional CLIP-style training.

### Strengths
1. The paper addresses a significant challenge in contrastive learning: that instance pairs often exhibit relationships between purely positive or negative. By accommodating these "in-between" relevance scores, the method could offer a more nuanced approach to contrastive learning.
2. The core idea of the paper is presented clearly.

### Weaknesses
1. The paper asserts that measuring relevance with softmax-based contrastive learning is challenging; however, existing soft-contrastive methods, such as IW softmax used in the baseline, enable weighting instance pairs by relevance. A discussion comparing this approach to soft-contrastive learning would be beneficial. Specifically, the paper should delve into why the proposed BCE loss is superior to simply weighting the softmax loss with the relevance scores, as the latter seems like a more direct way to incorporate relevance information. The current explanation lacks a detailed analysis of the limitations of weighted softmax in this context.
2. The title emphasizes learning a "universal" encoder, but the paper does not provide specific methods geared toward universal representation learning, which could mislead readers. The paper benchmarks on MTEB, which is a good start, but it does not explain how the proposed method is explicitly designed to generalize across diverse tasks. The term 'universal' implies a more deliberate design for broad applicability, which is not clearly demonstrated.
3. The main contribution—incorporating relevance scores with BCE loss for contrastive learning—yields only modest performance gains over the softmax loss, which may limit the overall impact of the contribution. The performance gains, while present, are not substantial enough to justify the claim of a significant advancement. The paper needs to better articulate the specific scenarios where the BCE loss provides a clear advantage over softmax, beyond the marginal improvements observed in the experiments.
4. While the design is conceptually sound, the function of the logit bias β feels somewhat ad hoc. Its purpose resembles methods aimed at addressing long-tail distributions, and related methods should be discussed to situate this approach within the broader context. The paper should provide a more rigorous justification for the logit bias, explaining why it is necessary and how it interacts with the BCE loss to achieve the reported results. Without this, the logit bias appears as an arbitrary parameter rather than a well-motivated component of the method.

Typo:
Line 303: We propose using Suppose we have...

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes pair relevance classification loss for training text embeddings. The pair relevance classification loss generalizes the sigmoid loss of the SigLIP work, and is a binary cross entropy loss between model prediction and ranking labels. When used with binary labels as most text embedding data, the loss reverse back to the same sigmoid loss as proposed in SigLIP. Compared to the standard contrastive learning loss, the loss falls in the category of point-wise ranking, where the model is optimized against absolute ranking labels instead of relative ranking of different documents. Experiments on the MTEB show the proposed loss leads to better embeddings than the standard contrastive loss. Furthermore, pair relevance classification loss can be naturally used when graded relevance labels are available.

### Strengths
1. The proposed pair relevance classification loss generalizes the sigmoid loss from SigLIP work.
2. This is the first work to demonstrate the pointwise sigmoid loss outperforms the standard contrastive loss for training text embeddings.
3. The proposed loss can better utilize data where graded labels are available.

### Weaknesses
1. The vast majority of existing text training data are of binary labels. For the binary labeled data, the proposed loss reverses back to the sigmoid loss of previous work.
2. For graded labels, this work fails to mention previous work on pointwise ranking which do regression on the absolute relevance labels. For example, see section 2.4 in https://arxiv.org/pdf/2105.11108.
3. The paper does not provide intuitions or analysis why the proposed loss would be better for the binary labeled text data. In the SigLIP work, the postulated benefits are 1) efficient processing enables large batch size in training and 2) robustness against noises prevalent in language-image pretraining data. In this work, the training batch size is relatively small, and it does not demonstrate noise robustness plays any roles in the text domain.

### Questions
The proposed loss falls into the category of pointwise ranking loss. Classic work such as Learning to Rank for Information Retrieval (http://didawikinf.di.unipi.it/lib/exe/fetch.php/magistraleinformatica/ir/ir13/1_-_learning_to_rank.pdf) usually consider pointwise approaches inferior to other methods as they lack the global view. As a matter of fact, I personally tried the sigmoid loss to train text embeddings with large language models before I review this paper, but failed to gain any benefit compared to the standard contrastive loss. Can the authors provide any intuitions why the pointwise loss would be better in this case?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This study proposes a new approach for fine-tuning the universal text encoders using binary cross-entropy loss. Using a simple pair classification loss with binary cross-entropy on relevance labels, the proposed method outperforms the standard softmax-based loss, improving average scores in the MTEB benchmark evaluations. Tested on the Meta-Llama-3-8B-Instruct model, this binary cross-entropy approach excels in benchmarks for Pair Classification and STS as well as offering better generalization advantages than softmax-based loss.

### Strengths
See the summary.

### Weaknesses
In general, the BCE loss has been previous studied in ML application literature as author described in Appendix (extended related work) and the experiments are relatively for small set of models and mteb dataset. In addition, the reported MTEB accuracy number is much lower the top-performing models in the MTEB leaderboard. More comments are included in questions.

### Questions
- What is the theoretical reasoning behind the claim that BCE loss outperforms softmax-based loss in fine-tuning embedding models?
- Besides LLM2VEC, can this loss function be used effectively with other embedding models, such as transformer-encoder based models like e5?
- Is this loss advantageous not only for the Llama model but also when applied to other foundational LLMs like Mistral-7b or Qwen-7b?
- The evaluation results are based solely on the MTEB dataset. Since the training data overlaps with MTEB’s training sets, the fine-tuned model might be overfitted to MTEB. Could you provide zero-shot evaluation results, for instance, using the AIR-Benchmark (https://github.com/AIR-Bench/AIR-Bench)?
- What is the theoretical intuition behind the proposed loss’s batch robustness?
- Does incorporating BCE loss also enhance accuracy when non-retrieval datasets (e.g., clustering, classification, STS) are included in the training data?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper adopts a binary classification loss, introduced by SigLIP, to enhance the text embedding learning domain. It follows the same setup as LLM2Vec, with only modifying the original CLIP-style contrastive loss to SigLIP-style binary classification loss. The authors carefully ablate the hyperparameters of this loss and demonstrate that the SigLIP loss brings moderate improvements over CLIP loss on MTEB, STS, and TREC-DL datasets.

### Strengths
- Technical sound: The authors conduct experiments on well-established benchmarks, and I verified that the reported baseline numbers match those in the corresponding papers. They also perform extensive ablation studies to explore the impact of SigLIP loss hyperparameters on final performance.
- Paper well written: The paper is generally well-written and easy to understand.

### Weaknesses
 - Limited contribution: The main concern is the lack of technical novelty. The paper only adapts the SigLIP loss for text embedding learning, strictly following the LLM2Vec setup, with the SigLIP loss as the only modification. This approach, while technically sound, essentially amounts to a direct application of an existing loss function to a new domain without introducing any novel mechanisms or insights into the underlying problem. The core idea of using a binary classification loss for representation learning is not new, and the paper does not sufficiently explore the nuances of this adaptation in the context of text embeddings.
- Minor improvements: The improvements achieved by SigLIP loss are minimal compared to the original CLIP loss. The reported gains on MTEB, STS, and TREC-DL datasets are not substantial enough to justify the introduction of a new training paradigm. The lack of significant performance boosts raises questions about the practical utility of the proposed method, especially considering the computational overhead associated with hyperparameter tuning of the SigLIP loss.
- Lack of insightful analysis: The paper does not provide in-depth analysis, such as why SigLIP is a preferable loss compared to CLIP loss, why it performs better on MetaLLaMA3 but not ShearedLLaMA3, or why it enhances graded relevance scores in retrieval settings. The absence of a detailed investigation into the underlying reasons for the observed performance differences limits the scientific contribution of the work. The paper would benefit from a more thorough exploration of the loss landscape and the specific properties of the SigLIP loss that lead to its performance characteristics.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
1
