# Large Language Models are Efficient Learners of Noise-Robust Speech Recognition

- Decision: Accept
- Avg Score: 5.75
- Scores: 8, 1, 6, 8

## Abstract
Recent advances in large language models (LLMs) have promoted generative error correction (GER) for automatic speech recognition (ASR), which leverages the rich linguistic knowledge and powerful reasoning ability of LLMs to improve recognition results.
The latest work proposes a GER benchmark with ``HyPoradise'' dataset to learn the mapping from ASR N-best hypotheses to ground-truth transcription by efficient LLM finetuning, which shows great effectiveness but lacks specificity on noise-robust ASR.
In this work, we extend the benchmark to noisy conditions and investigate \emph{if we can teach LLMs to perform denoising for GER just like what robust ASR do}, where one solution is introducing noise information as a conditioner into LLM.
However, directly incorporating noise embeddings from audio encoder could harm the LLM tuning due to cross-modality gap.
To this end, we propose to extract a language-space noise embedding from the N-best list to represent the noise conditions of source speech, which can promote the denoising process in GER.
Furthermore, in order to enhance its representation ability of audio noise, we design a knowledge distillation (KD) approach via mutual information estimation to distill the real noise information in audio embeddings to our language embedding.
Experiments on various latest LLMs demonstrate our approach achieves a new breakthrough with up to 53.9\% correction improvement in terms of word error rate while with limited training data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the noise-robust ASR. The method is based on the LLM-based generative error correction (GER), but contrary to the existing approaches, it extract the noise information from the N-best hypotheses of transcription languages, not directly from the audio. The proposed method significantly outperformed the existing baseline and advanced the area of noise-robust ASR.

### Strengths
Originality:
While it would normally be better to reduce the noise before ASR or to estimate the noise directly from the acoustic data, the idea of doing noise estimation from N-best transcription hypotheses is interesting. It is interesting that this method avoids the difficulty of cross-modal fine-tuning by doing so. It is also compelling because it seems that humans actually perform similar processing in noisy environments.

Quality:
The paper is rich in evaluation, and the improvement interval is significant compared with the existing baselines. Also, it provides theoretical hypotheses why the proposed method works better that sound convincing.

Clarity:
The description appears complete. I have not read all the details, but I get the impression that this paper is very well organized.

Significance:
The task addressed is clearly significant because it has many practical applications. The novel approach presented in this paper is also be interesting, and I think it can potentially be applied in other modalities.

### Weaknesses
- It was very difficult to find anything to explicitly criticize about the technical content of the paper. There may be flaws and room for improvement, but that is no longer something to do at the peer review stage of this paper.
- If I had to say something, I was concerned that the notation seemed sometimes inconsistent.

### Questions
- The notation seems to be mixed up. $\mathcal{P}$ may be used in the sense of probability density function in equation (2), but this is also used to mean "prompt". In the definition of KL, the probability distribution is denoted as $\mathbb{P}$. 
- I don't feel the need to use too much fancy notation like tensor product $\mathbb{P}_X \otimes \mathbb{P}_Z$ and Radon-Nikodym derivative $\log \frac{d\mathbb{P}}{d\mathbb{Q}}$.
- It may be just because I am conservative but $1e^{-2}$ looks like $1/\exp(2)$.
- $\mathbb{E}_p p \log p$ looks strange in Table 15.
- $\textit{i.e.}$ should not be italicized in standard writing convention.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work addresses noisy conditions by proposing a language-space noise embedding derived from ASR hypotheses to aid denoising with large language models (LLMs)-based generative error correction (GER). A knowledge distillation strategy further enhances noise representation. Tests on various LLMs show up to 53.9% improvement in word error rate with limited training data, demonstrating the effectiveness of the proposed noise embedding and denoising ability of LLMs.

### Strengths
From a generally purposed GER benchmark to a more focused noise-robust problem, it is a suitable extension in depth and kind of milestone using LLM for robust ASR.

### Weaknesses
The illustrations of (b) GER with audio-space denoising (Zhang et al., 2023b; Fathullah et al., 2023) and (c) GER with language-space denoising (ours) are a little challenging to follow. Is denoised audio directly fed to the LLM adapter, or is there something else you want to express?

We noticed that the HP database only comes from the n-best of a few models. Is it possible to introduce more diverse system outputs from various models?

According to the method in the article, Section 4.3 should be the most important part, relatively speaking. Unfortunately, the space allocated to it in the article is too cramped—too many things to fit into this small section, which is not very reader-friendly.

### Questions
see above

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work extends an established benchmark of generative error correction with a new "HyPoradise" dataset, in order to enable LLMs to perform error correction. The study presents application on noisy-robust speech recognition and claims that it reaches up to 53.9% improvement on word error rate.

The study itself follows the latest trend of research, where LLM is used to

### Strengths
1. The work itself holds certain level of novelty, with good review on earlier literatures on both error correction in ASR and LLM.
2. The methodology is clearly presented, along with the novelty of the paper.
3. With some ambiguities in the middle, the paper itself clarifies the idea with experiments subtlely.

### Weaknesses
1. I think the topic of error correction might be a poor fit to the conference. But perhaps I am wrong on this so correct me if so.
2. There lacks the practical discussion on additional workload, especially on resources.
3. The description of building the embedding space is somehow confusing in particular terms. For example, in Section 4.2.1 - what is "diversity similar to variance"?

Minor issues:
1. Section 5.4 - What is Table 14?
2. I suggest to put the definition of embedding a bit earlier from the beginning of Section 4. Otherwise, Figure 2 looks a bit confusing.

### Questions
1. I wonder the motivation of using Robust Hyporadise dataset for noisy ASR condition. What kind of noise it exactly contains? Is it replacible with other noisy datasets that are more commonly known to the ASR community, such as Switchboard and VoxCeleb (just two examples, they may not be good fit)?
2. Do you think your model will be sensitive to sampling frequency? I mentioned Switchboard in the last question, which is an 8KHz dataset.
3. In section 4.2.2, why you think MINE can enhance the noise representation ability? It looks like MINE is not part of novelty here, so any work backing it up?

### Soundness
2 fair

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
In a previous study, generative error correction (GER) is achieved by learning the mapping from ASR N-best hypotheses to ground-truth transcription through efficient LLM finetuning. This paper extends this idea and focuses on noisy conditions. To avoid the cross-modality gap, the authors propose a novel idea to extract a language-space noise embedding from the N-best list to represent the noise conditions of source speech. Furthermore, in order to enhance its representation ability of audio noise, a knowledge distillation (KD) approach via mutual information estimation (MINE) is employed. The experiments show that the proposed method can significantly outperform the conventional LM rescoring baseline. Several additional experiments are also included in the Appendix which provide more insight into the proposed RobustGER. Overall, the paper is very clear and well-written. It describes the problem and explains the solution well. The experiments done are reflective of the proposed model's performance.

### Strengths
1)	Novel idea to apply LLM for noise-robust ASR.
2)	Extract language-space noise embedding with knowledge distillation based on mutual information.
3)	Good performance improvement.
4)	Plenty of experiments and ablation studies.
5)	Insightful discussions, such as t-SNE visualization, and the relationship between noisy speech and n-best list diversity.

### Weaknesses
The way to extract the audio noise embedding is from the ASR encoder (i.e., Whisper Large-V2). This may only make sense for the Whisper ASR, as a recent paper [1] pointed out that the noise-robustness of Whisper does not come from noise-invariant, but recognizes speech conditioned on the noise type. In summary, the Whisper encoder is a suitable model to extract noise information. On the other hand, other ASR models may not have such ability and they achieve noise-robustness through the noise-invariant encoder. If this is the case, those ASR encoders may not be suitable to extract audio noise embedding. A discussion and simple experiment about this would be great.


As pointed out on page 5, the noise embedding is calculated by their diversity “similar to variance”, however in eq (4) and (6), the sentence embedding differences are simply summed, so I guess an abs or square operation is needed?

Following the previous question, in the appendix page 16, you mentioned that the dimension of language-space noise embedding E_LN is N(N-1)xD_sbert. Could you explain where N(N-1) comes from? I cannot see this dimension from eq (4) and (6).

In figure 2, and eq (3), why the language-space noise embedding is ‘subtracted’ from the prompt? I found another related equation in eq (13) of the Appendix and the authors only mention “the subtraction operation denotes “denoise””, more explanation is needed.

In eq(8), IΘ(X; Y ) should be IΘ(X; Z)

### Questions
1)	As pointed out on page 5, the noise embedding is calculated by their diversity “similar to variance”, however in eq (4) and (6), the sentence embedding differences are simply summed, so I guess an abs or square operation is needed?
2)	Following the previous question, in the appendix page 16, you mentioned that the dimension of language-space noise embedding E_LN is N(N-1)xD_sbert. Could you explain where N(N-1) comes from? I cannot see this dimension from eq (4) and (6).
3)	In figure 2, and eq (3), why the language-space noise embedding is ‘subtracted’ from the prompt? I found another related equation in eq (13) of the Appendix and the authors only mention “the subtraction operation denotes “denoise””, more explanation is needed.
4)	In eq(8), IΘ(X; Y ) should be IΘ(X; Z)

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
