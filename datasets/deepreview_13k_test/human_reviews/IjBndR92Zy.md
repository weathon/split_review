# Beatrix: Out-of-Distribution Generalization of Large EEG Model via Invariant Contrastive Fine-Tuning

- Decision: Reject
- Scores: 3, 8, 3, 1

## Abstract
The advent of large-scale foundation models has revolutionized EEG analysis; however, their ability to generalize to Out-of-Distribution (OoD) brain signals remains limited due to the inherent variability in physiological states, individual differences, and experimental setups. To address these challenges, we introduce Beatrix, a novel spectral EEG foundation model that achieves state-of-the-art OoD generalization across diverse brain activity tasks. Beatrix leverages a unique analytic wavelet-based spectral tokenization that captures the intricate non-stationary dynamics of EEG signals, and employs a semi-causal generative modeling approach during pre-training, enabling it to learn expressive latent representations capable of both interpolation and extrapolation across temporal and frequency domains. For fine-tuning, we propose an innovative Contrastive Invariant Fine-Tuning (CIFT) method that enhances domain-invariant learning without the need for explicit environment labels, thus significantly improving OoD generalizability in a parameter-efficient manner. Our multi-view Transformer architecture further integrates both spectral and temporal information, allowing Beatrix to comprehensively model EEG signals across channels. Extensive experiments demonstrate that Beatrix consistently outperforms existing EEG models in tasks such as seizure detection and forecasting, auditory neural decoding, motor imagery, and sleep staging, showcasing its robustness and broad applicability. By achieving superior performance with reduced fine-tuning costs, Beatrix represents a significant advancement in the field of EEG foundation models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
To address the challenges faced by EEG models in out-of-distribution scenarios, this work proposes a foundation model that employs a semi-causal generative modeling approach during the pretraining phase. In the fine-tuning stage, the model utilizes the Contrastive Invariant Fine-Tuning method, integrating both time-domain and frequency-domain information for representation learning.

### Strengths
This work conducted pretraining on a large-scale EEG dataset, focusing on key issues within EEG modeling. The model incorporates both time-domain and frequency-domain representations of EEG signals.

### Weaknesses
1. The writing of this paper is somewhat disorganized, with the related work section lacking necessary summaries and connections. The introduction of the methodology is also lacking in coherence and emphasis, resulting in low readability. 
2. While this work draws on advanced methods from various fields, there is insufficient discussion regarding the motivation and rationale for transferring these methods to the EEG domain, leading to a perception that the model is somewhat stitched together and lacks innovation. 
3. In terms of experimentation, the validation primarily relies on a self-collected dataset, which diminishes its persuasive power. Furthermore, the main text contains too few experimental results, lacking essential ablation studies, parameter experiments, and visualization results, rendering the findings inadequate.
4. The comparative methods employed in this work primarily consist of algorithms related to out-of-distribution (OOD) scenarios. However, as this study serves as a foundation model pretrained on large-scale data, it is recommended that comparisons be made with other foundation models.

### Questions
1. The contribution titled "Spectrotemporal Integration of EEG Representation" may be insufficient as a distinct contribution point, as this conclusion lacks novelty.
2. It appears that many related works have employed Analytic Wavelet Spectral features; however, there is a lack of citations to relevant literature.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presented a new EEG foundation model, which used the wavelet-based spectral tokenization. The model performance were systematically evaluated on many EEG task. And the new foundation model focused on the Out-of-Distribution generalizability in EEG analysis. The work was technically sound and solid. Overall, I like the paper and the work would be meaningful to the field.

### Strengths
The proposed EEG foundation model not only used the temporal tokenization that were used in previous studies, but included new wavelet-based spectral tokenization. Spectral features in EEG were usually very useful and stable for EEG analysis. Introducing the new module was a good idea.

### Weaknesses
More experimental results on diverse EEG tasks should be well organized in the main text. The main text only included the results of seizure detection and forecasting.

### Questions
1.  What were the importance of the two tokenization: the temporal tokenization and wavelet-based spectral tokenization. Did the authors have the ablation experiments on two modules? How much improvement did the spectral tokenization have for the model?
2. How was the out-of-distribution generalizability defined in the paper, different subjects, different tasks, or different data centers? I think the study would be strengthened to include more systematic experiments and analysis for the out-of-distribution generalizability. 
3. Why the EEG spectrogram in Figure 2 had up to 128 Hz frequency? We usually analyze up to 50 Hz spectrogram for scalp EEG. What were the frequency resolution and time resolution of spectrograms as the inputs to the spectral tokenization?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The submitted manuscript studies the problem of training and fine-tuning of electroencephalography (EEG) foundation models for out-of-distribution generalization (here, across subjects and sub-tasks).
Building upon prior works on EEG foundation models and invariant risk minimization, the authors propose a three-stage modeling strategy.

They split foundation model pre-training into two steps.
Using a corpus of publicly available diverse EEG datasets, they first train a tokenizer model that transforms short segments of single-channel spectrogram data into tokens.
They use a combination of several unsupervised loss terms (e.g., reconstruction, quantization, ...) to compose their training objective.
Thereafter, they use the same EEG corpus to train a combination of spectral and multi-view transformer networks.
The former is constrained to mix tokens within each spatial channel, and the latter is constrained to mix tokens along the channel-dimension independently for each time-frequency bin.
As loss they employ a reconstruction loss for masked tokens.
The employed semi-causal masking strategy combines BERT-style random masking and reconstruction with GPT-style autoregressive reconstruction.
After pre-training is completed most of the model parameters are frozen.

For model fine-tuning they propose contrastive invariant fine-tuning (CIFT) to adapt the model to specific downstream tasks, primarily, seizure detection and forecasting.
CIFT combines several ideas to perform parameter-efficient fine-tuning (PEFT) with a domain generalization learning objective.
First, a combination of prior PEFT methods (LoRA and bottleneck adaptors, trainable layernorm parameters) are utilized to tune the parameters of the spectral and multi-view transformer network. 
Additionally, a  temporal embedding layer is introduced along with trainable prompts.
A cross-attention layer is used to summarize the spectral and temporal information of each segment in the trainable prompts.
After passing the resulting tokens through the network, the proposed loss terms are computed.
Apart from the cross-entropy loss, the CIFT loss encompasses a CLIP loss between the spectral and temporal prompts that is tuned to focus on environment-invariant latent representations.
The authors evaluate their proposed approach in several experiments and ablation studies with EEG data.
Their evaluation focuses on seizure detection (n=16 subjects) and seizure forecasting (n=35 subjects) problems. Compared to many baseline methods, the proposed approach obtains the highest performance scores.

### Strengths
### Originality

The considered problem setting that tests for out-of-distribution generalization is a challenging yet highly relevant setting.
The proposed framework employs a domain generalization approach based on invariance minimization that has been under-explored in neuroimaging data including EEG. In combination with data-driven estimation of environment labels, the approach seems appealing for many practical use cases.

### Quality

Key to the success of EEG foundation models is to combine temporal/spectral/spatial integration in the presence of diverse hardware and electrode configurations.
The presented empirical results indicate that this contribution proposes a suitable solution for the problem.
Additionally, the presented ablation studies touches on some relevant directions.

### Clarity

The authors provide sufficient motivation for most of the design choices so that their combination of ingredients generates a plausible recipe to address the problem setting.

### Significance

Combining a foundation model with an invariant risk minimization fine-tuning objective to address the EEG domain generalization problem is a novel and interesting approach.

### Weaknesses
### Quality of the Experiments

- The presented empirical results (Table 1 to 11 as well as Figure 5) summarize the average performance across test sets, yet fail to indicate the variability of the results across random seeds and subjects. The lack of reporting variability is problematic because the considered datasets are of relatively small size. For example, the results presented in the main text (Table 1 to 2) consider datasets with a total of 16 to 35 subjects. Since subsets (whose sizes are not reported) are used for testing, the actual number of subjects in the test set are likely considerably smaller.
- I appreciate that the authors tested the proposed CIFT approach also with different model architectures (Table 2). However, after carefully studying the ablation experiments I am still wondering what factors drive the success of the proposed approach. 
Unlike stated in lines 463 to 466, the particular choice of fine-tuning adapter parameters seems to have a large impact on performance (Table 6).
In the same paragraph (lines 463 to 466) the authors mention that full-parameter and linear probing yielded similar OoD generalization as the proposed combination of adapter methods without substantiating the claims in terms of simulation results in tabular of graphical form.
- There seems to be a discrepancy between the performance of the proposed method (Beatrix + CIFT (r=16, K=8)) as summarized in Table 1 and the results summarized in Figure 5 (K=8, r={4,8,12,16}) at r=16. The results in Figure 5 are substantially lower (e.g., for the seizure forecasting dataset below 90% accuracy (blue line @ rank=16) compared to 91.8% reported in Table 1).
- The additional experiments on auditory brain decoding and motor imagery contain too little information to properly assess the presented results.
For example, the motor imagery experiments only comprise of Table 9 without any indication of the considered dataset.


### Clarity of Contrastive Invariant Fine-tuning (CIFT)

- It is unclear why you introduce a CLS token. Even though it is introduced it is not used in the considered loss functions.
- The function $\rho$ and its learnable parameters $\eta$ are not defined.
- The dimensionalities of the symbols in equations (5) to (10) are not defined.
- You use the undefined function $\rho$ to estimate the environment $\hat{e}$ and class $\hat{y}$ labels. However, in the considered datasets the number of classes is potentially different from your choice of virtual environment dimensionality $K$.

### Questions
### Introduction

- The first paragraph uses the terms neuroelectrophysiology and EEG (which is not defined but I assume you refer to electroencephalography) interchangeably. This is imprecise since both terms refer to different (but somewhat related) concepts. 
- Please use either "invariant contrastive fine-tuning" (title) or "contrastive invariant fine-tuning" (main text).

### Preliminaries

- $X^e$ and $Y^e$ in (1) are not defined.
- Readers who are not familiar with invariant risk minimization might not be familiar with the training objective, defined in (1). Please refer to relevant prior works.

### Methods

- lines 190 to 195: please additionally specify the dimensionality of the generated wavelet features as well as the patch size (as visually indicated in Figure 2.)
- Which probabilistic model did you assume in equation (4). If you used an isotropic Gaussian model, the NLL loss reduces to the classical MSE loss. Please clarify.
- $\mathrm{Aggregate}(\hat{V})$ in (7) should be $\mathrm{DifferentialbeHeaviside}(\hat{V})$ 
- dimensionalities of $\hat{e}$ and $l_{\mathrm{CIFT}}$ in (10) are unclear


### Experiments
- I would like the authors to clarify the differences between results in Table 1 and Figure 5.
- To address my concerns about variability, the authors should run additional experiments with more random seeds and report the obtained standard deviations (across seeds, but ideally also across subjects). Beyond that, the authors should conduct significance testing at the level of subjects. That is they should compute the performance of the model for each subject in the test set and then compare the results across baseline models with appropriate significance tests (or at least report test statistics like t-values).
- Since the authors report that the temporal domain tokenizer is an important ingredient in their method, they should also substantiate their claim with an appropriate ablation experiment.
- Please explicitly report the number of subjects and classes in the dataset as well as how you generated the data splits and their sizes (# subject and samples).
- Table 1: category SF is undefined (and overlaps with the scenario seizure forecasting (SF)). Column AUPRC/SD has formatting issues.

### Wording, Grammar and Organization

- line 159: SEEG is not defined.
- line 222: "adds" -> "add"
- line 230: "arrange" -> "range"
- line 331: "is" -> "are"
- line 377: $beta$ -> $\beta$
- line 430: define PEFT
- line 431: define ERM
- line 558: there is a broken reference so the appendix.
- line 664 to 666: the bibliography entry is incomplete.

### Soundness
1

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper presents Beatrix, an electroencephalogram (EEG) foundation model to enhance out-of-distribution (OOD) generalization. It employs the semi-causal generative approach for pre-training and the Contrastive Invariant Fine-Tuning (CIFT) method to facilitate domain-invariant learning without explicit environment labels. Experiments in the main paper and appendix demonstrate the performance of Beatrix in several tasks related to EEG analysis.

### Strengths
Extensive experiments conducted on multiple datasets and tasks, such as seizure detection, motor imagery, and sleep staging, offer comprehensive evidence of the model's performance.

### Weaknesses
- **Lack of Novelty**: All the components, including analytic wavelet transform, semi-causal generative pre-training, and VQGAN, have been previously proposed in the literature. The paper describes a lot for these parts, but it does not give correct citations. It seems to be packaged as its own work. For the remaining component, CIFT, there are factual errors and unclear representations in the description of the method.  Moreover, it is counter-intuitive to apply bottleneck adapters and low-rank adapters in the same model, which is not explained in the paper. Hence, the novelty of the paper is weak.
- **Factual Errors**:
1.  L262, 'CIFT incorporates three distinct low-rank adapters' and the following describes 'BottleNeck adaptor', 'Lora adaptor', 'Layer Normalization', where the 'Layer Normalization' is not a low-rank adapter but a common component in Transformer models.
2.  L212 admits that the model is based on Transformer, while the architecture in Figure 3 lacks the Feed-Forward component.
3.  In Figure 4, the right part of the figure is not clear. In particular, there are two arrows pointing to nothing and the computation of cross-entropy loss is not clear. 
- **Experiments**:
1. The main experiments compared with the state-of-the-art methods and ablation study are arranged in the appendix. The main paper should include the most important experiments and results.
2. The paper could have provided comprehensive ablation studies on CIFT, e.g. ablation on w/ or w/o CLIP loss.  
- **Representation Problem**:
1.  All the Figures are not vector diagrams, which are not formal.
2.  L141-143, the meaning of e is not clear.
3.  L237, the meaning of semi-causal is not clear. What is the difference between semi-causal and causal?
4.  A redundant left bracket in L250.
5.  Caption of Figure 3 dismatch the content of the figure.
6.  The words 'adaptor' and 'adapter' are used interchangeably, which is not formal.
7.  L377, 'beta' should be \beta.

### Questions
Discussed in Weaknesses.

### Soundness
2

### Presentation
1

### Contribution
1
