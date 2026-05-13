# BCQ: Block Clustered Quantization for 4-bit (W4A4) LLM inference

- Decision: Reject
- Scores: 8, 3, 5, 6

## Abstract
Post-training quantization (PTQ) is a promising approach to reducing the storage and computational requirements of large language models (LLMs) without additional training cost. Recent PTQ studies have primarily focused on quantizing only weights to sub-8-bits while maintaining activations at 8-bits or higher. Accurate sub-8-bit quantization for both weights and activations without relying on quantization-aware training remains a significant challenge. In this work, we introduce a novel quantization method called block clustered quantization (BCQ) wherein each operand tensor is decomposed into blocks (a block is a group of contiguous scalars), blocks are clustered based on their statistics, and a dedicated optimal quantization codebook is designed for each cluster. We propose a PTQ algorithm called Locally-Optimal BCQ (LO-BCQ) that iterates between the steps of block clustering and codebook design to greedily minimize the quantization mean squared error. When weight and activation scalars are encoded to W4A4 format (with 0.5-bits of overhead for storing scaling factors and codebook selectors), we advance the current state-of-the-art by demonstrating <1% loss in inference accuracy across several LLMs and downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents Block Clustered Quantization (BCQ), a post-training quantization (PTQ) method designed to compress both weights and activations in large language models (LLMs) to 4-bit precision. BCQ divides tensors into small blocks, clusters these blocks based on their statistical properties, and then quantizes each cluster using a dedicated codebook, reducing memory footprint and computational load while preserving model accuracy. The Locally Optimal Block Clustered Quantization (LO-BCQ) algorithm iteratively refines clusters and codebooks to minimize quantization error. With solid experiments with varying configurations on Llama2 and GPT3 models,  it has shown LO-BCQ outperforms the states-of-the-art methods on W4A4 quantization.

### Strengths
1. Introducing iterative block clustering to derive an optimal quantization codebook for each block is novel, providing a robust and flexible mapping to the most accurate representation of each block. This approach, I believe, is the core factor driving the success of this method.
   
2. It is a compelling finding that the codebook is universally applicable for quantizing any tensor, at any layer, across different models.

### Weaknesses
I find this paper impressive, with no obvious weaknesses in its methodology or presentation. Please refer to the Questions section for some discussion points

### Questions
1. How does this method perform on W2A2 and W8A8 quantization, and how does it compare to other methods? What are the bottlenecks when applying this method to more aggressive quantization?

    2. As shown in Fig. 6, the range of values within some codebooks is smaller than [-1, 1], which appears to compensate for the large L_A. Have you tested even smaller L_A values, and how do they perform?

    3. 223: fond → found.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The Paper introduces Block Clustered Quantization (BCQ), a novel method aimed at achieving accurate sub-8-bit quantization for weights and activations in large language models without relying on quantization-aware training (QAT). BCQ decomposes operand tensors into blocks, clusters these blocks and designs dedicated optimal quantization codebooks for each cluster. This approach allows for tailored quantization that minimizes mean squared error (MSE) and maintains high inference accuracy.

### Strengths
- Using LO-BCQ algorithm utilizing block clustering and dedicated codebooks effectively minimizes mean squared error (MSE) while maintaining high accuracy.
- The paper considers several datasets to evaluate, especially include the MMLU boolq and Race datasets.
- Achieving less than 1% loss when quantizing weights and activations to 4-bits.

### Weaknesses
- The experiment shows that LO-BCQ takes good performance but it is built on multiple codebooks and small block division, the current LLM has a huge number of parameters, 8 elements for a block division will lead to a large computational overhead, and it is still a question whether the good performance can be maintained if the size of the block is increased.

- LO-BCQ's fine-grained quantization does not seem to have an advantage over per-group quantization such as Atom[1], which quantizes 128 consecutive elements as a group, and achieves excellent results in W4A4, and even better if Atom's grouping is adjusted to 64 or smaller. In addition, LO-BCQ introduces operations such as clustering, indexing, updating codebooks, etc., which costs more computational overhead.
[1]Zhao, Yilong, et al. "Atom: Low-bit quantization for efficient and accurate llm serving.

### Questions
- In Table 4 Ablation experiments, only the case where $L_{b}$ is less than 8 is discussed, what is the performance of the model if the size of $L_{b}$ is aligned with the group quantization e.g. 128, 64?
- The performance improvement of LO-BCQ seems to partly come from the clustering of blocks, the value of activation in LLM has a large difference in the distribution of different datasets, does the use of pre-calibrate for activation to calculate the codebook of activation have an impact on the language modeling ability of LLM?
- What is the impact on model inference speed of performing clustering with block size 8, indexing, and looking up codebooks during model inference? Does it mask the gains from low-bit quantization?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a method named block clustered quantization (BCQ), which decomposes operand tensors into blocks, clustering them based on statistics and designing codebooks for each cluster. When weight and activation scalars are encoded to W4A4 format, BCQ achieves the current state-of-the-art by demonstrating < 1% loss in inference accuracy across several LLMs.

### Strengths
1. This paper is well written, clearly described, and presents an effective methodology that makes group quantization a significant enhancement across a wide range of tasks and models;
2. Combining a quantization problem with a clustering problem is novel enough, I think, and the author's algorithm is simple and effective enough.

### Weaknesses
1. Although the authors' group quantization achieved a significant improvement in accuracy, the paper does not report results on inference speed. From QServe we can learn that group quantization is very inefficient in terms of speed of reasoning. Does the authors' proposed quantization scheme have any performance advantage over group quantization, except for the advantage of saving some storage? Can the authors provide the corresponding latency metrics?
2. The authors' experiments should include other model types such as LLaMA3 and Mistral, or even LLaMA3.1 and LLaMA3.2, and I am very much looking forward to the performance of the authors' method on MOE LLM model.
3. Figure 2, Figure 3 and Figure 4 can be modified to better illustrate and/or an algorithm description of the steps.

### Questions
1. Has the author's algorithm been compared to GPTQ, which is a very effective way to quantify large models in PTQ quantization, and how does the author's method compare to GPTQ in terms of effectiveness and efficiency?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduce a novel block quantization method called LO-BCQ, which achieves state-of-the-art level while avoiding additional memory overheads by iterative block clustering and quantization through locally optimization pipeline.

### Strengths
1. This paper iteratively optimizes block clustering and per-cluster quantization to minimize MSE loss for both weight and activation and achieves advanced level. 
2. LO-BCQ avoids memory overheads caused by per-block specific codebook and scaling factors in previous methods by sharing scaling factors in a group of blocks.

### Weaknesses
1. The paper ignores to describe the distinctions between block quantization and group-wise quantization. because from the perspective of form and definition, there seems to be no difference between them.
2. This paper solely conduct comparison experiments with block quantization based methods. However, there are many other widely used PTQ methods for LLMs such as OmniQuant, GPTQ, QuIP, etc. 
3. In addition to accuracy, efficiency is an important criterion for measuring the effectiveness of a proposed method. Compared to general PTQ methods, LO-BCQ involves numerous optimization processes, which to some extent reduce the method's efficiency.
4. The logical flow of the writing needs to be improved, especially for Introduction.

### Questions
1. For weakness1, if feasible, please involve detailed analysis and experiments for block quantization and group-wise quantization, such as AWQ-g128.
2. For weakness2, to demonstrate the advanced nature of your method, please include comparisons with the mentioned PTQ methods in your experimental tables. 
3. For weakness3, Please provide the running time consumption of LO-BCQ. If the proposed method is faster than OmniQuant, which is currently known for a relatively low-efficient but effective PTQ method, it would still be within an acceptable range.
4. The author should check for some spelling errors in the manuscript, such as "biwidth" in line 054.

### Soundness
2

### Presentation
2

### Contribution
3
