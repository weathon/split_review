# Token to Token Learning From Videos

- Decision: Reject
- Scores: 5, 8, 3, 1

## Abstract
We empirically study generative pre-training from videos. Our approach is conceptually simple and inspired by generative pre-training from images, iGPT. To enable scaling to videos, we make several important improvements along the data, architecture, and evaluation axes. Our model, called Toto, is a causal transformer that generates videos autoregressively, one token at a time. We pre-train our model on a diverse set of videos with over 1 trillion visual tokens. Our tokens are quantized patch embeddings, rather than pixels, and we use relative embeddings for coarse-to-fine pre-training. We conduct a large-scale study across a suite of diverse benchmarks, including image recognition, video classification, object tracking, robotic manipulation and scaling behaviours. We find that, despite minimal inductive biases, our approach achieves competitive performance across all benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper analyzes generative pre-training on videos, in particular with an autoregressive decoder-only model. It aims to study the different components that go into these models and demonstrate that this is a useful paradigm for a strong general-purpose image and video encoder. The paper trains a Llama-style transformer model with a discrete tokenizer on 1T video tokens and shows good performance on a wide array of tasks spanning image classification, robotic manipulation and video tasks like tracking, action recognition and forecasting, while also showing the effect of different design choices in the tokenizer, model architecture, and token resolution.

### Strengths
1) I think this work is valuable as a systems paper that explores the benefits of various components used for visual generation, as well as their effect on creating strong video representations. 
2) The paper measures downstream performance of the proposed encoder on a very large array of diverse tasks, ranging from Imagenet classification to robotic manipulation. This is very valuable and clearly demonstrates the strengths of the Toto model.
3) The appendix contains many useful details that demonstrate other strengths from the Toto model, lending credence to the thoroughness of the study.
4) The paper is extremely well written and presented. It was a pleasure to read.

### Weaknesses
1) There is no major technical novelty in this work as autoregressive visual generation has been done before (e.g PARTI from Google).  The introduction mentions "necesary architectural changes for scaling to videos" but it's not mentioned clearly what those are - all the components described are standard for autoregressive decoder-only visual generation. The only thing I see is the attention pooling for token weighting, but that's referenced from a prior work as well. However, the value in this paper is from the analysis of the design choices, and this is not a weakness provided the experimental analysis is thorough and insightful. 

2) I think the analysis is missing some important pieces. While there are a lot of experiments, the takeaway and why is not really answered. For example, why is dVAE and patch-dVAE worse than VQGAN? Is the difference entirely due to label leak through perceptual loss? In Table 6, why is Mamba so much worse than Toto?  Furthermore, is the comparison to GPT2 really fair? Toto is based on Llama which is a much newer and upgraded architecture - shouldn't it be expected that Toto would be better? On Table 8, why is Toto much worse than other generative approaches for action recognition? In general, my criticism is that for the results section, a lot of results are presented without much analysis or experiments to explain why the results are there, which really limits the insight of the paper. I'd appreciate clarity on this if I missed something.

3) isn't the scaling behavior somewhat trivial? We know that Llama already exhibits these scaling behaviors, is it surprising that a generative decoder-only model with the same architecture but a different tokenizer would have similar scaling properties?

4) Where is the part of the paper that says/shows relative positional embeddings are better than absolute ones? this is mentioned in the introduction and conclusion but does not seem to be ablated or evaluated anywhere in the paper.

### Questions
I am assigning this paper a rating of 5 for now and will gladly increase my rating if my weaknesses listed are addressed and some of the questions below are answered, or if I misunderstood something and it is clarified.

1) I don't really think that VQGAN being "corrupted" by ImageNet labels makes much sense, it's the most commonly used discrete visual tokenizer and deserves careful analysis along with dVAE. If image net label leak was a concern, it would make more sense to evaluate a different image task than simple classification - maybe segmentation or object detection would make sense instead (though i understand that Imagenet linear probing is a standard measure of visual represenation quality)

2) What is the single insight of the Toto Model? It seems like a generative autoregressive decoder-only video model performs comparably with other visual encoders but it's not necessarily clearly better on all the tasks. Is there a reason this is expected?

3) Is there a reason that video-language tasks were not evaluated? Arguably the most common task with video encoders today is video + language (ie captioning, QA, etc). This would really demonstrate the strength of the encoder, and i think could provide a more compelling case for Toto being a strong encoder and for large scale video pre-training.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a causal autoregressive model that jointly learns on discrete image and video tokens (videos tokenized independently per frame). When trained on 1 trillion tokens sampled from ImageNet, Kinetics-600, Ego4D and HowTo100m, the model shows competitive downstream performance on ImageNet classification, action recognition on Kinetics, action anticipation on Ego4D and Video Segmentation Tracking on DAVIS-2017 compared to relevant baselines. The authors also show the emergence of a scaling law when training their joint model on images and videos.

### Strengths
- Originality

The proposed method is original in training a pure decoder only causal AR model on images and videos without any conditioning. The authors however do claim using discrete tokens and RoPE embeddings as contributions which can be considered not exactly original. Their use in this exact setting, however, is novel.

- Quality

Experiments are clearly defined and seem to be well executed. Not all decisions are thoroughly studied, such as the data used and data mixture per minibatch, or the efficacy of VQGAN tokenizer beyond Imagenet-1k results. The authors claim to study tokenizers in detail, however the study only scratches the surface (discussed later). However, given the computation budget required for these experiments, I believe these could be considered as good-to-have but not must-have. 

- Clarity 

The paper is written very clearly, barring minor writing errors and missing information.

- Significance

I am confident that this is a significant paper in terms of pushing discussion in the community forward re: generative vs discriminative pre-training for image and video models. They show diverse results (though mostly in-domain w.r.t. training data for quantitative results) and do not over-claim performance.

### Weaknesses
- Tokenizer study

The authors only study image tokenization. No video tokenization is attempted or discussed. Within image tokenization, the authors study discrete tokenizers using dVAE or VQGAN. They conclude that various tokenizers have little effect on ImageNet top-1 readout accuracy. However, there is more to unpack here. VQGAN can achieve the same performance using 16x16 tokens and 1k vocabulary as dVAE does with 32x32 tokens. This is not discussed. dVAE with 16x16 tokens and 8k vocabulary performs ~8% worse than VQGAN with 16x16 tokens and 1k vocabulary. The authors choose dVAE justify choosing dVAE due to its tokens showing higher coverage (usage of 1-gram, 2-gram tokens across data) over VQGAN-16k, which is reasonable, but definitely not enough to justify using dVAE given the ImageNet readout result. Showing results for ToTo trained with VQGAN tokenization beyond Imagenet-1k would be very appreciated and would shed more light into this design choice. VQGAN tokenizers at 32x32 tokens are not tested at all, or discussed.

- Related Work

The related work section is sparse, especially in the Robotics section. Video Prediction has been studied in Robotics as pre-training and needs to be discussed. For exampleL Wu et al. ICLR 2024: Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation. 
AIM, El-Nouby et al. ICML 2024, is a very related work that is only mentioned twice in the paper. No comparison results are shown despite AIM code and weights being available. The only discussion for AIM is that it trains on images only, using patch embeddings using data filtered using data filtering networks. In the abstract and conclusion, the authors say they use discrete tokens and RoPE embeddings as compared to prior work, which I must presume to be AIM since the authors do not cite any prior work with those sentences. The lack of comparison and mention of AIM across the paper needs to be improved. 
Vision-Mamba is not discussed at all.
There is almost no discussion of diffusion based models and their use as generative pre-training methods. This is also an oversight in my opinion, since they are being used as vision backbones for perception, notably Marigold-depth (CVPR 2024).

- Comparison with Mamba

The comparison to Mamba is unclear. Which model was used exactly? The table cites the original Mamba paper which does not have vision experiments as far as I know. Did you train your own model? What were the design choices used? How is it related to VisionMamba (Zhu et al. https://arxiv.org/abs/2401.09417)?

- Major experiments are in-domain

The major experiments in the paper are in-domain. The model was trained on ImageNet, Kinetics and Ego4D and later tested on those three datasets. The DAVIS experiment is out-of-domain and novel and appreciated. The robotics examples are simple and only compare to Masked Visual Pre-training (Radosavovic et al.). There are interesting experiments in the supplementary material on adapting the method for semantic segmentation, depth prediction and video generation. It would have made the paper much stronger to have evaluated those tasks as a sign of the strength of joint vision encoding and generation, which parallels recent efforts of repurposing diffusion based image and video generative models for perception.

- Ablating data

How was the data mixture per minibatch decided? How was the dataset decided? On that note, the authors in the conclusion mention they "collect" a large video dataset. This is misleading since they mix existing datasets together.

### Questions
Please address concerns from the weakness section. 

- Unclear details in Action Forecasting results
How were tokens at 5 layers extracted and fused using the pyramid network from StillFast? Please add this detail to the paper or supplementary and in the rebuttal. 

- Figures and writing
The writing refers to GPT-2 as GTP-2 at times. Figure 8 caption is copy pasted from Figure 4 and not updated. Section 4.8 about scaling laws refers to Figure 16 from supplementary, whereas it should refer to Table 16 from Supplementary. 

I am rating this paper as a 8, but really I see it as a 7 due to the concerns raise in the weaknesses section. I applaud the authors for their great work.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents an approach for generative pre-training from videos, and collect a large video dataset and conduct a large-scale empirical study across a range of diverse tasks.

### Strengths
1. This paper makes architectural improvements on generative pre-training to enable scaling to videos.
2. The approach achieves competitive performance across all tasks.

### Weaknesses
1.The logic of the abstract is confusing, the author only explains what he has done, and the motivation and purpose are not clear enough. The introduction part is too short.
2.The connotations of the evaluation indicators in Tables 7 and 10 need to be explained. Some of the test indicators in the table are illustrated, e.g. J, F in Table 10.
3. Tables 7 and 8 show that the Top1 indicators are not convincing in performance, for example, they are not even as high as the DINO using ViT-B. Please explain that their performance is still meaningful, although they do not exceed some of the existing methods.

### Questions
1. Whether the details of the datasets collected in the article can be explained in detail, it seems that it is just a mixture of several datasets. Please explain in detail how the selection criteria for the dataset, the pretreatment step, or the mixture were determined.
2. Please elaborate on the problem definition, application background, hardware specifications used for the experiment, and other details.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This is a tech report on failed attempts of using auto-regressive video token prediction objective for representation learning. In particular, the authors use the standard next patch prediction objective to train the LLaMa transformer model on the HowTo100m video dataset (with some data from other image and video datasets in the mix, but HowTo100m constitutes ~95% of the training data). They then evaluate the resulting representation on a variety of downstream task (image- and video-based, as well as robotics manipulation) with linear-probing and compare to a few baselines. Despite most evaluations being designed to favor the proposed approach (e.g. by comparing to smaller versions of baseline models or only reporting weak baselines) it still underperforms compared to the baselines in most experiments. Somehow, based on these results the authors clam that "despite minimal inductive biases, our approach achieves competitive performance across all benchmarks".

### Strengths
The paper is relatively well written and easy to follow for a tech report. For a research paper the overall presentation is not satisfactory (e.g. huge chunks of related work are omitted entirely).

A comprehensive ablation study of the proposed approach is reported.

### Weaknesses
There are major omissions in the related work overview (and, as a results, in the evaluated baselines). Most importantly, the paper completely ignores prior work on visual representation learning via image and video generation with diffusion. This is the closest research direction to the method proposed here, is widely adopted for downstream computer vision tasks (e.g. Namekata et al., ICLR'24, Zhu et al., ECCV'24), and thus would serve as the most natural baseline, but the authors never even mention it. In fact, for some of the tasks evaluated in this paper (e.g. video object segmentation) StableDiffsuion representation is the de-facto state of the art, outperforming the proposed approach by leaps and bound on DAVIS, but the authors conveniently do not compare to it.

Another critical omission is existing auto-regressive methods for video generation (which go at least as far back as Weissenborn et al., ICLR'20, more recently there's Language Model Beats Diffusion: Tokenizer is key to visual generation by Yu et al.). In fact, the authors go as far as to claim extending the auto-regressive objective to videos as their contribution. Consequently, the authors do not compare their auto-regressive video generation approach to the similar state-of-the-art methods neither in terms of video generation quality nor in terms of the downstream performance. 

In the presented evaluations, when compared to the versions of the baseline objectives (e.g. MAE) with a comparable number of parameters, the proposed approach underperforms dramatically on most tasks (e.g. by ~10 accuracy points on ImageNet or by ~14 accuracy points on Kinetics). The only task on which a comparable performance to the state-of-the-art is demonstrated is action forecasting, which is hardly surprising given the proposed representation is trained with a forecasting objective. In fact, what is surprising is that even on this highly favorable task the propped representation doesn't show significant advantages over auto-encode objectives like MAE.

On some of the tasks the authors try to show competitive performance by only comparing to weak baselines. For example, on DAVIS they ignore sota approaches, and only compare to DINOv1 and MAE-base. DIFT (Tang et al., NeurIPS'23) outperforms the best version of the proposed approach by 13.3 points by capitalizing on the image diffusion objective (no video data in training). In the robotics experiments they only compare to the baseline representation from the paper that introduced the dataset in 2022, omitting even the representations evaluated in the other experiments in this paper (e.g. MAE or DINO). Same goes for the CATER experiments, only here the baseline is a ResNet from 2019.

As discussed above, the key claim of the paper that the proposed approach achieves competitive performance across all benchmarks is simply not true. There are also no technical contributions in this paper. In short, there is just no contribution.

### Questions
Please compare your approach to the state-of-the-art image and video generation representations (both via diffusion and via next token prediction) on all tasks. 

Please compare the video generation quality of your approach to the state-of-the-art. 

Please report actual sota representations on all tasks (e.g. by searching through the latest citations for the corresponding dataset papers if you are not aware of what these are). 

What is the contribution of your paper?

### Soundness
1

### Presentation
2

### Contribution
1
