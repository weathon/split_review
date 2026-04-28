# DNA Language Models for RNA Analyses

- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
Genomic Language Models (gLMs), encompassing DNA models, RNA models, and multimodal models, are becoming widely used for the analysis of biological sequences. Typically, models trained on RNA are used for RNA-related tasks, and models trained on DNA sequences are used for DNA tasks. However, this requires the development and maintenance of several classes of models to match the modality of the sequence. These models take significant resources and data to create, and maintaining separate models for DNA and RNA tasks is a computational burden. 

To reduce this burden, we introduce novel Adaptive Mixture of Codon Reformative Experts (CodonMoE) that can be incorporated into DNA gLMs in order to adapt them for mRNA-based predictive tasks. We show that, by using this plug-and-play operator, DNA-based gLMs can achieve performance similar to that of RNA-trained models on mRNA tasks. We further show that recent, efficient sub-quadratic DNA-based state space model (SSM) architectures can be used with the CodonMoE to achieve parameter- and computationally-efficient predictions for mRNA tasks. Specifically, experimental results demonstrate that CodonMoE improves diverse DNA-based backbones by a big margin, with some models achieving comparable or superior performance to current state-of-the-art RNA-specific models across several downstream tasks, while reducing both time complexity and model parameters.

Our results provide a path for focusing development efforts of gLMs on DNA models, which can then be adapted to mRNA tasks. Because DNA data is more prevalent than assembled mRNA data, and modeling efforts can focus on a single class of model, this is likely to foster improved DNA models for mRNA tasks at lower computational cost, and is a significant step towards unifying genomic language modeling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors suggest a strategy to adapt models trained on DNA data for mRNA downstream tasks. The proposed strategy uses the pre-trained language model as a backbone model to create nucleotide-level representations of the sequence. From the nucleotide-level representations codon-level representations are created and fed into the MoE module, and eventually the output representation is fed into prediction layers for the downstream tasks. The authors show for three different backbone models (HYenaDNA, Caduceus, and GPN-MSA) that the performance on the RNA downstream tasks can be improved by using their MoE adapter.

### Strengths
- **Novelty**: Adapting DNA models for RNA downstream tasks with an MoE approach is novel and could be interesting.
- **Relevance**: 
  * The authors show that their adaption strategy improves backbone model performances on codon-level RNA downstream tasks (compared to the not fine-tuned backbone models). The presented performance values are comparable with selected baseline, i.e models trained on the RNA modality.
  * The ablation study shows that the MoE module outperforms a simple mean baseline.
- **Clarity**: The scope of this work and the author's main contribution, i.e. applying an MoE module to codon-level inputs retrieved from a DNA backbone model, is described clearly and well. 
- **Reproducibility**: The code wrt the MoE module is given. (Code for training and full reproduction is assumed to be given once acceptance.)

### Weaknesses
 - **Novelty**: The fact that Mixture of Expert models initialized from some backbone language model typically perform well is known in the general language space [1-2] and applying this principle to the DNA/RNA domain seems straight forward.
- **Clarity/Relevance**:
  * The authors missed to provide information about how many parameters were added by the MoE module? Could performance gains just arose because of the increased number of parameters? The authors should set up an experiment in which the MoE module is compared with a fine-tuning strategy for which the parameters of the prediction head is increased such that the number of parameters of both approaches match.
  * For comparison, the authors should report performance values of the backbone models trained on the RNA domain.
  * The design choice of using codon-level representations (and also the author's choice for codon-level based downstream tasks) is not explained well. How well would an naive MoE approach without codon-level representation (on nucleotide-level based downstream tasks) work?

### Questions
- What are the performance values of the backbone models trained on the RNA domain?
- How many parameters where added to the method by using the MoE module?
- Why do models trained on the DNA domain so poor? What is the intuition behind this? DNA and RNA domain seem highly correlated.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose a MoE-based head for finetuning DNA LMs for RNA specific tasks.
They apply their CodonMoE head on 2 DNA LMs (Evo and Caduceus) and demonstrate improved Spearman correlation on 2 benchmarking datasets (mRFP expression  and SARS-cov-2 vaccine degradation).

### Strengths
The authors introduce a method for improving DNA LMs on RNA tasks in a parameter efficient way by utilizing codon structure in their model architecture. The benchmark improvements seem to be significant.

### Weaknesses
The authors show that CodonMoE improves performance on RNA tasks, however it is not clear that the MoE is at all necessary, and may just be adding unnecessary complexity for a 20M param head. CodonMean is a good baseline for ablation, however this baseline does not have additional training parameters unlike CodonMoE (20M parameters). The authors should include an additional baseline to specifically ablate the mixture-of-experts architecture vs. standard dense transformer layers. This baseline should have the same number of trainable parameters as CodonMoE and use exactly the same training hyper-parameters.

- How is train/test split produced for each tasks. Did the authors apply sequence similarity based split, or how is train/test leakage avoided?

-Table 1 Model parameters are misleading. It does not contain the parameter count for the base models (Caduceus, etc), but does for CodonBert? This column should provide the number of params for the base mode, and the additional params for CodonMoE head. Additionally, the authors should give the exact number of parameters in M, not >80M and <20M.

### Questions
- How is train/test split produced for each tasks. Did the authors apply sequence similarity based split, or how is train/test leakage avoided?

-Table 1 Model parameters are misleading. It does not contain the parameter count for the base models (Caduceus, etc), but does for CodonBert? This column should provide the number of params for the base mode, and the additional params for CodonMoE head. Additionally, the authors should give the exact number of parameters in M, not >80M and <20M.

### Soundness
3

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
This paper presents Adaptive Mixture of Codon Reformative Experts (CodonMoE), which can be integrated into DNA gLMs to tailor them for mRNA-based predictive tasks. The proposed method is assessed using both Transformer and SSM-based architectures across two mRNA-related tasks, showing performance that is on par with that of RNA-specific models.

### Strengths
Leveraging LMs cross bio-modalities is a meaningful direction, given the amount of data available in DNA and protein modalities. The proposed CondonMoE is flexible and can be plug-and-play into different backbones. The performance is encouraging for a limited number of demonstrated use case. In addition, theoretical proof demonstrates that CodonMoE is a universal approximator of RNA properties at the codon level.

### Weaknesses
The primary limitation of the paper is that it evaluates only two mRNA downstream tasks, with the proposed method showing better performance on just one of these compared to RNA-specific models. This raises questions about the effectiveness of the proposed method and under what circumstances mRNA-specific models should be preferred. A broader evaluation of additional mRNA downstream tasks, similar to those presented in the CodonBERT paper, is necessary.

The experimental design can also be improved, especially in terms of ablation study of the respective influence of the backbone FMs for feature embedding and the head used for regression and prediction. For example:

•	It would be interesting to see what performance can be achieved if the proposed CondonMoE is plugged into the mRNA-specific models, given that CodonMoE just reads mRNA sequences with clearly-identified codons. 

•	In addition, The RNA baselines (RNABERT, RNA-FM and CodonBERT) have been trained with TextCNN head whereas their DNA counterparts has been trained with MLP and XGBoost heads. This makes it hard to do a fair comparison against the baselines.

It would also be interesting to see what performance can be achieved if protein-based LMs are used as another baseline, by converting the known codons to protein sequences as the input, given that protein-based LMs have been trained on even larger datasets.

### Questions
See Weakness

### Soundness
2

### Presentation
2

### Contribution
3
