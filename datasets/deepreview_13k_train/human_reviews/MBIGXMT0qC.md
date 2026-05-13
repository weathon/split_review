# Multi-Scale Protein Language Model for Unified Molecular Modeling

- Decision: Reject
- Scores: 5, 6, 6, 3

## Abstract
Protein language models have shown great potential in protein engineering. However, the current protein language models mainly work in the residue scale, which cannot offer information in the atom scale. The strong power of protein language models could not be fully exploited to benefit the applications that cross protein and small molecules. In this paper, we propose msESM(multi-scale ESM) to realize the multi-scale unified molecular modeling by pre-training on multi-scale code-switch protein sequence and describing relationships among residues and atoms with a multi-scale position encoding. Experimental results show that msESM outperforms previous methods in protein-molecule tasks and is on par with the state-of-the-art in protein-only and molecule-only tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work aims to appy the powerful protein language models (ESM) to the applications of both small molecules and proteins. 


Specifically, the authors provides a multi-scale ESM (ms-ESM) model for the unified molecular modeling. The ms-ESM model can take both protein sequences and molecules with 3D coordinates as input. 


The model is pretrained using both protein dataset (AlphaFoldDB) and molecule dataset (from uni-mol). Each residue in a protein can also be unzipped to several atoms. The pre-training tasks are masked language modeling (MLM) and pair-wise distance recovery. 


The architecture of ms-ESM is very similar to ESM, and one main difference is that the atom scale position encoding (Euclidean distance + Gaussian kernel) is used as a bias term in the attention layers.


The proposed ms-ESM is evaluated on protein-molecule tasks, protein-only tasks, and molecule-only tasks.

### Strengths
The idea seems interesting. By unzipping atoms in some residues, the protein-specific ESM model becomes a model at both residue and atom scales.

### Weaknesses
1. To me, the presentation, especially the experiments part, is not clear. For example, the authors use ‘for more details of …., readers can find them in …’ many times, but this really restrict me to understand the implementation details. A better way could be ‘following …, we fine tune … using ….’ In addition, please list the data size of downstream tasks. 

2. About the ms-ESM model: during pre-training, what percentage of residues are unzipped? 

3. Ablation: The pair-wise distance recovery is only used at atom scale and requires atom coordinates as inputs. How about removing this loss? What is the performance? Is this term necessary?

4. The performance on protein-molecule tasks: I can’t intuitively understand why ms-ESM can outperform two separate pre-trained models (one for protein, and one for molecule)? Basically, I think the capacity of two models should be greater than a single model. Is the comparison fair? Please provide more explanation.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a multi-scale language model for protein and small molecule modeling. The author combines masked language modeling and pair-wise distance recovery to pretrain the model. The authors present competitive results against baselines on multiple tasks.

### Strengths
1. The paper is clearly written.
2. The multiscale modeling technique is novel.

### Weaknesses
1. The proposed method could not outperform baselines, as shown in Table.5 and Table.6.
2. Insufficient experiments regarding molecular representation learning affects the significance of the paper.

### Questions
1. Could you provide head-to-head comparisons against Unimol on molecular representation learning tasks, such as BBBP,  BACE, Tox21?
2. How about scaling the 35 million model to 650 million? Could you provide the corresponding results?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In the context of protein language models, this paper attempts to fuse the information contained at the residue scale with the one contained at the atom scale (i.e. the structure of the resides themselves) to produce better models. The protein sequence is thus represented by inserting the set of atoms constituting a certain residue inbetween the residues. To accomodate this change, the authors propose ad hoc position encodings depending on the scale (atom or residue). The method is tested in several (protein-molecule, protein-only, and molecule-only) tasks with good overall performances.

### Strengths
- the proposed idea makes sense intuitively, and appears to be effective across different tasks.

- the experiments are well thought and the results seem convincing, both in depth and width.

### Weaknesses
 - the technical novelty is limited; I understand code-switching is not novel but I value that it is ported to this field. However, the rest of the techniques used in this paper (like RoPE, or the transformer architecture) are not novel.

- Lack of detail on certain topics. For example, in Section 2.2, the ORDER procedure is not explained (there is a referral to Appendix A, where however I didn't find an explanation). Similarly, the "Atom Scale Position Encoding" section is not informative with lots of unintroduced symbols.

- The "slight modification of the Transformer" in section 2.4 appears poorly justified or at least needs more clarification. Why is $E^A$ added to the standard attention? What happens if it's not added? 

- Also in Section 2.4, my guess is that the scaling by $\sqrt{d_k}$ gets disrupted by the $E^A$ term. Can you comment on this latter point?

- The ablation study in Table 7 shows almost no improvement from vanilla ESM to the "w/o RSPE in atoms" variant.

### Questions
Mostly related to the weaknesses, see above. On the more discussive side:
- did you consider the idea of representing the structure of the residue with a graph neural network? What could be the up/downsides of this approach?
- it is unclear how the sequence length is affected by the addition of the atoms constituting the residues. Can you detail how long are the sequences you deal with, and how much their lengths increase by adding the atoms?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper extends the concept of protein language models to atom-scale and molecular data. Methodologically, the contribution of the paper are three-fold: (1) the development of a universal transformer tailored for molecule and protein data; (2) the introduction of a code-switch protein sequence approach to unpack residues; (3) the presentation of a multi-scale position encoding designed specifically for code-switch sequences. The authors claim that they effectively demonstrate the efficacy of their approach through enzyme-substrate and drug-target affinity tasks. Additionally, their method achieves comparable results in areas such as contact prediction, secondary structure prediction, and molecular property prediction tasks.

### Strengths
1. The idea of designing a universal transformer for molecules and proteins are of high potential. Such an approach has the potential to unify various downstream tasks related to both molecules and proteins. However, there are evident flaws in the methodology presented in the paper.
2. To my knowledge, the related work section about protein pre-training is thorough and comprehensive.

### Weaknesses
1. There are significant flaws in the design of code-switch protein sequences, which can potentially make the model learn meaningful insights from the unzipped sequences. Specifically, the approach of unzipping residues into atom sequences and predicting the masked atom type is questionable. Given the residue type and the types of adjacent atoms, deducing the masked atom type is often trivial, as the atom set is predetermined for each residue type. This suggests that unzipping residues may not introduce unique or non-trivial information, and the masked atom type prediction loss might not contribute any meaningful insight. The paper lacks a thorough investigation into the necessity and impact of this design choice.
2. The concept of multi-scale position encoding, which merges residue- and atom-level embeddings, lacks novelty. This approach has been explored in previous works, and the paper does not adequately demonstrate a novel contribution in this aspect. The ablation study, which only considers ablations on position encoding, further neglects the paper's other two significant contributions, namely, the code-switch protein sequences and the unified pre-training approach.
3. The experimental results show only marginal improvements over established baselines. For instance, ProSmith's results with ms-ESM offer only a slight enhancement over baselines, such as He et al. (2023) and Kroll et al. (2023b). Furthermore, the unified pre-training appears to diminish performance on tasks focused solely on proteins or molecules, compromising its viability for practical applications. The paper does not provide sufficient evidence to support the claim that the unified pre-training approach offers significant advantages over existing methods.
4. The protein-only tasks seem trivial when protein structures are used as inputs. With knowledge of protein tertiary structures, it becomes straightforward to determine if two residues are in contact and to identify the secondary structure. Moreover, since the pre-training task includes pairwise distance prediction, there's potential for data leakage, as the test data might overlap with the pre-training dataset. This raises concerns about the validity of the experimental results and the fairness of the comparison with other methods. The paper does not adequately address these potential issues.

### Questions
1. The concept of unzipping residues into atom sequences and predicting the masked atom type appears flawed. Given the residue type or the types of adjacent atoms, deducing the type of the masked atom becomes straightforward, since the atom set is predetermined for each residue type. This indicates that unzipping residues does not introduce any unique or non-trivial information. Additionally, there is a lack of experiments to demonstrate that the masked atom type prediction loss contributes any meaningful insight.
2. As shown in the Tables 2 and 3, ProSmith's results with ms-ESM offer only a slight enhancement over baselines, such as He et al. (2023) in Table 2 and Kroll et al. (2023b) in Table 3.
3. Are the pre-trained language models fine-tuned for specific tasks? If not, the tables should encompass results with fine-tuning.
4. The protein-only tasks seem trivial when protein structures are used as inputs. With knowledge of protein tertiary structures, it becomes easy to determine if two residues are in contact and to identify the secondary structure. Moreover, since the pre-training task includes pairwise distance prediction, there's potential for data leakage. The test data might overlap with the pre-training dataset.
5. Despite the possible data and information leakage in the experimental framework, the proposed method fails to outperform standard protein language models like ESM-2 in tasks such as contact and secondary structure prediction. Given that the model incorporates a broader range of pre-training loss than ESM-2, these results suggest that universal pre-training across both proteins and molecules may not offer advantages in protein-only or molecule-only tasks. This significantly weakens the paper's primary claim: the benefit of combining protein and molecule data for pre-training.
6. The ablation study only consider ablations on position encoding, neglecting the paper's other two significant contributions. It would be beneficial for the authors to explore comparisons with protein- or molecule-only pre-training, consider pre-training without unzipped sequences, and evaluate the impact of removing each pre-training loss.

Overall, I recognize the significance of developing universal models for molecule and protein pre-training. However, the paper exhibits considerable flaws in its methodologies and experimental sections, making it below the standard expected for publication.

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor
