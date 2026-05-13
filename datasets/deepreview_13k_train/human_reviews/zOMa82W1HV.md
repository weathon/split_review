# SQuBa: Speech Mamba Language Model with Querying-Attention for Efficient Summarization

- Decision: Reject
- Scores: 5, 5, 6, 3, 3

## Abstract
Abstractive Speech Summarization (SSum) becomes increasingly difficult as the input speech length grows. To address this, we present SQuBa (Speech Querying Mamba Architecture), an end-to-end model designed explicitly for efficient speech summarization. SQuBa leverages a querying-attention Mamba projector to condense extended acoustic features into compact semantic tokens, which are subsequently summarized by the Mamba Large Language Model (LLM). The architecture’s computational complexity scales linearly with input length, enabling efficient handling of longer inputs. A two-stage training framework, complemented by bootstrapped Direct Preference Optimization (DPO) fine-tuning, empowers SQuBa to generate concise and coherent summaries. Experimental results demonstrate that SQuBa delivers competitive performance while significantly improving inference speed, making it ideal for real-world applications such as podcast and meeting transcriptions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper explores the use of Mamba-based multimodal LLMs to process long speech segments. The authors also apply DPO to enhance alignment during the instruction fine-tuning stage. Their experiments focus primarily on the speech summarization task, showing that the model can successfully process long speech.

### Strengths
The paper is clearly structured and represents a valuable exploration of using LLMs for long speech processing.

### Weaknesses
 - Although the paper explores long speech processing using LLMs, the motivation is not sufficiently compelling. Notably, LLMs excel at summarization, and long speech summarization could be effectively handled by combining an ASR model with a strong LLM. While ASR may introduce some errors, LLMs are generally robust enough to manage this task. Therefore, long speech summarization may not be the most suitable task for evaluating LLMs in handling extended long speech inputs.
- The contribution is somewhat limited, as Mamba-based multimodal LLMs and DPO have both been explored in speech instruction tuning. This work primarily combines these two methods and tests them on the speech summarization task.
- The experiments are insufficiently comprehensive; relying only on speech summarization does not robustly support the model’s capability with long speech. Furthermore, the LLM used here is not particularly strong.

### Questions
I'm curious about the performance of advanced models (e.g., Whisper v3 and Llama 3) in building a cascade pipeline. Since this work aims to explore LLMs for speech processing, and LLMs are effective in handling long text and summarization tasks, how would these models compare?

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
4

### Summary
The authors propose a sub-linear complexity speech summarization model by combining Q-former and pretrained Mamba. Segmented audios are processed by Whisper and compressed by Q-former with Mamba-processed query vectors, which are then fed to Mamba LLM to generate the summarization. A 3-stage training with different tasks is carried out, i.e. short-form ASR, long-form ASR, and summarization, accompanied by DPO. Empirical studies show better results and speed compared to cascaded models and a HuBERT+LLAMA E2E model.

### Strengths
* The model enables efficient speech summarization by combining pretrained Mamba and Q-former.
* Empirical results are strong.

### Weaknesses
 * Ablation studies are not sufficient to demonstrate the advantages of the proposed methods and to identify the impact of each component. Some design choices are yet to be well-motivated.
* The method is more like replacing transformers in existing methods (esp. arxiv:2407.02005) with Mamba, which leads to doubt on the technical novelty.
* Only one synthetic dataset is used.

### Questions
Q-former-like mechanism should be able to compress input of any length into fixed length. Hence I'm a bit confused about the decision to compress every 0.33s of audio into 2 query vectors. This differs from previous works including arxiv:2309.13963 and arxiv:2407.02005, which considered 30~100 vectors for every 30s of audio. In this way, the contextual information further than 0.33s will not be captured by the Q-former. I guess that the reason is to avoid the high-cost quadratic cross-attention but it will be better for the author to discuss that explicitly. Also, compressing a short sequence (only dozens of vectors, as each Whisper frame takes 25ms) into merely 2 vectors is rather simple and I doubt if the complicated Q-former will really outperform a much simpler one, e.g. pooling or convolution, which may also process information within such a short context well. More ablation studies will be necessary to justify this decision, by comparing with pooling or CNN, and comparing with different context lengths.

There are many other approaches to compress speech signals into "token-like" embeddings to be processed by LMs, e.g. HuBERT units, speech tokens, and neural audio codec, while Q-former is somehow similar to a kind of VQ, but with continuous features. Can you elaborate on the reasons why you chose Q-former? Do you think there is any specific advantage?

I am particularly concerned with the unidirectional Mamba used in Q-Mamba, and I fail to find the motivation to apply Mamba to the sequence of query vectors. Trainable query vectors should be already capable of introducing positional information. Ablation studies (e.g. by removing this Mamba layer) should be necessary to justify this choice.

I also have some questions regarding the use of DPO. What is the experiment without DPO in Table 4? Using supervised fine-tuning only?

If the issue w/o DPO is that the summary will be too detailed, has the author considered any other more straightforward solution, e.g. length penalty during generation, downsampling the input sequence, or upweighting EOS during training?

It is commonly believed that instruction fine-tuning leads to better alignment, but at the cost of flexibility and adaptability to specific downstream tasks in fine-tuning, while the authors use a instruction fine-tuned version of Mamba-2.8B as the base LLM. Is there any specific reason to use Mamba-2.8B-Zephyr instead of the original Mamba-2.8B model?

What is the LLM used in the Cascaded model? The original Mamba-2.8B or the instruction fine-tuned one? Is it further fine-tuned to summarization?

Can you elaborate more on the speedup of the model compared to the cascaded one? With both of them using Whisper and Mamba (though the inputs to Mamba are different), I'm curious about the source of the extra overhead in the cascaded pipeline. Also, it can be helpful to report the average input sequence length to the final LLM model as a reference to the expected computational costs.

Using only synthesized datasets is a weak point of the empirical evaluation, particularly when the labels are also synthetic. It can be necessary to also report the results on real datasets, e.g. SLUE-SUMM, and include more examples and human evaluations.

It can be interesting to report the ASR performance of the model after either of the two Alignment stages.

It will be better to also include the original transcript in Appendix C.

In Figure 3, is Whisper frozen in the Fine-tuning Stage?

Minor issues:
L210: Figure 4.1?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents SQuBa, an end-to-end speech summarization model that combines a Mamba language model with a novel querying-attention mechanism for efficient processing of long speech inputs. The key contributions are:

- A query-attention Mamba projector that compresses acoustic features into compact semantic tokens.
- Extension of Mamba-based LLM for speech summarization with a two-stage training process including bootstrapped DPO.
- Empirical demonstration of competitive performance with significantly faster inference speeds compared to transformer-based approaches.

The model achieves this through:

- Using Whisper encoder for speech features.
- Novel Q-Mamba projector for efficient feature compression.
- Pre-trained Mamba LLM (2.8B parameters) for generation.
- Two-stage training: speech alignment followed by summarization fine-tuning.
- Bootstrapped DPO for improved summary quality.

### Strengths
- Novel Architecture:

Innovative combination of Mamba with querying-attention for speech processing.

Well-motivated design choices for handling long-form speech.

Clear architectural improvements over existing approaches.

- Strong Empirical Results:

Significant speed improvements (17x faster than cascaded baseline).

Competitive performance on standard metrics.

Comprehensive ablation studies validating design choices.

- Technical Soundness:

Thorough theoretical foundation and clear mathematical formulation.

Well-documented training process and implementation details.

Careful experimental design with appropriate baselines.

### Weaknesses
Limited Dataset:
- Uses synthetic speech data for fine-tuning
- Could benefit from evaluation on more diverse real-world speech datasets
- Lack of cross-lingual evaluation

Architectural Constraints:
- Fixed 30-second chunks due to Whisper encoder limitations
- Query length choices could use more theoretical justification
- Potential information loss in compression not fully analyzed

Evaluation Metrics:
- Limited human evaluation or qualitative analysis
- No discussion of failure cases or limitations

### Questions
/

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper describes an approach to summarizing 6-minute-long audio recordings by combining the Whisper speech encoder with the Mamba LLM through a cross-attention based Mamba querying projector. The authors show that DPO improves ROUGE and METEOR metrics, and that the proposed model has a better ROUGE and METEOR score, and latency over the cascade model.

### Strengths
1. The paper attempts to address an important challenge, i.e., summarization of longform audio through a cross-attention based temporal downsampling module. 
2. It applies the recently introduced DPO technique to speech summarization, and demonstrates improved ROUGE and METEOR scores from this.

### Weaknesses
1. I have serious concerns about the novelty of the proposed approach. From a modeling standpoint, the work is very similar to Shang et al. (2024). From a training method standpoint, the 2-stage fine-tuning approach involving speech recognition and speech summarization is well established in the field since Sharma et al. (2021), leaving only two differences: (a) having an ASR training stage over both short and long audio as opposed to just short audio, and (b) using DPO post hoc, another well established technique to improve ROUGE and METEOR numbers. All in all, it appears that there is little technical novelty in the paper.  

2. Validating the proposed approach on a single relatively shortform audio dataset (upto 6 minutes) comprising synthetic audio is not very convincing. Furthermore, the work is done on a custom dataset whose LLM-generated summary labels have not been validated for correctness, either through automatic or human evaluations.  Since LLMs are known to hallucinate, it is hard to make a meaningful case using any numbers on this dataset. The authors should ideally consider evaluating on any real other dataset(s) with real audio. 

To add more context, here is a paper [1] that used synthetic data for speech summarization but still reported a myriad of automatic and human evaluation metrics to validate that the data used was reasonable. Something similar to this might be more convincing than what is in the paper currently. 

3. The metrics used for speech summarization in this paper do not go far enough. It is well known that ROUGE and METEOR based evaluations for summarization are not all encompassing, and that the metrics have significant flaws. This again makes it hard to validate that the observed improvements correlate with summaries of higher quality. The authors could supplement these measures using human evaluations of coherence, consistency, factuality and relevance. 

4. Table 4 could be expanded to show the impact of the long audio transcription based alignment if any. 

5. The manner in which DPO is performed is not very convincing. The authors use the model generated responses as the non-preferred responses and the ground-truth summaries as the preferred responses. Do the authors validate that the model generated responses are in fact undesirable, and record metrics that demonstrate the same ?

### Questions
1. In Equation 1, what is h'(t) ? 
2. The "ideal" query length for speech transcription is likely not representative of representations necessary for speech summarization. Can the authors clarify why these ablations were done for the transcription task on Librispeech ?
3. How does the speed of Scuba compare to that of the model by Shang et al ? 
4. The Whisper speech encoder is frozen, and it is not clear why this modeling choice was made.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces an end-to-end abstractive summarization method that processes speech inputs directly. It utilizes a querying-attention Mamba projector to condense extended acoustic features into compact semantic tokens, which are subsequently fed into the Mamba Large Language Model (LLM). They further employ Direct Preference Optimization (DPO) fine-tuning to produce coherent summaries. Experiments on a TTS-synthesized speech summarization dataset demonstrate that this approach outperforms both a cascaded baseline and an end-to-end baseline.

### Strengths
Originality:
1. The Mamba-based approach has not yet been utilized for speech summarization.

Quality:
1. Faster inference with better summarization performance against a cascaded and E2E baseline.

Clarity:
1. The paper is mostly easy to follow.

Significance: Results could be significant to speech summarization community.

### Weaknesses
Clarity:
1. The biggest weakness to me is the lack of clarity on the baseline models. They use Whisper large v2 as the ASR model in the cascaded system, but it has a limit of 30 seconds. How do they use it to get ASR output? Do they feed every 30-second window of audio as input? Further, do they finetune ASR or LLM or are they used in a zero-shot manner? What are the results in both these scenarios? If LLM is finetuned, do they also use DPO finetuning? The paper should provide more details about the E2E speech summarization baseline in the main text to make the paper self-contained. Specifically, the paper should clarify whether the cascaded system uses a sliding window approach with Whisper, and if so, what the window size and stride are. The paper should also specify the exact training procedure for the LLM in the cascaded baseline, including the dataset used and the optimization parameters. For the end-to-end baseline, the paper should provide a detailed description of the architecture and training procedure, including the loss function and optimization parameters. Without these details, it is difficult to assess the validity of the comparison.
2. It’s also unclear how the approach handles long speech sequences, which seems to be a central aspect of this work's novelty. The paper mentions chunking audio into 30-second segments, yet doesn’t address how contextual continuity is managed between chunks. Prior studies on streaming ASR (e.g., https://arxiv.org/abs/2107.09428) indicate that chunk boundary in the middle of token can result in generation inaccuracies. Clarifying whether any overlap is applied between chunks and providing additional discussion on this topic would improve the paper's depth and accessibility. The paper should also discuss the potential impact of chunking on the summarization quality, and whether any specific techniques are used to mitigate the loss of context across chunks. The lack of overlap between chunks could lead to discontinuities in the generated summaries, especially for longer speech inputs.

Soundness:
1. The evaluation is limited to one dataset, a TTS-generated synthetic speech summarization dataset. Including publicly available human speech datasets, such as SLUE_TED (https://huggingface.co/datasets/asapp/slue-phase-2) or AMI (https://groups.inf.ed.ac.uk/ami/corpus/), would provide a more robust assessment and ensure that the approach is tested on natural human speech data. The paper should also include results on a diverse set of datasets to ensure the generalizability of the proposed approach. The lack of evaluation on real-world data makes it difficult to assess the practical applicability of the proposed method.
2. Additional details on the synthetic dataset would be valuable, including whether it consists of single-speaker audio, and its quality (e.g., WER for the TTS output as evaluated by a pre-trained ASR model or via human relevance judgment). The paper should provide a detailed description of the TTS system used to generate the synthetic data, including the model architecture and training procedure. It should also report the WER of the synthetic speech as evaluated by a pre-trained ASR model to quantify the quality of the generated audio. Furthermore, the paper should include human evaluations of the synthetic speech quality to ensure that it is natural and understandable.
3. Further analysis is needed to pinpoint where the model outperforms a cascaded baseline. Does this improvement stem primarily from avoiding error cascading (that can potentially be addressed by improving the ASR system), or does the model also capture non-phonemic audio signals that enhance summarization quality? The paper should conduct an ablation study to determine the contribution of different factors to the performance of the proposed approach. Specifically, it should investigate the impact of error cascading by comparing the performance of the proposed approach with a cascaded baseline that uses a state-of-the-art ASR system. It should also analyze the contribution of non-phonemic audio signals by comparing the performance of the proposed approach with a variant that only uses phonemic information.

### Questions
Please refer to weaknesses

### Soundness
2

### Presentation
3

### Contribution
2
