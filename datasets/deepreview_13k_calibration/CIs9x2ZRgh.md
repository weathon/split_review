# CR-CTC: Consistency regularization on CTC for improved speech recognition

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 5, 8, 8

## Abstract
\vspace{-0.5em}

Connectionist Temporal Classification (CTC) is a widely used method for automatic speech recognition (ASR), renowned for its simplicity and computational efficiency. 
However, it often falls short in recognition performance.  
In this work, we propose the Consistency-Regularized CTC (CR-CTC), which enforces consistency between two CTC distributions obtained from different augmented views of the input speech mel-spectrogram.
We provide in-depth insights into its essential behaviors from three perspectives: 1) it conducts self-distillation between random pairs of sub-models that process different augmented views; 2) it learns contextual representation through masked prediction for positions within time-masked regions, especially when we increase the amount of time masking; 3) it suppresses the extremely peaky CTC distributions, thereby reducing overfitting and improving the generalization ability. Extensive experiments on LibriSpeech, Aishell-1, and GigaSpeech datasets demonstrate the effectiveness of our CR-CTC.  
It significantly improves the CTC performance, achieving state-of-the-art results comparable to those attained by transducer or systems combining CTC and attention-based encoder-decoder (CTC/AED).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper applies a new type of self-consistency loss on different augmented view for CTC based ASR model. The new consistency regularized loss is doing KL over CTC output. Experimental results shows WER got improved.

### Strengths
The proposed idea is intuitive. Although the gain is small, the paper is compared with couple competitive baseline on librispeech.

### Weaknesses
The paper lack of citation to many very relevant work:

Most important one:
Contrastive siamese network for semi-supervised speech recognition (https://arxiv.org/pdf/2205.14054). The paper focus on compare with SoTA, instead of compare with literature self-distill or other consistency based baseline. In that paper, it include practical trick to make SimSiam type of model work for ASR.

### Questions
Please properly cite literature work and make proper comparison.

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
This paper proposes an improved version of Connectionist Temporal Classification (CTC) called Consistency-Regularized CTC (CR-CTC) for automatic speech recognition (ASR). CR-CTC enforces consistency between two CTC distributions obtained from different augmented views of the input speech mel-spectrogram.  The proposed method has 3 advantages: 1) it conducts self-distillation between random pairs of sub-models that process different augmented views; 2) it learns contextual representation through masked prediction for positions within time-masked regions, especially when we increase the amount of time masking; 3) it suppresses the extremely peaky CTC distributions, thereby reducing overfitting and improving the generalization ability. Extensive experiments on LibriSpeech, Aishell-1, and GigaSpeech datasets demonstrate the effectiveness of CR-CTC, which achieves performance comparable to, or even slightly better than, that of transducer and CTC/AED.

### Strengths
CR-CTC takes two different augmented views of the same speech mel-spectrogram as the inputs and enforce consistency between the two obtained CTC distributions. This method helps the model to do self-distillation between randomly sampled sub-models, learn contextual representation through masked prediction and reduce the peaky CTC distribution. The idea is simple and easy to implement. The training cost didn’t increase based on the description in section 4.1. The experiments on LibriSpeech, Aishell-1, and GigaSpeech show the proposed method outperform standard CTC in all these sets for different model sizes. It achieves comparable accuracy or even better than the advanced transducer or CTC/AED model. The paper also provided detailed ablation study to help the reader understand more details about the method.

### Weaknesses
Comparing results in table 1 and 3, the advantages of CR-CTC over standard CTC is smaller for GigaSpeech set than that for LibriSpeech set.  This may indicate that the proposed method may not work very well for big training data, e.g. tens of thousands of speech hours.
    In table 1, 2 and 3, it’s not mentioned that the results for transducer and CTC/AED models are from beam search or greedy search. For these two models, the results of beam or greedy search usually have big differences. If the results given are from greedy search, it may mean the accuracy of CR-CTC model still have gap from that of transducer and CTC/AED model with beam search.

### Questions
For the combination of transducer and CR-CTC model, does the CTC score is used during the decoding?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
Consistency regularization (CR) is a well established existing method, where you forward through some model two times with different augmentation (and maybe also dropout or other randomness) to get two predictions, and then you minimize the symmetric KL between both, or similar. Thus, this method is purely on the training side, and doesn't change any modeling aspect.

Here, CR is applied to speech recognition, specifically to CTC models, on a frame-by-frame basis, called CR-CTC. The main difference in the two branches is caused by different SpecAugment masking.

For fair comparison, due to forwarding the data twice now, the number of epochs and the batch size are both halfed for the CR-CTC case.

Experiments are done on Librispeech, Gigaspeech and Aishell.

The method is mainly tested on CTC, but then some extension to that is when they used a joint AED/CTC model in the end, where CR is applied only to the CTC part.

A number of ablations has been made on the loss scale and on increasing the SpecAugment masking, which seems ot help more on CR-CTC, but for pure CTC, the original amount of SpecAugment masking already seems optimal.

The improvements on Librispeech test-other are quite large: From 5.72% WER to 4.35% WER.

It is also shown that it reduces the peakiness of the alignment behavior a bit.

### Strengths
- Simple method.

- Seems to give huge improvements, at least in some settings.

### Weaknesses
 - Some smaller details are a bit unclear.
- Only tested for Zipformer. More standard would be Conformer, but this is missing.
- Unclear how well this method works in other cases, e.g. other models, other datasets, some other hyperparams different. Specifically, I tested it in my setup, and it didn't really helped.

- Abstract starts a bit strange. It says CTC is worse than RNN-T and AED. Yes sure, we know. But then it talks about some method to maybe improve CTC. So why is mentioning RNN-T/AED relevant? Is it because you think the gap between CTC and AED/RNN-T is larger than what you would expect, and some methods like the presented here should close the gap? But I don't think that this really is being shown here in this work. Also, some variant of this method could maybe be applied to AED/RNN-T just as well. So, I don't really see why mentioning AED/RNN-T in the abstract is really relevant for this work here. It's fine in the introduction, to put CTC into perspective, but I don't think it's relevant in the abstract. I was a bit confused about this.

Eq 3 and also Figure 1, the CTC loss is maybe better formulated on z, not on x? I found it weird that x goes into L_CTC but z goes into L_CR.


"a time warping factor of 80" - what does that mean? I don't think you make the sequence 80 times longer?

Please clarify the downsampling of the Zipformer. Do you stick to the original Zipformer here, where the Conv Frontend downsamples the 100Hz feature frames to 50Hz, and then the residual/bypass connection is always at 50Hz, and at the very end, you downsample again to get 25Hz output frames, i.e. the log probs are at 25 Hz?

Did you investigate how the downsampling influences the CR-CTC loss? I think this can have quite a crucial impact, as we know that in general, for CTC, the ratio of input length to output length plays an important role for convergence and training dynamics.

Did you also test with other vocab sizes? 500 BPE size seems quite small to me. How does it perform with larger vocab sizes, e.g. with 10k?

How does the Zipformer influence the results? Specifically, do you think you get the same improvements with a normal Conformer?


"auxiliary head of AED" (p9, l483) (and also same with transducer) / Table 7: I don't exactly understand what you report here. Is the AED (or transducer) head just used as an aux loss, and during recognition, you only use the CTC head and ignore the AED (or transducer)? Please be more clear about that. Also, you are giving the wrong citation for that. The reference you give is about joint AED/CTC, where both AED and CTC heads are used for recognition, so nothing is ignored, nothing is just used as aux loss. The only reference I know where AED is used as an aux loss for CTC is "Keep Decoding Parallel With Effective Knowledge Distillation From Language Models To End-To-End Speech Recognisers", Hentschel et al, 2024.


On GigaSpeech, improvement seems much less (XL, test: 10.87 -> 10.28) compared to Librispeech (5.72 -> 4.35). Why?

Table 3 caption: "GigaSpeeech" typo.


Transducer w/ CR-CTC, what exactly is that? The same approach applied on transducer? But then this is not CTC? Or is it combined CTC with transducer?


Note, as your method is very simple to implement, and your improvements here are really impressive, I was just trying it out myself. However, with negative result: For my Conformer CTC baseline, on 100Hz inputs, downsampled by factor 6, with BPE 10k vocab, with aux AED loss ("Keep Decoding Parallel With Effective Knowledge Distillation From Language Models To End-To-End Speech Recognisers", Hentschel et al, 2024), where my baseline with greedy decoding without LM was at 5.93% on dev-other, it degraded with CR-CTC to 5.99% on dev-other. I halved the number epochs and halved the batch size for the CR experiment, just like you did. This is with CR loss scale 0.2. I did not adapt SpecAugment yet, but from your paper, I would expect that even with this setting, I should already see quite some improvement. So, why don't I? Your paper is lacking such study on other settings, as mentioned above (Conformer, other BPE sizes, other downsampling) to know whether I can/should expect similar improvements there or not, and whether I maybe need a very different CR loss scale there, or whether I need to care about other things.


Note, halving the batch size can have other effects. Many methods (e.g. optimizer, LR schedule, regularization, etc) don't work in the same way for different batch sizes. You do effectively more updates to the model. It can also have a regularization effect. So, I think an important missing experiment is: What happens to the baseline when you half the batch size? Maybe you also get improvements there?

### Questions
Abstract starts a bit strange. It says CTC is worse than RNN-T and AED. Yes sure, we know. But then it talks about some method to maybe improve CTC. So why is mentioning RNN-T/AED relevant? Is it because you think the gap between CTC and AED/RNN-T is larger than what you would expect, and some methods like the presented here should close the gap? But I don't think that this really is being shown here in this work. Also, some variant of this method could maybe be applied to AED/RNN-T just as well. So, I don't really see why mentioning AED/RNN-T in the abstract is really relevant for this work here. It's fine in the introduction, to put CTC into perspective, but I don't think it's relevant in the abstract. I was a bit confused about this.

Eq 3 and also Figure 1, the CTC loss is maybe better formulated on z, not on x? I found it weird that x goes into L_CTC but z goes into L_CR.


"a time warping factor of 80" - what does that mean? I don't think you make the sequence 80 times longer?

Please clarify the downsampling of the Zipformer. Do you stick to the original Zipformer here, where the Conv Frontend downsamples the 100Hz feature frames to 50Hz, and then the residual/bypass connection is always at 50Hz, and at the very end, you downsample again to get 25Hz output frames, i.e. the log probs are at 25 Hz?

Did you investigate how the downsampling influences the CR-CTC loss? I think this can have quite a crucial impact, as we know that in general, for CTC, the ratio of input length to output length plays an important role for convergence and training dynamics.

Did you also test with other vocab sizes? 500 BPE size seems quite small to me. How does it perform with larger vocab sizes, e.g. with 10k?

How does the Zipformer influence the results? Specifically, do you think you get the same improvements with a normal Conformer?


"auxiliary head of AED" (p9, l483) (and also same with transducer) / Table 7: I don't exactly understand what you report here. Is the AED (or transducer) head just used as an aux loss, and during recognition, you only use the CTC head and ignore the AED (or transducer)? Please be more clear about that. Also, you are giving the wrong citation for that. The reference you give is about joint AED/CTC, where both AED and CTC heads are used for recognition, so nothing is ignored, nothing is just used as aux loss. The only reference I know where AED is used as an aux loss for CTC is "Keep Decoding Parallel With Effective Knowledge Distillation From Language Models To End-To-End Speech Recognisers", Hentschel et al, 2024.


On GigaSpeech, improvement seems much less (XL, test: 10.87 -> 10.28) compared to Librispeech (5.72 -> 4.35). Why?

Table 3 caption: "GigaSpeeech" typo.


Transducer w/ CR-CTC, what exactly is that? The same approach applied on transducer? But then this is not CTC? Or is it combined CTC with transducer?


Note, as your method is very simple to implement, and your improvements here are really impressive, I was just trying it out myself. However, with negative result: For my Conformer CTC baseline, on 100Hz inputs, downsampled by factor 6, with BPE 10k vocab, with aux AED loss ("Keep Decoding Parallel With Effective Knowledge Distillation From Language Models To End-To-End Speech Recognisers", Hentschel et al, 2024), where my baseline with greedy decoding without LM was at 5.93% on dev-other, it degraded with CR-CTC to 5.99% on dev-other. I halved the number epochs and halved the batch size for the CR experiment, just like you did. This is with CR loss scale 0.2. I did not adapt SpecAugment yet, but from your paper, I would expect that even with this setting, I should already see quite some improvement. So, why don't I? Your paper is lacking such study on other settings, as mentioned above (Conformer, other BPE sizes, other downsampling) to know whether I can/should expect similar improvements there or not, and whether I maybe need a very different CR loss scale there, or whether I need to care about other things.


Note, halving the batch size can have other effects. Many methods (e.g. optimizer, LR schedule, regularization, etc) don't work in the same way for different batch sizes. You do effectively more updates to the model. It can also have a regularization effect. So, I think an important missing experiment is: What happens to the baseline when you half the batch size? Maybe you also get improvements there?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a method to improve CTC performance by applying self-distillation between sub-models using drop-based techniques. The approach aims to enhance target token distribution predictions within time-masked regions and develop contextual representations from unmasked segments, drawing inspiration from self-supervised learning methods. By increasing time-masking, this technique promotes effective masked prediction, reducing peaky CTC distributions and strengthening the model's generalization ability. Experiments on multiple datasets—Librispeech, Aishell-I, and GigaSpeech—demonstrate that the proposed method achieves performance on par with transducer and CTC/AED models when used in joint training.

### Strengths
* This paper presents a simple yet effective distillation method by extending time-masking to develop contextual representations from unmasked segments across two different augmented views.
* It demonstrates that CTC performance is comparable to that of transducer and CTC/AED models.

### Weaknesses
The method generates two different augmented views by independently applying existing SpecAugment to Zipformer. However, it raises the question of how generalizable this claim is when applied to other architectures like Conformer, E-Branchformer, or Branchformer. 

 The choice of alpha set to 0.2 in Equation 3 lacks sufficient justification. An ablation study demonstrating the impact of different alpha values on performance is needed to understand the method's sensitivity to this hyperparameter. 

 The specific choice of a beam size of 4 for comparisons with other state-of-the-art models is not well-motivated. The authors should include results with different beam sizes (e.g., 1, 4, 8) to show the method's sensitivity to this parameter. 

 The authors employ a larger amount of time-masking by increasing both the number of time-masking regions and the maximum masking fraction by a factor of 2.5. However, it is unclear how much time-masking is optimal for masked prediction. An ablation study showing performance with different amounts of time-masking (e.g., 1x, 1.5x, 2x, 2.5x, 3x) for ZipformerXL and at least one baseline model in Table 15 is necessary to understand the criticality and generalizability of this choice. 

 In Tables 1, 2, and 3, the decoding methods for the CTC/AED baselines (CTC-only or CTC/AED joint decoding) are not specified. This lack of clarity makes it difficult to compare the results fairly. The table captions should specify the decoding methods for both the baselines and the proposed method. 

 For a deeper understanding, the authors should include results showing the impact of increased time-masking on the baseline CTC model as well. This would help isolate whether the benefit comes from the two-branch architecture of CR-CTC or simply from more aggressive augmentation. Although the authors reported one of the baselines with larger time-masking, it would be helpful if results were provided for the other tables as well. 

 In Table 3, the best results were obtained using Zipformer XL. However, the authors should: 1. Explain the rationale for using Zipformer-M in Tables 4 and 5 instead of Zipformer-XL. 2. Provide results for Zipformer-XL in Table 11 for completeness. 3. Clarify whether the results in Table 11 are from self-distillation or masked prediction in CR-CTC. 

 The results of SR-CTC in Table 6 are slightly worse than those of CR-CTC. The authors should provide an explanation for this behavior, and clarify whether SR-CTC also uses increased time-masking.

### Questions
* Why was the choice of alpha set to 0.2 in Equation 3? It would benefit readers if the authors could provide results from an ablation study showing the impact of different alpha values on performance. This would offer greater insight into the method's sensitivity to this hyperparameter choice.
* Why was a beam size of 4 specifically chosen for comparisons with other state-of-the-art models? The authors may consider including results with different beam sizes (e.g., 1, 4, 8) in an appendix to show the method's sensitivity to this parameter.
* The authors employed a larger amount of time-masking by increasing both the number of time-masking regions and the maximum masking fraction by a factor of 2.5. However, it would be interesting to know how much time-masking is optimal for masked prediction. The authors could provide results from an ablation study showing performance with different amounts of time-masking (e.g., 1x, 1.5x, 2x, 2.5x, 3x) for ZipformerXL and at least one baseline model in Table 15. This would help readers understand how critical this choice is and how generalizable the method is.
* In Tables 1, 2, and 3, are the CTC/AED baseline results reported with CTC-only decoding or CTC/AED joint decoding? This could be clarified by specifying the decoding methods for the baselines and the proposed method in the table captions.
* For a deeper understanding, the authors could include results showing the impact of increased time-masking on the baseline CTC model as well. This would help isolate whether the benefit comes from the two-branch architecture of CR-CTC or simply from more aggressive augmentation. Although the authors reported one of the baselines with larger time-masking, it would be helpful if results were provided for the other tables as well.
* In Table 3, the best results were obtained using Zipformer XL. However, the authors should:
1. Explain the rationale for using Zipformer-M in Tables 4 and 5 instead of Zipformer-XL.
2. Provide results for Zipformer-XL in Table 11 for completeness.
3. Clarify whether the results in Table 11 are from self-distillation or masked prediction in CR-CTC.
* The results of SR-CTC in Table 6 are slightly worse than those of CR-CTC. Do the authors have any explanation for this behavior, and does SR-CTC also use increased time-masking?

### Soundness
3

### Presentation
3

### Contribution
3
