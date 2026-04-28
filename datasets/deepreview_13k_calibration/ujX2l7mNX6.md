# MindGPT: Interpreting What You See with Non-invasive Brain Recordings

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Decoding of seen visual contents with non-invasive brain recordings has important scientific and practical values. Efforts have been made to recover the seen images from brain signals. However, most existing approaches cannot faithfully reflect the visual contents due to insufficient image quality or semantic mismatches. Compared with reconstructing pixel-level visual images, speaking is a more efficient and effective way to explain visual information. Here we introduce a non-invasive neural decoder, termed as MindGPT, which interprets perceived visual stimuli into natural languages from fMRI signals. Specifically, our model builds upon a visually guided neural encoder with a cross-attention mechanism, which permits us to guide latent neural representations towards a desired language semantic direction in an end-to-end manner by the collaborative use of the large language model GPT. By doing so, we found that the neural representations of the MindGPT are explainable, which can be used to evaluate the contributions of visual properties to language semantics. Our experiments show that the generated word sequences truthfully represented the visual information (with essential details) conveyed in the seen stimuli. The results also suggested that with respect to language decoding tasks, the higher visual cortex (HVC) is more semantically informative than the lower visual cortex (LVC), and using only the HVC can recover most of the semantic information.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new method to reconstruct visual stimuli from the brain activities using fmri, that seeks to decode the information encoded in the human brain when processing visual information. One of the main bottlenecks of this approach is the limit on acquiring more high quality features while staying non invasive. Previous work has achieved only limited success in this field, where most of the reconstructions are blurry and without any low-level texture in the image. Having this said, the authors open new doors by using semantic feature extraction as opposed to pixel wise, feeding them to another generative model. They argue that the mentioned method is not only more robust, but obtain more detailed and relevant images after all.

### Strengths
1. Paper is very well-written even for a general reviewer. Furthermore, the settings of the model and experiments are accurately described as to make it easier for reproducibility.
2. The novelty of using semantic features in the middle of their end-to-end model is quite intuitive. Plus this message has been delivered quite clear to the reader. 
3. Using augmentation to compensate that lack of data is justified, and they modify already existing methods to apply better in their case. 
4. Formulation of the loss is carefully written to adhere to the main purpose of the paper. 
5. Images generated with the proposed algorithm contain more low-level details and texture as shown in the paper.

### Weaknesses
1. The paper has circumvented the main goal of visual reconstruction, we are completely relying on the generative model to build the images.  In other words, images generated this way won't be closer than a certain amount despite having enormous details. 
2. Comparison with other methods in the field has been mentioned scarcely after the introduction part, e.g., in the experiments it's done only among the different versions of their own algorithm.

### Questions
Can you please mention more methods before this paper that aimed the same goal? Also highlight if using semantic methods are a complete novelty or it has been used before to some extent, with other approaches.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper authors propose MindGPT to generate captions of the images perceived by humans from the fMRI responses during perception. To do so first they align fMRI responses to visual feature space (CLIP) using a fMRI encoder (ViT) and then guide a language decoder to generate captions of images from fMRI embeddings using cross attention.

The training and evaluation is performed on publicly available fMRI dataset(Horikawa and Kamitani, 2017 ; Shen et al. ). The results show that captions generated by MindGPT correctly capture some of the semantic information present in the scene perceived. They also perform additional analysis which show

1. voxels from higher visual cortex (HVC) lead to more accurate captions as compared to lower visual cortex (LVC). 
2. which visual cues were relevant for caption generation

### Strengths
1. The paper is easy to follow, well written with descriptive figures.
2. Although the idea to generate captions from fMRI responses is not new and has been explored previously (see references in weaknesses section) but the use of recent methods such as image captioning (SMALLCAP) to generate pseudo groundtruth captions, alignment with CLIP encoder and use of cross attention to guide GPT-2 makes this a new contribution
3. Qualitatively the results are impressive (I would have preferred to see the captions of all 50 test images ). I do not have expertise in captioning literature so I am not sure how good are quantitative results though.
4. The analysis showing HVC generates more accurate captions is exciting and could be combined with reconstruction methods to generate reconstructions that are both pixel-level and semantically accurate. In reconstruction LVC contribution is more, this paper shows that complementary information can be decoded from HVC.
5. Authors perform additional analysis to show which visual cues were relevant for caption generation and tsne analysis to show latent representation of different brain regions 
6. Use of virtual training examples to augment the smaller training dataset.

### Weaknesses
1. The results in this paper are from DIR dataset (1200 training and 50 test images) which is smaller compared to NSD dataset (10k images). Another advantage of NSD is that images are from MS-COCO dataset which contain more semantically complex scenes as compared to imagenet images in DIR which contain a single object centered. The single object nature of ImageNet images limits the complexity of the captions that can be generated and evaluated. Therefore, the authors should justify their choice of dataset and discuss how it might affect the generalizability of their findings to more complex real world scenes.

2. There are a few relevant references missing (Matsuo et al. , Sakata et al.) which generate captions from brain activity. Specifically, the work by Matsuo et al. uses a similar approach of mapping brain activity to a visual feature space and then using that representation to generate text. Similarly the work by Sakata et al. uses an unsupervised text latent space for caption generation. I am not sure if the code of these papers are available that’s why I am not asking to compare the results but I believe they should be at least discussed for readers to understand how this paper is different from previous fMRI→ caption generation methods. The lack of discussion of these related works makes it difficult to contextualize the novelty and contribution of the current work.

3. Self-attention maps of MindGPT encoder can be used to inform which brain region was more relevant in generating captions. Analyzing these attention maps could provide insights into how the model is utilizing different brain regions for different types of images or caption content. For example, it would be interesting to see if the model relies more on visual cortex for generating captions about objects and more on semantic regions for generating captions about actions. This analysis could provide valuable insights into the neural mechanisms underlying image caption generation from fMRI data.

4. It is not clear what groundtruth is used to compute language similarity metrics. If it is compared to Image captions generated by SMALLCAP then it is a major limitation of this approach. Accuracy of image generated captions will be upper bound by SMALLCAP. This means that the evaluation metric is not measuring the quality of fMRI-based caption generation but rather the quality of SMALLCAP. Collecting human captions for at least the test set and comparing both SMALLCAP and MindGPT would have been more informative. The use of pseudo-captions limits the conclusions that can be drawn from the quantitative evaluation.

5. Minor: I assume blue color text in Figure 3,4 indicates correct captions and black colored text indicate incorrect text. These should be mentioned in the Figure captions for clarity.

### Questions
Questions

1. Why was NSD not considered for this paper?
2. Was any ablation performed to assess how crucial was the data augmentation performed using virtual training examples? e.g. will including more images per category further improve results?

Clarification

1. Identification of visual cues using cosine similarity between fMRI encoder output and patch tokens inform which cues can be extracted from fMRI responses? Can this be helpful in answering where in an image subject was attending. If that is the case generating captions from fMRI data of Horikawa and Kamitani 2022 can lead to interesting findings.

Suggestions
1. Please refer to weaknesses section. I am confident that this contribution has the potential to be a good paper if the authors address weaknesses. 

Reference: 
Horikawa, Tomoyasu, and Yukiyasu Kamitani. "Attention modulates neural representation to render reconstructions according to subjective appearance." *Communications Biology* 5.1 (2022): 34.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces MindGPT, a non-invasive neural decoder that interprets perceived visual stimuli into natural languages from fMRI signals. The model employs a visually guided neural encoder with a cross-attention mechanism that uses the large language model GPT to guide latent neural representations toward a desired language semantic direction.

### Strengths
The proposed method, MindGPT, is a novel and innovative approach to interpreting visual stimuli using non-invasive brain recordings.
MindGPT has been shown to generate word sequences that truthfully represent the visual information conveyed in the seen stimuli, with essential details.
MindGPT has also been shown to be more semantically informative than other methods, and to be able to recover most of the semantic information using only the higher visual cortex (HVC).

### Weaknesses
About the novelty. Though the authors consider the proposed method as the first task-agnostic neural decoding model, CLIP-like models have been integrated in extensive research areas to make alignment with their specific representations in a similar way. Also, the claim of novelty is weakened by the fact that the core mechanism, cross-attention, is a well-established technique. The specific application to fMRI data is novel, but the underlying method is not fundamentally new. 
Also the evaluation, could you compare your model with exist CLIP-like models and show the strength of yours. The current evaluation lacks a direct comparison with models that use similar visual-semantic alignment techniques, making it difficult to assess the true advantage of MindGPT. The dataset is not big enough to support the model. The use of a single subject from the DIR dataset is a significant limitation, as it does not demonstrate the generalizability of the model across different individuals. The lack of diversity in the dataset could lead to overfitting and limit the applicability of the model in real-world scenarios.

### Questions
How well does MindGPT perform on a variety of different visual stimuli?
How does MindGPT compare to other state-of-the-art methods for interpreting visual stimuli using non-invasive brain recordings?
Could you add more detail on the dataset? How many subjects you used? How long the fMRI signal? 
Does your work design a alignment between fMRI signal and images?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present an approach to decode semantic textual representations of images from brain activity data recorded with fMRI. An fMRI encoder (ViT) is trained (1) to predict the CLIP-Vision CLS embedding of the seen image given the fMRI activity and (2) as part of a pipeline where the CLIP prediction is fed to each layer of a frozen GPT-2 text generative model through cross-attention layers to predict the next word in the ground truth caption of the image. The pipeline is trained on the DIR dataset containing multiple presentations of 1200 training and 50 test images for three participants. Qualitative and quantitative results suggest the pipeline could predict similar captions to the ground truth. Further analysis showed that using voxels from the higher visual cortex areas leads to better reconstruction than lower or whole visual cortex areas.

### Strengths
Originality: The proposed pipeline (fMRI encoder + GPT-2 with cross-attention layers) appears like a novel application of a SMALLCAP-inspired approach (Ramos et al., 2023) but with CLIP latents predicted from fMRI and no retrieval-based prompting. However, similar fMRI-to-caption work has not been cited or compared to (see Weaknesses).

Quality: The paper is of acceptable quality, with a sound justification of the proposed approach and clear reporting of the results. However, as mentioned above, there is a lack of comparison to the existing literature.

Clarity: The paper is overall clear, though some information is missing (see Q1).

Significance: It is hard to evaluate the significance of the results given the lack of comparison to the existing literature. The analysis of Section 4.3 on decoding from specific ROIs provides interesting evidence into the properties of different cortical areas.

### Weaknesses
The main weakness to me is the lack of comparison to existing work on the topic of fMRI-to-caption decoding. I am aware of at least two papers proposing a similar fMRI-to-pretrained latent alignment + generative text modeling approach which also report qualitative and quantitative results on an fMRI-to-caption task (Mai & Zhang, 2023; Ferrante et al., 2023). However, the presented results are not compared to any previous baseline. Given the similarity of the approaches, a clear comparison must be made to establish whether the proposed approach provides an improvement over existing approaches. On a similar note, I believe a useful result to include in the analysis of Table 1 would be the performance of the pipeline if GPT-2 receives the ground-truth CLIP latents, instead of the fMRI-based predictions. This would provide an upper-bound for the proposed approach and help situate the reported results. Finally, the DIR dataset contains a small number of examples and categories as compared to the recent NSD dataset. As part of comparing the proposed approach to existing approaches, it would make sense to include results on this larger dataset as well.

### Questions
1. What is the value of H in the voxel vectors? Is there any lag between the image presentation and the extracted window? How much zero padding does this vectorization scheme lead to? Is there any aggregation of the presentations (at the BOLD or prediction level), or are the reported predictions obtained from single fMRI windows?

2. My understanding is that the input to the fMRI encoder is a sequence of 7 items (each one a vectorized set of ROI voxels) passed through a linear projection to 768 dimensions. Is the linear projection common to all items of the sequence? If so, I am curious to know what kind of operation it ended up learning to do.

3.  In Section 4.1: “Our MindGPT trained on DIR and a subset of ImageNet (Deng et al., 2009), including 150 categories totaling 200.7k images.” How was ImageNet used, and how were these 200.7k images selected? My understanding from Section 3.1 is that DIR contains 1250 unique images.

4. In Section 4.2: “Note that the default training/test split of DIR has no overlapping image categories, we randomly sampled 50 fMRI-image training pairs, and added them to the test set for the few-shot evaluation.” Can you confirm this means that these images were removed from the training set and added to the test set?

5. How do the results vary across subjects? It is not clear whether the results of Table 1 and 2 are across subjects or for a specific subject.

6. How were the examples of Figure 3 selected? What is the proportion of “failure cases” and high-quality reconstructions? Since there are only 50 test examples (times 3 subjects) my understanding is that all reconstructions could be presented in e.g. a table.

7. The analysis of Section 4.4 is an interesting way to see how the predicted latent shares information with the different image patches. What would this analysis give if you were to use the actual CLIP CLS token instead of the decoder’s prediction to compute the similarity scores? Would the scores look different for examples like the killer whale image (Figure 6, bottom left)? This might be a way to confirm that this analysis tells us about the brain decoding objective and not mostly the CLIP embedding itself.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair
