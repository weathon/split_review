# Self-Attention-Based Contextual Modulation Improves Neural System Identification

- Decision: Accept
- Scores: 8, 6, 3, 8

## Abstract
Convolutional neural networks (CNNs) have been shown to be state-of-the-art models for visual cortical neurons. Cortical neurons in the primary visual cortex are sensitive to contextual information mediated by extensive horizontal and feedback connections. Standard CNNs integrate global contextual information to model contextual modulation via two mechanisms: successive convolutions and a fully connected readout layer. In this paper, we find that self-attention (SA), an implementation of non-local network mechanisms, can improve neural response predictions over parameter-matched CNNs in two key metrics: tuning curve correlation and peak tuning. We introduce peak tuning as a metric to evaluate a model's ability to capture a neuron's feature preference. We factorize networks to assess each context mechanism, revealing that information in the local receptive field is most important for modeling overall tuning, but surround information is critically necessary for characterizing the tuning peak. We find that self-attention can replace posterior spatial-integration convolutions when learned incrementally, and is further enhanced in the presence of a fully connected readout layer, suggesting that the two context mechanisms are complementary. Finally, we find that decomposing receptive field learning and contextual modulation learning in an incremental manner may be an effective and robust mechanism for learning surround-center interactions.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The manuscript asks if self-attention can improve predictions of primary visual cortex (V1) response to images. This is motivated by two facts: one is surround modulation data in V1, usually attributed to lateral and top-down feedback connections; and the other is that artificial recurrent architectures predict some aspects of V1 responses better than purely feedforward. Self-attention could augment feedforward networks with spatial context information, beyond or differently from what can be achieved with receptive field expansion due to successive layers and final fully connected layer.

The authors execute a series of well thought-out comparisons between alternative architectures and learning schemes. The main results indicate that self-attention indeed improves predictive power, particularly when models are trained incrementally (learning the receptive field first). And that this improvement is more visible in the ability to capture responses to the most driving images for the neurons, rather than the overall response correlation across all images. This is interpreted as evidence that receptive field computations are more important to capture overall tuning, whereas surround computations are modulatory.

### Strengths
Excellently well written and executed. The problem is situated in the relevant literature, the motivation and significance of findings are conveyed strongly, the novelty is not overstated and the design focuses sharply on the question being asked. The results are very convincing. A pleasure to read!

### Weaknesses
Minor only.

1) The paper certainly adds to understanding neural system identification. But at a high level, do the result say anything about V1 contextual modulation itself? Or do the authors envision a path to that goal by fitting self-attention augmented CNNs? In any event, I don’t think this detracts from the value of the manuscript.

2) Even though not systems identification, this paper https://pubmed.ncbi.nlm.nih.gov/37738258/ is very relevant and in my opinion should be discussed.



### Questions
1) It seems important to add a performance comparison between the self-attention augmented CNNs and CNNs with recurrent layers. Or to explain why not relevant. 

2) Does any of the model capture the basic modulatory natural of extra-classical receptive fields, i.e. surround suppression and no response to an annular stimulus? The analysis of Fig. 6 goes in that direction but it’s not quite the same, if I interpreted it correctly.

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
5

### Summary
This paper presents a method for predicting the neural activity of neurons in the primary visual cortex of primates upon presentation of natural images. This method is based on the use of a hierarchical neural network comprising several convolutional layers and learned in a supervised manner with the aim of predicting neuronal activity. An innovation of this algorithm lies in the inclusion of a self-attention mechanism in the processing sequence. This attention mechanism could then, on the one hand, help improve prediction capabilities and, on the other, help understand the modulation mechanisms present in a biological neural network which consist in facilitating or depressing the response of neurons according to a context.

### Strengths
The strength of this paper lies in the rigorous introduction of this model and the comparison of different architectures, enabling the reader to disentangle the role of different network components. This method is validated by computational simulations that quantify the correlation between observed and predicted activity. This methodology then enables predictions to be made that confirm or refute certain biological theories, such as the modulation of normal activity according to the context of neighboring neurons.

### Weaknesses
I've noted a number of weaknesses in the document that affect its comprehensibility and potential impact. Foremost, the presentation needs to be simplified. First, it is difficult to understand from the abstract that your aim is to predict neural activity. In terms of the structure of the paper, there are inconsistencies in the sequence of sections, making section 3.5 and the model evaluation seem to conclude the paper. Some parts of the methods imply knowledge of intermediate results, and a major restructuring is needed.

Secondly, the model is missing some essential elements for a proper understanding. If you describe it well, the input image given to the network is not the one you want to produce. From the figure, I deduce that it's the fluorescence contrast of the image, but this needs to be written more explicitly. Furthermore, the precise nature of the input to the network is unclear. Is it a single image patch, or a larger field of view? The spatial dimensions of the input and how they relate to the receptive field sizes of the V1 neurons being modeled need to be clearly stated. The lack of detail makes it difficult to assess the biological plausibility of the model.

Thirdly, the figures are not always clear: figure four, for example, neither shows nor explains what is shown here. I'm guessing that the images are sorted according to their response, and that you superimpose the prediction that is made. Figure five shows results, but with fonts too small to read. This figure can also be simplified, as many elements seem redundant. Finally, the results discussed in the discussion are interesting, as they allow biological facts to be deduced from the study of a neural network, and in particular from the inclusion of an attention layer. However, this conclusion may also be the consequence of the limitations of the various models. To be validated, the conclusion should be causally related to the mechanisms described. In particular, I'm surprised that you don't look more closely at the activity in the attention layer: what are the strength and distance of the different modulations? This would enable you to draw neurological conclusions.

### Questions
Assuming that the limitations detailed above will be corrected, I have many questions about this work:

You use a correlation measure to compare your predictions with neurobiological observations. Can you justify this approach in relation to the observed distribution of neuronal activity? Indeed, it seems that this distribution is sparse and that another measure might be more appropriate.

You have placed the attention layer after a features layer that is supposed to represent simulated activity in a neuron in the primary visual area. As such, can you interpret the various Q, K, and V features you've inferred during learning?

It seems you're trying to predict activity on a per-frame basis, but neural activity is dynamic. Do you think you can apply this type of model, and in particular the attentional layer, to the temporal domain?

Finally, you mention a homology between the neural network that learns to predict neural activity and the network of biological neurons underlying the production of this activity. This major point needs to be better introduced.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper demonstrates that a self-attention layer inserted in a convolutional network can improve its ability to predict neural responses to natural stimuli from macaque area V1. The neural responses were collected with two-photon imaging in two separate monkeys. Different variants of a feed-forward CNN are compared (with or without self-attention, with or without fully-connected spatial integration, with end-to-end learning or incremental pretraining and fine-tuning of specific layers). The authors conclude that self-attention can improve neural prediction accuracy, especially for explaining “peak tuning” (i.e., the top 1% of highest responses).

### Strengths
* Fitting neural network models to brain data is an important approach to determine the biological plausibility of artificial systems, and to understand computational brain mechanisms
* The methods are generally sound and the compared models and ablations allow us to draw conclusions about the investigated mechanisms

### Weaknesses
 * The paper does not clearly state its primary objective, and the reader is left to choose between two options. The main objective could be to prove that recurrent and horizontal interactions help explain extra-classical receptive field properties in V1, with self-attention as one specific way to implement these interactions. Or, it could be to argue that self-attention (as implemented in modern neural networks with Q, K and V projections) is a good model for recurrent/horizontal interactions in area V1. I believe the former interpretation is better supported by the data, although less novel (since earlier papers have already reported that recurrent layers can improve neural predictions). However, I fear that the community would more readily jump to the latter conclusion, which is unfortunately not well supported. To make this interpretation, the self-attention models should be directly contrasted with other baselines including one (or more) recurrent layer(s) that implement horizontal interactions without self-attention. In the absence of these baselines, only the first conclusion can be supported, but this hinders the novelty of the paper’s message. In any event, the authors should clearly state which of these two goals they are targeting.

 * There is no clear description of the training objective for the different models compared. I assume it to be a regression of single-neuron activation from each training image, using an MSE loss, but this should be described much more explicitly.
* The notions of “overall tuning” and “tuning peak” are used in the abstract and introduction, but these are not standard terms, and cannot be understood without some amount of explanation (e.g. “the tuning peak corresponds to the top 1% of highest responses”).
* The Zhang (2022) reference does not include information about a journal, preprint server or conference venue.

### Questions
* There is no clear description of the training objective for the different models compared. I assume it to be a regression of single-neuron activation from each training image, using an MSE loss, but this should be described much more explicitly.
* The notions of “overall tuning” and “tuning peak” are used in the abstract and introduction, but these are not standard terms, and cannot be understood without some amount of explanation (e.g. “the tuning peak corresponds to the top 1% of highest responses”).
* The Zhang (2022) reference does not include information about a journal, preprint server or conference venue.

### Soundness
2

### Presentation
2

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
This paper explores the role of self-attention mechanisms in modeling contextual modulation in primary visual cortex (V1) neurons of macaque monkeys. Key findings and contributions include:

* Adding a self-attention layer to convolutional neural networks (CNNs) improves neural response prediction of macaque V1 neurons in terms of overall tuning curve correlation and peak tuning (PT metrics). This suggests self-attention provides additional flexibility and benefits complementary to CNNs' inherent contextual modulation mechanisms (successive convolutions and fully connected layers).

* The classical receptive field is the primary driver of a neuron's overall response, as models focusing on receptive field information achieve the highest correlation. However, contextual modulation, especially via self-attention, is crucial for strong and robust peak tuning.

* Incremental learning, where the receptive fields are learned first followed by self-attention and fully connected layers, allows the model to properly learn the contributions of the receptive field and contextual modulation. This incremental approach leads to a receptive field-centric model more aligned with neurophysiological evidence.

* Interpretable contextual modulation effects, such as association fields, emerge in the self-attention module of models that capture peak tuning well.

* Self-attention augmented CNNs are more data-efficient compared to baseline CNNs.

Overall, the paper provides insights into the computational role of self-attention (single head) in modeling horizontal connectivity and contextual modulation in the visual cortex, and proposes an incremental learning approach to best train networks with self-attention.

### Strengths
The paper is overall well written and the results are quite convincing. Here are the points I believe are strengthening the submission:

* The paper introduces a new perspective on modeling contextual modulation in V1 neurons using self-attention mechanisms, which has not been extensively explored before.

* The authors systematically investigate the contributions of different contextual modulation mechanisms (convolutions, self-attention, and fully connected layers) and their interactions, providing insights into their roles in modeling neural responses.

* The incremental learning approach, where receptive fields are learned before contextual modulation, is inspired by the developmental process in the visual cortex, adding biological plausibility to the model.

* New evaluation metric: the peak tuning index is introduced to assess a model's ability to capture a neuron's feature preference, addressing the limitations of standard metrics like Pearson correlation.

* The authors demonstrate that models with strong peak tuning display interpretable contextual modulation effects, such as association fields, in the self-attention module. I actually believe that this last point should be included in the main paper instead of the Appendix, as it brings added value by bridging previous research at the interface of neuroscience, perception, and machine learning.

### Weaknesses
 **Major Weaknesses**

* While the paper compares the proposed models to established CNN architectures, it does not include comparisons with more recent state-of-the-art models, such as transformer-based models, which have shown promising results in modeling mouse V1 neurons. More precisely, while Li et al. (2023) is mentioned in the introduction, no comparison with this model is provided in the paper. Although it's true that multiple attention heads may intuitively seem unnecessarily complex for the task outlined in the paper, Li et al. (2023) demonstrates very good results in predicting neural responses in mouse V1 neurons. The lack of comparison with this model is a significant oversight, as it prevents a clear understanding of the relative performance of the proposed approach compared to the current state-of-the-art.

**Minor Details**

* Figure 1(b) is not readable: The axes labels, ticks, and different images are unclear. Consider resizing or reorganizing the figure differently.

### Questions
Just a minor question: In section 3.4, I read that the loss is MSE. Many (if not most) papers in the field use a Poisson NLL loss, even with two-photon data (where, I agree that assumptions of e.g., electrophysiological recordings and Poisson counting aren't met). Could you elaborate on the use of MSE? Have you tried both and found better results with MSE?

Overall, I'm happy to maintain the assigned score (I believe the paper is more of a 7 in its current state, but 7 is not among the allowed ratings) if a more extensive comparison with Li et al. (2023) is provided.

### Soundness
3

### Presentation
3

### Contribution
3
