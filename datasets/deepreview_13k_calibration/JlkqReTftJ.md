# Model Zoos for Benchmarking Phase Transitions in Neural Networks

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3

## Abstract
Understanding the complex dynamics of neural network training remains a central challenge in deep learning research.
Work rooted in statistical physics has identified phases and phase transitions in neural network (NN) models, where models within the same phase exhibit similar characteristics but qualitatively differ across phases. A prominent example is the double-descent phenomenon. 
Recognizing these transitions is essential for building a deeper understanding of model behavior and the underlying mechanics.
So far, these phases are typically studied in isolation or in specific applications. 
In this paper, we show that phase transitions are a widespread phenomenon.
However, identifying phase transitions across different methods requires populations that cover different phases.
For that reason, we introduce Phase Transition Model Zoos, a structured collection of neural networks trained on diverse datasets and architectures. These model zoos are carefully designed to help researchers systematically identify and study phase transitions in their methods. 
We demonstrate the relevance of phase transitions across multiple applications, including fine-tuning, transfer learning, out-of-distribution generalization, pruning, ensembling, and weight averaging. The diversity of applications underscores the universal nature of phase transitions and their impact on different tasks.
By providing the first structured dataset specifically designed to capture phase transitions in NNs, we offer a valuable tool for the community to systematically evaluate machine learning methods and improve their understanding of phase behavior across a wide range of applications and architectures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Phase Transition Model Zoos, a comprehensive collection of neural networks trained across various datasets, architectures, and methods, including fine-tuning and transfer learning. The authors present phase diagrams based on established metrics across diverse settings and include detailed experimental procedures for generating these model zoos.

### Strengths
- The paper provides a clear and accessible background, making it understandable for readers who may be unfamiliar with the topic.
- This paper offers an extensive benchmark of model zoos for studying phase transitions in neural networks, covering a variety of network architectures, datasets, and training methods, which is valuable for further research and analysis in this area.

### Weaknesses
 - The number of runs (i.e., three) used to average the results may be insufficient to substantiate certain claims and could impact the robustness of the findings.
- As noted by the authors, these model zoos are restricted to classification models within the computer vision domain, which may limit generalizability.
- The learning rate scheduler likely influences the phase diagrams of neural networks [1], yet the model zoos do not include datasets trained without a learning rate scheduler, which could provide additional insights into phase behavior.

### Questions
### Major
- While these model zoos offer valuable resources for exploring phase transitions in neural network training for both ML and statistical physics communities, their large size may present challenges for practical use. Can users download or access only specific parts of the zoos they need?

### Minor
- There is an inconsistency in the seed settings: lines 242 and 665 list seeds as {1, 2, 3}, while Table 1 uses {0, 1, 2}. Please ensure consistency in these settings.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a structured dataset of trained neural networks to facilitate the study of phase transitions in neural networks. Specifically, the authors trained a collection of two types of ResNet models (18 and 50) on SVHN, CIFAR-10, CIFAR-100, and TinyImageNet as well as a ViT on CIFAR-10 and CIFAR-100. For each model and dataset, they trained a grid of models using 8 (7 for the ViT) different model widths (as an example of a "load-like" hyperparameter, determining the model capacity) and 8 (7 for the ViT) different batch sizes (as an example of a "temperature-like" hyperparameter, affecting the noise-level of training). Each training is repeated with 3 different random seeds for a total of >1800 trained models.
The dataset contains multiple checkpointed model weights at different training epochs, along with performance metrics (e.g. train/test loss & accuracy), and crucially, "loss landscape metrics". These metrics, such as the trace and largest eigenvalue of the Hessian, or mode connectivity measurements, help describe in which "phase" a neural network is (e.g. underfitted, undersized, etc.) and identify phase boundaries.

The authors then use their dataset to demonstrate the usefulness of phase information in four ML methods (fine-tuning, transfer learning, pruning, and ensembling). For example, they identify that "the best pre-trained model does not result in the best transfer-learned model" and that incorporating phase information can be beneficial.

### Strengths
- The paper curates a structured dataset of trained neural networks aimed specifically at phase transitions. The provided neural networks include meaningful observables, like Hessian statistics. Sharing this dataset could help facilitate research, by allowing researchers to directly use the dataset without spending the compute training a large number of models. In my opinion, the strength of the dataset is the addition of loss landscape metrics describing the network beyond the performance metrics.
- The paper is well-written and organized. It is structured clearly, describing the included metrics, and the process of generating the dataset, as well as a section describing potential applications.
- Phase transitions are an interesting lens to study neural networks. Having a comprehensive dataset is a great building block to accelerate research in this area. In particular, studying fine-tuning, transfer learning, pruning, and ensembling using phases is interesting and - at least to me - novel.

### Weaknesses
### Dataset has a limited scope

- As mentioned by the authors, the model zoo is limited to computer vision models and specifically image classification. Furthermore, it only uses (relatively) small-scale models and datasets. I appreciate that the paper acknowledges the domain limitation and that this current version of the dataset already required significant computational resources. However, I also believe that the usefulness and therefore impact of the work would increase significantly by considering other domains or model scales. For example, including models trained on text or audio data, or exploring larger models with more parameters, would broaden the applicability of the dataset.
- By varying batch size and model width, the current dataset only explores a single temperature-like and load-like parameters. As a reader, I often asked myself whether a specific conclusion applies to all temperature or load-like parameters or is a specific property of batch size/model width. Having only one hyperparameter per type makes it impossible to disentangle the question and thus limits the usefulness of the dataset. For instance, different learning rate schedules or optimizers could act as alternative temperature-like parameters, and varying the number of layers or the dimensionality of hidden layers could serve as different load-like parameters. The lack of diversity in these parameters restricts the scope of the conclusions that can be drawn from the dataset.
- Additionally, the "grid resolution" (i.e. number of batch sizes or model widths) is relatively low. I am aware that increasing the grid also substantially increases the computational costs. However, I am not sure whether the current resolution allows a sufficient distinction between smooth and abrupt changes, i.e. allow meaningful identification of phase transitions. In other words, phase transitions are basically about detecting sharp edges in the plots but a low-resolution or blurred plot makes it hard to detect edges. In comparison, Yang et al. (2001), seemed to use a significantly higher resolution.

### Phase transitions insights

I am unsure how robust the provided insights are and how well they generalize.
For example, the conclusion that "fine-tuned models exhibit clear phase transitions in their performance, and these phases overlap substantially with the phases of the pre-trained models" is only drawn from 2 or 3 examples (the section mentions Figures 4, 9, and 11, but Figure 11 doesn't have a "fine-tuning" subplot). The limited number of examples makes it hard to assess the generality of the claim. Furthermore, the observed overlap could be a coincidence in the specific scenarios considered, rather than a general property of fine-tuning.
Similarly, the conclusion that "Choosing the best pre-trained model does not result in the best transfer-learned model" is taken from 3 examples (Figures 5, 15, and 16). However, in Figure 16, as far as I can tell, the best test accuracy is achieved at the same point as the best fine-tuning test accuracy (batch size 128 and 256 model width). This specific counter-example raises concerns about the robustness of the conclusion. Additionally, the distinction between fine-tuning and transfer learning is unclear (see "Questions" Section) with all subplots being labeled "Fine-tuning Test Acc".

Similarly, the conclusion on pruning, "Models pre-trained in higher-temperature phases [...] tend to perform better post-pruning [...]" (line 358), seems to be based on a single example (Figure 6) (and even here, the batch size of 256 seems to be a bit of a counter-example). The lack of multiple examples and the presence of a counter-example make this conclusion weak. For weight averaging, the authors state that "Averaging over epochs improves performance in early phases (I and II), where the Hessian trace is large" (line 422). However, Figure 14 seems to be a counter-example: Here, the $\Delta$ Test Acc Wise-FT is negative where the Hessian trace is large (i.e. top right corner). The presence of counter-examples and the reliance on single examples for some conclusions weaken the overall impact of the findings.

Overall, I think the conclusions are not convincingly demonstrated. Perhaps showcasing the predicted power of the data could strengthen this. By only looking at the phase information, can you predict which model will have the best pruning/fine-tuning performance?

### Unclear applications for future research

This might be subjective and due to my research background but I have trouble grasping concrete applications of the dataset beyond further studying the dataset itself. For example, in line 105, the authors write, that the dataset "can help researchers systematically identify phase transitions in their methods, and comprehensively benchmark those". What type of methods does this refer to? How can the model zoo be used to identify phase transitions for new methods? The lack of concrete examples makes it difficult to understand the practical utility of the dataset. Despite the dedicated section (Section 5), I find it hard to see direct use cases of the dataset which wouldn't require extensive re-training. The dataset seems more like a collection of models and metrics, rather than a tool that can be readily applied to new research problems.

### Questions
### Open Questions

- I am unfamiliar with CKA. Does a larger CKA indicate more similar representations (or less similar)?
- Do you perform any hyperparameter tuning, e.g. for the learning rate? You mention that "By varying the width, we achieve variations in model capacity without changing the architecture or having to adapt the training scheme" (line 238), but wouldn't changing the width require tuning the learning rate if not using something like muP?
- In line 256, do you mean "Phase IV-A" instead of "IV-B"?
- What is your distinction between fine-tuning (Section 4.1) and transfer learning (Section 4.2)? Depending on the community, the difference might be adapting to a new dataset vs. a new task. But here, in both cases, it is image classification no? And Figure 5, which belongs to the transfer learning section, also calls it "Fine-Tuning Test Acc".

### Plots

To me, some of the plots were confusing or missing information. Some (subjective)examples:

- Some plots are small and thus hard to read, e.g. the subplots in Figure 3.
- I think the plots would be improved if all subplots contained the phase annotation. For example, in Figure 3, only the subplot a has annotated phases and I would love to see the same separation in the other subplots. Same with the plots in the appendix, where no phase distinction is provided.
- Figure 1 is missing a color bar. Although primarily a qualitative plot, I believe a color would still be useful as the main argument is about the existence of phase transitions, i.e. abrupt changes in model behavior. Without a color bar, it is difficult to distinguish between an abrupt and a smooth change given the low grid resolution.
- Figure 6 seems to have the wrong subplot (or wrong caption) for the top subplot.
- What are subplots with the title "$\Delta$ Test Acc Wise-FT"? Judging from the context, I am assuming this is the weight-averaging strategy (i) as described in Section 4.5.

### Nitpicks

- Line 74: Is there a typo in "over different pre-trained models - model populations"?
- In line 90, you mention that the "model zoos contain a total of 1829 models". My calculation results in 1830 models, as follows: $(\underbrace{2}_{\text{ResNet models}} \cdot \underbrace{4}_{\text{ResNet datasets}} \cdot \underbrace{8 \cdot 8}_{\text{ResNet grid, e.g.~width and batch size}} + \underbrace{1}_{\text{ViT models}} \cdot \underbrace{2}_{\text{ViT datasets}} \cdot \underbrace{7 \cdot 7}_{\text{ViT grid, e.g.~width and batch size}}) \cdot \underbrace{3}_{\text{random seeds}}$. Did I misunderstand something?
- The paper uses inconsistent capitalization, i.e. "Testing Methods on Populations of Neural Networks" (line 70) vs. "Loss landscape metrics" (line 133).
- Line 286, there should be a space before the citation.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a dataset of trained models with multiple checkpoints across 10 combinations of ResNet and ViT architectures, trained on CIFAR-10, CIFAR-100, SVHN, and Tiny ImageNet. Each model is trained over a grid of varying batch and model sizes (interpreted as the temperature-load landscape). Through analysis of loss landscape metrics, the paper identifies distinct phases and phase transitions within this landscape. The main result demonstrates that phases and phase transitions exist also in a range of applications such as pruning, fine-tuning, ensembling, transfer learning, and weight averaging, suggesting that the presence of distinct phases is a prevalent phenomenon.

### Strengths
The paper demonstrates the existence of phase transitions in a more diverse set of models/datasets compared to prior work as well as on a variety of neural network methods including pruning, fine-tuning, ensembling, transfer learning, and weight averaging.

The work encourages evaluating methods across different model phases and phase transitions, suggesting that examining model behavior systematically across various regimes can lead to more robust evaluation methods than single-point evaluations.

In particular cases, the analysis of the phases provides insight on how certain components of the training pipelines such as learning rate decay and data augmentation impact the phases.

### Weaknesses
The paper primarily extends earlier work on phase transitions in neural networks to a broader range of datasets, models and methods but lacks substantial novelty.

Despite Section 5 outlining possible uses for the Model Zoo dataset, no concrete application is provided to demonstrate its practical relevance. Including a simple concrete example would be highly beneficial in demonstrating the utility of the dataset.

The scope of the Model Zoo dataset is limited by the use of relatively small datasets and models, excluding e.g larger and more widely used datasets such as ImageNet.

### Questions
- Could you please elaborate on how Model Zoos specifically "help researchers systematically identify phase transitions in their methods", as suggested in the paper?

- In general, how can researchers utilize the provided Model Zoo to benefit different methods beyond those directly included in this work?

- Could you please elaborate on the statement in lines 258-259: "... decaying the learning rate by 1e4 under cosine annealing increases the area of Phase IV (well-trained regime) while reducing the presence of Phase II …". It is not quite clear to me how this conclusion is made?

- Why does line 242 say models are trained using random seeds {1, 2, 3}, but in Table.1 seeds are reported to be {0,1,2}?

- In Figure.5 the dataset used in the bottom grid, CIFAR10, doesn't match the dataset specified in the caption STL-10.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work presents model zoos as a contribution to the study of phase transitions of neural networks (NNs) occurring in different scenarios. The authors recognize the necessities of phase transitions in NNs for a deeper understanding of deep learning, which could bridge the gap of our understanding of NNs. Based on the loss landscape taxonomy (loss landscape metrics and the categorized phases) of previous works, the authors annotated performance and loss landscape metrics across a large population of pre-trained models to identify such phases in their corresponding loss landscapes. The study empirically shows that phases robustly emerge within each model zoo population, and demonstrates that it also relates to the phases of different NN training methods or applications.

### Strengths
Presenting a large scale of model zoos for phase transition of NNs is indeed strength of the work. I agree with the authors that the model zoo about this scale could be valuable to researches of understanding the fundamental behavior of NNs.
While related works have already shown the existence of different phases based on loss landscape metrics, this work strenghten the previous works by building a diverse population of model zoos.

Section 3 shows distinct phases emerge across model population, and Section 4 relates these phases of the pre-trained models with diverse NN training methods. These heavy empirical results are the strengths of the paper.

### Weaknesses
While I highly appreciate the authors work for building a large scale of model zoos to the community those who are interested in the foundational understanding of NNs, I think that the following points should not be left undiscussed.
1. First of all, while the authors claim 'phase transitions' or 'phases' of NNs, I think this term should be used with more strictness. I understand the phase transition of NNs couldn't be nicely written with mathematical (or physical) rigor. The previous study which seems to provide the basic setting of this work [1] is published almost 5 years ago, and I would expect to give more theoretical aspects of this empirical findings. For instance, what is the order parameter in this scenarios? Is it a discontinuous or continuous transition? Of course it is indeed a challenging problem, but providing a theoretical discussion and its corresponding empirical evidence would highly improve the concreteness of this work. Also, while the answers of my sample questions could be interpreted with the provided experimental results, but I expect adding a discussion about this would add more clarification to the general audience.
2. Closely related to the first point, where is the phase 'transition'? While it is helpful to discriminate distinct phases across the loss landscape, in the notion of phase transition, investigating the transition between two phases should be accompanied in this empirical study. For example, between Phase IV-A and Phase IV-B, if temperature corresponds to the control parameter and CKA corresponds to the order parameter (my tentative guess), I would expect a empirical results showing the phase transition curve along these two parameters.
3. In the Figure 4 and 5, I'm curious about the model similarity (model distance or CKA) between the pre-trained model and after fine tuning or transfer learning. I couldn't find the exact settings for the fine tuning or the transfer learning both in main text and supplementary materials, so if I might be so bold as to predict, I don't expect the model before and after transfer learning should differ that much, and based on that, it does not seems surprising. Providing the model similarity before and after fine tuning transfer learning, and the different phase plots across different transfer learning settings (e.g. training only the last block, last two blocks, and so on.) could be helpful.
4. Similar with the third point, ablation experiment with respect to pruning ratio could help support the authors claims.

### Questions
My main concerns are stated in the weaknesses part above. For the questions, I've found several typos and possible miswritten texts that made me confused to follow the paper. I would like to ask some of ambiguities regarding those, please correct me if I'm wrong.
1. Near line 305, how does Figure 9 and 11 relates the phase of the pre-trained model? In the supplementary materials, the captions for Figure 9 and 11 says weight averaging.
2. Same for line 332; Figure 15 and 16, line 385; Figure 11.
3. Due to the minor point 1 and 2, maybe the captions of Figure 9-17 (line 421) which are intended to show more examples of weight averaging could be wrong I believe?
4. In Figure 6, the caption describes that the figure shows (top) before pruning and (bottom) after pruning. However the top subfigure shows the plot for mode connectivity. Which description is correct?
5. It would help the general audience to understand the setting of the experiments regarding weight averaging if Wise-FT method is mentioned in the main text (which happens to be not, while Git Re-basin have been mentioned).

### Soundness
1

### Presentation
2

### Contribution
2
