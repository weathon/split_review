# EEG-Based Emotion Recognition via Prototype-Guided Disambiguation and Noise Augmentation in Partial-Label Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3, 5, 5, 5

## Abstract
EEG-based emotion recognition offers an objective method for diagnosing emotion-related health issues, but the inherent complexity of emotions often leads to annotation errors and noisy labels. To simulate this labeling process in emotion recognition, we propose a semantic-based candidate label generation method leveraging the GloVe vectors, which considers the semantic relationships between emotions. Under the Partial Label Learning (PLL) scenario, we introduce a novel model called PGNA-PL (Prototype-Guided Noise-Augmented Partial Label Learning). This model learns inter-class relationships of emotions using prototypes, and uses a self-distillation mechanism to iteratively guide the classifier's disambiguation process. To address the low signal-to-noise ratio (SNR) of EEG, we introduce a noise augmentation strategy inspired by the mixup method, incorporating controllable noise to enhance model robustness. Experiments on three public datasets (SEED, SEED-IV, SEED-V) show that our approach achieves state-of-the-art performance, surpassing existing PLL baselines across different candidate label generation modes. Our method effectively disambiguates complex emotions and shows promising results in assisting in the recognition of fear-related disorders.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel EEG-based emotion recognition model, PGNA-PL, which utilizes prototype-guided disambiguation and noise augmentation to improve accuracy in partial label learning (PLL) settings. By leveraging GloVe embeddings to generate semantically informed candidate labels, the approach addresses label ambiguity and low SNR in EEG signals, achieving state-of-the-art results across multiple datasets.

### Strengths
1. The setting of partial label learning for EEG-based emotion recognition is relatively new and interesting.
2. Experiments on three challenging EEG datasets (SEED, SEED-IV, and SEED-V) reveal the approach’s effectiveness in both accuracy and F1 measures.
3. The code is provided and implementation details are comprehensive.

### Weaknesses
1. The emotional semantic labels derived via GloVe are innovative, but it's unclear how these candidate labels compare to using the original dataset labels directly. A comparative analysis between semantic-based and default labels would help clarify the added value of semantic embedding, especially as GloVe vectors may not always capture the full emotional nuance specific to EEG-based emotion recognition. The paper needs to demonstrate that the semantic embeddings provide a genuine improvement over simply using the original labels as candidates, particularly given the potential for semantic drift when applying general-purpose word embeddings to a specialized domain like EEG-based emotion recognition.
2. Although the noise augmentation module is inspired by mixup, the connection to addressing low SNR remains speculative without clear comparative evidence. The paper would benefit from directly comparing PGNA-PL’s noise augmentation with a simple mixup approach to demonstrate its unique effectiveness. A straightforward ablation study excluding the noise augmentation does not sufficiently confirm its necessity; a specific baseline comparison with mixup is essential to establish its impact and necessity in the model's performance. The current justification for the noise augmentation is weak, and a more rigorous comparison is needed to show that the proposed method is superior to existing augmentation techniques.
3. While the study describes its method as a partial label learning (PLL) approach, it seems to depend heavily on fully annotated labels from the datasets to generate candidate labels. Traditional PLL assumes that a data sample's true label is unknown among several candidates, yet here, the candidates seem to be predetermined using GloVe embeddings for emotion categories. This difference in the PLL approach could merit further discussion, particularly regarding the rationale for using the same candidate labels across emotion categories and the method's applicability in true PLL settings. The paper needs to clarify how the method's reliance on fully annotated data for candidate generation aligns with the core principles of PLL, which typically deals with incomplete or ambiguous labels.
4. The method's performance would be more convincing if compared with a fully supervised version of the proposed model, where true labels are directly utilized without PLL. This comparison would reveal the performance trade-offs or benefits PGNA-PL offers in balancing between label ambiguity and robust emotion classification. Without this comparison, it is difficult to assess whether the PLL approach is truly beneficial or if the model's performance could be achieved more effectively through standard supervised learning.

### Questions
1. The tables refer to Semantic Distribution and Russell Distribution as label generation methods, but further explanation is needed. Could the authors clarify the conceptual and practical differences between these two approaches in the context of EEG-based emotion recognition? Additionally, it would help to explain how each distribution affects the model's performance across different emotion categories, given that these distributions likely represent different assumptions on emotion relationships.
2. What is the value of \beta_p in Equation 9?

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
The paper proposed a new method for EEG-based emotion recognition. The method used the semantic relationships between emotions and some prototype, and used a noise augmentation strategy to enhance model robustness. The experiments were done on three public EEG datasets. The paper was well organized.

### Strengths
The work introduced a new aspect to the EEG emotion recognition field, partial label learning. The target problem was clear, the emotion labels might not be accurate and EEG has low SNR.

### Weaknesses
Although the proposed method might provide a new aspect to the problem. But it seemed that the authors might not be fully familiar to EEG analysis. The study was incremental and the contribution was limited. The proposed method was the combination of existing methods in other domains and be modified to EEG analysis. And it was not well modified. For example, the model structure did not fully consider EEG temporal-spatial-spectral information.

### Questions
1. The performance improvement of the proposed method seemed small on the three datasets compared to the baselines. Was the improvement significant enough to draw a conclusion that the proposed method outperformed others?
2. In the experiments, the baselines were not the classic baselines that were often used in EEG analysis. It seems that the work simply took some machine learning methods in other domains and applied them to the EEG domain. Has the authors compared the model performance with other baselines on the same datasets in the literature? 
3. How many prototypes are needed to update in the model? Was it possible to use more prototypes and how did the number of prototypes influence the model performance?
4. There were many writing typos in the paper, the authors should carefully check the English writing.

### Soundness
2

### Presentation
2

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
This paper aims to address challenges in semantic-based candidate label generation, signal-to-noise ratio (SNR) issues in EEG data using a novel prototype-based approach for decoding emotional relationships. The authors apply their method to three publicly available EEG-based datasets on emotion recognition, namely SEED, SEED-IV, SEED-V, and claimed the proposed method achieving the state-of-the-art performance over existing methods across these datasets.

### Strengths
The authors incorporate real-world ambiguous labeling simulation and partial label learning to address the challenge of annotation errors due to the complexity of emotions.

### Weaknesses
1. Semantic Similarity for Candidate Label Generation: The authors claim that the lack of semantic-based candidate label generation in existing partial label learning work for emotion recognition poses a challenge in the field.
However, this assumption is questionable, as it overlooks the psychological closeness of emotions. While GloVe embeddings were used to capture contextual word usage, these embeddings don’t reflect the psychological relationships between emotions. For example, in daily life, 'happy' and 'neutral' are often more easily confused than 'happy' and 'sad'. This difference has been correctly represented in Russell's model but not in the GloVe-based semantic panel. Specifically, as shown in Figure 3(b),  'happy'-'neutral' similarity is 0.5, while 'happy'-'sad' similarity is 0 in the Russell's circumplex model. However, in the semantic panel shown in Figure 3(a), 'happy'-'neutral' similarity is 0.21 while 'happy'-'sad' similarity is 0.64 (3x higher). 
Furthermore, as shown in Figure 3, I think author made a mistake in the captions of Figures 3(a) and 3(b), where it should be 'inter-class similarity' instead of 'inter-class distance'. Since the authors mentioned 'cosine distance' only once in the manuscript (line 425) but mentioned 'cosine similarity' several times, and evidenced in the function 'Semantic_Distribution_similarity' in 'utils.py'(code line 69). Therefore, I strongly suggest that the authors clarify 'distance' in both the main text and figure captions as emotions are closer when their similarity is higher or distance is smaller.  

2. Challenge of Low SNR in EEG: The authors claim to address the challenge of low SNR issue in EEG, as 'To mitigate the low SNR of EEG signals, inspired by the mixup method, we introduce a noise augmentation strategy, incorporating controllable noise to enhance model robustness'. However, this has already been done in CR[1] and PiCO[2] methods. The claim of 'advanced prototype-guided approach require a clearer clarification.

3. Marginal Performance Improvement: The authors claim that 'Experiments on three public datasets (SEED, SEED-IV, SEED-V) show that our approach achieves state-ofthe-art performance.' However, as shown in Tables 1, 2, & 3,the improvement are very marginal, in most cases less than 1%.

4. Evaluation Metric Choice: Why is F1 score chosen as the evaluation metric for the balanced datasets? Additionally, if F1 is used, why not include standard deviation (SD), as is done with accuracy? In 335-228, the authors claim 'The SEED-V dataset adopts a similar design to SEED-IV for cross-validation without the need for sample balancing, since five videos of different emotions always appear sequentially, leading to a 30:15 ratio of 'initial training set' to test set trials.' ...' However, as desribed in the original paper publishing the dataset [3], in SEED-V, each participant repeat session three times, each time contains 15 trials (3 per emotional category), this design ensures that the samples are balanced across emotions in both the training and test sets and no data leakage would occur. It can be also found in the official PyTorch Datasets link: https://torcheeg.readthedocs.io/en/latest/generated/torcheeg.datasets.SEEDVDataset.html#torcheeg.datasets.SEEDVDataset. Could authors provide evidence to support the claims of imbalanced dataset and data leakge in the train-test protocol proposed in [3] or in any dataset used in this study?


5. Comparision with Inappropriate Data Augmentation: Table 4 compares with an augmentation technique, namely additive pepper&salt noise, which is not recommened for EEG data augmentation as it can distort intrinsic EEG features [4, 5].

6. Code Ethics: The authors should properly acknowledge external sources to maintain transparency and integrity. For example, lines 28-309 in 'train_func.py' are directly copied from 'https://github.com/guangyizhangbci/PLL-Emotion-EEG/blob/main/train_func.py'. Similarly, most parts of the code in 'utils.py', even including comments, are identical to 'https://github.com/guangyizhangbci/PLL-Emotion-EEG/blob/main/utils.py'.

### Questions
1. As mentioned above in the 'Weakness' section, authors should clarify the term 'inter-class distance' in both main text and figure captions. 

2. The motivation for applying PLL methods for EEG-based emotion recognition needs further explanation. Specifically, why is PLL necessary in emotion recognition? If annotation error is the issue, how reliable is the labeling in the SEED-series datasets?

3. The SEED dataset includes only three emotions, namely 'happy', 'neutral', and 'sad', which are often not difficult to distinguish. Why not select datasets with a broader range of emotions where ambiguous labeling is more likely to occur?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper, EEG-Based Emotion Recognition via Prototype-Guided Disambiguation and Noise Augmentation in Partial-Label Learning, presents the PGNA-PL model, leveraging Partial Label Learning (PLL) to enhance emotion recognition from EEG signals. Recognizing challenges like noisy data and ambiguous labels in traditional emotion recognition, the authors use a semantic-based candidate label generation method with GloVe embeddings to capture relationships between overlapping emotions. The PGNA-PL model incorporates a prototype-guided noise augmentation module that improves classification accuracy by disambiguating labels and enhancing robustness through controllable noise injection. Evaluations on SEED, SEED-IV, and SEED-V datasets demonstrate state-of-the-art (SOTA) performance, especially in detecting nuanced emotional states.

### Strengths
1) Innovative Use of Semantic Embeddings: The GloVe-based candidate label generation effectively captures the relationships between overlapping emotions, improving the model's ability to distinguish nuanced emotional states.
2) Enhanced Robustness with Noise Augmentation: The PGNA-PL model’s noise augmentation strategy, inspired by the mixup method, adds controlled noise to enhance resilience against EEG’s low SNR.
3) Comprehensive Evaluation and Ablation Studies: Evaluations on three major datasets, including SEED, SEED-IV, and SEED-V, provide a robust validation of the model’s effectiveness.

### Weaknesses
1) Dependency on GloVe Embeddings: The reliance on GloVe embeddings may limit adaptability, particularly as other, more dynamic contextual embeddings (e.g., from transformer models) could provide richer semantic information for label disambiguation. The static nature of GloVe embeddings means that they cannot capture the nuances of context-dependent word meanings, which could be crucial for distinguishing subtle differences between emotional states. This limitation could be particularly problematic when dealing with complex or metaphorical emotional language.
2) Potential Instability with Prototype Guidance: While the prototype guidance module stabilizes the model by not updating candidate labels, there could still be some instability, especially in EEG settings where signals are prone to noise. The prototype vectors, while intended to represent class centroids, might be susceptible to being skewed by noisy EEG data, leading to misrepresentation of the true emotional states and potentially causing the model to converge to suboptimal solutions. The lack of adaptive mechanisms for prototype adjustment could exacerbate this issue.
3) Noise Augmentation Choices: The study could examine how different types of noise augmentation affect model robustness. Currently, the mixup method is effective, but real-world noise may be more complex. The mixup method, while beneficial, might not fully simulate the diverse forms of noise encountered in real-world EEG recordings, such as physiological artifacts or environmental interference. This could limit the model's generalizability to practical scenarios where noise characteristics are more varied and complex.

### Questions
1) How does the model handle datasets  like DEAP?
2) What are the implications of using alternative embeddings?
3) How does the model address unseen emotions or emotions not mapped in the initial GloVe embedding setup?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Summary of the paper:
The present paper proposes a novel approach for EEG-based emotion recognition. The authors propose a method that combines three things to enhance the accuracy of emotion predictions:
1) Semantic-based candidate label generation method for partial label learning (PLL) that incorporates the semantic relationships of emotions.
2) A model which uses emotional prototypes and self-distillation (utilizing KL divergence).
3) A novel noise augmentation approach for EEG data.

Through experiments using three publicly available emotion-based EEG datasets, the authors show that their proposed method achieves state-of-the-art emotion classification results.

### Strengths
Strengths:
1) Three novel proposals (PLL method + model using emotional prototypes + augmentation method), each of which might be useful for the EEG-based emotion recognition community.
2)	The proposed approach obtains good results consistently on three publicly available EEG-based emotion recognition datasets.
3)	It is well motivated that there are ambiguities and annotation errors when annotating emotion-related data.
4)	There is a simple and clever source of inspiration for developing a novel data augmentation strategy for EEG data.
5)	The algorithm listing is clear and concise.
6)	The majority of images and tables are constructed using vector graphics. In particular the tables are visually appealing and easy to read.

### Weaknesses
Weak points:
1) The authors make multiple strong statements and assumptions in the text which are not accompanied with strong evidence (literature/theoretical proof/strong empirical results). As an example, in the text, the authors claim that their proposed method “shows promising results”, “shows potential advantages”, “shows exceptional efficacy”, and shows “potential superiority” in recognizing phobias. If a model has a good classification accuracy of recognizing the emotional category "fear" (ranging between 0.64 to 0.75 in terms of recall), I would argue that one cannot deduce from this whether the model can be used to detect phobias. There are multiple reasons for this: First, phobias are very specific, intense fears which are triggered by particular situations or objects. Simply recognizing the emotional category “fear” well does not provide the context needed to identify a phobia. Second, to automatically detect phobias, machine-learning models would require training data that includes specific phobia-related scenarios and responses. Without data like this, the trained model might not generalize well for phobia detection. Third, phobias can be complex physiological and/or psychological responses, and a model trained for general-level emotion recognition might not be able to capture these kinds of nuances. Therefore, I would argue that the authors do not provide enough evidence to be able to state that their method shows “exceptional efficacy” in recognizing phobias.
2) The motivation for the present work is severely lacking. As the motivation for using EEG-based emotion recognition, the authors state that “Traditional modes of emotion expression, such as facial expressions and spoken language, are easy to disguise, pushing the frontier towards emotion recognition through physiological signals as a more objective assessment method.”. However, EEG-based emotion recognition is far more invasive than video- or speech-based emotion recognition, and test subjects need to basically be in a lab or in lab-like conditions for EEG-based emotion recognition to be carried out. The authors do not give any use-cases or practical reasons on why EEG-based emotion recognition would be more convenient or applicable than using video- or speech-based emotion recognition.
3) One of the key points of the proposed prototype-guided module is mentioned in lines 222-224: "As the iterations progress, different prototype features will provide stable representations for different emotion categories.". Without stableness, the entire PLL process proposed by the authors does not work. However, the authors do not provide anything to assure the reader that the stableness of their method is guaranteed, such as strong backing up using PLL literature, theoretical deductions/proof, or strong empirical results.
4) There are countless typos in the text, making the reader feel like the manuscript was written in a hurry. Also, many concepts (e.g. the GloVe dictionary) are not well introduced to the reader, further adding to the impression that the manuscript is not well-polished.
5) The text flows very unnaturally, in particular in the equations. As of now, the equations are not a natural part of the text, but they appear as if they were appendices within the text. I strongly suggest that the authors take a thorough look at how equations are typically presented in papers related to machine learning.
6) Section 3 (Methods) is very difficult to follow, many parts and details are left unclear even after multiple read-throughs. It is essential that the description of the proposed novel approaches is clear for the reader.
7) The present work would benefit from having notably more references. Currently, there are practically no occasions where there would be more than one reference to support the claims made by the authors.
8) The majority of figure and table captions are not very descriptive, and these figures/tables cannot be understood completely without reading the main text first.
9) Since the datasets that were used in the present study are public, it would be beneficial for both the authors and the EEG-based emotion recognition community to have the code publicly available. (Edit 3rd of December: This statement was false, as there was code provided in the supplementary material which I hadn't noticed.)
10) It is not good practice to start sentences with a variable, e.g. line 200: "p is further processed by C..."
11) It is also not very good practice to end a section with an equation, such as in Equation 8.
12) I appreciate that the majority of images and tables are constructed using vector graphics. However, why are Figures 2 and 3 created with raster graphics? These figures would benefit from being produced in a vector graphics format.
13) Even though the proceedings of the vast majority of conferences are nowadays not in printed format, it is still essential to consider how the paper appears if someone would print it in regular A4 format. For example, in Figures 2 and 3, there are multiple details that cannot be seen properly if the paper is printed in A4 format.
14) Some of the colors of the visualizations are difficult to see against a white background, e.g. in Figure 3 parts (c) and (d).
15) Table captions should always be above the tables (see Table 4).
16) Even though ICLR accepts work on relevant application areas of machine learning such as  applications to neuroscience & cognitive science, in its current state the work is not interesting enough to bring value for the ICLR community. After revising the manuscript, I would strongly suggest that the authors submit the paper to some other relevant conference (e.g. IEEE EMBC 2025), where the target audience would be more suitable for the present study.

Initial recommendation: This paper should be rejected since it contains far too many weak points for it to be considered as an acceptable paper for ICLR (see list of weak points above). These weak points include, for example, multiple strong statements that are not backed up in any way, severely lacking motivation for conducting the present study, and poorly written methodological descriptions that are difficult to follow.

Here are more detailed notes:

Abstract:
1) The Abstract is a little bit confusing and hard to follow overall, having read it two times without reading the main text. However, after reading the main text through once, the Abstract was understandable. In particular, it was difficult to understand on the first read-through that there are three different things that are proposed: the label generation method, a model utilizing emotional prototypes and self-distillation, and a noise augmentation approach.
2) The Abstract ends in a rather strong statement regarding the detection of phobias. Please see the “weak points” section above for a more detailed comment.


1. Introduction:
3) The first few sentences arouse the interest of the reader quite well. However, to support your strong claims (such as the strong linkage between negative emotions and conditions, and that EEG is notable for its precision and high temporal resolution), it would be highly beneficial to have more references. This same issue is repeated throughout the whole paper, where there are practically no occasions where there would be more than one reference to support the claims made by the authors.
4) Motivation is severely lacking: In its current state, EEG-based emotion recognition is a lot more difficult to set up and it is not even nearly as practical or convenient as recognizing emotions from facial (micro)expressions or spoken language. Therefore, the authors’ statement "pushing the frontier towards emotion recognition through physiological signals as a more objective assessment method" is not very valid, because many researchers working on emotion recognition from video or speech data are not progressing towards working on physiological signals; There is still plenty of work to be done in these fields alone, e.g. recognizing emotions from realistic, noisy input video data. Although, I do understand that physiological signal-based emotion recognition can be notably more accurate than recognizing emotions from e.g. videos if the person expressing the emotions is aiming to hide his/her emotions. I would like to see stronger motivation for when and where it would be beneficial or convenient to use an EEG-based emotion recognition setup over other setup types, "traditional modes of emotion expression are easy to disguise" is not a very strong motivation for the present work as it does not give any context on the actual use-cases of EEG-based emotion recognition.
5) "Among these, EEG is notable for its precision and high temporal resolution" --> EEG data is also notable for not generalizing well to machine-learning models, due to e.g. the large variability of EEG measurement setups and configurations (see e.g. https://www.sciencedirect.com/science/article/pii/S0925231224011251 and https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.765525/full).
6) It is well motivated that there are ambiguities and annotation errors when annotating emotion-related data. However, a few additional references would strengthen the given claims.
7) "The introduction of this method can significantly mitigate the impact of labeling errors in EEG-based emotion recognition tasks." --> References are needed to support this claim.
8) Line 080: “…of another samples…” --> “…of other samples…”


2. Related Work:
9) The Related Work section feels rushed and unfinished, and reading it leaves the reader a feeling that he/she has not been thoroughly guided through the work that is relevant to the field. There are many claims that are not given enough support through the use of references, e.g. lines 118-121 contain multiple claims, some of which are rather strong ones, but there are no references at all. The same thing applies for many other parts of the Related Work section, such as in lines 125-129. Additionally, this section is not coherent, for example the last paragraph begins with the sentence "Recent research suggests ABS methods may have greater potential.", greater potential in what? Since paragraphs should be independent entities that can be understood well on their own, this sentence is difficult to understand without a context.
10) The explanation of generating emotionally semantic candidate labels is difficult to follow, in particular the notations for the equations could be clearer. Please see the “weak points” section above for a more detailed comment on the equation notation.
11) Line 179: "...as shown in Equation 2. Where i represents the real emotion category." --> “...Equation 2, where i represents…”

3. Methods:

Section 3.2:

12) In the Introduction section, it is briefly mentioned what is the GloVe dictionary. However, you do not elaborate what GloVe is in the Methods section, which I consider to be a highly important piece of information for the reader to understand what the authors are trying to achieve in the present study. It should be explained to the reader what the GloVe dictionary is. Moreover, in the Abstract, Introduction, and Conclusion there is talk about the GloVe dictionary, in the Methods section there is talk about GloVe Vectors (and why is Vector with a capital letter?), and in the Experiments section there is talk about GloVe embeddings. I am assuming that all of these mean the same thing, so why are you using different terms in your text? Or if they mean different things, you should elaborate on this detail better.

13) Lines 183-184: “This step ensures that the labels can be interpreted as probabilities, which is useful for training probabilistic models” --> Discriminative neural networks, such as CNNs that were used in the present study, are NOT probabilistic models! These models are deterministic, meaning that once trained, they give the same output for the same input. These models learn a mapping from the input to the output without modeling the probability distributions of the data.

Section 3.3:

14) When talking about differential entropy features, should there be a reference to https://ieeexplore.ieee.org/document/6695876?
15) Line 195: section 3.2 --> Section 3.2
16) The following sentence "n is the number of samples in the dataset, and m is the batch size." is completely disconnected. The variable m is not even used anywhere nearby in the text, so why is it defined in this sentence?
17) Lines 197-198: "It is noted in the Figure 1 that basic modules contain an encoder E and a classifier C, which are used to extract high level features and achieve emotion recognition, respectively." This sentence has many issues. First of all, there isn't anything mentioned about Figure 1 beforehand, so "the" cannot be used before "Figure 1". Also, what is meant by a "basic module"? The entire text does not talk anything about basic modules before or after this appearance of the concept. How can the reader know what is meant by a "basic module"? Furthermore, when talking about classification models in neural networks, it is not very formal to say that these classifiers "achieve emotion recognition". A better way to phrase this would be e.g. that these classifiers "assigns the high-level features produced by the encoder to specific emotion categories" or "process the high-level features to determine the most likely emotion for each input signal" etc. etc.
18) Line 198: "The function in E..." --> "The functions in E..."

Section 3.3.1:

19) Lines 222-224: "As the iterations progress, different prototype features will provide stable representations for different emotion categories." This is a very strong statement, that requires either strong backing up using PLL literature, theoretical deductions/proof, or strong empirical results.
20) Line 227: "By calculating the distance-based similarity between the different prototype features". I am assuming that the authors should be referring to Equation 1?
21) Lines 228-229: "As shown in Equation 7." --> This sentence is completely disconnected from the previous sentence.

Section 3.3.2:

22) Lines 244-246: "Considering that the differences in EEG signal distributions between different emotional categories are smaller than those between EEG signals and other types of noise..." This is a good source of inspiration for developing a novel data augmentation strategy for EEG data.
23) Lines 247-249: "Unlike mixup, our method retains most of the current sample’s features without changing the corresponding candidate label." This is a strong claim that is backed up in the following text. However, in my opinion, it should be already briefly elaborated in this sentence that how does the proposed data augmentation method retain most of the current sample's features, as in its current state the sentence just raises more questions and confuses the reader. For example, "...without changing the corresponding candidate label by (something here). This is further detailed below."
24) The algorithm listing is clear and concise.
25) Equation 11: The formatting for x_i_noised should be further examined.
26) Lines 262-264: "Furthermore, the Beta sampling method provided by Equation 9 offers a wider range of blending possibilities, enhancing the model’s generalization and robustness." --> This claim is not supported anywhere in the text, there are e.g. no experiments of references to show that this statement is valid.

Section 3.3.3:

27) Line 294: "...proposed by DNPL (Seo & Huh, 2021)" --> "...proposed by (Seo & Huh, 2021)". The method DNPL has not proposed anything, but the authors of the method have.

Section 3.3.4:

28) Why is there such a short section? This section should be merged to e.g. Section 3.3.3.
29) Line 306: "L_overall" --> The appearance of this variable should be double-checked.

Section 3.3.5:

30) The title is misspelled.
31) Lines 314-317: There are multiple errors/inaccuracies in the text. First of all, there isn't such a thing as a "batch normalization layer", it is just "batch normalization". Second, I believe the authors mean "...through a flattening operation..." and not "...through a flattening...". Third, it is just a single linear layer, not a "single-layer linear layer".

Section 4.1:

32) Why is "initial training set" in quotation marks?
33) Why are evaluation metrics (e.g. Accuracy) written using capital letters?
34) Line 342: "Appendix A.3", not "Appendices A.3".
35) Line 347: It should be mentioned what the Russell distribution is. Now it is only briefly mentioned in the Introduction section, and there it is not very well detailed either.

Section 4.2.1:

36) Line 355: Why is Macro written with a capital letter?
37) Line 365: The authors mention potentially unstable training as a drawback for IBS-based PLL methods. However, they do not elaborate anywhere in the manuscript on how their approach produces a stable training process.
38) Line 404: Why is Semantic written with a capital letter?

Section 4.2.2:

39) Line 411: Again, why is Semantic written using capital letters?
40) Figure 2: The datasets and conditions should be visualized in the subplots. Now it is not explicitly shown (or elaborated on in the caption) that which of the subplots correspond to which dataset or label distribution.
41) If a model has a good classification accuracy of recognizing the emotional category "fear" (approx. 70%), I would argue that one cannot deduce from this whether the model can be used to detect phobias. Please see the “weak points” section above for a more detailed comment.
42) In Section 4.1, the authors refer to the emotional categories using lower case letters, but in this section the authors use capital letters. The same applies for Section 4.2.3.

Section 4.2.3:

43) It is not explained well how PCA was used for the visualization of Subfigures (c) and (d) of Figure 3. From which features were the PCA features computed? For visualizing that data in 2D, how many principal components were used in the calculation of PCA? And were the two highest-variance components then selected for the visualization to get a 2D image? Is there only one prototype for each emotion, or are the shown categories somehow fused together from the prototypes of the dataset samples?
Conclusion:
44) Concise wrap-up to the present work.
45) Line 539: “The confusion matrix suggests our method’s potential superiority in treating phobias.” --> This is a very strong statement, please see the “weak points” section above for a more detailed comment.

References:

46) There are a little over 30 references. The text would most certainly benefit from a stronger linkage to theory and prior work through the use of more references.
47) The bibliography style is not consistent: Some references have page numbering using the abbreviation “pp.” while others don’t, some journals have ISSN and/or DOI displayed and some don’t etc. etc.
48) Some title names need to be reformatted in terms of capital letters. For example, the abbreviation for principal component analysis never appears in the form “pca”, but it is always in capital letters, i.e. “PCA”. As another example, electroencephalography is typically abbreviated with capital letters, i.e. EEG, but now some appearances of the abbreviation are with small letters (eeg) and others have the same abbreviation with capital letters (EEG).

Appendix A.1:

49) Line 647: "Conv Layer" is not a proper way of writing "convolutional layer" in the body text.

Appendix A.2:

50) "...focused on binary or three emotion classification." --> "...focused on binary or ternary emotion classification."
51) Line 675: "The SEED-IV dataset extends the SEED dataset..." --> It is not elaborated whether the SEED dataset is included in SEED-IV (as the term "extends" suggests), or if it is a completely distinct dataset. Given that there are additional emotion categories, the latter option seems more probable.
52) Line 683: Why is "Disgust" written with a capital letter?
53) Lines 690-691: "To prepare for model training, we normalized the vector of each DE feature as input." --> What normalization strategy what used? For example, was each 4-second segment normalized at segment-level, or was each 4-second segment normalized at dataset-level? Also, was the normalization carried out so that there would be zero-mean and unit-variance segments, or was some other normalization method used?
54) It is not explicitly mentioned how many samples are there in each of the three datasets. This information is very important in machine learning, as it impacts many details regarding the model training process.

Appendix A.3:

55) Line 701: Why are the random seed numbers explicitly mentioned? This information is not useful at all.

Appendix A.4:

56) Line 733: "Notably effective in EEG-based emotion recognition applications." --> This is not a well-formulated sentence.
57) Lines 735-754: The sentences are not well-formulated. For example, the sentence on line 745 should start something like "The method performs..." etc., and not "Performs...".
58) It is very difficult to understand how the presented ABS and IBS methods work, since the methods are presented very shortly but with lots of technical details that would need a larger context. For example, on line 742 it is mentioned that "...uses intrinsic representations learned through a CAV model...", but nowhere in the entire manuscript there is anything said about what these CAV models are, or let alone what the abbreviation CAV even stands for.

### Questions
See detailed notes.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a semantic-based candidate label generation approach for addressing the challenge of Partial Label learning (PLL) in EEG-based emotion recognition by incorporating the semantic relationship of emotions. Their approach incorporated a prototype-guided module with a self-distillation strategy to improve the generalization capability.
Experiments were conducted on three benchmark affective computing datasets.

### Strengths
•	The overall application is interesting. The Emotion recognition task using EEG signals is challenging in the affective computing field.
•	Partial labeling learning (PLL) is an emerging framework in weakly supervised machine learning with interesting application in the affective computing. PLL can potentially model the case where the affective label is uncertain i.e. PLL can model the case where each training example corresponds to a candidate affective label set and only one label concealed in the set is the ground-truth label.

### Weaknesses
•	The novelty contribution of the paper is limited. The overall method seems quite specific to the task and the benchmark datasets. No theoretical and empirical evidence was provided on how the approach can be generalized on different affective computing tasks (e.g., multi-task scenario) and different naturalistic datasets
•	The SNR augmentation techniques proposed by the authors are not novel and seem completely based on the paper Zhang et al., 2018. This point cannot be a claim for contribution
•	The paper is not correctly placed in the context of related literature. It is not clear the difference concerning other partial label learning approaches and the difference concerning self-distillation methods
•	Generating Emotionally Semantic Candidate Labels: The GloVe approach was proposed by Pennington et al. 2014. The authors fully replicate the GloVe approach to obtain semantic embedding for various emotions. Moreover, emotions can be very complex (different hierarchy, scale, etc..). The authors should cover different approaches for modeling the emotion (i.e., dimensional and continuous affect modeling). This multi-dimensional nature of the emotions is not taken into account in Eq1-3
•	Prototype-Guided Noise-Augmented Partial Label Learning Model: Also here, the module seems composed of a standard decoder and classifier approach widely used in the literature
•	Architecture details: It is not clear why the authors do not explore other models architecture
•	Experimental setup: Although the authors provide details on the hyperparameters in Appendix Table 6, it is unclear how the hyperparameter tuning was performed, i.e., hyperparameter range and optimized metric.
•	Experimental setup: It is unclear why the authors do not implement a Leave-one-subject-out procedure. In the emotion recognition task, it is highly relevant that the model can generalize across unseen subjects instead of unseen trials (perhaps to the same training subject)
•	Experimental setup: experiments are limited. Multiple task case is not considered. Several emotions can occur simultaneously. Moreover, other naturalistic datasets should be considered for evaluating the proposed approach
•	Results: Tables 1,2 and 3. Standard deviation accuracy is very high. Macro-f1 and micro-f1 are reported without any statistical test. Overall, it is impossible to justify the significative gain of the proposed approach concerning other state-of-the-art methodologies.
•	Visualization of prototype-guided capabilities: this analysis tries to visualize the latent relationship among different emotion labels. However, it is unclear how this relationship is connected with the predictive performance of the proposed model. 

Minor points 

•	Prototype-Guided Noise-Augmented Partial Label Learning Model: authors should provide a rationale behind the feature extraction stage. It is not clear why only the differential entropy features of EEG are used
•	Notation of different equations is sometimes omitted or ill-defined (e.g. v_{j} and v_{i} in equation 1)
•	The overall organization of the paper is poor. For instance, section 3.3 provides a feature preprocessing step to increase the SNR. It should be placed before the methodological section. Moreover, there are several sentences that disrupt the logical flow of the paper

### Questions
•	The paper lacks a clear differentiation from existing partial label learning and self-distillation methods. Can you clarify how your approach significantly differs from these established methods?
•	Considering the complexity and multi-dimensionality of emotions, why was the GloVe method chosen exclusively for semantic embedding? Are there alternative approaches that might capture the multi-dimensional nature of emotions more effectively?
•	Could you elaborate on the process for hyperparameter tuning, including the range of hyperparameters tested and the criteria for optimization?
•	Why was the leave-one-subject-out procedure not implemented, given its relevance in demonstrating generalizability across unseen subjects in emotion recognition tasks?
•	The experiments appear limited to specific tasks and datasets. How might the model perform across multiple simultaneous emotional tasks and other naturalistic datasets?
•	Is the performance of the proposed approach significantly better than that of other competitors?

### Soundness
2

### Presentation
3

### Contribution
2
