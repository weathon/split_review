# Are Bert Family Good Instruction Followers?  A Study on Their Potential And Limitations

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Language modeling at scale has proven very effective and brought unprecedented success to natural language models. Many typical representatives, especially decoder-only models, e.g., BLOOM and LLaMA, and encoder-decoder models, e.g., Flan-T5 and AlexaTM, have exhibited incredible instruction-following capabilities while keeping strong task completion ability. These large language models can achieve superior performance in various tasks and even yield emergent capabilities, e.g., reasoning and universal generalization. Though the above two paradigms are mainstream and well explored, the potential of the BERT family, which are encoder-only based models and have ever been one of the most representative pre-trained models, also deserves attention, at least should be discussed. In this work, we adopt XML-R to explore the effectiveness of the BERT family for instruction following and zero-shot learning. We first design a simple yet effective strategy to utilize the encoder-only models for generation tasks and then conduct multi-task instruction tuning.  Experimental results demonstrate that our fine-tuned model, Instruct-XMLR, outperforms Bloomz on all evaluation tasks and achieves comparable performance with mT0 on most tasks. Surprisingly, Instruct-XMLR also possesses strong task and language generalization abilities, indicating that Instruct-XMLR can also serve as a good instruction follower and zero-shot learner. Besides, Instruct-XMLR can accelerate decoding due to its non-autoregressive generation manner, achieving around 3 times speedup compared with current autoregressive large language models. Although we also witnessed several limitations through our experiments, such as the performance decline in long-generation tasks and the shortcoming of length prediction, Instruct-XMLR can still become a good member of the family of current large language models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors adopt XML-R to explore the effectiveness of the BERT family for instruction following and zero-shot learning. They first design a simple yet effective strategy to utilize the encoder-only models for generation tasks and then conduct multi-task instruction tuning. Experimental results demonstrate that our fine-tuned model, Instruct-XMLR, outperforms Bloomz on all evaluation tasks and achieves comparable performance with mT0 on most tasks. Besides, Instruct-XMLR can accelerate decoding due to its non-autoregressive generation manner.

### Strengths
1. The idea is interesting and novel. It is great to know BERT family can also do instruction tuning. It can potentially lead to another series of research. 
2. The proposed method shows competitive performance compared to auto-regressive methods. And it can achieve 3 times speed up. 
3. The proposed method is simple and effective.
4. The paper is well-written and easy to read.

### Weaknesses
1. The method is not tested on longer sequence generation. The classification tasks don't need a longer output sequence. And machine translation fits the non-auto-regressive methods. Need to test it on the tasks like dialogue, summarization, etc. Specifically, the performance on tasks with a significant length difference between input and output sequences should be evaluated. For example, how does the model perform when generating long summaries from short documents or vice-versa? Evaluation on datasets such as XSUM, Gigaword, WIKI-AUTO, QQP, COMMONGEN, and PersonaChat would provide a clearer picture of the method's capabilities in these scenarios.
2. It would be better to analyze how stable the method is. How do the prompt templates affect the performance. Need to report the variance or significant test. Specifically, the paper should include an analysis of the model's performance across multiple runs with different prompt templates. Reporting the variance in performance metrics (e.g., ROUGE, BLEU) across these runs would provide insights into the method's sensitivity to prompt variations. Additionally, a significance test (e.g., t-test) comparing the performance with different prompts would help determine if the observed differences are statistically significant.
3. The proposed method cannot handle fewshot prompt learning. This is a significant limitation, as few-shot learning is a crucial aspect of modern NLP models. The inability to incorporate few-shot examples in the prompt limits the model's adaptability to new tasks and domains where labeled data is scarce.

### Questions
Have you tried to use a larger model?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This manuscript studies the instruction following capabilities of the BERT-family of language models, featuring an encoder-only architecture, which is one of the first of its kind. The work proposes a series of approaches that have made this possible, which eventually results in Instruct-XMLR (from XML-R), revealing promising task and language generalization abilities, previously undiscovered.

### Strengths
This is quite an interesting work with a refreshing perspective on language modeling via encoder-only architecture. I really appreciated the author's detailed analysis of relevant works, especially the mention of the work Wang & Cho (2019), which appears to be crucial to this work. The approaches, and training processes are detailed and well-motivated, and the benchmarks are extensive.

### Weaknesses
1. Some minor issues regarding citation formats (e.g. "Following the previous work Muennighoff et al. (2022), we evaluate the
model’s ability of task" is not directly readable, may need to include parenthesis)
2. As the authors have pointed out, the text generation capabilities, one of the arguably most important capabilities of language models, is still weak for Instruct-XMLR. This may limit the significance of this work.
3. Also arguably not a deal-breaker, but the compute resource (8xA100, unclear 40GB or 80GB, PCIe or SXM) and the model size (3.5B params on 0.6B tokens) may still be too small compared to cutting-edge decoder-only equivalents.

### Questions
It's a fascinating topic to explore beyond decoder-only autoregressive models. Would the authors agree that the benefit in text generation mainly comes from the next-token prediction formulation itself, and not necessarily the decoder architecture? One such example may be [1].

[1]: RWKV: Reinventing RNNs for the Transformer Era

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
We've been witnessing the rise of instruction-tuned language models since T0, FLAN, NaturalInstructions, Alpaca, etc. These models typically have a decoder-only (Alpaca) or encoder-decoder (T0, FLAN) architecture. This paper wants to study the question of whether encoder-only models such as the BERT family, can also be instruction-tuned and exhibit zero-shot task-generalization abilities. 

To do so, they first develop a new MLM training scheme that mimics the Seq2Seq training paradigm by concatenating source and target sequences to feed into BERT but with proper masking so that the source sequence tokens won't attend to the target sequence tokens. When training, they mask some tokens from the target sequences to do MLM training. During inference, they first predict the length of the sequence and then iteratively predict masked tokens (all tokens are [MASK] at the beginning). 

They then did instruction tuning on the 3.5B XML-R backbone model with the multilingual xP3 dataset. The performance is somewhat comparable to baselines like BLOOMZ-3B and mT0-3.7B, although still lagging behind on language generalization, generation tasks, few-shot learning, etc.


----------------------------------------------------------
POST-REBUTTAL UPDATE:
I'm raising my score from 5 to 6.

### Strengths
- I think the experiments are pretty solid. 
- The writing is generally clear and well-organized.

### Weaknesses
 - I'm not exactly sure what's the core contribution of the paper - it reads too much like an experiment report in this current draft. My biggest takeaway is that you can also do instruction tuning on encoder-only models. But why is that particularly "surprising"? To be fair, I'd be surprised it actually works much better than decoder-only or encoder-decoder models because then it means that the popular approach is wrong and they should go back to encoder-only models instead. But based on your experiments, it's not the case, decoder-only and encoder-decoder models still seem better at similar sizes. 

- The experiments are not exactly controlled in the sense that, your baselines - BLOOMZ-3B and mT0-3.7B, are not even based on the same backbone model as Instruct-XMLR. This means that many confounders (e.g., pretraining data / steps) exist for making any scientific conclusions based on the experiments.

- I am a bit confused by the method description in Section 3.2. Initially, you were describing it as if you train a separate "decoder" MLM, and H_{src} and H_{tgt} are from the two different models. But what I think you are actually doing is that, you just concatenate the source and target sequence and feed into the same BERT model, but with a modified masking scheme, such that source sequence tokens cannot attend to target sequence tokens.

### Questions
- Why don't you also include an XMLR without instruction-tuning baseline so that we can directly see the relative improvement coming from instruction tuning? 

- I am a bit confused by the method description in Section 3.2. Initially, you were describing it as if you train a separate "decoder" MLM, and H_{src} and H_{tgt} are from the two different models. But what I think you are actually doing is that, you just concatenate the source and target sequence and feed into the same BERT model, but with a modified masking scheme, such that source sequence tokens cannot attend to target sequence tokens.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
