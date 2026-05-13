# SONICS: Synthetic Or Not - Identifying Counterfeit Songs

- Decision: Accept
- Scores: 6, 5, 6, 3

## Abstract
The recent surge in AI-generated songs presents exciting possibilities and challenges. While these inventions democratize music creation, they also necessitate the ability to distinguish between human-composed and synthetic songs to safeguard artistic integrity and protect human musical artistry. Existing research and datasets in fake song detection only focus on singing voice deepfake detection (SVDD), where the vocals are AI-generated but the instrumental music is sourced from real songs. However, these approaches are inadequate for detecting contemporary end-to-end artificial songs where all components (vocals, music, lyrics, and style) could be AI-generated. Additionally, existing datasets lack music-lyrics diversity, long-duration songs, and open-access fake songs. Furthermore, we highlight the importance of modeling long-range temporal dependencies in songs for effective authenticity detection, an aspect entirely overlooked in existing methods. To utilize long-range patterns, we introduce SpecTTTra, a novel architecture that significantly improves time and memory efficiency over conventional CNN and Transformer-based models. In particular, for long audio samples, our top-performing variant outperforms ViT by 8\% F1 score while being 38\% faster and using 26\% less memory. Additionally, in comparison with ConvNeXt, our model achieves 1\% gain in F1 score with 20\% boost in speed and 67\% reduction in memory usage. Other variants of our model family provide even better speed and memory efficiency with competitive performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presented a dataset for detecting AI generated music from well-known AI generated music services, Suno and Udio. The authors basically configured two group of music which are fake and real songs. For real songs, they retrieved 48,090 real songs from YouTube and for fake songs, they generated music from Suno and Udio. Finally, they trained a model for detecting whether the song is real or fake. To do this, SpecTTTra model is proposed. In this model, the authors proposed to use spectral and temporal patches (full-size in one dimension) to construct spectral and temporal tokens for their transformer-based classification model. The results showed that the proposed model is highly effective in detection. Also, the authors compared the model performance with Human performance.

### Strengths
Overall, the paper is well-written and easy-to-read, and the details of the proposed method, experimental design, the dataset, and the experimental results are well addressed. I think the following researchers will be easily follow and use the proposed dataset, and the models as the authors described them well.

### Weaknesses
It is good to see some research paper in the direction of detecting AI generated content in the domain of music. However, I think the paper lacks of analysis part. The scores that's shown in result tables seem to prove the effectiveness of the proposed method, however, without such in-depth analysis, the proposed dataset and the proposed method might not be useful in the future if the algorithms are updated. Therefore, I think having some analysis section would be beneficial for further future researches. (I think leaving some comments that is related to more high-level explanation on why the proposed model is detecting the AI generated content well, e.g. vocal characteristics, temporal/timbral characteristics, etc) At least, some additional case study on Appendix would be nice. For example, If some real song is detected as a fake, then try to give some analysis on why it's been detected as fake or vice versa.

### Questions
I think the title of the paper and the term real and fake are a bit too generalized terms. 
For example, the proposed dataset is about detection on Suno and Udio generated contents. (not counterfeit songs, maybe synthetic is okay) 
I think the authors can carefully suggest a better title.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a dataset of real and "fake" music recordings, where the fake recordings have been generated using commercial music generation systems. An attempt has been made to match some characteristics between the real and fake recordings. In addition, a new transformer architecture is proposed that is aimed at capturing longer-term temporal context in music audio classification. Finally, results on the fake vs. real music classification task are presented.

### Strengths
The introduction of a dataset for fake vs. real music classification is a welcome and very timely contribution. Different systems by two major commercial providers are considered and the dataset is separated in terms of different levels of fake (fully, mostly, half), which provides interesting insights - notably the half-fake songs with real lyrics seem to be easier to recognize. In the provided transformer architecture, I believe it makes a lot of sense to have one token per time step rather than several tokens for different frequency patches.

### Weaknesses
Unfortunately, the steps of the dataset preparation pipeline do not seem to be evaluated rigorously, which limits the usefulness of the resulting dataset. I am also not very convinced by the usefulness of the proposed spectral tokens.
Overall, because of these and some other issues (see "Questions"), I recommend to reject this paper, although this is a borderline recommendation.

Major questions/comments:
- Line 81f: "the fake songs in our dataset are free from copyright issues, as they are generated through paid subscriptions that provide a license to use and share the content legally" --- Given that the generation models used are very likely to have been trained on copyrighted data, how can you ensure that the fake songs in your dataset are free from copyright issues? What if generations are identical or similar to existing real music recordings - in particular, when real lyrics and styles are used for generation (cf. "half fake" subset).
- Several steps in the dataset preparation pipeline will probably produce very noisy or incorrect results, but their performance is never evaluated. This is concerning, given that the dataset is the main contribution of this paper. In particular:
  - How well does PyAnnotate work for vocal detection on this data (line 189)?
  - How accurate are the extracted song-styles? This, in particular, I would expect to work rather poorly. Vocal type classification from music audio, for example, is a hard problem.
  - How accurate are the transcribed lyrics?
  - In the cases were generated instead of transcribed lyrics were used: How often do these regurgitate the lyrics from real songs?
- In the proposed SpecTTTra model, I am unconvinced that the proposed spectral clips can provide very helpful information for long songs. The resulting spectral tokens would contain something similar to an average spectrum, which would not be very informative for real vs. fake classification. Indeed, increasing the number $f$ of spectral clips does not improve results in Table 4. However, this was not independently evaluated from the choice of $t$.
- Following up on the previous comment, it seems like results for the SpecTTTra-$α$ model are best, even though this utilizes the proposed architecture the least (low $f$ and $t$).

Minor questions/comments:
- In Table 1, consider adding "Total hours".
- Line 142f: "Meanwhile, long audio classification remains an uncharted area in audio research." --- This statement seems too strong and should be removed. A wide range of music audio classification tasks involve long audio classification, for example: genre classification, global key detection, global tempo estimation, etc.
- Line 211f: How was the list of topics for the full fake generation obtained? The list given in the appendix seems very biased. Is "matt damon vs jimmy kimmel" really a representative example of a topic for a real song?
- Line 288: Why were significantly more MF songs than HF or FF songs included?
- Line 471: What was the musical experience level of the human annotators? Did they have access to spectral analysis tools (which could be helpful for the fake vs. real classification task)?

Additional comments:
- Line 12: "these inventions democratize music creation" --- This is a highly questionable, opinionated slogan that has its place in marketing but not in science. It should be removed.
- Line 68 (and others): Please do not use the bibliography to refer to companies such as Suno or Udio. A company is not a scientific publication. Same, e.g., for wandb (line 392).
- Table 4: Consider clarifying in the caption what the positive and negative classes are (i.e. what is real and what is fake). Furthermore, indicate which algorithms are seen and unseen during training.

### Questions
Major questions/comments:
- Line 81f: "the fake songs in our dataset are free from copyright issues, as they are generated through paid subscriptions that provide a license to use and share the content legally" --- Given that the generation models used are very likely to have been trained on copyrighted data, how can you ensure that the fake songs in your dataset are free from copyright issues? What if generations are identical or similar to existing real music recordings - in particular, when real lyrics and styles are used for generation (cf. "half fake" subset).
- Several steps in the dataset preparation pipeline will probably produce very noisy or incorrect results, but their performance is never evaluated. This is concerning, given that the dataset is the main contribution of this paper. In particular:
  - How well does PyAnnotate work for vocal detection on this data (line 189)?
  - How accurate are the extracted song-styles? This, in particular, I would expect to work rather poorly. Vocal type classification from music audio, for example, is a hard problem.
  - How accurate are the transcribed lyrics?
  - In the cases were generated instead of transcribed lyrics were used: How often do these regurgitate the lyrics from real songs?
- In the proposed SpecTTTra model, I am unconvinced that the proposed spectral clips can provide very helpful information for long songs. The resulting spectral tokens would contain something similar to an average spectrum, which would not be very informative for real vs. fake classification. Indeed, increasing the number $f$ of spectral clips does not improve results in Table 4. However, this was not independently evaluated from the choice of $t$.
- Following up on the previous comment, it seems like results for the SpecTTTra-$\alpha$ model are best, even though this utilizes the proposed architecture the least (low $f$ and $t$). 

Minor questions/comments:
- In Table 1, consider adding "Total hours".
- Line 142f: "Meanwhile, long audio classification remains an uncharted area in audio research." --- This statement seems too strong and should be removed. A wide range of music audio classification tasks involve long audio classification, for example: genre classification, global key detection, global tempo estimation, etc.
- Line 211f: How was the list of topics for the full fake generation obtained? The list given in the appendix seems very biased. Is "matt damon vs jimmy kimmel" really a representative example of a topic for a real song?
- Line 288: Why were significantly more MF songs than HF or FF songs included?
- Line 471: What was the musical experience level of the human annotators? Did they have access to spectral analysis tools (which could be helpful for the fake vs. real classification task)?

Additional comments:
- Line 12: "these inventions democratize music creation" --- This is a highly questionable, opinionated slogan that has its place in marketing but not in science. It should be removed.
- Line 68 (and others): Please do not use the bibliography to refer to companies such as Suno or Udio. A company is not a scientific publication. Same, e.g., for wandb (line 392).
- Table 4: Consider clarifying in the caption what the positive and negative classes are (i.e. what is real and what is fake). Furthermore, indicate which algorithms are seen and unseen during training.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces SONICS (Synthetic Or Not - Identifying Counterfeit Songs), featuring the largest synthetic song dataset to date with over 97,000 songs (4,751 hours), including 49,074 AI-generated songs from Suno and Udio platforms. SONICS includes end-to-end generated content with both music and lyrics, and features longer duration songs (averaging 176 seconds). To effectively detect these synthetic songs, the authors propose SpecTTTra (Spectro-Temporal Tokens Transformer), a novel architecture specifically designed for capturing long-range patterns in music. This new model demonstrates superior efficiency compared to traditional approaches, running 38% faster than ViT while using 26% less memory and achieving better detection performance, particularly with longer audio samples. This work provides essential tools for detecting AI-generated music as these technologies become increasingly sophisticated and widespread.

### Strengths
- The paper presents a clear and reproducible workflow for synthetic song generation, with detailed documentation of the prompt engineering process, generation parameters, and data processing steps. 
- The generated song dataset can be an important addition to SVS and SVDD community.
- The Spectro-Temporal tokenizer uses a simple but seemingly effective way to capture the long-range information.

### Weaknesses
 - The paper lacks sample demonstrations of the generated synthetic songs for evaluation. Without access to audio examples, it is difficult for reviewers and readers to assess the quality and diversity of the generated content, as well as validate the claims about different types of synthetic artifacts (e.g., "Karaoke effect"). The authors should provide a representative set of samples across different generation categories (Full Fake, Half Fake, Mostly Fake) and generation platforms (Suno, Udio).
- The naming "SpecTTTra" (Spectro-Temporal Tokens Transformer) is potentially misleading as the architecture only employs a transformer encoder component rather than a full transformer architecture. Furthermore, while the model claims to better capture long-range dependencies, the paper lacks ablation studies to demonstrate this capability. The authors should provide specific experiments showing how the separate temporal and spectral tokenization contributes to capturing long-range patterns in music.
- The performance improvements over baseline models, particularly ConvNeXt, are modest given similar computational costs. The F1 score gain of 1% with 20% speed improvement doesn't strongly justify the introduction of a new architecture. The authors should either provide additional experiments demonstrating clear advantages of SpecTTTra (e.g., ablation studies, analysis of captured patterns), or consider separating the dataset contribution from the model architecture into two papers.
- The quotation mark is used incorrectly.

### Questions
- Could the authors provide a representative set of audio samples from different categories (Full Fake, Half Fake, Mostly Fake) and platforms (Suno, Udio)?
- What quality control measures were used to ensure the generated songs are suitable for the dataset?
- Could the authors provide ablation studies demonstrating how the separate temporal and spectral tokenization contributes to capturing long-range patterns?
- What was the rationale behind the specific clip sizes chosen for the three variants (α, β, γ)? And how sensitive is the model performance to these hyperparameters?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces SONICS, a large-scale dataset designed for end-to-end synthetic song detection, addressing the limitations of existing datasets such as lack of musical diversity, short song durations, and absence of fully AI-generated music. They also propose a novel model, SpecTTTra, which excels in capturing long-range temporal dependencies within songs, outperforming current models in terms of speed and memory efficiency. The paper establishes both human and AI benchmarks to advance research in distinguishing AI-generated music, thereby protecting artistic integrity.

### Strengths
The paper presents three data acquisition pipelines for fake songs, significantly expanding the dataset for synthetic song detection and providing valuable reference for peers looking to augment this dataset. The paper also introduces a new model for synthetic song detection that achieves better detection results while reducing training costs, offering a new reference method for the field.

### Weaknesses
1. The data collection for fake songs is not comprehensive, leading to potential biases. Only songs generated by Suno and Udio were collected, while other AI music generation tools such as SeedMusic and SkyMusic exist in the market.
2. Music generated by AI tools from the same company tends to have a consistent style. The authors need to demonstrate how they can distinguish between real and fake songs, rather than just identifying the music styles of Suno and Udio. Suno and Udio's song styles are concentrated in certain genres that, while present in real-world music, are less common. For instance, if the model achieves an 80% accuracy rate, it might mean that 20% of the ground truth song collection consists of pop and rock styles generated by Suno and Udio, while the remaining 80% are styles rarely generated by these tools. Thus, the model might be performing genre classification rather than accurately distinguishing between real and fake songs.
   I suggest that to reduce this interference and truly identify AI and non-AI differences, rather than stylistic differences, the authors could introduce songs generated by other AI tools, different from the training data, as a test set. For example, if the model is trained to distinguish between real and fake songs using data from Suno and Udio, it could be tested with songs generated by SkyMusic, SeedMusic, and other models. If the model can still identify songs from SkyMusic and SeedMusic as fake, it would demonstrate the model's effectiveness.
3. The authors need to prove that they are identifying real songs versus fake songs, not just differences in audio quality. The dataset includes real songs and AI-generated songs. Real songs are sourced from YouTube, where the sampling rate is generally higher and the audio quality is better. In contrast, AI-generated songs mentioned in the paper have a sampling rate of 16kHz/32kHz, which is of poorer quality, and even if upscaled to match YouTube's quality, there would be significant loss in the high-frequency spectrum.
   The paper does not explore or explain this aspect, nor does it mention whether the audio quality was normalized before training and testing. It is unclear whether the model has truly learned to distinguish AI-generated songs or if it has been judging audio quality.

   Whether it's distinguishing between 16kHz resolution songs and high-resolution songs or differentiating between up-sampled 16kHz songs and original high-resolution songs, it's clear that these are audio quality tasks, not real song vs fake song recognition tasks. Only by reducing all to the same low-quality audio can the bias of audio quality on the model be avoided.
4. The experimental tables in the paper do not indicate which metrics are the best, making it difficult to intuitively compare the effectiveness from the table.
5. There is a lack of Ablation Study to show the model's performance using only Spectral or Temporal information.
6. There is no experimental comparison with other models and methods used in Synthetic Song Detection papers.

### Questions
1. The dataset's limited scope to Suno and Udio-generated songs may introduce bias, overlooking other AI music tools like SeedMusic and SkyMusic.
2. The model's high accuracy might reflect genre classification rather than distinguishing real from fake songs due to the focused style of Suno and Udio.
3. The study lacks evidence to confirm the model's ability to identify fake songs independently of audio quality differences.
4. The paper's experimental tables fail to highlight the best-performing metrics, hindering clear comparison.
5. An Ablation Study is missing to assess the model's reliance on Spectral or Temporal information alone.
6. The paper does not compare the model's performance with other methods from the Synthetic Song Detection literature.

### Soundness
2

### Presentation
2

### Contribution
3
