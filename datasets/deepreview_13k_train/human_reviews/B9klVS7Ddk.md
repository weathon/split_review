# Compressing LLMs: The Truth is Rarely Pure and Never Simple

- Decision: Accept
- Scores: 8, 5, 8, 6

## Abstract
Despite their remarkable achievements, modern Large Language Models (LLMs) face exorbitant computational and memory footprints. Recently, several works have shown significant success in \textit{training-free} and  \textit{data-free} compression (pruning and quantization) of LLMs that achieve 50 - 60\% sparsity and reduce the bit width to 3 or 4 bits per weight, with negligible degradation of perplexity over the uncompressed baseline. As recent research efforts are focused on developing increasingly sophisticated compression methods, our work takes a step back and re-evaluates the effectiveness of existing SoTA compression methods, which rely on a fairly simple and widely questioned metric, perplexity (even for dense LLMs). We introduce \textbf{K}nowledge-\textbf{I}ntensive \textbf{C}ompressed LLM Benchmar\textbf{K} \textbf{(LLM-KICK)}, a collection of carefully curated tasks to redefine the evaluation protocol for compressed LLMs, which have significant alignment with their dense counterparts and perplexity fail to capture subtle change in their true capabilities. LLM-KICK unveils many favorable merits and unfortunate plights of current SoTA compression methods: all pruning methods suffer significant performance degradation, sometimes at trivial sparsity ratios (\emph{e.g.}, 25-30\%), and fail for N:M sparsity in knowledge-intensive tasks; current quantization methods are more successful than pruning; yet, pruned LLMs even at $\geq 50$\% sparsity are robust in-context retrieval and summarization systems; among others. LLM-KICK is designed to holistically access compressed LLMs' ability for language understanding, reasoning, generation, in-context retrieval, in-context summarization, \emph{etc.}
We hope our study can foster the development of better LLM compression methods.\blfootnote{\faApple~Work done during an internship at Apple.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper is very timely and identifies an important gap in evaluation of compression on LLMs. It points out how perplexity is not a correct metric to evaluate compression benchmarks (which is also previously observed in other contexts). They curate a set of datasets which can form a better representation of language model capabilities.

### Strengths
- timely ... with an array of papers on compressing LLMs with especially surprising results such as training free pruning coming out. It is important to enable researchers with better tools of evaluation
- provides a decent array of dataset benchmarks that will be use ful in research.
- clearly shows the gap between evaluation of perplexity and other proposed datasets.

### Weaknesses
Not weaknesses. but suggestions. 
1. add a summarizing table to list dataset statistics.

### Questions
None

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper benchmarks a few LLM compression methods based on quantization and pruning, on different datasets.

### Strengths
I think it is important to have a more fine-grained understanding of compression methods, specially to design new algorithms that can improve upon current weaknesses.

### Weaknesses
- This paper is essentially benchmarking a few algorithms on a few datasets. Although the insights are interesting, the paper does not include any new model, data or algorithm, which I'd say makes this paper more suitable for a workshop, not a full conference paper.

- Some arguments are rather subjective. Why choose the 5% threshold? If we change the threshold to 10% it seems 4-bit quantization is then in the range in most cases, and sparse models can still be "competitive" for around 50% sparsity.

- The loss of accuracy also has to be contextualized with the inference time speedups. If a 5% loss of accuracy leads to a 10% reduction in inference time, I'd call that successful.

### Questions
The authors say that SparseGPT is data-free. Is that true?

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
This paper revisits the efficiency of some compression (pruning and quantization) techniques for LLMs. It conveys that more than perplexity is needed for performance comparison among compressed and uncompressed models. It displays several tasks and benchmarks over which the compressed models exhibit performance degradation despite having similar perplexities. 

Essentially, the proposed benchmarks show that quantization if mostly more efficient than pruning where structured pruning appears to offer least ML performance. Interestingly, the paper also shows that even 8-bit quantization if not on par with the uncompressed baseline. 

Importantly, the paper states that their related codes are planed to be open-sourced

### Strengths
1. Compression of LLMs is very timely and important.

2. The paper reveals new and yet widely unknown gaps in compressed LLMs in comparison to their uncompressed counterparts. 

3. The paper shows that compressed models may offer better performance in some tasks (e.g., In-Context Text Summarization) than others (e.g., Factoid-based Question Answering)

4. The authors plan to release their code which may be help in the development of future compression techniques.

### Weaknesses
1. It would make the conclusions more robust and convincing if the evaluations use more than a single family of LLMs (i.e., Vicuna).  Why not repeat these experiments with, e.g., Llama 2 and Falcon?

2. Regarding the observation that even 8-bit quantization has evident gaps with respect to uncompressed models, have the authors considered evaluating LLM.int8()?  (https://arxiv.org/pdf/2208.07339.pdf) 

3. It would help the reader to have a table summarizing all the tasks' performance over the different architectures, compression techniques and the their resulting perplexity.

### Questions
See weakness 1 and 2. Also, does the authors have insights regarding why, in the paper's evaluation, quantization works better than pruning?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper benchmarks compressing techniques, pruning and quantization, on various datasets and metrics, highlighting that a common evaluation metric, perplexity, does not always translate into real-world values.

### Strengths
The paper is well-written, all the plots are clear and comprehensive. It's easy to understand information in most of the cases (see weaknesses for improvement). 
Authors correctly pinpoint that most of the compression algorithms do not validate extensively on real-world scenarios and show some interesting insights. For example, there is evidence that pruning may not work as well as quantization methods. Or that 8-bit quantization works well on majority on datasets. These insights are easy to use and can have a big impact to how practitioners use these models.

### Weaknesses
A few ways to improve this paper.
1. More LLMs. Right now, it's only vicuna model (7B and 13B), having other architectures and perhaps bigger sizes (e.g. llama 70b) would add more evidence for the insights. Specifically, the conclusions drawn from Vicuna might not generalize to other architectures with different pre-training procedures or scaling laws. It would be beneficial to see results on models with different architectural choices, such as the LLaMA family or models with different attention mechanisms. Furthermore, the current evaluation is limited to relatively small models; larger models might exhibit different behaviors under compression, and it is important to validate the findings on models with significantly larger parameter counts to ensure the robustness of the conclusions.
2. Add prompt designs to the main body of the paper. This will make it easy to understand how each task is distinct. The current description of the tasks lacks the necessary detail to fully understand the nuances of each evaluation. Including the exact prompts used for each task would allow for better reproducibility and a clearer understanding of the task difficulty and the specific skills being tested. This is crucial for interpreting the results and understanding the impact of compression on different types of reasoning and language understanding.
3. More quantization methods. AWQ/SmoothQuant are interesting to see. The paper would benefit from a more comprehensive exploration of quantization techniques. While GPTQ is a strong baseline, other methods like AWQ and SmoothQuant have shown promising results in preserving accuracy at low bit-widths. Evaluating these methods would provide a more complete picture of the trade-offs between compression and performance and allow for a better understanding of the state-of-the-art in LLM quantization.

### Questions
Why do we see these performance degradations? Any way to explain why some methods work and some do not? 
Are there are any counter forces one can use to mitigate performance degradation while still preserving the quality?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
