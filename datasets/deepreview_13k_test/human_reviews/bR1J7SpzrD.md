# Synthio: Augmenting Small-Scale Audio Classification Datasets with Synthetic Data

- Decision: Accept
- Scores: 8, 8, 5, 6

## Abstract
\vspace{-2mm}
We present \textbf{Synthio}, a novel approach for augmenting small-scale audio\footnote{We use ``audio'' to refer to acoustic events comprising non-verbal speech, non-speech sounds, and music.} classification datasets with synthetic data. Our goal is to improve audio classification accuracy with limited labeled data. Traditional data augmentation techniques, which apply artificial transformations (e.g., adding random noise or masking segments), struggle to create data that captures the true diversity present in real-world audios. To address this shortcoming, we propose to augment the dataset with synthetic audio generated from text-to-audio (T2A) diffusion models. However, synthesizing effective augmentations is challenging because not only should the generated data be \textit{acoustically consistent} with the underlying small-scale dataset, but they should also have sufficient \textit{compositional diversity}. To overcome the first challenge, we align the generations of the T2A model with the small-scale dataset using preference optimization. This ensures that the acoustic characteristics of the generated data remain consistent with the small-scale dataset. To address the second challenge, we propose a novel caption generation technique that leverages the reasoning capabilities of Large Language Models to (1) generate diverse and meaningful audio captions and (2) iteratively refine their quality. The generated captions are then used to prompt the aligned T2A model. We extensively evaluate Synthio on ten datasets and four simulated limited-data settings. Results indicate our method consistently outperforms all baselines by 0.1\%-39\% using a T2A model trained only on weakly-captioned AudioSet.
\vspace{-2mm}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper explores the use of synthetic data to enhance small-scale audio classification tasks, addressing two primary challenges in synthetic augmentation: acoustic consistency and compositional diversity. To improve consistency, a preference alignment approach is introduced to better align the domain of synthetic data with the source dataset. For diversity, the authors propose language-guided audio imagination, utilizing large language models to iteratively generate captions that blend existing and novel acoustic components, feeding into a text-to-audio generation model.

### Strengths
- The paper effectively identifies two key challenges in synthetic data-based augmentation, providing clear and well-reasoned explanations.
- The proposed techniques directly address these challenges and are demonstrated to be both practical and beneficial according to the experimental results.
- The experimental setup is comprehensive, covering various types of audio events, which strengthens the validity of the findings.

### Weaknesses
The work is well-presented and thorough, with no significant weaknesses noted. However, the reviewer has a few suggestions and minor comments, outlined in the Questions section below.

### Questions
- Although the paper strives to present all concepts (with background) in a single, self-contained format, it would benefit from careful notation selection. Reusing the same notation for different concepts could be confusing. For example, using the symbol "beta" in different contexts (e.g., in diffusion, RLHF, and DPO) might lead to misunderstandings.
- Minor correction:  In Table 10, please correct "Stable Stable" to "Stable."
- A major concern with the proposed method is balancing human effort with the complexity of the introduced steps. While the pipeline can operate fully automatically, the large number of hyper-parameters may introduce significant uncertainty in practical applications. The reviewer appreciates the current approach, but simplifying the pipeline to reduce complexity while retaining the core concepts could be a valuable direction for future work.
- Additional experiments:
    - While Synthio shows promising performance, it would be interesting to investigate whether it has complementary or joint effects with other augmentation methods, such as random noise addition, pitch shifting, or other common techniques.
    - Further experiments could examine how changes in T2A models influence the effectiveness of the augmentation process. Specifically, it would be valuable to understand how the quality of T2A models affects the overall performance of the augmentation technique.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents Synthio, a synthetic data generation approach for improving audio classification models. Synthio leverages a pre-trained text-to-audio generation model, it first aligns the generations with acoustic preferences (obtained from a small dataset), then it leverages an LLM to synthetically generate captions for the generated audio. To further improve data quality and model performance, Synthio refines the dataset via rejection sampling. 
The authors evaluated their approach using different benchmarks while generating trainings sets of different sizes. The authors empirically demonstrated the proposed approach is superior to standard data augmentation techniques and to vanilla data generation.

### Strengths
1. Leveraging DPO to better align audio generation with real acoustics is a novel idea.
2. The whole data generation pipeline is an interesting idea, including the MixCap approach.
3. Under fine-tuning at small-scale regimes the proposed approach achieves significant improvement over the baseline methods.

### Weaknesses
1. Unfair comparisons to the evaluated baselines (more details below).
2. When increasing the number of generated samples the gap in performance between the proposed approach and no aug. at all is closing, very fast.

### Questions
As mentioned before, the proposed approach is interesting and novel (in the context of audio generation). However, I have several concerns about the evaluation process and presented results: 
1. The authors compare the proposed approach to several baseline methods including Gold-only (meaning no augmentations at all), and more traditional data augmentation techniques. Although the proposed method reaches significantly better results (especially under a small number of samples in D_test), it uses much more resources, meaning, the T2A model was trained on ~1.5M of audio samples. Hence, models trained with Synthio were introduced to more and diverse set of samples than just D_test, which were greatly influenced by the pre-training data of the T2A model. 
2. How many samples did you generate for each of the N samples on D_test in Table 1. This is another potential issue as the models trained with Synthio were also trained on more data (nxN) in comparison to standard augmentation techniques which were trained on N samples only. 
3. As I mentioned before, it seems the gap in performance is getting smaller very fast as we increase the size of D_test (especially compared to a model with no augmentations). This means that the proposed approach is beneficial for model fine-tuning under very low resource regimes (less than 500 samples). I advise the authors to put more emphasis on that in the paper and discussions. 
4. The authors additionally presented results for audio captioning. What text labels were used to both train and evaluate model performance considering both the proposed method and baselines? I'm asking as in the proposed approach text labels are much reacher, hence I'm not sure the comparison is fair. 

I'm willing to increase my score in case I missed something.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes a straightforward method: Given small scale audio classification task - use an existing audio generation model in this paper, a text-to-audio generator, to generate a lot of audio files similar to the smaller dataset and augment it with a factor of 1x to 5x samples to fine-tune an existing audio classification. The authors show the method outperforms their proposed baseline by (relative) 0.1-39%. The authors say that their contributions are,

 -- it is a novel approach for augmenting the small-scale dataset
--  their ability to generate novel, diverse, consistent data and its performance on tasks such as audio captioning.

In brief, this is a paper on audio classification on small-scale audio. The methodology is once the dataset is created == straightforwardly fine-tune the model.

### Strengths
== The paper has extensive experimentation that is far more than what was needed. It would have been much stronger if the authors focussed on a subset of these results with a sound, solid method. 

== The paper appears to be well-structured and written despite its flaws. 

== The data and code will be open-sourced, reproducible and easy to follow, which is a good point in favour of the paper. 

== A well-explained background on DPO, diffusion model, and RLHF. It should have included background for audio classification, zero-shot learning, etc. 

== The problem is interesting; exploring synthetic data to improve audio classification and pushing the performance is worth exploring.

### Weaknesses
The paper is being submitted to the topmost ML venue; hence, my comments are made accordingly to adhere to the highest quality of the paper. At the outset, the paper appears strong, but there are flaws that need to be addressed / claims that are not correct. Please do not carry out extra experiments to justify any other points and generate a new version of the paper. Please answer these points in 1-2 lines of text at maximum. 

1. The authors should drop a novel approach for audio classification as several papers exist that should be referenced. i) Open-Set Tagging Dataset (OST) Mark Cartwright, ii) BLAT Bootstrapping language-audio pertaining based audio set .... iii) Can synthetic audio from generative foundational models assist audio recognition ....iv) Synthetic training set generation using T2A models for environmental sound classification. There exist many more papers for audio generation tasks, which I do not include here, but the authors should have included them. These should be adequately referenced in the related work. If not, it gives a very false impression that the authors are the first ones to do it, including in the abstract.

2. The whole point of audio classification is robustness to unseen conditions and good performance for out-of-distribution data. DPO aligns generated data with the small dataset but fails to capture the variations that are needed in real life, as claimed by the author. The claim made by the authors, "T2A models trained on internet-scale data often generate audio that diverges from the characteristics of
small-scale datasets, resulting in distribution shifts.
These mismatches can include variations in spectral
(e.g., frequency content), perceptual (e.g., pitch, loud-
ness), harmonic, or other acoustic characteristics 2" is correct, but for audio classification, we do want to incorporate all of these variations. 


This is the point of training on a large corpus of datasets, such as an audio set, to include all the variations different from the training corpus. If I take very few examples and align a T2A model with DPO to the smaller dataset, it will generate samples in that small dataset distribution, as mentioned in all of the plots. This is shown precisely in Figure 3, and we do not want that. I would rather want a lot of diversity in pitch and spectral flux to make audio classification good in unseen cases rather than have the training data similar to my small corpus. 

There is a whole subfield on "out of distribution classification" = how to make models perform well when the classification dataset is not of the same distribution as that of the original training dataset. Whereas here, the authors are trying to do just the opposite and make the training corpus as close to the actual data using DPO, which is counter-intuitive to the field of how to build robust classifiers and get good classification accuracy out-of-distribution examples and data. 

3. Audiomentations has a list of 40 possible audio augmentations. The setup with n being 50-500 for ten categories would not be able to generate enough diverse augmentations. How do the authors report the numbers for it and carry it out? With N being at max 5, how would one incorporate it? Are all of the combinations not needed/not needed? how were they chosen? 

4. From Table 1, it does not appear that this paper was an academic paper. The comparisons do not include any benchmark reported by any other paper. The baselines are poorly reported and are not compared to any other paper. Even for data augmentation literature, there are papers that compare various techniques. 

5. Section 6.4 mentions that the scaling 4x is better than 5x. This appears strange as to why this would happen. The audio captioning section is definitely not needed for this paper and should ideally be dropped. 

6. The issue with alignment to the dataset is also the fact that there are categories that often overlap in FSD-50K, ESC-50, etc. What happens in that setup? In that case, the model is forced to generate one kind of audio sample/or prefer one over the other even though both have the same label. 

7. Accuracy mentioned in 6.5 is 0%. It is mentioned that the categories had the lowest frequencies in the dataset. This makes the claims in the paper shaky as it appears that the training was not normalized according to the category probabilities or sub-sampled/oversampled to make the training balanced.

### Questions
1. How would aligning the T2A model with the small dataset create the diversity of audio as exists in the real world as claimed in the Abstract as DPO would make it close to the samples chosen.  

2. Why was random mix augmentation not carried out in the Table 1 ? 

3. Was the performance boost mentioned in the abstract 0.1-39% relative or absolute. I could not find that in Table 1. Why were MAP metrics not report as is a standard practice for FSD-50K

4. Why are the characteristics like spectral flux and spectral flatness done globally as opposed to local behavior of NSynth and Urban Sound dataset. 

5. Are there any papers that have the experimental setup similar to the Table 1. Please cite a paper that fine-tunes such a small corpus in a similar setup. 

6. Why was the whole background on few-shot classification and zero shot audio classification not included. This is very similar to zero shot and few shot classification. The baselines should be included as well. Why should someone generated synthetic examples and not do few shot audio classification. What are the drawbacks of those methods. Why are the baselines not included with any of the previous works on synthetic dataset. n=50  is a few-shot setting, and it would be unfair not to include any literature or mention it anywhere in the paper. 

7. Why have the authors gone the T2A route. Taking an audio and writing a caption is an extremely lossy compression which will remove most of the information needed about the audio. what were the advantages of a T2A model that will be helpful for this problem. 

8. Why was the scaling factor limited to only 1x-5x scaling. What happens if I do 20x. It seems it might start overfitting ? The results in 6.4 are strange that it works with 4x scaling than 5x scaling. Either the models are not tuned properly or they are overfitting on smaller corpus.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed a pipeline to augment small-scale audio classification datasets with synthetic data and shows promising improvements.

### Strengths
1. The performance improvement when the data is in small scale (e.g., 50, 100, 200, 500) is pretty significant. 
2. The experimental setup is pretty complete and extensive.

### Weaknesses
1. The performance improvement with the proposed synthetic pipeline is limited. Despite the proposed augmentation showing quite significant improvement on the curated small dataset with a few hundred samples, it only shows marginal improvement on the full-scale dataset (Table 7). 
2. The proposed method is not practical. As we usually have data that is much larger than a few hundred samples (in this case, the proposed method does not work well), the traditionality of the proposed method is questionable. Also the proposed pipeline is much complex comparing with traitional augmentation method such as audiomentations, increasing the cost for model training. 
3. Heavy reliance on pretrained CLAP model. This reliance may bias the synthetic data as CLAP model. 
4. It is unclear what CLAP threshold is used in filtering and self-reflection. This is usually a tricky operation as the optimal threshold can vary with different types of sound. More explanations are welcomed.

### Questions
The result in Section 6.5 and Figure 5 is not convincing enough:
1. Line 516 “ We selected categories with the lowest frequency in the datasets”: 
The categories in the ESC-50 dataset have the same number of samples; how do you decide which category has a lower frequency?
2. Figure 5 shows only four classes to demonstrate the improvement of long-tailed categories. This is not convincing enough as those selected classes may represent only partial information. 

Table 2: Can you please explain what is “compositional diversity” and how it correlates with the CLAP score?
Line 214: DSmall -> D_{small}
Line 226 “no scalable methods”: Is it possible to estimate the loudness with the signal processing method?
Line 242 “fostering more diverse augmentation”: Any evidence for this claim?
Please double check the equation 8, 9, and 10 as the “x_0 : T” notation looks a bit confusing to me.
Line 318 “The CLAP model is pre-trained on Da-c and fine-tuned on Dsmall to adapt to the target datase”: Do you mean finetuning CLAP model on each of the dataset you used (ESC50, GTZAN, etc)? If so, how do you perform finetuing on such a small dataset, such as when n=50? Doesn’t that can cause overfiting?
Line 413: remove duplicated “the”
What dataset is utilized for the experiment in Table 5? Please specify. 
Line 503: What are the possible reasons why SpecAug does not scale well?

Please consider rewording the following sentence that is a bit confusing to read:
- “Abusing notation, we will also x0 as random variables for language”
- “We elaborate on these next”

### Soundness
3

### Presentation
3

### Contribution
2
