# Language Reconstruction with Brain Predictive Coding from fMRI Data

- Decision: Reject
- Scores: 3, 6, 5, 5

## Abstract
Many recent studies have shown that the perception of speech can be decoded from brain signals and subsequently reconstructed as continuous language.
However, there is a lack of neurological basis for how the semantic information embedded within brain signals can be used more effectively to guide language reconstruction.
The theory of predictive coding suggests that human brain naturally engages in continuously predicting future word representations that span multiple timescales.
This implies that the decoding of brain signals could potentially be associated with a predictable future.
To explore the predictive coding theory within the context of language reconstruction, this paper proposes a novel model \textsc{PredFT} for jointly modeling neural decoding and brain prediction.
It consists of a main decoding network for language reconstruction and a side network for predictive coding.
The side network obtains brain predictive coding representation from related brain regions of interest with a multi-head self-attention module. 
This representation is fused into the main decoding network with cross-attention to facilitate the language models' generation process. 
Experiments are conducted on the largest naturalistic language comprehension fMRI dataset Narratives. 
\textsc{PredFT} achieves current state-of-the-art decoding performance with a maximum BLEU-1 score of $27.8\%$.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper describes a decoding method "PredFT" that uses a main decoding network and a side network to perform decoding from fMRI recordings of subjects listening to stories to text. The side network is responsible for obtaining predictive coding representations from specific brain regions and integrating them into the main network, enhancing language decoding. The authors claim that this integration leverages brain regions known for predictive functions (like the parietal-temporal-occipital areas) to better align brain signal decoding with anticipated semantic content. This is supported by results that have claimed the brain performs predictive coding during language stimulation.

### Strengths
The attempt to use hypothesized predictive coding representations to enable better text decoding is interesting.

### Weaknesses
My main concern is that the metric does not seem to produce even locally coherent text, which substantially damages the authors' claims that this method is an advancement over prior work, such as Tang et al., which uses an LM to guarantee local coherence. Consider the following example from the case study: "He don’t know my girl you of the eyes but his girl sleep he and he said and he said and the to the and and which I not wrong. But the Guy". Clearly, this has no meaning, and does not even obey basic local grammatical rules (e.g. "and and"). The problem seems to be that the model has merely learned repeat short, high-frequency words like "the", "he" and "and", which improves BLEU/ROGUE score but does not actually move forward towards the goal of better language decoding. I imagine if you just had the model repeatedly and randomly output words sampled from the top 100 most common English words that it would behave fairly similarly. My expectation is that a small percentage of the improvement in BLEU score is genuinely derived from brain signals, with most of the benefit deriving from this output bias. The unreasonably high 5.62 BLEU-3 score when compared to other methods is more of a red flag, because its pretty clear that the model is simply guessing every high frequency trigram in the English language.

The paper is also quite difficult to read for no reason and pointlessly notational, for example when the self-attention equation is repeated three separate times in only slightly different ways.

### Questions
Please see weaknesses. I would need to be convinced that majority of the claimed improvements in the model are not merely from a bias towards outputting high-frequency words, and thereby overfitting the chosen test metrics of BLEU and ROGUE, in order to change my score. Right now, I am fairly convinced that this is the case.

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
The paper presents PREDFT (FMRI-to-Text Decoding with Predictive Coding), a novel framework that utilizes predictive coding to translate fMRI signals into continuous language. This approach combines a primary decoding network with an auxiliary network focused on capturing brain predictive coding, aiming to improve the accuracy of language reconstruction from brain signals. The authors conduct experiments on two established naturalistic language comprehension fMRI datasets, showing that PREDFT achieves state-of-the-art performance across multiple evaluation metrics.

### Strengths
1. Integrating predictive coding theory into the decoding process offers a fresh perspective on reconstructing language from brain signals.
2. Experimental results demonstrate that PREDFT outperforms other methods across various evaluation metrics, showing significant improvements.

### Weaknesses
1. In Section 3.3, the authors state, 'During the inference stage, as illustrated in Figure 8, the decoder in the side network is abandoned.' However, they do not provide a detailed explanation of why the decoder is discarded or discuss the potential impact of this decision. It is recommended to elaborate on the rationale behind this choice and its implications on the overall performance and functionality of the model. Specifically, the authors should clarify if the side network decoder is only used as an auxiliary loss during training and is not necessary for the inference stage, and if so, why this design choice was made. A more detailed explanation of the role of the side network decoder and its contribution to the overall model's learning process is needed.

2. As shown in Table 1, PREDFT does not achieve the best performance on ROUGE1-R. The authors should analyze the potential reasons for this and discuss any factors that may have contributed to the lower performance in this specific model. For instance, the model's architecture, training process, or characteristics of the ROUGE1-R metric that might explain the discrepancy. If the authors observed any patterns in the types of language constructs where PREDFT underperformed on ROUGE1-R, they should provide examples. It would be beneficial to understand if the model struggles with specific syntactic structures or semantic content when evaluated with ROUGE1-R.

3. As shown in Table 1, PREDFT without SideNet performs similarly to other methods. However, the inclusion of SideNet leads to a significant performance improvement. The authors should provide a detailed analysis of this phenomenon to explain how SideNet contributes to the model's enhanced performance. It is crucial to understand the specific mechanisms through which the SideNet influences the main network's decoding process. For example, how does the predictive coding representation from the SideNet interact with the main network's input, and what is the nature of the information that SideNet provides that is not captured by the main network alone?

4. Although the authors provide a detailed description of the hyperparameter selection, they do not explain the rationale behind these choices. How these choices relate to the model's performance or the underlying theory of predictive coding. For instance, the authors should explain how the chosen learning rate, batch size, and number of layers in the Transformer architecture align with the predictive coding framework and how these choices were optimized for the specific task. A discussion of the sensitivity of the model's performance to these hyperparameters would also be beneficial.

5. In the regions of interests selection experiment, the authors only consider 'random,' 'whole,' and 'BPC' as the ROIs, which appears somewhat limited. The paper does not clarify whether there are other potential ROIs associated with predictive coding, nor does it provide supporting neuroscience literature for the selection of BPC. It is recommended to either justify the choice of BPC with relevant references or explore additional ROIs to strengthen the study's validity. If authors can explain the process for selecting these particular ROIs and why authors believe these are sufficient to demonstrate the effectiveness of their approach. Additionally, if authors considered any other ROIs and why those were not included in the study. The authors should also clarify if the BPC region is consistent across different subjects or if there are variations that might impact the results.

6. It is recommended that the authors provide pseudocode for the method and an analysis of its time complexity to enhance the reproducibility of the article. The pseudocode should clearly outline the steps involved in both training and inference, and the time complexity analysis should consider the computational cost of each step, particularly the side network and the main network.

7. The results provided by the authors mostly only include the meanvalue. The experimental results should provide the mean, variance, and statistical test results. This is crucial for assessing the statistical significance of the observed improvements and for understanding the variability in the model's performance.

8. In the methods section, some symbols are not defined. It is recommended that the authors compile a list of symbols used in the paper in an appendix to help readers understand better.

### Questions
1. In Section 3.3, the authors state that the decoder in the side network is abandoned during the inference stage. Could the authors provide a detailed explanation of why the decoder is discarded and discuss the potential impact of this decision on the overall performance and functionality of the model?

2. As shown in Table 1, PREDFT does not achieve the best performance on ROUGE1-R. Could the authors analyze the potential reasons for this and discuss any factors that may have contributed to the lower performance in this specific model? For instance, how might the model's architecture, training process, or characteristics of the ROUGE1-R metric explain this discrepancy? Did the authors observe any patterns in the types of language constructs where PREDFT underperformed on ROUGE1-R?

3. As shown in Table 1, PREDFT without SideNet performs similarly to other methods, while the inclusion of SideNet leads to a significant performance improvement. Could the authors provide a detailed analysis of this phenomenon to explain how SideNet contributes to the model's enhanced performance?

4. Although the authors provide a detailed description of the hyperparameter selection, could they explain the rationale behind these choices? How do these choices relate to the model's performance or the underlying theory of predictive coding?

5. In the regions of interest selection experiment, the authors only consider 'random,' 'whole,' and 'BPC' as the ROIs. Could the authors clarify whether there are other potential ROIs associated with predictive coding? If so, could they provide supporting neuroscience literature for the selection of BPC? Additionally, can the authors explain the process for selecting these particular ROIs and why they believe these are sufficient to demonstrate the effectiveness of their approach? Did the authors consider any other ROIs, and if so, why were those not included in the study?

6. Could the authors provide pseudocode for the method and an analysis of its time complexity to enhance the reproducibility of the article?

7. The results provided by the authors mostly only include the mean value. Could the authors include the variance and statistical test results in the experimental results?

8. In the methods section, some symbols are not defined. Could the authors compile a list of symbols used in the paper in an appendix to help readers understand better?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In the submission-6263, the authors  propose PREDFT (FMRI-to-Text decoding with Predictive coding) , which was inspired by predictive coding theory. This theory suggests that when humans listen to a certain speech, their subconscious brain predicts the words they may hear next. Then the author validated this theory through a prediction score. The verification method is to first calculate the correlation coefficient between the features extracted by LLM at the current location and the brain features, and then add the features of an upcoming text segment to the current location features, calculate the correlation coefficient again, and observe the changes in the correlation coefficient. The experimental results show that incorporating upcoming text features can increase the correlation coefficient between LLM features and brain features. Based on the above experimental results, the author designed their own model, which includes the side network to decode upcoming text. In the decoding of current text, the feature from the side network is used to incorporate the predictive coding theory into the method.

### Strengths
The author provided sufficient experiments to demonstrate the significance of his motivation.

### Weaknesses
Although the author's explanation of motivation is very sufficient, I still have a few major questions about the author's method and list them in the questions part.

(1) Why did the author only use BLEU and ROUGE in the experiment? Why doesn't the author use WER, METEOR, and BERTScore which is used in the Tang and MapGuide? BLEU and ROUGE both evaluate the matching degree of n-grams, which can easily lead to surface matching but semantic mismatch. METEOR and BERTScore can better reflect semantic similarity.
(2) Many of the methods compared by the author incorporate LLM, while the author's model is entirely trained with their own transformer. Does this result in the author's method being inferior to the baseline method in terms of semantic similarity?
(3) The author's method was inspired by predictive coding and validated it on LLM using a prediction score. But can the author's own model still observe the same phenomenon on the prediction score? I haven't seen the same experiment evaluating the author's own model.
(4) In some parts of the paper, fMRI is spell as FMRI.

### Questions
(1) Why did the author only use BLEU and ROUGE in the experiment? Why doesn't the author use WER, METEOR, and BERTScore which is used in the Tang and MapGuide? BLEU and ROUGE both evaluate the matching degree of n-grams, which can easily lead to surface matching but semantic mismatch. METEOR and BERTScore can better reflect semantic similarity.
(2) Many of the methods compared by the author incorporate LLM, while the author's model is entirely trained with their own transformer. Does this result in the author's method being inferior to the baseline method in terms of semantic similarity?
(3) The author's method was inspired by predictive coding and validated it on LLM using a prediction score. But can the author's own model still observe the same phenomenon on the prediction score? I haven't seen the same experiment evaluating the author's own model.
(4) In some parts of the paper, fMRI is spell as FMRI.

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
4

### Summary
Recent brain decoding studies have demonstrated that speech perception can be decoded from fMRI recordings and subsequently reconstructed as continuous language. These studies reconstruct continuous language either from specific regions of interest (ROIs) or from the whole brain, using decoder-based language models like GPT-2. Additionally, recent predictive coding studies reveal that the human brain naturally engages in continuously predicting future words across multiple timescales. Building on recent linguistic brain decoding research and the predictive coding approach, this paper explores predictive coding theory in the context of continuous language reconstruction. To this end, the authors propose PREDFT (fMRI-to-Text decoding with Predictive Coding), which consists of a main decoding network and a side network (the predictive coding component). Experimental results on two naturalistic brain datasets (Moth Radio Hour and Narratives) indicate that PREDFT achieves superior decoding performance when comparing the actual story with the reconstructed story.

### Strengths
1. The motivation for using predictive coding in continuous language reconstruction is clear and well-explained.
2. The proposed approach aims to improve the reconstruction of narrative stories from fMRI brain data. This is a very interesting research area because reconstructing language is challenging due to the slowness of the hemodynamic response.
3. The authors compared the reconstruction performance using evaluation metrics against recent studies. Additionally, ablation studies were conducted on the proposed approach, with and without the predictive coding component.

### Weaknesses
1. There are several major weaknesses in this work, particularly concerning the evaluation of reconstruction results:
	- A major concern is that the current study (PREDFT) does not provide a clear evaluation of reconstruction results compared to the baseline paper by Tang et al. (2023). The authors should provide a direct comparison of the reconstructed text with the ground truth, including examples of both successful and failed reconstructions to illustrate the model's strengths and limitations.
	- For example, the authors did not evaluate the word rate in the generated narrative story. Since the fMRI data was captured while participants were listening to stories, each word has an onset and offset. Similarly, during decoding, what is the word rate predicted by the proposed model, and does this word rate match the actual word rate of the original stimuli? A mismatch in word rate would indicate a fundamental flaw in the reconstruction process. Therefore, comparing the reconstructed stimulus to the ground truth (i.e., the actual transcripts of the stimuli) would provide a good sense of whether the outputs are meaningful, as the dataset includes the ground truth of what words participants heard and when they heard them.

2. Furthermore, the authors performed decoding using either random selections of ROIs, the whole brain, or BPC, which includes language-related ROIs. However, prior studies have focused on specific ROIs, such as the language, prefrontal, and auditory association cortices. Therefore, it is unclear how the proposed method compares with prior methods. Since the authors' main research question revolves around how semantic information is embedded in brain signals to improve decoding, they should consider these ROIs, as they maintain a hierarchy of language processing. The lack of focus on established language-related ROIs makes it difficult to assess the contribution of the proposed method.
	- The random selection of ROIs generally leads to low decoding performance. What are these random ROIs? Do they have any overlap with BPC ROIs? The authors should provide a detailed list of the randomly selected ROIs and clarify whether they are entirely distinct from the BPC ROIs. If there is overlap, the results become difficult to interpret.
	- Previous studies have conducted both quantitative and qualitative analyses, reporting what the stimulus decoded at each ROI, including language-related regions in both the left and right hemispheres, as well as using four evaluation metrics. However, this paper does not report any reconstructed stimulus in the main content, nor does it include analysis at the ROI level. Additionally, the authors only used two metrics, and throughout the paper, the focus is more on the scores rather than on the main reconstructed language results. The absence of qualitative analysis and ROI-specific results significantly limits the interpretability of the findings.

3. Although the authors report some results on predictive length and distance from the current word in Figure 1, there are no qualitative reconstruction results for these different predictive lengths and distances. What type of information is the model forecasting based on brain data? Is it syntactic information, such as nouns and verbs, or semantic content? This analysis is clearly missing from the paper. Without this analysis, it is difficult to understand the predictive capabilities of the model.

4. All the figures lack detailed captions. The results presented in the figures are difficult to understand. For instance, what is the prediction score in each subplot of Figure 1? What does each line in the top plots represent? What does prediction distance "d" refer to? Without providing clear details in the figure captions or placing the figures appropriately in the text, it becomes challenging for readers to understand the content and what is being conveyed. The lack of detailed captions hinders the reproducibility and understanding of the results.

5. Since the authors use two encoders and two decoders in the proposed PREDFT, it is unclear which component is primarily responsible for reconstructing the language and which component provides the theme and narrative structure. It would be interesting if the authors reported the generated stimulus from individual components and from PREDFT as a whole, along with the performance metrics. This would help identify the shared and individual contributions of each component during language reconstruction.

### Questions
1. What would be the chance-level performance when reconstructing continuous language? Is there a baseline available for comparison? Additionally, what is the percentage of overlap between random ROIs and whole-brain voxels? Did the authors repeat the selection of random ROIs multiple times to ensure robustness, or did they only select a single set of random ROIs?
2. What is the rationale for using 4D volume data from the Narratives dataset while using 2D brain data from the Moth Radio Hour dataset? Since the Narratives dataset includes both smoothed and unsmoothed versions, along with brain masks to select activated voxels from the 4D volume, why did the authors make these choices regarding data representation?
3. There is no interpretation provided for the two encoders used in PREDFT. The authors could project these voxels onto brain maps to verify the quality of their encoders.
4. Figures 3, 4, 6, and 8 appear redundant. The authors could combine these into a single figure with a comprehensive caption, instead of presenting multiple, repetitive figures.
5. What does the y-axis represent in Figure 9?
5. Several major questions are raised in the weaknesses section.

Typos:

1. Line 35: Bhattasali et al. (2019); Wang et al. (2020); Affolter et al. (2020); Zouet al. (2021)  - > (Bhattasali et al. 2019; Wang et al. 2020; Affolter et al. 2020; Zouet al. 2021)

### Soundness
3

### Presentation
2

### Contribution
2
