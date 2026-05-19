### Summary

This paper introduces a new task, Layout-aware Scientific Poster Generation (LayoutSciPG), which aims to generate flexible scientific posters from academic papers through integrated automatic content extraction and layout design. To achieve this, the authors first created a large-scale dataset containing over 10,000 pairs of scientific papers and their corresponding posters. Then, they propose a multimodal extractor-generator framework that employs a multimodal extractor to retrieve key text and image elements from the papers and designs an interactive generator with an adaptive memory mechanism to seamlessly paraphrase the extracted content and generate a structured layout. This approach effectively addresses challenges related to GPU memory consumption and long-term dependencies when handling lengthy inputs (scientific papers) and outputs (posters). Both qualitative and quantitative evaluations demonstrate the effectiveness of the proposed approach while highlighting remaining challenges.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper introduces a new task, Layout-aware Scientific Poster Generation (LayoutSciPG), which aims to generate flexible scientific posters from academic papers through integrated automatic content extraction and layout design.
2. This paper creates a large-scale dataset containing over 10,000 pairs of scientific papers and their corresponding posters, which is crucial for further research in this area.
3. This paper proposes a multimodal extractor-generator framework that employs a multimodal extractor to retrieve key text and image elements from the papers and designs an interactive generator with an adaptive memory mechanism to seamlessly paraphrase the extracted content and generate a structured layout.
4. This paper effectively addresses challenges related to GPU memory consumption and long-term dependencies when handling lengthy inputs (scientific papers) and outputs (posters).

### Weaknesses

#### Some Related Works


#### comment

1. The paper mentions that the generated poster is relatively simple, and the layout aesthetics score is low. This may be due to the limited diversity of the dataset or the model's inability to capture complex layout patterns. The low aesthetic score suggests that the generated layouts lack the visual appeal and sophisticated design elements often found in human-created posters. This could be due to the model's focus on content extraction and placement rather than on aesthetic considerations. The dataset might not contain enough examples of diverse and aesthetically pleasing layouts to train the model effectively in this aspect.
2. The paper does not provide a user study to evaluate the usability and user satisfaction of the generated posters. Without user feedback, it is difficult to assess how well the generated posters meet the needs of researchers and whether they are effective in communicating scientific information. The absence of a user study leaves a gap in understanding the practical utility of the generated posters. It is unclear if the generated posters are actually useful for researchers or if they are easily understood and appreciated by the target audience.

### Suggestions

To address the limitations in layout aesthetics, the authors should consider incorporating more sophisticated layout models that can capture complex design patterns. This could involve exploring techniques such as generative adversarial networks (GANs) or variational autoencoders (VAEs) that are specifically designed for image generation and can produce more visually appealing layouts. Furthermore, the training dataset could be augmented with more diverse and aesthetically pleasing posters, potentially through data augmentation techniques or by incorporating additional datasets. The model could also be trained to optimize for aesthetic metrics, such as those based on principles of design, in addition to content relevance. This would encourage the model to generate layouts that are not only informative but also visually appealing. Another approach could be to incorporate a layout evaluation module that assesses the aesthetic quality of the generated posters and provides feedback to the generator, allowing it to iteratively improve the visual appeal of the layouts.

To evaluate the usability and user satisfaction of the generated posters, a comprehensive user study should be conducted. This study should involve researchers from the relevant fields who can provide feedback on the clarity, completeness, and overall effectiveness of the generated posters. The study should include both quantitative measures, such as task completion time and error rates, and qualitative measures, such as user satisfaction surveys and interviews. The user study should also compare the generated posters with human-created posters to assess how well the generated posters meet the needs of researchers. The study should also investigate how well the generated posters communicate the key findings of the scientific papers and whether they are easily understood by the target audience. This would provide valuable insights into the practical utility of the generated posters and help identify areas for improvement.

Finally, the authors should consider exploring methods to allow for more user control over the generated posters. This could involve providing users with options to customize the layout, such as choosing different templates or adjusting the placement of elements. This would allow users to tailor the generated posters to their specific needs and preferences. Additionally, the authors could explore methods to incorporate user feedback into the generation process, allowing users to provide feedback on the generated posters and refine them iteratively. This would make the generated posters more user-centric and improve their overall usability and effectiveness.

### Questions

1. The paper mentions that the generated poster is relatively simple, and the layout aesthetics score is low. What are the specific reasons for this? Is it due to the limitations of the model or the dataset?
2. Can the model handle more complex scientific posters with multiple columns, figures, and tables?
3. How does the model perform on different types of scientific papers, such as those with different writing styles or content structures?
4. How does the model handle the generation of figures and tables in the posters? Are the figures and tables generated automatically, or are they extracted from the original papers?
5. How does the model ensure the accuracy and completeness of the extracted content? Are there any mechanisms in place to verify the extracted content against the original papers?
6. How does the model handle the generation of large posters with a lot of content? Are there any limitations on the size or complexity of the generated posters?
7. How does the model compare to other existing methods for scientific poster generation? Are there any benchmarks or comparisons available?
8. How does the model handle the generation of posters for different types of scientific conferences or journals? Are there any differences in the generated posters for different venues?

### Rating

6

### Confidence

4

**********
