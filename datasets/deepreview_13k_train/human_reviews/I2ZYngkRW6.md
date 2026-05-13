# Distilling Non-Autoregressive Model Knowledge for Autoregressive De Novo Peptide Sequencing

- Decision: Reject
- Scores: 3, 3, 5, 6

## Abstract
Autoregressive (next-token-prediction) models excel in various language generation tasks compared to non-autoregressive (parallel prediction) models. However, their advantage diminishes in certain biology-related tasks like protein modeling and de novo peptide sequencing. Notably, previous studies show that Non-Autoregressive Transformers (NAT) can largely outperform Autoregressive Transformers (AT) in amino acid sequence prediction due to their bidirectional information flow. Despite their advantages, NATs struggle with generalizing to longer sequences, scaling to larger models, and facing extreme optimization difficulties compared to AT models. Motivated by this, we propose a novel framework for directly distilling knowledge from NATs, known for encoding superior protein representations, to enhance autoregressive generation. Our approach employs joint training with a shared encoder and a specially designed cross-decoder attention module. Additionally, we introduce a new training pipeline that uses importance annealing and cross-decoder gradient blocking to facilitate effective knowledge transfer. Evaluations on a widely used 9-species benchmark show that our proposed design achieves state-of-the-art performance. Specifically, AT and NAT baseline models each excel in different types of data prediction due to their unique inductive biases. Our model combines these advantages, achieving strong performance across all data types and outperforming baselines across all evaluation metrics. This work not only advances de novo peptide sequencing but also provides valuable insights into how autoregressive generation can benefit from non-autoregressive knowledge and how next-token prediction (GPT-style) can be enhanced through bidirectional learning (BERT-style).
We release our code for reproduction in the anonymous repository here: https://anonymous.4open.science/r/CrossNovo-E263.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Note: I am not familiar with proteins research. However, I have given my best analysis of the work from a methodical perspective.

CrossNovo is a framework to autoregressive (AT) de novo peptide sequencing by distilling knowledge from non-autoregressive (NAT) models. This allows the model to capture bidirectional protein representation for decoding. Leveraging a shared encoder and cross-decoder attention, the approach combines strengths of both model types, purportedly achieving superior performance across multiple benchmarks. The study aims to address NAT's limitations with sequence generalization and optimization by combining AT’s sequential generation with NAT's bidirectional capabilities. Experimental results show state-of-the-art performance on two datasets, demonstrating improved amino acid precision and peptide recall. CrossNovo is suggested as a valuable tool for proteomics research.

### Strengths
* Combines AT with NAT in a novel way
* Achieves State-of-the-art performance
* Comprehensive benchmarking
* Detailed experiments

### Weaknesses
This reads like an engineering paper. It largely focuses on ensemble and engineering strategies without introducing a novel methodology. The use of a shared encoder and cross-decoder attention mechanism, while useful, does not represent a fundamental advance in model architecture for peptide sequencing.

Moreover, I am concerned that such engineering project could have led to extensive evaluations and finetuning, raising concerns about potential overfitting.

There might be ways to combine NAT and AT, but I believe the proposed approach is quite naive and has no theoretical grounding. It might be a result of the very short sequences that it works, I would like to see biological evaluations on longer sequences.

In general, for this conference I'd expect evaluations across diverse biological benchmarks with longer sequences to highlight how deep learning extends to proteomics.

### Questions
I'd like to see a comparison with the size of models for previous work, I want to know that this is not just a result of a larger model capacity.

### Soundness
3

### Presentation
2

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
The paper proposes a two-stage approach for mass-spectrum based De Novo peptide sequencing where the sequence of a particular peptide is predicted given its mass spectrum as input. The authors seem to combine the advantages of both autoregressive transformer (AT) and non-autoregressive transformer (NAT) for this task, by using the more efficient AT for decoding while incorporating the bidirectional representations from NAT. The first stage involves jointly training an autoregressive decoder an a non-autoregressive decoder to output the peptide’s amino acid sequence prediction. The second stage of supervised training involves concatenating the output representation of the non-autoregressive to the mass spectrum representations for the AT to condition on them during its decoding. Experiments on two benchmark datasets show that the proposed approach outperforms baseline approaches on most tasks.

### Strengths
Approach shows better empirical performance than baseline approaches

Combining the strength of both non-autoregressive transformer and auto-regressive transformer is an interesting idea

### Weaknesses
Limited Novelty: It seems to the reviewer that the approach is combining the representations from a trained non-autoregressive transformer (NAT) with the mass spectrum representations for the autoregressive transformer (AT) to condition on. It does not seem that there is distillation involved as what the distillation term is generally understood in the ML community. Rather, the proposed approach is a two-stage supervised training where the second stage is a finetuning process by adding the NAT representations as additional input representation for the AT decoder.

Application-specific studies: While combining the strengths of NAT and AT have the potential to impact various applications, only mass spectrum based de novo peptide sequencing is studied here which might only be of interest to a small subset of the ML community in this venue.

Clarity: Rationale and explanation of the proposed approach can be further improved (see questions below). The paper is at times challenging to follow even though the concept is actually rather simple.

Questionable design choice: the choice of CTC loss is rather uncommon for peptide and protein modeling but not explained or backed by experiments.

### Questions
Why is CTC loss selected over cross-entropy for NAT training even though cross-entropy is generally used for protein modeling? Why is only CTC used for NAT but not for AT training? It is common for peptides and proteins to have consecutive similar amino acid where they should not be merged; why would this be appropriate to merge these amino acid here? The reviewer would suggest an ablation study to support this choice.

Why is equation 1 used to encode the mass spectrum? How is v there related to mass-to-charge ratio and intensities, mz_i and g_i?

What is h_t^{update}? Does it refer to the AT decoder’s representation at the cross decoder attention block?
Typo: Line 249: docoders -> decoders

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
3

### Summary
This work introduces CrossNovo, a novel method for de novo peptide sequencing that integrates the advantages of both autoregressive (AT) and non-autoregressive (NAT) transformer architectures. The authors developed a joint training and distillation-based training approach that employs a shared encoder for both AT and NAT decoders. They also designed a novel cross-decoder attention mechanism that facilitates the transfer of knowledge from the NAT component to the AT component. The experiment results demonstrated that CrossNovo achieves superior performance on widely-used benchmarks for de novo peptide sequencing, surpassing existing AT and NAT models across various species and evaluation criteria.

### Strengths
The paper presents a novel hybrid approach combining AT and NAT models for peptide sequencing, featuring innovative cross-decoder attention and importance annealing techniques. It also provides comprehensive experiments and ablation studies. The clear structure and presentation enhance its accessibility. This work advances de novo peptide sequencing, with potential applications in other domains and implications for biological and medical research. The improved accuracy in peptide sequencing demonstrates the practical value of this contribution to proteomics.

### Weaknesses
There are a couple of points that can strengthen the paper.

- While the results are strong, the improvements over baselines are relatively modest in some cases (e.g. 1-3% on some species). The authors could provide more discussion on the practical significance of these improvements. It is unclear if these small gains are truly meaningful in real-world applications, especially considering the inherent variability in biological data. A more detailed analysis of the error distribution and the types of sequences where the model performs better would be beneficial.
- The computational difficulties of CrossNovo compared to baselines is not discussed. Given the additional components, it would be worth clarifying any additional computational costs required in the training. The paper should include a detailed breakdown of training time, memory usage, and hardware requirements compared to the baseline models. This is crucial for assessing the practical feasibility of the proposed approach.
- The experiments focus solely on protein tasks. Exploring the applicability of the proposed approach to other general domain sequence generation tasks could broaden the impact. The current evaluation is limited to peptide sequencing, and it's unclear if the proposed cross-attention mechanism would be effective in other sequence generation tasks such as natural language processing or DNA sequencing. Testing on diverse datasets would demonstrate the generalizability of the approach.
- While the paper provides problem formulations, I think it’s still quite difficult to understand the problem backgrounds due to limited explanations contained in the paper. For example, the authors didn’t fully explain about the inputs set such as mass-to-charge ratios. For the completeness of the paper, it would greatly helpful if the authors can provide more problem backgrounds and explanations as the supplementary materials. The paper needs more context on the mass spectrometry process and how the input data is generated. A detailed explanation of the data preprocessing steps and the specific features used as input would greatly enhance the paper's clarity.

### Questions
1.	Can you provide insights into why the cross-decoder attention mechanism is effective? What kind of information is being transferred from NAT to AT?
2.	Given that NAT models struggle with varying sequence lengths, how does CrossNovo handle this issue? Can you provide any experiment results regarding this point?
3.	Have you explored using the proposed approach for other sequence generation tasks beyond peptide sequencing? If not, do you think it would be effective, and what modifications might be needed?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes CrossNovo, a novel framework for distilling the bidirectional information of non-autoregressive transformers (NAT) for autoregressive transformers (AT). The training scheme consists of two parts: (1) a pre-training scheme for spectrum encoder + AT with regular cross-entropy loss and spectrum encoder + NAT with CTC loss with shared encoder parameters, and (2) cross-attention that transfers the final layer NAT embeddings to AT while freezing the NAT decoder. Experiments show SOTA results across all metrics.

### Strengths
- The writing is very clear, with neat figures, making the paper easy to follow.
- The motivation for the proposed method is well-explained.
- The results are strong, with thorough evaluations.

### Weaknesses
 - The two-step training scheme, while effective, is more time-consuming than previous methods. 
- The proposed method is a straightforward and expected combination of existing techniques (e.g., knowledge distillation is essentially a cross-attention with additional NAT embeddings).

Minor (typos):
- Figure 2: “Step 2: Cross-Decoder *Traning* for *Distiling* Learned Knowledge”, "*Probably* Matrix" 
- Figure 3 caption: Shouldn’t it be purple lines instead of green lines?

### Questions
How much extra training time does CrossNovo need compared to existing end-to-end methods?

### Soundness
4

### Presentation
4

### Contribution
3
