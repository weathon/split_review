# Multi-session, multi-task neural decoding from distinct cell-types and brain regions

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
Recent work has shown that scale is important for improved brain decoding, with more data leading to greater decoding accuracy. However, large-scale decoding across many different datasets is challenging because neural circuits are heterogeneous---each brain region contains a unique mix of cellular sub-types, and the responses to different stimuli are diverse across regions and sub-types. It is unknown whether it is possible to pre-train and transfer brain decoding models between distinct tasks, cellular sub-types, and brain regions. To address these questions, we developed a multi-task transformer architecture and trained it on the entirety of the Allen Institute's Brain Observatory dataset. This dataset contains responses from over 100,000 neurons in 6 areas of the brains of mice, observed with two-photon calcium imaging, recorded while the mice observed different types of visual stimuli. Our results demonstrate that transfer is indeed possible -combining data from different sources is beneficial for a number of downstream decoding tasks. As well, we can transfer the model between regions and sub-types, demonstrating that there is in fact common information in diverse circuits that can be extracted by an appropriately designed model. Interestingly, we found that the model's latent representations showed clear distinctions between different brain regions and cellular sub-types, even though it was never given any information about these distinctions. Altogether, our work demonstrates that training a large-scale neural decoding model on diverse data is possible, and this provides a means of studying the differences and similarities between heterogeneous neural circuits.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper explores large-scale, multi-task neural decoding across different cell types and brain regions. It introduces a multi-task transformer model, named POYO+, trained on data from the Allen Institute’s Brain Observatory dataset. The paper aims to determine whether transfer learning and multi-task decoding are feasible in the paper of neural heterogeneity, where each cell type and brain region exhibits distinct response dynamics.

### Strengths
* Calcium Data: From what I can tell, neural decoding with calcium data is rare. Scaling calcium data could have benefits.
* Interpretability: The paper includes several interpretability analyses to show learned features in the latent representation space. This is useful for neural decoding, which should be more than just performance driven but also have scientific value. 
* Transfer: The authors demonstrate that Poyo+ could be applied to other datasets as well, although I would have liked to see a dataset with different regions instead.

### Weaknesses
 * Distinct Regions: I found the region coverage in the paper to be rather weak, only focusing on mice visual cortex. Although multiple sub-regions are considered as well, other papers use multi-region to mean coverage of the whole brain such as [1] or [2]. If the claim of novelty comes from handling diverse brain regions, then I would expect a dataset that spans multiple, functionally distinct areas of the brain. Could the authors explain why they only used the visual cortex? Is it because calcium data is difficult to collect across wider regions? If so, could the authors discuss the application of their findings to a broader set of regions? Also I’m not sure I quite buy the huge distinctions covered in Appendix A -- neural recording datasets can incorporate much larger amounts of spatial coverage. 
* Experimental Limitations
    * More broadly, only using one dataset is a bit weak to clearly establish benefits from scaling. I would appreciate it if an additional more substantial experiment was studied on the OpenScope dataset or something manageable with new regions. 
    * Moreover, I found figure 3 to show that Poyo+ and Poyo were rather comparable despite needing to train 12 variants of Poyo. Could the authors discuss these findings? 

Overall, the paper is well written but I’m not entirely convinced of the claims. I think more discussion can go into the findings. I would raise my scores after seeing a deeper description of using distinct regions and some more focus on added experiments/limitations.

### Questions
* I’m really surprised that CEBRA does worse than an MLP in Figure 3B. Why would this happen?
* Neuron Dropout: The paper uses a neuron dropout to remove some neurons during training. Is this normal? I couldn’t tell from CEBRA overall.

### Soundness
3

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
3

### Summary
The paper introduces a novel tokenization method and multimodal neural decoder to decode behavioral and stimulus information from calcium responses recorded from multiple regions of the mouse visual cortex. The proposed model achieved state-of-the-art decoding performance in the Allen Brain Dataset; it outperforms previous models in cross-session, cross-region, and cross-dataset settings. Moreover, the clustering of cell types and brain regions emerges from the latent representation of the model purely from response-task pairs. These results suggest that it is beneficial to train neural decoders on multi-task and multi-session recordings.

### Strengths
- This paper demonstrates training a neural decoder on large-scale multi-session, multi-region, and multi-task recordings can greatly improve model decoding performance across a wide range of scenarios, and is an important step towards a foundation model of neural data, a topic of great interest in NeuroAI.
- The experiments are thorough, covering a wide range of realistic transfer learning scenarios. 
- The analysis of the latent embedding on the trained POYO encoder is very interesting. It shows that the model, purely trained on decoding tasks, without any information on the neurons (location, type, region, etc.), learns cell-specific properties.
- Overall, the paper is clear and well-written.

### Weaknesses
I don’t think the paper has any major weaknesses, however, there are several points I hope the authors can clarify regarding the model setup. Please find them in the Questions section below.


### Questions
- What is the difference between the query tokens and output tokens in Figure 1? My understanding is that the decoder takes latent representation from the POYO encoder and the query tokens. The query tokens inform/query the decoder which task(s) to predict (e.g. running speed, pupil dilation, etc.), and then a task-specific linear layer processes the output tokens to generate the prediction. However, in Figure 1, the color code suggests the output tokens are used as query tokens. Can the authors clarify this point (and perhaps update the caption of Figure 1)?
- Following the previous question, does the model predict in an autoregressive fashion? i.e. predict one time-step at a time. Or does the model input the entire calcium trace and predict the whole segment at once? If it is the latter, is causal attention used so that the model doesn’t have access to future time-steps?
- In Section 3.1 and Figure 3, the authors compare single-session trained baselines vs multi-session trained POYO+ (also POYO and CEBRA). Do the authors have a sense of how data-hungry POYO+ is? For instance, would POYO+ outperform the baseline models in a single-session setting?
- When comparing the models' performance (Figure 3, Table 1, 2, and 3), can the authors report s.e.m. or standard deviation across (one of) trials/sessions/animals so that the readers can have a sense of how much variation is in the performance?
- In Section C.2 Training details, can the authors clarify that “the weight for each task is determined based on the scale of the loss from an initial model”? Does this mean that an untrained (randomly initialized) model is used to make predictions for each task, and then their loss magnitude is used to determine the loss scale?
- A very minor comment: I don’t think “POYO+” was introduced in the main text as the name of the method.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors proposed a study that extends POYO, a method for decoding cell-types and brain regions according to neural recordings, to multi-session data and multiple tasks. The authors proposed a multi-task decoder and a training strategy that used multi-session data. They also demonstrated the merits of multi-session and multi-task training through extensive experiments and comparisons.

### Strengths
The idea of multi-session and multi-task decoding of cell-types and brain regions is not entirely new, however, the authors proposed several key components to realize such an idea. The study was clearly presented and the validations are extensive.

### Weaknesses
Some details can be further elaborated. Specifically, the architecture of the multi-task decoder can be presented with more details, e.g., the numbers of self-attention blocks and attention heads. The description of the multi-task decoder lacks sufficient detail to understand its unique design choices compared to standard multi-task transformer decoders. The explanation of loss weighting is vague, and the method for determining the weights is not clearly defined. The performance comparison with CEBRA is limited to only one task, and it is unclear how the proposed model performs on other tasks. There is a discrepancy between the number of single-task variants of POYO mentioned (12) and the number of cases reported in Fig. 3C (9), with no explanation for the missing cases. The claim about the model trained on inhibitory Cre-lines performing surprisingly well on the drifting gratings task is not supported by results on other tasks, making it difficult to assess the generality of this finding. The manuscript uses both POYOplus and POYO+, which should be made consistent. There are also minor typos, such as “one for each mouse, imaging depth, and visual area. from various depths...”. Finally, the relatively low decoding accuracies raise concerns about the practical utility of the model for neuroscience research.

### Questions
1. It is better to provide a figure to illustrate the multi-task decoder, maybe in Appendix . 
2. How is the multi-task decoder proposed in this study different from a general multi-task transformer decoder? What are the unique designs in this multi-task decoder and how are those designs related to the unique characteristics of the decoding tasks?
3. “The losses are summed and weighted...”, how to determine the weight? Is it inverse proportional to the number of predictions?
4. The proposed model outperforms CEBRA in natural the movie frame decoding task, how about other tasks?
5. There are 12 single-task variants of POYO, but it seems that Fig. 3C reports 9 cases. Why are the results for the other three cases missing?
6. “ we find that the model trained on inhibitory Cre-lines does surprisingly well on the drifting gratings task.” How about other tasks?

Minor issues:
Both POYOplus and POYO+ were used in the manuscript (e.g., Fig.3). Please try to make it consistent. 
Typos: “one for each mouse, imaging depth, and visual area. from various depths...”
How such relatively low decoding accuracies can support neuroscience research?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study investigates the impact of data scale on the performance of brain decoding models, developing a multi-task transformer architecture trained on the brain observation dataset from the Allen Institute for Brain Science. This dataset includes response data from over 100,000 neurons across six brain regions in mice, demonstrating the effects of different stimuli on neuronal activity. The research finds that transfer learning across brain regions and cell subtypes is effective, and that integrating data from heterogeneous datasets can enhance decoding performance. Despite the heterogeneity of neural circuits, the model's latent representations can automatically distinguish between different brain regions and cell subtypes, indicating that the shared computational principles among them can be extracted. The main contributions of the research include: 1) the introduction of a novel multi-task decoder capable of flexibly handling various decoding tasks; 2) validation of successful transfer learning across brain regions and cell types; 3) provision of evidence that increasing the diversity of brain regions can improve decoding performance; and 4) demonstration of meaningful structures in the model's latent representations that reflect biological differences. Overall, this work offers new insights into the similarities and differences among heterogeneous neural circuits and lays the groundwork for training large-scale neural decoding models.

### Strengths
This paper presents a novel multi-task transformer architecture for decoding neural activity from a large dataset comprising over 100,000 neurons across six different brain regions.  The originality lies not only in the innovative architecture itself but also in the approach of leveraging transfer learning across heterogeneous datasets.  By demonstrating that insights gained from one brain region can enhance decoding performance in another, the authors push the boundaries of existing methodologies in neural decoding. The quality of the research is commendable, with a robust experimental setup that includes training on extensive neural response data.  The authors employ rigorous validation techniques and comprehensive analyses, providing a solid foundation for their claims.  The results are quantitatively backed by clear metrics that illustrate the performance improvements achieved through their proposed model, showcasing its practical applicability. Generally, this findings not only contribute to our understanding of neural dynamics but also propose a framework that can be utilized in various applications, ranging from neuroprosthetics to brain-computer interfaces.

### Weaknesses
While the authors provide a comprehensive analysis of their proposed multi-task transformer architecture, the experimental validation could be further strengthened.   Specifically, the comparison against state-of-the-art methods in the field is somewhat limited.   For a more robust assessment of the proposed model's efficacy, additional benchmarks should be included, such as comparisons with other established neural decoding frameworks.   This would provide clearer context for the reported performance improvements and demonstrate the advantages of the proposed approach more convincingly.  Meanwhile, this study relies heavily on a large dataset from six brain regions;   however, the diversity of this dataset may not sufficiently represent the variability found across different species or experimental conditions.   To enhance the generalizability of the model, the authors could consider including additional datasets that encompass various neural activity patterns from other organisms or contexts.   This would help validate the transfer learning claims and ensure that the model performs well across a broader spectrum of neural encoding scenarios.
Furthermore, the discussion of limitations is relatively sparse.   A more thorough acknowledgment of potential shortcomings, such as the influence of noise in the data or the computational demands of the proposed model, would provide a more balanced perspective.   Including these considerations would demonstrate the authors' awareness of the challenges and offer avenues for future research to address these limitations effectively.

### Questions
The authors mention a data-driven feature selection process.  Could they elaborate on the specific criteria and methods used for selecting features from the neural data?  

The evaluation metrics presented in the paper primarily focus on accuracy and predictive performance.  Can the authors justify their choice of metrics, particularly in relation to the biological significance of the results?  Are there any additional metrics that could provide a more comprehensive assessment of the model's effectiveness, particularly in understanding the underlying neural mechanisms?

With the model's complexity and the relatively limited size of the dataset (six brain regions), what steps have the authors taken to mitigate the risk of overfitting?

### Soundness
2

### Presentation
3

### Contribution
2
