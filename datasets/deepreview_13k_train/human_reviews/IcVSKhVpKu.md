# Improving Sequence Level Distillation through Hidden State Matching

- Decision: Accept
- Scores: 3, 8, 6

## Abstract
Hidden State Matching is a prominent technique in the knowledge distillation of language models. Most existing methods follow DistilBERT in using a cosine loss to encourage similarity between the student and the teacher's hidden states. However, the cosine loss restricts the architecture and dimensionality of the student, thereby severely limiting the compression ratio. We present a different technique using Centered Kernel Alignment (CKA) to match hidden states of different dimensionality, allowing for smaller students and higher compression ratios. We show the efficacy of our method using encoder--decoder (BART, mBART \& T5) and encoder-only (BERT) architectures across a range of tasks from classification to summarization and translation. Our technique is competitive with the current state-of-the-art distillation methods at comparable compression rates and does not require already pretrained student models. It can scale to students smaller than the current methods, is no slower in training and inference, and is considerably more flexible.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
- This paper presents an approach to knowledge distillation that allows matching latent representations between different dimensionalities by using centered kernel alignment (CKA) instead of cosine similarity.
- Comprehensive experiments on encoder-decoder models and masked language models confirmed that the proposed method consistently achieves higher performance compared to simple baselines, such as cases without added loss or with linear projection.

### Strengths
- The experiments are comprehensive, covering encoder-decoder models (BART, mBART, T5) and masked language models (BERT). The task settings range from fine-tuning on specific tasks to instruction tuning. This experimental section is valuable for readers interested in knowledge distillation in similar settings.
- The CKA used is simple, and the authors utilize a linear kernel (Line 108). This choice is expected to make the implementation easier to reproduce and facilitate scalability in training.

### Weaknesses
 - There is limited mention of related work in knowledge distillation, making it difficult to assess the value of this study. For instance, there is no reference to research that incorporates modifications to divergence (e.g., Wen et al. ACL 2023, Gu et al. ICLR 2024) or to the distillation of causal language models, which is extensively discussed in Xu et al. (arXiv:2402.13116) and is currently of significant interest to readers.
- The tasks addressed in this study do not align with the practical use cases of modern language models. For example, summarization is often performed using causal language models today, and instruction tuning is naturally suited for causal language models rather than encoder-decoder models. While papers with significant theoretical contributions may be accepted even if their experimental settings are somewhat “toy” or “outdated,” this paper does not focus on theory (there is no theoretical section). Instead, it proposes that replacing cosine similarity with linear CKA can improve knowledge distillation in various practical settings. The value of empirical studies is considerable, and this topic is indeed appealing. However, given that the experimental setup feels somewhat outdated, it may not align well with ICLR—a leading conference for representation learning.

### Questions
- Linear CKA is equivalent to the RV coefficient and can be thought of as similar to Pearson correlation. Is it possible to provide any reasoning or justification for why this method is effective?
- Additionally, is there a reason why linear CKA performs better than simple regularization techniques (e.g., weight decay on the student side), including methods that adjust divergence? In practice, does it empirically outperform basic or current regularization methods?

### Soundness
2

### Presentation
2

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
This paper looks at improving distillation between a teacher and student model using Centered Kernel Alignment (CKA). The main benefit of this is that it allows for the hidden dimension to be a different size than most other distillation methods used today and is much more flexible. Overall, this is a nice approach with interesting use of isotropy and math that makes it a valuable insight to the field.

Experiments were done on encoder and encoder-decoder models (BART, mBART, BERT, T5) and the results on three different NLP tasks all justified the method. It would have been nice to see an experiment on a decoder-only architecture, as well as experiments on larger versions of the models discussed, but none of these downsides are enough for me to lower my review score. I’m also not super well-versed in the distillation literature so there is a chance that there are additional baselines that should have been considered that I’m not aware of, but the current experiments show the benefit of the method.

### Strengths
Really interesting application of CKA to fix a problem with distillation and make it much more general.

### Weaknesses
Larger versions of BART or mBART for at least one experiment would have been nice.

### Questions
I think of distillation being useful for very large models, but the current teacher models are relatively small. What happens if you try it on a larger model?

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
3

### Summary
The paper proposes a novel technique for knowledge distillation (KD) in LLMs using Centered Kernel Alignment (CKA) to address limitations in hidden state matching. Traditional methods rely on cosine loss, which restricts the student model's architecture to match the teacher's dimensions. This paper introduces CKA to match hidden states of different dimensionalities, enabling higher compression ratios and allowing more compact and efficient student models.

The authors tested their approach on various NLP tasks:
- Summarization: Using BART on CNN and XSum datasets, evaluated by ROUGE scores. 
- Machine Translation: Tested mBART with multilingual data and evaluated on EN-RO (WMT16) and EN-FR (IWSLT2017) datasets with BLEU scores.
- Classification: Used BERT on the GLUE benchmark for classification tasks, comparing with linear projection and cosine-based baselines.
The CKA-based student models consistently outperformed models with other hidden state matching.

### Strengths
The method is innovative, offering an effective alternative to traditional cosine loss by using CKA for hidden state matching, which enables distillation with flexible model architectures. This approach allows for higher compression ratios and more adaptable student models, overcoming limitations of previous distillation methods. 
Additionally, while most other KD methods overlook computational complexity, the authors present techniques that reduce inference times while maintaining competitive accuracy. 
The performance improvement is substantial.

### Weaknesses
 - although the authors conduct experiments across three tasks, this is relatively limited compared to other KD studies. I would encourage the authors to expand their evaluation to cover more tasks within the GLUE or SuperGLUE benchmarks for a more comprehensive analysis. Specifically, the paper would benefit from including a more diverse set of classification tasks, such as those that evaluate logical reasoning or natural language inference, to demonstrate the robustness of the proposed method across different types of semantic understanding.
- the teacher models used in this paper are relatively small (e.g., BART, T5, and BERT), whereas the current research trend is increasingly focused on larger models (e.g., over 7 billion parameters) like LLaMA, which have stronger pre-training capabilities. It would be insightful to see whether the proposed method can sustain similar performance gains with larger models, as this would make the findings more applicable to the broader research community. The paper should address the scalability of the CKA approach to models with significantly larger parameter counts and different architectural designs, as the computational cost of CKA might become a bottleneck.
- the authors appear to primarily focus on methods involving hidden state matching. I would suggest including comparisons with other methods based on KL divergence or alternative distillation losses to provide a more thorough context for the proposed approach. Specifically, the paper should compare the performance of CKA-based hidden state matching with other distillation techniques that directly minimize the divergence between the teacher's and student's output distributions, such as using KL divergence on the logits, to provide a more comprehensive evaluation of the proposed method's effectiveness.

### Questions
n/a

### Soundness
3

### Presentation
3

### Contribution
2
