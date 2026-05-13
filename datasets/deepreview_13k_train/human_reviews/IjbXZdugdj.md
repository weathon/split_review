# Bio-xLSTM: Generative modeling, representation and in-context learning of biological and chemical sequences

- Decision: Accept
- Scores: 8, 6, 6, 3

## Abstract
Language models for biological and chemical sequences 
enable crucial applications such as drug discovery, protein engineering, and precision medicine. 
Currently, these language models are predominantly based on Transformer architectures. 
While Transformers have yielded impressive results, their quadratic runtime dependency on the sequence length complicates their use for long genomic sequences and in-context learning on proteins and chemical sequences. 
Recently, the recurrent {xLSTM} architecture has been shown to perform favorably compared to Transformers and modern \ac{ssm} architectures
in the natural language domain. 
Similar to \acp{ssm}, xLSTMs have a linear runtime dependency on the sequence length and allow for constant-memory decoding at inference time, 
which makes them prime candidates for modeling long-range dependencies in biological and chemical sequences.
In this work, we tailor xLSTM towards these domains and propose a suite of architectural variants called Bio-xLSTM. 
Extensive experiments in three large domains, genomics, proteins, and chemistry, were performed to assess xLSTM's ability to model biological and chemical sequences. 
The results show that models based on Bio-xLSTM 
a) can serve as proficient generative models for 
DNA, protein, and chemical sequences, 
b) learn rich representations for those modalities, and
c) can perform in-context learning for proteins and small molecules.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces Bio-xLSTM, a set of models that is tailored towards modeling of biological sequences. Specifically, the authors apply xLSTMs to different tasks of DNA, protein and small molecular modeling, analyzing the capabilities of xLSTMs in these domains compared to transformer and state-space models. Bio-xLSTM shows remarkable performance across all three domains and achieves state-of-the-art performance at homology aware protein generation.

### Strengths
- The usage of xLSTMs in the biological domain is a reasonable approach, particularly in the field of DNA where long context appears to be of importance.
- The paper is well-written, the evaluations and benchmarking is strong and includes reasonable baselines/competitors.
- The overall performance of Bio-xLSTM is strong and Bio-xLSTM is a valuable model for future research in the field.

### Weaknesses
 - I’m missing an evaluation of the diversity of the generated proteins and small molecules. 
- Regarding small molecule generation, I do not really see the benefit of large contexts. Specifically, the unconditional molecule generation uses a context size of 100 tokens. Maybe the authors could explain why the usage of xLSTMs should be beneficial in this domain (I see the point of ICL here, but for unconditional generation there doesn't seem to be any advantage, or?).

### Questions
- Do the authors have any explanations why Bio-xLSTM is strong on the histone tasks, but outperformed by NT-v2 500M on the regulatory annotation and splice site annotation tasks (Table A1)? Is there a general difference between the tasks that makes it harder to model it with xLSTMs?

- Did the authors generally observe any patterns where the xLSTM approach is beneficial, and where it might be less effective?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors adapt the xLSTM model architecture to the DNA, protein, and chemical informatics space. They compare with SoA models and benchmarks.

### Strengths
Generally I think the paper is well written, and the relevant baselines and comparisons across all domains are there.

I think the DNA-xLSTM tasks and benchmarks presented in Table 1 are strong.

Generally, I think the models (parameter sizes, configurations, training data) are comparable across baselines.

### Weaknesses
Generally, I feel like this paper is a bit of a grab-bag of computational biology. While the xLSTM architecture is consistent, the additional model additions are quite varied and bespoke. The use of different equivariant layers (PH and PS) across the DNA and protein tasks, while potentially beneficial, makes it harder to isolate the impact of the core xLSTM architecture itself. It would be beneficial to see a more systematic ablation of these architectural choices.

I’m not sure the large blocks of sLSTM and mLSTM math contribute much to this paper. Do you ever refer back to these equations later in the work?

Typo in header 3 - “BIO-XLSTM: LONGE-RANGE MODELING OF BIOLOGICAL AND CHEMICAL SEQUENCES”

“Hamming distance, HMMER score, and structural scores correlate well with sequence perplexity, with an average absolute Pearson correlation of 0.57 across clusters for the large Prot-xLSTM model” I would not say those correlate well. The R**2 is approx 0.325, which is not a lot of variance explained. Moreover, are these distributions normal? Should you be using spearman?

### Questions
“While Transformers have yielded impressive results, their quadratic runtime dependency” - In theory this is true, but it practice, there are more efficient implementations, such as Longformer (Beltagy 202), Linformer (Wang 2020), etc.

For the DNA-xLSTM tasks, to what degree do the PH or PS architecture additions cause a benefit vs just a xLSTM model? Same with the Mamba models (Table 1).

What are the spikes in the validation loss in Figure 3?

For Table 3, I’m always curious about an HMM baseline. How would a HMM of that cluster perform? It’s most certainly going to have many many fewer parameters.

### Soundness
3

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
The contribution describes application of an LSTM architecture to the modeling of sequential representation of molecules (biomolecules). The motivation for this choice of the architecture is to overcome quadratic scaling of transformers and offer linear scaling and constant memory requirements decoding. Three models are introduced as components of bio-xLSTM suite, specialized in modeling sequential representations of small molecules, proteins, and DNA. The reported results demonstrate performance improvement in certain tasks compared to the alternatives.

### Strengths
The paper explores alternatives to the modeling sequential molecular representations in chemistry that are expected to improve scaling and memory requirements. This is a great motivation, considering a) footprint of generative computing and b) its accessibility.

The authors discuss how to tailor the described architecture in relevant tasks.

### Weaknesses
The general weakness is that the paper contributes to an oversaturated field but does not offer any breakthrough. The case for LSTM is made by the appeal to their compute requirements, which are not discussed in terms of factual requirements of this study concerning memory bottlenecks, prefactors, scaling, etc. If all the reported results are produced on the same computing resource and performance improvement with LSTM  is marginal, why bother?

### Questions
The main motivation for the choice of LSTM is their favorable scaling. There is no scaling analysis in the paper, that clarifies the factual scaling and the observed prefactors. Even with fundamentally improved scaling, prefactors can be prohibitively unfavorable.

The authors provide performance measures in the form of averages and error bars over an ensemble of runs, which is great. At this point, however, it is more meaningful to test if the distributions of performance results are distinguishable instead of comparing averages. The authors do not have to do this exhaustively, but at least for the cases when their models are claimed to be outperforming the alternatives.

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
This paper presents the Bio-xLSTM framework, which encompasses three specialized models for distinct biological sequences: DNA-xLSTM, Prot-xLSTM, and Chem-xLSTM. DNA-xLSTM introduces reverse-complement equivariant blocks, essential for capturing the symmetry in DNA sequences. Prot-xLSTM is a homology-aware protein language model that employs in-context learning, addressing the variability in protein sequence lengths and context sizes. Chem-xLSTM is designed for SMILES representations of small molecules. Experiments demonstrate that the Bio-xLSTM framework is proficient in generative modeling and representation learning for DNA, proteins, and small molecules.

### Strengths
The paper introduces the novel xLSTM architecture, demonstrating its versatility in biological sequence modeling.It incorporates homology awareness in Prot-xLSTM and reverse-complement equivariance in DNA-xLSTM, addressing key challenges in protein and DNA sequence analysis.

### Weaknesses
1. **Lack of Motivation**: The paper fails to provide a compelling justification for the use of xLSTM over existing SSM models like Mamba. The authors do not clearly articulate why xLSTM is a better choice for the tasks at hand, which leaves readers without a clear understanding of the advantages it offers over established models.

2. **Lack of Novelty**: The concept of reverse-complement equivariance and the application of post-hoc conjoining (PH) and parameter sharing (PS) within the model architecture have been previously discussed in the literature, as seen in the Caduceus model (Schiff et al., 2024). This reduces the perceived novelty of the current work and may be perceived as a weak contribution to the field.

3. **Results Lack Convincing Evidence**: The manuscript's results section lacks the depth required to fully convince the reader of the proposed xLSTM models' effectiveness. An ablation study would significantly strengthen the paper by demonstrating the impact of the xLSTM components on performance, which is currently not provided.

4. **Redundant Writing**: The paper repetitively introduces the xLSTM architecture and training stategies, which has already been described in the original paper. This redundancy is unnecessary and detracts from the focus on the paper's new contributions and findings.

### Questions
1. Could you elaborate on the specific motivations behind choosing xLSTM over other SSM models? What unique advantages or improvements does xLSTM offer in the context of biological sequence design presented in this paper?
2. The performance improvements demonstrated in the paper may not be solely attributable to the xLSTM architecture itself. To convincingly argue that the enhancements are a result of the architecture and not just parameter tuning, the authors could provide a more detailed ablation study.

### Soundness
2

### Presentation
2

### Contribution
1
