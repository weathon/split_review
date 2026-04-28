# ProPicker: Promptable Segmentation for Particle Picking in Cryogenic Electron Tomography

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
Cryogenic electron tomography (cryo-ET) can produce detailed 3D images called
tomograms of cellular environments. An essential step of cryo-ET reconstruction and analysis is to find all instances of a protein in tomograms, a task known as particle picking. Due to the low signal-to-noise ratio, artifacts, and vast diversity in proteins, particle picking is a challenging 3D object detection problem. Existing approaches are either slow or limited to picking a few particles of interest, which requires large annotated and difficult to obtain training datasets. In this work, we propose ProPicker, a fast and universal particle picker that can detect particles beyond those in the training set. Our promptable design allows for selectively detecting a specific protein in the volume based on an input prompt. Our experiments demonstrate that through a favorable trade-off between performance and speed, ProPicker can achieve performance close to or on par with state-of-the-art universal pickers, while being up to an order of magnitude faster. Moreover, ProPicker can be efficiently adapted to new proteins through fine-tuning on few annotated samples.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduced a particle picking method for cryo-electron tomography (cryo-ET), ProPicker, that formulate particle picking in cryo-ET as a promptable segmentation problem. Particle picking in cryo-ET is a challenging problem and is also one of the bottlenecks in the cryo-ET data processing. The authors claims that ProPicker is a universal model that balances the speed and performance, by being significantly faster than other methods, while having similar picking accuracies.

### Strengths
ProPicker as a particle picking application seems to be significantly faster than other methods, which is an advantage for the end users. The promptable design inspired by SAM also provides good flexibility so that users can use it for different targets to explore their tomograms.

### Weaknesses
1. The main weakness of this manuscript as a submission of ICLR is the lack of novelty in the methods. It seems that the major difference between ProPicker and other deep learning-based picking methods are the promptable design. The encoder for the prompt is taken from TomoTwin as-is, the segmentation model is a standard 3D U-Net, and the particle coordinate finding uses clustering or template matching which both are very standard procedures in other similar methods. The SAM-inspired promptable design itself is not completely novel in the cryo-EM/ET field either, as there are similar methods like cryoSAM [1, 2].

2. Not enough performance comparison with other methods. The authors mainly used TomoTwin as the baseline comparison, where there are other modern methods like DeepETPicker, DeePiCt, cryoSAM. Also I noticed that the authors used TomoTwin as the baseline for some tasks, while switched to DeepFinder for other tasks, which is not satisfying. How does ProPicker compare with them in terms of performance and speed on both synthetic data and real data?

3. In many cases, the ultimate goal of cryo-ET data processing is to achieve the best reconstruction. Using the picked particles by ProPicker or by other methods in real data, how do the reconstructions look like? Will ProPicker's reconstruction achieves a better or on-par resolution?

4. The authors presented two real data cases, but in both of them the targets are ribosomes. Ribosome is well-known as an easy target for picking due to their relatively large size and being abundance in the in situ data. The authors should present at least one other real case in which the picking target is not ribosome.

5. For the related works, there should also be some brief mentions of particle picking methods for single-particle cryo-EM, as these two problems are very closely related.

6. There are no available ablation studies in the manuscript; for example. I feel that the discussion about the stride s should be reformatted into an ablation study section for a better reading. If there are other hyperparameters, it should be discussed as well.

### Questions
How does the missing wedge artifact affect ProPicker? To elaborate, the tomogram will suffer from the missing wedge artifact, and so will be the prompt if it is a subtomogram cropped from the larger tomogram.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a cryo-ET particle-picking method called ProPicker, which is a promptable encoder-decoder-based segmentation model. ProPicker is trained on synthetic data and can be finetuned on experimental data with few prompts. The prompts are processed with a prompt encoder which is further used as input to the decoder of the segmentation model. With such a strategy, ProPicker demonstrated fast prompt-based picking on several synthetic and experimental cryo-ET datasets.

### Strengths
The authors proposed a working learning-based solution for particle picking in cryo-ET, which is an important problem in cellular and structural biology.

### Weaknesses
*Novelty: I highly doubt whether there is any actual novelty in this work. Prompt-based segmentation for particle picking has been already introduced for cryo-ET (See CryoSAM, MICCAI 2024).

*No discussion and comparison with related works: There are several learning-based particle-picking methods for cryo-ET now. The mentionable ones are DeepETPicker, CryoSAM, Huang et. al. (ECCV, 2022), CrYOLO, etc. However, the authors did not mention them at all, let alone provide any comparison with them. They only used TomoTwin as baseline.

*Evaluation: The quantitative evaluation of real data is questionable. Since there are annotations on the tomograms,  the authors could have simply calculated the F1 score as they did on synthetic data. Instead, the authors used the IoU score for the evaluation of real data, which does not make much sense, since the annotations are points, not volumes. Moreover, the IoU score is very small. The authors claimed that expert annotations miss some particles without properly validating such claims. The visualization in Figure 7 is simply not enough as a blob-like shape may or may not be a particle of interest. Moreover, there are also FAS particles apart from ribosomes in EMPIAR-10988. One way to validate the author’s claim is to perform subtomogram averaging (STA). The authors talked about STA in the appendix but did not perform it for their predictions.

*Depends on Denoising: While finetuned on real tomograms, the authors performed denoising. For EMPIAR 10045, the tomograms were denoised with CryoCARE. For EMPIAR 10988, the tomograms (did not mention if only VPP, only defocus, or both) are denoised with Topaz. ProPicker was applied to the denoised tomograms. Such dependence on denoising methods is a significant limitation for ProPicker. Moreover, different denoising methods were used for different tomograms- which method to use can be a difficult choice.

*Usability: The authors argued that many learning-based picking methods require particle radius as input which limits their usability. However, the authors initiated another parameter stride value (s), which is crucial for ProPicker to work. The authors used very different s value for baseline TomoTwin and their method ProPicker. From the choice of values they made for ProPicker, it seems like they are just using the approximate diameter of the ribosome as pixels as the stride value. In other words, they are indirectly using the radius, which according to their claims will limit the usability of the method.

### Questions
* How do you know the optimal stride (s) value? You used a very small (s) value for TomoTwin but a large stride value for ProPicker, why? 
Also, the stride value used for ProPicker is similar to the diameter of the ribosome in pixels. In such a case, you indirectly need an idea of the particle radius to select the optimal stride value. Is this the case?  
* EMPIAR 10988 also contains FAS. I wonder why ProPicker was not tested for FAS picking. Can you check your picking performance for FAS particles? 
* You mentioned authors missed many True particles for EMPIAR 10988 that ProPicker picked. However, such a statement is not experimentally validated. One way is to perform subtomogram averaging (with the same parameters) for both author-annotated and ProPicker-annotated particles and see if ProPicker improves resolution. 
* How did you finetune on real tomograms from EMPIAR 10045 and EMPIAR 10988? How many tomograms did you use? How many prompts did you use? For EMPIAR 10988, did you use VPP tomograms or Defocus-only tomograms? 
* How dependent is ProPicker’s performance on denoising?
* You mentioned prompts can be amino acid sequences or atomic coordinates as well. How does that work?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new promptable method for particle picking in cryo-ET data. By using the off-the-shelf encoder TomoTwin, it encodes a manually selected prompt into an embedding, which is then injected into the decoder of a 3D U-Net to achieve prompt-based particle segmentation. The authors demonstrate the method's advantages in speed and discuss its generalization capabilities and applicability to real experimental data.

### Strengths
- Through an additional U-Net, this method enables TomoTwin to perform particle picking with a larger stride, thereby achieving a speed increase while maintaining on-par accuracy.
- The paper discusses the method's generalization performance and demonstrates its effectiveness on real experimental data, indicating its practical value.

### Weaknesses
 - The paper claims promptable, fast and universal particle picking, but there is already closely related work in this area that is neither cited nor compared in this study. 
[1] CryoSAM: Training-Free CryoET Tomogram Segmentation with Foundation Models. MICCAI 2024
[2] Accurate Detection of Proteins in Cryo-Electron Tomograms from Sparse Labels. ECCV 2022
- This paper relies on a robust prompt encoder, TomoTwin, which itself is already capable of generalized reference-based or clustering-based particle picking. A key question is whether the model's generalization capability mainly stems from this strong prompt encoder. The addition of the extra U-Net could potentially undermine TomoTwin’s inherent generalization ability by introducing layers that may reduce the flexibility of the learned embeddings, potentially limiting adaptability to unseen particles. Specifically, the U-Net's convolutional layers might impose a fixed receptive field, which could hinder the model's ability to adapt to variations in particle size or shape compared to the more flexible embedding space of TomoTwin.
- The method shows some generalization capability on unseen particles but is quite sensitive to variations among different particles, with performance dropping significantly on certain particles. Fine-tuning can mitigate this issue; however, the need for fine-tuning contradicts the claim of universal picking. This sensitivity suggests that the method might be overfitting to the specific characteristics of the training particles, and the fine-tuning process might be merely adapting the model to new particle types rather than achieving true generalization. The claim of universality should be supported by a more robust performance across diverse particle types without the need for fine-tuning.
- Figure 3 also reveals considerable sensitivity to prompt choice for many proteins, with several outliers showing low performance. The reasons behind these low-performing outliers need further exploration, including a more detailed description of how prompt choices are selected and what is a good choice supposed to be like. The authors recommend trying a few prompts for each particle, if prompt selection relies solely on random attempts, the practical usability of the method is compromised. The lack of a clear strategy for prompt selection makes the method less practical, as users would need to rely on trial-and-error, which is not ideal for a supposedly universal method. A more systematic approach to prompt selection, perhaps based on particle features or structural characteristics, would be necessary to improve the method's usability.

### Questions
- Why does each chart in the experimental results display different proteins? Is it possible to unify the experiments and compare them on the same proteins?
- In Section 4.6, the visualization results of the experimental data are quite difficult to compare. For example, in Figure 6, from my perspective, ProPicker has missed recalling quite a few objects that appear to be white particles. Additionally, this section compares the IoU of TomoTwin, ProPicker, with the expert labels, but IoU may not be a suitable metric for this task. On one hand, it only reflects the overlap of the global mask and does not indicate the proportion of objects that have been picked; on the other hand, the precision of the expert labeled mask does not seem very high from the figure, making it inappropriate to pursue a high IoU blindly. Metrics similar to average precision at certain IoU threshold in object detection would better reflect the issues at hand.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a 3D U-Net based pipeline for particle picking, i.e. object detection, in cryo electron tomography based on a prompt in the form of a reference image of a sought particle. The pipeline employs an off-the-shelf CNN from the current state of the art in the field, TomoTwin, to embed the prompt image; It then uses the U-Net along with a conditioning mechanism in the decoder, FiLM, to generate a segmentation map of the prompted particle; The foreground of this map is then leveraged to reduce the search space of the sought particle, either by using each connected component as a candidate location, or by using the full foreground in a traditional template matching approach.  The pipeline achieves a significant speed-up over TomoTwin, which uses a sliding window CNN in place of a U-Net in an overall otherwise similar pipeline.

### Strengths
The work is clearly written and easy to follow. The speedup over TomoTwin is clearly demonstrated and of clear practical relevance.

### Weaknesses
The reported speedup, while practically relevant, appears methodologically fully due to replacing a sliding window CNN with a U-Net. This is methodologically not new, as it was the core contribution of the FCN [Long et al., Fully Convolutional Networks for Semantic Segmentation, CVPR 2015] and further refined by the original U-Net work as cited by the authors. Thus the work appears to be out-of-scope for ICLR due to the absence of methodological novelty, while a more application-focused publication venue could be very fitting. 

Furthermore, the work appears to neglect previous work on formal properties of encoder-decoder architectures of the U-Net: The authors perform a "stride analysis" to find the best trade-off between window tiling (i.e., chopping the large input image into digestible pieces) and accuracy of the U-Net. (Outputs are then stitched back together, with averaging applied in overlapping regions of the output tiles.) The authors report that larger strides / less overlap in general lead to less accurate predictions. However, it has been shown that U-Nets can be run in a tile-and-stitch manner that is provably equivalent to processing full images as a whole [Rumberger et al., How Shift Equivariance Impacts Metric Learning for Instance Segmentation, ICCV 2021], thus enabling sound processing of arbitrarily large / too-large-for-GPU-memory images. To this end, the U-Net needs to be applied with valid padding and feasible output window size. This approach renders tile-and-stitch processing with a U-Net periodic-k shift equivariant, which may alleviate the need for any output tile overlap in case of the authors' application. Note, there is still a chance though that averaging over test time augmentations in the form of input image shifts by <k pixels may improve accuracy. Both should be tried out by the authors for a formally sound analysis of the impact of window tiling on particle presence map accuracy and speed.

### Questions
What kind of padding do you employ in the U-Net? What is the input- (and output-) window size?
Please try valid padding in combination with input window size as large as your GPU can take, and output window cropping to the closest multiple of 2^l, where l is the number of pooling layers in your U-Net (I believe 5?), as described in Rumberger et al., 2021.

### Soundness
2

### Presentation
3

### Contribution
2
