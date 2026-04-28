# Unsupervised ASR via Cross-Lingual Pseudo-Labeling

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 3, 6, 6

## Abstract
Recent work has shown that it is possible to train an \emph{unsupervised} automatic speech recognition (ASR) system using only unpaired audio and text. Existing unsupervised ASR methods assume that no labeled data can be used for training. 
We argue that even if one does not have any labeled audio for a given language, there is \emph{always} labeled data available for other languages. We show that it is possible to use character-level acoustic models (AMs) from other languages to bootstrap an \emph{unsupervised} AM in a new language. Here, ``unsupervised'' means no labeled audio is available for the \emph{target} language. Our approach is based on two key ingredients: (i) generating pseudo-labels (PLs) of the \emph{target} language using some \emph{other} language AM and (ii) constraining these PLs with a \emph{target language model}. Our approach is effective on Common Voice: e.g. transfer of English AM to Swahili achieves 18\% WER. It also outperforms character-based wav2vec-U 2.0 by 15\% absolute WER on LJSpeech with 800h of labeled German data instead of 60k hours of unlabeled English data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, the authors propose a cross-lingual unsupervised ASR training framework built on top of the iterative pseudo labeling (IPL) method. They assume a practical situation where unpaired audio and text is available for some low-resource languages and the proposed method is designed to leverage existing source AM (obtained from supervised training on a source language) to generate pseudo labels for the target audio under the regulation of the target LM. The resulting target AM is then iteratively trained on the pseudo labels. Experiments are designed to explore different combination of target & source languages, impact of data size etc. The results demonstrate the effectiveness of the proposed method.

### Strengths
1. The design of the experiment is comprehensive. The source & target language set covers not just common European languages but also the less common Arican languages such that the cross-family source & target language situation can also be studied.
2. Comparison with baseline systems such as supervised training and wav2vec-U 2.0 shows that the proposed method is effective in training an ASR model in unsupervised way.

### Weaknesses
1. The contribution of this work is limited in cross-lingual scenarios.
2. Baseline system setting is relatively limited. In the core validation experiments (section 5.2), the baseline is only zero-shot evaluation w/ and w/o target LM plus the fully supervised training. It would be more informative if other unsupervised training methods can be compared side-by-side.
3. The paper does not demonstrate sufficient novelty. The author sets an assumption: the target language has no labelled speech accessible but has a fair amount of text data to train an LM. The paper reports how an existing IPL method works under this assumption.

### Questions
Question:
1. The LMs seem to be trained and fixed for experiments. Have you tested the correlation between the LM's PPL VS. final WERs?

Suggestion:
1. Please check and fix typos (e.g. section 5.2: "any Indo-European language, any Indo-European language")
2. Please give pointers to the tables/figures in line. E.g. in section 5.5 "the results below" doesn't correctly point to the corresponding table.

### Soundness
3 good

### Presentation
3 good

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
This paper tackles multilingual ASR, especially for dealing with unsupervised training in target languages given source languages' ASR systems trained on supervised source data. The idea is simple but powerful. The method uses PL techniques but extends it for a transfer learning scenario from source to target languages. The paper investigates this transfer learning capability with various dimensions (e.g., across the language, across the language family, variants of PL methods, amount of labeled source data and unlabelled target data, the use of LMs, etc.). With these investigations, the method finally achieved sufficient performance in some language pairs. Although most languages are based on the standard Latin scripts, the paper also shows the potential of applying this method to target languages with unseen scripts with the help of a transliteration technique.

### Strengths
- Multilingual ASR is an important research topic to bridge the digital divide in underrepresented regions.
- The proposed method does not require labeled data for the target languages
- Intensive analyses of the proposed methods with various dimensions

### Weaknesses
 - Although the topic is very important, the technique itself does not have sufficient novelty as an ML conference paper. The topic is specific to ASR, and the technique is based on one particular ASR method (i.e., CTC). The connection to general ML problems is not clear.
  - for example, some experimental results (e.g., the use of n-gram LMs, etc.) are specific to CTC, and it does not seem to be generalized to the other architectures.
- Most experimental findings are expected, and there are not so many new findings (e.g., it's a bit trivial that large data help the performance, etc.).
- The methodology is not very new. Although there are several differences, some prior studies try to transcribe unseen languages with seen language ASR systems (e.g., Hasegawa-Johnson, Mark A., et al. "ASR for under-resourced languages from probabilistic transcription." IEEE/ACM Transactions on Audio, Speech, and Language Processing 25.1 (2016): 50-63.). The core idea of using a source language model to generate pseudo-labels for a target language is not novel, and the paper does not sufficiently highlight the differences from existing approaches. The use of self-training, while a core component, is not a new concept in itself, and the paper does not provide a strong justification for its specific application in this context.


### Questions
- Did you use SSLs? Since SSLs are obtained by unsupervised training, combining this method and SSL would be very powerful.
- Can you explain why this method uses CTC? Is there a particular reason, or is this method applicable to the other methods (e.g., HMM, attention-based encoder-decoder, RNN-T)? I think that this part makes the paper's scope narrow.
- Section 4.1 "(iii) converting characters into the Latin token set via unidecode3 package; characters failing the conversion were discarded from the text": Can you describe the examples? Also, I'm concerned that if we discard some characters in the reference, we cannot evaluate the performance validly with the other reports. Can you clarify this part?
- Section 5.7: It is difficult to conclude since they are very different to compare (e.g., I'm not sure which one is more difficult using 800h of labeled German data and 60k hours of unlabeled English data). Can you explain the benefits of your method more clearly?

Other suggestions
- For me, the method is a little bit over-claimed since this method is primarily applicable to languages with the same scripts or with transliteration systems. It would not be easy to apply this method to the ideogram languages (e.g., Chinese and Japanese, although they are rich-resource languages, and we can build ASR systems easily). I think the paper requires some discussion about it (e.g., adding it to the DISCUSSION AND LIMITATIONS section?).
- Section 2.2: $(\alpha > 0)$ suddenly appears. This should be shown around Eq. (1), where $\alpha$ first appears.
- Section 4, first paragraph: These experimental setups are difficult to follow, as they are very diverse. I recommend you describe the design of the experiment (or the intention of what you want to show) when you describe each experimental setup.
- Figure 3 is too small... Please improve it.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper describes an approach to training an ASR model without transcribed speech in a language – “Unsupervised ASR”.  The central idea is to use an ASR model for some high resource source language to generate hypotheses for the target language, and integrate target language information through an LM. Then iterative pseudolabeling can be used to refine performance.  The authors show competitive performance.  The authors also demonstrate performance if the source and target language do not share a writing script.

### Strengths
The clearest strength of this approach is its simplicity.  The technical approach uses mostly off-the-shelf, well understood techniques to solve a challenging task.

Evaluations are largely well done across a variety of language families (though more limited than other work on unsupervised ASR)

### Weaknesses
It would be good to compare performance on more languages, prior work has investigated FLEURS.  Comparing performance on this data set would enable clearer comparisons.

There is a reliance on the unidecode to “romanize” the character sets of various languages to Latin script.  The recognition performance in a language should be in its own script, not a romanized version.  It does not seem as though unidecode inverted prior to CER calculation. (Though I suppose this could also be a “question” rather than a “weakness”

It is unclear how much the performance is impacted by the choice of source language. While the authors show results across a few languages, a more systematic analysis of source language selection would be beneficial. The current analysis does not provide a clear understanding of the acoustic or linguistic properties that make a source language suitable for transfer learning in this context.



### Questions
Is the example in Figure 1 a real example or made up to demonstrate idealized behavior? This wasn’t clear from the context.

In Section 2.0 it is claimed that ‘unsupervised ASR is viable, as long as source and target language share enough ”similarities”’.  Which similarities are critical for performance here? Acoustic, lexical, other?

Just a note for Section 5.6 – the title describes transfer across “Alphabets”, however, not all writing systems are alphabets. Would this approach extend to abugida, abjad or logographic writing systems?

Note: it would be nice if Figure 4 used the same Y axis in both tables.  (It’s more understandable that the X axis varies)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces an innovative approach for training unsupervised Automatic Speech Recognition (ASR) systems in low-resource languages, using only unmatched speech and text data. The method takes advantage of the similarity in pronunciation between characters in a paired language to create pseudo-labels for the target language, which are further refined by a language model. This approach demonstrates promising results in both cross-language and cross-family scenarios.

### Strengths
1. This paper addresses a practical and underexplored problem. Implementing the proposed method in the pseudo-labeling framework is more straightforward than using GAN-based approaches.
2. This approach demonstrates promising results in both cross-language and cross-family scenarios.
3. The performance is further enhanced with the use of multi-lingual source AMs.
4. The paper is well-written and straightforward to understand.

### Weaknesses
1. The results are not particularly encouraging:
    * It would be more valuable to demonstrate that a single source AM can be effectively applied to multiple target languages (e.g., en -> {sw, ha, X, Y, Z}) rather than showcasing the application of multiple source AMs to the same target language (e.g., {en, es, ge, fr} -> sw):
    * It appears that this method is effective primarily for the language pairs { *-> sw} and {be -> cs}, which raises concerns about its generalization to other low-resource languages.

2. In contrast to wav2vec-u, the concept of "similarity" might restrict the applicability of this method, potentially preventing it from identifying an appropriate source language for a specific target language.

### Questions
1. In the paper, it is claimed that "for African languages, we use Kinyarwanda only as a source language (as text data are not available in the Common Crawl dataset)." How is the Kinyarwanda AM trained without text data?
2. Table 3 indicates that the performance of the de degrades when language model decoding is applied. Is there any analysis provided in the paper to explain this

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
