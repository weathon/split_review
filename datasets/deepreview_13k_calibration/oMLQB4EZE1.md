# DNABERT-2: Efficient Foundation Model and Benchmark For Multi-Species Genomes

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Decoding the linguistic intricacies of the genome is a crucial problem in biology, and pre-trained foundational models such as DNABERT and Nucleotide Transformer have made significant strides in this area. Existing works have largely hinged on k-mer, fixed-length permutations of A, T, C, and G, as the token of the genome language due to its simplicity. However, we argue that the computation and sample inefficiencies introduced by k-mer tokenization are primary obstacles in developing large genome foundational models. We provide conceptual and empirical insights into genome tokenization, building on which we propose to replace k-mer tokenization with Byte Pair Encoding (BPE), a statistics-based data compression algorithm that constructs tokens by iteratively merging the most frequent co-occurring genome segment in the corpus. We demonstrate that BPE not only overcomes the limitations of k-mer tokenization but also benefits from the computational efficiency of non-overlapping tokenization.
Based on these insights, we introduce DNABERT-2, a refined genome foundation model that adapts an efficient tokenizer and employs multiple strategies to overcome input length constraints, reduce time and memory expenditure, and enhance model capability. Furthermore, we identify the absence of a comprehensive and standardized benchmark for genome understanding as another significant impediment to fair comparative analysis. In response, we propose the Genome Understanding Evaluation (GUE), a comprehensive multi-species genome classification dataset that amalgamates $36$ distinct datasets across $9$ tasks, with input lengths ranging from $70$ to $10000$. Through comprehensive experiments on the GUE benchmark, we demonstrate that DNABERT-2 achieves comparable performance to the state-of-the-art model with $21 \times$ fewer parameters and approximately $92 \times$ less GPU time in pre-training. 
Compared to DNABERT, while being $3 \times$ more efficient, DNABERT-2 outperforms it on $23$ out of $28$ datasets, with an average improvement of $6$ absolute scores on GUE.
The code, data, and pre-trained model are available at \url{https://github.com/MAGICS-LAB/DNABERT_2}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces DNABERT-2, an advancement in genome foundation modeling, which aims to decode the linguistic intricacies of genomes. The authors assert that the computational and sample inefficiencies of k-mer tokenization, predominantly used in earlier models, act as barriers in the development of foundational models for large genomes. To address this, the paper introduces Byte Pair Encoding (BPE) as a replacement for k-mer tokenization. BPE is more efficient and overcomes the limitations of the k-mer approach. The authors also emphasize the need for a standardized benchmark for genome understanding and consequently introduce the Genome Understanding Evaluation (GUE) dataset. Experimental results reveal that DNABERT-2 performs on par with state-of-the-art models but with fewer parameters and less GPU time during pre-training. The model also shows significant improvements over the original DNABERT.

### Strengths
1. DNABERT-2 incorporates ALiBi and Flashattention mechanisms, enhancing speed and context length.
2. The model successfully borrows several techniques from LLM (Large Language Models) and integrates them into DNABERT.
3. The authors have collected a comprehensive dataset tailored for short sequence prediction.
4. The research is detailed, with a focus on the nuances of the biology setting and the existing benchmarks, showcasing a holistic approach.

### Weaknesses
1. The input size for the proposed benchmark seems to be on the shorter side for genomics, potentially limiting its applicability to broader genomics problems. Specifically, the current benchmark focuses on sequences up to 1000 base pairs, which may not be sufficient to capture long-range dependencies and interactions that are crucial in many genomic contexts, such as enhancer-promoter interactions or structural variations. This limited input size might restrict the model's ability to generalize to more complex genomic tasks.
2. The benchmark's design appears constrained, lacking baseline models like CNNs and omits language model training from scratch, which could provide comparative insights. The absence of CNN baselines, which are commonly used in genomic sequence analysis, makes it difficult to assess the relative strengths and weaknesses of the proposed transformer-based approach. Furthermore, not including a language model trained from scratch limits the understanding of the impact of pre-training on the model's performance.
3. While the paper is apt for an ML conference, there is a discernible deficiency in the depth of biological insights. Better downstream tasks, such as CAGE-seq prediction and so on.... (longer sequence context)

### Questions
1. In the introduction, can you clarify what you specifically mean by "genome language modeling"?
2. Following up on the theme, why was there no citation or reference to models like deepbind/deepSEA? For instance, the TF-DNA binding prediction from Wang et al., 2022, seems not a great citation? Not a genomics language modeling. 
3. Given the unique structure and function of DNA, why is there a continued emphasis on tokenization in DNA language modeling?
4. I recommend adding the count of sequences for each dataset in Table 1 to provide a clearer understanding of the dataset sizes.
5. Why weren't tasks involving longer sequences incorporated after introducing DNABERT?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
DNABERT2 is an update of the DNABERT, which is an application of the BERT structure to DNA data. My guess is that it first performs tokenisation of input DNA sequence, then pre-trains on DNA dataset to get the token embeddings, after that it adds a few layers to utilise the token embeddings for classification tasks such as promoter detection and transcription factor prediction. The manuscript made the following improvements: (1) use Byte Pair Encoding (BPE) for tokenisation (2) use attention with linear biases (ABiLi) for position encoding and (3) use flash attention and low-rank adaptation (LoRA) for acceleration. It also compiles a larger benchmark dataset for comparing different methods. The manuscript demonstrated that DNABERT2 improved over DNABERT and had a similar performance as Nucleotide transformer. 

I think the authors have done a decent amount of work and the work could be more useful for the community if the authors could
(1) perform an ablation study to quantify the contribution of BPE and ALiBi independently.
(2) explain why the code, data and pre-trained model could not be made public now
(3) explain why mcc and f1 are used as the comparison metric for different tasks
(4) explain the benefit of further pre-training. I get lost in understanding the sentence "This results in 0.41B training tokens..." right above section 5.3.

### Strengths
DNABERT2 is an update of the DNABERT, which is an application of the BERT structure to DNA data. My guess is that it first performs tokenisation of input DNA sequence, then pre-trains on DNA dataset to get the token embeddings, after that it adds a few layers to utilise the token embeddings for classification tasks such as promoter detection and transcription factor prediction. The manuscript made the following improvements: (1) use Byte Pair Encoding (BPE) for tokenisation (2) use attention with linear biases (ABiLi) for position encoding and (3) use flash attention and low-rank adaptation (LoRA) for acceleration. It also compiles a larger benchmark dataset for comparing different methods. The manuscript demonstrated that DNABERT2 improved over DNABERT and had a similar performance as Nucleotide transformer. 

I think the authors have done a decent amount of work and the work could be more useful for the community if the authors could
(1) perform an ablation study to quantify the contribution of BPE and ALiBi independently.
(2) explain why the code, data and pre-trained model could not be made public now
(3) explain why mcc and f1 are used as the comparison metric for different tasks
(4) explain the benefit of further pre-training. I get lost in understanding the sentence "This results in 0.41B training tokens..." right above section 5.3.

### Weaknesses
DNABERT2 is an update of the DNABERT, which is an application of the BERT structure to DNA data. My guess is that it first performs tokenisation of input DNA sequence, then pre-trains on DNA dataset to get the token embeddings, after that it adds a few layers to utilise the token embeddings for classification tasks such as promoter detection and transcription factor prediction. The manuscript made the following improvements: (1) use Byte Pair Encoding (BPE) for tokenisation (2) use attention with linear biases (ABiLi) for position encoding and (3) use flash attention and low-rank adaptation (LoRA) for acceleration. It also compiles a larger benchmark dataset for comparing different methods. The manuscript demonstrated that DNABERT2 improved over DNABERT and had a similar performance as Nucleotide transformer. 

I think the authors have done a decent amount of work and the work could be more useful for the community if the authors could
(1) perform an ablation study to quantify the contribution of BPE and ALiBi independently.
(2) explain why the code, data and pre-trained model could not be made public now
(3) explain why mcc and f1 are used as the comparison metric for different tasks
(4) explain the benefit of further pre-training. I get lost in understanding the sentence "This results in 0.41B training tokens..." right above section 5.3.

### Questions
DNABERT2 is an update of the DNABERT, which is an application of the BERT structure to DNA data. My guess is that it first performs tokenisation of input DNA sequence, then pre-trains on DNA dataset to get the token embeddings, after that it adds a few layers to utilise the token embeddings for classification tasks such as promoter detection and transcription factor prediction. The manuscript made the following improvements: (1) use Byte Pair Encoding (BPE) for tokenisation (2) use attention with linear biases (ABiLi) for position encoding and (3) use flash attention and low-rank adaptation (LoRA) for acceleration. It also compiles a larger benchmark dataset for comparing different methods. The manuscript demonstrated that DNABERT2 improved over DNABERT and had a similar performance as Nucleotide transformer. 

I think the authors have done a decent amount of work and the work could be more useful for the community if the authors could
(1) perform an ablation study to quantify the contribution of BPE and ALiBi independently.
(2) explain why the code, data and pre-trained model could not be made public now
(3) explain why mcc and f1 are used as the comparison metric for different tasks
(4) explain the benefit of further pre-training. I get lost in understanding the sentence "This results in 0.41B training tokens..." right above section 5.3.

### Soundness
3 good

### Presentation
4 excellent

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
The authors describe a foundation model for DNA sequences, improving on existing models (of which there are relatively few) in terms of computational requirements.

### Strengths
-Incorporation of more recent language model techniques into the modeling approach.

- Foundation models have the potential to be a highly useful resource for the computational biology community.  There are very few options at the moment, and the significantly reduced computational requirements of DNABERT2 compared to the Nucleotide Transformer on the one hand, and improved accuracy over DNABERT, make it a welcome addition.

- DNABERT2 is appropriately benchmarked against DNABERT and the Nucleotide Transformer.

- The authors have curated a collection of datasets for benchmarking DNA language models.  The benchmark datasets are sufficiently challenging to provide good discrimination between the performance of the various methods, and indicate that there is still plenty of room for improvement.

### Weaknesses
 - Deep learning models applied to one-hot encoded genomic sequences appear to have a much higher level of interpretability than those that utilize k-mer tokenization, and I expect this to be even worse for the BPE encoding used in this work.  Unlike other areas of application, in computational biology applications, interpretability is a key factor in choosing a model.

 - "Despite having 30% more parameters than DNABERT, DNABERT-2 requires only one-third the number of FLOPs. This indicates the superiority of the Byte Pair Encoding (BPE)-based tokenization method over overlapping k-mer tokenization in terms of modeling efficiency." 
Not sure I agree with this statement - the increased efficiency might be the result of other differences between the models.
"This underscores the importance of providing the model with adequate data, particularly when the model size is scaled up, and further highlights the inefficiency of overlapping k-mer tokenization. The comparison between DNABERT and NT-2500M-1000g exposes the sample inefficiency of non- overlapping k-mer tokenization. Despite being trained on 2.5 times more tokens, NT-2500M-1000g achieves a performance similar to that of DNABERT."
Again, there are other differences between the models, so ascribing this to the difference in tokenization method is a stretch.  If you want to demonstrate the advantage of BPE tokenization, you will need to perform an experiment on two different versions of DNABERT2 - one with k-mer tokenization, and one with BPE tokenization.



### Questions
- "Despite having 30% more parameters than DNABERT, DNABERT-2 requires only one-third the number of FLOPs. This indicates the superiority of the Byte Pair Encoding (BPE)-based tokenization method over overlapping k-mer tokenization in terms of modeling efficiency."
Not sure I agree with this statement - the increased efficiency might be the result of other differences between the models.
"This underscores the importance of providing the model with adequate data, particularly when the model size is scaled up, and further highlights the inefficiency of overlapping k-mer tokenization. The comparison between DNABERT and NT-2500M-1000g exposes the sample inefficiency of non- overlapping k-mer tokenization. Despite being trained on 2.5 times more tokens, NT-2500M-1000g achieves a performance similar to that of DNABERT."
Again, there are other differences between the models, so ascribing this to the difference in tokenization method is a stretch.  If you want to demonstrate the advantage of BPE tokenization, you will need to perform an experiment on two different versions of DNABERT2 - one with k-mer tokenization, and one with BPE tokenization.  **The authors have addressed this point with a thorough ablation study**.

- Please compare your benchmark datasets with the recently published "Genomic benchmarks":
Grešová, K., Martinek, V., Čechák, D. et al. Genomic benchmarks: a collection of datasets for genomic sequence classification. BMC Genom Data 24, 25 (2023). https://doi.org/10.1186/s12863-023-01123-8

typos / grammar:

BENCKMARK: GENOME UNDERSTANDING EVALUATION (GUE)

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The author proposes a tokenizer for DNA language model, namely, using BPE, in contrast to the k-mer approaches as used before. The authors also propose a large-scale benchmark called GUE to compare DNA language models.

### Strengths
- Clear definition of motivations, challenges, and solutions
- The use of BPE makes intuitive sense
- Experiments look solid and extensive
- Solving an important problem of DNA LM 
- A new large-scale benchmark

### Weaknesses
 - Novelty is questionable since BPE is a well-known technique. The use of FlashAttention, LoRA, and AliBi are also not new. So methodologically, it is hard to gauge its novelty.

 - Is there potential for cross-species information leakage? For instance, given the substantial overlap in genomes between humans and primates, the model might easily predict the masked token.

- How does this compare to HyenaDNA?

- On page 7, the authors note that they utilize LoRA for NT but opt for full fine-tuning for DNABERT/DNABERT-2. However, in the methods section, LoRA is described as an integral part of the approach. This is somewhat perplexing.

- While the authors suggest further pre-training on GUE sequences, this might raise concerns regarding its ability to generalize to datasets with novel sequences. For a balanced comparison, it might be best if the authors refrain from additional pre-training on GUE sequences.

- Did the authors evaluate the sequence statistics of the GUE sequences in relation to the sequences from the pre-training corpus?

- The authors claim the method requires significantly less computational power and memory. Did they test the performance with a larger model size? If there wasn't a notable performance enhancement, it would be noteworthy to highlight this.

- Have the authors assessed how the model's performance varies with different dataset sizes?

- Have the authors conducted ablation on FlashAttention, AliBi, and LoRA?

### Questions
- Is there potential for cross-species information leakage? For instance, given the substantial overlap in genomes between humans and primates, the model might easily predict the masked token.

- How does this compare to HyenaDNA?

- On page 7, the authors note that they utilize LoRA for NT but opt for full fine-tuning for DNABERT/DNABERT-2. However, in the methods section, LoRA is described as an integral part of the approach. This is somewhat perplexing.

- While the authors suggest further pre-training on GUE sequences, this might raise concerns regarding its ability to generalize to datasets with novel sequences. For a balanced comparison, it might be best if the authors refrain from additional pre-training on GUE sequences.

- Did the authors evaluate the sequence statistics of the GUE sequences in relation to the sequences from the pre-training corpus?

- The authors claim the method requires significantly less computational power and memory. Did they test the performance with a larger model size? If there wasn't a notable performance enhancement, it would be noteworthy to highlight this.

- Have the authors assessed how the model's performance varies with different dataset sizes?

- Have the authors conducted ablation on FlashAttention, AliBi, and LoRA?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair
