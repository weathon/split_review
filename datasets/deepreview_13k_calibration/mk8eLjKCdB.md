# WaveletGPT: Wavelet Inspired LLMs

- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 3, 6, 1

## Abstract
Large Language Models (LLMs) have ushered in a new wave of artificial intelligence advancements impacting every scientific field and discipline. We live in a world where most of the data around us, e.g., text, audio, and music, has a multi-scale structure associated with it. This paper infuses LLMs with a traditional signal processing idea, namely wavelets, during pre-training to take advantage of the structure. Without adding \textbf{any extra parameters} to a GPT-style LLM architecture in academic setup, we achieve the same pre-training performance almost twice as fast in text, raw audio, and symbolic music. This is achieved by imposing a structure on intermediate embeddings. When trained for the same number of training steps, we achieve significant gains in performance, which is comparable to pre-training a larger neural architecture. Our architecture allows every next token prediction access to intermediate embeddings at different temporal resolutions in every Transformer decoder block. This work will hopefully pave the way for incorporating multi-rate signal processing ideas into traditional LLM pre-training. Further, we showcase pushing model performance by improving internal structure instead of just going after scale.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a method to encode multi-resolution context in GPT-style LLMs inspired by haar wavelet transform.

The method works by modifying the intermediate embeddings of the transformer blocks: replacing half the embeddings by the average pooling (of this half) over the context with windows growing exponentially in size.

### Strengths
The proposed method is simple with minimal computation overhead but results in performance improvements and a great reduction in the training time. The authors show this in different modalities and datasets. I feel the idea of encoding the context as an inductive bias is relevant for the community and worth studying.

### Weaknesses
 - I think the study has been done in a small setup, architecture, context length, and datasets; it's hard to tell if these findings would scale up, as the baseline does. From the results, it seems this method helps by sacrificing half the embedding space to average pooling over the context (albeit with different windows); it's hard to tell if this would be the case when scaling to more difficult tasks and longer context. Specifically, the experiments are limited to relatively small models and datasets, and it's unclear if the observed benefits would persist with larger models, longer context windows, or more complex tasks. The concern is that the average pooling operation, while computationally efficient, might lead to a loss of fine-grained information, especially in scenarios requiring precise contextual understanding. It's also not clear how this method would interact with other techniques for handling long-range dependencies, such as sparse attention mechanisms.
- Table 1, lacks the complete results for learnable and unlearnable kernels on all the datasets. 
- Although the authors motivate their method by wavelet transform from signal processing, I think the final method can be simpler to describe, as it's implemented as simply an average pooling operation (with different window sizes; window size is a function of the band).

Minor Issues:


- Lines 53 and 76, the text is duplicated.
- Line 114 typos
- Sections 4.3, 4.4 and 4.5, I think it's better to summarize the results in a table.

### Questions
In addition to the weaknesses above, I have the following questions:


- How do you deal with residual connections for the modified embedings 0:E÷2 . I mean, in the top transformer blocks, these embedings have residual connections coming from the modified (pooled) embedings. Is this the optimal setup? 

- Why choose the avg-pooling on the embedings instead of biasing the attention mechanism like WavSPA? 

- From Line 247, it seems the max window size is determined during training to be the context L, will this hinder the ability to expand the model context size after training ?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces WaveletGPT, a method that integrates wavelets with Large Language Models (LLMs). By applying a multi-scale structure to intermediate embeddings in a GPT-style LLM architecture, WaveletGPT achieves pre-training performance nearly twice as fast in text, raw audio, and symbolic music without adding much parameters. The architecture ensures that each token prediction can access intermediate embeddings at varied temporal resolutions in every layer. The effectiveness of WaveletGPT is demonstrated using three open-source datasets: text-8 for natural language, YouTube-Mix-8 for raw audio waveform, and MAESTRO for symbolic music. Additionally, the architecture's performance on the Long Range Arena (LRA) benchmark tasks shows significant improvements across all three modalities.

### Strengths
1. The authors proposed an almost free technique to help training LLMs from scratch, without the need of pre-trained larger teachers or significant modifications of the model architecture. 
2. The proposed technique is simple but plausible. The authors also tried to address the feasibility in areas like audio and symbolic music.

### Weaknesses
1. The idea of leveraging wavelets in Transformers is novel. However, the exploration of wavelet transform is insufficient in the paper, instead, the technique degrades to hand-crafted intermediate convolutional layers between the Transformer blocks (averaging and upsampling is just a special case of a convolutional layer). So extremely speaking, the authors simply added multi-scale convolutional layers between Transformer blocks to speed up convergence, which is rather intuitive. This undermines the innovativeness. The authors claim inspiration from wavelet filter banks, but the implementation lacks the core properties of a true wavelet transform, such as orthogonality and perfect reconstruction. The use of simple averaging and upsampling operations does not capture the frequency decomposition characteristics that make wavelets powerful. The method essentially becomes a multi-scale feature extraction using convolution, which is a well-explored area, and the connection to wavelets is tenuous at best.
2. Still the concern, the authors claim that the proposed method is superior because it gathers multi-scale information. However, there is no evidence to support that a single-scale averaging/convolution operation is underperformed (i.e., an averaging operation or convolutional layer with fixed kernal length). The paper does not include a comparison against a single-scale convolutional layer with a kernel size equivalent to the largest window used in the proposed method. This comparison is crucial to demonstrate the specific benefits of the multi-scale approach over a simpler, single-scale alternative. Without this, it is unclear whether the performance gains are due to the multi-scale nature of the method or simply the introduction of additional convolutional layers.
3. There is a lack of ablation experiments, and many of the designs are assumed rather than experimentally supported. Details are listed in the Questions section.
4. The experimental setup is unclear, which brings huge obstacles for reproducibility. The authors repeatedly mention "academic setup" without describing the actual setup they have. The paper lacks crucial details regarding the hardware used, the specific software versions, and the exact hyperparameters for each experiment. This lack of detail makes it difficult for other researchers to replicate the results. The authors should provide a detailed description of the experimental environment, including the GPU model, CPU, RAM, and the versions of the deep learning libraries used. Furthermore, the specific optimizer settings, batch sizes, and learning rate schedules for each dataset should be clearly stated.
5. The writing is poor, with countless gramatical errors and repeating sentences.

### Questions
1. line 127-128, the authors claimed that the proposed method can be easily extrapolated to state space architectures. However, there is no evidence or validation in this paper to support this claim. 
2. line 250, what is this "$l$" in $xn^l_{(i)}(k)$? Is that the layer index defined before? Because the fonts are different, and according to the definition in paragraph 189-201, this could also stand for wavelet coefficient level. 
3. line 248, if in this case i <= E/2, F will be a negative integer, f(i) will be less then 1, is this a mistake?
4. line 433, the authors mentioned a 32-dim version of the proposed model, where the performance was illustrated in Figure 4. However, in line 384, Figure 4 is mentioned to refer the full size model. In addition, in line 450, Figure 4 is mentioned to refer the learnable version. So which architecture does this diagram actually refer to? Is there a contradiction here?
5. line 115-116, the authors used an audio dataset, YouTube-Mix-8, for "long-context modeling". However, the context length remains still, which is 512 and is identical to other datasets. So why did the authors emphasize long context? Furthermore, in common practice of audio language modeling, a codec tokenizer is utilized to encode and compress audio signals to yeild short representations, because, as also mentioned in line 389, a context length of 512 only represents 32ms of audio, which is practically meaningless. Why didn't the authors tokenize the audios first nor expand the context length? 
6. line 416, the authors used an $\alpha$ linearly varying between 0 and 1. However, $ 0 < \alpha < 1 $. So, what are the boundary values of $\alpha$ at the two endpoints? Also, in line 417-418, what are the other scores regarding the audio and music?
7. Still considering $\alpha$, why an $\alpha$ linearly varying between 0 and 1 is equivalent to the proposed multi-scale wavelet transform? The smallest kernel size of the proposed transform is 2, so it's the average of 2 tokens, which is approximately equivalent to the situation where $\alpha = 0.5$. The fairness of this comparison needs further verification. 
8. There is a lack of ablation experiments, and many of the designs are assumed rather than experimentally supported. For example, why did the authors manipulate exact half of the coordinates of the hidden representations? What will happen if we manipulate more? Less?
9. If I understand correctly, the proposed method is implemented with two feed-forward-networks (FFN), mentioned in line 360-361, while the baseline (a scaled-down version of GPT-2) still consists of one FFN each layer. This introduces siginificant parameter advantage and makes the comparison unfair. Please correct me if I understood wrong. 
10. line 448, the authors mentioned that the learnable convolution layers only introduce 0.02M extra parameters. However, I believe a 10-layer Transformer with a hidden dimension of 128 inherently contains fewer parameters, so an absolute number is meaningless. What is the proportion of newly introduced parameters? What is the proportion of newly introduced FLOPs?
11. There are also countless grammatical errors and typos in the paper, such as:

    a. line 48, "Hinton et al. (2015)" should be "(Hinton et al., 2015)"

    b. line 53-79, repeating sentences.

    c. line 127, "Large Language models" -> "Large Language Models" (or just LLM, since mentioned before)

    Most of the grammatical errors are too minor to list individually here. I know I shouldn't be overly demanding about writing standards, as the idea is what matters most, but the writing errors in this paper is so much that I can't help but question the author's rigor.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a novel approach to Large Language Model (LLM) pre-training by embedding wavelet-based multi-scale structures into a GPT-style architecture. This method enables the model to access intermediate embeddings at different temporal resolutions without adding extra parameters, resulting in significant speedups (40-60%) in training time across text, raw audio, and symbolic music modalities. By structuring embeddings in a multi-scale manner, the authors achieve performance comparable to larger models, highlighting a new direction for improving model performance through internal structural modifications rather than sheer scale. The results suggest promising potential for incorporating signal processing techniques, such as wavelets, into LLM pre-training.

### Strengths
The proposed method is highly original, combining traditional signal processing concepts with contemporary LLM pre-training. The research methodology is robust, and the work addresses an important problem in LLM development, particularly in optimizing efficiency for multi-modal data without expanding model parameters.

### Weaknesses
 * The paper lacks explicit details about model parameters; assuming a GPT-2 scale (~120M parameters), an exploration of 300M-1B parameters could be feasible given the authors’ computational resources. Such scaling would be valuable to determine if results hold at larger model sizes. 
* Although the approach aims to address long-sequence modeling, experiments are limited to sequences of length 512.
* The paper lacks detailed downstream task results and analysis, limiting the assessment of its practical impact.  You may test on tasks like text summarization, question answering, or machine translation etc. to demonstrate the model's effectiveness in real-world applications

### Questions
The following questions are easier to solve under limited computational resources. I would change the decision to marginal accept if the answer to the following questions are intuitive.
* What implications arise from the significant loss reduction observed after applying wavelet transforms? For instance, could case studies illustrate improved sentence generation quality during inference? You can compare generated text samples from the baseline and wavelet-enhanced models on specific prompts or analyzing perplexity improvements on different types of text (e.g., formal vs. informal language).
* While the authors achieve better performance with learnable wavelet transforms, analyzing the learned wavelet parameters compared to traditional Haar wavelets would add valuable insights. It would be most interesting to visualize the learned wavelet shapes, compare their frequency responses to Haar wavelets, or analyze how they evolve during training.
* In Section 4, various experimental data are mentioned without tabular representation or inclusion in the appendix. Could the authors clarify the reasoning behind this omission?
* The paper includes two figures detailing Haar wavelet definitions yet lacks visual representation for the more critical learnable wavelet transform defined in Section 3.3.
* Many paragraphs, particularly in the introduction, are quite lengthy, with the introduction itself comprising only 1-2 dense paragraphs, making the paper somewhat difficult to read. Would breaking these up improve readability?

### Soundness
3

### Presentation
1

### Contribution
4

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper proposes WaveletGPT, which encompasses incorporating wavelet transform within the intermediate representations to impose multi-scale learning. Instead of going for SOTA, the paper focuses on demonstrating how the new WaveletGPT stands compared to standard Transformer based approaches, albeit on reduced scales.

### Strengths
The paper is sufficiently original in ideation, but the quality and clarity are not. The subject matter itself had the potential to have a significant impact if investigated well.

Some pros of the paper are:

- Several domains are covered: text, raw audio and music, which is great, since the approach has the potential for impacting multiple domains.  
- The approach sounds interesting and demonstrates faster convergence to same NLL score compared to standard transformer based baseline.

### Weaknesses
The paper is sufficiently original in ideation, but the quality and clarity are not. The subject matter itself had the potential to have a significant impact if investigated well.

Some pros of the paper are:

- Several domains are covered: text, raw audio and music, which is great, since the approach has the potential for impacting multiple domains.  
- The approach sounds interesting and demonstrates faster convergence to same NLL score compared to standard transformer based baseline.

The paper has the following shortcomings.

1. The paper is tremendously hard to read. The introduction reads like statements stitched together and is incoherent. Sections of the introduction are repeated, for instance: lines 76-79 about clockwork RNN. Related works are explained rather poorly. This paper needs to be proofread and phrased better: writing alone is unfit for an ICLR publication.
2. The datasets used are rather arbitrary and their usage is motivated well enough. Why not use a standard verifiable audio task such as speech?
3. Dataset scale. Even if we let the choice of "text-8" slide, Youtube-Mix-8 and Maestro are not exactly large datasets, with fewer than 10k samples each. 
4. The inclusion of LRA tasks is great, but there is simply not enough evaluation done in the paper. WaveletGPT should be investigated on more mainstream, even if smaller scale, datasets and benchmarks. The choice of architecture is fine, but more evaluations are needed.
5. Table 2 states that "non-transformer based or modified attention based hybrid architectures are not reported", however, FNET and WavSPA makes the cut. The choice of what models were benchmarked/reported is not justified enough.

The idea is interesting, but simply not executed well enough. More empirical evaluations are warranted, and a significant overhaul in the writing department is needed as well.


POST-REBUTTAL EDIT

Updated some language that the authors had issues with.

**POST-REBUTTAL EDIT 2: responses to the final comment made by the authors**

>  The goal in this work is only pretraining performance and not going after NLP benchmarks that are often used to evaluate much much larger models. 

> We have in fact gone to show the same architecture works for raw pixels, raw audio samples, math expressions, byte level text, GPT-2 tokenized text, character level text, acoustic tokens and audio waveform which is a more comprehensive result in our opinion as compared to a larger NLP dataset

Yes, but you have gone into that now, after the rebuttal. Pre-rebuttal the authors used 2 small, outdated NLP datasets and 2 small audio datasets.

---

> We again differ and it is not a correct statement. We are modeling raw audio therefore the tokens here are raw samples. Your statement is incorrect. 

That still doesn't change the fact that 5 hours of audio is a small audio dataset. Numerous approaches work with raw audio waveforms. For eg. wav2vec2 processes 16 kHz raw waveforms from LibriSpeech and LibriVox, which are ~1k hours and 60k hours of speech audio data, respectively. I'm not asking the authors to experiment on 60k hours of speech data, but my statement that the datasets used in the study are small is not incorrect.

> The dataset is large from point of view of raw acoustic sample tokens.

From the point of view of total hours of audio data, these datasets are small. Yet the authors are adamant in claiming that my statements are incorrect. What makes this discourse an even bigger exercise in futility is that the authors did conduct additional experiments on larger audio datasets: viz, LibriSpeech and FSD50K. The authors should be amplifying the improvements they've made and commenting and clarifying the additional analysis they've done (there is next to no information about how you did these experiments, apart from the fact that you show us some numbers), not trying to assert that the reviewer is wrong.

>  The same argument can be made for MAESTRO which was used to train Music Transformer models the most cited music generation paper. 

This paper is not a music generation paper.

---

Thanks for posting the FSD50K and LibriSpeech results, but there's no accompanying text for these experiments? You're mixing metrics in the table. There's no information about how these models were trained.

Also, I would like to note that the errors and issues with writing still persist and have not been updated in the main paper.

---

> To clarify, these were not allegations but direct quotes from the review including the new statements and opinions like 'It is disrespectful and undermining of the time and value reviewers put into reviewing your paper out of their schedule' and 'an appeal to established authority.' We felt the language and inappropriate statements are not suitable in the context of public reviews. 

I'm not going to comment on this any further, apart from saying that I am completely in the right to point out what felt was undermining and disrespectful of the time and effort I have put into reviewing this paper and writing prompt, detailed responses to authors comments in a public discourse. 

---

> My main concern is that the authors use the argument ...... we will not conduct so many additional experiments in such a short rebuttal period." I think such practices are contrary to the spirit of ICLR.

I agree with reviewer 4yst here.

---

Response to Last rebuttal comments

> We mentioned the link where the paper is updated. We share it again. The updated paper is here with extra experiments. https://drive.google.com/file/d/1u9OGe6VwnKhkyIBs9-k5a87c-rVFF637/view?usp=sharing

I can only make review decisions for paper revisions as they appear on the ICLR submission page. Maybe the Chairs can suggest otherwise, but sharing an external link to your updated paper allows post-rebuttal editions to the paper and also prohibits tracking of changes made to the paper, which to the best of my knowledge would be against ICLR policy.

Regarding other comments:

- The authors bring up SaShiMi, an audio generation paper. Evaluating the long-term context modelling capabilities of your approach through YouTube-Mix-8 is fine, but the dataset alone was not sufficient to evaluate your paper because your paper is not a music generation paper, it's an LLM paper, as the authors have repeatedly said so.

- The authors are getting fewer tokens for LibriSpeech than YouTube-Mix-8 because of design decisions and token sampling strategy. LLMs operate on tokens, fair, but that doesn't make the number of hours in an audio dataset irrelevant. 

---.

### Questions
N/A

### Soundness
2

### Presentation
1

### Contribution
2
