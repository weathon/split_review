# Population Transformer: Learning Population-level Representations of Neural Activity

- Decision: Accept
- Scores: 8, 8, 8, 5, 8, 8

## Abstract
We present a self-supervised framework that learns population-level codes for arbitrary ensembles of neural recordings at scal. We address two key challenges in scaling models with neural time-series data: sparse and variable electrode distribution across subjects and datasets. The Population Transformer (PopT) stacks on top of pretrained representations and enhances downstream decoding by enabling learned aggregation of multiple spatially-sparse data channels. The pretrained PopT lowers the amount of data required for downstream decoding experiments, while increasing accuracy, even on held-out subjects and tasks. Compared to end-to-end methods, this approach is computationally lightweight and more interpretable, while still retaining competitive performance. We further show how our framework is generalizable to multiple time-series embeddings and neural data modalities. Beyond decoding, we interpret the pretrained PopT and fine-tuned models to show how they can be used to extract neuroscience insights from massive amounts of data. We release our code as well as a pretrained PopT to enable off-the-shelf improvements in multi-channel intracranial data decoding and interpretability.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The manuscript introduces the Population Transformer (PopT). This self-supervised framework tackles two key challenges in neural time-series analysis: sparse electrode distribution and variable electrode placement across subjects and datasets. PopT uses a transformer architecture that combines temporal embeddings with spatial information and trains through self-supervised learning to aggregate signals across variable electrode layouts. The model outperforms baselines on neural decoding tasks, requires less training data, generalizes to new subjects, and reveals interpretable brain connectivity patterns.

### Strengths
- Validation across two types of neural recordings: EEG and intracranial EEG (iEEG)
- Thorough comparison against common aggregation methods and state-of-the-art models
- Strong ablations to test the importance of ensemble-wise loss, channel-wise loss, position encoding, and reconstruction loss

### Weaknesses
 - In Tables 1, 2, and 3, consider adding statistical testing (e.g., Wilcoxon) between the best model and others. Then, correct p-values for multiple comparisons (e.g., Holm). Otherwise "We see significant improvements in performance" is not justified.
- I am confused about construction for " (1) ensemble-wise —the model determines if activities from two channel ensembles occurred consecutively, requiring an effective brain state representation at the ensemble-level". How do we know if activities from two channels occurred consecutively? In other words, could you explain how you construct pairs? How do you get the states?

### Questions
- Figure 1 has a short-time Fourier transform, but I did not find it to be discussed anywhere in the text.
- It would be great to see how much Gaussian fuzzing contributes to the final performance. EEG is spatially very smoothed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors introduce a self-supervised learning framework called PopT to learn embeddings for EEG and iEEG recordings for the improving downstream decoding analysis. In general, the problem is hard because of the spatially varying channel placements in different experiments. Their method leverages unannotated data to optimize channel-level and ensemble-level objectives, which helps them build generic representations and also allows to capture some dynamical relationships. Their tests show improved decoding on held-out subjects. Based on the interpretation of the weights, they propose a new method for brain region connectivity analysis and for identifying candidate brain regions.

### Strengths
- They tackle an important and difficult problem for the field

- Interesting approach backed with strong empirical results.

- I appreciate the work authors put in doing new analyses and interpreting the weights. 

-Well written and interesting.

### Weaknesses
I have some questions about their connectivity analyses below

### Questions
In Fig. 8, how does the connectivity shown compare with cross-correlation or some other metrics that are used in the field?

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
3

### Summary
The authors introduce Population Transformer (PopT), a transformer-based and contrastive learning approach for decoding neural time series data. The PopT aggregates and decodes channel-wise temporal encodings of neural time series data from, e.g., a pretrained BrainBert but is agnostic to the encoder. The authors introduce two contrastive loss terms for training the PopT. One contrastive loss term requires the PopT to learn temporal representations for each channel, and the other contrastive loss term requires the PopT to learn spatial representations across channels. The PopT receives electrode placement as input, allowing it to decode neural activity across varying electrode placements (e.g., from several subjects). In an application with EEG and iEEG, the paper presents that the PopT converges with fewer samples than other shown methods, achieves superior decoding performance compared to other shown methods, and provides evidence for the PopT's ability to generalize across subjects. The authors also suggest measuring and interpreting functional connectivity based on the ablation of individual channel input to their PopT and performance degradation for all other channels. They also suggest interpreting the weights of the model to map the task-associated function to specific electrodes.

### Strengths
The claimed contributions of the PopT would present an exciting leap forward in decoding neural time series data. This is because unreliable and slow decoding of neural activity limits applications and scientific insights from models. A method that requires comparably few data, no labeled data, and learns representations that generalize across subjects regardless of electrode layout makes decoding more fast and reliable for new subjects and unlocks new applications. The ability of the PopT to generalize across subjects is a major strength of the approach. Another strength is that the PopT relies on pre-trained encoding models that it is agnostic to. The formulations of the contrastive learning objectives seem original. The suggested ways to interpret the model to understand the data are interesting.

### Weaknesses
The paper presents multiple weaknesses that could be addressed to improve its clarity and reliability.

First, the abstract describes PopT's benefits, such as "computationally lightweight" and "more interpretable," which lacks precision without clear comparison groups or quantitative metrics. For example, calling PopT computationally lightweight in comparison to end-to-end trained models is misleading since it relies on pre-trained, e.g., BrainBert weights, which already bear significant computational demands. As another example, the interpretability analysis does not include any comparison method.

In addition, the generalizability claims lack thorough validation: the hold-one-out subject analysis does not sufficiently establish robustness. This experiment could benefit from a broader validation, e.g., cross-validation approaches. 

Additionally, when comparing the performances to other models the analysis does not account for the differences in free parameters and nonlinearities across models.

Last, the codebase requires significant improvements, as it is messy, poorly documented, and lacks proper instructions or tutorials. For example, the readme is incorrectly titled BrainBert 2.0. This contrasts the authors claim of it being "plug-and-play."

I am not up-to-date and fully familiar with related work. This is why my expertise might be insufficient to fully weigh the significance of the central contribution against the current limitations of the paper in the clarity and reliability of the results.

I am generally excited about the direction of the work and happy to give a higher evaluation once the presentation of the current version of the paper is significantly improved and the detailed questions below are addressed.

### Questions
# **Major Questions**

1. You show that the decoding performance increases with more subjects and decreases with holding out a subject. However, these experiments are limited because they consider a validation on specific channels of one specific subject, or holding out one specific subject. Is this also valid across arbitrary channels and arbitrary subjects?  
2. Figure 4: Do the baseline aggregation approaches have fewer free parameters and nonlinearities than the PopT? Could you report the number of free parameters and nonlinearities of all networks and factor this into the discussion of your results?  
3. Results 366-370: The model's ability to generalize is a central claim. However, the hold-one-out analysis seems somewhat limited. What if the held-out subject was a lucky draw? Can this comparison be done in a crossvalidation? Can the performance decrease be computed for hold-k-out and presented as a function of k? Separately, is there a different model class that can generalize to provide a comparison group in this test?  
4. 371-377 and Figure 6 and 7: I would have expected that "All subjects" and "0 subjects" correspond to "All" and "Non-pre-trained PopT" but the numbers are different. Can I rely on this data? Why is there a mismatch?  
5. Figure 7: What if "across channel ensembles 5-30 on a held out test subject" is a lucky draw? Could this be more robustly supported with an extended analysis?  
6. 414-416: To say this, I would expect an analysis of representations resulting from different loss functions. Can one show that the contrastive learning objective results in the clearest association/separation of inputs?  
7. 468-470: One obtains N-squared performances, where N is the number of channels. Can one present the raw functional connectivity matrices inferred this way in addition to the aggregate? This could help to gauge how effective the approach is.  
8. 468-470: Can one compare the results to the functional connectivity inferred with traditional cross-correlation methods on the measurements? This would help to illustrate the true utility of the PopT-based analysis.  
9. 475-485: Same here. Can one compare to neuroscience ways to characterize the activated brain area, e.g., z-score based?  
10. Results 296-297: What are differences in, e.g., architecture or training that makes LaBraM outperform the PopT? Could one provide possible explanations for why LaBraM outperforms the PopT on EEG decoding (whereas end-to-end approaches specifically designed for iEEG do not)?  
11. Figure 4: there is a much more significant improvement for the sentence onset and speech vs. non-speech tasks over the improvement in the pitch and volume tasks. Could one provide an explanation for this in the results section?  
12. In contrast to one of the central claims in the abstract, 23-24, the codebase is messy, and lacks documentation, clear examples, instructions, and tutorials. The readme title is BrainBert 2.0. Could the codebase please be significantly cleaned and documented?

# **Clarifications and Minor Questions**

13. Abstract 16-18: The sentence "lowers the amount of data for downstream decoding experiments" is compatible with the presented results (Fig. 4 and 5). However, the verb 'lowers' requires a comparison group, and 'downstream decoding experiments' is vague. The meaning of 'downstream' is also ambiguous. Could you please rephrase this?  
14. Abstract 18-20: Calling the PopT computationally lightweight in comparison to end-to-end approaches is misleading because the PopT only works with pretrained weights from BrainBert. Could you please rephrase this?  
15. Abstract 18-20: Calling the PopT "more interpretable" when not comparing the interpretations to existing traditional neuroscientific methods for interpretability is misleading. Could you please rephrase this?  
16. Abstract 18-20: What does 'retaining competitive performance' mean? In all iEEG data, it outperforms the end-to-end method used, in all EEG data it is outperformed by LaBraM. Could you please provide this information without ambiguity?  
17. Abstract 21-23: What are "massive" amounts of data according to the authors?  
18. Discussion 524-525: "\[ … \] could provide an even higher resolution latent space \[ … \]". Higher than what? Could you please rephrase this?  
19. Conclusion 538-539: I wouldn't know how to use it "for plug-and-play pretraining". The codebase is messy and lacks clear examples, instructions, or tutorials. Is this a work in progress or the cleaned-up codebase? 
20. 206-208: The explanation is not reader-friendly and not comprehensible for someone who does not know the types of neurorecordings. Could you please explain to the reader why intracranial and scalp electroencepholography lead to two different types of time-series data, and why and which resolution extremes these represent?  
21. 3 Population Transformer Approach 178-179: these are rather "contrastive" components and not "discriminative" components. Could one please adopt "contrastive" instead of discriminative throughout the text?  
22. Figure 2, 6, 7: Could one use violin (or box) plots instead of bar plots to convey the variability and scatter the individual data points on top to convey the sample size?  
23. 375: "potentially due to adaption to the temporal embeddings used" meaning unclear. Could you please rephrase this?  
24. 363-365: These sentences seem contradictory, which might be easily resolved with rephrasing them. Could you please rephrase this? Part of the Figure 5 caption could go here into the main text.  
25. Results Figure 4: What is 'highly' sample efficient?

# **Minor Formatting**

26. 214-215: Could you please remove the parenthesis inside the parenthesis?  
27. Table 1: Could you please emphasize your result better by bolding the label Pretrained PopT or star it for "best overall"?  
28. Results 264-269: hard to read. Could you please remove the parenthesis inside the parenthesis?  
29. Figure 3 is referred to before Figure 2 in the text. Could you please renumber the figures to maintain clarity?  
30. Table 1 and Figure 1: Could you please make latex keep them inside the section where they are referred to?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces a self-supervised framework, the Population Transformer (PopT), designed to learn population-level representations for large neural recording datasets.  PopT addresses challenges related to sparse and variable electrode distribution across subjects and datasets by using pretrained embeddings. By using a modular approach the model is more flexible and lightweight. The authors claim that the approach is computationally efficient, interpretable, and performs competitively against end-to-end methods.

### Strengths
This paper demonstrates strong rigor by evaluating the proposed method across two types of neural time-series data (iEEG and EEG), enhancing the generalizability and robustness of its findings. The authors plan to share both the data and code upon acceptance, promoting transparency and reproducibility within the community. Additionally, they test their method using hold-out subject tests to validate the model’s performance on unseen data, which is essential for assessing real-world applicability. The method’s effectiveness is benchmarked against a diverse set of models, providing a comprehensive view of its performance relative to other approaches. Furthermore, ablation studies are conducted to examine the contribution of different components in the proposed framework, offering valuable insights into how each part enhances overall model performance.

### Weaknesses
The study offers a comprehensive evaluation of PopT, and assess it using various experiments. However, the paper would benefit from clearer organization and writing, particularly in emphasizing the significance of each experiment.

- **Introduction and Field Context**: Despite the extensive experimentation, the paper lacks a clear introduction to the field and a focused statement of its goals. Important background information and foundational definitions are often buried in the appendix rather than integrated into the main text.
    - For instance, a key innovation of the study is the use of channel-level and ensemble objectives. Providing a more detailed literature review on current approaches to these objectives would help the reader understand the limitations of existing methods and the advantages of the proposed improvements. This contextualization would make the study’s contributions clearer and more impactful. Specifically, the paper should discuss how existing methods handle variable electrode layouts across subjects, and how PopT's approach differs. The paper should also clarify the specific challenges associated with learning population-level representations from sparse and variable electrode distributions, which are not adequately addressed in the current introduction.
    - The connection between experiments is also unclear, with critical information about the pretrained PopT model only appearing in the appendix. Providing a clear description of the data used for pretraining within the main text would help readers understand the study’s foundation and goals more effectively. For example, the paper should specify the size and characteristics of the pretraining dataset, and how it relates to the datasets used for evaluation. The lack of this information makes it difficult to assess the generalizability of the pretrained model.
    - Similarly, Table 3 introduces PopT with an L1 reconstruction loss as an additional experiment. However, this experiment is not discussed in the text, and it appears tangential to the core contributions of the study. Omitting such details could allow space to expand on more relevant analyses. The paper should clarify why an L1 reconstruction loss is used, and what specific insights it provides in the context of the proposed method. Without this discussion, the experiment seems arbitrary and detracts from the main focus.
- **Benchmarking Choices**: While Chronos/TS2Vec and BrainBERT/TOTEM are used as benchmarks for PopT, it remains unclear why these specific models were selected. The authors could strengthen the study by discussing the criteria for choosing these benchmarks. For example, the paper should explain why these models are representative of the current state-of-the-art in neural time-series analysis, and how their architectures and training procedures compare to PopT. A more detailed discussion of the strengths and weaknesses of each benchmark would help readers understand the relative performance of PopT.
- **Minor Presentation Issue**: In Figure 8, the plot slightly overlaps with the title on the left image.

### Questions
1. Table 3 refers to “PoPT w/o group-wise loss”, is the group-wise loss the same of ensemble-wise loss. To improve clarity, could the authors consider using consistent terminology throughout?
2. It would be insightful to see how one of the baseline models, specifically BrainBERT from Table 1, performs on the hold-out dataset, similar to the performance reported for PoPT in Figure 6. This comparison would provide additional context for the robustness of PoPT relative to other methods. Could the authors report the performance of BrainBERT on the hold-out dataset in a format similar to Figure 6?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The Population Transformer (PopT) is a self-supervised framework designed to learn brain-wide neural activity representations. The approach aims to address common challenges faced by invasive iEEG and non-invasive EEG neural recordings, namely 1) sparsity of recording channels within the brain and 2) variability in channel positioning and reliability. The authors propose a smart data embedding and combining two loss functions that allow pre-training of the network using data from multiple datasets and individuals. Pre-training is shown to be fundamental to lowering the amount of data necessary for fine-tuning neuroscientific tasks, such as decoding experiments. Finally, the authors show experiments and analyses to support the claim that this framework is interpretable and generalizable.

### Strengths
This paper has many merits. The idea and approach, from a computational neuroscience perspective, are novel and very interesting. The proposed framework could benefit the neuroscience community at large: combining data from multiple datasets, and learning brain-wide representations that are not idiosyncratic to a specific individual are key to advancing neuroscience research. Many points made throughout the paper and several experiments are convincing and valuable, and I don’t think much work is required in terms of experiments/compute.

### Weaknesses
On the flip side, the paper is, at some points, lacking in precision and clarity, at some points a bit colloquial, and at other points, unnecessary jargon. I think that the paper would be stronger, and more accessible, if the authors put some effort into clarifying and streamlining it. Moreover, the claims of interpretability are currently unclear and potentially overstated.

**Clarity**:  the paper is not really neat. Moreover, there is some sloppiness in the mathematical notation and technical explanation of the method. Finally, the figures are uneven and quite messy. Follows a list of detailed complaints:
- general lack of dimensionality: in many points, it is not clear what the dimensions are of the variables. for example, lines 160-161, what is the dimension of $X_B^t$? Is the “+” used for concatenation or for an actual sum? What is the output dimensionality of the temporal embedding model $B$? Some of these are in Appendix A, but it would be useful to streamline and clarify. The lack of clarity around the dimensions of $X_B^t$ is particularly problematic as it is the core input to the transformer model. The paper should explicitly state if $X_B^t$ is a matrix or a tensor, and what each dimension represents (e.g., channels, time points, embedding dimension). Furthermore, the operation used to combine temporal embeddings and positional encodings, whether it is element-wise addition or concatenation, needs to be explicitly stated in the main text, not just in the figure caption. The output dimensionality of the temporal embedding model $B$ is also crucial for understanding the subsequent processing steps and should be clearly defined.
- $[CLS]$ token: it is stated nowhere that this is the token used for downstream decoding/classification tasks, and what space it belongs to. Is it only binary? Please clarify in the text or figure legend. The paper needs to clarify the nature of the $[CLS]$ token, specifically whether it is a learned embedding or a fixed vector. Furthermore, the dimensionality of this token needs to be specified, and it should be explicitly stated how this token is used in downstream tasks. For instance, is it directly fed into a classifier, or are additional layers applied? The term 'decoding' is used without a formal definition, which makes it difficult to understand the exact nature of the downstream tasks.
- Self-supervised Loss (line 173-197): the losses are described in words, but it would be useful and much clearer to write them in formulas. Right now, this paragraph is a bit messy and somewhat colloquial. The description of the self-supervised loss is indeed vague and hard to follow. The paper should include the mathematical formulas for the loss functions, clearly defining each term and its role. For example, the masking procedure should be formalized, and the specific form of the reconstruction loss should be provided. The current description relies too much on intuition and lacks the necessary mathematical rigor.
- Fine-tuning (line 199-201): colloquial and relies on details only available in the appendix. It would also be useful to formally define what is meant by a decoding task. The description of fine-tuning is too high-level and lacks the necessary technical details. The paper should clearly specify the architecture of the fine-tuning model, including the number of layers, the activation functions, and the optimization algorithm used. Furthermore, the term 'decoding task' needs to be formally defined, including the nature of the input, the output, and the evaluation metric used. The reliance on the appendix for these details makes the main text difficult to understand.
- Figures: Fig 1 is unclear and messy. Why does it go from bottom to top, rather than the opposite? Currently, the “Population Transformer inputs” title of Fig 1a is just above the output, making it very confusing. Moreover, the figure has at least four different font sizes. The “+” used in temporal embedding + 3D position is confusing; does it refer to concatenation or addition. The title of the colorbar near the STTF is nearly illegible. Panels b and c could provide clearer information on the loss. Fig 3-4: font sizes widely different across figures; Fig 3 text is hard to read on print. Same for Figs 6-7-8. Fig 8 left title is partially covered by the plot.

**Interpretability**: the claim of interpretability requires some work to be convincing/useful. For example, the connectivity analyses are far from clear (also after reading the Appendix!). It is not immediately clear how one infers (pairwise) connectivity by masking out the activity of one channel at the time and measuring the degradation in channel-wise loss. Can you add a few details on that? And do we learn anything new from this analysis as compared to previous coherence or cross-correlations analyses? Can we have a few more qualitative and/or quantitative comparisons? Same questions go for the functional brain regions from attention weights. Moreover, what are the possible caveats of inferring connectivity or functional regions from PopT?

**Minor comments**:
- line 153: *adapt* -> adopt?
- lines 132, 158, …: BrainBERT was used but never cited.
- line 163: *sinusoidal position encoding*: is there a simple formula or a couple of words to explain this method without necessarily having to read the cited paper?
- line 171: and $\tilde y_i$ *and(?)* respectively, …
- line 188: …is *again(?)* the binary cross-entropy…
- line 374, 478, 483: Figure X -> (Figure X)

**Additional questions**:
*[These questions popped up while first reading the paper; some got clearer on a second read, some not. I don’t think it’s necessary for the authors to answer all these questions, but hopefully, they’ll be useful for improving discussion and intro, or future experiments, or mybe just food for thoughts.]*

The paper claims to learn representations of neural activity; do the authors mean the final output of the PopT or only the CLS output? Can one also learn a neural representation without using a CLS token? Can this representation be thought of and used as a dimensionality reduction method? Who are the intended users of this method? Can this method be used for non-human invasive research, such as calcium imaging, neuropixels, etc? Is it possible that the discriminative nature of the pre-training objective leads to potentially misleading representations in case of noisy/faulty channels?

### Questions
**Clarity**:  the paper is not really neat. Moreover, there is some sloppiness in the mathematical notation and technical explanation of the method. Finally, the figures are uneven and quite messy. Follows a list of detailed complaints:
- general lack of dimensionality: in many points, it is not clear what the dimensions are of the variables. for example, lines 160-161, what is the dimension of $X_B^t$? Is the “+” used for concatenation or for an actual sum? What is the output dimensionality of the temporal embedding model $B$? Some of these are in Appendix A, but it would be useful to streamline and clarify.
- $[CLS]$ token: it is stated nowhere that this is the token used for downstream decoding/classification tasks, and what space it belongs to. Is it only binary? Please clarify in the text or figure legend.
- Self-supervised Loss (line 173-197): the losses are described in words, but it would be useful and much clearer to write them in formulas. Right now, this paragraph is a bit messy and somewhat colloquial.
- Fine-tuning (line 199-201): colloquial and relies on details only available in the appendix. It would also be useful to formally define what is meant by a decoding task.
- Figures: Fig 1 is unclear and messy. Why does it go from bottom to top, rather than the opposite? Currently, the “Population Transformer inputs” title of Fig 1a is just above the output, making it very confusing. Moreover, the figure has at least four different font sizes. The “+” used in temporal embedding + 3D position is confusing; does it refer to concatenation or addition. The title of the colorbar near the STTF is nearly illegible. Panels b and c could provide clearer information on the loss. Fig 3-4: font sizes widely different across figures; Fig 3 text is hard to read on print. Same for Figs 6-7-8. Fig 8 left title is partially covered by the plot.

**Interpretability**: the claim of interpretability requires some work to be convincing/useful. For example, the connectivity analyses are far from clear (also after reading the Appendix!). It is not immediately clear how one infers (pairwise) connectivity by masking out the activity of one channel at the time and measuring the degradation in channel-wise loss. Can you add a few details on that? And do we learn anything new from this analysis as compared to previous coherence or cross-correlations analyses? Can we have a few more qualitative and/or quantitative comparisons? Same questions go for the functional brain regions from attention weights. Moreover, what are the possible caveats of inferring connectivity or functional regions from PopT?

**Minor comments**:
- line 153: *adapt* -> adopt?
- lines 132, 158, …: BrainBERT was used but never cited.
- line 163: *sinusoidal position encoding*: is there a simple formula or a couple of words to explain this method without necessarily having to read the cited paper?
- line 171: and $\tilde y_i$ *and(?)* respectively, …
- line 188: …is *again(?)* the binary cross-entropy…
- line 374, 478, 483: Figure X -> (Figure X)

**Additional questions**:
*[These questions popped up while first reading the paper; some got clearer on a second read, some not. I don’t think it’s necessary for the authors to answer all these questions, but hopefully, they’ll be useful for improving discussion and intro, or future experiments, or mybe just food for thoughts.]*

The paper claims to learn representations of neural activity; do the authors mean the final output of the PopT or only the CLS output? Can one also learn a neural representation without using a CLS token? Can this representation be thought of and used as a dimensionality reduction method? Who are the intended users of this method? Can this method be used for non-human invasive research, such as calcium imaging, neuropixels, etc? Is it possible that the discriminative nature of the pre-training objective leads to potentially misleading representations in case of noisy/faulty channels?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
In this paper, the authors propose a self-supervised learning framework for neural time series data. The model is trained using ensemble and channel-wise discrimination strategies to address the problem of sparse and variable electrode distribution across subjects and datasets. The authors presented the validity of the proposed method on two datasets with diverse analyses.

### Strengths
In this paper, the author tried to solve the problem of sparse and variable electrode distribution across subjects and neural time series data datasets by modeling with a single-channel embedding method.

The effectiveness of the proposed method was supported through various experiments and analyses.

It achieved high performance with fewer computational resources compared to existing pre-trained models.

### Weaknesses
It is unclear how exactly the position of each channel is defined in spatial position encoding. The reference provides coarse positions only, which is important information in spatial relation learning.
Page 4, line 166: The notations used in position embedding are not defined.

Supporting materials must be presented for the Gaussian fuzzing in channel embedding to ensure its effectiveness in avoiding overfitting.

The experiments are somehow limited. More rigorous and thorough experiments should be conducted over diverse datasets. Other more challenging tasks, e.g., TUEV in the TUH EEG corpus, should be conducted and compared with the comparative methods.

The results in the ablation study (Table 3) suggest that position encoding played a significant role in performance improvements, while other proposed loss functions had marginal effects. In this regard, the related contexts should be provided in detail.

Regarding the connectivity construction in Section 6, it is not straightforward to understand how the connectivity is measured. More detailed explanations and rationales should be provided regarding why the proposed method can estimate channel connectivity.

### Questions
Page 3, line 161: According to the paper's description, the input to the temporal encoding is a single value of a channel at a time t. Is this correct?

### Soundness
3

### Presentation
2

### Contribution
3
