# The Brain's Bitter Lesson: Scaling Speech Decoding With Self-Supervised Learning

- Decision: Reject
- Scores: 6, 5, 6

## Abstract
The past few years have produced a series of spectacular advances in the decoding of speech from brain activity. The engine of these advances has been the acquisition of labelled data, with increasingly large datasets acquired from single subjects. However, participants exhibit individual differences, such as anatomy, and datasets use varied scanners and task designs. As a result, prior work has struggled to leverage data from multiple subjects, multiple datasets, multiple tasks, and unlabelled datasets. In turn, the field has not benefited from the rapidly growing number of open neural data repositories to exploit large-scale data and deep learning. This gap exists for all neural data, but especially for magnetoencephalography (MEG), where the scale of individual datasets has not yet caught up with other modalities. To address this, we develop a set of neuroscience-inspired self-supervised objectives, together with a neural architecture, for representation learning from heterogeneous and unlabelled neural recordings. Experimental results with MEG show that representations learned with these objectives scale with data, generalise across subjects, datasets, and tasks, outperform using the raw input representation, and even surpass comparable self-supervised approaches. In addition, we set new benchmarks for two foundational speech decoding tasks. Collectively, these methods now unlock the potential for training speech decoding models with orders of magnitude more existing data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The manuscript describes a pipeline for self-supervised learning for  Magnetoencephalography (MEG) datasets. They introduce three pretext tasks predicting hand-designed perturbations of the input signal, predicting either 1) which frequency band was removed via bandstop filter (band prediction); 2) how much the phase was shifted in a random subset of sensors (phase shift prediction);  3) how much the amplitude was scaled in a random subset of sensors (amplitude scale prediction).  
They use the medical Cam-CAN MEG dataset as the unlabelled self-supervised dataset and evaluate on speech detection and voice classification as downstream tasks for which the self-supervised-trained model is finetuned. Results show improvement over a linear baseline, no pretraining and a reimplemented self-supervised baseline from prior work. THey find combining all three pretext tasks outperforms any single one. Furthermore, increasing unlabelled pretraining data improves downstream performance.

### Strengths
* Presentation is good, writing is understandable, if a bit longwinded at times, figures are professional and everything is legible
* motivation and main idea is straightforward and clear
* results for varying unlabelled dataset sizes are interesting

### Weaknesses
The scientific value of such a manuscript is highly dependent on the presented comparisons to other works as well as the comparability of the current results for future works.

For the failed BIOT experiments, is it possible to obtain a pretrained BIOT model and apply it, potentially to a subset of electrodes?

For the   [[2405.18765] Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI](https://arxiv.org/abs/2405.18765)  work, a comparison to this may be very helpful. I think (not sure) they also have pretrained models available.

Is it possible to compare to the to existing results for the downstream tasks like the Defoussez works for example?

In general, reporting further metrics other than AUROC that allow more direct comparisons to other speech decoding works would be crucial to better understand the performance of the proposed approach.

Minor: [[1911.05419] Self-supervised representation learning from electroencephalography signals](https://arxiv.org/abs/1911.05419)  might be  another relevant work utilizing different pretext tasks.

### Questions
The phase perturbation, how is it done? Is it applied in the frequency domain to all frequency bins? Did you consider only shifting randomly selected bands like gamma alpha etc.? Same for the amplitude scaling.

The subject conditioning, how does it work exactly, it is only trained during pretraining as far as I understand from the figure? So when you have a new dataset fora  new subject what exactly do you need to compute?

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
5

### Summary
The manuscript reports on an attempt to improve MEG decoding by pretraining on unlabelled data.  In particular, the authors focus on two binary classification tasks: speech detection and voicing detection.  In the pretraining (pretext) task, the input MEG signal is either phase shifted on randomly selected sensors (by a single, random, discrete phase); amplitude scaled at random sensors (by a single, random, discrete scalar); or bandstop filtered at a single random frequency band.  The network is trained to classify which phase shift, amplitude scaling, or filter was applied.  The authors report that pretraining improves performance on the binary-classification tasks, with simultaneous training on all three pretexts yielding the best results.  Performance on data from subjects not in the fine-tuning training set also improves with number of data used in pretraining.

### Strengths
The result is statistically significant and novel in the area of MEG, at least to this reviewer's knowledge.  The pretext tasks are potentially applicable to other neural recording modalities (e.g., scalp and intracranial EEG).

### Weaknesses
(1) The amount of information being extracted from the MEG signals under even the best models is very low. The best AUC achieved on these binary-classification tasks is ~0.62 (chance being 0.5). This kind of performance on speech *detection* does not inspire confidence in the ability of MEG to scale up to actual decoding of words (to say nothing of the fact that it is perceived, rather than attempted, speech that is being decoded). The authors describe performance as scaling linearly in the log of the number of hours of data, which might seem to give some hope for BCI application. But (eyeballing Fig. 4) the slope is around 0.025 in AUC per order of magnitude, at which rate something like 10^32 hours of data would be required to reach 90% AUC on *speech detection* (assuming the linearity held out that long). And these are the stongest results in the MS. The use of multiple datasets in pretraining does not improvement classification performance on the Armeni data at all (Table 2), and the improvement from the Gwilliams data does not appear likely to be statistically significant (the authors should certainly test this). In short, the results are not encouraging for the use of MEG in speech decoding.

(2) There are lots of other models attempting to use self-supervised learning on EEG and the like (i.e., in addition to BIOT), e.g.,

Brant (https://proceedings.neurips.cc/paper_files/paper/2023/file/535915d26859036410b0533804cee788-Paper-Conference.pdf)
BrainBERT (the authors reference this study)
MMM (https://openreview.net/pdf?id=hiOUySN0ub)
BENDR (https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.653659/full)
LaBraM (the authors reference this study)
EEGFormer (https://arxiv.org/abs/2401.10278)

I don't think the authors need to have compared to all of these, but since BIOT seems to have failed entirely (chance performance), surely they could have tried one of these others instead.

MINOR
There are at least two ECoG studies of speech decoding that do train single models on multiple subjects' data: Anumanchipalli et al., Nature, 2019; and Makin et al., Nature Nueroscience, 2020.

### Questions
I take it Table 1 is for speech detection (as opposed to voicing).  (I don't see this is the caption or text but I may have missed it.)  If that's right, how does voicing detection compare?  Likewise for Table 2 (although this is clearly labeled "speech detection").

Are the differences between "band-only" pretraining and "all tasks" statistically significant?  (This seems unlikely, at least for the Gwilliams data, since N=3.)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
- In short, the proposed approach uses self-supervised training on MEG data to improve downstream MEG-to-speech decoding. New pretraining tasks are proposed, with a focus on building a model that can learn from many different subjects and perform decoding on many different subjects. The authors find that the pretraining improves decoding over naive baselines and that increasing the amount of pretraining data leads to increased performance.

### Strengths
- There are other pretraining approaches for learning representations of brain data. But there is novelty in that the application (decoding speech from MEG) seems new. 
- The approach is sound.
- The proposed pretraining tasks are all validated by ablation studies. The authors motivate the proposed tasks with neuroscience insights. 
- The scaling results are promising for speech applications, especially for held-out subjects. I have concerns about novelty (see weaknesses) but these are tempered by the fact that at the very least, the proposed approach seems effective.

### Weaknesses
 - While the application to MEG speech decoding is novel, there is limited novelty in the technique. Self supervised training for learning neural representations has been studied before, even for subject-generic representations, which is the main claim to novelty for this work. For example, [1,2,3,4] present subject generic approaches and use self-supervised training. And [5] presents a neuron-generic approach, but with the same principles. This is without mentioning all the work for foundational time-series models that exist in general. Given the existing work, it seems that the way for new work to distinguish itself is either to (1) show a downstream application of pretraining in a new domain or (2) show that the proposed pretraining tasks are different and more effective than others that exist. This work has (1) covered, but leaves (2) disputable. The proposed pretraining tasks share similarities with existing tasks (replace-discriminative learning from [4] or frequency phase forecasting from [1]). The formulations are not the exact same, but given that similar approaches exist, it seems that a new approach should justify why a different set of pretraining tasks is necessary.
- BIOT is used as a baseline. But it seems to be just the off-the-shelf version, without adaptation to the MEG domain (did I misunderstand? see questions section). So it's not fair to say that this approach is better than the complete BIOT self-supervised approach. 
- The band prediction task seems unmotivated. The fact of presence/absence of information in a certain frequency band doesn't seem like semantic information. Importantly, it doesn't seem like the sort of task which encourages the model to learn anything specific about the distribution of neural activity. The ablation test shows that it is useful to performance, which is believable, since it could encourage some useful attention to low-level features, but there are many other plausible tasks that could fill this role.

### Questions
- What is the nature of the subject conditioning on line 207? Is it a concatenated prompt vector? Some sort of fine-tuning?
- What is the downsampling rate from $t$ to $\tau$ (line 203)?
- Eq. 4 describes weightings $w_i$. Is anything other than a uniform weighting used?
- Line 326 suggests that BIOT was taken off-the-shelf (?) But Line 363 suggests that it was pre-trained on Cam-CAN?

### Soundness
3

### Presentation
3

### Contribution
2
