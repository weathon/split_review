# Parameter-Efficient Orthogonal Finetuning via Butterfly Factorization

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 6, 5

## Abstract
\vspace{-1.6mm}
Large foundation models are becoming ubiquitous, but training them from scratch is prohibitively expensive.
Thus, efficiently adapting these powerful models to downstream tasks is increasingly important. In this paper, we study a principled finetuning paradigm -- Orthogonal Finetuning (OFT) -- for downstream task adaptation. Despite demonstrating good generalizability, OFT still uses a fairly large number of trainable parameters due to the high dimensionality of orthogonal matrices. To address this, we start by examining OFT from an information transmission perspective, and then identify a few key desiderata that enable better parameter-efficiency. Inspired by how the Cooley-Tukey fast Fourier transform algorithm enables efficient information transmission, we propose an efficient orthogonal parameterization using  butterfly structures. We apply this parameterization to OFT, creating  a novel parameter-efficient finetuning method, called Orthogonal Butterfly~(BOFT). By subsuming OFT as a special case, BOFT introduces a generalized orthogonal finetuning framework. Finally, we conduct an extensive empirical study of adapting large vision transformers, large language models, and text-to-image diffusion models to various downstream tasks in vision and language. %The results validate the effectiveness of BOFT as a generic finetuning method.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper is an extension to [Orthogonal Finetuning (OFT)][oft], which involves modulating a pretrained weight matrix by multiplying it with an orthogonal matrix during finetuning; updating only the orthogonal matrix during finetuning. OFT, for efficiency reasons, parameterise the orthogonal matrix with a block-diagonal structure, with each block using a Cayley parameterization:
$$
R = (I+Q)(I-Q)^{-1}
$$
where $Q$ is a skew-symmetric matrix. The complete orthogonal matrix therefore becomes $\text{diag}(R_1, R_2, ..., R_r)$.

Because this orthogonal matrix is an arbitrary choice, the authors state that "it makes no sense to divide the dimensions of a neuron into $r$ groups based on their indices". This paper aims to produce a dense orthogonal matrix parameterization.

To that end they suggest a butterfly parameterisation, where each stage connects each unit to itself and another unit, through which information may flow from any two units after enough stages; inspired by the Cooley-Tukey Fast Fourier Transform. 

This improvement to OFT is tested by experiment on large language model finetuning for natural language understanding (GLUE), multitask language understanding (MMLU) and mathematical question answering (GSM8K and MATH). It is tested on a vision foundation model (SAM) classification (VTAB-1K) and segmentation (HQSeg-44K). Adapting a diffusion model (stable diffusion) was tested on controllable generation and subject-driven generation. BOFT performed better in most comparisons, except for some results on VTAB-1K and was outperformed by LoRA on some GLUE and MMLU benchmarks.

In general it was demonstrated as a competitive method for finetuning and a definite improvement over OFT.

[oft]: https://neurips.cc/virtual/2023/poster/72033

### Strengths
The paper provides a good review of other methods employing butterfly parameterisations in the literature and the relative benefits such a parameterisation provides. The description of the parameterisation in Section 3 is thorough and well paced. This appears to be an original and valuable way to apply the parameterisation in deep learning.

Expressivity analysis in Section 5 is a valuable contribution, identifying an advantage over OFT and making a strong argument for better performance over LoRA. This is supported by the experiments in Section 6.

Finetuning large pretrained models is a valuable area of research, it has become neither necessary nor practical to train a model from scratch on new problems. This method extends the work on orthogonal finetuning in a valuable direction and demonstrates that it is effective.

### Weaknesses
The information transmission framework, presented as a novel contribution, bears a strong resemblance to established connectivist principles in deep learning. The bipartite diagram illustrating this framework is conceptually similar to diagrams found in standard deep learning texts, such as the one on page 170 of Goodfellow's Deep Learning book. While the authors may have a nuanced interpretation, the current presentation lacks sufficient differentiation from existing connectivist representations.

The description of Orthogonal Finetuning (OFT) is delayed and could benefit from earlier introduction. Introducing the concept and potentially Figure 1 earlier in the paper would enhance the reader's understanding. Furthermore, including an illustration of the butterfly parameterisation alongside Figure 1 could provide a clearer initial overview of the paper's core premise.

Table 5 is misplaced, appearing adjacent to the description of the VTAB-1K task but presenting results for a subsequent task. The extensive use of wrapped figures and tables, while potentially effective, requires careful placement to ensure proximity to the relevant text.

The paper extends OFT, but the improvements seem incremental, offering minor performance gains over competing methods. While the authors highlight the spectral benefits of their method over LoRA, they do not delve into this aspect in their experimental evaluation, focusing primarily on benchmark results. A more thorough investigation of the spectral properties and their implications would strengthen the paper's contribution.

### Questions
I would expect that one of the main motivations for a butterfly parameterisation would be the reduced memory usage at inference time. Unfortunately, I'm not sure this method allows that, as it still requires that the original weight matrix is multiplied with the butterfly factorized matrix before being applied to the inputs. Is there any way this method provides some inference time savings?

In Section 5 when approximating random dense matrices, what distribution are the matrices drawn from, and is that distribution a good choice for modeling the types of matrices found in deep neural networks or orthogonal deep neural network adapters?

Is there any significant extra computational cost to matrix multiplying the original parameters with the orthogonal matrix adapter? I realise this would be the same issue OFT would have.

How do you train the butterfly parameterisation in practice? In most autograd frameworks a naive implementation would have a massive memory cost because each layer of the butterfly transform would require it's own cached activations.

Do the spectral properties of LoRA mean it should systematically fail in some way? Can you demonstrate that experimentally and show how BOFT doe not?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors tailor Orthogonal Fine-tuning to a parameter-efficient fine-tuning (PEFT) technique called Orthogonal Butterfly (BOFT) that is motivated from the Cooley-Tukey algorithm to perform fast Fourier transform, showing convincing potential as a PEFT approach.

### Strengths
The paper for the first time proposes BOFT, a PEFT method inspired by orthogonal fine-tuning and the Cooley-Tukey algorithm, and shows the performance of BOFT on various applications from computer vision to natural language processing.

### Weaknesses
The ability to switch different tasks efficiently would be lost in BOFT due to the fact that BOFT is based on multiplication whereas LoRA is based on addition.

For the MMLU dataset, the performance of Llama 2 13B and/or Llama 2 70B should be given, because PEFT methods are designed for fine-tuning large language models. The performance comparison of Llama 2 7B seems not to be enough.

The ablation study of $b$ and $m$ of BOFT seems to be necessary because all different $b$ and $m$ of BOFT are chosen in Table 2, 4, and 5, ,which implies that BOFT seems not to be practical compared to LoRA. Furthermore, the repeated process of merging and unmerging BOFT weights through multiplication may introduce unacceptable floating-point errors, whereas LoRA's addition/subtraction operations are more numerically stable.

### Questions
I just wonder whether or not BOFT can outperform LoRA (r=64) in Table 2 and 3 as well.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper attempts to analyze Orthogonal Finetuning from an information transmission perspective and proposes an efficient orthogonal
parameterization using butterfly structures. Their framework transforms the task of crafting a parameter-efficient dense orthogonal matrix into an information transmission problem within a grid-structured graph and also provides theoretical insights. Very interestingly, with similar block size, the authors have demonstrated better performance of BOFT in comparison with OFT.

### Strengths
Firstly, I appreciate the work including a good amount of experiments to show the effectiveness of BOFT. The paper is well written and the appendix provides significant experimental details. Application to SAM is interesting and useful. The motivation behind Orthogonal Butterfly technique is nicely explained.

### Weaknesses
One major concern I have is, in comparison with LoRA, I can immediately see the benefit due to a reduction in #Params but with OFT with comparable params, I see a marginal performance gain. I am not sure if OFT will be able to outperform the proposed method with some hyperparameter fine-tuning. OFT-SAM is missing in Table 5, and I would recommend authors to add the results for completion. I also have some novelty concerns with the work considering OFT, since the proposed method doesn't provide a noticeable gain over OFT. One question to authors, if there exists some b for OFT that can outperform BOFT with some m, b with similar #params, or BOFT always beats OFT with comparable params.

### Questions
See above.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
