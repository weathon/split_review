# Efficient Long-range Language Modeling with Self-supervised Causal Retrieval

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Recently, retrieval-based language models (RLMs) have received much attention. However, most of them leverage a pre-trained retriever with fixed parameters, which may not adapt well to causal language models. In this work, we propose Grouped Cross-Attention, a novel module enabling joint pre-training of the retriever and causal LM, and apply it to long-context modeling. For a given input sequence, we split it into chunks and use the current chunk to retrieve past chunks for subsequent text generation. 
Our innovation allows the retriever to learn how to retrieve past chunks that better minimize the auto-regressive loss of subsequent tokens in an end-to-end manner.
By integrating top-$k$ retrieval, our model can be pre-trained efficiently from scratch with context lengths up to 64K tokens. 
Our experiments show our model, compared with long-range LM baselines, can achieve lower perplexity with comparable or lower pre-training and inference costs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to build a differentiable retrieval-based transformers (DRT) that optimizes the retriever together with generation in an end-to-end manner. It proposes to replace the Chunked Cross Attention with Group Cross Attention that allows the gradient to back-propagate to the retriever so that retriever can be trained as well where in previous work, the retriever is not trained. The evaluation on PG19 and ArXiv-math shows the effectiveness of the proposed method while being much faster than landmark attention.

### Strengths
The authors successfully trained a differentiable retrieval-based transformers where adding grouped cross attention shows better perplexity compared to the baseline model.

### Weaknesses
1. All the models are trained using very small model size (i.e. 133M), compare to the popular LLMs, e.g. 1B or 7B model size. The improvement could diminish when scaling to larger model sizes and a larger model size should be reported to make the claim more convincing.
2. It is not surprising that the model gets better perplexity by using more compute. Existing SOTA models mostly choose to scale the data size to better utilize the compute. Thus, a more interesting research question could be that given fixed amount of compute, should we allocate the extra compute to train more data or change the architecture to a differentiable retrieval-based transformer.

### Questions
1. Will the improvement over baseline model diminish when scaling up the model size?
2. Will the authors open source the codebase? Making it open source might benefit more researchers.

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
3

### Summary
This paper proposes Differentiable Retrieval-based Transformers (DRT). Following a previous line of work on retrieval-augmented LMs (e.g. RETRO and RPT), the key novelty of this paper is Grouped Cross Attention – instead of concatenating top k retrieved units, the authors proposed to use retrieval score to fuse outputs derived independently from each unit in the top K. The authors pre-train a DRT model and several baselines (RPT, Landmark Attention, etc.) from scratch and conduct perplexity evaluation on long-range language modeling tasks. Results show that DRT obtains roughly on-par or better performance compared to the baseline, with better performance as the context length increases.

### Strengths
* The paper proposes a method to train retrieval-augmented LMs, aiming to improve LM’s capability to handle long context, which is a practical use-case and active research area.
* The paper contains comprehensive experiments against several baselines as well as ablation studies.

### Weaknesses
While I appreciate the inclusions of different baselines (RPT, Landmark attention) and the motivation of training RALM in an end-to-end manner,  I am finding it a little bit hard to situate this paper against previous work  and the major benefit of the proposed method:
* It seems like the authors are advocating for the use of GCA, which enables training time efficiency due to end-to-end training. Yet, if I am reading table 1 correctly, it seems like baseLM (+2 layers) achieve lower perplexity on PG19 consistently compared to DRT and also with lower training wall clock time. 

* It is also unclear how to isolate the benefit of GCA, given that the baselines have several other different design choices (RPT might be the closest, but it doesn’t use the landmark tokens as this paper, nor grouping the layers) and there is no ablation of using GCA v.s. a different method to train the retrieval module (e.g. the method employed by the RPT model which involves using a reference LM to score the retrieved chunks). It would be helpful to include an ablation study on GCA, besides those that are already included in Table 1.



### Questions
* The original RPT paper uses representation from the lower layer to retrieve chunks for upper layers, and train the retriever using a reference model. This paper implements RPT using a contreiver to retrieve chunks, how is that exactly done, i.e. what is the representation for the query and the chunks? And is a fixed contriever used? If so, this seems like a weaker baseline than the originally-proposed RPT, it would be helpful to include a discussion on this.

* The paper mentioned that the proposed method enables “multi-hop retrieval” several times in the paper (e.g. second paragraph in section 3.1), what does this mean and what’s the experiment that demonstrates the ability?

* It seems like the proposed method perform better on the Arxiv-math dataset compared to the PG-19 dataset and it'd be helpful to include analysis to understand the reason. It'd also be helpful to experiment on other domains that are tested in previous work, such as Code [0] and books [1].

[0] https://arxiv.org/pdf/2306.13421
[1] https://arxiv.org/pdf/2402.16617

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new approach to enhancing the efficiency and effectiveness of retrieval-based language models through a mechanism called Grouped Cross-Attention (GCA). The authors address the limitations of existing models, which typically rely on separately pre-trained retrievers with fixed parameters that may not optimally align with causal language modeling objectives. The chunk selection part of GCA can be optimized with language modeling loss, and this method can be implemented based on Flash-attention 2, which remarkably reduces the training and inference cost.

### Strengths
1. the  proposed GCA method  facilitates the joint pre-training of the retriever and the causal language model in an end-to-end manner. This allows the retriever to dynamically learn to select past chunks.
2. The integration of top-k retrieval and hardware-aware implementations (based on FlashAttention-2) ensures that DRT achieves lower perplexity with reduced training time, outperforming  baselines like Retrieval-Pretrained Transformer and Landmark Attention.
3. During inference, DRT employs memory offloading techniques to manage GPU memory usage efficiently, substantially reducing the memory footprint while maintaining high performance.

### Weaknesses
1. The proposed GCA module is difficult to understand because the authors do not provide sufficient motivation for the design of each step. Additionally, there are alternative methods to implement the differentiable operation, but the paper does not include any analysis or comparison of these alternatives. This lack of clarity and justification makes it challenging for the community to follow and reproduce the work.
2. My primary concern is the lack of scalability. Most of the baselines use models with fewer than 200M parameters. The authors mention having access to 8 A100 GPUs, which should enable the training of larger-scale models. I believe this method could benefit from being adopted with a fine-tuning approach, such as CEPE[1], in combination with existing  LLMs like Llama to demonstrate its effectiveness at a larger scale.
3. The authors only provide experiments on language modeling. Evaluating the method across a diverse range of downstream tasks would allow the community to better assess the overall effectiveness and applicability of this work.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a novel long-range language model called Differentiable Retrieval-based Transformer (DRT), which introduces a Grouped Cross-Attention (GCA) module to enable joint pre-training of the retriever and causal language model. The main innovation lies in splitting input sequences into chunks and dynamically retrieving relevant past chunks to enhance the prediction of subsequent tokens. The retriever learns how to minimize the auto-regressive loss by retrieving past chunks in a differentiable manner, allowing more efficient training with context lengths up to 64K tokens.
With GCA, the model maintains random-access flexibility during auto-regressive generation while reducing memory and computational costs. Experiments show that DRT outperforms baseline long-range language models by achieving lower perplexity, faster inference speeds, and more efficient memory usage.

### Strengths
1. The introduction of Grouped Cross-Attention enables joint optimization of the retriever and language model, solving the issue of fixed retriever parameters in traditional models and making the retriever more adaptive to causal language modeling tasks.
2. The model minimizes memory consumption by performing chunk-based retrieval and leverages hardware optimization to accelerate both training and inference.
3. By offloading historical chunk representations to CPU memory and reloading them as needed, the model significantly reduces GPU memory usage and achieves up to 100 times faster inference compared to existing baselines.

### Weaknesses
The method requires pre-training from scratch, as it cannot simply add modules to fine-tune existing models, leading to a substantially higher computational cost.

### Questions
1. In Figure 2, the tokens in chunk c7 rely on the relevance score from the LMK in chunk c6 regarding the previous chunks instead of from the token in c7 regarding the previous chunks. Is there any inconsistency?
2. As noted in previous work, there are some problems associated with using PPL as a metric. Do you have any other tasks or metrics that could demonstrate the effectiveness of your method?
3. Could you provide the performance results of your model on long-context benchmarks such as LongBench?

### Soundness
3

### Presentation
3

### Contribution
2
