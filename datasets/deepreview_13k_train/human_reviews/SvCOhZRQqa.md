# Token Pruning Meets Audio: Investigating Unique Behaviors in Vision Transformer-Based Audio Classification

- Decision: Accept
- Scores: 6, 6, 5, 5, 6

## Abstract
Vision Transformers (ViTs) have achieved state-of-the-art performance across various computer vision tasks. To reduce the high computational cost of ViTs, token pruning has been proposed to selectively remove tokens that are not crucial. While effective in vision tasks by discarding non-object regions, applying this technique to audio tasks presents unique challenges. In audio processing, distinguishing relevant from non-relevant regions is less straightforward. In this study, we applied token pruning to a ViT-based audio classification model using Mel-spectrograms and analyzed the trade-offs between model performance and computational cost. We show AudioMAE-TopK model can reduce MAC operations by $2\times$ with less than a 1\% decrease in accuracy for both speech command recognition and environmental sound classification. Notably, while many tokens from signal (high-intensity) regions were pruned, tokens from background (low-intensity) regions were frequently retained, indicating the model’s reliance on these regions. In the ablation study, forcing the model to focus only on signal (high-intensity) regions led to lower accuracy, suggesting that background (low-intensity) regions contain unique, irreplaceable information for AudioMAE. In Addition, we find that when token pruning is applied, the supervised pre-trained AST model emphasizes tokens from signal regions more than AudioMAE.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
In this paper authors propose to prune blocks from the ViT when processing audio mel-spec data thus improving the computational efficiency without too much effect on the performance.

### Strengths
Potentially useful way to process large audio corpora with this setup. ViT is useful in when first considering mel-spec as an image and then progressing as it would be an image. So the complete ViT pipeline for images would be applicable. Removing unnecessary blocks is reasonable as not every pixel in mel-spec is useful. 

Extensive ablation tests on the proposed method are clearly a positive side of this work.

### Weaknesses
 - Empirical comparisons to other published works is the main problem in this work. Authors do explain multiple different ways to improve computational efficiency (for images) and also for audio all using ViT framework as far as I can decode.

- Reading the title I was expecting to see something where peculiarities of spectrogram (or mel-spec as it is compressed spectrogram) would be utilized to improve the pruning. But I really do not see anything of the sort, I hope authors can clarify this in the rebuttal stage. it is noteworthy that even though spectrogram is an image it is a very structured image, y-axis refers to frequency and x-axis refers to time, so for example in speech processing only a slice of the spectrogram would contain useful content. And in detail, speech spectrograms have a peculiar stucture of with harmonic and non-harmonic portions (such as 'a' has harmonics, whereas 's' not so much).

### Questions
-

### Soundness
3

### Presentation
3

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
This paper investigates the application of token pruning in Vision Transformer (ViT)-based audio classification, a novel approach given that token pruning has predominantly been explored in image classification. The authors propose the Mean-Pooling EViT (MP-EViT) model, which applies token pruning to audio data represented as Mel-spectrograms. Their model successfully reduces computational costs—specifically, the multiply-accumulate operations (MACs)—by approximately 50%, while maintaining a high level of accuracy with only a minor loss (<1%) in performance. The authors demonstrate that, unlike in vision tasks where background tokens are frequently pruned, audio classification tasks require a more nuanced approach as both signal (high-intensity) and background (low-intensity) regions contribute significantly to classification accuracy. The paper’s contribution is the adaptation of token pruning techniques for audio tasks, providing insights into the behavior of ViT models in audio classification and highlighting the importance of background regions in this domain.

### Strengths
1.Originality:
This paper presents an innovative application of token pruning within Vision Transformer (ViT)-based audio classification, specifically utilizing Mel-spectrograms as input data. While token pruning has been extensively explored in vision tasks, its application to audio tasks is relatively novel, providing new insights into how ViT models can handle non-visual data.
2.Quality:
The research is methodologically robust, supported by thorough experimental setups and well-designed ablation studies. 
3.Clarity:
The paper is clearly structured, with each section building upon the previous one to ensure that the readers can follow the motivations, methods, and analyses without ambiguity. 
4.Significance:
By extending token pruning to audio classification, this paper contributes to the broader research community by highlighting the potential of ViT models in diverse non-visual domains. The findings regarding the significant role of background tokens in audio classification provide a valuable perspective that may influence future research on feature importance within various data types.

### Weaknesses
1.Limited Generalization Across Audio Tasks:
The experiments focus primarily on speech command recognition and environmental sound classification, which may limit the generalizability of the MP-EViT model to other types of audio classification tasks, such as speaker identification, music genre classification, or emotion recognition. The current evaluation does not explore the model's performance on tasks with different acoustic characteristics or temporal dynamics, which could reveal limitations in its token pruning strategy. For instance, speaker identification relies heavily on subtle variations in voice timbre, while music genre classification involves complex harmonic and rhythmic patterns. It is unclear how MP-EViT would perform in these contexts, where the importance of different spectral and temporal regions might vary significantly compared to the tasks studied.
2.Lack of Comparative Baselines:
While the paper compares the proposed MP-EViT model against the baseline without token pruning, it lacks comparisons with other state-of-the-art models or alternative token pruning methods adapted for audio tasks. For example, methods like DynamicViT and SPViT, which use prediction-based token pruning, could serve as useful comparisons to understand the relative benefits and limitations of the mean-pooling approach used here. This absence makes it difficult to assess whether the observed performance gains are specific to the proposed method or if similar results could be achieved with other pruning techniques. Furthermore, the lack of comparison with other pruning methods makes it difficult to determine if the mean-pooling approach is optimal for audio data, or if other methods might be more effective at identifying and removing less important tokens.

### Questions
1.Generalizability of MP-EViT:
Could the authors elaborate on the potential limitations of applying MP-EViT to other audio classification tasks beyond speech command recognition and environmental sound classification? Have they considered tasks like speaker identification or music genre classification, which may involve different types of audio features? Expanding the evaluation to these tasks would provide a clearer picture of MP-EViT’s adaptability and robustness.
2.Comparative Baselines:
MP-EViT is evaluated mainly against a non-pruned baseline. Could the authors include comparisons with other token pruning methods adapted for audio, to give readers a broader context of the model’s performance? This would highlight MP-EViT’s unique advantages and any areas where other pruning methods may outperform it.

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
The authors applied a token pruning method originally used in vision tasks to audio classification, successfully reducing MAC operations and improving throughput with minimal accuracy loss. While the experiments were limited to only two datasets (SPC-2 and ESC-50), making the scope somewhat narrow, the detailed analysis provided valuable insights.

### Strengths
I think the strength of the paper lies in its discussion and ablation studies.

Until Section 3.4, I thought it was merely applying a pruning method in ViT directly to audio classification, which, in my opinion, makes the contribution fall below the ICLR bar. However, the discussion and ablation study that follow are much more interesting than the proposed pruning method. I am a bit surprised that "background" patches are attended. So it brings some new knowledge to me.

### Weaknesses
There are a few major flaws:

1- Audio MAE is a special Transformer model that is trained with Masked Data Modeling, i.e., it learns to attend to minimal patches by design. Thus, the conclusion of this paper is conditioned on a special MAE model, or the general Transformer model is questionable. This is a fatal issue and needs to be either clarified or experiments added on Transformers trained without MAE (e.g., the original AST). I cannot recommend acceptance without fixing this.

2- The pruning method is almost the same as the vision version, which is not novel enough.

3- The discussion is interesting, but for non-trivial conclusions, we also need to be careful. Why -0.65 (is that dB?) is a good measure of signal and background? If I remember correctly, speech commands are mostly clean speech, so the low intensity might be just some consonants / vowel transitions. Also, it is just 10-32 keywords classification; the model does not need to attend to everything (in contrast, doing large vocab ASR needs). So, more fine-tuning datasets are also needed.

### Questions
See in weakness.

### Soundness
2

### Presentation
2

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
The paper propose token pruning in Vision transformers fed with spectrograms for audio based classification tasks. Authors prune tokens which are least attended by the other tokens. The paper shows that token pruning can lead to less computation with very minimal drop in accuracy. Authors further show that unlike vision, for audio tasks background tokens are also being retained thereby showing their importance for such tasks.

### Strengths
The paper presents a novel application of token pruning techniques by applying them in audio classifications tasks. The presentation of this paper is clear and it is easy to read. Authors also provide various analysis providing insights on the nature of token pruning for such tasks showing that background tokens can also be important for audio tasks. Moreover, on the two datasets considered in the paper, authors show almost no drop in accuracy while reducing MAC operations significantly.

### Weaknesses
1. ViTs are very data hungry. The size of datasets considered is not that huge. This combined with high accuracy values in Table 1 could indicate model may be over-fitting to tasks or datasets at hand. Have authors tried to train the model on a bigger dataset e.g. Audioset and then evaluate its performance on other audio classification tasks such as the two mentioned in paper (SPC-v2 and ESC-50). Authors should show better generalizability of their proposed approach to make their claims stronger.

 2. The proposed approach reduces tokens from one layer to next similar to downsampling. Have the authors compared their proposed approach with other operations such as averaging blocks of n-tokens, uniform downsampling, downsampling by picking tokens randomly to name a few.

 3. Showing similar experiments with AST instead of audio-MAE can help give us an idea of generalizability of this method across different architectures. Also, since audio MAE uses mean pooling, it is kind of intuitive that CLS-EViT will work worse than MP-EViT. A better comparison would be against CLS-EViT of AST (since AST uses CLS token for classification) and MP-EViT of Audi-MAE

### Questions
In the experiments, authors have used token pruning at layers 4, 7 and 10. Why were these three layers chosen? What is the effect of token pruning at every layer on the tasks at hand i.e. can too much pruning be harmful for the tasks at hand?

### Soundness
3

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
4

### Summary
The authors propose the MP-EViT model, which is the first time the token pruning technique is applied to the Vision Transformer-based audio classification task. A comprehensive experimental analysis reveals the unique token pruning patterns in audio classification, proves the importance of background tokens, and significantly reduces the amount of computation while maintaining high accuracy.

### Strengths
1. For the first time, token pruning is applied to the audio classification task, and its unique behavioral patterns are deeply analyzed. This opens up a new research direction for the efficient application of ViT in the audio domain.

2. This study provides an important efficiency optimization scheme for the application of ViT in the audio domain, and reveals the unique characteristics of audio data processing, which is of great significance in promoting the development of audio AI.

3. The authors demonstrate through a large number of ablation experiments that what token pruning focuses on in the speech domain is dramatically different from that in the image domain, and analyze the reasons for this.

### Weaknesses
1. The experimental dataset and model scale are relatively limited. The study utilized only the SPC-2 and ESC-50 datasets, and the ViT-B configuration was exclusively employed. Expanding the experimental scope could provide more comprehensive insights. It is recommended to conduct experiments on additional audio classification tasks, such as emotion recognition and speaker identification, to validate the generalizability of the proposed method. The limited dataset choice restricts the conclusions that can be drawn about the robustness of the proposed token pruning approach across diverse audio characteristics and task complexities. Furthermore, the exclusive use of the ViT-B configuration leaves open questions about how the pruning strategy would perform with smaller or larger models, potentially impacting the practical applicability of the method.

2. There is a lack of comparison with other audio classification methods. The manuscript primarily compares the proposed method with baseline models, without assessing performance against other state-of-the-art audio classification techniques. This omission makes it difficult to comprehensively evaluate the advantages of the proposed approach. Has consideration been given to comparing token pruning with other model compression techniques, such as knowledge distillation and quantization?

3. The explanation of the mechanism for retaining background tokens is insufficiently detailed. While experiments demonstrate the significance of background tokens, the analysis of the underlying mechanisms that lead the model to preferentially retain these tokens is not adequately explored. The manuscript does not delve into the specific features or patterns within the background tokens that contribute to the model's performance. A more detailed analysis, perhaps involving visualization or feature analysis, is needed to understand why these tokens are important.

4. The manuscript mentions that due to resource constraints, only the ViT-B configuration was employed. Could supplementary small-scale experiments be conducted to investigate the impact of model capacity on the pruning strategy?

5. Is it possible to extend the use of mel spectrograms to magnitude spectrograms? This is particularly relevant, as magnitude spectrograms are more widely utilized in the field of speech processing.

### Questions
The contents are the same as Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
