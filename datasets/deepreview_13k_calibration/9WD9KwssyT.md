# Zipformer: A faster and better encoder for automatic speech recognition

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8

## Abstract
The Conformer has become the most popular encoder model for automatic speech recognition (ASR).  It adds convolution modules to a Transformer to learn both local and global dependencies. In this work we describe a faster, more memory-efficient, and better-performing Transformer, called Zipformer.  Modeling changes include: 1) a U-Net-like encoder structure where middle stacks operate at lower frame rates; 2) reorganized block structure with more modules, within which we re-use attention weights for efficiency; 3) a modified form of LayerNorm called BiasNorm allows us to retain some length information; 4)  new activation functions SwooshR and SwooshL work better than Swish.  
We also propose a new optimizer, called ScaledAdam, which scales the update by each tensor's current scale to keep the relative change about the same, and also explictly learns the parameter scale. It achieves faster convergence and better performance than Adam. 
Extensive experiments on LibriSpeech, Aishell-1, and WenetSpeech datasets demonstrate the effectiveness of our proposed Zipformer over other state-of-the-art ASR models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new encoder architecture based on conformer for speech recognition task. Some of the newly introduced modifications are well motivated based on some findings on trained the original conformer models. The experiments show strong performance compared with original conformer model and multiple other conformer variants. Considering the popularity of conformer for speech recognition and other speech tasks, the findings and contribution of this paper could benefit the speech/audio community a lot!

### Strengths
1. A newly designed conformer variant that achieve SOTA performance on speech recognition task.
2. Experiments are done on different datasets with training data at different scales (hundreds, thousands and tens of thousands).
3. Experimental results are strong, indicating the effectiveness of model.

### Weaknesses
1. While the motivation for biasnorm and scaledadam are well explained, the motivation for zipformer blcok, especially those downsampling and upsampling modules are not well presented. The paper lacks a clear explanation of how these specific downsampling and upsampling methods were chosen, and why they are expected to be more effective than other common techniques like strided convolutions or pooling layers. The connection between the multi-resolution processing and the final performance is not sufficiently detailed.
2. The results on aishell1 is not quite convincing compared to other conformer variants. The author could elaborate more on the performance. Could be that this is a small dataset? The paper should include a more detailed analysis of why the proposed model does not show the same level of improvement on this dataset as it does on others. It would be beneficial to explore if the model's architecture is less suitable for smaller datasets or if there are other factors at play.

### Questions
1. Curious about whether the authors tried the new activation functions, biasnorm and scaledadam on other tasks? Do they still show superiority?
2. How could you make the model work in streaming fasion?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Context: Automatic speech recognition (ASR), where Conformer currently is the state-of-the-art encoder, which is used by most groups. A new variant of the Conformer is proposed in this paper, along with a lot of changes.

- New ZipFormer model as an alternative to the Conformer.
- BiasNorm as an alternative to LayerNorm.
- Bypass module instead of residual connections
- Downsample module instead of simply average or max pooling or striding
- Re-use of attention weights inside a ZipFormer block
- Non-linear attention instead of standard attention, which uses a multiplicative element
- New activation functions SwooshR and SwooshL as an alternative to Swish.
- Additional learnable scalar for the scale of weights
- ScaledAdam optimizer as an alternative to Adam.
- Eden learning rate scheduling which is both step-based and epoch-based, as an alternative to purely step-based or purely epoch-based LR schedules.

### Strengths
- There are a lot of interesting novelties here in the paper, like the ZipFormer model itself, ScaledAdam, BiasNorm, new activation functions, and more. (Although having so many different novelties is also a weakness, see below.)

- Improvements are very good, i.e. good relative WER improvements, while also having it more efficient.

- Good ASR baselines.

### Weaknesses
 - There are maybe too many new things being introduced here, which are all interesting by themselves, but each of them would maybe require more investigation and analysis on their own. E.g. introducing a new optimizer (ScaledAdam) is interesting, but it should be tested on a couple of different models and benchmarks, and this would basically a work on its own. Now we have way too little analysis for each of the introduced methods to really tell how good they are. The ablation study is basically only a single experiment, showing ScaledAdam vs Adam, or LayerNorm vs BiasNorm. A single experiment is not really enough to really see how ScaledAdam vs Adam performs, or BiasNorm vs LayerNorm, etc. E.g. replaying LayerNorm by BiasNorm in a standard Transformer, maybe for language modeling, how would this perform? Many of these introduced methods seem to be quite orthogonal to each other.

- For comparisons, it would have been better to use a more standard transducer, not a pruned transducer. Or maybe even CTC, or CTC/AED. This would have made it easier to compare the results to other results from the literature (Table 2).

- Measuring just FLOPs can sometimes be misleading as indicator for speed, because certain operations might be faster than others, and certain operations can be executed in parallelized, while others can not. It would be interesting to also see the actual measured speed on some given hardware.

- No systematic comparison to other Conformer variants, e.g. E-Branchformer, etc. (I don't just mean to have the number from literature as a comparison, as done in Table 2. I mean that the differences are compared, i.e. discussed and maybe also experimentally compared.)

### Questions
The capitalization is a bit inconsistent. Transformer is always lower case (transformer), while Conformer, ZipFormer etc are all capitalized.

It would make sense to state that (or whether) the code is published (even if you want to put the link only in the final version).

How long does the training take? What batch sizes are used?


> Downsample module averages every 2 frames with 2 learnable scalar weights (after softmax normalization)

I don't exactly understand how this is done. For the whole module, there are two learnable scalar weights only? So it could learn to always take really the average, but also to always take the first and ignore the second, or vice versa? This does not make sense to me. Why does it make sense to learn that? What happens if you just take the average? Or maybe use max-pooling instead? What is the influence of this?


If you downsample at the very end to 25 Hz, why not do that earlier, and downsample right in the beginning to 25 Hz, and then never to 50 Hz again? That would make it quite a bit faster. So how much worse does this get?


LayerNorm/BiasNorm: When there is a large value, as even explicitly modelled by the bias in BiasNorm, isn't this a problem, that there is a large number in the denominator, so then all the values become very small? The exp(γ) can compensate that then again, however, I wonder if there are numerical problems.

What is the influence of exp(γ) vs just γ (without exp) in BiasNorm?


How does ScaledAdam compare to methods like WeightNorm, where the weights are also normalized?


> Since Adam is nearly invariant to changes in the gradient scale, for simplicity we replace this with ht = gt ·(rt−1 ⊙θt′−1) = gt ·θt−1

I'm not sure that this would make the code simpler, to have this special case? But I also wonder, what is the influence of this?


For ScaledAdam, as I understand, adding the learnable parameter scale would actually change the model, as this scale now is also part of the model? Is this added for every parameter, or only some selected ones, e.g. the linear transformations?

What is the influence of the Eden learning rate scheduling?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents an interesting alternative, zipformer, to the transformer/conformer encoder which are widely used for automatic speech recognition. The author also claims their modified optimizer, ScaledAdam, learns faster and converges to better optimum than the standard adam. The authors have presented that with the proposed zipformer and together with the modified optimizer, the resultant system achieves similar performance compared to conformer, but with better memory and FLOPS efficiency.

### Strengths
This work presents an alternative approach to the standard (or widely used) transformer encoder structure, which is very interesting to read. The authors explain motivations behind some of the proposed modification, together with the ablation studies.

### Weaknesses
From my biased view, the major weakness in this paper lies in the fact that this work actually presents two inter-connected but (arguably) separate works: one is to the novel new encoder structure, including the U-net with middle stacks operate at a lower frame rates, sharing the attention weight with two self attentions, a novel non-linear attention, a BiasNorm and a slightly modified swooshL/swooshR activation function; the other is about the modified Adam optimizer, scaledAdam, which the authors claim that it can explicitly learn the parameter scale, which the widely used adam failed to. Though the author gives some motivations behind these changes and give some ablation studies, it still points to the following unanswered questions:

  - the authors claim that the zipformer is better than the (reproduced) conformer, squeezeformer or other variants of transformer. However, it is unclear to me whether this is because of the model structure or because of the modified optimizer ? For example, in Table 5, the author presents that with all the proposed change (model and optimizer), zipformer-M can achieve 4.79% WER on test-other, however, with the standard adam optimizer, the WER becomes 5.51%. Will the other variants of transformer get better WER with the author proposed optimizer ? 

  - On the other hand, I am wondering whether the proposed optimizer, which has many adhoc modifications compared with the much widely used adam optimizer, can be more widely used for other deep learning optimization tasks or does it only work for speech tasks or does it only work for zipformer ? Given the zipformer-L is a pretty small model (only 60M parameters) trained on limited data (<1000hrs) according to today's standard,  will the proposed change still work better than the standard adam when the model and the training data scales up?


Other weakness of this paper include: 

  - The authors propose changes to many widely used components, which have been well tested over time and over different tasks beyond just speech recognition. For example, the authors claim that the mean extraction in layer norm is not necessary and also remove the variance normalization. While this may seem to work for authors use case, I am intrigued to learn how generalizable this claim can be. 

  - Some of the proposed modification seem arbitrary. It would be great if the authors can explain a bit. For example, in Eq (4), for the swooshR and swooshL functions, how the -0.08 is selected ? The authors mentioned that the coefficient 0.035 in Eq (4) is slightly tuned. How general is this parameter ? 

- In the ablation study, quite a few modifications results in less than 0.2% absolute WER change. How sensitive of the WERs on librispeech relative to other factors like checkpoint choosing, different training run with different seed ? In my own experiments, these factors can result in up to 0.1% WER changes.


- The authors also miss a series of work in the literature that directly apply standard transformer (without much modification) for ASR. For example, 
   * Y. Wang, A. Mohamed, D. Le, C. Liu et al., “Transformer-based Acoustic Modeling for Hybrid Speech Recognition,” in Proc ICASSP, 2020, it reports a WER of 2.26% / 4.85% on test-clean/test-other of librispeech, achieved by CTC + external NNLM; 
This is followed by a work in: 
  * Zhang, Frank, et al. "Faster, simpler and more accurate hybrid asr systems using wordpieces." arXiv preprint arXiv:2005.09150 (2020).
which achieves a WER of 2.10% and 4.20% using a similar architecture. 

It is also noted that in 

- Wang, Y., Chen, Z., Zheng, C., Zhang, Y., Han, W. and Haghani, P., 2023, June. Accelerating rnn-t training and inference using ctc guidance. In ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 1-5). IEEE.

It achieved almost the same WER as the initial conformer paper, but part of the conformer layers (10 out of total 17 layers) is running at much lower frame rate (about 120ms-160ms per frame). This is related to the temporal downsampling used in zipformer.

### Questions
- In Table 5 and section 4.0.3, it is unclear to me why "no temporal downsampling" will result in increased #params (from 65.6M to 94.2M). All the major components in zipformers: attention , feedfoward and convolution use the same parameters for different temporal resolution.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper offers a number of incremental improvements over the well-known Conformer architecture. In aggregate, these improvements set a new state of the art for supervised Librispeech.

### Strengths
This paper makes the most significant type of contribution in ASR - it improves the state of the art on a well-studied benchmark.  Since it has done so with a collection of small improvements, it offers detailed ablations quantifying the usefulness of each modification.  Importantly, it appears that each modification by itself offers improvement over Conformer.

### Weaknesses
In my option, this paper has the same problem that it identifies in the original Conformer write-up: It's closed-source, complicated, and it will likely not be possible for the results to be reproduced.  This is not by itself disqualifying; it is the nature of the field that SOTA systems are often published without source code.  However, I expect that future work iterating on this design will struggle with direct comparison, much in the same way that this paper compares to a weaker reproduction of the original Conformer.

The comparison to the original conformer is not quite apples-to-apples, in that Zipformer-L is substantially larger than Conformer-L in both the original publication and in this paper's reproduction.  I think the authors should consider including a variant of Zipformer with ~120M parameters, as originally used by Gulati et al.   This would prevent the suspicion that the stronger WER simply reflects the fact that the Zipformer is larger.  It is also concerning that the Conformer baseline reported here is significantly weaker than previously published results, which raises questions about the specific training and evaluation procedures used in this work.

### Questions
The comparison to the original conformer is not quite apples-to-apples, in that Zipformer-L is substantially larger than Conformer-L in both the original publication and in this paper's reproduction.  I think the authors should consider including a variant of Zipformer with ~120M parameters, as originally used by Gulati et al.   This would prevent the suspicion that the stronger WER simply reflects the fact that the Zipformer is larger.

Still, I think Zipformer's substantially reduced computational needs demonstrate that superiority over Conformer does not only reflect model size.  So, I'll recommend this paper for acceptance despite the flaw in this comparison.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
