# Multimodal Lego: Model Merging and Fine-Tuning Across Topologies and Modalities in Biomedicine

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 8, 5

## Abstract
Learning holistic computational representations in physical, chemical or biological systems requires the ability to process information from different distributions and modalities within the same model. Thus, the demand for multimodal machine learning models has sharply risen for modalities that go beyond vision and language, such as sequences, graphs, time series, or tabular data. While there are many available multimodal fusion and alignment approaches, most of them require end-to-end training, scale quadratically with the number of modalities, cannot handle cases of high modality imbalance in the training set, or are highly topology-specific, making them too restrictive for many biomedical learning tasks. This paper presents Multimodal Lego (MM-Lego), a general-purpose fusion framework to turn any set of encoders into a competitive multimodal model with no or minimal fine-tuning. We achieve this by introducing a wrapper for any unimodal encoder that enforces shape consistency between modality representations. It harmonises these representations by learning features in the frequency domain to enable model merging with little signal interference. We show that MM-Lego 1) can be used as a model merging method which achieves competitive performance with end-to-end fusion models without any fine-tuning, 2) can operate on any unimodal encoder, and 3) is a model fusion method that, with minimal fine-tuning, surpasses all benchmarks in five out of seven datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors study the multimodal learning problem and propose a novel method that can merge encoders from different modalities freely. This is achieved through their newly proposed Lego block, which iteratively applies a discrete FFT to modality-specific dataset X^m and modality-specific latent representation L^m. The authors further propose LegoMerge, which can merge Lego blocks from different modalities without any additional training, and LegoFuse, which merge Lego blocks by stacking all the blocks and fine-tuning.

### Strengths
1. The idea of the LegoBlocks is novel and interesting.
2. Both LegoMerge and LegoFuse show promising results.
3. The wrapper nature of LegoBlocks allows its application to wider range of tasks.

### Weaknesses
1. The experiments do not include the merge between image and textual data, which might be the most common/important scenario. 
2. The authors state one of the advantage of the proposed method is the ability to merge more than 2 modalities, yet all experiments are conducted with only 2 modalities.

### Questions
1. I suggest to carry out the same type of experiments on CheXpert (https://arxiv.org/abs/1901.07031), where the downstream task can be disease classification. The experiments can be done only on the subset of CheXpert given the limited time during rebuttal.
2. If possible, I'd like to see the performance on datasets with >=3 modalities.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The presented work introduces multimodal Lego, a novel strategy to fuse latent embeddings from different domains, such as representations learned from images, tabular or time series. The authors hypothesize that processing and fusing embeddings in the frequency domain allows them to be agnostic towards the topology of the representation space and avoid signal interference when merging embeddings. To this end, the authors propose a so-called "LegoBlock" that converts multimodal embeddings via a Fourier transform before iteratively updating them via an attention mechanism. Multiple of these modules can be combined by calculating the harmonic mean between the embeddings ("LegoMerge") or by training a cascade of modules that sequentially update the latent embedding based on information from the various domains ("LegoFuse"). The utility of the method is demonstrated on three medical datasets that each combine two data modalities. LegoMerge is shown to outperform unimodal methods, while LegoFuse outperforms various recent multimodal baselines.

### Strengths
- The paper researches a very timely topic, the processing and fusion of multimodal medical data. The authors compellingly motivate this in a well written introduction and background section.

- The proposed method of adapting and fusing multimodal embeddings in the frequency domain code appears to be interesting, novel, and have some theoretical grounding.

- The conducted experiments include three public datasets spanning various data domains, as well as several relevant baseline methods.

### Weaknesses
 - The authors only provide limited theoretical motivation for their design choice of converting and processing embeddings in frequency space.

- Some parts of the proposed method are not clearly described. In particular, several aspects with regard to the architecture, functioning, training and tuning of the LegoBlocks are ambiguous or not described at all.

- Similarly, the description of the experimental setup is missing key information so that it is probably not possible to reimplement the benchmarking experiments.

- Several of the core claims made by the authors are not backed up by experimental evidence. In particular the method's ability to handle more than two modalities and its computational efficiency are not adequately evaluated.

- Finally, a meaningful ablation study is currently missing.

### Questions
Questions and suggestions regarding the work's motivation:

- The authors motivate processing the embeddings in frequency space by citing the advantageous properties of Fourier space with regard to its compactness, robustness against noise and robustness against signal interference. However, several of the referenced works are rather unspecific with regard to these claims and the authors do not provide detailed proof. I suggest that the authors expand the corresponding section and include more detailed arguments for this design choice.

- I believe that the statement that "LegoMerge does not require any finetuning" is slightly misleading. If I understand the method correctly the LegoBlocks are a wrapper around already existing embeddings that have to be trained themselves in order to tune (at least) the weights of the attention mechanism, $W^q_m$, $W^k_m$, and $W^v_m$. Compared to simply merging the embeddings, this does require additional fine-tuning steps. Accordingly, I do not believe that the statement that LegoMerge does not require any training time (cf. Table 3) is accurate. Consequently, I believe the paper should be adjusted to clearly reflect this.


Questions and suggestions regarding the proposed methodology:

- The paper is ambiguous on whether the raw input embeddings $h^{(A)}$ or their Fourier transform $\mathcal{F}(h^{(A)})$ are used in the attention mechanism of the LegoBlocks and the calculation of the harmonic mean during LegoMerge. Equations 3 and 4 indicate the former, while Figure 1 depicts the latter case. Please clarify this and clean up the notation.

- Also, in the right-most panel of Figure 1, why is one of the inputs to the LegoBlocks $L^{(A)}$?

- In the LegoBlocks, how is $L_0$ initialized, and is it updated during tuning? 

- How is the number of update steps $S$ tuned?

- One of the main claims of the work is its robustness against different topologies of embeddings. What happens if the initial data embeddings, $X^{(A)}$, $X^{(B)}$, $X^{(C)}$, have different dimensionalities and consequently require Fourier transforms of different dimensionalities? It is not apparent to me, why embeddings of time series and tabular information should be two-dimensional as suggested by the paper.

- Why do the authors apply an inverse Fourier transform at the end of each LegoBlock only to convert it back into frequency domain for a subsequent block or the final task head? Do any artifacts occur because of this repeated conversion?


Questions and suggestions regarding the conducted experiments:

- Even after reading Appendix C and D, many aspects about the conducted experiments are unclear to me and I do not believe that it is possible for a reader to reimplement them based on the current description. For example, how were the 80,000 $\times$ 80,000 histopathology images of the TCIA dataset encoded? Which mortality was assessed during the experiments with the MIMIC-III dataset? Which model was used to encode the time series data? The authors should aim to provide much more detail with regard to the conducted experiments.

- In light of the considerable effort required to fine-tune each LegoBlock (see earlier comments), I am missing a comparable effort to tune a neural network that processes the concatenated multimodal embeddings. Analogously to the proposed method, one could employ a multi-layer perceptron with S layers and an attention mechanism at each layer. If this approach was adequately tuned, it would function as meaningful, simple and potentially powerful baseline, while simultaenously directly ablating the design choice of converting embeddings to Fourier space.

- The authors should include experiments in which three or more different modalities are included. Currently, none of the conducted experiments supports their main claim that their proposed method scales effectively beyond two modalities.

- While the authors have conducted basic experiments demonstrating their method's ability to handle missing data, the conducted experiments are rather simplistic and only included in the supplementary material. Considering they pertain to a main claim of the work, the authors should expand these experiments and work them into the main paper.

- Have the authors conducted experiments whether the order of fusion during LegoFuse influces its performance?

- What is the added benefit of including both Tables 1 and 4 instead of simply merging them?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Multimodal Lego (MM-Lego), a flexible framework for transforming any set of encoders into a multimodal model with minimal or no fine-tuning. By using a wrapper mechanism to ensure shape consistency among different modality representations, MM-Lego enables efficient fusion of representations in the frequency domain, reducing signal interference across modalities. Results on seven tasks demonstrate MM-Lego’s strong performance.

### Strengths
1. MM-Lego offers a versatile solution to integrate various encoders into a single multimodal model with limited fine-tuning, bringing novelty with its wrapper and frequency-domain fusion approach.

2. The paper provides an extensive comparison with existing multimodal fusion methods, addressing multiple advanced criteria and establishing MM-Lego’s relative advantages.

3. Comprehensive experiments validate MM-Lego’s performance, particularly in the biomedical domain.

### Weaknesses
1. A primary concern is the lack of rigorous evidence supporting the claim that frequency-domain merging avoids signal interference. Unlike data types like images or time series, frequency representations of high-dimensional embeddings lack intuitive clarity, making the necessity of this approach uncertain. Specifically, the paper does not adequately demonstrate why a harmonic mean in the frequency domain is superior to other fusion methods in the spatial domain, such as concatenation or weighted averaging, particularly given the high dimensionality of the embeddings. The orthogonality argument, while theoretically sound for simple sinusoids, may not directly translate to the complex, high-dimensional embeddings produced by neural networks, and this leap requires more empirical justification.

2. While the authors highlight MM-Lego’s ability to handle multiple modalities, the paper lacks experiments involving more than two *distinct* modalities. Although the TCGA experiments use multiple tabular data sources, these are all of the same general data type, and therefore do not test the model's ability to handle truly heterogeneous modalities (e.g., text, audio, and images). This limitation leaves the model’s robustness in such scenarios untested.

### Questions
1. Could additional ablation studies be conducted to establish the necessity of frequency-domain representations in both LegoBlock and LegoMerge? For example, how would performance change if fusion occurred in the spatial domain?

2. Could the performance of LegoBlock be included in Table 1, not just in Table 4, to facilitate a more direct comparison in the main text? Additionally, certain phenomena, such as LegoBlock’s occasional underperformance compared to individual encoders like SNN or ABMIL, could benefit from further discussion.

3. A case study involving the fusion of more than two modalities would strengthen the paper’s claims about MM-Lego’s multimodal capabilities.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents MM-Lego, a general-purpose and modular learning framework to build performant multimodal models with minimal fine-tuning.  They introduce a wrapper for unimodal encoders to enforce shape consistency between modality representations and also harmonize the latent representations in the frequency domain to enable model merging with little signal interference. This paper conduct experiments on biomedical datasets and shows good results.

### Strengths
1. The study problem is interesting and useful. How to fuse the feature/prediction from multimodal data better.
2. The proposed framework demonstrate good results on the datasets.

### Weaknesses
In general, the presentation of this paper needs improvement, and the experimental section should be enhanced. 

1. The motivation for some key parts is not clearly articulated. For example, the authors mention "topological equivalence" and "topology agnostic." However, it is unclear why these properties are necessary for the problem being addressed. Specifically, the authors claim that their approach addresses a limitation of existing methods that assume equivalent network architectures across modalities. However, if a late-fusion strategy is adopted, where features are extracted independently and then combined, there is no inherent requirement for equivalent architectures. The authors' method also appears to be a form of late fusion, thus the motivation for this aspect is not clear.

2. The proposed framework falls under the category of "model merging." However, I am uncertain if this classification is accurate. Essentially, the authors aim to explore how to enhance the fusion of different modalities. If the method is truly a model merging approach, it should be combining the weights of pre-trained models, not just their feature representations. The paper does not clearly articulate how the proposed method differs from existing feature fusion techniques.

3. The key technical advancement appears to be the feature fusion conducted in the frequency domain. Again, the motivation for this approach is not well presented. Why is this method necessary? While the authors mention the orthogonal properties of the Fourier transform, it is unclear why this is beneficial compared to direct feature fusion in the original feature space. The paper does not provide a clear explanation of the advantages of frequency domain fusion over spatial domain fusion, especially considering the added computational cost of the transform.

4. The authors claim that the proposed framework is scalable, particularly regarding the number of modalities. However, in most of the experiments, they only utilize two modalities. This claim requires more experimental results to substantiate it. Furthermore, it is not clear if the different tabular data sources should be considered separate modalities. Modalities should represent different data formats or data sources, not just different information types within the same data format. For example, copy number variations and mutation status are both genomic data and should not be considered different modalities.

5. It is unclear how the proposed framework addresses the issue of missing modality data, which is an important challenge in the field. While the authors suggest their iterative approach can handle missing data, it is not clear how this approach benefits cross-modal interaction, which is a key aspect of multimodal learning. The paper should clarify if the model can still learn cross-modal interaction when some modalities are missing during training or inference.

6. The authors should elaborate more on the experimental settings and the methods used for comparison. For instance, it would be helpful to know if they employed the same feature backbone across experiments.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
2

### Contribution
2
