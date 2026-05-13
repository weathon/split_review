# InstructRetro: Instruction Tuning post Retrieval-Augmented Pretraining

- Decision: Reject
- Scores: 5, 6, 8

## Abstract
Pretraining auto-regressive large language models~(LLMs) with retrieval demonstrates better perplexity and factual accuracy by leveraging external databases. 
However, the size of existing pretrained retrieval-augmented LLM is still limited~(e.g., \emph{Retro} has 7.5B parameters), which limits the effectiveness of instruction tuning and zero-shot generalization.
In this work, we introduce \emph{Retro} 48B, the largest LLM pretrained with retrieval. 
Specifically, we continue to pretrain a 43B GPT model on additional 100 billion tokens using the {Retro} augmentation method by retrieving from 1.2 trillion tokens.
Notably, the obtained foundation model, Retro 48B, largely outperforms the counterpart GPT 43B trained on 1.2T tokens in terms of perplexity with only 2.58\% additional GPU hours, demonstrating the significant scaling potential of the method.
After instruction tuning on \retro, \emph{InstructRetro} demonstrates significant improvement over the instruction tuned GPT on a wide range of zero-shot tasks. 
Specifically, the average improvement of \method is 7\% over its GPT counterpart across 8 short-form QA and reading comprehension tasks, 10\% over GPT across 4 challenging long-form QA tasks, and 16\% over GPT across 3 summarization tasks. 
Surprisingly, we find that one can ablate the encoder from \method architecture and directly use its decoder backbone, while achieving comparable results. 
Our results highlight the promising direction to obtain a better GPT decoder through continued pretraining with retrieval before instruction tuning.
Our code and checkpoints are publicly available at: \url{https://huggingface.co/nvidia/retro-48b-instruct-4k}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a significant advancement in large language models (LLMs) by leveraging retrieval-based pretraining. The authors introduce Retro 48B, the largest LLM pretrained with retrieval prior to instruction tuning, addressing limitations posed by the size of existing models. By augmenting the 43B GPT model with an additional 100 billion tokens retrieved from a vast database of 1.2 trillion tokens, they achieve a notable improvement in perplexity. Following instruction tuning, InstructRetro 48B demonstrates substantial enhancements in zero-shot question-answering tasks, surpassing its GPT counterpart. Overall, this work highlights the potential for further advancements in LLMs through retrieval-based training.

### Strengths
1. Proposal of the largest LLM pretrained with retrieval.
2. Good zero-shot question-answering capability.

### Weaknesses
1. The model is only evaluated on QA tasks
2. The paper should better include the results of retrieval-augmented LMs.
3. The paper could benefit from providing additional explanations or motivation regarding how retrieval-augmented training enhances the performance of LLMs. Could this improvement be attributed to potential data leakage during the training of Retro 48B or continued training with more data?

### Questions
n/a

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents "Retro 48B", a large language model pretrained with retrieval before instruction tuning. Compared to the 43B GPT, Retro 48B showcases enhanced perplexity performance. After instruction tuning, InstructRetro significantly outperforms in zero-shot question answering tasks. Notably, removing InstructRetro's encoder and using only its decoder yields similar results. This highlights the decoder's enhanced capability for QA when pretrained with retrieval.

### Strengths
- The research highlights the benefits of continuing pretraining with retrieval mechanisms before proceeding to instruction tuning, a methodology that hasn't been extensively explored before.
- The paper brings to light the enhanced capability of the decoder in context incorporation for QA tasks when it's pretrained with retrieval, offering a fresh perspective on the potential of decoders in LLMs.
- The empirical results look nice. Retro 48B demonstrates enhanced perplexity performance when compared to the established 43B GPT model.

### Weaknesses
 - The scalability, computational costs, and efficiency of training such models might be a concern.
- A more diverse set of metrics, especially some human evaluation, could provide a comprehensive understanding of the model's performance.

### Questions
- What is the computational overhead for introducing the retrieval part?
- How did the authors balance the blend of instruction tuning datasets?
- How does the authors explain the difference of question acc only appears after instruction finetuning.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces (1) RETRO-48B, the largest LM pre-trained with retrieval using a 1.2T token database following the RETRO (Borgeaud et al., 2022) architecture, and (2) instruction-tuning RETRO-48B on diverse instruction-response pairs. To achieve (1), they explore multiple quantization and efficient indexing methods to speed up retrieval from 1.2T token storage and unfreeze decoder parameters during retrofitting. Experimental results show that RETRO-48B constantly achieves better perplexity than their continued pre-trained GPT-48B (GPT-fitting) or pre-trained GPT. For (2), they skip the cross attention through a manually set gate mechanism when retrieved neighbors are not available and conduct instruction-tuning on diverse instruction-tuning datasets (e.g., Open Assistant). Their experimental results show that InstructRetro even without an encoder (retrieved chunks) can significantly outperform GPT-48B.

I am impressed by the first contribution of this work -- making retrieval from 1.2T under 4ms only using a DGX-a100 node is difficult--RETRO has not yet been open-sourced and no one has reproduced their results at 1+T scale yet. It is also exciting to see that pre-training with retrieval can even enhance larger base LM (43B) as in the community there isn’t a clear consensus on whether retrieval still helps on a larger scale or whether larger LMs already encode necessary information without retrieval. Especially if the authors can open-source the code and checkpoints, it can inspire follow-up research on scaling retrieval-augmented LM pre-training. I wish they provided ablations on different quantization methods to see whether different techniques can affect final performance or not, as conducting ablations on invidious quantization techniques can also be really expensive. Also given that the great progress of pre-training retrieval models, I wonder if we could replace a frozen BERT-base retriever with a more recent and competitive retrieval model e.g., Contriever. 

On the other hand, I am not fully convinced by the contribution (2). The descriptions of the instruction-tuning parts are confusing, and making it difficult to understand the concrete setup. Is retrieval or encoder indeed used instruction-tuning, or is skipped most of the time? Figure 1 seems to indicate that retrieval is skipped during instruction tuning while the text in Section 3.2. says retrieval is skipped only when retrieval context is not available. But there are no clear descriptions of what "retrieval context is not available". I listed detailed questions in Weaknesses and Questions. 
If it’s mostly a standard instruction tuning without retrieval on top of RETRO-48B, I don’t think it’s that technically novel. Also, the experimental results indicate that removing the encoder block doesn’t affect the performance that much, which contradicts prior findings where retrieving documents gives large improvements on top of strong LLMs in tasks like OpenQA. While the authors argue this indicates pre-training with retrieval can enhance a decoder-only LM, this result makes me question the effectiveness of instruction tuning or the proposed model's ability to use retrieved context. I suspect the limited deterioration may be from the limited performance of the retrieval component itself (i.e., the BERT encoder is far from the current SOTA retrieval system in the same parameter scale) but it is unclear as there are not many ablations or analyses on different decision choices. 

Overall, I think (1) provides strong technical contributions, but many questions are left in the second part, in terms of implementations and results. I suspect more clarification,  improvement of presentations or analysis might help, and am happy to increase my score once I am convinced.

### Strengths
- This paper introduces the largest scale of LM pre-trained with retrieval (RETRO-48B).
- They retrieve relevant chunks from a 1.2T token datastore, and by extensive quantization and efficiency techniques they make retrieval fast and scalable. 
- They further instruction-tune RETRO-48B on diverse instruction-response pairs.

### Weaknesses
I like this paper and believe this paper provides great technical contributions in terms of pre-training retrieval-augmented LM at scale. On the other hand, I have several concerns, especially for the instruction tuning part and their downstream task evaluations. That being said, my concerns partially come from confusion between inconsistent descriptions in the paper, and I am happy to increase my score once I am convinced during the discussion period.


**1. Technical novelty**

Introducing RETRO-like architecture on top of a decoder-only model has been recently studied by [Wang et al. (2023)](https://arxiv.org/abs/2304.06762). Although RETRO-48B is the order of magnitude larger in terms of parameter counts and index size and they employed a lot of techniques to achieve this (Section B), I wish they had provided a more detailed analysis of individual quantization techniques to help the community learn more from this work. Unfreezing decoder parameters is one notable difference from RETRO, but I am not sure if this provides sufficient contributions. The instruction-tuning results seem to be rather mixed and some details aren't super clear to me (discussed below) if it's a standard instruction-tuning, I don't think it provides sufficient contribution either.

**2. Unclear details of instruction-tuning**

The biggest question I had about the instruction-tuning part is in how much of the instruction-tuning, retrieval is indeed used during the instruction-tuning stage.  

> However, one noticeable difference is that Retro requires retrieval of nearest neighbors for the input instructions, which is not available from all the instruction tuning datasets. Since the instruction tuning data is high-quality, retrieval from the pertaining corpus can yield noisy neighbors, thus not helping improve the model capabilities to follow instructions. We instead skip the cross-attention connection through a manually-set gated mechanism, which sets the gate to zero when retrieved neighbors are not available. 

The description says that the gate is set to zero when retrieved context is not available, but it's unclear what retrieved-context is unavailable means. None of the instruction-following datasets such as OpenAssistant comes with a pre-given retrieved document. Does this mean retrieval is always off during pre-training? Or it is used for some datasets with pre-given context? The lack of details makes it difficult what's new for the instruction-tuning stage. 

**3. Evaluation and comparison with baselines**

To my understanding, by default, RETRO-48B uses top documents for tasks like Open-domain QA (Implementation details). Then should a baseline that simply takes the same documents in input space (which is often called a retrieval-augmented generation) be used as a baseline? Also for me, Table 3 and 4 results look strange -- in prior work in retrieval-augmentation even on top of the SOTA LMs such as Codex, GPT-003, or Llama2-65B shows retrieval-augmentation gives large gain on tasks like open-domain QA. Why on RETRO-48B get even slightly better performance by removing encoders (and thus completely remove retrieved text)? Also even on Table 4 about long-form QA, the performance gap between w and w/o retrieval may not be statistically significant. While the authors claim this is evidence that pre-training with retrieval helps us to achieve a better decoder LM, I am rather confused about why their findings are different from prior work on retrieval augmentations. More quantitative and qualitative analysis on why this happens would help, but the paper doesn't have much ablations to address those questions. 

Also, the gains in perplexity are impressive, there could be a certain risk of data leakage (e.g., a string similar to the test instance may be included in the database or training data), as also discussed in the RETRO paper. Probably more analysis and a sophisticated approach to mitigate the potential leak as in the RETRO paper could be helpful.

**Minor (but many) typos**

Although this is minor, there are at least 20 typos about pretraining (In the draft, many lines include the word "pertaining" -- I think the authors meant to say pretraining), including sub section titles. I recommend authors to fix this issue in the updated version of the draft.

### Questions
- How often the gate is set to zero during the instruction-tuning time?
- Do you have any insights into why removing encoders doesn't affect the performance? 
- Have you tried different encoder moels rather than BERT-base? e.g., Contriever 
- Did you do any analysis on the potential leak between train (database) /test splits in the pre-training corpus?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
