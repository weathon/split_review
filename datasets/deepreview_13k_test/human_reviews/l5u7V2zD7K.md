# Temporal Spiking Generative Adversarial Networks for Heading Direction Decoding

- Decision: Reject
- Scores: 5, 1, 8, 5

## Abstract
The spike-based neuronal responses of the ventral intraparietal area (VIP) for different heading directions appear highly spatial and temporal dynamics in the posterior parietal cortex. The data amount of biological population level VIP neuronal response is usually relatively small due to the practical data collection difficulty, which impedes the application of the complex decoding model and even causes model overfitting. To overcome the above problem, we attempt to build the unified spike-based decoding framework with a spiking neural network (SNN) for the generative and decoding model since the SNN is biologically plausible and quite suitable for neural decoding. In this paper, we propose the temporal spiking generative adversarial networks (T-SGAN) based on a spiking transformer to generate synthetic time-series data of the neuronal response of VIP neurons, followed by the recurrent SNNs with an attention mechanism to capture the spatial and temporal dynamics and decoding the heading direction. The temporal segmentation is designed in T-SGAN to reduce the length of temporal dimension and spatial self-attention is adopted to extract associated information among VIP neurons. The experiments are conducted on the collected biological datasets from monkeys to evaluate the decoding performance of the proposed framework. Experiments show that the proposed T-SGAN successfully generates realistic synthetic data and promote decoding accuracy of recurrent SNNs up to 1.75%. The above SNN-based decoding framework could further exploit the low power consumption advantages and benefit the neuronal response decoding application.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The work proposes methods for augmentation of spike recordings and decoding them into heading directions for VIP brain area. In particular, the paper employs a spike transformer for generation of synthetic data of neuronal spiking time-series of VIP neurons. The synthetic data along with real data is then processed by spiking recurrent neural network (SNN) to decode the responses into  heading directions. The decoding with the proposed approach is compared against decoding without the approach on two proprietry datasets of recordings from monkeys VIP.

### Strengths
1. The approach proposes a decoding pipeline for VIP neural recordings based on spiking time-series and spiking neural networks without transformation to and from firing rates.

2. The proposed approach appears to enhance the eventual decoding accuracy.

3. The approach proposes temporal dimension segmentation through self-attention as a component of Spikeformer to deal with long sparse time-series of spikes.

### Weaknesses
1. Contribution of the augmentation (synthetical generation) vs. SNN decoding to increase in accuracy is unclear.

2. Related to previous point, the presented augmentation approach in principle appears to be plausible for other neural recordings, i.e. other brain areas and tasks. However, the presented work does not consider generalization and is too specialized towards VIP and decoding heading direction. 

3. Data visualization shows differences in synthetically generated spike trains data vs. real data. Also t-SNE embedding shows very different embedded points. These differences are not explained. On the contrary, spike trains are claimed to be similar. 

4. There is no full description of experimental setup of data acquisition, how data was preprocessed, validated and whether this will part of this work.

5. While it is possible to understand the content, the manuscript is not well-written and includes grammatically incorrect sentences and typos.

### Questions
Would appreciate authors answers to W1-W5 listed above. In particular:

Re. W1 &W2, how one would discern the contribution of the augmentation vs. the special decoder?
Does the approach have independent merit as an augmentation method? 
If real data would replace synthetic data would accuracy increase be similar?

Re. W3, it is unclear why the authors claim that the generated spike trains are similar to real spike trains. How do authors assess similarity.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a spiking neural network (SNN) approach to decode heading direction from neural activity in parietal cortex of monkeys. In addition, it proposes a GAN-based data augmentation strategy. The authors fit their model on two datasets of 90 and 210 neurons from area VIP in monkey parietal cortex and show that it outperforms two alternative (SNN-based?) baselines.

Unfortunately the paper is written so poorly that I found it impossible to figure out what exactly is happening and why. I think this paper needs a full rewrite and resubmission at a future venue.

### Strengths
I have a hard time listing any, since I simply did not understand the paper.

### Weaknesses
1. Extremely poor writing; paper is basically impossible to follow
 1. Motivation for SNN-based approach unclear
 1. Motivation for GAN-based data augmentation unclear
 1. Simple baselines (e.g. linear model) missing

### Questions
While I think I understood the overall objective (decode heading direction), I had a really hard time figuring out why they take the SNN as opposed to standard neural networks or even simpler methods such as (generalized) linear decoding. Despite best efforts and multiple reads of abstract, introduction etc. I could not follow the reasoning.

In terms of evaluation, the most straightforward baselines such as a (generalized) linear model are missing. Thus, it is not clear what any of the numbers in the paper mean.

The effect of the GAN is questionable, as the differences reported in Table 1 are small and there are no error bars reported.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a unified spike-based decoding framework for studying the neuronal responses in the ventral intraparietal area (VIP) related to heading directions. Given the limited biological data for VIP neuronal responses, the paper presents a novel approach using spiking neural networks (SNNs) and generative adversarial networks (GANs) to create synthetic neuronal response data. This synthetic data is then employed to improve the decoding of heading directions, with a focus on temporal and spatial dynamics. The proposed temporal spiking generative adversarial networks (T-SGAN) generate realistic synthetic data, enhancing the decoding accuracy of recurrent SNNs. The paper demonstrates that this framework leverages the benefits of biological plausibility and low energy consumption of SNNs in neuronal response decoding.

### Strengths
1. The paper introduces an innovative approach to studying neuronal responses in the VIP, combining spiking neural networks and generative adversarial networks. The use of SNNs for decoding and T-SGAN for data augmentation is a unique and original contribution to the field.
2. The paper presents a well-structured and detailed methodology, making it easy for the reader to understand the proposed framework. The experiments conducted on biological datasets from monkeys provide robust evidence of the framework's effectiveness.
3. This research addresses a critical challenge in neuroscience, offering a new approach for decoding neuronal responses in the VIP. The potential applications of this framework, including its low energy consumption advantages, make it significant in the field.

### Weaknesses
1.  It would be beneficial to discuss the limitations and potential biases associated with using synthetic data for training neural networks. Additionally, addressing the potential discrepancies between synthetic and real data would provide a more comprehensive understanding of the framework's applicability.
2.  The paper mentions that SNNs were trained to decode heading directions using the generated synthetic data. More information about the SNN training would enhance the reproducibility of the research.

### Questions
see weaknesses

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a spiking neural network that reproduces neural data from the VIP cortical area to compensate for the scarcity of this experimental data. In order to design this model, they use a sophisticated network based on spiking transformers, which they then evaluate by computing the decoding performance. They show a modest but significant improvement in performance.

### Strengths
The paper is relatively clear. The results are interesting. My first major comment is that the paper proposes an application to neuroscience using neural networks to improve decoding capabilities. This is a completely original and promising line of research that is not often presented at this conference and should be encouraged.

### Weaknesses
I find that the neuroscience aspect is very lightly touched upon. For example, the authors do not show a selectivity curve for the neurons studied, but only the decoder performance results in the form of tables of numbers. The impact of the paper could be improved if the authors presented in a synthetic way the principle of encoding the direction of the head in the VIP area, as well as the different results as improved by their methods. Finally, one of the interesting results of this paper is to show that different decoding architectures give different performances. This result could shed light on the inherent complexity of the neural representation underlying the distributed representation of head orientation in the population of neurons studied, but I lack this analysis.

### Questions
I think the paper could be improved by addressing the following points:
- " With the sparse spike-form Query, Key, and Value, its computation becomes more efficient.": please justify
- in the model, why use firing rates when you claim that the representation is spiking?
- Figure 1 is too small, "sythetic" > "synthetic"
- Figure 3: the description of the t-SNE analysis is vague and the results seem rather negative, this is hardly discussed in "Visualisation of generated data". Please clarify.

Minor:
- The syntax of the paper did not allow me to fully follow the arguments. I have not taken this into account in my evaluation, but the authors should use a service, even an automatic one, that allows clarification of certain points. 
- The LaTeX formatting of the paper could be improved. In particular, quotations in the text should be enclosed in parentheses, e.g. using ``citep''. Text appearing in equations ("real", "data", ...) should be formatted as text, e.g. using `\text'.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
