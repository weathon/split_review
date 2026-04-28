# FakeShield: Explainable Image Forgery Detection and Localization via Multi-modal Large Language Models

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
The rapid development of generative AI is a double-edged sword, which not only facilitates content creation but also makes image manipulation easier and more difficult to detect. Although current image forgery detection and localization (IFDL) methods are generally effective, they tend to face two challenges: \textbf{1)} black-box nature with unknown detection principle, \textbf{2)} limited generalization across diverse tampering methods (e.g., Photoshop, DeepFake, AIGC-Editing). To address these issues, we propose the explainable IFDL task and design FakeShield, a multi-modal framework capable of evaluating image authenticity, generating tampered region masks, and providing a judgment basis based on pixel-level and image-level tampering clues. Additionally, we leverage GPT-4o to enhance existing IFDL datasets, creating the Multi-Modal Tamper Description dataSet (MMTD-Set) for training FakeShield's tampering analysis capabilities. Meanwhile, we incorporate a Domain Tag-guided Explainable Forgery Detection Module (DTE-FDM) and a Multi-modal Forgery Localization Module (MFLM) to address various types of tamper detection interpretation and achieve forgery localization guided by detailed textual descriptions. Extensive experiments demonstrate that FakeShield effectively detects and localizes various tampering techniques, offering an explainable and superior solution compared to previous IFDL methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper designs a multimodal framework called FakeShield, which uses the power of large language models to train the model by building a Multi-Modal Tamper Description dataSet (MMTDSet), enabling it to analyze, detect, and locate image tampering. The author uses GPT-4o to generate text descriptions and convert the existing IFDL image dataset into a dataset containing accurate text descriptions.

### Strengths
1. FakeShield is the first proposed multimodal large-scale image forgery detection and localization model, which can provide a more reasonable basis for judgment.
2. By combining visual and language models, the paper's method can provide more comprehensive image analysis. The paper enhances the existing IFDL dataset through GPT-4o and constructs MMTDSet, which also makes a certain contribution to the field of forgery detection.
3. The DTEFDM and MFLM modules proposed in the paper enable the model to flexibly handle different types of image tampering. This paper has potential value in practical applications.

### Weaknesses
1. The model proposed in the paper may require high computing resources and training time.
2. The generalization ability of the model on new types of tampering that have not been seen yet needs further verification.  Also further work may be needed to quantify and verify the quality of the model's explanation.

### Questions
It is recommended that the authors further validate model generalizability as well as quantify and validate the quality of the model explanations.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper employs LLM to enhance existing IFDL datasets from a forgery perspective. Based on these new data, a multimodal and explainable forgery detection method (FakeShield) is proposed. FakeShield first derives text description of the possible forgery type and reasons based on the finetuned LLM, and then uses the text description to guide the output of the forgery location mask. Experimental demonstrations in forgery detection, localization, and explanation aspects demonstrate the effectiveness of the proposed method.

### Strengths
The paper generates language descriptions for some existing IFDL datasets based on GPT-4o, so as to explain the types and causes of forgeries.

The introduction of the Domain Tag Generator offers initial predictions of the domain O_det of input images, thereby avoiding conflicts in tampered data domains and precisely guiding subsequent detection/localization models towards the forgery types of interest.

The proposal of MFLM involves the alignment of textual (O_det) and image features, facilitating the joint prediction of forgery masks from a multimodal perspective.

The experiment compares the traditional forgery detection and localization with the existing IFDL methods, and also compares with the existing LLMs from the perspective of forgery interpretability.

### Weaknesses
I believe there are some critical issues in the following aspects:

Dataset:
- Using GPT to generate textual descriptions for forgery regions and treating them as ground-truth (GT) lacks comparative validation. While the generation process of these textual GTs involves multiple rounds of dialogue and expert proofreading to ensure accuracy, I believe it lacks internal validation. Specifically, the mask GTs of existing datasets are (mainly) constructed based on the residual comparison between the original (authentic) images and forged ones to prevent mislabeling authentic regions as forgery. However, in creating textual GTs, this comparative process is missing, making it challenging to ensure the credibility of the textual GTs. Therefore, I suggest that GPT should simultaneously receive "original image, forged image, and/or forgery mask" for joint assessment, potentially enhancing the precision of the generated textual GTs.
- Furthermore, Figure 2 depicts the dataset construction process involving "expert proofreading", but this procedure is not mentioned in the main text.

Methodology:
- The modules (LLM, SAM, specialized token <seg>, etc.) and loss functions (ce, bce, dice, etc.) involved in the FakeShield are largely derived from existing works. Therefore, I think its original contribution is not solid enough.
- Given that the final predicted mask M_loc relies on the guidance of O_det, a natural concern arises: if O_det produces incorrect content (for example, it generates a completely authentic description for forgery data), could M_loc be significantly misled? Along this line, incorporating a corrective mechanism in TCM might better mitigate the aforementioned situation.

Experiments:
- **Lack of cross-validation**: Although FakeShield can provide detailed explanations for forgery  reasons, it appears to forcefully interpret all forgeries from preset perspectives. For example, in the last case of Figure 16, the inside of the clock is forged, while the external background/shadow, etc. are original (real). However, FakeShield still believes that its shadows do not conform to the light source logic. Therefore, it is necessary to add some forgeries that only contain some types to cross-validate whether FakeShield has truly learned the knowledge of different types of forgeries. For example, manipulating only the shadow part of an image while keeping other aspects such as lighting, edges, resolution, perspective relationships, and physical laws unchanged, to assess whether FakeShield can identify this specific manipulation involving only shadows without affecting the rest.
- **Lack of stronger generalization evaluation**: Based on the data distribution summarized in Table 7, the evaluation data is not completely cross-domain for training data. Specifically, the sources and creation processes of Deepfake and AIGC data in both training and testing are highly similar (e.g., all the AIGCs are generated by SD-inpainting). Therefore, the claim in Line 382 that FakeShield generalizes well to Deepfake and AIGC tampering is overstated. It is recommended to add completely cross-database data for evaluation, such as adding data from FFIW, CelebA-DF, DFDC, etc. for Deepfake detection.
- **Ablation experiment is not sufficient**:
  - Line 505 only evaluates the performance of FakeShield with and without DTG. However, the more critical question is why it is decided to use three forgery domain tags instead of more detailed tags? For instance, following HiFi-Net, it is possible to subdivide Photoshop-type data into splicing, pasting, and inpainting; and subdivide AIGC data into categories like “GANs” or “Diffusion” (of course I understand that all AIGC data in MMTD-Set is produced by the SD-inpainting technique). Similarly, the issue extends to the authentic domain (as per Figure 2, defining only “Scene” and “Face” as authentic tags). Could a broader range of authentic/forgery domain tags lead to performance improvements? I think it requires more in-depth discussion.
  - The ablation design in the paragraph at Line 515 is inadequate and should further evaluate the results when using only T_tag or T_img. Additionally, the experimentation in this section solely focuses on the CASIA1+ dataset, and there may be potential data bias.

Presentation:
- While the core focus of this paper is on "explainable", the main body of the experiments is still on forgery detection and localization. It may not be appropriate to put the experimental results on explanation in the appendix.

Incorrect formulas/symbols:
- Eq. (4): \hat{\mathbf{O}}_{det} and \mathbf{O}_{txt} are never defined or explained. The same problem applies to \hat{\mathbf{T}}_{tag}.
- The description of Line 318~322 (including Eq. (5)) is inconsistent with the previous text. Please confirm whether the model's predicted output is \hat{\mathbf{M}} or \mathbf{M}.
- Does the second case in Figure 14 show an incorrect response? The response is exactly the same as the first case.

Minor Issues:
- The symbol of Domain Tag Generator in Fig. 3 is a handwritten G, which should be consistent with the bold G used in the text (line 266).
- The caption of Fig. 3 describes that I_ori will be input into the Tamper Comprehension Module, but this does not match the content of the picture.
- Line 245: change "a original" to "an original"
- Line 1292: change "the first picture has glasses …" to "the second picture has glasses …"

### Questions
- Table 2: Why do competitors CADDM and HiFi-Net only achieve an accuracy close to random guessing? It seems unreasonable that competitors perform so poorly when both the training and testing sets are sourced from FFHQ and FaceAPP. Or, maybe it is because CADDM and HiFi-Net have not been retrained? (Lines 355-357 did not explicitly mention whether these methods were retrained).

- Figure 5: Why does the untrained FakeShield (epoch=0) already achieve an IoU of 0.40 on the CASIA1+ dataset? This result far surpasses the results of well-trained comparative algorithms, such as ManTraNet with 0.09 IoU and HiFi-Net with 0.13 IoU.

- Why is the localization of Deepfake-type data not evaluated in the experiment? From Figures 2 and 19, Deepfake data has masks that mark the forged areas, but the experimental results on Deepfake (Figures 4, 14, and Table 4) are deliberately omitted.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents FakeShield, a multi-modal framework for explainable image forgery detection and localization. It uses multi-modal large language model to detect manipulations, generate tampered region masks, and provide detailed explanations based on visual artifacts and semantic inconsistencies. Utilizing carefully designed prompts, GPT-4o constructs the MMTD-Set to enhance model training. Incorporating modules like DTE-FDM and MFLM, FakeShield achieves superior performance in detection accuracy and localization across various forgery techniques compared to existing IFDL methods.

### Strengths
This paper possesses several notable strengths: 

1.Clear motivation and remarkable innovation: This paper firstly proposes an explainable image forgery detection and localization task and innovatively designs a multi-modal large model Fakeshield, which enhances the transparency of forgery detection and effecitively pinpoints the tampered areas. 

2.Cross-domain generalization and satisfactory performance: The proposed FakeShield can effectively differentiate and handle various tampering domains such as PS-tampered, DeepFake, and AIGC-based editing. The detection, explaination, and localization performance outperforms most of the SOTA methods, as reported on Tab.1, 2, 3, 4. 

3.Dataset construction and potantial contribution: This paper uses GPT-4o to enrich existing datasets through carefully designed prompts, constructing the Multi-Modal Tamper Description dataSet (MMTD-Set). It has the potantial to serve for the IFDL community and future explorations.

4.Clear organization and good writing: The writing and organization of this paper is generally good, easily comprehensible, and effectively presents its methods in Figures 1-3.

### Weaknesses
1.Unclear statement about domain tag generator: The paper does not clearly explain how the domain-tag generator works to handle different types of image tampering. It is suggested to explain the network structure, working principle and training method of domain-tag generator more clearly.

2.Insufficient comparison with DeepFake detection methods: In Tab.2, the paper only compares FakeShield with two other DeepFake detection methods. This limited number of comparison models may not provide a comprehensive evaluation of FakeShield’s performance against a wider range of existing state-of-the-art methods. Please add more deepfake detection method for comparison.

3.Incomplete ablation studies: In Tab.6, the authors only conducted experiments on CASIA1+ dataset for PS tampering, which may have some bias. It is suggested to verify the role of domain-tag generator on more datasets.

### Questions
Please refer to the weakness.

### Soundness
4

### Presentation
4

### Contribution
3
