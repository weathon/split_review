# Brain-to-Text Decoding with Context-Aware Neural Representations and Large Language Models

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
Decoding attempted speech from neural activity offers a promising avenue for restoring communication abilities in individuals with speech impairments. Previous studies have focused on mapping neural activity to text using phonemes as the intermediate target. 
While successful, decoding neural activity directly to phonemes ignores the context dependent nature of the neural activity-to-phoneme mapping in the brain, leading to suboptimal decoding performance.
In this work, we propose the use of diphone - an acoustic representation that captures the transitions between two phonemes - as the context-aware modeling target. We integrate diphones into existing phoneme decoding frameworks through a novel divide-and-conquer strategy in which we model the phoneme distribution by marginalizing over the diphone distribution. Our approach effectively leverages the enhanced context-aware representation of diphones while preserving the manageable class size of phonemes, a key factor in simplifying the subsequent phoneme-to-text conversion task. We demonstrate the effectiveness of our approach on the Brain-to-Text 2024 benchmark, where it achieves state-of-the-art Phoneme Error Rate (PER) of 15.34\% compared to 16.62\% PER of monophone-based decoding. When coupled with finetuned Large Language Models (LLMs), our method yields a Word Error Rate (WER) of 5.77\%, significantly outperforming the 8.93\% WER of the leading method in the benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposes a multi-stage brain-to-text decoding framework consisting of an RNN phone decoding model integrating diphone as context-aware representations, and an LLM-based ensembling strategy utilizing both the decoded words by n-gram models and decoded phonemes as input to an fine-tuned LLM or by the ICL manner for correction. They demonstrate the effectiveness on the Brain-to-Text 2024 benchmark, where their approach achieves state-of-the-art (SOTA) PER of 15.34% and WER of 5.77%.

### Strengths
1. This paper is generally well written and easy to follow. The authors illustrate their methodology in a well-organized way and the results on Brain-to-Text 2024 are strong to prove its effectiveness.

2. Brain-to-text decoding could offer promising pathways for restoring communication ability and thus is a research topic that can make difference.

### Weaknesses
1. Utilizing diphone or triphone is a well-known technique for ASR community for enhancing phoneme decoding, and application to brain-to-text decoding shows some merits, but lacks some novelty in general. Also, the authors improve the ensembling strategy by integrating both the phoneme and word sequences for LLM, which is also a minor modification of the ensembling pipeline.

2. It seems to me the phoneme to sequence pipeline is a combination of NPTL and LISA besides the integration of the phoneme information. The procedure is a bit lengthy and there could be better way for improvement considering both efficiency and effectveness.

### Questions
1. If I understand it correctly, the authors utilize similar 5-layer RNN for phoneme decoding as in NPTL? I suggest the authors provide detailed specifications of their models in the experimental parts.

2. The authors analyze the tradeoff between diphone and monophone losses in Table 2, I wonder if the hypeparameter is generalizable for different datasets.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on decoding attempted speech from neural activity, a technology that can aid people with certain disabilities. Instead of representing the output with phonemes as done by other studies, they propose to represent the output with diphones, which can better model the coarticulation effects. They propose a divide-and-conquer strategy for decoding, which marginalizes the biphone distribution to get phoneme distribution. They also propose utilizing LLMs to improve the results, and in particular, an in-context learning paradigm as compared to fine-tuning methods. They report SotA results on the brain-to-text 2024 benchmark.

### Strengths
The paper is mostly well-written and easy to follow (with some exceptions of the technical aspect which I will mention in the weakness section). The problem it works on is a potentially important one, which leverages technology to help those with speech impairments, and the findings can potentially be beneficial for other fields where neural activity is used. They report SOTA results in the benchmark used, and present interesting analysis delving into the inner workings of the model.

### Weaknesses
Although the paper does a generally good job describing methods with textual descriptions, there are a few issues when it comes to mathematical notations. Some examples are,
- in Section 3, in the problem statement, the authors use Z to represent phoneme sequence, with Z being a vector of R (real numbers). This is an unusual choice since Z is discrete representing different identities of phonemes. 
- In the same paragraph, the author mentioned using GRU to model the function f: X -> Z. When I read this, I was confused since X and Z are typically of different lengths, involving a hidden alignment between x and z, which is beyond the modeling capacity of GRUs. The authors, in a later section, mentioned using a CTC model to learn the implicit alignment. It would be better to mention that first in the method description section to reduce confusion and misunderstanding. 
- I am having a bit of trouble understanding Equation (1). From the previous definition, Z and X are both multi-dimensional vectors, but here, if I understand correctly, X and Z are single-dimensional numbers. Some clarification on this would be beneficial. 
- The authors mentioned the issue of sparsity when discussing triphones, but I don't see explicit mention of how they deal with diphones. With just 40 phonemes, there are 1600 different possible diphones, and I would imagine the distribution among those 1600 choices can be highly unbalanced. It would be helpful to see stats regarding sparsity in those combinations. In the earlier days of speech recognition research where modular models were used, a common way to deal with sparsity was to build phonetic decision trees to cluster different triphones into equivalent classes. I would imagine this would also be a good choice to make triphone work in the context of this paper. So I'm not fully convinced that diphones would outperform triphones, if using clustering techniques like decision trees. 
- It seems that in generating the representation of output, the authors assume there is always going to be SIL between words. I'm not sure if this is a reasonable assumption without providing justification or comparisons. 

In section 4.3, there are references to Table 7 which I believe is a typo. Should be Table 1?

### Questions
Please see weakness.

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
4

### Summary
This paper tackles the challenge of converting brain activity to text as part of Brain-Computer Interfaces for individuals with speech impairments. The primary contributions of the paper are:

- The use of diphones, rather than monophones, for mapping neural activity to targets. Previous work has relied on monophones, which can be noisy since phones are influenced by preceding sounds during articulation.

- The application of an LLM with in-context learning examples for error correction.

Experimental results demonstrate the effectiveness of the proposed approach, achieving state-of-the-art performance on the Brain-to-Text benchmark.

### Strengths
- The approach of using diphones and subsequently normalizing them to monophones is well-motivated and delivers superior performance.

- The experimental results, where LLMs are employed for error correction, show significant improvements over strong baselines.

- The ablation study, which explores different architectures (including transformers), open-source LLMs, and various in-context learning examples for LLMs, thoroughly examines multiple aspects of the approach.

### Weaknesses
 - While the results are state-of-the-art, the major contributions of this paper are established concepts within the ASR literature. The use of diphones and triphones has been common in non-neural methods to address articulation issues.

 - The application of LLMs for ASR correction is also a well-explored area in the field.

### Questions
1. In the paper, diphones were normalized to monophones before being used with an n-gram language model to obtain word sequences. Is this normalization necessary? An n-gram language model could also be trained to directly transform diphone sequences into word sequences. 

2. What effect would using the richer context of diphone sequences have when processing with LLMs, as opposed to using the normalized monophone sequences?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper presents a novel approach to decoding speech from neural activity, focusing on individuals with neurological conditions that impair their ability to articulate speech. The key contributions of the paper are:

1. DCoND (Divide-and-Conquer Neural Decoder): A new framework that decodes phonemes from neural activity during attempted speech. DCoND leverages the context-dependent nature of phonemes by using diphones (sequences of two adjacent phonemes) as the intermediate representation, which enhances phoneme decoding performance.

2. LLM-Enhanced Ensembling: The paper proposes incorporating decoded phonemes alongside decoded words in a Large Language Model (LLM)-based ensembling strategy to improve speech decoding performance. It also introduces the use of In-Context Learning (ICL) as an efficient alternative to fine-tuning LLMs, offering a more resource-efficient solution for brain-to-text systems.

3. State-of-the-Art Performance: The proposed DCoND-LIFT (DCoND with LLM FineTuning) achieves state-of-the-art (SOTA) performance on the Brain-to-Text 2024 benchmark, with a Phoneme Error Rate (PER) of 15.34% and a Word Error Rate (WER) of 5.77%, significantly outperforming the leading SOTA method with an 8.93% WER.  The paper includes extensive ablation studies and analyses to demonstrate the effectiveness of the proposed methods, including trade-offs between diphone and monophone losses, alternative context-dependent phoneme representations, and the contribution of LLMs in the decoding pipeline.

Overall, the paper advances the field of brain-computer interfaces by offering a more accurate and efficient method for decoding speech from neural activity, with potential applications in restoring communication abilities for individuals with speech impairments.

### Strengths
The paper introduces a divide-and-conquer strategy (DCoND) that leverages diphones, a context-dependent representation of phonemes, to enhance the decoding performance. This approach is grounded in neuroscientific insights about the variability and context-dependence of neural signals during speech production.

The paper demonstrates the effectiveness of the proposed methods on the Brain-to-Text 2024 benchmark, achieving state-of-the-art performance in terms of Phoneme Error Rate (PER) and Word Error Rate (WER). The paper also includes detailed ablation studies and sensitivity analyses to validate the contributions of different components of the proposed system.

### Weaknesses
While the paper presents a promising approach to decoding speech from neural activity, it primarily builds upon established methods from the field of speech recognition, particularly in the use of diphones and language models. The novelty of the paper appears to be limited to the application of these mature techniques from hybrid speech recognition to the specific context of brain-to-text decoding, rather than introducing fundamentally new methodologies or insights.

Given the nature of the paper and its focus on applying existing methods from speech recognition to the brain-to-text decoding domain, it might be more appropriate for the authors to submit their work to journals that specialize in interdisciplinary research or those that focus on practical applications of existing technologies. 

From the perspective of academic paper writing, I recommend that the authors elaborate further on the Divide-and-Conquer strategy and its innovative aspects compared to traditional speech recognition methods. Expanding on this topic will not only enhance the depth of the paper but also assist readers in better comprehending the unique characteristics and advantages of this approach. Such a discussion will more effectively highlight the novel contributions of the research and provide valuable insights and references for scholars in related fields.

### Questions
Could you briefly explain the main technical differences between speech-to-text and brain-to-text tasks?

### Soundness
3

### Presentation
2

### Contribution
2
