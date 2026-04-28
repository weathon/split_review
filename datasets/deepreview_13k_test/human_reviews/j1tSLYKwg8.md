# Scaling Diffusion Language Models via Adaptation from Autoregressive Models

- Decision: Accept
- Scores: 6, 5, 6, 8

## Abstract
Diffusion Language Models (DLMs) have emerged as a promising new paradigm for text generative modeling, potentially addressing limitations of autoregressive (AR) models. However, current DLMs have been studied at a smaller scale compared to their AR counterparts and lack fair comparison on language modeling benchmarks. Additionally, training diffusion models from scratch at scale remains challenging.
Given the prevalence of open-source AR language models, we propose adapting these models to build text diffusion models. We demonstrate connections between AR and diffusion modeling objectives and introduce a simple continual pre-training approach for training diffusion models.
Through systematic evaluation on language modeling, reasoning, and commonsense benchmarks, we show that we can convert AR models ranging from 127M to 7B parameters (GPT2 and LLaMA) into diffusion models DiffuGPT and DiffuLLaMA, using less than 200B tokens for training. Our experimental results reveal that these models outperform earlier DLMs and are competitive with their AR counterparts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies diffusion language models (DLMs) and how they could be a good alternative to autoregressive (AR) LMs for generating text. It highlights the lack of fair comparisons on language modeling benchmarks and the challenges of training DLMs at scale. The authors propose adapting open-source AR models to build text diffusion models. By demonstrating the connections between AR and diffusion modeling objectives, they introduce a simple continual pre-training approach for training these models. The study shows that popular AR LMs can be converted into diffusion models (DiffuGPT and DiffuLLaMA) using less than 200B tokens for training, outperforming earlier DLMs and being competitive with their AR counterparts. The paper contributes a suite of DLMs capable of generating fluent text, performing in-context learning, text in-filling and following instructions.

### Strengths
The paper presents a simple and effective approach to adapting AR models to build DLMs, bridging the gap between the two modeling paradigms, while the proposed continual discrete diffusion pre-training approach for training diffusion models is practical and effective.
The proposed models, DiffuGPT and DiffuLLaMA, show competitive performance with AR models and outperform earlier DLMs in generating fluent text, perform in-context learning, filling in the middle without prompt re-ordering, and following instructions. 
The writing, organization and presentation of the paper are also good; I enjoyed reading the manuscript.

### Weaknesses
Overall, I appreciate the achievement of well-performing (discrete) diffusion LMs at scale, but I do have some concerns regarding novelty and evaluation. 

**About building DLMs by scaling and adapting from pre-trained large-scale LMs:**
Building (discrete) diffusion LMs from pre-trained Masked LMs has been studied in [1], while scaling and instruct-tuning (discrete) diffusion by adapting large-scale pre-trained LMs (mainly Masked-LMs while they also attempted to use AR-LMs/Llama1 to test reasoning) has also been studied in [2]. While this paper makes a solid step forward and effectively improves the performance of DLMs by leveraging AR LLMs, the authors should have thoroughly discussed the connections and major differences of their proposed approach with these prior works in the introduction or at least method/related work sections. Can the authors elorabrate the substantial differences and new contributions introduced by this paper?

**About progressively adapting AR text generation models into non-AR models:**
Two core techniques introduced in this paper are "Attention Mask Annealing" and "Shift Operation" to effectively reprogram an AR LM into a DLM. However, a similar approach has also been proposed in [3] in the case of non-autoregressive machine translation, which should have been discussed in this paper.

**Some claims are not supported by evaluations, hence the true advantages of DLMs are not convincing:**
The paper introduces the motivation of pushing the limits of DLMs by arguing that 
> Notable challenges include difficulties in **future planning** (Bachmann & Nagarajan, 2024; Hu* et al., 2024; Xie et al., 2024) and **self-correction** (Huang et al., 2024). These constraints have spurred researchers to explore alternative architectures for next-generation LLMs.

and accordingly,
> Notably, DLMs exhibit promising capabilities in **intermediate token correction** (Ye et al., 2024) and **global planning** (Zhang et al., 2023), thereby addressing key limitations inherent in the AR approach.

However, there is no clear evidence in this paper, not even qualitative ones or case studies, to showcase that DiffuGPT and DiffuLLaMA possess such promising capabilities of self-correction and global planning. Only evaluating on language understanding benchmarks with weaker performance compared to AR-LLMs (Table 1) cannot convince the community why we need really DLMs as an alternative to AR LMs and as a new LLM paradigm (I think this is the most important question every DLM paper needs to address). Plus, the in-filling performance of AR-LMs was unfairly assessed as they are only provided with prefixes, according to Table 1's caption. Thus, the paper still fails to demonstrate the unique, distinct advantages of DLMs over AR-LMs. I strongly suggest the authors provide more evidence to differentiate DLMs' strengths in these regards, which can also support the motivations of this work in the introduction.

Overall, I think this manuscript stands a good contributions to DLM research, and I believe it could be greatly improved if authors can address the aforementioned concerns. 

----

[1] DiffusionBERT: Improving generative masked language models with diffusion models. ACL 2023

[2]  Diffusion language models can perform many tasks with scaling and instruction-finetuning. Arxiv 2023

[3] Fine-Tuning by Curriculum Learning for Non-Autoregressive Neural Machine Translation. AAAI 2020

### Questions
See weaknesses.

### Soundness
3

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
3

### Summary
The paper introduces a methodology for adapting pretrained autoregressive (AR) language models to discrete diffusion (DD) models. It identifies two main points of conflict between them: 1) Causal attention (AR) vs. bidirectional attention (DD), 2) next-token-prediciton (AR) vs. denoising (DD). In order to resolve 1), the paper proposes attention mask annealing, where the causal attention mask is slowly turned into a full attention mask over training. For 2), the DD loss is adapted by shifting the logits by 1 to be in line with AR models.
In the experimental evaluation, they continue to finetune pretrained AR models of various sizes using the derived adaptation scheme. The models are evaluated on various knowledge, reasoning, coding, and math benchmarks.

### Strengths
* Adapting AR models to diffusion models is a problem that is of interest to the ICLR community.
* The proposed method is intuitive and simple.
* The paper is well written and flows really well.
* The results demonstrate that the adaptation is successful to some extent: Adapting larger LLMs leads to better performance.
* The DD model shows superior performance on some tasks that mostly require infilling.

### Weaknesses
1. In lines 364-368, it states that "by observing different scales of our adapted diffusion models, we can draw the conclusion that scaling diffusion language models results in improved performance". This statement suggests that if a DD model was trained from scratch, performance would scale with the size of the model. However, this isn't supported by the experiments, which merely shows that AR models of increasing size can be adapted to DD models in such a way, that larger adapted models perform better than smaller adapted models. However, it is possible that the adaptation process is merely retaining some of the knowledge/skills that were learned by the pretrained AR model. It doesn't mean that the DD model could attain these capabilities itself through scaling. I think it is important to be precise here.

2. In lines 367-369: "This discrepancy [between DiffuGPT's performance compared to the base model vs. DiffuLLaMA's performance compared to the base model] is presumably attributed to the extensive amount of training tokens processed by the DiffuGPT series models, whereas the 7B model has not undergone equivalent training." This explanation may be true, but needs to be verified. Since DiffuLLaMA has been pretrained on more than twice as many tokens (65B vs 30B), it doesn't seem obvious. What is the reason not to finetune both models on the same data?

3. In lines 373-375: "In tasks that require more extensive global reasoning, such as complex mathematics and coding, DLMs consistently exhibit better performance compared to AR models that rely solely on left-to-right modeling capabilities." This claim can only be substantiated through a controlled experiment that continues to finetune the base model on the same data in AR mode vs DD mode. Table 3 conducts this experiment, but only on a single downstream dataset that is quite small. Having a fair, controlled comparison between AR and DD models is the biggest weakness of this paper.

4. Table 2: Different models here correspond to different prompting methods. hit@k is not a prompting method, it is an evaluation metric whose value is at least as high as the standard evaluation metric with hit@1. Stylizing the respective row with hit@k incorrectly suggests that this is the best "method", which could mislead the reader into thinking that the difference to the LLaMA-2 baseline is smaller than it actually is.

### Questions
* From the paper, it is unclear to what extent the continuous-time discrete diffusion processes described in 3.1 are a novel contribution. If this is not novel, I would move it to section 2 for clarity about your contributions.

* In diffusion processes, do we need to know the number of tokens ahead of time in order to know the number of MASK tokens? If not, how is decoding done?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to adapt pre-trained autoregressive models to build discrete diffusion models via continual pre-training. This way, they can convert AR to diffusion parameters by training on fewer than 200B tokens. Technically, they propose  (1) annealed attention masking, (2) inheriting the shift inductive bias from AR. The experiment section suggests that this diffusion model demonstrates strong performance in math, word lambada, and infilling, and ablation suggests that the shift inductive bias is crucial for the transfer.

### Strengths
1. The paper proposes to adapt AR pretraining parameters to Diffusion parameters, which solves a very important problem about improving the training efficiency of diffusion models. 
2. The result seems solid, with a fair amount of improvement over previous diffusion models. But I still think there are some unresolved problems as shown in the weakness section. 
3. The experiment seems pretty comprehensive, with a wide range of downstream task, generation quality, analysis, ablation, and inference efficiency.

### Weaknesses
Since the paper claimed to tackle the parameter transferability problem, there remain some unresolved scientific questions: 
(1) suppose we have more compute, is this transfer still optimal? would this transfer converge to a worse local optimum than if we train from scratch for longer? 
(2) The paper included ablation results on GSM8K performance, but more fundamentally, what's the loss in terms of PPL for the (without shift) and (without annealing) baselines? I think these are more important and more general-purpose to report than a specific downstream task. I saw the disclaimer that PPL may not directly reflect the correctness and it's only ELBO. I still think it's good to report ELBO on the test set in the paper.   
(3) What's the number of flops for the training? 200B tokens is a bit abstract, especially 200B token for diffusion is different from 200B token for AR (due to lack of KV caching) and 200B token means different Flops across model sizes.

### Questions
see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper addresses limitations in autoregressive (AR) models, particularly issues with global planning and intermediate token correction. In response, Diffusion Language Models (DLMs) were introduced but face scalability challenges due to the computational costs of training with only 400 billion tokens. This work proposes a novel training mechanism that redefines DLM objectives. The approach also addresses architectural limitations in AR models, using attention mask annealing and a shift operation to remove causal masking bias. Scaled models ranging from 127 million to 7 billion parameters, specifically DiffuGPT and DiffuLLaMA, demonstrate better or comparable performance to existing AR models. Additionally, the authors release open-source code for these models, providing valuable resources to the research community for faster inference speeds with minimal iterations.

### Strengths
- Well-written and easy to understand.
- Comprehensive evaluation on multiple tasks, including word completion, reading comprehension, commonsense reasoning, math problems, and coding.
- Ablation study conducted to emphasize the importance of shift operation and attention mask annealing.
- Mathematically grounded and novel approach.
- Demonstrates increased token diversity without compromising quality.

### Weaknesses
- Missing qualitative examples and human evaluation.
- No statistical significance testing across tasks.
- The current T is set to 32. It would help to see the quality performance across different T, since it was mentioned in section 4.5 that decreasing T leads to faster decoding but with loss of quality.

### Questions
The current T is set to 32. It would help to see the quality performance across different T, since it was mentioned in section 4.5 that decreasing T leads to faster decoding but with loss of quality.
Please include this.

### Soundness
4

### Presentation
2

### Contribution
3
