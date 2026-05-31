## Human Reviewer 1

### Summary
This paper introduces the task of inverse protocol prediction which is the problem of inferring experimental metadata such as cell line, edium, seeding density, timepoint, microscopy, etc... from a single spheroid image. The authors use the publicly available SLiMIA dataset to benchmark different model types for this task. They further propose two custom designs.

### Strengths
* Interesting new problem with potential uses in science and industry
* Clearly described experimental setup

### Weaknesses
* reverse inference is a problematic term as it is an established term in neuroscience and also has misleading implications in an ML context
* The task of inverse protocol prediction is essentially multi-label metadata classification. The framing as a new “inverse modeling” paradigm is overstated
* The model likely captures acquisition-specific signatures more than biologically meaningful morphology - while this can also be interesting it points to less new biological understanding than implied

### Questions
Consider renaming the reverse inference task - maybe Inverse Protocol Prediction which I think you mentioned in the paper or Protocol Inference

### Soundness
3

### Presentation
1

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper introduces inverse protocol prediction, via inferring experimental metadata such as cell line, medium, density, timepoint and imaging parameters from single bright-field spheroid images. Using the SLiMIA dataset, the authors benchmark CNN, transformer, hybrid and hierarchical architectures for segmentation, protocol prediction and time series forecasting. They report strong results and interpret the model attention with GradCAM.

### Strengths
- **Interesting framing for the protocol prediction.** The idea of inverse prediction is interesting and can be useful when including potentially confounding factors and providing causal analysis.

- **Systematic benchmark.** The paper spans segmentation, protocol prediction, morphology related predictions, temporal prediction while also covering broad range of architectures.

- **Temporal task.** Constructing short temporal subsets with consistent protocols for sequence prediction is a practical and reproducible contribution.

### Weaknesses
- **Lack of code and seeds.** No implementation or split scripts are provided, limiting reproducibility and independent verification.

- **No confidence intervals.** Reported accuracies differ by small margins, making it very hard to rank without any significance tests or confidence intervals.

- **Dataset size and saturation.** SLiMIA (8k samples) is small for the model zoo evaluated. Results show very strong accuracies across almost all models and appear saturated. I suggest tempering the claims, or expanding the evaluation (creating harder splits, mask-only inputs, additional stress tests or more datasets).

- **Overly descriptive presentation.** Specifically Section 2 lists architectures, losses, optimizers at great length with very little interpretation. Much of this could be a part of the appendix. I would suggest the authors to create a figure where they present the bag of models, optimizers, losses and then use the saved space to explain how they operated the sweeps and what is the methodology together with their takeaways.

- **No empirical evidence for disentanglement.** The paper claims to separate morphology from imaging artifacts but provides no adversarial or cross domain validation supporting that. As far as I understand, the models that predict protocol values are trained independently from the morphology related tasks. I do not see any motivation drawn in the experimental section to justify or demonstrate the value of protocol tasks. I would expect creating an architecture such that the features for those tasks are shared vs independent; and try to demonstrated when the features are shared the morphology related accuracies improve. This would motivate the additional protocol prediction task significantly.

- **Causal ordering in HMTT unclear.** The sequence cell line, medium, seeding density, ..., replicates is asserted causal but I do not see clearly how or why that would be the clear order.

- **Consistency claims.** Related to my previous point, HMTT is said to yield consistent predictions despite lower accuracy, however consistency is not defined or measured. I did not understand if the model is doing the subsequent predictions given the previous ones to be consistent.

- **No ablations.** There is no vanilla baseline removing the proposed morphometric fusion or hierarchical conditioning (or adversarial training?).

- **Quantitative validation.** Can the authors come up with a quantitative measure for the biological validity? For the Grad-CAM results it would be beneficial to see the model attentions side by side across the models and relate them to their performance.

- **Temporal prediction baseline.** A simple copy the last frame baseline should be reported to verify that the models outperform trivial predictions.

- **Overstated conclusions.** For example in the conclusion the paper claims to "pave the way for AI systems that explain and validate experimental biology." which I dont think is supported by the experiments. Please either tune down such claims or provide empirical evidence to support.

### Questions
See the weaknesses above.


### Minor
I would recommend underscoring the 2nd best in the tables to improve readability.

### Soundness
3

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This work introduces "protocol prediction" from images, a novel task that reconstructs experimental conditions (cell line, medium, seeding density, timepoint, formation method, microscope, magnification) directly from a single bright-field spheroid image. Using the SLiMIA dataset of ~8,000 annotated spheroid images spanning diverse culture conditions, the authors frame this as a structured multi-label prediction problem and benchmark multiple architectures including CNNs (ConvNeXt-Tiny), transformers (ViT-B/16), hybrid models (CoAtNet), feature-augmented designs (Image-Shape Fusion Transformer integrating classical morphometric descriptors like area, compactness, eccentricity with learned embeddings), and hierarchical models.

### Strengths
The idea of predicting the experimental conditions from the images is intriguing, because it will allow change in protocol to guide one or the other outcomes. Authors compare a variety of architectures to predict multiple labels that describe the protocol from the images.  CoAtNet achieves best overall performance (95.72% accuracy, 0.8790 F1) by balancing local texture through convolution with global context via attention. The method achieves particularly strong performance on biologically grounded attributes: cell line (F1=0.9944), culture medium (F1=0.9642), and formation method (F1=0.9949), demonstrating that morphological signals in bright-field microscopy encode recoverable information about culture conditions. The work also presents the first temporal modeling of spheroid dynamics using ConvLSTM, PredRNN++, MetadataFusion, and PhyDNet to predict future morphological states, with MetadataFusion achieving best performance (SSIM=0.3985) by incorporating protocol-aware conditioning. Grad-CAM interpretability analyses confirm predictions rely on biologically meaningful features such as spheroid compactness, boundary sharpness, and necrotic core structure, while exposing dataset artifacts in replicate and magnification predictions. This demonstrates that microscopy-driven reverse inference can serve as an automated reproducibility check, flagging potential protocol mislabeling or execution deviations.

### Weaknesses
My assessment of weaknesses is centered on the practicality of capturing metadata relevant to the protocol and strategies used for training the models: 
* Protocol data (e.g., culture condition) is often captured at very coarse level. The specific image results after many steps in the protocol and influenced by parameters of imaging. The images are also subject to intrinsic heterogeneity in the cell/spheroid shape. Therefore the problem requires choosing the aspects of protocol that can be predicted and that should be controlled. 
* Technical replicate prediction is uniformly poor (best F1=0.5668 with CoAtNet) because replicates correspond to repeated imaging of the same spheroid with little morphological signal—models default to majority classes (T1-T8 account for 89.2% of images) despite focal loss and reweighting. 
*Microscope and magnification achieve near-perfect scores (F1>0.999) but they can be thought of as dataset artifacts (optical signatures like field of view, resolution) rather than biological inference. 
* Temporal prediction performance remains modest (SSIM<0.40, PSNR≈18 dB) because spheroid growth follows complex, non-linear biological processes (proliferation, compaction, necrosis) only partially visible in bright-field images, and SLiMIA provides short and irregular sequences making it difficult for recurrent models to learn long-term dependencies. 
* Finally, critical data limitations constrain validation: SLiMIA provides no persistent cell IDs across time, making it impossible to validate whether predicted temporal orderings or protocol attributes accurately reflect true single-cell progressions. The dataset is limited to a single experimental context (specific cell lines, culture conditions, imaging setups), and the framework has not been tested on diverse 3D culture systems (organoids, embryoid bodies, tumor spheroids) to establish generalizability. Attributes with fragmented or weak visual encoding (timepoint with >100 distinct values, seeding density with overlapping morphologies) remain challenging despite high accuracy, indicating the precision-recall trade-off may impact biological interpretation.

### Questions
* How did authors pick this dataset? What signal in data is available that protocol information is accurate? Can you acquire or identify a time-lapse microscopy dataset where individual spheroids/organoids are tracked with persistent IDs across complete maturation cycles (e.g., Cell Tracking Challenge datasets: http://celltrackingchallenge.net/ which provide ground-truth lineage information). Train inverse protocol prediction models on this dataset and quantitatively validate whether: (1) predicted temporal positions correlate with true temporal ordering, (2) predicted protocol attributes (seeding density, formation method, medium) match ground truth across developmental stages, (3) morphological reconstructions at intermediate timepoints not used for training match actual observations. 
* If you must use SLiMIA dataset, conduct biological validation experiments: for attributes where models make high-confidence predictions (e.g., "this spheroid was cultured in DMEMLG medium"), perform orthogonal experimental validation (e.g., mass spectrometry analysis of residual media, genotyping for cell line verification) to confirm predictions. This addresses the critical limitation that SLiMIA provides no cell tracking and establishes whether learned representations capture genuine biological dynamics rather than spurious correlations.
* Apply the inverse protocol prediction framework to diverse 3D culture systems beyond spheroids to establish generalizability: in addition to cell tracking challenge, you can consider the datasets from Allen Institute and Bioimage archive.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Summary
The authors propose a new classification task on the SLiMIA dataset of cell images, which they term "inverse protocol prediction". The paper benchmarks (i) segmentation models, which are required to differentiate the cell from the background for subsequent steps, (ii) classification models for inverting the protocol, and (iii) time series models for leveraging the predicted protocol features to predict future cell state. A GradCAM analysis is performed, which suggests that for some protocol labels (e.g. cell line), morphology is highly predictive, while for others (e.g. replicates), a latent confounder likely drives the predictions.

### Strengths
**Originality.** The work relies on a publicly available dataset of ~8,000 images, which is new enough that there are is not much work on it yet. The newly proposed task is essentially a metadata prediction task, although the framing as inverse protocol prediction is novel and potentially useful. The evaluation metrics are standard, and the use of GradCAM is nice but also a fairly standard diagnostic.

**Quality.** The dataset's offerings are well-exploited. The evaluations seem fair, i.e. not biased toward any particular model.

**Clarity.** The paper is fairly clear. I am not familiar with the dataset, but could follow the key details.

**Significance.** I am generally convinced that inverse protocol prediction could be a useful task, but I am not a domain expert. I am less convinced that the problem is yet in need of a benchmark of this nature.

### Weaknesses
My central issue is a combination of significance/novelty/suitability for ICLR's audience. My understanding is:

* The paper is at best a benchmark paper, and makes no methodological contributions. The benchmark target however is new and of unclear biological significance. The paper restricts to considering a particular modality (bright-field spheroid images) for which a single small dataset is available (~8,000 images).
* The authors argue that "inverse protocol prediction" (prediction of metadata from biological images) is a novel and significant task for this type of image. ICLR's primary audience (i.e. non-biologists) are not well-suited to evaluate or understand this. A cynical reader might assume that the authors trained easily accessible architectures to predict the only labels available (the image metadata), and got results with predictably variable performance depending on the information content of the label in the image (i.e. microscope is obvious, technical replicate is harder or impossible).
* The task framing seems to be the only novelty, and indeed the easy tasks seem solved/saturated (segmentation; cell line prediction) while the "hard" tasks remain predictably elusive (replicate prediction). To the authors credit, the GradCAM analysis provides some insight as to how and why.
* The time series task again seems somewhat contrived. The authors fit time series-class models (e.g. RNNs/LSTMs/CNNs) to a **two-timepoint input** and predict a subsequent frame. It is unclear what the biological significance of this is.
* Aggregating metrics across targets (Table 2) seems problematic, given that performance for some labels is saturated while for others it's clearly not.

### Questions
1. To what extent does an average accuracy of 0.9503 really differ from an average accuracy of 0.9572 (Table 2) given the size of the dataset and the nature of aggregation? What does this mean for the proposed use of these models in practice?
2. Can the authors demonstrate (through prior work ideally) the significance of the time series prediction task, or is this a novel task formulation as well?
3. Is this benchmark, as framed, solved? Why or why not? (Clearly the saturated tasks are solved, but e.g. for the tasks that are unsaturated, the authors at least acknowledge that maybe the information does not live in the images.)
4. The authors highlight several drawbacks of the dataset (particularly for the time series task, due to there being a small number of timepoints available), is this dataset optimal for this inverse protocol prediction task?
5. Are there other publicly available datasets that are suitable for the inverse protocol prediction task? For example, there are a large number of cell painting datasets available [1], which seem to meet the criteria: (1) segmentation is a useful pre-processing step and (2) experimental metadata with a similar structure is available. These datasets are also huge relative to the dataset in this paper. Could these be used to evaluate this same class of models on the same tasks, or at least the IPP task (number 2)? Why or why not?
6. What future work is there for machine learning scientists to do for this task?

[1] Chandrasekaran, S.N., Cimini, B.A., Goodale, A. et al. Three million images and morphological profiles of cells treated with matched chemical and genetic perturbations. Nat Methods 21, 1114–1121 (2024). https://doi.org/10.1038/s41592-024-02241-6

### Soundness
3

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 5

### Summary
The paper describes a methodology for processing 2D spheroid images from 3D stacks to predict the experimental conditions in which these images were captured. To that end, the paper introduces a dataset with 8K images and their annotations, and describes a data analysis workflow that involves deep neural networks for classification and segmentation.

### Strengths
* Exploration of a different paradigm to analyze spheroid images.

### Weaknesses
* The motivation and applicatios of "reverse inference" are not completely clear. 
* The need for predicting experimental parameters does not have a strong biological foundation.
* The methodology is based on existing methods and not new technical innovation is introduced.
* The experimental results indicate that the task can be solved with existing methods with high-accuracy.
* The dataset split for training and validation seems to be randomly assigned, introducing images with the same parameters both in training and validation. This may produce overly optimistic results and may not reflect a realistic use case (predicting parameters in a new experiment).

### Questions
* What is the need for predicting experimental conditions when these parameters are known and chosen by experts ahead of time?
* Why the reverse inference problem has value for biological analysis? What is the biological problem that this methodology aims to solve and why it was not possible before?
* Why the validation and test sets do not have examples of completely new experiments?

### Soundness
1

### Presentation
2

### Contribution
1

### Rating
0

### Confidence
4