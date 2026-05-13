# SpikeBERT: A Language Spikformer Learned from BERT with Knowledge Distillation

- Decision: Reject
- Scores: 8, 8, 3

## Abstract
Spiking neural networks (SNNs) offer a promising avenue to implement deep neural networks in a more energy-efficient way.
However, the network architectures of existing SNNs for language tasks are still simplistic and relatively shallow, and deep architectures have not been fully explored, resulting in a significant performance gap compared to mainstream transformer-based networks such as BERT.
To this end, we improve a recently-proposed spiking Transformer (i.e., Spikformer) to make it possible to process language tasks and propose a two-stage knowledge distillation method for training it, which combines pre-training by distilling knowledge from BERT with a large collection of unlabelled texts and fine-tuning with task-specific instances via knowledge distillation again from the BERT fine-tuned on the same training examples.
Through extensive experimentation, we show that the models trained with our method, named SpikeBERT, outperform state-of-the-art SNNs and even achieve comparable results to BERTs on text classification tasks for both English and Chinese with much less energy consumption.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose SpikeBERT, a spiking neural network (SNN) architecture for language tasks. SpikeBERT extends and improves Spikformer architecture to process text instead of images. It replaces certain modules in Spikformer to make it suitable for language tasks.
The approach uses a two-stage knowledge distillation method to train SpikeBERT: First stage is pre-training distillation using a large unlabeled corpus to align embeddings and features. Second stage is task-specific distillation using a fine-tuned BERT on a downstream task as teacher. The model is evaluated on 6 English and Chinese text classification datasets: it outperforms prior SNN methods and achieves comparable accuracy to BERT. The estimated theoretical energy consumption is much lower for SpikeBERT as compared to traditional approaches.

### Strengths
Advantages:
Uses a highly scalable Transformer-based architecture as the backbone and outperforms prior SNN methods by 3.49% on average across 6 datasets.
Two-stage distillation allows pre-training on large unlabeled data.
Feature alignment loss aligns hidden representations.
Data augmentation further facilitates distillation.
Evaluated on diverse English and Chinese datasets: works well for both English and Chinese text classification.
Significantly reduces theoretical energy consumption (by 27.82% compared to fine-tuned BERT).

The claims are reasonably supported by the results. The proposed SpikeBERT outperforms prior SNN methods significantly and achieves comparable accuracy to BERT on multiple datasets. Ablation studies provide insights into model architecture and training.

### Weaknesses
Potential weaknesses include:
The method relies on the teacher ANN, so can not learn directly from the data. This reliance on a pre-trained ANN limits the potential for the SNN to discover novel representations or learn directly from the temporal dynamics of the input data, potentially hindering its ability to generalize beyond the teacher's knowledge.
The method does not address zero-shot generalization to novel language tasks, which is the main appeal of the LLMs. The focus on task-specific fine-tuning limits the model's applicability to new tasks without retraining, which is a significant limitation compared to the zero-shot capabilities of large language models.
Fails to capture fine-grained word semantics well. The spiking nature of the model and the distillation process may lead to a loss of fine-grained semantic information, potentially impacting performance on tasks that require nuanced understanding of word meanings and relationships.
Requires GPUs with large memory due to additional time dimension. The need for large GPU memory during training due to the added time dimension can limit the scalability of the approach and make it difficult to train on resource-constrained environments.
Energy reduction based on theoretical estimates, actual hardware measurements would be more compelling. The energy efficiency claims are based on theoretical calculations, and actual hardware measurements would provide more concrete evidence of the model's practical energy savings.

### Questions
The approach was evaluated on datasets created for ANNs, not neuromorphic data. It would be interesting to consider using e.g. a neuromorphic cochlea for speech signal.
Adding scaling experiments would be helpful - trying bigger versions of SpikeBERT with more layers, heads and timesteps to explore the scaling law.
It would be helpful to provide visualizations of the learned spike patterns to offer insights into model operation and interpretability.
How would the chioce of alternate surrogate gradient functions would impact training convergence and accuracy?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes SpikeBERT, a spiking BERT model designed for language tasks based, and describes a two-stage distillation method employed in its training.

The authors conduct experiments on several text classification tasks on English and Chinese datasets. The results show that SpikeBERT outperforms state-of-the-art spiking neural networks and achieves comparable results to BERT on text classification tasks for English and Chinese, while consuming significantly less energy.

### Strengths
1. The authors provide the necessary background on spiking neural networks (SNNs) and Spikformer architecture.

2. This work is the first Transformer-based SNNs for language tasks, and achieve state-of-the-art performance on text classification tasks.

3. The authors present an ablation analysis for all their contributions, and compare SpikeBERT with other BERT variants like TinyBERT and DistilBERT on Appendix.

### Weaknesses
1. Although SNNs can reduce the energy consumption when inference, the proposed two-stage distillation method may lead to more energy costs when training. Can you explain this matter?

2. In Figure 3(b), it seems there are no emergent abilities in the SpikeBERT, which is different from non-spiking large language models.

### Questions
Q: I wonder why the authors choose BERT as their teacher model. 

If the authors can respond reasonably to all my questions and comments, I will improve the score of this manuscript.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a spiking neural network variant of BERT called SpikeBERT, thereby employing knowledge distillation using BERT as the teacher model. The main advantage of SpikeBERT compared to vanilla BERT seems to be that it is consuming less “energy” (measured in mJ).

### Strengths
- **Table 2**: It’s interesting and promising to see that SpikeBERT has much lower energy consumption than FT BERT.


- **Section 4.5**: I appreciate the comprehensive ablation study that was performed on the hyperparameters. It’s good scientific practice to scrutinize the impact/effect of different hyperparameters.

### Weaknesses
 - **Contributions**: I think contribution 2 is misleading. While the authors show that their model performs better than existing SNN methods, their method performs on par with a simple TextCNN (from **ten** years ago) which I think is computationally much less expensive than their whole pre-training and fine-tuning pipeline because TextCNN is a much smaller architecture whose outputs are non-contextual/static word representations that can easily be pre-computed.

- **Section 3**: The entire “pre-training + knowledge distillation + fine-tuning” pipeline appears to require a vanilla BERT model that has previously been pretrained on a large language corpus as is standard. If you rely on BERT, why would I not “just” fine-tune or probe BERT instead of applying your pipeline? What is the advantage here? The authors do not justify the need for such a complex pipeline when simpler methods exist.


- **Notation/Math**: The math and notation in Section 3 are a bit sloppy and not very precise. For example, the description of the spike generation process lacks clarity, and the equations do not fully explain the temporal dynamics of the spiking neural network. The use of generic terms without proper definitions makes it hard to follow the technical details.


- **Table 1**: The results in Table 1 are misleading. The authors bold-faced their model’s performances. However, “FT BERT” (which is clearly not SOTA anymore on these tasks) achieves much stronger performance than their model across all reported datasets. Moreover, TextCNN --- which was one of the **first** CNN models for text sequences and whose representations are non-contextual/static word representations --- shows better performance on two datasets (Subj and ChnSenti) and only marginally worse performance on the other four datasets. I’d be curious to see the standard deviations here. Because, if they overlap, then the performances between TextCNN and SpikeBERT are not statistically significantly different. Please report the standard deviations in brackets next to the averages and unbold your numbers or at least explain in the caption what bold-face means here. It’s not good practice to mislead the reader by simply bold-facing your numbers without further explanation.


- **Conclusion**: The conclusion is pretty short for a scientific conference paper. There is no discussion of results or impact. Moreover, I think the claim “*[...] can even achieve comparable results to BERTs with much less energy consumption across multiple datasets for both English and Chinese, leading to future energy-efficient implementations of BERTs or large language models.*” is misleading. I think SpikeBERT achieves comparable results to TextCNN but not to FT BERT. Also, BERT is not SOTA anymore since 2021. How would SpikeBERT compare against more recent variants of Transformer-based foundation models such as RoBERTa, Albert, or T5? (see the [Glue](https://gluebenchmark.com/), [SuperGlue](https://super.gluebenchmark.com/) and [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) leaderboards for an up-to-date list of models in NLP). I am not convinced that the approach reported in this paper is “*leading to future energy-efficient implementations of BERTs or large language models*”. There are numerous other approaches that have demonstrated this via distillation techniques (e.g., [DistilBERT](https://huggingface.co/docs/transformers/model_doc/distilbert)).


- No limitations are discussed as part of the conclusion. Unfortunately, there is no discussion section.


- An entire body of work that has employed distillation techniques over the past 4 years in NLP is not discussed here.

### Questions
- **Section 3**: The entire “pre-training + knowledge distillation + fine-tuning” pipeline appears to require a vanilla BERT model that has previously been pretrained on a large language corpus as is standard. If you rely on BERT, why would I not “just” fine-tune or probe BERT instead of applying your pipeline? What is the advantage here? Linear probing is much less expensive than fine-tuning (it only requires a linear classifier) and often equally performant (depending on the task).


- **Section 4**: Could you elaborate why I would use SpikeBERT over TextCNN although the methods perform equally well on all the reported datasets (see my comment on Table 1 above)? TextCNN is a computationally much less expensive method and has the "advantage" of static word representations. So, I could just compute the representations for each word used in the datasets a priori and then run inference as many times as I want without the need to run the sentences through the model. That being said, I don’t think that anyone in the community would still use a TextCNN from 2013 that produces non-contextual word representations for NLP tasks.


- Why didn’t you compare SpikeBERT against [DistilBERT](https://huggingface.co/docs/transformers/model_doc/distilbert)? DistilBERT is a distilled version of BERT that is much faster and cheaper and has comparable performance to BERT (probably better than SpikeBERT on the benchmarks that you looked at). AFAIK, DistilBERT exists since 2020. So, there must be an even better and more recent version of DistilBERT such as DistilRoBERTa or DistilALBERT. But please take a look yourself.


- **Table 2**: Why is the number of FLOPs consistently larger for SpikeBERT than for FT BERT although SpikeBERT’s energy consumption is much lower? How do you explain that? I’d like to see FLOPs and energy consumption of TextCNN reported in this table and not just SpikeBERT vs. FT BERT. Could you please report those? In addition to the FLOPs and energy consumption of TextCNN it would like to see these numbers for [DistilBERT](https://huggingface.co/docs/transformers/model_doc/distilbert) which has been shown to be much more computationally efficient/energy efficient than BERT while preserving most of its performance (around 95%) via knowledge distillation but their pipeline seems to be easier than your pipeline and does not necessitate "embedding alignment". Again, there probably exist even better distilled versions of BERT or RoBERTa or GPT-2/GPT-3 by now.


- **Table 3**: Did you employ the same data augmentation strategies to all methods that you compared SpikeBERT against? If data augmentation plays a crucial role in the performance of the model (which it does according to your ablations), then it seems not fair to compare SpikeBERT + DA against other methods without DA.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
