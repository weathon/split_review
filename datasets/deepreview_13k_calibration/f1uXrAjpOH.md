# Open-vocabulary Multimodal Emotion Recognition: Dataset, Metric, and Benchmark

- Decision: Reject
- Avg Score: 5.40
- Scores: 8, 5, 3, 5, 6

## Abstract
Multimodal Emotion Recognition (MER) is an important research topic. This paper advocates for a transformative paradigm in MER. The rationale behind our work is that current approaches often rely on a limited set of basic emotion labels, which do not adequately represent the rich spectrum of human emotions. These traditional and overly simplistic emotion categories fail to capture the inherent complexity and subtlety of human emotional experiences, leading to limited generalizability and practicality. Therefore, we propose a new MER paradigm called Open-vocabulary MER (OV-MER), which encompasses a broader range of emotion labels to reflect the richness of human emotions. This paradigm relaxes the label space, allowing for the prediction of arbitrary numbers and categories of emotions. To support this transition, we provide a comprehensive solution that includes a newly constructed database based on LLM and human collaborative annotations, along with corresponding metrics and a series of benchmarks. We hope this work advances emotion recognition from basic emotions to more nuanced emotions, contributing to the development of emotional AI.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper centers on the task of multimodal emotion recognition. Unlike prior work, which primarily assigns a single label and fixes the label space, this study expands upon earlier tasks, enabling the prediction of multiple labels across various categories. This approach allows for a more nuanced representation of a person’s emotional state. In addition to establishing this new task, the paper also presents a newly constructed dataset, defines evaluation metrics and baseline systems, and undertakes foundational work within this area. Furthermore, the experimental sections offer insights and guidelines for advancing solutions to this task in future research.

### Strengths
This paper introduces a novel task, OV-MER, which extends traditional multimodal emotion recognition (MER) to more comprehensively capture individuals' emotional states. The authors have conducted foundational research in this area by constructing a dataset, defining evaluation metrics, and proposing initial solutions. Overall, the paper is well-structured, and this advancement may enhance the application of MER in downstream tasks such as human-computer interaction. Additionally, the paper includes discussions on ethics and reproducibility.

### Weaknesses
1. The color scheme in Figure 5 does not align with the main visual style of the paper. It is recommended to redraw this figure for consistency.
2. In Section 6, please provide additional elaboration on the recommendations for framework design, as this could be valuable for future researchers. Specifically, the paper should detail concrete strategies for integrating subtitle information, such as specific fusion techniques (e.g., attention mechanisms, late fusion, early fusion) and their expected impact on performance. Furthermore, the discussion should include the choice of pre-trained models for each modality and how they are fine-tuned for the OV-MER task.
3. Traditional facial emotion recognition methods often utilize AU units and assign a single label per face. However, this paper’s OV-MER assigns multiple labels to a video. Could you clarify why videos in multimodal scenarios are suited to convey multiple emotions? It would be beneficial to discuss the temporal dynamics of emotions in videos, and how these dynamics justify the need for multiple labels, as opposed to a single dominant emotion.
4. Table 1 includes only a limited selection of emotion datasets. Please consider expanding it to include additional datasets, such as MSP-Podcast. The table should also include details on the size, modality, and annotation scheme of each dataset to provide a comprehensive comparison.
5. In Table 2, please further clarify the distinctions between the labels extracted from CLUE-Multi and the final ground truth. Specifically, what types of discrepancies were observed between the different language versions, and what specific manual checks were performed to ensure the final ground truth is reliable?

### Questions
Please refer to my comments on weaknesses.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work focuses on introducing a new perspective on emotion annotation by not restricting it to classic categories and taking advantage of large language models in collaboration with humans for a more nuanced translation into labels. The proposed method increases the label space of emotion labels with a more detailed multi-label perspective, which can promote efficiency and understanding of emotions by systems. Furthermore, using an LLM over the output from multimodal LLMs can promote a detailed, closer-to-machine understanding of these labels. By grouping labels and defining metrics for sound evaluation, the authors provide a deeper view of label similarity to assess the system’s true understanding of emotion.

### Strengths
The work presents an improvement over conventional emotion labeling by proposing a richer annotation which can enhance machine’s understanding of emotion. Additionally, the study focuses on the ambiguities and overlaps in emotional labels—a vital contribution to the field. Leveraging LLMs along human experts bridges the gap between human intuition and machine learning, making the model's emotional comprehension more transferable and adaptable.

### Weaknesses
dependency of this approach to a certain versions of large language model definitely has its own limitations. From known weaknesses of this models to potential future risks of such approach. Furthermore, attempts to control this is quite expensive and risky. The bigger concern that comes to my mind is the effect of mirrors reflection in learning. How can we be sure that from this circle of learning, a limited and biased understanding is not created for machine learning?
A broader concern is the issue of model feedback loops—how can we be confident that machine learning isn't developing a narrow, biased interpretation of emotions from these circular, LLM-driven annotations? This feedback cycle may compromise the depth of emotional understanding in machine learning.

What is meant by the "short duration of video"? How can you be sure that a few frames (3) can thoroughly describe and capture facial motions indicating emotions? As you know, previous work in the field highlights the importance of facial movement features in video inputs, and as humans, we can imagine how fast movements can show excitement, which may not necessarily be captured by three frames. Furthermore, have you experimented to see if increasing the frame count could improve levels of hallucination in VLLM? Could the information gap be pushing the model?

As you mentioned, the role of VLLM control annotators includes adding missing content. How did the human annotators who evaluated the VLLM output capture visual data? Did they view the entire video or the same inputs as the VLLM?

What is the reason behind the difference in performance between matching-based and LLM-based metrics? I would prefer a more analytical study rather than just reporting results. I also suggest a deeper study on the effectiveness of multimodal fusion, as this title suggests an important question that has not been investigated as deeply as it could be.

Did you consider human evaluation of the combined output of ALLM and VLLM? How capable do you think this combination is of handling ambiguous and contradictory cases? Furthermore, how can we ensure that our fusion is unbiased?

I see that no annotation control has been used for the merging step. Do you have a control measure for this step? How can we be sure the merge is effective enough?

Regarding the language test, I appreciate that you included it, but one question that comes to mind is the purpose of comparing the similarity of the label sets from Yce to Yee. I believe these sets are not from the same data, as the former comes from data originally in Chinese (translated to English) and the latter from data in English. Given this, I understand the importance of comparing Yec to Yee, which can ensure that the model is not biased by language in the same data, but not Yce to Yee. In any case, I believe you could include more details on language.

In a comparison of human-only and human-LLM collaboration in clue generation, I couldn't understand why you relate the longer length of clues in human-LLM collaboration to informativeness regarding minor details. I don't question the assumption, as I see this fact more clearly in the comparison of label counts; perhaps elaborate more on that.

### Questions
What is meant by the "short duration of video"? How can you be sure that a few frames (3) can thoroughly describe and capture facial motions indicating emotions? As you know, previous work in the field highlights the importance of facial movement features in video inputs, and as humans, we can imagine how fast movements can show excitement, which may not necessarily be captured by three frames. Furthermore, have you experimented to see if increasing the frame count could improve levels of hallucination in VLLM? Could the information gap be pushing the model?

As you mentioned, the role of VLLM control annotators includes adding missing content. How did the human annotators who evaluated the VLLM output capture visual data? Did they view the entire video or the same inputs as the VLLM?

What is the reason behind the difference in performance between matching-based and LLM-based metrics? I would prefer a more analytical study rather than just reporting results. I also suggest a deeper study on the effectiveness of multimodal fusion, as this title suggests an important question that has not been investigated as deeply as it could be.

Did you consider human evaluation of the combined output of ALLM and VLLM? How capable do you think this combination is of handling ambiguous and contradictory cases? Furthermore, how can we ensure that our fusion is unbiased?

I see that no annotation control has been used for the merging step. Do you have a control measure for this step? How can we be sure the merge is effective enough?

Regarding the language test, I appreciate that you included it, but one question that comes to mind is the purpose of comparing the similarity of the label sets from Yce to Yee. I believe these sets are not from the same data, as the former comes from data originally in Chinese (translated to English) and the latter from data in English. Given this, I understand the importance of comparing Yec to Yee, which can ensure that the model is not biased by language in the same data, but not Yce to Yee. In any case, I believe you could include more details on language.

In a comparison of human-only and human-LLM collaboration in clue generation, I couldn't understand why you relate the longer length of clues in human-LLM collaboration to informativeness regarding minor details. I don't question the assumption, as I see this fact more clearly in the comparison of label counts; perhaps elaborate more on that.

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
5

### Summary
Traditional emotion recognition tasks typically focus on predicting a single label for a given data point, such as "angry," "happy," or "surprised." This work argues that more nuanced emotions cannot be captured by this limited set of labels. Therefore, it proposes an open-vocabulary approach (OV-MER), where the number of categories is greatly expanded, thus facilitating the development of emotion AI. Overall, the main contributions include the development of datasets, new metrics, and a new task.

### Strengths
1. The authors have effectively expanded upon a previous dataset by implementing thoughtfully designed metrics grounded in fundamental emotional theories.

2. The problem formulation is clear, and the motivation is intuitive.

3. The experiments are well-conducted and organized.

4. Significant effort and comprehensive content have been included to ensure reproducibility.

### Weaknesses
1. While it's true that nuanced emotional labels can't always be conveyed by a single adjective, like "surprised," as it may stem from either positive or negative experiences, the VAD (valence, arousal, and dominance) framework can help mitigate this issue. This is why emotion recognition tasks are generally categorized as either discrete label-based or dimensional-based. By using VAD scores, we can better distinguish whether "surprise" is elicited by positive or negative emotions. Discrepancies do exist within each subject's understanding and annotators's agreement. However, it is not clear how the proposed approach addresses this issue, particularly regarding the intensity of emotions. The authors mention in Appendix Section G, 'Specifically, in the first round, we randomly select four annotators to check the clues and labels; in the second round, we merge the clues and labels reviewed by the first four annotators and ask another four annotators to perform a second round of checks.' However, the specific criteria for aligning annotations, and what has been removed or kept, remains unclear. The process of merging and refining labels across multiple annotators needs more detailed explanation, especially how disagreements are resolved and how the final label set is determined.

2. Section 2, which focuses on the construction of the 'OV-MERD dataset', is one of the most significant contributions of this work. However, the authors first discuss feature extractions and annotations, leaving readers unclear about the original data source until Section 2.3. This structure is not well-designed; as a reader, it became frustrating to navigate from the first page to Figure 2 and then through Sections 2.1 and 2.2 without understanding the origins (where and what) of the original data until Section 2.3 on page 4. This makes the paper difficult to follow. The lack of initial context regarding the source dataset hinders the reader's ability to fully grasp the significance of the annotation process.

3. In Section 2.3, the phrase "evenly select samples with further annotation" is vague. Does this refer to the original dataset (MER2023), which (I can only assume) has an even number of samples under each category? Or is it discussing the newly constructed dataset? I interpret it as referring to the original dataset based on Section E in the Appendix, but this should be stated more clearly. The ambiguity surrounding the selection process for further annotation needs to be resolved to understand the dataset construction fully.

4. Another concern is the grouping strategy. The authors utilized LLM and Putchik's emotional wheels to group several emotions into single labels. However, the order of discrete emotions in each group—such as "surprise," "nervous," and "dissatisfied"—is crucial, as different arrangements can lead to varied interpretations of the data points. This perspective is not addressed or mentioned anywhere in the paper. The potential impact of label order on the interpretation of data points is a critical aspect that requires further consideration and discussion.

5. Additionally, what are the visual and acoustic cues mentioned? Are there any low-level details? Or are they just text output from LLM? The lack of clarity regarding the nature and detail of visual and acoustic cues used in the annotation process is a significant gap in the methodology description.

6. A key issue in emotion recognition and affective computing is the cultural differences that influence emotional interpretation. People from different linguistic and cultural backgrounds can interpret and express emotions, like anger, in distinct ways. Although the authors primarily used Chinese and English in this work, they have not discussed these potential differences, especially considering they propose new metrics and benchmarks. Further background on the 'expert annotators' is not detailed enough. The absence of a discussion on cultural influences and the limited background on the annotators raises concerns about the generalizability and reliability of the proposed approach.

7. The discussion regarding "Limitations" is quite vague. What does "more effective" model mean? How do the authors intend to "broaden the scope of your evaluations"? The lack of specific details in the limitations section makes it difficult to assess the future direction of the research.

Minor Issues:
Does 'MLLM' first mentioned in the third contribution stand for Multimodal LLM? It needs to be specified.

The dataset comparison can be more comprehensive by including more recently released datasets in 2023 and 2024.

### Questions
Please see the 'weaknesses.'

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a novel paradigm in multimodal emotion recognition called Open-vocabulary Multimodal Emotion Recognition (OV-MER), which aims to address the limitations of traditional methods that rely on a fixed set of emotion labels. The OV-MER aims to better capture the subtle variations in human emotions by allowing predictions across a broader range of emotion categories. To support this method, the authors developed a new dataset named OV-MERD, using a collaborative annotation strategy between humans and large language models (LLMs) to generate detailed emotion-related descriptions (CLUE), which enrich the variety and depth of emotion labels. The paper defines new evaluation metrics based on emotional similarity grouping and conducts extensive experiments with various baseline models to highlight the challenges and limitations of this task. The study also emphasizes the advantages of human-LLM collaboration in generating more comprehensive emotion descriptions, as opposed to human-only annotations.

### Strengths
1. The paper introduces a novel paradigm, which extends beyond traditional methods that rely on a fixed set of emotion labels. 
2. The development of the OV-MERD dataset, which includes a wide range of emotion categories, is a significant contribution. Its rich diversity allows models to learn from a broader spectrum of emotional expressions, which may be used to improve the generalizability of emotion recognition systems.
3. The paper conducts comprehensive experiments and benchmarks, demonstrating the effectiveness of human-LLM collaboration-based  CULE-Multi.

### Weaknesses
1. The baseline results rely on CLUE-Multi/A/V/T descriptions that include human checks. In real-world scenarios, the human intervention is impractical and the actual performance may be lower. Specifically, the reliance on human-verified CLUE descriptions for training the baseline models introduces a significant gap between the experimental setup and real-world applicability, where such manual verification is not feasible. This raises concerns about the generalizability of the reported results.
2. The dataset’s cartoonish style could hinder the model’s ability to generalize to real-world data, potentially limiting its effectiveness in practical applications. The stylized nature of the dataset, while potentially useful for controlled experiments, may not accurately represent the complexities and nuances of real-world emotional expressions, leading to a domain shift problem when applied to more realistic scenarios.
3. There is a lack of information on the total number of samples and the train/validation/test split. The absence of detailed dataset statistics, including the total number of samples and the specific division into training, validation, and testing sets, makes it difficult to assess the robustness and reliability of the experimental results. This lack of transparency also hinders reproducibility and comparability with other studies.
4. The paper mentioned, "This is because, in MER, text is emotionally ambiguous; without integrating other modalities, we cannot accurately understand the emotions conveyed through text." However, as far as I know, there are datasets like MOSI and MOSEI where the text/language modality contributes more than other modalities, as evidenced by relevant experimental results [1-4]. Is this explanation of yours appropriate, or is it specific to this particular dataset?

### Questions
1. The models in the paper are trained using CLUE-Multi/A/V/T data that includes manual checks, which ensures high-quality and detailed emotion descriptions. However, in real-world applications, it is likely that only LLMs-generated CLUEs without any human oversight will be available. Would this discrepancy lead to significant performance degradation in models trained using CLUE-Multi/A/V/T data?
2. Would the cartoonish style of the dataset cause a significant domain shift problem? Specifically, how would a model pre-trained on this dataset perform when tested or fine-tuned on other datasets like DFEW and IEMOCAP? Do you consider any adaptation strategies to mitigate potential domain shifts?
3. What is the sample size of the dataset, and how are the train/validation/test sets divided?
4. The paper mentioned, "This is because, in MER, text is emotionally ambiguous; without integrating other modalities, we cannot accurately understand the emotions conveyed through text." However, as far as I know, there are datasets like MOSI and MOSEI where the text/language modality contributes more than other modalities, as evidenced by relevant experimental results [1-4]. Is this explanation of yours appropriate, or is it specific to this particular dataset?

Reference

[1] Hazarika, Devamanyu, Roger Zimmermann, and Soujanya Poria. "Misa: Modality-invariant and-specific representations for multimodal sentiment analysis." in ACM MM 20.

[2] Yu, Wenmeng, et al. "Learning modality-specific representations with self-supervised multi-task learning for multimodal sentiment analysis." in AAAI 2021.

[3] Zhang, Haoyu, et al. "Learning Language-guided Adaptive Hyper-modality Representation for Multimodal Sentiment Analysis." in EMNLP 2023.

[4] Feng, Xinyu, et al. "Knowledge-Guided Dynamic Modality Attention Fusion Framework for Multimodal Sentiment Analysis." in EMNLP 2024.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new task in the realm of MER, termed Open-vocabulary MER (OV-MER), which contains a broader and more diverse range of emotion labels. The authors propose an LLM-based framework to generate labels for OV-MER, along with corresponding metrics and benchmarks for evaluation.

### Strengths
1. Extensive experiments with plenty of SOTA LLM methods are conducted.
2. The visualizations are clear and straightforward, making the content easy to follow.
3. The idea of extending MER to OV-MER is novel and adds a fresh perspective to the field.

### Weaknesses
1. The dataset scale is not mentioned or compared in Sec 2 or Tab 1.
2. There is no quality evaluation for the generated labels (e.g., comparison with manual annotations), and their validity has not been assessed (e.g., by using the dataset for pre-training or other downstream tasks). Although there are comparisons with humans regarding clue length, label count, and word cloud, the label accuracy is never evaluated or discussed. This raises concerns about the reliability and overall usefulness of the dataset for the study.
3. The setup in Table 2 and 3 presents a data leakage issue. The ground truth label is generated using SALMONN and GPT-4V, but both of these methods are also being evaluated.

### Questions
1. Sec 2.1, pre-annotation, what is the average duration of the videos? I'm concerned that using only three frames as input may miss a significant amount of visual info, especially since the paper later notes that there are errors, duplicates, and missing info related to visual clues.
2. Sec 2.1, manual check, could you please clarify why ALLM struggles to capture emotion-related acoustic features? From my understanding, paralinguistic information in the audio modality contains meaningful emotion-related features, which should be useful in this context.
3. Table 1, CMU-MOSEI has discrete emotion labels.
4. In Sec 3.1, the GPT-based grouping is described as costly, but if the entire process only costs $1, it doesn't seem to be a significant expense. Could you clarify the reason?
5. Fig 4 (a), typo in video branch: ALLM -> VLLM.
6. Sec 4.1, CLUE-A, could you explain why text is used to generate acoustic clues when the audio already contains the necessary content information? It seems redundant.
7. It is not clear what fusion method you use in Tab 3.

### Soundness
3

### Presentation
3

### Contribution
3
