# SciPG: A New Benchmark and Approach for Layout-aware Scientific Poster Generation

- Decision: Reject
- Scores: 6, 6, 8, 3

## Abstract
Scientific posters are an effective and expressive medium for conveying the core ideas of academic papers, facilitating the communication of research techniques. However, creating high-quality scientific posters is a complex and time-consuming task that requires advanced skills to summarize key concepts and arrange them logically and visually appealingly. Previous studies have primarily focused on either content extraction or the layout and composition of posters, often relying on small-scale datasets. The scarcity of large, publicly available datasets has further limited advancements in this field.
In this paper, we introduce a new task called layout-aware scientific poster generation (LayoutSciPG), which aims to generate flexible posters from scientific papers through integrated automatic content extraction and layout design.
To achieve this, we first build a large-scale dataset containing over 10,000 pairs of scientific papers and their corresponding posters. We then propose a multimodal extractor-generator framework, which employs a multimodal extractor to retrieve key text and image elements from the papers and designs an interactive generator with an adaptive memory mechanism to seamlessly paraphrase the extracted content and generate a structured layout. This approach effectively tackles challenges related to GPU memory consumption and long-term dependencies when handling the lengthy inputs (scientific papers) and outputs (posters). Finally, both qualitative and quantitative evaluations demonstrate the effectiveness of our approach while highlighting remaining challenges.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper is focused on the task of scientific poster generation, and introduces two novel contributions in the field. First, a dataset of 10k examples with pairs of papers and posters (SciPG), with relevant annotations about content and layout. Second, they propose a new method for poster generation, designed for jointly generate the layout and the content of a poster. The method first extracts relevant texts and images from an input document (paper), by computing CLIP and RoBERTa embeddings, for images and texts respectively, and predicting an extractive score. They keep top-k from the predicted scores. Second, they leverage a BART model to process multimodal inputs and generate the summarized (paraphrased) texts and layout of the poster.

### Strengths
- The paper is generally well written and easy to follow.
- It develops new dataset with strong level of processing and curation. It also provides a good level of documentation on how to reproduce the processing pipeline. This dataset will be of great benefit to the community.
- The proposed method seems effective in addressing the limitations of previous works i.e. they focus on independently generating layout or content, and the proposed method performs both tasks.
- The paper has substantial experiments and ablations of the method.

### Weaknesses
- Authors claim this is a large-scale dataset, which might be not the best term to use, given the dimension of other datasets considered large scale (in the millions). A medium size dataset is more well suited.
- The paper does not argue about PosterLayout [1]. Even though it does not focus on scientific poser generation, it is good to have it as reference.
- There is just one baseline to compare. I understand this is a new task but authors should be absolutely certain that there are no other possible baselines. (See my question about this later)
- The qualitative samples in Figure 4 show that the texts are overlapping with each other, showing that the method has quite room for improvement. 
- The human evaluation is done over 3 humans, which seems a rather small portion in order to draw conclusions.
- 
[1] Hsu, Hsiao Yuan, et al. "Posterlayout: A new benchmark and approach for content-aware visual-textual presentation layout." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.

### Questions
- About baselines. For instance, In Section 2.3 the paper describes that previous methods focus on layout or composition. Would it be possible to select a random layout and allow the baseline to generate its content? The same things applies the other way around, evaluating how the other baseline generates the layout. It would be interesting to compare both tasks separately.

- Can you elaborate more on why the KL term is needed in the generative loss? Authors mention " to prevent the model from
becoming overconfident." Some more detail would be appreciated.

- Authors define an Adaptive Memory mechanism to manage long range dependencies. Is this done because of conext length limitations in the Bert encoder? In that case, could this adaptive memory be avoided with sufficient context length? 

(see other points commented in Weaknesses)

Format Questions
- I noticed you should use more the \citep{} command, when citing several works. They will appear better in the paper.
- Did the authors change some of the margins of the template? Some parts are quite to packed with content, seems too much use of vspace.

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
3

### Summary
This paper investigates the layout-aware scientific poster generation (LayoutSciPG) task. Specifically, it addresses three challenges: multimodal extraction, multimodal generation, and the need for large-scale training data. To tackle LayoutSciPG, the authors develop a multimodal extractor-generator framework that includes extraction and interactive generation modules. Overall, the proposed solution is sound and reasonable. Additionally, a novel poster dataset has been constructed.

### Strengths
1.	This work explores an interesting task called layout-aware scientific poster generation, which is useful for generating flexible posters from scientific papers through integrated automatic content extraction and layout design.
2.	A large-scale dataset is created, containing over 10,000 pairs of scientific papers and their corresponding posters.
3.	Extensive experiments are conducted to evaluate both the qualitative and quantitative performance of the proposed approach.
4.	Practical issues, such as GPU memory consumption and long-term dependencies, are considered and addressed in this paper.

### Weaknesses
1.	Although the paper claims to present a novel research task, the research novelty is not particularly significant, as poster design has been extensively studied.
2.	The technical contributions are marginal, as most techniques have been developed and are commonly used. For instance, the multimodal extractor (MDE) is based on RoBERTa and BiLSTM, while the interactive generator (IG) relies on BART and RMT. The developed framework is relatively straightforward. The authors could better highlight their differences to better highlight its technical novelties.
3.	The experimental results are not convincing enough, as they only compare with one baseline, AdaD2P. Including comparisons with more recent advanced baselines would strengthen the advantages and make the empirical results more persuasive.
4.	As shown in Figure 4, the generated posters are still poor and not suitable for practical applications. It would be beneficial to present and compare posters generated with other baselines.

### Questions
Is it possible to incorporate prompts to generate the posters, allowing for personalized control by users over the final output?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors define the task of layout-aware scientific poster generation (LayoutSciPG) which takes both content extraction and layout into account (compared to previous work which looks at these things in isolation). To facilitate data-driven approaches the authors first collect a novel dataset (SciPG) of paper-poster pairs and automatically align text and image contents. The authors then introduce a novel two-stage pipeline architecture tailored to LayoutSciPG and finetune it on SciPG). Both in automatic and human evaluation the authors showcase the effectiveness of their approach to automatically generate scientific posters conditioned on papers.

### Strengths
The provided dataset is orders of magnitudes larger then existing related datasets and will surely be useful to other researchers. The authors promise to release code and data artifacts.

The proposed architecture is also very novel and constitutes a core contribution of this work. Even though there are a lot of newly introduced custom components, the authors quantify the contribution of each component in an ablation study.

The human evaluation  supports the findings from automatic evaluation and increases their credibilty.

### Weaknesses
The main experimental results are a bit lacking due to the lack of baselines (only one baseline provided). While I understand that the task is a novel one, I don't see why the approaches that tackle content extraction and layout in isolation mentioned in the introduction and related work couldn't serve as baselines. Providing a simple end2end baseline (or maybe a diffusion-based one) would also have been insightful.

The paper definitely needs more examples. As of know only two (bit hard to read) examples are provided in the main text. The authors should provide more examples in the appendix.

While the paper is generally easy to follow some parts don't feel very polished and can potentially be confusing. E.g., there are are passages with duplicated information (l. 45-51 & l. 125-130) and sometimes the paper is short on details (l. 387-388 & l. 395-397).

### Questions
#### Comments

The title of the paper is SciPG, but this term is not defined anywhere in the text. Only from Table 1 do we know that this is the name of the dataset. This leads to confusion especially since a similar term (LayoutSciPG) is used very often.

ImgR and ImgP are not clearly defined. While it can be understood from the context, being more precise could alleviate confusion.

Table 2 is a bit hard to read. Which column belongs to documents and which one to posters? Adding vertical bars or cmidrule's could help.

#### Questions

One thing I don't understand is the role of the BiLSTM on top of the Roberta embeddings. The authors claim that this "captures contextualized representations" (l.257) but the Roberta embeddings should already be contextualized. Unfortunately the contribution of the LSTM has not been investigated in the ablation study.

Posters might contain original content (e.g. images that do not appear in the paper as mentioned in l.183). Do the authors have an idea how that could be addressed in future work?

Your dataset contains a validation split but do you actually use it somewhere? Maybe for the experiments in Figure 2?

Do the authors think that a perceptual image similarity metric [1] between generated and reference posters could be a useful addition to the automatic evaluation?

[1] DreamSim: Learning New Dimensions of Human Visual Similarity using Synthetic Data

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work studies an important problem – automatically generate a poster from a scientific paper. It contributes a dataset with 10k pairs of scientific papers and their corresponding posters. It proposes an extractor to retrieve critical text and image elements from the papers and a generator to paraphrase the extracted content and generate a layout.

### Strengths
1.	It focuses on a very important and practical problem – scientific poster generation. This problem receives little attention currently. If it is well-solved, lots of people will benefit from it.

2.	The paper is easy to follow. The idea is clearly expressed.

3.	It contributes a new dataset for scientific poster generation, which will have big impact on this domain if released.

### Weaknesses
1.	The reason behind the model architecture choice is not clearly explained. 

a) Why is BiLSTM instead of Transformer used in multimodal extractor? The other components in the framework are all based on Transformer. What is the reason for such a special design that only uses BiLSTM in this part?  

b) In the interactive generator, what does ‘interactive’ refer to here? Does it mean users can participate in this process? 

2.	The evaluation for the layout part is not sufficient. Layout is important for a scientific poster as it relates to whether the poster is attractive and conveys information effectively. 

a) There are lots of studies focus on the layout generation problem [1][2]. They take the elements as input and generate their positions.  The comparison with them could be using the output of the multimodal extractor as their input. If the performance of the existing layout generation model is worse than the proposed interactive generator, I will be convinced that it is necessary to design a specific interactive generator; otherwise, the novelty and contribution of this work will be very limited. 

b) Important metrics for layout are missing, e.g., FID and alignment used in existing work [1][2].

3.	There is no discussion and ablation study about whether the problem decomposition is reasonable. Currently, the problem is decomposed into two parts, where the first part is to extract key text and image from the paper and the second part is to paraphrase text as well as generate layout. Why not put the paraphrase task a separate part or merge it into the first part, since it is a natural language processing task and is far from layout generation problem? Besides, if the task is decomposed as I suggested, the existing techniques [1][2] about layout generation can be reused, which may be beneficial for overall performance.

4.	There are only two qualitative results, which are not enough for justifying the performance of the proposed method. Besides, from the qualitative results shown, I can find many overlaps between elements, which indicate that the performance is not good enough.

[1] LayoutFormer++: Conditional Graphic Layout Generation via Constraint Serialization and Decoding Space Restriction

[2] PosterLlama: Bridging Design Ability of Language Model to Contents-Aware Layout Generation

### Questions
For the discussion in Section 4.3.2, what is the total token length for this task?

### Soundness
3

### Presentation
3

### Contribution
2
