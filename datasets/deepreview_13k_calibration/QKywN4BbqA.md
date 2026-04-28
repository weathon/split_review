# $E^3$former: An Adaptive Energy-Aware Elastic Equivariant Transformer Model For Protein Representation Learning

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
Structure-informed protein representation learning is essential for effective protein function annotation and \textit{de novo} design. However, the presence of inherent noise in both crystal and AlphaFold-predicted structures poses significant challenges for existing methods in learning robust protein representations. To address these issues, we propose a novel equivariant Transformer-State Space Model(SSM) hybrid framework, termed $E^3$former, designed for efficient protein representation. Our approach leverages energy function-based receptive fields to construct proximity graphs and incorporates an equivariant high-tensor-elastic selective SSM within the transformer architecture. These components enable the model to adapt to complex atom interactions and extract geometric features with higher signal-to-noise ratios. Empirical results demonstrate that our model outperforms existing methods in structure-intensive tasks, such as inverse folding and binding site prediction, particularly when using predicted structures, owing to its enhanced tolerance to data deviation and noise. Our approach offers a novel perspective for conducting biological function research and drug discovery using noisy protein structure data. Our code is available on https://anonymous.4open.science/r/E3former-207E

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents $E^3$former, a novel protein representation model that combines an equivariant Transformer and State Space Model (SSM) architecture. $E^3$former aims at enhancing robustness against noise in protein structure data, it employs an energy-aware radius graph to dynamically adapt to node proximity and a high-tensor elastic selective SSM to efficiently capture geometric features. Experimental results indicate that $E^3$former surpasses existing models in tasks like protein binding site prediction and inverse folding, especially when dealing with AlphaFold-predicted noisy data.

### Strengths
- The paper proposes an innovative hybrid Transformer-SSM model that addresses noise issues in protein structure data.
- It implements an energy-aware radius function to adaptively construct protein graphs based on node proximity to mitigate data biases.
- It demonstrates substantial performance improvements over SOTA models across multiple datasets and tasks.

### Weaknesses
 - The captions of the figures and tables are too short and lack sufficient detail to facilitate understanding. For instance, Figure 2 requires more comprehensive descriptions of the depicted processes and components. Additionally, several terminologies and notations used throughout the paper are not clearly defined, leading to potential confusion for readers unfamiliar with the specific domain.

- While the model demonstrates efficacy on AlphaFold and crystal structures, its generalizability to other types of protein data with different structural features remains unclear. The reliance on these specific data types could potentially limit the model's applicability to broader protein structure prediction tasks.

- In Section 4.2, the rationale for selecting specific baseline models and configurations lacks clarity. The authors should provide a more detailed justification for their choices, including the specific strengths and weaknesses of each baseline model in the context of the tasks considered. A more thorough explanation of the implementation details and the motivations behind them would enhance the reproducibility and interpretability of the experimental setup.

- The results analysis and discussions are insufficient, particularly regarding the comparison across baseline models. For example, in Tables 2 and 3, a more in-depth discussion is needed to explain why the baseline results differ from the proposed model. What specific factors contribute to these discrepancies? Furthermore, in Table 3, the addition of certain features (e.g., ($\kappa$), ($\alpha$)) resulted in decreased performance in some tasks. The authors should thoroughly investigate and discuss the potential reasons for this phenomenon, such as potential overfitting or feature redundancy.

### Questions
- In the energy-aware radius graph module, the authors chose fixed parameters (($\epsilon$) and ($\sigma$)). Can the authors provide more detail on the rationale for these choices? What impact do these parameters have on results across different datasets? Has experimentation been conducted with alternative parameter combinations?
- In Table 3, the addition of certain features (e.g., ($\kappa$), ($\alpha$)) led to performance declines in some tasks. Can the authors elaborate on this phenomenon?
- In Figure 3, the authors state: "As illustrated in Figure 3, our model demonstrates a more substantial performance enhancement when the confidence is reduced." However, this does not seem convincing based on the figure. For instance, while $E^3$former’s AUPRC slightly outperforms the baseline in the 90-100 confidence interval, it is lower than the baseline in the 85-90 interval. More comprehensive results should be included, like reporting box plots for each confidence interval would be more informative.
- Based on Table 2 and Figure 3 (PPBS-AF All dataset AUPRC), there may be a long-tail problem in the results. Can the authors present the outcomes for the top 10 examples within the PPBS-AF All dataset to explore this further?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposed an Energy-aware Elastic Equivariant Transformer-SSM hybrid architecture
for 3D macromolecular structure representation learning. The core of the model is to adaptively
utilize the energy-aware module to bulid proximity graph and use the equivariant SSM module to
express high-order features sparsely. The above improvements enable model more tolerant to data
deviation and noise.

### Strengths
1. The evaluation is complete and thorough. I appreciate the authors’ effort on using confidence split for validing the noise tolerence. A kind suggestion is that the split interval is a little narrow (80-85,90-95…), instead using 0-60, 60-70, 70-80…. may be more approporiate. And the readers may also want to know the performance under noisy structures (e.g. with confidence below 70, 60, etc)
2. The writing of introduction is good and clear

### Weaknesses
1. There are typos and incorrect spaces in the method section, in Eq,3,4, 10,11. I kindly suggest the authors to keep a clean format.
2. The connections between equivariant elastic selective SSM and rotation noise are week for me. It’s hard for me to get the logic from rotation noise to SSM. I kindly suggest the authors to introduce more details about this part.
3. Performance improvement on some tasks are a little marginal and the improvement introduced by the key component Energy-aware radius function is marginal. The motivation for using SSM is missing.

### Questions
1. can we achieve the noise tolerance via some simple data augumentation such as adding some noise to the original protein structure as done in ProteinMPNN?
2. What’s the running time of E^3former? Can E^3former be applied to protein property predition tasks?
3. Does the noise tolerence problem really exsit? Since the structure prediction accuracy will continue to improve and this tolerance should be easily maintained via some data augumentation and pretraining technique like Graph Structure Learning on proteins.  I kindly welcome the disccusions on this from the authors.

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
5

### Summary
The authors present E3Former, an equivariant architecture based on Transformer-State Space Model for protein representation learning. The authors show strong empirical performance on a wide range of benchmarking tasks, exploring the robustness of the proposed method to structural artefacts by examining the performance on both experimental and predicted structures. The paper is generally well written though presentation can be improved.

### Strengths
* Evaluating the method on both crystal and predicted structures
* Empirical results are convincing across a broad range of tasks

### Weaknesses
My primary concern with this work is with the authors' premise that robustness to noise is a fundamental limitation of existing works. Often, works in this area have shown that adding noise to crystal structures provides a form of regularisation that generally boosts performance -- sometimes quite substantially. I think the issue that the authors are highlighting is not so much "noise" in experimental structures, but with \emph{prediction errors} which can substantially alter the input graphs and affect model training. I'd suggest being clearer with this distinction

Also, the trend in this area of research has been towards developing large pre-trained models which can be fine-tuned for a range of tasks. I think this contribution would be strengthened by some exploration of the ability to scale the proposed method and how it compares to existing pre-trained structural encoders.


### Minor

* L49: "Highly sensitive" -> High sensitivity
* "while also tackling the flexible property of macromolecules" - What exactly are the authors referring to?
* L79: " t omaintain" -> to maintain
* L79: repetition of "in various tasks"
* Mind missing spaces thoughout (L129,132, 271, 272, 305, 307)
* L189: Should this not be \Epsilon_{norm}
* L273: Inconsistent bolding of $G$
* I believe L277 should read: "NOT used in inverse folding task"
* L283: Displacement vector?
* Table 5: seq indentity -> Seq. identity
* Appendix D: "BOARDER IMPACT" -> "Broader Impact"

### Questions
* How much hyperparameter tuning did the authors do? Particularly for the models that were not drawn from the ProteinWorkshop benchmark such as equiformer.


* L284: During each training or inference stage -> What does stage refer to here? Every epoch? Every batch? Or is the adjacency fixed for a given training run?
* In Figure 4, a crystallographer would consider all of these resolutions extremely good -> good. I suggest expanding the range of resolutions considered
* Were the ablation studies hyperparameter tuned?
* What does the highlighting denote in Table 6?
* In the appendix, the authors mention there were difficulties mapping the Masif site dataset labels to AF2 predictions. Could they please elaborate a little here?

### Soundness
3

### Presentation
2

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
The paper introduces $E^3$former, an adaptive energy-aware, elastic, equivariant Transformer model designed to handle protein representation learning effectively, especially in the context of noisy data from protein structures. Traditional models struggle with robustness due to structural noise from both experimentally determined and predicted protein models (e.g., AlphaFold structures). The E3former addresses these issues with a novel hybrid approach, combining a Transformer with a state space model (SSM) that enhances its robustness and adaptability to noise. Inspired by molecular dynamics, this model uses an energy-aware radius function and adaptive radius sampling to define local neighborhoods, mitigating data bias effects in protein proximity graphs. The model incorporates an elastic selective SSM that leverages high-order tensors and sparse representations to improve signal-to-noise ratio and retain equivariance.

### Strengths
1. This paper is well-organized and clearly written.
2. The combination of energy-aware radius functions and equivariant high-order tensors offers a fresh approach to handling noise in protein structures.
3. The paper exhibits a high level of technical rigor and methodological detail. Each component, from the energy-aware graph construction to the high-order tensor elastic selective SSM, is thoughtfully designed and empirically validated.

### Weaknesses
1. The paper’s primary motivation is to address noise in structural data from both experimental and AlphaFold-predicted sources. However, the paper lacks a detailed quantitative or qualitative analysis of the specific types and impacts of noise present in these datasets. Without a thorough analysis of how noise in these data affects current models, it is difficult to assess whether the E3former’s adaptive mechanisms effectively target the underlying issues. For example, the paper does not discuss whether the noise is primarily in bond lengths, angles, or dihedral angles, nor does it quantify the magnitude of these deviations. This makes it difficult to understand the specific challenges the model is designed to overcome.
2. While the authors introduce two new datasets (CATH-AF and PPBS-AF) based on AlphaFold-predicted structures, these datasets appear to be relatively simple conversions of existing datasets into AlphaFold’s predicted coordinates. The paper does not provide sufficient detail on how these datasets were generated, specifically how the mapping between original experimental structures and AlphaFold predictions was handled. This lack of clarity raises concerns about the potential for data leakage or biases introduced during the conversion process.
3. The experimental setup, while extensive, could be strengthened by testing E3former’s generalization across experimental and predicted data sources. For example, evaluating the model’s robustness by training on CATH-AF’s training set and then testing on the CATH test set would provide critical insights into E3former’s performance across different data domains. The current evaluation primarily focuses on performance within the same data source, which does not fully demonstrate the model's ability to handle the variability between experimental and predicted structures.

### Questions
Can the authors provide a detailed analysis of the types and magnitudes of noise typically found in both experimental and AlphaFold-predicted protein structures? How do these impact the performance of existing models?

Did the authors test E3former’s ability to generalize by training on one data source (e.g., CATH-AF) and testing on another (e.g., experimental CATH)? If so, what were the results, and if not, what are the anticipated challenges or expected outcomes?

### Soundness
2

### Presentation
2

### Contribution
2
