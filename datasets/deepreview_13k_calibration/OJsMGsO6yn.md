# SIM: Surface-based fMRI Analysis for Inter-Subject Multimodal Decoding from Movie-Watching Experiments

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Current AI frameworks for brain decoding and encoding, typically train and test models within the same datasets. This limits their utility for brain computer interfaces (BCI) or neurofeedback, for which it would be useful to pool experiences across individuals to better simulate stimuli not sampled during training. A key obstacle to model generalisation is the degree of variability of inter-subject cortical organisation, which makes it difficult to align or compare cortical signals across participants. In this paper, we address this through the use of surface vision transformers, which build a generalisable model of cortical functional dynamics through encoding the topography of cortical networks and their interactions as a moving image across a surface. This is then combined with tri-modal self-supervised contrastive (CLIP) alignment of audio, video, and fMRI modalities to enable the retrieval of visual and auditory stimuli from patterns of cortical activity (and vice-versa).  We validate our approach on 7T task-fMRI data from 174 healthy participants engaged in the movie-watching experiment from the Human Connectome Project (HCP). Results show that it is possible to detect which movie clips an individual is watching purely from their brain activity, even for individuals and movies *not seen during training*. Further analysis of attention maps reveals that our model captures individual patterns of brain activity that reflect semantic and visual systems. This opens the door to future personalised simulations of brain function. Code \& pre-trained models will be made available at \url{https://github.com/}, processed data for training will be available upon request at \url{https://gin.g-node.org}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new technique for decoding brain signals that is generalizable across participants. They integrate surface vision transformers (SiTs) with multi-modal contrastive learning to decode audio and visual stimuli from cortical fMRI data. They demonstrate the efficacy of their approach on the HCP movie watching database and show superior decoding performance. The model shows strong performance not only on the same subjects and stimuli seen during training but also on new subjects and previously unseen stimuli

### Strengths
- The idea of multimodal alignment of vision, audition and fMRI through contrastive learning seems novel and promising 
- The study demonstrates that the model can generalize across unseen subjects and stimuli, which is a crucial aspect of developing robust brain decoding methods.
- The paper builds on established techniques in brain decoding by introducing more advanced architectures, like surface vision transformers (SiTs) which are better able to capture long-range structure in surface imaging data

### Weaknesses
 - Comparison against alternative architectures like 3D CNNs etc is lacking in this work, which makes it harder to understand the contribution of the Surface vision transformer 
-  Quantitative evaluations of the reconstructed visual clips against other state of the art decoding models is also currently lacking in those work. At the very least, the authors should include more examples of reconstructed clips
- Model performance is presented using retrieval tests which are much easier than reconstructions; Given that most studies nowadays can perform decent decoding with the help of powerful generative models, this should atleast be discussed.

### Questions
- During inference, why not use the full test set for retrieval? The size of the set clearly has an impact on the retrieval performance. Why do the authors choose a lower set size for the auditory domain? 
- Can the authors comment on the biological plausibility of the encoder architectures used for stimulus encoding - eg wav2vec which works directly with raw audio waveforms instead of cochleograms/spectrograms may not be the best choice for reformatting auditory signals into brain-aligned representations

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors present a novel approach to modeling cortical functional dynamics by leveraging Vision Transformers (ViTs) tailored for surface data analysis. Their method integrates a tri-modal alignment using CLIP, aligning audio, video, and fMRI data to enhance the retrieval of visual and auditory stimuli from cortical activity patterns and vice versa. The model demonstrates high within-subject accuracy, effectively identifying audio and video samples from just 3-second fMRI recordings. Additionally, the authors investigate attention maps that reveal distinct patterns associated with the brain's semantic and visual systems. They explore model's generalizability on (i) unseen subjects; (ii) unseen stimuli; and (iii) unseen stimuli within unseen subjects.

### Strengths
The authors: 
- design a novel framework composed of SiTs and tri-modal CLIP alignment for brain decoding. 
- evaluate the model on unseen subjects and unseen stimuli
- leverage attention maps providing interpretability of the model's behavior, and make the connection between the information extracted from attention heads and specific functional networks
- show the recontruction of visual stimuli improves through the tri-modal approach

### Weaknesses
 - Limited to decoding 3-second clips, may not capture longer-term temporal dynamics
- Only tested on movie watching data, unclear how well it would generalize to other tasks/stimuli
- Requires high computational resources (multiple A100 GPUs)
- Limited diversity in the movie stimuli used for training

### Questions
What constraints or shortcomings resulted from training the models using only 3-second temporal windows? How might this impact the model's ability to capture longer-term temporal dynamics or more complex cognitive processes?

The caption for Figure 4 lacks clarity in identifying specific brain regions. It would be more informative to directly label or annotate the relevant areas (such as Broca's area, auditory cortex, sensorimotor cortex, visual areas, and the face area) on the attention map visualizations.

How does performance compare to other state-of-the-art brain decoding methods?

What are the privacy/ethical implications of being able to reconstruct visual experiences from brain data?

The study uses a fixed temporal lag of 6 seconds to account for the hemodynamic response. However, the hemodynamic response lag is known to vary across different brain regions. How might this fixed lag approach impact the model's ability to accurately capture temporal dynamics in regions with differing hemodynamic response functions?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses the challenge of generalizing decoding models for video and audio stimuli to fMRI responses from subjects not included in the training data, aiming for a universal cognitive model rather than subject-specific ones typically achieved in this field. The authors propose an approach that combines anatomical and functional alignment to map across subject-specific response spaces. Their method leverages two main principles: topographical alignment and space-time pattern matching. To implement this, they use a Vision Transformer with cortical surface response patches as input, alongside a tri-modal CLIP criterion imposed on a shared embedding space for audio, video, and fMRI. The approach is evaluated on the 7T HCP movie dataset with over 170 subjects, demonstrating successful nearest-neighbor identification of video and audio samples from responses of held-out subjects. Additionally, some success is shown in the fully zero-shot setting, where both the test subject and test stimuli are unseen during training.

### Strengths
- Significant Challenge Addressed: The paper tackles the important and well-recognized challenge of inter-subject generalization in brain decoding tasks. By striving for a universal cognitive model that can apply to responses from unseen subjects, the authors make a meaningful contribution to the field, which often relies on subject-specific models that limit broader applicability.

- Innovative Methodology: The authors present an intriguing combination of a Vision Transformer (ViT) applied to patches of cortical surface responses, paired with a multi-modal contrastive learning criterion. This approach leverages the strengths of ViT for spatial representation while effectively integrating different modalities (audio, video, fMRI) to enhance the decoding process.

### Weaknesses
The main issue is the combination of too many ideas within a single paper. While the focus on inter-subject generalization in stimulus decoding is critical, the inclusion of multi-modal audio and video adds complexity that obscures the primary contributions. The rationale for combining these modalities should be clearly justified, particularly since generalization across subjects poses challenges even in simpler stimulus domains like images. A more focused exploration of the decoding problem could strengthen the paper's impact.

The results are difficult to interpret, especially in Table 1. The meaning of the "inter" and "intra movie" columns needs clarification. It would be beneficial to restrict the table to test movies included in the training dataset. Additionally, an evaluation of audio versus video identification success is lacking. The absence of same-subject (intra-subject) baseline results and chance-level metrics makes it challenging to assess the significance of the reported accuracies (e.g., 80% vs. 77% top-1 accuracy). The authors should enhance guidance in the text to help the reader grasp the key contrasts of interest.

Furthermore, the decoding problem addressed appears to be a nearest-neighbor classification, which is arguably a basic form of decoding. Given the recent advancements in within-subject stimulus reconstruction, a more compelling approach would explore inter-subject generalization in the context of these more popular and challenging brain decoding tasks.

Additional comments:
- The originality of the work is challenging to evaluate. The authors should more thoroughly situate their contributions within the context of previous research, particularly in relation to cited works by Dahan et al. (2024), Tong et al. (2022), and Feichtenhofer et al. (2022), emphasizing the added value of their approach.
- The paper lacks plots that could effectively convey findings in a more visual and intelligible manner. Incorporating proper uncertainty estimates in graphical representations would enhance clarity.
- The writing style is overly cryptic, with excessive notation making the paper difficult to follow. Simplifying the presentation could greatly improve readability.
- The figures, particularly in the main figure (Fig. 1), suffer from poor quality; the font sizes are too small, and the caption is not sufficiently explanatory.
- There are numerous grammatical and syntactical errors throughout the manuscript. A thorough review is necessary to enhance clarity and professionalism.
- The authors only consider a single dataset. Demonstrating the applicability of their approach across multiple publicly available datasets would strengthen the paper’s generalizability.
- The authors use the terms "movie" and "video" interchangeably, creating ambiguity regarding whether "movie" refers to video with audio or just video alone. This should be clearly defined.
- Main results, such as those in Table 1, should not be conflated with ablation studies to avoid confusion.
- The manuscript is missing comparisons to other identification/classification approaches, both within and across subjects, which would provide valuable context and relevance to the proposed method.

### Questions
1) I suggest creating figures with plots to visually represent the data. Each figure should have clear takeaways that are explicitly stated in their captions to guide the reader's understanding.

2) Why is the inter-movie accuracy typically higher than the intra-movie accuracy in Tables 1, 2, and 3? Given that inter-movie represents the held-out movie case, which is expected to be more challenging, this finding is counterintuitive and warrants further explanation.

3) It would be beneficial to apply the method to another dataset, ideally focusing on a single modality. This would help demonstrate the robustness and generalizability of the approach.

4) If feasible, I recommend breaking down the impact of the Vision Transformer (ViT) compared to the CLIP approach. This could involve substituting CLIP with a more conventional training and classification method (e.g., referencing works from the Kamitani and Gallant group over the past decade). Such a comparison would strengthen the case for the specific contributions related to subject canonical space mapping, rather than merely showcasing advanced training and classification techniques.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel approach for brain decoding using surface vision transformers (SiT) and tri-modal CLIP contrastive learning to generalize audiovisual stimuli decoding from fMRI data across different subjects and unseen stimuli. The model leverages the spatial topography of the brain’s cortical surface, combined with alignment between fMRI, audio, and video embeddings, achieving up to 80% top-1 accuracy in identifying stimuli across subjects in a movie-watching task. The approach is validated on the HCP 7T movie-watching dataset, showing strong generalization and offering interpretability through attention maps that highlight brain regions involved in audiovisual processing.

### Strengths
- The use of tri-modal CLIP alignment for fMRI, audio, and video embeddings is an innovative contribution, extending prior unimodal or bimodal approaches.

- The integration of state-of-the-art techniques, like vision transformers and contrastive learning, is well-grounded and technically solid. Also, the model is rigorously evaluated on unseen subjects and stimuli, demonstrating strong performance in terms of Top-K accuracy.

- Its potential impact on brain-computer interfaces (BCIs) and neuroscience research is significant, with promising future applications.

### Weaknesses
 **Limited Generalization Beyond the Dataset**: The model’s generalization is limited to the HCP 7T dataset, with no evaluation on more diverse or real-world stimuli. This raises concerns about the model's robustness and applicability to scenarios beyond the specific characteristics of the training data. The lack of testing on abstract visual stimuli, silent films, or non-narrative content limits the assessment of its capacity to generalize across different types of audiovisual information. 

**Computation**: the model’s self-attention mechanisms are computationally expensive, limiting scalability to higher resolutions. The use of multi-head self-attention (MHSA) operations, while effective, poses a significant computational burden, potentially hindering its application to higher-resolution fMRI data or larger-scale datasets. This computational cost could be a barrier to practical implementation and further development of the model.


Some of the typos that need to be corrected:

1. Appendix C.1, under Table C.1.'s caption. "3-frame reconstruction taskon", should be "3-frame reconstruction task on"?
2. Line 512, "evalute" should be "evaluate"

### Questions
1. In section 4.4, the authors propose the potential for training encoding/decoding frameworks that exhibit generalizability. While the model shows robust generalization performance on the HCP 7T movie-watching dataset, have the authors considered evaluating its generalizability under more diverse experimental conditions, such as with abstract visual stimuli, silent films, or non-narrative content? Given that the HCP dataset primarily includes specific cinematic types, how do the authors anticipate the model’s performance on stimuli with varying visual and auditory properties?


2. In Table 1:
-  The vsMAE pre-training appears to significantly enhance performance compared to training from scratch. For instance, in the case of $f_{MRI}\rightarrow \mathcal{V}$ with SiT, vsMAE pre-training substantially improves the top-1 metrics. Could the authors elaborate on how this pre-training enhances the model’s generalization capabilities? Is this improvement consistent across different stimulus types (e.g., non-movie visual content), or is it specifically tied to the training dataset?

   - Some results exhibit considerable variance. For example, the results for $f_{MRI} \rightarrow \mathcal{A}$ with SiT show $70.9 \pm 20.3$, and $f_{MRI} \rightarrow \mathcal{V}$ shows $80.3 \pm 18.0$. Could the authors provide an explanation for this variability?

3. I am a little bit confused about the information that Figure 4 wants to present. Could the authors clarify how these maps are quantitatively validated against known functional networks (Yeo et al), and how confident we can be that these maps are genuinely reflecting underlying neural processes rather than model artifacts?

4. The overall generalizability of the model was evaluated using the same dataset. From my understanding, the contribution to generalizability here is that the model improves upon previous methods (which focused on single-subject analysis) by making it more generalizable to future tasks, but still within the same study population or dataset. Is this correct? Could the authors comment on this? Typically, when referring to generalizability, it implies extending the model’s applicability to a broader population or more diverse datasets. 

5. In the discussion section, the author mentioned that the current model does not include sub-cortical structures, despite their known role in sensory processing, such as the Lateral Geniculate Nucleus (LGN) in vision. Is it viable to handle the noise in subcortical area using CIFTI dataset?

6. The authors utilize sine-cosine positional embeddings to encode the locations of cortical patches in the SiT model. Have the authors evaluated the effectiveness of this choice for representing the complex geometry of the brain’s surface? Would alternative methods, such as learned positional embeddings, improve performance or better capture spatial relationships in cortical data?

7. What's the computation time?

### Soundness
3

### Presentation
2

### Contribution
3
