# LLMZip: Lossless Text Compression using Large Language Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6

## Abstract
We provide new estimates of an asymptotic upper bound on the entropy of English using the large language model LLaMA-7B as a predictor for the next token given a window of past tokens. 
This estimate is significantly smaller than currently available estimates in \cite{cover1978convergent}, \cite{lutati2023focus}.
A natural byproduct is an algorithm for lossless compression of English text which combines the prediction from the large language model with a lossless compression scheme. 
Preliminary results from limited experiments suggest that our scheme outperforms state-of-the-art text compression schemes such as BSC, ZPAQ, and paq8h.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper examines text compression utilizing the pretrained Large Language Model (LLaMa2) in conjunction with Arithmetic Coding (AC). The authors present an estimation of the entropy rate of the input text. Additionally, by using a summary as side information, they achieve a marginally improved compression ratio.

### Strengths
Utilizing a state-of-the-art Large Language Model for text compression to attain a higher compression ratio is interesting.

### Weaknesses
1. The concept of compressing text with pretrained language models is not groundbreaking. The paper's attempt to innovate using the advanced LLaMa2 as an LLM seems to lack strong novelty. The use of a more recent model does not inherently constitute a significant contribution without demonstrating a substantial improvement over existing methods or a novel application of the model itself. The paper does not clearly articulate how LLaMa2 is being utilized in a way that is fundamentally different from prior work with other language models.

2. Sections 2.1.1 and 2.1.2, which discuss text compression methods other than arithmetic coding, appear superfluous. These sections do not directly contribute to the core argument of the paper and could be omitted or significantly condensed. The inclusion of these methods without a clear purpose or connection to the main approach creates unnecessary clutter.

3. The detailed explanation of Arithmetic coding might be redundant; perhaps it would be better placed in an appendix. While some background is necessary, the level of detail provided seems excessive for a paper primarily focused on language model-based compression. The space could be better utilized for more in-depth analysis of the proposed method or experimental results.

4. In Section 2.2 regarding Entropy bounds, the equation H(S) = H(X) / E[B] does not appear to be a significant finding. This equation seems to be a straightforward application of known relationships and does not offer any new insights into the problem of text compression or entropy estimation. The paper does not sufficiently motivate the need for this particular derivation.

5. The use of text-summary for compression seems misjudged. Theoretically, adding bits to describe a summary would only be beneficial if the probability estimation isn't flawless. The paper does not adequately address the overhead introduced by the summary and how this overhead is balanced against the potential gains in compression. The conditions under which this approach is beneficial are not clearly defined.

6. The claims about the entropy bounds of the English language are debatable. For instance, Table 1 lists 0.6936, while Table 2 cites 0.7741 from a different dataset. The input data chosen for testing does not seem to be a true representation of English text, with entropy rates that fluctuate depending on the input. The lack of consistency in the reported entropy values raises concerns about the reliability and generalizability of the results. The paper should provide a more rigorous justification for the chosen datasets and their representativeness of English text.

7. Minor Remarks:
- The use of "It's" may not be suitable for a formal paper.
- Terminologies such as $N_{tg}$, $N_{cg}$, and others need clear and precise definitions.

### Questions
Please see Weakness section.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a LLM based text compression algorithm and empirically demonstrate the superiority of the proposed method over commonly used compression approaches. The authors also explores the usage of side information such as summary of the text to boots the compression performance further.

### Strengths
- The authors improve the text compression performance by combining LLMs and arithmetic coding. 
- The paper provides new estimates of an asymptotic upper bound on the entropy of English

### Weaknesses
 - The authors should provide more background introduction about text compression and make the paper more self-contained.


### Questions
- What are the baseline results mentioned in Table 1? I would suggest the authors include more introductions about the baseline methods and their performances.    

- Table 3 shows the performance varies based on the summary quality. How can we determine if the side information is helpful or not before compression? 

- Why does side information available in the encoder and decoder perform better than the encoder-only? 

- From the perspective of evaluation metric, does a lower bpc indicate a stronger LLM model potential in common downstream NLP tasks(summarization, translation, classification, etc.)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents LLMZip, an algorithm that leverages the recently developed Transformer-decoder-based Large Language Models (LLMs) for better compression. In this paper, we study the combination of LLM with various lossless compression schemes and analyze their empirical performance. We also explore how LLMZip's performance can be further enhanced with the availability of side information, such as text summaries. Experimental studies on various datasets are provided to demonstrate the effectiveness of the proposed LLMZip approach, which indicates that LLMZip achieves a better bits-per-character ratio compared to the traditional Zlib lossless compression method.

### Strengths
- The proposed idea is intuitive and easy to follow.
- Exploring the potential applications of LLMs in compression is a promising research direction.
- The paper is well presented in general.

### Weaknesses
 - The novelty of the LLMZip method seems to be limited. As mentioned in the introduction, it seems the connection between compression and prediction has been developed decades ago. Using language models for compression has also been explored before, with LSTM and/or RNN being used. Therefore, it appears that the sole contribution of this paper is the substitution of previously explored smaller language models with large language models (LLMs)
- Only Llama2 has been used as the language model in the experiment. It is unclear how the performance of LLMZip would vary when employing LLMs of different types and sizes. The lack of experimentation with diverse LLM architectures and parameter counts limits the generalizability of the findings. Specifically, the impact of architectural differences (e.g., decoder-only vs encoder-decoder) and scaling laws on compression performance is not explored.
- LLMs usually require GPUs for execution, whereas traditional compression algorithms can run on CPUs, which are more widely accessible and easier to democratize. This poses a significant practical barrier to adoption, especially in resource-constrained environments. The computational overhead of LLMs also introduces latency, which is not ideal for real-time compression scenarios.
- The LLMZip approach presented in this paper appears to be more suitable for submission to an information theory conference or journal, such as ISIT.

### Questions
- How does the performance of LLMZip vary when using aligned LLMs, e.g., Vicuna or fine-tuned Llama2?
- How does the performance of LLMZip vary when using LLMs with various scales, e.g., 13B or 65/70B?
- What does the end-to-end running time of LLMZip look like when compared to Zlib?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
