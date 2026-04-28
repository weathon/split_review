# Textural or Textual: How Visual Models Understand Texts in Images

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
It is widely assumed that typographic attacks succeed because multimodal pre-trained visual models can recognize the semantics of text within images, allowing text to interfere with image understanding. However, the assumption that these models truly comprehend textual semantics remains unclear and underexplored. We investigate how the CLIP encoder represents textual semantics and identify the mechanisms through which text disrupts visual semantic understanding. To facilitate this analysis, we propose a novel ToT (Texture or Textual) dataset, which includes a subset that disentangles orthographic forms (i.e., the visual shape of words) from their semantics. Using Intrinsic Dimension (ID) to assess layer-wise representation complexity, we examine whether the representations are built on texture or textual information under typographic manipulations. Contrary to the common belief that semantics are progressively built across layers, we find that texture and semantics compete in the early layers. In the later layers, while semantic accuracy improves, this gain primarily stems from texture learning that aids orthographic recognition. Only in the final block does the visual model construct a semantic-focused representation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper investigates how vision-language models, particularly CLIP, process text in images, questioning whether they truly understand semantics or merely recognize visual patterns. Using a novel dataset and Intrinsic Dimension analysis, the authors find that texture heavily influences representations, even in later layers, with semantic understanding primarily emerging in the final block. They propose a defense against typographic attacks by fine-tuning this final block.

### Strengths
1. The ToT dataset, particularly the subset designed to disentangle orthography and semantics, is a valuable contribution and allows for a more nuanced investigation of how visual models process text.
2. The use of Intrinsic Dimension (ID) provides a quantitative measure of representational complexity, offering insights beyond qualitative visualizations. The analysis reveals a complex interplay between texture and semantics across different layers.
3. The proposed defense strategy of fine-tuning only the final block is a practical and potentially efficient approach, grounded in their analysis of representational changes across layers.

### Weaknesses
1. The analysis primarily focuses on CLIP. While CLIP is a representative vision-language model, exploring other architectures, particularly those with different training objectives or architectural designs, would significantly strengthen the generalizability of the findings. For example, models that incorporate attention mechanisms differently or those trained with contrastive losses that emphasize different aspects of visual and textual information could reveal whether the observed texture-dependence is a universal phenomenon or specific to CLIP's architecture.
2.  While the proposed defense strategy shows promise, a comparison with existing defense mechanisms against typographic attacks is missing. This would provide a better context for evaluating the effectiveness of their approach. The paper should benchmark against established methods, such as adversarial training techniques or input transformation methods, to determine if the proposed fine-tuning approach offers a significant advantage or if it is merely comparable to existing solutions. Without such a comparison, it is difficult to assess the true novelty and practical utility of the defense.
3. While the paper analyzes the impact of text size and semantics, a more comprehensive ablation study is needed. For instance, exploring different font styles, text placements, and background complexities would further elucidate the interplay of texture and semantics. The current study does not fully explore the parameter space of typographic variations. Specifically, variations in font weight, kerning, and anti-aliasing could significantly impact the model's representation of text. Additionally, the study should consider more complex background scenarios, such as those with varying textures or patterns, to evaluate the robustness of the findings.

### Questions
1. What are the long-term effects of fine-tuning only the final block on the model's performance over time? Are there any observed degradations in performance on non-typographic tasks?
2. The paper uses ImageNet-1k as the basis for the ToT dataset. How might the findings change if the dataset were based on a different image dataset with more diverse scenes and text occurrences?
3. The authors mention that "genuine semantic comprehension only emerges in the final block." Could you provide further evidence or analysis to support this claim? How do you define and measure "genuine semantic comprehension" in this context? How does this relate to the observed decrease in ID for consistent text overlays in the final block?

### Soundness
4

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
4

### Summary
The paper discusses the problem of how CLIP confuses  text inside images with visual object itself, and introduces some defenses to typographic attacks.

### Strengths
This is an interesting problem, and I also find the dataset proposed interesting. 
The defense method is simple and seems to do better than baseline methods used for comparison.

### Weaknesses
The paper seems to have parts that are not well connected: the results on the intrinsic dimension (ID) seem disconnected from the defenses and results presented in section 5. It will be better to strengthen the connection to justify why the ID is needed for this paper. The analysis of intrinsic dimensionality, while interesting, feels somewhat tangential to the core problem of typographic attacks and defenses. The paper does not clearly articulate how the ID analysis informs the design or evaluation of the proposed defenses. It's unclear if the ID is used to select specific layers for analysis or if it is just an independent observation. The lack of a clear connection weakens the overall narrative. 

Some parts of the paper would benefit from more clarification. I do not think this is an important weakness as the paper is overall clear. But I include some suggestions later.

### Questions
Here there are some suggestions to improve the paper clarity in case they are useful to the authors:

1. I would recommend making some questions softer. For instance, the question “do these models genuinely understand the semantics of the text or are they merely recognizing it as a visual pattern?” is a really difficult question and cannot be answered by the experiments shown in this paper. I do not think the authors need to set such a high bar so early in the paper.

2. Line 68, the sentence “Our findings reveal a non-linear pattern in representation” is repeated twice.

3. Maybe you could rename the orthographic pairs as “Paronyms”: words that are similar in spelling but have different meanings.

4. In the algorithm 1, you first store in R the ratios between the first and second nearest neighbors for all images. Then you compute the intrinsic dimension by “linear regression on R”. This last step is not clear. What is being regressed? It is a regression between R and what?

5. In the equation in line 229, the variable “d” is not defined. Could you describe that equation? 

6. Figure 3 is hard to see because the dots are very small (even when zooming into the figure). The authors conclude from that analysis that “we hypothesize that multi-modal visual models may initially interpret text as a textural feature in the earlier layers”. In my opinion, I do not think one can conclude anything about how text is encoded there by just looking at the result from figure 3. The text is small in the image. The representation in the first layers is likely to be dominated by image features that occupy large image regions. 
But isn’t it better to interpret the result as if that representation in early layers is dominated by all the image features (not just text)? Clearly, the last layer can focus on smaller image regions that contain important information, and it separates all the information (image and text) and t-sne can differentiate among the 6 sets. 

7. In figure 3, what happens with the nonsense text?

8. Could you describe the notation used in table 1? What does the number in Cons_80, … Irr_* means? I assume it refers to the font size as shown in the appendix, but I think it will be useful to point the reader to the appendix or to include a short description in the text somewhere in the lines 315-320 or in the table caption. 

9. Once the reader arrives to section 5, there seems to be no connections between the experiments performed in section 5 and the analysis in the previous sections. The previous sections seem to be used only to support the observation that “early layers of visual models primarily rely on texture features rather than true semantic understanding”. But one could arrive to the same conclusion just from the experiments of section 5.

### Soundness
2

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
3

### Summary
This paper investigates how the CLIP encoder represents textual semantics and identify the mechanisms through which text disrupts visual semantic understanding. A novel ToT (Texture or Textual) dataset is built on texture or textual information under typographic manipulations. Authors claim to find that texture and semantics compete in the early layers. In the later layers, while semantic accuracy improves, this gain primarily stems from texture learning that aids orthographic recognition. Only in the final block does the visual model construct a genuine semantic representation.  The experiments are thorough.

### Strengths
They analyze the representations of semantics and textures in different layers of CLIP more clearly with Intrinsic Dimension.
Also try to construct a reasonable dataset for typographic attack analysis  with extensive experiments.

### Weaknesses
The Intrinsic dimension (ID) is interesting, but a more explicit investigation into ID for this task should be well studied.


### Questions
A more explicit investigation into ID for this task should be well studied. 
As the title is “How visual models understand texts in images”, does this conclusion apply to CNN-based CLIP models or other visual models?
In Table 3 and Table 5, why did the accuracy for Cons show a significant decrease in the Hard case? If the model is only required to identify text within images, how well it perform?
In section 5.2.2, If other methods are trained using the same dataset as yours, how about the performance?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper challenges the assumption that multimodal pretrained visual models, like CLIP, effectively comprehend textual semantics within images. It investigates how the CLIP encoder represents textual semantics and how text disrupts visual understanding. To facilitate this, the authors introduce a new dataset, ToT (Texture or Textual), which separates orthographic forms from their semantics. Their analysis reveals that texture and semantics compete in early layers, and while semantic accuracy improves in later layers, this is largely due to texture learning. Genuine semantic representation is only constructed in the final layer of the model.

### Strengths
1. This paper conducted a more detailed experimental analysis, and the experimental results reveal the layers of visual models mainly depend on texture features instead of authentic semantic understanding. Genuine semantic representation is constructed only in the final block, following substantial compression of the textural information.
2. The paper finetunes the last block based on its findings, resulting in overall better performance in defending against typographic attacks compared to other methods.

### Weaknesses
1. The authors do not intuitively explain the motivation for using the Intrinsic Dimension. Although it is introduced in the related work section and Section 3.2, the authors do not emphasize what phenomenon this metric intends to reveal in this paper's context. It makes the experimental results not easily understood in Figure 4. Specifically, the paper lacks a clear explanation of why the intrinsic dimension is a suitable measure for assessing the complexity of the learned representations and how changes in this dimension relate to the disentanglement of texture and semantics. The connection between a high intrinsic dimension and the dominance of texture features, or a low dimension and semantic understanding, is not explicitly stated, leaving the reader to infer the meaning.
2. The analysis of the experimental results requires significant effort to understand. In the section on Intrinsic Dimensionality Estimation, lines 268 to 272, the authors discuss the swell-shrink pattern. However, this is not related to the conclusions of this section, which may lead to confusion. The experiment's conclusion on Semantic Constancy with Varying Font Sizes (lines 234-236) indicates that multimodal models are influenced by the semantics of the text. However, the authors do not clarify the connection to the disentangling cross-layer textual and textural representations discussed in Section 4.2. The paper does not clearly articulate how the font size experiment demonstrates the model's sensitivity to semantic content versus textural variations. The link between the observed semantic constancy and the broader goal of disentangling textual and textural representations across different layers of the model is not made explicit. It's unclear how this experiment isolates the semantic influence from the textural influence, especially since font size changes also affect the texture of the text.
3. The paper should also present the results of fine-tuning using the **Nonsense** type pairs from the dataset to enrich the experiments of defense against typographic attacks. This type of attack is also common in practice. The current evaluation focuses primarily on semantic-preserving typographic variations. The absence of results on nonsense text attacks leaves a gap in understanding the model's robustness against more adversarial inputs. The paper should include an analysis of how the proposed fine-tuning method performs when faced with text that lacks semantic meaning, as this is a crucial aspect of real-world robustness.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
