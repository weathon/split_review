# BarLeRIa: An Efficient Tuning Framework for Referring Image Segmentation

- Decision: Accept
- Scores: 6, 8, 8

## Abstract
Pre-training followed by full fine-tuning has gradually been substituted by Parameter-Efficient Tuning (PET) in the field of computer vision. PET has gained popularity, especially in the context of large-scale models, due to its ability to reduce transfer learning costs and conserve hardware resources. However, existing PET approaches primarily focus on recognition tasks and typically support uni-modal optimization, while neglecting dense prediction tasks and vision language interactions. To address this limitation, we propose a novel PET framework called **B**i-direction**a**l Inte**r**twined Vision **L**anguage Effici**e**nt Tuning for **R**eferring **I**mage Segment**a**tion (**BarLeRIa**), which leverages bi-directional intertwined vision language adapters to fully exploit the frozen pre-trained models' potential in cross-modal dense prediction tasks. In BarLeRIa, two different tuning modules are employed for efficient attention, one for global, and the other for local, along with an intertwined vision language tuning module for efficient modal fusion.
Extensive experiments conducted on RIS benchmarks demonstrate the superiority of BarLeRIa over prior PET methods with a significant margin, i.e., achieving an average improvement of 5.6\%. Remarkably, without requiring additional training datasets, BarLeRIa even surpasses SOTA full fine-tuning approaches. The code is available at https://github.com/NastrondAd/BarLeRIa.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors have proposed a novel intertwined vision language efficient tuning algorithm based on the large-scale CLIP model. They claim that the previous methods overlook adapting the biased feature from pre-trained models and global prior regularization. The proposed method achieves state-of-the-art performance on RefCOCO, RefCOCO+, and G-Ref.

### Strengths
1. The proposed method brings a few trainable parameters into CLIP for both feature adaptation and modal fusion, which achieves the best performance on several RIS datasets.
2. The proposed method utilizes a novel intertwined structure to assist modal feature fusion.

### Weaknesses
1. The global prior is predicted after the vision-language blocks. Then, the global prior is input to the global shortcut tuning module. However, such a design is quite a long path. The inference speed may be very slow.
2. The comparison with other methods may be unfair. The proposed method utilizes ViT-Large as its backbone.
3. The dimensions and meanings of different symbols are not introduced in the paper, such as [Fl, Fv].
4. The decoder is not introduced in this paper. Although the authors have claimed they follow previous works, it is not detailed enough.

### Questions
Could you provide any results of the inference time compared with other parameter tuning methods?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the problem of using parameter efficient fine-tuning in referring image segmentation (RIS). A sophisticated PEFT paradigm is proposed, consisting of Adapting Shortcut with Normalizing Flow (SNF),  Local Intertwined Module (LIM), and Global Shortcut Tuning (GST). Results are presented on commonly used RIS benchmarks of RefCOCO, RefCOCO+, and G-Ref. A detailed evaluation shows superior results of the proposed method over previous PEFT method in RIS.

### Strengths
- The paper is well written. Adequate background is provided, the literature review covers very recent approaches, and the paper provides necessary background to the required concepts.
- It seems novel to me to use a small side network that takes text+image features with attention and output side features containing global priors. And the ablation study shows a significant improvement with this module.
- The proposed approach gets strong results that beats the previous parameter efficient fine-tuning approach in RIS.
- The paper conducts a thorough ablation study to show the effectiveness of each proposed module.

### Weaknesses
 - Writing in Section 3.3 and 3.4 is not clear enough. It should be possible to write in one equation for (2)(3)(4) with a better subscription. Also it's a bit unclear whether $F_v^i$ is the same as (the $i^{th}$) $[cls, embed]$.
- (typo): it should be intertwine not interwine in Figure 2.
- The description of the Global Shortcut Tuning Network lacks clarity regarding its operational mode relative to the main vision/language encoder. Specifically, it's unclear if this network operates in parallel or sequentially. Furthermore, the necessity of caching each $F_v^i$ for the side network raises concerns about the computational overhead, which is not adequately addressed in the paper. The paper should provide a more detailed analysis of the time and memory costs associated with this caching mechanism, particularly in comparison to other parameter-efficient fine-tuning methods.

### Questions
Does the side network (Global Shortcut Tuning Network) not operate in parallel with the vision/language encoder? And is it required to cache each $F_v^i$ for the side network? If so, what is the extra time and memory cost for this approximately?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel Parameter-Efficient Tuning framework for Referring Image Segmentation. By designing a bi-directional intertwined vision-language adapter, this frame exploits the frozen power of pre-trained vision-language models. In addition, this paper introduces a Global Prior Module and a Global Shortcut Tuning Network to extract global prior from text input to regularize the visual feature.
Combining these contributions, this paper outperforms previous parameter-efficient tuning methods on RIS benchmarks and even surpasses SOTA full fine-tuning approaches on several tasks of RIS benchmarks.

### Strengths
* Strong performance on three referring image segmentation benchmarks.
* The well-designed Local Intertwined Module: according to the Table 4: Local Intertwined Module improves can outperform ETRIS with very small amount parameters.

### Weaknesses
 * The limited improvement brought by Global Shortcut Tuning.  According to Table 5, Compared with No Global, BarLeRIa achieves 72.2 on RefCOCO using 2.21M, while without GST, the model achieves 71.4 using 0.39M. It seems that the model without GST owns a better balance between performance and parameters.


### Questions
* See in Weaknesses.
* Is any possible to provide the training time comparison between ETRIS and BarLeRIa?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
