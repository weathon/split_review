# FLAIR: A Foundation Model for Grapheme Recognition in Ancient Scripts with Few-Shot Learning

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
The Indus Valley Civilization (IVC) left behind an undeciphered script, posing a significant challenge to archaeologists and linguists. This paper introduces FLAIR, a few-shot learning approach that aims to establish a foundational model for recognizing and identifying individual graphemes from the limited available Indus script. As a foundational model, FLAIR is designed to be versatile, supporting multiple potential applications in script recognition and beyond. It leverages prototypical networks combined with a modified proposed encoder network for segmentation, ProtoSegment to extract intricate features from the grapheme images. We evaluate FLAIR’s ability to generalize from minimal data using IVC grapheme classification tasks and further experiment with pre-trained Omniglot models for fine-tuning. Additionally, we simulate real-world data scarcity by intentionally restricting training data on the Omniglot dataset. Our experiments demonstrate FLAIR’s accuracy in digitizing and recognizing Indus Valley seal graphemes, outperforming traditional machine learning classification approaches. These results underscore FLAIR's potential not only for the digitization of ancient scripts with limited labeled datasets but also for broader applications where data is scarce. FLAIR’s success in grapheme recognition highlights its promise as a foundational model capable of extending to other undeciphered writing systems, thereby contributing to the integration of classic scientific tools and data-driven approaches.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents "FLAIR", a foundational model designed for the grapheme recognition of the Indus Valley script, an ancient un-deciphered writing system. Recognizing the limited availability of labeled data, the authors leverage few-shot learning (FSL) through prototypical networks enhanced with a custom segmentation encoder called ProtoSegment.

### Strengths
The only positive aspect of this article is the topic.

### Weaknesses
(i) No details on IVC dataset. 

(ii) What is the functionality of the protosegment model is also not properly illustrated  and hence the key contribution (if any at all  ) also cannot be perceived. This part should  have been aided with more illustrative diagrams. 

(iii) Sloppy text - for example in page 3 line 147-148. 

(iv) Extremely poor language and sentence formation. 

(v) irrelevant references - just for the sake of filling up the paper , for example Line 44 in page 1.

### Questions
Seems the method described in this paper is just an off-the shelf algorithm - Could you specify what was the real contribution?

Where from did this IVC dataset was procured? 

What was the reason for putting the details of the grant in the acknowledgement section??  This is completely against ICLR submission policy as this might reveal the authors identity.

### Soundness
1

### Presentation
1

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
This paper introduces FLAIR, a few-shot learning model for recognizing graphemes from the undeciphered script of the Indus Valley Civilization (IVC). Utilizing prototypical networks and a specialized encoder, FLAIR excels at digitizing IVC seal graphemes, outperforming traditional method.

### Strengths
1.	FLAIR fills a critical gap in ancient script recognition, providing a versatile model not previously available in OCR or grapheme recognition.
2.	ProtoSegment outperforms existing few-shot and deep learning methods, achieving higher accuracy in grapheme classification tasks across both datasets.

### Weaknesses
1.	The paper focuses on grapheme recognition in ancient scripts, which is a niche topic and represents a small subfield of OCR. This has weak influence on our scholar field, which makes this paper is not suitable for a top-tier conference like ICLR. Additionally, general OCR methods might also perform well on this dataset.
2.	The proposed method largely relies on existing approaches (CNN backbone + Classifier head), merely applying the framework on your dataset. This raises concerns about the contribution and innovation of this work. The novelty of the segmentation encoder is not clearly articulated, and it's unclear how it differs substantially from standard feature extraction techniques used in other CNN-based approaches.
3.	The method employs a very basic CNN architecture for the classification task, which seems outdated in the current era of large models. Moreover, referring to it as a "foundational model" appears somewhat exaggerated. The choice of a simple CNN is not well-justified, particularly given the complexity of the grapheme images and the potential for more sophisticated architectures to capture finer details.
4.	Figure 1 is also quite unclear. The diagram lacks sufficient detail to understand the data flow and the specific operations within each component of the model. The visual presentation is not intuitive, making it difficult to grasp the model's architecture.
5.	Furthermore, will this paper release the dataset publicly? If not, the lack of innovation in your method significantly diminishes the paper's contribution to the academic community. The absence of a publicly available dataset hinders reproducibility and prevents other researchers from building upon this work.
6.	The experimental section lacks ablation studies to validate the components of your proposed method. Without ablation studies, it is difficult to ascertain the individual contributions of the segmentation encoder and the CNN backbone to the overall performance.
7.	As shown in Table 1, the accuracy of your method and other state-of-the-art approaches has reached over 98%, even approaching 99%. In such cases of minimal improvement, it is difficult to determine whether the results stem from experimental variability or the enhancements offered by your method. The reported gains are marginal and might not be statistically significant, raising questions about the practical impact of the proposed method.

### Questions
As shown in Weakness.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper describes a method, FLAIR, to classify graphemes in ancient Indus valley civilization scripts. FLAIR adopts a few-shot learning approach to circumvent small datasets by introducing the protosegment model designed for images of graphemes. The authors evaluated their technique on an existing dataset OmniGlot as well as their custom Index valley civilization scripts dataset.

### Strengths
* Applying deep learning techniques to scripts could be very beneficial to archaeologist and linguists to help study many undeciphered scripts. This could also be applied to other ancient scripts outside of scripts used in indux valley civilizations.

### Weaknesses
 * Details about the dataset is not clear.
* There is limited novelty in the proposed network architecture

* The paper is not blinded
* The writing of the paper needs edits. e.g.,
    * The flow of the paper is hard to follow. 
    * It wasn’t easy to link Figure 4 to the text describing it
    * References are not correctly added throughout the paper
    * Abbreviations are not defined carefully (e.g., convolutional neural network -> CNN was defined 3 times)

### Questions
* How was the dataset annotated?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The article proposes FLAIR, which uses a few-shot learning method to recognize individual characters from a limited set of Indus scripts. FLAIR uses prototypical networks and ProtoSegment to extract complex features in grapheme images to achieve recognition of Indus script. FLAIR was pre-trained on the Omniglot dataset and then migrated to the recognition and classification tasks of the IVD dataset, achieving state-of-the-art results. FLAIR's ability to perform efficient feature extraction from small samples and its potential adaptability to unseen symbols make it a powerful tool not only to digitize and analyze ancient scripts but also potentially aid in their decipherment.

### Strengths
The paper uses meta-learning and few-shot learning to perform classification and recognition tasks on a small sample of Indus Valley Civilization. The article improves Prototypical Networks and proposes ProtoSegment, which achieves state-of-the-art performance on the IVC Dataset. The findings of this paper may contribute to new discoveries and interpretations of ancient texts of the Indus Valley Civilization.

### Weaknesses
This paper has major writing problems. For example, there are a large number of incorrect symbols and formulas in the text, the citation format of references in the text is incorrect and confusing, the pictures in the text are blurry, and the model training process is not clearly explained, which will cause great confusion for readers who are not familiar with Prototypical Networks. In terms of innovation, although the paper proposes a relatively novel task, there are few improvements to the methods used. The paper only adds a segmentation encoder to the original Prototypical Networks. If I understand correctly, the segmentation encoder should be a convolution-based encoder-decoder, but I don’t understand what specific role this network can play and why it can segment images into individual graphemes. In the experimental part, the article lacks qualitative analysis of the experimental results. Why is there such a result? What caused the difference in the experimental results? What conclusions can we draw from the experimental results? I think these should be added to the paper.

### Questions
1. In the paper, all figure uses jpg or png format. The drawn image should be saved in pdf format before being inserted into the paper.
2. In section 3.2 PROTOSEGMENT MODEL, there are a lot of errors in mathematical symbols and formulas. Some symbols appear out of thin air without explanation, which is not conducive to readers' understanding.
3. What role does Deep Learning: MobileNet mentioned in Figure 1 play in the entire task? The article does not explain it clearly.
4. In Tables 1 and 2, it should be explained clearly what K-way and N-shot refer to, as this may be confusing to readers who are not familiar with Prototypical Learning.
5. There are errors in the reference citation format in the paper, and the content of the references is mixed with the main text, which is not conducive to the reader's reading experience.
6. Why does the Backward Pass in Figure 4 point to the Support Sample and Query Sample from the network? Aren't these samples extracted from the dataset and cannot be updated?
7. In Table 1, why is the result of 20-way worse than that of 5-way? I hope to see the explanation of this experimental phenomenon.

### Soundness
3

### Presentation
2

### Contribution
2
