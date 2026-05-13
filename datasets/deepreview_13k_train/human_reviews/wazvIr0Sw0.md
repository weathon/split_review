# OpenDAS: Open-Vocabulary Domain Adaptation for Segmentation

- Decision: Reject
- Scores: 3, 6, 5, 5

## Abstract
Recently, Vision-Language Models (VLMs) have advanced segmentation techniques by shifting from the traditional segmentation of a \emph{closed-set} of predefined object classes to \emph{open-vocabulary} segmentation (OVS), allowing users to segment 
\emph{novel} classes and concepts unseen during training of the segmentation model.
However, this flexibility comes with a trade-off: fully-supervised closed-set methods still outperform OVS methods on \emph{base} classes, that is on classes on which they have been explicitly trained.
This is due to the lack of pixel-aligned training masks for VLMs (which are trained on image-caption pairs), and the absence of domain-specific knowledge, such as autonomous driving.
Therefore, we propose the task of \textit{open-vocabulary domain adaptation} to
infuse domain-specific knowledge into VLMs while preserving their open-vocabulary nature. By doing so, we achieve improved performance in base \emph{and} novel classes.
Existing VLM adaptation methods %, when applied to segmentation tasks,
improve performance on base (training) queries,
but fail to fully preserve the open-set capabilities of VLMs on novel queries.
To address this shortcoming, we combine parameter-efficient prompt tuning with a triplet-loss-based training strategy that uses auxiliary negative queries.
Notably, our approach is the only parameter-efficient method that consistently surpasses the original VLM on novel classes.
Our adapted VLMs can seamlessly be integrated into existing OVS pipelines, e.g., improving OVSeg by
+$6.0\%$ mIoU on ADE20K for open-vocabulary 2D segmentation, and OpenMask3D by +$4.1\%$ AP on ScanNet++ Offices for open-vocabulary 3D instance segmentation without other changes.% to these methods.

\vspace{-10pt}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces the task of domain adaptation for language-vision models in open-vocabulary 2D and 3D segmentation. In this framework, language-vision models are fine-tuned in a weakly supervised manner to enhance performance on domain-specific segmentation tasks.

The authors propose a method specifically tailored for the CLIP architecture. A pretrained CLIP model is extended by adding trainable prompts to the inputs of selected layers in both the textual and visual encoders, with the number of layers modified as a hyperparameter. The optimization process occurs in two phases. In the first phase, only the visual prompts are trained: an image passes through the visual encoder, while a set of domain-specific labels—comprising both positive and ChatGPT-generated negative queries—passes through the textual encoder. A cross-entropy loss is used to bring the image embedding closer to the correct textual embedding. In the second phase, only the textual prompts are trained, using a combined cross-entropy and triplet loss. For the triplet loss, a hard negative sample mining strategy is employed to refine results.

The authors conduct experiments on both 2D and 3D segmentation tasks, along with ablation studies to analyze the impact of different components in the proposed approach.

### Strengths
S1) Paper is clearly written

S2) Experimental results demonstrate improvements over baseline CLIP performance when integrated with the OVSeg model. Additionally, the proposed prompt-learning method for specializing vision-language models (VLMs) outperforms alternative approaches

### Weaknesses
W1 The paper diverges from the established definition and test setup for open-vocabulary segmentation. While previous studies assume that a segmentation model fine-tuned on one domain should retain its generalizability across other domains, this work fine-tunes on a more general domain and evaluates on a narrower domain. Consequently, the test setup is not directly comparable to previous open-vocabulary approaches, such as those in (Liang et al. 2023)

W2 The fine-tuning approach assumes access to densely labeled, domain-specific images, which differs from previous domain adaptation frameworks that often use self-supervised or student-teacher setups. Here, the fine-tuning process effectively performs domain-specific classification training.

### Questions
1) What are the relations between ADE20K, SN++ Offices and KITTI-360 classes in Table 2?
2) Were the image segments used for "domain adaptation" obtained from densely labelled images?

### Soundness
2

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
5

### Summary
This paper introduces OpenDAS, a novel approach to open-vocabulary domain adaptation (OVDA) for 2D and 3D segmentation. Traditional segmentation models are typically limited to closed-set vocabularies, lacking flexibility for novel classes or domain-specific knowledge. OpenDAS addresses this by adapting Vision-Language Models (VLMs), such as CLIP, to domain-specific segmentation tasks without sacrificing their open-vocabulary capabilities. The authors propose a method combining prompt tuning with a triplet-loss-based training strategy, incorporating auxiliary negative queries to boost generalization to novel classes within a target domain. OpenDAS integrates seamlessly with existing segmentation models, such as OVSeg for 2D and OpenMask3D for 3D segmentation, and experimental results show significant improvements over baseline methods on various benchmarks.

### Strengths
* It defines a new task that adaptes VLMs to domain-specific segmentation tasks while preserving open-vocabulary capabilities.

* Extensive experiments demonstrate adaptability for both 2D and 3D segmentation tasks, improving performance on existing pipelines without extensive modifications.

### Weaknesses
 * The proposed framework is engineering, because the triple loss, visual and textual prompt tuning are common ways in open-vocabulary and domain adaptation communities.

* More recent vision-language models should be compared, like SigLIP, llama, etc.

* Several ablation studies are needed, like the discussion about the margin $\mu$.

* The writing and structure should be further improved, e.g., the pipeline fig is a bit ambiguous.

### Questions
Please see weaknesses.

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
This submission tends to address the task of the open vocabulary domain adaptation to infuse domain specific knowledge into vision language models. Extensive experiments are conducted.

### Strengths
The motivation in this paper is convincing, addressing the issue of the lack of pixel-aligned training for pre-trained VLMs.

### Weaknesses
1) The "lack of pixel-aligned training masks for VLMs (which are trained on image-caption pairs)" has been extensively studied in previous work [1, 2]. The authors should analyze and compare with [1, 2], even though they use different optimization strategies

2) This work introduces the concept of Domain Adaptation in OVS. The authors need to clarify the distinction between Domain Adaptation OVS and standard OVS. OVS itself can segment any text and has a general concept of data domains. In experimental settings, the authors use cross-dataset evaluation, which does not differ from the standard OVS settings.

3) In Table 3, the authors only compare with the CVPR23 work, which is insufficient. The latest OVS works [3, 4, 5] should be included for comparison.

4) I have questions about the process of using GPT to generate Negative Queries (specifically the example from "ceiling" to "ceiling fan" in L303). Does this require image input? If only text input is provided, I believe GPT would return synonyms instead.

5) Minor Weaknesses: The writing contains redundancy and needs optimization. e.g., L227-231 does not describe the authors' proposed method; I suggest placing this part in Sec. 4.1.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a new task called open-vocabulary domain adaptation for segmentation. The goal of this task is to improve the recognition performance of vision-language models on a specific domain, while preserving the open-vocabulary recognition capabilities. The proposed method relies on paramater efficient prompt tuning with a combination of cross-entropy and triplet loss. The success of adaptation is measured as classification performance on masked images containing a single segment corresponding to either base or novel semantic class. The experiments are conducted on 2D and 3D segmentation on three different datasets.

### Strengths
The proposed method outperforms other adaptation methods on segment classification on both base and novel classes on different benchmarks.
The experiments reveal that the proposed method can also improve the segmentation performance when combined with two existing open-vocabulary segmentation models.

The proposed adaptation approach is simple, sound and effective.

### Weaknesses
In my opinion, task name is missleading. The adaptation procedure actually optimizes segment classification (images containing individual segments), while it assumes there is a mask proposal generator available. More precisely, it assumes perfect mask generator both during training and evaluation. The term "open-vocabulary segmentation" implies both localization (mask proposal generation) and classification. Because of that, I was confused while reading the manuscript all the way until section 5 and the description of evaluation metrics. I think that this difference must be clearly stated and thoroughly described earlier in the manuscript.

The manuscript lacks a proper comparison with the related work from open-vocabulary segmentation. Table 3 shows that the adapted model can be used to improve performance of the open-vocabulary segmentation model OVSeg. However, the table shows results only for the ADE20k validation set which contains only in-vocabulary (base) classes, while it is usual to evaluate the performance on datasets with different vocabularies. Furthermore, OVSeg significantly lacks in performance for the current SOTA models (e.g. CatSeg (Cho et al.,2023) or FC-CLIP (Yu et al., 2024)).

The proposed approach is computationally inefficient. For a single full image segmentation it requires multiple forward passes through CLIP backbone in order to classify all the mask proposals. This causes a lot of overhead due to processing potentially overlapping (or empty) image regions. On the other hand, some open-vocabulary segmentation methods avoid this by extracting features with CLIP backbone once, and then pooling these features for each mask (FC-CLIP, OpenSeg, ODISE). The proposed approach might also hurt the classification performance by removing the context (background) from each segment image. It is not clear what are the real performance relations between the two mentioned approaches. Hence, the proper comparison with related methods from open-vocabulary segmentation is necessary.

It is unclear if other open-vocabulary segmentation methods which do not rely on image segment classification (e.g. FC-CLIP) could benefit from the proposed adaptation. This needs further investigation.

### Questions
/

### Soundness
3

### Presentation
2

### Contribution
2
