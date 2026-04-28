# Slot-Guided Adaptation of Pre-trained Diffusion Models for Object-Centric Learning and Compositional Generation

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 6, 8

## Abstract
We present SlotAdapt, an object-centric learning method that combines slot attention with pretrained diffusion models by introducing adapters for slot-based conditioning. Our method preserves the generative power of pretrained diffusion models, while avoiding their text-centric conditioning bias. We also incorporate an additional guidance loss into our architecture  to align cross-attention from adapter layers with slot attention. This enhances the alignment of our model with the objects in the input image without using external supervision. Experimental results show that our method outperforms state-of-the-art techniques in object discovery and image generation tasks across multiple datasets, including those with real images. Furthermore, we demonstrate through experiments that our method performs remarkably well on complex real-world images for compositional generation, in contrast to other slot-based generative methods in the literature.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to incorporate object-centric information into the pre-trained diffusion models. Specifically, they argue that previous works have struggled with text-conditioning bias even though they can leverage the potential of pre-trained diffusion models. To eliminate the text-conditioning-related bias, the authors propose SlotAdapt, which utilizes the adapter layers for the condition with slot, to enable the incorporation of diverse slot conditions. For their design choice, T2I adapter design and register tokens-like approaches are introduced. Then, they also use cross-attention masks for better conditioning, which enables a dual path of guidance for the diffusion models and masks. Through their experiments, they present various benchmarks and comparisons with previous object-centric methods to validate the effectiveness of their method.

### Strengths
- The major strength is the performance of the proposed method. In their benchmark, their method significantly outperforms the baseline.
- The paper is well-written and easy to follow.

### Weaknesses
 - W1: A significant concern with the proposed method is its novelty. While the object-centric approach may offer a fresh perspective within the realm of object-centric learning, the use of adapter layers is a well-established technique in diffusion fields, widely known to be effective. This familiarity may make the method appear somewhat trivial or lackluster in terms of innovation for diffusion model applications.

- W2: Additionally, the paper lacks an ablation study, which is critical for understanding the impact of the guidance loss on the model’s performance. Specifically, it would be insightful to see how the model behaves without the guidance loss, as this could further clarify the contribution of each component in the proposed approach.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces SlotAdapt, an object-centric learning method that integrates slot attention with pre-trained diffusion models using adapter layers for slot-based conditioning. This work can significantly avoid biases generated from the text-centric conditioning models. The proposed adapter layers with slot attention can enhance the model's alignment with image objects without external supervision.

### Strengths
Introducing adapter layers for slot-based conditioning enables the model to deviate from text embedding space representations while preserving the generative capabilities of pre-trained diffusion models.

The compositional image generation results on complex real-world images demonstrate the effectiveness of the model in handling compositional generation tasks.

### Weaknesses
The paper inconsistently uses both "UNet" and "Unet" to refer to the U-Net architecture. It is advised that the authors adhere to the standard capitalization "UNet" consistently across the document. Additionally, it is recommended to introduce the term "register token" earlier in the paper to establish its significance and reducing confusion. It is crucial for the authors to perform a thorough review and correct grammar and syntax problems.
The reconstructed images may exhibit slight changes or artifacts comparing to the source image. This issue might be attributed to over-segmentation, which could lead to the misrepresentation of certain image components during the generation process.

### Questions
How can the authors demonstrate that the unique contributions of their model extend beyond the use of adapters, which are becoming increasingly common in the LDM？
The paper's outcomes appear heavily reliant on segmentation quality. Could the authors clarify if the model's success is primarily due to the performance of segmentation, and whether integrating a superior segmentation method could achieve similar results?

### Soundness
2

### Presentation
2

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
This paper introduces an object-centric learning approach, SlotAdapt, with the focus on scaling to real-world dataset. Instead of directly frozening or fine-tuning the pretrained stable diffusion model, SlotAdapt adds an adapter module on top of pretrained stable diffusion so that the learned slots are not strictly limited to lie in the text embedding space, enabling better slot-object alignment for real world images. The resulted flexibility of slots is traded with an additional module, Adapter, needing to be trained when compared with the frozen pretrained stable diffusion case. SlotAdapt also self-supervises slot attention maps with cross-attention maps for semantic alignment. Experiment results show improvements on the segmentation performance.

The main contribution of this paper comes from the architecture design.

### Strengths
1. The writing is smooth and easy to follow

2. The paper is tackling an important problem in the object-centric learning community, i.e., pushing the boundary of object-centric learning approaches towards real world images, and shows some non-trival improvements on the segmentation performance.

3. The proposed approach is straightforward and effective by borrowing and combining ideas from LSD and T2I adapters without requiring additional supervision. It largely benefits from the prior knowledge stored in pretrained stable diffusion models while allows flexible representation learning ability of slots.

### Weaknesses
1. This paper claims, "Our method performs remarkably well on complex real-world images for compositional generation, in contrast to other slot-based generative methods in the literature." However, only qualitative results are provided, even without a comparison with existing approaches. It should be noted that existing approaches like LSD [1] and Slate [5] can already perform compositional generation on real world datasets like FFHQ in Figures 3, 4, and 10 https://arxiv.org/pdf/2303.10834. Comparing your approach with LSD and/or other approaches on Movi-E or COCO is necessary to support your claim. Otherwise, the sentence should be revised. Similarly, quantitative scores like FID are helpful to demonstrate the statements on high fidelity generation in the section "Generation and Compositional Editing".

2. For the guidance strategy, the FG-ARI in Table 2 shows that guidance doesn't help a lot for segmentation, while Fig 2 qualitatively illustrates that guidance might help a bit. Are the qualitative results of Fig 2 possibly due to random seeds used in the experiments? Is there any intuition that guidance can help avoid over-splitting? After all, there is no external supervision, it is possible that both slot attention map and cross attention map oversplit. Furthermore, in section 4.1, it says "In turn, the generated (reconstructed) images are more faithful to the original input images", which is not that persuasive depending on what you focus on (the clothes of base ball player, the closets and ceiling lamp).


3. There are several overclaims in the paper. For example, in Figure 5, it says "SlotAdapt generates nearly perfect reconstructions" while the figure shows that details are still largely different between GT and reconstruction. In Abstract and Conclusion, it claims outperforming baselines in compositional generation; however, there is no qualitative and quantitative comparison in any section in compositional generation.

4. Now that the paper is titled with Compositional Generation, some relevant reference, such as [2][3][4] etc., are suggested to be discussed in related works though not directly compared.

5. Limitation discussion. (1)  LSD paper finds that their approach shows significant gains in complex naturalistic scenes but a somewhat diminished performance in terms of segmentation and representation when the dataset consists of only visually simple and monotonous scene images like CLEVR. Does SlotAdapt share similar limitation when it comes to simple scenes like CLEVR or CLEVRTex? (2) Although adopting pretrained stable diffusion models allows using prior knowledge to improve segmentation performance on real-world images like COCO,  it on the other hand might limit the model's ability to discover per-dataset components, for example facial slots in LSD [1].

### Questions
1. Does the number of slots used in the experiments have an impact on the part-whole results? For COCO dataset, do you simply assume the slot number is 80? In that case, is the training slow?

2. Looks like the quantitative scores of baselines in Table 3 are directly copied from LSD paper. In that case, it should be guaranteed that the experimental settings of yours and that of LSD paper are identical for fair comparison.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes SlotAdapt, a novel approach to leverage large-scale pre-trained diffusion models (DMs) for the task of object-centric learning (OCL). There are priors work trying to combine OCL with DMs, yet they usually just treat slots as text embeddings, and directly input them to the cross-attention layer in the diffusion U-Net. SlotAdapt instead inserts a new adapter layer to the U-Net to condition on slots. With this design, slots do not need to lie in the text embedding space, leading to better object-centric representations. Authors conduct extensive experiments including both segmentation and generation on real-world datasets COCO and VOC. The results are impressive and the generation result is clearly better than previous works.

### Strengths
- The adapter design is reasonable, and the motivation behind it is clear -- slots capture object semantic information, which might be incompatible with the text embedding space. With this new adapter layer, one can freeze the pre-trained DM while not sacrificing the expressiveness of learned object slots.
- The guidance loss is novel. While there are concurrent work (e.g. GLASS) applying a similar loss, they usually require external supervisions such as captioner (to get text from input images). I am surprised that just letting slot attention mask and cross-attention mask to guide each other can work so well (I would expect some stop gradient operation to stabilize training). The ablation studies in Table 2 are comprehensive and answer my concerns very well.
- As far as I know, SlotAdapt is the first work showing compositional generation ability on real-world images (prior work only show segmentation results). I find the results in Fig.6 impressive.

### Weaknesses
I do not find any big weakness of this paper. There is one claim that sounds not precise to me and I hope the author can revise it.
- In line 468 and Fig.5 caption, authors claim that SlotAdapt "generates nearly perfect reconstructions". I do not think this is the case, as apparently the reconstructed images are clearly different from the input image. This result itself is not a weakness of the method, as slots are compressed representations and cannot preserve all visual details. However, I do believe the statement itself is wrong.

Minor:
- Please unify the name of U-Net in the paper. In Fig.1 and line 230 it is called "Unet", in line 207 "U-Net", in line 223 and 224 "UNet".
- Line 320 "v1.5 for MOVi-E; and COCO", I think this ";" is redundant.
- The generation results of SlotAdapt are impressive, yet authors only put small figures in the main paper (Fig. 5 and 6). I understand this is due to page limit. Please add text to refer readers to large figures in Appendix Fig. 8 and 10.

### Questions
1. What will happen if you add the guidance loss from the beginning of training? Will the training diverge?
2. Why using SD 1.5 on COCO and SD 2.1 on VOC? In SlotDiffusion Appeidix E.5, they do mention that using the v-prediction objective sometimes leads to degenerate results. Is it also the case here as SD 2.1 is using v-prediction?
3. Have you tried classifier-free guidance (CFG)? I am curious if using a larger CFG scale, will the reconstruction result be even better.
4. Instead of pooling all slots to form the register token, I guess an interesting alternative is 1) add an additional slot in your slot attention module, and 2) only input this new slot to the cross-attention layer. This slot is dedicated to capture global information and may perform better than pooling object slots.

### Soundness
3

### Presentation
3

### Contribution
3
