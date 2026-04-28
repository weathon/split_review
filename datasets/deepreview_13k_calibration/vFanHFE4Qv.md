# Neuron Platonic Intrinsic Representation From Dynamics Using Contrastive learning

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
The Platonic Representation Hypothesis posits that behind different modalities of data (what we sense or detect), there exists a universal, modality-independent representation of reality. Inspired by this, we treat each neuron as a system, where we can detect the neuron’s multi-segment activity data under different peripheral conditions. We believe that, similar to the Platonic idea, there exists a time-invariant representation behind the different segments of the same neuron, which reflects the intrinsic properties of the neuron’s system. Intrinsic properties include the molecular profiles, brain regions and morphological structure, etc. The optimization objective for obtaining the intrinsic representation of neurons should satisfy two criteria: (I) segments from the same neuron should have a higher similarity than segments from different neurons; (II) the representations should generalize well to out-of-domain data. To achieve this, we employ contrastive learning, treating different segments from the same neuron as positive pairs and segments from different neurons as negative pairs. During the implementation, we chose the VICReg, which uses only positive pairs for optimization but indirectly separates dissimilar samples via regularization terms. To validate the efficacy of our method, we first applied it to simulated neuron population dynamics data generated using the Izhikevich model. We successfully confirmed that our approach captures the type of each neuron as defined by preset hyperparameters. We then applied our method to two real-world neuron dynamics datasets, including spatial transcriptomics-derived neuron type annotations and the brain regions where each neuron is located. The learned representations from our model not only predict neuron type and location but also show robustness when tested on out-of-domain data (unseen animals). This demonstrates the potential of our approach in advancing the understanding of neuronal systems and offers valuable insights for future neuroscience research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduced NeurPIR, a self-supervised contrastive learning approach to learn intrinsic representation for each neuron from population dynamics. The method leveraged CEBRA and VICReg for representation learning, and was evaluated using synthetic and two mouse datasets, showing ability to learn representations indicative of neuronal intrinsic properties that are decodable by downstream classifiers.

### Strengths
* The method combines CEBRA and VICReg to incorporate surrounding information and learn enhanced representation with contrastive learning, which is a novel approach.
* The paper is well motivated and tackles an important problem in neuroscience.
* The writing is clear and logical.

### Weaknesses
 * The usefulness of the out-of-domain evaluation on Steinmetz dataset is questionable. It seems as described on line 266, the self-supervised contrastive learning is performed on all neurons of all mice, including the test mice, i.e. the self-supervised model and classifier have to be retrained everytime new mice come in. Can any part of the model at least be reused during test time?
* Model architecture is not clearly explained by figures or texts. Some details of the methods are missing (elaborated in Questions).
* Some ablation studies are missing that would otherwise be helpful to understand the method in greater detail. For example, an ablation on which surrounding information included in the CEBRA framework has the most impact, or an ablation on different choices of contrastive learning methods besides VICReg might be helpful. 
* Results in tables and figures do not have errorbars. Adding sensitivity analyses would be helpful to quantify how significant the improvements of NeurPIR over the baselines are.

### Questions
* Line 54 and 55: the paper is motivated to make segments of activity from the same neuron or similar neurons to converge, while dissimilar neurons diverge. However, VICReg only uses positive pairs, and adds regularization to prevent representation collapse. How does using VICReg help push dissimilar neurons apart according to the motivation? 
* Figure 1: description in the texts and accompanying caption to understand this figure are missing. The figure does illustrate negative pairs, however, VICReg does not use negative pairs as mentioned above. How are negative pairs processed by the NeurPIR model?
* Line 134: the goal was to learn intrinsic neuronal representations on neuron population data, but it does not seem that activity of other neurons are used in the model (equations 1 to 4). How does the model use population dynamics to learn neuronal representations?
* Line 149: what is the length of one segment? Is there a chance that two randomly selected segments overlap with each other?
* Line 155: what is session information $X_{se}$? What are dimensions of $X_{st}$, $X_{be}$, $X_{se}$, $X_{si}$?
* Line 161: can the author provide more details on what is adaptive average pooling?
* Line 202: how the target value $\mu$ was set?
* Figure 4: how about precision, recall, and F1 scores (to be consistent with Tables 1 and 2)?
* It would also be helpful to provide additional details on the architecture design and training process, e.g. hyper-parameters, training time, etc.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work proposed NeurPIR, which focus on learning a platonic representation from neural activities data to reflect the inherent properties and neuronal identity, relating to molecular information. The goal of this work is to learned representations robust to variations due to external stimuli and experiment conditions. It utilized the self-supervised multi-segment contrastive learning strategy from CEBRA, and learning representations for neurons with compare data from different segments, different behavior information, session information, and for neurons share similar functional roles to align closely in their representations. And they further aggregate the representation with adaptive average pooling to extract time-invariant representations. They further incorporate VICReg loss to enhance the prediction. The work is evaluated on three benchmarks: Izhikevich simulation model, spatial transcriptomics data with neural activities, neuron location with out-of-domain data, and compared with two existing baselines NeuPRINT and LOLCAT.

### Strengths
1. The work is evaluated on three representative benchmarks, including one synthetic dataset, and two neural datasets. And it is compared against with two baselines and demonstrating SOTA performance in most of the tasks.
2. The work utilized a novel, distinct and effective method to utilize contrastive learning strategy to learn the platonic representation, compared to NeuPRINT with learning time-invariant representations with a neuron-wise look-up table for dynamics forecasting during self-supervised learning, or LOLCAT with label-guided representation with end-to-end supervised learning. 
3. The out-of-domain evaluation on unseen mice is an important question, which increases the soundness of the evaluations.

### Weaknesses
1. The core of the proposed approaches similar strategy as CEBRA to utilize the contrastive self-supervised approach for representation learning. The major difference from CEBRA is that it utilizes the adaptive average pooling to aggregated into time-invariant embedding, which might not necessarily guarantee the converge of the representation based on the data sampling. Further investigation could be done on how to guarantee converge based on different sampling strategy, or the requirement of amount of data to affect the predictive performance of the downstream tasks.
2. The evaluation on Steinmetz dataset is evaluated on decoding brain region with the learned intrinsic representations is related to analyze the invariant properties of the neurons, while brain region is only coarsely reflecting information from neuronal level, would it be possible to evaluate on more fine-grained information such as spatial location of individual units?
3. Ablation studies of VICReg loss should be performed.
3. Sensitivity analysis (i.e. error bar) are not included in Fig 4, the effect of data shuffling, random initialization, etc. could be reported.
4. Figure quality (i.e. font size, resolution) in the paper as limited, presentation and writing could be improved.

### Questions
1. Time complexity of NeuPIR compared to other baselines?
2. How many data samples are required to learn effective embedding?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a contrastive learning method (NeuPIR) for analyzing single-neuron activity data, with the goal of obtaining a representation which preserves property-level similarity of neurons (e.g. cell type). The method combines a variational autoencoder (CEBRA) with a contrastive loss (VICreg). NeuPIR is applied to a synthetic dataset and real neural datasets with cell type and brain area information, and compared against a few other methods of feature extraction (PCA, UMAP, NeuPRINT, & LOLCAT).

### Strengths
* Understanding the role of cell type diversity is a major challenge for neuroscience. A contrastive approach like this one, which can in principle be trained without labels, is likely to be the way forward given the difficulty of obtaining cell type information and activity simultaneously.
* Furthermore, learning representations which preserve cell property information is a application of obvious interest to the ICLR community.
* This paper performs the right experimental evaluations for its method, starting with a synthetic dataset, then moving to a real dataset where ground truth cell type information is available, and finally a real dataset with only brain region information, and compares against appropriate competitor methods.

### Weaknesses
 * The framing in terms of the "Platonic Representation Hypothesis" [1] feels like hype chasing. What is being presented here is just a contrastive learning method which is meant to identify similarity and differences in properties of neurons. This is not actually related to the PRH in a meaningful sense, which is about how representations _of the world_ converge across models in completely different domains. I am willing to raise my score if the framing of the paper (primarily title, abstract, introduction) is substantially revised to take this into account.
* The details of the method are not clear to me. CEBRA [2], at least as proposed, takes in a window of activity across a population of neurons (among other covariates) and maps it to a single latent point. I believe that here CEBRA is being applied to the activity of single neurons and their covariates but this is an important distinction which is not made explicit in the text. Furthermore, it's unclear how the temporal aspect of the data is handled within the CEBRA framework when applied to single neurons, as the original CEBRA was designed to process population-level activity over time. The paper should clarify whether each segment of a single neuron's activity is treated as an independent input to CEBRA, or if there's some form of temporal aggregation or windowing applied before feeding it into CEBRA.
* I am not convinced that other methods are being fairly compared to NeuPIR. There is a lack of detail about how hyperparameter selection occurred in the experiments which makes this difficult to evaluate. For instance, LOLCAT fails to label any neurons at all as Sst in Table 2 which suggests it wasn't tuned correctly for the task. The paper should include a detailed description of the hyperparameter search space and the cross-validation strategy used for each baseline method. It's also important to specify whether the same evaluation protocol was used for all methods, including the data splits and the metrics calculation.
* The method is not significantly original as it is combining the pre-existing CEBRA architecture [2] with the VIC contrastive loss [3], making this nearly a pure applications paper. This is not necessarily a flaw but does put the burden of innovation on the value of its scientific findings.

### Questions
* The abstract says "PRH posits that representations of different activity segments of the same neuron converge, while segments from inherently dissimilar neurons diverge" (lines 19-21). What representations this is referring to is not clear in context.
* The introduction should be more specific about what the method actually is, what the contrastive objective is, etc.
* Identifying cell type seems like a paradigmatic task where compressing neural activity into binned firing rate loses important information which may be contained in the spike train.
* The method section should provide more information about what CEBRA is.
* The cross-animal generalization experiment (5.3) is interesting but as predicting cell type is the more relevant problem I would be interested to see a similar generalization experiment with a cell type dataset as in 5.2.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proses a novel method called NeurPIR for extracting individual neuron representation based of neuron population recordings in a self-supervised fashion. For this purpose NeurPIR essentially combines a neural data specific sampling method, average pooled CEPRA embeddings, and a VICReg contrastive loss in a cohesive manner. The method is evaluated on a suite of synthetic and real neuron population activity recordings, where it superior performance to alternative methods.

### Strengths
- The paper tackles a relevant, yet extremely challanging task: extracting individual neuron characteristics from neuron population data.
- The paper convincingly demonstrates the proposed methods ability to do so to some extent, in particular compared to other available methods.
- The related literature, methods and experiments section is very detailed and well written, aiding interpretability of the results and reproducibility.

### Weaknesses
 * 1) The Steinmetz dataset experiment: likely doeant support the claim of being able to extract neuron internal represenations, as the method was trained to predict the location of the neurons, arguably an external neuron property?
   - Even if two exactly same neurons were integrated into two different brain regions they are likely identifiable through their activity as the differences in input to the two regions typically significantly deviates.
   - To claim exactraction of neuron intrinsic properties, the above effect would have to be significantly smaller than neuron intrinsic properly related differences, which is not validated.
* 2) The Conclusion: is crucially missing a paragraph on the limitations of the proposed method and the experimental findings. The paper would significantly benefit from it.
* 3) The Abstract: the first half is very confusing to read and doesn’t make it clear what the paper is actually about (for someone from a general computational neuroscience background). The paper would therefore greatly benefit from simpler and more concrete wording there.
   - Examples of terms that were not really helpful to me : “decoupling of intrinsic properties, “time-varying dynamics”, “dynamic activities”, “varying signals”, etc. What property, whos dynamics, what activity, which signal?
   - In particular “intrinsic properties” should be immediately followed by examples (later given), and the first mention of PRH feels out of place and its unclear how it relates to the sentences surrounding it. 
   - Furthermore, in the context of computational neuroscience “what information is conveyed by neural activities” most often implies figuring out what neurons try to communicate to process information, which the paper is not about. 
   - Finally, a statement like “NeurPIR captures the preset hyperparameters of each neuron” implies precise recovery e.g. $b = 0.2$. The proposed method was rather shown to capture rough categorical differences instead. More appropriate would could be e.g. “NeurPIR captures the class/category/type of each neuron”.
* 4) The Figures: have barely readable label sizes and legends, or missing annotation.
   - Figures 2 and 3 feature barely readable label sizes and legend
  - Figure 1 could use more labels that help relate the model description to the images in the figure. (e.g. X, H, Z, P, F, CEBRA, VICReg)
* 5) The Tables (or their descriptions): would benefit from some aggregate metrics across all categories.
* 6) For Reproducibility: manual labeling like in the Bugeon is hard to reproduce, and its unclear to me from the text whether these will be / are provided.

### Questions
1) How exactly are the experiments on the Steinmetz dataset supporting the claims of neuron intrinsic representation learning?
2) For the Bugeon Dataset: why was only data of mice A used?
3) For the Steinmetz Dataset; why wan’t also e.g. a 10-fold crossvalidation used (folds along the mice identity)?
4) Would you expect you method to also perform well if the number of Izhikevich neuron “types” was greatly increased (e.g. 10,20,30 categories)?
5) Will/are the exact labels used for three experiments, and in particular for Bugeon be available for others to be able to reproduce the experiments exactly?
6) Would you expect different results if max-pooling was used instead of mean-pooling?
7) Is there any more literature / papers exactly doing single neuron characterization based on neuron population activity (possibly on other datasets)? It seems to be challenging to find more related literature.

### Soundness
3

### Presentation
3

### Contribution
3
