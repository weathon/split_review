# TiC-CLIP: Continual Training of CLIP Models

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 5, 6

## Abstract
Keeping large foundation models up to date on latest data is inherently expensive. To avoid the prohibitive costs of constantly retraining, it is imperative to \emph{continually} train these models. 
This problem is exacerbated by the lack of any large scale continual learning benchmarks or baselines.
We introduce the first set of web-scale
Time-Continual (TiC) benchmarks 
for 
training vision-language models: \benchname{}, \cyfcc{}, and \credcaps{}. \benchname{}, our largest dataset, contains over 12.7B timestamped image-text pairs spanning 9 years (2014--2022).
We first use our benchmarks to curate various \emph{dynamic} evaluations to measure temporal robustness of existing models. We show OpenAI's CLIP (trained on data up to 2020) loses $\approx 8\%$ zero-shot accuracy on our curated retrieval task from 2021--2022
compared with more recently trained models in OpenCLIP repository. 
We then study how to efficiently train models on time-continuous data.
We demonstrate that a simple rehearsal-based approach that continues training from the last checkpoint 
and replays old data reduces compute by $2.}. 

\vspace{-10pt}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper creates the first set of webscale Time-Continual (TiC) benchmarks for training vision-language models: TIC-DataComp, TIC-YFCC, and TIC-RedCaps with over 12.7B timestamped imagetext pairs spanning 9 years (2014–2022). And they use their benchmarks to curate various dynamic valuations to measure temporal robustness of existing models.

### Strengths
The paper collects a large amount of dynamic data to study how to effectively train CLIP models continuously, ensuring the comprehensiveness of the research.

In order to ensure fairness in the evaluation, the paper has established a corresponding experimental protocol.

### Weaknesses
The dataset being solely focused on training CLIP may be somewhat limited. Can the article consider incorporating more vision-language models?

The YFCC100M dataset might be somewhat outdated in terms of the years it covers. It may be more representative to explore newer datasets for the research.

The fundamental issue of continual learning is catastrophic forgetting. If we fine-tune a small number of parameters (e.g., prompt tuning) in the CLIP model, is catastrophic forgetting a major concern? On the other hand, if we fine-tune a large number of parameters, resource limitations may become a factor. Therefore, from this perspective, is it necessary to construct such benchmarks?

### Questions
The fundamental issue of continual learning is catastrophic forgetting. If we fine-tune a small number of parameters (e.g., prompt tuning) in the CLIP model, is catastrophic forgetting a major concern? On the other hand, if we fine-tune a large number of parameters, resource limitations may become a factor. Therefore, from this perspective, is it necessary to construct such benchmarks?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces new pretraining datasets and dynamic downstream tasks for web-scale continual learning using CLIP on natural distribution shifts.

Datasets introduced by ordering metadata by time:
- **TiC-DataComp**: 12.7 billion image-text pairs from datacomp-xlarge ordered by first seen snapshot (monthly increments available from 2014-2022), with 7 timesteps from (2014-2016) and every subsequent year.
- **TiC-YFCC**: 15M image-text pairs on subset of YFCC100M which have captions and timestamps. Data from 2008–2014, with 4 timesteps involving (2008-2011) and every subsequent year.
- **TiC-RedCaps**: 12M image-text curated from Reddit in 2011-2020 ordered by creation timestamps of posts, with 4 timesteps (2011-2017) and three subsequent years.

Evaluation

**Static Tasks**: Zero-shot evaluation on a set of 28 downstream tasks similar to (Radford et al 2021)

**Dynamic Tasks**: On a small subset of samples reserved for testing at each timestep,
- (i) T2I retrieval for samples in a given timestep
- (ii) Classification on a LAIONNet-like 1000 class dataset (filtered by sentence embedding). Similar in nature to a scaled up CLEAR dataset. 

**Metric**: Use the checkpoint after every timestep and perform classification across different timesteps to evaluate In-domain Acc, Backward Transfer and Forward Transfer.

**Primary Findings**:
1) Continual training saves Cumulative* ~3x the cost for TiC-Datacomp compared to training-from-scratch (Oracle**), with a similar savings  shown for ImageNet IID-incremental.

2) Comparison between Sequential and Cumulative-all on TiC-Datacomp: This highlights sequential has
- significant catastrophic forgetting (low backward transfer performance)
- similar forward transfer performance – indicating catastrophic forgetting does not impact generalization to new distributions

This entails:
- poor performance static benchmarks, having poor backward transfer performance leads to a performance hit on static benchmarks which have old data (supported by other evidence: Fig 9&11)
- Consequently adding a memory buffer seems to help static tasks.
3) Patching helps a lot more than traditional continual learning methods like LwF when training without past data, indicating different continual learning approaches might help in these settings.

4) Different models work better for static and dynamic evaluation tasks.

### Strengths
S1) **Tackles an important problem** [Critical]: This work correctly highlights the need to shift focus in continual learning and introduces time-evolving benchmarks for evaluating continual pretraining which turns out is quite important. I really liked the dynamic retrieval and the classification task design. Retrieval captures performance shifts in time by new concepts and distribution shifts, whereas classification task ablates the performance gap caused due to new things (e.g. covid) by choosing the same 1000 classes

S2) **Insightful analysis** [Critical]: This work was a delight to read. I liked this work motivating a case where optimizing models for old datasets might lead to continuously worse performance on current-day tasks. Similarly, summary (4) indicates picking continual SSL training strategies based on downstream tasks might lead to poor design choices (best models worse than intended), shown in experiments on best-pool filtering.

S3) **High-quality work** [Critical]: The contributions seem fairly clear, experiments investigate interesting related claims well and experimentation is quite extensive.

### Weaknesses
W1) **Sequential and cumulative models behave quite differently between TiC-YFCC15M and TiC-Datacomp** [Critical]
- The paper nicely illustrates that YFCC15M has strong distribution shifts in Figure 15.
- However, does TiC-DataComp have significant distribution shifts?
    - The case for continually training CLIP primarily relies on Datacomp-like data having strong distribution shifts.
    - I suspect the case there is far weaker than YFCC15M (I am worried it's too small to make this setting exciting).
- Can the authors create a plot similar to Figure 15 for TiC-DataComp or some other mechanism to analyze distribution shift in TiC-Datacomp?

W1.1) Further unexplained variations between Sequential and -All:
- In TiC-YFCC15M and TiC-RedCaps, the performance of forward transfer is significantly affected, but that is not the case in TiC-Datacomp.
- Similarly, the gap between backward transfer and ID retrieval is far smaller between them in TiC-Datacomp. Why is this the case?

W1.2): Fig1 (mid) and Figure 10 present a different picture than Table 2.
- Comparing backward transfer retrieval to ID performance for Cumulative exp (oracle) in Table 2
    - Intuitively, ID performance should be higher (equal).
- To what degree is the drop in forward transfer attributable to tasks getting harder vis-a-vis encountering new distributions.

Hypothesis: Past tasks are easier! Can the authors help shed some light on why the difference?

W2) **Major results simply not present** [Critical]

I cannot find any results for LAIONNet-like dynamic classification task. Did I miss something?

Other missing ablations:
- a) “Same maximum LR works best across all runs when using cosine schedule” – Didn't find supporting evidence.
- b) “Warm up helps training on data from the first time step, but hurts on subsequent time steps.” – After correcting the minor shift issue, the table seems to robustly support the opposite conclusion. This seems surprising to me! I would have not expected warmup to help as the init is a very good one. Warmup mostly mitigates over-updating to high gradients when starting from a poor (random) init in my view.
- c) “Given a fixed buffer size for each past step, we observe minimal to no difference between random subsampling and other strategies.” – Didn't find supporting evidence.

W3) **Serious Design Flaws in Continual Learning Setup** [Critical]

W3.1) *4-7 timesteps are too few*
- I am worried the major findings would significantly change when tested on 20/50 timesteps but with the same computational cost per timestep, as the streams become far more non-i.i.d in that case.
- Why? Because of memory buffers become far smaller, that it becomes very hard in my experience to bridge the gap between CL methods and -all.
- Similarly, I am concerned there will be a far larger gap between -all and Oracle.

This critically affects some of the core findings presented in this work.

W3.2) *Is memory constrained?*
- For TiC-RedCaps and TiC-YFCC15M, all and exp/equal only differ at last timestep (Until timestep 3, they all can store all the data). This grossly undermines the comparisons as even at the last timestep, they still store 2/3rd of the data. It is very surprising that the difference in training for timestep causes such a big gap! If this is caused by D/3 data missing at the last timestep, the findings given 20-50 will probably be quite different!   
- This issue is mitigated in TiC-DataComp as at last timestep, equal would store D/3 samples per timestep (2D/6D) which is indeed much  smaller! (Minor note: Am I correct that buffer conserved here is 2.3x smaller, not the claimed 3.5x smaller? -- The replay+current is 3D/7D).

W3.3) *Replay buffers not utilized effectively, computation implicitly constrains memory.*
- I worry most of the decline in performance is due to random sampling, and hence wanted to see supporting evidence for W2.c). I make my case below:
- *Why?* This seems to be a case of imbalance data across timesteps due to the buffer constraints.
   - If trained without oversampling less-represented data, I am not surprised to see a bias against replay data (i.e. poor backward transfer).
- *Why not data loss constraining replayable sample?* I focus on TiC-Datacomp because there is a significant gap in replay buffers here
   - In TiC-Datacomp-medium, 35k iterations with 4096 samples barely allows ~1 pass through the 128M samples.
   - Hence, there seems to be a far stronger implicit memory constraint, as even after storing kD samples at timestep k, the network can only pass through 1/k fraction of samples from each past timestep at timestep k (training with oversampling).
   - Given a fixed buffer size, retaining equal samples of past data still stores 2/(k-1) samples which is far higher than the limitation introduced by computational constraints. It seems possible to train on mostly unique samples, mimicking -all.

Hence, the gap in performance between -equal and -all should have been minimal (which seems like a serious design issue-- alleviated by far smaller buffers in the 20-50 timestep setup discussed above). However, the fact that gap still exists seems to compound the issue, and I worry it is due to poor sampling.

W4) **Little discussion of past work despite similar findings/parallels** [Important]

Although I fully admit the dominant setups in CL are quite synthetic and need improvement, as correctly pointed out by the authors.
- (Cai et al., 2021) also has analysis covering several aspects of interest here, e.g. YFCC distribution shift plot (see their Fig 2), learning rate modulation, comparing impacts of replay buffer, web-scale training and similar compute constraints as here but on 600K timesteps. This avoids promoting CL methods which work only on a short timescale and degrade quickly when scaled beyond 5-20 timesteps (i.e. my worry about the 4-7 timesteps). 
- Finding (1) on Imagenet IID seems out-of-place here, and has detailed precisely in several works, e.g. “Computationally Budgeted Continual Learning: What Does Matter?”, CVPR23. Other works like “One Pass ImageNet” NeurIPS-W 2021 have analysis on Sequential/Cumulative variants as discussed here on Imagenet but these papers are not discussed.
- Other works which have interesting investigations with computational limits (Bornschein et al., 2022) and (Jang et al., 2022) have nice analysis quite relevant to this work. E.g. hyperparamter optimization as a cost in the compute budget C (will be required when training in the unknown)

### Questions
Q1) What is the size of dynamic retrieval and LAIONNet test sets per chunk?

Minor Comments: (Not considered for score)

C1) Metric
- The backward and forward transfer metric utilized here seems to be from (Lin et. al., 2021).
- (Lopez-Paz & Ranzato, 2017) have a very different metric for backward and forward transfer, while (Díaz-Rodríguez et al., 2018) do not introduce any modification to this metric.

Overall, I strongly agree with the motivations and findings from analysis (filtering, CLIP vs OpenCLIP) presented. I worry the continual learning experiments made poor design choices which might seriously impact most of the major findings in this work (W1, W3). If addressed, I will be very happy to increase my score. 

Note: I tried to detail why the ask, primarily to minimize superfluous asks which I find annoying from reviewers on my submissions (Did not mean to sound pretentious).

[Edit]: Increased score from 3 to 8 and soundness from 1 to 4, as additional analysis resolve my pointed concerns.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a benchmark for continual learning using large pretrained vision-language models, e.g., CLIP. The authors construct multiple datasets with timestamp information to evaluate the performance of existing methods on time-continuous data. The experimental results show that the rehearsal-based approach can reduce computation while achieving similar performance as the oracle algorithms.

### Strengths
1. The authors construct multiple datasets with time information based on existing datasets for continual learning settings. This is an non-trivial contribution for continue learning to evaluate the effectiveness of algorithms when facing natural distribution shifts.
2. This paper is well-written and easy-to-follow.

### Weaknesses
1. This benchmark lacks various types of continual learning methods [1]: elastic weights consolidation methods, progressive neural network methods, dynamic architecture methods, etc. Therefore, the experiments of this benchmark is relative weak and insufficient. 
2. This paper lacks some in-depth analysis of vision-language models solving continual learning. Vision-language models enable various novel model tuning paradigms, such as prompt tuning, vision prompt tuning, parameter-efficient tuning, etc. If these aspects are ignored when discussing the solving of continual learning with the CLIP model, then this benchmark is a bit over-claimed.

### Questions
Please refer to questions in weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a study on training CLIP with time-evolving data in an incremental manner. The authors timestamp the training data spanning 2014-2022, treating each timestamp as a distinct incremental learning step. Their analysis delves into the backward and forward compatibility of CLIP as it undergoes training, leading to some findings.

Firstly, the research demonstrates that employing simple small replay techniques effectively mitigate forgetfulness, an insight in the context of continual learning. Secondly, the study reveals an unsurprising yet noteworthy performance gap: CLIP underperforms on future, unseen data.

------------------------- After Rebuttal ----------------------------------------------------------------------------------------------

Dear authors, 

I did not imply linear probing, but more downstream task adaptation, since CLIP has been applied to almost all computer vision tasks by now. 

I went through all the reviews and the rebuttal. I was optimistic about this paper prior to rebuttal. My optimism remains.

### Strengths
S1:
This paper addresses a critical and, to the best of my knowledge, an open issue in continual foundation model training. The challenge lies in the impracticality of re-training large foundation models like ChatGPT or CLIP, highlighting the necessity for continual learning solutions. Despite this urgency, there's a notable absence of organized datasets for the community to tackle this problem. While the CLEAR benchmark exists, it has not gained traction and lacks essential components like Web captions. This benchmark, being a captioned version of CLEAR that evolves over time, fills a gap, offering a valuable resource for researchers in the continual learning domain.

S2:
The authors conduct insightful analyses using fundamental regularization and replay techniques. Unsurprisingly, the results show that preserving and replaying a portion of the data during incremental learning effectively mitigates forgetfulness. This empirical validation underscores the importance of such techniques in preserving model performance over time, providing a practical and valuable contribution to the field.

S3:
The paper's central discussion on the fine-tuning cost in terms of compute MAC carries some value. This perspective equips researchers with a framework to explore low MAC solutions, emphasizing a nuanced approach rather than blindly minimizing the forget ratio.

### Weaknesses
W1: No method, only benchmarking

The paper is commendable in its focus as a benchmark study, emphasizing data and existing baselines without introducing new methodologies. The utilization of well-known and straightforward baselines is executed competently. However, the paper could have significantly bolstered its strength by incorporating benchmarks from related works such as Continual-CLIP [1] and the methods outlined in "Robust fine-tuning of zero-shot models" [2]. Including these comparisons would have provided a more comprehensive evaluation, highlighting the benchmark's effectiveness in contrast to existing state-of-the-art approaches.

W2: No fine-tuning, only pre-training

An additional area of improvement lies in the paper's scope, particularly concerning the fine-tuning stage. While the study adeptly focuses on the continual pre-training phase, it would have been more insightful and impactful to extend the analysis to the fine-tuning stage. Specifically, investigating how well the obtained checkpoint at a given time transfers to standard vision benchmarks, beyond simple retrieval tasks, would have provided a more nuanced understanding of the model's performance. This consideration is essential for gauging the real-world applicability and adaptability of the continual learning approach outlined in the paper.

### Questions
No questions so far.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
