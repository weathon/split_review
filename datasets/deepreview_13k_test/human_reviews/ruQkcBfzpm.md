# mBLIP: Efficient Bootstrapping of Multilingual Vision-LLMs

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Modular vision-language models (Vision-LLMs) align pretrained image encoders with (frozen) large language models (LLMs)
and post-hoc condition LLMs to `understand' the image input.
With the abundance of readily available high-quality English image-text data as well as strong monolingual English LLMs, the research focus has been on English-only Vision-LLMs. 
Multilingual vision-language models are still predominantly obtained via expensive end-to-end pretraining, resulting in comparatively smaller models, trained on limited multilingual image data supplemented with text-only multilingual corpora. 
We present mBLIP, the first Vision-LLM leveraging multilingual LLMs, which we obtain in a computationally efficient manner on consumer-level hardware.
To this end, we \textit{re-align} an image encoder previously tuned to an English LLM to a new, multilingual LLM using only a few million multilingual training examples derived from a mix of vision-and-language tasks, which we obtain by machine-translating high-quality English data to 95 languages. 
On the IGLUE benchmark and XM3600, mBLIP yields results competitive with state-of-the-art models and it greatly outperforms strong English-only Vision-LLMs like Llava 1.5.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a multi-lingual LVLM that relies on aligning a frozen backbone and an LLM following BLIP2. The novelty relies on the alignment to a multi-language model, and how to tweak the alignment module (the Qformer) for this use case from a starting point of having a Qformer trained for the English language.

### Strengths
The approach is interesting in the sense that it covers a reasonable use case, that of multi-lingual LVLM by aligning frozen models. It seems like the authors found a good space where a solution did not exist in the literature.

The proposed approach seems technically reasonable. 

The paper is mostly clear, the target application is clear and the explanations are usually clear (although some issues are flagged later on). 

Results are positive, although there isn't a lot to compare against.

### Weaknesses
The paper does not seem to have a strong technical contribution. On the pro side, I like the application, and there's some analysis of the impact of the different pieces in Table 3, which offsets somewhat the lack of technical contribution.

I am a bit unsure about the impact of LoRA. A task prompt has much lower capacity to adapt to any downstream task compared to adding LoRA (especially if LoRA adapters are added to every 1x1 layer). So I'm wondering if part of the performance is due to LoRA vs no LoRA.  

Also, if there is enough data to train LoRA adapters, why then there is no data to train a task prompt? 

is "re-aligning" actually fine-tuning?

### Questions
Any answers to the "weakness" above. In particular: did I miss something with regards to novelty? can the use of LoRA be better justified?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper is to propose mBLIP: Introduction of the first multilingual Vision-LLM, mBLIP, achieved by realigning an image encoder to a multilingual LLM from English only Vision-LLM. In addition, mBLIP is created using only about 2.5 million images and training 124 million parameters on consumer hardware to convert high-quality English data into 95 languages for training.
The contribution of this paper is to presents a cost-effective approach to developing multilingual vision-language models with broad language coverage and strong performance.

### Strengths
mBLIP is created using only about 2.5 million images and training 124 million parameters on consumer hardware to convert high-quality English data into 95 languages for training.
The contribution of this paper is to presents a cost-effective approach to developing multilingual vision-language models with broad language coverage and strong performance.

### Weaknesses
There are still big differences of accuracy between English and other languages on XM3600 and xFlickerCo testing.
In addition, Table 2 is not so clean to understand.

### Questions
There are still big differences of accuracy between English and other languages on XM3600 and xFlickerCo testing.
In addition, Table 2 is not so clean to understand.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The work introduces mBLIP, which is a multi-lingual version of BLIP2. In summary, mBLIP replaces BLIP2's language decoder with stronger and newer multi-lingual LLMs (which breaks the alignment of vision encoder and the LLM) and re-aligns the vision encoder and the LLM with a dataset with images-text pairs, containing 96 machine translated languages.

### Strengths
- The work proposes a dataset (if will be released) with image-text pairs coming from 96 different languages, which could be useful for future research.
- Experiments are decent. The work also covers some important ablation studies.

### Weaknesses
- The major concern is the novelty. In short, the work can be summarized as (1) using machine translation to translate image-text pairs (in English) to different languages, and (2) replace the language decoder in BLIP2 with a multi-lingual one and train the model with translated dataset.
- The mixture of task highlighted in the paper as a contribution to the success of the model, although not considered in BLIP2, was actually explored in PALI. This fact further deteriorates the novelty of this work.
- It's not a surprise that task mix helps most in VQA and VNLI tasks because such an objective in included in the pre-training stage. The mixture of task actually hurts the captioning performance.
- The model can be trained on 4 cheap RTX-3090 GPUs, which is great. But this claim in the conclusion has nothing to do with the contribution of the work, i.e., any similar models will enjoy the speed-up with 8-bit quantization and LoRA PEFT.

### Questions
- The paper does not state the data portion used to pre-train the model. In the model pre-training, 3 tasks are considered, but the captioning dataset looks much bigger than VQAs. Meanwhile, the small size of VQA could contribute less to comprehensive pre-training, but only provide some demonstration to downstream QA tasks (that's probably why QA and VNLI tasks perform well).
- The paper claims that based on a few prior works, the re-alignment does not need larger dataset. However, some of the listed prior works (on arXiv) have very weak quantitative studies, which may not support authors' claim. Thus, such a claim has to be validated by ablation studies like re-alignment with different size of pre-training data, e.g., 3M, 12M, 120M, 400M, etc.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed an efficient method to adapt a pre-trained English vision language model to multilingual models. The dataset is created from an English only source, with machine translation to obtain multilingual data.The model is then partially finetuned on the machine translated multilingual dataset, where the Q-former in between is trainable and the LLM is LoRA tuned. Experimental results are behind the state-of-the-art methods, but it provides a cheap way to support multilinguality for an English model.

### Strengths
1. The proposed method is quite affordable, in that the training only takes a few days on a few GPUs. The method overall is adaptation cheap thanks to the limited amount of trainable parameters in Q-former, and the LoRA tuning of LLMs. 
2. This paper tackles an important problem of multilingual vision language models, that enables wider accessibility of the vision language models especially for non-English speakers.

### Weaknesses
1. One weakness is to name a translated dataset as a multilingual dataset, which doesn't cover the real benefits of multilingual at all (i.e. multiple cultures, examples from different locations from local people speaking those languages). This is misleading as the future work will use the translated dataset which will reinforce the emphasis of English centric research, under the translated "multilingual" directions.
2. The idea of applying Q-Former to LLMs is not novel and has been explored by the previous BLIP papers. I have not found BLIP baselines reported (at least on EN) in the paper (except for the right sub-table of Table 1). More comparisons with BLIP baselines, especially on the impact of multilingual data to the original English tasks would be nice to show the impact of this paper.

### Questions
See above sections. More questions:

1. The comparison of mBLIP with PaLI is quite unclear. Is mBLIP a zero-shot model or finetuned model? If it's the latter then it doesn't make any sense to claim that mBLIP outperforms (zero-shot) PaLI.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
