### Summary

This paper introduces a new task, layout-aware scientific poster generation (LayoutSciPG), which aims to generate flexible scientific posters from academic papers through integrated automatic content extraction and layout design. To achieve this, the authors first created a large-scale dataset containing over 10,000 pairs of scientific papers and their corresponding posters. Then, they propose a multimodal extractor-generator framework that employs a multimodal extractor to retrieve key text and image elements from the papers and designs an interactive generator with an adaptive memory mechanism to seamlessly paraphrase the extracted content and generate a structured layout.

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

1. The paper mentions that the generated poster is relatively simple, and the layout aesthetics score is low. This may be due to the limited diversity of the dataset or the model's inability to capture complex layout patterns.
2. The paper does not provide a user study to evaluate the usability and user satisfaction of the generated posters.

### Suggestions

The authors should investigate methods to enhance the aesthetic quality of the generated posters. This could involve exploring more sophisticated layout generation techniques, such as incorporating attention mechanisms that allow the model to focus on specific regions of the poster when placing elements. Additionally, the model could benefit from a more diverse training dataset that includes a wider range of layout styles and complexities. This could be achieved by augmenting the existing dataset with synthetic data or by incorporating additional real-world examples. Furthermore, the authors should consider incorporating aesthetic evaluation metrics into the training process to directly optimize for visual appeal. This could involve using a combination of quantitative metrics, such as those based on layout symmetry and balance, and qualitative metrics derived from user feedback. By addressing these points, the authors can significantly improve the visual quality and overall impact of the generated posters.

To address the lack of user evaluation, the authors should conduct a comprehensive user study to assess the usability and user satisfaction of the generated posters. This study should involve participants from the target user group, such as researchers and students, and should evaluate the posters based on criteria such as clarity, readability, and overall effectiveness in communicating scientific information. The study should also compare the generated posters with human-created posters to determine how well the model performs in relation to human expertise. The authors should also consider collecting qualitative feedback from the participants to identify specific areas for improvement. This feedback can provide valuable insights into the strengths and weaknesses of the generated posters and guide future development efforts. The user study should be designed to provide statistically significant results and should be reported in detail to ensure reproducibility.

Finally, the authors should explore methods to allow for more user control over the generated posters. This could involve providing users with options to customize the layout, such as choosing different templates or adjusting the placement of elements. This would allow users to tailor the generated posters to their specific needs and preferences. Additionally, the authors could explore methods to incorporate user feedback into the generation process, allowing users to refine the generated posters iteratively. This would make the generated posters more user-centric and improve their overall usability and effectiveness. By incorporating these suggestions, the authors can create a more practical and user-friendly tool for scientific poster generation.

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
