# A Joint Spectro-Temporal Relational Thinking Based Acoustic Modeling Framework

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 3, 6

## Abstract
Relational thinking refers to the inherent ability of humans to form mental impressions about relations between sensory signals and prior knowledge, and subsequently incorporate them into their model of their world. Despite the crucial role relational thinking plays in human understanding of speech, it has yet to be leveraged in any artificial speech recognition systems. Recently, there have been some attempts to correct this oversight, but these have been limited to coarse utterance-level models that operate exclusively in the time domain. In an attempt to narrow the gap between artificial systems and human abilities, this paper presents a novel spectro-temporal relational thinking based acoustic modeling framework. Specifically, it first generates numerous probabilistic graphs to model the relationships among speech segments across both time and frequency domains. The relational information rooted in every pair of nodes within these graphs is then aggregated and embedded into latent representations that can be utilized by downstream tasks.
Models built upon this framework outperform state-of-the-art systems with a 7.82\% improvement in phoneme recognition tasks over the TIMIT dataset. In-depth analyses further reveal that our proposed relational thinking modeling mainly improves the model's ability to recognize vowels, which are the most likely to be confused by phoneme recognizers.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper describes an approach to representing smoothed spectrograms using a graph formulation where features are computed from pairwise interactions between spectrogram chunks. These features are then used for phoneme classification in TIMIT, where they show good performance, achieving 9.2% phoneme error rate on the TIMIT test set.

### Strengths
The experiments seem to show that the approach works well.

### Weaknesses
This paper was very difficult to read and understand. It uses many words with very suggestive connotations like "Thinking" in the title, "unconscious", "mental impressions", etc. without the necessary strong justification for invoking them in the setting of a machine learning paper. These words obscure what is actually going on in the approach and are not necessary.

The task of phoneme classification on TIMIT is very old and is a reasonable first step in demonstrating the promise of an approach, but is definitely not sufficient to show that a model is learning a reasonable representation. Additionally, while the proposed system's results are good on the task (9.2% PER on the test set from Table 2), the reported wav2vec 2.0 baseline numbers (9.98% PER on the test set) are not the numbers that are reported in that paper (8.3% PER on the test set). It is not clear where the 9.98% number comes from.

Figure 5 visualizes four relational graphs that show hard to interpret spectrogram pieces without axis labels conected by lines of varying weights. It is not clear which weights we should expect to be strong or weak, although some are strong and some are weak.

There is also an analysis of the proportion of frames in which each phoneme is predicted in figure 6, showing that the proposed system predicts phonemes with closer proportions to the ground truth than the baseline system of wav2vec 2.0, although it does not show error rates or accuracies for these predictions. It is not clear which phonemes are more accurately predicted, just which ones are more frequently predicted.

There are 13 pages of appendices and reading through all of it still does not explain all of the necessary details like explicitly stating the loss that is optimized.

### Questions
Where do the numbers in table 2 for wav2vec 2.0 come from?

What is the loss that is actually optimized and what parameters are adjusted to optimize that loss?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors present a  spectrotemporal relational thinking-based framework for acoustic modeling. The proposed framework improves upon the original relational thinking-based frame by extending the probabilistic graph modeling from the temporal domain to the frequency-temporal domain. The paper reports a 7.82% improvement in phoneme recognition over the state-of-the-art for TIMIT phoneme recognition task.

### Strengths
- Biological Inspiration and Acoustic Modeling: The exploration of biologically-inspired algorithms, such as relational thinking, in acoustic modeling is noteworthy. Given humans' inherent ability to process audio signals across both frequency and temporal domains, the extension of the original relational thinking network to a temporal-frequency domain seems  reasonable.

- Promising Results on TIMIT: Experimental results on the TIMIT dataset, though small, show promise against various baselines. Additionally, the detailed analysis and visualization of the generated graph and its relationship with different phoneme categories provide valuable insights.

### Weaknesses
 - Incremental Technical Contribution: The technical developments in this work appear to be an incremental advancement from Huang et al. (2020). The main modification is the extension of the input from one dimension to two dimensions, followed by a direct application of the relational thinking network proposed by Huang et al.

- Dataset Limitations: The experiments rely heavily on the TIMIT dataset, which is relatively small in size. To firmly establish the proposed method's efficacy and robustness, it is imperative to test it on larger, more diverse datasets and under complex conditions.

### Questions
See weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposed to use relational thinking-based acoustic model to learn the spectro-temporal correlation for automtic speech recognition task. Specficially, the proposed method is applied on the speech features extracted by a pre-trained wav2vec module. In the experiment, two tasks are performed including phenome recognition and automatic speech recognition. The results show the performance gain compared to these baseline systems.  These baseline systems are mostly the pre-training based methods which output the speech features.

### Strengths
The paper attempts to solve a valuable problem for acoustic modeling. The motivation of the work is clear and reasonable.

### Weaknesses
1, The innovation is not clear. The paper claims their innovation of using relational thinking based modeling method on spectro-temporal domain for acoustic modeling. However, from the description in the paper, there is no distinction between relational thinking based modeling and self-attention based modeling. For example, with several self-attention modeling layers stacked, it's equivalent to the so called relational thinking based model that pair-wised relation will be learnt among the transformed forms of each node (each time step), rather than the single step embedding. Therefore, theoretically, there is no difference between self-attention and relational thinking based method. The paper does not adequately explain how the proposed relational thinking mechanism differs fundamentally from the established self-attention mechanism in terms of the learned representations and the underlying mathematical operations. Specifically, it is unclear whether the relational thinking model truly captures higher-order relationships beyond what can be achieved with stacked self-attention layers, which also learn pairwise relationships, albeit through different parameterizations. The claim that relational thinking is inherently different needs more rigorous justification, including a detailed mathematical comparison of the two approaches.
2, The experiment part is not complete. In order to demonstrate the superiority of the proposed relational thinking based method compared to the self-attention based method, the results of the self-attention should be included as one of the baseline results. However, the results of the paper only includes these feature extraction based method without extra modeling. In addition, the paper should also list the model size of each compared method to have a more fair comparision. The experimental section lacks a direct comparison with a self-attention based model that uses a similar architecture to the proposed method, but replaces the relational thinking module with a self-attention module. This is crucial to isolate the contribution of the relational thinking component. Furthermore, the paper should provide a detailed breakdown of the model sizes, including the number of parameters for each layer, not just the total number, to allow for a more granular analysis of the computational cost and efficiency of the proposed method. Without this, it's difficult to assess whether the performance gains justify the added complexity.
3, The tradeoff study between temporal context and spectral context is not able to lead such conclusion that higher frequency domain resolution provideds more benefits compared higher time domain resolution, as the results of these two setting are very close in the test set (20.80 vs. 20.66). The conclusion drawn from the trade-off study between temporal and spectral context is not sufficiently supported by the experimental results. The performance difference between the two settings (20.80 vs. 20.66) is marginal and does not provide a strong basis for claiming the superiority of higher frequency resolution. A more comprehensive analysis with a wider range of resolution settings and a statistical significance test is needed to validate this claim. The current results could be due to random variation or other confounding factors.

### Questions
1, Have you  done such experiment that replace the relational thinking based model with Transfomer/Conformer type of module? If so, what is the performance?
2, Could you please explain why the proposed method cannot perform well in non-vower recognition?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates injection of relational thinking on the frame-level phoneme recegnition task on TIMIT. The main proposal of the paper is that instead of focusing on time-only or frequency-only relations between consecutive frames, they should be jointly modeled. The acoustic model uses wav2vec2 features from audio and concatenates them with the features extracted from the relational thinking based graph embeddings before applying a classification layer. The model parameters are trained using a variational lower bound based approach. Experimental results show that joint time-frequency relations are important and the proposed method can outperform the wav2vec2 based baseline in phone recognition task on TIMIT. Analysis of the results show that the model is more effective on vowels as compared to the consonants.

### Strengths
- Originality:

1. The joint modeling of time-frequency seems to be effective on the phoneme recognition task. Additional analyses on the learned graphs show that the model can learn the vowel patterns more consistently. 

2. It is nice to see the parallelism between human perception of vowels and the model’s results. 

- Quality:
1. The paper has shown the model's effectiveness on the TIMIT task. The paper investigated various aspects of the model and design choices (even though they are sometimes limited). 

- Clarity:
Clearly written

- Significance: 
1. Even though the acoustic and graph embedding combination is performed in a rather straightforward way, the formulation of the learning objective can provide an opportunity for further extensions of the graph parameters.

### Weaknesses
1. More parameter settings and comparisons could have been investigated to strengthen the conclusions from the results. Specifically, the paper lacks a thorough exploration of the window size ($w$) used for constructing the feature map $\mathbf{C}_t$, and the number of temporal and spectral dimensions ($d^{(t)}$ and $d^{(f)}$) for the relational graphs. The impact of these parameters on the model performance is not analyzed, which could lead to a better understanding of the model's behavior. For example, a grid search over different values of $w$, $d^{(t)}$, and $d^{(f)}$ could provide more robust conclusions about the effectiveness of the proposed approach. Furthermore, the paper could benefit from a comparison with other graph-based methods for phoneme recognition, which would help to contextualize the contribution of the proposed method.
2. Some additional analysis of the results could have been useful. For instance, the paper mentions that the model is more effective on vowels compared to consonants, but it does not provide a detailed analysis of why this is the case. A more in-depth investigation of the model's performance on specific phoneme classes, and a confusion matrix analysis, could provide a better understanding of the model's strengths and weaknesses. Also, it would be beneficial to analyze the learned graph embeddings to see if they capture any meaningful phonetic relationships. Visualizing the graph embeddings or performing some clustering analysis could help to interpret the learned representations.

### Questions
1. Are the baselines trained with cross-entropy objective?

2. Would it make sense to Impose left to right constraint between the time steps for causality?

3. PER Analysis at the speaker level may give further intuition on how the model performs as compared to human perceptions.

4. It would be good to see Fig.5 repeated with t1f8 and t8f1 models.

5. Does feature mapping (Eq. 1) involve mixing of features within frequency bins? Is $  \Lambda $ diagonal or not? 

6. Have you considered other types of spectra-temporal features for comparison? One example could be from, https://engineering.jhu.edu/lcap/data/uploads/pdfs/interspeech2012_carlin.pdf

7. Have you considered a comparison between spectro-temporal HMM based recognition and the proposed approach?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
